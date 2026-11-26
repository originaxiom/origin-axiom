#!/usr/bin/env python3
"""Failing control for B2013's claim card (Review 87 entered, a process arc).

The decisive check is B2013's lock, frontier/B2013_*/verification/test_b2013_review_87.py, which on main prints
"2 passed".  This control runs the lock's own text (read from the repository and exec'd unchanged) against a COPY of
the files the lock reads, built in a temporary folder outside the repository.  Three runs:

  clean     the copy as on main; both tests must pass, or the copy is not faithful and the control is VOID
  change 1  plants.txt in the copy has one plant row altered after the seal (PLANT 4's "now: At mod 153" undone to
            "now: At mod 135"); test_plants_sealed must fail by AssertionError
  change 2  B1995's FINDINGS.md in the copy has Review 87's mend undone: the mended W± row is replaced by the anchor's
            row "| every mode of W± | 2, 2, 0 | ⅓, ⅓, ⅓ |" (36f9cc5c2), the fault reader A found; test_mends_present
            must fail by AssertionError

Run:  python3 -B control.py
      The repository root is found upward from this file or the current folder; otherwise set OA_REPO.
      OA_CONTROL_TMP names the folder for the copy (default: a fresh system temporary folder, removed at the end).

Exit status: 1 = the control fails as it must (each change makes its test fail by AssertionError, the clean copy
passes); 0 = a change left its test passing (the control cannot fail: a D3 breach); 2 = a crash (VOID); 3 = the clean
copy did not pass, or the lock's text is not the hashed one (VOID).  Standard library only.
"""

import sys as _sys, os as _os, traceback as _tb
def _crash(et, ev, tb):   # main's trial convention (P-885): a crash is never a failing control; it exits 3
    _tb.print_exception(et, ev, tb); print("CONTROL INVALID: the control raised; a crash is not a failing control")
    _sys.stdout.flush(); _os._exit(3)
_sys.excepthook = _crash
import hashlib, os, pathlib, shutil, sys, tempfile, traceback

LOCK_SHA16 = "fd0b275025f027ea"   # sha256 of test_b2013_review_87.py, first 16 hex, as on the card
ARC = "B2013"
LOCK_REL = "verification/test_b2013_review_87.py"
# the files the lock reads, relative to each arc's folder (the lock finds a folder by the glob "<arc>_*")
READS = {
    "B2013": ["verification/plants.txt", LOCK_REL],
    "B1980": ["FINDINGS.md"], "B1983": ["FINDINGS.md"], "B1995": ["FINDINGS.md"],
    "B1996": ["FINDINGS.md", "verification/test_b1996_tower.py"],
    "B2009": ["FINDINGS.md"], "B2012": ["FINDINGS.md"],
    "B1993": ["verification/test_b1993_integers.py"],
}
PLANT_NOW = "now: At mod 153 ρ factors and"
PLANT_UNDONE = "now: At mod 135 ρ factors and"
MEND_ROW = ("| W±'s modes (its eigenvalue-2 space is a plane) | 2, 2, 0 | [Review 87, 2026-11-26: the row printed ⅓, ⅓, ⅓ "
            "for sympy's basis of that plane, which depends on the basis; only the plane's projector is meaningful, and "
            "it gives each member 2/3, the long run below] |")
ANCHOR_ROW = "| every mode of W± | 2, 2, 0 | ⅓, ⅓, ⅓ |"


def find_repo():
    env = os.environ.get("OA_REPO")
    if env:
        return pathlib.Path(env).resolve()
    for start in (pathlib.Path(__file__).resolve().parent, pathlib.Path.cwd().resolve()):
        for p in (start, *start.parents):
            if (p / "WORKING_RULES.md").is_file() and any((p / "frontier").glob(ARC + "_*")):
                return p
    return None


def arc_dir(root, arc):
    hits = sorted((root / "frontier").glob(arc + "_*"))
    if len(hits) != 1:
        raise RuntimeError(f"{arc}: {len(hits)} folders match {arc}_*")
    return hits[0]


def build_copy(repo, dest):
    if dest.exists():
        shutil.rmtree(dest)
    for arc, rels in READS.items():
        src = arc_dir(repo, arc)
        for rel in rels:
            out = dest / "frontier" / src.name / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src / rel, out)
    return dest


def run_lock(text, copy_root):
    """exec the lock's text with __file__ inside the copy; return {test: ("PASS"|"FAIL"|"CRASH", detail)}."""
    lock_path = arc_dir(copy_root, ARC) / LOCK_REL
    ns = {"__file__": str(lock_path), "__name__": "b2013_lock_copy"}
    code = compile(text, str(lock_path), "exec")
    exec(code, ns)
    src_lines = text.splitlines()
    out = {}
    for name in ("test_plants_sealed", "test_mends_present"):
        try:
            ns[name]()
            out[name] = ("PASS", "")
        except AssertionError:
            tb = [f for f in traceback.extract_tb(sys.exc_info()[2]) if f.filename == str(lock_path)]
            ln = tb[-1].lineno if tb else 0
            out[name] = ("FAIL", f"AssertionError at lock line {ln}: {src_lines[ln - 1].strip()[:110]}" if ln else "AssertionError")
        except Exception as e:  # anything else is a crash, never a failing control
            out[name] = ("CRASH", f"{type(e).__name__}: {e}")
    return out


def edit(path, old, new):
    t = path.read_text()
    if t.count(old) != 1:
        raise RuntimeError(f"{path.name}: the text to change occurs {t.count(old)} times, not once")
    path.write_text(t.replace(old, new))


def main():
    repo = find_repo()
    if repo is None:
        print("CONTROL VOID: repository not found (set OA_REPO)")
        return 3
    lock_text_b = (arc_dir(repo, ARC) / LOCK_REL).read_bytes()
    sha16 = hashlib.sha256(lock_text_b).hexdigest()[:16]
    print(f"lock {ARC}/{LOCK_REL} sha256 {sha16}")
    if sha16 != LOCK_SHA16:
        print(f"CONTROL VOID: the lock's sha256 is {sha16}, not the card's {LOCK_SHA16}")
        return 3
    text = lock_text_b.decode()
    tmp_env = os.environ.get("OA_CONTROL_TMP")
    base = pathlib.Path(tmp_env).resolve() if tmp_env else pathlib.Path(tempfile.mkdtemp(prefix="b2013_control_"))
    if str(base).startswith(str(repo) + os.sep):
        print("CONTROL VOID: the copy folder is inside the repository")
        return 3
    try:
        runs = {}
        # clean
        c0 = build_copy(repo, base / "clean")
        runs["clean"] = run_lock(text, c0)
        # change 1: one plant row altered after the seal
        c1 = build_copy(repo, base / "change1_plant_row_altered")
        edit(arc_dir(c1, ARC) / "verification/plants.txt", PLANT_NOW, PLANT_UNDONE)
        runs["change 1 (PLANT 4 'mod 153' undone to 'mod 135' in plants.txt)"] = run_lock(text, c1)
        # change 2: B1995's mend undone (the anchor's row restored)
        c2 = build_copy(repo, base / "change2_B1995_mend_undone")
        edit(arc_dir(c2, "B1995") / "FINDINGS.md", MEND_ROW, ANCHOR_ROW)
        runs["change 2 (B1995's W± row restored to the anchor's)"] = run_lock(text, c2)
    except Exception as e:
        print(f"CONTROL VOID: crash while building or running the copy: {type(e).__name__}: {e}")
        return 3
    finally:
        if not tmp_env:
            shutil.rmtree(base, ignore_errors=True)

    for label, res in runs.items():
        for name, (st, det) in res.items():
            print(f"{label}: {name} {st}" + (f" ({det})" if det else ""))
    if any(st == "CRASH" for res in runs.values() for st, _ in res.values()):
        print("CONTROL VOID: a run crashed")
        return 3
    if not all(st == "PASS" for st, _ in runs["clean"].values()):
        print("CONTROL VOID: the clean copy does not pass, so the copy is not faithful")
        return 3
    k1, k2 = list(runs)[1:]
    hit1 = runs[k1]["test_plants_sealed"][0] == "FAIL"
    hit2 = runs[k2]["test_mends_present"][0] == "FAIL"
    tally = lambda res: (sum(st == "PASS" for st, _ in res.values()), sum(st == "FAIL" for st, _ in res.values()))
    if hit1 and hit2:
        (p1, f1), (p2, f2) = tally(runs[k1]), tally(runs[k2])
        print(f"CONTROL FAILS: as it must, under each change the lock no longer gives '2 passed' "
              f"(change 1: {p1} passed, {f1} failed; change 2: {p2} passed, {f2} failed)")
        return 1
    print(f"CONTROL CANNOT FAIL: change 1 caught {hit1}, change 2 caught {hit2}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
