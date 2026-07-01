"""B106 -- the trace-map at the DEHN-FILLING fixed points: Jacobian, eigenvalue anatomy, census completion.

The third class of trace-map fixed points, never computed. The Jacobian was computed at the TRIVIAL rep
(the Dickson tower, B89-T) and the GEOMETRIC rep (the adjoint torsion, B98/B99); here it is computed at the
DEHN-FILLING reps (where degree=rank lives). The Dehn-filling reps are IRREDUCIBLE, so -- unlike the
degenerate trivial rep -- the trace-coordinate Jacobian is clean (no eps-series rank-drop).

D1 -- THE JACOBIAN (raw data; the GATE). The figure-eight trace map T_1^2 (a->aba, b->ab) at the Dehn-filling
   fixed point has a stability signature DISTINCT from the trivial and geometric reps:
     - trivial (tower):    hyperbolic saddle (real eigenvalues = the Dickson tower);
     - geometric (torsion): saddle with COMPLEX eigenvalues (twisted Alexander);
     - Dehn-filling:        PARTIALLY ELLIPTIC -- many eigenvalues on the unit circle (roots of unity),
                            with few hyperbolic directions. SL(3) W1/W2: 1 stable, 1 unstable, 6 neutral;
                            SL(4) principal/secondary: 4 stable, 4 unstable, 7 neutral.
   HONEST NEGATIVE: the stability TYPE does NOT encode the exponent -- both SL(4) components are 4-4-7, yet
   the principal has exponent 4 and the secondary 3. So the degree=rank exponent is NOT read off the Jacobian
   signature; no mechanism is claimed (the hinge test is not met by stability).

D4 -- THE EIGENVALUE ANATOMY (high precision). mu (meridian) and [A,B] (longitude) COMMUTE on the
   Dehn-filling components; simultaneously diagonalized, the paired (M_i, L_i) satisfy, PER EIGENVECTOR,
     L_i = c * M_i^k,   c a root of unity,
   verified to ~1e-10 or better: SL(3) W1 (k=3, c=1), W2 (k=-3, c=1); SL(4) principal (k=4, c=-1),
   secondary (k=3, c=i). So the degree=rank relation holds eigenvector-by-eigenvector, with the B89/B88
   scalar c. The secondary's M_i differ from the principal's (different A-spectrum).

D3 -- THE CENSUS COMPLETION. On the two SL(4) components, M^4=L (principal, c^4=1) and M^3=L (secondary)
   hold; the CONJUGATE relations M^4*L=1 and M^3*L=1 are ABSENT on both (devs O(1)). (At SL(3), by contrast,
   W1 gives M^3=L and W2 the conjugate M^3*L=1.) Exhaustiveness over all rank-4 spectra needs the symbolic
   Fix(T_1^2) -- open.

Standalone low-dim topology / trace-map dynamics. NO physics (the Jacobian eigenvalues are MATHEMATICAL
data); no Origin-core claim; P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import itertools
import pathlib

import numpy as np
from scipy.linalg import expm

_ROOT = pathlib.Path(__file__).resolve().parents[2]
inv = np.linalg.inv
_W = np.exp(2j * np.pi / 3)


def _load(mod, rel):
    s = importlib.util.spec_from_file_location(mod, _ROOT / rel)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def _b71():
    return _load("b71", "frontier/B71_sl3_apoly/probe.py")


def _per():
    return _load("per", "frontier/B71_sl3_apoly/peripheral.py")


def _df():
    return _load("df", "frontier/B73_sl4_apoly/dehn_filling.py")


def _jc():
    return _load("jc", "frontier/B58_phaseA/jacobian_closure.py")


SL4_SPECTRA = {"principal": [1, 1, _W, _W ** 2], "secondary": [np.exp(1j * np.pi / 4 * j) for j in (1, 3, 5, 7)]}
SL4_EXPONENT = {"principal": 4, "secondary": 3}


# ---------------------------------------------------------------------------
# D1 -- the trace-map Jacobian at the Dehn-filling fixed points
# ---------------------------------------------------------------------------
def _stability(ev, tol=1e-3):
    mags = np.abs(ev)
    return (int(np.sum(mags < 1 - tol)), int(np.sum(mags > 1 + tol)), int(np.sum(np.abs(mags - 1) < tol)))


def sl3_dehn_jacobian(component, p=2.3, q=3.1):
    """The 8x8 Jacobian of the SL(3) figure-eight trace map T_1^2 at the W1/W2 Dehn-filling fixed point.
    Returns (eigenvalues, (n_stable, n_unstable, n_neutral))."""
    b71, per = _b71(), _per()
    gen = {"W1": per.W1, "W2": per.W2}[component]
    coords = np.array(gen(p, q), dtype=complex)
    T = lambda c: np.array(b71.T1_sq(c), dtype=complex)
    h = 1e-6; J = np.zeros((8, 8), complex)
    for j in range(8):
        e = np.zeros(8, complex); e[j] = h
        J[:, j] = (T(coords + e) - T(coords - e)) / (2 * h)
    ev = np.linalg.eigvals(J)
    return ev, _stability(ev)


def _cvec(A, B, words):
    g = {"a": A, "b": B, "A": inv(A), "B": inv(B)}
    out = []
    for w in words:
        M = np.eye(A.shape[0], dtype=complex)
        for ch in w:
            M = M @ g[ch]
        out.append(np.trace(M))
    return np.array(out)


def sl4_dehn_jacobian(component):
    """The 15x15 Jacobian of the SL(4) figure-eight trace map at the irreducible Dehn-filling rep (computed
    on the character-variety tangent: J = d(c o sigma) . pinv(dc), sigma(A,B)=(ABA,AB)). Returns (eigenvalues,
    stability)."""
    df, jc = _df(), _jc()
    A, B, t = df.realize_bundle_rep(np.array(SL4_SPECTRA[component]), seed=0)
    basis = [np.array(b, dtype=complex) for b in jc.basis_sln(4)]
    pool = ["".join(p) for L in range(1, 5) for p in itertools.product("abAB", repeat=L)]
    h = 1e-6
    sigma = lambda A, B: (A @ B @ A, A @ B)

    def dcmat(words, after_sigma=False):
        D = np.zeros((len(words), 30), complex)
        for k, X in enumerate(basis):
            Ap, Am, Bp, Bm = A @ expm(h * X), A @ expm(-h * X), B @ expm(h * X), B @ expm(-h * X)
            if after_sigma:
                D[:, k] = (_cvec(*sigma(Ap, B), words) - _cvec(*sigma(Am, B), words)) / (2 * h)
                D[:, 15 + k] = (_cvec(*sigma(A, Bp), words) - _cvec(*sigma(A, Bm), words)) / (2 * h)
            else:
                D[:, k] = (_cvec(Ap, B, words) - _cvec(Am, B, words)) / (2 * h)
                D[:, 15 + k] = (_cvec(A, Bp, words) - _cvec(A, Bm, words)) / (2 * h)
        return D
    Dall = dcmat(pool)
    chosen, cur = [], np.zeros((0, 30), complex)        # QR-pivot 15 words to full rank at THIS rep
    for i in range(len(pool)):
        test = np.vstack([cur, Dall[i]])
        if np.linalg.matrix_rank(test, tol=1e-6) > cur.shape[0]:
            chosen.append(pool[i]); cur = test
        if len(chosen) == 15:
            break
    dc, dcs = dcmat(chosen), dcmat(chosen, after_sigma=True)
    J = dcs @ np.linalg.pinv(dc)
    ev = np.linalg.eigvals(J)
    return ev, _stability(ev)


def d1_neutral_eigenvalues_are_roots_of_unity(seeds=(0, 1, 2)):
    """[V93 hygiene] The SL(4) Dehn-filling Jacobian's NEUTRAL eigenvalues (|.|=1) are EXACTLY roots of unity
    and seed-stable -- NOT gauge noise from the pinv at the repeated-eigenvalue rep (the B84 lesson). Returns,
    per component, the sorted multiset of neutral-eigenvalue angles/(2*pi) and whether they are stable across
    the realize seeds. (The realize seed varies the point B on the component; the elliptic/root-of-unity
    neutral angles are invariant, only the hyperbolic pair moves.)"""
    df, jc = _df(), _jc()
    out = {}
    for comp in ("principal", "secondary"):
        per_seed = []
        for sd in seeds:
            A, B, t = df.realize_bundle_rep(np.array(SL4_SPECTRA[comp]), seed=sd)
            ev = _sl4_jacobian_from_rep(A, B, jc)
            # Neutrality window 1e-4, NOT 1e-2: the genuine neutral eigenvalues sit
            # within ~1e-5 of the unit circle at every realize seed, while a moving
            # HYPERBOLIC pair can pass as close as ~7e-3 (principal, seed 1) -- a
            # 1e-2 window captures it and pollutes the angle set with non-root-of-
            # unity angles. (Audit fix 2026-07-01; measured separation >= 2 orders
            # of magnitude on each side of 1e-4.)
            ang = sorted(round(float(np.angle(e) / (2 * np.pi)), 3) for e in ev if abs(abs(e) - 1) < 1e-4)
            # are they all rational p/q with q<=6 (roots of unity)?
            rou = all(min(abs(a - k / q) for q in range(1, 7) for k in range(-q, q + 1)) < 1e-3 for a in ang)
            per_seed.append((tuple(ang), rou))
        angles0 = per_seed[0][0]
        out[comp] = {"angles_over_2pi": list(angles0), "all_roots_of_unity": all(r for _, r in per_seed),
                     "seed_stable": all(s[0] == angles0 for s in per_seed)}
    return out


def _sl4_jacobian_from_rep(A, B, jc):
    basis = [np.array(b, dtype=complex) for b in jc.basis_sln(4)]
    pool = ["".join(p) for L in range(1, 5) for p in itertools.product("abAB", repeat=L)]
    h = 1e-6
    sigma = lambda A, B: (A @ B @ A, A @ B)

    def dcmat(words, after_sigma=False):
        D = np.zeros((len(words), 30), complex)
        for k, X in enumerate(basis):
            Ap, Am, Bp, Bm = A @ expm(h * X), A @ expm(-h * X), B @ expm(h * X), B @ expm(-h * X)
            if after_sigma:
                D[:, k] = (_cvec(*sigma(Ap, B), words) - _cvec(*sigma(Am, B), words)) / (2 * h)
                D[:, 15 + k] = (_cvec(*sigma(A, Bp), words) - _cvec(*sigma(A, Bm), words)) / (2 * h)
            else:
                D[:, k] = (_cvec(Ap, B, words) - _cvec(Am, B, words)) / (2 * h)
                D[:, 15 + k] = (_cvec(A, Bp, words) - _cvec(A, Bm, words)) / (2 * h)
        return D
    Dall = dcmat(pool)
    chosen, cur = [], np.zeros((0, 30), complex)
    for i in range(len(pool)):
        test = np.vstack([cur, Dall[i]])
        if np.linalg.matrix_rank(test, tol=1e-6) > cur.shape[0]:
            chosen.append(pool[i]); cur = test
        if len(chosen) == 15:
            break
    return np.linalg.eigvals(dcmat(chosen, True) @ np.linalg.pinv(dcmat(chosen)))


def jacobian_stability_does_not_encode_exponent():
    """HONEST NEGATIVE: both SL(4) Dehn-filling components have the SAME stability signature (4,4,7), yet the
    principal exponent is 4 and the secondary 3 -- the exponent is NOT read off the Jacobian."""
    sp = sl4_dehn_jacobian("principal")[1]
    se = sl4_dehn_jacobian("secondary")[1]
    return sp, se, (sp == se)


# ---------------------------------------------------------------------------
# D4 -- eigenvalue anatomy: per-eigenvector L_i = c * M_i^k
# ---------------------------------------------------------------------------
def _anatomy(mu, comm, k):
    mu, comm = np.array(mu, complex), np.array(comm, complex)
    w, V = np.linalg.eig(mu); Vi = inv(V)
    Cd = Vi @ comm @ V; L = np.diag(Cd)
    offdiag = float(np.max(np.abs(Cd - np.diag(L))))
    Mk = w ** k; cvals = L / Mk; c = np.mean(cvals)
    return {"commute_offdiag": offdiag, "c": complex(c), "c_to_k": complex(c ** k),
            "per_eigenvector_dev": float(np.max(np.abs(L - c * Mk)))}


def eigenvalue_anatomy(component):
    """Per-eigenvector L_i = c * M_i^k on a Dehn-filling component (mu and [A,B] commute). Returns the dict
    with c, c^k, the commute residual, and the max per-eigenvector deviation."""
    if component in ("W1", "W2"):
        per = _per(); gen = {"W1": per.W1, "W2": per.W2}[component]; k = 3 if component == "W1" else -3
        A, B = per.realize(gen(2.3, 3.1)); mu, _ = per.meridian(A, B)
    else:
        df = _df(); k = SL4_EXPONENT[component]
        A, B, t = df.realize_bundle_rep(np.array(SL4_SPECTRA[component]), seed=0); mu = inv(A) @ t
    comm = A @ B @ inv(A) @ inv(B)
    r = _anatomy(mu, comm, k); r["k"] = k
    return r


# ---------------------------------------------------------------------------
# D3 -- the SL(4) census completion: M^k = L  vs  M^k * L = 1
# ---------------------------------------------------------------------------
def _scalar_dev(M):
    c = np.trace(M) / M.shape[0]
    return float(np.max(np.abs(M - c * np.eye(M.shape[0])))), complex(c)


def census_relations(component):
    """For the SL(4) component: deviations of M^k=L ([A,B] mu^-k scalar) and the conjugate M^k L=1
    ([A,B] mu^k scalar) for k=3,4. Returns a dict of (relation -> (dev, c))."""
    df = _df()
    A, B, t = df.realize_bundle_rep(np.array(SL4_SPECTRA[component]), seed=0)
    mu = inv(A) @ t; comm = A @ B @ inv(A) @ inv(B)
    out = {}
    for k in (3, 4):
        out[f"M^{k}=L"] = _scalar_dev(comm @ np.linalg.matrix_power(inv(mu), k))
        out[f"M^{k}L=1"] = _scalar_dev(comm @ np.linalg.matrix_power(mu, k))
    return out


def main():
    print("B106 -- the trace map at the DEHN-FILLING fixed points (the third class)\n")
    print("D1 -- the Jacobian (stability signature) vs the trivial (tower) and geometric (torsion) reps:")
    for comp in ("W1", "W2"):
        ev, st = sl3_dehn_jacobian(comp)
        print(f"  SL(3) {comp}: stability (stable,unstable,neutral)={st}  |eig|={np.round(np.sort(np.abs(ev)),3)}")
    for comp in ("principal", "secondary"):
        ev, st = sl4_dehn_jacobian(comp)
        print(f"  SL(4) {comp}: stability={st}  |eig|={np.round(np.sort(np.abs(ev)),3)}")
    sp, se, same = jacobian_stability_does_not_encode_exponent()
    print(f"  HONEST NEGATIVE: SL(4) principal {sp} == secondary {se}: {same} -> stability does NOT encode the exponent")
    print("\nD4 -- per-eigenvector L_i = c * M_i^k (c a root of unity), high precision:")
    for comp in ("W1", "W2", "principal", "secondary"):
        r = eigenvalue_anatomy(comp)
        print(f"  {comp:10} k={r['k']:+d}: c={np.round(r['c'],4)} c^k={np.round(r['c_to_k'],3)} "
              f"commute={r['commute_offdiag']:.1e} | per-eigvec |L_i-c M_i^k|={r['per_eigenvector_dev']:.1e}")
    print("\nD3 -- SL(4) census completion (M^k=L vs the conjugate M^k L=1):")
    for comp in ("principal", "secondary"):
        rels = census_relations(comp)
        hits = [r for r, (d, c) in rels.items() if d < 1e-6]
        print(f"  {comp}: holds={hits}; conjugates M^kL=1 absent (devs "
              f"{[round(rels[f'M^{k}L=1'][0],2) for k in (3,4)]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
