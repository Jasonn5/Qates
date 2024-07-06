from __future__ import annotations
import json
from pathlib import Path

BASE = Path(__file__).absolute().parent.parent

def resources_credential_path(path):
    return BASE / "resources" / "credentials" / path

def load_credential_resource(filename):
    with resources_credential_path(filename).open() as f:
        return json.load(f)

