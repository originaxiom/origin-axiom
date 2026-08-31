#!/usr/bin/env python3
"""S1 -- every external appeal in THE PAPER must point at a source, and every source must be used.

Found by the submission campaign's premise audit: the paper's bibliography was DECORATIVE. Twelve
of its thirteen \\bibitem entries were never \\cite'd. LaTeX prints an unused bibitem WITHOUT a
warning -- only an undefined \\cite warns -- so the build was clean and the document looked
referenced while no claim in the body pointed at any source.

Three checks, all of which can fail:
  (a) a named external result appearing in the prose with no \\cite nearby;
  (b) a \\bibitem nothing cites -- furniture, not a reference;
  (c) a \\cite key with no \\bibitem -- LaTeX warns on this one, but we check it here too.

    python3 scripts/checks/paper_citations.py            # the report
    python3 scripts/checks/paper_citations.py --selftest # MB12 bite control
"""
import io
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAPER = ROOT / "papers" / "P3_THE_PAPER" / "main.tex"
WINDOW = 260   # chars either side of a named appeal in which a \cite counts as attached

# Named external RESULTS the paper leans on -- an appeal that owes a source.
#
# Deliberately NOT here: names that function as standard TERMINOLOGY rather than as appeals --
# "Weyl data", "Galois", "Eisenstein", "Jordan algebra", "Coxeter number", "Sturmian". Citing
# those would be as odd as citing "abelian group", and a checker that demanded it would be
# training the author to add furniture. The distinction is the instrument's judgement and is
# stated here rather than buried: a name earns a row when the paper USES that result's content.
NAMED = ["Morse--Hedlund", "Hurwitz", "Thurston", "Riley", "McKay", "Mostow",
         "Borel--de~Siebenthal", "Dynkin", "Bala", "Krutelevich", "Mayer--Vietoris"]


def load():
    s = io.open(PAPER, encoding="utf-8").read()
    i = s.index("\\begin{document}")
    j = s.index("\\begin{thebibliography}") if "\\begin{thebibliography}" in s else len(s)
    return s, s[i:j]


def audit(s, body):
    keys = re.findall(r"\\bibitem\{([^}]*)\}", s)
    cited = set(k.strip() for m in re.findall(r"\\cite\{([^}]*)\}", body) for k in m.split(","))
    orphan_items = [k for k in keys if k not in cited]
    dangling = sorted(cited - set(keys))
    uncited_names = []
    for n in NAMED:
        for m in re.finditer(re.escape(n), body):
            w = body[max(0, m.start() - WINDOW):m.start() + WINDOW]
            if "\\cite" not in w:
                uncited_names.append(n)
            break
    return keys, sorted(set(cited)), orphan_items, dangling, uncited_names


def selftest():
    """MB12: plant both defect kinds and require both to be reported."""
    s, body = load()
    s2 = s.replace("\\end{thebibliography}",
                   "\\bibitem{plantedorphan} A source nothing points at.\n\\end{thebibliography}")
    body2 = body + "\n\nA claim resting on Krutelevich with no citation attached whatsoever.\n"
    body2 = body2.replace("\\cite", "\\XXcite")     # strip every real citation from the window
    _, _, orph, _, names = audit(s2, body2)
    got_orphan = "plantedorphan" in orph
    got_name = len(names) > 0
    print(f"PLANT uncited bibitem      reported: {got_orphan}")
    print(f"PLANT citation-free appeal reported: {got_name} ({len(names)} names)")
    ok = got_orphan and got_name
    print("CONTROLS", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    s, body = load()
    keys, cited, orphan_items, dangling, uncited_names = audit(s, body)
    print(f"bibitems: {len(keys)}   cited: {len(cited)}")
    print(f"\n(a) named appeals with NO citation within {WINDOW} chars: {len(uncited_names)}")
    for n in uncited_names:
        print(f"      {n}")
    print(f"\n(b) bibitems nothing cites (furniture): {len(orphan_items)}")
    for k in orphan_items:
        print(f"      {k}")
    print(f"\n(c) cite keys with no bibitem: {len(dangling)}")
    for k in dangling:
        print(f"      {k}")
    total = len(uncited_names) + len(orphan_items) + len(dangling)
    print(f"\nDEFECTS: {total}")
    sys.exit(0)
