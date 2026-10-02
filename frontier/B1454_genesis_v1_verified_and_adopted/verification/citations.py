#!/usr/bin/env python3
"""B1454 -- every place GENESIS cites a record of main's, checked against that record's own files.

    python3 citations.py        # prints the table, writes citations.json; exit 1 if a citation is not found

Each row: what GENESIS says, the files of main it cites, and an expression that must match in them.  The expression
is the cited content (a number, a phrase), not the arc's id, so a row can fail.  Two controls at the end are rows that
must NOT match.
"""
import glob, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

ROWS = [
 # (GENESIS item, what it says, files, expression)
 ("GM1", "the two routes are not independent: Z^2 is the punctured torus's H1 (B1422)", ["frontier/B1422_*/FINDINGS.md"], r"A1's ℤ² is the punctured torus's H₁"),
 ("GM1", "fork F9 robust at depth three, fragile past it (B749 addendum; B1323; B1414)", ["frontier/B749_*/FINDINGS.md"], r"true at the depth B1323 enumerated and false past it"),
 ("GM3", "every periodic alternative is degenerate (B749 F2 ROBUST)", ["frontier/B749_*/FINDINGS.md"], r"F2 periodicity \| ROBUST"),
 ("GM4", "the anatomy needs geometry (B749 F8)", ["frontier/B749_*/arc_verdict.json"], r"F8 geometry-necessary"),
 ("GM4", "the prices locked: two fragile forks, orientation and the puncture (B1003)", ["frontier/B1003_*/arc_verdict.json"], r"FRAGILE are F5 \(A6, orientation\) and F6 \(A5b, the punc"),
 ("GM5c", "the record swap is an added axiom (B1422)", ["frontier/B1422_*/FINDINGS.md"], r"The record swap is an added axiom"),
 ("GM5c", "LP the unique GL(2,Z) square root of A up to sign; a = b (B14)", ["frontier/B14_*/arc_verdict.json"], r"unique GL\(2,Z\) square root of A up to sign.*iff a=b"),
 ("GM5c", "P unique up to sign, forced by (LX)^2 = A and not by the axioms (B16)", ["frontier/B16_*/arc_verdict.json"], r"forced by \(LX\)\^2=A but not by axioms A1-A6"),
 ("GM5c", "three exchange conditions give exactly +-P (B19)", ["frontier/B19_*/arc_verdict.json"], r"exactly plus/minus P"),
 ("GM5c", "every metallic bundle double-covers a non-orientable one (B469)", ["frontier/B469_*/arc_verdict.json"], r"every metallic bundle double-covers a non-orientable bundle"),
 ("GM5c", "the founding torsor's two bits are the swap and the reversal (B1083)", ["frontier/B1083_*/arc_verdict.json"], r"two bits are C \(swap\) and P \(reversal\)"),
 ("§3", "758 states; 95 carry a background at their own level (B1439)", ["frontier/B1439_*/arc_verdict.json"], r"758 states.*95 of the 758 states"),
 ("§3", "the 13 members with a non-integral trace: 99 in the class (B1453)", ["frontier/B1453_*/arc_verdict.json"], r"99 are in m004's commensurability class"),
 ("§3", "A7 is load-bearing at the based level, one bit (B979)", ["frontier/B979_*/arc_verdict.json"], r"A7 IS LOAD-BEARING.*BASED invariant"),
 ("§3", "(LP)^2 = LR, (PL)^2 = RL: the swap's placement inside the tick (B1323)", ["frontier/B1323_*/FINDINGS.md"], r"A7 is the placement of the swap inside the single tick"),
 ("SE1", "the m003 volume tie is broken by torsion (B197)", ["frontier/B197_*/arc_verdict.json"], r"m003 volume tie is broken by torsion"),
 ("T-ROOT", "trace 3 is the unique torsion-free hyperbolic trace (CLAIMS C3)", ["CLAIMS.md"], r"\| C3 \| Trace 3 is the unique torsion-free hyperbolic trace"),
 ("SE2", "the det -1 sibling is the Gieseking; F5 FRAGILE (B749)", ["frontier/B749_*/arc_verdict.json"], r"F5 and F6 FRAGILE \(the det −1 sibling is the Gieseking"),
 ("SE2", "the walls trace to orientation: 40 of 40 against 6 of 200; 48 surjections (B1234)", ["frontier/B1234_*/arc_verdict.json"], r"40 OF 40 AMPHICHIRAL.*6 OF 200.*48 SURJECTIONS"),
 ("§4", "the forcing is over-determined; a consistency demonstration (B1422)", ["frontier/B1422_*/FINDINGS.md"], r"over-determined\s+rather\s+than\s+tight.*consistency\s+demonstration"),
 ("§4", "the quotation of B1434, as B1434 has it", ["frontier/B1434_*/FINDINGS.md"], r"The root has none and cannot:\s+its\s+fibre\s+has\s+no\s+finite\s+character\."),
 ("§4", "the object preceded the axioms: the 22nd and the 28th (B1422)", ["frontier/B1422_*/FINDINGS.md"], r"naming\s+the\s+figure-eight\s+to\s+the\s+22nd,\s+while\s+the\s+axioms\s+were\s+committed\s+on\s+the\s+28th"),
 ("§4", "the two routes are one construction (B1323)", ["frontier/B1323_*/FINDINGS.md"], r"one construction in two presentations"),
 ("§4", "m free; m = 1 selected only by the systole (B92)", ["frontier/B92_*/arc_verdict.json"], r"m=1 selected only by the systole"),
 ("§4", "arithmeticity selects m = 1 and m = 2 (B125)", ["frontier/B125_*/arc_verdict.json"], r"selects m=1 \(Q\(sqrt-3\)\) and m=2 \(Q\(i\)\)"),
 ("§4", "the unique unitary anyon; the unique superconformal chain (B218, B224)", ["frontier/B218_*/arc_verdict.json", "frontier/B224_*/arc_verdict.json"], r"unique metallic mean"),
 ("§4", "H1(M_m) = Z + (Z/m)^2; only m = 1 a knot complement (B251, B126)", ["frontier/B251_*/arc_verdict.json"], r"forces only m=1 to be a knot complement"),
 ("§4", "P000: m = 1 most-selected, not forced; the family the intended shape", ["philosophy/P000_what_is_not_nothing.md"], r"would be the suspicious outcome.*most-selected"),
 ("§1", "existence as a frustrated cancellation (GOVERNANCE §1)", ["GOVERNANCE.md"], r"existence as a frustrated cancellation"),
 ("§1", "A0, unpriceable (the P3 paper)", ["papers/P3_THE_PAPER/main.tex"], r"A0 --- unpriceable"),
 ("§1", "non-cancellation is the Fricke-Vogt invariant (P008)", ["philosophy/P008_*.md"], r"Non-cancellation is the positivity of the Fricke–Vogt invariant"),
 ("§1", "kappa = 4 I_FV + 2 (B148); kappa = 2 the one positive-measure fibre (B162)", ["frontier/B148_*/arc_verdict.json", "frontier/B162_*/arc_verdict.json"], r"kappa = 4\*I_FV \+ 2|unique fiber with positive-measure spectrum"),
 ("§1", "kappa names two quantities (ERROR_LEDGER E72)", ["docs/ERROR_LEDGER.md"], r"E72 the ONE-SYMBOL-TWO-QUANTITIES class.*κ = tr\[a,b\]"),
 ("F-CI", "M3 to M6 carry 48, 256, 400, 2 160 (B1432)", ["frontier/B1432_*/FINDINGS.md"], r"2 160 backgrounds, every count ±1"),
 ("F-CI", "m369 (8) and s639 (16) at their own level; m010 none at its three-fold level (B1434)", ["frontier/B1434_*/FINDINGS.md"], r"m369, chiral.*\*\*8\*\*.*s639, chiral.*\*\*16\*\*.*m010 \| \*\*0\*\*"),
 ("F-CI", "the five firing members (B1418)", ["frontier/B1418_*/arc_verdict.json"], r"s958.*v2873.*t12833.*t12835.*o10_150701"),
 ("F-MC", "the claim on one page, with its counted hypotheses (THE_CLAIM; B1014)", ["docs/THE_CLAIM.md"], r"Hypotheses \(the counted input list\).*plus \*\*five\*\* typed external data"),
 ("F-MC", "reaching E6 is generic at about 1 in 3 (B993)", ["frontier/B993_*/arc_verdict.json"], r"GENERIC AT ROUGHLY 1 IN 3"),
 ("F-MC", "the golden is the unique metallic grammar with a McKay shadow (B997)", ["frontier/B997_*/arc_verdict.json"], r"UNIQUE METALLIC GRAMMAR WHOSE OWN-CONDUCTOR SHADOW IS A McKAY GROUP"),
 ("F-MC", "the siblings have no door (B1019)", ["frontier/B1019_*/arc_verdict.json"], r"THE SIBLINGS HAVE NO DOOR"),
 ("F-MC", "39 of 43 links forced (B1123); eleven irreducible inputs (B1266)", ["frontier/B1123_*/arc_verdict.json", "frontier/B1266_*/arc_verdict.json"], r"FORCED \(non-axiom\) 39 of 43|THE IRREDUCIBLE NUMBER IS 11"),
 ("GAP5", "the dynamics and chirality sweep: neither is missing (B944); no intrinsic time (B721)", ["frontier/B944_*/arc_verdict.json"], r"NEITHER IS MISSING.*dynamics, not intrinsic time"),
 ("GAP5", "the action exists exactly at the monodromy (B1341); the parameter-free action card (B1088)", ["frontier/B1341_*/arc_verdict.json", "frontier/B1088_*/arc_verdict.json"], r"ACTION EXISTS EXACTLY AT ITS MONODROMY|ZERO free dimensionless constants"),
 ("§8", "the path registry: 18 never touched (B1422)", ["frontier/B1422_*/arc_verdict.json"], r"18 untouched"),
 ("§8", "L229 (iii) and (iv)", ["docs/OPEN_LEADS.md"], r"## L229.*\(iii\) \*\*The frame off the root's field\.\*\*.*\(iv\) \*\*What singles out"),
]
CONTROLS = [  # must not match: the v1.0 wording of the quotation, and a count main's arc does not give
 ("control", "v1.0's wording of the quotation is not B1434's", ["frontier/B1434_*/FINDINGS.md"], r"cannot, since its fibre"),
 ("control", "main's B1422 does not say seventeen untouched", ["frontier/B1422_*/arc_verdict.json"], r"17 untouched"),
]


def found(files, rx):
    pat = re.compile(rx, re.S)
    for g in files:
        for f in sorted(glob.glob(os.path.join(ROOT, g))):
            if pat.search(open(f, errors="replace").read()): return os.path.relpath(f, ROOT)
    return None


def registry():
    c = {}
    for line in open(os.path.join(ROOT, "paths", "PATHS.md")):
        m = re.match(r"\| \*\*([A-Z])(\d+)\*\* \|[^|]*\|[^|]*\| \**([A-Z-]+)", line)
        if m and not (m.group(1) == "E" and int(m.group(2)) > 20):          # E21+ are instantiations, not enumerated paths
            c[m.group(3)] = c.get(m.group(3), 0) + 1
    return c


def main():
    out = []; ok = True
    for item, says, files, rx in ROWS:
        f = found(files, rx); ok &= f is not None
        out.append(dict(item=item, says=says, found_in=f)); print("%-7s %-5s %s" % (item, "ok" if f else "FAIL", says))
    for item, says, files, rx in CONTROLS:
        f = found(files, rx); ok &= f is None
        out.append(dict(item=item, says=says, absent=f is None)); print("%-7s %-5s %s" % (item, "ok" if f is None else "FAIL", says))
    reg = registry(); print("path registry:", reg)
    ok &= reg == {"DEAD": 1, "IN-PROGRESS": 3, "STALLED": 3, "UNTOUCHED": 18} and sum(reg.values()) == 25
    json.dump(dict(rows=out, path_registry=reg), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "citations.json"), "w"), indent=1, ensure_ascii=False)
    print("VERDICT genesis-citations: %s (%d citations, %d controls)" % ("PASS" if ok else "FAIL", len(ROWS), len(CONTROLS)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
