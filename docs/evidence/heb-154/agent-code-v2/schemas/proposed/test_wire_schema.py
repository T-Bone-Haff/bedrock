"""Advisory schema-authoring tests, not fixture/runtime/agent implementation.

Uses the selected Haffey pytest profile without choosing a service framework.
Lexical and relational helpers below are specimen detectors only, not supplied
production parsers, canonicalizers, approval logic or durable-finality proof.
"""

import copy
import hashlib
import json
from pathlib import Path
import re

import pytest
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SCHEMA_FILES = (
    "frd-wire.schema.json",
    "frd-source-body.schema.json",
    "frd-source-derivation.schema.json",
)
WIRE = "frd-wire.schema.json"
BODY = "frd-source-body.schema.json"
ACTION_NAMES = {
    "order_context.read": "OrderContextRead",
    "source.read": "SourceRead",
    "availability.read": "AvailabilityRead",
    "requirements.clarify": "RequirementsClarify",
    "approval.request": "ApprovalRequest",
    "inventory.reserve": "InventoryReserve",
    "arrangement.record": "ArrangementRecord",
    "operation.reconcile": "OperationReconcile",
    "operation.cancel": "OperationCancel",
}
RESULT_TAGS = {
    "order_context.read": {"context"},
    "source.read": {"source", "unavailable", "denied"},
    "availability.read": {"availability"},
    "requirements.clarify": {"accepted_revision", "unresolved", "unavailable"},
    "approval.request": {"granted", "denied", "unavailable"},
    "inventory.reserve": {"committed", "rejected", "unresolved"},
    "arrangement.record": {"committed", "rejected", "unresolved"},
    "operation.reconcile": {"committed", "closed_not_applied", "unresolved"},
    "operation.cancel": {"accepted", "unsupported"},
}


def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError("duplicate_decoded_key")
        out[key] = value
    return out


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs)


SCHEMAS = {name: read_json(HERE / name) for name in SCHEMA_FILES}
EXAMPLES = read_json(HERE / "wire-schema-examples.json")["examples"]
BY_ID = {item["id"]: item for item in EXAMPLES}


def deny_remote(uri):
    raise NoSuchResource(ref=uri)


def validator(file, definition=None, schemas=None):
    population = SCHEMAS if schemas is None else schemas
    schema = population[file]
    registry = Registry(retrieve=deny_remote).with_resources(
        (value["$id"], Resource.from_contents(value)) for value in population.values()
    )
    selected = schema if definition is None else {"$ref": schema["$id"] + "#/$defs/" + definition}
    return Draft202012Validator(selected, registry=registry)


def example(id):
    return copy.deepcopy(BY_ID[id]["value"])


def objects(value, path=()):
    if isinstance(value, dict):
        yield path, value
        for key, child in value.items():
            yield from objects(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from objects(child, path + (index,))


def at(value, path):
    for part in path:
        value = value[part]
    return value


def sha(raw):
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def scalar_tree(value, depth=0):
    if isinstance(value, str):
        value.encode("utf-8", errors="strict")
    elif isinstance(value, (list, dict)):
        if depth + 1 > 32:
            raise ValueError("container_depth")
        if isinstance(value, list) and len(value) > 256:
            raise ValueError("list_limit")
        children = value if isinstance(value, list) else [*value.keys(), *value.values()]
        for child in children:
            scalar_tree(child, depth + 1)


def strict_object(raw):
    """Specimen-only lexical detector; no HTTP framing/streaming implementation."""
    if len(raw) > 1_048_576:
        raise ValueError("body_too_large")
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("bom")

    def integer(token):
        if re.fullmatch(r"0|[1-9][0-9]*", token) is None:
            raise ValueError("numeric_lexeme")
        value = int(token)
        if value > 9_007_199_254_740_991:
            raise ValueError("numeric_range")
        return value

    def reject_number(token):
        raise ValueError("numeric_lexeme")

    value = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                       parse_int=integer, parse_float=reject_number,
                       parse_constant=reject_number)
    if not isinstance(value, dict):
        raise ValueError("root_object")
    scalar_tree(value)
    return value


def check_source(source, definition):
    """Exact example bytes/body shape/identity only; not publication authority."""
    raw = source["body_utf8"].encode("utf-8")
    if len(raw) > 262_144 or len(raw) != source["body_length_bytes"]:
        raise ValueError("source_length")
    if sha(raw) != source["source_ref"]["content_digest"]:
        raise ValueError("source_digest")
    body = strict_object(raw)
    validator(BODY, definition).validate(body)
    id_fields = {"customer_brief": "record_id", "supplier_notice": "record_id",
                 "quote": "quote_id", "stock": "stock_id", "order": "order_id"}
    ref = source["source_ref"]
    if (body[id_fields[ref["kind"]]], body["revision"]) != (ref["record_id"], ref["revision"]):
        raise ValueError("source_identity")
    return body


def check_reconciled(result, kind):
    raw = result["original_result_utf8"].encode("utf-8")
    if sha(raw) != result["original_result_digest"]:
        raise ValueError("original_result_digest")
    original = strict_object(raw)
    definition = {"inventory.reserve": "CommittedReservation",
                  "arrangement.record": "CommittedArrangement"}[kind]
    validator(WIRE, definition).validate(original)
    if original["effect"]["committed_attempt"]["operation"]["operation_kind"] != kind:
        raise ValueError("original_operation_kind")
    return original


@pytest.mark.parametrize("file", SCHEMA_FILES)
def test_meta_schema(file):
    Draft202012Validator.check_schema(SCHEMAS[file])


@pytest.mark.parametrize("item", EXAMPLES, ids=lambda item: item["id"])
def test_schema_specimens(item):
    errors = list(validator(item["schema_file"], item["definition"]).iter_errors(item["value"]))
    assert (not errors) is item["expected_schema"], [error.message for error in errors]


def test_declared_action_and_variant_inventory():
    assert len(BY_ID) == len(EXAMPLES)
    requests = {item["value"]["action"] for item in EXAMPLES if item["id"].startswith("request:")}
    assert requests == set(ACTION_NAMES)
    for action, name in ACTION_NAMES.items():
        tags = {item["value"]["result"]["tag"] for item in EXAMPLES
                if item["id"].startswith("response:" + action + ":")}
        assert tags == RESULT_TAGS[action]
        assert name + "Response" in SCHEMAS[WIRE]["$defs"]
    dirty = requests - {"operation.cancel"}
    assert dirty != set(ACTION_NAMES)


def check_grammar_fields(text):
    """Full flat record declarations in the companion's code blocks only."""
    blocks = re.findall(r"```text\n(.*?)```", text, re.S)
    records = dict(re.findall(r"^(\w+)\s*=\s*\{([^}]*)\}", "\n".join(blocks), re.M | re.S))
    expected = {"SourceRef", "Request", "Response", "Terms", "Plan", "Grant", "Source",
                "Publication", "ObservationScope", "Mutation", "OperationIdentity", "AttemptIdentity",
                "Reservation", "Arrangement", "CommittedReservation", "CommittedArrangement",
                "ReconciledCommit", "Closure", "Rejected"}
    if set(records) != expected:
        raise ValueError("grammar_record_inventory")
    for name, content in records.items():
        fields = re.findall(r"\b(\w+)(\?)?:", content)
        declared = {field for field, optional in fields}
        required = {field for field, optional in fields if not optional}
        if name == "Request":
            targets = [SCHEMAS[WIRE]["$defs"][n + "Request"] for n in ACTION_NAMES.values()]
        elif name == "Response":
            targets = [SCHEMAS[WIRE]["$defs"][n + "Response"]["oneOf"][0] for n in ACTION_NAMES.values()]
        else:
            targets = [SCHEMAS[WIRE]["$defs"][name]]
        for target in targets:
            if set(target["properties"]) != declared or set(target["required"]) != required:
                raise ValueError("grammar_fields:" + name)


def test_grammar_to_schema_fields_and_identity_vectors():
    text = (ROOT / "wire-and-identity-contract.md").read_text()
    check_grammar_fields(text)
    with pytest.raises(ValueError, match="grammar_fields:Terms"):
        check_grammar_fields(text.replace("Terms = {quote_ref:", "Terms = {missing_control:"))
    vectors = read_json(ROOT / "scenarios/proposed/wire-identity-examples.json")["semantic_vectors"]
    for vector in vectors:
        definition = {"plan": "PlanIdentityValue", "grant": "GrantIdentityValue"}.get(vector["id"], "EffectIdentityValue")
        validator(WIRE, definition).validate(vector["value"])
        dirty = {**vector["value"], "physical_request_id": "REQUEST-CONTROL"}
        assert not validator(WIRE, definition).is_valid(dirty)


@pytest.mark.parametrize("item", [x for x in EXAMPLES if x["expected_schema"]], ids=lambda x: x["id"])
def test_closed_records_and_required_fields(item):
    valid = validator(item["schema_file"], item["definition"])
    for path, record in objects(item["value"]):
        changed = copy.deepcopy(item["value"])
        at(changed, path)["unexpected_control"] = True
        assert not valid.is_valid(changed), (item["id"], path, "unknown_field")
        for key in record:
            changed = copy.deepcopy(item["value"])
            del at(changed, path)[key]
            assert not valid.is_valid(changed), (item["id"], path, key)


def test_action_correlation_and_optional_replay_permit():
    for action, name in ACTION_NAMES.items():
        request = example("request:" + action)
        assert validator(WIRE).is_valid(request)
        for other, other_name in ACTION_NAMES.items():
            assert validator(WIRE, other_name + "Request").is_valid(request) is (action == other)
    reserve = example("request:inventory.reserve")
    reserve["payload"]["replay_permit_id"] = "PERMIT-A"
    assert validator(WIRE).is_valid(reserve)
    reserve["payload"]["replay_permit_id"] = None
    assert not validator(WIRE).is_valid(reserve)
    result = example("response:inventory.reserve:committed")
    assert not validator(WIRE, "ArrangementRecordResponse").is_valid(result)
    result["result"]["effect"]["committed_attempt"]["operation"]["operation_kind"] = "arrangement.record"
    assert not validator(WIRE, "InventoryReserveResponse").is_valid(result)


def test_weakened_schema_controls():
    request = example("request:inventory.reserve")
    request["unexpected_control"] = True
    assert not validator(WIRE).is_valid(request)
    weak = copy.deepcopy(SCHEMAS)
    weak[WIRE]["$defs"]["InventoryReserveRequest"]["additionalProperties"] = True
    assert validator(WIRE, schemas=weak).is_valid(request)
    rejection = example("invalid:rejected-without-closure")
    assert not validator(WIRE, "InventoryReserveResponse").is_valid(rejection)
    weak = copy.deepcopy(SCHEMAS)
    weak[WIRE]["$defs"]["Rejected"]["required"].remove("closure")
    assert validator(WIRE, "InventoryReserveResponse", weak).is_valid(rejection)


def test_reference_resolution_is_local_and_discriminating():
    request = example("request:inventory.reserve")
    assert validator(WIRE).is_valid(request)
    with pytest.raises(NoSuchResource):
        deny_remote("https://example.invalid/unbound-schema")
    # Regression for the observed legacy resolver failure on nested URN fragments.
    response = example("response:order_context.read:context")
    valid = validator(WIRE, "OrderContextReadResponse")
    assert valid.is_valid(response)
    assert not valid.is_valid({**response, "unexpected_control": True})


def test_complete_initial_source_population():
    pack = read_json(ROOT / "scenarios/proposed/scenario-pack.json")
    mapping = {"orders": "OrderInitial", "briefs": "CustomerBriefPack",
               "inventory": "Stock", "quotes": "Quote", "supplier_notices": "SupplierNoticeProposed"}
    for world in pack["worlds"]:
        for key, definition in mapping.items():
            for record in world["initial_state"][key]:
                valid = validator(BODY, definition)
                valid.validate(record)
                dirty = {**record, "oracle_answer": True}
                assert not valid.is_valid(dirty)
    ref = read_json(ROOT / "scenarios/proposed/frd-01.json")["actor_visible"]
    for key, definition in [("order", "OrderInitial"), ("accepted_customer_brief", "CustomerBriefReference")]:
        validator(BODY, definition).validate(ref[key])
    for key, definition in [("inventory", "Stock"), ("transport_quotes", "Quote")]:
        for record in ref[key]:
            validator(BODY, definition).validate(record)
    # Missing order_id is valid only for the actual reference artifact's shape.
    assert not validator(BODY, "CustomerBriefPack").is_valid(ref["accepted_customer_brief"])


@pytest.mark.parametrize("raw", [
    b'{"q":1,"q":2}', b'{"q":1,"\\u0071":2}', b'{"q":2.0}',
    b'{"q":2e0}', b'{"q":-0}', b'{"q":NaN}', b'{"q":Infinity}',
    b'{"q":9007199254740992}', b'{"q":"\\ud800"}', b'{"q":"\xff"}',
    b'\xef\xbb\xbf{}', b'{}{}', b'[]', b'{"q":'+b'['*32+b'0'+b']'*32+b'}',
    b'{"q":['+b'0,'*256+b'0]}', b'{"q":"'+b'a'*1_048_576+b'"}',
])
def test_lexical_known_dirty(raw):
    assert strict_object(b' {"q":2}\n') == {"q": 2}
    with pytest.raises((ValueError, UnicodeError)):
        strict_object(raw)


def test_schema_alone_is_not_a_lexical_or_byte_guard():
    request = example("request:inventory.reserve")
    request["payload"]["terms"]["quantity"] = 2.0
    assert validator(WIRE).is_valid(request)
    with pytest.raises(ValueError, match="numeric_lexeme"):
        strict_object(json.dumps(request).encode())
    request = example("request:requirements.clarify")
    request["payload"]["question"] = "é" * 2049
    assert validator(WIRE).is_valid(request)
    assert len(request["payload"]["question"].encode()) > 4096
    assert len(("é" * 2048).encode()) == 4096
    assert validator(WIRE, "Id").is_valid("A" * 128)
    assert not validator(WIRE, "Id").is_valid("A" * 129)
    assert validator(WIRE, "UInt").is_valid(9_007_199_254_740_991)
    assert not validator(WIRE, "UInt").is_valid(9_007_199_254_740_992)


def test_source_and_original_result_bytes():
    source = example("response:source.read:source")["result"]["source"]
    check_source(source, "CustomerBriefPack")
    changed = copy.deepcopy(source)
    changed["body_utf8"] += "\n"
    with pytest.raises(ValueError, match="source_length"):
        check_source(changed, "CustomerBriefPack")
    changed["body_length_bytes"] += 1
    with pytest.raises(ValueError, match="source_digest"):
        check_source(changed, "CustomerBriefPack")
    result = example("response:operation.reconcile:committed")["result"]
    check_reconciled(result, "inventory.reserve")
    changed = copy.deepcopy(result)
    changed["original_result_utf8"] += " "
    with pytest.raises(ValueError, match="original_result_digest"):
        check_reconciled(changed, "inventory.reserve")
    # A checksum-valid rejected object still cannot be a reconciled commitment.
    changed["original_result_utf8"] = json.dumps(example("response:inventory.reserve:rejected")["result"])
    changed["original_result_digest"] = sha(changed["original_result_utf8"].encode())
    assert validator(WIRE, "ReconciledCommit").is_valid(changed)
    from jsonschema.exceptions import ValidationError
    with pytest.raises(ValidationError):
        check_reconciled(changed, "inventory.reserve")


def test_derivation_pointer_and_original_record_equality():
    entry = example("derivation:existing-brief")
    artifact = ROOT / entry["input_artifact"]["path"]
    assert sha(artifact.read_bytes()) == entry["input_artifact"]["sha256"]
    actual = read_json(artifact)
    for segment in entry["json_pointer"].split("/")[1:]:
        segment = segment.replace("~1", "/").replace("~0", "~")
        actual = actual[int(segment)] if isinstance(actual, list) else actual[segment]
    derived = check_source(entry["source"], entry["source_body_definition"])
    assert actual == derived
    changed = {**derived, "message": "An incomplete replacement."}
    assert actual != changed


def test_event_origin_candidate_structure():
    entry = example("derivation:existing-brief")
    valid = validator("frd-source-derivation.schema.json")
    assert valid.is_valid(entry)
    entry["event_origin"] = {
        "specification_artifact": entry["input_artifact"],
        "case_id": "FRD-02A", "event_json_pointer": "/cases/3/event_schedule/0",
    }
    assert valid.is_valid(entry)  # Shape only, not a provenance assertion.
    del entry["event_origin"]["case_id"]
    assert not valid.is_valid(entry)
    entry = example("derivation:existing-brief")
    entry["input_artifact"]["path"] += "\n"
    assert not valid.is_valid(entry)


def check_bindings(bindings):
    expected = set(SCHEMA_FILES) | {"wire-schema-examples.json", "test_wire_schema.py",
                                    "requirements-authoring.txt", "README.md"}
    if set(bindings["artifact_sha256"]) != expected:
        raise ValueError("artifact_inventory")
    for name, digest in bindings["artifact_sha256"].items():
        if sha((HERE / name).read_bytes()) != digest:
            raise ValueError("artifact_identity")
    if set(bindings["actions"]) != set(ACTION_NAMES):
        raise ValueError("action_binding_inventory")
    for action, name in ACTION_NAMES.items():
        for part in ["Request", "Response", "Payload", "Result"]:
            if bindings["actions"][action][part.lower()] != "#/$defs/" + name + part:
                raise ValueError("action_binding_reference")
    if sha((ROOT / "wire-and-identity-contract.md").read_bytes()) != bindings["wire_design_sha256"]:
        raise ValueError("wire_design_identity")


def test_bound_artifacts_and_entries():
    bindings = read_json(HERE / "wire-schema-bindings.json")
    check_bindings(bindings)
    dirty = copy.deepcopy(bindings)
    dirty["artifact_sha256"][WIRE] = "sha256:" + "0" * 64
    with pytest.raises(ValueError, match="artifact_identity"):
        check_bindings(dirty)
    dirty = copy.deepcopy(bindings)
    del dirty["actions"]["operation.cancel"]
    with pytest.raises(ValueError, match="action_binding_inventory"):
        check_bindings(dirty)


def test_independent_completeness_specimen():
    """Synthetic catalog comparison, not a real service/snapshot boundary test."""
    first = example("response:source.read:source")["result"]["source"]
    second = copy.deepcopy(first)
    body = json.loads(second["body_utf8"])
    body["record_id"] = "BRIEF-A-CONFLICT"
    body["message"] = "Use Site B; this conflicts with the equally current brief."
    second["body_utf8"] = json.dumps(body, separators=(",", ":"))
    second["body_length_bytes"] = len(second["body_utf8"].encode())
    second["source_ref"].update(record_id=body["record_id"], content_digest=sha(second["body_utf8"].encode()))
    for source in [first, second]:
        check_source(source, "CustomerBriefPack")
    expected_catalog = [first["source_ref"], second["source_ref"]]

    def complete(sources, member_refs):
        refs = [source["source_ref"] for source in sources]
        key = lambda ref: (ref["kind"], ref["record_id"], ref["revision"], ref["content_digest"])
        if sorted(refs, key=key) != sorted(member_refs, key=key):
            raise ValueError("self_membership")
        if sorted(refs, key=key) != sorted(expected_catalog, key=key):
            raise ValueError("independent_catalog_omission")

    complete([first, second], expected_catalog)
    # All remaining hashes and the shortened membership list still agree.
    with pytest.raises(ValueError, match="independent_catalog_omission"):
        complete([first], [first["source_ref"]])
