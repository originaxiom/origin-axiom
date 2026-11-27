#!/usr/bin/env python3
"""Failing control for P-610 (decisive wrapper: r610_decisive.py beside this file).

It copies the sealed folder relays/sm_r610/ to a fresh temporary directory and makes ONE deliberate change in
the copy's run.py: the object is made wrong. In rho(T) = zeta8 L^-1 the sign of L^-1's entry -1 is dropped, so
rho(T) becomes zeta8 times a plain permutation. Its determinant moves by a half turn (c = 21 + 3a, not 9 + 3a), and
it is no longer a representation equivalent to main's rho_T. The copy then runs with the repository root as its
main-checkout argument. The sealed folder is never edited. (A wrong cusp normalisation in the instrument, T-phase
a/12, was tried first: it leaves no admissible datum and the sealed script stops on an empty minimum, an invalid
control, so it is not used.)

If the claim's checks could not tell the object, the changed run would still report every deciding cell held, with
three chiral 27s first at 17/24. It must not.

    python3 relays/claims/sm_refile/r610_control.py

Exit 1, with a last line "CONTROL FAILS: ...", when the changed run completes and the check rejects it (the expected
outcome). Exit 0, "CONTROL DID NOT FAIL: ...", when the decisive cells still all hold. Exit 3, "CONTROL INVALID: ...",
when the edit cannot be applied or the run crashes. No traceback escapes.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

OLD = "RHO_T = Mono([0, 2, 1], [F(1, 8), F(1, 8) + F(1, 2), F(1, 8)])"
NEW = "RHO_T = Mono([0, 2, 1], [F(1, 8), F(1, 8), F(1, 8)])"
DECIDING = ("R0", "R1", "R2", "R3", "R4", "R5")


def main():
    try:
        here = pathlib.Path(__file__).resolve().parent
        root = None
        for start in (here, pathlib.Path.cwd().resolve()):
            for d in (start, *start.parents):
                if (d / "frontier").is_dir() and (d / "GENESIS.md").is_file():
                    root = d
                    break
            if root:
                break
        if root is None:
            print("CONTROL INVALID: the repository root was not found")
            return 3
        with tempfile.TemporaryDirectory() as tmp:
            work = pathlib.Path(tmp) / "sm_r610"
            shutil.copytree(root / "relays" / "sm_r610", work,
                            ignore=shutil.ignore_patterns("r610_results.json", "r610_run.txt", "__pycache__"))
            text = (work / "run.py").read_text(encoding="utf-8")
            if text.count(OLD) != 1:
                print("CONTROL INVALID: the planted change did not apply (%d matches)" % text.count(OLD))
                return 3
            (work / "run.py").write_text(text.replace(OLD, NEW), encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", "-B", "run.py", str(root)], cwd=str(work), capture_output=True,
                               text=True)
            res = work / "r610_results.json"
            data = json.loads(res.read_text(encoding="utf-8")) if res.is_file() else None
        if r.returncode != 0 or data is None:
            last = (r.stderr.strip().splitlines() or [""])[-1]
            print("CONTROL INVALID: the changed run crashed (exit %d): %s" % (r.returncode, last))
            return 3
        cells = data["cells"]
        threes = [tuple(x) for x in data["R4"]["threes"]]
        least = min((abs(x[1]) for x in threes), default=None)
        failed = [c for c in DECIDING if not cells.get(c, False)]
        print("CONTROL: changed run completed; deciding cells failed: %s; least |m| with three: %s"
              % (failed or "none", least))
        if failed:
            print("CONTROL FAILS: as it must; with L^-1's sign dropped, cells %s fail" % ", ".join(failed))
            return 1
        print("CONTROL DID NOT FAIL: every deciding cell still holds for the wrong object")
        return 0
    except Exception as exc:  # a crash is never a failing control
        print("CONTROL INVALID: the control raised %s" % exc.__class__.__name__)
        return 3


if __name__ == "__main__":
    sys.exit(main())
