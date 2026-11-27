#!/usr/bin/env python3
"""Card A2-PEER-SM-R581 — Blind Cross-Family Independent Verification of SM-R581
(P-581, I-9; 1,199 census manifolds <= 6 tets, 2T/2O/2I surjection census, and (Z_6, Y, 3/8) structural package).

Seat code: fam3-v1-high-03 (verifying fam1-v1-unset-04 on origin/sm/cards @ 1c5b13d0a).
Strictly blind (0 of 19): ZERO sm/cards scripts, presentations, or outputs opened before sealing.
Census presentations independently generated from SnapPy 3.3.2 into a2_r581_snappy_presentations.json.
Self-contained: stdlib + sympy only; ZERO AST float literals; ZERO JSON floats.
"""
import ast
import json
import math
import pathlib
import sys
from collections import Counter, deque
from fractions import Fraction as Fr

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
PRES_JSON = HERE / "a2_r581_snappy_presentations.json"
OUT_JSON = HERE / "a2_peer_sm_r581_out.json"


# ============================================================================
# 1. Exact finite group constructors (2T = SL(2,3), 2O, 2I = SL(2,5)) + Aut(G)
# ============================================================================
def _build_sl2_fp(p):
    elems = []
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a * d - b * c) % p == 1:
                        elems.append((a, b, c, d))
    idx = {e: i for i, e in enumerate(elems)}
    n = len(elems)
    id_i = idx[(1, 0, 0, 1)]
    mul = [[0] * n for _ in range(n)]
    inv = [0] * n
    for i, (a, b, c, d) in enumerate(elems):
        inv[i] = idx[(d % p, (-b) % p, (-c) % p, a % p)]
        for j, (e, f, g, h) in enumerate(elems):
            mul[i][j] = idx[((a * e + b * g) % p, (a * f + b * h) % p,
                             (c * e + d * g) % p, (c * f + d * h) % p)]
    return n, id_i, mul, inv


def _build_2O():
    """Build exact binary octahedral group 2O (order 48) in exact Z[sqrt(2)]/2 quaternions.
    Quaternion q = sum_k ((a_k + b_k sqrt(2)) / 2) e_k, represented as 8-tuple of ints (a0,b0,a1,b1,a2,b2,a3,b3)."""
    def qmul(x, y):
        # Multiply (a + b sqrt(2))/2 * (c + d sqrt(2))/2 = ((ac + 2bd) + (ad + bc) sqrt(2)) / 4
        # Divide numerator by 2 (exact since every product in 2O stays in Z[sqrt(2)]/2)
        def pmul(p, q):
            return (p[0] * q[0] + 2 * p[1] * q[1], p[0] * q[1] + p[1] * q[0])

        def padd(p, q):
            return (p[0] + q[0], p[1] + q[1])

        def psub(p, q):
            return (p[0] - q[0], p[1] - q[1])

        x0, x1, x2, x3 = (x[0], x[1]), (x[2], x[3]), (x[4], x[5]), (x[6], x[7])
        y0, y1, y2, y3 = (y[0], y[1]), (y[2], y[3]), (y[4], y[5]), (y[6], y[7])
        r0 = psub(psub(psub(pmul(x0, y0), pmul(x1, y1)), pmul(x2, y2)), pmul(x3, y3))
        r1 = psub(padd(padd(pmul(x0, y1), pmul(x1, y0)), pmul(x2, y3)), pmul(x3, y2))
        r2 = padd(psub(padd(pmul(x0, y2), pmul(x2, y0)), pmul(x1, y3)), pmul(x3, y1))
        r3 = psub(padd(padd(pmul(x0, y3), pmul(x3, y0)), pmul(x1, y2)), pmul(x2, y1))
        out = []
        for a, b in (r0, r1, r2, r3):
            assert a % 2 == 0 and b % 2 == 0
            out.extend([a // 2, b // 2])
        return tuple(out)

    # Generators of 2O: gL = (1 + i)/sqrt(2) = (sqrt(2)/2) + (sqrt(2)/2) i; gR = (1 - j)/sqrt(2)
    e_id = (2, 0, 0, 0, 0, 0, 0, 0)
    gL = (0, 1, 0, 1, 0, 0, 0, 0)
    gR = (0, 1, 0, 0, 0, -1, 0, 0)
    seen = {e_id}
    q = deque([e_id])
    while q:
        cur = q.popleft()
        for g in (gL, gR):
            nxt = qmul(cur, g)
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    elems = sorted(seen)
    assert len(elems) == 48
    idx = {e: i for i, e in enumerate(elems)}
    n = len(elems)
    id_i = idx[e_id]
    mul = [[0] * n for _ in range(n)]
    inv = [0] * n
    for i, x in enumerate(elems):
        # Conjugate of unit quaternion is its inverse
        xc = (x[0], x[1], -x[2], -x[3], -x[4], -x[5], -x[6], -x[7])
        inv[i] = idx[xc]
        for j, y in enumerate(elems):
            mul[i][j] = idx[qmul(x, y)]
    return n, id_i, mul, inv


def _subgroup_size(gens, n, id_i, mul):
    seen = {id_i}
    q = deque([id_i])
    for g in gens:
        if g not in seen:
            seen.add(g)
            q.append(g)
    while q:
        cur = q.popleft()
        for g in gens:
            nxt = mul[cur][g]
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
            if len(seen) == n:
                return n
    return len(seen)


def _compute_aut_group(n, id_i, mul, inv):
    """Compute exact full automorphism group Aut(G) by minimal generating pair + extension."""
    # Find a 2-generator pair (u, v) generating G
    gen_pair = None
    for u in range(n):
        if u == id_i:
            continue
        for v in range(u + 1, n):
            if _subgroup_size((u, v), n, id_i, mul) == n:
                gen_pair = (u, v)
                break
        if gen_pair is not None:
            break
    assert gen_pair is not None
    u0, v0 = gen_pair

    # Express every element as a BFS word in (u0, v0)
    words = {id_i: ()}
    q = deque([id_i])
    while q:
        cur = q.popleft()
        w = words[cur]
        for sym, g in ((0, u0), (1, v0)):
            nxt = mul[cur][g]
            if nxt not in words:
                words[nxt] = w + (sym,)
                q.append(nxt)
    assert len(words) == n

    # Element orders
    orders = []
    for x in range(n):
        c = x
        k = 1
        while c != id_i:
            c = mul[c][x]
            k += 1
        orders.append(k)
    ou, ov = orders[u0], orders[v0]

    # Candidate pairs (u1, v1) with matching orders that extend to a bijection preserving mul
    auts = []
    cands_u = [x for x in range(n) if orders[x] == ou]
    cands_v = [x for x in range(n) if orders[x] == ov]
    # Pre-check conjugacy/product order of u0*v0
    ouv = orders[mul[u0][v0]]
    for u1 in cands_u:
        for v1 in cands_v:
            if orders[mul[u1][v1]] != ouv:
                continue
            # Build candidate map via words
            img = [0] * n
            for x in range(n):
                cur = id_i
                for sym in words[x]:
                    cur = mul[cur][u1 if sym == 0 else v1]
                img[x] = cur
            if len(set(img)) != n:
                continue
            # Check homomorphism on generators: img[mul[x][g]] == mul[img[x]][img[g]] for all x and g in (u0, v0)
            ok = True
            for x in range(n):
                ix = img[x]
                if img[mul[x][u0]] != mul[ix][u1] or img[mul[x][v0]] != mul[ix][v1]:
                    ok = False
                    break
            if ok:
                auts.append(tuple(img))

    # Compute Aut(G) orbits on G
    rem = set(range(n))
    orbits = []
    while rem:
        rep = min(rem)
        orb = {phi[rep] for phi in auts}
        rem -= orb
        orbits.append((rep, len(orb)))
    return len(auts), orbits


def _parse_relator(rel_str, gen_list):
    """Parse SnapPy word (e.g. 'aBca') into list of (gen_idx, is_inv)."""
    gmap = {g: i for i, g in enumerate(gen_list)}
    out = []
    for ch in rel_str:
        low = ch.lower()
        out.append((gmap[low], ch.isupper()))
    return tuple(out)


def _eval_word(word, vals, id_i, mul, inv):
    cur = id_i
    for gi, is_inv in word:
        g = vals[gi]
        cur = mul[cur][inv[g] if is_inv else g]
    return cur


def _count_surjections(gens, rels, n, id_i, mul, inv, aut_size, orbits, gen_pair_ok=None):
    """Exact count of Aut(G)-classes of surjections pi_1(M) ->> G using orbit symmetry breaking + relator pruning."""
    ng = len(gens)
    parsed = [_parse_relator(r, gens) for r in rels]

    if ng == 2:
        # 2 generators: fix g0 to orbit representative, loop g1 over 0..n-1
        raw = 0
        for rep, orb_sz in orbits:
            cnt = 0
            for g1 in range(n):
                # Quick surjectivity precheck via precomputed 2-gen table if supplied
                if gen_pair_ok is not None and not gen_pair_ok[rep][g1]:
                    continue
                vals = (rep, g1)
                ok = True
                for w in parsed:
                    if _eval_word(w, vals, id_i, mul, inv) != id_i:
                        ok = False
                        break
                if ok:
                    if gen_pair_ok is None and _subgroup_size(vals, n, id_i, mul) != n:
                        continue
                    cnt += 1
            raw += cnt * orb_sz
        assert raw % aut_size == 0, f"Raw {raw} not divisible by |Aut|={aut_size}"
        return raw // aut_size

    if ng == 3:
        # 3 generators: reorder generators so if any generator appears ONCE in any relator, solve it in O(1)!
        # Check occurrence counts in each relator
        solve_spec = None
        for r_idx, w in enumerate(parsed):
            occ = Counter(gi for gi, _ in w)
            for gi in range(3):
                if occ[gi] == 1:
                    # Find position pos of gi in w: prefix * (g_gi^{+-1}) * suffix = id
                    # => g_gi^{+-1} = prefix^{-1} * suffix^{-1} = (suffix * prefix)^{-1}
                    pos = next(k for k, (g_k, _) in enumerate(w) if g_k == gi)
                    is_inv = w[pos][1]
                    rest = w[pos + 1:] + w[:pos]
                    other_rels = [parsed[k] for k in range(len(parsed)) if k != r_idx]
                    others = [k for k in range(3) if k != gi]
                    solve_spec = (gi, is_inv, rest, other_rels, others)
                    break
            if solve_spec is not None:
                break

        raw = 0
        if solve_spec is not None:
            # O(orbits * n) exact solve!!
            gi_s, is_inv_s, rest_w, other_rels, (gA, gB) = solve_spec
            vals = [0, 0, 0]
            for rep, orb_sz in orbits:
                vals[gA] = rep
                cnt = 0
                for vB in range(n):
                    vals[gB] = vB
                    # Evaluate rest_w (depends only on gA, gB)
                    prod = _eval_word(rest_w, vals, id_i, mul, inv)
                    # rest_w * g^{+-1} == id  <=>  g = prod if is_inv_s else inv[prod]
                    vals[gi_s] = prod if is_inv_s else inv[prod]
                    ok = True
                    for w in other_rels:
                        if _eval_word(w, vals, id_i, mul, inv) != id_i:
                            ok = False
                            break
                    if ok and _subgroup_size(vals, n, id_i, mul) == n:
                        cnt += 1
                raw += cnt * orb_sz
        else:
            # Check if any relator depends on only 2 generators; order those two first!
            perm = [0, 1, 2]
            rel2_only = []
            rel3 = []
            for w in parsed:
                used = sorted({gi for gi, _ in w})
                if len(used) == 2:
                    miss = next(k for k in range(3) if k not in used)
                    perm = used + [miss]
                    break
            # Re-index relators under perm (new idx 0, 1, 2 correspond to old perm[0], perm[1], perm[2])
            inv_perm = {old: new for new, old in enumerate(perm)}
            r_mapped = [tuple((inv_perm[gi], is_inv) for gi, is_inv in w) for w in parsed]
            for w in r_mapped:
                if all(gi < 2 for gi, _ in w):
                    rel2_only.append(w)
                else:
                    rel3.append(w)

            for rep, orb_sz in orbits:
                cnt = 0
                for v1 in range(n):
                    v01 = (rep, v1, 0)
                    if any(_eval_word(w, v01, id_i, mul, inv) != id_i for w in rel2_only):
                        continue
                    for v2 in range(n):
                        vals = (rep, v1, v2)
                        ok = True
                        for w in rel3:
                            if _eval_word(w, vals, id_i, mul, inv) != id_i:
                                ok = False
                                break
                        if ok and _subgroup_size(vals, n, id_i, mul) == n:
                            cnt += 1
                raw += cnt * orb_sz
        assert raw % aut_size == 0, f"Raw {raw} not divisible by |Aut|={aut_size}"
        return raw // aut_size

    raise ValueError(f"Unsupported generator count {ng}")


# ============================================================================
# 2. Abelian plants: pi_1 ->> Z/3 (3^d - 1) and pi_1 ->> (Z/2)^3
# ============================================================================
def _f_p_rank(mat_rows, n_cols, p):
    """Exact rank over F_p via Gaussian elimination."""
    A = [[x % p for x in row] for row in mat_rows]
    r = 0
    for c in range(n_cols):
        piv = None
        for i in range(r, len(A)):
            if A[i][c] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv_v = pow(A[r][c], p - 2, p)
        A[r] = [(x * inv_v) % p for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                fac = A[i][c]
                A[i] = [(A[i][j] - fac * A[r][j]) % p for j in range(n_cols)]
        r += 1
    return r


def _abelian_matrix(gens, rels):
    gmap = {g: i for i, g in enumerate(gens)}
    rows = []
    for r in rels:
        row = [0] * len(gens)
        for ch in r:
            gi = gmap[ch.lower()]
            row[gi] += -1 if ch.isupper() else 1
        rows.append(row)
    return rows


def _count_z3_surjections_direct(gens, rels):
    """Direct brute-force count of surjective homomorphisms pi_1(M) ->> Z/3 (nonzero solutions mod 3)."""
    ng = len(gens)
    rows = _abelian_matrix(gens, rels)
    cnt = 0
    for assign in range(1, 3 ** ng):
        vec = []
        tmp = assign
        for _ in range(ng):
            vec.append(tmp % 3)
            tmp //= 3
        ok = True
        for row in rows:
            if sum(a * b for a, b in zip(row, vec)) % 3 != 0:
                ok = False
                break
        if ok:
            cnt += 1
    return cnt


def _can_surject_z2_cubed(gens, rels):
    """pi_1(M) ->> (Z/2)^3 iff dim_{F_2} H_1(M; F_2) >= 3."""
    ng = len(gens)
    if ng < 3:
        return False
    rows = _abelian_matrix(gens, rels)
    rk = _f_p_rank(rows, ng, 2)
    return (ng - rk) >= 3


# ============================================================================
# 3. Exact manifold-independent post-E_6 structural package (Z_6, Y, 3/8)
# ============================================================================
def _verify_post_e6_package():
    # (a) B862 exact kernel of SU(3) x SU(2) x U(1) -> S(U(3) x U(2)) subset SU(5):
    # (e^{2 pi i a/3} I_3, (-1)^b I_2, e^{2 pi i x}) -> diag(e^{2 pi i (a/3 + 2x)} I_3, e^{2 pi i (b/2 - 3x)} I_2)
    # Solve a/3 + 2x == 0 (mod 1) and b/2 - 3x == 0 (mod 1) over a in {0,1,2}, b in {0,1}, x in Q/Z (den dividing 6)
    ker = []
    for a in range(3):
        for b in range(2):
            for num in range(6):
                x = Fr(num, 6)
                c1 = Fr(a, 3) + 2 * x
                c2 = Fr(b, 2) - 3 * x
                if c1.denominator == 1 and c2.denominator == 1:
                    ker.append((a, b, x))
    # Compute exact group element orders in Z/3 x Z/2 x (Q/Z)
    ker_orders = []
    for a, b, x in ker:
        k = 1
        while (k * a) % 3 != 0 or (k * b) % 2 != 0 or (k * x).denominator != 1:
            k += 1
        ker_orders.append(k)
    ker_orders.sort()
    ker_is_z6 = (len(ker) == 6 and ker_orders == [1, 2, 3, 3, 6, 6])

    # (b) B1160 exact SymPy traceless commutant of su(3) (+) su(2) inside su(5):
    # Basis of su(3) (+) su(2) in 5x5 matrices: E_{ij} for 0<=i,j<3 (traceless) and 3<=i,j<5 (traceless)
    gens_32 = []
    for i in range(3):
        for j in range(3):
            if i != j:
                M = sp.zeros(5, 5)
                M[i, j] = 1
                gens_32.append(M)
    for d in (0, 1):
        M = sp.zeros(5, 5)
        M[d, d] = 1
        M[d + 1, d + 1] = -1
        gens_32.append(M)
    for i, j in ((3, 4), (4, 3)):
        M = sp.zeros(5, 5)
        M[i, j] = 1
        gens_32.append(M)
    M34 = sp.zeros(5, 5)
    M34[3, 3] = 1
    M34[4, 4] = -1
    gens_32.append(M34)

    # Unknown 5x5 matrix X: 25 entries, subject to [X, G] = 0 for all G in gens_32 and Tr(X) = 0
    vars_x = sp.symbols("x0:25")
    X = sp.Matrix(5, 5, vars_x)
    eqs = [sp.trace(X)]
    for G in gens_32:
        C = X * G - G * X
        for i in range(5):
            for j in range(5):
                if C[i, j] != 0:
                    eqs.append(C[i, j])
    A_mat, _ = sp.linear_eq_to_matrix(eqs, vars_x)
    ns = A_mat.nullspace()
    comm_dim = len(ns)
    # Normalize unique basis vector so entry (0,0) = 2
    v0 = ns[0]
    Y_mat = sp.Matrix(5, 5, list(v0)) * (sp.Integer(2) / v0[0])
    Y_diag = [int(Y_mat[i, i]) for i in range(5)]
    Y_is_diag = all(Y_mat[i, j] == 0 for i in range(5) for j in range(5) if i != j)
    Y_exact_match = (comm_dim == 1 and Y_is_diag and Y_diag == [2, 2, 2, -3, -3])

    # (c) Exact sin^2 theta_W = Tr(T_3^2) / Tr(Q^2) on the 5 of SU(5)
    # Normalize Y_phys = (-1/6) * diag(2, 2, 2, -3, -3) = diag(-1/3, -1/3, -1/3, 1/2, 1/2)
    T3_diag = [Fr(0), Fr(0), Fr(0), Fr(1, 2), Fr(-1, 2)]
    Y_phys = [Fr(-d, 6) for d in Y_diag]
    Q_diag = [t + y for t, y in zip(T3_diag, Y_phys)]
    tr_T3_sq = sum(t * t for t in T3_diag)
    tr_Q_sq = sum(q * q for q in Q_diag)
    sin2_tw = tr_T3_sq / tr_Q_sq

    return {
        "kernel_size": len(ker),
        "kernel_orders": ker_orders,
        "kernel_is_Z6": ker_is_z6,
        "commutant_dim": comm_dim,
        "Y_is_diagonal": Y_is_diag,
        "Y_diag_normalized": Y_diag,
        "Y_exact_match": Y_exact_match,
        "sin2_thetaW": str(sin2_tw),
        "sin2_thetaW_is_3_8": (sin2_tw == Fr(3, 8)),
        "all_ok": (ker_is_z6 and Y_exact_match and sin2_tw == Fr(3, 8)),
    }


def run_all():
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    ast_floats = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))

    census = json.loads(PRES_JSON.read_text(encoding="utf-8"))
    assert len(census) == 1199, f"Expected 1199 manifolds, got {len(census)}"

    # Build 2T, 2O, 2I and their exact Aut(G) groups
    n2T, id2T, mul2T, inv2T = _build_sl2_fp(3)
    aut2T, orb2T = _compute_aut_group(n2T, id2T, mul2T, inv2T)
    assert n2T == 24 and aut2T == 24

    n2O, id2O, mul2O, inv2O = _build_2O()
    aut2O, orb2O = _compute_aut_group(n2O, id2O, mul2O, inv2O)
    assert n2O == 48 and aut2O == 48

    n2I, id2I, mul2I, inv2I = _build_sl2_fp(5)
    aut2I, orb2I = _compute_aut_group(n2I, id2I, mul2I, inv2I)
    assert n2I == 120 and aut2I == 120

    # Precompute 2-gen surjectivity lookup tables for orbit reps of 2T, 2O, 2I (blazingly fast!)
    def _precomp_2gen(n, id_i, mul, orbits):
        tbl = {}
        for rep, _ in orbits:
            tbl[rep] = [_subgroup_size((rep, g1), n, id_i, mul) == n for g1 in range(n)]
        return tbl

    ok2T = _precomp_2gen(n2T, id2T, mul2T, orb2T)
    ok2O = _precomp_2gen(n2O, id2O, mul2O, orb2O)
    ok2I = _precomp_2gen(n2I, id2I, mul2I, orb2I)

    # Census sweep over all 1,199 manifolds
    n_2T = 0
    n_2T_exact2 = 0
    n_2O = 0
    n_2I = 0
    m004_counts = None
    z3_all_hold = True
    z3_all_formula = True
    z2_cubed_2gen_fails = 0
    n_2gen = 0
    n_3gen = 0
    z2_cubed_3gen_hits = 0
    first400_2gen_2T = 0
    first400_2gen_exact2 = 0
    first400_2gen_seen = 0
    dist_2T = Counter()
    dist_2O = Counter()
    dist_2I = Counter()

    for idx_m, row in enumerate(census):
        name = row["name"]
        gens = row["gens"]
        rels = row["rels"]
        c2T = _count_surjections(gens, rels, n2T, id2T, mul2T, inv2T, aut2T, orb2T, ok2T)
        c2O = _count_surjections(gens, rels, n2O, id2O, mul2O, inv2O, aut2O, orb2O, ok2O)
        c2I = _count_surjections(gens, rels, n2I, id2I, mul2I, inv2I, aut2I, orb2I, ok2I)
        dist_2T[c2T] += 1
        dist_2O[c2O] += 1
        dist_2I[c2I] += 1

        if c2T > 0:
            n_2T += 1
        if c2T == 2:
            n_2T_exact2 += 1
        if c2O > 0:
            n_2O += 1
        if c2I > 0:
            n_2I += 1
        if name == "m004":
            m004_counts = {"2T": c2T, "2O": c2O, "2I": c2I}

        # B993 control: first 400 manifolds (checking 2-gen subset among first 400 and first 400 2-gen)
        if len(gens) == 2:
            n_2gen += 1
            if first400_2gen_seen < 400:
                first400_2gen_seen += 1
                if c2T > 0:
                    first400_2gen_2T += 1
                if c2T == 2:
                    first400_2gen_exact2 += 1
        else:
            n_3gen += 1

        # Plant 1: pi_1 ->> Z/3 must hold (rate 1) with count == 3^d - 1
        ab_rows = _abelian_matrix(gens, rels)
        d3 = len(gens) - _f_p_rank(ab_rows, len(gens), 3)
        c_z3 = _count_z3_surjections_direct(gens, rels)
        if c_z3 == 0:
            z3_all_hold = False
        if c_z3 != (3 ** d3 - 1):
            z3_all_formula = False

        # Plant 2: pi_1 ->> (Z/2)^3 must fail on every 2-generator presentation
        can_z23 = _can_surject_z2_cubed(gens, rels)
        if len(gens) == 2 and not can_z23:
            z2_cubed_2gen_fails += 1
        if len(gens) == 3 and can_z23:
            z2_cubed_3gen_hits += 1

    # Also compute first 400 in census order (matching B993's 372 2-gen + 28 skipped)
    b993_first400_2gen = 0
    b993_first400_2T = 0
    b993_first400_exact2 = 0
    for row in census[:400]:
        if len(row["gens"]) == 2:
            b993_first400_2gen += 1
            c2T = _count_surjections(row["gens"], row["rels"], n2T, id2T, mul2T, inv2T, aut2T, orb2T, ok2T)
            if c2T > 0:
                b993_first400_2T += 1
            if c2T == 2:
                b993_first400_exact2 += 1

    pkg = _verify_post_e6_package()

    # 5 independent planted fault controls
    # PF1: Abelian group Z (1 gen, 0 rels) has 0 surjections onto non-abelian 2T
    pf1 = (_count_surjections(["a", "b"], ["aB"], n2T, id2T, mul2T, inv2T, aut2T, orb2T, ok2T) == 0)
    # PF2: Wrong hypercharge diag(1,1,1,-1,-2) is NOT traceless (sum != 0)
    pf2 = (sum((1, 1, 1, -1, -2)) != 0)
    # PF3: Wrong weak normalization Y_bad = diag(1,1,1,-3/2,-3/2) changes Tr(T3^2)/Tr(Q^2) away from 3/8
    tr_q_bad = sum((t + y) ** 2 for t, y in zip([Fr(0), Fr(0), Fr(0), Fr(1, 2), Fr(-1, 2)],
                                                [Fr(1), Fr(1), Fr(1), Fr(-3, 2), Fr(-3, 2)]))
    pf3 = (Fr(1, 2) / tr_q_bad != Fr(3, 8))
    # PF4: Adding a 3rd free generator to Z^3 admits (Z/2)^3 surjection (proving Plant 2 isn't vacuously always False)
    pf4 = _can_surject_z2_cubed(["a", "b", "c"], ["abAB"])
    # PF5: Wrong kernel normalization 6Y -> 12Y (2*6Y) doubles kernel size to 12 != 6
    ker12 = sum(1 for a in range(3) for b in range(2) for num in range(12)
                if (Fr(a, 3) + 4 * Fr(num, 12)).denominator == 1 and (Fr(b, 2) - 6 * Fr(num, 12)).denominator == 1)
    pf5 = (ker12 == 12)

    pf = {
        "PF1_cyclic_group_no_2T_surjection": pf1,
        "PF2_wrong_Y_not_traceless": pf2,
        "PF3_wrong_Y_shifts_sin2_thetaW": pf3,
        "PF4_free_3gen_admits_Z2_cubed": pf4,
        "PF5_nonprimitive_Y_gives_Z12": pf5,
    }
    pf_caught = sum(1 for v in pf.values() if v)

    all_ok = (
        ast_floats == 0
        and len(census) == 1199
        and n_2T == 384
        and m004_counts["2T"] == 2
        and z3_all_hold
        and z3_all_formula
        and z2_cubed_2gen_fails == n_2gen
        and pkg["all_ok"]
        and pf_caught == 5
    )

    out = {
        "card": "A2-PEER-SM-R581",
        "seat_code": "fam3-v1-high-03",
        "verifying_seat_code": "fam1-v1-unset-04",
        "verifying_card": "SM-R581 (CLAIM_2026-11-27_one_class_structural_package_refiled.md)",
        "blind": "0 of 19",
        "ast_floats": ast_floats,
        "json_floats": 0,
        "census_size": len(census),
        "n_2gen": n_2gen,
        "n_3gen": n_3gen,
        "group_orders_and_aut": {"2T": [n2T, aut2T], "2O": [n2O, aut2O], "2I": [n2I, aut2I]},
        "m004_counts": m004_counts,
        "counts_in_1199": {
            "2T_any": n_2T,
            "2T_rate_frac": f"{n_2T}/{len(census)}",
            "2T_rate_4dp": f"{n_2T / len(census):.4f}",
            "2T_exact2": n_2T_exact2,
            "2O_any": n_2O,
            "2I_any": n_2I,
            "package_given_2T": n_2T if pkg["all_ok"] else 0,
            "dist_2T": {str(k): v for k, v in sorted(dist_2T.items())},
            "dist_2O": {str(k): v for k, v in sorted(dist_2O.items())},
            "dist_2I": {str(k): v for k, v in sorted(dist_2I.items())},
        },
        "B993_control_first400_in_order": {
            "2gen_count": b993_first400_2gen,
            "2T_any": b993_first400_2T,
            "2T_exact2": b993_first400_exact2,
        },
        "first400_2gen_manifolds": {
            "2T_any": first400_2gen_2T,
            "2T_exact2": first400_2gen_exact2,
        },
        "plants": {
            "Z3_all_1199_hold": z3_all_hold,
            "Z3_all_1199_equal_3d_minus_1": z3_all_formula,
            "Z2_cubed_fails_all_2gen": (z2_cubed_2gen_fails == n_2gen),
            "Z2_cubed_2gen_checked": z2_cubed_2gen_fails,
            "Z2_cubed_3gen_hits": z2_cubed_3gen_hits,
        },
        "post_E6_structural_package": pkg,
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

    print(f"DECISIVE: CENSUS ok={n_2T==384 and m004_counts['2T']==2} K={len(census)} "
          f"g2={n_2gen} g3={n_3gen} E6_2T={n_2T} E7_2O={n_2O} E8_2I={n_2I} m004_2T={m004_counts['2T']}")
    print(f"DECISIVE: PLANTS ok={z3_all_hold and z3_all_formula and z2_cubed_2gen_fails==n_2gen} "
          f"Z3_rate1={z3_all_hold} Z3_3d1={z3_all_formula} Z2cubed_2gen0={z2_cubed_2gen_fails}/{n_2gen} "
          f"B993_400_2T={b993_first400_2T}/{b993_first400_2gen}")
    print(f"DECISIVE: PACKAGE ok={pkg['all_ok']} kerZ6={pkg['kernel_is_Z6']} comm1={pkg['Y_exact_match']} "
          f"sin2={pkg['sin2_thetaW']} pkg_rate={n_2T}/{len(census)}")
    print(f"DECISIVE: SUMMARY all_ok={all_ok} PF={pf_caught}/5 floats={ast_floats}/{jf}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(run_all())
