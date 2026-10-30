#!/usr/bin/env python3
"""Referee's independent check of B1822 (data-free; no measured number is read).

Shares no code with tnorm.py:
  * theta functions by PRODUCT formulas (Jacobi triple product), validated against mpmath.jtheta;
  * the twisted theta via theta[a,b](z;T) = e^{i pi T a^2 + 2 pi i a (z+b)} theta3(z + aT + b; T), with a reduced mod 1
    (exact: theta[a+1,b] = theta[a,b]);
  * quadrature: each PUNCTURE-CENTRED cell c + {x + t tau : |x|,|t| <= 1/2} cut into four triangles with apex at the
    puncture, Duffy-collapsed (Jacobian u cancels the 1/|z| of |F|^2); Gauss-Legendre n x n per triangle;
  * the four-fold cover C/2L as the union of the four centred cells at c = 0, 1, tau, 1+tau, the integrand evaluated at
    the actual z in each (no transformation law used).
Computes, per twist class:
  N     ||F||^2 on the centred cell (against the arc's stored norm_F2);
  P0    the naive cell Gram on the cell centred at 0 and at 1 (against the arc's stored cell_P0, cell_P0+1 entries);
  COV   A_cov = (1/4) int_{E'} F F^dagger dA, against (||F||^2 / 2) I_2  (the structural fact behind the cover Gram);
        the cover Gram of the frame's blocks (QJ, QI, QK) and of a RANDOM triple of unit quaternions, against
        ||F||^2 * (1/2) tr(C_p^dagger C_q)  (the R^4 Gram of the blocks): the off-diagonal test fails exactly when the
        blocks are not orthonormal quaternions;
  A1    the cell matrix A_cell = int_cell F F^dagger / ||F||^2 and its eigenvalues (why one cell gives ~1);
  MON   r = F1/F0 under z -> z+1, z+tau; |F|^2 periodicity.
And, algebraically (no quadrature): the real dimension of the invariant hermitian forms on C^2 (x) C^3 under
  (i) the flat holonomy alone; (ii) plus the characters on the generation index; (iii) plus a product structure
  h_V (x) h_M; (iv) the diagonal SU(2) (2 (x) adjoint) in which the holonomy lies; (v) SU(2) x SO(3) acting separately;
  and the restriction of each family to the zero modes psi_p = C_p F (x) e_p.
    OMP_NUM_THREADS=1 nice -n 10 python3 -I independent.py
"""
import json, math, pathlib, time, itertools
from fractions import Fraction as Fr
import numpy as np
from numpy.polynomial.legendre import leggauss
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent / "B1822_t_norm_on_the_frames_matter" / "verification" / "tnorm_results.json"
NP = 40                                    # product factors

QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; ONE = np.eye(2, dtype=complex)
BL = [QJ, QI, QK]


def theta1(z, tau):
    z = np.asarray(z, dtype=complex); q = np.exp(1j * np.pi * tau); n = np.arange(1, NP + 1)
    q2n = q ** (2 * n)
    w = np.exp(2j * np.pi * z)[..., None]
    prod = np.prod((1 - q2n) * (1 - q2n * w) * (1 - q2n / w), -1)
    return 2 * np.exp(1j * np.pi * tau / 4) * np.sin(np.pi * z) * prod


def theta3(u, T):
    u = np.asarray(u, dtype=complex); Q = np.exp(1j * np.pi * T); n = np.arange(1, NP + 1)
    w = np.exp(2j * np.pi * u)[..., None]
    return np.prod((1 - Q ** (2 * n)) * (1 + Q ** (2 * n - 1) * w) * (1 + Q ** (2 * n - 1) / w), -1)


def theta_ab(a, b, z, T):
    a = float(Fr(a) % 1); b = float(b); z = np.asarray(z, dtype=complex)
    return np.exp(1j * np.pi * T * a * a + 2j * np.pi * a * (z + b)) * theta3(z + a * T + b, T)


def density(a, b, tau, z):
    """P = F F^dagger as (P00, P11, P10 = F1 conj F0), branch-free:
    F0 = X0/s0, F1 = X1/s1, s0 s1 = den := i e^{-i pi tau/2} e^{-i pi z} th1(z) (a global square root of th1(z) th1(z+tau));
    1/(s1 conj s0) = th1(z)/(|th1(z)| den)."""
    T = 2 * tau
    X0 = theta_ab(a, b, z, T); X1 = np.exp(1j * np.pi * float(b)) * theta_ab(a, b, z + tau, T)
    t0 = theta1(z, tau); t1 = theta1(z + tau, tau)
    den = 1j * np.exp(-1j * np.pi * tau / 2) * np.exp(-1j * np.pi * z) * t0
    return np.abs(X0) ** 2 / np.abs(t0), np.abs(X1) ** 2 / np.abs(t1), X1 * np.conj(X0) * t0 / (np.abs(t0) * den)


def mat_density(a, b, tau, z):
    P00, P11, P10 = density(a, b, tau, z)
    P = np.empty(z.shape + (2, 2), dtype=complex)
    P[..., 0, 0] = P00; P[..., 1, 1] = P11; P[..., 1, 0] = P10; P[..., 0, 1] = np.conj(P10)
    return P


def cell_integral(a, b, tau, c, n):
    """int over the cell centred at lattice point c of F F^dagger dA (a 2x2 matrix), four apex triangles"""
    V = [0.5 + 0.5 * tau, -0.5 + 0.5 * tau, -0.5 - 0.5 * tau, 0.5 - 0.5 * tau, 0.5 + 0.5 * tau]
    x, w = leggauss(n); u = 0.5 * (x + 1); wu = 0.5 * w
    U, Vv = np.meshgrid(u, u, indexing="ij"); W = np.outer(wu, wu)
    tot = np.zeros((2, 2), dtype=complex)
    for k in range(4):
        P0, P1 = V[k], V[k + 1]
        J = abs((np.conj(P0) * (P1 - P0)).imag)          # |det| of the (real) map (u, v) -> u (P0 + v (P1 - P0))
        z = c + U * (P0 + Vv * (P1 - P0))
        M = mat_density(a, b, tau, z)
        tot += np.einsum("ij,ijab->ab", W * U * J, M)
    return tot


def validate_thetas():
    mp.mp.dps = 30; worst = 0.0
    for tau in (0.3 + 1.2j, 0.85 + 3.45j, 0.3 + 6j):
        q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag))
        for z in (0.23 + 0.31 * tau, -0.4 + 1.3 * tau, 0.7 + 2.4 * tau):
            ref1 = complex(mp.jtheta(1, mp.pi * mp.mpc(z.real, z.imag), q))
            mine1 = complex(theta1(np.array(z), tau))
            T = 2 * tau; Q = mp.exp(1j * mp.pi * mp.mpc(T.real, T.imag))
            ref3 = complex(mp.jtheta(3, mp.pi * mp.mpc(z.real, z.imag), Q)); mine3 = complex(theta3(np.array(z), T))
            worst = max(worst, abs(mine1 / ref1 - 1), abs(mine3 / ref3 - 1))
    return worst


def monodromy(a, b, tau, rng):
    zs = rng.uniform(-0.45, 0.45, 16) + rng.uniform(-0.45, 0.45, 16) * tau
    def ratio(z):
        P00, P11, P10 = density(a, b, tau, z)
        return P10 / P00, P00 + P11            # r = F1/F0 = P10/P00 ; |F|^2
    r, n = ratio(zs); r1, n1 = ratio(zs + 1); rt, nt = ratio(zs + tau)
    return {"max |r(z+1) + r(z)|/|r|": float(np.max(np.abs(r1 + r) / np.abs(r))),
            "r(z+tau) r(z) (mean)": [float(np.mean(rt * r).real), float(np.mean(rt * r).imag)],
            "spread of r(z+tau) r(z)": float(np.max(np.abs(rt * r - np.mean(rt * r)))),
            "|F|^2 periodic, max rel": float(max(np.max(np.abs(n1 / n - 1)), np.max(np.abs(nt / n - 1))))}


def random_unit_quaternions(rng, k):
    out = []
    for _ in range(k):
        v = rng.normal(size=4); v /= np.linalg.norm(v)
        out.append(v[0] * ONE + v[1] * QI + v[2] * QJ + v[3] * QK)
    return out


def classes_from_arc():
    R = json.loads(ARC.read_text()); G = R["G_results"]; M = R["G_config_to_class"]
    want = ["Q|zero|1j", "e|2/5,3/10|(0.35+2.75j)", "u|ord7 2/7,3/7|(0.85+3.45j)", "L|ord12 5/12,1/12|(0.3+6j)",
            "d|ord9 1/9,1/9|(0.05+2.05j)", "Q|ord4 0,1/4|(0.3+6j)", "e|ord3 1/3,2/3|(0.5+4j)", "u|2/5,7/10|(0.25+1j)"]
    return [(w, G[M[w]]) for w in want]


# ---------------------------------------------------------------- algebra: invariant hermitian forms
def herm_basis(n):
    B = []
    for i in range(n):
        E = np.zeros((n, n), dtype=complex); E[i, i] = 1; B.append(E)
    for i in range(n):
        for j in range(i + 1, n):
            E = np.zeros((n, n), dtype=complex); E[i, j] = E[j, i] = 1; B.append(E)
            E = np.zeros((n, n), dtype=complex); E[i, j] = 1j; E[j, i] = -1j; B.append(E)
    return B


def invariant_forms(gens, n, extra_linear=None):
    """real basis of hermitian X with g^dagger X g = X for g in gens (and extra linear constraints), via SVD null space"""
    B = herm_basis(n); cols = []
    for E in B:
        parts = [(g.conj().T @ E @ g - E).ravel() for g in gens]
        if extra_linear is not None: parts.append(extra_linear(E).ravel())
        v = np.concatenate(parts); cols.append(np.concatenate([v.real, v.imag]))
    A = np.array(cols).T; U_, s, Vh = np.linalg.svd(A)
    rank = int(np.sum(s > 1e-9 * s.max())); null = Vh[rank:]
    return [sum(c * E for c, E in zip(vec, B)) for vec in null]


def restrict_to_modes(X):
    """H_pq = (psi_p, X psi_q)/|F|^2 averaged over the direction of F (the modes' Gram for the form X, with the cover-
    averaged F F^dagger = |F|^2/2 I_2): H_pq = (1/2) tr(C_p^dagger X_pq C_q)"""
    return np.array([[0.5 * np.trace(BL[p].conj().T @ X[2 * p:2 * p + 2, 2 * q:2 * q + 2] @ BL[q]) for q in range(3)] for p in range(3)])


def adjoint_on_blocks(g):
    """R(g)_qp with g C_p g^-1 = sum_q R_qp C_q, in the frame's block basis (QJ, QI, QK)"""
    R = np.zeros((3, 3), dtype=complex)
    for p in range(3):
        Y = g @ BL[p] @ np.linalg.inv(g)
        for q in range(3): R[q, p] = 0.5 * np.trace(BL[q].conj().T @ Y)
    return R


def algebra(rng):
    out = {}
    Phi = {"1": QI, "tau": QJ}
    chi = {}
    for p, C in zip("jik", BL):
        chi[p] = tuple(int(round((0.5 * np.trace(C @ P @ np.linalg.inv(C) @ np.linalg.inv(P))).real)) for P in (QI, QJ))
    out["characters (chi(1), chi(tau)) in block order j, i, k"] = chi
    # the rank-6 holonomy in the arc's ordering (generation outer, doublet inner), with arbitrary U(1) phases
    ph = np.exp(1j * rng.uniform(0, 2 * np.pi, 2))
    rho6 = [ph[k] * np.kron(np.diag([chi[p][k] for p in "jik"]).astype(complex), P) for k, P in enumerate((QI, QJ))]
    fam = invariant_forms(rho6, 6); out["(i) flat holonomy alone: real dim"] = len(fam)
    # every member restricted to the modes, and the claim G = H |F|^2 with X_pq = H_pq C_p C_q^-1
    Hs = [restrict_to_modes(X) for X in fam]
    worst = 0.0
    for X, H in zip(fam, Hs):
        Xr = np.block([[H[p, q] * BL[p] @ np.linalg.inv(BL[q]) for q in range(3)] for p in range(3)])
        worst = max(worst, float(np.max(np.abs(X - Xr))))
    out["(i) every invariant form is X_pq = H_pq C_p C_q^-1 (max residual)"] = worst
    out["(i) span of the restricted H's (real dim)"] = int(np.linalg.matrix_rank(np.array([np.concatenate([H.real.ravel(), H.imag.ravel()]) for H in Hs]), tol=1e-9))
    flav = [np.kron(np.diag([chi[p][k] for p in "jik"]).astype(complex), np.eye(2)) for k in range(2)]
    out["(ii) plus the characters on the generation index: real dim"] = len(invariant_forms(rho6 + flav, 6))
    # (iii) product structure X = h_M (x) h_V: Schur on a diagonal block forces h_V ~ I_2; then count the invariant h_M
    hV = np.eye(2); diag_ok = []
    for hM in herm_basis(3):
        X = np.kron(hM, hV); diag_ok.append(all(np.allclose(g.conj().T @ X @ g, X) for g in rho6))
    out["(iii) product forms h_M (x) I_2 invariant: real dim of the surviving h_M (diagonal only)"] = int(sum(diag_ok))
    # (iv) diagonal SU(2): g (x) R(g) acting as (generation outer, doublet inner) = kron(R(g), g)
    gs = []
    for _ in range(4):
        v = rng.normal(size=4); v /= np.linalg.norm(v); g = v[0] * ONE + v[1] * QI + v[2] * QJ + v[3] * QK
        gs.append(np.kron(adjoint_on_blocks(g), g))
    # consistency: is the flat holonomy inside this diagonal SU(2)?  rho6 / phase == kron(R(Phi), Phi)
    inside = max(float(np.max(np.abs(np.kron(adjoint_on_blocks(P), P) - rho6[k] / ph[k]))) for k, P in enumerate((QI, QJ)))
    out["(iv) the holonomy lies in the diagonal SU(2) (2 (x) adjoint): residual"] = inside
    famD = invariant_forms(gs, 6); out["(iv) diagonal SU(2): real dim"] = len(famD)
    out["(iv) restricted to the modes (each basis form, H/trace)"] = [np.round(restrict_to_modes(X) / np.trace(restrict_to_modes(X)) * 3, 10).real.tolist() for X in famD]
    # (v) SU(2) x SO(3) acting separately: kron(R(h), g) with independent g, h
    gs2 = []
    for _ in range(4):
        v = rng.normal(size=4); v /= np.linalg.norm(v); g = v[0] * ONE + v[1] * QI + v[2] * QJ + v[3] * QK
        w = rng.normal(size=4); w /= np.linalg.norm(w); h = w[0] * ONE + w[1] * QI + w[2] * QJ + w[3] * QK
        gs2.append(np.kron(adjoint_on_blocks(h), g))
    out["(v) SU(2) x SO(3) separately: real dim"] = len(invariant_forms(gs2, 6))
    # (vi) the Q8 outer automorphism of order 3, realised as conjugation by the 2T element u = (1+i+j+k)/2 on the doublet
    # together with the induced permutation of the blocks: Z = kron(R(u), u) (R(u) a permutation, up to signs, of j, i, k)
    u = 0.5 * (ONE + QI + QJ + QK); Ru = adjoint_on_blocks(u)
    out["(vi) R(u) on the blocks (j, i, k)"] = np.round(Ru.real, 12).tolist()
    Z = np.kron(Ru, u)
    out["(vi) flat holonomy + Z (order-3 automorphism) : real dim"] = len(invariant_forms(rho6 + [Z], 6))
    out["(vi) flat holonomy + characters + Z : real dim"] = len(invariant_forms(rho6 + flav + [Z], 6))
    return out


def main():
    t0 = time.time(); rng = np.random.default_rng(1822)
    R = {"what": "referee's independent check of B1822; data-free", "theta product formulas vs mpmath.jtheta, max rel": validate_thetas()}
    print("thetas", R["theta product formulas vs mpmath.jtheta, max rel"], flush=True)
    R["algebra"] = algebra(rng); print(json.dumps(R["algebra"], indent=1, default=str), flush=True)
    rows = []; Qr = random_unit_quaternions(rng, 3)
    for w, g in classes_from_arc():
        a, b = Fr(g["a"]), Fr(g["b"]); tau = complex(*g["tau"])
        row = {"config": w, "class": g["key"], "a": g["a"], "b": g["b"], "tau": g["tau"]}
        row["monodromy"] = monodromy(a, b, tau, rng)
        res = {}
        for n in (32, 48):
            cells = {nm: cell_integral(a, b, tau, c, n) for nm, c in (("0", 0), ("1", 1), ("tau", tau), ("1+tau", 1 + tau))}
            res[n] = cells
        c0 = res[48]["0"]; nF = float(np.trace(c0).real)
        row["norm_F2 (mine, n=48)"] = nF; row["norm_F2 (arc)"] = g["cover"]["norm_F2"]; row["norm rel diff"] = abs(nF / g["cover"]["norm_F2"] - 1)
        row["norm n=32 vs 48"] = abs(np.trace(res[32]["0"]).real / nF - 1)
        # naive cell Grams
        def cellgram(A, blocks):
            return np.array([[np.trace(blocks[p].conj().T @ blocks[q] @ A) for q in range(3)] for p in range(3)])
        G0 = cellgram(c0, BL) / nF; G1 = cellgram(res[48]["1"], BL) / nF
        mine0 = {"ji": G0[0, 1], "jk": G0[0, 2], "ik": G0[1, 2]}; mine1 = {"ji": G1[0, 1], "jk": G1[0, 2], "ik": G1[1, 2]}
        arc0 = g["cell_P0"]["offdiag_entries_normalised"]; arc1 = g["cell_P0+1"]["offdiag_entries_normalised"]
        # the arc's class rep may differ from my reduction by b -> b + integer: entries agree up to the sign pattern diag(1,-1,1)
        d0 = max(min(abs(mine0[e] - complex(*arc0[e])), abs(mine0[e] + complex(*arc0[e]))) for e in mine0)
        d1 = max(min(abs(mine1[e] - complex(*arc1[e])), abs(mine1[e] + complex(*arc1[e]))) for e in mine1)
        row["cell P0 entries (mine)"] = {e: [round(v.real, 12), round(v.imag, 12)] for e, v in mine0.items()}
        row["cell P0 entries: max |mine - arc| (up to the b-shift sign)"] = d0
        row["cell P0+1 entries: max |mine - arc| (up to the b-shift sign)"] = d1
        row["sign flip I(P0+1) = chi(1) I(P0): residual"] = max(abs(G1[p, q] - BLchi1[p] * BLchi1[q] * G0[p, q]) for p in range(3) for q in range(3) if p != q)
        # cover
        Acov = sum(res[48].values()) / 4
        row["A_cov/|F|^2 - I/2 (max abs)"] = float(np.max(np.abs(Acov / nF - 0.5 * np.eye(2))))
        row["A_cov n=32 vs 48 (max abs, /|F|^2)"] = float(np.max(np.abs(sum(res[32].values()) / 4 - Acov)) / nF)
        Gc = cellgram(Acov, BL) / nF
        row["cover Gram, frame's blocks: max |G - I|"] = float(np.max(np.abs(Gc - np.eye(3))))
        Gr = cellgram(Acov, Qr) / nF; Gpred = np.array([[0.5 * np.trace(Qr[p].conj().T @ Qr[q]) for q in range(3)] for p in range(3)])
        row["cover Gram, random unit quaternions: max |G - R^4 Gram|"] = float(np.max(np.abs(Gr - Gpred)))
        row["random blocks' largest |off-diagonal| (shows the test can fail)"] = float(max(abs(Gpred[p, q]) for p in range(3) for q in range(3) if p != q))
        ev = np.linalg.eigvalsh(c0 / nF)
        row["A_cell(P0)/|F|^2 eigenvalues"] = [float(e) for e in ev]
        rows.append(row)
        print(json.dumps({k: row[k] for k in ("config", "norm rel diff", "cell P0 entries: max |mine - arc| (up to the b-shift sign)",
                                              "cell P0+1 entries: max |mine - arc| (up to the b-shift sign)", "A_cov/|F|^2 - I/2 (max abs)",
                                              "cover Gram, frame's blocks: max |G - I|", "cover Gram, random unit quaternions: max |G - R^4 Gram|",
                                              "A_cell(P0)/|F|^2 eigenvalues")}, default=str), flush=True)
    R["rows"] = rows; R["seconds"] = round(time.time() - t0, 1)
    json.dump(R, open(HERE / "independent.json", "w"), indent=1, default=str)
    print("done", R["seconds"], "s", flush=True)


BLchi1 = [-1, 1, -1]          # chi_p(1) for blocks (QJ, QI, QK)
if __name__ == "__main__":
    main()
