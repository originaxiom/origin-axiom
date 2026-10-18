"""Strengthen the existing prospective gate without changing its sealed bytes.

The base policy, historical failures and main-acceptance requirement remain.
This wrapper adds independent index/worktree checks around that gate. It never
admits a packet rejected by the base gate and launches no scientific code.
"""
import argparse
import json
from pathlib import Path

try:
    from . import prospective, tracked_state
except ImportError:
    import prospective
    import tracked_state


def evaluate(admission, root=None):
    root = Path(root if root is not None else prospective.gates.ROOT).resolve()
    before = tracked_state.inspect(root)
    if not before["clean"]:
        return {"prospective_admissible": False, "global_compliant": None,
                "packet": None, "errors": ["Strict tracked state is not clean before admission"],
                "tracked_state_before": before,
                "limits": "Preflight rejected before base governance; no scientific execution."}
    report = prospective.evaluate(admission, root=root)
    after = tracked_state.inspect(root, expected_head=before["head_after"])
    report["tracked_state_before"] = before
    report["tracked_state_after"] = after
    if not after["clean"]:
        report["errors"].append("Strict tracked state changed during admission")
        report["prospective_admissible"] = False
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--admission", required=True)
    args = parser.parse_args()
    report = evaluate(args.admission)
    print(json.dumps(report, sort_keys=True, indent=2))
    return 0 if report["prospective_admissible"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
