"""Authoring-only integrity checks. Does not run agents, events, or runtime oracles."""

import copy
import hashlib
import json
from pathlib import Path
import re
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate_json_key")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(), object_pairs_hook=unique_object)


def ids(rows, key, label):
    values = [row[key] for row in rows]
    require(len(values) == len(set(values)), "duplicate_" + label)
    return set(values)


def world_digest(state):
    encoded = json.dumps(state, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def feasible(world, order_id, now=0):
    """Initial fixture arithmetic, not a validator for emitted agent plans."""
    req = world["evaluator_requirements"][order_id]
    fields = ("sku", "quantity", "substitutions_allowed", "destination",
              "arrival_time_max_inclusive", "extra_transport_cost_minor_max_inclusive",
              "currency", "single_source_required")
    if any(req.get(key) is None for key in fields):
        return []
    allowed = {req["sku"]}
    if req["substitutions_allowed"]:
        allowed.update(req.get("allowed_substitute_skus", []))
    state = world["initial_state"]
    stock = {(row["site"], row["sku"]): row["available"] for row in state["inventory"]}
    return sorted(q["quote_id"] for q in state["quotes"] if (
        q["sku"] in allowed and q["quantity"] == req["quantity"]
        and q["destination"] == req["destination"]
        and stock.get((q["site"], q["sku"]), 0) >= req["quantity"]
        and now < q["expires_at"]
        and q["estimated_arrival_time"] <= req["arrival_time_max_inclusive"]
        and q["currency"] == req["currency"]
        and q["extra_transport_cost_minor"] <= req["extra_transport_cost_minor_max_inclusive"]
    ))


def normalized_reference(reference):
    a = reference["actor_visible"]
    return {
        "orders": [a["order"]],
        "briefs": [{**a["accepted_customer_brief"], "order_id": "ORDER-A"}],
        "inventory": a["inventory"], "quotes": a["transport_quotes"],
        "supplier_notices": [],
        "reservations": a["initial_reservations"],
        "arrangements": a["initial_recovery_arrangements"],
        "customer_drafts": a["initial_communication_drafts"],
        "operator_summaries": a["initial_operator_summaries"],
        "effect_log": a["initial_effect_log"],
        "outbound_messages": a["initial_outbound_messages"],
        "payments": a["initial_payments"],
    }


def check_links(guide):
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", guide):
        if target.startswith(("https://", "http://", "#")):
            continue
        path = target.split("#", 1)[0]
        require((ROOT / path).exists(), "missing_guide_link")


def check(pack, reference, guide, design):
    require(pack["status"] == "proposed-not-frozen", "unexpected_freeze_claim")
    world_ids = ids(pack["worlds"], "world_id", "world")
    case_ids = ids(pack["cases"], "case_id", "case")
    oracle_ids = ids(pack["oracles"], "oracle_id", "oracle")
    ids(pack["controls"], "control_id", "control")
    guide_cases = re.findall(r"^\| (FRD-\d{2}[A-Z]) \|", guide, re.M)
    require(len(guide_cases) == len(set(guide_cases)), "duplicate_guide_case")
    require(case_ids == set(guide_cases), "case_guide_membership")
    required_families = set(re.findall(r"^\| (FRD-\d{2}) —", design, re.M))
    require(bool(required_families), "family_source_empty")
    require({c["family_id"] for c in pack["cases"]} == required_families,
            "family_coverage")
    require(set(pack["common"]["universal_oracles"]) <= oracle_ids, "unknown_universal_oracle")
    for c in pack["cases"]:
        require(c["world_id"] in world_ids, "unknown_world")
        require(c["case_id"].startswith(c["family_id"]), "case_family_mismatch")
        require(c["paired_case_ids"] and set(c["paired_case_ids"]) <= case_ids
                and c["case_id"] not in c["paired_case_ids"], "invalid_pair")
        require(set(c["oracle_ids"]) <= oracle_ids and c["oracle_ids"], "unknown_oracle")
        require(c["status"] == "proposed-not-frozen", "case_freeze_claim")
        require(set(c["expected"]["roles"]) == {"investigator", "planner", "correspondent"},
                "role_expectation_missing")
        require(c["expected"]["required_claims"] and c["expected"]["state_predicates"],
                "expected_outcome_missing")
        world = next(w for w in pack["worlds"] if w["world_id"] == c["world_id"])
        require(c["initial_world_sha256"] == world["initial_world_sha256"], "case_world_digest")
        require(set(c["expected"]["outcomes"]) == {o["order_id"] for o in world["initial_state"]["orders"]},
                "expected_order_population")
        minutes = [e["at"] for e in c["event_schedule"]]
        require(all(type(t) is int and t >= 0 for t in minutes) and minutes == sorted(minutes),
                "event_clock_order")
    require({c["world_id"] for c in pack["cases"]} == world_ids, "unused_world")
    for world in pack["worlds"]:
        state = world["initial_state"]
        require(world_digest(state) == world["initial_world_sha256"], "world_digest_mismatch")
        orders = ids(state["orders"], "order_id", "order")
        require(orders == set(world["evaluator_requirements"]) == set(world["initial_eligible_quotes"]),
                "world_order_population")
        require(orders == {b["order_id"] for b in state["briefs"]}, "brief_order_population")
        ids(state["briefs"], "record_id", "brief")
        ids(state["inventory"], "stock_id", "stock")
        ids(state["quotes"], "quote_id", "quote")
        balances = [(s["site"], s["sku"]) for s in state["inventory"]]
        require(len(balances) == len(set(balances)), "duplicate_stock_balance")
        require(all(type(s["available"]) is int and s["available"] >= 0 for s in state["inventory"]),
                "invalid_initial_stock")
        for order in state["orders"]:
            oid = order["order_id"]
            require(type(order["quantity"]) is int and order["quantity"] > 0
                    and order["quantity"] == world["evaluator_requirements"][oid]["quantity"],
                    "quantity_disagreement")
            require(feasible(world, oid) == sorted(world["initial_eligible_quotes"][oid]),
                    "initial_feasibility_disagreement")
        require(all(not state[key] for key in ("reservations", "arrangements", "customer_drafts",
                    "operator_summaries", "effect_log", "outbound_messages", "payments")),
                "initial_effects_not_empty")
    ordinary = next(w for w in pack["worlds"] if w["world_id"] == "ordinary")
    require(ordinary["initial_state"] == normalized_reference(reference), "baseline_parity")
    require(ordinary["evaluator_requirements"]["ORDER-A"] == reference["evaluator_only"]["derived_customer_requirements"],
            "baseline_requirements_parity")
    covered = set()
    for control in pack["controls"]:
        require(control["oracle_id"] in oracle_ids, "control_unknown_oracle")
        require(control["clean_specimen"] and control["dirty_specimen"] and control["expected_reason"],
                "unpaired_control")
        covered.add(control["oracle_id"])
    require(covered == oracle_ids, "oracle_without_control")
    check_links(guide)


def main():
    pack_path = HERE / "scenario-pack.json"
    baseline_path = HERE / "frd-01.json"
    guide_path = ROOT / "scenario-and-oracle-pack.md"
    design_path = ROOT / "consumer-proving-design.md"
    pack, reference = read_json(pack_path), read_json(baseline_path)
    guide, design = guide_path.read_text(), design_path.read_text()
    require(hashlib.sha256(baseline_path.read_bytes()).hexdigest() == pack["baseline_source"]["sha256"],
            "baseline_digest_mismatch")
    check(pack, reference, guide, design)
    document_paths = sorted(ROOT.glob("*.md"))
    for document_path in document_paths:
        check_links(document_path.read_text())
    caught = []

    def dirty(name, mutation, reason):
        changed = copy.deepcopy(pack)
        mutation(changed)
        try:
            check(changed, reference, guide, design)
        except ValueError as exc:
            require(str(exc) == reason, "wrong_dirty_control_reason:" + name + ":" + str(exc))
            caught.append(name)
        else:
            raise ValueError("undetected_dirty_control:" + name)

    dirty("missing_case", lambda p: p["cases"].pop(), "case_guide_membership")
    dirty("duplicate_case", lambda p: p["cases"].append(copy.deepcopy(p["cases"][0])), "duplicate_case")
    dirty("unknown_world", lambda p: p["cases"][0].update(world_id="absent-world"), "unknown_world")
    dirty("unknown_pair", lambda p: p["cases"][0].update(paired_case_ids=["FRD-99Z"]), "invalid_pair")
    dirty("wrong_feasible_set", lambda p: p["worlds"][0]["initial_eligible_quotes"]["ORDER-A"].pop(),
          "initial_feasibility_disagreement")
    dirty("unpaired_oracle", lambda p: p.update(controls=[c for c in p["controls"] if c["oracle_id"] != "O-ACCESS"]),
          "oracle_without_control")
    dirty("world_bytes_drift", lambda p: p["worlds"][0]["initial_state"]["briefs"][0].update(message="Changed brief"),
          "world_digest_mismatch")
    def change_baseline_and_rehash(p):
        world = p["worlds"][0]
        world["initial_state"]["briefs"][0]["message"] = "Changed brief"
        world["initial_world_sha256"] = world_digest(world["initial_state"])
        for case in p["cases"]:
            if case["world_id"] == world["world_id"]:
                case["initial_world_sha256"] = world["initial_world_sha256"]
    dirty("baseline_drift_with_fresh_digest", change_baseline_and_rehash, "baseline_parity")
    dirty("case_world_digest", lambda p: p["cases"][0].update(initial_world_sha256="0" * 64),
          "case_world_digest")
    try:
        check_links(guide + "\n[dirty](missing-frd-authoring-control.invalid)\n")
    except ValueError as exc:
        require(str(exc) == "missing_guide_link", "wrong_link_control_reason")
        caught.append("missing_local_link")
    else:
        raise ValueError("undetected_missing_link")
    try:
        json.loads('{"case_id":1,"case_id":2}', object_pairs_hook=unique_object)
    except ValueError as exc:
        require(str(exc) == "duplicate_json_key", "wrong_json_control_reason")
        caught.append("duplicate_json_key")
    else:
        raise ValueError("undetected_duplicate_key")
    cost_world = next(w for w in pack["worlds"] if w["world_id"] == "cost-at-cap")
    require(feasible(cost_world, "ORDER-A", 29) == ["Q-EAST", "Q-WEST"], "inclusive_boundary_error")
    require(feasible(cost_world, "ORDER-A", 30) == [], "expiry_boundary_error")
    paths = [pack_path, baseline_path, *document_paths, Path(__file__).resolve()]
    report = {
        "instrument": "frd-pack-authoring-check/draft-1",
        "scope": "Complete local public draft registry, initial-state arithmetic and local links in all root Markdown documents; no agents, event execution, runtime or semantic oracle calibration, hidden cases, provider calls or adoption evidence.",
        "result": "authoring_checks_passed",
        "python": sys.version.split()[0],
        "interpreter": sys.executable,
        "case_ids": [c["case_id"] for c in pack["cases"]],
        "family_ids": sorted({c["family_id"] for c in pack["cases"]}),
        "world_ids": [w["world_id"] for w in pack["worlds"]],
        "initial_world_sha256": {w["world_id"]: w["initial_world_sha256"] for w in pack["worlds"]},
        "oracle_specifications": [o["oracle_id"] for o in pack["oracles"]],
        "unexecuted_oracle_control_specifications": [c["control_id"] for c in pack["controls"]],
        "authoring_dirty_controls_detected": caught,
        "initial_boundary_checks": ["cost and arrival equality accepted", "expiry equality rejected"],
        "input_sha256": {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
