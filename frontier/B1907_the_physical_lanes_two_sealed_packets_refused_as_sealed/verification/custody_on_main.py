#!/usr/bin/env python3
"""P-746: custody of the two sealed packets, by main.  The specification is read raw by this script and nothing of it
is printed but paths and counts: for every pinned sha256 (the design, the environment where pinned, every artifact),
the hash of the blob at the sealed commit and at the lane's head, in full."""
import subprocess, json, hashlib, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
HEAD = "1aa76251ff9cf1f60c08a2b3c83323ae8f069f97"   # the lane's head when main read it (a commit, never the moving branch)
PK = {"packet 1": ("bda89f04a94d09217551cef96056f375b21c260b", "reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_transport_joint_2026_11_05/SPECIFICATION.json", "f5390767ebc04f68ee5ce0f1a5e854a9dcdea131586ae1812557fd3f9c3a4238"),
      "packet 2": ("d1a33e921d5cb16e4606b196fa970b91a2abfb6d", "reports/physical_bridge_2026_09_05/foundation_selection_2026_11_07/verification_gauge_response_2026_11_08/SPECIFICATION.json", None)}
def blob(rev, path):
    r = subprocess.run(["git", "cat-file", "blob", "%s:%s" % (rev, path)], capture_output=True)
    return hashlib.sha256(r.stdout).hexdigest() if r.returncode == 0 else None
def custody(pk=PK, head=HEAD, quiet=False):
    """for each packet: its pins, and how many hash to the pinned sha256 at the sealed commit and at the lane's head"""
    out = {}
    for name, (rev, spec, spec_hash) in pk.items():
        h = blob(rev, spec); S = json.loads(subprocess.run(["git", "show", "%s:%s" % (rev, spec)], capture_output=True, text=True).stdout)
        pins = []
        def walk(o):
            if isinstance(o, dict):
                if isinstance(o.get("path"), str) and isinstance(o.get("sha256"), str): pins.append((o["path"], o["sha256"]))
                for v in o.values(): walk(v)
            elif isinstance(o, list):
                for v in o: walk(v)
        walk(S); pins = sorted(set(pins))
        at_seal = sum(1 for p, s in pins if blob(rev, p) == s); at_head = sum(1 for p, s in pins if blob(head, p) == s)
        bad = [p for p, s in pins if blob(rev, p) != s]
        out[name] = {"sealed commit": rev, "the specification's own sha256": h, "equal to the hash in the lane's request": (h == spec_hash) if spec_hash else "not compared (the request's hash is partly masked)",
                     "pins": len(pins), "equal at the sealed commit": at_seal, "equal at the lane's head": at_head, "the lane's head": head[:9], "not equal at the seal": bad,
                     "experiment": S.get("experiment_id"), "methods named in commands or outputs": None}
        if not quiet: print(name, json.dumps(out[name]))
    return out

if __name__ == "__main__":
    json.dump(custody(), open(HERE / "custody_on_main.json", "w"), indent=1)
