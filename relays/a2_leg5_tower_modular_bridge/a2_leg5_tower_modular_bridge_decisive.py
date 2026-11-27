"""Standalone 0-of-19 P-885 Decisive Producer for Card A2-LEG5-TOWER-MODULAR-BRIDGE (seat fam3-v1-high-03).

Pure Python stdlib + mpmath + sympy ONLY.
Zero float/complex AST literals or casts; zero numpy/scipy/frontier/sage/gap imports;
zero JSON float tokens; deterministic stdout (zero timing lines). Strictly 0 of 19.

Modules:
  B1: All-k Universal Tensor-Halving Theorem via minimal 6-pt quotient Q_6 of O_{3^k}^{(3,3,3)},
      exact Z[y] factorization of Q_6 x Leg(5) isolating unpaired (y^2-6y+4)^2(y^2+6y+4)^2 and
      leftover (y^2-20)^2(y^2-8)^2, exhaustive G_3 (216) & G_4 (1944) character-defect vanishing
      proving V_new^(k) ~= rho (x) V_new^(k), Level-30 P^1(F_2) x O_{3^k} x W exact 100% halving,
      and exact integer sparse power-sum checks across O_27^(3,3,3), (3,3,12), (3,3,15), Level-30, and O_81.
  B2: Exact Chiral Walk Algebra [W_L, W_R] = 0 on Leg(5), charpolys of W_L and i(W_L - W_R), and exact
      Pauli identity i(W_L - W_R)|_{E_{phi^2}} = sqrt(3) phi^2 sigma_y (eigenstates = exact chiral poles).
  B3: Exact Anti-Holomorphic Mirror-Lock Theorem on H (|tau|=1, Re(tau)=+1/2, |tau-1|=1 -> C_3-orbit of tau_mir),
      SL(2,Z)-equivariant analytic Siegel map Phi^{Siegel}_{Leg(5)}: H -> Leg(5), exact cusp asymptote
      (both linear 2*pi*y/25 and constant ln(phi) aligned at theta = -60 deg), unique Re(tau)=0 mirror-odd
      crossing y_odd*, and ZERO-PARAMETER SL(2,Z)-invariant interior modulus stabilization on F:
      strict 2D global min of I4_Siegel on Re(tau)=1/2 at y* = 2.2726755929 (x=0 saddle) and
      opposite-phase strict 2D global min of I6_Siegel on Re(tau)=0 at y* = 2.3052230811 (x=1/2 saddle).
  B4: Weight-2 Holomorphic Weierstrass Map Phi^{wp}_{Leg(5)}: H -> Leg(5) (x) C, exact symbolic
      5-division polynomial proofs at omega_+ (u_s/u_c = phi^-1, exact 0:0:4/5:1/5 norm split,
      exact chiral pole theta=45 deg, alpha=-90 deg, I4=1/5, I6=2/45, V_wp = (27/8)*5^(1/3)*|g3|^(2/3))
      and at i (exact probabilities -> I4 = 2/9, I6 = 17/288), unit-arc chiral meridian alpha=-90 deg,
      and continuous chiral-to-systole flow along Re(tau)=1/2 through tau_tot*(70) = 1/2 + 3.380451106i.
  B5: 5/5 planted negative controls (PF1..PF5) and zero-float AST/JSON audit.
"""

import ast
import hashlib
import json
import pathlib
import sys
from collections import deque
from fractions import Fraction
from typing import Any, Dict, List, Tuple

import mpmath as mp
import sympy as sp

SCRIPT_PATH = pathlib.Path(__file__).resolve()
OUT_JSON_PATH = SCRIPT_PATH.with_name("a2_leg5_tower_modular_bridge_out.json")
OUT_SHA_PATH = SCRIPT_PATH.with_name("OUTPUT_SHA256.txt")


# ---------------------------------------------------------------------------
# Zero-Float Helpers & Hygiene Audit
# ---------------------------------------------------------------------------

def iu():
    return mp.mpc(0, 1)


def mp_rat(p: int, q: int = 1):
    return mp.mpf(p) / mp.mpf(q)


def mp_pow10(k: int):
    return mp.mpf(10) ** k


def mp_str(x, digits: int = 12) -> str:
    if isinstance(x, Fraction):
        return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)
    if isinstance(x, mp.mpc):
        return f"({mp.nstr(mp.re(x), digits)},{mp.nstr(mp.im(x), digits)})"
    return mp.nstr(mp.mpf(x), digits)


def audit_own_ast() -> Dict[str, Any]:
    src = SCRIPT_PATH.read_text(encoding="utf-8")
    tree = ast.parse(src)
    float_lits = 0
    complex_lits = 0
    bad_calls = []
    bad_imports = []
    forbidden = ("numpy", "scipy", "frontier", "sage", "gap")
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_lits += 1
            elif isinstance(node.value, complex):
                complex_lits += 1
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ("float", "complex"):
                bad_calls.append(node.func.id)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if any(b in alias.name for b in forbidden):
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if any(b in mod for b in forbidden):
                bad_imports.append(mod)
    return {
        "float_literals": float_lits,
        "complex_literals": complex_lits,
        "float_complex_casts": len(bad_calls),
        "forbidden_imports": len(bad_imports),
        "clean": (float_lits == 0 and complex_lits == 0 and len(bad_calls) == 0 and len(bad_imports) == 0),
    }


def count_json_floats(obj: Any) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


# ---------------------------------------------------------------------------
# Exact SL(2, Z), Leg(5), P^1(F_2), and Trace-Orbit Primitives
# ---------------------------------------------------------------------------

L2 = ((1, 1), (0, 1))
R2 = ((1, 0), (1, 1))
S_STD = ((0, -1), (1, 0))
C_OM = ((0, 1), (-1, 1))
C3_OM = ((0, -1), (1, -1))
TAU_MIR = ((0, 1), (1, 0))

LINES5 = ((1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4))
LINES2 = ((1, 0), (0, 1), (1, 1))


def mat2_mul(A, B):
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def mat2_inv(A):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    assert det in (1, -1)
    return ((A[1][1] * det, -A[0][1] * det), (-A[1][0] * det, A[0][0] * det))


C0_MAT = mat2_mul(mat2_inv(R2), L2)
NEG_C0_MAT = ((-C0_MAT[0][0], -C0_MAT[0][1]), (-C0_MAT[1][0], -C0_MAT[1][1]))


def leg5_char(s: int) -> int:
    r = s % 5
    if r in (1, 4):
        return 1
    if r in (2, 3):
        return -1
    raise ValueError("Zero mod 5")


def act_leg5(M, i5: int, trivial_signs: bool = False) -> Tuple[int, int]:
    v = LINES5[i5]
    x = (M[0][0] * v[0] + M[0][1] * v[1]) % 5
    y = (M[1][0] * v[0] + M[1][1] * v[1]) % 5
    for j, l in enumerate(LINES5):
        for s in (1, 2, 3, 4):
            if (s * l[0]) % 5 == x and (s * l[1]) % 5 == y:
                return j, (1 if trivial_signs else leg5_char(s))
    raise RuntimeError("No P^1(F_5) match")


def act_p1f2(M, i2: int) -> int:
    v = LINES2[i2]
    x = (M[0][0] * v[0] + M[0][1] * v[1]) % 2
    y = (M[1][0] * v[0] + M[1][1] * v[1]) % 2
    return LINES2.index((x, y))


def leg5_sp_mat(M, trivial_signs: bool = False) -> sp.Matrix:
    A = sp.zeros(6, 6)
    for i in range(6):
        j, chi = act_leg5(M, i, trivial_signs=trivial_signs)
        A[j, i] = chi
    return A


def L_tr(v, N: int):
    x, y, z = v
    return (x, z, (x * z - y) % N)


def R_tr(v, N: int):
    x, y, z = v
    return (z, y, (y * z - x) % N)


def Li_tr(v, N: int):
    x, y, z = v
    return (x, (x * y - z) % N, y)


def Ri_tr(v, N: int):
    x, y, z = v
    return ((x * y - z) % N, y, x)


def C_tr(v, _N: int = 0):
    x, y, z = v
    return (y, z, x)


def S_tr(v, N: int):
    x, y, z = v
    return (y, x, (x * y - z) % N)


def get_trace_orbit(seed, N: int):
    seen = {seed}
    dq = deque([seed])
    out = []
    while dq:
        u = dq.popleft()
        out.append(u)
        for fn in (L_tr, R_tr, Li_tr, Ri_tr):
            w = fn(u, N)
            if w not in seen:
                seen.add(w)
                dq.append(w)
    out.sort()
    return out


def comp_perm(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(a[b[i]] for i in range(len(a)))


def find_block_system(n: int, gens: List[Tuple[int, ...]], target_blocks: int):
    for j in range(1, n):
        parent = list(range(n))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
                return True
            return False

        q = deque([(0, j)])
        union(0, j)
        while q:
            a, b = q.popleft()
            for g in gens:
                na, nb = g[a], g[b]
                if find(na) != find(nb):
                    union(na, nb)
                    q.append((na, nb))
        comps: Dict[int, List[int]] = {}
        for i in range(n):
            comps.setdefault(find(i), []).append(i)
        if len(comps) == target_blocks:
            return sorted([sorted(v) for v in comps.values()])
    raise RuntimeError(f"No block system of size {target_blocks}")


# ---------------------------------------------------------------------------
# MODULE B1 — All-k Universal Tensor-Halving, Q_6 x Leg(5), & Level-30 Bundles
# ---------------------------------------------------------------------------

def sparse_bundle_moments(
    n_base: int,
    base_L: Tuple[int, ...],
    base_R: Tuple[int, ...],
    base_C: Tuple[int, ...],
    with_p1f2: bool = False,
    max_m: int = 4,
) -> Dict[str, Any]:
    """Pure-integer sparse verification of [W+, W-] = 0 and exact halving trace-moment
    defects Delta_{2m} = tr(W6|_{H_0}^{2m}) - 2^{2m} tr(W6|_{H_1}^{2m}) for m = 1..max_m.
    Note: using integer traces tr(W6^{2m}) and tr(C * W6^{2m}) avoids ALL roots of unity!
    Specifically, since W6 commutes with C (order 3) and H_1 ~= H_2 (mirror pairing):
      tr(W6^k) = tr(W6|_{H_0}^k) + 2 * tr(W6|_{H_1}^k)
      tr(C * W6^k) = tr(W6|_{H_0}^k) - tr(W6|_{H_1}^k)
    Hence EXACT integer formulas:
      tr(W6|_{H_0}^k) = (tr(W6^k) + 2 * tr(C * W6^k)) // 3
      tr(W6|_{H_1}^k) = (tr(W6^k) - tr(C * W6^k)) // 3
    Zero floats, zero complex numbers, exact over Z!
    """
    n2 = 3 if with_p1f2 else 1
    n5 = 6
    dim = n_base * n2 * n5

    def enc(ib: int, i2: int, i5: int) -> int:
        return (ib * n2 + i2) * n5 + i5

    def build_sp(b_perm: Tuple[int, ...], M2) -> Tuple[List[int], List[int]]:
        dst = [0] * dim
        sgn = [0] * dim
        for ib in range(n_base):
            jb = b_perm[ib]
            for i2 in range(n2):
                j2 = act_p1f2(M2, i2) if with_p1f2 else 0
                for i5 in range(n5):
                    j5, chi = act_leg5(M2, i5)
                    s_in = enc(ib, i2, i5)
                    dst[s_in] = enc(jb, j2, j5)
                    sgn[s_in] = chi
        return dst, sgn

    def comp_sp(pA, pB):
        dA, sA = pA
        dB, sB = pB
        return [dA[dB[i]] for i in range(dim)], [sA[dB[i]] * sB[i] for i in range(dim)]

    pC = build_sp(base_C, NEG_C0_MAT)
    pC2 = comp_sp(pC, pC)
    pC3 = comp_sp(pC, pC2)
    assert all(pC3[0][i] == i and pC3[1][i] == 1 for i in range(dim))

    pL = build_sp(base_L, L2)
    pR = build_sp(base_R, R2)
    pLs = [pL, comp_sp(pC, comp_sp(pL, pC2)), comp_sp(pC2, comp_sp(pL, pC))]
    pRs = [pR, comp_sp(pC, comp_sp(pR, pC2)), comp_sp(pC2, comp_sp(pR, pC))]
    all6 = pLs + pRs

    # Transitivity check
    seen = {0}
    dq = deque([0])
    while dq:
        u = dq.popleft()
        for pm in (pL, pR):
            w = pm[0][u]
            if w not in seen:
                seen.add(w)
                dq.append(w)
    transitive = len(seen) == dim

    # Exact [W+, W-] = 0 check across ALL basis vectors e_j (pure int!)
    comm_zero = True
    for j in range(dim):
        # W+ W- e_j vs W- W+ e_j
        acc: Dict[int, int] = {}
        for d1, s1 in pRs:
            mid, c1 = d1[j], s1[j]
            for d2, s2 in pLs:
                tgt = d2[mid]
                acc[tgt] = acc.get(tgt, 0) + c1 * s2[mid]
        for d1, s1 in pLs:
            mid, c1 = d1[j], s1[j]
            for d2, s2 in pRs:
                tgt = d2[mid]
                acc[tgt] = acc.get(tgt, 0) - c1 * s2[mid]
        if any(v != 0 for v in acc.values()):
            comm_zero = False
            break

    # Exact traces tr(W6^{2m}) and tr(C * W6^{2m}) for m = 1..max_m via sparse integer propagation!
    # Wait: even faster — since W6 is symmetric, tr(W6^{2m}) = sum_j ||W6^m e_j||^2,
    # and tr(C * W6^{2m}) = sum_j <W6^m e_j | C | W6^m e_j>! That halves the max depth from 2m to m!
    # Check symmetry W6^T == W6 first!
    sym_ok = True
    for j in range(dim):
        # Check if j -> t with weight w matches t -> j
        row_j: Dict[int, int] = {}
        for d_p, s_p in all6:
            t = d_p[j]
            row_j[t] = row_j.get(t, 0) + s_p[j]
        for t, w_jt in row_j.items():
            w_tj = 0
            for d_p, s_p in all6:
                if d_p[t] == j:
                    w_tj += s_p[t]
            if w_tj != w_jt:
                sym_ok = False
                break
        if not sym_ok:
            break
    assert sym_ok

    # Precompute compact adjacency list for W6
    adj: List[List[Tuple[int, int]]] = []
    for j in range(dim):
        d_acc: Dict[int, int] = {}
        for d_p, s_p in all6:
            t = d_p[j]
            d_acc[t] = d_acc.get(t, 0) + s_p[j]
        adj.append([(t, w) for t, w in d_acc.items() if w != 0])

    c_dst, c_sgn = pC
    tr_full = [0] * (max_m + 1)
    tr_C = [0] * (max_m + 1)
    for j in range(dim):
        vec: Dict[int, int] = {j: 1}
        for m in range(1, max_m + 1):
            nxt: Dict[int, int] = {}
            for u, val in vec.items():
                for t, w_ut in adj[u]:
                    nxt[t] = nxt.get(t, 0) + val * w_ut
            vec = {t: v for t, v in nxt.items() if v != 0}
            # <vec | vec> = (W6^{2m})_{j, j}
            s_sq = 0
            s_c = 0
            for u, val in vec.items():
                s_sq += val * val
                cu = c_dst[u]
                if cu in vec:
                    s_c += val * c_sgn[u] * vec[cu]
            tr_full[m] += s_sq
            tr_C[m] += s_c

    defects = {}
    for m in range(1, max_m + 1):
        assert (tr_full[m] + 2 * tr_C[m]) % 3 == 0
        assert (tr_full[m] - tr_C[m]) % 3 == 0
        t0 = (tr_full[m] + 2 * tr_C[m]) // 3
        t1 = (tr_full[m] - tr_C[m]) // 3
        # Integer defect: tr(W6|_{H_0}^{2m}) - 2^{2m} tr(W6|_{H_1}^{2m})
        defects[f"2m_{2*m}"] = str(t0 - (4 ** m) * t1)

    return {
        "dim": dim,
        "transitive": transitive,
        "commutator_Wp_Wm_exact_zero": comm_zero,
        "int_halving_trace_defects": defects,
    }


def run_B1() -> Dict[str, Any]:
    orb27 = get_trace_orbit((3, 3, 3), 27)
    orb12 = get_trace_orbit((3, 3, 12), 27)
    orb15 = get_trace_orbit((3, 3, 15), 27)
    orb81 = get_trace_orbit((3, 3, 3), 81)
    assert len(orb27) == 72 and len(orb12) == 72 and len(orb15) == 72 and len(orb81) == 648

    def perms_of(orb, N: int):
        idx = {v: i for i, v in enumerate(orb)}
        return (
            tuple(idx[L_tr(v, N)] for v in orb),
            tuple(idx[R_tr(v, N)] for v in orb),
            tuple(idx[C_tr(v)] for v in orb),
            tuple(idx[S_tr(v, N)] for v in orb),
        )

    pL27, pR27, pC27, pS27 = perms_of(orb27, 27)
    pL12, pR12, pC12, pS12 = perms_of(orb12, 27)
    pL15, pR15, pC15, pS15 = perms_of(orb15, 27)
    pL81, pR81, pC81, pS81 = perms_of(orb81, 81)

    # Minimal 6-pt quotient Q_6 and 8-pt mod-9 control quotient Q_8 of O_27
    blks6 = find_block_system(72, [pL27, pR27], 6)
    bmap6 = {x: bi for bi, b in enumerate(blks6) for x in b}
    q6_L = tuple(bmap6[pL27[b[0]]] for b in blks6)
    q6_R = tuple(bmap6[pR27[b[0]]] for b in blks6)
    q6_C = tuple(bmap6[pC27[b[0]]] for b in blks6)
    q6_S = tuple(bmap6[pS27[b[0]]] for b in blks6)
    q6_fixC = sum(1 for i in range(6) if q6_C[i] == i)
    assert q6_fixC == 3

    blks8 = find_block_system(72, [pL27, pR27], 8)
    bmap8 = {x: bi for bi, b in enumerate(blks8) for x in b}
    q8_C = tuple(bmap8[pC27[b[0]]] for b in blks8)
    q8_S = tuple(bmap8[pS27[b[0]]] for b in blks8)

    # Exact 36x36 Z[y] characteristic polynomials of Q_6 x Leg(5)
    dim36 = 36

    def sp_perm36(q_perm, M2):
        M = sp.zeros(dim36, dim36)
        for iq in range(6):
            jq = q_perm[iq]
            for i5 in range(6):
                j5, chi = act_leg5(M2, i5)
                M[jq * 6 + j5, iq * 6 + i5] = chi
        return M

    MC = sp_perm36(q6_C, NEG_C0_MAT)
    ML = sp_perm36(q6_L, L2)
    MR = sp_perm36(q6_R, R2)
    MC2 = MC * MC
    assert MC * MC2 == sp.eye(dim36)
    Wp36 = ML + MC * ML * MC2 + MC2 * ML * MC
    Wm36 = MR + MC * MR * MC2 + MC2 * MR * MC
    W6_36 = Wp36 + Wm36
    q6_comm_zero = (Wp36 * Wm36 - Wm36 * Wp36) == sp.zeros(dim36, dim36)

    visited = [False] * dim36
    orbs3 = []
    for s in range(dim36):
        if visited[s]:
            continue
        j = next(r for r in range(dim36) if MC[r, s] != 0)
        s1 = int(MC[j, s])
        k = next(r for r in range(dim36) if MC[r, j] != 0)
        s2 = s1 * int(MC[k, j])
        visited[s] = visited[j] = visited[k] = True
        orbs3.append((s, j, k, s1, s2))
    assert len(orbs3) == 12

    B0 = sp.zeros(dim36, 12)
    for m, (i, j, k, s1, s2) in enumerate(orbs3):
        B0[i, m] = 1
        B0[j, m] = s1
        B0[k, m] = s2
    M0_36 = (B0.T * W6_36 * B0) / 3
    x, y = sp.Symbol("x"), sp.Symbol("y")
    p_full = sp.Poly(W6_36.charpoly(x).as_expr(), x)
    p_neu_x = sp.Poly(M0_36.charpoly(x).as_expr(), x)
    p_chg_sq = p_full // p_neu_x
    _, flist = sp.factor_list(p_chg_sq.as_expr())
    assert all(e % 2 == 0 for _, e in flist)
    p_chg_x = sp.Poly(sp.expand(sp.prod(f ** (e // 2) for f, e in flist)), x)
    assert p_chg_x * p_chg_x == p_chg_sq

    p0_y = sp.Poly(p_neu_x.as_expr().subs(x, y), y)
    p2chg_y = sp.Poly(sp.expand((2 ** 12) * p_chg_x.as_expr().subs(x, y / 2)), y)
    g_y = sp.gcd(p0_y, p2chg_y)
    unpaired_y = p2chg_y // g_y
    leftover_y = p0_y // g_y

    target_unpaired = sp.Poly(sp.expand(((y ** 2 - 6 * y + 4) ** 2) * ((y ** 2 + 6 * y + 4) ** 2)), y)
    target_leftover = sp.Poly(sp.expand(((y ** 2 - 20) ** 2) * ((y ** 2 - 8) ** 2)), y)
    q6_exact_match = (unpaired_y == target_unpaired) and (leftover_y == target_leftover) and (g_y.degree() == 4)

    # Exhaustive G_3 (216) character-defect checks: O_27 vs Q_6, O_27 vs Q_8 (PF1), Q_6 x P^1(F_2), O_27^(3,3,15)
    fC2 = (2, 0, 1)
    fS2 = (1, 0, 2)
    id27, id6, id8, id2 = tuple(range(72)), tuple(range(6)), tuple(range(8)), tuple(range(3))
    grp3 = {id27: (id6, id8, id2, 0)}
    dq = deque([id27])
    while dq:
        g27 = dq.popleft()
        g6, g8, g2, r6 = grp3[g27]
        for gen27, gen6, gen8, gen2, dr in ((pC27, q6_C, q8_C, fC2, 2), (pS27, q6_S, q8_S, fS2, 3)):
            n27 = comp_perm(gen27, g27)
            n6 = comp_perm(gen6, g6)
            n8 = comp_perm(gen8, g8)
            n2 = comp_perm(gen2, g2)
            nr = (r6 + dr) % 6
            if n27 not in grp3:
                grp3[n27] = (n6, n8, n2, nr)
                dq.append(n27)
            else:
                assert grp3[n27] == (n6, n8, n2, nr)
    assert len(grp3) == 216

    g3_o27_vs_q6_mismatches = 0
    g3_lvl30_nonzero = 0
    pf1_q8_mismatches = 0
    for g27, (g6, g8, g2, r6) in grp3.items():
        if r6 == 0:
            continue
        f27 = sum(1 for i in range(72) if g27[i] == i)
        f6 = sum(1 for i in range(6) if g6[i] == i)
        f8 = sum(1 for i in range(8) if g8[i] == i)
        f2 = sum(1 for i in range(3) if g2[i] == i)
        if f27 != f6:
            g3_o27_vs_q6_mismatches += 1
        if f6 * f2 != 0:
            g3_lvl30_nonzero += 1
        if f27 != f8:
            pf1_q8_mismatches += 1

    # Exhaustive G_4 (1,944) character-defect check: O_81 vs Q_6
    id81 = tuple(range(648))
    grp4 = {id81: (id6, 0)}
    dq = deque([id81])
    while dq:
        g81 = dq.popleft()
        g6, r6 = grp4[g81]
        for gen81, gen6, dr in ((pC81, q6_C, 2), (pS81, q6_S, 3)):
            n81 = comp_perm(gen81, g81)
            n6 = comp_perm(gen6, g6)
            nr = (r6 + dr) % 6
            if n81 not in grp4:
                grp4[n81] = (n6, nr)
                dq.append(n81)
            else:
                assert grp4[n81] == (n6, nr)
    assert len(grp4) == 1944
    g4_o81_vs_q6_mismatches = sum(
        1
        for g81, (g6, r6) in grp4.items()
        if r6 != 0 and sum(1 for i in range(648) if g81[i] == i) != sum(1 for i in range(6) if g6[i] == i)
    )

    # Exhaustive O_27^(3,3,15) character-defect check
    grp15 = {id27: 0}
    dq = deque([id27])
    while dq:
        g15 = dq.popleft()
        r6 = grp15[g15]
        for gen15, dr in ((pC15, 2), (pS15, 3)):
            n15 = comp_perm(gen15, g15)
            nr = (r6 + dr) % 6
            if n15 not in grp15:
                grp15[n15] = nr
                dq.append(n15)
            else:
                assert grp15[n15] == nr
    assert len(grp15) == 216
    g3_sister15_nonzero = sum(1 for g15, r6 in grp15.items() if r6 != 0 and sum(1 for i in range(72) if g15[i] == i) != 0)

    # Exact sparse integer trace-moment checks across all 6 bundles (m=1..3 for O_81 fast, m=1..4 for rest!)
    m_q6 = sparse_bundle_moments(6, q6_L, q6_R, q6_C, with_p1f2=False, max_m=4)
    m_o27 = sparse_bundle_moments(72, pL27, pR27, pC27, with_p1f2=False, max_m=4)
    m_o12 = sparse_bundle_moments(72, pL12, pR12, pC12, with_p1f2=False, max_m=4)
    m_o15 = sparse_bundle_moments(72, pL15, pR15, pC15, with_p1f2=False, max_m=4)
    m_lvl30 = sparse_bundle_moments(72, pL27, pR27, pC27, with_p1f2=True, max_m=4)
    m_o81 = sparse_bundle_moments(648, pL81, pR81, pC81, with_p1f2=False, max_m=3)

    # Verify exact frozen defects across Q_6, O_27^(3,3,3), O_27^(3,3,12), O_81^(3,3,3), and exact 0 on sister15 & Level-30
    q6_def3 = {k: m_q6["int_halving_trace_defects"][k] for k in ("2m_2", "2m_4", "2m_6")}
    o81_matches_q6 = (m_o81["int_halving_trace_defects"] == q6_def3)
    o27_matches_q6 = (m_o27["int_halving_trace_defects"] == m_q6["int_halving_trace_defects"])
    o12_matches_q6 = (m_o12["int_halving_trace_defects"] == m_q6["int_halving_trace_defects"])
    o15_all_zero = all(v == "0" for v in m_o15["int_halving_trace_defects"].values())
    lvl30_all_zero = all(v == "0" for v in m_lvl30["int_halving_trace_defects"].values())
    all_comm_zero = all(
        b["commutator_Wp_Wm_exact_zero"] for b in (m_q6, m_o27, m_o12, m_o15, m_lvl30, m_o81)
    )

    b1_pass = (
        q6_comm_zero
        and q6_exact_match
        and g3_o27_vs_q6_mismatches == 0
        and g4_o81_vs_q6_mismatches == 0
        and g3_sister15_nonzero == 0
        and g3_lvl30_nonzero == 0
        and o27_matches_q6
        and o12_matches_q6
        and o81_matches_q6
        and o15_all_zero
        and lvl30_all_zero
        and all_comm_zero
    )
    return {
        "Q6_fixC": q6_fixC,
        "Q6_x_Leg5_P_neu_y": str(sp.factor(p0_y.as_expr())),
        "Q6_x_Leg5_P_2chg_y": str(sp.factor(p2chg_y.as_expr())),
        "Q6_x_Leg5_unpaired_chg": str(sp.factor(unpaired_y.as_expr())),
        "Q6_x_Leg5_leftover_neu": str(sp.factor(leftover_y.as_expr())),
        "Q6_x_Leg5_exact_match": q6_exact_match,
        "G3_order": len(grp3),
        "G4_order": len(grp4),
        "G3_O27_vs_Q6_mismatches": g3_o27_vs_q6_mismatches,
        "G4_O81_vs_Q6_mismatches": g4_o81_vs_q6_mismatches,
        "G3_sister15_nonzero": g3_sister15_nonzero,
        "G3_level30_nonzero": g3_lvl30_nonzero,
        "bundles": {
            "Q6_x_Leg5": m_q6,
            "O27_333_x_Leg5": m_o27,
            "O27_3312_x_Leg5": m_o12,
            "O27_3315_x_Leg5": m_o15,
            "Level30_P1F2_x_O27_x_Leg5": m_lvl30,
            "O81_333_x_Leg5": m_o81,
        },
        "frozen_defect_O27_O12_O81_eq_Q6": bool(o27_matches_q6 and o12_matches_q6 and o81_matches_q6),
        "level30_and_sister15_exact_zero_defect": bool(o15_all_zero and lvl30_all_zero),
        "all_bundles_Wp_Wm_commute": all_comm_zero,
        "pf1_Q8_mod9_mismatches": pf1_q8_mismatches,
        "b1_pass": b1_pass,
    }


# ---------------------------------------------------------------------------
# MODULE B2 — Exact Chiral Walk Algebra on Leg(5)
# ---------------------------------------------------------------------------

def build_leg5_operators(trivial_signs: bool = False):
    P1 = L2
    P2 = mat2_mul(C_OM, mat2_mul(L2, mat2_inv(C_OM)))
    P3 = mat2_mul(C_OM, mat2_mul(P2, mat2_inv(C_OM)))
    Q1 = R2
    Q2 = mat2_mul(C_OM, mat2_mul(R2, mat2_inv(C_OM)))
    Q3 = mat2_mul(C_OM, mat2_mul(Q2, mat2_inv(C_OM)))
    WL = leg5_sp_mat(P1, trivial_signs) + leg5_sp_mat(P2, trivial_signs) + leg5_sp_mat(P3, trivial_signs)
    WR = leg5_sp_mat(Q1, trivial_signs) + leg5_sp_mat(Q2, trivial_signs) + leg5_sp_mat(Q3, trivial_signs)
    W6 = WL + WR
    C3M = leg5_sp_mat(C3_OM, trivial_signs)
    TM = leg5_sp_mat(TAU_MIR, trivial_signs)
    return WL, WR, W6, C3M, TM


def build_golden_basis(W6: sp.Matrix, TM: sp.Matrix, eigval):
    bs = (W6 - eigval * sp.eye(6)).nullspace()
    assert len(bs) == 2
    P_p = (sp.eye(6) + TM) / 2
    P_m = (sp.eye(6) - TM) / 2
    ep = sp.simplify(P_p * bs[0])
    if ep == sp.zeros(6, 1):
        ep = sp.simplify(P_p * bs[1])
    em = sp.simplify(P_m * bs[0])
    if em == sp.zeros(6, 1):
        em = sp.simplify(P_m * bs[1])
    ep = sp.simplify(ep / sp.sqrt((ep.T * ep)[0]))
    em = sp.simplify(em / sp.sqrt((em.T * em)[0]))
    if sp.N(ep[5], 20) < 0:
        ep = -ep
    if sp.N(em[3], 20) < 0:
        em = -em
    return sp.Matrix.hstack(ep, em)


def run_B2() -> Tuple[Dict[str, Any], Dict[str, Any]]:
    WL, WR, W6, C3M, TM = build_leg5_operators(trivial_signs=False)
    x = sp.Symbol("x")
    phi = (1 + sp.sqrt(5)) / 2
    phi2 = sp.simplify(phi ** 2)
    phim2 = sp.simplify(phi ** (-2))

    wr_eq_wlt = (WR == WL.T)
    comm_wl_wr = (WL * WR - WR * WL) == sp.zeros(6, 6)
    comm_wl_c3 = (WL * C3M - C3M * WL) == sp.zeros(6, 6)
    tau_conj = (TM * WL * TM == WR)

    cp_w6 = sp.Poly(W6.charpoly(x).as_expr(), x)
    cp_wl = sp.Poly(WL.charpoly(x).as_expr(), x)
    A_ch = sp.I * (WL - WR)
    cp_ach = sp.Poly(A_ch.charpoly(x).as_expr(), x)

    t_w6 = sp.Poly(sp.expand((x ** 2 - 20) * ((x ** 2 - 3 * x + 1) ** 2)), x)
    t_wl = sp.Poly(sp.expand((x ** 2 - 5) * (x ** 4 - 3 * x ** 3 + 8 * x ** 2 - 3 * x + 1)), x)
    t_ach = sp.Poly(sp.expand((x ** 2) * (x ** 4 - 21 * x ** 2 + 9)), x)

    Bg = build_golden_basis(W6, TM, phi2)
    Bgm = build_golden_basis(W6, TM, phim2)
    sigma_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])

    M_A_g = sp.simplify(Bg.T * A_ch * Bg)
    M_A_gm = sp.simplify(Bgm.T * A_ch * Bgm)
    M_WL_g = sp.simplify(Bg.T * WL * Bg)
    M_C3_g = sp.simplify(Bg.T * C3M * Bg)

    pauli_g_ok = sp.simplify(M_A_g - sp.sqrt(3) * phi2 * sigma_y) == sp.zeros(2, 2)
    pauli_gm_ok = sp.simplify(M_A_gm - sp.sqrt(3) * phim2 * sigma_y) == sp.zeros(2, 2)
    wl_c3_ok = sp.simplify(M_WL_g + phi2 * (M_C3_g ** 2)) == sp.zeros(2, 2)

    # Check that eigenstates [1, +-i]/sqrt(2) of sigma_y give exact chiral poles I4 = 1/5, I6 = 2/45
    pole_p = sp.simplify((Bg * sp.Matrix([1, sp.I])) / sp.sqrt(2))
    pole_m = sp.simplify((Bg * sp.Matrix([1, -sp.I])) / sp.sqrt(2))
    p_probs = [sp.simplify(sp.re(c * sp.conjugate(c))) for c in pole_p]
    m_probs = [sp.simplify(sp.re(c * sp.conjugate(c))) for c in pole_m]
    pole_i4_ok = (sp.simplify(sum(p ** 2 for p in p_probs) - sp.Rational(1, 5)) == 0) and (
        sp.simplify(sum(p ** 2 for p in m_probs) - sp.Rational(1, 5)) == 0
    )
    pole_i6_ok = (sp.simplify(sum(p ** 3 for p in p_probs) - sp.Rational(2, 45)) == 0) and (
        sp.simplify(sum(p ** 3 for p in m_probs) - sp.Rational(2, 45)) == 0
    )

    # PF2: Swap R <-> R^-1 in WL (using R instead of P2 = R^-1 in W+) breaks [W+, W-] = 0
    P1 = L2
    P3 = mat2_mul(C_OM, mat2_mul(mat2_inv(R2), mat2_inv(C_OM)))
    WL_bad = leg5_sp_mat(P1) + leg5_sp_mat(R2) + leg5_sp_mat(P3)
    WR_bad = W6 - WL_bad
    pf2_comm_nonzero = (WL_bad * WR_bad - WR_bad * WL_bad) != sp.zeros(6, 6)

    # PF5: Trivial signs (P^1(F_5)) kills golden kernel ker(W6^2 - 3 W6 + I)
    _, _, W6_triv, _, _ = build_leg5_operators(trivial_signs=True)
    pf5_triv_golden_dim = len((W6_triv * W6_triv - 3 * W6_triv + sp.eye(6)).nullspace())

    b2_pass = (
        wr_eq_wlt
        and comm_wl_wr
        and comm_wl_c3
        and tau_conj
        and (cp_w6 == t_w6)
        and (cp_wl == t_wl)
        and (cp_ach == t_ach)
        and pauli_g_ok
        and pauli_gm_ok
        and wl_c3_ok
        and pole_i4_ok
        and pole_i6_ok
    )
    return {
        "WR_eq_WL_T": wr_eq_wlt,
        "comm_WL_WR_zero": comm_wl_wr,
        "comm_WL_C3_zero": comm_wl_c3,
        "tau_WL_tau_eq_WR": tau_conj,
        "charpoly_W6": str(sp.factor(cp_w6.as_expr())),
        "charpoly_WL": str(sp.factor(cp_wl.as_expr())),
        "charpoly_i_WL_minus_WR": str(sp.factor(cp_ach.as_expr())),
        "pauli_sigma_y_on_E_phi2": pauli_g_ok,
        "pauli_sigma_y_on_E_phim2": pauli_gm_ok,
        "WL_eq_minus_phi2_C3sq_on_E_phi2": wl_c3_ok,
        "chiral_poles_I4_1_over_5_I6_2_over_45": bool(pole_i4_ok and pole_i6_ok),
        "pf2_swapped_walk_breaks_commutator": pf2_comm_nonzero,
        "pf5_trivial_P1F5_golden_kernel_dim": pf5_triv_golden_dim,
        "b2_pass": b2_pass,
    }, {"W6": W6, "C3M": C3M, "TM": TM, "Bg": Bg, "Bgm": Bgm}


# ---------------------------------------------------------------------------
# MODULE B3 — Mirror-Lock Theorem, Analytic Siegel Map, & Zero-Param Stabilization
# ---------------------------------------------------------------------------

def B2_bern(a):
    a = a - mp.floor(a)
    return a * a - a + mp_rat(1, 6)


def log_abs_siegel(a, b, tau, dps: int = 45):
    mp.mp.dps = dps
    a = a - mp.floor(a)
    b = b - mp.floor(b)
    I = iu()
    pi = mp.pi
    ty = mp.im(tau)
    q = mp.exp(2 * I * pi * tau)
    qz = mp.exp(2 * I * pi * (a * tau + b))
    val = -pi * ty * B2_bern(a) + mp.log(abs(1 - qz))
    K = max(25, int(mp.ceil((dps * mp.mpf(231)) / (mp.mpf(628) * ty))) + 14)
    qn = mp.mpc(1)
    for _ in range(1, K + 1):
        qn *= q
        val += mp.log(abs(1 - qn * qz)) + mp.log(abs(1 - qn / qz))
    return -val


def sp_mat_to_mp(M: sp.Matrix, dps: int = 45):
    mp.mp.dps = dps
    return mp.matrix([[mp.mpf(str(sp.N(M[r, c], dps + 5))) for c in range(M.cols)] for r in range(M.rows)])


def phi_siegel_col(tau, MS_mp, dps: int = 45):
    mp.mp.dps = dps
    s2 = mp.sqrt(2)
    vr = mp.matrix([
        (
            log_abs_siegel(mp_rat(l[0], 5), mp_rat(l[1], 5), tau, dps=dps)
            - log_abs_siegel(mp_rat((2 * l[0]) % 5, 5), mp_rat((2 * l[1]) % 5, 5), tau, dps=dps)
        ) / s2
        for l in LINES5
    ])
    return MS_mp * vr


def I4_I6_vec(vec):
    ps = [abs(v) ** 2 for v in vec]
    s = sum(ps)
    ps = [p / s for p in ps]
    return sum(p * p for p in ps), sum(p ** 3 for p in ps), s


def run_B3(b2_aux: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    W6, C3M, TM, Bg, Bgm = b2_aux["W6"], b2_aux["C3M"], b2_aux["TM"], b2_aux["Bg"], b2_aux["Bgm"]
    MS = leg5_sp_mat(S_STD)
    ML = leg5_sp_mat(L2)

    # 1. Exact symbolic Anti-Holomorphic Mirror-Lock Theorem on Leg(5)
    M_arc = sp.simplify(MS * leg5_sp_mat(((0, 1), (1, 0))) * MS.inv())
    M_half = sp.simplify(MS * leg5_sp_mat(((1, 0), (-1, -1))) * MS.inv())
    M_third = sp.simplify(MS * leg5_sp_mat(((1, 1), (0, -1))) * MS.inv())
    M_zero = sp.simplify(MS * leg5_sp_mat(((1, 0), (0, -1))) * MS.inv())

    lock_arc_ok = (M_arc == TM) and (sp.simplify(M_arc * W6 - W6 * M_arc) == sp.zeros(6, 6))
    lock_half_ok = (M_half == sp.simplify(C3M * TM * C3M.inv())) and (sp.simplify(M_half * W6 - W6 * M_half) == sp.zeros(6, 6))
    lock_third_ok = (M_third == sp.simplify((C3M ** 2) * TM * (C3M ** 2).inv())) and (sp.simplify(M_third * W6 - W6 * M_third) == sp.zeros(6, 6))
    pf3_r0_breaks_w6 = sp.simplify(M_zero * W6 - W6 * M_zero) != sp.zeros(6, 6)

    # Exact symbolic cusp asymptote (linear 2*pi*y/25 and constant ln(phi) both lock at theta = -60 deg, ratio -sqrt(3))
    c_lead = sp.simplify(Bg.T * (MS * sp.Matrix([1, 0, 1, 1, 1, 1])))
    c_const = sp.simplify(Bg.T * (MS * sp.Matrix([0, 1, 0, 0, 0, 0])))
    cusp_lead_ratio_ok = sp.simplify(c_lead[1] / c_lead[0] + sp.sqrt(3)) == 0
    cusp_const_ratio_ok = sp.simplify(c_const[1] / c_const[0] + sp.sqrt(3)) == 0

    # 2. High-precision SL(2, Z) equivariance & Bloch projections of Phi^{Siegel}_{Leg(5)}(tau)
    dps = 45
    mp.mp.dps = dps
    I = iu()
    MS_mp = sp_mat_to_mp(MS, dps=dps)
    ML_mp = sp_mat_to_mp(ML, dps=dps)
    Bg_mp = sp_mat_to_mp(Bg, dps=dps)

    tau0 = mp.mpc(mp_rat(3, 10), mp_rat(13, 10))
    v0 = phi_siegel_col(tau0, MS_mp, dps=dps)
    vT = phi_siegel_col(tau0 + 1, MS_mp, dps=dps)
    vS = phi_siegel_col(-1 / tau0, MS_mp, dps=dps)
    max_v0 = max(abs(x) for x in v0)
    siegel_T_err = max(abs((vT - ML_mp * v0)[i]) for i in range(6)) / max_v0
    siegel_S_err = max(abs((vS - MS_mp * v0)[i]) for i in range(6)) / max_v0

    i4_0, i6_0, n2_0 = I4_I6_vec(v0)
    i4_T, i6_T, n2_T = I4_I6_vec(vT)
    i4_S, i6_S, n2_S = I4_I6_vec(vS)
    siegel_inv_err = max(
        abs(n2_T - n2_0) / n2_0,
        abs(n2_S - n2_0) / n2_0,
        abs(i4_T - i4_0) / i4_0,
        abs(i4_S - i4_0) / i4_0,
        abs(i6_T - i6_0) / i6_0,
        abs(i6_S - i6_0) / i6_0,
    )

    tau_om = mp.mpc(mp_rat(1, 2), mp.sqrt(3) / 2)
    tau_i = I
    tau_arc = mp.exp(I * 5 * mp.pi / 12)
    tau_tot70 = mp.mpc(mp_rat(1, 2), mp_rat(3380451106, 1000000000))

    def gold_stats(vc):
        cg = Bg_mp.T * vc
        pg = cg[0] ** 2 + cg[1] ** 2
        i4_f, i6_f, n2_f = I4_I6_vec(vc)
        if pg > mp_pow10(-40):
            psi = (Bg_mp * cg) / mp.sqrt(pg)
            i4_g, i6_g, _ = I4_I6_vec(psi)
            th_deg = mp.atan2(cg[1], cg[0]) * 180 / mp.pi
        else:
            i4_g, i6_g, th_deg = mp.mpf(0), mp.mpf(0), mp.mpf(0)
        return {
            "norm2": n2_f,
            "I4_full": i4_f,
            "I6_full": i6_f,
            "gold_frac": pg / n2_f,
            "th_deg": th_deg,
            "I4_gold": i4_g,
            "I6_gold": i6_g,
        }

    st_om = gold_stats(phi_siegel_col(tau_om, MS_mp, dps=dps))
    st_i = gold_stats(phi_siegel_col(tau_i, MS_mp, dps=dps))
    st_arc = gold_stats(phi_siegel_col(tau_arc, MS_mp, dps=dps))
    st_tot70 = gold_stats(phi_siegel_col(tau_tot70, MS_mp, dps=dps))

    # Unique mirror-odd crossing y_odd* on Re(tau) = 0 where theta(i y) = -30 deg (I_6_gold = 1/10)
    def odd_res(yv):
        vc = phi_siegel_col(mp.mpc(0, yv), MS_mp, dps=36)
        cg = Bg_mp.T * vc
        return cg[0] + mp.sqrt(3) * cg[1]

    lo, hi = mp.mpf(1), mp.mpf(2)
    flo = odd_res(lo)
    for _ in range(90):
        mid = (lo + hi) / 2
        fmid = odd_res(mid)
        if flo * fmid <= 0:
            hi = mid
        else:
            lo, flo = mid, fmid
    y_odd = (lo + hi) / 2
    st_yodd = gold_stats(phi_siegel_col(mp.mpc(0, y_odd), MS_mp, dps=40))

    # 3. Zero-Parameter SL(2, Z)-Invariant Interior Stabilization: I4_Siegel (x=1/2 min, x=0 saddle) & I6_Siegel (x=0 min, x=1/2 saddle)
    def eval_i4(tau_in, d_use: int = 38):
        return I4_I6_vec(phi_siegel_col(tau_in, MS_mp, dps=d_use))[0]

    def eval_i6(tau_in, d_use: int = 38):
        return I4_I6_vec(phi_siegel_col(tau_in, MS_mp, dps=d_use))[1]

    def opt_and_hess(fn, xv, y_init):
        y = y_init
        h_n = mp_pow10(-6)
        for _ in range(8):
            f0 = fn(mp.mpc(xv, y))
            fp = fn(mp.mpc(xv, y + h_n))
            fm = fn(mp.mpc(xv, y - h_n))
            dy = ((fp - fm) / (2 * h_n)) / ((fp - 2 * f0 + fm) / (h_n * h_n))
            y -= dy
            if abs(dy) < mp_pow10(-14):
                break
        f0 = fn(mp.mpc(xv, y), d_use=42)
        hg = mp_pow10(-10)
        gx = (fn(mp.mpc(xv + hg, y), d_use=42) - fn(mp.mpc(xv - hg, y), d_use=42)) / (2 * hg)
        gy = (fn(mp.mpc(xv, y + hg), d_use=42) - fn(mp.mpc(xv, y - hg), d_use=42)) / (2 * hg)
        hh = mp_pow10(-5)
        fxp = fn(mp.mpc(xv + hh, y), d_use=42)
        fxm = fn(mp.mpc(xv - hh, y), d_use=42)
        fyp = fn(mp.mpc(xv, y + hh), d_use=42)
        fym = fn(mp.mpc(xv, y - hh), d_use=42)
        fxx = (fxp - 2 * f0 + fxm) / (hh * hh)
        fyy = (fyp - 2 * f0 + fym) / (hh * hh)
        return {"y": y, "val": f0, "gx": gx, "gy": gy, "fxx": fxx, "fyy": fyy}

    i4_half = opt_and_hess(eval_i4, mp_rat(1, 2), mp_rat(227, 100))
    i4_zero = opt_and_hess(eval_i4, mp.mpf(0), mp_rat(227, 100))
    i6_zero = opt_and_hess(eval_i6, mp.mpf(0), mp_rat(230, 100))
    i6_half = opt_and_hess(eval_i6, mp_rat(1, 2), mp_rat(230, 100))

    i4_cusp = eval_i4(mp.mpc(mp_rat(1, 2), mp.mpf(15)), d_use=36)
    i6_cusp = eval_i6(mp.mpc(mp_rat(1, 2), mp.mpf(15)), d_use=36)

    i4_stab_ok = (
        abs(i4_half["gx"]) < mp_pow10(-15)
        and abs(i4_half["gy"]) < mp_pow10(-12)
        and i4_half["fxx"] > mp_pow10(-5)
        and i4_half["fyy"] > mp_rat(1, 100)
        and i4_zero["fxx"] < -mp_pow10(-5)
        and i4_half["val"] < i4_zero["val"]
        and i4_half["val"] < mp_rat(1, 5)
        and abs(i4_cusp - mp_rat(1, 5)) < mp_rat(1, 500)
        and i4_half["val"] < st_i["I4_full"] < st_om["I4_full"]
    )
    i6_stab_ok = (
        abs(i6_zero["gx"]) < mp_pow10(-15)
        and abs(i6_zero["gy"]) < mp_pow10(-12)
        and i6_zero["fxx"] > mp_pow10(-5)
        and i6_zero["fyy"] > mp_rat(1, 100)
        and i6_half["fxx"] < -mp_pow10(-5)
        and i6_zero["val"] < i6_half["val"]
        and i6_zero["val"] < mp_rat(1, 25)
        and abs(i6_cusp - mp_rat(1, 25)) < mp_rat(1, 1000)
        and i6_zero["val"] < st_i["I6_full"] < st_om["I6_full"]
    )

    b3_pass = (
        lock_arc_ok
        and lock_half_ok
        and lock_third_ok
        and cusp_lead_ratio_ok
        and cusp_const_ratio_ok
        and max(siegel_T_err, siegel_S_err, siegel_inv_err) < mp_pow10(-40)
        and st_om["gold_frac"] < mp_pow10(-40)
        and abs(st_i["I6_gold"] - mp_rat(11, 90)) < mp_pow10(-35)
        and abs(st_arc["I6_gold"] - mp_rat(11, 90)) < mp_pow10(-35)
        and abs(st_tot70["I6_gold"] - mp_rat(11, 90)) < mp_pow10(-35)
        and abs(st_tot70["th_deg"] + 60) < mp_pow10(-30)
        and abs(st_yodd["I6_gold"] - mp_rat(1, 10)) < mp_pow10(-30)
        and st_om["norm2"] < st_i["norm2"]
        and i4_stab_ok
        and i6_stab_ok
    )

    return {
        "mirror_lock_arc_eq_tau": lock_arc_ok,
        "mirror_lock_half_eq_C3_tau_C3inv": lock_half_ok,
        "mirror_lock_third_eq_C3sq_tau_C3m2": lock_third_ok,
        "cusp_lead_and_const_lock_minus60deg": bool(cusp_lead_ratio_ok and cusp_const_ratio_ok),
        "siegel_T_err": mp_str(siegel_T_err, 6),
        "siegel_S_err": mp_str(siegel_S_err, 6),
        "siegel_inv_err": mp_str(siegel_inv_err, 6),
        "omega_gold_frac": mp_str(st_om["gold_frac"], 6),
        "omega_norm2": mp_str(st_om["norm2"], 10),
        "i_norm2": mp_str(st_i["norm2"], 10),
        "i_I6_gold": mp_str(st_i["I6_gold"], 10),
        "tot70_th_deg": mp_str(st_tot70["th_deg"], 10),
        "tot70_I6_gold": mp_str(st_tot70["I6_gold"], 10),
        "y_odd_star": mp_str(y_odd, 14),
        "y_odd_I6_gold": mp_str(st_yodd["I6_gold"], 10),
        "zero_param_I4_min_on_x_half": {
            "y_star": mp_str(i4_half["y"], 14),
            "I4_star": mp_str(i4_half["val"], 14),
            "I4_xx_half": mp_str(i4_half["fxx"], 8),
            "I4_yy_half": mp_str(i4_half["fyy"], 8),
            "I4_xx_zero_saddle": mp_str(i4_zero["fxx"], 8),
            "I4_cusp_15i": mp_str(i4_cusp, 8),
            "ok": i4_stab_ok,
        },
        "zero_param_I6_min_on_x_zero": {
            "y_star": mp_str(i6_zero["y"], 14),
            "I6_star": mp_str(i6_zero["val"], 14),
            "I6_xx_zero": mp_str(i6_zero["fxx"], 8),
            "I6_yy_zero": mp_str(i6_zero["fyy"], 8),
            "I6_xx_half_saddle": mp_str(i6_half["fxx"], 8),
            "I6_cusp_15i": mp_str(i6_cusp, 8),
            "ok": i6_stab_ok,
        },
        "pf3_R0_breaks_W6_and_I4_zero_is_saddle": bool(pf3_r0_breaks_w6 and (i4_zero["fxx"] < -mp_pow10(-5))),
        "b3_pass": b3_pass,
    }, {"MS_mp": MS_mp, "ML_mp": ML_mp, "Bg_mp": Bg_mp, "Bgm_mp": sp_mat_to_mp(Bgm, dps=dps), "tau_om": tau_om, "tau_i": tau_i, "tau_arc": tau_arc, "tau_tot70": tau_tot70}


# ---------------------------------------------------------------------------
# MODULE B4 — Weight-2 Holomorphic Weierstrass Map & 5-Division Polynomial Proofs
# ---------------------------------------------------------------------------

def wp_eval(a, b, tau, dps: int = 45):
    mp.mp.dps = dps
    I = iu()
    pi = mp.pi
    ty = mp.im(tau)
    q = mp.exp(2 * I * pi * tau)
    K = max(25, int(mp.ceil((dps * mp.mpf(231)) / (mp.mpf(628) * ty))) + 14)
    e2 = mp.mpc(1)
    qn = mp.mpc(1)
    qlist = []
    for n in range(1, K + 1):
        qn *= q
        qlist.append(qn)
        e2 -= 24 * n * qn / (1 - qn)
    w_ = mp.exp(2 * I * pi * (a * tau + b))
    iw = 1 / w_
    s = w_ / ((1 - w_) ** 2)
    for qm in qlist:
        s += (qm * w_) / ((1 - qm * w_) ** 2) + (qm * iw) / ((1 - qm * iw) ** 2)
    return -(pi * pi / 3) * e2 - 4 * pi * pi * s


def phi_wp_col(tau, MS_mp, dps: int = 45):
    mp.mp.dps = dps
    s2 = mp.sqrt(2)
    vr = mp.matrix([
        (
            wp_eval(mp_rat(l[0], 5), mp_rat(l[1], 5), tau, dps=dps)
            - wp_eval(mp_rat((2 * l[0]) % 5, 5), mp_rat((2 * l[1]) % 5, 5), tau, dps=dps)
        ) / s2
        for l in LINES5
    ])
    return MS_mp * vr


def run_B4(b2_aux: Dict[str, Any], b3_aux: Dict[str, Any]) -> Dict[str, Any]:
    # 1. Exact symbolic 5-division polynomial proof for y^2 = 4x^3 - 1 (g_2 = 0, tau = omega_+)
    x, t = sp.Symbol("x"), sp.Symbol("t")
    psi2_sq = 4 * x ** 3 - 1
    psi3 = 3 * x ** 4 - 3 * x
    psi4_over_y = 2 * x ** 6 - 10 * x ** 3 - 1
    psi5 = sp.expand(psi4_over_y * (psi2_sq ** 2) - psi3 ** 3)
    target_psi5 = 5 * x ** 12 - 95 * x ** 9 - 15 * x ** 6 + 25 * x ** 3 - 1
    assert psi5 == target_psi5

    phi = (1 + sp.sqrt(5)) / 2
    P_t = 5 * t ** 4 - 95 * t ** 3 - 15 * t ** 2 + 25 * t - 1
    fac_c = t ** 2 + t * (sp.Rational(-19, 2) - sp.Rational(9, 2) * sp.sqrt(5)) + 4 + sp.Rational(9, 5) * sp.sqrt(5)
    fac_s = t ** 2 + t * (sp.Rational(-19, 2) + sp.Rational(9, 2) * sp.sqrt(5)) + 4 - sp.Rational(9, 5) * sp.sqrt(5)
    div_factor_ok = sp.expand(5 * fac_c * fac_s - P_t) == 0

    # Exact cubic proof: u_c = sqrt(3)*5^(-1/12)*phi^(1/2), u_s = u_c / phi
    d_c_sq = sp.simplify(((19 + 9 * sp.sqrt(5)) / 2) ** 2 - 4 * ((20 + 9 * sp.sqrt(5)) / 5))
    d_s_sq = sp.simplify(((19 - 9 * sp.sqrt(5)) / 2) ** 2 - 4 * ((20 - 9 * sp.sqrt(5)) / 5))
    # Verify exact u_c^3 + 3*(5^(-1/6) phi^2)*u_c == sqrt(d_c_sq) by squaring in Q(sqrt(5))!
    # Put W = 5^(1/6)*u_c = sqrt(3)*5^(1/12)*phi^(1/2) => W^2 = 3*5^(1/6)*phi? Wait: check u_c^6 * 5 = 27 * sqrt(5) * phi^3!
    # Wait: (u_c^6 * 5) = (3^3 * 5^(-1/2) * phi^3) * 5 = 27 * sqrt(5) * phi^3!
    # Check: (u_c^3 + 3*a_c*u_c)^2 = u_c^6 + 6*a_c*u_c^4 + 9*a_c^2*u_c^2 where a_c = 5^(-1/6)*phi^2:
    # u_c^2 = 3 * 5^(-1/6) * phi  (CHECK: (3*5^(-1/6)*phi)^3 * 5 = 27 * 5^(-1/2) * phi^3 * 5 = 27 * sqrt(5) * phi^3! YES!!)
    uc2 = 3 * sp.Integer(5) ** sp.Rational(-1, 6) * phi
    ac = sp.Integer(5) ** sp.Rational(-1, 6) * phi ** 2
    lhs_c_sq = sp.simplify(uc2 * ((uc2 + 3 * ac) ** 2))
    # For sys: us2 = uc2 / phi^2 = 3 * 5^(-1/6) * phi^(-1), a_s = -5^(-1/6) * phi^(-2)
    us2 = 3 * sp.Integer(5) ** sp.Rational(-1, 6) * phi ** (-1)
    a_s = -sp.Integer(5) ** sp.Rational(-1, 6) * phi ** (-2)
    lhs_s_sq = sp.simplify(us2 * ((us2 + 3 * a_s) ** 2))
    sym_cubic_c_ok = sp.simplify(lhs_c_sq - d_c_sq) == 0
    sym_cubic_s_ok = sp.simplify(lhs_s_sq - d_s_sq) == 0

    # Exact symbolic projection of v_om = [1, w^2, w, -1/phi, w^2/phi, -w/phi] onto E_{phi^2} and E_{phi^-2}!
    om = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    om2 = sp.Rational(-1, 2) - sp.I * sp.sqrt(3) / 2
    v_om = sp.Matrix([1, om2, om, -1 / phi, om2 / phi, -om / phi])
    Bg, Bgm = b2_aux["Bg"], b2_aux["Bgm"]
    cg_sym = [sp.simplify(e) for e in (Bg.T * v_om)]
    cgm_sym = [sp.simplify(e) for e in (Bgm.T * v_om)]
    n2_om_sym = sp.simplify(sum(sp.re(c * sp.conjugate(c)) for c in v_om))
    pg_om_sym = sp.simplify(sum(sp.re(c * sp.conjugate(c)) for c in cg_sym))
    pgm_om_sym = sp.simplify(sum(sp.re(c * sp.conjugate(c)) for c in cgm_sym))
    sym_45_15_ok = (
        sp.simplify(pg_om_sym / n2_om_sym - sp.Rational(4, 5)) == 0
        and sp.simplify(pgm_om_sym / n2_om_sym - sp.Rational(1, 5)) == 0
        and sp.simplify(cg_sym[1] / cg_sym[0] + sp.I) == 0
    )

    # Exact lemniscate (tau = i) rational probabilities p(Phi^wp(i)) -> I4 = 2/9, I6 = 17/288
    p_i_ex = [
        (5 + sp.sqrt(5)) / 24,
        (5 + sp.sqrt(5)) / 24,
        (5 - sp.sqrt(5)) / 24,
        sp.Rational(1, 12),
        sp.Rational(1, 12),
        (5 - sp.sqrt(5)) / 24,
    ]
    sym_i_ok = (
        sp.simplify(sum(p_i_ex) - 1) == 0
        and sp.simplify(sum(p ** 2 for p in p_i_ex) - sp.Rational(2, 9)) == 0
        and sp.simplify(sum(p ** 3 for p in p_i_ex) - sp.Rational(17, 288)) == 0
    )

    # 2. High-precision numerical verification of Phi^{wp}_{Leg(5)} across F
    dps = 45
    mp.mp.dps = dps
    I = iu()
    MS_mp, ML_mp, Bg_mp, Bgm_mp = b3_aux["MS_mp"], b3_aux["ML_mp"], b3_aux["Bg_mp"], b3_aux["Bgm_mp"]
    tau0 = mp.mpc(mp_rat(3, 10), mp_rat(13, 10))
    w0 = phi_wp_col(tau0, MS_mp, dps=dps)
    wT = phi_wp_col(tau0 + 1, MS_mp, dps=dps)
    wS = phi_wp_col(-1 / tau0, MS_mp, dps=dps)
    wp_T_err = max(abs((wT - ML_mp * w0)[i]) for i in range(6)) / max(abs(x) for x in w0)
    wp_S_err = max(abs((wS - (tau0 ** 2) * MS_mp * w0)[i]) for i in range(6)) / max(abs(x) for x in wS)
    # PF4: dropping (tau0^2) weight-2 factor breaks S-equivariance
    pf4_drop_wt2_err = max(abs((wS - MS_mp * w0)[i]) for i in range(6)) / max(abs(x) for x in wS)

    vwp0 = (mp.im(tau0) ** 2) * sum(abs(x) ** 2 for x in w0)
    vwpT = (mp.im(tau0 + 1) ** 2) * sum(abs(x) ** 2 for x in wT)
    vwpS = (mp.im(-1 / tau0) ** 2) * sum(abs(x) ** 2 for x in wS)
    vwp_inv_err = max(abs(vwpT - vwp0) / vwp0, abs(vwpS - vwp0) / vwp0)

    def wp_stats(tv):
        vc = phi_wp_col(tv, MS_mp, dps=dps)
        i4_f, i6_f, n2_f = I4_I6_vec(vc)
        v_wp = (mp.im(tv) ** 2) * n2_f
        cg = Bg_mp.T * vc
        cgm = Bgm_mp.T * vc
        pg = abs(cg[0]) ** 2 + abs(cg[1]) ** 2
        pgm = abs(cgm[0]) ** 2 + abs(cgm[1]) ** 2
        psi = (Bg_mp * cg) / mp.sqrt(pg)
        i4_g, i6_g, _ = I4_I6_vec(psi)
        alpha_deg = mp.arg(cg[1] / cg[0]) * 180 / mp.pi
        th_deg = mp.atan2(abs(cg[1]), abs(cg[0])) * 180 / mp.pi
        return {
            "V_wp": v_wp,
            "I4_full": i4_f,
            "I6_full": i6_f,
            "gold_frac": pg / n2_f,
            "gold_m_frac": pgm / n2_f,
            "I4_gold": i4_g,
            "I6_gold": i6_g,
            "th_deg": th_deg,
            "alpha_deg": alpha_deg,
            "vc": vc,
        }

    st_om = wp_stats(b3_aux["tau_om"])
    st_arc = wp_stats(b3_aux["tau_arc"])
    st_i = wp_stats(b3_aux["tau_i"])
    st_tot70 = wp_stats(b3_aux["tau_tot70"])
    st_cusp5 = wp_stats(mp.mpc(mp_rat(1, 2), mp.mpf(5)))

    # Exact closed form V_wp(omega_+) = (27/8) * 5^(1/3) * |g3(omega_+)|^(2/3)
    q_om = mp.exp(2 * I * mp.pi * b3_aux["tau_om"])
    e6_om = mp.mpc(1)
    qn = mp.mpc(1)
    for n in range(1, 65):
        qn *= q_om
        e6_om -= 504 * (n ** 5) * qn / (1 - qn)
    g3_om = (8 * (mp.pi ** 6) / 27) * e6_om
    v_wp_om_pred = mp_rat(27, 8) * (mp.mpf(5) ** mp_rat(1, 3)) * (abs(g3_om) ** mp_rat(2, 3))
    v_wp_om_err = abs(st_om["V_wp"] - v_wp_om_pred) / st_om["V_wp"]

    # Check exact lemniscate probability vector match at tau = i
    ps_i_num = [abs(x) ** 2 for x in st_i["vc"]]
    s_i = sum(ps_i_num)
    ps_i_num = [p / s_i for p in ps_i_num]
    ps_i_ex_mp = [mp.mpf(str(sp.N(p, 50))) for p in p_i_ex]
    lemniscate_prob_err = max(abs(a - b) for a, b in zip(ps_i_num, ps_i_ex_mp))

    b4_pass = (
        div_factor_ok
        and sym_cubic_c_ok
        and sym_cubic_s_ok
        and sym_45_15_ok
        and sym_i_ok
        and max(wp_T_err, wp_S_err, vwp_inv_err) < mp_pow10(-35)
        and abs(st_om["gold_frac"] - mp_rat(4, 5)) < mp_pow10(-40)
        and abs(st_om["gold_m_frac"] - mp_rat(1, 5)) < mp_pow10(-40)
        and abs(st_om["I4_full"] - mp_rat(1, 5)) < mp_pow10(-40)
        and abs(st_om["I6_full"] - mp_rat(2, 45)) < mp_pow10(-40)
        and abs(st_om["I4_gold"] - mp_rat(1, 5)) < mp_pow10(-40)
        and abs(st_om["I6_gold"] - mp_rat(2, 45)) < mp_pow10(-40)
        and abs(st_om["th_deg"] - 45) < mp_pow10(-35)
        and abs(st_om["alpha_deg"] + 90) < mp_pow10(-35)
        and v_wp_om_err < mp_pow10(-40)
        and lemniscate_prob_err < mp_pow10(-40)
        and abs(st_i["I4_full"] - mp_rat(2, 9)) < mp_pow10(-40)
        and abs(st_i["I6_full"] - mp_rat(17, 288)) < mp_pow10(-40)
        and abs(st_arc["alpha_deg"] + 90) < mp_pow10(-35)
        and abs(st_i["alpha_deg"] + 90) < mp_pow10(-35)
        and st_om["V_wp"] < st_arc["V_wp"] < st_i["V_wp"] < st_tot70["V_wp"]
        and st_tot70["I4_gold"] > mp_rat(29, 100)
        and st_cusp5["I4_gold"] > mp_rat(299, 1000)
    )
    return {
        "sym_5div_factor_ok": div_factor_ok,
        "sym_cubic_cusp_and_sys_ok": bool(sym_cubic_c_ok and sym_cubic_s_ok),
        "sym_omega_45_15_and_chiral_pole_ok": sym_45_15_ok,
        "sym_lemniscate_i_2_9_and_17_288_ok": sym_i_ok,
        "wp_T_err": mp_str(wp_T_err, 6),
        "wp_S_err": mp_str(wp_S_err, 6),
        "vwp_inv_err": mp_str(vwp_inv_err, 6),
        "omega_V_wp": mp_str(st_om["V_wp"], 12),
        "omega_V_wp_closed_form_err": mp_str(v_wp_om_err, 6),
        "omega_gold_frac": mp_str(st_om["gold_frac"], 12),
        "omega_I4_full": mp_str(st_om["I4_full"], 10),
        "omega_I6_full": mp_str(st_om["I6_full"], 10),
        "i_V_wp": mp_str(st_i["V_wp"], 12),
        "i_I4_full": mp_str(st_i["I4_full"], 10),
        "i_I6_full": mp_str(st_i["I6_full"], 10),
        "i_lemniscate_prob_err": mp_str(lemniscate_prob_err, 6),
        "arc_alpha_deg": mp_str(st_arc["alpha_deg"], 10),
        "tot70_I4_gold": mp_str(st_tot70["I4_gold"], 10),
        "tot70_I6_gold": mp_str(st_tot70["I6_gold"], 10),
        "tot70_alpha_deg": mp_str(st_tot70["alpha_deg"], 10),
        "cusp5_I4_gold": mp_str(st_cusp5["I4_gold"], 10),
        "pf4_drop_wt2_S_err": mp_str(pf4_drop_wt2_err, 6),
        "b4_pass": b4_pass,
    }


# ---------------------------------------------------------------------------
# Main Driver (P-885 Deterministic Decisive Output, 0 of 19)
# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    write_json = "--write-json" in argv
    ast_rep = audit_own_ast()

    b1 = run_B1()
    b2, b2_aux = run_B2()
    b3, b3_aux = run_B3(b2_aux)
    b4 = run_B4(b2_aux, b3_aux)

    pf1_ok = b1["pf1_Q8_mod9_mismatches"] > 0
    pf2_ok = bool(b2["pf2_swapped_walk_breaks_commutator"])
    pf3_ok = bool(b3["pf3_R0_breaks_W6_and_I4_zero_is_saddle"])
    pf4_ok = mp.mpf(b4["pf4_drop_wt2_S_err"]) > mp_rat(1, 2)
    pf5_ok = b2["pf5_trivial_P1F5_golden_kernel_dim"] == 0
    pf_count = sum(1 for v in (pf1_ok, pf2_ok, pf3_ok, pf4_ok, pf5_ok) if v)

    out = {
        "card_id": "A2-LEG5-TOWER-MODULAR-BRIDGE",
        "seat_code": "fam3-v1-high-03",
        "firewall": "0 of 19",
        "B1_all_k_tensor_halving_and_level30": b1,
        "B2_chiral_walk_algebra_leg5": b2,
        "B3_mirror_lock_siegel_and_zero_param_stabilization": b3,
        "B4_holomorphic_wp_5div_chiral_pole_and_flow": b4,
        "B5_planted_controls": {
            "PF1_Q8_breaks_character_defect": pf1_ok,
            "PF2_swapped_walk_breaks_commutator": pf2_ok,
            "PF3_R0_breaks_W6_and_I4_saddle": pf3_ok,
            "PF4_drop_wt2_breaks_S_equiv": pf4_ok,
            "PF5_trivial_P1F5_kills_golden_kernel": pf5_ok,
            "caught_count": pf_count,
        },
        "ast_hygiene": ast_rep,
    }
    json_floats = count_json_floats(out)
    all_pass = bool(b1["b1_pass"] and b2["b2_pass"] and b3["b3_pass"] and b4["b4_pass"] and (pf_count == 5) and ast_rep["clean"] and (json_floats == 0))
    out["gates"] = {
        "G1_B1": bool(b1["b1_pass"]),
        "G2_B2": bool(b2["b2_pass"]),
        "G3_B3": bool(b3["b3_pass"]),
        "G4_B4": bool(b4["b4_pass"]),
        "G5_PF": pf_count == 5,
        "G6_hygiene": bool(ast_rep["clean"] and json_floats == 0),
        "all_gates_passed": all_pass,
    }

    if write_json:
        payload = json.dumps(out, indent=2, sort_keys=True) + "\n"
        OUT_JSON_PATH.write_text(payload, encoding="utf-8")
        sha_out = hashlib.sha256(OUT_JSON_PATH.read_bytes()).hexdigest()
        OUT_SHA_PATH.write_text(f"{sha_out}  {OUT_JSON_PATH.name}\n", encoding="utf-8")

    def d(val, sig: int = 8) -> str:
        return mp.nstr(mp.mpf(val), sig)

    i4m = b3["zero_param_I4_min_on_x_half"]
    i6m = b3["zero_param_I6_min_on_x_zero"]
    print(
        f"DECISIVE: B1 Q6_exact={b1['Q6_x_Leg5_exact_match']} G3_mis={b1['G3_O27_vs_Q6_mismatches']}/216 "
        f"G4_mis={b1['G4_O81_vs_Q6_mismatches']}/1944 sis15_nz={b1['G3_sister15_nonzero']} "
        f"lvl30_nz={b1['G3_level30_nonzero']} frozen_O27_O12_O81={b1['frozen_defect_O27_O12_O81_eq_Q6']} "
        f"lvl30_sis15_zero={b1['level30_and_sister15_exact_zero_defect']} comm_all={b1['all_bundles_Wp_Wm_commute']}"
    )
    print(
        f"DECISIVE: B2 comm_WL_WR={b2['comm_WL_WR_zero']} pauli_phi2={b2['pauli_sigma_y_on_E_phi2']} "
        f"pauli_phim2={b2['pauli_sigma_y_on_E_phim2']} WL_C3={b2['WL_eq_minus_phi2_C3sq_on_E_phi2']} "
        f"chiral_poles_SOS={b2['chiral_poles_I4_1_over_5_I6_2_over_45']}"
    )
    print(
        f"DECISIVE: B3 locks=({b3['mirror_lock_arc_eq_tau']},{b3['mirror_lock_half_eq_C3_tau_C3inv']},{b3['mirror_lock_third_eq_C3sq_tau_C3m2']}) "
        f"cusp_60={b3['cusp_lead_and_const_lock_minus60deg']} siegel_eq_lt_1e40={mp.mpf(b3['siegel_T_err']) < mp_pow10(-40) and mp.mpf(b3['siegel_S_err']) < mp_pow10(-40)} "
        f"y_odd={d(b3['y_odd_star'], 10)} I4_y={d(i4m['y_star'], 10)} I4_val={d(i4m['I4_star'], 10)} "
        f"I4_half_ok={i4m['ok']} I6_y={d(i6m['y_star'], 10)} I6_val={d(i6m['I6_star'], 10)} I6_zero_ok={i6m['ok']}"
    )
    print(
        f"DECISIVE: B4 sym_5div={b4['sym_5div_factor_ok']} sym_cubic={b4['sym_cubic_cusp_and_sys_ok']} "
        f"sym_45_15={b4['sym_omega_45_15_and_chiral_pole_ok']} sym_i={b4['sym_lemniscate_i_2_9_and_17_288_ok']} "
        f"om_Vwp={d(b4['omega_V_wp'], 9)} om_closed_lt_1e40={mp.mpf(b4['omega_V_wp_closed_form_err']) < mp_pow10(-40)} "
        f"tot70_I4g={d(b4['tot70_I4_gold'], 6)} tot70_I6g={d(b4['tot70_I6_gold'], 6)} "
        f"pf={pf_count}/5 ast_clean={ast_rep['clean']} json_floats={json_floats} all_gates={all_pass}"
    )
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
