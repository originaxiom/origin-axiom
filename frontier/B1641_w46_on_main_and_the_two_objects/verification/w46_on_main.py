#!/usr/bin/env python3
"""B1641 -- W46 ON MAIN, AND THE TWO OBJECTS (sealed before this runs; see PREREGISTRATION.md).

  O1  the inner automorphisms conj(a), conj(b), conj(c) (c = a b^-1 a^-1 b) on V = (+)_p H^1(F2; chi_p (x) rho_Q):
      (i) the record's uniform lift (B1617's lift_of, B1600's move_matrix); (ii) the block-wise geometric lift
      M_p(c) = chi_p(c) rho_Q(c)
  O2  Delta^4 = (L R^-1 L)^4 as the product of the move matrices, restricted to T; conj(c) with the geometric lift on T
  O3  (a) semi-invariants of the parity action in T(x)T and T(x)T(x)T; (b) c = sum over distinct triples in rho_theta's
      coordinates: a one-dimensional subrepresentation of rho_theta^(x3), its character, and c(u, u, u) = 24 eta^6;
      (c) c(., ., u) against B1636's golden coupling
  W1  the six local solutions L6 = (+)_u C^2_u from main's lifts: Mp2(Z) relations, exponents of rho6(T), the commutant
      and the invariant pieces
  W2  chi_1 on the pieces and on L6 for every valid identification; chi_{3/2}(rho_T), chi_{1/2}(rho_T-bar); eta^2
  W3  the table index(Lambda+, n) = -chi_{3/2+12n}(rho_T) + sum chi_{1+12n}(pieces) against n(|Lambda+| - 3)
  H   read-out: does rho_T or rho_T-bar (up to a scalar) occur as a subrepresentation or quotient of rho6?

    python3 -B w46_on_main.py        # writes w46_on_main.json beside itself
"""
import cmath, contextlib, importlib.util, io, itertools, json, math, os, pathlib
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, FRONTIER / rel)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


om = load("om", "B1617_the_weave_at_tau_omega/verification/weave_at_omega.py")
w45 = load("w45", "B1632_w45_verified_on_main/verification/w45_on_main.py")
W, cp, TB = om.W, om.cp, om.cp.TB
inv = np.linalg.inv
out = {}


def close(A, B, tol=1e-9):
    return bool(np.allclose(A, B, atol=tol))


def prop(X, Y, tol=1e-9):
    """X = lam Y for a scalar lam; returns lam or None"""
    i = np.unravel_index(np.argmax(abs(Y)), Y.shape)
    lam = X[i] / Y[i]
    return complex(lam) if np.allclose(X, lam * Y, atol=tol) else None


def T3(M):
    return cp.restrict(M, TB)


def conj_auto(c):
    return {x: om.red(c + x + om.inv(c)) for x in "ab"}


def move_matrix_blockwise(m, gs):
    """B1600's move_matrix with an intertwiner per parity block: z -> g_p^-1 (z o m) on block p"""
    Mx = np.zeros((6, 6), dtype=complex)
    for ip, p in enumerate(W.PAR):
        q = W.act_parity(m, p); iq = W.PAR.index(q)
        basis_p, _ = W.BASES[p]; basis_q, Pq = W.BASES[q]
        gi = inv(gs[p])
        for k in range(2):
            vec = basis_p[:, k]; z = {"a": vec[:2], "b": vec[2:]}
            w = np.concatenate([gi @ W.cocycle_value(z, m["a"], p), gi @ W.cocycle_value(z, m["b"], p)])
            Mx[2 * iq: 2 * iq + 2, 2 * ip + k] = basis_q.conj().T @ (Pq @ w)
    return Mx


def parity_signs(c):
    return np.diag([W.chi(p, "a") ** c.count("a") * W.chi(p, "a") ** c.count("A") * W.chi(p, "b") ** c.count("b") * W.chi(p, "b") ** c.count("B")
                    for p in W.PAR for _ in range(2)]).astype(complex)


# ---- O1 ----------------------------------------------------------------------------------------------------------------
O1 = {}
for c in ("a", "b", "aBAb"):
    m = conj_auto(c)
    g = om.lift_of(m)
    rec = W.move_matrix(m, g)
    geo = move_matrix_blockwise(m, {p: W.rep(c, p) for p in W.PAR})
    P = parity_signs(c)
    O1[c] = {"record_is_plus_parity": close(rec, P), "record_is_minus_parity": close(rec, -P),
             "geometric_is_identity": close(geo, np.eye(6)), "geometric_on_T_is_identity": close(T3(geo), np.eye(3)),
             "parity_signs": [int(round(P[2 * i, 2 * i].real)) for i in range(3)]}
out["O1"] = O1

# ---- O2 ----------------------------------------------------------------------------------------------------------------
Lm, Rm = {"a": "a", "b": "ab"}, {"a": "ab", "b": "b"}
Rinv = {"a": "aB", "b": "b"}
assert om.compose(Rm, Rinv) == {"a": "a", "b": "b"}
D = om.compose(Lm, om.compose(Rinv, Lm))
D4 = om.compose(D, om.compose(D, om.compose(D, D)))
cands = [w for n in range(1, 7) for w in ("".join(t) for t in itertools.product("aAbB", repeat=n)) if om.red(w) == w]
c_of_D4 = [w for w in cands if conj_auto(w) == D4]
MD = W.ML @ inv(W.MR) @ W.ML
MD4 = np.linalg.matrix_power(MD, 4)
O2 = {"Delta4_is_inner_by": c_of_D4[:4], "moves_Delta4_on_T": None, "geometric_conj_c_on_T": None}
if c_of_D4:
    c = c_of_D4[0]
    geo = move_matrix_blockwise(conj_auto(c), {p: W.rep(c, p) for p in W.PAR})
    O2["moves_Delta4_on_T_is_minus_I"] = close(T3(MD4), -np.eye(3))
    O2["moves_Delta4_on_T_scalar"] = str(prop(T3(MD4), np.eye(3)))
    O2["geometric_conj_c_on_T_is_plus_I"] = close(T3(geo), np.eye(3))
    O2["rho_Q_of_c"] = str(prop(W.rep(c, (0, 0)), np.eye(2)))
out["O2"] = O2

# ---- O3 ----------------------------------------------------------------------------------------------------------------
def semi_invariants(gens, n):
    """for commuting diagonal generators: the multiplicity of each joint eigenvalue tuple on the n-th tensor power"""
    from collections import Counter
    mats = []
    for G in gens:
        Gn = np.eye(1)
        for _ in range(n):
            Gn = np.kron(Gn, G)
        mats.append(Gn)
    return Counter(zip(*[np.round(np.diag(M), 9) for M in mats]))


par_T = {c: T3(parity_signs(c)) for c in ("a", "b")}
# the parity lines of T: joint eigenbasis of the parity action on T
_, PB = np.linalg.eig(par_T["a"] + 0.3719 * par_T["b"]); PB, _ = np.linalg.qr(PB)
pa, pb = (PB.conj().T @ par_T[c] @ PB for c in ("a", "b"))
O3 = {"parity_action_diagonal_in_lines": close(pa, np.diag(np.diag(pa))) and close(pb, np.diag(np.diag(pb)))}
for n in (2, 3):
    cnt = semi_invariants([pa, pb], n)
    triv = sum(v for k, v in cnt.items() if all(abs(x - 1) < 1e-6 for x in k))
    O3[f"T^{n}_invariant_dim"] = int(triv)
# the symmetric invariants of degree 3
basis3 = [np.kron(np.kron(e1, e2), e3) for e1, e2, e3 in itertools.product(np.eye(3), repeat=3)]
inv3 = [v for v in basis3 if close(np.kron(np.kron(pa, pa), pa) @ v, v) and close(np.kron(np.kron(pb, pb), pb) @ v, v)]
sym = sum(inv3) if inv3 else None
O3["T^3_invariant_monomials"] = len(inv3)
O3["T^3_invariant_monomials_all_distinct"] = all(len({int(np.argmax(abs(v.reshape(3, 3, 3)).sum(axis=(1, 2)))),
                                                       int(np.argmax(abs(v.reshape(3, 3, 3)).sum(axis=(0, 2)))),
                                                       int(np.argmax(abs(v.reshape(3, 3, 3)).sum(axis=(0, 1))))}) == 3 for v in inv3)
# (b) in rho_theta's own coordinates
P13 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], complex); P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], complex)
rS, rT = -1j * P13, np.diag([1j, 1, 1]) @ P23
ct = np.zeros(27, complex)
for p, q, r in itertools.permutations(range(3)):
    ct[9 * p + 3 * q + r] = 1
k3 = lambda A: np.kron(np.kron(A, A), A)
lamS, lamT = prop(k3(rS) @ ct[:, None], ct[:, None]), prop(k3(rT) @ ct[:, None], ct[:, None])
O3["c_character"] = {"S": str(lamS), "T": str(lamT)}
mp.mp.dps = 30


def thetas(t):
    q4 = lambda x: mp.exp(1j * mp.pi * t * x)
    th2 = mp.fsum(q4((n + mp.mpf(1) / 2) ** 2) for n in range(-40, 40))
    th3 = mp.fsum(q4(n * n) for n in range(-40, 41))
    th4 = mp.fsum((-1) ** abs(n) * q4(n * n) for n in range(-40, 41))
    eta = mp.exp(1j * mp.pi * t / 12) * mp.fprod(1 - mp.exp(2j * mp.pi * t * n) for n in range(1, 300))
    return th2, th3, th4, eta


rng = np.random.default_rng(1641)
res, golden_ok = [], True
for _ in range(5):
    t = mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.6, 1.8))
    th2, th3, th4, eta = thetas(t)
    u = [th2 ** 2, th3 ** 2, th4 ** 2]
    cuuu = mp.fsum(u[p] * u[q] * u[r] for p, q, r in itertools.permutations(range(3)))
    res.append(float(abs(cuuu - 24 * eta ** 6) / abs(24 * eta ** 6)))
    Y = [[mp.fsum(u[r] for r in range(3) if len({p, q, r}) == 3) if p != q else 0 for q in range(3)] for p in range(3)]
    G = [[0, u[2], u[1]], [u[2], 0, u[0]], [u[1], u[0], 0]]
    golden_ok = golden_ok and all(abs(Y[i][j] - G[i][j]) < 1e-20 for i in range(3) for j in range(3))
O3["c_uuu_over_24eta6_max_rel_err"] = max(res)
O3["c_of_u_is_golden_coupling"] = bool(golden_ok)
out["O3"] = O3

# ---- W1 ----------------------------------------------------------------------------------------------------------------
def blocks_action(m, g):
    A = np.zeros((6, 6), dtype=complex)
    for i, u in enumerate(W.PAR):
        j = W.PAR.index(W.act_parity(m, u))
        A[2 * i:2 * i + 2, 2 * j:2 * j + 2] = g
    return A


gL, gR = W.gL, W.gR
St = om.compose(Rm, om.compose({"a": "a", "b": "Ab"}, Rm))          # S~ = R L^-1 R (B1630)
gSt = gR @ inv(gL) @ gR
assert all(close(gSt @ q @ inv(gSt), om.rho_word(St[x])) or close(-gSt @ q @ inv(gSt), om.rho_word(St[x])) for x, q in (("a", W.qi), ("b", W.qj)))
A_L, A_R, A_St = blocks_action(Lm, gL), blocks_action(Rm, gR), blocks_action(St, gSt)
W1 = {"braid_six": close(A_L @ inv(A_R) @ A_L, inv(A_R) @ A_L @ inv(A_R))}
idents = {}
for sname, Sm in (("S~", A_St), ("S~^-1", inv(A_St))):
    for tname, Tm in (("L", A_L), ("L^-1", inv(A_L))):
        rel = close(Sm @ Sm, np.linalg.matrix_power(Sm @ Tm, 3)) and close(np.linalg.matrix_power(Sm, 8), np.eye(6)) \
              and prop(Sm @ Sm, np.eye(6)) is not None
        idents[(sname, tname)] = (Sm, Tm, rel)
W1["valid_identifications"] = [f"S={s}, T={t}" for (s, t), v in idents.items() if v[2]]
ex = sorted(round(((cmath.phase(e) / (2 * math.pi)) % 1.0) * 8) / 8 for e in np.linalg.eigvals(A_L))
W1["exponents_rho6_T_in_eighths"] = [round(x * 8) for x in ex]
gens = [A_L, A_R]
rows = [np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6)) for g in gens]
sv = np.linalg.svd(np.vstack(rows), compute_uv=False)
W1["commutant_dim"] = int(sum(sv < 1e-9))
_, _, Vh = np.linalg.svd(np.vstack(rows))
null = [Vh[-i - 1].conj().reshape(6, 6, order="F") for i in range(W1["commutant_dim"])]
X = sum((0.37 + 0.11 * i) * N for i, N in enumerate(null))
ev, Vv = np.linalg.eig(X)
groups = {}
for i, e in enumerate(ev):
    groups.setdefault(tuple(np.round([e.real, e.imag], 6)), []).append(i)
pieces = [np.linalg.qr(Vv[:, idx])[0] for idx in groups.values()]
W1["piece_dims"] = sorted(Q.shape[1] for Q in pieces)
out["W1"] = W1

# ---- W2, W3 ------------------------------------------------------------------------------------------------------------
chi = w45.chi
W2 = {"eta2_chi1": None, "by_identification": {}}
eta_S, eta_T = np.array([[cmath.exp(-1j * math.pi / 4) ** 2]]), np.array([[cmath.exp(2j * math.pi / 24) ** 2]])
W2["eta2_chi1"] = round(chi(1, eta_S, eta_T), 9)
for (s, t), (Sm, Tm, ok) in idents.items():
    if not ok:
        continue
    row = {"weight_1_allowed": bool(w45.allowed(1, Sm)), "L6": round(chi(1, Sm, Tm), 9)}
    for Q in pieces:
        r = lambda M: Q.conj().T @ M @ Q
        row[f"piece{Q.shape[1]}"] = round(chi(1, r(Sm), r(Tm)), 9)
    W2["by_identification"][f"S={s}, T={t}"] = row
# rho_T as B1634: rho(S) = lift(S~)^-1, rho(T) = lift(L)^-1 on T; rho_T-bar its conjugate
MSt = W.MR @ inv(W.ML) @ W.MR
rTS, rTT = inv(T3(MSt)), inv(T3(W.ML))
W2["chi_3/2_rho_T"] = round(chi(1.5, rTS, rTT), 9)
W2["chi_1/2_rho_T_bar"] = round(chi(0.5, rTS.conj(), rTT.conj()), 9)
out["W2"] = W2
W3 = {}
for (s, t), (Sm, Tm, ok) in idents.items():
    if not ok:
        continue
    tab = {}
    by = {}
    for Q in pieces:
        r = lambda M, Q=Q: Q.conj().T @ M @ Q
        by[Q.shape[1]] = (r(Sm), r(Tm))
    for lam_name, members in (("0", []), ("V2", [2]), ("V4", [4]), ("L6", [2, 4])):
        size = sum(members)
        for n in (-1, 0, 1):
            val = -chi(1.5 + 12 * n, rTS, rTT) + sum(chi(1 + 12 * n, *by[d]) for d in members if d in by)
            tab[f"{lam_name},n={n}"] = (round(val, 9), n * (size - 3))
    W3[f"S={s}, T={t}"] = {"table": tab, "all_match": all(abs(v - w) < 1e-6 for v, w in tab.values())}
out["W3"] = W3

# ---- H -----------------------------------------------------------------------------------------------------------------
def occurs(Sm, Tm, rS3, rT3):
    """is (rS3, rT3), up to a scalar on each generator, a subrepresentation (Hom(rho3, rho6) != 0) or a quotient
    (Hom(rho6, rho3) != 0) of (Sm, Tm)?  Scalars: the eta characters; tried over 24th roots of unity."""
    found = {"sub": [], "quotient": []}
    for a, b in itertools.product(range(24), repeat=2):
        zS, zT = cmath.exp(2j * math.pi * a / 24), cmath.exp(2j * math.pi * b / 24)
        for kind, (X, Y) in (("sub", ((zS * rS3, zT * rT3), (Sm, Tm))), ("quotient", ((Sm, Tm), (zS * rS3, zT * rT3)))):
            (A1, B1), (A2, B2) = X, Y
            n1, n2 = A1.shape[0], A2.shape[0]
            M = np.vstack([np.kron(np.eye(n1), A2) - np.kron(A1.T, np.eye(n2)), np.kron(np.eye(n1), B2) - np.kron(B1.T, np.eye(n2))])
            if np.linalg.svd(M, compute_uv=False)[-1] < 1e-8:
                found[kind].append((a, b))
    return found


H = {}
for (s, t), (Sm, Tm, ok) in idents.items():
    if not ok:
        continue
    H[f"S={s}, T={t}"] = {"rho_T": occurs(Sm, Tm, rTS, rTT), "rho_T_bar": occurs(Sm, Tm, rTS.conj(), rTT.conj())}
out["H"] = H

json.dump(out, open(HERE / "w46_on_main.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:6000])
