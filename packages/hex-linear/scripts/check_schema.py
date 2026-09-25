"""Validate every shipped GraphQL document against an explicit provider schema."""
import argparse
import hashlib
import json
from pathlib import Path

from graphql import build_schema, parse, validate
from hex_linear._documents import DOCUMENTS

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("schema", type=Path)
args = parser.parse_args()
raw = args.schema.read_bytes()
schema = build_schema(raw.decode())
results = {name: [str(error) for error in validate(schema, parse(document))]
           for name, document in DOCUMENTS.items()}
# Known-invalid query proves the validation instrument rejects an absent field.
control = validate(schema, parse("query { hexDeliberatelyMissingField }"))
assert control, "schema validator did not reject the negative control"
print(json.dumps({"schema_sha256": hashlib.sha256(raw).hexdigest(),
                  "documents": results, "negative_control_rejected": True}, indent=2))
raise SystemExit(1 if any(results.values()) else 0)
