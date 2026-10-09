#!/usr/bin/env python3
"""B1635 -- THE COUPLINGS IN TAU ALONE ON THE RULED BRANCH (the SM seat's W50 section 3 on main) AND THE FIRST COUNT.  On the
ruled branch the weave's residual at a generic tau is scalars (B1634), so a coupling in tau alone is a vector-valued modular
form for the tensor representation built from rho = rho_theta (B1634: the weave's own lift, exactly the multiplier of
eta^21 (theta_2^2, theta_3^2, theta_4^2)).  Main's own route, independent of the seat's q-expansion code and of the
Borcherds-Skoruppa formula (which is run beside it as the cross-check):
  T (x) T  (Y -> rho^-T Y rho^-1, odd weight k):  W = eta^18 Y is a 3x3 matrix of degree-(k+9) polynomials in
           u = (theta_2^2, theta_3^2, theta_4^2) modulo u_3^2 = u_2^2 + u_4^2 with W(A u) = A^-T W(u) A^-1 (A the weight-one
           multiplier of u), every entry vanishing below q^(3/4); pieces D (diagonal), O+ (symmetric off-diagonal),
           O- (antisymmetric) in the theta basis (= the parity basis up to B1634's monomial map).
  Tbar (x) T (Y -> rho Y rho^-1, even weight k):  Y a matrix of degree-k polynomials with Y(A u) = A Y(u) A^-1.
 K1  dim by piece, T (x) T, k = 1, 3, ..., 11: algebraic = formula.
 K2  dim, Tbar (x) T, k = 0, 2, ..., 10: algebraic = formula.
 K3  at three generic tau, every coupling of a single piece with k <= 7 (each basis element), and five random
     combinations of D (+) O+ at k = 5 and 7: singular values, smallest relative gap.
 K4  the seat's N5 at tau0 = 0.17 + 1.13i with main's own forms: (a) O+ at k = 3 against D at k = 5; (c) D at k = 5
     against k = 7; V = U1^H U2 from the left singular vectors; distance from the permutations = min over the six P of
     max ||V_ij| - P_ij| (the seat's metric).
 K5  at tau = i and tau = omega: the same couplings as K3 -- which are degenerate (smallest relative gap < 1e-6).
 K6  the count: free real numbers for sectors at weights k_s = 2 (tau) + sum_s (2 d(k_s) - 1), d the coupling dimension
     (symmetric D (+) O+ for a Majorana-type sector, full T (x) T for a Dirac sector of two T fields, Tbar (x) T for a Dirac
     sector of T and Tbar); and for the lowest two-sector choice (O+ at k = 1 against O+ at k = 3, d = 1 each): masses
     at generic tau and their mixing.
Writes couplings_on_the_ruled_branch.json."""
import json, pathlib, os, importlib.util, itertools, cmath, math
import numpy as np
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("w45", FRONTIER / "B1632_w45_verified_on_main" / "verification" / "w45_on_main.py")
w45 = importlib.util.module_from_spec(spec); spec.loader.exec_module(w45)
I = 1j
# rho_theta (B1634), theta basis (theta_2^2, theta_3^2, theta_4^2)
P13 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=complex); P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
rS = cmath.exp(-23j * math.pi / 4) * P13
rT = cmath.exp(7j * math.pi / 4) * np.diag([1j, 1, 1]) @ P23
# A: u(-1/tau) = tau A_S u(tau), u(tau + 1) = A_T u(tau)
A_S = -1j * P13
A_T = np.diag([1j, 1, 1]) @ P23
TAU0 = complex(0.17, 1.13)
GENERIC = [TAU0, complex(0.31, 0.97), complex(-0.23, 1.41)]
OMEGA = complex(-0.5, math.sqrt(3) / 2)


# ---- polynomials in u modulo u3^2 = u2^2 + u4^2 (normal form: u3 exponent <= 1); keys (a2, a3, a4) ----
def pmul(p, q):
    out = {}
    for (a, b, c), x in p.items():
        for (d, e, f), y in q.items():
            key = (a + d, b + e, c + f); out[key] = out.get(key, 0) + x * y
    return reduce_(out)


def reduce_(p):
    out = {}
    stack = list(p.items())
    while stack:
        (a, b, c), x = stack.pop()
        if abs(x) == 0: continue
        if b >= 2:                                           # u3^2 -> u2^2 + u4^2
            stack.append(((a + 2, b - 2, c), x)); stack.append(((a, b - 2, c + 2), x)); continue
        out[(a, b, c)] = out.get((a, b, c), 0) + x
    return {k: v for k, v in out.items() if abs(v) > 1e-14}


def normal_monomials(d):
    return [(a, 0, d - a) for a in range(d + 1)] + [(a, 1, d - 1 - a) for a in range(d)]


def subst(mon, A):
    """the monomial u^mon with u -> A u (A monomial: u_i -> A[i, j] u_j for the one j with A[i, j] != 0)"""
    p = {(0, 0, 0): 1.0 + 0j}
    for i, e in enumerate(mon):
        j = int(np.argmax(np.abs(A[i]))); c = A[i, j]
        lin = {tuple(1 if t == j else 0 for t in range(3)): c}
        for _ in range(e): p = pmul(p, lin)
    return p


def equivariant_space(d, left, right):
    """3x3 matrices W of degree-d polynomials with W(A u) = left(A) W(u) right(A) for A in {A_S, A_T}; returns a basis as
    arrays of shape (n, 3, 3, M) over the normal monomials"""
    mons = normal_monomials(d); M = len(mons); idx = {m: t for t, m in enumerate(mons)}
    nunk = 9 * M
    rows = []
    for A in (A_S, A_T):
        Lm, Rm = left(A), right(A)
        sub = [subst(m, A) for m in mons]                     # each a poly in normal form
        # entry (r, c) of W(Au) - Lm W(u) Rm, coefficient of normal monomial t
        for r in range(3):
            for c in range(3):
                block = np.zeros((M, nunk), dtype=complex)
                for t0, m in enumerate(mons):                 # W_rc(Au): sum_t0 w[r,c,t0] * sub[t0]
                    for key, val in sub[t0].items():
                        block[idx[key], (3 * r + c) * M + t0] += val
                for a in range(3):
                    for b in range(3):
                        coef = Lm[r, a] * Rm[b, c]
                        if coef != 0:
                            for t0 in range(M): block[t0, (3 * a + b) * M + t0] -= coef
                rows.append(block)
    Asys = np.vstack(rows)
    _, s, Vh = np.linalg.svd(Asys)
    rank = int(np.sum(s > 1e-9 * max(1.0, s[0])))
    null = Vh[rank:].conj()
    return null.reshape(-1, 3, 3, M), mons, s


# ---- q-series of u in x = q^(1/8) ----
def u_series(N):
    th2 = np.zeros(N, dtype=object); th3 = np.zeros(N, dtype=object); th4 = np.zeros(N, dtype=object)
    for arr in (th2, th3, th4): arr[:] = 0
    n = 0
    while (2 * n + 1) ** 2 < N: th2[(2 * n + 1) ** 2] += 2; n += 1
    for n in range(-N, N + 1):
        if 4 * n * n < N: th3[4 * n * n] += 1; th4[4 * n * n] += (-1) ** abs(n)
    sq = lambda a: np.array([sum(a[i] * a[k - i] for i in range(k + 1)) for k in range(N)], dtype=object)
    return [sq(th2), sq(th3), sq(th4)]


def series_of_mon(mon, us, N):
    out = np.zeros(N, dtype=object); out[0] = 1
    for i, e in enumerate(mon):
        for _ in range(e):
            out = np.array([sum(out[j] * us[i][k - j] for j in range(k + 1)) for k in range(N)], dtype=object)
    return out


def cusp_condition(basis, mons, order_x, N=16):
    """restrict the span of `basis` to W whose entries vanish below x^order_x (x = q^(1/8))"""
    if basis.shape[0] == 0: return basis
    us = u_series(N); ser = [series_of_mon(m, us, N) for m in mons]
    S = np.array([[complex(ser[t][k]) for t in range(len(mons))] for k in range(order_x)])   # (order_x, M)
    rows = []
    for b in basis:
        rows.append(np.concatenate([(S @ b[r, c]) for r in range(3) for c in range(3)]))
    C = np.array(rows).T                                       # constraints x coefficients-of-basis
    _, s, Vh = np.linalg.svd(C) if C.size else (None, np.array([]), np.eye(basis.shape[0]))
    rank = int(np.sum(s > 1e-9 * max(1.0, s[0] if len(s) else 1.0)))
    comb = Vh[rank:].conj()
    return np.einsum("ij,jrcm->ircm", comb, basis)


def piece_projector(name):
    D = np.zeros((3, 3, 3, 3)); Op = np.zeros((3, 3, 3, 3)); Om = np.zeros((3, 3, 3, 3))
    for r in range(3):
        for c in range(3):
            if r == c: D[r, c, r, c] = 1
            else:
                Op[r, c, r, c] += 0.5; Op[r, c, c, r] += 0.5
                Om[r, c, r, c] += 0.5; Om[r, c, c, r] -= 0.5
    return {"D": D, "O+": Op, "O-": Om}[name]


def restrict_piece(basis, name):
    if basis.shape[0] == 0: return basis
    Pp = piece_projector(name)
    proj = np.einsum("rcab,nabm->nrcm", Pp, basis)
    flat = proj.reshape(proj.shape[0], -1)
    U, s, Vh = np.linalg.svd(flat, full_matrices=False)
    rank = int(np.sum(s > 1e-9 * max(1.0, s[0] if len(s) else 1.0)))
    return Vh[:rank].reshape(rank, 3, 3, basis.shape[3])


def u_eta(tau, N=40):
    t = mp.mpc(tau.real, tau.imag); e = lambda x: mp.exp(1j * mp.pi * t * x)
    th2 = mp.fsum(e((n + mp.mpf(1) / 2) ** 2) for n in range(-N, N))
    th3 = mp.fsum(e(n * n) for n in range(-N, N + 1))
    th4 = mp.fsum((-1) ** abs(n) * e(n * n) for n in range(-N, N + 1))
    eta = mp.exp(1j * mp.pi * t / 12) * mp.fprod(1 - mp.exp(2j * mp.pi * t * n) for n in range(1, 4 * N))
    return [complex(th2 ** 2), complex(th3 ** 2), complex(th4 ** 2)], complex(eta)


def evaluate(b, mons, tau, eta_power):
    u, eta = u_eta(tau)
    vals = np.array([u[0] ** m[0] * u[1] ** m[1] * u[2] ** m[2] for m in mons])
    return (b @ vals) / (eta ** eta_power)


def svals(Y):
    s = np.linalg.svd(Y, compute_uv=False); s = s / s[0] if s[0] > 0 else s
    gaps = [abs(s[i] - s[j]) for i in range(3) for j in range(i + 1, 3)]
    return [round(float(x), 9) for x in s], float(min(gaps))


def perm_distance(V):
    best = 9.0
    for p in itertools.permutations(range(3)):
        P = np.zeros((3, 3)); P[range(3), p] = 1
        best = min(best, float(np.max(np.abs(np.abs(V) - P))))
    return best


def mixing(Y1, Y2):
    U1 = np.linalg.svd(Y1)[0]; U2 = np.linalg.svd(Y2)[0]
    return perm_distance(U1.conj().T @ U2)


def law_check(b, mons, eta_power, act, k, tau=complex(0.29, 1.07)):
    """Y(-1/tau) against tau^k act_S(Y(tau)) and Y(tau + 1) against act_T(Y(tau)); relative errors"""
    Y = evaluate(b, mons, tau, eta_power)
    eS = np.abs(evaluate(b, mons, -1 / tau, eta_power) - tau ** k * act("S", Y)).max() / np.abs(Y).max() / abs(tau) ** k
    eT = np.abs(evaluate(b, mons, tau + 1, eta_power) - act("T", Y)).max() / np.abs(Y).max()
    return float(eS), float(eT)


def main():
    out = {}
    inv = np.linalg.inv
    # T (x) T: Y -> rho^-T Y rho^-1;  W = eta^18 Y, degree k + 9, W(Au) = A^-T W A^-1, vanishing below q^(3/4) = x^6
    actTT = lambda g, Y: (inv(rS).T @ Y @ inv(rS)) if g == "S" else (inv(rT).T @ Y @ inv(rT))
    RS9 = np.kron(inv(rS).T, inv(rS).T); RT9 = np.kron(inv(rT).T, inv(rT).T)
    TT = {}; k1 = {}
    for k in range(1, 12, 2):
        full, mons, _ = equivariant_space(k + 9, lambda A: inv(A).T, lambda A: inv(A))
        hol = cusp_condition(full, mons, 6)
        row = {"allowed": bool(w45.allowed(k, RS9)), "formula_full": round(w45.chi(k, RS9, RT9), 9) if w45.allowed(k, RS9) else None,
               "algebraic_full": int(hol.shape[0])}
        for nm in ("D", "O+", "O-"):
            pb = restrict_piece(hol, nm); TT[(k, nm)] = (pb, mons); row["algebraic_" + nm] = int(pb.shape[0])
        if hol.shape[0]:
            row["law_check_relative_errors"] = law_check(hol[0], mons, 18, actTT, k)
        if k == 1:                                            # bite control: a random, non-equivariant W fails the law
            rnd = np.random.default_rng(7).normal(size=(3, 3, len(mons))) + 0j
            row["control_random_W_law_errors"] = law_check(rnd, mons, 18, actTT, k)
        k1[str(k)] = row
    out["K1_TT_dims"] = k1
    # Tbar (x) T: Y -> rho Y rho^-1 = A Y A^-1, degree k, no cusp condition
    actTbT = lambda g, Y: (rS @ Y @ inv(rS)) if g == "S" else (rT @ Y @ inv(rT))
    RS9b = np.kron(rS, inv(rS).T); RT9b = np.kron(rT, inv(rT).T)
    k2 = {}; TbT = {}
    for k in range(0, 11, 2):
        full, mons, _ = equivariant_space(k, lambda A: A, lambda A: inv(A))
        TbT[k] = (full, mons)
        k2[str(k)] = {"allowed": bool(w45.allowed(k, RS9b)), "formula": round(w45.chi(k, RS9b, RT9b), 9) if w45.allowed(k, RS9b) else None,
                      "algebraic": int(full.shape[0]),
                      "law_check_relative_errors": law_check(full[0], mons, 0, actTbT, k) if full.shape[0] else None}
    b0 = TbT[0][0]
    k2["k0_is_identity"] = bool(b0.shape[0] == 1 and np.allclose(b0[0][:, :, 0] / b0[0][0, 0, 0], np.eye(3), atol=1e-9))
    out["K2_TbarT_dims"] = k2
    # K3 / K5: masses at generic tau, at i and at omega
    rng = np.random.default_rng(1635)
    cases = {}
    for (k, nm), (pb, mons) in TT.items():
        if k <= 7:
            for j in range(pb.shape[0]): cases[f"TT {nm} k={k} #{j}"] = (pb[j], mons, 18)
    for k in (5, 7):
        pb = np.concatenate([TT[(k, "D")][0], TT[(k, "O+")][0]]); mons = TT[(k, "D")][1]
        for sd in range(5):
            c = rng.normal(size=pb.shape[0]) + 1j * rng.normal(size=pb.shape[0])
            cases[f"TT sym generic k={k} seed{sd}"] = (np.einsum("n,nrcm->rcm", c, pb), mons, 18)
    for k in (2, 4, 6):
        pb, mons = TbT[k]
        for j in range(pb.shape[0]): cases[f"TbT k={k} #{j}"] = (pb[j], mons, 0)
    pts = {"generic_" + str(i): t for i, t in enumerate(GENERIC)}; pts["i"] = 1j; pts["omega"] = OMEGA
    k35 = {}
    for name, (b, mons, ep) in cases.items():
        k35[name] = {p: svals(evaluate(b, mons, t, ep)) for p, t in pts.items()}
    out["K3_K5_masses"] = k35
    out["K3_nondegenerate_at_every_generic_point"] = sorted(n for n, r in k35.items() if all(r[f"generic_{i}"][1] > 0.05 for i in range(3)))
    out["K5_degenerate_at_i"] = sorted(n for n, r in k35.items() if r["i"][1] < 1e-6)
    out["K5_degenerate_at_omega"] = sorted(n for n, r in k35.items() if r["omega"][1] < 1e-6)
    out["K5_nondegenerate_at_i"] = sorted(n for n, r in k35.items() if r["i"][1] >= 1e-6)
    out["K5_nondegenerate_at_omega"] = sorted(n for n, r in k35.items() if r["omega"][1] >= 1e-6)
    # K4: the seat's N5 (a) and (c) at tau0
    O3 = TT[(3, "O+")]; D5 = TT[(5, "D")]; D7 = TT[(7, "D")]
    Y = lambda pb, j, t: evaluate(pb[0][j], pb[1], t, 18)
    out["K4"] = {"(a) O+ k=3 vs D k=5": {"dims": [int(O3[0].shape[0]), int(D5[0].shape[0])],
                                        "distance": round(mixing(Y(O3, 0, TAU0), Y(D5, 0, TAU0)), 6) if O3[0].shape[0] and D5[0].shape[0] else None},
                 "(c) D k=5 vs D k=7": {"dims": [int(D5[0].shape[0]), int(D7[0].shape[0])],
                                       "distance": round(mixing(Y(D5, 0, TAU0), Y(D7, 0, TAU0)), 6) if D5[0].shape[0] and D7[0].shape[0] else None}}
    # K6: the count
    d_sym = {k: int(TT[(k, "D")][0].shape[0] + TT[(k, "O+")][0].shape[0]) for k in range(1, 12, 2)}
    d_full = {k: d_sym[k] + int(TT[(k, "O-")][0].shape[0]) for k in range(1, 12, 2)}
    d_tbt = {k: int(TbT[k][0].shape[0]) for k in range(0, 11, 2)}
    O1 = TT[(1, "O+")]
    lowest = {}
    if O1[0].shape[0] == 1 and O3[0].shape[0] == 1:
        for i, t in enumerate(GENERIC):
            Y1, Y3 = Y(O1, 0, t), Y(O3, 0, t)
            lowest[f"generic_{i}"] = {"masses_k1": svals(Y1), "masses_k3": svals(Y3), "mixing_distance": round(mixing(Y1, Y3), 6)}
    out["K6_count"] = {"d_symmetric": d_sym, "d_full_TT": d_full, "d_TbarT": d_tbt,
                       "free_real_numbers": "2 (tau) + sum over sectors of (2 d(k_s) - 1)",
                       "two sectors at the lowest symmetric weights (k = 1, 3)": 2 + (2 * d_sym[1] - 1) + (2 * d_sym[3] - 1),
                       "lowest_two_sector_readout": lowest}
    json.dump(out, open(HERE / "couplings_on_the_ruled_branch.json", "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in out.items() if k != "K3_K5_masses"}, indent=1, default=str)[:6000])


if __name__ == "__main__":
    main()
