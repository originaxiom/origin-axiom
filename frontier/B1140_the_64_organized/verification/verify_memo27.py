#!/usr/bin/env python3
"""
INDEPENDENT verification of cloud memo 27 ("THE 64 ORGANIZED"), own-code,
scratchpad-only. Repo tree is NEVER modified (read-only imports of two
already-banked/locked modules).

Reused (read-only, NOT rebuilt):
  - frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py
      (certified Chevalley e6: 72 roots, dim 78, br/evec/hvec/ip/A/BB)
  - frontier/B1138_structural_completion/verification/verify_memo11_fork.py
      (the FORK construction: a2_span, find_a2_in, principal_triple,
       color_gens, VendoredE6 adapter, run_ladder -- imported as module F,
       called with its own functions, not copied)
  - frontier/B1138_structural_completion/verification/my_chevalley.py
      (generic exact linear algebra: exact_rank, centralizer_rows,
       nullspace_basis_exact -- imported, not copied)

Everything past that point (Killing form, weight bookkeeping, highest-weight
enumeration, su(3) irrep identification via Weyl dimension formula) is my
own code, written for this task. Exact rational (fractions.Fraction)
arithmetic throughout; no floats anywhere in the algebra.

No Standard-Model numerical value enters anywhere (Gate 5): this is pure
group theory over Q.
"""
import os
import sys
import time
from fractions import Fraction as Fr
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
B1102 = os.path.join(REPO, "frontier/B1102_exact_hypercharge_solve")
B1138V = os.path.join(REPO, "frontier/B1138_structural_completion/verification")
sys.path.insert(0, B1102)
sys.path.insert(0, B1138V)

import e6_bracket_vendored as V              # noqa: E402  banked+locked, read-only
import my_chevalley as MC                    # noqa: E402  exact_rank / centralizer_rows / nullspace_basis_exact
import verify_memo11_fork as F                # noqa: E402  the FORK construction, read-only reuse

ALG = F.ALG
N = F.N
DIM = ALG.DIM
ROOTS = ALG.roots

assert DIM == 78 and len(ROOTS) == 72 and N == 6, "vendored e6 shape mismatch"

# ---------------------------------------------------------------- utilities
def add(u, v):
    return [a + b for a, b in zip(u, v)]


def smul(c, u):
    c = Fr(c)
    return [c * a for a in u]


def is_zero(u):
    return all(a == 0 for a in u)


def basis_vec(k, dim=DIM):
    v = [Fr(0)] * dim
    v[k] = Fr(1)
    return v


def cartan_part(vec):
    return tuple(vec[:N])


def pair6(root_tuple, cart6):
    """ip(root, x) with x given as a length-N Cartan-coordinate tuple, using
    the SAME (Killing-normalised, simply-laced) bilinear form as ALG.pairing."""
    total = Fr(0)
    for i in range(N):
        ai = Fr(root_tuple[i])
        if ai == 0:
            continue
        for j in range(N):
            xj = Fr(cart6[j])
            if xj == 0:
                continue
            total += ai * Fr(ALG.A[i][j]) * xj
    return total


LOG = []


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.append(s)


t_start = time.time()

log("=" * 78)
log("MEMO 27 ('THE 64 ORGANIZED') -- independent own-code verification")
log("=" * 78)

# ============================================================ STEP 1 + 2 ==
log("\n--- STEP 1-2: build T1,T2,COLOR exactly as B1138 (slot A), re-confirm ladder ---")
a0 = tuple(1 if k == 0 else 0 for k in range(N))
a2 = tuple(1 if k == 2 else 0 for k in range(N))
ladder, (S0, S1, S2) = F.run_ladder((a0, a2), "memo27-verify, slot A (matches B1138 cert)")
LADDER_OK = (ladder == (16, 8, 8, 0))
log(f"ladder = {ladder}  ->  {'CONFIRMED matches B1138 (16,8,8,0)' if LADDER_OK else 'MISMATCH'}")

T1 = F.principal_triple(F.find_a2_in(S0))   # [e,h,f], sl2 relations already asserted inside
T2 = F.principal_triple(F.find_a2_in(S1))
COLOR = F.color_gens(S2)                     # 6 root gens (sorted S2) + 2 Cartan (r2,s2)
r2, s2 = F.find_a2_in(S2)

SUBALG = T1 + T2 + COLOR
assert len(SUBALG) == 14

rank14 = MC.exact_rank(SUBALG, DIM)
log(f"rank(14 subalgebra generators) = {rank14}  (expect 14) -> "
    f"{'CONFIRMED independent' if rank14 == 14 else 'REFUTED'}")


def bracket_count_nonzero(A, B):
    bad = 0
    for x in A:
        for y in B:
            if not is_zero(ALG.br(x, y)):
                bad += 1
    return bad


c_t1t2 = bracket_count_nonzero(T1, T2)
c_t1col = bracket_count_nonzero(T1, COLOR)
c_t2col = bracket_count_nonzero(T2, COLOR)
log(f"[T1,T2] nonzero pairs = {c_t1t2}/9   (expect 0)")
log(f"[T1,COLOR] nonzero pairs = {c_t1col}/24  (expect 0)")
log(f"[T2,COLOR] nonzero pairs = {c_t2col}/24  (expect 0)")
MUTUAL_COMMUTE_OK = (c_t1t2 == 0 and c_t1col == 0 and c_t2col == 0)
log(f"mutual commutativity T1,T2,COLOR -> {'CONFIRMED' if MUTUAL_COMMUTE_OK else 'REFUTED'} "
    "(so su(2)xsu(2)xsu(3) is an honest Lie-algebra direct sum inside e6, not just a vector-space sum)")

color_rank = MC.exact_rank(COLOR, DIM)
log(f"rank(COLOR's 8 generators) = {color_rank}  (expect 8)")

closure_bad = []
for i in range(8):
    for j in range(i + 1, 8):
        br_ij = ALG.br(COLOR[i], COLOR[j])
        if is_zero(br_ij):
            continue
        test_rank = MC.exact_rank(COLOR + [br_ij], DIM)
        if test_rank != 8:
            closure_bad.append((i, j))
log(f"COLOR closure under bracket: failures = {len(closure_bad)}/28 pairs "
    f"(expect 0) -> {'CONFIRMED COLOR is closed (an sl3)' if not closure_bad else 'REFUTED'}")

d4_direct = DIM - MC.exact_rank(MC.centralizer_rows(ALG, SUBALG), DIM)
log(f"dim z(T1,T2,COLOR) recomputed directly on the 14-gen union = {d4_direct} "
    f"(expect 0, matches ladder[3]={ladder[3]}) -> "
    f"{'CONFIRMED' if d4_direct == 0 else 'REFUTED'}")

STEP12_OK = LADDER_OK and rank14 == 14 and MUTUAL_COMMUTE_OK and color_rank == 8 and (not closure_bad) and d4_direct == 0
log(f"\nSTEP 1-2 OVERALL: {'CONFIRMED' if STEP12_OK else 'REFUTED -- STOP, downstream steps invalid'}")
assert STEP12_OK, "subalgebra construction failed its own consistency checks"

print(f"\n[timing] steps 1-2 done at {time.time()-t_start:.1f}s")

# ================================================================ STEP 3 ==
# The 64-dim complement of the 14-dim subalgebra, as the Killing-form
# orthogonal complement in the ambient e6 (78-dim). K(x,y) = tr(ad(x)ad(y)),
# computed by brute-force nested bracket -- no shortcuts assumed, so this is
# a ground-truth computation, not a theory-derived guess.
log("\n" + "=" * 78)
log("STEP 3: the 64-dim complement, via the Killing form (brute force trace)")
log("=" * 78)


def killing_general(x, y):
    """trace(ad(x) ad(y)) for two general DIM-vectors, fully brute force."""
    total = Fr(0)
    for m in range(DIM):
        ycol = ALG.br(y, basis_vec(m))
        if is_zero(ycol):
            continue
        xcol = ALG.br(x, ycol)
        if xcol[m]:
            total += xcol[m]
    return total


def killing_vs_basis(x, j):
    """trace(ad(x) ad(e_j)) reusing V.BB[j] (=ad(e_j)'s columns) directly,
    since ad(e_j) e_m = br(e_j,e_m) = V.BB[j][m] needs no recomputation."""
    total = Fr(0)
    for m in range(DIM):
        ycol = V.BB[j][m]
        if is_zero(ycol):
            continue
        xcol = ALG.br(x, ycol)
        if xcol[m]:
            total += xcol[m]
    return total


t3 = time.time()
# 14x14 Gram matrix: confirm the Killing form restricted to the subalgebra
# is non-degenerate (standard fact for a semisimple subalgebra; verified,
# not assumed).
GRAM = [[killing_general(SUBALG[i], SUBALG[j]) for j in range(14)] for i in range(14)]
gram_rank = MC.exact_rank(GRAM, 14)
log(f"Killing-form Gram matrix on the 14 subalgebra generators: rank = {gram_rank} "
    f"(expect 14, i.e. non-degenerate) -> {'CONFIRMED' if gram_rank == 14 else 'REFUTED'}")

# 14x78 matrix M[i][j] = K(g_i, e_j); complement = null space of M.
M_KILL = [[killing_vs_basis(SUBALG[i], j) for j in range(DIM)] for i in range(14)]
log(f"[timing] 14x78 Killing matrix computed at {time.time()-t3:.1f}s "
    f"(cumulative {time.time()-t_start:.1f}s)")

COMPLEMENT = MC.nullspace_basis_exact(M_KILL, DIM)
log(f"dim(Killing-orthogonal complement) = {len(COMPLEMENT)}  (expect 64) -> "
    f"{'CONFIRMED' if len(COMPLEMENT) == 64 else 'REFUTED'}")

# sanity: complement + subalgebra should together span all of e6 (rank 78),
# and be disjoint (14+64=78 exactly, already implied by nullspace dimension
# count given rank(M)=14=rank of the subalgebra's own Gram matrix, but spot
# check independence of the union too).
union_rank = MC.exact_rank(SUBALG + COMPLEMENT, DIM)
log(f"rank(14 subalgebra U 64 complement) = {union_rank}  (expect 78) -> "
    f"{'CONFIRMED they together span e6' if union_rank == 78 else 'REFUTED'}")

DIM64_OK = (gram_rank == 14 and len(COMPLEMENT) == 64 and union_rank == 78)
assert DIM64_OK, "complement construction failed"

# ============================================================ STEP 3.5 ===
# Weight quadruple (m1,m2,c1,c2) of every complement basis vector under
# ad(h_T1), ad(h_T2), ad(h_c1), ad(h_c2). h_T1,h_T2,h_c1,h_c2 are all
# elements of e6's OWN 6-dim Cartan, which is abelian, so this is exact
# eigenvector bookkeeping, not an approximation.
log("\n" + "=" * 78)
log("STEP 3.5: weight quadruples of the 64 complement states under the 4 Cartan gens")
log("=" * 78)

h_T1, h_T2 = T1[1], T2[1]
h_c1, h_c2 = COLOR[6], COLOR[7]
e_T1, f_T1 = T1[0], T1[2]
e_T2, f_T2 = T2[0], T2[2]
e_r2, e_s2 = ALG.evec(r2), ALG.evec(s2)

CARTAN4 = [("m1", h_T1), ("m2", h_T2), ("c1", h_c1), ("c2", h_c2)]


def eigen_or_none(h, v):
    """If br(h,v) is a scalar multiple of v, return that scalar; else None."""
    hv = ALG.br(h, v)
    k = next((i for i, x in enumerate(v) if x != 0), None)
    if k is None:
        return Fr(0)
    lam = hv[k] / v[k]
    if hv == smul(lam, v):
        return lam
    return None


weights = []
bad_eigen = 0
for v in COMPLEMENT:
    quad = []
    ok = True
    for name, h in CARTAN4:
        lam = eigen_or_none(h, v)
        if lam is None:
            ok = False
            break
        quad.append(lam)
    if not ok:
        bad_eigen += 1
        weights.append(None)
    else:
        weights.append(tuple(quad))

log(f"complement vectors that are NOT clean joint eigenvectors of (h_T1,h_T2,h_c1,h_c2): "
    f"{bad_eigen}/64")

if bad_eigen:
    log("  -> degenerate weight-mixing detected; re-diagonalizing the affected block(s).")
    # Collect indices that failed; they must all share weight (0,0,0,0) territory
    # (the only place multiple subalgebra Cartan directions can collide) -- rebuild
    # a clean eigenbasis for exactly that troublesome span using the same 4
    # commuting operators, via repeated nullspace-of-(H - lambda) restricted to
    # the span of the bad vectors. (General-purpose fallback; see analysis below
    # for whether this path is actually exercised.)
    bad_idx = [i for i, w in enumerate(weights) if w is None]
    bad_vecs = [COMPLEMENT[i] for i in bad_idx]
    # candidate eigenvalues to scan: small integers -6..6 for each of the 4 ops
    import itertools as _it
    span_rank = MC.exact_rank(bad_vecs, DIM)
    log(f"  troublesome span dimension = {span_rank} (from {len(bad_vecs)} vectors)")
    remaining = list(bad_vecs)
    new_eig = []
    for name, h in CARTAN4:
        nxt_remaining = []
        for lam in range(-6, 7):
            # rows: (H - lam I) applied to combos of `remaining`, find kernel coeffs
            if not remaining:
                break
            k = len(remaining)
            imgs = []
            for v in remaining:
                hv = ALG.br(h, v)
                diff = [hv[t] - Fr(lam) * v[t] for t in range(DIM)]
                imgs.append(diff)
            # transpose to rows for nullspace_basis_exact
            trows = [[imgs[i][col] for i in range(k)] for col in range(DIM)]
            ker = MC.nullspace_basis_exact(trows, k)
            for c in ker:
                vec = [Fr(0)] * DIM
                for i, ci in enumerate(c):
                    if ci:
                        vec = add(vec, smul(ci, remaining[i]))
                nxt_remaining.append((lam, vec))
        remaining = [nv for _, nv in nxt_remaining]
        new_eig.append([lam for lam, _ in nxt_remaining])
    log(f"  recovered {len(remaining)} eigenvectors after re-diagonalization "
        f"(expect {len(bad_vecs)})")
    # splice back
    ptr = 0
    for i in bad_idx:
        COMPLEMENT[i] = remaining[ptr]
        m1v = new_eig[0][ptr]
        ptr += 1
    # recompute weights fully clean this time
    weights = []
    for v in COMPLEMENT:
        quad = tuple(eigen_or_none(h, v) for _, h in CARTAN4)
        weights.append(quad)
    bad_eigen2 = sum(1 for w in weights if any(x is None for x in w))
    log(f"  after fix: non-eigenvector count = {bad_eigen2} (expect 0)")
    assert bad_eigen2 == 0, "re-diagonalization failed"

WEIGHT_CLASSES_OK = (bad_eigen == 0)
log(f"clean-eigenvector check on the 64: {'CONFIRMED (no fallback needed)' if WEIGHT_CLASSES_OK else 'handled via fallback re-diagonalization above'}")

# group by weight
weight_groups = defaultdict(list)
for v, w in zip(COMPLEMENT, weights):
    weight_groups[w].append(v)

log(f"\ndistinct weight quadruples (m1,m2,c1,c2) among the 64: {len(weight_groups)}")
for w in sorted(weight_groups.keys()):
    log(f"   weight {w}: multiplicity {len(weight_groups[w])}")

print(f"\n[timing] step 3.5 done at {time.time()-t_start:.1f}s")

# ================================================================ STEP 4 ==
# Highest-weight enumeration: for each weight class Vw (possibly multi-dim),
# find the kernel of "kill by ALL FOUR raising operators" (e_T1, e_T2, e_r2,
# e_s2) restricted to Vw. Kernel dimension = number of irreducible
# su(2)xsu(2)xsu(3) components of the 64-dim complement with that exact
# highest weight. This is complete-reducibility-correct and makes no
# assumption about which decomposition to expect.
log("\n" + "=" * 78)
log("STEP 4: highest-weight enumeration (su(2)_T1 x su(2)_T2 x su(3)_COLOR)")
log("=" * 78)

RAISERS = [e_T1, e_T2, e_r2, e_s2]

hw_records = []   # (weight_quad, multiplicity, [explicit hw vectors])
for w in sorted(weight_groups.keys(), key=lambda t: tuple(-x for x in t)):
    Vw = weight_groups[w]
    k = len(Vw)
    # R[i] = concat of the 4 raising images of Vw[i]
    R = []
    for v in Vw:
        row = []
        for op in RAISERS:
            row.extend(ALG.br(op, v))
        R.append(row)
    ncols_big = len(R[0])
    trows = [[R[i][col] for i in range(k)] for col in range(ncols_big)]
    ker = MC.nullspace_basis_exact(trows, k)
    mult = len(ker)
    hw_vecs = []
    for c in ker:
        vec = [Fr(0)] * DIM
        for i, ci in enumerate(c):
            if ci:
                vec = add(vec, smul(ci, Vw[i]))
        hw_vecs.append(vec)
    if mult:
        hw_records.append((w, mult, hw_vecs))

log(f"\n{len(hw_records)} distinct highest weights found (with multiplicity) among the 64:\n")


def su3dim(p, q):
    p, q = int(p), int(q)
    d = (p + 1) * (q + 1) * (p + q + 2)
    assert d % 2 == 0
    return d // 2


def su3name(p, q):
    p, q = int(p), int(q)
    names = {(0, 0): "1", (1, 0): "3", (0, 1): "3bar", (1, 1): "8",
             (2, 0): "6", (0, 2): "6bar", (3, 0): "10", (0, 3): "10bar",
             (2, 1): "15", (1, 2): "15bar"}
    return names.get((p, q), f"[{p},{q}]")


total_check = 0
DECOMP = []   # (spin_a, spin_b, (p,q), mult, block_dim)
for w, mult, hw_vecs in hw_records:
    m1, m2, c1, c2 = w
    assert m1 >= 0 and m2 >= 0 and c1 >= 0 and c2 >= 0, f"non-dominant highest weight {w} -- BUG"
    spin_a = m1 / 2
    spin_b = m2 / 2
    p, q = int(c1), int(c2)
    d_su3 = su3dim(p, q)
    block_dim = int(m1 + 1) * int(m2 + 1) * d_su3
    total_check += mult * block_dim
    DECOMP.append((spin_a, spin_b, (p, q), mult, block_dim))
    log(f"  highest weight (m1,m2,c1,c2)={w}  "
        f"->  (spin_T1={spin_a}, spin_T2={spin_b}; su3={su3name(p,q)}={d_su3}d)  "
        f"mult={mult}  block dim={block_dim}  [x{mult} = {mult*block_dim}]")

log(f"\nTOTAL dimension recovered from highest-weight sum = {total_check}  (expect 64) -> "
    f"{'CONFIRMED' if total_check == 64 else 'REFUTED'}")
assert total_check == 64, "highest-weight decomposition does not reconstruct the full 64-dim space"

print(f"\n[timing] step 4 done at {time.time()-t_start:.1f}s")

# ================================================================ STEP 5 ==
# claims (a)-(e), each checked exactly against DECOMP (the highest-weight
# decomposition just derived, not assumed).
log("\n" + "=" * 78)
log("STEP 5: claims (a)-(e)")
log("=" * 78)

# (a) total dim = 64
CLAIM_A = (total_check == 64)
log(f"(a) total dim = 64 : computed {total_check} -> {'CONFIRMED' if CLAIM_A else 'REFUTED'}")

# (b) invariant content (trivial under all three) = 0
inv_entries = [d for d in DECOMP if d[0] == 0 and d[1] == 0 and d[2] == (0, 0)]
inv_mult = sum(d[3] for d in inv_entries)
CLAIM_B = (inv_mult == 0)
log(f"(b) invariant content (spin_T1=0,spin_T2=0;su3=1) multiplicity = {inv_mult} "
    f"-> {'CONFIRMED zero' if CLAIM_B else 'REFUTED -- invariant(s) found: ' + str(inv_entries)}")

# (c) exactly two color-singlet spin-2 pieces, one under each su(2), dim 5 each
singlet_entries = [d for d in DECOMP if d[2] == (0, 0)]
graviton_like = [d for d in singlet_entries if d[4] == 5 and d[3] == 1]
CLAIM_C = (len(singlet_entries) == 2 and
           {(d[0], d[1]) for d in singlet_entries} == {(2, 0), (0, 2)} and
           all(d[3] == 1 and d[4] == 5 for d in singlet_entries))
log(f"(c) color-singlet pieces found: {singlet_entries}")
log(f"    exactly two, spins {{(2,0),(0,2)}}, mult 1, dim 5 each -> "
    f"{'CONFIRMED (the graviton)' if CLAIM_C else 'REFUTED'}")

# (d) remaining 54 states all colored (non-singlet su(3))
colored_entries = [d for d in DECOMP if d[2] != (0, 0)]
colored_dim = sum(d[3] * d[4] for d in colored_entries)
CLAIM_D = (colored_dim == 54) and all(d[2] != (0, 0) for d in colored_entries)
log(f"(d) colored (non-singlet) entries: {colored_entries}")
log(f"    total colored dimension = {colored_dim} (expect 54) -> "
    f"{'CONFIRMED' if CLAIM_D else 'REFUTED'}")

# (e) the only (0,0)-Lorentz-weight color-singlet states are the middle
# weights of the two spin-2 strings. A component contributes Lorentz-(0,0)
# substates iff spin_a and spin_b are BOTH integers (top weight even); among
# those substates exactly d_su3 appear, and they are color-singlet iff the
# block's own su3 label is (0,0).
lorentz00_singlet = 0
lorentz00_colored = 0
lorentz00_breakdown = []
for spin_a, spin_b, (p, q), mult, block_dim in DECOMP:
    top1, top2 = int(2 * spin_a), int(2 * spin_b)
    if top1 % 2 == 0 and top2 % 2 == 0:   # integer spins -> weight 0 is on the ladder
        d3 = su3dim(p, q)
        n00 = mult * d3
        lorentz00_breakdown.append(((spin_a, spin_b, (p, q)), n00))
        if (p, q) == (0, 0):
            lorentz00_singlet += n00
        else:
            lorentz00_colored += n00
log(f"(e) Lorentz-(0,0) state count by block: {lorentz00_breakdown}")
log(f"    color-SINGLET (0,0)-Lorentz states = {lorentz00_singlet} (expect 2)")
log(f"    color-NONsinglet (0,0)-Lorentz states = {lorentz00_colored} (expect 6 = 3+3bar middles)")
CLAIM_E = (lorentz00_singlet == 2)
log(f"    -> {'CONFIRMED: only the two graviton middles are color singlets at (0,0)' if CLAIM_E else 'REFUTED'}")

print(f"\n[timing] step 5 done at {time.time()-t_start:.1f}s")

# ================================================================ STEP 6 ==
# Robustness: rerun the ENTIRE pipeline from a DIFFERENT adjacent simple
# pair (indices 3,4 -- the same alternate choice B1138 itself used for its
# own robustness check), fully independent of slot A's root labels. If
# memo 27's structure is real (not a slot artifact) the SAME 4-piece
# 5+5+27+27bar decomposition must reappear.
log("\n" + "=" * 78)
log("STEP 6: robustness -- independent slot choice B (indices 3,4)")
log("=" * 78)


def full_pipeline(base_pair, tag):
    ladder_, (S0_, S1_, S2_) = F.run_ladder(base_pair, tag)
    if ladder_ != (16, 8, 8, 0):
        return ladder_, None
    T1_ = F.principal_triple(F.find_a2_in(S0_))
    T2_ = F.principal_triple(F.find_a2_in(S1_))
    COLOR_ = F.color_gens(S2_)
    r2_, s2_ = F.find_a2_in(S2_)
    SUB_ = T1_ + T2_ + COLOR_
    if MC.exact_rank(SUB_, DIM) != 14:
        return ladder_, None

    M_ = [[killing_vs_basis(SUB_[i], j) for j in range(DIM)] for i in range(14)]
    COMP_ = MC.nullspace_basis_exact(M_, DIM)
    if len(COMP_) != 64:
        return ladder_, None

    h1_, h2_ = T1_[1], T2_[1]
    hc1_, hc2_ = COLOR_[6], COLOR_[7]
    C4_ = [h1_, h2_, hc1_, hc2_]
    wgroups_ = defaultdict(list)
    for v in COMP_:
        quad = []
        for h in C4_:
            lam = eigen_or_none(h, v)
            if lam is None:
                return ladder_, "NONEIGEN"
            quad.append(lam)
        wgroups_[tuple(quad)].append(v)

    raisers_ = [T1_[0], T2_[0], ALG.evec(r2_), ALG.evec(s2_)]
    decomp_ = []
    tot_ = 0
    for w, Vw in wgroups_.items():
        k = len(Vw)
        R = []
        for v in Vw:
            row = []
            for op in raisers_:
                row.extend(ALG.br(op, v))
            R.append(row)
        trows = [[R[i][col] for i in range(k)] for col in range(len(R[0]))]
        ker = MC.nullspace_basis_exact(trows, k)
        if ker:
            m1, m2, c1, c2 = w
            d3 = su3dim(c1, c2)
            bd = int(m1 + 1) * int(m2 + 1) * d3
            decomp_.append((m1 / 2, m2 / 2, (int(c1), int(c2)), len(ker), bd))
            tot_ += len(ker) * bd
    return ladder_, (decomp_, tot_)


a3 = tuple(1 if k == 3 else 0 for k in range(N))
a4 = tuple(1 if k == 4 else 0 for k in range(N))
ladderB, resultB = full_pipeline((a3, a4), "memo27-verify, slot B (indices 3,4)")
log(f"slot B ladder = {ladderB}")
if resultB and resultB != "NONEIGEN":
    decompB, totB = resultB
    log(f"slot B decomposition: {sorted(decompB, key=lambda d: (-d[0], -d[1]))}")
    log(f"slot B total = {totB} (expect 64)")
    setA = sorted([(d[0], d[1], d[2], d[3], d[4]) for d in DECOMP])
    setB = sorted([(d[0], d[1], d[2], d[3], d[4]) for d in decompB])
    SLOT_MATCH = (setA == setB) and (totB == 64)
    log(f"slot A vs slot B decomposition IDENTICAL -> "
        f"{'CONFIRMED (slot-independent, not an artifact of the S0,S1,S2 choice)' if SLOT_MATCH else 'MISMATCH -- see raw lists above'}")
else:
    SLOT_MATCH = False
    log(f"slot B pipeline did not complete cleanly: {resultB}")

print(f"\n[timing] step 6 done at {time.time()-t_start:.1f}s")

# ============================================================== VERDICT ==
log("\n" + "=" * 78)
log("FINAL VERDICT")
log("=" * 78)
log(f"exact decomposition (multiset), slot A: 64 = "
    + " + ".join(f"{d[3]}x(spin_T1={d[0]},spin_T2={d[1]};su3={su3name(*d[2])}={d[4]//((int(2*d[0])+1)*(int(2*d[1])+1))}d)[dim {d[4]}]"
                  for d in sorted(DECOMP, key=lambda d: (-d[4], -d[0], -d[1]))))
log(f"(a) total dim 64:                    {'CONFIRMED' if CLAIM_A else 'REFUTED'}")
log(f"(b) invariant content = 0:            {'CONFIRMED' if CLAIM_B else 'REFUTED'}")
log(f"(c) two color-singlet spin-2 (5+5):   {'CONFIRMED' if CLAIM_C else 'REFUTED'}")
log(f"(d) remaining 54 all colored:         {'CONFIRMED' if CLAIM_D else 'REFUTED'}")
log(f"(e) only-2-singlets-at-(0,0):         {'CONFIRMED' if CLAIM_E else 'REFUTED'}")
log(f"slot-independence robustness check:   {'CONFIRMED' if SLOT_MATCH else 'NOT CONFIRMED (see above)'}")
ALL_OK = STEP12_OK and DIM64_OK and CLAIM_A and CLAIM_B and CLAIM_C and CLAIM_D and CLAIM_E
log(f"\nmemo 27 load-bearing claim (invariant content zero -> no u(1)/hypercharge "
    f"can organize in the spacetime branch's 64): "
    f"{'HOLDS -- zero invariant content confirmed exactly, by direct highest-weight enumeration' if CLAIM_B else 'FAILS'}")
log(f"\nALL CHECKS: {'CONFIRMED' if ALL_OK else 'AT LEAST ONE REFUTED -- see above'}")
print(f"\n[timing] TOTAL {time.time()-t_start:.1f}s")
# (side-effect-free: full transcript is on stdout; no run_log.txt written, so the
#  in-lock reproduction never dirties the tree)
