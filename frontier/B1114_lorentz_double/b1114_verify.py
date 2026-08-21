#!/usr/bin/env python3
"""B1114 VERIFICATION BENCH -- LORENTZ ON THE DOUBLE.

Independent, own-code re-derivation of the outside-bench memo
`breakthrough_memos/LORENTZ_ON_THE_DOUBLE.md` (2026-08-21), whose canonical
computation is `lorentz_double3_out.txt` (the FAILED first method
`lorentz_double2_out.txt` is the error ledger -- its "VERIFIED" lines are
WRONG and are not reproduced here).

Convention: uses the SAME e6 Chevalley basis/bracket B1098 and B1102 use --
`frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py`, loaded via
spec_from_file_location (never re-derived with a different sign/basis
convention, since the stored triple JSON only type-checks against this one).
The stored A2 triple is `frontier/B1098_nonabelian_hatch/b1098_a2_triple.json`.

Every number in this script is EXACT (Python Fraction / sympy Rational).
Layer 4's bonus color-refinement is exact too; nothing here uses floats for
a load-bearing number (the modular-rank cross-checks use machine ints mod p,
which is also exact arithmetic, not a float approximation).

Repo is READ-ONLY; this script and its outputs live entirely in
`b1114_staging/`. Run: `python3 b1114_verify.py`.
"""
import importlib.util
import json
import os
import random
import sys
import time
from collections import Counter
from fractions import Fraction as Fr

import sympy as sp

REPO_ROOT = os.environ.get("B1114_REPO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VENDORED = os.path.join(REPO_ROOT, "frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py")
A2_TRIPLE_JSON = os.path.join(REPO_ROOT, "frontier/B1098_nonabelian_hatch/b1098_a2_triple.json")
B1098_RESULTS_JSON = os.path.join(REPO_ROOT, "frontier/B1098_nonabelian_hatch/b1098_results.json")

HERE = os.path.dirname(os.path.abspath(__file__))
PRIMES = [1000003, 1000033]

T0 = time.time()
LOG = []


def log(msg):
    line = f"[{time.time()-T0:7.2f}s] {msg}"
    print(line, flush=True)
    LOG.append(line)


# ================================================================== helpers
def load_e6b():
    spec = importlib.util.spec_from_file_location("e6b_b1114", VENDORED)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def add(u, v):
    return [a + b for a, b in zip(u, v)]


def sub(u, v):
    return [a - b for a, b in zip(u, v)]


def smul(c, u):
    return [Fr(c) * a for a in u]


def is_zero(v):
    return all(x == 0 for x in v)


def veq(u, v):
    return all(a == b for a, b in zip(u, v))


def sprat(x):
    """Any numeric (Fraction/int/sp.Rational) -> exact sp.Rational."""
    if isinstance(x, Fr):
        return sp.Rational(x.numerator, x.denominator)
    return sp.Rational(x)


def frac(x):
    """Any numeric -> exact Python Fraction."""
    r = sprat(x)
    return Fr(int(r.p), int(r.q))


def to_sp_vec(v):
    return sp.Matrix([sprat(c) for c in v])


def sp_col_to_frac(col, n=None):
    n = n if n is not None else col.shape[0]
    return [frac(col[i]) for i in range(n)]


def modular_rank(rows, ncols, p):
    """Exact-rational matrix (list of rows of Fraction/int/sp.Rational) -> rank mod p."""
    def to_mod(x):
        r = sprat(x)
        num, den = int(r.p) % p, int(r.q) % p
        return (num * pow(den, p - 2, p)) % p

    M = [[to_mod(x) for x in row] for row in rows]
    nrows = len(M)
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if M[i][c] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(nrows):
            if i != r and M[i][c] % p != 0:
                f_ = M[i][c]
                M[i] = [(x - f_ * y) % p for x, y in zip(M[i], M[r])]
        r += 1
        if r == nrows:
            break
    return r


# ============================================================== main script
def main():
    R = {}  # results dict, written to b1114_results.json

    # ---------------------------------------------------------- load e6
    log("loading the vendored e6 bracket module (B1098/B1102's convention)")
    e6b = load_e6b()
    ROOTS, IDX, N, DIM = e6b.ROOTS, e6b.IDX, e6b.N, e6b.DIM
    br, evec, hvec, ip, eps = e6b.br, e6b.evec, e6b.hvec, e6b.ip, e6b.eps
    log(f"  e6 loaded: {len(ROOTS)} roots, dim {DIM}")
    assert len(ROOTS) == 72 and DIM == 78
    SIMPLE = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]

    def ad_matrix(Z):
        cols = []
        for i in range(DIM):
            ei = [Fr(0)] * DIM
            ei[i] = Fr(1)
            img = br(Z, ei)
            cols.append([sprat(c) for c in img])
        return sp.Matrix(cols).T

    def centralizer(vecs):
        """{v : [z,v]=0 for all z in vecs}, exact nullspace, plus the stacked matrix."""
        S = sp.Matrix.vstack(*[ad_matrix(z) for z in vecs])
        ns = S.nullspace()
        return [sp_col_to_frac(c) for c in ns], S

    def modular_confirm(S, dim_claimed, label):
        for p in PRIMES:
            rk = modular_rank([[S[i, j] for j in range(DIM)] for i in range(S.rows)], DIM, p)
            nulmod = DIM - rk
            ok = nulmod == dim_claimed
            log(f"    modular cross-check p={p} [{label}]: nullity={nulmod} {'OK' if ok else 'MISMATCH!'}")
            assert ok, f"{label}: modular mismatch at p={p}"

    # ---------------------------------------------------------- load stored hatch triple
    log("loading B1098's stored A2-class hatch triple")
    trip = json.load(open(A2_TRIPLE_JSON))
    dec = lambda lst: [Fr(a, b) for a, b in lst]
    X, H, Y = dec(trip["X"]), dec(trip["H"]), dec(trip["Y"])
    stored_dimc = trip["dim_c"]
    log(f"  stored dim_c = {stored_dimc}")

    ok_XY = veq(br(X, Y), H)
    ok_HX = veq(br(H, X), smul(2, X))
    ok_HY = veq(br(H, Y), smul(-2, Y))
    log(f"  hatch triple relations exact: [X,Y]=H {ok_XY}, [H,X]=2X {ok_HX}, [H,Y]=-2Y {ok_HY}")
    assert ok_XY and ok_HX and ok_HY

    hatch_nodes = None
    for i in range(N):
        for j in range(i + 1, N):
            if veq(add(evec(SIMPLE[i]), evec(SIMPLE[j])), X):
                hatch_nodes = (i, j)
    log(f"  hatch X identified as Levi{hatch_nodes}-regular (own search, not assumed)")
    assert hatch_nodes == (0, 2), f"unexpected hatch nodes {hatch_nodes} -- stop and inspect"

    R["setup"] = {"stored_dim_c": stored_dimc, "hatch_levi_nodes": list(hatch_nodes),
                  "triple_relations_exact": bool(ok_XY and ok_HX and ok_HY)}

    # =====================================================================
    # LAYER 2 -- CONTROL: reproduce B1098's dim_c=16 with OWN centralizer code
    # =====================================================================
    log("")
    log("=== CONTROL: z_e6(hatch triple) via own ad-matrix nullspace ===")
    c_basis, S_c = centralizer([X, H, Y])
    dim_c_direct = len(c_basis)
    log(f"  dim z_e6(X,H,Y) [own code] = {dim_c_direct}  (B1098 banked / stored triple: {stored_dimc})")
    assert dim_c_direct == 16 == stored_dimc
    modular_confirm(S_c, dim_c_direct, "control z(hatch triple)")

    b1098_table = json.load(open(B1098_RESULTS_JSON))
    a2a2_rows = [r for r in b1098_table if r.get("ss_type") == "a2+a2"]
    dimc_values_in_table = sorted(set(r["dim_c"] for r in b1098_table))
    log(f"  B1098 table row(s) tagged 'a2+a2': {a2a2_rows}")
    log(f"  B1098 table's full dim_c value set: {dimc_values_in_table}")
    control_pass = (dim_c_direct == 16 and len(a2a2_rows) == 1 and a2a2_rows[0]["dim_c"] == 16)
    log(f"  CONTROL PASS: {control_pass}")
    assert control_pass
    R["control"] = {"dim_c_direct": dim_c_direct, "b1098_a2a2_row": a2a2_rows,
                     "b1098_dimc_value_set": dimc_values_in_table, "pass": control_pass}

    # =====================================================================
    # LAYER 2a -- the A2+A2 orthogonal subsystem and the two ideals
    # =====================================================================
    log("")
    log("=== the roots orthogonal to the hatch A2 -> A2+A2 -> I1, I2 ===")
    a_i, a_j = SIMPLE[hatch_nodes[0]], SIMPLE[hatch_nodes[1]]
    orth_roots = [r for r in ROOTS if ip(r, a_i) == 0 and ip(r, a_j) == 0]
    log(f"  roots orthogonal to the A2: {len(orth_roots)} (expect 12)")
    assert len(orth_roots) == 12

    def components(roots_list):
        remaining = set(roots_list)
        comps = []
        while remaining:
            seed = next(iter(remaining))
            comp = {seed}
            frontier = [seed]
            remaining.discard(seed)
            while frontier:
                r = frontier.pop()
                for s in list(remaining):
                    if ip(r, s) != 0:
                        comp.add(s)
                        remaining.discard(s)
                        frontier.append(s)
            comps.append(sorted(comp))
        return comps

    comps = components(orth_roots)
    sizes = sorted(len(c) for c in comps)
    log(f"  orthogonal-subsystem components: {sizes} (expect [6, 6])")
    assert sizes == [6, 6]
    comp1, comp2 = comps
    cross_ok = all(ip(r, s) == 0 for r in comp1 for s in comp2)
    log(f"  full cross-component orthogonality (all 36 pairs): {cross_ok}")
    assert cross_ok

    def find_simple_pair(comp):
        for r1 in comp:
            for r2 in comp:
                if r1 == r2:
                    continue
                if ip(r1, r2) == -1:
                    s = tuple(a + b for a, b in zip(r1, r2))
                    if s in comp:
                        return r1, r2
        raise RuntimeError("no simple pair found in component")

    def build_ideal(comp, label):
        r1, r2 = find_simple_pair(comp)
        root_vecs = [evec(r) for r in comp]
        h1c = br(evec(r1), evec(tuple(-x for x in r1)))
        h2c = br(evec(r2), evec(tuple(-x for x in r2)))
        basis = root_vecs + [h1c, h2c]
        M = sp.Matrix([[sprat(c) for c in v] for v in basis])
        rk = M.rank()
        log(f"  ideal {label}: dim(span) = {rk} (expect 8); simple pair {r1, r2}")
        return basis, rk, (r1, r2), (h1c, h2c)

    I1_basis, I1_rank, I1_simple, I1_coroots = build_ideal(comp1, "I1")
    I2_basis, I2_rank, I2_simple, I2_coroots = build_ideal(comp2, "I2")
    assert I1_rank == 8 and I2_rank == 8

    def all_cross_zero(bA, bB):
        return all(is_zero(br(a, b)) for a in bA for b in bB)

    I1I2_commute = all_cross_zero(I1_basis, I2_basis)
    log(f"  [I1,I2]=0 (all 64 cross pairs): {I1I2_commute}")
    assert I1I2_commute

    def commutes_with_triple(basis, Xv, Hv, Yv):
        return all(is_zero(br(v, Xv)) and is_zero(br(v, Hv)) and is_zero(br(v, Yv)) for v in basis)

    I1_comm_hatch = commutes_with_triple(I1_basis, X, H, Y)
    I2_comm_hatch = commutes_with_triple(I2_basis, X, H, Y)
    log(f"  [I1,hatch triple]=0: {I1_comm_hatch}   [I2,hatch triple]=0: {I2_comm_hatch}")
    assert I1_comm_hatch and I2_comm_hatch

    combined = I1_basis + I2_basis
    Mc = sp.Matrix([[sprat(c) for c in v] for v in combined])
    rank_combined = Mc.rank()
    log(f"  rank(I1 union I2) = {rank_combined} (expect 16 = 8+8, i.e. a direct sum)")
    assert rank_combined == 16
    log("  I1 (+) I2 verified to EQUAL z_e6(hatch triple) exactly (same dim 16, "
        "contained by the commuting check above => equality)")

    rationality_ok = all(isinstance(x, Fr) for v in combined for x in v)
    log(f"  Q-rationality: every I1/I2 basis-vector entry is an exact Fraction: {rationality_ok}")
    assert rationality_ok

    R["layer2a_orthogonal_subsystem"] = {
        "n_orthogonal_roots": len(orth_roots), "component_sizes": sizes,
        "cross_orthogonal": cross_ok, "I1_dim": I1_rank, "I2_dim": I2_rank,
        "I1_simple_pair": [list(I1_simple[0]), list(I1_simple[1])],
        "I2_simple_pair": [list(I2_simple[0]), list(I2_simple[1])],
        "I1_I2_commute": I1I2_commute, "I1_commutes_hatch": I1_comm_hatch,
        "I2_commutes_hatch": I2_comm_hatch, "rank_I1_plus_I2": rank_combined,
        "I1_plus_I2_equals_centralizer": (rank_combined == 16 == dim_c_direct),
        "Q_rational": rationality_ok,
    }

    # =====================================================================
    # LAYER 2a(cont) -- I1's principal JM triple
    # =====================================================================
    log("")
    log("=== I1's principal JM triple (e2,h2,f2), general ad^2 solver ===")

    def jm_triple_general(Xv, label=""):
        adX = ad_matrix(Xv)
        ad2 = adX * adX
        target = -2 * to_sp_vec(Xv)
        sol = ad2.gauss_jordan_solve(target)[0]
        free = sol.free_symbols
        if free:
            sol = sol.subs({s: 0 for s in free})
        resid = ad2 * sol - target
        assert all(sp.simplify(v) == 0 for v in resid), f"[{label}] ad^2 f=-2X unsolvable"
        Yv = sp_col_to_frac(sol)
        Hv = br(Xv, Yv)
        assert veq(br(Hv, Xv), smul(2, Xv)), f"[{label}] [H,X] != 2X"
        HY = br(Hv, Yv)
        if not veq(HY, smul(-2, Yv)):
            adH = ad_matrix(Hv)
            Madj = adH + 2 * sp.eye(DIM)
            rhs = to_sp_vec(HY) + 2 * to_sp_vec(Yv)
            kerX = adX.nullspace()
            assert kerX, f"[{label}] correction impossible: ker(adX) trivial"
            Kb = sp.Matrix.hstack(*kerX)
            csol = (Madj * Kb).gauss_jordan_solve(rhs)[0]
            cfree = csol.free_symbols
            if cfree:
                csol = csol.subs({s: 0 for s in cfree})
            Yv = sp_col_to_frac(to_sp_vec(Yv) - Kb * csol)
            Hv = br(Xv, Yv)
            assert veq(br(Hv, Yv), smul(-2, Yv)), f"[{label}] correction failed"
            log(f"    [{label}] required the ker(adX) correction step")
        return Xv, Hv, Yv

    r1, r2 = I1_simple
    e2 = add(evec(r1), evec(r2))
    e2v, h2v, f2v = jm_triple_general(e2, "I1-principal")
    ok2 = (veq(br(e2v, f2v), h2v) and veq(br(h2v, e2v), smul(2, e2v))
           and veq(br(h2v, f2v), smul(-2, f2v)))
    log(f"  (e2,h2,f2) exact sl2 relations: [e2,f2]=h2, [h2,e2]=2e2, [h2,f2]=-2f2 : {ok2}")
    assert ok2

    commutes9 = all(is_zero(br(v, w)) for v in (e2v, h2v, f2v) for w in (X, H, Y))
    log(f"  I1's triple commutes with hatch's stored triple (9 brackets exactly 0): {commutes9}")
    assert commutes9

    R["layer2b_principal_triple"] = {
        "relations_exact": ok2, "commutes_with_hatch_9_brackets": commutes9,
        "e2": [[c.numerator, c.denominator] for c in e2v],
        "h2": [[c.numerator, c.denominator] for c in h2v],
        "f2": [[c.numerator, c.denominator] for c in f2v],
    }

    # =====================================================================
    # LAYER 2c -- same nilpotent class
    # =====================================================================
    log("")
    log("=== same-class checks (I1's principal vs the hatch's own A2) ===")
    c2_basis, S_c2 = centralizer([e2v, h2v, f2v])
    dim_c2 = len(c2_basis)
    log(f"  dim z_e6(e2,h2,f2) [reductive, B1098-style] = {dim_c2} (hatch's own: 16)")
    modular_confirm(S_c2, dim_c2, "z(I1 principal triple)")
    same_class_reductive = (dim_c2 == 16)
    log(f"  reductive-centralizer-dim match (B1098's own class-key component): {same_class_reductive}")

    def cartan_spectrum(hv):
        spec = [0] * N
        for r in ROOTS:
            val = br(hv, evec(r))[N + IDX[r]]
            spec.append(int(val))
        return tuple(sorted(spec))

    specH = cartan_spectrum(H)
    spec_h2 = cartan_spectrum(h2v)
    spectrum_match = specH == spec_h2
    log(f"  ad(H) spectrum == ad(h2) spectrum (B1098's other class-key component): {spectrum_match}")
    log(f"    spectrum (both, sorted 78 eigenvalues): {specH}")
    assert spectrum_match
    same_class_by_b1098_key = same_class_reductive and spectrum_match
    log(f"  SAME CLASS by B1098's ACTUAL (dim_c, ad-h spectrum) key: {same_class_by_b1098_key}")
    assert same_class_by_b1098_key

    def nilpositive_centralizer_dim(ev, label):
        adE = ad_matrix(ev)
        ns = adE.nullspace()
        d = len(ns)
        for p in PRIMES:
            rk = modular_rank([[adE[i, j] for j in range(DIM)] for i in range(DIM)], DIM, p)
            nulmod = DIM - rk
            assert nulmod == d, f"{label}: modular mismatch for nilpositive centralizer"
        return d

    dim_zX = nilpositive_centralizer_dim(X, "z(X)")
    dim_ze2 = nilpositive_centralizer_dim(e2v, "z(e2)")
    log(f"  dim z_e6(X)  [nilpositive of hatch ALONE, not the reductive triple-centralizer] = {dim_zX}")
    log(f"  dim z_e6(e2) [nilpositive of I1's principal ALONE]                              = {dim_ze2}")
    nilpositive_match = (dim_zX == dim_ze2)
    log(f"  dim z_e6(X) == dim z_e6(e2): {nilpositive_match}  (second, independent same-orbit invariant)")
    assert nilpositive_match

    memo_claims_36 = (dim_ze2 == 36)
    table_has_36 = 36 in dimc_values_in_table
    log(f"  memo's claimed value 'dim z_e6(e2)=36': matches our computation? {memo_claims_36}")
    log(f"  Is 36 anywhere in B1098's own dim_c table? {table_has_36} "
        f"(that table's dim_c column is the REDUCTIVE triple-centralizer, "
        f"max value {max(dimc_values_in_table)}; 36 is a DIFFERENT invariant -- "
        f"dim z_g(nilpositive alone) -- not tabulated by B1098 at all)")

    R["layer2c_same_class"] = {
        "dim_c2_reductive": dim_c2, "same_class_reductive_dim": same_class_reductive,
        "adh_spectrum_match": spectrum_match, "same_class_by_b1098_key": same_class_by_b1098_key,
        "dim_z_nilpositive_X": dim_zX, "dim_z_nilpositive_e2": dim_ze2,
        "nilpositive_dims_match": nilpositive_match,
        "memo_36_matches_computation": memo_claims_36,
        "b1098_table_contains_36": table_has_36,
        "note": ("The memo's 'dim z_e6(e2)=36 (A2 class <=> 36)' cites B1098's dim-c table as "
                 "the source, but B1098's table (checked programmatically above) contains no "
                 "value 36 -- its dim_c column is the REDUCTIVE centralizer of the whole triple "
                 "(max 35, the a5/minimal-orbit row), not the centralizer of the nilpositive "
                 "alone. The underlying 'same class' CLAIM is nonetheless correct and is "
                 "confirmed here by two independent, properly-sourced invariants: (1) B1098's "
                 "actual class key (dim_c=16 + matching ad-h spectrum, both exact matches), and "
                 "(2) an equal-but-different invariant dim z_g(nilpositive alone), which we "
                 "compute fresh for BOTH X and e2 and find equal (36 each) -- so 36 is a real, "
                 "verifiable fact about this orbit, just mis-cited as living in B1098's table."),
    }

    # =====================================================================
    # LAYER 2d -- THE CRUX: the joint centralizer
    # =====================================================================
    log("")
    log("=== LAYER 2d (the crux): joint centralizer of the two commuting A2 triples ===")
    joint_basis, S_joint = centralizer([X, H, Y, e2v, h2v, f2v])
    dim_joint = len(joint_basis)
    log(f"  dim joint centralizer (own nullspace code) = {dim_joint}  (claim: 8)")
    modular_confirm(S_joint, dim_joint, "joint centralizer")
    assert dim_joint == 8

    # theoretical cross-check: principal sl2 of a simple algebra has TRIVIAL reductive
    # centralizer WITHIN that algebra (standard fact -- matches B1098's own
    # Levi(0,1,2,3,4,5)-regular [full e6 principal] row: dim_c=0). Since I1, I2 commute
    # entirely, z_{I1+I2}(I1's triple) = z_{I1}(triple) (+) z_{I2}(triple) = 0 (+) I2 = I2.
    # So the joint centralizer (inside the FULL e6) should equal I2 exactly.
    union_basis = joint_basis + I2_basis
    Mu = sp.Matrix([[sprat(c) for c in v] for v in union_basis])
    rank_union = Mu.rank()
    joint_equals_I2 = (rank_union == 8)
    log(f"  theory check: joint centralizer should equal I2 EXACTLY (principal-sl2-of-I1 has "
        f"trivial centralizer WITHIN I1, so only I2 survives). rank(joint_basis U I2_basis) = "
        f"{rank_union} (expect 8, proving equality since both individually already span dim 8): "
        f"{joint_equals_I2}")
    assert joint_equals_I2

    Mjoint = sp.Matrix([[sprat(c) for c in v] for v in joint_basis])
    rank_joint_basis = Mjoint.rank()
    assert rank_joint_basis == dim_joint

    def in_span_rows(vec, Mrows, base_rank):
        M2 = Mrows.col_join(sp.Matrix([[sprat(c) for c in vec]]))
        return M2.rank() == base_rank

    closure_ok = True
    npairs = 0
    for i in range(len(joint_basis)):
        for j in range(i + 1, len(joint_basis)):
            npairs += 1
            w = br(joint_basis[i], joint_basis[j])
            if not in_span_rows(w, Mjoint, rank_joint_basis):
                closure_ok = False
    log(f"  joint centralizer closes under bracket ({npairs} pairs checked): {closure_ok}")
    assert closure_ok

    def joint_center_dim(basis):
        n = len(basis)
        BRK = [[br(basis[i], basis[j]) for j in range(n)] for i in range(n)]
        rows = []
        for j in range(n):
            for k in range(DIM):
                rows.append([sprat(BRK[i][j][k]) for i in range(n)])
        M = sp.Matrix(rows)
        ns = M.nullspace()
        return len(ns)

    center_dim = joint_center_dim(joint_basis)
    log(f"  center of the joint centralizer: dim {center_dim} (expect 0 -- simple, no abelian part)")
    assert center_dim == 0

    def reductive_rank_generic(basis, trials=6, seed=20260821):
        n = len(basis)
        rng = random.Random(seed)
        best = n
        best_kernel = None
        for _ in range(trials):
            coeffs = [rng.randint(-9, 9) or 1 for _ in range(n)]
            xg = [Fr(0)] * DIM
            for c_, b in zip(coeffs, basis):
                xg = add(xg, smul(c_, b))
            cols = [br(xg, b) for b in basis]
            Mcols = sp.Matrix([[sprat(c) for c in col] for col in cols]).T
            ns = Mcols.nullspace()
            if len(ns) < best:
                best = len(ns)
                best_kernel = (xg, ns)
        return best, best_kernel

    rank_joint_alg, _ = reductive_rank_generic(joint_basis)
    log(f"  reductive rank (generic-element method, 6 trials, min): {rank_joint_alg} (expect 2)")
    assert rank_joint_alg == 2

    joint_type = "A2 (su(3), complexified) -- the unique rank-2 dim-8 semisimple Lie algebra"
    log(f"  JOINT CENTRALIZER VERDICT: dim=8, center=0, rank=2 => {joint_type}")
    log("  E6 ⊇ (I1's A2-triple) ⊕ (hatch's A2-triple) ⊕ (this su(3)) "
        "= realified so(3,1) ⊕ su(3): Lorentz plus color, and this su(3) IS I2 exactly.")

    R["layer2d_joint_centralizer"] = {
        "dim": dim_joint, "equals_I2_exactly": joint_equals_I2, "closes_under_bracket": closure_ok,
        "center_dim": center_dim, "reductive_rank": rank_joint_alg, "type": joint_type,
        "pass": (dim_joint == 8 and center_dim == 0 and rank_joint_alg == 2 and joint_equals_I2),
    }

    # =====================================================================
    # LAYER 3 -- the signature structure (Q-rationality => no swap)
    # =====================================================================
    log("")
    log("=== LAYER 3: Q-rationality of I1, I2 and the no-swap argument ===")
    I1_rational = all(isinstance(x, Fr) for v in I1_basis for x in v)
    I2_rational = all(isinstance(x, Fr) for v in I2_basis for x in v)
    log(f"  I1 basis entirely Q-rational (exact Fraction entries, no field extension): {I1_rational}")
    log(f"  I2 basis entirely Q-rational: {I2_rational}")
    assert I1_rational and I2_rational
    dim_I1_cap_I2 = I1_rank + I2_rank - rank_combined
    log(f"  dim(I1 ∩ I2) = dim(I1)+dim(I2)-rank(I1+I2) = {I1_rank}+{I2_rank}-{rank_combined} "
        f"= {dim_I1_cap_I2} (a genuine direct sum, not merely a spanning set)")
    assert dim_I1_cap_I2 == 0

    no_swap_argument = (
        "I1 and I2 are each cut out by Q-rational linear conditions (root-vector + coroot spans "
        "in the Chevalley Q-basis) and I1 (+) I2 is a DIRECT sum (verified: dim I1 + dim I2 = "
        "rank(I1+I2), so I1 ∩ I2 = 0). Any field automorphism sigma of C/Q fixes every "
        "Q-rational vector pointwise (by definition of 'defined over Q'), hence fixes I1 and I2 "
        "SETWISE (sigma(I1)=I1, sigma(I2)=I2) rather than swapping them: if sigma swapped them, "
        "a nonzero v in I1 would have to map to sigma(v)=v (pointwise fixed) which must then also "
        "lie in I2 -- contradicting I1 ∩ I2 = 0. So no Galois twist internal to the object's "
        "own arithmetic (in particular the q -> 1-q mirror) can supply the antilinear swap that "
        "glues two same-class sl2's into so(3,1) = sl(2,C)_R; that swap is extra data -- the "
        "observer's choice of real structure, not the object's."
    )
    log("  " + no_swap_argument)
    R["layer3_rationality"] = {
        "I1_rational": I1_rational, "I2_rational": I2_rational,
        "dim_I1_cap_I2": dim_I1_cap_I2, "argument": no_swap_argument,
        "pass": I1_rational and I2_rational and dim_I1_cap_I2 == 0,
    }

    # =====================================================================
    # LAYER 1 -- the one-line lemma
    # =====================================================================
    log("")
    log("=== LAYER 1: the one-line lemma (real form vs complex subalgebra) ===")
    lemma_statement = (
        "LEMMA. Let g be a complex Lie algebra and g0 subset g a real form "
        "(g = g0 (+) i*g0 as real vector spaces). Then g0 contains no nonzero complex "
        "subalgebra of g."
    )
    lemma_proof = (
        "PROOF. Suppose s subset g0 is a C-subspace of g (i.e. i*s = s) and s is nonzero. "
        "Then s subset g0 and s = i*s subset i*g0, so s subset g0 ∩ i*g0. But g0 ∩ i*g0 = 0 "
        "by definition of a real form (g0 (+) i*g0 is a DIRECT real-vector-space sum). "
        "Hence s = 0, contradiction. QED."
    )
    log("  " + lemma_statement)
    log("  " + lemma_proof)

    rank_xhy = sp.Matrix([[sprat(c) for c in v] for v in (X, H, Y)]).rank()
    log(f"  formal check: rank{{X,H,Y}} over C = {rank_xhy} (expect 3 -- a genuine, "
        f"non-degenerate 3-dim complex Lie subalgebra of e6(C), isomorphic to sl2(C))")
    assert rank_xhy == 3
    triple_is_sl2c = veq(br(X, Y), H) and veq(br(H, X), smul(2, X)) and veq(br(H, Y), smul(-2, Y))
    assert triple_is_sl2c

    consequence = (
        "CONSEQUENCE (applying the lemma). The density premise -- the object's hyperbolic "
        "holonomy rho: pi_1 -> SL(2,C) is irreducible+non-elementary (tr[A,B] = 3/2+(sqrt3/2)i "
        "!= 2) hence Zariski-dense in SL(2,C) -- is a CITED fact from B1086/B1098, about a "
        "hyperbolic 3-manifold representation; it is NOT re-derived here (outside this "
        "Lie-algebra sandbox's scope -- no hyperbolic-manifold data is loaded in this script). "
        "What IS verified here is the piece the lemma actually needs: span_C(X,H,Y) [and, "
        "identically, span_C(e2,h2,f2)] is confirmed (rank 3, exact triple relations) to be a "
        "genuine 3-complex-dimensional Lie subalgebra of e6(C) isomorphic to sl2(C), i.e. the "
        "Lie algebra of the group the composed holonomy is claimed dense in. Given the CITED "
        "density premise, its Zariski closure IS this full complex sl2(C) (not some smaller "
        "real slice), so by the lemma above no real form of E6 can contain it. This is a valid "
        "deduction, not a new computation; the premise's citation status is flagged, not hidden."
    )
    log("  " + consequence)

    R["layer1_lemma"] = {
        "statement": lemma_statement, "proof": lemma_proof,
        "formal_check_rank_XHY_is_3": rank_xhy == 3, "triple_is_sl2C": triple_is_sl2c,
        "consequence": consequence,
        "density_premise_status": "CITED (B1086/B1098 tr[A,B]!=2), NOT re-derived in this script",
        "pass": rank_xhy == 3 and triple_is_sl2c,
    }

    # =====================================================================
    # LAYER 4 -- the 27 under so(3,1): the bi-weight spectrum
    # =====================================================================
    log("")
    log("=== LAYER 4: the 27's (h1,h2) bi-weight spectrum (own crystal-of-omega1 build) ===")

    def build_27_own():
        Msys = sp.Matrix(N, N, lambda i, j: ip(SIMPLE[i], SIMPLE[j]))
        rhs = sp.Matrix([1] + [0] * (N - 1))
        w1 = Msys.solve(rhs)
        omega1 = tuple(sprat(w1[k]) for k in range(N))

        def tadd(a, b):
            return tuple(x + y for x, y in zip(a, b))

        def tsub(a, b):
            return tuple(x - y for x, y in zip(a, b))

        def ipr(a, b):
            return sum(a[i] * b[j] * Msys[i, j] for i in range(N) for j in range(N))

        weights = [omega1]
        seen = {omega1}
        queue = [omega1]
        while queue:
            lam = queue.pop()
            for al in SIMPLE:
                if ipr(lam, al) == 1:
                    mu = tsub(lam, al)
                    if mu not in seen:
                        seen.add(mu)
                        weights.append(mu)
                        queue.append(mu)
        assert len(weights) == 27, f"expected 27 weights, got {len(weights)}"
        WIDX = {w: i for i, w in enumerate(weights)}
        qlat = {w: tuple(int(x) for x in tsub(w, omega1)) for w in weights}
        for w in weights:
            assert all(sprat(a) == int(a) for a in tsub(w, omega1)), "non-integral shift"

        def act_root(r):
            out = {}
            for w in weights:
                tgt = tadd(w, r)
                if tgt in WIDX:
                    out[WIDX[w]] = (WIDX[tgt], Fr(eps(r, qlat[w])))
            return out

        ROOTACT = {r: act_root(r) for r in ROOTS}

        CJ = []
        for j in range(N):
            CJ.append([br(hvec(j), evec(al))[N + IDX[al]] for al in SIMPLE])

        def cartan_eig(j, lam):
            return sum(sprat(CJ[j][k]) * sprat(lam[k]) for k in range(N))

        def rho27(vec):
            M = [[Fr(0)] * 27 for _ in range(27)]
            for j in range(N):
                if vec[j]:
                    for w in weights:
                        ev = cartan_eig(j, w)
                        if ev:
                            i2 = WIDX[w]
                            M[i2][i2] += vec[j] * frac(ev)
            for r in ROOTS:
                c = vec[N + IDX[r]]
                if c:
                    for col, (row, s) in ROOTACT[r].items():
                        M[row][col] += c * s
            return M

        return weights, WIDX, rho27

    weights27, WIDX27, rho27 = build_27_own()
    log(f"  27 weights constructed (crystal of omega_1, own code): {len(weights27)} states")

    # ---- own full certification: rho27([u,v]) == [rho27(u),rho27(v)] on ALL Chevalley pairs
    log("  certifying rho27 is a genuine representation (own code, all C(78,2)=3003 pairs)...")
    basis_ad = [hvec(j) for j in range(N)] + [evec(r) for r in ROOTS]

    def matQ_mul(A, B):
        n = len(A)
        C = [[Fr(0)] * n for _ in range(n)]
        for i in range(n):
            Ai = A[i]
            Ci = C[i]
            for t in range(n):
                a = Ai[t]
                if a:
                    Bt = B[t]
                    for j in range(n):
                        bj = Bt[j]
                        if bj:
                            Ci[j] += a * bj
        return C

    RHO = [rho27(v) for v in basis_ad]
    import itertools
    fails = 0
    checked = 0
    for (i2, j2) in itertools.combinations(range(len(basis_ad)), 2):
        lhs = rho27(br(basis_ad[i2], basis_ad[j2]))
        Lm = matQ_mul(RHO[i2], RHO[j2])
        Rm = matQ_mul(RHO[j2], RHO[i2])
        rhs27 = [[Lm[a][b] - Rm[a][b] for b in range(27)] for a in range(27)]
        checked += 1
        if lhs != rhs27:
            fails += 1
    rep_certified = (fails == 0)
    log(f"  rep certification: {checked} pairs checked, {fails} failures -- "
        f"{'PASS' if rep_certified else 'FAIL'}")
    assert rep_certified, "the own-built 27 is not a genuine e6-representation -- STOP"

    rhoH = rho27(H)
    rho_h2 = rho27(h2v)
    diagH = all(rhoH[i][j] == 0 for i in range(27) for j in range(27) if i != j)
    diag_h2 = all(rho_h2[i][j] == 0 for i in range(27) for j in range(27) if i != j)
    log(f"  rho27(H) diagonal: {diagH}   rho27(h2) diagonal: {diag_h2} (both pure-Cartan elements)")
    assert diagH and diag_h2

    biweights = [(int(rhoH[i][i]), int(rho_h2[i][i])) for i in range(27)]
    biweight_counts = Counter(biweights)
    all_even = all(a % 2 == 0 and b % 2 == 0 for a, b in biweights)
    log(f"  ALL bi-weights even: {all_even}")
    assert all_even

    claimed = {(2, 2): 1, (2, -2): 1, (-2, 2): 1, (-2, -2): 1,
               (2, 0): 4, (-2, 0): 4, (0, 2): 4, (0, -2): 4, (0, 0): 7}
    computed = dict(biweight_counts)
    match = (computed == claimed)
    log(f"  computed bi-weight multiset: {sorted(computed.items())}")
    log(f"  memo's claimed multiset:     {sorted(claimed.items())}")
    log(f"  EXACT MATCH to memo's {{(+-2,+-2):1, (+-2,0):4, (0,+-2):4, (0,0):7}}: {match}")
    assert match
    total_states = sum(computed.values())
    assert total_states == 27

    R["layer4_biweights"] = {
        "rep_certified": {"pairs_checked": checked, "fails": fails},
        "biweight_multiset": {f"{k}": v for k, v in sorted(computed.items())},
        "claimed_multiset": {f"{k}": v for k, v in sorted(claimed.items())},
        "all_even": all_even, "exact_match": match, "exactness": "exact (Fraction throughout)",
    }

    # ---- bonus: color refinement using I2's own (already-built) pure-Cartan coroots
    # (I2 = the joint centralizer exactly, layer 2d) as the su(3)_color Cartan generators.
    log("")
    log("  -- bonus: color refinement of the (0,0) Lorentz block via I2's own coroots --")
    c1v, c2v = I2_coroots
    commute_c1c2 = is_zero(br(c1v, c2v))
    commute_with_H = is_zero(br(c1v, H)) and is_zero(br(c1v, h2v)) and is_zero(br(c2v, H)) and is_zero(br(c2v, h2v))
    log(f"  I2's coroots commute with each other: {commute_c1c2}; with H,h2: {commute_with_H}")
    assert commute_c1c2 and commute_with_H
    rho_c1, rho_c2 = rho27(c1v), rho27(c2v)
    diag_c1 = all(rho_c1[i][j] == 0 for i in range(27) for j in range(27) if i != j)
    diag_c2 = all(rho_c2[i][j] == 0 for i in range(27) for j in range(27) if i != j)
    log(f"  rho27(c1) diagonal: {diag_c1}   rho27(c2) diagonal: {diag_c2}")
    assert diag_c1 and diag_c2

    four_tuples = [(int(rhoH[i][i]), int(rho_h2[i][i]), frac(rho_c1[i][i]), frac(rho_c2[i][i]))
                   for i in range(27)]
    by_biweight = {}
    for (h1w, h2w, cc1, cc2) in four_tuples:
        by_biweight.setdefault((h1w, h2w), []).append((cc1, cc2))

    def classify_color_pattern(pts):
        """Very small helper: label the (c1,c2) pattern within one Lorentz bi-weight block by
        its size (1 = singlet-like, 3 = triplet-like) -- exact multiset, no assumptions."""
        return sorted((str(a), str(b)) for a, b in pts)

    color_report = {f"{k}": classify_color_pattern(v) for k, v in sorted(by_biweight.items())}
    zero_block = by_biweight[(0, 0)]
    log(f"  the (0,0) Lorentz block has {len(zero_block)} states (expect 7 = 1+3+3); "
        f"their (c1,c2) color weights: {sorted(str(p) for p in zero_block)}")
    # distinct nonzero color-weight directions among the 6 non-origin states, and the singlet count
    origin_count = sum(1 for p in zero_block if p == (Fr(0), Fr(0)))
    nonorigin = [p for p in zero_block if p != (Fr(0), Fr(0))]
    log(f"  color-singlet states (c1=c2=0) inside the (0,0) block: {origin_count} (expect 1)")
    log(f"  remaining {len(nonorigin)} states' color weights: {sorted(str(p) for p in nonorigin)}")
    # each (+-2,0)/(0,+-2) block has multiplicity 4 (already confirmed above): the claimed
    # decomposition (1,1)@1_c (+) (1,0)@3_c (+) (0,1)@3_c-bar puts exactly ONE color-singlet
    # state (from (1,1)@1_c) and THREE color-nonsinglet states (the 3_c or 3_c-bar factor)
    # at each of these blocks. Split each block that way before asking about the triplet shape.
    def split_singlet(block):
        singlets = [p for p in block if p == (Fr(0), Fr(0))]
        rest = [p for p in block if p != (Fr(0), Fr(0))]
        return singlets, rest

    blocks4 = {k: by_biweight[k] for k in [(2, 0), (-2, 0), (0, 2), (0, -2)]}
    split4 = {k: split_singlet(v) for k, v in blocks4.items()}
    for k, (sing, rest) in split4.items():
        log(f"  {k} block ({len(blocks4[k])} states): {len(sing)} color-singlet + "
            f"{len(rest)} color-nonsinglet {sorted(str(p) for p in rest)}")

    def is_weight_triangle(pts):
        return len(set(pts)) == 3 and all(p != (Fr(0), Fr(0)) for p in pts)

    one_singlet_each = all(len(sing) == 1 for sing, rest in split4.values())
    triangle_each = {str(k): is_weight_triangle(rest) for k, (sing, rest) in split4.items()}
    log(f"  exactly one color-singlet per block: {one_singlet_each}")
    log(f"  remaining 3 states form a distinct-nonzero weight triangle per block: {triangle_each}")
    assert one_singlet_each and all(triangle_each.values())

    # the four pure-(1,1) blocks (each total multiplicity 1) should be purely color-singlet
    pure_blocks = {k: by_biweight[k] for k in [(2, 2), (2, -2), (-2, 2), (-2, -2)]}
    pure_singlet_ok = all(len(v) == 1 and v[0] == (Fr(0), Fr(0)) for v in pure_blocks.values())
    log(f"  the four (+-2,+-2) blocks (mult 1 each) are purely color-singlet: {pure_singlet_ok}")
    assert pure_singlet_ok

    # su(3) representation-theoretic cross-checks (exact set equality / negation):
    rest20, restm20 = split4[(2, 0)][1], split4[(-2, 0)][1]
    rest02, rest0m2 = split4[(0, 2)][1], split4[(0, -2)][1]
    same_3c_across_h1 = (set(rest20) == set(restm20))
    same_3cbar_across_h1 = (set(rest02) == set(rest0m2))
    neg = lambda pts: set((-a, -b) for a, b in pts)
    triplet_vs_antitriplet_negated = (neg(set(rest20)) == set(rest02))
    log(f"  the SAME 3_c copy appears (identical weights) at h1=+2 and h1=-2 "
        f"(spin carried by Lorentz alone, color factor fixed): {same_3c_across_h1}")
    log(f"  the SAME 3_c-bar copy appears at h2=+2 and h2=-2: {same_3cbar_across_h1}")
    log(f"  the (1,0) factor's color triplet and the (0,1) factor's color triplet are exact "
        f"NEGATIVES of each other (3 vs 3-bar weight relation): {triplet_vs_antitriplet_negated}")
    assert same_3c_across_h1 and same_3cbar_across_h1 and triplet_vs_antitriplet_negated

    R["layer4_bonus_color_refinement"] = {
        "I2_is_joint_centralizer": joint_equals_I2,
        "by_biweight_color_patterns": color_report,
        "zero_block_singlet_count": origin_count,
        "one_singlet_per_2_0_type_block": one_singlet_each,
        "triangle_per_block": triangle_each,
        "pure_1_1_blocks_are_color_singlet": pure_singlet_ok,
        "same_3c_weights_at_h1_plus_and_minus_2": same_3c_across_h1,
        "same_3cbar_weights_at_h2_plus_and_minus_2": same_3cbar_across_h1,
        "3_and_3bar_weights_are_negatives": triplet_vs_antitriplet_negated,
        "reading_confirmed": ("(1,1)@1_c [4 pure-singlet Lorentz corners + the (0,0) block's "
                               "singlet] (+) (1,0)@3_c [(+-2,0) triplets + (0,0)'s 3 states] "
                               "(+) (0,1)@3_c-bar [(0,+-2) triplets + (0,0)'s other 3 states] "
                               "-- matches the memo's claimed decomposition exactly, verified "
                               "as an EXACT computed fact (weight identities), not assumed."),
        "note": ("Supplementary check (not strictly required by the task's core layer-4 ask, "
                 "which is the bi-weight multiset alone -- confirmed exact above). Uses I2's "
                 "own root-derived coroots as the su(3)_color Cartan (valid since layer 2d "
                 "proved the joint centralizer literally IS I2). Exact throughout (Fraction), "
                 "no float rounding anywhere in this bonus section either."),
    }

    # =====================================================================
    # OVERALL VERDICT
    # =====================================================================
    log("")
    log("=== OVERALL ===")
    layer_verdicts = {
        "layer1_lemma": "CONFIRMED" if R["layer1_lemma"]["pass"] else "DISCREPANT",
        "layer2_algebra": "CONFIRMED" if (control_pass and same_class_by_b1098_key
                                           and R["layer2d_joint_centralizer"]["pass"]) else "DISCREPANT",
        "layer3_rationality": "CONFIRMED" if R["layer3_rationality"]["pass"] else "DISCREPANT",
        "layer4_biweights": "CONFIRMED" if (rep_certified and match) else "DISCREPANT",
    }
    overall = "CONFIRMED" if all(v == "CONFIRMED" for v in layer_verdicts.values()) else "PARTIAL"
    log(f"  layer verdicts: {layer_verdicts}")
    log(f"  OVERALL: {overall}")
    log(f"  (documentation flag, not a computational failure: the memo's '36 per B1098's "
        f"dim-c table' mis-cites its source -- 36 is real but not in that table; see "
        f"layer2c_same_class.note)")

    R["verdicts"] = layer_verdicts
    R["overall"] = overall
    R["runtime_seconds"] = round(time.time() - T0, 2)
    R["log"] = LOG

    out_path = os.path.join(HERE, "b1114_results.json")
    with open(out_path, "w") as f:
        json.dump(R, f, indent=1)
    log(f"wrote {out_path}")
    log(f"TOTAL runtime: {time.time()-T0:.2f}s")
    return R


if __name__ == "__main__":
    main()
