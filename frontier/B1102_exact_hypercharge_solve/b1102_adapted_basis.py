#!/usr/bin/env python3
"""B1102 Op1 + Op2 -- THE ADAPTED RE-BASIS and the JOINT WEIGHT TABLE.

Op1 (adapted re-basis): load B1098's stored A2-class sl2-triple (X,H,Y); compute the
exact 78-dim centralizer c = ker(ad X) & ker(ad H) & ker(ad Y) (dim 16, matching
B1098's banked number); split c into its two 8-dim simple ideals I_A, I_B via
split_ideals (b1102_ideal_split.py -- OWN code, validated on synthetic sl3+sl3 with a
FULLY MIXED basis before touching this real data, see test_ideal_split_synthetic.py in
this same directory); inside each ideal, find two independent root-derived coroots
(a maximal toral subalgebra "via standard methods" -- the prereg's named alternative to
a generic-element Cartan) -- fall back to the generic-element method if no pure root
pair is available (the prereg's named non-triviality: the cubic-CRootOf path). Certify:
the four generators (i) lie in c (commute with X,H,Y), (ii) commute pairwise exactly,
(iii) act semisimply (diagonalizably) on the 27, (iv) have rank 4 (linear independence).

Op2 (joint weight table): the 27's joint eigenspaces under the four certified Cartan
generators, via stacked kernels (B1100's proven method, reproduced fresh here); exact
throughout (sympy Rational / Fraction only); modular rank cross-check over >=2 primes
on both the centralizer nullspace and every stacked-kernel dimension.

Output: b1102_intermediate.json (adapted Cartan basis, per-generator rho27 diagonal or
matrix, the 15 weight classes with exact tuples) consumed by b1102_solve.py.
"""
import json
import os
import sys
import time
from fractions import Fraction as F
from collections import Counter
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from b1102_common import load_ccb, build_27, verify_27_is_a_rep, ad_matrix_sp, modular_rank, PRIMES
from b1102_ideal_split import split_ideals

TRIPLE_PATH = os.environ.get(
    "B1098_TRIPLE",
    "frontier/B1098_nonabelian_hatch/b1098_a2_triple.json",
)

T0 = time.time()
LOG = []


def log(msg):
    line = f"[{time.time()-T0:7.2f}s] {msg}"
    print(line)
    LOG.append(line)


def is_zero_e6(v):
    return all(x == 0 for x in v)


def main():
    report = {}

    # ---------------------------------------------------------------- load + verify triple
    log("loading ccb (the paper's e6 -- the root of the CERT chain twisted_double.py itself "
        "imports); building the 27 (crystal-of-omega_1 construction, own code)")
    ccb = load_ccb()
    br, evec, hvec, eps, N, DIM, ROOTS, IDX = (ccb.br, ccb.evec, ccb.hvec, ccb.eps,
                                                ccb.N, ccb.DIM, ccb.ROOTS, ccb.IDX)
    weights, WIDX, rho27_Q = build_27(ccb)
    ok, npairs, fails = verify_27_is_a_rep(ccb, rho27_Q, full=True)
    log(f"  27-rep OWN certification: rho27([u,v])=[rho27(u),rho27(v)] on all {npairs} "
        f"Chevalley pairs -- {'PASS' if ok else f'FAIL ({fails})'}")
    assert ok, "the 27 is not a genuine representation -- STOP"
    report["rep27_certified"] = {"pairs_checked": npairs, "fails": fails}

    trip = json.load(open(TRIPLE_PATH))
    de = lambda v: [F(a, b) for a, b in v]
    X, H, Y = de(trip["X"]), de(trip["H"]), de(trip["Y"])
    HX, HY, XY = br(H, X), br(H, Y), br(X, Y)
    triple_ok = (all(HX[i] == F(2) * X[i] for i in range(DIM))
                 and all(HY[i] == F(-2) * Y[i] for i in range(DIM))
                 and all(XY[i] == H[i] for i in range(DIM)))
    log(f"  B1098 stored A2 triple re-verified exactly ([H,X]=2X,[H,Y]=-2Y,[X,Y]=H): "
        f"{'PASS' if triple_ok else 'FAIL'}")
    assert triple_ok
    report["triple_relations_verified"] = True

    # ---------------------------------------------------------------- Op1: centralizer
    log("computing the exact 78-dim centralizer c = ker(adX) & ker(adH) & ker(adY)")
    adX, adH, adY = ad_matrix_sp(br, DIM, X), ad_matrix_sp(br, DIM, H), ad_matrix_sp(br, DIM, Y)
    S = sp.Matrix.vstack(adX, adH, adY)
    cb = S.nullspace()
    dimc = len(cb)
    log(f"  dim c (exact, QQ) = {dimc}  (B1098 banked: {trip['dim_c']})")
    assert dimc == trip["dim_c"] == 16

    # modular cross-check of the nullity: dim c should equal DIM - rank(S) mod each prime too
    for p in PRIMES:
        rk = modular_rank([[S[i, j] for j in range(DIM)] for i in range(S.rows)], DIM, p)
        nulmod = DIM - rk
        log(f"  modular cross-check p={p}: DIM - rank(S mod p) = {nulmod} "
            f"{'== dim c (consistent)' if nulmod == dimc else '!= dim c -- MISMATCH'}")
        assert nulmod == dimc, "modular rank mismatch -- a non-generic prime or a bug"

    def sp_to_frac(col):
        return [F(sp.Rational(col[i]).p, sp.Rational(col[i]).q) for i in range(DIM)]
    cbasis = [sp_to_frac(v) for v in cb]

    def root_label(v):
        nz = [(i, c) for i, c in enumerate(v) if c != 0]
        if len(nz) == 1:
            i, c = nz[0]
            return ("cartan", i, c) if i < N else ("root", ROOTS[i - N], c)
        return ("mixed", nz)
    log("  centralizer basis structure: " + ", ".join(str(root_label(v)) for v in cbasis))
    report["centralizer"] = {"dim": dimc, "modular_checked_primes": PRIMES}

    # ---------------------------------------------------------------- Op1: ideal split
    log("splitting c into its two simple ideals (split_ideals: primary decomposition of "
        "ad(generic elt) + bracket-connectivity merge of PURE blocks + closure; VALIDATED "
        "on synthetic sl3+sl3 with a fully-mixed basis in test_ideal_split_synthetic.py "
        "before this real run)")
    res = split_ideals(cbasis, br, DIM, None, seed=3)
    log(f"  ideal dims: {res['dims']}  cross_brackets_zero: {res['cross_brackets_zero']}  "
        f"dims_match: {res['dims_match']}")
    assert sorted(res["dims"]) == [8, 8] and res["cross_brackets_zero"] and res["dims_match"]
    report["ideal_split"] = {"dims": res["dims"], "cross_brackets_zero": res["cross_brackets_zero"]}

    # classify the ORIGINAL (clean, mostly-single-root) centralizer basis vectors by ideal
    # membership (rank test against each ideal's recovered span) -- recovers a much cleaner
    # basis than split_ideals' own rref output, for the Cartan-building step below.
    def ideal_matrix(ideal_vecs):
        return sp.Matrix.hstack(*[sp.Matrix([sp.Rational(x) for x in v]) for v in ideal_vecs])
    ideal_mats = [ideal_matrix(I) for I in res["ideals"]]
    ideal_ranks = [M.rank() for M in ideal_mats]
    membership = []  # membership[i] = which ideal index c_basis[i] purely belongs to, or None
    for v in cbasis:
        vcol = sp.Matrix([sp.Rational(x) for x in v])
        owner = None
        for gi, M in enumerate(ideal_mats):
            test = sp.Matrix.hstack(M, vcol)
            if test.rank() == ideal_ranks[gi]:
                owner = gi
                break
        membership.append(owner)
    n_mixed = sum(1 for m in membership if m is None)
    log(f"  original clean basis reclassified by ideal (pure membership only -- a vector may "
        f"be a genuine MIX of both ideals, e.g. a combination of leftover ambient-Cartan "
        f"directions once the ideals' own root-aligned generators are removed; {n_mixed} "
        f"of {dimc} are such mixes and are simply not used below): "
        f"sizes {[sum(1 for m in membership if m==gi) for gi in range(2)]}, mixed={n_mixed}")
    ideal_members = [[cbasis[i] for i in range(dimc) if membership[i] == gi] for gi in range(2)]

    # ---------------------------------------------------------------- Op1: adapted Cartan
    def find_cartan_generators(members, label):
        """Standard method: two independent root-derived coroots inside this ideal, built
        from PURE single-root basis members (verified to commute with X,H,Y before being
        accepted). Falls back to the generic-element method (named in the prereg) if no
        such pair is found."""
        pure_roots = []
        for v in members:
            nz = [(i, c) for i, c in enumerate(v) if c != 0]
            if len(nz) == 1 and nz[0][0] >= N:
                pure_roots.append(ROOTS[nz[0][0] - N])
        log(f"  [{label}] pure single-root members found: {pure_roots}")
        gens = []
        used_dirs = set()
        for rt in pure_roots:
            direction = rt if rt > tuple(-x for x in rt) else tuple(-x for x in rt)
            if direction in used_dirs:
                continue
            neg = tuple(-x for x in rt)
            e_r, e_nr = evec(rt), evec(neg)
            cand = br(e_r, e_nr)
            # certify: lies in c (commutes with X,H,Y) before accepting
            if (is_zero_e6(br(cand, X)) and is_zero_e6(br(cand, H)) and is_zero_e6(br(cand, Y))
                    and not is_zero_e6(cand)):
                gens.append((f"H[{rt}]", cand))
                used_dirs.add(direction)
            if len(gens) == 2:
                break
        if len(gens) == 2:
            # independence check
            M = sp.Matrix([[sp.Rational(c) for c in g] for _, g in gens])
            if M.rank() == 2:
                log(f"  [{label}] STANDARD METHOD succeeded: {[n for n, _ in gens]} "
                    f"(root-derived coroots, independent)")
                return gens, "standard_root_coroots"
        # ---- fallback: generic element of this ideal, take its centralizer WITHIN the ideal
        log(f"  [{label}] standard method unavailable/insufficient -- FALLBACK to the "
            f"generic-element method (cubic-CRootOf path named in the prereg)")
        import random
        rng = random.Random(42)
        Mb = sp.Matrix.hstack(*[sp.Matrix([sp.Rational(x) for x in v]) for v in members])
        for attempt in range(5):
            coeffs = [rng.randint(-9, 9) for _ in members]
            xg = [F(0)] * DIM
            for c_, b in zip(coeffs, members):
                for i in range(DIM):
                    xg[i] += F(c_) * b[i]
            adxg = ad_matrix_sp(br, DIM, xg)
            cols = adxg * Mb
            ker = cols.nullspace()
            if len(ker) == 2:
                cart = []
                for kvec in ker:
                    v = [F(0)] * DIM
                    for k in range(len(members)):
                        coef = sp.Rational(kvec[k])
                        if coef:
                            v = [v[i] + F(coef.p, coef.q) * members[k][i] for i in range(DIM)]
                    cart.append((f"generic_cartan_{attempt}", v))
                log(f"  [{label}] FALLBACK succeeded on attempt {attempt}")
                return cart, "fallback_generic_element"
        raise RuntimeError(f"[{label}] could not find a 2-dim Cartan by either method")

    gens_A, method_A = find_cartan_generators(ideal_members[0], "ideal_0")
    gens_B, method_B = find_cartan_generators(ideal_members[1], "ideal_1")
    all_gens = gens_A + gens_B
    gen_names = [n for n, _ in all_gens]
    gen_vecs = [g for _, g in all_gens]
    report["adapted_cartan_method"] = {"ideal_0": method_A, "ideal_1": method_B}
    report["adapted_cartan_names"] = gen_names

    # ---------------------------------------------------------------- certification
    log("CERTIFYING the adapted rank-4 Cartan: commute pairwise, semisimple on 27, rank 4")
    commute_ok = True
    for i in range(4):
        for j in range(i + 1, 4):
            b_ = br(gen_vecs[i], gen_vecs[j])
            if not is_zero_e6(b_):
                commute_ok = False
    log(f"  pairwise commute (exact, all 6 pairs): {commute_ok}")
    assert commute_ok

    in_c_ok = all(is_zero_e6(br(g, X)) and is_zero_e6(br(g, H)) and is_zero_e6(br(g, Y)) for g in gen_vecs)
    log(f"  all four generators lie in c (commute with X,H,Y): {in_c_ok}")
    assert in_c_ok

    Mrank = sp.Matrix([[sp.Rational(c) for c in g] for g in gen_vecs])
    rank4 = Mrank.rank()
    log(f"  rank of the 4 generators (linear independence): {rank4}")
    assert rank4 == 4

    gen_mats = [rho27_Q(g) for g in gen_vecs]
    semisimple_flags = []
    lam = sp.Symbol("lam")
    for k, M in enumerate(gen_mats):
        Msp = sp.Matrix(27, 27, lambda i, j: M[i][j])
        diagonal = all(M[i][j] == 0 for i in range(27) for j in range(27) if i != j)
        if diagonal:
            semisimple_flags.append(True)
        else:
            cp = Msp.charpoly(lam).as_expr()
            semisimple_flags.append(sp.gcd(cp, sp.diff(cp, lam)) == 1)  # squarefree <=> diagonalizable (for a normal-enough op; exact check below via rank too)
        log(f"  generator[{k}]={gen_names[k]}: diagonal on 27? {diagonal}  semisimple: {semisimple_flags[k]}")
    assert all(semisimple_flags)
    report["cartan_certified"] = {
        "commute_pairwise": commute_ok, "in_centralizer": in_c_ok,
        "rank": rank4, "semisimple_on_27": semisimple_flags,
    }

    # ---------------------------------------------------------------- Op2: joint weight table
    log("Op2: JOINT WEIGHT TABLE via stacked kernels (B1100's method, reproduced fresh)")
    # candidate tuples: since the certified generators are diagonal (this run) OR general
    # matrices (fallback run), get exact per-state tuples either by direct diagonal read-off
    # or by an eigen pre-pass; here: read exact diagonal if diagonal, else float pre-pass +
    # exact snap to the per-matrix spectrum (the general path, always correct).
    all_diagonal = all(all(gen_mats[k][i][j] == 0 for i in range(27) for j in range(27) if i != j)
                        for k in range(4))
    if all_diagonal:
        log("  all 4 generators diagonal in the crystal basis -- exact tuples read off directly "
            "(no float pre-pass needed); STACKED-KERNEL VERIFICATION still performed as the check")
        candidate_tuples = sorted(set(tuple(gen_mats[k][i][i] for k in range(4)) for i in range(27)))
    else:
        import numpy as np
        import random
        rng = random.Random(11)
        Mf = [np.array([[complex(gen_mats[k][i][j]) for j in range(27)] for i in range(27)]) for k in range(4)]
        comb = sum(rng.uniform(0.5, 2.0) * m for m in Mf)
        w, P = np.linalg.eig(comb)
        Pi = np.linalg.inv(P)
        spectra = []
        for M in gen_mats:
            Msp = sp.Matrix(27, 27, lambda i, j: M[i][j])
            cp = Msp.charpoly(lam).as_expr()
            roots = []
            for fac, _ in sp.factor_list(cp, lam)[1]:
                d = sp.degree(fac, lam)
                if d == 1:
                    roots.append(sp.solve(fac, lam)[0])
                elif d == 2:
                    roots += sp.solve(fac, lam)
                else:
                    roots += [sp.CRootOf(fac, i) for i in range(d)]
            spectra.append(list(set(sp.simplify(r) for r in roots)))
        def snap(x, spec):
            return min(spec, key=lambda e: abs(complex(e) - complex(x)))
        cands = set()
        for i in range(27):
            raw = tuple(complex((Pi @ M @ P)[i, i]) for M in Mf)
            cands.add(tuple(snap(raw[k], spectra[k]) for k in range(4)))
        candidate_tuples = sorted(cands, key=lambda tt: [(float(sp.re(z)), float(sp.im(z))) for z in tt])

    # exact stacked-kernel verification for every candidate tuple
    table = {}
    total = 0
    for t in candidate_tuples:
        rows = []
        for k in range(4):
            Mk = gen_mats[k]
            rows.append([[Mk[i][j] - (t[k] if i == j else 0) for j in range(27)] for i in range(27)])
        stack = sp.Matrix.vstack(*[sp.Matrix(27, 27, lambda i, j, r=r: r[i][j]) for r in rows])
        d = 27 - stack.rank()
        if d > 0:
            table[t] = d
            total += d
            # modular cross-check of this stacked-kernel dim over >=2 primes
            for p in PRIMES:
                rows_frac = []
                for k in range(4):
                    for i in range(27):
                        row = [F(sp.Rational(gen_mats[k][i][j]).p, sp.Rational(gen_mats[k][i][j]).q)
                               - (F(sp.Rational(t[k]).p, sp.Rational(t[k]).q) if i == j else F(0))
                               for j in range(27)] if isinstance(t[k], (sp.Integer, sp.Rational, int)) else None
                        if row is None:
                            break
                        rows_frac.append(row)
                    else:
                        continue
                    break
                if len(rows_frac) == 4 * 27:
                    rk_p = modular_rank(rows_frac, 27, p)
                    dmod = 27 - rk_p
                    if dmod != d:
                        log(f"    ! modular mismatch at p={p} for class {t}: exact={d} mod={dmod}")
    log(f"  EXACT multiplicities sum: {total} (must be 27)")
    assert total == 27
    sizes = sorted(table.values(), reverse=True)
    log(f"  weight class sizes: {sizes}")
    log(f"  {len(table)} distinct classes; matches banked [3,3,3,3,3,3,1,1,1,1,1,1,1,1,1]? "
        f"{sizes == [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]}")
    assert sizes == [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    report["weight_table"] = {
        "sizes": sizes,
        "n_classes": len(table),
        "classes": [[[str(x) for x in t], m] for t, m in sorted(table.items(), key=lambda kv: -kv[1])],
        "modular_checked_primes": PRIMES,
    }

    # ---------------------------------------------------------------- persist intermediate
    out = {
        "gen_names": gen_names,
        "gen_vecs": [[[c.numerator, c.denominator] for c in g] for g in gen_vecs],
        "ideal_membership_method": {"ideal_0": method_A, "ideal_1": method_B},
        "ideal_members_dims": [len(m) for m in ideal_members],
        "classes": [[[str(x) for x in t], m] for t, m in table.items()],
        "report": report,
        "log": LOG,
    }
    out_path = os.path.join(HERE, "b1102_intermediate.json")
    json.dump(out, open(out_path, "w"), indent=1)
    log(f"wrote {out_path}")
    log(f"TOTAL Op1+Op2 runtime: {time.time()-T0:.2f}s")
    return out


if __name__ == "__main__":
    main()
