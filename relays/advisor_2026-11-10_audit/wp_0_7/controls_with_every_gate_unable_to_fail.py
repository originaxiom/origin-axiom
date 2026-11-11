#!/usr/bin/env python3
"""A read-out for WP-0.7's planted case PV16: does a gate's control turn ITS gate red?

The controls gate (series 3, patch 6) reads a control and does not run it.  What reading cannot show is that the control
depends on its gate's answer.  This shows it by a run: in a scratch worktree of a commit, every gate is made unable to fail
(each gate function, and each entry of GATES, returns a pass), and the registered controls are run there.

  a control that FAILS there        depends on its gate's answer: with the gate unable to fail, the control notices
  a control that still PASSES there does not: it drives the checker beside the gate, or asserts something else

It changes nothing in the repository it is given: the worktree is made outside it and removed.

EXPECTATIONS, written before the first run (2026-11-11), from reading the 53 controls and not from running them:
  E1  the instrument is valid: with no gate changed, every control passes in the worktree (the control run);
  E2  at least 13 controls still pass with every gate unable to fail: the 13 whose body never names its gate's function
      (carry-age, doc-currency, doc-facts, genesis-cited, harvest-debt, lead-debt, point-debt, pretense-phrases,
      relay-debt, retraction-sweep, review-core, seal-provenance, seen-first);
  E3  at least 20 controls fail there, as a control should;
  E4  some of the 40 that do name their gate still pass, because they name it only to assert `GATES[x] is gate_x`.
      How many, this seat does not know: read-out.

Usage:  controls_with_every_gate_unable_to_fail.py --repo CLONE --ref REF --work DIR      (DIR outside the clone)
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys

STUB = '''

# ---- appended by the read-out: every gate made unable to fail ----
def _made_unable_to_fail(*_a, **_k):
    return True, "ok (made unable to fail)"


for _n in list(GATES):
    GATES[_n] = _made_unable_to_fail
for _n in [n for n in list(globals()) if n.startswith("gate_") and callable(globals()[n])]:
    globals()[_n] = _made_unable_to_fail

'''


def run(cmd, cwd=None, timeout=1800):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)


def outcomes(wt, refs):
    """each node id -> PASSED / FAILED / SKIPPED / ERROR, from one pytest run in the worktree"""
    r = run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-p", "no:randomly", "-rA", "--tb=no", *refs], cwd=wt)
    out = {}
    for line in r.stdout.splitlines():
        m = re.match(r"^(PASSED|FAILED|SKIPPED|ERROR|XFAIL|XPASS)\s+(\S+)", line)
        if m:
            out[m.group(2).split(" ")[0]] = m.group(1)
    return out, r.stdout[-400:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--work", required=True)
    a = ap.parse_args()
    repo, wt = os.path.abspath(a.repo), os.path.abspath(a.work)
    assert not wt.startswith(repo + os.sep), "the work folder must be outside the clone"
    if os.path.exists(wt):
        run(["git", "-C", repo, "worktree", "remove", "--force", wt])
        shutil.rmtree(wt, ignore_errors=True)
    head = run(["git", "-C", repo, "rev-parse", "--short=9", a.ref]).stdout.strip()
    r = run(["git", "-C", repo, "worktree", "add", "--detach", wt, a.ref])
    assert r.returncode == 0, r.stderr
    try:
        reg = json.load(open(os.path.join(wt, "tests", "GATE_CONTROLS.json"), encoding="utf-8"))
        refs = sorted(set(reg.values()))
        print(f"commit {head}: {len(reg)} gates, {len(refs)} distinct controls\n")
        base, tail = outcomes(wt, refs)
        not_passing = sorted(g for g, ref in reg.items() if base.get(ref) != "PASSED")
        print(f"E1  the control run, no gate changed: {sum(1 for v in base.values() if v == 'PASSED')} of {len(refs)} controls pass"
              + (f"; NOT passing: {', '.join(not_passing)}" if not_passing else ""))
        gates_py = os.path.join(wt, "scripts", "gates", "gates.py")
        src = open(gates_py, encoding="utf-8").read()
        mark = '\nif __name__ == "__main__":'
        assert src.count(mark) == 1
        open(gates_py, "w", encoding="utf-8").write(src.replace(mark, STUB + mark))
        check = run([sys.executable, "-B", os.path.join("scripts", "gates", "gates.py")], cwd=wt)
        lines = [l for l in check.stdout.splitlines() if l.startswith("  ")]
        print(f"    with the stub, the runner prints {sum(1 for l in lines if l.startswith('  PASS'))} PASS of {len(lines)} lines "
              f"(every gate made unable to fail)\n")
        after, tail = outcomes(wt, refs)
        still, fails, other = [], [], []
        for g, ref in sorted(reg.items()):
            if base.get(ref) != "PASSED":
                other.append((g, ref, base.get(ref), after.get(ref)))
            elif after.get(ref) == "PASSED":
                still.append((g, ref))
            else:
                fails.append((g, ref, after.get(ref)))
        print(f"with every gate unable to fail:\n  {len(fails)} controls FAIL (they depend on their gate's answer)\n"
              f"  {len(still)} controls still PASS (they do not)\n  {len(other)} could not be read (not passing in the control run)\n")
        print("the controls that still pass:")
        for g, ref in still:
            print(f"  {g:28s} {ref}")
        print("\nthe controls that fail, as a control should:")
        for g, ref, what in fails:
            print(f"  {g:28s} {what:7s} {ref}")
        for g, ref, b, x in other:
            print(f"\n  not read: {g} {ref} (control run: {b}; stubbed: {x})")
        named = {"carry-age", "doc-currency", "doc-facts", "genesis-cited", "harvest-debt", "lead-debt", "point-debt", "pretense-phrases",
                 "relay-debt", "retraction-sweep", "review-core", "seal-provenance", "seen-first"}
        s = {g for g, _ in still}
        print("\nEXPECTATIONS")
        print(f"  E1  every control passes with no gate changed: {'holds' if not not_passing else 'DOES NOT HOLD'}")
        print(f"  E2  the 13 named controls still pass: {'holds' if named <= s else 'DOES NOT HOLD: ' + ', '.join(sorted(named - s)) + ' fail'}")
        print(f"  E3  at least 20 controls fail: {'holds' if len(fails) >= 20 else 'DOES NOT HOLD'} ({len(fails)})")
        print(f"  E4  read-out: {len(s - named)} of the 40 that name their gate still pass: {', '.join(sorted(s - named)) or 'none'}")
    finally:
        run(["git", "-C", repo, "worktree", "remove", "--force", wt])
        shutil.rmtree(wt, ignore_errors=True)


if __name__ == "__main__":
    main()
