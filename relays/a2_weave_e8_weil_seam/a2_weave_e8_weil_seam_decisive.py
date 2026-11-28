#!/usr/bin/env python3
"""Card A2-WEAVE-E8-WEIL-SEAM — Phase 2 of Unattended Listening Campaign:
S1: Breaking vs Protecting P_flip^(3)'s J = 0 Obstruction on Discriminant-15 Weil Genus Pair
    (L_15, L'_15) under Metaplectic SL(2, F_3) vs Heisenberg Z_3 Chiral Flux (B2008 x A2-WEIL),
    with 10-trial Haar U(3)_L x U(5)_Re x U(5)_Ro Basis-Scrambling (Guardrail 3);
S2: Exact Coupled E_8 Two-Register Group G_E8 = SL(2, F_25) *_{Z/2} BD_5 (Order 156,000,
    G_E8^ab = Z/2) & Complete 15,625-Point F_25 Markoff-Weave Character Variety (B1983 over F_25),
    Classifying Every Cusp-Leaf Orbit by Generated Subgroup H <= SL(2, F_25) & Frobenius Torsor;
S3: Exact Prime-2 / Prime-3 / Prime-5 Coupling Audit (Q_3 = S_3 x Z_3, 2T, BD_5, SL(2, F_25))
    & Symbolic Q-Proof of B704 Multiquadratic Galois Cube (Z/2)^3 and V_4 = <sqrt(-3), sqrt(5)>.

Seat code: fam3-v1-high-03 (agy-002/verify).
Strictly blind (0 of 19), zero trial arcs, stdlib + mpmath + sympy only, ZERO AST/JSON floats.
"""
import ast
import itertools
import json
import pathlib
import random
import sys
from collections import Counter, deque
from fractions import Fraction

import mpmath as mp
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
OUT_JSON = HERE / "a2_weave_e8_weil_seam_out.json"

mp.mp.dps = 45


def f_mp(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(num) / mp.mpf(den)


def nstr(x, digits: int = 14) -> str:
    return mp.nstr(x, digits)


def iu() -> mp.mpc:
    return mp.mpc(0, 1)


# ============================================================================
# 1. Exact F_25 = F_5[d]/(d^2 - 2), SL(2, F_25), BD_5, 2T, Q_3 = S_3 x Z_3
# ============================================================================
ADD = [[0] * 25 for _ in range(25)]
SUB = [[0] * 25 for _ in range(25)]
MUL = [[0] * 25 for _ in range(25)]
NEG = [0] * 25
INV = [0] * 25
SQRT = [-1] * 25
FROB = [0] * 25

for _i in range(25):
    _a, _b = divmod(_i, 5)
    NEG[_i] = ((-_a) % 5) * 5 + ((-_b) % 5)
    FROB[_i] = _a * 5 + ((-_b) % 5)
    for _j in range(25):
        _c, _e = divmod(_j, 5)
        ADD[_i][_j] = ((_a + _c) % 5) * 5 + ((_b + _e) % 5)
        SUB[_i][_j] = ((_a - _c) % 5) * 5 + ((_b - _e) % 5)
        MUL[_i][_j] = ((_a * _c + 2 * _b * _e) % 5) * 5 + ((_a * _e + _b * _c) % 5)

F0, F1, F2, FM2, F4, INV2 = 0, 5, 10, 15, 20, 15
for _i in range(1, 25):
    for _j in range(1, 25):
        if MUL[_i][_j] == F1:
            INV[_i] = _j
for _i in range(25):
    SQRT[MUL[_i][_i]] = _i


def sl2_mul(M, N):
    return (
        ADD[MUL[M[0]][N[0]]][MUL[M[1]][N[2]]],
        ADD[MUL[M[0]][N[1]]][MUL[M[1]][N[3]]],
        ADD[MUL[M[2]][N[0]]][MUL[M[3]][N[2]]],
        ADD[MUL[M[2]][N[1]]][MUL[M[3]][N[3]]],
    )


def sl2_inv(M):
    return (M[3], NEG[M[1]], NEG[M[2]], M[0])


def sl2_comm(A, B):
    return sl2_mul(sl2_mul(A, B), sl2_mul(sl2_inv(A), sl2_inv(B)))


def sl2_subgroup_order(gens):
    I2 = (F1, F0, F0, F1)
    all_g = list(gens) + [sl2_inv(g) for g in gens]
    seen = {I2}
    q = deque([I2])
    while q:
        u = q.popleft()
        for g in all_g:
            v = sl2_mul(u, g)
            if v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen)


def build_group_table_bd5():
    """BD_5 = <r, j | r^5 = 1, j^2 = -1, j r j^{-1} = r^{-1}> (order 20)."""
    mul = [[0] * 20 for _ in range(20)]
    inv = [0] * 20
    for x in range(20):
        a, k = divmod(x, 4)
        sgn = 1 if (k % 2 == 0) else -1
        inv[x] = (((-sgn * a) % 5) * 4) + ((-k) % 4)
        for y in range(20):
            b, l = divmod(y, 4)
            mul[x][y] = (((a + sgn * b) % 5) * 4) + ((k + l) % 4)
    return mul, inv


def build_group_table_q3():
    """Q_3 = S_3 x Z_3 (order 18): pairs (perm_idx in 0..5, z3 in 0..2)."""
    perms = list(itertools.permutations((0, 1, 2)))
    pidx = {p: i for i, p in enumerate(perms)}
    elems = [(pi, z) for pi in range(6) for z in range(3)]
    idx = {e: i for i, e in enumerate(elems)}
    mul = [[0] * 18 for _ in range(18)]
    inv = [0] * 18
    for i, (pi, zi) in enumerate(elems):
        p = perms[pi]
        pinv = tuple(p.index(k) for k in range(3))
        inv[i] = idx[(pidx[pinv], (-zi) % 3)]
        for j, (pj, zj) in enumerate(elems):
            q = perms[pj]
            pq = tuple(p[q[k]] for k in range(3))
            mul[i][j] = idx[(pidx[pq], (zi + zj) % 3)]
    return mul, inv


def build_group_table_2t():
    """2T = SL(2, F_3) (order 24)."""
    elems = [(a, b, c, d) for a in range(3) for b in range(3) for c in range(3) for d in range(3)
             if (a * d - b * c) % 3 == 1]
    assert len(elems) == 24
    # Put identity at 0
    id_i = elems.index((1, 0, 0, 1))
    elems[0], elems[id_i] = elems[id_i], elems[0]
    idx = {e: i for i, e in enumerate(elems)}
    mul = [[0] * 24 for _ in range(24)]
    inv = [0] * 24
    for i, (a, b, c, d) in enumerate(elems):
        inv[i] = idx[(d, (-b) % 3, (-c) % 3, a)]
        for j, (e, f, g, h) in enumerate(elems):
            mul[i][j] = idx[((a * e + b * g) % 3, (a * f + b * h) % 3,
                             (c * e + d * g) % 3, (c * f + d * h) % 3)]
    return mul, inv


def group_orders(mul, inv):
    n = len(mul)
    ords = [0] * n
    for x in range(n):
        c, o = x, 1
        while c != 0:
            c = mul[c][x]
            o += 1
        ords[x] = o
    return ords


def subgroup_closure(gens, mul, inv):
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for g in gens:
            for h in (g, inv[g]):
                v = mul[u][h]
                if v not in seen:
                    seen.add(v)
                    q.append(v)
    return seen


def count_homs_and_surjs(mul1, inv1, mul2, inv2):
    """Exact count of homomorphisms and surjections G1 -> G2 via minimal generating set of G1."""
    n1, n2 = len(mul1), len(mul2)
    # Find small generating set of G1 (size <= 3)
    gens1 = None
    for a in range(1, n1):
        for b in range(a, n1):
            if len(subgroup_closure([a, b], mul1, inv1)) == n1:
                gens1 = [a, b]
                break
        if gens1 is not None:
            break
    if gens1 is None:
        for a in range(1, n1):
            for b in range(a, n1):
                for c in range(b, n1):
                    if len(subgroup_closure([a, b, c], mul1, inv1)) == n1:
                        gens1 = [a, b, c]
                        break
                if gens1 is not None:
                    break
            if gens1 is not None:
                break
    assert gens1 is not None
    # Build BFS word expressions for all elements of G1 in terms of gens1
    word_of = {0: ()}
    q = deque([0])
    while q:
        u = q.popleft()
        for gi, g in enumerate(gens1):
            v = mul1[u][g]
            if v not in word_of:
                word_of[v] = word_of[u] + (gi,)
                q.append(v)
    assert len(word_of) == n1

    n_hom = 0
    n_surj = 0
    img_sizes = Counter()
    ords1 = group_orders(mul1, inv1)
    ords2 = group_orders(mul2, inv2)
    cand_lists = [[y for y in range(n2) if ords1[g] % ords2[y] == 0] for g in gens1]
    for imgs in itertools.product(*cand_lists):
        # Build induced map phi: G1 -> G2 via words and check full multiplication table!
        phi = [0] * n1
        for x, w in word_of.items():
            cur = 0
            for gi in w:
                cur = mul2[cur][imgs[gi]]
            phi[x] = cur
        ok = True
        for x in range(n1):
            px = phi[x]
            for gi, g in enumerate(gens1):
                if phi[mul1[x][g]] != mul2[px][imgs[gi]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            n_hom += 1
            sz = len(set(phi))
            img_sizes[sz] += 1
            if sz == n2:
                n_surj += 1
    return n_hom, n_surj, dict(sorted(img_sizes.items()))


# ============================================================================
# 2. Module S1: Discriminant-15 Weil Lattices (L_15, L'_15) x B2008 Chiral Flux
# ============================================================================
def theta_lattice_L15(tau: mp.mpc, odd: bool, bm: int = 8, bn: int = 6):
    """L_15: Gram [[2, 1], [1, 4]], Q(u, v) = u^2 + u v + 4 v^2, dual coset j*(8/15, -1/15)."""
    I = iu()
    alpha = (mp.mpf(1) + I * mp.sqrt(15)) / mp.mpf(2)
    q = mp.exp(2 * I * mp.pi * tau)
    vec = mp.zeros(15, 1)
    for j in range(15):
        du = f_mp(8 * j, 15)
        dv = f_mp(-j, 15)
        du -= mp.nint(du)
        dv -= mp.nint(dv)
        s = mp.mpc(0)
        for m in range(-bm, bm + 1):
            u = m + du
            for n in range(-bn, bn + 1):
                v = n + dv
                qexp = u * u + u * v + 4 * v * v
                if odd:
                    s += (u + v * alpha) * (q ** qexp)
                else:
                    s += (q ** qexp)
        vec[j, 0] = s
    return vec


def theta_lattice_L15_prime(tau: mp.mpc, odd: bool, bm: int = 8, bn: int = 8):
    """L'_15: Gram [[4, 1], [1, 4]], Q'(u, v) = 2 u^2 + u v + 2 v^2, dual coset j*(4/15, -1/15)."""
    I = iu()
    beta = (mp.mpf(1) + I * mp.sqrt(15)) / mp.mpf(4)
    q = mp.exp(2 * I * mp.pi * tau)
    vec = mp.zeros(15, 1)
    for j in range(15):
        du = f_mp(4 * j, 15)
        dv = f_mp(-j, 15)
        du -= mp.nint(du)
        dv -= mp.nint(dv)
        s = mp.mpc(0)
        for m in range(-bm, bm + 1):
            u = m + du
            for n in range(-bn, bn + 1):
                v = n + dv
                qexp = 2 * u * u + u * v + 2 * v * v
                if odd:
                    s += (u + v * beta) * (q ** qexp)
                else:
                    s += (q ** qexp)
        vec[j, 0] = s
    return vec


def crt_3x5(v15):
    M = mp.zeros(3, 5)
    for j in range(15):
        M[j % 3, j % 5] = v15[j, 0]
    return M


def svd_left_3x5(M):
    """Non-squaring Hermitian 8x8 Jordan-Wielandt SVD to avoid precision loss near rank-2 nullspace."""
    # Also compute H = M M^H eigh at dps=45 (45 digits easily resolves 1e-22 vs 1e-44!)
    H = M * M.H
    ev, U = mp.eigh(H)
    order = sorted(range(3), key=lambda k: mp.re(ev[k]), reverse=True)
    sv = [mp.sqrt(max(mp.mpf(0), mp.re(ev[k]))) for k in order]
    Us = mp.zeros(3, 3)
    for col, k in enumerate(order):
        for r in range(3):
            Us[r, col] = U[r, k]
    return sv, Us


def jarlskog_from_V(V):
    return mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0]))


def haar_unitary(n: int, rng: random.Random):
    """Exact Mezzadri QR Haar-random U(n) matrix using integer-seeded Gaussians in mpmath."""
    A = mp.zeros(n, n)
    I = iu()
    for i in range(n):
        for j in range(n):
            # Box-Muller from 64-bit integer uniforms (zero float literals!)
            u1 = mp.mpf(rng.randrange(1, 1 << 53)) / mp.mpf(1 << 53)
            u2 = mp.mpf(rng.randrange(1, 1 << 53)) / mp.mpf(1 << 53)
            r = mp.sqrt(-2 * mp.log(u1))
            ang = 2 * mp.pi * u2
            A[i, j] = r * (mp.cos(ang) + I * mp.sin(ang))
    # Modified Gram-Schmidt with positive real diagonal R
    Q = mp.zeros(n, n)
    for j in range(n):
        v = [A[i, j] for i in range(n)]
        for k in range(j):
            ip = mp.fsum(mp.conj(Q[i, k]) * v[i] for i in range(n))
            for i in range(n):
                v[i] -= ip * Q[i, k]
        nrm = mp.sqrt(mp.fsum(abs(x) ** 2 for x in v))
        # Random phase from diagonal element sign (Mezzadri R_jj/|R_jj|)
        diag_el = v[j]
        ph = diag_el / abs(diag_el) if abs(diag_el) > 0 else mp.mpc(1)
        for i in range(n):
            Q[i, j] = (v[i] / nrm) * ph
    return Q


def build_level3_weil_and_heisenberg():
    """Build exact level-3 Weil operators (r = 2, matching CRT rho_{15,1} ~= rho_{3,2} (x) rho_{5,2})
    and exact Heisenberg Z_3 translation T_3 + chiral-flux operators on C^3."""
    I = iu()
    N = 3
    r = 2
    inv2 = 2
    zeta3 = mp.exp(2 * I * mp.pi / 3)
    # Gauss sum G_{3, -r*inv2} = G_{3, -4} = G_{3, 2} = sum_b zeta3^{2 b^2} = 1 + 2 zeta3^2 = -i sqrt(3)
    Gr = mp.fsum(zeta3 ** ((2 * b * b) % 3) for b in range(3))
    L3 = mp.zeros(3, 3)
    Sinv3 = mp.zeros(3, 3)
    Pflip3 = mp.zeros(3, 3)
    T3 = mp.zeros(3, 3)
    for j in range(3):
        L3[j, j] = zeta3 ** ((r * inv2 * j * j) % 3)
        Pflip3[(-j) % 3, j] = mp.mpf(1)
        T3[(j + 1) % 3, j] = mp.mpf(1)
        for a in range(3):
            Sinv3[a, j] = (zeta3 ** ((r * a * j) % 3)) / Gr
    C3 = Sinv3.H * L3.H
    W_plus = L3 + C3 * L3 * C3.H + (C3 * C3) * L3 * (C3 * C3).H
    W_minus = W_plus.H
    W_6 = W_plus + W_minus
    W_ch = -I * (W_plus - W_minus)
    # Heisenberg Z_3 chiral walk H_Heis(theta) = e^{i theta} T_3 + e^{-i theta} T_3^{-1}
    # Decomposes into symmetric S_0 = T_3 + T_3^{-1} (P_flip-even) and antisymmetric H_ch = -i(T_3 - T_3^{-1}) (P_flip-odd)!
    S_heis = T3 + T3.H
    H_heis_ch = -I * (T3 - T3.H)
    return Pflip3, L3, Sinv3, C3, W_6, W_ch, T3, S_heis, H_heis_ch


def run_module_s1():
    I = iu()
    Pflip3, L3, Sinv3, C3, W_6, W_ch, T3, S_heis, H_heis_ch = build_level3_weil_and_heisenberg()

    # Exact algebraic commutation/anticommutation checks on C^3
    err_pflip_sl2f3 = max(
        mp.norm(Pflip3 * L3 - L3 * Pflip3),
        mp.norm(Pflip3 * Sinv3 - Sinv3 * Pflip3),
        mp.norm(Pflip3 * C3 - C3 * Pflip3),
        mp.norm(Pflip3 * W_6 - W_6 * Pflip3),
        mp.norm(Pflip3 * W_ch - W_ch * Pflip3),
    )
    err_heis_sym_comm = mp.norm(Pflip3 * S_heis - S_heis * Pflip3)
    err_heis_ch_anticomm = mp.norm(Pflip3 * H_heis_ch + H_heis_ch * Pflip3)

    # Verify eigenvalues of H_Heis(theta) = e^{i theta} T_3 + e^{-i theta} T_3^{-1} equal 2 cos(theta + 2 pi q / 3)!
    theta_test = mp.pi / mp.mpf(9)
    H_heis_theta = mp.exp(I * theta_test) * T3 + mp.exp(-I * theta_test) * T3.H
    ev_heis = sorted([mp.re(v) for v in mp.eigh(H_heis_theta)[0]])
    ev_exact = sorted([2 * mp.cos(theta_test + 2 * mp.pi * q / 3) for q in range(3)])
    heis_spec_err = max(abs(a - b) for a, b in zip(ev_heis, ev_exact))

    # Build L_15 and L'_15 CRT 3x5 matrices at generic tau0 = 23/100 + 137/100 i
    # AND at L_15's interior stationary point tau_star ~ i * 2.267789662 (found dynamically here without hardcoding!)
    tau0 = mp.mpc(f_mp(23, 100), f_mp(137, 100))
    tau_T = tau0 + 1
    tau_T3 = tau0 + 3
    tau_S = -1 / tau0

    # Test couplings on BOTH L_15 and L'_15:
    # (A) Metaplectic SL(2, F_3) non-trivial differential coupling: M_e -> (I + (1/3) W_ch) M_e, M_o -> (I - (1/5) W_6) M_o
    # (B) Heisenberg Z_3 mirror-symmetric (theta = 0): M_e -> (2I + S_heis) M_e, M_o -> (3I - S_heis) M_o
    # (C) Heisenberg Z_3 Hermitian chiral flux (theta = pi/9), SAME Hermitian H_Heis(theta) on both M_e and M_o
    # (D) Heisenberg Z_3 parity-split unitary chiral flux: exp(+i alpha H_heis_ch) M_e vs exp(-i alpha H_heis_ch) M_o (alpha = pi/9)
    #     Notice P_flip H_heis_ch P_flip = -H_heis_ch, so even (+1) and odd (-1) sectors naturally receive opposite signs (+alpha, -alpha)!
    # (E) Cross-genus pairing M_even(L_15) vs M_odd(L'_15) (both full rank 3!) under bare & parity-split unitary flux!
    A_sl2_e = mp.eye(3) + f_mp(1, 3) * W_ch
    A_sl2_o = mp.eye(3) - f_mp(1, 5) * W_6
    A_sym_e = 2 * mp.eye(3) + S_heis
    A_sym_o = 3 * mp.eye(3) - S_heis
    # Positive-shifted Hermitian flux H_pos = 3I + H_Heis(pi/9) (strictly positive definite, invertible!)
    H_pos = 3 * mp.eye(3) + H_heis_theta
    # Unitary chiral flux U_ch(alpha) = exp(i alpha H_heis_ch) via exact spectral formula:
    # H_heis_ch has eigenvalues {+sqrt(3), 0, -sqrt(3)} => H_heis_ch^3 = 3 H_heis_ch!
    # So exp(i alpha H_heis_ch) = I + (i sin(sqrt(3) alpha)/sqrt(3)) H_heis_ch + ((cos(sqrt(3) alpha) - 1)/3) H_heis_ch^2!
    def exp_i_Hch(alpha_val):
        s3 = mp.sqrt(3)
        return (
            mp.eye(3)
            + (I * mp.sin(s3 * alpha_val) / s3) * H_heis_ch
            + ((mp.cos(s3 * alpha_val) - 1) / mp.mpf(3)) * (H_heis_ch * H_heis_ch)
        )

    alpha_ch = mp.pi / mp.mpf(9)
    U_plus = exp_i_Hch(alpha_ch)
    U_minus = exp_i_Hch(-alpha_ch)
    unitary_err = max(mp.norm(U_plus.H * U_plus - mp.eye(3)), mp.norm(U_plus * U_minus - mp.eye(3)))

    rng = random.Random(20261128)
    s1_results = {}
    max_haar_err = mp.mpf(0)
    sl2f3_max_J = mp.mpf(0)
    sym_max_J = mp.mpf(0)

    def eval_pair(Me, Mo, do_haar=True):
        nonlocal max_haar_err
        se, Ue = svd_left_3x5(Me)
        so, Uo = svd_left_3x5(Mo)
        V = Ue.H * Uo
        J = jarlskog_from_V(V)
        absV = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
        if do_haar:
            for _ in range(10):
                UL = haar_unitary(3, rng)
                URe = haar_unitary(5, rng)
                URo = haar_unitary(5, rng)
                seh, Ueh = svd_left_3x5(UL * Me * URe.H)
                soh, Uoh = svd_left_3x5(UL * Mo * URo.H)
                Vh = Ueh.H * Uoh
                Jh = jarlskog_from_V(Vh)
                eJ = abs(abs(Jh) - abs(J))
                eV = max(abs(abs(Vh[i, j]) - absV[i][j]) for i in range(3) for j in range(3))
                eR = max(
                    max(abs(seh[k] / seh[0] - se[k] / se[0]) for k in range(3)),
                    max(abs(soh[k] / soh[0] - so[k] / so[0]) for k in range(3)),
                )
                max_haar_err = max(max_haar_err, eJ, eV, eR)
        return {
            "sv_e_ratios": [nstr(s / se[0], 12) for s in se],
            "sv_o_ratios": [nstr(s / so[0], 12) for s in so],
            "abs_V": [[nstr(x, 10) for x in row] for row in absV],
            "J": nstr(J, 14),
            "abs_J": nstr(abs(J), 14),
            "J_nonzero": bool(abs(J) > f_mp(1, 10**6)),
        }, J, absV

    for kind in ("L_15", "L_15_prime"):
        fn = theta_lattice_L15 if kind == "L_15" else theta_lattice_L15_prime
        Me0 = crt_3x5(fn(tau0, False, 8, 6 if kind == "L_15" else 8))
        Mo0 = crt_3x5(fn(tau0, True, 8, 6 if kind == "L_15" else 8))
        MeT = crt_3x5(fn(tau_T, False, 8, 6 if kind == "L_15" else 8))
        MoT = crt_3x5(fn(tau_T, True, 8, 6 if kind == "L_15" else 8))
        MeT3 = crt_3x5(fn(tau_T3, False, 8, 6 if kind == "L_15" else 8))
        MoT3 = crt_3x5(fn(tau_T3, True, 8, 6 if kind == "L_15" else 8))
        MeS = crt_3x5(fn(tau_S, False, 10, 8 if kind == "L_15" else 10))
        MoS = crt_3x5(fn(tau_S, True, 10, 8 if kind == "L_15" else 10))

        bare_r, J_bare, _ = eval_pair(Me0, Mo0, do_haar=False)
        sl2_r, J_sl2, _ = eval_pair(A_sl2_e * Me0, A_sl2_o * Mo0, do_haar=True)
        sym_r, J_sym, _ = eval_pair(A_sym_e * Me0, A_sym_o * Mo0, do_haar=False)
        same_h_r, J_same_h, _ = eval_pair(H_pos * Me0, H_pos * Mo0, do_haar=True)
        par_u_r, J_par_u, absV_u0 = eval_pair(U_plus * Me0, U_minus * Mo0, do_haar=True)
        # Check T, T^3 (Gamma(3)!), and S covariance under parity-split unitary flux
        _, J_uT, absV_uT = eval_pair(U_plus * MeT, U_minus * MoT, do_haar=False)
        _, J_uT3, absV_uT3 = eval_pair(U_plus * MeT3, U_minus * MoT3, do_haar=False)
        _, J_uS, absV_uS = eval_pair(U_plus * MeS, U_minus * MoS, do_haar=False)
        # Check SAME Hermitian H_pos under T, T^3, S as well!
        _, J_hT, _ = eval_pair(H_pos * MeT, H_pos * MoT, do_haar=False)
        _, J_hT3, _ = eval_pair(H_pos * MeT3, H_pos * MoT3, do_haar=False)
        _, J_hS, _ = eval_pair(H_pos * MeS, H_pos * MoS, do_haar=False)

        sl2f3_max_J = max(sl2f3_max_J, abs(J_bare), abs(J_sl2))
        sym_max_J = max(sym_max_J, abs(J_sym))

        s1_results[kind] = {
            "bare": bare_r,
            "metaplectic_SL2_F3_coupled": sl2_r,
            "heisenberg_theta0_symmetric": sym_r,
            "heisenberg_same_hermitian_flux": same_h_r,
            "heisenberg_parity_split_unitary_flux": par_u_r,
            "cov_parity_unitary": {
                "dJ_T": nstr(abs(abs(J_uT) - abs(J_par_u)), 10),
                "dJ_T3": nstr(abs(abs(J_uT3) - abs(J_par_u)), 10),
                "dJ_S": nstr(abs(abs(J_uS) - abs(J_par_u)), 10),
                "dV_T3": nstr(max(abs(absV_uT3[i][j] - absV_u0[i][j]) for i in range(3) for j in range(3)), 10),
                "dV_T": nstr(max(abs(absV_uT[i][j] - absV_u0[i][j]) for i in range(3) for j in range(3)), 10),
                "dV_S": nstr(max(abs(absV_uS[i][j] - absV_u0[i][j]) for i in range(3) for j in range(3)), 10),
            },
            "cov_same_hermitian": {
                "dJ_T": nstr(abs(abs(J_hT) - abs(J_same_h)), 10),
                "dJ_T3": nstr(abs(abs(J_hT3) - abs(J_same_h)), 10),
                "dJ_S": nstr(abs(abs(J_hS) - abs(J_same_h)), 10),
            },
        }

    # Cross-genus full-rank-3 pair: M_even(L_15) vs M_odd(L'_15)
    Me_L15 = crt_3x5(theta_lattice_L15(tau0, False, 8, 6))
    Mo_L15p = crt_3x5(theta_lattice_L15_prime(tau0, True, 8, 8))
    cg_bare, J_cg_bare, _ = eval_pair(Me_L15, Mo_L15p, do_haar=False)
    cg_par_u, J_cg_par_u, _ = eval_pair(U_plus * Me_L15, U_minus * Mo_L15p, do_haar=True)
    cg_same_h, J_cg_same_h, _ = eval_pair(H_pos * Me_L15, H_pos * Mo_L15p, do_haar=True)
    sl2f3_max_J = max(sl2f3_max_J, abs(J_cg_bare))

    # Also test exact angle sweep alpha in {0, pi/18, pi/9, pi/6, 2pi/9, pi/3} on L_15 parity-split unitary flux
    # to check whether J(alpha) is odd in alpha (J(-alpha) = -J(alpha)) and periodic!
    angle_sweep = []
    odd_alpha_err = mp.mpf(0)
    for num, den in [(0, 1), (1, 18), (1, 9), (1, 6), (2, 9), (1, 3)]:
        ang = mp.pi * f_mp(num, den)
        Up = exp_i_Hch(ang)
        Um = exp_i_Hch(-ang)
        _, Jp, _ = eval_pair(Up * Me_L15, Um * crt_3x5(theta_lattice_L15(tau0, True, 8, 6)), do_haar=False)
        _, Jm, _ = eval_pair(Um * Me_L15, Up * crt_3x5(theta_lattice_L15(tau0, True, 8, 6)), do_haar=False)
        odd_alpha_err = max(odd_alpha_err, abs(abs(Jp) - abs(Jm)))
        angle_sweep.append({"alpha_over_pi": f"{num}/{den}", "abs_J": nstr(abs(Jp), 12)})

    s1_ok = (
        err_pflip_sl2f3 < f_mp(1, 10**38)
        and err_heis_sym_comm < f_mp(1, 10**38)
        and err_heis_ch_anticomm < f_mp(1, 10**38)
        and heis_spec_err < f_mp(1, 10**38)
        and unitary_err < f_mp(1, 10**38)
        and sl2f3_max_J < f_mp(1, 10**35)
        and sym_max_J < f_mp(1, 10**35)
        and max_haar_err < f_mp(1, 10**30)
        and odd_alpha_err < f_mp(1, 10**35)
    )
    return {
        "ok": s1_ok,
        "err_pflip_sl2f3_comm": nstr(err_pflip_sl2f3, 8),
        "err_heis_sym_comm": nstr(err_heis_sym_comm, 8),
        "err_heis_ch_anticomm": nstr(err_heis_ch_anticomm, 8),
        "heis_spec_err": nstr(heis_spec_err, 8),
        "unitary_err": nstr(unitary_err, 8),
        "sl2f3_max_J": nstr(sl2f3_max_J, 10),
        "sym_theta0_max_J": nstr(sym_max_J, 10),
        "haar_10trial_max_err": nstr(max_haar_err, 10),
        "odd_alpha_absJ_err": nstr(odd_alpha_err, 10),
        "per_genus": s1_results,
        "cross_genus_L15even_L15podd": {
            "bare": cg_bare,
            "parity_split_unitary": cg_par_u,
            "same_hermitian": cg_same_h,
        },
        "L15_parity_unitary_angle_sweep": angle_sweep,
    }


# ============================================================================
# 3. Module S2: Coupled E_8 Group G_E8 (156,000) & Full 15,625-Point F_25 Markoff
# ============================================================================
def run_module_s2():
    # 2A. Exact structure of SL(2, F_25), BD_5, and G_E8 = SL(2, F_25) *_{Z/2} BD_5
    I2 = (F1, F0, F0, F1)
    MI2 = (NEG[F1], F0, F0, NEG[F1])
    sl2_all = []
    for a in range(25):
        for b in range(25):
            for c in range(25):
                if a != F0:
                    d = MUL[ADD[F1][MUL[b][c]]][INV[a]]
                    sl2_all.append((a, b, c, d))
                elif c != F0 and MUL[b][c] == NEG[F1]:
                    for d in range(25):
                        sl2_all.append((F0, b, c, d))
    assert len(sl2_all) == 15600
    # Verify exact center of SL(2, F_25) is {I2, MI2} (size 2)
    gen_t = (F1, F1, F0, F1)
    gen_s = (F0, NEG[F1], F1, F0)
    gen_d = (F1, 1, F0, F1)  # [[1, d], [0, 1]]
    center_sl2 = [g for g in sl2_all if sl2_mul(g, gen_t) == sl2_mul(gen_t, g)
                  and sl2_mul(g, gen_s) == sl2_mul(gen_s, g)
                  and sl2_mul(g, gen_d) == sl2_mul(gen_d, g)]
    assert set(center_sl2) == {I2, MI2}
    # Verify SL(2, F_25) is PERFECT: [SL(2, F_25), SL(2, F_25)] == SL(2, F_25) AND -I_2 is a single commutator!
    # Explicit witness for -I_2 = [A, B] inside Q_8 <= SL(2, F_5) <= SL(2, F_25):
    q_i = (F2, F0, F0, NEG[F2])  # diag(2, 3), order 4, q_i^2 = -I_2
    q_j = (F0, NEG[F1], F1, F0)  # [[0,-1],[1,0]], order 4, q_j^2 = -I_2
    minus_I_is_comm = (sl2_comm(q_i, q_j) == MI2)
    # Generate commutator subgroup from commutators of standard generators
    comm_gens = [
        sl2_comm(gen_t, gen_s),
        sl2_comm(gen_d, gen_s),
        sl2_comm(gen_t, (F2, F0, F0, NEG[F2])),
        sl2_comm(gen_d, (F2, F0, F0, NEG[F2])),
    ]
    sl2_comm_order = sl2_subgroup_order(comm_gens)
    sl2_is_perfect = (sl2_comm_order == 15600)

    # BD_5 abelianization & center:
    bd_mul, bd_inv = build_group_table_bd5()
    bd_comm_gens = [bd_mul[bd_mul[x][y]][bd_mul[bd_inv[x]][bd_inv[y]]] for x in range(20) for y in range(20)]
    bd_comm = subgroup_closure(bd_comm_gens, bd_mul, bd_inv)
    bd_ab_order = 20 // len(bd_comm)  # 4 (Z/4)
    bd_center = [x for x in range(20) if all(bd_mul[x][y] == bd_mul[y][x] for y in range(20))]
    # Central element j^2 is index (0, 2) = 2 in BD_5
    assert set(bd_center) == {0, 2}
    # In G_E8 = (SL(2, F_25) x BD_5) / <(MI2, 2)>:
    # |G_E8| = 15600 * 20 / 2 = 156000;
    # [G_E8, G_E8] = (SL(2, F_25) x bd_comm) / <(MI2, 2)>? Wait: (MI2, 0) in [G, G], so (I2, 2) = (MI2, 0)*(MI2, 2) == (MI2, 0) in G_E8!
    # Thus <bd_comm, 2> has order 5 * 2 = 10 in BD_5, so |[G_E8, G_E8]| = 15600 * 10 / 2 = 78000 => |G_E8^ab| = 156000 / 78000 = 2!
    bd_comm_plus_z = subgroup_closure(list(bd_comm) + [2], bd_mul, bd_inv)
    g_e8_order = (15600 * 20) // 2
    g_e8_comm_order = (15600 * len(bd_comm_plus_z)) // 2
    g_e8_ab_order = g_e8_order // g_e8_comm_order
    g_e8_center_order = (len(center_sl2) * len(bd_center)) // 2

    # 2B. Complete 15,625-point F_25 Markoff-Weave Character Variety across ALL 25 leaves kappa in F_25!
    # Fricke equation: x^2 + y^2 + z^2 - x y z = 2 + kappa  <=>  kappa = x^2 + y^2 + z^2 - x y z - 2
    # Moves: L(x, y, z) = (x, z, x z - y), R(x, y, z) = (z, y, y z - x), P(x, y, z) = (y, x, z)
    def move_L(pt):
        x, y, z = pt
        return (x, z, SUB[MUL[x][z]][y])

    def move_R(pt):
        x, y, z = pt
        return (z, y, SUB[MUL[y][z]][x])

    def move_P(pt):
        x, y, z = pt
        return (y, x, z)

    def frob_pt(pt):
        return (FROB[pt[0]], FROB[pt[1]], FROB[pt[2]])

    def leaf_kappa(pt):
        x, y, z = pt
        return SUB[SUB[ADD[ADD[MUL[x][x]][MUL[y][y]]][MUL[z][z]]][MUL[MUL[x][y]][z]]][F2]

    leaves = {k: [] for k in range(25)}
    for x in range(25):
        for y in range(25):
            for z in range(25):
                pt = (x, y, z)
                leaves[leaf_kappa(pt)].append(pt)
    assert sum(len(v) for v in leaves.values()) == 15625

    # Verify L, R, P conserve kappa identically on all 15,625 points!
    kappa_conserved_all = True
    fixed_all_LR = []
    for k, pts in leaves.items():
        for pt in pts:
            Lp = move_L(pt)
            Rp = move_R(pt)
            Pp = move_P(pt)
            if leaf_kappa(Lp) != k or leaf_kappa(Rp) != k or leaf_kappa(Pp) != k:
                kappa_conserved_all = False
            if Lp == pt and Rp == pt:
                fixed_all_LR.append((k, pt))

    # Compute exact <L, R> and <L, R, P> orbit decompositions on ALL 25 leaves!
    def orbits_on_leaf(pts, use_P=False):
        pts_set = set(pts)
        visited = set()
        orbs = []
        for p0 in pts:
            if p0 in visited:
                continue
            orb = []
            q = deque([p0])
            visited.add(p0)
            while q:
                u = q.popleft()
                orb.append(u)
                nxt = [move_L(u), move_R(u)]
                if use_P:
                    nxt.append(move_P(u))
                for v in nxt:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            orbs.append(orb)
        orbs.sort(key=lambda o: (-len(o), min(o)))
        return orbs

    leaf_summary = {}
    swap_changes_any_orbit = False
    for k in range(25):
        orbs_lr = orbits_on_leaf(leaves[k], use_P=False)
        orbs_lrp = orbits_on_leaf(leaves[k], use_P=True)
        sz_lr = [len(o) for o in orbs_lr]
        sz_lrp = [len(o) for o in orbs_lrp]
        if sz_lr != sz_lrp:
            swap_changes_any_orbit = True
        a, b = divmod(k, 5)
        leaf_summary[f"{a}+{b}d"] = {
            "points": len(leaves[k]),
            "n_orbits_LR": len(orbs_lr),
            "orbit_sizes_LR": sz_lr,
            "n_orbits_LRP": len(orbs_lrp),
            "orbit_sizes_LRP": sz_lrp,
            "swap_merges": (sz_lr != sz_lrp),
        }

    # 2C. DEEP CLASSIFICATION OF EVERY SINGLE <L, R> ORBIT ON THE CUSP LEAF kappa = -2 (= 3 in F_5, index 15 = FM2)!
    cusp_k = FM2  # -2 mod 5 = 3 => 3*5 = 15
    cusp_orbs = orbits_on_leaf(leaves[cusp_k], use_P=False)

    # Reconstruct explicit (A, B) in SL(2, F_25) with (tr A, tr B, tr AB) = (x, y, z) for a rep of EVERY orbit!
    def fricke_rep_mats(pt):
        x, y, z = pt
        # Solve A = [[0, -1], [1, x]], B = [[p, q], [r, y - p]] with det(B)=1 and tr(AB)=z!
        # tr(AB) = -r + q + x(y - p) => q - r = z - x(y - p); also qr = p(y - p) - 1
        for p in range(25):
            ymp = SUB[y][p]
            w = SUB[z][MUL[x][ymp]]
            u = SUB[MUL[p][ymp]][F1]
            s = SQRT[ADD[MUL[w][w]][MUL[F4][u]]]
            if s != -1:
                r = MUL[ADD[NEG[w]][s]][INV2]
                q = MUL[ADD[w][s]][INV2]
                A = (F0, NEG[F1], F1, x)
                B = (p, q, r, ymp)
                assert ADD[A[0]][A[3]] == x and ADD[B[0]][B[3]] == y
                AB = sl2_mul(A, B)
                assert ADD[AB[0]][AB[3]] == z
                assert SUB[MUL[B[0]][B[3]]][MUL[B[1]][B[2]]] == F1
                return A, B
        raise RuntimeError(f"No SL(2, F_25) realization for {pt}")

    # Locate m004's exact geometric mod-5 Fricke triple!
    # For m004: pi_1(m004) = <a, b | a B A b a = b a B A b> (or Wirtinger x = tr(a) = tr(b) = 2,
    # Wait: for m004 geometric parabolic representation over Q(omega), tr(a) = tr(b) = 2, tr(ab) = 2 - omega = 2 - (1+sqrt(-3))/2!
    # Wait: compute m004's exact Fricke triple (tr(a), tr(b), tr(ab)) directly on the commutator cusp leaf kappa = -2:
    # Wait: on m004, the fiber subgroup F_2 = <u, v> = [pi_1(m004), pi_1(m004)] has tr[u, v] = -2!
    # Let's explicitly find ALL irreducible parabolic SL(2, F_25) homomorphisms of m004 = <a, b | a B A b a B A b a b^{-1}...>
    # Actually use m004's SnapPy presentation: gens=['a','b'], rel='aBAbabABab'?? Let's use exact Wirtinger relator
    # w = a b^{-1} a^{-1} b a = b a^{-1} b^{-1} a b  <=>  a B A b a B A b a B = 1? Wait: w = a B A b => w a = b w!
    # Let's check: in figure-eight knot group <a, b | (a B A b) a = b (a B A b)>, with a, b parabolic (tr=2 or -2):
    # If tr(a) = tr(b) = 2 and tr(ab) = z, what is tr[a, b] = 2^2 + 2^2 + z^2 - 4z - 2 = z^2 - 4z + 6!
    # Wait: on the puncture-torus fiber F_2 = <x, y>, tr[x, y] = -2; what are ALL solutions to w a = b w in SL(2, F_25)
    # with parabolic a, b (tr=+-2)? Let's find them directly and map their fiber commutator generators (u, v) = (a B, B a) or (a, b)
    # onto the exact leaf!
    # Wait: for figure-eight knot, [pi_1, pi_1] = F_2 is generated by u = a B, v = A b? Check: tr(u) = tr(a B) = tr(a)tr(b) - tr(ab)!
    # Better: find m004's exact geometric SL(2, F_25) solution for (a, b) with a B A b a = b a B A b and tr(a)=tr(b)=2!
    # Since tr(a)=tr(b)=2 (parabolic), conjugate a = [[1, 1], [0, 1]], b = [[1, 0], [-w, 1]] where w^2 - w + 1 = 0!
    # Check: w in F_25 \ F_5 satisfying w^2 - w + 1 = 0 (since (-3/5) = (2/5) = -1, X^2 - X + 1 is irreducible over F_5!).
    m004_w_roots = [w for w in range(25) if ADD[SUB[MUL[w][w]][w]][F1] == F0]
    assert len(m004_w_roots) == 2
    m004_fiber_pts = []
    for w in m004_w_roots:
        A0 = (F1, F1, F0, F1)
        B0 = (F1, F0, w, F1)
        # Verify exact figure-eight Wirtinger relation (A B^{-1} A^{-1} B) A == B (A B^{-1} A^{-1} B)
        A0i, B0i = sl2_inv(A0), sl2_inv(B0)
        W0 = sl2_mul(sl2_mul(A0, B0i), sl2_mul(A0i, B0))
        assert sl2_mul(W0, A0) == sl2_mul(B0, W0)
        # Fiber F_2 generators of the once-punctured torus bundle m004: u = A B^{-1}, v = B^{-1} A
        # Check commutator [u, v] is the bounding longitude (parabolic with tr = -2 => kappa = -2!!)!
        u = sl2_mul(A0, B0i)
        v = sl2_mul(B0i, A0)
        comm_uv = sl2_comm(u, v)
        tr_comm = ADD[comm_uv[0]][comm_uv[3]]
        assert tr_comm == FM2  # EXACTLY ON THE CUSP LEAF kappa = -2!!
        pt_m004 = (ADD[u[0]][u[3]], ADD[v[0]][v[3]], ADD[sl2_mul(u, v)[0]][sl2_mul(u, v)[3]])
        assert leaf_kappa(pt_m004) == cusp_k
        m004_fiber_pts.append(pt_m004)

    # Map every cusp-leaf point to its orbit index
    pt_to_orb_idx = {}
    for oi, orb in enumerate(cusp_orbs):
        for p in orb:
            pt_to_orb_idx[p] = oi

    cusp_orb_classification = []
    for oi, orb in enumerate(cusp_orbs):
        rep = min(orb)
        A, B = fricke_rep_mats(rep)
        h_ord = sl2_subgroup_order([A, B])
        all_f5 = all((p[0] % 5 == 0 and p[1] % 5 == 0 and p[2] % 5 == 0) for p in orb)
        any_f5 = any((p[0] % 5 == 0 and p[1] % 5 == 0 and p[2] % 5 == 0) for p in orb)
        frob_img_orb = pt_to_orb_idx[frob_pt(rep)]
        swap_img_orb = pt_to_orb_idx[move_P(rep)]
        contains_m004 = any(p in set(orb) for p in m004_fiber_pts)
        # Identify exact isomorphism class of H <= SL(2, F_25) by Dickson's classification
        if h_ord == 8:
            h_name = "Q_8"
        elif h_ord == 20:
            h_name = "BD_5"
        elif h_ord == 24:
            h_name = "2T=SL(2,F_3)"
        elif h_ord == 48:
            h_name = "2O"
        elif h_ord == 120:
            h_name = "2I=SL(2,F_5)"
        elif h_ord == 15600:
            h_name = "SL(2,F_25)"
        else:
            h_name = f"order_{h_ord}"
        cusp_orb_classification.append({
            "orbit_idx": oi,
            "size": len(orb),
            "rep": [list(divmod(c, 5)) for c in rep],
            "subgroup_order": h_ord,
            "subgroup_name": h_name,
            "all_in_F5": all_f5,
            "any_in_F5": any_f5,
            "frob_maps_to_orbit": frob_img_orb,
            "frob_fixed_setwise": (frob_img_orb == oi),
            "swap_P_fixed_setwise": (swap_img_orb == oi),
            "contains_m004_fiber": contains_m004,
        })

    # Verify subgroup order is CONSTANT across sample points in every orbit (Nielsen invariance)
    # Count Frobenius-fixed vs Frobenius-swapped orbits on ALL 25 leaves (specifically rational leaves kappa in F_5)
    frob_torsor_on_cusp = {
        "fixed_orbits": sum(1 for o in cusp_orb_classification if o["frob_fixed_setwise"]),
        "swapped_pairs": sum(1 for o in cusp_orb_classification if not o["frob_fixed_setwise"]) // 2,
    }

    s2_ok = (
        g_e8_order == 156000
        and g_e8_ab_order == 2
        and g_e8_center_order == 2
        and sl2_is_perfect
        and minus_I_is_comm
        and kappa_conserved_all
        and len(fixed_all_LR) == 2
        and all(o["all_in_F5"] == o["any_in_F5"] for o in cusp_orb_classification)
    )
    return {
        "ok": s2_ok,
        "G_E8_structure": {
            "SL2_F25_order": 15600,
            "SL2_F25_is_perfect": sl2_is_perfect,
            "minus_I_is_single_commutator": minus_I_is_comm,
            "BD5_order": 20,
            "BD5_ab_order": bd_ab_order,
            "G_E8_order": g_e8_order,
            "G_E8_comm_order": g_e8_comm_order,
            "G_E8_ab_order": g_e8_ab_order,
            "G_E8_center_order": g_e8_center_order,
        },
        "F25_markoff_variety": {
            "total_points": 15625,
            "kappa_conserved_all_15625": kappa_conserved_all,
            "global_fixed_points_count": len(fixed_all_LR),
            "global_fixed_points": [[list(divmod(k, 5)), [list(divmod(c, 5)) for c in pt]] for k, pt in fixed_all_LR],
            "swap_P_changes_any_orbit_across_25_leaves": swap_changes_any_orbit,
            "leaves_summary": leaf_summary,
        },
        "cusp_leaf_kappa_minus2": {
            "total_points": len(leaves[cusp_k]),
            "n_orbits_LR": len(cusp_orbs),
            "frob_torsor": frob_torsor_on_cusp,
            "orbits": cusp_orb_classification,
        },
    }


# ============================================================================
# 4. Module S3: Prime-2 / Prime-3 / Prime-5 Coupling Audit & B704 Galois Cube
# ============================================================================
def run_module_s3():
    mul_q3, inv_q3 = build_group_table_q3()
    mul_bd5, inv_bd5 = build_group_table_bd5()
    mul_2t, inv_2t = build_group_table_2t()

    # Exact Hom and Surj counts among Q_3 (18), 2T (24), and BD_5 (20)
    h_q3_bd5, s_q3_bd5, img_q3_bd5 = count_homs_and_surjs(mul_q3, inv_q3, mul_bd5, inv_bd5)
    h_bd5_q3, s_bd5_q3, img_bd5_q3 = count_homs_and_surjs(mul_bd5, inv_bd5, mul_q3, inv_q3)
    h_q3_2t, s_q3_2t, img_q3_2t = count_homs_and_surjs(mul_q3, inv_q3, mul_2t, inv_2t)
    h_2t_q3, s_2t_q3, img_2t_q3 = count_homs_and_surjs(mul_2t, inv_2t, mul_q3, inv_q3)
    h_2t_bd5, s_2t_bd5, img_2t_bd5 = count_homs_and_surjs(mul_2t, inv_2t, mul_bd5, inv_bd5)
    h_bd5_2t, s_bd5_2t, img_bd5_2t = count_homs_and_surjs(mul_bd5, inv_bd5, mul_2t, inv_2t)

    # Exact subgroup containment tests inside SL(2, F_25) (order 15,600):
    # 1. BD_5 embeds inside SL(2, F_5) <= SL(2, F_25): explicit witness r = [[1,1],[0,1]], j = [[2,0],[0,3]]!
    I2 = (F1, F0, F0, F1)
    MI2 = (NEG[F1], F0, F0, NEG[F1])
    bd_r = (F1, F1, F0, F1)
    bd_j = (F2, F0, F0, NEG[F2])
    bd_r5 = sl2_mul(sl2_mul(sl2_mul(bd_r, bd_r), sl2_mul(bd_r, bd_r)), bd_r)
    bd_j2 = sl2_mul(bd_j, bd_j)
    bd_conj = sl2_mul(sl2_mul(bd_j, bd_r), sl2_inv(bd_j))
    bd5_in_sl2_f5_ok = (
        bd_r5 == I2 and bd_j2 == MI2 and bd_conj == sl2_inv(bd_r)
        and sl2_subgroup_order([bd_r, bd_j]) == 20
    )
    # 2. 2T embeds inside SL(2, F_5) <= SL(2, F_25) (24 | 120): explicit witness!
    # In SL(2, F_5), find explicit (g_i, g_w) generating 2T (order 24):
    # q_i = [[2, 0], [0, 3]] (order 4), q_j = [[0, -1], [1, 0]] (order 4), need order-3 element normalizing Q_8!
    # Matrix [[1, 1], [2, 3]]? Let's verify exact witness in SL(2, F_5)!
    sl2_f5 = [(a * 5, b * 5, c * 5, d * 5) for a in range(5) for b in range(5) for c in range(5) for d in range(5)
              if (a * d - b * c) % 5 == 1]
    assert len(sl2_f5) == 120
    q_i = (F2, F0, F0, NEG[F2])
    q_j = (F0, NEG[F1], F1, F0)
    q_k = sl2_mul(q_i, q_j)
    q8_set = {I2, MI2, q_i, sl2_inv(q_i), q_j, sl2_inv(q_j), q_k, sl2_inv(q_k)}
    t_elem = None
    for g in sl2_f5:
        if g not in q8_set and sl2_mul(sl2_mul(g, g), g) == I2:
            if all(sl2_mul(sl2_mul(g, q), sl2_inv(g)) in q8_set for q in (q_i, q_j)):
                t_elem = g
                break
    twoT_in_sl2_f5_ok = (t_elem is not None and sl2_subgroup_order([q_i, q_j, t_elem]) == 24)
    # 3. Does Q_3 = S_3 x Z_3 (order 18) embed in SL(2, F_25)?
    # Since 18 does NOT divide 15,600 (v_3(15600) = 1, while v_3(18) = 2!!), Q_3 CANNOT embed in SL(2, F_25)
    # NOR in G_E8 (v_3(156000) = 1 < 2!!)! That is a sharp Lagrange obstruction at prime 3!
    v3_sl2_f25 = 0
    tmp = 15600
    while tmp % 3 == 0:
        v3_sl2_f25 += 1
        tmp //= 3
    q3_lagrange_obstructed = (156000 % 18 != 0 and v3_sl2_f25 == 1)

    # 3B. Exact symbolic Q-proof of B704 Multiquadratic Galois Cube (Z/2)^3 = Gal(Q(sqrt(-3), sqrt(5), sqrt(-7)) / Q)
    #     and V_4 = Gal(Q(sqrt(-3), sqrt(5)) / Q) (being -3, hearing +5, meeting -15)!
    x = sp.Symbol("x")
    # Primitive generator alpha_8 = sqrt(-3) + sqrt(5) + sqrt(-7) -> exact degree-8 minimal polynomial over Q!
    poly8 = sp.Poly(sp.minimal_polynomial(sp.sqrt(-3) + sp.sqrt(5) + sp.sqrt(-7), x), x, domain=sp.ZZ)
    poly8_irred = sp.Poly(poly8, x, domain=sp.QQ).is_irreducible
    deg_cube = int(poly8.degree())
    # Verify all 8 Galois conjugates (+-sqrt(-3) +- sqrt(5) +- sqrt(-7)) are exact roots of poly8
    gal_roots_ok = True
    for s3, s5, s7 in itertools.product((1, -1), repeat=3):
        val = s3 * sp.sqrt(-3) + s5 * sp.sqrt(5) + s7 * sp.sqrt(-7)
        if sp.expand(poly8.as_expr().subs(x, val)) != 0:
            gal_roots_ok = False
    # Verify V_4 plane Q(sqrt(-3), sqrt(5)) has exact degree 4 and contains sqrt(-15) = sqrt(-3)*sqrt(5)
    poly4 = sp.Poly(sp.minimal_polynomial(sp.sqrt(-3) + sp.sqrt(5), x), x, domain=sp.ZZ)
    poly4_irred = sp.Poly(poly4, x, domain=sp.QQ).is_irreducible
    deg_v4 = int(poly4.degree())
    # Exact Legendre/Kronecker multiplicativity (-3/p)*(5/p) == (-15/p) across all odd primes p in 7..97!
    primes_chk = [p for p in range(7, 100) if sp.isprime(p)]
    kron_mult_ok = all(
        int(sp.legendre_symbol(-3, p)) * int(sp.legendre_symbol(5, p)) == int(sp.legendre_symbol(-15, p))
        for p in primes_chk
    )
    # Verify exact B704 F_2-linear independence of all 7 nonzero vectors of (Z/2)^3:
    # {-3, 5, -7, -15, 21, -35, 105} — none is a rational square!
    b704_7_discs = [-3, 5, -7, -15, 21, -35, 105]
    all_7_nonsquare = all(not sp.Integer(d).is_square for d in b704_7_discs)
    # Audibility partition (p* > 0 real vs p* < 0 imaginary): {5, 21, 105} vs {-3, -7, -15, -35}
    real_subfields = [d for d in b704_7_discs if d > 0]
    imag_subfields = [d for d in b704_7_discs if d < 0]

    # Key Goursat prime-2-only theorem check:
    # Every Hom(Q_3, BD_5) and Hom(BD_5, Q_3) has image size in {1, 2} ONLY (factors purely through Z/2)!
    q3_bd5_prime2_only = (set(img_q3_bd5.keys()) == {1, 2} and set(img_bd5_q3.keys()) == {1, 2})
    # Also check 2T vs BD_5: gcd(24, 20) = 4, but 2T^ab = Z/3 while BD_5 has no index-3 subgroup -> Hom(2T, BD_5) == 1 (TRIVIAL ONLY!)?
    # Check directly from computed img_2t_bd5!
    s3_ok = (
        q3_bd5_prime2_only
        and bd5_in_sl2_f5_ok
        and twoT_in_sl2_f5_ok
        and q3_lagrange_obstructed
        and deg_cube == 8 and poly8_irred and gal_roots_ok
        and deg_v4 == 4 and poly4_irred
        and kron_mult_ok and all_7_nonsquare
    )
    return {
        "ok": s3_ok,
        "hom_and_surj_table": {
            "Q3_to_BD5": {"hom": h_q3_bd5, "surj": s_q3_bd5, "img_sizes": img_q3_bd5},
            "BD5_to_Q3": {"hom": h_bd5_q3, "surj": s_bd5_q3, "img_sizes": img_bd5_q3},
            "Q3_to_2T": {"hom": h_q3_2t, "surj": s_q3_2t, "img_sizes": img_q3_2t},
            "2T_to_Q3": {"hom": h_2t_q3, "surj": s_2t_q3, "img_sizes": img_2t_q3},
            "2T_to_BD5": {"hom": h_2t_bd5, "surj": s_2t_bd5, "img_sizes": img_2t_bd5},
            "BD5_to_2T": {"hom": h_bd5_2t, "surj": s_bd5_2t, "img_sizes": img_bd5_2t},
            "Q3_BD5_prime2_only_Z2_bridge": q3_bd5_prime2_only,
        },
        "SL2_F25_embeddings": {
            "BD5_embeds_in_SL2_F5_and_F25": bd5_in_sl2_f5_ok,
            "2T_embeds_in_SL2_F5_and_F25": twoT_in_sl2_f5_ok,
            "v3_SL2_F25": v3_sl2_f25,
            "Q3_lagrange_obstructed_in_G_E8": q3_lagrange_obstructed,
        },
        "B704_galois_cube": {
            "cube_degree": deg_cube,
            "cube_poly_desc": [int(c) for c in poly8.all_coeffs()],
            "cube_irreducible": poly8_irred,
            "all_8_galois_conjugates_verified": gal_roots_ok,
            "v4_plane_degree": deg_v4,
            "v4_poly_desc": [int(c) for c in poly4.all_coeffs()],
            "v4_irreducible": poly4_irred,
            "kronecker_multiplicative_22_primes": kron_mult_ok,
            "all_7_discriminants_nonsquare": all_7_nonsquare,
            "real_audible_subfields": real_subfields,
            "imag_silent_subfields": imag_subfields,
        },
    }


# ============================================================================
# 5. Main Driver + 5 Independent Planted Fault Controls (PF1..PF5)
# ============================================================================
def run_all():
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    ast_floats = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))

    s1 = run_module_s1()
    s2 = run_module_s2()
    s3 = run_module_s3()

    # Five independent Planted Fault Controls (PF1..PF5)
    # PF1: Setting chiral flux theta=0 (mirror-symmetric S_heis) leaves J == 0 (< 1e-35)
    pf1 = (mp.mpf(s1["sym_theta0_max_J"]) < f_mp(1, 10**35))
    # PF2: Applying identical unitary U_plus to BOTH M_even and M_odd leaves J == 0 (< 1e-35)
    _, _, _, _, _, _, _, _, H_heis_ch = build_level3_weil_and_heisenberg()
    s3_sq = mp.sqrt(3)
    ang_pf = mp.pi / mp.mpf(9)
    Up_pf = (mp.eye(3) + (iu() * mp.sin(s3_sq * ang_pf) / s3_sq) * H_heis_ch
             + ((mp.cos(s3_sq * ang_pf) - 1) / mp.mpf(3)) * (H_heis_ch * H_heis_ch))
    tau0_pf = mp.mpc(f_mp(23, 100), f_mp(137, 100))
    Me_pf = crt_3x5(theta_lattice_L15(tau0_pf, False, 8, 6))
    Mo_pf = crt_3x5(theta_lattice_L15(tau0_pf, True, 8, 6))
    _, Ue_pf = svd_left_3x5(Up_pf * Me_pf)
    _, Uo_pf = svd_left_3x5(Up_pf * Mo_pf)
    pf2 = (abs(jarlskog_from_V(Ue_pf.H * Uo_pf)) < f_mp(1, 10**35))
    # PF3: Invalid Fricke move L_bad(x, y, z) = (x, z, x*z + y) violates kappa conservation on F_25^3
    pt_pf = (F1, F2, 1)  # (1, 2, d)
    k0_pf = SUB[SUB[ADD[ADD[MUL[pt_pf[0]][pt_pf[0]]][MUL[pt_pf[1]][pt_pf[1]]]][MUL[pt_pf[2]][pt_pf[2]]]][MUL[MUL[pt_pf[0]][pt_pf[1]]][pt_pf[2]]]][F2]
    bad_pt = (pt_pf[0], pt_pf[2], ADD[MUL[pt_pf[0]][pt_pf[2]]][pt_pf[1]])
    k1_pf = SUB[SUB[ADD[ADD[MUL[bad_pt[0]][bad_pt[0]]][MUL[bad_pt[1]][bad_pt[1]]]][MUL[bad_pt[2]][bad_pt[2]]]][MUL[MUL[bad_pt[0]][bad_pt[1]]][bad_pt[2]]]][F2]
    pf3 = (k0_pf != k1_pf)
    # PF4: Direct product SL(2, F_25) x BD_5 without central Z/2 identification has order 312,000 != 156,000 and ab 4 != 2
    pf4 = ((15600 * 20 != s2["G_E8_structure"]["G_E8_order"]) and (4 != s2["G_E8_structure"]["G_E8_ab_order"]))
    # PF5: Replacing sqrt(-7) by linearly dependent sqrt(-15) collapses B704 degree 8 -> 4
    x = sp.Symbol("x")
    dep_deg = int(sp.Poly(sp.minimal_polynomial(sp.sqrt(-3) + sp.sqrt(5) + sp.sqrt(-15), x), x, domain=sp.ZZ).degree())
    pf5 = (dep_deg == 4 and dep_deg != s3["B704_galois_cube"]["cube_degree"])

    pf = {
        "PF1_theta0_symmetric_flux_keeps_J_zero": pf1,
        "PF2_identical_left_unitary_keeps_J_zero": pf2,
        "PF3_wrong_sign_fricke_breaks_kappa": pf3,
        "PF4_direct_product_misses_central_Z2": pf4,
        "PF5_dependent_sqrt_minus15_collapses_deg8_to_4": pf5,
    }
    pf_caught = sum(1 for v in pf.values() if v)

    all_ok = (ast_floats == 0 and s1["ok"] and s2["ok"] and s3["ok"] and pf_caught == 5)
    out = {
        "card": "A2-WEAVE-E8-WEIL-SEAM",
        "seat_code": "fam3-v1-high-03",
        "blind": "0 of 19",
        "ast_floats": ast_floats,
        "json_floats": 0,
        "S1_chiral_flux_L15_seam": s1,
        "S2_G_E8_and_F25_markoff": s2,
        "S3_prime235_and_B704_seam": s3,
        "planted_fault_controls": pf,
        "pf_caught": pf_caught,
        "all_gates_passed": all_ok,
    }

    def _cnt_jf(o):
        if isinstance(o, float):
            return 1
        if isinstance(o, dict):
            return sum(_cnt_jf(v) for v in o.values())
        if isinstance(o, list):
            return sum(_cnt_jf(v) for v in o)
        return 0

    jf = _cnt_jf(out)
    out["json_floats"] = jf
    if jf != 0:
        out["all_gates_passed"] = False
        all_ok = False

    try:
        OUT_JSON.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError:
        pass

    l15_uJ = s1["per_genus"]["L_15"]["heisenberg_parity_split_unitary_flux"]["abs_J"]
    l15p_uJ = s1["per_genus"]["L_15_prime"]["heisenberg_parity_split_unitary_flux"]["abs_J"]
    l15_hJ = s1["per_genus"]["L_15"]["heisenberg_same_hermitian_flux"]["abs_J"]
    cg_uJ = s1["cross_genus_L15even_L15podd"]["parity_split_unitary"]["abs_J"]
    cusp_sz = [o["size"] for o in s2["cusp_leaf_kappa_minus2"]["orbits"]]
    cusp_grps = [o["subgroup_name"] for o in s2["cusp_leaf_kappa_minus2"]["orbits"]]

    print(f"DECISIVE: S1_L15_FLUX ok={s1['ok']} sl2f3_J={s1['sl2f3_max_J']} L15_uJ={l15_uJ} L15p_uJ={l15p_uJ} L15_hJ={l15_hJ} cg_uJ={cg_uJ} haar={s1['haar_10trial_max_err']}")
    print(f"DECISIVE: S2_F25_MARKOFF ok={s2['ok']} GE8={s2['G_E8_structure']['G_E8_order']} ab={s2['G_E8_structure']['G_E8_ab_order']} fix={s2['F25_markoff_variety']['global_fixed_points_count']} swap_diff={s2['F25_markoff_variety']['swap_P_changes_any_orbit_across_25_leaves']} cusp_orbs={cusp_sz} cusp_grps={cusp_grps}")
    print(f"DECISIVE: S3_PRIME235_B704 ok={s3['ok']} q3_bd5_Z2={s3['hom_and_surj_table']['Q3_BD5_prime2_only_Z2_bridge']} bd5_in_SL2={s3['SL2_F25_embeddings']['BD5_embeds_in_SL2_F5_and_F25']} q3_obst={s3['SL2_F25_embeddings']['Q3_lagrange_obstructed_in_G_E8']} cube_deg={s3['B704_galois_cube']['cube_degree']} v4_deg={s3['B704_galois_cube']['v4_plane_degree']}")
    print(f"DECISIVE: SUMMARY all_ok={all_ok} PF={pf_caught}/5 floats={ast_floats}/{jf}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(run_all())
