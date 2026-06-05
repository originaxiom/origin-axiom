"""B89-T (Task T) -- the metallic tower's cohomological route is closed; the explicit Sym-module
reduction (symbolic in m).

GOAL of Task T (the CC-web handoff capstone): prove the tower char(J(m)) = the Dickson catalog for ALL
n -- upgrade B62's "structural n=5,6" to "PROVED all n" -- via the cohomological / root-height route
(J(m) = the once-punctured-torus monodromy M_m on H^1(F_2; ad rho), graded by root height).

RESULT, honest: the cohomological route is FORECLOSED (a third dead shortcut, after B84's numerics and
B85's Lambda^2 V). But pushing on the genuine remaining gap (B85's Procesi assembly) yields a concrete
advance: an EXPLICIT closed-form for the all-n tower (a two-sequence symmetric-power product), verified
SYMBOLICALLY IN m to equal the proved tower at n=3,4 and the structural tower at n=5 -- strengthening
B58's m=1-only check -- which reduces the all-n proof to one clean module-isomorphism.

-----------------------------------------------------------------------------------------------------
(1) THE COHOMOLOGICAL ROUTE FAILS (C1).  The handoff's premise was J(m) = action of the monodromy on
    H^1(F_2; ad rho).  But the metallic trace-map fixed line is "all traces = n", i.e. the TRIVIAL
    representation (first-order degenerate: d tr(W)=0 for every word -- B58 FINDINGS).  There
        H^1(F_2; ad triv) = Hom(F_2^ab, sl(n)) = sl(n) (+) sl(n),   phi_m acts = M_m (x) id_sl(n),
    so its char poly is char(M)^(n^2-1) -- ALL char(M), NO higher powers -- not the tower (which has
    char(M^2), char(M^3), char(M^4), char(-M^2), ...).  The tower-carrying object is the TRACE-COORDINATE
    Jacobian (a Procesi/trace-ring object), NOT a representation linearization.  The two cohomological
    repairs are already refuted: principal-SL(2)/Kostant sl(n)=(+)Sym^{2k} is even-powers-only (misses
    char(M),char(M^3)), and the H^1(F_2)=C^2 coupling was killed from the multiplicity side
    (B58 Stage 1 = V27 kill #25).  So the cohomological route does not reach the tower.

(2) THE EXPLICIT Sym-MODULE REDUCTION (the advance).  Each Sym^d(M) factors over the Dickson catalog in
    BOTH parities (Sym^3 = char(M^-1)char(M^3), Sym^4 = (t-1)char(-M^2)char(M^4), ...).  The all-n tower
    equals the explicit two-sequence symmetric-power product
        char(J(m))  =  prod_{d=2}^{n} char(Sym^d M_m)  *  prod_{d=0}^{n-3} char(Sym^d M_m)         (T)
    with M_m=[[m,1],[1,0]].  Verified here SYMBOLICALLY IN m: (T) equals the PROVED tower (B80/B65) at
    n=3,4 and the STRUCTURAL tower (B62) at n=5 -- B58 had only checked m=1 (the Fibonacci det=-1 case).
    Degrees: 3+...+(n+1) plus 0+...+(n-2) = n^2-1, exactly.  This converts B85's "assemble the symbolic
    trace map sigma" into a concrete target: the all-n tower is now ONE module-isomorphism conjecture --
        J(m)  ~=  M_m acting on  [ (+)_{d=2}^{n} Sym^d C^2 ]  (+)  [ (+)_{d=0}^{n-3} Sym^d C^2 ]        (M)
    over the mapping-class SL(2) (M_m on H_1(F_2)=C^2).  (M) is PROVED for n<=4 (it equals B80's tower)
    and matches B62 at n=5; the derivation of (M) for all n -- WHY J(m) is this Sym module -- is the lone
    open item (the Procesi structure, B58 Gate 1).

(3) THE n=6 DISCRIMINATOR.  (T) predicts the multiplicity of char(M^3) at n=6 is a_3 = 2 -- AGREEING with
    the independent opposition-involution theta-split (B62) and CONTRADICTING only B66's pinv a_3 = 1,
    which B84 showed is gauge-corrupted at exactly this doubly-degenerate sector.  So the open n=6 row is
    now corroborated 2-of-3 toward a_3 = 2, the lone dissent being the known-bad numerics.

Labels: (1) rigorous route-closure; (T) at n<=4 is PROVED-consistent (= the proved tower, symbolic m),
at n=5 matches structural; (M) for all n is CONJECTURED (the derivation is open); (3) a_3(n=6)=2 is a
CANDIDATE corroborated by two independent constructions.  Standalone Lie/invariant theory; no physics,
no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import sympy as sp

t, m, x, y = sp.symbols("t m x y")
M = sp.Matrix([[m, 1], [1, 0]])                 # metallic homological monodromy M_m


def Lk(k):
    Mk = M**k if k >= 0 else (M.inv()) ** (-k)
    return sp.expand(sp.trace(Mk))


def char_Mk(k, sign=1):
    """char(sign*M^k) = t^2 - sign*L_k t + (-1)^k."""
    return sp.expand(t**2 - sign * Lk(k) * t + (-1) ** (k % 2))


def sym_power(Mat, d):
    """Sym^d of a 2x2 matrix: action on degree-d monomials x^{d-i} y^i."""
    a, b, c, dd = Mat[0, 0], Mat[0, 1], Mat[1, 0], Mat[1, 1]
    S = sp.zeros(d + 1, d + 1)
    for i in range(d + 1):
        poly = sp.expand((a * x + c * y) ** (d - i) * (b * x + dd * y) ** i)
        for j in range(d + 1):
            S[j, i] = poly.coeff(x, d - j).coeff(y, j)
    return S


def sym_charpoly(d):
    """char poly of Sym^d(M_m); Sym^0 := (t-1)."""
    if d == 0:
        return t - 1
    return sp.expand(sym_power(M, d).charpoly(t).as_expr())


# --------------------------------------------------------------------------- #
# (1) the cohomological route fails
# --------------------------------------------------------------------------- #

def cohomological_at_trivial(n):
    """char poly of phi_m on H^1(F_2; ad triv) = M_m (x) id_sl(n): char(M)^(n^2-1)."""
    return sp.expand(char_Mk(1) ** (n * n - 1))


# --------------------------------------------------------------------------- #
# (2) the explicit two-sequence Sym-power tower (symbolic m)
# --------------------------------------------------------------------------- #

def sym_tower(n):
    """The explicit reduction (T): prod_{d=2}^n char(Sym^d) * prod_{d=0}^{n-3} char(Sym^d)."""
    P = sp.Integer(1)
    for d in range(2, n + 1):
        P *= sym_charpoly(d)
    for d in range(0, n - 3 + 1):
        P *= sym_charpoly(d)
    return sp.expand(P)


def proved_tower(n):
    """The proved (n<=4) / structural (n=5) metallic tower, symbolic m (B65/B80/B62)."""
    if n == 3:
        return sp.expand((t - 1) * (t + 1) * char_Mk(-1) * char_Mk(2) * char_Mk(3))
    if n == 4:
        return sp.expand((t - 1) ** 2 * (t + 1) * char_Mk(-1) * char_Mk(1) * char_Mk(2)
                         * char_Mk(3) * char_Mk(4) * char_Mk(2, -1))
    if n == 5:
        return sp.expand((t - 1) ** 2 * (t + 1) ** 2 * char_Mk(-1) * char_Mk(1) ** 2
                         * char_Mk(2) ** 2 * char_Mk(3) * char_Mk(4) * char_Mk(5)
                         * char_Mk(2, -1) * char_Mk(3, -1))
    raise ValueError(n)


def char_M3_multiplicity(n):
    """Multiplicity of char(M^3) in the explicit Sym tower (T) -- the n=6 discriminator a_3."""
    P = sp.Poly(sym_tower(n), t)
    c3 = sp.Poly(char_Mk(3), t)
    cnt = 0
    while sp.rem(P, c3).as_expr() == 0:
        P = sp.quo(P, c3)
        cnt += 1
    return cnt


def main():
    print("B89-T (Task T) -- the tower's cohomological route closed; the explicit Sym reduction\n")
    print("(1) cohomological route FAILS (C1): H^1 action at the trivial-rep fixed line vs the tower")
    for n in (3, 4, 5):
        coh = cohomological_at_trivial(n)
        match = sp.expand(coh - proved_tower(n)) == 0
        print(f"    n={n}: char(M)^{n*n-1} == tower?  {match}   (cohomological != tower)")
    print("\n(2) the explicit two-sequence Sym tower == proved/structural tower, SYMBOLIC in m:")
    for n in (3, 4, 5):
        ok = sp.expand(sym_tower(n) - proved_tower(n)) == 0
        tag = "PROVED tower" if n <= 4 else "structural tower"
        print(f"    n={n}: prod char(Sym^d M_m) == {tag}?  {ok}   (deg {sp.degree(sym_tower(n),t)} = n^2-1)")
    print("\n(3) the n=6 discriminator: multiplicity of char(M^3) from the Sym tower:")
    print(f"    a_3(n=6) = {char_M3_multiplicity(6)}   (Sym + theta-split both say 2; B66 pinv said 1,")
    print("              and B84 showed that pinv is gauge-corrupted at this sector -> 2-of-3 toward 2)")
    print("\nReduction: the all-n tower is now ONE module-iso conjecture (M): J(m) ~= M_m on")
    print("  [(+)_{d=2}^n Sym^d] (+) [(+)_{d=0}^{n-3} Sym^d] -- PROVED n<=4, structural n=5; derivation open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
