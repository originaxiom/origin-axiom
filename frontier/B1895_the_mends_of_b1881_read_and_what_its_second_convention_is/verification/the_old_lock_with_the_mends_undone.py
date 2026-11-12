#!/usr/bin/env python3
"""B1895 -- the fourth finding reproduced: B1881's lock, as it stood at the commit that was read, with each mend undone.

The reading found that the lock held two of the nine mends of Review 79.  Here B1881 is taken as it stood at 87bfa1f05, from git,
into a temporary folder.  Each mend is undone there, one at a time, and the lock of that commit is run.  A plant that passes
every test is a mend the lock did not hold.  The last entry changes what the lock did hold, and must be caught.  Nothing in the
repository is changed.

    python3 the_old_lock_with_the_mends_undone.py            # prints the table and whether the committed result agrees
    python3 the_old_lock_with_the_mends_undone.py --write
"""
import io
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
READ = "87bfa1f05"
ARC = "frontier/B1881_the_whole_and_the_value_verified"


def main():
    r = subprocess.run(["git", "-C", str(ROOT), "archive", READ, ARC], capture_output=True)
    led = subprocess.run(["git", "-C", str(ROOT), "show", READ + ":docs/HARVEST_LEDGER.md"], capture_output=True)
    if r.returncode != 0 or led.returncode != 0:
        print("not run here: the commit that was read is not in this clone")
        return None
    work = pathlib.Path(tempfile.mkdtemp(prefix="b1895_old_lock_"))
    tarfile.open(fileobj=io.BytesIO(r.stdout)).extractall(work)
    (work / "docs").mkdir()
    (work / "docs" / "HARVEST_LEDGER.md").write_bytes(led.stdout)
    arc = work / ARC
    keep = {p: p.read_bytes() for p in arc.rglob("*") if p.is_file()}
    script, page, data = arc / "verification" / "whole_and_value_on_main.py", arc / "FINDINGS.md", arc / "verification" / "whole_and_value_on_main.json"

    def run():
        out = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", str(arc / "verification")], capture_output=True, text=True).stdout
        return sorted(set(re.findall(r"FAILED \S+::(\w+)", out)))

    def sub(path, old, new):
        t = path.read_text(encoding="utf-8")
        assert old in t, old[:60]
        path.write_text(t.replace(old, new), encoding="utf-8")

    def cut(path, pattern):
        t = path.read_text(encoding="utf-8")
        t2 = re.sub(pattern, "", t, flags=re.S)
        assert t2 != t, pattern[:60]
        path.write_text(t2, encoding="utf-8")

    plants = [
        ("nothing: the lock as it stood", "", lambda: None),
        ("the single runs' check passed the literal True again", "SM-13, X7", lambda: sub(script, 'for the run of 5m + 1", single_ok,', 'for the run of 5m + 1", True,')),
        ("the mirror's check passed the literal True again", "SM-13, X7", lambda: sub(script, "mirror_ok and len(box) >= 200 and sum(1 for x in box if x[2] != 0) >= 200,", "True,")),
        ("the bound 0.9 to 1 dropped from the script's check", "SM-14", lambda: sub(script, ' and mp.mpf("0.9") < (one6 - own["(6)"]) / own["(6)"] * 100 < 1', "")),
        ("every correction bracket deleted from the page", "SM-11, SM-12, SM-16, SM-17", lambda: cut(page, r" ?\[CORRECTED\s+2026-11-12.*?\]")),
        ("the bullet on the three checks deleted from the page", "SM-13, SM-14, SM-15", lambda: cut(page, r"- \*\*Three checks did not check what they said\*\*.*?recomputes all three now\.\n")),
        ("one cusp width changed in the run's file: what the lock did hold", "SM-15, X8", lambda: sub(data, '"quotient_line": [\n   6,\n   [\n    1,\n    5\n   ]', '"quotient_line": [\n   6,\n   [\n    1,\n    4\n   ]')),
    ]
    out = []
    for name, mends, fn in plants:
        for p, b in keep.items():
            p.write_bytes(b)
        fn()
        failed = run()
        out.append({"undone": name, "the mends it belongs to": mends, "tests failing": failed})
        print("%-70s %-28s %s" % (name, mends, "caught: " + ", ".join(failed) if failed else "PASSES EVERY TEST"))
    shutil.rmtree(work)
    return {"the commit read": READ, "tests in the lock at that commit": 5, "plants": out,
            "undone with every test passing": sum(1 for o in out[1:-1] if not o["tests failing"]), "of": len(out) - 2,
            "the lock as it stood passes": not out[0]["tests failing"], "what it did hold is caught": bool(out[-1]["tests failing"])}


if __name__ == "__main__":
    res = main()
    if res is not None:
        f = HERE / "the_old_lock_with_the_mends_undone.json"
        print("\nundone with every test passing: %d of %d | the lock as it stood passes: %s | what it did hold is caught: %s"
              % (res["undone with every test passing"], res["of"], res["the lock as it stood passes"], res["what it did hold is caught"]))
        if "--write" in sys.argv:
            f.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        else:
            print("the committed result agrees: %s" % (json.loads(f.read_text(encoding="utf-8")) == res if f.is_file() else False))
