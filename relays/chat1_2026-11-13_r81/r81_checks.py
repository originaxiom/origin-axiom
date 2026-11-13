#!/usr/bin/env python3
"""Review 81, the web seat's checks (card W-R81).

Usage:  python3 -I r81_checks.py CHECKOUT CLONE
  CHECKOUT  a scratch worktree made by `git worktree add CHECKOUT c40446392` and then
            `git diff --binary c40446392 7d7ab1dfa | git apply --index` inside it: the window as a difference, so that
            7d7ab1dfa is not opened by itself
  CLONE     a clone of the repository that holds c40446392, 7d7ab1dfa, 38d2a36dc, 0dda7b472, e6298271a and 896cae025

What it prints: counts, booleans and the literal strings this seat looks for. It prints no text of a file. Section P
changes one file of CHECKOUT, runs a lock, and puts the file back from the index; nothing else is written.

EXPECTATIONS, written before the run:
  A  B1898 § 4's row for agy-exp holds "15 of 15"; the recount gives [14, 14]; the second table's head and the verdict
     line hold "14 of 14"; main's kept check of agy-exp's quotations has 14 findings and 15 lines of quotation.
  B  The second table's row 18 names `e6298271a`; main's probe for SM-18 counted at 896cae025; at e6298271a there are
     1,407 files tests/test_b*.py and 1,537 files test_*.py under tests/ at any depth; the gates' anchor is e6298271a.
  C  Register row P-670 holds "within 5.8 × 10⁻³³"; the kept run holds 5.775751444006791e-31; B1836's note holds
     "by at most 5.8 × 10⁻³¹".
  D  B1892 § 5's table sums to 53, 43 and 9; B1892 § 1 and the second table's row 06 give 52.
  E  Of the 73 findings main checked in full that are not this seat's, some have no file in `checks/` behind them (a
     row counts as having one if its cell names a file there, if main's probe of the SM seat's rows or its plants
     against B1881's lock hold the row, or if it is "the same as" an agy-002 row that has one); the rows are printed.
  F  Review 79's window 38d2a36dc..0dda7b472 has 31 older arcs changed, 25 in their verdict or findings; B1880's
     class A has 7 files and class B 2; main's scan of literal-only tests at c40446392 gives 92, 24 and 68.
  G  The six rows moved on 2026-11-13 each carry a dated note of that day; P-670's script and run are where the row
     says; the bang programme page has a wave, guards and seats; the draft plan is tracked at neither end; the
     builder's page holds card C15.
  P  With B1898 § 4's "15 of 15" turned into "16 of 16" in CHECKOUT, B1898's lock passes (it does not read § 4).
"""
import json, pathlib, re, subprocess, sys

W = pathlib.Path(sys.argv[1]).resolve()
C = pathlib.Path(sys.argv[2]).resolve()
B98 = W / "frontier" / "B1898_review_80_one_hundred_findings_and_what_main_checked"
OUT = {}


def git(*a):
    return subprocess.run(["git", "-C", str(C), *a], capture_output=True, text=True, check=True).stdout


def say(key, value):
    OUT[key] = value
    print("%-4s %s" % (key, json.dumps(value, ensure_ascii=False)))


def rows(text, first):
    return [l for l in text.split("\n") if l.startswith("| %s |" % first)]


# ---- A
f98 = (B98 / "FINDINGS.md").read_text(encoding="utf-8")
s57 = (B98 / "STATUS_OF_THE_57.md").read_text(encoding="utf-8")
a43 = (B98 / "ANSWERS_the_first_43.md").read_text(encoding="utf-8")
ver = json.loads((B98 / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
rec = json.loads((B98 / "verification" / "recount.json").read_text(encoding="utf-8"))
qx = json.loads((B98 / "verification" / "checks" / "quote_check_agyexp.json").read_text(encoding="utf-8"))
say("A1", {"B1898 § 4's agy-exp row holds '| 14 | 15 of 15 |'": any("| 14 | 15 of 15 |" in r for r in rows(f98, "agy-exp"))})
say("A2", {"recount: agy-exp: quotations found, of": rec["the outputs main kept"]["agy-exp: quotations found, of"]})
say("A3", {"second table's head holds 'and 14 of 14'": "and 14 of 14" in s57, "verdict line holds '14 of 14)'": "14 of 14)" in ver})
say("A4", {"kept check: findings": qx["summary"]["findings"], "lines of quotation": sum(r["lines of the quotation"] for r in qx["rows"])})

# ---- B
probe = json.loads((B98 / "verification" / "checks" / "sm_rows_probe.json").read_text(encoding="utf-8"))["SM-18"]
say("B1", {"row 18 names recount at e6298271a": any("recount at `e6298271a`" in r for r in rows(s57, "18")),
           "probe": probe})
for c in ("e6298271a", "896cae025"):
    names = git("ls-tree", "-r", "--name-only", c, "tests/").split("\n")
    say("B2", {"commit": c,
               "tests/test_*.py at the top": sum(1 for p in names if re.match(r"tests/test_[^/]*\.py$", p)),
               "tests/test_b*.py at the top": sum(1 for p in names if re.match(r"tests/test_b[^/]*\.py$", p)),
               "test_*.py under tests/ at any depth": sum(1 for p in names if re.search(r"/test_[^/]*\.py$", p))})
gates = (W / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
say("B3", {"the gates' anchor begins e6298271a": bool(re.search(r'NOTHING_LEAVES_FROM = "e6298271a', gates))})

# ---- C
reg = (W / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
p670 = rows(reg, "P-670")
run = next(W.glob("frontier/B1836_*/verification/main/p670_sheet_law_check_run.txt")).read_text(encoding="utf-8")
b36 = next(W.glob("frontier/B1836_*/FINDINGS.md")).read_text(encoding="utf-8")
say("C1", {"P-670 rows": len(p670), "holds 'within 5.8 × 10⁻³³'": "within 5.8 × 10⁻³³" in p670[0],
           "holds 'to 6 × 10⁻³¹'": "to 6 × 10⁻³¹" in p670[0]})
say("C2", {"kept run holds 5.775751444006791e-31": "5.775751444006791e-31" in run,
           "B1836's note holds 'by at most 5.8 × 10⁻³¹'": "by at most 5.8 × 10⁻³¹" in b36})

# ---- D
b92 = next(W.glob("frontier/B1892_*/FINDINGS.md")).read_text(encoding="utf-8").split("\n")
end = next(i for i, l in enumerate(b92) if l.startswith("| the governing pages | 3"))
start = end
while b92[start - 1].startswith("|"):
    start -= 1
sums = [0, 0, 0]
for l in b92[start + 2:end + 1]:
    c = [x.strip() for x in l.strip("|").split("|")]
    for k in range(3):
        sums[k] += int(re.match(r"\d+", c[k + 1]).group())
say("D1", {"B1892 § 5's table: rows": end - start - 1, "column sums": sums})
say("D2", {"B1892 holds 'the first reader has 52 findings, the second 43, and 9 are common'":
           "the first reader has 52 findings, the second 43, and 9 are common" in "\n".join(b92),
           "the governing pages' row holds 'the two columns sum to 53 and 43'": "the two columns sum to 53 and 43" in b92[end],
           "the second table's row 06 holds 'the table: 52, 43, 9 in common'": any("the table: 52, 43, 9 in common" in r for r in rows(s57, "06"))})

# ---- E
stems = sorted({p.stem for p in (B98 / "verification" / "checks").iterdir()})
say("E0", {"files in checks/, by stem": stems,
           "the second table's head holds \"The check's output is in `checks/`.\"": "The check's output is in `checks/`." in s57})
first = {}
for l in a43.split("\n"):
    m = re.match(r"\| (A\d+(?: to A\d+)?) \|", l)
    if m:
        cell = [x.strip() for x in l.strip("|").split(" | ")][3]
        first[m.group(1)] = cell
file_of_first = {"A5": "strict_recheck_r79_quotations", "A6": "plants_agy002", "A8": "literal_only_tests", "A9": "plants_agy002",
                 "A12": "plants_agy002", "A14": "plants_agy002", "A15": "plants_agy002", "A24 to A36": "builder_rows_probe"}
named_in_cell = {k: [s for s in stems if s in v] for k, v in first.items()}
say("E1", {"first table, agy-002's rows": len(first),
           "rows whose check cell names a file of checks/": sorted(k for k, v in named_in_cell.items() if v),
           "rows this seat matched to a file by what the file does": sorted(file_of_first),
           "rows with no file": sorted((k for k in first if k not in file_of_first), key=lambda k: int(k[1:].split()[0]))})
second = {}
for l in s57.split("\n"):
    m = re.match(r"\| (\d\d|F\d+) \|", l)
    if m:
        second[m.group(1)] = [x.strip() for x in l.strip("|").split(" | ")]
full = {k: v for k, v in second.items() if v[3] != "not checked" and not v[3].startswith("(a) the same as the web seat")
        and "not checked" not in v[3]}
same_as = {k: re.search(r"the same as agy-002's row (\d+)", v[3]) for k, v in full.items()}
in_probe = {k[3:] for k in json.loads((B98 / "verification" / "checks" / "sm_rows_probe.json").read_text(encoding="utf-8"))}
in_plants = {x["plant"].split(":")[0] for x in json.loads((B98 / "verification" / "checks" / "plants_b1881_third.json").read_text(encoding="utf-8"))}
with_file = sorted(k for k, v in full.items() if any(s in v[3] for s in stems) or k in in_probe or k in in_plants
                   or (same_as[k] and "A%s" % same_as[k].group(1) in file_of_first))
say("E2a", {"rows in sm_rows_probe.json": sorted(in_probe), "plants in plants_b1881_third.json": sorted(in_plants)})
say("E2", {"second table: rows checked in full": len(full), "of them, with a file of checks/ or a row of agy-002's that has one": with_file,
           "with none": sorted(k for k in full if k not in with_file)})
n_first = 13 + sum(1 for k in first if k != "A24 to A36")
n_first_file = 13 + sum(1 for k in file_of_first if k != "A24 to A36")
say("E3", {"findings checked in full, not this seat's": n_first + len(full),
           "with a file": n_first_file + len(with_file), "with none": (n_first - n_first_file) + (len(full) - len(with_file))})

# ---- F
old = set(l.split("/")[1] for l in git("ls-tree", "-d", "--name-only", "38d2a36dc", "frontier/").split("\n") if l)
ch = {}
for p in git("diff", "--name-only", "38d2a36dc", "0dda7b472", "--", "frontier/").split("\n"):
    if p.count("/") >= 2 and p.split("/")[1] in old:
        ch.setdefault(p.split("/")[1], []).append(p)
say("F1", {"Review 79's window: older arcs changed": len(ch),
           "in their verdict file or findings": sum(1 for v in ch.values() if any(re.search(r"/(arc_verdict\.json|FINDINGS\.md)$", p) for p in v))})
hl = json.loads(next(W.glob("frontier/B1880_*/verification/all_hash_lists.json")).read_text(encoding="utf-8"))["other_names_not_verifying"]
say("F2", {"B1880: class A": len(hl["class_A"]), "class B": len(hl["class_B"])})
lit = subprocess.run([sys.executable, str(B98 / "verification" / "checks" / "literal_only_tests.py"), "c40446392"],
                     capture_output=True, text=True, cwd=str(W)).stdout.split("\n")[0]
say("F3", {"main's scan, first line, numbers": [int(x) for x in re.findall(r"\d+", lit.split(":", 1)[1])]})

# ---- G
marks = {}
for p in ("P-239", "P-262", "P-263", "P-268", "P-670", "P-694"):
    r = rows(reg, p)
    marks[p] = {"rows": len(r), "ESCALATED(2026-11-13": "ESCALATED(2026-11-13" in r[0], "[2026-11-13:": "[2026-11-13:" in r[0],
                "DRAFT-DECLINED(2026-11-13": "DRAFT-DECLINED(2026-11-13" in r[0]}
say("G1", marks)
say("G2", {"P-670's script is there": bool(list(W.glob("frontier/B1836_*/verification/main/p670_sheet_law_check.py"))),
           "and its run": bool(list(W.glob("frontier/B1836_*/verification/main/p670_sheet_law_check_run.txt")))})
bang = (W / "docs" / "THE_BANG_PROGRAMME.md").read_text(encoding="utf-8")
say("G3", {"## Wave 1": "\n## Wave 1" in bang, "## Guards": "\n## Guards" in bang, "## Seats": "\n## Seats" in bang})
say("G4", {"audit/drafts/bang_programme_plan.md tracked at c40446392": "audit/drafts/bang_programme_plan.md" in git("ls-tree", "-r", "--name-only", "c40446392"),
           "or in the window": "audit/drafts/bang_programme_plan.md" in git("diff", "--name-only", "c40446392", "7d7ab1dfa")})
adv = (W / "docs" / "seats" / "cld-advisor.md").read_text(encoding="utf-8")
say("G5", {"the builder's page holds 'Card C15 (register row P-239, its next action)'": "Card C15 (register row P-239, its next action)" in adv})

# ---- P
target = B98 / "FINDINGS.md"
before = target.read_text(encoding="utf-8")
assert before.count("| 14 | 15 of 15 |") == 1
try:
    target.write_text(before.replace("| 14 | 15 of 15 |", "| 14 | 16 of 16 |"), encoding="utf-8")
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", str(B98 / "verification" / "test_b1898_review_80.py")],
                       capture_output=True, text=True, cwd=str(W))
    tail = [l for l in r.stdout.strip().split("\n") if l][-1]
    say("P1", {"plant": "B1898 § 4: '| 14 | 15 of 15 |' made '| 14 | 16 of 16 |'", "the lock's status": r.returncode,
               "its last line, numbers and words": re.sub(r" in [\d.]+s.*", "", tail)})
finally:
    subprocess.run(["git", "-C", str(W), "checkout", "--", str(target.relative_to(W))], check=True)
say("P2", {"the file is back as the window has it": target.read_text(encoding="utf-8") == before})
