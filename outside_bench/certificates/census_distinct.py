#!/usr/bin/env python3
"""CELL A6 -- CENSUS ENRICHMENT: EXACT ORBIT DIMENSIONS FOR THE 20 CHARACTERISTICS.

Reuses cp1_strata.py's construction (itself built on the twisted_double.py e6
stack: exact Chevalley basis ROOTS/br/evec/smul_, DIM=78, N=6) to rebuild, from
scratch, all 20 dominant {0,1,2}-labelings c of the E6 Cartan that admit an
exact sl2 triple (e, H_c, f) with a generic e in the +2 grade piece. For each
of the 20 nilpotents e, the centralizer z(e) = ker(ad e) on the full 78-dim
adjoint is computed by EXACT rational-arithmetic rank (Fraction elimination,
no floating point), giving the orbit dimension dim O_e = 78 - dim z(e).

PREREGISTERED FACTS (every one is backed by an assert below):
 (1) All 20 sl2 triples (e,h,f) rebuilt from the 729-labeling sweep satisfy,
     exactly over Q: [e,f] = h, [h,e] = 2e, [h,f] = -2f.
 (2) For each of the 20, dim ker(ad e) is computed by exact rank of the
     78x78 matrix of ad(e) acting on the Chevalley basis (72 root vectors +
     6 Cartan generators = 78 = DIM, confirmed a genuine basis by its being
     exactly the enumeration basis of the underlying stack). Hence orbit dim
     = 78 - rank. The resulting *multiset* of the 20 orbit dimensions was
     ORIGINALLY going to be compared, for equality, against a CITED-attempt
     multiset copied into this docstring's first draft:
         [22,32,40,42,46,48,50,52,54,54,56,58,60,60,62,64,64,66,68,70]
     (attributed source: Carter, "Finite Groups of Lie Type", Ch.13, E6 orbit
     table). Per protocol that equality assert WAS RUN and FAILED -- see the
     ERROR LOG below. The claim is therefore corrected: the exact computed
     multiset is reported as the result, and is instead checked against two
     independent, individually-CITED closed-form facts that do not depend on
     the (evidently mistranscribed) reference list: the regular/principal
     nilpotent orbit of a semisimple Lie algebra g has dimension exactly
     dim(g) - rank(g) (Kostant: the centralizer of a regular nilpotent has
     dimension = rank(g)), and the minimal nonzero nilpotent orbit has
     dimension exactly 2*h^vee(g) - 2 where h^vee is the dual Coxeter number
     (h^vee(E6) = 12, CITED). Both are asserted against the computed extremes.
 (3) The full pairing (dominant characteristic label c -> exact orbit dim) is
     printed as a 20-row table, together with a position-by-position diff
     against the (mistranscribed) reference list from fact (2)'s first draft,
     filed as data rather than forced to agree.

ERROR LOG (machine-caught, corrected in this final version):
 - Preregistered fact (2), first draft: asserted computed_sorted_multiset ==
   sorted([22,32,40,42,46,48,50,52,54,54,56,58,60,60,62,64,64,66,68,70]).
   MACHINE RESULT: assert failed. Computed (exact rank, Fraction arithmetic):
   [22,32,40,42,46,48,50,52,54,56,58,60,60,62,64,64,66,68,70,72]. Position-by-
   position (both ascending) the two lists agree on the first 9 entries
   (22..54) plus two coincidental index-alignments at the shared duplicated-
   60 and duplicated-64 slots (11/20 total), then diverge everywhere else:
   the supplied reference list repeats 54 a second time and tops out at 70,
   while the computed list has a single 54 and tops out at 72, i.e. the
   reference list is exactly the computed list with entry "72" deleted and
   entry "54" duplicated to keep the count at 20 -- the signature of a
   transcription slip, not a computational error.
   MECHANISM IDENTIFIED / CORRECTION: the computed maximum, 72, occurs at the
   principal characteristic c=(2,2,2,2,2,2), where the code independently
   measured dim ker(ad e) = 6 exactly. By Kostant's theorem (CITED) the
   centralizer of ANY regular nilpotent in a semisimple Lie algebra has
   dimension exactly rank(g); here rank(E6) = N = 6, so dim ker(ad e) = 6 is
   forced and dim O = 78 - 6 = 72 is the necessarily-correct value for the
   regular orbit -- 70 cannot be the E6 regular-orbit dimension. The claim in
   fact (2) was corrected accordingly: drop the false equality assert, add
   the two independent closed-form checks above (asserted below and both
   passing), and report the reference-list mismatch as filed data.

FENCE: this corroborates the cited completeness fact (E6 has exactly 20
nonzero nilpotent orbits) with an independently computed, exact orbit-dimension
invariant per stratum; it is NOT a completeness proof. Jacobson-Morozov
(existence/conjugacy of sl2-triples for each nilpotent) and the theorem that
the dominant characteristic (weighted Dynkin diagram) is a complete conjugacy
invariant are CITED, not re-derived. The Bala-Carter dimension table itself is
CITED reference data (comment above); everything else (the 20 triples, all 20
centralizer ranks, the exact bracket identities) is computed and asserted.
"""
import os, itertools
from fractions import Fraction as F
from collections import Counter

SCR = os.path.dirname(os.path.abspath(__file__))
src = open(SCR + "/twisted_double.py").read()
exec(src[:src.index("# ---------------- stage 4")])
# provides: ROOTS (72 e6 roots), DIM=78, N=6, evec, br, smul_, rho27_Q, ...

random_seed_note = "cp1_strata.py's construction is deterministic-seeded (seed=4); reused verbatim below."
import random
random.seed(4)

# ---- rebuild the Cartan matrix from brackets (exactly as cp1_strata.py does) ----
SIMPLE = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]


def hvec(coeffs):
    h = [F(0)] * DIM
    for k in range(N):
        h[k] = F(coeffs[k])
    return h


A = [[None] * N for _ in range(N)]
for j in range(N):
    hj = hvec(SIMPLE[j])
    for i in range(N):
        ei = evec(SIMPLE[i])
        brr = br(hj, ei)
        val = None
        for k in range(DIM):
            if ei[k] != 0:
                val = brr[k] / ei[k]
                break
        assert all(brr[k] == val * ei[k] for k in range(DIM))
        A[i][j] = val


def grade(root, c):
    return sum(F(root[k]) * c[k] for k in range(N))


def solve_lin(Mrows, rhs):
    m = len(Mrows)
    n = len(Mrows[0]) if m else 0
    aug = [row[:] + [rhs[i]] for i, row in enumerate(Mrows)]
    piv = []
    r = 0
    for col in range(n):
        p = None
        for i in range(r, m):
            if aug[i][col] != 0:
                p = i
                break
        if p is None:
            continue
        aug[r], aug[p] = aug[p], aug[r]
        pv = aug[r][col]
        aug[r] = [x / pv for x in aug[r]]
        for i in range(m):
            if i != r and aug[i][col] != 0:
                f_ = aug[i][col]
                aug[i] = [x - f_ * y for x, y in zip(aug[i], aug[r])]
        piv.append(col)
        r += 1
        if r == m:
            break
    for i in range(r, m):
        if aug[i][n] != 0:
            return None
    y = [F(0)] * n
    for i, col in enumerate(piv):
        y[col] = aug[i][n]
    return y


def inv_matrix(M):
    n = len(M)
    aug = [[F(M[i][j]) for j in range(n)] + [F(1) if k == i else F(0) for k in range(n)] for i in range(n)]
    for col in range(n):
        p = next(i for i in range(col, n) if aug[i][col] != 0)
        aug[col], aug[p] = aug[p], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for i in range(n):
            if i != col and aug[i][col] != 0:
                f_ = aug[i][col]
                aug[i] = [x - f_ * y for x, y in zip(aug[i], aug[col])]
    return [row[n:] for row in aug]


Ainv = inv_matrix(A)


def Hc(c):
    t = [sum(Ainv[i][j] * F(c[j]) for j in range(N)) for i in range(N)]
    return hvec(t)


def is_characteristic(c, tries=4):
    H = Hc(c)
    P2 = [r for r in ROOTS if grade(r, c) == 2]
    if not P2:
        return None
    M2 = [r for r in ROOTS if grade(r, c) == -2]
    basneg = [evec(r) for r in M2]
    for t in range(tries):
        xs = [F(random.randint(1, 9)) for _ in P2]
        e = [F(0)] * DIM
        for x, r in zip(xs, P2):
            e = [a + x * b for a, b in zip(e, evec(r))]
        cols = [br(e, bn) for bn in basneg]
        Mrows = [[cols[j][i] for j in range(len(cols))] for i in range(DIM)]
        y = solve_lin(Mrows, H)
        if y is not None:
            f = [F(0)] * DIM
            for yy, bn in zip(y, basneg):
                f = [a + yy * b for a, b in zip(f, bn)]
            assert br(e, f) == H
            assert br(H, e) == smul_(2, e) and br(H, f) == smul_(-2, f)
            return (e, H, f)
    return None


# ---- 1. full enumeration of the 20 nonzero characteristics ----
chars = {}
for c in itertools.product((0, 1, 2), repeat=N):
    if all(x == 0 for x in c):
        continue
    w = is_characteristic(c)
    if w is not None:
        chars[c] = w
print(f"nonzero nilpotent characteristics found: {len(chars)} (CONTROL: expect 20)")
assert len(chars) == 20

# PREREGISTERED FACT (1): every rebuilt triple obeys the exact sl2 relations.
for c, (e, h, f) in chars.items():
    assert br(e, f) == h, f"[e,f]!=h failed at c={c}"
    assert br(h, e) == smul_(2, e), f"[h,e]!=2e failed at c={c}"
    assert br(h, f) == smul_(-2, f), f"[h,f]!=-2f failed at c={c}"
print("fact (1) VERIFIED: all 20 triples satisfy [e,f]=h, [h,e]=2e, [h,f]=-2f exactly.")

# ---- 2. exact centralizer dimension z(e) = dim ker(ad e) on the full 78-dim adjoint ----
# basis: 72 root vectors (evec(r) for r in ROOTS) + 6 Cartan generators (hvec(SIMPLE[i]))
ADJ_BASIS = [evec(r) for r in ROOTS] + [hvec(SIMPLE[i]) for i in range(N)]
assert len(ADJ_BASIS) == DIM == 78  # basis must span the full 78-dim adjoint


def rank_exact(Mrows, ncols):
    """Exact rank via Fraction Gaussian elimination. Mrows: list of row-lists length ncols."""
    aug = [row[:] for row in Mrows]
    m = len(aug)
    r = 0
    for col in range(ncols):
        p = next((i for i in range(r, m) if aug[i][col] != 0), None)
        if p is None:
            continue
        aug[r], aug[p] = aug[p], aug[r]
        pv = aug[r][col]
        aug[r] = [x / pv for x in aug[r]]
        for i in range(m):
            if i != r and aug[i][col] != 0:
                fq = aug[i][col]
                aug[i] = [x - fq * y for x, y in zip(aug[i], aug[r])]
        r += 1
        if r == m:
            break
    return r


def centralizer_dim(e):
    """dim ker(ad e) via exact rank of the (DIM x DIM) matrix of ad(e) on ADJ_BASIS."""
    img_cols = [br(e, b) for b in ADJ_BASIS]  # each is a DIM-vector = ad(e)(basis vector)
    # matrix with these as COLUMNS -> Mrows[i][j] = img_cols[j][i]
    Mrows = [[img_cols[j][i] for j in range(len(img_cols))] for i in range(DIM)]
    rk = rank_exact(Mrows, len(img_cols))
    return DIM - rk


# The reference multiset as first drafted from the prompt's instructions (kept verbatim
# for the diff below -- this is the list the FIRST run's equality assert failed against).
REFERENCE_DRAFT_DIMS = [22, 32, 40, 42, 46, 48, 50, 52, 54, 54, 56, 58, 60, 60, 62, 64, 64, 66, 68, 70]
assert len(REFERENCE_DRAFT_DIMS) == 20  # sanity on the reference list itself

results = {}
for c in sorted(chars):
    e, h, f = chars[c]
    z = centralizer_dim(e)
    dimO = DIM - z
    results[c] = dimO

computed_dims_sorted = sorted(results.values())
print(f"\ncomputed orbit-dimension multiset (sorted, exact): {computed_dims_sorted}")
print(f"reference draft multiset (sorted):                 {sorted(REFERENCE_DRAFT_DIMS)}")

MATCH = (computed_dims_sorted == sorted(REFERENCE_DRAFT_DIMS))
print("MATCH with reference draft:" , MATCH,
      "(expected False -- filed as data per protocol, see ERROR LOG in docstring)")
assert not MATCH  # this IS the (corrected) preregistered expectation: they disagree, and we know why

# PREREGISTERED FACT (2), corrected form: two independent CITED closed-form checks
# that do not depend on the mistranscribed reference list.
principal_c = (2, 2, 2, 2, 2, 2)
assert principal_c in chars  # the all-2 labeling must be among the 20 (it is the regular one)
e_reg, h_reg, f_reg = chars[principal_c]
z_reg = centralizer_dim(e_reg)
# Kostant's theorem (CITED): centralizer of a regular nilpotent has dim = rank(g) = N.
assert z_reg == N, f"Kostant check failed: dim z(e_regular)={z_reg}, expected rank={N}"
assert results[principal_c] == DIM - N == 72
print(f"Kostant check PASSED: dim z(e_regular) = {z_reg} = rank(E6) = {N};"
      f" regular orbit dim = {DIM}-{N} = {results[principal_c]}.")

DUAL_COXETER_E6 = 12  # CITED (standard tabulated invariant of E6)
minimal_orbit_dim_expected = 2 * DUAL_COXETER_E6 - 2  # CITED formula, minimal nonzero nilpotent orbit
assert min(results.values()) == minimal_orbit_dim_expected == 22
print(f"minimal-orbit check PASSED: min computed dim = {min(results.values())} "
      f"= 2*h^vee(E6)-2 = 2*{DUAL_COXETER_E6}-2 = {minimal_orbit_dim_expected}.")

# CITED structural fact: nilpotent orbit dimensions in a semisimple Lie algebra are always even
# (the orbit carries a G-invariant symplectic form, the Kirillov-Kostant-Souriau form).
assert all(d % 2 == 0 for d in results.values())
print("evenness check PASSED: all 20 computed orbit dimensions are even.")

print("fact (2) VERIFIED (corrected form): computed multiset disagrees with the reference draft"
      " exactly where Kostant's theorem independently pins the regular-orbit value to 72"
      " (not 70), corroborating the computation rather than the reference draft.")

# ---- 3. the pairing table: characteristic label -> exact orbit dimension ----
print("\nTHE 20-ROW TABLE (characteristic c -> exact orbit dim, 78 - dim ker(ad e)):")
print(f"{'label c':<20} {'dim O_e':>8}")
for c in sorted(chars, key=lambda cc: (results[cc], cc)):
    print(f"{str(c):<20} {results[c]:>8d}")

# position-by-position diff against the reference draft (both ascending) -- filed as data,
# NOT asserted to match (see fact (2) correction above).
pairs_sorted = sorted(results.items(), key=lambda kv: kv[1])
ref_sorted = sorted(REFERENCE_DRAFT_DIMS)
print("\nposition-by-position diff (computed dim vs reference-draft dim, both ascending):")
n_agree = 0
for i, (c, d) in enumerate(pairs_sorted):
    rd = ref_sorted[i]
    ok = (d == rd)
    n_agree += int(ok)
    print(f"  #{i+1:2d}  c={str(c):<20} computed={d:3d}  reference-draft={rd:3d}  {'agree' if ok else 'DIFFERS'}")
assert n_agree == 11  # PREREGISTERED (corrected): positions 1-9 (dims 22..54) plus two coincidental
# index-alignments at the duplicated-60 and duplicated-64 slots (positions 13, 16) agree by
# construction of both lists sharing those duplicate pairs; all other 9 positions differ.
# (First corrected-run attempt asserted 10 by miscount; machine reported 11 -- corrected here.)
print(f"\n{n_agree}/20 positions agree with the reference draft; disagreement begins exactly at the"
      " point where the draft's duplicated-54 / missing-72 transcription error takes effect.")

print(f"\nCELL A6 SUMMARY: 20/20 sl2 triples rebuilt exactly; 20/20 exact centralizer ranks computed;")
print(f"orbit-dimension multiset = {computed_dims_sorted}.")
print("This computed multiset, not the mistranscribed reference draft, is the certified result;")
print("it is independently corroborated by Kostant's theorem (regular orbit = dim g - rank = 72)")
print("and by the minimal-orbit formula (2*h^vee-2 = 22), both CITED, plus universal evenness.")
print("FENCE: corroboration of cited completeness (20 nonzero orbits) via independent exact")
print("       dimension data; NOT a completeness proof. Jacobson-Morozov and the theorem that")
print("       the dominant characteristic is a complete conjugacy invariant remain CITED.")
