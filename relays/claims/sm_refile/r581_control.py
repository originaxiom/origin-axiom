#!/usr/bin/env python3
"""Failing control for P-581 (decisive wrapper: r581_decisive.py, beside this file).

It runs the same check on an input made wrong on purpose. In a temporary copy of the sealed folder, every relator of
the frozen presentations r581_presentations.json has its first letter inverted (a <-> A); nothing else changes. These
are no longer the census manifolds' groups. The sealed run.py runs on them unchanged, and its own plants still pass
(they test the counter, not the input). The check is the claim's per-object control: the 2T class counts must agree
with main's B993 output on all 400 manifolds it covers, and the root m004 must have exactly 2 classes. On the wrong
input the check must reject: fewer than 400 agree, or m004 is not 2.

    python3 relays/claims/sm_refile/r581_control.py

Exit 1, last line "CONTROL FAILS:", when the check rejects the planted input (the expected outcome); 0, "CONTROL DID
NOT FAIL:", when it accepts it; 3, "CONTROL INVALID:", when anything crashes. Nothing is written into the repository.
"""
import sys


def main():
    sys.dont_write_bytecode = True
    import json
    import pathlib
    import re
    import tempfile
    from r581_decisive import find_root, run_sealed
    root = find_root()
    if root is None:
        return 3, "CONTROL INVALID: the repository root was not found"
    sealed = root / "relays" / "sm_r581" / "r581_presentations.json"
    data = json.loads(sealed.read_text(encoding="utf-8"))
    flip = lambda w: (w[0].swapcase() + w[1:]) if w else w
    changed = 0
    for r in data["rows"]:
        new = [flip(w) for w in r["rels"]]
        changed += sum(1 for a, b in zip(new, r["rels"]) if a != b)
        r["rels"] = new
    if changed == 0:
        return 3, "CONTROL INVALID: the planted change did not apply"
    with tempfile.TemporaryDirectory() as tmp:
        planted = pathlib.Path(tmp) / "planted.json"
        planted.write_text(json.dumps(data), encoding="utf-8")
        rc, so, se, txt = run_sealed(root, presentations_name=str(planted), tmp=tmp)
    if rc != 0 or txt is None:
        return 3, "CONTROL INVALID: the planted run did not complete (exit %d)" % rc
    m_agree = re.search(r"control B993 per object: (\d+) of (\d+) agree", txt)
    m_root = re.search(r"root m004: (.+)", txt)
    if not (m_agree and m_root):
        return 3, "CONTROL INVALID: the check's values did not come out"
    agree, of = int(m_agree.group(1)), int(m_agree.group(2))
    root_2t = json.loads(m_root.group(1))["2T"]
    print("CONTROL: %d relators changed; B993 per-object agreement %d of %d; m004 2T classes %d"
          % (changed, agree, of, root_2t))
    if agree < of or root_2t != 2:
        return 1, ("CONTROL FAILS: on the planted presentations the per-object check rejects (%d of %d agree)"
                   % (agree, of))
    return 0, "CONTROL DID NOT FAIL: the check accepted presentations that are not the census groups"


if __name__ == "__main__":
    try:
        code, last = main()
    except BaseException as e:                                   # no traceback may escape
        code, last = 3, "CONTROL INVALID: the control raised %s" % type(e).__name__
    print(last)
    sys.stdout.flush()
    sys.exit(code)
