#!/usr/bin/env python3
"""Decisive wrapper for P-581 (the sealed card relays/cards/SM_R581_one-class-for-the-structural-grades.md).

It copies the sealed folder relays/sm_r581/ to a fresh temporary directory and runs the sealed run.py there, unchanged,
on the frozen presentations r581_presentations.json (already in the folder) with the repository root as its
main-checkout argument. The extractor, which needs the census package, is not run. It prints the values the claim
decides, one per line, each beginning "DECISIVE: ". Nothing is written into the repository.

    python3 relays/claims/sm_refile/r581_decisive.py

Exit 0 when the run completes and every decisive value comes out; 1 otherwise. Depends on the standard library; the
sealed script needs numpy and sympy.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile


def find_root():
    for start in (pathlib.Path(__file__).resolve().parent, pathlib.Path.cwd().resolve()):
        for d in (start, *start.parents):
            if (d / "frontier").is_dir() and (d / "GENESIS.md").is_file():
                return d
    return None


def run_sealed(root, presentations_name="r581_presentations.json", tmp=None):
    """(exit status, stdout, stderr, run.txt text or None) of the sealed run.py on a temp copy of the sealed folder"""
    sealed = root / "relays" / "sm_r581"
    work = pathlib.Path(tmp) / "sm_r581"
    shutil.copytree(sealed, work)
    out = work / "out"
    r = subprocess.run([sys.executable, "-I", "-B", "run.py", str(root), presentations_name, str(out)],
                       cwd=str(work), capture_output=True, text=True)
    txt = out / "r581_run.txt"
    return r.returncode, r.stdout, r.stderr, (txt.read_text(encoding="utf-8") if txt.is_file() else None)


def decisive_lines(txt):
    """the claim's values, read from the sealed script's r581_run.txt; None for any that is missing"""
    t = txt or ""
    rate = lambda label: re.search(re.escape(label) + r"\s+(\d+) /\s+(\d+) =", t)
    want = [
        ("class size N (rule K)", re.search(r"rule K, N = (\d+)", t)),
        ("E6 route, 2T classes >= 1", rate("E6 route (2T classes >= 1)")),
        ("exactly the root's count, 2T classes == 2", rate("exactly the root's count (2T classes == 2)")),
        ("Z6 global form", rate("Z6 global form")),
        ("hypercharge direction", rate("hypercharge direction")),
        ("sin^2 = 3/8 at SU(5)", rate("sin^2 = 3/8 at SU(5)")),
        ("the package (all four)", rate("the package (all four)")),
        ("E7 label, 2O classes >= 1", rate("E7 label (2O classes >= 1)")),
        ("E8 label, 2I classes >= 1", rate("E8 label (2I classes >= 1)")),
        ("plant Z/3 (must be all)", rate("plant Z/3 (must be 1)")),
        ("package by tetrahedra", re.search(r"package rate by tetrahedra: (.+)", t)),
        ("steps after E6", re.search(r"steps after E6 \(object-independent\): (.+)", t)),
        ("root m004", re.search(r"root m004: (.+)", t)),
        ("control B993 per object", re.search(r"control B993 per object: (\d+ of \d+) agree", t)),
        ("plants", re.search(r"plants: (.+)", t)),
    ]
    lines = []
    for label, m in want:
        if m is None:
            return None
        if m.re.groups == 2:
            a, b = int(m.group(1)), int(m.group(2))
            lines.append("DECISIVE: %s: %d of %d (%.4f)" % (label, a, b, a / b))
        else:
            lines.append("DECISIVE: %s: %s" % (label, m.group(1).strip()))
    return lines


def main():
    root = find_root()
    if root is None:
        print("could not find the repository root (a folder with frontier/ and GENESIS.md)")
        return 1
    with tempfile.TemporaryDirectory() as tmp:
        try:
            rc, so, se, txt = run_sealed(root, tmp=tmp)
        except Exception as e:                                   # a missing folder or interpreter
            print("the sealed run could not be made: %s" % type(e).__name__)
            return 1
    if rc != 0 or txt is None:
        print("the sealed run did not complete (exit %d): %s" % (rc, (se.strip().splitlines() or [""])[-1]))
        return 1
    lines = decisive_lines(txt)
    if lines is None:
        print("a decisive value did not come out")
        return 1
    sealed_txt = (root / "relays" / "sm_r581" / "r581_run.txt").read_text(encoding="utf-8")
    print("\n".join(lines))
    print("DECISIVE: rerun output identical to the sealed r581_run.txt: %s" % (txt == sealed_txt))
    return 0


if __name__ == "__main__":
    sys.exit(main())
