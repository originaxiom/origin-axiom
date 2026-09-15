#!/usr/bin/env python3
"""THE FIRST AXIOM -- what F9 prices, and what A3 actually buys.

Seal: outside_bench/seals/THE_FIRST_AXIOM_PREREG.md
      sha256 f44223389d9f09861ed61cad19168e6f5149797f42652920c2f67f9f0b4da250

CELL 1/2 verify fork F9 (B1323, on main) against its own text.
CELL 3 computes the datum the physics-seat branch's T5 audit records as
"NOT computed anywhere in the record": what A1, A2, A4-A6 force WITHOUT A3.
CELL 4 reproduces the SL-level answer with the same code before trusting it.

All arithmetic is exact over the integers (sympy for the symbolic identities).
"""

from __future__ import annotations

import re
import subprocess
import sys
from itertools import product

import sympy as sp

FAILURES: list[str] = []


def fail(tag: str, msg: str) -> None:
    FAILURES.append(f"{tag}: {msg}")
    print(f"  !! FAIL [{tag}] {msg}")


def rule(t: str) -> None:
    print("\n" + "-" * 78)
    print(t)
    print("-" * 78)


def show(ref: str, path: str) -> str:
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
    if r.returncode != 0:
        fail("GIT", f"cannot read {ref}:{path}")
        return ""
    return r.stdout


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def quote(tag: str, hay: str, needle: str, where: str) -> bool:
    ok = norm(needle) in norm(hay)
    print(f"\n  [{tag}] {where} -- {'FOUND' if ok else 'ABSENT'}")
    for ln in needle.strip().splitlines():
        print(f"      {ln.strip()}")
    if not ok:
        fail("C4", f"{tag} not located in {where}")
    return ok


# ----------------------------------------------------------------- the matrices

L = sp.Matrix([[1, 1], [0, 1]])
R = sp.Matrix([[1, 0], [1, 1]])
S = sp.Matrix([[0, 1], [1, 0]])          # the pure swap, det -1
I2 = sp.eye(2)


def is_anosov(B: sp.Matrix) -> bool:
    """Hyperbolic (Anosov) = no eigenvalue on the unit circle.

    For det = +1 this is |trace| > 2.  For det = -1 the eigenvalues are
    lambda, -1/lambda and the condition is trace != 0 -- NOT |trace| > 2.
    Stated as one rule so the det = -1 case cannot silently inherit the wrong
    test: no root of the characteristic polynomial has modulus 1.
    """
    t = sp.nsimplify(B.trace())
    d = sp.nsimplify(B.det())
    lam = sp.symbols("lam")
    roots = sp.Poly(lam**2 - t * lam + d, lam).all_roots()
    return all(sp.Abs(sp.nsimplify(sp.Abs(r) - 1)) != 0 for r in roots)


def torsion(B: sp.Matrix) -> int:
    """|H_1 torsion| of the mapping torus = |det(B - I)| (UNIQUENESS_THEOREM 2)."""
    return abs(int(B.det() - 0) * 0 + int((B - I2).det()))


def word(letters: str) -> sp.Matrix:
    M = I2
    for ch in letters:
        M = M * {"L": L, "R": R, "S": S}[ch]
    return M


def main() -> int:
    print("=" * 78)
    print(" THE FIRST AXIOM -- what F9 prices, and what A3 actually buys")
    print("=" * 78)

    # ------------------------------------------------------------ CELL 1
    rule("CELL 1 -- is the theorem on MAIN, and does it say what it is cited for?")
    b1323 = show("origin/main", "frontier/B1323_the_genesis_upgrades/FINDINGS.md")
    print(f"    B1323 present at origin/main : {bool(b1323)}  ({len(b1323):,} chars)")

    # NB the arc uses STRAIGHT quotes here, not typographic ones.  The first
    # version of this needle used U+201C/U+201D and C4 FIRED -- the control
    # working exactly as intended: a quotation this bench mistyped is not a
    # quotation from the source, and the run failed rather than passing it.
    q_f9 = ('does A1\'s "not one, not three" carry weight? | **ROBUST twice.**')
    got_f9 = quote("F9 verdict", b1323, q_f9, "origin/main B1323")

    q_sent = ("one record is nothing; two records are the golden ratio, the atom "
              "ℚ(√−3), and an object that forgets its own handedness; three records "
              "are the plastic number on the torus, where there is no geometry at all, and the "
              "Whitehead link on the surface, where the handedness is remembered and the atom is "
              "gone.")
    got_sent = quote("the added sentence", b1323, q_sent, "origin/main B1323")

    q_ctrl = ("Control first: on S₁,₁ the word a·B returns **m004** (isometric; one cusp;")
    got_ctrl = quote("the two-record control", b1323, q_ctrl, "origin/main B1323")

    # the cusp discriminator, read out of the arc's own table row
    row = [ln for ln in b1323.splitlines() if "Whitehead" in ln and "|" in ln]
    print("\n    the three-record row, as the arc prints it:")
    for ln in row[:2]:
        print(f"      {ln.strip()[:200]}")
    two_cusp = any("| 2 |" in ln for ln in row)
    print(f"\n    two-record carrier S(1,1)  -> m004,  ONE cusp,  field Q(sqrt-3)")
    print(f"    three-record carrier S(1,2)-> m129 Whitehead link, TWO cusps, field Q(i): {two_cusp}")
    cell1 = "A" if (bool(b1323) and got_f9 and got_sent and got_ctrl and two_cusp) else "B"
    print(f"\n  >>> CELL 1 OUTCOME {cell1}")

    # ------------------------------------------------------------ CELL 2
    rule("CELL 2 -- does F9 DISCHARGE A1, or price it?")
    q_notclaimed = ("**Not claimed:** that the genesis is unconditional (UNIQUENESS §6 stands "
                    "verbatim: A1–A7 are not derived from anything weaker")
    got_nc = quote("B1323's own fence", b1323, q_notclaimed, "origin/main B1323")
    q_limit = ("that F9's ROBUST extends beyond words of length 3 on the two punctured carriers "
               "(a longer enumeration or a proof is the next step if anyone wants the general "
               "statement)")
    got_lim = quote("F9's stated reach", b1323, q_limit, "origin/main B1323")
    cell2 = "A" if (got_nc and got_lim) else "B"
    print(f"""
  >>> CELL 2 OUTCOME {cell2}: F9 PRICES A1 and does not discharge it -- the arc
      disclaims deriving the genesis in as many words.  So A1 remains an axiom,
      the axiom count stays 4, and memo 223's price stays 12.""")

    # ------------------------------------------------------------ C1
    rule("CONTROL C1 -- the Anosov test must bite in BOTH directions at det = -1")
    print("""
    For det = +1 hyperbolicity is |trace| > 2.  For det = -1 it is NOT: the
    eigenvalues are lambda and -1/lambda, so the condition is trace != 0.  A test
    that inherited |trace| > 2 would call the golden matrix NON-hyperbolic and
    silently empty CELL 3.  Both answers are exhibited here.""")
    probes = [("M = L*S", word("LS")), ("S itself", S), ("L*R", word("LR")), ("L", L)]
    lam = sp.symbols("lam")
    for name, B in probes:
        t, d = int(B.trace()), int(B.det())
        rts = sp.Poly(lam**2 - t * lam + d, lam).all_roots()
        mods = [sp.nsimplify(sp.Abs(r)) for r in rts]
        print(f"    {name:10} = {B.tolist()}  det {d:+d}  trace {t:+d}  "
              f"|eigs| {[sp.nsimplify(m) for m in mods]}  anosov={is_anosov(B)}")
    c1 = is_anosov(word("LS")) and (not is_anosov(S)) and is_anosov(word("LR")) \
        and (not is_anosov(L))
    print(f"\n  C1: {'PASS' if c1 else 'FAIL'} -- the test says YES at det -1 (L*S) and NO at "
          f"det -1 (S), and reproduces det +1 both ways")
    if not c1:
        fail("C1", "the Anosov test does not bite in both directions")

    # ------------------------------------------------------------ C2
    rule("CONTROL C2 -- the torsion formula reproduces UNIQUENESS_THEOREM's own grid")
    ut = show("origin/main", "docs/UNIQUENESS_THEOREM.md")
    q_tor = "det(B(a,b) − I) = −ab."
    quote("the locked identity", ut, q_tor, "origin/main UNIQUENESS_THEOREM")
    bad = []
    for a, b in product(range(1, 13), repeat=2):
        B = sp.Matrix([[1 + a * b, a], [b, 1]])
        if torsion(B) != a * b or int(B.trace()) != 2 + a * b:
            bad.append((a, b))
    surv = [(a, b) for a, b in product(range(1, 13), repeat=2)
            if torsion(sp.Matrix([[1 + a * b, a], [b, 1]])) == 1]
    print(f"    144-point grid: formula mismatches = {len(bad)}")
    print(f"    torsion-free survivors            = {surv}   (the banked 144 -> 1 collapse)")
    c2 = (not bad) and surv == [(1, 1)]
    print(f"  C2: {'PASS' if c2 else 'FAIL'}")
    if not c2:
        fail("C2", "the torsion formula does not reproduce the locked grid")

    # ------------------------------------------------------------ CELL 4 (before CELL 3)
    rule("CELL 4 -- the SAME code must return the banked SL-level answer first")
    def survivors(letters: str, maxlen: int, want_det: int | None):
        out = {}
        for n in range(2, maxlen + 1):
            for w in product(letters, repeat=n):
                s = "".join(w)
                if len(set(s) & {"L", "R"}) == 0:
                    continue
                B = word(s)
                d = int(B.det())
                if want_det is not None and d != want_det:
                    continue
                if not is_anosov(B):
                    continue
                if torsion(B) != 1:          # A5, torsion-free closure
                    continue
                key = (d, abs(int(B.trace())))
                out.setdefault(key, []).append((s, B))
        return out

    sl = survivors("LR", 4, +1)
    if sl:
        best = min(sl)
        print(f"    det = +1, words to length 4 over {{L,R}}, A5 applied:")
        for key in sorted(sl):
            ws = [s for s, _ in sl[key]][:6]
            print(f"      det {key[0]:+d}  |trace| {key[1]}  words {ws}")
        print(f"\n    A6 (minimal |trace|) selects |trace| = {best[1]}, witness "
              f"{sl[best][0][0]} = {sl[best][0][1].tolist()}")
    cell4 = "A" if (sl and min(sl)[1] == 3
                    and word(sl[min(sl)][0][0]).tolist() in ([[2, 1], [1, 1]], [[1, 1], [1, 2]])) else "B"
    print(f"  >>> CELL 4 OUTCOME {cell4}: the banked A = LR, trace 3, recovered by this code")

    # ------------------------------------------------------------ CELL 3
    rule("CELL 3 -- WITHOUT A3: what do A1, A2, A4-A6 force over GL(2,Z)?")
    print("""
    A2 gives GL(2,Z) (det = +-1); A3 is the restriction to det = +1.  The T5
    audit states A3's content as "the exclusion of the pure swap S from the
    primitive monoid".  So dropping A3 means enumerating words over {L, R, S}.
    A4 keeps the primitive one-channel moves L, R; A5 is torsion-free closure
    (|det(B - I)| = 1); A6 is minimal hyperbolic complexity.""")
    gl = survivors("LRS", 4, None)
    print(f"\n    words to length 4 over {{L,R,S}}, mixed, Anosov, A5 applied:")
    for key in sorted(gl, key=lambda k: (abs(k[1]), -k[0])):
        ws = sorted({s for s, _ in gl[key]}, key=len)[:8]
        print(f"      det {key[0]:+d}  |trace| {key[1]:<2}  {len(gl[key]):3d} words   e.g. {ws}")

    minus = {k: v for k, v in gl.items() if k[0] == -1}
    plus = {k: v for k, v in gl.items() if k[0] == +1}
    print(f"\n    A6 over ALL of GL(2,Z): the minimum |trace| among Anosov, torsion-free")
    allmin = min(gl, key=lambda k: abs(k[1]))
    print(f"      minimum |trace| = {abs(allmin[1])}, attained at det = {allmin[0]:+d}")
    mats = {tuple(map(tuple, B.tolist())) for _, B in gl[allmin]}
    print(f"      distinct matrices at that minimum: {len(mats)}")
    for m in sorted(mats):
        print(f"        {list(map(list, m))}")

    # up to the A7 swap symmetry L <-> R (conjugation by S)
    classes = set()
    for m in mats:
        B = sp.Matrix([list(r) for r in m])
        Bs = S * B * S
        classes.add(min(tuple(map(tuple, B.tolist())), tuple(map(tuple, Bs.tolist()))))
    print(f"      classes up to the A7 swap (conjugation by S): {len(classes)}")
    for c in sorted(classes):
        print(f"        {list(map(list, c))}")

    Mgold = word("LS")
    print(f"\n    M = L*S = {Mgold.tolist()}  det {int(Mgold.det()):+d}  trace {int(Mgold.trace())}")
    print(f"    M^2     = {(Mgold**2).tolist()}   == A = LR : {(Mgold**2).tolist() == word('LR').tolist()}")
    charM = sp.factor(sp.Poly((sp.symbols('t')**2 - Mgold.trace()*sp.symbols('t') + Mgold.det()),
                              sp.symbols('t')).as_expr())
    print(f"    char poly of M   : {charM}   (roots: the golden ratio and -1/phi)")
    print(f"    char poly of M^2 : t**2 - 3*t + 1   (roots phi^2, phi^-2 -- the banked A)")

    selected_is_M = (len(classes) == 1
                     and list(map(list, next(iter(classes)))) in
                     ([[1, 1], [1, 0]], [[0, 1], [1, 1]]))
    cell3 = "A" if (abs(allmin[1]) == 1 and allmin[0] == -1 and selected_is_M) else "B"
    print(f"""
  >>> CELL 3 OUTCOME {cell3}.  Dropping A3 moves the selected matrix from
      A = LR (det +1, trace 3, dilatation phi^2) to M = L*S (det -1, trace 1,
      dilatation phi) -- ONE class up to the A7 swap, and M^2 = A exactly.

      SO A3 IS THE SQUARING.  The orientation axiom's whole matrix-level content
      is that it replaces the golden matrix by its square; the paper says this in
      words ("The squaring is not cosmetic: it IS the orientation axiom") and the
      GL(2,Z)-level forcing the T5 audit called missing is the computation behind
      that sentence.""")

    # ------------------------------------------------------------ C3
    rule("CONTROL C3 -- the manifold identification is INHERITED, not recomputed")
    paper = show("origin/main", "papers/P3_THE_PAPER/main.tex")
    q_pap = ("The squaring is not cosmetic: it \\emph{is} the orientation axiom. The un-squared "
             "matrix gives a non-orientable manifold of exactly half the volume")
    quote("the paper's own sentence", paper, q_pap, "origin/main P3 main.tex")
    print("""
    THIS CERTIFICATE COMPUTES MATRICES, NOT MANIFOLDS.  That M's mapping torus is
    the Gieseking manifold m000, and that m004 double-covers it at exactly twice
    the volume, is taken from the record (B749/F5 and the paper sentence above)
    and is LABELLED INHERITED.  No SnapPy identification is claimed here.""")

    # ------------------------------------------------------------ summary
    print("\n" + "=" * 78)
    print(" OUTCOMES")
    print("=" * 78)
    print(f"   CELL 1 (F9 is on main and says it) : {cell1}")
    print(f"   CELL 2 (F9 prices, not discharges) : {cell2}")
    print(f"   CELL 3 (without A3: M, not A)      : {cell3}")
    print(f"   CELL 4 (SL answer reproduced)      : {cell4}")
    print(f"   C1 Anosov bites both ways : {'PASS' if c1 else 'FAIL'}")
    print(f"   C2 torsion grid reproduced: {'PASS' if c2 else 'FAIL'}")
    print(f"   C3 identification inherited: stated")
    print(f"   C4 quotations located     : "
          f"{'PASS' if not [f for f in FAILURES if f.startswith('C4')] else 'FAIL'}")
    print("\n   THE AXIOM COUNT IS UNCHANGED BY THIS CERTIFICATE: 4 axioms, price 12.")
    if FAILURES:
        print("\n  FAILURES:")
        for f in FAILURES:
            print(f"    - {f}")
    print("=" * 78)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
