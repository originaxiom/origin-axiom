#!/usr/bin/env python3
"""B1895 -- planted reversions against B1881's lock.

A reading of B1881's mends found that its lock held two of the nine mends of Review 79: the other seven could be undone with every
test passing.  The lock now has five more tests.  Here each mend is undone, one at a time, in a scratch copy of the arc, and the
lock is run on the copy.  A plant that passes every test is a mend that nothing holds.  The first entry plants nothing and must
pass.  Nothing in the repository is changed: the copy is made in a temporary folder and removed.

    python3 planted_reversions.py            # prints the table and whether the committed result agrees
    python3 planted_reversions.py --write
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WORK = pathlib.Path(tempfile.mkdtemp(prefix="b1895_plants_")) / "copy"
ARC = "frontier/B1881_the_whole_and_the_value_verified"


def fresh():
    if WORK.exists(): shutil.rmtree(WORK)
    (WORK / "frontier").mkdir(parents=True); (WORK / "docs").mkdir()
    shutil.copytree(ROOT / ARC, WORK / ARC, ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copy(ROOT / "docs" / "HARVEST_LEDGER.md", WORK / "docs" / "HARVEST_LEDGER.md")
    return WORK / ARC

def sub(path, old, new, count=1):
    t = path.read_text(encoding="utf-8")
    assert t.count(old) >= 1, (path.name, old[:60])
    path.write_text(t.replace(old, new) if count is None else t.replace(old, new, count), encoding="utf-8")

def run(arc):
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", str(arc / "verification")], capture_output=True, text=True)
    failed = sorted(set(re.findall(r"FAILED \S+::(\w+)", r.stdout)))
    return failed, r.stdout.strip().splitlines()[-1]

def p_literal_true_single(arc):
    sub(arc / "verification/whole_and_value_on_main.py", 'for the run of 5m + 1", single_ok,', 'for the run of 5m + 1", True,')
def p_literal_true_mirror(arc):
    sub(arc / "verification/whole_and_value_on_main.py", 'mirror_ok and len(box) >= 200 and sum(1 for x in box if x[2] != 0) >= 200,', 'True,')
def p_name_bound_to_true(arc):
    sub(arc / "verification/whole_and_value_on_main.py", "    single_ok = all(", "    single_ok = True\n    unused = all(")
def p_drop_the_bound(arc):
    sub(arc / "verification/whole_and_value_on_main.py", ' and mp.mpf("0.9") < (one6 - own["(6)"]) / own["(6)"] * 100 < 1', '')
def p_delete_the_brackets(arc):
    f = arc / "FINDINGS.md"; t = f.read_text(encoding="utf-8")
    t2 = re.sub(r" ?\[CORRECTED\s+2026-11-12.*?\]", "", t, flags=re.S)
    t2 = re.sub(r"- \*\*Three checks did not check what they said\*\*.*?recomputes all three now\.\n", "", t2, flags=re.S)
    assert t2 != t; f.write_text(t2, encoding="utf-8")
def p_delete_only_the_bullet(arc):
    f = arc / "FINDINGS.md"; t = f.read_text(encoding="utf-8")
    t2 = re.sub(r"- \*\*Three checks did not check what they said\*\*.*?recomputes all three now\.\n", "", t, flags=re.S)
    assert t2 != t; f.write_text(t2, encoding="utf-8")
def p_delete_the_second_note(arc):
    f = arc / "FINDINGS.md"; t = f.read_text(encoding="utf-8")
    t2 = re.sub(r"> \*\*CORRECTED 2026-11-12, a second time,\*\*.*?>   header\.\n", "", t, flags=re.S)
    assert t2 != t; f.write_text(t2, encoding="utf-8")
def p_verdict_reproduced(arc):
    sub(arc / "arc_verdict.json", "every printed number recomputed [CORRECTED 2026-11-12: this read 'reproduced', a word the record keeps for the same code run again; none of the seat's code was run]", "every printed number reproduced")
def p_verdict_transpose_only(arc):
    v = arc / "arc_verdict.json"; t = v.read_text(encoding="utf-8")
    t2 = re.sub(r" CORRECTED AGAIN the same day, found by a second reading of that note:.*?an instance of an identity\]", "]", t, flags=re.S)
    assert t2 != t; v.write_text(t2, encoding="utf-8")
def p_old_label(arc):
    old = "the least apex over every cyclic run sequence of even length to 6 with runs to 5 is the ground's own, sqrt5/2 (16275 sequences)"
    j = arc / "verification/whole_and_value_on_main.json"; d = json.loads(j.read_text(encoding="utf-8"))
    k = [x for x in d if x.startswith("the least apex over every run sequence")][0]
    d = {(old if x == k else x): y for x, y in d.items()}; j.write_text(json.dumps(d, indent=1) + "\n", encoding="utf-8")
    r = arc / "verification/whole_and_value_on_main_run.txt"; t = r.read_text(encoding="utf-8"); r.write_text(t.replace(k, old), encoding="utf-8")
def p_wrong_count_in_json(arc):
    j = arc / "verification/whole_and_value_on_main.json"; d = json.loads(j.read_text(encoding="utf-8"))
    d["B_counts"]["up_to_every_rotation"] = 2816; j.write_text(json.dumps(d, indent=1) + "\n", encoding="utf-8")
def p_e12_or(arc):
    sub(arc / "verification/whole_and_value_on_main.py", "RES[name] = (disagree == 0 and rev == 0 and agree == 6 ** 2 + 6 ** 4 + 6 ** 6)", "RES[name] = (disagree == 0 or rev == 0 or rot == 0)")
def p_old_docstring(arc):
    sub(arc / "verification/whole_and_value_on_main.py", '"""this arc\'s second convention: L = [[1,1],[0,1]], R = [[1,0],[1,1]], columns, v = (1,2).', '"""B1872\'s convention: L = [[1,1],[0,1]], R = [[1,0],[1,1]], columns, v = (1,2).')
def p_another_second_mark(arc):
    sub(arc / "verification/whole_and_value_on_main.py", "    col = ((Wd[0] * 1 + Wd[1] * 2) % 5, (Wd[2] * 1 + Wd[3] * 2) % 5)\n    return line(col) == line((1, 2))",
        "    col = ((Wd[0] * 1 + Wd[1] * 3) % 5, (Wd[2] * 1 + Wd[3] * 3) % 5)\n    return line(col) == line((1, 3))")
def p_second_convention_is_the_transpose(arc):
    # make the script's second function the transpose proper: the letters in reversed order
    sub(arc / "verification/whole_and_value_on_main.py", "    for k, r in enumerate(runs):\n        Wd = mul(Wd, (1, r % 5, 0, 1) if k % 2 == 0 else (1, 0, r % 5, 1))",
        "    for k, r in enumerate(runs):\n        Wd = mul((1, r % 5, 0, 1) if k % 2 == 0 else (1, 0, r % 5, 1), Wd)")
def p_page_88(arc):
    sub(arc / "FINDINGS.md", "for (1, 1) the two agree on 88 of the 120", "for (1, 1) the two agree on 104 of the 120")
def p_page_figure(arc):
    sub(arc / "FINDINGS.md", "reads 3.6515, 0.92 percent above its own value", "reads 3.6515, 0.93 percent above its own value")
def p_page_reproduced(arc):
    f = arc / "FINDINGS.md"; t = f.read_text(encoding="utf-8")
    t2 = re.sub(r"is recomputed by main's own code:\*\* 65 checks, none failing\. \[CORRECTED.*?was run\.\]", "is reproduced by main's own code:** 65 checks, none failing.", t, flags=re.S)
    assert t2 != t; f.write_text(t2, encoding="utf-8")
def p_nothing(arc):
    pass

PLANTS = [("control: nothing planted", p_nothing), ("the single runs' check passed the literal True again", p_literal_true_single), ("the mirror's check passed the literal True again", p_literal_true_mirror),
          ("a name bound to True passed to a check", p_name_bound_to_true), ("the bound 0.9 to 1 dropped from the script's check", p_drop_the_bound),
          ("every [CORRECTED] bracket and the bullet deleted from the page", p_delete_the_brackets), ("the bullet 'Three checks did not check what they said' deleted", p_delete_only_the_bullet),
          ("the second note on the transpose deleted", p_delete_the_second_note), ("the verdict line says 'reproduced' again", p_verdict_reproduced),
          ("the verdict line keeps 'the transpose' with its second correction removed", p_verdict_transpose_only), ("the old label 'cyclic run sequence (16275 sequences)' back in the run and its file", p_old_label),
          ("one count changed in the run's file", p_wrong_count_in_json), ("the check on the two conventions passes on any of three again", p_e12_or), ("the docstring names B1872 again", p_old_docstring),
          ("the script's second mark moved to the mark's own column", p_another_second_mark), ("the script's second word made the transpose (letters in reversed order)", p_second_convention_is_the_transpose),
          ("the page says 104 of 120 for the control", p_page_88), ("the page says 0.93 percent", p_page_figure), ("the page says 'is reproduced' again, the bracket removed", p_page_reproduced)]

if __name__ == "__main__":
    out = []
    for name, fn in PLANTS:
        arc = fresh(); fn(arc)
        failed, last = run(arc)
        out.append({"plant": name, "tests failing": failed})
        print("%-92s %s  %s" % (name, "CAUGHT" if failed else "passes", ", ".join(x[5:] for x in failed)))
    shutil.rmtree(WORK.parent)
    res = {"control passes": not out[0]["tests failing"], "caught": sum(1 for o in out[1:] if o["tests failing"]), "of": len(out) - 1, "plants": out}
    print("\ncontrol passes: %s | planted reversions caught: %d of %d" % (res["control passes"], res["caught"], res["of"]))
    f = HERE / "planted_reversions.json"
    if "--write" in sys.argv:
        f.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        # which plants are caught is compared, not which tests catch them: the lock has gained tests since (B1897), and the
        # committed file is the record of the lock as it stood on the day of this arc
        old = json.loads(f.read_text(encoding="utf-8")) if f.is_file() else {"plants": []}
        same = [bool(o["tests failing"]) for o in old["plants"]] == [bool(o["tests failing"]) for o in res["plants"]] and [o["plant"] for o in old["plants"]] == [o["plant"] for o in res["plants"]]
        print("the committed result agrees in which plants are caught: %s" % same)
