#!/usr/bin/env python3
"""Review 80: main's second probe of the rows of agy-002's file that are in the enforcement package's code, WRITTEN AGAIN.

Main kept the output of this probe (../checks/builder_rows_probe2.json: rows 46 to 53, fourteen cases, each made again)
and not its script.  Sent back by the builder with R80a; main's fault by its word in M16.  This script is the builder's,
written on 2026-11-12 from the fourteen kept lines: one case for each line, under the line's own words, given to the
package's own function.  It prints each case, what the function answered, and whether the answer is the one main kept.

What it cannot say: that a case here is the case main ran.  Main's lines give the case in a few words and the answer cut
short; where a line leaves the case open, the case below is the builder's reading of it, and its comment says so.

Nothing in the repository is changed.  The answers are those of the package as it stands where the script is run: a
series that mends a row changes its answer, and the kept file beside this script says on which commit it was run.

    python3 builder_rows_probe2.py        # prints the cases, and writes builder_rows_probe2.json beside itself
"""
import importlib.util, inspect, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "scripts" / "gates" / "gates.py").is_file())
KEPT = json.loads((HERE.parent / "checks" / "builder_rows_probe2.json").read_text(encoding="utf-8"))


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m)
    return m


g = load("gates_probe2", "scripts/gates/gates.py")
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
import retraction_sweep as rs

OUT = []


def say(row, case, answer):
    kept = next((k for k in KEPT if k["row"] == row and k["case"] == case), None)
    same = kept is not None and kept["answer"] == answer
    OUT.append({"row": row, "case": case, "answer": answer, "main kept": kept["answer"] if kept else None, "the same as main kept": same})
    print("row %-3s %-82s -> %-52s %s" % (row, case[:82], answer[:52], "AS MAIN KEPT" if same else "NOT AS MAIN KEPT"))


# ---- row 46: the claims gate asks that a cited lock holds a test, by one pattern on the file's text
pattern = re.search(r're\.search\(r"([^"]+)", open\(full', inspect.getsource(g.gate_claims))
a_file = '"""a file of notes\n\n    def test_this_is_inside_the_docstring():\n        pass\n"""\nX = 1\n'
say(46, "(a) a file whose only 'def test' is inside its docstring is taken for a lock",
    str(bool(pattern and re.search(pattern.group(1), a_file, re.M))))

# ---- row 47: the sweep's reader of a registry row, and its flattening of a line
kind = lambda row: rs.rows_in("| phrase | arc | why |\n|---|---|---|\n" + row + "\n")[0][0]
say(47, "(a) a row of two quoted phrases joined by a slash", kind('| "a first phrase" / "a second phrase" | B1, 2026-11-12 | why |'))
say(47, "(a) a row whose scope note is in italics", kind('| "a phrase" *(of the whole family)* | B1, 2026-11-12 | why |'))
say(47, "the control: the same with a plain bracket", kind('| "a phrase" (of the whole family) | B1, 2026-11-12 | why |'))
say(47, "(c) the flattening leaves asterisks and a curly apostrophe",
    "%r %r" % (rs._flatten("the *weave's* lifts"), rs._flatten("the weave’s lifts")))

# ---- row 48: a ceiling that is no whole number
path = "docs/ATTRIBUTION_BASELINE.json"
say(48, "a new ceiling of five and a half, with none at the anchor", str(g.ceiling_rises(path, {"a/page.md": 5.5}, {})))
say(48, "the control: a new ceiling of five", str(g.ceiling_rises(path, {"a/page.md": 5}, {})[0])[:60])

# ---- row 49: a raise of the baseline recorded "from false to true"
then = {"unearned": 1, "_baseline_raises": []}
a_raise = {"date": "2026-11-12", "reason": "a reason", "from": False, "to": True}
problem, note = g.baseline_rise({"unearned": 2, "_baseline_raises": [a_raise]}, then)
say(49, "a rise of one covered by a recorded raise from false to true", str((problem, note[:40])))
say(49, "the control: the same rise with no raise recorded", str(g.baseline_rise({"unearned": 2, "_baseline_raises": []}, then)[0])[:70])

# ---- row 50: the identification register reads a row's status as a whole cell (the builder's reading of main's line: the gate's
#      own line is looked for in its source)
say(50, "the status is looked for as a whole cell",
    str('if c in ("EARNED", "REFUTED", "UNEARNED")' in inspect.getsource(g.gate_identification_register)))

# ---- row 51: what a page has held is taken from the log of its history (the builder's reading: the option is looked for in the
#      source of the function that reads that log)
say(51, "the page's history is read with no --reverse", str("--reverse" in inspect.getsource(g.held_since)))

# ---- row 52: a law's row is passed over when three hyphens stand anywhere on its line
law_map = ("| law | arc | status |\n|---|---|---|\n"
           "| **A law with a dash in its prose** | B1 --- and a note | THEOREM |\n"
           "| **Another law** | B2 | THEOREM |\n")
say(52, "(a) a row with three hyphens in its prose", str(g._law_titles(law_map)))

# ---- row 53: the test that gates are a function of the commit
test = (ROOT / "tests" / "test_gates_are_a_function_of_the_commit.py").read_text(encoding="utf-8")
clock = re.compile(re.search(r'clock = re\.compile\(r"([^"]+)"\)', test).group(1))
harvest = (ROOT / "scripts" / "checks" / "harvest_debt.py").read_text(encoding="utf-8").split("\n")
line = next((l for l in harvest if "fromtimestamp(" in l), "")          # the builder's reading: the line that takes a day in the machine's zone
say(53, "(a) the test's pattern for a read of the clock, on the harvest checker's line", str(bool(line) and bool(clock.search(line.split("#", 1)[0]))))
sub = re.compile(re.search(r"_SUB = re\.compile\(r'''(.+?)'''\)", test).group(1))
say(53, "(b) the subcommand read from a call that begins with -c", str(sub.search('["git", "-c", "user.name=x", "log", "-1"]').groups()))

json.dump(OUT, open(HERE / "builder_rows_probe2.json", "w"), indent=1, ensure_ascii=False)
print("\nrows probed: %s | cases: %d | the same as main kept: %d | main's kept lines with no case here: %d"
      % (sorted({o["row"] for o in OUT}), len(OUT), sum(o["the same as main kept"] for o in OUT),
         sum(1 for k in KEPT if not any(o["row"] == k["row"] and o["case"] == k["case"] for o in OUT))))
