from __future__ import annotations
import json
from pathlib import Path

BASE = Path(__file__).absolute().parent.parent

def resources_credential_path(path):
    return BASE / "resources" / "credentials" / path

def load_credential_resource(filename):
    with resources_credential_path(filename).open() as f:
        return json.load(f)

class PayloadPaths:
    EMAIL_DRAFT_SUCCESS = BASE / 'payloads' / 'mail_draft' / 'payload_email_draft_success.json'
    EMAIL_DRAFT_INVALID_EMAIL_FORMAT = BASE / 'payloads' / 'mail_draft' / 'payload_email_draft_invalid_email_format.json'

def load_payload(filepath):
    with filepath.open() as file:
        return json.load(file)
