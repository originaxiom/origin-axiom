"""B122 -- the tower is symmetric powers of the external monodromy fundamental W = V (+) 1 (unifies B121).

The interleaving/two-sequence (B117) re-expressed: as a virtual GL(2)-character/module,

    rho_n  =  Sym^n(W)  (+)  ( Sym^{n-3}(W)  (-)  W ),      W = V (+) 1   (3-dim),

where V is the 2-dim defining rep of the figure-eight monodromy and 1 the trivial. This BANKS Chat-2's W-identity
AND unifies it with B121 (they are ONE result, not two -- do not double-count). Honest strength throughout: a
genuine GL(2)-module repackaging + a canonical identification of W; NOT a proof route / wall-bypass.

WHAT IS PROVED / VERIFIED.
  (1) CHARACTER identity rho_n = Sym^n(W)+Sym^{n-3}(W)-1-V matches the two-sequence mu_d (B103/B117), n=2..11.
      Cleaner form: Sym^0(+)Sym^1 = 1(+)V = W, so the correction is Sym^{n-3}(W) (-) W (the nonlinear part).
  (2) It is a genuine GL(2)-MODULE iso (NOT vacuous): Sum_d mu_d h_d(x,y) = h_n(x,y,1)+h_{n-3}(x,y,1)-1-(x+y) holds
      SYMBOLICALLY in general (x,y), DET-INDEPENDENT, n=2..8. The tower is a GL(2,Z)-rep (B103); over GL(2),
      module = character is NOT automatic, and Sym^a(V(+)1)=(+)_{k<=a}Sym^k(V) is a functorial module decomposition.
      Module-level proved n=3,4 (B103 P-iso); character-level all n.
  (3) W IS B121's EXTERNAL monodromy fundamental. det(W=V(+)1) = det(V)*1 = -1 (the external det=-1 parity);
      det(Fricke = Sym^2 V) = +1 (the internal principal/Kostant parity). So Chat-2's KILL of "W = Fricke 3-space"
      IS B121's external != internal: Fricke carries the internal embedding (even weights), the tower the external
      one (mixed parity). The tower's ODD weights = Sym^n(V(+)1) including V (weight 1) = the B121 parity
      obstruction, re-derived. => B121 and the W-identity are ONE object.

COROLLARIES (A7a/A1, math tier).
  - Sym^4(3-dim) = 15 = dim sl(4), and 4 is the UNIQUE saturating order (Sym^3=10!=8, Sym^5=21!=24): the n=4 fixed
    point of the dimension identity (B117), restated.
  - band offset = dim(W) = 3 (in the W-power index) = the offset-2 in the Sym(V)-index (B117 doubling): one
    structure, reconciled readings.

NOT A WALL-BYPASS (honest -- the brave functorial test, run and reported).
  The identity is the elementary expansion Sym^a(V(+)1)=(+)Sym^k(V) applied to the two-sequence; it is module-iso-
  EQUIVALENT to the two-sequence (proving it for all n == proving mu_d). NO functorial Sym(W)->trace-ring map was
  found; the n=4-only Sym^4(3)=15 coincidence does not generalize (the correction term blocks a single clean Sym^n).
  So it REPACKAGES the prize and IDENTIFIES W canonically, but does NOT lower the trace-ring wall. The re-aimed
  prize: prove the tower is *functorially* Sym^n(W) (+) (Sym^{n-3}(W) (-) W) for the external fundamental W -- a
  construction that does not yet exist. This is the MAGNITUDE layer (Sym content); the signs char(M^h)/char(-M^h)
  are the orthogonal det=-1 layer (B118's (-1)^{h+1}).

Standalone rep theory; the 3+1 / spin-2 geometric READINGS are firewalled (speculations/S028, fenced). NO physics
here; no CLAIMS.md promotion; the rho_n / Sym-mu_d proof stays the prize; P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys
from itertools import combinations_with_replacement

import numpy as np
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_B103 = _load("b122_b103", "frontier/B103_tower_equivariance/probe.py")
_x, _y, _m = sp.symbols("x y m")


def _mu(n):
    return _B103.two_sequence_mult(n)


def _h(vs, d):
    """Complete homogeneous symmetric polynomial h_d = character of Sym^d of a rep with eigenvalues vs."""
    if d < 0:
        return sp.Integer(0)
    if d == 0:
        return sp.Integer(1)
    return sp.expand(sum(sp.prod(c) for c in combinations_with_replacement(vs, d)))


# --------------------------------------------------------------------------- #
# (1) the character identity vs the two-sequence
# --------------------------------------------------------------------------- #
def w_identity_character(nmax=11):
    """rho_n = Sym^n(W)+Sym^{n-3}(W)-1-V decomposes into Sym^k(V) with multiplicity == mu_d, n=2..nmax.
    (Sym^a(W)=(+)_{k=0}^a Sym^k(V) since W=V(+)1.)"""
    bad = []
    for n in range(2, nmax + 1):
        from collections import Counter
        c = Counter()
        for k in range(0, n + 1):
            c[k] += 1
        for k in range(0, max(n - 3, -1) + 1):
            c[k] += 1
        c[0] -= 1
        c[1] -= 1
        pred = {k: v for k, v in c.items() if v != 0}
        if pred != dict(_mu(n)):
            bad.append((n, pred, dict(_mu(n))))
    return {"nmax": nmax, "all_match": len(bad) == 0, "mismatches": bad,
            "cleaner_form": "rho_n = Sym^n(W) (+) (Sym^{n-3}(W) (-) W);  Sym^0(+)Sym^1 = 1(+)V = W"}


# --------------------------------------------------------------------------- #
# (2) the GL(2)-module iso (symbolic, det-independent) -- the corrected hinge (a)
# --------------------------------------------------------------------------- #
def w_identity_is_gl2_module_iso(nmax=8):
    """The identity holds SYMBOLICALLY in general (x,y) (any det), n=2..nmax => a genuine GL(2)-module iso
    (the tower is a GL(2,Z)-rep, B103; module != character is non-trivial over GL(2))."""
    residuals = {}
    for n in range(2, nmax + 1):
        lhs = sp.expand(sum(v * _h((_x, _y), d) for d, v in _mu(n).items()))
        rhs = sp.expand(_h((_x, _y, 1), n) + _h((_x, _y, 1), n - 3) - 1 - (_x + _y))
        residuals[n] = sp.simplify(lhs - rhs)
    return {"all_zero_general_xy": all(r == 0 for r in residuals.values()),
            "det_independent": True,
            "note": "Sym^a(V(+)1) = (+)_{k<=a} Sym^k(V) is a FUNCTORIAL module decomposition; the identity is a "
                    "genuine GL(2)-module iso (proved module-level n=3,4 via B103; character-level all n). NOT "
                    "vacuous -- over GL(2), module-iso is not implied by a single element's character."}


# --------------------------------------------------------------------------- #
# (3) W is B121's external fundamental (det=-1) -- the unification
# --------------------------------------------------------------------------- #
def W_is_external_fundamental():
    """W = V(+)1 carries det=-1 (B121's EXTERNAL parity); Fricke = Sym^2(V) carries det=+1 (INTERNAL/principal).
    So Chat-2's Fricke KILL = B121's external != internal; the tower's odd weights = Sym^n(V(+)1) ni V."""
    M = sp.Matrix([[_m, 1], [1, 0]])                                  # V = the seed, det = -1
    det_V = sp.simplify(M.det())
    # W = V (+) 1 : a 3x3 block diag
    W = sp.Matrix(3, 3, lambda i, j: (M[i, j] if i < 2 and j < 2 else (1 if i == j == 2 else 0)))
    det_W = sp.simplify(W.det())
    # Fricke = Sym^2(V): eigenvalues t^2, 1, 1/t^2 -> det = +1
    t = sp.symbols("t")
    sym2 = sp.diag(t ** 2, 1, t ** (-2))
    det_fricke = sp.simplify(sym2.det())
    return {"det_V": det_V, "det_W": det_W, "det_fricke_Sym2V": det_fricke,
            "W_external_det_minus_1": det_W == -1, "fricke_internal_det_plus_1": det_fricke == 1,
            "verdict": "W=V(+)1 is the EXTERNAL monodromy fundamental (det=-1, B121); Fricke=Sym^2(V) is INTERNAL "
                       "(det=+1, Kostant). The Fricke kill = external != internal; odd weights = Sym^n(V(+)1) ni V. "
                       "B121 and the W-identity are ONE object."}


# --------------------------------------------------------------------------- #
# corollaries (A7a / A1) + the not-a-wall-bypass verdict
# --------------------------------------------------------------------------- #
def a7a_corollaries():
    """Sym^4(3-dim)=15=sl(4) is the UNIQUE saturating order; band offset = dim(W) = 3."""
    sym_dim = {a: (a + 1) * (a + 2) // 2 for a in range(2, 7)}        # dim Sym^a(3-space)
    sl_dim = {n: n * n - 1 for n in range(2, 7)}
    saturating = [a for a in sym_dim if sym_dim[a] == sl_dim.get(a, -1)]
    return {"dim_Sym_a_3space": sym_dim, "dim_sl_n": sl_dim, "saturating_orders": saturating,
            "unique_at_4": saturating == [4], "band_offset_eq_dimW": 3}


def not_a_wall_bypass():
    """Honest: module-iso-equivalent to the two-sequence; no functorial Sym(W)->trace-ring map; the n=4-only
    Sym^4(3)=15 coincidence does not generalize. Repackaging + canonical W, NOT a proof route."""
    a7 = a7a_corollaries()
    return {"sym4_unique_saturation": a7["unique_at_4"],
            "wall_bypassed": False,
            "verdict": "module-iso-EQUIVALENT to the two-sequence (proving it all-n == proving mu_d); NO functorial "
                       "Sym(W)->trace-ring map found; the correction term + the n=4-only saturation block a single "
                       "clean Sym^n. Re-aims the prize (prove the tower is *functorially* Sym^n(W)(+)(Sym^{n-3}(W)-W)) "
                       "but does NOT lower the trace-ring wall. Magnitude layer only (signs = the det=-1 layer, B118)."}


# --------------------------------------------------------------------------- #
# the two layers split by det (Chat-2 interlude finding 1) + the n<=14 confirmation
# --------------------------------------------------------------------------- #
def fig8_is_golden_squared():
    """The figure-eight monodromy is the golden unit SQUARED: M_1^2 = [[2,1],[1,1]], det=+1, eigenvalue phi^2.
    Squaring the golden (det=-1) seed gives the fig-8 (det=+1) -- squares the eigenvalues, collapses the signs."""
    M1 = sp.Matrix([[1, 1], [1, 0]])                    # golden, det = -1
    M2 = M1 * M1
    return {"M1sq": M2.tolist(), "det": int(M2.det()), "trace": int(M2.trace()),
            "det_is_plus_one": M2.det() == 1, "eigenvalue": "phi^2 = (3+sqrt5)/2"}


def magnitude_layer_det_independent(nmax=14):
    """The MAGNITUDE layer (the W-identity / Sym content mu_d) is DET-INDEPENDENT: the identity holds for general
    (x,y) (B122), so it is NOT a det=-1 feature; the multiplicity form matches mu_d through n=nmax (confirmation,
    extends the banked n<=11)."""
    from collections import Counter
    bad = []
    for n in range(2, nmax + 1):
        c = Counter()
        for k in range(0, n + 1):
            c[k] += 1
        for k in range(0, max(n - 3, -1) + 1):
            c[k] += 1
        c[0] -= 1
        c[1] -= 1
        if {k: v for k, v in c.items() if v != 0} != dict(_mu(n)):
            bad.append(n)
    return {"matches_through_n": nmax, "all_match": len(bad) == 0,
            "det_independent": True,
            "note": "the W-identity is a polynomial identity in (x,y) (B122), so the magnitude layer holds for "
                    "det=+1 as well as det=-1 -- it is MORE GENERAL than the metallic ray (det=-1)."}


def sign_layer_is_det_minus_one():
    """The SIGN layer (the inversion identity char(M^-1)=char(-M), the parity factor) is DET=-1-SPECIFIC:
    char(M^-1)-char(-M) = 0 at det=-1, = -2*t*tau at det=+1 (fails); the parity factor (t-1)(t-det) collapses
    (t-1)(t+1) -> (t-1)^2 going golden(det-1) -> fig8(det+1=golden^2)."""
    tt, tau, dd = sp.symbols("t tau d")
    diff = sp.simplify((tt ** 2 - (tau / dd) * tt + 1 / dd) - (tt ** 2 + tau * tt + dd))
    return {"inversion_holds_det_minus_1": sp.simplify(diff.subs(dd, -1)) == 0,
            "inversion_fails_det_plus_1": sp.simplify(diff.subs(dd, 1)) != 0,
            "parity_det_minus_1": str(sp.factor((tt - 1) * (tt + 1))),
            "parity_det_plus_1": str(sp.factor((tt - 1) * (tt - 1))),
            "note": "the signs (char(M^h) vs char(-M^h), B118) are the metallic/orientation feature; squaring "
                    "golden->fig8 squares the eigenvalues and COLLAPSES the (t-1)(t+1) parity to (t-1)^2."}


# --------------------------------------------------------------------------- #
# the Sym tower is VOID-SPECIFIC (Chat-2 interlude finding 2; SL(2), order-6 corrected)
# --------------------------------------------------------------------------- #
def sym_tower_is_void_specific():
    """At SL(2) on the trace map T(x,y,z)=(z,x,xz-y): at the VOID (2,2,2) the Jacobian eigenvalues are
    {-1, phi^2, psi^2} = Sym^2(M) (the n=2 tower); at the OTHER fixed point (0,0,0) they are {-1, e^{+-i pi/3}} =
    6th roots of unity (char poly lambda^3+1, DT^6=I) -- elliptic, NOT Sym-organized. So the Sym tower is the
    linearization where the abelianization M acts: VOID-SPECIFIC (corroborates B106). [Order 6, not order 3.]"""
    xs, ys, zs, lam = sp.symbols("xs ys zs lam")
    T = [zs, xs, xs * zs - ys]
    DT = sp.Matrix([[sp.diff(Ti, v) for v in (xs, ys, zs)] for Ti in T])
    cp_void = sp.factor(DT.subs({xs: 2, ys: 2, zs: 2}).charpoly(lam).as_expr())
    cp_zero = sp.expand(DT.subs({xs: 0, ys: 0, zs: 0}).charpoly(lam).as_expr())
    phi = (1 + sp.sqrt(5)) / 2
    sym2 = sp.expand(sp.prod([lam - e for e in (phi ** 2, sp.Integer(-1), 1 / phi ** 2)]))
    void_is_sym2 = sp.simplify(cp_void - sym2) == 0
    zero_is_lam3p1 = sp.simplify(cp_zero - (lam ** 3 + 1)) == 0       # 6th roots; NOT lambda^3-1 (cube roots)
    return {"void_charpoly_is_Sym2M": bool(void_is_sym2),
            "zero_charpoly_is_lam3_plus_1": bool(zero_is_lam3p1),
            "zero_spectrum": "{-1, e^{+-i pi/3}} = 6th roots of unity (DT^6=I, order 6)",
            "order_is_6_not_3": bool(zero_is_lam3p1),
            "note": "the Sym^d(M) tower lives at the void (where M acts); the other fixed point is elliptic / "
                    "root-of-unity (order 6), NOT Sym -- the Sym organization is void-specific (B106 made explicit)."}


def main():
    print("=" * 78)
    print("B122 -- the tower is symmetric powers of the external fundamental W = V (+) 1 (unifies B121)")
    print("=" * 78)
    c = w_identity_character(11)
    print(f"\n[1 character] rho_n = Sym^n(W)+Sym^{{n-3}}(W)-1-V == mu_d, n=2..11: {c['all_match']}")
    print(f"    {c['cleaner_form']}")
    g = w_identity_is_gl2_module_iso(8)
    print(f"\n[2 GL(2)-module iso] identity holds SYMBOLICALLY in general (x,y) [any det], n=2..8: "
          f"{g['all_zero_general_xy']}  -> a GENUINE GL(2)-module iso (NOT vacuous)")
    w = W_is_external_fundamental()
    print(f"\n[3 unification] det(W=V(+)1)={w['det_W']} (external, B121) vs det(Fricke=Sym^2V)={w['det_fricke_Sym2V']} "
          f"(internal). {w['verdict']}")
    a = a7a_corollaries()
    print(f"\n[A7a] Sym^a(3-space) dims {a['dim_Sym_a_3space']}; saturates n^2-1 only at a={a['saturating_orders']} "
          f"(=sl(4)); band offset = dim W = {a['band_offset_eq_dimW']}")
    nb = not_a_wall_bypass()
    print(f"\n[VERDICT] wall bypassed: {nb['wall_bypassed']}")
    print(f"    {nb['verdict']}")
    print("\n" + "-" * 78)
    print("Chat-2 interlude extensions (terrain-sweeping; none touch the wall)")
    print("-" * 78)
    fg = fig8_is_golden_squared()
    print(f"\n[F1] fig-8 monodromy = golden^2: M_1^2={fg['M1sq']}, det={fg['det']} (+1), eigenvalue {fg['eigenvalue']}")
    md = magnitude_layer_det_independent(14)
    print(f"[F1 magnitude] the W-identity is DET-INDEPENDENT (holds general (x,y)); matches mu_d through n={md['matches_through_n']}: "
          f"{md['all_match']}")
    sl = sign_layer_is_det_minus_one()
    print(f"[F1 sign] inversion char(M^-1)=char(-M): det=-1 {sl['inversion_holds_det_minus_1']}, det=+1 FAILS "
          f"{sl['inversion_fails_det_plus_1']}; parity (t-1)(t+1) [det-1] -> {sl['parity_det_plus_1']} [det+1]")
    vs = sym_tower_is_void_specific()
    print(f"\n[F2 void-specific] void (2,2,2) = Sym^2(M): {vs['void_charpoly_is_Sym2M']}; (0,0,0) char poly lambda^3+1 "
          f"= {vs['zero_spectrum']}: {vs['zero_charpoly_is_lam3_plus_1']} (order 6, NOT 3: {vs['order_is_6_not_3']})")
    print("\nNone of these lower the wall: the functorial Sym(W)->trace-ring map is still the one missing piece.")


if __name__ == "__main__":
    main()
