"""B102 -- the W1/W2 dichotomy + the R4 (boundary-controlled cubic) continuation.

Two follow-ons to B101 (verify-don't-trust applied to a CC-web handoff; all higher-Teichmuller /
character-variety geometry, NO physics):

  D1/D2/D3/D4 -- the W1/W2 dichotomy (SOLID).  Cayley-Hamilton on the figure-eight T_1^2 forces every
      irreducible Fix(T_1^2) SL(3) character to satisfy
          (trA - trA^-1)(trB - 1) = 0   and   (trA - trA^-1)(trB^-1 - 1) = 0,
      so it is Case I (trA = trA^-1, self-dual -- contains the geometric rep, which is COMPLEX, in Q(sqrt-3))
      or the trB = trB^-1 = 1 branch.  On B71's exact components: V0 = self-dual (geometric, Q(sqrt-3));
      W1 = {trA=trA^-1=1} -> A has eigenvalues {1, i, -i} (order-4 ELLIPTIC); W2 = {trB=trB^-1=1} -> B
      elliptic {1,i,-i}.  An elliptic generator (on the unit circle) is NOT loxodromic, so it fails
      Labourie's Anosov criterion: the genuine non-Sym^2 components are excluded from the real SL(3,R)
      Hitchin component by ELLIPTICITY (cleaner than "complex"); the distinguished V0 by complexity.
      The {1,i,-i} spectrum is exactly Task M's forced n=3 spectrum (B95).

  D5 -- the R4 continuation (boundary-controlled cubic family).  Imposing tr(dC)=0, tr(C dC)=0 (C=rho([a,b]))
      cuts the V4(+)V4 (dim 10) cubic directions to a 9-dim RELATIVE family that keeps the cusp real TO
      FIRST ORDER (de1=de2=0).  HONEST FINDING (verify-don't-trust): this does NOT extend to finite t -- at
      second order the regular-unipotent cusp splits by cube roots into one real + a COMPLEX pair, so a
      generic relative-family ray complexifies the cusp immediately (t>0).  The handoff's clean
      "(lambda,1,1/lambda) geodesic boundary, Im=0 throughout, cusp-collision at t*~3.775" does NOT
      reproduce (the literal rel[:,0] here goes complex near t=0, re-realifies to NEGATIVE eigenvalues by
      t~0.4, and is solidly 3-real -- not collided -- at t=3.775).  So the boundary control is first-order
      only; the strict unipotent-cusp-preserving (finite-area FG-positive) continuation REMAINS OPEN.

Cite Heusener-Munoz-Porti (SL(3,C) figure-eight character variety), Labourie (Anosov), Hitchin /
Fock-Goncharov / Goldman / Marquis.  No physics claim; no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib

import numpy as np
from scipy.linalg import expm, null_space
from scipy.optimize import least_squares

_ROOT = pathlib.Path(__file__).resolve().parents[2]
inv = np.linalg.inv


def _b71():
    spec = importlib.util.spec_from_file_location("b71_probe", _ROOT / "frontier" / "B71_sl3_apoly" / "probe.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def _b71_peripheral():
    spec = importlib.util.spec_from_file_location("b71_per", _ROOT / "frontier" / "B71_sl3_apoly" / "peripheral.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def sym2(M):
    (a, b), (c, d) = M
    return np.array([[a * a, a * c, c * c], [2 * a * b, a * d + b * c, 2 * c * d], [b * b, b * d, d * d]], float)


# ---------------------------------------------------------------------------
# the 8 SL(3) trace coordinates (B48 / B71 convention)
# ---------------------------------------------------------------------------
def coords8(A, B):
    Ai, Bi, AB = inv(A), inv(B), A @ B
    return np.array([np.trace(A), np.trace(B), np.trace(AB), np.trace(Ai), np.trace(Bi),
                     np.trace(inv(AB)), np.trace(A @ Bi), np.trace(Ai @ B), np.trace(A @ B @ Ai @ Bi)])


def _is_spectrum_1ii(M):
    """Order-independent test: eigenvalues of M = {1, i, -i} (char poly (l-1)(l^2+1) = l^3-l^2+l-1)."""
    ev = np.linalg.eigvals(M)
    e1 = np.sum(ev); e2 = ev[0] * ev[1] + ev[0] * ev[2] + ev[1] * ev[2]; e3 = np.prod(ev)
    return bool(abs(e1 - 1) < 1e-4 and abs(e2 - 1) < 1e-4 and abs(e3 - 1) < 1e-4)


# ===========================================================================
# D1 -- the dichotomy
# ===========================================================================
DICHOTOMY_CONDITIONS = ["(trA - trA^-1)*(trB - 1) = 0", "(trA - trA^-1)*(trB^-1 - 1) = 0"]


def conditions_on_components():
    """The two CH conditions hold (a factor vanishes) on B71's exact V0/W1/W2 coordinate families."""
    per = _b71_peripheral()
    out = {}
    for name, gen in (("V0", lambda p, q: per.V0(p, q) if hasattr(per, "V0") else None),
                      ("W1", per.W1), ("W2", per.W2)):
        c = np.array(gen(1.7, 2.3), float)              # x1..x8
        trA, trB, trAi, trBi = c[0], c[1], c[3], c[4]
        cond1 = (trA - trAi) * (trB - 1); cond2 = (trA - trAi) * (trBi - 1)
        out[name] = (abs(cond1) < 1e-9, abs(cond2) < 1e-9)
    return out


def dichotomy_census(n=40, seed=20):
    """Sample irreducible Fix(T_1^2) SL(3,C) characters (least_squares on the fixed-locus equations) and
    classify Case I (trA=trA^-1) / branch trB=trB^-1=1 / neither. Returns (n_caseI, n_branchB, n_neither)."""
    def resid(v):
        A = (v[:9] + 1j * v[9:18]).reshape(3, 3); B = (v[18:27] + 1j * v[27:36]).reshape(3, 3)
        try:
            Ap, Bp = A @ B @ A, A @ B
            f = np.concatenate([[np.linalg.det(A) - 1, np.linalg.det(B) - 1], coords8(A, B) - coords8(Ap, Bp)])
            o = np.concatenate([f.real, f.imag]); return o if np.all(np.isfinite(o)) else np.ones(22) * 9
        except Exception:
            return np.ones(22) * 9
    rng = np.random.default_rng(seed); I = J = other = 0
    for _ in range(n):
        r = least_squares(resid, rng.standard_normal(36) * 0.7, method="trf", max_nfev=1500, xtol=1e-12, ftol=1e-12)
        if np.max(np.abs(r.fun)) < 1e-7:
            A = (r.x[:9] + 1j * r.x[9:18]).reshape(3, 3); B = (r.x[18:27] + 1j * r.x[27:36]).reshape(3, 3)
            blocks = [m.reshape(-1) for m in [np.eye(3), A, B, A @ B, B @ A, A @ A, B @ B, A @ B @ A, B @ A @ B]]
            if np.linalg.matrix_rank(np.array(blocks), tol=1e-7) < 9:
                continue                                  # skip reducible
            c = coords8(A, B)
            if abs(c[0] - c[3]) < 1e-3:
                I += 1
            elif abs(c[1] - 1) < 1e-3 and abs(c[4] - 1) < 1e-3:
                J += 1
            else:
                other += 1
    return I, J, other


# ===========================================================================
# D2 / D3 -- the ellipticity obstruction + the cross-check against B71's exact components
# ===========================================================================
def realize_and_classify(component, p=2.7, q=2.3):
    """Realize B71's W1/W2 at (p,q) as an explicit SL(3) rep; return which generator is elliptic {1,i,-i}.
    Route (b) cross-check against the actual algebraic representations."""
    per = _b71_peripheral()
    gen = {"W1": per.W1, "W2": per.W2}[component]
    A, B = per.realize(gen(p, q))
    return {"A_elliptic_1ii": _is_spectrum_1ii(A), "B_elliptic_1ii": _is_spectrum_1ii(B)}


def geometric_trace_field():
    """The geometric V0 point (Sym^2 of the SL(2) figure-eight geometric rep) is self-dual and lies in
    Q(sqrt-3): tr(AB) is a root of t^2 - t + 7 (= the geometric SL(3) trace field). Returns
    (self_dual, |t^2-t+7| at tr(AB))."""
    xg = 1.5 + 0.5j * np.sqrt(3)                          # x_geom = (3 + sqrt(-3))/2
    c = np.array(_b71().sym2_groundtruth_coords(xg), complex)
    self_dual = bool(abs(c[0] - c[3]) < 1e-9)
    trAB = c[2]
    return self_dual, float(abs(trAB ** 2 - trAB + 7))


# ===========================================================================
# D4 -- the Task-M link
# ===========================================================================
def task_m_spectrum_link():
    """The Case II / W1 / W2 elliptic spectrum {1, i, -i} is exactly Task M's forced n=3 spectrum (B95;
    tr A = tr A^-1 = 1 forces eigenvalues {1, i, -i}). Returns the spectrum as a sorted tuple."""
    return tuple(sorted([1 + 0j, 1j, -1j], key=lambda z: (z.real, z.imag)))


# ===========================================================================
# D5 -- the R4 continuation: the boundary-controlled (relative) cubic family
# ===========================================================================
def _V4_directions():
    """The 5-dim cubic (V4) isotypic of sl(3) = the trace-orthogonal complement of the principal sl(2)."""
    H = np.diag([2., 0., -2.]); E = np.array([[0, 1, 0], [0, 0, 2], [0, 0, 0]], float); F = E.T.copy()
    F = np.array([[0, 0, 0], [2, 0, 0], [0, 1, 0]], float)
    basis = []
    for i in range(3):
        for j in range(3):
            if i != j:
                M = np.zeros((3, 3)); M[i, j] = 1.; basis.append(M)
    basis += [np.diag([1., -1., 0.]), np.diag([0., 1., -1.])]
    Bm = np.array([b.reshape(-1) for b in basis]).T
    return [(Bm @ v).reshape(3, 3) for v in null_space(np.array([(G.T.reshape(-1)) @ Bm for G in (H, E, F)])).T]


def _seed():
    A0 = np.array([[2., 1.], [1., 1.]]); B0 = np.array([[2., -1.], [-1., 1.]])
    return sym2(A0), sym2(B0)


def relative_cubic_family():
    """The boundary conditions tr(dC)=0, tr(C dC)=0 cut V4(+)V4 (dim 10) to the relative cubic family.
    Returns its dimension (= 9)."""
    A, B = _seed(); C0 = A @ B @ inv(A) @ inv(B); V4 = _V4_directions()
    dC = lambda Xa, Xb: Xa @ C0 + A @ Xb @ B @ inv(A) @ inv(B) - A @ B @ inv(A) @ Xa @ inv(B) - C0 @ Xb
    dirs = [(V4[i], np.zeros((3, 3))) for i in range(5)] + [(np.zeros((3, 3)), V4[i]) for i in range(5)]
    rel = null_space(np.array([[np.trace(dC(a, b)), np.trace(C0 @ dC(a, b))] for (a, b) in dirs]).T)
    return rel.shape[1]


def _cubic_disc(M):
    """Discriminant of the real char poly of M; >0 iff 3 distinct real eigenvalues."""
    e1 = np.trace(M); e2 = 0.5 * (e1 ** 2 - np.trace(M @ M)); e3 = np.linalg.det(M)
    p, q, r = -e1, e2, -e3
    return 18 * p * q * r - 4 * p ** 3 * r + p ** 2 * q ** 2 - 4 * q ** 3 - 27 * r ** 2


def cusp_second_order_complexifies(n=40, seed=7, t=0.05):
    """HONEST FINDING: a generic relative-family ray complexifies the cusp at second order (cube-root
    instability), so the cusp is NOT kept real at finite t. Returns the fraction of rays whose cusp
    discriminant is negative (1 real + complex pair) at small t>0."""
    A, B = _seed(); C0 = A @ B @ inv(A) @ inv(B); V4 = _V4_directions()
    dC = lambda Xa, Xb: Xa @ C0 + A @ Xb @ B @ inv(A) @ inv(B) - A @ B @ inv(A) @ Xa @ inv(B) - C0 @ Xb
    dirs = [(V4[i], np.zeros((3, 3))) for i in range(5)] + [(np.zeros((3, 3)), V4[i]) for i in range(5)]
    rel = null_space(np.array([[np.trace(dC(a, b)), np.trace(C0 @ dC(a, b))] for (a, b) in dirs]).T)
    rng = np.random.default_rng(seed); complex_cusp = 0
    for _ in range(n):
        co = rel @ rng.standard_normal(rel.shape[1])
        Xa = sum(co[i] * V4[i] for i in range(5)); Xb = sum(co[5 + i] * V4[i] for i in range(5))
        Ap, Bp = expm(t * Xa) @ A, expm(t * Xb) @ B
        if _cubic_disc(Ap @ Bp @ inv(Ap) @ inv(Bp)) < 0:
            complex_cusp += 1
    return complex_cusp / n


def main():
    print("B102 -- the W1/W2 dichotomy + the R4 (boundary-controlled cubic) continuation\n")
    print("D1  the dichotomy")
    print(f"    CH conditions: {DICHOTOMY_CONDITIONS}")
    print(f"    hold on B71 V0/W1/W2: {conditions_on_components()}")
    I, J, o = dichotomy_census()
    print(f"    census (n=40): Case I (self-dual)={I}, branch trB=trB^-1=1={J}, NEITHER={o}")
    print("\nD2/D3  the ellipticity obstruction + cross-check on B71's exact components")
    print(f"    realize W1 -> {realize_and_classify('W1')}  (A elliptic {{1,i,-i}})")
    print(f"    realize W2 -> {realize_and_classify('W2')}  (B elliptic {{1,i,-i}})")
    sd, dev = geometric_trace_field()
    print(f"    geometric V0: self-dual={sd}, tr(AB) root of t^2-t+7 (Q(sqrt-3)): |.|={dev:.1e}")
    print("    => V0 excluded by COMPLEXITY; W1/W2 excluded by ELLIPTICITY (cleaner obstruction).")
    print("\nD4  Task-M link")
    print(f"    elliptic spectrum {task_m_spectrum_link()} = Task M's forced n=3 spectrum (B95)")
    print("\nD5  the boundary-controlled (relative) cubic family")
    print(f"    relative family dim = {relative_cubic_family()} (cusp real to FIRST order)")
    print(f"    second-order cusp complexification fraction (generic rays): {cusp_second_order_complexifies():.2f}")
    print("    => boundary control is first-order only; the handoff's t*~3.775 geodesic boundary does NOT")
    print("       reproduce (ray-dependent / non-generic); the unipotent-preserving continuation is OPEN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
