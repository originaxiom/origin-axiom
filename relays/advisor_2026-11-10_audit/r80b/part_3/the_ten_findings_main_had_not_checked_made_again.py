#!/usr/bin/env python3
"""The ten findings of part 3 that main's table gives as not checked, each made again on the tree before the part.

    python3 the_ten_findings_main_had_not_checked_made_again.py <a checkout of the commit before part 3>

It reads files, imports three of the tree's own modules and counts.  It changes nothing.  The findings are the web seat's 8
and 9, the SM seat's 26, 32, 33 and 41, and a reader's F6 (its second part), F11, F13 and F14, as main's table gives them."""
import importlib.util, json, pathlib, re, sys
root = pathlib.Path(sys.argv[1]); F = root / "frontier"
arc = lambda b: next(F.glob(b + "_*"))
read = lambda p: pathlib.Path(p).read_text(encoding="utf-8")
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

print("1. The web seat's 8: the closing paragraph of B732 gives the level as (8) with no correction beside it")
p = read(arc("B732") / "FINDINGS.md"); last = p.rstrip().split("\n\n")[-1]
print("   the closing paragraph says it: %s; holds a correction: %s; the page carries the correction elsewhere: %s"
      % ("IS congruence at level (2)^3=(8)" in last, "CORRECTED" in last, "the congruence level is (4)" in p.replace(last, "")))

print("2. The web seat's 9: the dated note of B942's page does not say in which group the image has its order")
p = read(arc("B942") / "FINDINGS.md"); note = [l for l in p.split("\n") if l.startswith("> *Dated note 2026-11-11")][0]
line = json.loads(read(arc("B942") / "arc_verdict.json"))["claim_one_line"]
print("   the note ends with the sentence quoted: %s; it names the quotient by every central unit for that order: %s; the verdict line does: %s"
      % (note.endswith("the image order it quotes is the image's at (8) and is not changed."), "2560" in note, "2560 is the image's order in the quotient at (8) by every central unit of square one" in line))

print("3. The SM seat's 26: B874's verdict line opens 'exact over Q', and what its bracket gives as computed in B892 is in double precision")
line = json.loads(read(arc("B874") / "arc_verdict.json"))["claim_one_line"]; s = read(arc("B892") / "verification" / "walls_on_the_line.py")
print("   the line opens so: %s; the bracket says anything of precision: %s" % (line.startswith("The measurement ladder, exact over Q"), "double precision" in line))
print("   B892's script: numerical eigenvectors: %s; a rank from singular values: %s; its docstring says the basis is not the same from run to run: %s"
      % ("np.linalg.eig(" in s, "np.linalg.svd(" in s, "it is not the same from run to run" in " ".join(s.split())))

print("4. The SM seat's 32: main's message of 2026-11-11 to the web seat")
m = read(root / "docs" / "handoffs" / "CC_TO_CHAT1_2026-11-11_YOUR_TWO_RELAYS_VERIFIED.md")
print("   says 'reproduced': %s; gives the second convention as B1872's: %s; lists the agreement under 'Three additions': %s; carries a note: %s"
      % ("is reproduced by main's own code" in m, "B1872's (columns, v = (1, 2))" in m, "## 3. Three additions" in m and "**One allowed set in the two conventions.**" in m, "NOTE 2026-11-12" in m))

print("5. The SM seat's 33: B1882's lock asks only for the day within 120 characters after an old phrase of the verdict line")
t = read(next((arc("B1882") / "verification").glob("test_*.py")))
print("   the lock's line stands: %s" % ('assert "2026-11-12" in line[i:i + len(old) + 120], old' in t))
line = json.loads(read(arc("B1882") / "arc_verdict.json"))["claim_one_line"]
for old in ("THE AUDIT'S FIGURE IS REPRODUCED AND IS NOT ABOUT RARITY", "a lower bottom end almost none"):
    i = line.index(old) + len(old); bare = line[:i] + " [see the note of 2026-11-12]" + line[line.index("]", i) + 1:]
    j = bare.index(old)
    print("   with the bracket after %r replaced by a bare mention of the day, the lock's line passes: %s" % (old[:28] + "...", "2026-11-12" in bare[j:j + len(old) + 120]))

print("6. The SM seat's 41: the test of B874's bracket asks for four labels")
old = "the complete ladder is {78, 46, 30, 12}"; after = json.loads(read(arc("B874") / "arc_verdict.json"))["claim_one_line"]; after = after[after.index(old):]
asks = lambda a: "SCOPED 2026-11-12" in a[:400] and "COMPUTED ON MAIN (B892)" in a and "BY THE AUDIT SEAT'S RELAY" in a and "locks not imported" in a
for false, where in (("all real, to 16 and to 26", "all imaginary, to 14 and to 18"), ("so on the real line it reaches 26", "so on the real line it is 12 at every point but the plane stratum's")):
    print("   with %r planted in the bracket, what the test asks passes: %s" % (false, where in after and asks(after.replace(where, false))))

print("7. A reader's F6, second part: B1891's lock does not compare the set of rows of the status tables, nor a row with no spaces at its bars")
b = arc("B1886") / "verification"; bs = load("bs", b / "build_status_cells.py"); snap = json.loads(read(b / "status_cells.json"))["v1.65"]; G = read(root / "GENESIS.md")
def compares(text):
    now_id, now_tab = bs.identifier_rows(text), bs.status_table_rows(text)
    for kind, now in (("identifier_rows", now_id), ("status_table_rows", now_tab)):
        if sorted(set(snap[kind]) - set(now)) or {k for k in snap[kind] if k in now and snap[kind][k] != now[k]}:
            return False
    return set(now_id) == set(snap["identifier_rows"])
at = G.index("\n| PF1 ") + 1
for what, row in (("a row with no identifier added to a status table", "| a new face | planted | planted words | DERIVED |\n"), ("a row with an identifier and no spaces at its bars", "|PF9|planted|planted words|DERIVED|\n")):
    print("   %s: the lock's comparisons pass: %s" % (what, compares(G[:at] + row + G[at:])))

print("8. A reader's F11: B862's function answers a grid with no point with an empty kernel")
gf = load("gf", arc("B862") / "global_form.py")
for g in (0, -6, -12):
    try: print("   a grid of %3d: %d element(s), nothing raised" % (g, len(gf.kernel_exact(g))))
    except Exception as e: print("   a grid of %3d: refused (%s)" % (g, type(e).__name__))

print("9. A reader's F13: the correction on B1222's page is an item of its own, and the sweep of B1028's test reads a tight list as one unit")
p = read(arc("B1222") / "FINDINGS.md").split("\n")
i = [k for k, l in enumerate(p) if l.startswith("- [CORRECTED 2026-11-11 (the audit's finding E7)")]
print("   the correction opens an item of its own: %s; the next item states the zero: %s" % (len(i) == 1, bool(i) and p[i[0] + 1].startswith("- **designer freedom 0.000 bits**")))
t = read(root / "tests" / "test_b1028_freedom_ledger.py")
print("   the sweep joins a paragraph's lines into one unit: %s" % ('prose = " ".join(l for l in para.split("\\n") if not l.lstrip().startswith("|"))' in t))

print("10. A reader's F14: the sweep of B734's test reads one field of a verdict file, and its neighbour reads three")
a, b = read(root / "tests" / "test_b734_m004_congruence.py"), read(root / "tests" / "test_b1028_freedom_ledger.py")
print("   B734's: %s; B1028's: %s" % ('text = json.loads(text).get("claim_one_line", "")' in a, 'for k in ("claim_one_line", "scope", "note")' in b))
