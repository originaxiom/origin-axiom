#!/usr/bin/env python3
"""THE PAPER ALREADY HAD IT? -- verify the MEMO'S NOVELTY, not its quotations.

Sealed: outside_bench/seals/THE_PAPER_ALREADY_HAD_IT_PREREG.md
sha256 74591eb3a2a0007b4d90c451381ea9f11273a5c8aef4ea1de01df555bd939017 (committed 739b94c5).

memo 235's ADDENDA 1-3 reported three conclusions. This asks whether
papers/P3_THE_PAPER/main.tex -- in this working tree the whole time -- already
states them, and whether it carries B1427's census (banked on main TODAY).

OUTCOME A: all three present AND B1427's figures absent.
OUTCOME B: at least one conclusion absent -- named individually.

Controls: C1 a phrase the paper certainly has must be FOUND (else the search is
broken and no absence is evidence); C2 an invented phrase must be ABSENT;
C3 the numeral 976, which the paper does contain, must be shown to be a
BIBLIOGRAPHY YEAR and not B1427's count of firing modules -- a raw grep count is
not a finding until its hits are read.
"""
import re
import sys

PAPER = "papers/P3_THE_PAPER/main.tex"
TEXT = open(PAPER, encoding="utf-8").read()
FLAT = re.sub(r"\s+", " ", TEXT)


def has(needle):
    return re.sub(r"\s+", " ", needle) in FLAT


def line_of(needle):
    """The line where the needle STARTS.

    A needle may span a line break (K4 does), so a per-line scan returns nothing
    for it -- the first run of this cell printed `main.tex:None` beside a PRESENT
    verdict, which is a reporting defect, not a verdict defect. Fixed by locating
    the needle in the flattened text and mapping the offset back to a line, and
    by saying so when the match spans lines."""
    n = re.sub(r"\s+", " ", needle)
    pos = FLAT.find(n)
    if pos < 0:
        return None
    # map the flattened offset back: count tokens consumed.
    consumed, line = 0, 1
    for i, ln in enumerate(TEXT.split("\n"), 1):
        seg = re.sub(r"\s+", " ", ln).strip()
        step = len(seg) + (1 if seg else 0)
        if consumed + step > pos:
            line = i
            break
        consumed += step
    spans = n not in re.sub(r"\s+", " ", TEXT.split("\n")[line - 1])
    return f"{line}{' (spans lines)' if spans else ''}"


# The three conclusions the addenda reported, each as the paper's OWN words.
CONCLUSIONS = [
    ("K1  A6 -- the b_2 >= 2 condition for a symmetric triple",
     "the Z/3 = 2T/Q8 forcing b2 >= 2 for a symmetric triple"),
    ("K2  the no-seesaw exclusion of the apex design",
     "is excluded as it stands: it has no seesaw and a refuted tree-level flavour texture"),
    ("K3  the hollow texture, sigma_1 = sigma_2 + sigma_3",
     "the mass matrices are hollow (sigma\\_1 = sigma\\_2 + sigma\\_3"),
    ("K4  where three comes from, in the paper's own sentence",
     "three appears\nonly through the $\\Z/3$ descent, which is vector-like"),
]

# B1427's census figures (main, 2026-09-18). Several spellings each, because a
# LaTeX file may thin-space its thousands.
CENSUS = {
    "80 800 backgrounds": ["80\\,800", "80800", "80 800"],
    "12 800 generation-shaped backgrounds": ["12\\,800", "12800", "12 800"],
    "240 300 modules scanned": ["240\\,300", "240300", "240 300"],
    "89 non-split loci on Y_4": ["89 non-split", "89 loci"],
    "639 loci on Y_6": ["639 loci", "639 non-split"],
    "the level-7 reach": ["level 7", "level seven"],
    "'never two, never three'": ["never two, never three"],
}

print("=" * 78)
print(" THE PAPER ALREADY HAD IT?  --  memo 235's NOVELTY, measured")
print("=" * 78)
print(f"  source: {PAPER}   ({len(TEXT.split(chr(10)))} lines)")
print()
print("-" * 78)
print(" PART 1 -- the three conclusions the addenda reported")
print("-" * 78)
present = []
for tag, needle in CONCLUSIONS:
    ok = has(needle)
    ln = line_of(needle)
    print(f"  [{'PRESENT' if ok else 'ABSENT ':7s}] {tag}")
    if ok:
        print(f"              main.tex:{ln}")
    present.append(ok)

print()
print("-" * 78)
print(" PART 2 -- B1427's census, banked on MAIN TODAY (2026-09-18)")
print("-" * 78)
census_hits = []
for label, spellings in CENSUS.items():
    hit = [s for s in spellings if has(s)]
    print(f"  [{'PRESENT' if hit else 'ABSENT ':7s}] {label:42s} tried: {spellings}")
    if hit:
        census_hits.append((label, hit))

print()
print("-" * 78)
print(" PART 3 -- WHY THIS BENCH KEPT MISSING IT: the surfaces the pre-flight reads")
print("-" * 78)
AB = "scripts/checks/already_banked.py"
ab_src = open(AB, encoding="utf-8").read()
globs = sorted(set(re.findall(r"ROOT\s*/\s*[\"\']([^\"\']+)[\"\']|ROOT\.glob\([\"\']([^\"\']+)[\"\']\)", ab_src)))
globs = sorted({a or b for a, b in globs})
print(f"  {AB} reads, by its own source:")
for g in globs:
    print(f"      {g}")
reads_papers = any(g.startswith("papers") for g in globs)
print(f"  [{'FAIL' if reads_papers else 'CONFIRMED'}] the pre-flight NEVER READS papers/ -- "
      f"so the programme's most consolidated")
print("              statement is invisible to the instrument that exists to stop this bench")
print("              from calling a thing missing. That is an INSTRUMENT GAP, not a lapse of")
print("              attention, and it is computed here from the script's own source.")

print()
print("-" * 78)
print(" CONTROLS")
print("-" * 78)
c1_needle = "Generation counting needs \\emph{net} chirality"
c1 = has(c1_needle)
print(f"  [{'PASS' if c1 else 'FAIL'}] C1 POSITIVE -- a phrase the paper certainly has is FOUND "
      f"(main.tex:{line_of(c1_needle)})")

c2_needle = "the compact curved closing is constructed in this paper"
c2 = not has(c2_needle)
print(f"  [{'PASS' if c2 else 'FAIL'}] C2 NEGATIVE -- an invented phrase is ABSENT")

# C3 -- read the 976 hits instead of counting them.
hits_976 = [(i, ln.strip()) for i, ln in enumerate(TEXT.split("\n"), 1) if "976" in ln]
print(f"  C3 DISAMBIGUATION -- {len(hits_976)} line(s) contain '976':")
for i, ln in hits_976:
    print(f"      main.tex:{i}  {ln[:96]}")
c3 = bool(hits_976) and all(re.search(r"\\bibitem|\(19\d\d\)", ln) for _, ln in hits_976)
print(f"  [{'PASS' if c3 else 'FAIL'}] C3 -- every '976' is a BIBLIOGRAPHY YEAR, "
      f"not B1427's count of firing modules")

print()
print("=" * 78)
outcome = "A" if (all(present) and not census_hits) else "B"
print(f" OUTCOME {outcome}")
if outcome == "A":
    print(" The paper ALREADY STATES all of memo 235's reported conclusions, in its own")
    print(" words, and does NOT carry B1427's census. So the addenda were NEW TO THIS")
    print(" BENCH, NOT TO THE RECORD -- and the single relay is the dated count.")
else:
    for (tag, _), ok in zip(CONCLUSIONS, present):
        if not ok:
            print(f"   ABSENT from the paper, so genuinely added: {tag}")
    if census_hits:
        print(f"   and the paper already carries: {census_hits}")
controls = [c1, c2, c3]
print(f" CONTROLS: {sum(controls)}/3 PASS")
print("=" * 78)
print(" FENCE (sealed before the run): this measures WHAT THE PAPER SAYS, never")
print(" whether it is right. No claim about the mathematics. No value.")
print(" I-26 UNEARNED. Gate 5 untouched.")
sys.exit(0 if all(controls) else 1)
