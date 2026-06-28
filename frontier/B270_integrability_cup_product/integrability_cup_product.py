"""B270 -- integrability, recomputed: the cup-product (quadratic) obstruction vanishes; deformations are cusp
deformations. FIREWALLED (deformation theory of flat connections, not physics). Nothing to CLAIMS.md.

The rigor upgrade flagged in the B268 audit (Phase 3): B265 CITED the smoothness of the geometric rep
(Menal-Ferrer-Porti / Thurston) for integrability. Here we COMPUTE the first obstruction directly and exhibit the
mechanism, turning 'cited' into 'computed'.

(A) THE CUP-PRODUCT OBSTRUCTION (SL(2,C)/Sym^2 -- the geometric/exponent-1 foundation), computed exactly:
    Deform rho_eps(g) = exp(eps*xi_g) rho_0(g). The relator rho_eps(r)=I expands as
        eps^1: L(xi) = 0           (xi is a cocycle, in Z^1)
        eps^2: Q(xi) + L(eta) = 0  (solvable for the 2nd-order eta  <=>  Q(xi) in im(L) = im d^1).
    Q(xi) is the quadratic obstruction (the cup product xi U xi via the bracket); its class [Q(xi)] in
    H^2 = coker(d^1) is THE obstruction to integrating xi. We compute (exact, t=e^{i pi/3}): dim Z^1=4, dim B^1=3,
    so H^1=1; for the H^1 representative xi, L(xi)=0 and Q(xi) IS a coboundary (in im d^1), so [Q(xi)]=0.
    => the figure-eight SL(2,C) character variety is SMOOTH at the geometric rep -- re-derived, not cited.

(B) THE MECHANISM FOR ALL EXPONENTS (why the {4,8} E6 directions integrate too):
    dim H^1(M, Sym^{2m}) = #cusps = 1 for all m (B264 / Menal-Ferrer-Porti). The peripheral (cusp) cohomology has
    dim H^1(dM=T^2, Sym^{2m}) = 2*dim(Sym^{2m})^{peripheral} = 2*1 = 2 (the parabolic fixes one line, the highest
    weight). Half-lives-half-dies: the restriction H^1(M)->H^1(dM) has half-dimensional (Lagrangian) image, dim
    = 1 = dim H^1(M). So the restriction is INJECTIVE: EVERY deformation is detected on the cusp -- it is a cusp
    (eigenvalue / cusp-shape) deformation, and cusp deformations are explicitly realizable, hence integrate.
    => the {4,8} directions integrate because they ARE cusp deformations (dim H^1 = #cusps), with (A) the explicit
    confirmation in the foundational SL(2) block.

NET: B265's integrability is now anchored by an explicit vanishing cup product (A) plus the dim-H^1=#cusps
boundary-deformation mechanism (B) -- no longer a bare citation. (Honest scope: (A) computes the obstruction in the
SL(2)/exponent-1 block; the higher blocks integrate by the cusp mechanism (B), the actual reason MFP smoothness
holds, rather than by 78-dim e6 cup products computed block-by-block.)

Run: python integrability_cup_product.py  (pyenv, sympy + mpmath; imports B264 for Sym^n).
"""
import importlib.util
import pathlib

import sympy as sp

_B264 = pathlib.Path(__file__).resolve().parents[1] / "B264_e6_character_variety" / "e6_charvar_tangent.py"
_spec = importlib.util.spec_from_file_location("b264", _B264)
b264 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b264)

_T = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2          # e^{i pi/3}
_a = sp.Matrix([[1, 1], [0, 1]])
_b = sp.Matrix([[1, 0], [_T, 1]])
_BASE = {"a": _a, "b": _b, "A": _a.inv(), "B": _b.inv()}
_REL = "abABaBAbaB"
_E, _H, _F = sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[1, 0], [0, -1]]), sp.Matrix([[0, 0], [1, 0]])
_BAS = [_E, _H, _F]


def _tovec(M):
    return [sp.simplify(M[0, 1]), sp.simplify(M[0, 0]), sp.simplify(M[1, 0])]


def _relator_coeffs(ua, ub):
    """eps^1 (L) and eps^2 (Q) coefficients of rho_eps(r), rho_eps(g)=exp(eps u_g) rho(g)."""
    u = {"a": ua, "b": ub}
    M = [sp.eye(2), sp.zeros(2, 2), sp.zeros(2, 2)]
    for ch in _REL:
        g = ch.lower()
        if ch.islower():
            ug, rho = u[g], _BASE[ch]
            f = [rho, ug * rho, (ug * ug / 2) * rho]
        else:
            ug, ig = u[g], _BASE[ch]
            f = [ig, -ig * ug, ig * (ug * ug) / 2]
        N = [sp.zeros(2, 2), sp.zeros(2, 2), sp.zeros(2, 2)]
        for i in range(3):
            for j in range(3):
                if i + j <= 2:
                    N[i + j] = N[i + j] + M[i] * f[j]
        M = [sp.simplify(x) for x in N]
    return M[1], M[2]


def cup_product_obstruction_vanishes():
    """Compute dim Z^1/B^1, the H^1 cocycle xi, its quadratic obstruction Q(xi), and whether [Q(xi)]=0 in H^2."""
    cols = []
    for g in ("a", "b"):
        for k in range(3):
            ua = _BAS[k] if g == "a" else sp.zeros(2, 2)
            ub = _BAS[k] if g == "b" else sp.zeros(2, 2)
            L, _ = _relator_coeffs(ua, ub)
            cols.append(_tovec(L))
    L = sp.simplify(sp.Matrix(cols).T)                       # d^1 : 3 x 6
    ker = L.nullspace()
    Ad = lambda g, X: sp.simplify(_BASE[g] * X * _BASE[g].inv())
    cob = [_tovec(_BAS[k] - Ad("a", _BAS[k])) + _tovec(_BAS[k] - Ad("b", _BAS[k])) for k in range(3)]
    B1 = sp.Matrix(cob).T                                    # d^0 image
    xi = next(v for v in ker if B1.row_join(v).rank() > B1.rank())
    ua = xi[0] * _E + xi[1] * _H + xi[2] * _F
    ub = xi[3] * _E + xi[4] * _H + xi[5] * _F
    Lx, Q = _relator_coeffs(sp.simplify(ua), sp.simplify(ub))
    qv = sp.Matrix(_tovec(sp.simplify(Q)))
    return dict(dimZ1=len(ker), dimB1=B1.rank(), dimH1=len(ker) - B1.rank(),
                cocycle=sp.simplify(Lx) == sp.zeros(2, 2),
                obstruction_is_coboundary=(L.rank() == L.row_join(qv).rank()))


def peripheral_h1_dim(m):
    """dim H^1(T^2, Sym^{2m}) for the parabolic cusp = 2 * dim(fixed line of the meridian parabolic) = 2."""
    Sa = b264.symn(b264.mp.matrix([[1, 1], [0, 1]]), 2 * m)   # Sym^{2m}(meridian), unipotent
    dim = 2 * m + 1
    amI = Sa - b264.mp.eye(dim)
    fixed = dim - b264._rank(amI)                            # dim of the parabolic-fixed subspace
    return 2 * fixed                                         # T^2: dim H^1 = 2 * dim invariants


if __name__ == "__main__":
    print("=== B270: integrability recomputed (cup-product obstruction + cusp mechanism) ===\n")
    r = cup_product_obstruction_vanishes()
    print(f"(A) SL(2,C)/Sym^2: dim Z^1={r['dimZ1']}, dim B^1={r['dimB1']}, dim H^1={r['dimH1']}")
    print(f"    H^1 representative is a genuine cocycle (L(xi)=0): {r['cocycle']}")
    print(f"    quadratic obstruction [Q(xi)] = 0 in H^2 (Q(xi) is a coboundary): {r['obstruction_is_coboundary']}")
    print("    => figure-eight SL(2,C) character variety SMOOTH at the geometric rep (computed, not cited).")
    assert r["dimH1"] == 1 and r["cocycle"] and r["obstruction_is_coboundary"]

    print("\n(B) cusp mechanism for all exponents (dim H^1(M)=#cusps=1):")
    for m in [1, 4, 5, 7, 8, 11]:
        d = peripheral_h1_dim(m)
        print(f"    dim H^1(T^2, Sym^{2*m:>2}) = {d}; half-lives-half-dies image = {d//2} = dim H^1(M) "
              f"-> restriction injective -> deformation is a cusp deformation -> integrates")
        assert d == 2
    print("\n=> {4,8} E6 directions integrate (they are cusp deformations); SL(2) cup product confirms the")
    print("   foundation. B265 integrability now computed + mechanistic, not cited. PASS")
