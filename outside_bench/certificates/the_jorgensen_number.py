#!/usr/bin/env python3
"""THE JORGENSEN NUMBER -- the uniqueness theorem the owner named, verified exactly.

No seal: every claim is either (i) exact arithmetic in Z[zeta_6] recomputed here
from the object's own holonomy, or (ii) a string assertion against tracked files
at origin/main and the paper-verification branch, or (iii) a literature theorem
CITED and labelled as cited.

The point of the cell: J(m004) = 1 needs NO minimisation search.  At a pair whose
first element is parabolic the first Jorgensen term vanishes EXACTLY, so the
quantity equals |kappa - 2| -- and the record has banked |kappa - 2| = 1 for
hundreds of arcs under a different name.  One exact value plus a 1976 inequality
pins the number from both sides.
"""

from __future__ import annotations

import re
import subprocess
import sys

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
    return r.stdout if r.returncode == 0 else ""


def quote(tag: str, hay: str, needle: str, where: str) -> bool:
    ok = re.sub(r"\s+", " ", needle).strip() in re.sub(r"\s+", " ", hay)
    print(f"\n  [{tag}] {where} -- {'FOUND' if ok else 'ABSENT'}")
    for ln in needle.strip().splitlines():
        print(f"      {ln.strip()}")
    if not ok:
        fail("C-QUOTE", f"{tag} not located in {where}")
    return ok


# ---------------------------------------------------------------- exact holonomy

u = sp.exp(sp.I * sp.pi / 3)          # zeta_6, the Eisenstein point
u = sp.nsimplify(sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2)

A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [u, 1]])


def comm(X, Y):
    return sp.simplify(X * Y * X.inv() * Y.inv())


def jq(X, Y):
    """Jorgensen's quantity |tr^2 X - 4| + |tr[X,Y] - 2|."""
    t1 = sp.simplify(sp.Abs(sp.expand(sp.trace(X) ** 2 - 4)))
    t2 = sp.simplify(sp.Abs(sp.expand(sp.trace(comm(X, Y)) - 2)))
    return sp.nsimplify(sp.simplify(t1 + t2)), sp.nsimplify(t1), sp.nsimplify(t2)


def main() -> int:
    print("=" * 78)
    print(" THE JORGENSEN NUMBER -- verified exactly from the object's own holonomy")
    print("=" * 78)

    # ------------------------------------------------------------ the object
    rule("STEP 1 -- the holonomy, and the relator, exactly")
    print(f"    u = zeta_6 = {u},   u^2 - u + 1 = {sp.simplify(u**2 - u + 1)}")
    print(f"    rho(a) = {A.tolist()}   tr = {sp.trace(A)}  (PARABOLIC)")
    print(f"    rho(b) = {B.tolist()}   tr = {sp.trace(B)}  (PARABOLIC)")
    # the figure-eight relator in this presentation: a W b^-1 W^-1, W = bABa
    a, b = A, B
    Ai, Bi = A.inv(), B.inv()
    # W = bABa in the record's convention: lowercase = generator, UPPERCASE = INVERSE.
    # The first version read the capitals as generators and the relator did NOT
    # close -- the check caught a wrong word, which is exactly its job.
    W = b * Ai * Bi * a           # W = b a^-1 b^-1 a
    relN = sp.simplify(sp.expand(a * W * Bi * W.inv()))
    print(f"\n    W = b a^-1 b^-1 a = {sp.nsimplify(sp.simplify(W)).tolist()}")
    print(f"    relator a W b^-1 W^-1 = {sp.nsimplify(relN).tolist()}")
    plus = sp.simplify(relN - sp.eye(2)) == sp.zeros(2, 2)
    minus = sp.simplify(relN + sp.eye(2)) == sp.zeros(2, 2)
    rel_ok = plus or minus
    print(f"    relator = {'+I' if plus else ('-I' if minus else 'NEITHER')} in SL(2,C); "
          f"the identity in PSL(2,C): {rel_ok}")
    print("    (so <a,b> IS the figure-eight knot group and the upper bound applies)")
    if not rel_ok:
        fail("RELATOR", "the presentation does not close -- wrong holonomy")

    # ------------------------------------------------------------ kappa
    rule("STEP 2 -- kappa, and it is the record's OWN banked number")
    K = sp.simplify(sp.trace(comm(A, B)))
    print(f"    kappa = tr[a,b]           = {sp.nsimplify(K)}")
    print(f"    kappa - 2                 = {sp.nsimplify(sp.simplify(K - 2))}")
    print(f"    u^2                       = {sp.nsimplify(sp.expand(u**2))}")
    same = sp.simplify(K - 2 - u**2) == 0
    print(f"    kappa - 2 == u^2          : {same}")
    modv = sp.nsimplify(sp.simplify(sp.Abs(K - 2)))
    print(f"    |kappa - 2|               = {modv}")
    # u^2 is a primitive cube root of unity
    cube = sp.simplify(sp.expand((K - 2) ** 3) - 1) == 0
    prim = sp.simplify(sp.expand((K - 2) ** 2 + (K - 2) + 1)) == 0
    print(f"    (kappa-2)^3 = 1           : {cube}")
    print(f"    Phi_3(kappa-2) = 0        : {prim}   (a PRIMITIVE cube root of unity)")
    if not (same and modv == 1 and cube and prim):
        fail("KAPPA", "kappa - 2 is not the unit Eisenstein obstruction")

    # ------------------------------------------------------------ J
    rule("STEP 3 -- J(m004) = 1, PROVED from both sides, with NO search")
    q, t1, t2 = jq(A, B)
    print(f"    at the pair (a, b):")
    print(f"      |tr^2 a - 4|   = {t1}      <- EXACTLY zero, because a is parabolic")
    print(f"      |tr[a,b] - 2|  = {t2}")
    print(f"      Jorgensen's quantity = {q}")
    print(f"""
    UPPER BOUND: the pair (a, b) generates the group (relator verified above), so
      J(m004) <= {q}.
    LOWER BOUND, CITED not proved -- Jorgensen (1976): for every NON-ELEMENTARY
      DISCRETE <X,Y> < PSL(2,C),  |tr^2 X - 4| + |tr[X,Y] - 2| >= 1.
      The figure-eight group is discrete and non-elementary (it is a finite-volume
      Kleinian group), so J(m004) >= 1.

    >>> J(m004) = 1 EXACTLY.  No minimisation was run and none is needed:
        one exact value from the object's own holonomy, and a 1976 inequality.""")
    proved = (q == 1)
    if not proved:
        fail("J", f"the quantity at (a,b) is {q}, not 1")

    # ------------------------------------------------------------ C1
    rule("CONTROL C1 -- the quantity must be able to EXCEED 1 on this same group")
    print("""
    If every pair gave 1 the computation would be vacuous.  The bound is
    saturated only where the first term vanishes; a non-parabolic first element
    must push it above 1.""")
    probes = [("(ab, b)", A * B, B), ("(a, ab)", A, A * B), ("(ab, ba)", A * B, B * A),
              ("(a*a, b)", A * A, B)]
    vals = []
    for name, X, Y in probes:
        v, x1, x2 = jq(X, Y)
        vn = sp.N(v, 12)
        vals.append(vn)
        print(f"    {name:10}  |tr^2-4| = {sp.N(x1,8)!s:<14} |tr[.,.]-2| = {sp.N(x2,8)!s:<14} "
              f"total = {vn}")
    above = [v for v in vals if v > 1 + sp.Rational(1, 10**6)]
    c1 = len(above) > 0
    print(f"\n    pairs strictly above 1: {len(above)} of {len(vals)}")
    print(f"  C1: {'PASS' if c1 else 'FAIL'} -- the quantity is not identically 1")
    if not c1:
        fail("C1", "the Jorgensen quantity never exceeded 1; the cell is vacuous")

    # ------------------------------------------------------------ C2
    rule("CONTROL C2 -- the record banked this number under ANOTHER NAME, on main")
    hint = show("origin/main", "docs/HINT_LEDGER.md")
    # NB the ledger writes these WITHOUT spaces around "=".  The first version of
    # this needle added them and C-QUOTE fired -- the control doing its job.
    quote("the unit obstruction", hint,
          "κ−2=ω², |κ−2|=1 (unit obstruction)",
          "origin/main HINT_LEDGER H96")
    b1200 = show("origin/main", "frontier/B1200_one_polynomial/FINDINGS.md")
    quote("B1200's sentence", b1200,
          "the object sits at **|κ − 2| = 1**, the unit obstruction",
          "origin/main B1200")
    print("""
    So the value J(m004) = 1 has been in the record for hundreds of arcs as
    "THE UNIT OBSTRUCTION", and the record did not know it is the SATURATION of
    Jorgensen's 1976 discreteness bound.  That is an absence-under-another-name
    ACROSS the record/literature boundary rather than inside the record.""")

    # ------------------------------------------------------------ C3
    rule("CONTROL C3 -- the fibre/meridian collision: WHICH kappa saturates")
    print("""
    The branch arc B1344 flags a collision (its E72): there are two kappas.
    Only the MERIDIAN one saturates.  Checked here on the object's own data.""")
    print(f"    meridian kappa : kappa - 2 = {sp.nsimplify(sp.simplify(K-2))}, "
          f"|kappa - 2| = {modv}   -> saturates")
    print(f"    fibre kappa    : kappa = -2 (banked), |kappa - 2| = 4          "
          f"-> does NOT saturate")
    print("    A cell that took the fibre kappa would report 4 and miss the theorem.")

    # ------------------------------------------------------------ C4
    rule("CONTROL C4 -- the uniqueness theorem, CITED, with its hypothesis intact")
    BR = "origin/<remote>/paper-verification-ufp0zn"
    b1345 = show(BR, "frontier/B1345_the_jorgensen_number/FINDINGS.md")
    print(f"    B1345 present on {BR}: {bool(b1345)}")
    quote("Callahan's corollary", b1345,
          "Callahan (2009) Cor. 2.4 — the only **orientable** hyperbolic\n"
          "3-manifold with `J = 1` is the figure-eight complement — is cited, not re-proved.",
          f"{BR} B1345")
    quote("the slack table", b1345,
          "Nine of eleven reproduce exactly: m000 **1**, m004 **1**, m009 **√2**",
          f"{BR} B1345")
    print("""
    LOAD-BEARING, and this certificate does not prove it: the hypothesis is
    ORIENTABLE.  The branch's own slack table gives m000 -- the GIESEKING
    MANIFOLD, NON-orientable, the sibling the orientation axiom discards -- the
    same value J = 1.  So J = 1 does NOT single out m004 among hyperbolic
    3-manifolds; it singles it out among ORIENTABLE ones, and the orientation
    axiom is exactly what separates the two.

    B1345 and the m000 value are INHERITED from the branch arc and labelled as
    such: not recomputed here (m000's holonomy is not in PSL(2,C)).""")

    # ------------------------------------------------------------ summary
    print("\n" + "=" * 78)
    print(" WHAT IS ESTABLISHED HERE")
    print("=" * 78)
    print(f"   kappa - 2 = u^2, a primitive cube root of unity, |kappa - 2| = 1  : exact")
    print(f"   J(m004) = 1, from the pair (a,b) plus Jorgensen's inequality      : exact + cited")
    print(f"   the record banked this number as 'the unit obstruction'           : verified on main")
    print(f"   the uniqueness theorem needs ORIENTABLE, and m000 also has J = 1  : cited/inherited")
    print(f"   C1 non-vacuity : {'PASS' if c1 else 'FAIL'}")
    if FAILURES:
        print("\n  FAILURES:")
        for f in FAILURES:
            print(f"    - {f}")
    print("=" * 78)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
