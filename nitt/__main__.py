import argparse
from .ci import CIInputs, ci_exponential, ci_from_overlap
from .disclose import disclosure
from .audit import init_audit, log_event
import json as _json

def main():
    p = argparse.ArgumentParser(prog="nitt", description="NITT v1.0 playground tools")
    sub = p.add_subparsers(dest="cmd", required=True)

    s1 = sub.add_parser("ci", help="Compute CI proxy")
    s1.add_argument("--dI", type=float, default=0.0)
    s1.add_argument("--dE", type=float, default=0.0)
    s1.add_argument("--dt", type=float, default=0.0)
    s1.add_argument("--alpha", type=float, default=1e-6)
    s1.add_argument("--wI", type=float, default=1.0)
    s1.add_argument("--wE", type=float, default=1.0)
    s1.add_argument("--wT", type=float, default=1.0)

    s2 = sub.add_parser("overlap", help="CI from state overlap (0..1)")
    s2.add_argument("--fraction", type=float, required=True)

    s3 = sub.add_parser("disclose", help="Print mandatory disclosure")
    s3.add_argument("--ci", type=float)

    s4 = sub.add_parser("audit-init", help="Create audit log file")
    s5 = sub.add_parser("audit-log", help="Append an event to audit log")
    s5.add_argument("--kind", required=True)
    s5.add_argument("--data", default="{}", help='JSON string with extra fields')

    args = p.parse_args()

    if args.cmd == "ci":
        ci = ci_exponential(CIInputs(args.dI, args.dE, args.dt, (args.wI,args.wE,args.wT), args.alpha))
        print(f"CI ≈ {ci:.6f}")
    elif args.cmd == "overlap":
        print(f"CI ≈ {ci_from_overlap(args.fraction):.6f}")
    elif args.cmd == "disclose":
        print(disclosure(args.ci))
    elif args.cmd == "audit-init":
        init_audit(); print("Initialized nitt_audit.json")
    elif args.cmd == "audit-log":
        log_event(args.kind, **_json.loads(args.data)); print("Event logged")
