from datetime import datetime
from pathlib import Path
import json

def init_audit(path="nitt_audit.json"):
    if not Path(path).exists():
        Path(path).write_text(json.dumps({"events": []}, indent=2))

def log_event(kind, **data):
    path = Path("nitt_audit.json")
    if not path.exists():
        init_audit(path)
    obj = json.loads(path.read_text())
    obj["events"].append({"ts": datetime.utcnow().isoformat() + "Z", "kind": kind, **data})
    path.write_text(json.dumps(obj, indent=2))
