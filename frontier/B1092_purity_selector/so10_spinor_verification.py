"""
Independent from-scratch re-derivation: so(10) acting on the 16-dim EVEN
half-spin representation, realized on the fermionic Fock space Lambda^*(C^5),
via bilinears in creation/annihilation operators a_i^dagger, a_i (i=1..5).

Pure python3 + sympy, exact rational arithmetic throughout. No external
so(10)/Lie-algebra libraries used -- everything (Fock space, operators,
generators, commutators, ranks, nullspaces) is built and checked by hand.

Convention (Jordan-Wigner style, fixed once and for all, then VERIFIED
against the canonical anticommutation relations before being trusted):

  Basis state for S = {i_1 < i_2 < ... < i_k} subset of {1,...,5}:
      |S> = a_{i_1}^dagger a_{i_2}^dagger ... a_{i_k}^dagger |0>

  a_j^dagger |S> = 0                                  if j in S
                 = (-1)^p |S u {j}>                    otherwise, p = #{i in S : i<j}

  a_j |S>       = 0                                   if j not in S
                 = (-1)^p |S \\ {j}>                    otherwise, p = #{i in S : i<j}
"""

import itertools
from sympy import Rational, Matrix, zeros, eye

N = 5
MODES = list(range(1, N + 1))
half = Rational(1, 2)

# =================================================================
# STEP 0: Fock space basis (32-dim), and a_i, a_i^dagger as exact
#         32x32 matrices, built directly from the sign rule above.
# =================================================================
all_subsets = []
for k in range(N + 1):
    for c in itertools.combinations(MODES, k):
        all_subsets.append(frozenset(c))
DIM_FULL = len(all_subsets)
assert DIM_FULL == 32
idx = {s: i for i, s in enumerate(all_subsets)}


def act_create(S, j):
    if j in S:
        return 0, None
    p = sum(1 for m in S if m < j)
    return (-1) ** p, frozenset(S | {j})


def act_annihilate(S, j):
    if j not in S:
        return 0, None
    p = sum(1 for m in S if m < j)
    return (-1) ** p, frozenset(S - {j})


def build_op(j, dagger):
    M = zeros(DIM_FULL, DIM_FULL)
    for S in all_subsets:
        c = idx[S]
        sgn, newS = act_create(S, j) if dagger else act_annihilate(S, j)
        if sgn != 0:
            M[idx[newS], c] = sgn
    return M


ADAG = {j: build_op(j, True) for j in MODES}
A = {j: build_op(j, False) for j in MODES}
I_FULL = eye(DIM_FULL)
Z_FULL = zeros(DIM_FULL, DIM_FULL)

# =================================================================
# STEP 0b: VERIFY the canonical anticommutation relations (CAR) on
#          the full 32-dim Fock space. This is the self-consistency
#          check on the sign convention itself.
# =================================================================
car_fail = []
for i in MODES:
    for j in MODES:
        ac1 = A[i] * ADAG[j] + ADAG[j] * A[i]
        exp1 = I_FULL if i == j else Z_FULL
        if ac1 != exp1:
            car_fail.append(('{a_i,adag_j}', i, j))
        ac2 = A[i] * A[j] + A[j] * A[i]
        if ac2 != Z_FULL:
            car_fail.append(('{a_i,a_j}', i, j))
        ac3 = ADAG[i] * ADAG[j] + ADAG[j] * ADAG[i]
        if ac3 != Z_FULL:
            car_fail.append(('{adag_i,adag_j}', i, j))
CAR_OK = (len(car_fail) == 0)
print("=" * 70)
print("STEP 0: CAR relations {a_i,a_j^dagger}=delta_ij, {a_i,a_j}=0, "
      "{adag_i,adag_j}=0")
print("        verified on full 32-dim Fock space:", CAR_OK)
if not CAR_OK:
    print("        FAILURES:", car_fail)
assert CAR_OK, "Sign convention is inconsistent -- stop."

# =================================================================
# STEP 1: even subspace (16-dim), canonical ordering; verify the
#         45 candidate generators preserve it (no even<->odd leakage)
# =================================================================
even_subsets = sorted([s for s in all_subsets if len(s) % 2 == 0],
                       key=lambda s: (len(s), sorted(s)))
odd_subsets = [s for s in all_subsets if len(s) % 2 == 1]
assert len(even_subsets) == 16
eidx = {s: i for i, s in enumerate(even_subsets)}
print("\nEven-degree basis (16 states), in fixed order:")
for i, s in enumerate(even_subsets):
    print(f"  [{i:2d}] |{sorted(s)}>")


def preserves_parity(M):
    for Se in even_subsets:
        ce = idx[Se]
        for So in odd_subsets:
            ro = idx[So]
            if M[ro, ce] != 0:
                return False
    for So in odd_subsets:
        co = idx[So]
        for Se in even_subsets:
            re = idx[Se]
            if M[re, co] != 0:
                return False
    return True


def restrict_even(M):
    R = zeros(16, 16)
    for S1 in even_subsets:
        for S2 in even_subsets:
            R[eidx[S1], eidx[S2]] = M[idx[S1], idx[S2]]
    return R


# =================================================================
# STEP 2: build the 45 so(10) generators, restricted to the 16-dim
#         even space:
#           gl(5) block  E_ij = adag_i a_j - (1/2) delta_ij   (25)
#           creators     C_ij = adag_i adag_j,   i<j          (10)
#           annihilators D_ij = a_i a_j,         i<j          (10)
# =================================================================
gens = []
gen_labels = []
gl5_indices = []
cartan_indices = []
creator_indices = []
annihilator_indices = []
leakage_fail = []

for i in MODES:
    for j in MODES:
        Mfull = ADAG[i] * A[j]
        if i == j:
            Mfull = Mfull - half * I_FULL
        if not preserves_parity(Mfull):
            leakage_fail.append(('gl5', i, j))
        gens.append(restrict_even(Mfull))
        pos = len(gens) - 1
        gen_labels.append(f"E_{i}{j}")
        gl5_indices.append(pos)
        if i == j:
            cartan_indices.append(pos)

for i, j in itertools.combinations(MODES, 2):
    Mfull = ADAG[i] * ADAG[j]
    if not preserves_parity(Mfull):
        leakage_fail.append(('creator', i, j))
    gens.append(restrict_even(Mfull))
    creator_indices.append(len(gens) - 1)
    gen_labels.append(f"C_{i}{j}")

for i, j in itertools.combinations(MODES, 2):
    Mfull = A[i] * A[j]
    if not preserves_parity(Mfull):
        leakage_fail.append(('annihilator', i, j))
    gens.append(restrict_even(Mfull))
    annihilator_indices.append(len(gens) - 1)
    gen_labels.append(f"a_{i}{j}")

NGEN = len(gens)
assert NGEN == 45
LEAKAGE_OK = (len(leakage_fail) == 0)
print("\n" + "=" * 70)
print("STEP 1/2: 45 candidate generators built (25 gl(5) + 10 creators "
      "+ 10 annihilators)")
print("          even/odd block-diagonality (no leakage) verified:", LEAKAGE_OK)
if not LEAKAGE_OK:
    print("          FAILURES:", leakage_fail)
assert LEAKAGE_OK

# =================================================================
# STEP 3: linear independence of the 45 generators (as 16x16 matrices)
# =================================================================
def flatten(M):
    return [M[r, c] for r in range(16) for c in range(16)]


GEN_ROWS = Matrix([flatten(g) for g in gens])  # 45 x 256
rank_gens = GEN_ROWS.rank()
LIN_INDEP_OK = (rank_gens == 45)
print("\nSTEP 3: linear independence of the 45 generators (as 16x16 "
      f"matrices): rank = {rank_gens}  ->  PASS={LIN_INDEP_OK}")
assert LIN_INDEP_OK

# =================================================================
# STEP 4: CLOSURE under commutator: for every pair a<b, [G_a,G_b]
#         must lie in the span of the 45 generators. Exact check via
#         rank-preservation (augment and recompute rank).
# =================================================================
print("\nSTEP 4: closure under commutator -- checking all C(45,2) = 990 "
      "pairs ...")
closure_fail = []
pair_count = 0
for a in range(NGEN):
    for b in range(a + 1, NGEN):
        pair_count += 1
        comm = gens[a] * gens[b] - gens[b] * gens[a]
        row = Matrix([flatten(comm)])
        aug = GEN_ROWS.col_join(row)
        if aug.rank() != 45:
            closure_fail.append((gen_labels[a], gen_labels[b]))
CLOSURE_OK = (len(closure_fail) == 0)
print(f"        pairs checked: {pair_count}")
print(f"        CLOSURE_OK = {CLOSURE_OK}")
if not CLOSURE_OK:
    print("        FAILURES (first 20):", closure_fail[:20])

# =================================================================
# STEP 5: Cartan / rank, via the root-space (simultaneous eigenvector)
#         decomposition of ad(h_i) on the 45 generators.
#         h_i = gens[cartan_indices[i-1]], i=1..5 (mode order 1..5)
# =================================================================
print("\n" + "=" * 70)
print("STEP 5: Cartan subalgebra, rank, root decomposition")

cartan_mats = [gens[p] for p in cartan_indices]
cartan_diag_ok = all(h.is_diagonal() for h in cartan_mats)
cartan_indep_ok = (Matrix([flatten(h) for h in cartan_mats]).rank() == 5)
cartan_commute_ok = all(
    (cartan_mats[i] * cartan_mats[j] - cartan_mats[j] * cartan_mats[i]) == zeros(16, 16)
    for i in range(5) for j in range(5)
)
print(f"  5 diagonal h_i: pairwise-diagonal={cartan_diag_ok}, "
      f"linearly independent={cartan_indep_ok}, mutually commuting={cartan_commute_ok}")

# For every generator, determine its root (5-tuple) under ad(h_1..h_5),
# verifying it really IS a simultaneous eigenvector (not assumed).
roots = []
not_pure_weight = []
for a in range(NGEN):
    Ga = gens[a]
    root = []
    for i in range(5):
        h = cartan_mats[i]
        C = h * Ga - Ga * h
        if C == zeros(16, 16):
            root.append(Rational(0))
            continue
        # find a nonzero entry of Ga to read off the candidate eigenvalue
        found = False
        for r in range(16):
            for c in range(16):
                if Ga[r, c] != 0:
                    lam = C[r, c] / Ga[r, c]
                    found = True
                    break
            if found:
                break
        if C != lam * Ga:
            not_pure_weight.append((a, i))
            root.append(None)
        else:
            root.append(lam)
    roots.append(tuple(root))

ROOT_VECTORS_OK = (len(not_pure_weight) == 0)
print(f"  every generator is a simultaneous eigenvector of ad(h_1..h_5): {ROOT_VECTORS_OK}")
if not ROOT_VECTORS_OK:
    print("    FAILURES:", not_pure_weight)

zero_root = [a for a in range(NGEN) if roots[a] == (0, 0, 0, 0, 0)]
CENTRALIZER_IS_CARTAN = (set(zero_root) == set(cartan_indices))
print(f"  generators with zero root (centralizer of full Cartan): "
      f"{len(zero_root)} -> {[gen_labels[a] for a in zero_root]}")
print(f"  centralizer(Cartan) == Cartan exactly (self-centralizing, "
      f"confirming rank=5, no larger toral subalgebra): {CENTRALIZER_IS_CARTAN}")

nonzero_roots = [roots[a] for a in range(NGEN) if a not in cartan_indices]
distinct_nonzero_roots = set(nonzero_roots)
print(f"  number of nonzero roots: {len(nonzero_roots)}  "
      f"(distinct root vectors: {len(distinct_nonzero_roots)}, "
      f"expected 40 roots of D5, i.e. all length-1 sqrt(2)... here "
      f"normalized as +-e_i+-e_j)")

RANK_OK = cartan_diag_ok and cartan_indep_ok and cartan_commute_ok and CENTRALIZER_IS_CARTAN and ROOT_VECTORS_OK

# extra semisimplicity evidence: trace-form non-degeneracy + trivial center
K = zeros(45, 45)
for a in range(45):
    for b in range(45):
        K[a, b] = (gens[a] * gens[b]).trace()
TRACE_FORM_NONDEGENERATE = (K.det() != 0)
print(f"  trace form <X,Y>=tr(XY) on the 45-dim algebra non-degenerate "
      f"(supporting reductivity): {TRACE_FORM_NONDEGENERATE}")
CENTER_TRIVIAL = (len(zero_root) == 5)  # zero-root space IS the center since all roots accounted for
print(f"  center of the 45-dim algebra trivial (=Cartan has no extra "
      f"invariant direction beyond itself... center dim via zero-root "
      f"count consistent with simple, non-abelian): "
      f"zero-weight space dim = {len(zero_root)} (center of a semisimple "
      f"algebra is 0; here the zero-WEIGHT space equals Cartan itself, "
      f"as expected for a semisimple algebra where Cartan is self-normalizing)")

# =================================================================
# STEP 6: spinor weights on the 16-dim rep + PARITY control
# =================================================================
print("\n" + "=" * 70)
print("STEP 6: weights of the 16 basis vectors + parity control")

half = Rational(1, 2)

def basis_vec(S):
    v = zeros(16, 1)
    v[eidx[frozenset(S)]] = 1
    return v


weight_mismatch = []
weights = []
for S in even_subsets:
    formula_w = tuple(half if i in S else -half for i in MODES)
    # cross-check against the actual matrix diagonal entries
    matrix_w = tuple(cartan_mats[i - 1][eidx[S], eidx[S]] for i in MODES)
    if formula_w != matrix_w:
        weight_mismatch.append((S, formula_w, matrix_w))
    weights.append(matrix_w)

WEIGHTS_MATCH_FORMULA = (len(weight_mismatch) == 0)
print(f"  hand-formula weights match matrix diagonal read-off exactly: "
      f"{WEIGHTS_MATCH_FORMULA}")
if weight_mismatch:
    print("    MISMATCHES:", weight_mismatch)

ALL_WEIGHT_VECTORS_OK = True  # by construction (basis states are simultaneous
                               # eigenvectors of diagonal h_i -- manifest since
                               # h_i are diagonal matrices in this basis)

parities = [sum(1 for x in w if x < 0) % 2 for w in weights]
PARITY_CONSTANT = (len(set(parities)) == 1)
print(f"  all 16 basis vectors are weight vectors with weights in "
      f"(+-1/2)^5: {ALL_WEIGHT_VECTORS_OK}")
print(f"  parity (# of minus signs mod 2) for each of the 16 states:")
for S, w, p in zip(even_subsets, weights, parities):
    print(f"    |{sorted(S)!s:14s}>  weight={tuple(str(x) for x in w)}  "
          f"#minus={sum(1 for x in w if x<0)}  parity={p}")
print(f"  PARITY CONSTANT across all 16 (single chiral half): "
      f"{PARITY_CONSTANT}  (constant value = {parities[0] if PARITY_CONSTANT else 'N/A'})")


# =================================================================
# STEP 7: stabilizer machinery
# =================================================================
print("\n" + "=" * 70)
print("STEP 7: stabilizer machinery (definitions)")
print("""
  For a nonzero vector v in the 16-dim rep, and the map
      phi_v : C^45 -> C^16,   phi_v(c) = ( sum_a c_a G_a ) v
  define:
    LITERAL stabilizer   S_lit(v)  = ker(phi_v)               [X v = 0 exactly]
    PROJECTIVE stabilizer S_proj(v) = phi_v^{-1}( C.v )        [X v = lambda v, any scalar lambda]
  Always S_lit(v) subseteq S_proj(v) subseteq so(10), and
      dim S_proj(v) - dim S_lit(v) in {0,1}
  (the +1 occurs iff v is an eigenvector of the residual quotient,
   which -- since so(10) is semisimple, has NO nontrivial characters --
   is a genuine extra coincidence, not a scaling symmetry of so(10) itself;
   it happens whenever some X in so(10) has v as an honest eigenvector
   with nonzero eigenvalue.)

  TORAL part of a stabilizer S is computed, per the task's own operational
  definition, as S intersected with the fixed Cartan h_1..h_5:
  i.e. restrict phi_v to the 5 Cartan generators only.
""")


def apply_all_gens_matrix(v):
    """16x45 matrix whose a-th column is G_a . v"""
    cols = [gens[a] * v for a in range(NGEN)]
    M = zeros(16, NGEN)
    for a in range(NGEN):
        for r in range(16):
            M[r, a] = cols[a][r]
    return M


def stabilizer_report(v, label, cartan_idx=cartan_indices):
    M = apply_all_gens_matrix(v)                 # 16x45
    lit_ns = M.nullspace()
    proj_M = M.row_join(-v)                      # 16x46
    proj_ns = proj_M.nullspace()

    Mc = M[:, cartan_idx]                         # 16x5, restricted to Cartan
    toral_lit_ns = Mc.nullspace()
    proj_Mc = Mc.row_join(-v)                     # 16x6
    toral_proj_ns = proj_Mc.nullspace()

    # sanity: verify each nullspace vector really works, exactly
    for x in lit_ns:
        assert M * x == zeros(16, 1)
    for x in proj_ns:
        c = x[:45, 0]
        lam = x[45, 0]
        assert M * c == lam * v
    for x in toral_lit_ns:
        assert Mc * x == zeros(16, 1)
    for x in toral_proj_ns:
        c = x[:5, 0]
        lam = x[5, 0]
        assert Mc * c == lam * v

    print(f"  [{label}]")
    print(f"    literal stabilizer dim    = {len(lit_ns)}")
    print(f"    projective stabilizer dim = {len(proj_ns)}   "
          f"(delta = {len(proj_ns) - len(lit_ns)})")
    print(f"    toral part (literal, Cartan ∩ S_lit)    = {len(toral_lit_ns)}")
    print(f"    toral part (projective, Cartan ∩ S_proj) = {len(toral_proj_ns)}")
    return {
        'lit_dim': len(lit_ns), 'proj_dim': len(proj_ns),
        'toral_lit_dim': len(toral_lit_ns), 'toral_proj_dim': len(toral_proj_ns),
        'lit_ns': lit_ns, 'proj_ns': proj_ns,
    }


def classify_action_per_generator(v, label):
    """For each of the 45 individual (single) generators, classify
    G_a . v as 'zero', 'proportional (nonzero scalar)' or 'other'."""
    zero_list, prop_list, other_list = [], [], []
    for a in range(NGEN):
        Gv = gens[a] * v
        if Gv == zeros(16, 1):
            zero_list.append(a)
        else:
            # check proportional to v
            ratio = None
            ok_prop = True
            for r in range(16):
                if v[r] == 0:
                    if Gv[r] != 0:
                        ok_prop = False
                        break
                else:
                    this_ratio = Gv[r] / v[r]
                    if ratio is None:
                        ratio = this_ratio
                    elif this_ratio != ratio:
                        ok_prop = False
                        break
            if ok_prop and Gv == ratio * v:
                prop_list.append((a, ratio))
            else:
                other_list.append(a)
    print(f"  [{label}] per-generator action on v (45 individual generators, "
          f"NOT combinations):")
    print(f"    exactly ZERO:              {len(zero_list)}  -> "
          f"{[gen_labels[a] for a in zero_list]}")
    print(f"    PROPORTIONAL (lambda!=0):  {len(prop_list)}  -> "
          f"{[(gen_labels[a], str(l)) for a,l in prop_list]}")
    print(f"    other (not proportional):  {len(other_list)}")
    return zero_list, prop_list, other_list


# =================================================================
# ITEM 1: PURE SPINOR |0>
# =================================================================
print("\n" + "=" * 70)
print("ITEM 1: PURE SPINOR |0>  (vacuum, degree 0)")

v0 = basis_vec(set())
classify_action_per_generator(v0, "|0>")
res0 = stabilizer_report(v0, "|0>")

item1_lit34 = (res0['lit_dim'] == 34)
item1_toral_lit4 = (res0['toral_lit_dim'] == 4)
item1_proj = res0['proj_dim']
item1_toral_proj = res0['toral_proj_dim']

print(f"\n  --- ITEM 1 claim check ---")
print(f"  claimed dim 34 matches the LITERAL (exact, X|0>=0) stabilizer: "
      f"{item1_lit34}  (computed {res0['lit_dim']})")
print(f"  claimed dim 34 vs the PROJECTIVE (X|0>=lambda|0>) stabilizer: "
      f"computed {item1_proj}  "
      f"(these DIFFER by exactly the scalar direction: every one of the "
      f"5 diagonal h_i individually satisfies h_i|0>=(-1/2)|0>, a nonzero "
      f"eigenvalue, so the FULL 25-dim gl(5) -- not just its traceless "
      f"24-dim sl(5) part -- lies in the projective stabilizer)")
print(f"  toral part of LITERAL stabilizer = {res0['toral_lit_dim']} "
      f"(claim: rank drops 5->4): {item1_toral_lit4}")
print(f"  toral part of PROJECTIVE stabilizer = {res0['toral_proj_dim']} "
      f"(all 5 h_i stabilize |0> projectively, since |0> is simultaneously "
      f"an eigenvector of every h_i)")

# =================================================================
# ITEM 2: GENERIC SPINORS
# =================================================================
print("\n" + "=" * 70)
print("ITEM 2: GENERIC SPINORS")

# v1: literally the prompt's suggested example, with mildly generic
# (distinct, nonzero) rational coefficients
v1 = 2 * basis_vec(set()) + 3 * basis_vec({1, 2, 3, 4}) + 5 * basis_vec({1, 2})
print("\n  v1 = 2|0> + 3|1234> + 5|12>   (the prompt's literal example, "
      "support size 3 of 16)")
res1 = stabilizer_report(v1, "v1 (prompt's example)")

# v2, v3: fully random rational combinations of ALL 16 basis vectors,
# two different seeds, to guard against accidental non-genericity
import random

def random_vector(seed, lo=-30, hi=30):
    rng = random.Random(seed)
    coeffs = []
    for _ in range(16):
        c = 0
        while c == 0:
            c = rng.randint(lo, hi)
        coeffs.append(Rational(c))
    v = Matrix(coeffs)
    return v, coeffs

v2, coeffs2 = random_vector(20260817)
print(f"\n  v2 = random combination of all 16 basis states, coeffs (seed A) = {coeffs2}")
res2 = stabilizer_report(v2, "v2 (random #1)")

v3, coeffs3 = random_vector(918273645)
print(f"\n  v3 = random combination of all 16 basis states, coeffs (seed B) = {coeffs3}")
res3 = stabilizer_report(v3, "v3 (random #2)")

print(f"\n  --- ITEM 2 claim check ---")
print(f"  v1 (prompt's literal example) literal stabilizer dim = {res1['lit_dim']}, "
      f"toral(literal) = {res1['toral_lit_dim']}")
print(f"  v2 (fully random) literal stabilizer dim = {res2['lit_dim']}, "
      f"toral(literal) = {res2['toral_lit_dim']}")
print(f"  v3 (fully random) literal stabilizer dim = {res3['lit_dim']}, "
      f"toral(literal) = {res3['toral_lit_dim']}")
item2_generic_agree = (res2['lit_dim'] == res3['lit_dim'] and
                        res2['toral_lit_dim'] == res3['toral_lit_dim'] == 0)
item2_lit29 = (res2['lit_dim'] == 29 and res3['lit_dim'] == 29)
item2_v1_matches_generic = (res1['lit_dim'] == res2['lit_dim'] and
                             res1['toral_lit_dim'] == res2['toral_lit_dim'])
print(f"  v2 and v3 agree with each other (both are honestly generic): "
      f"{item2_generic_agree}")
print(f"  claimed generic dim 29 matches fully-random v2,v3: {item2_lit29}")
print(f"  does the PROMPT's example vector v1 behave like a generic vector? "
      f"{item2_v1_matches_generic}  "
      f"(if False: v1 has an ACCIDENTAL extra symmetry not present for a "
      f"truly generic spinor -- exactly the failure mode the prompt's own "
      f"'try >=2 generic vectors' instruction is designed to catch)")

# =================================================================
# ITEM 3: TRANSITIVITY ON THE PURE CONE
# =================================================================
print("\n" + "=" * 70)
print("ITEM 3: TRANSITIVITY ON THE PURE SPINOR CONE")

orbit_dim_via_lie_algebra = 45 - res0['lit_dim']
print(f"  dim so(10) - dim S_lit(|0>) = 45 - {res0['lit_dim']} = "
      f"{orbit_dim_via_lie_algebra}")
print(f"  projective pure spinor variety S_10 has dim 10 (given); "
      f"cone = variety + scaling direction = 10 + 1 = 11")
item3_orbit11 = (orbit_dim_via_lie_algebra == 11)
print(f"  orbit_dim == 11 == 10+1 : {item3_orbit11}")

# cross-check via the PROJECTIVE stabilizer directly: dim(G/P) should be
# 45 - dim(S_proj(|0>)) and should equal 10 exactly (the variety itself,
# no +1, since working projectively already quotients the cone direction)
proj_orbit_dim = 45 - res0['proj_dim']
print(f"  cross-check: 45 - dim S_proj(|0>) = 45 - {res0['proj_dim']} = "
      f"{proj_orbit_dim}  (expected: exactly 10, the bare projective "
      f"variety dimension, since S_proj is the parabolic stabilizing the "
      f"LINE, so so(10)/S_proj IS S_10 itself)")
item3_proj_orbit10 = (proj_orbit_dim == 10)

# second pure spinor: top wedge on modes {1,2,3,4} (degree 4, even)
print("\n  second pure spinor: w = a_1^dagger a_2^dagger a_3^dagger a_4^dagger |0>"
      "  (degree 4, mode 5 empty)")
w = basis_vec({1, 2, 3, 4})
classify_action_per_generator(w, "w")
resw = stabilizer_report(w, "w = |1234>")

item3_same_dim = (resw['lit_dim'] == res0['lit_dim'])
print(f"\n  --- ITEM 3 claim check ---")
print(f"  dim S_lit(w) = {resw['lit_dim']}  vs  dim S_lit(|0>) = {res0['lit_dim']}"
      f"   -> SAME DIMENSION (orbit-homogeneity evidence): {item3_same_dim}")
print(f"  dim S_proj(w) = {resw['proj_dim']}  vs  dim S_proj(|0>) = {res0['proj_dim']}"
      f"   -> SAME: {resw['proj_dim'] == res0['proj_dim']}")
print(f"  (note: a vector attaining the MAXIMAL possible literal-stabilizer "
      f"dimension 34 among nonzero spinors is, by the standard "
      f"highest-weight-orbit / minimal-nilpotent-orbit characterization, "
      f"exactly the defining property of purity for a spinor of so(10); "
      f"so this dimension match is itself independent evidence that w IS "
      f"a pure spinor, not merely that it 'is homogeneous with' one.)")


# =================================================================
# FINAL SUMMARY
# =================================================================
print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print(f"""
SETUP
  CAR relations verified on 32-dim Fock space ......... {CAR_OK}
  45 generators preserve even/odd grading (no leak) .... {LEAKAGE_OK}
  45 generators linearly independent ................... {LIN_INDEP_OK}
  closure under commutator (all 990 pairs) ............. {CLOSURE_OK}
  Cartan (5 diag h_i): indep/commuting/self-centralizing  {RANK_OK}
  trace-form non-degenerate on the 45-dim algebra ...... {TRACE_FORM_NONDEGENERATE}
  all 16 basis vectors are weight vectors in (+-1/2)^5 .. {ALL_WEIGHT_VECTORS_OK}
  PARITY CONSTANT across all 16 (single chiral half) ... {PARITY_CONSTANT}

ITEM 1 (pure spinor |0>)
  literal stabilizer dim S_lit(|0>) = {res0['lit_dim']}   [claim 34]        -> {'PASS' if item1_lit34 else 'FAIL'}
  projective stabilizer dim S_proj(|0>) = {res0['proj_dim']}  [claim conflates with 34] -> honest value reported, see note
  toral(literal) = {res0['toral_lit_dim']}  [claim: rank drops 5->4]        -> {'PASS' if item1_toral_lit4 else 'FAIL'}
  toral(projective) = {res0['toral_proj_dim']}  [reductive rank of parabolic = 4+1]  -> {'PASS' if item1_toral_proj==5 else 'FAIL'}

ITEM 2 (generic spinor)
  v1 (prompt's literal example) lit dim = {res1['lit_dim']}, toral = {res1['toral_lit_dim']}
  v2 (random #1)                lit dim = {res2['lit_dim']}, toral = {res2['toral_lit_dim']}
  v3 (random #2)                lit dim = {res3['lit_dim']}, toral = {res3['toral_lit_dim']}
  generic (v2,v3) literal stabilizer = 29  [claim 29]         -> {'PASS' if item2_lit29 else 'FAIL'}
  generic (v2,v3) toral part = 0           [claim 0]          -> {'PASS' if (res2['toral_lit_dim']==0 and res3['toral_lit_dim']==0) else 'FAIL'}
  v1 matches generic behaviour?                                -> {'YES' if item2_v1_matches_generic else 'NO -- v1 is NOT generic, see note'}

ITEM 3 (transitivity)
  45 - dim S_lit(|0>) = {orbit_dim_via_lie_algebra}  [claim 11 = 10+1]      -> {'PASS' if item3_orbit11 else 'FAIL'}
  45 - dim S_proj(|0>) = {proj_orbit_dim}  [cross-check: should be 10]     -> {'PASS' if item3_proj_orbit10 else 'FAIL'}
  second pure spinor w=|1234>: dim S_lit(w) = {resw['lit_dim']}  [claim: same as |0>, 34] -> {'PASS' if item3_same_dim else 'FAIL'}
""")
print("=" * 70)
print("DONE")
