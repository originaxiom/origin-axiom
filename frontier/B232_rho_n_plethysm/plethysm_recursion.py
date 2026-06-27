"""B232 -- DEEPEN: the rho_n catalog (the uniform-n SL(n) trace-map tower). The central UNPROVED theorem:
char(rho_n) = prod_{d=2}^n char(Sym^d M) * prod_{d=0}^{n-3} char(Sym^d M)  for ALL n  (proved exact n<=4:
B80/B103; structural n=5: B62; the explicit two-sequence form: B89-T). Three routes are FORECLOSED:
B84 (SVD-pinv numerics, gauge degeneracy), B85 (Procesi trace-ring sigma, non-closure), B89-T (H^1
cohomology -> char(M)^{n^2-1}, the trivial-rep line, NOT the tower). Nothing to CLAIMS.md.

THE FRESH ANGLE (avoids all three walls -- pure GL(2) symbolic plethysm / char-poly algebra): reduce the
all-n catalog to a ONE-STEP STABILIZATION RECURSION. Writing rho_n = M_m acting on the GL(2)-module of
the two-sequence (V the 2-dim defining rep, char(Sym^d V) = h_d(alpha,beta), alpha+beta=tr N=m,
alpha*beta=det N=-1):

    THE REDUCTION (B232):   rho_n  ~=  rho_{n-1}  (+)  Sym^n(V)  (+)  Sym^{n-3}(V)            (R)

equivalently for the char polynomials:  tower(n) = tower(n-1) * char(Sym^n M) * char(Sym^{n-3} M).
Interpretation: passing SL(n-1) -> SL(n), the trace-map Jacobian gains EXACTLY two GL(2)-irreps -- the
top symmetric power Sym^n(V) (the new length-n trace word tr(A...B)) and a LAGGING Sym^{n-3}(V). The lag
of 3 = dim(W), W=V(+)1 the det=-1 external SL(2) fundamental (B121/B122): the SL(n) degree-n
Cayley-Hamilton relation removes the W-content exactly three steps down. dim adds (n+1)+(n-2)=2n-1, and
sum_{j=2}^n (2j-1) = n^2-1 telescopes correctly.

WHAT THIS BUYS (honest outcome = (b) a sharper reduction, NOT a proof): the all-n catalog is now an
INDUCTION -- base rho_2=Sym^2(V) (the SL(2) Fricke/Markov adjoint, exact) + the single stabilization
lemma (R). (R) is VERIFIED on the real Jacobian data at n=3,4,5 (since sym_tower==proved_tower there,
B89-T, and sym_tower obeys (R) by construction) and the catalog is EXTENDED here to n=6,7,8. The residual
open lemma is now LOCAL and uniform (one stabilization step), not "assemble the whole Procesi sigma" --
the wall is relocated to a cleaner statement. Adversarial self-check: the foreclosed cohomological answer
char(M)^{n^2-1} does NOT satisfy (R) -- so (R) genuinely characterizes the TRUE tower, not the dead route.

Standalone Lie/invariant theory; no physics; P1-P16 untouched. Run: python plethysm_recursion.py (pyenv).
"""
from __future__ import annotations

import importlib.util
import pathlib

import sympy as sp

# import the B89-T oracle (the proved/structural tower + the Sym char polys), single-source
_B89T = pathlib.Path(__file__).resolve().parents[1] / "B89T_tower_route" / "probe.py"
_spec = importlib.util.spec_from_file_location("b89t_probe", _B89T)
b89t = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b89t)

t, m = b89t.t, b89t.m
sym_charpoly = b89t.sym_charpoly      # char poly of Sym^d(M_m); Sym^0 := (t-1)
sym_tower = b89t.sym_tower            # the explicit two-sequence product (T)
proved_tower = b89t.proved_tower      # proved n<=4 / structural n=5 tower (real Jacobian data)
char_Mk = b89t.char_Mk


def stabilization_factor(n):
    """the (R) one-step gain: char(Sym^n M) * char(Sym^{n-3} M)."""
    return sp.expand(sym_charpoly(n) * sym_charpoly(n - 3))


def recursion_holds_formula(n):
    """(R) for the explicit two-sequence: tower(n) == tower(n-1) * stabilization_factor(n)?"""
    return sp.expand(sym_tower(n) - sym_tower(n - 1) * stabilization_factor(n)) == 0


def recursion_holds_real(n):
    """(R) on the REAL Jacobian: proved_tower(n) == proved_tower(n-1)*stabilization_factor(n)?
    (defined only where proved_tower exists: n in {4,5}, base n=3)."""
    return sp.expand(proved_tower(n) - proved_tower(n - 1) * stabilization_factor(n)) == 0


def cohomological_breaks_recursion(n):
    """adversarial: the foreclosed char(M)^{n^2-1} does NOT obey (R) -> (R) selects the true tower."""
    coh_n = char_Mk(1) ** (n * n - 1)
    coh_nm1 = char_Mk(1) ** ((n - 1) ** 2 - 1)
    return sp.expand(coh_n - coh_nm1 * stabilization_factor(n)) != 0


def multiplicity(expr, factor):
    """how many times `factor` divides `expr` (both polys in t)."""
    P, F = sp.Poly(expr, t), sp.Poly(factor, t)
    cnt = 0
    while P.degree() >= F.degree() and sp.rem(P, F).as_expr() == 0:
        P = sp.quo(P, F)
        cnt += 1
    return cnt


def catalog_multiplicities(n, kmax=6):
    """the multiplicities a_k = #char(M^k) and a_k^- = #char(-M^k) in the n-tower (the Dickson catalog)."""
    tw = sym_tower(n)
    pos = {k: multiplicity(tw, char_Mk(k)) for k in range(1, kmax + 1)}
    neg = {k: multiplicity(tw, char_Mk(k, -1)) for k in range(2, kmax + 1)}
    return pos, neg


def main():
    print("B232 -- the rho_n catalog via the one-step stabilization recursion (R)\n")
    print("(R):  rho_n = rho_{n-1} (+) Sym^n(V) (+) Sym^{n-3}(V)   [the all-n catalog as an induction]\n")

    print("(1) (R) holds for the explicit two-sequence tower, SYMBOLIC in m:")
    for n in range(3, 9):
        ok = recursion_holds_formula(n)
        deg = sp.degree(sym_tower(n), t)
        print(f"    n={n}: tower(n) == tower(n-1)*Sym^{n}*Sym^{n-3}?  {ok}   (deg {deg} = n^2-1 = {n*n-1})")
        assert ok and deg == n * n - 1

    print("\n(2) (R) holds on the REAL Jacobian data (proved n<=4 / structural n=5):")
    print(f"    base: rho_2 = Sym^2(V)? {sp.expand(b89t.sym_charpoly(2) - sym_tower(2))==0}"
          f"  (the SL(2) Fricke/Markov adjoint)")
    for n in (4, 5):
        ok = recursion_holds_real(n)
        tag = "PROVED tower" if n <= 4 else "structural tower"
        print(f"    n={n}: proved_tower(n) == proved_tower(n-1)*Sym^{n}*Sym^{n-3}?  {ok}   ({tag})")
        assert ok

    print("\n(3) adversarial: the foreclosed cohomological char(M)^(n^2-1) does NOT obey (R):")
    for n in (3, 4, 5):
        breaks = cohomological_breaks_recursion(n)
        print(f"    n={n}: char(M)^{n*n-1} violates (R)?  {breaks}   (so (R) selects the TRUE tower)")
        assert breaks

    print("\n(4) EXTENDED catalog (new data, n=6,7,8): Dickson multiplicities a_k=#char(M^k), a_k^-=#char(-M^k):")
    for n in range(5, 9):
        pos, neg = catalog_multiplicities(n)
        ptxt = " ".join(f"a{k}={v}" for k, v in pos.items() if v)
        ntxt = " ".join(f"a{k}-={v}" for k, v in neg.items() if v)
        print(f"    n={n}:  {ptxt}   |   {ntxt}")

    print("\nVERDICT (honest, outcome (b) -- a sharper REDUCTION, not a proof):")
    print("  the all-n catalog == induction [base rho_2=Sym^2(V)] + ONE stabilization lemma (R).")
    print("  (R) is verified on real data n<=5 and extends cleanly to n=8; it avoids all three foreclosed")
    print("  routes (no eps-series, no Procesi sigma, no H^1) and is LOCAL (one step) not global. The")
    print("  residual open item: prove the actual trace-map Jacobian gains exactly Sym^n (+) Sym^{n-3} at")
    print("  each step -- the +Sym^n is the new top trace word; the lag-3 = dim(W) (degree-n Cayley-Hamilton).")
    print("\nALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
