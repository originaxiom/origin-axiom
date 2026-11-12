#!/usr/bin/env python3
"""B1897 -- B1881's lock, planted against a second time.

A session that did not write the lock planted 23 errors against it as it stood after B1895 (main's 3c5ab6bef).  Seventeen were
caught and six passed.  The lock has four more tests now.  [CORRECTED 2026-11-12 (Review 80): five more; the fifth tests the weaker
comparison and came before this arc's push, 644d5b40f.]  Here the six are made again by main from the session's descriptions
of them, since main does not run that session's code, together with the eighteen reversions of B1895, each in a scratch copy
of the arc, and the lock is run on the copy.  The first entry plants nothing and must pass.  Nothing in the repository is
changed: the copy is made in a temporary folder and removed.

    python3 planted_a_second_time.py            # prints the table and whether the committed result agrees
    python3 planted_a_second_time.py --write
"""
import importlib.util
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARC = "frontier/B1881_the_whole_and_the_value_verified"
FIRST = ROOT / "frontier" / "B1895_the_mends_of_b1881_read_and_what_its_second_convention_is" / "verification" / "planted_reversions.py"


def _first():
    """B1895's runner, for its eighteen plants and its helpers; its copy is made in a folder of this run's own"""
    spec = importlib.util.spec_from_file_location("b1895_planted_reversions", FIRST)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def six(m):
    script = lambda arc: arc / "verification" / "whole_and_value_on_main.py"

    def a_paragraph_of_its_own(arc):
        f = arc / "FINDINGS.md"
        t = f.read_text(encoding="utf-8")
        at = t.index("## 6. What it means for the read-out on the whole")
        f.write_text(t[:at] + "The column convention, with the ground [[2, 1], [1, 1]], is the matrix transpose of the seat's [[1, 1], [1, 2]].\n\n" + t[at:], encoding="utf-8")

    def the_functions_docstring(arc):
        m.sub(script(arc), "These letters are the seat's\n    conjugated by the swap of the two coordinates; see the note at E12 in the header.]",
              "These letters are the transpose\n    of the seat's convention; see the note at E12 in the header.]")

    def the_counts_typed(arc):
        s = script(arc)
        t = s.read_text(encoding="utf-8")
        t2 = re.sub(r"    by_all = len\(\{min\(seq\[i:\] \+ seq\[:i\] for i in range\(len\(seq\)\)\) for seq in seqs\}\)\n", "    by_all = 2815\n", t)
        t2 = re.sub(r"    by_even = len\(\{min\(seq\[i:\] \+ seq\[:i\] for i in range\(0, len\(seq\), 2\)\) for seq in seqs\}\)\n", "    by_even = 5575\n", t2)
        assert t2.count("by_all = 2815") == 1 and t2.count("by_even = 5575") == 1
        s.write_text(t2, encoding="utf-8")

    def the_run_file_edited(arc):
        r = arc / "verification" / "whole_and_value_on_main_run.txt"
        t = r.read_text(encoding="utf-8")
        t2 = t.replace("(16275 sequences as written; 2815 up to rotation; 5575 up to the rotations that keep which letter a run is)", "(16275 sequences)")
        t2 = t2.replace("{'the twin exchange': ['-11 + 2*I', '-11 - 2*I'], 'W': ['5*sqrt(5)'], 'W with the twin exchange': ['-5*sqrt(5)']}",
                        "{'the twin exchange': {'-11 - 2*I', '-11 + 2*I'}, 'W': {'5*sqrt(5)'}, 'W with the twin exchange': {'-5*sqrt(5)'}}")
        assert t2 != t and t2.count("(16275 sequences)") == 1
        r.write_text(t2, encoding="utf-8")

    def a_clause_that_is_always_true(arc):
        m.sub(script(arc), "mirror_ok and len(box) >= 200 and sum(1 for x in box if x[2] != 0) >= 200,", "mirror_ok and len(box) >= 200 and sum(1 for x in box if x[2] != 0) >= 200 or len(box) > 0,")
        m.sub(script(arc), 'for the run of 5m + 1", single_ok,', 'for the run of 5m + 1", single_ok or len(single) > 0,')

    def the_sorting_undone(arc):
        m.sub(script(arc), "{k: sorted(v) for k, v in over.items()})", "over)")

    return [("a sentence that states the withdrawn claim, in a paragraph of its own", a_paragraph_of_its_own),
            ("the docstring of the script's second function given the withdrawn word", the_functions_docstring),
            ("the script's counts of run sequences typed in place of computed", the_counts_typed),
            ("the committed run file edited where the lock did not read it", the_run_file_edited),
            ("a clause that is not a literal and is always true, joined by `or` to two conditions", a_clause_that_is_always_true),
            ("the sorting of a printed set undone", the_sorting_undone)]


if __name__ == "__main__":
    m = _first()
    shutil.rmtree(m.WORK.parent, ignore_errors=True)          # the folder B1895's runner makes for itself when it is loaded
    m.WORK = pathlib.Path(tempfile.mkdtemp(prefix="b1897_plants_")) / "copy"
    plants = [m.PLANTS[0]] + [("of the six that passed: " + n, f) for n, f in six(m)] + [("of B1895's eighteen: " + n, f) for n, f in m.PLANTS[1:]]
    out = []
    for name, fn in plants:
        arc = m.fresh()
        fn(arc)
        failed, last = m.run(arc)
        out.append({"plant": name, "tests failing": failed})
        print("%-112s %s  %s" % (name, "CAUGHT" if failed else "passes", ", ".join(x[5:60] for x in failed)))
    shutil.rmtree(m.WORK.parent)
    six_caught = sum(1 for o in out[1:7] if o["tests failing"])
    res = {"control passes": not out[0]["tests failing"], "of the six that passed, caught now": six_caught, "of B1895's eighteen, caught": sum(1 for o in out[7:] if o["tests failing"]),
           "caught": sum(1 for o in out[1:] if o["tests failing"]), "of": len(out) - 1, "plants": out}
    print("\ncontrol passes: %s | of the six that passed, caught now: %d of 6 | of B1895's eighteen: %d of 18 | all: %d of %d"
          % (res["control passes"], six_caught, res["of B1895's eighteen, caught"], res["caught"], res["of"]))
    f = HERE / "planted_a_second_time.json"
    if "--write" in sys.argv:
        f.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        print("the committed result agrees: %s" % (json.loads(f.read_text(encoding="utf-8")) == res if f.is_file() else False))
