#!/usr/bin/env python3
"""Card AGY-C60 Disjoint Cold-Room Countercheck (Guardrail 6; python3 -I; stdlib + sympy + mpmath only).

Shares zero code with c60_listening_halving_and_p884_producer.py and independently verifies E1..E5 + RPF1..RPF5:
- Read-only custody verification of SCRIPT_SHA256.txt and OUTPUT_SHA256.txt (zero runtime hash writes).
- E1: Algebraic 3-adic locus a^2 + b^2 + c^2 - 3abc == 0 mod 3^{k-1} (zero BFS); full 36x36 Z[omega] matrix operator
      equality U_gamma (V^2 P_2^-) == (W_6^2 P_1^-) U_gamma; genuine 324 -> 108 projected unitary matrix intertwiner
      T_J5 (T_J5^H T_J5 == I_108 and T_J5 M_0 == M_q T_J5); SymPy Berkowitz Z-polynomials at mod 27, characteristic-zero
      sparse power-trace Newton polynomials at mod 81 (verifying Tr(V^{2r}|_{P_0^-}) - Tr(V^{2r}|_{P_1^-}) == 9^r in Z),
      and Danilevsky Frobenius companion reduction over disjoint 712-bit primes at mod 243 (matching all 6 SHA-256 hashes).
- E2: SymPy Schreier-Sims PermutationGroup verification of |G_k| (24, 216, 1944, 52488), |Stab_{G_k}(3,3,3)| (3, 3, 3, 9),
      derived subgroup indices [G_k : [G_k, G_k]] = (2, 6, 6, 6), and ord([C^-1, sigma]^3) = 3 at mod 243, plus CRT
      mod-135 characteristic-zero trace series + rational Pade (6, 6) recovery of exact unpaired factors (zero primes).
- E3-E5: Direct primitive 18th-root product prod(2 + zeta_18^m) == 73 and analytic trigonometric reconstruction of P_6(x);
         numerical 6x6 complex QR eigensolver mp.eig on W_+^2(pi/M) for NH-2; and mp.expm anti-Hermitian U(3) rotations +
         column-by-column mp.lu_solve (zero matrix inversion, zero Cayley) across K = 1..9 for P-884 E3b."""
import ast
from fractions import Fraction as Fr
import hashlib
import json
from pathlib import Path
import mpmath as mp
import sympy as sp
from sympy.combinatorics import Permutation, PermutationGroup

HERE = Path(__file__).resolve().parent
PROD_SCRIPT = HERE / "c60_listening_halving_and_p884_producer.py"
PROD_SCRIPT_SHA = HERE / "SCRIPT_SHA256.txt"
PROD_JSON = HERE / "c60_out.json"
PROD_OUT_SHA = HERE / "OUTPUT_SHA256.txt"
OUT_JSON = HERE / "c60_countercheck_out.json"
IMAG = mp.mpc(0, 1)


def verify_ast_clean() -> dict:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    fl = 0
    fc = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            fl += 1
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
            fc += 1
    assert fl == 0 and fc == 0, (fl, fc)
    return {"ast_float_complex_literals": fl, "ast_float_complex_calls": fc}


def q2mp(q: Fr) -> mp.mpf:
    return mp.mpf(q.numerator) / mp.mpf(q.denominator)


def fmt_mp(val: mp.mpf, digits: int = 25) -> str:
    return mp.nstr(val, digits)


def check_custody_hashes_readonly() -> dict:
    s_hash = hashlib.sha256(PROD_SCRIPT.read_bytes()).hexdigest()
    o_hash = hashlib.sha256(PROD_JSON.read_bytes()).hexdigest()
    rec_s = PROD_SCRIPT_SHA.read_text(encoding="utf-8").strip().split()[0]
    rec_o = PROD_OUT_SHA.read_text(encoding="utf-8").strip().split()[0]
    assert s_hash == rec_s, (s_hash, rec_s)
    assert o_hash == rec_o, (o_hash, rec_o)
    return {"producer_script_sha256": s_hash, "producer_output_sha256": o_hash, "custody_intact": True}


def algebraic_3tower_locus(k: int) -> list:
    m = 3 ** (k - 1)
    if k == 2:
        pts = [(3 * a, 3 * b, 3 * c) for a in (1, 2) for b in (1, 2) for c in (1, 2)]
        pts.sort()
        return pts
    prev = algebraic_3tower_locus(k - 1)
    step = 3 ** (k - 2)
    pts = []
    for x0, y0, z0 in prev:
        a0, b0, c0 = x0 // 3, y0 // 3, z0 // 3
        for da in range(3):
            a = a0 + da * step
            for db in range(3):
                b = b0 + db * step
                for dc in range(3):
                    c = c0 + dc * step
                    if (a * a + b * b + c * c - 3 * a * b * c) % m == 0:
                        pts.append((3 * a, 3 * b, 3 * c))
    pts.sort()
    return pts


def crt_locus_with_5(k_three: int) -> list:
    m3 = 3 ** k_three
    n_tot = m3 * 5
    pts3 = algebraic_3tower_locus(k_three)
    pts5 = [
        (a, b, c)
        for a in range(5)
        for b in range(5)
        for c in range(5)
        if (a or b or c) and (a * a + b * b + c * c - a * b * c) % 5 == 0
    ]
    e3 = 5 * pow(5, -1, m3)
    e5 = m3 * pow(m3, -1, 5)
    out = [
        tuple((u3[t] * e3 + u5[t] * e5) % n_tot for t in range(3))
        for u3 in pts3
        for u5 in pts5
    ]
    out.sort()
    return out


def zw_add(x: tuple, y: tuple) -> tuple:
    return (x[0] + y[0], x[1] + y[1])


def zw_mul(x: tuple, y: tuple) -> tuple:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def zw_conj(z: tuple) -> tuple:
    return (z[0] - z[1], -z[1])


def newton_charpoly_exact(power_sums: list) -> list:
    coeffs = [1]
    for k in range(1, len(power_sums) + 1):
        s = sum(coeffs[k - j] * power_sums[j - 1] for j in range(1, k + 1))
        assert s % k == 0
        coeffs.append(-s // k)
    return coeffs


def sparse_zw_power_traces_fast(dense_zw: list, max_r: int) -> list:
    n = len(dense_zw)
    sp_rows = [[(j, val) for j, val in enumerate(row) if val != (0, 0)] for row in dense_zw]
    pa = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    pb = [[0] * n for _ in range(n)]
    trs = []
    for _ in range(max_r):
        na = [[0] * n for _ in range(n)]
        nb = [[0] * n for _ in range(n)]
        tr_a, tr_b = 0, 0
        for a in range(n):
            ra = na[a]
            rb = nb[a]
            for b, (va, vb) in sp_rows[a]:
                pba = pa[b]
                pbb = pb[b]
                if vb == 0:
                    for j in range(n):
                        ra[j] += va * pba[j]
                        rb[j] += va * pbb[j]
                else:
                    for j in range(n):
                        xa = pba[j]
                        xb = pbb[j]
                        ra[j] += va * xa - vb * xb
                        rb[j] += va * xb + vb * xa - vb * xb
            tr_a += ra[a]
            tr_b += rb[a]
        pa, pb = na, nb
        trs.append((tr_a, tr_b))
    return trs


def danilevsky_frobenius_charpoly_modp(mat: list, p: int) -> list:
    n = len(mat)
    if n == 0:
        return [1]
    a = [row[:] for row in mat]
    end = n
    factors = []
    k = n - 1
    while k >= 0:
        if k == 0:
            m = end
            factors.append([1] + [(p - a[0][j]) % p for j in range(m)])
            break
        piv = -1
        for j in range(k - 1, -1, -1):
            if a[k][j] != 0:
                piv = j
                break
        if piv == -1:
            m = end - k
            factors.append([1] + [(p - a[k][k + j]) % p for j in range(m)])
            end = k
            k -= 1
            continue
        c = k - 1
        if piv != c:
            a[c], a[piv] = a[piv], a[c]
            for i in range(end):
                a[i][c], a[i][piv] = a[i][piv], a[i][c]
        row_k = a[k][:end]
        inv_p = pow(row_k[c], p - 2, p)
        for i in range(end):
            a[i][c] = (a[i][c] * inv_p) % p
        for i in range(end):
            aic = a[i][c]
            if aic:
                ai = a[i]
                for j in range(end):
                    if j != c and row_k[j]:
                        ai[j] = (ai[j] - aic * row_k[j]) % p
        new_rc = [0] * end
        for r_idx in range(end):
            rk = row_k[r_idx]
            if rk:
                ar = a[r_idx]
                for j in range(end):
                    new_rc[j] = (new_rc[j] + rk * ar[j]) % p
        a[c][:end] = new_rc
        a[k][:end] = [1 if j == c else 0 for j in range(end)]
        k -= 1
    res = [1]
    for fac in factors:
        nxt = [0] * (len(res) + len(fac) - 1)
        for i, xv in enumerate(res):
            if xv:
                for j, yv in enumerate(fac):
                    nxt[i + j] = (nxt[i + j] + xv * yv) % p
        res = nxt
    return res


def poly_conv(a: list, b: list) -> list:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def sha_poly(coeffs: list) -> str:
    return hashlib.sha256(",".join(str(v) for v in coeffs).encode("utf-8")).hexdigest()


def bipartite_lift(u_poly: list, x_shift: int, mul4: bool) -> list:
    m = len(u_poly) - 1
    deg = 2 * m + x_shift
    res = [0] * (deg + 1)
    for j, c in enumerate(u_poly):
        d = 2 * (m - j) + x_shift
        if d >= 0:
            res[deg - d] = ((4 ** j) * c) if mul4 else c
        else:
            assert c == 0
    return res


def walk_moves_mod(n_mod: int):
    return (
        lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % n_mod),
        lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % n_mod),
        lambda v: (v[0], (v[0] * v[1] - v[2]) % n_mod, v[1]),
        lambda v: ((v[0] * v[1] - v[2]) % n_mod, v[1], v[0]),
        lambda v: (v[1], (v[1] * v[2] - v[0]) % n_mod, v[2]),
        lambda v: ((v[0] * v[2] - v[1]) % n_mod, v[0], v[2]),
    )


def countercheck_e1(prod_e1: dict, discrepancies: list) -> dict:
    pts27 = algebraic_3tower_locus(3)
    pts27_m = [v for v in pts27 if ((v[0] // 3) * (v[1] // 3) * (v[2] // 3)) % 3 == 2]
    idx27_m = {v: i for i, v in enumerate(pts27_m)}
    n27m = len(pts27_m)
    assert n27m == 36
    moves27 = walk_moves_mod(27)
    s1_27 = lambda v: ((v[1] * v[2] - v[0]) % 27, v[1], v[2])
    s2_27 = lambda v: (v[0], (v[0] * v[2] - v[1]) % 27, v[2])
    s3_27 = lambda v: (v[0], v[1], (v[0] * v[1] - v[2]) % 27)
    v2_mat = [[(0, 0)] * n27m for _ in range(n27m)]
    w2_mat = [[(0, 0)] * n27m for _ in range(n27m)]
    for j, v in enumerate(pts27_m):
        for ga in (s1_27, s2_27, s3_27):
            u = ga(v)
            for gb in (s1_27, s2_27, s3_27):
                i = idx27_m[gb(u)]
                v2_mat[i][j] = zw_add(v2_mat[i][j], (1, 0))
        for g1 in moves27:
            u = g1(v)
            for g2 in moves27:
                i = idx27_m[g2(u)]
                w2_mat[i][j] = zw_add(w2_mat[i][j], (1, 0))
    pow_zw = ((1, 0), (0, 1), (-1, -1))
    pc27 = [idx27_m[(v[1], v[2], v[0])] for v in pts27_m]
    p3_q1 = [[(0, 0)] * n27m for _ in range(n27m)]
    p3_q2 = [[(0, 0)] * n27m for _ in range(n27m)]
    for j in range(n27m):
        j1 = pc27[j]
        j2 = pc27[j1]
        p3_q1[j][j] = zw_add(p3_q1[j][j], (1, 0))
        p3_q1[j1][j] = zw_add(p3_q1[j1][j], pow_zw[2])
        p3_q1[j2][j] = zw_add(p3_q1[j2][j], pow_zw[1])
        p3_q2[j][j] = zw_add(p3_q2[j][j], (1, 0))
        p3_q2[j1][j] = zw_add(p3_q2[j1][j], pow_zw[1])
        p3_q2[j2][j] = zw_add(p3_q2[j2][j], pow_zw[2])
    gam27 = [pow_zw[(((v[1] ** 2) - (v[0] ** 2)) // 27) % 3] for v in pts27_m]

    def mm_zw(a, b):
        sz = len(a)
        out = [[(0, 0)] * sz for _ in range(sz)]
        for r in range(sz):
            for k in range(sz):
                if a[r][k] != (0, 0):
                    ark = a[r][k]
                    for c in range(sz):
                        if b[k][c] != (0, 0):
                            out[r][c] = zw_add(out[r][c], zw_mul(ark, b[k][c]))
        return out

    u_diag = [[(gam27[i] if i == j else (0, 0)) for j in range(n27m)] for i in range(n27m)]
    lhs_op = mm_zw(u_diag, mm_zw(v2_mat, p3_q2))
    rhs_op = mm_zw(mm_zw(w2_mat, p3_q1), u_diag)
    if lhs_op != rhs_op:
        discrepancies.append("E1: Matrix operator identity U_gamma V^2 P_2^- == W_6^2 P_1^- U_gamma failed!")

    idx27 = {v: i for i, v in enumerate(pts27)}
    vis = [False] * 72
    fix27, orbs27 = [], []
    for i, v in enumerate(pts27):
        if vis[i]:
            continue
        i1, i2 = idx27[(v[1], v[2], v[0])], idx27[(v[2], v[0], v[1])]
        if i1 == i:
            vis[i] = True
            fix27.append((i,))
        else:
            vis[i] = vis[i1] = vis[i2] = True
            orbs27.append((i, i1, i2))
    orbs27_0 = fix27 + orbs27
    oid27_0 = {vi: k for k, o in enumerate(orbs27_0) for vi in o}
    w27_0 = [[0] * 26 for _ in range(26)]
    for col, oj in enumerate(orbs27_0):
        for vi in oj:
            for g in moves27:
                tk = oid27_0[idx27[g(pts27[vi])]]
                w27_0[tk][col] += 1
        for tk in range(26):
            w27_0[tk][col] //= len(orbs27_0[tk])
    x_sp = sp.Symbol("x")
    pn27 = [int(c) for c in sp.Poly(sp.Matrix(w27_0).charpoly(x_sp).as_expr(), x_sp).all_coeffs()]
    oid27_3 = {vi: (k, p) for k, o in enumerate(orbs27) for p, vi in enumerate(o)}
    w27_12 = [[0] * 46 for _ in range(46)]
    for k, (u0, u1, u2) in enumerate(orbs27):
        for bi, (pp, np_) in enumerate(((u0, u2), (u1, u2))):
            col = 2 * k + bi
            acc = {}
            for sgn, vi in ((1, pp), (-1, np_)):
                for g in moves27:
                    wi = idx27[g(pts27[vi])]
                    if wi in oid27_3:
                        tk, tp = oid27_3[wi]
                        acc[(tk, tp)] = acc.get((tk, tp), 0) + sgn
            for tk in {tk for tk, _ in acc}:
                w27_12[2 * tk][col] = acc.get((tk, 0), 0)
                w27_12[2 * tk + 1][col] = acc.get((tk, 1), 0)
    p27_12 = sp.Poly(sp.Matrix(w27_12).charpoly(x_sp).as_expr(), x_sp)
    p27_1_expr = sp.prod(fac ** (m // 2) for fac, m in p27_12.factor_list()[1])
    pc27 = [int(c) for c in sp.Poly(p27_1_expr, x_sp).all_coeffs()]
    if sha_poly(pn27) != prod_e1["exact_z_polynomials"]["27"]["p_neutral_sha256"]:
        discrepancies.append("E1: mod 27 neutral polynomial SHA-256 mismatch!")
    if sha_poly(pc27) != prod_e1["exact_z_polynomials"]["27"]["p_charged_single_sha256"]:
        discrepancies.append("E1: mod 27 charged polynomial SHA-256 mismatch!")

    pts243 = algebraic_3tower_locus(5)
    pts243_m = [v for v in pts243 if ((v[0] // 3) * (v[1] // 3) * (v[2] // 3)) % 3 == 2]
    set243_m = set(pts243_m)
    bases81 = sorted({(v[0] % 81, v[1] % 81, v[2] % 81) for v in pts243_m})
    by_b81 = {}
    for v in pts243_m:
        b = (v[0] % 81, v[1] % 81, v[2] % 81)
        if b not in by_b81 or v < by_b81[b]:
            by_b81[b] = v
    lifts81 = [by_b81[b] for b in bases81]
    b81_idx = {b: i for i, b in enumerate(bases81)}
    inv9 = {a: pow(a, -1, 9) for a in (1, 2, 4, 5, 7, 8)}

    def decomp243(v):
        assert v in set243_m
        b = (v[0] % 81, v[1] % 81, v[2] % 81)
        i = b81_idx[b]
        u = lifts81[i]
        s = [(c // 3) % 3 for c in u]
        m = tuple((s[t] * (((v[t] - u[t]) % 243) // 81)) % 3 for t in range(3))
        assert (m[0] + m[1] + m[2]) % 3 == 0
        return i, m

    s1 = lambda v: ((v[1] * v[2] - v[0]) % 243, v[1], v[2])
    s2 = lambda v: (v[0], (v[0] * v[2] - v[1]) % 243, v[2])
    s3 = lambda v: (v[0], v[1], (v[0] * v[1] - v[2]) % 243)
    raw_v2 = []
    c_lift = []
    j5_lift = []
    j5_bad_lift = []
    sym_leaves_surface = 0
    for u in lifts81:
        raw_v2.append([decomp243(gb(ga(u))) for ga in (s1, s2, s3) for gb in (s1, s2, s3)])
        c_lift.append(decomp243((u[2], u[0], u[1])))
        a0, a1, a2 = (u[0] // 3) % 9, (u[1] // 3) % 9, (u[2] // 3) % 9
        ju = ((u[0] + 27 * inv9[a0]) % 243, (u[1] + 27 * inv9[a1]) % 243, (u[2] + 27 * ((inv9[a2] - 3 * a2) % 9)) % 243)
        ju_sym_off = ((u[0] + 27 * inv9[a0]) % 243, (u[1] + 27 * inv9[a1]) % 243, (u[2] + 27 * inv9[a2]) % 243)
        if ju_sym_off not in set243_m:
            sym_leaves_surface += 1
        s_m = [(c // 3) % 3 for c in u]
        ju_tau111 = tuple((u[t] + 81 * s_m[t]) % 243 for t in range(3))
        j5_lift.append(decomp243(ju))
        j5_bad_lift.append(decomp243(ju_tau111))
    assert sym_leaves_surface == 324

    vis81 = [False] * 324
    orbs81 = []
    for i, b in enumerate(bases81):
        if vis81[i]:
            continue
        i1, i2 = b81_idx[(b[1], b[2], b[0])], b81_idx[(b[2], b[0], b[1])]
        vis81[i] = vis81[i1] = vis81[i2] = True
        orbs81.append((i, i1, i2))
    oid81 = {bi: (k, p) for k, o in enumerate(orbs81) for p, bi in enumerate(o)}

    def build_108_zw_mat(l_vec: tuple, q_ch: int) -> list:
        mat = [[(0, 0)] * 108 for _ in range(108)]
        for rk, (rb0, _, _) in enumerate(orbs81):
            rm = {}
            for tj, tm in raw_v2[rb0]:
                ph = (l_vec[0] * tm[0] + l_vec[1] * tm[1] + l_vec[2] * tm[2]) % 3
                rm[tj] = zw_add(rm.get(tj, (0, 0)), pow_zw[ph])
            for tj, vm in rm.items():
                ck, pos = oid81[tj]
                _, b1, b2 = orbs81[ck]
                if pos == 0:
                    pc_ph = 0
                elif pos == 1:
                    _, mc1 = c_lift[b1]
                    pc_ph = (l_vec[0] * mc1[0] + l_vec[1] * mc1[1] + l_vec[2] * mc1[2] - q_ch) % 3
                else:
                    _, mc1 = c_lift[b1]
                    _, mc2 = c_lift[b2]
                    pc_ph = (
                        l_vec[0] * (mc1[0] + mc2[0])
                        + l_vec[1] * (mc1[1] + mc2[1])
                        + l_vec[2] * (mc1[2] + mc2[2])
                        - 2 * q_ch
                    ) % 3
                mat[rk][ck] = zw_add(mat[rk][ck], zw_mul(vm, pow_zw[pc_ph]))
        return mat

    m_000_q0 = build_108_zw_mat((0, 0, 0), 0)
    m_000_q1 = build_108_zw_mat((0, 0, 0), 1)
    tr_000_q0 = sparse_zw_power_traces_fast(m_000_q0, 108)
    tr_000_q1 = sparse_zw_power_traces_fast(m_000_q1, 108)
    assert all(tb == 0 for _, tb in tr_000_q0) and all(tb == 0 for _, tb in tr_000_q1)
    assert all(tr_000_q0[r - 1][0] - tr_000_q1[r - 1][0] == 9 ** r for r in range(1, 109))
    u_000_q0 = newton_charpoly_exact([ta for ta, _ in tr_000_q0])
    u_000_q1 = newton_charpoly_exact([ta for ta, _ in tr_000_q1])
    pn81 = bipartite_lift(u_000_q0, 2, True)
    pc81 = bipartite_lift(u_000_q1, -1, False)
    if sha_poly(pn81) != prod_e1["exact_z_polynomials"]["81"]["p_neutral_sha256"]:
        discrepancies.append("E1: mod 81 neutral polynomial SHA-256 mismatch!")
    if sha_poly(pc81) != prod_e1["exact_z_polynomials"]["81"]["p_charged_single_sha256"]:
        discrepancies.append("E1: mod 81 charged polynomial SHA-256 mismatch!")

    m_012_q0 = build_108_zw_mat((0, 1, 2), 0)
    m_012_q1 = build_108_zw_mat((0, 1, 2), 1)
    m_012_q2 = build_108_zw_mat((0, 1, 2), 2)

    def build_projected_intertwiner(jlift_table, target_q: int):
        t3 = [[(0, 0)] * 108 for _ in range(108)]
        for x_idx in range(324):
            rk, rpos = oid81[x_idx]
            _, rb1, rb2 = orbs81[rk]
            if rpos == 0:
                r_ph = 0
            elif rpos == 1:
                _, rc1 = c_lift[rb1]
                r_ph = (rc1[1] + 2 * rc1[2] - target_q) % 3
            else:
                _, rc1 = c_lift[rb1]
                _, rc2 = c_lift[rb2]
                r_ph = (rc1[1] + rc2[1] + 2 * (rc1[2] + rc2[2]) - 2 * target_q) % 3
            bra_ph = (-r_ph) % 3
            tj, tm = jlift_table[x_idx]
            j_ph = (tm[1] + 2 * tm[2]) % 3
            ck, cpos = oid81[tj]
            _, cb1, cb2 = orbs81[ck]
            if cpos == 0:
                c_ph = 0
            elif cpos == 1:
                _, cc1 = c_lift[cb1]
                c_ph = (cc1[1] + 2 * cc1[2]) % 3
            else:
                _, cc1 = c_lift[cb1]
                _, cc2 = c_lift[cb2]
                c_ph = (cc1[1] + cc2[1] + 2 * (cc1[2] + cc2[2])) % 3
            tot_ph = (bra_ph + j_ph + c_ph) % 3
            t3[rk][ck] = zw_add(t3[rk][ck], pow_zw[tot_ph])
        assert all(val[0] % 3 == 0 and val[1] % 3 == 0 for row in t3 for val in row)
        return [[(val[0] // 3, val[1] // 3) for val in row] for row in t3]

    def is_unitary_108(t_mat: list) -> bool:
        th = [[zw_conj(t_mat[r][c]) for r in range(108)] for c in range(108)]
        prod = mm_zw(th, t_mat)
        eye108 = [[((1, 0) if i == j else (0, 0)) for j in range(108)] for i in range(108)]
        return prod == eye108

    t_to_1 = build_projected_intertwiner(j5_lift, 1)
    t_to_2 = build_projected_intertwiner(j5_lift, 2)
    eq_q1 = is_unitary_108(t_to_1) and (mm_zw(t_to_1, m_012_q0) == mm_zw(m_012_q1, t_to_1))
    eq_q2 = is_unitary_108(t_to_2) and (mm_zw(t_to_2, m_012_q0) == mm_zw(m_012_q2, t_to_2))
    assert eq_q1 or eq_q2
    t_bad_1 = build_projected_intertwiner(j5_bad_lift, 1)
    t_bad_2 = build_projected_intertwiner(j5_bad_lift, 2)
    rpf2_caught = (sym_leaves_surface == 324) and (not is_unitary_108(t_bad_1)) and (not is_unitary_108(t_bad_2))
    assert rpf2_caught

    tr_012_q0 = sparse_zw_power_traces_fast(m_012_q0, 108)
    u_012_q0 = newton_charpoly_exact([ta for ta, _ in tr_012_q0])

    vis_j = [False] * 324
    j_orbs = []
    for i in range(324):
        if vis_j[i]:
            continue
        i1, m1 = j5_lift[i]
        i2, m2 = j5_lift[i1]
        vis_j[i] = vis_j[i1] = vis_j[i2] = True
        j_orbs.append((i, i1, i2, m1[0] % 3, (m1[0] + m2[0]) % 3))
    j_oid = {o[p]: (k, p) for k, o in enumerate(j_orbs) for p in range(3)}

    disjoint_primes = []
    cand_q = int(sp.nextprime(1 << 712))
    while len(disjoint_primes) < 2:
        while cand_q % 9 != 1:
            cand_q = int(sp.nextprime(cand_q))
        for g_b in range(2, 100):
            z9 = pow(g_b, (cand_q - 1) // 9, cand_q)
            w = pow(z9, 3, cand_q)
            if w != 1 and (1 + w + (w * w) % cand_q) % cand_q == 0:
                disjoint_primes.append((cand_q, w, z9))
                break
        cand_q = int(sp.nextprime(cand_q))

    dan_lifts = []
    for pq, wq, z9q in disjoint_primes:
        prod_p = [1]
        for s_i in range(3):
            eig = (z9q * pow(wq, s_i, pq)) % pq
            eig2 = (eig * eig) % pq
            blk = [[0] * 108 for _ in range(108)]
            for rk, (rb0, _, _, _, _) in enumerate(j_orbs):
                rm = {}
                for tj, tm in raw_v2[rb0]:
                    rm[tj] = (rm.get(tj, 0) + pow(wq, tm[0] % 3, pq)) % pq
                for tj, vm in rm.items():
                    ck, pos = j_oid[tj]
                    _, _, _, ph1, ph2 = j_orbs[ck]
                    c_ph = 1 if pos == 0 else ((eig * pow(wq, (-ph1) % 3, pq)) % pq if pos == 1 else (eig2 * pow(wq, (-ph2) % 3, pq)) % pq)
                    blk[rk][ck] = (blk[rk][ck] + vm * c_ph) % pq
            cp_b = danilevsky_frobenius_charpoly_modp(blk, pq)
            nxt = [0] * (len(prod_p) + len(cp_b) - 1)
            for ia, va in enumerate(prod_p):
                if va:
                    for ib, vb in enumerate(cp_b):
                        nxt[ia + ib] = (nxt[ia + ib] + va * vb) % pq
            prod_p = nxt
        hq = pq // 2
        dan_lifts.append([v - pq if v > hq else v for v in prod_p])
    assert dan_lifts[0] == dan_lifts[1]
    u_100 = dan_lifts[0]

    u_012_sq = poly_conv(u_012_q0, u_012_q0)
    u_100_sq = poly_conv(u_100, u_100)
    v2_243_0 = poly_conv(u_000_q0, poly_conv(u_012_sq, u_100_sq))
    v2_243_1 = poly_conv(u_000_q1, poly_conv(u_012_sq, u_100_sq))
    pn243 = bipartite_lift(v2_243_0, 2, True)
    pc243 = bipartite_lift(v2_243_1, -1, False)
    if sha_poly(pn243) != prod_e1["exact_z_polynomials"]["243"]["p_neutral_sha256"]:
        discrepancies.append("E1: mod 243 neutral polynomial SHA-256 mismatch!")
    if sha_poly(pc243) != prod_e1["exact_z_polynomials"]["243"]["p_charged_single_sha256"]:
        discrepancies.append("E1: mod 243 charged polynomial SHA-256 mismatch!")
    if str(pn243[2]) != prod_e1["exact_z_polynomials"]["243"]["p_neutral_x2_coeff"]:
        discrepancies.append("E1: mod 243 neutral x^2 coeff mismatch!")

    pc243_bad = pc243[:]
    pc243_bad[-2] += 1
    lhs243 = [pn243[k] * (2 ** (1946 - k)) for k in range(1947)]
    rhs243_bad = [(2 ** 1946) * c for c in poly_conv([1, 0, -9, 0], pc243_bad)]
    rpf1_caught = lhs243 != rhs243_bad
    assert rpf1_caught
    return {
        "u_gamma_matrix_operator_27_exact": lhs_op == rhs_op,
        "j5_explicit_108x108_matrix_intertwiner_exact": bool(eq_q1 or eq_q2),
        "mod81_characteristic_zero_power_traces_exact": True,
        "mod27_81_243_sha256_all_matched": len(discrepancies) == 0,
        "rpf1_perturbed_mod243_poly_caught": rpf1_caught,
        "rpf2_wrong_sign_j5_intertwiner_caught": rpf2_caught,
    }


def countercheck_e2(prod_e2: dict, discrepancies: list) -> dict:
    ab_orders = {}
    for k, n_mod in ((2, 9), (3, 27), (4, 81), (5, 243)):
        pts = algebraic_3tower_locus(k)
        idx = {v: i for i, v in enumerate(pts)}
        perm_c = Permutation([idx[(v[1], v[2], v[0])] for v in pts])
        perm_s = Permutation([idx[(v[1], v[0], (v[0] * v[1] - v[2]) % n_mod)] for v in pts])
        grp = PermutationGroup(perm_c, perm_s)
        g_ord = int(grp.order())
        if g_ord != prod_e2["group_stats"][str(n_mod)]["image_group_order"]:
            discrepancies.append(f"E2: Schreier-Sims order mismatch at mod {n_mod}!")
        der_ord = int(grp.derived_subgroup().order())
        ab_orders[str(n_mod)] = g_ord // der_ord
        if k >= 3:
            v0 = idx[(3, 3, 3)]
            stab_ord = int(grp.stabilizer(v0).order())
            if stab_ord != prod_e2["group_stats"][str(n_mod)]["stab_333_order"]:
                discrepancies.append(f"E2: Stabilizer order mismatch at mod {n_mod}!")
        if n_mod == 243:
            comm = (~perm_c) * perm_s * perm_c * perm_s
            assert int((comm ** 3).order()) == 3
    if ab_orders != {"9": 2, "27": 6, "81": 6, "243": 6}:
        discrepancies.append(f"E2: Abelianization order mismatch: {ab_orders}")
    rpf3_caught = ab_orders["243"] != 2
    assert rpf3_caught

    pts135 = crt_locus_with_5(3)
    if len(pts135) != prod_e2["mod135_orbit_size"]:
        discrepancies.append("E2: mod 135 CRT locus size mismatch!")
    pts135_m = [v for v in pts135 if (((v[0] % 27) // 3) * ((v[1] % 27) // 3) * ((v[2] % 27) // 3)) % 3 == 2]
    bases45 = sorted({(v[0] % 45, v[1] % 45, v[2] % 45) for v in pts135_m})
    by_b45 = {}
    for v in pts135_m:
        b = (v[0] % 45, v[1] % 45, v[2] % 45)
        if b not in by_b45 or v < by_b45[b]:
            by_b45[b] = v
    lifts45 = [by_b45[b] for b in bases45]
    b45_idx = {b: i for i, b in enumerate(bases45)}

    def decomp135(v):
        b = (v[0] % 45, v[1] % 45, v[2] % 45)
        i = b45_idx[b]
        u = lifts45[i]
        s = [((c % 27) // 3) % 3 for c in u]
        m = tuple((s[t] * (((u[t] - v[t]) % 135) // 45)) % 3 for t in range(3))
        return i, m

    s1 = lambda v: ((v[1] * v[2] - v[0]) % 135, v[1], v[2])
    s2 = lambda v: (v[0], (v[0] * v[2] - v[1]) % 135, v[2])
    s3 = lambda v: (v[0], v[1], (v[0] * v[1] - v[2]) % 135)
    to_cos = lambda v: 3 * decomp135(v)[0] + ((decomp135(v)[1][1] + 2 * decomp135(v)[1][2]) % 3)
    rep_c = {}
    for v in pts135_m:
        c = to_cos(v)
        if c not in rep_c:
            rep_c[c] = v
    pc_c = [to_cos((rep_c[c][1], rep_c[c][2], rep_c[c][0])) for c in range(480)]
    c_sp = []
    for c in range(480):
        u0 = rep_c[c]
        row = {}
        for ga in (s1, s2, s3):
            xv = ga(u0)
            for gb in (s1, s2, s3):
                tc = to_cos(gb(xv))
                row[tc] = row.get(tc, 0) + 1
        c_sp.append(list(row.items()))
    pa = [[1 if i == j else 0 for j in range(480)] for i in range(480)]
    d_tr = []
    for _ in range(14):
        na = [[0] * 480 for _ in range(480)]
        for a in range(480):
            ra = na[a]
            for b, val in c_sp[a]:
                pb = pa[b]
                if val == 1:
                    for j in range(480):
                        ra[j] += pb[j]
                else:
                    for j in range(480):
                        ra[j] += val * pb[j]
        pa = na
        d_tr.append(sum(pa[p_idx][col] for col, p_idx in enumerate(pc_c)))
    ser = [Fr(1)]
    for k in range(1, 15):
        ser.append(-sum(Fr(d_tr[j - 1]) * ser[k - j] for j in range(1, k + 1)) / Fr(k))
    a_v = sp.symbols("a1:7")
    b_v = sp.symbols("b1:7")
    a_arr = [1] + list(a_v) + [0] * 8
    b_arr = [1] + list(b_v) + [0] * 8
    eqs = [
        a_arr[k] - sum(sp.Rational(ser[k - j].numerator, ser[k - j].denominator) * b_arr[j] for j in range(min(k + 1, 7)))
        for k in range(1, 15)
    ]
    sol = sp.solve(eqs, list(a_v) + list(b_v))
    x_sym = sp.Symbol("x")
    q0_u = (x_sym ** 12) + sum(sol[a_v[i]] * (x_sym ** (10 - 2 * i)) for i in range(6))
    q1_u = (x_sym ** 12) + sum(sol[b_v[i]] * (x_sym ** (10 - 2 * i)) for i in range(6))
    unp_neu = str(sp.factor(sp.simplify(x_sym * q0_u)))
    unp_chg = str(sp.factor(sp.simplify(q1_u / (x_sym ** 2))))
    if unp_chg != prod_e2["mod135_unpaired_charged_poly"]:
        discrepancies.append(f"E2: mod 135 unpaired charged poly mismatch: {unp_chg}")
    if unp_neu != prod_e2["mod135_unpaired_neutral_poly"]:
        discrepancies.append(f"E2: mod 135 unpaired neutral poly mismatch: {unp_neu}")
    return {
        "schreier_sims_abelianization_orders": ab_orders,
        "mod135_pade_zero_prime_unpaired_matched": unp_chg == prod_e2["mod135_unpaired_charged_poly"],
        "rpf3_false_z2_at_243_caught": rpf3_caught,
    }


def countercheck_e3_e4_e5(prod: dict, discrepancies: list) -> dict:
    mp.mp.dps = 60
    prod_plus = mp.mpc(1, 0)
    prod_minus = mp.mpc(1, 0)
    for m in (1, 5, 7, 11, 13, 17):
        zeta = mp.exp(2 * IMAG * mp.pi * m / 18)
        prod_plus *= 2 + zeta
        prod_minus *= 2 - zeta
    if abs(prod_plus - 73) > mp.mpf(10) ** (-50):
        discrepancies.append("E3: Root-of-unity product for Phi_18(-2) != 73!")
    rpf4_caught = abs(prod_minus - 57) < mp.mpf(10) ** (-50) and int(mp.nint(mp.re(prod_minus))) != 73
    assert rpf4_caught

    roots_sq = [4 * (5 + 4 * mp.cos(k_ang * mp.pi / 9)) for k_ang in (1, 5, 7)]
    e1_s = sum(roots_sq)
    e2_s = roots_sq[0] * roots_sq[1] + roots_sq[1] * roots_sq[2] + roots_sq[2] * roots_sq[0]
    e3_s = roots_sq[0] * roots_sq[1] * roots_sq[2]
    if max(abs(e1_s - 60), abs(e2_s - 1008), abs(e3_s - 4672)) > mp.mpf(10) ** (-48):
        discrepancies.append("E3: Analytic trigonometric roots failed to reconstruct P_6(x)!")

    al_dual = lambda kv: (kv[0], kv[0] - kv[1])
    ar_dual = lambda kv: (kv[1] - kv[0], kv[1])
    shell = sorted({(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)})
    sh_i = {v: i for i, v in enumerate(shell)}
    max_nh2_diff = mp.mpf(0)
    for m_per in (3, 9, 5, 25, 7):
        th = mp.pi / m_per
        m10 = mp.zeros(6, 6)
        m01 = mp.zeros(6, 6)
        for j, kv in enumerate(shell):
            il, ir = sh_i[al_dual(kv)], sh_i[ar_dual(kv)]
            m10[il, j] += 1
            m10[ir, j] += 1
            m01[il, j] += mp.exp(IMAG * th * kv[0])
            m01[ir, j] += mp.exp(IMAG * th * kv[1])
        w_sq = m01 * m10
        eig_vals, _ = mp.eig(w_sq)
        lam_num = max(mp.sqrt(abs(ev)) for ev in eig_vals) / 2
        prod_val = mp.mpf(prod["e4_peer_agy_exp_nh2_nh4"]["nh2_benchmarks"][str(m_per)])
        diff = abs(lam_num - prod_val)
        if diff > max_nh2_diff:
            max_nh2_diff = diff
    if max_nh2_diff > mp.mpf(10) ** (-20):
        discrepancies.append(f"E4: NH-2 numerical Bloch eigenvalue diff too large: {fmt_mp(max_nh2_diff, 10)}")

    def expm_u3(anti_h: mp.matrix) -> mp.matrix:
        return mp.expm(anti_h)

    uq = expm_u3(
        mp.matrix(
            [
                [IMAG * q2mp(Fr(2, 5)), q2mp(Fr(1, 4)) + IMAG * q2mp(Fr(1, 9)), -q2mp(Fr(2, 11))],
                [-q2mp(Fr(1, 4)) + IMAG * q2mp(Fr(1, 9)), -IMAG * q2mp(Fr(3, 7)), q2mp(Fr(1, 8))],
                [q2mp(Fr(2, 11)), -q2mp(Fr(1, 8)), IMAG * q2mp(Fr(1, 13))],
            ]
        )
    )
    uqr = expm_u3(
        mp.matrix(
            [
                [-IMAG * q2mp(Fr(3, 11)), -q2mp(Fr(1, 6)) + IMAG * q2mp(Fr(2, 7)), q2mp(Fr(1, 15))],
                [q2mp(Fr(1, 6)) + IMAG * q2mp(Fr(2, 7)), IMAG * q2mp(Fr(2, 9)), -q2mp(Fr(3, 13))],
                [-q2mp(Fr(1, 15)), q2mp(Fr(3, 13)), -IMAG * q2mp(Fr(1, 5))],
            ]
        )
    )
    ys = []
    for k_i in range(9):
        ym = mp.zeros(3, 3)
        for r in range(3):
            for c in range(3):
                ym[r, c] = q2mp(Fr(2, 3 + k_i + 2 * r + c)) + IMAG * q2mp(Fr((-1) ** (k_i + r), 4 + k_i + r + 2 * c))
        ys.append(ym)

    def solve_boundary_dirac_lu(y_list: list) -> mp.matrix:
        k_len = len(y_list)
        if k_len == 1:
            return y_list[0]
        dim_b = 3 * (k_len - 1)
        b_mat = mp.zeros(dim_b, dim_b)
        a_mat = mp.zeros(dim_b, 3)
        d_mat = mp.zeros(3, dim_b)
        for r in range(3):
            b_mat[r, r] = -mp.mpf(1)
            for c in range(3):
                a_mat[r, c] = y_list[0].transpose_conj()[r, c]
                last_y = y_list[-1].transpose_conj() if (k_len % 2 == 1) else y_list[-1]
                d_mat[r, dim_b - 3 + c] = last_y[r, c]
        for blk in range(1, k_len - 1):
            r0 = 3 * blk
            yb = y_list[blk] if blk % 2 == 1 else y_list[blk].transpose_conj()
            for r in range(3):
                b_mat[r0 + r, r0 + r] = -mp.mpf(1)
                for c in range(3):
                    b_mat[r0 + r, r0 - 3 + c] = yb[r, c]
        x_sol = mp.zeros(dim_b, 3)
        for col in range(3):
            rhs_col = mp.matrix([a_mat[r, col] for r in range(dim_b)])
            sol_col = mp.lu_solve(b_mat, rhs_col)
            for r in range(dim_b):
                x_sol[r, col] = sol_col[r]
        return (-d_mat * x_sol).transpose_conj()

    def fnorm(m: mp.matrix) -> mp.mpf:
        return mp.sqrt(sum(mp.re(m[r, c]) ** 2 + mp.im(m[r, c]) ** 2 for r in range(m.rows) for c in range(m.cols)))

    lu_defects = {}
    for k_len in range(1, 10):
        y_orig = solve_boundary_dirac_lu(ys[:k_len])
        ys_rot = [uq * yj * uqr.transpose_conj() for yj in ys[:k_len]]
        y_rot = solve_boundary_dirac_lu(ys_rot)
        err = fnorm(y_rot - uq * y_orig * uqr.transpose_conj()) / fnorm(y_orig)
        lu_defects[str(k_len)] = fmt_mp(err, 12)
        if k_len % 2 == 1:
            if err > mp.mpf(10) ** (-42):
                discrepancies.append(f"E5: Odd K={k_len} LU chiral check failed!")
        else:
            if err < q2mp(Fr(1, 2)):
                discrepancies.append(f"E5: Even K={k_len} failed to violate chiral covariance!")
    rpf5_caught = mp.mpf(lu_defects["6"]) > q2mp(Fr(1, 2)) and mp.mpf(lu_defects["5"]) < mp.mpf(10) ** (-42)
    assert rpf5_caught
    return {
        "phi18_minus2_root_product_exact": True,
        "nh2_max_numerical_bloch_diff": fmt_mp(max_nh2_diff, 12),
        "e5_lu_chiral_defects_k1_to_k9": lu_defects,
        "rpf4_sign_flipped_phi18_caught": rpf4_caught,
        "rpf5_even_k6_lu_chiral_violation_caught": rpf5_caught,
    }


def main():
    ast_res = verify_ast_clean()
    cust_res = check_custody_hashes_readonly()

    def bad_float(val):
        raise ValueError(f"JSON float forbidden: {val}")

    prod_data = json.loads(PROD_JSON.read_text(encoding="utf-8"), parse_float=bad_float)
    discrepancies = []
    c_e1 = countercheck_e1(prod_data["e1_all_k_halving_and_mod243"], discrepancies)
    c_e2 = countercheck_e2(prod_data["e2_b2004_b2005_group_and_mixed_levels"], discrepancies)
    c_345 = countercheck_e3_e4_e5(prod_data, discrepancies)
    assert len(discrepancies) == 0, discrepancies

    rpf = {
        "rpf1_perturbed_mod243_poly_caught": c_e1["rpf1_perturbed_mod243_poly_caught"],
        "rpf2_wrong_sign_j5_intertwiner_caught": c_e1["rpf2_wrong_sign_j5_intertwiner_caught"],
        "rpf3_false_z2_at_243_caught": c_e2["rpf3_false_z2_at_243_caught"],
        "rpf4_sign_flipped_phi18_caught": c_345["rpf4_sign_flipped_phi18_caught"],
        "rpf5_even_k6_lu_chiral_violation_caught": c_345["rpf5_even_k6_lu_chiral_violation_caught"],
    }
    assert all(rpf.values())

    report = {
        "card": "AGY-C60",
        "empirical_anchor": "0 of 19",
        "ast_firewall": ast_res,
        "custody": cust_res,
        "e1_countercheck": c_e1,
        "e2_countercheck": c_e2,
        "e3_e4_e5_countercheck": c_345,
        "referee_planted_faults": rpf,
        "referee_planted_faults_caught_count": sum(1 for v in rpf.values() if v),
        "discrepancies": discrepancies,
        "discrepancies_count": len(discrepancies),
    }
    raw_out = json.dumps(report, indent=2, sort_keys=True) + "\n"
    json.loads(raw_out, parse_float=bad_float)
    OUT_JSON.write_text(raw_out, encoding="utf-8")


if __name__ == "__main__":
    main()
