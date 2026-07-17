"""B662 CELL C -- L103: the golden sigma*-matrix repair.

Prereg: frontier/B662_successor_campaign/CAMPAIGN_PREREGISTRATION.md, CELL C
clause (sealed before launch). Outcomes: gap REPAIRED (matrix persisted +
laws verified + one invariant cross-checked) / obstruction stated.

BACKGROUND. B638 (b638_swap.py, gate G2) computed the deck-swap action
sigma* on the five H^1(D;27) classes of the golden (figure-eight) unbent
weld double IN-FLIGHT -- the matrix exists only as five printed lines in
b638_output.txt; no machine-readable artifact was persisted (the silver
analogue sigma_matrix_L.json exists; B660/S2 flagged the golden gap:
deck_swap_accessible = false). This cell re-runs the identical computation
on the identical basis and persists sigma_matrix_golden.json.

THE CONSTRUCTION (identical to B638 = identical to b637_threeform.double_Y):
  - D = the unbent weld double of the figure-eight 27-rep: the amalgam
    pi_1(D) on generators a,b (side 1: A27,B27) and c,d (side 2:
    U27 conj(.) U27^-1 letters), relators [REL(a,b), REL(c,d), aC,
    LONG(a,b)+LONG(c,d)].
  - The five classes rep_0..rep_4 = the first five vectors of
    nullspace(rows_all) independent mod coboundaries, in construction
    order (deterministic; exactly double_Y(None)'s reps).
  - J = Ad(U27) o conj (antilinear); (sigma* z)(x) = J(z(sigma x)) with
    sigma: a<->c, b<->d.
  - M[i][j] in K = Q(sqrt(-3)): sigma*(rep_i) = sum_j M[i][j] rep_j mod
    coboundaries (ROW convention; sigma* itself is ANTILINEAR: applying
    twice gives conj(M).M).

LAWS VERIFIED (banked B638/B649):
  L1 sigma*^2 = id mod coboundaries (cocycle level, all 5 classes);
  L2 conj(M).M = I = M.conj(M) exactly (the C.conj(C) = I analogue --
     the antilinear involution's matrix identity);
  L3 the persisted matrix == the B638 in-flight printout (transcribed).

INVARIANT CROSS-CHECK vs the B660/S4 evaluator (different presentation --
compare at the invariant level, NOT raw entries):
  golden pipeline (this run, b637 machinery): the B645 unit cross-ratio
    (Y[023]*Y[134])/(Y[034]*Y[123]) on the 024-silent unbent double = 1;
  S4 pipeline (sealed exact output s4_matrices.json): its Y-type tensor
    is W = antisym(T), T(u_i,u_j;w_k) = kappa_k*M_ij, computed here on
    ALL 10 triples exactly (the sealed record sampled only 4). The
    normalization-free lattice of W's support is computed exactly; the
    one fully basis-free invariant evaluable on BOTH sides -- the
    GL(5,C)-orbit genericity of the trivector (dual 2-form B with
    B^B != 0) -- is computed exactly on both tensors.

Exact arithmetic (Fraction pairs over Q(sqrt(-3))) in every decisive step.
New files only; nothing tracked is touched.
"""
import itertools as it
import json
import os
import re
import time
from fractions import Fraction as Fr

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "..", "B637_corrected_cell3")
S4JSON = os.path.join(HERE, "..", "..", "B660_structure_campaign",
                      "packet", "s4_massshape", "s4_matrices.json")


def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)


# ===========================================================================
log("STEP 0: exec b637_threeform.py (the exact 27 apparatus)...")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG, REL = mod["LONG"], mod["REL"]
side1, Side = mod["side1"], mod["Side"]
double_Y = mod["double_Y"]
apply_ = mod["apply"]
kconj, mconj, minv = mod["kconj"], mod["mconj"], mod["minv"]
meye, mmul = mod["meye"], mod["mmul"]
nullspace = mod["nullspace"]
ns = mod["ns"]
U27, U27i, u = mod["U27"], mod["U27i"], mod["u"]
Solver = ns["Solver"]
log("apparatus loaded")

gates = {}

# ===========================================================================
log("STEP 1: the five H^1(D;27) classes + the full Y table "
    "(double_Y(None) -- the unbent weld double, B637's construction)...")
Yn, reps, sides_of, side2 = double_Y(None, verbose=False)
log(f"  classes: {len(reps)} (expect 5); Y components: {len(Yn)} (expect 10)")
gates["five_classes"] = (len(reps) == 5)
assert gates["five_classes"]

# ===========================================================================
log("STEP 2: G1 gates (B638's involution checks, re-run)...")
uc = [[kconj(x) for x in row] for row in u]
prod = [[sum((u[i][t] * uc[t][j] for t in range(2)), K0) for j in range(2)]
        for i in range(2)]
gates["u_conj_u_plus1"] = all(
    (prod[i][j] - (K1 if i == j else K0)).is_zero()
    for i in range(2) for j in range(2))
log(f"  u*conj(u) = +1 (SL2 level): {gates['u_conj_u_plus1']}")


def Jop(v):
    return apply_(U27, [kconj(x) for x in v])


def sigma_star(z):
    za, zb, zc, zd = z[0:27], z[27:54], z[54:81], z[81:108]
    return (list(Jop(zc)) + list(Jop(zd)) + list(Jop(za)) + list(Jop(zb)))


# cocycle test rows (exactly B638's rebuild = double_Y's relator system)
lets4 = {'a': mod["A27"], 'b': mod["B27"], 'A': mod["A27i"],
         'B': mod["B27i"], 'c': side2.lets['a'], 'd': side2.lets['b'],
         'C': side2.lets['A'], 'D': side2.lets['B']}
prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
            "aC", LONG + LONG.translate(str.maketrans("abAB", "cdCD"))]
rows_all = []
for w in relators:
    L = {g: [[K0] * 27 for _ in range(27)] for g in "abcd"}
    Pi = meye(27)
    for ch in w:
        g = prim[ch]
        if ch.islower():
            term = Pi
            sgn = 1
        else:
            term = mmul(Pi, lets4[ch])
            sgn = -1
        if sgn < 0:
            term = ns["mscale"](K(-1), term)
        L[g] = ns["madd"](L[g], term)
        Pi = mmul(Pi, lets4[ch])
    for i in range(27):
        rows_all.append([L[g][i][j] for g in "abcd" for j in range(27)])


def is_cocycle(z):
    for row in rows_all:
        s = sum((row[t] * z[t] for t in range(108) if not z[t].is_zero()), K0)
        if not s.is_zero():
            return False
    return True


gates["sigma_star_cocycles"] = all(is_cocycle(sigma_star(r)) for r in reps)
log(f"  sigma*(rep_i) cocycles, 5/5: {gates['sigma_star_cocycles']}")
assert gates["sigma_star_cocycles"]

# coboundaries
cob = []
for j in range(27):
    v = [K1 if t == j else K0 for t in range(27)]
    entry = []
    for g in "abcd":
        gv = apply_(lets4[g], v)
        entry.extend([gv[i] - v[i] for i in range(27)])
    cob.append(entry)


def in_span(vecs, wv):
    try:
        Solver([x[:] for x in vecs]).coords(list(wv))
        return True
    except ValueError:
        return False


icob = []
for c in cob:
    if not icob or not in_span(icob, c):
        icob.append(c)
log(f"  independent coboundary basis: rank {len(icob)} (expect 26)")

gates["sigma_sq_id_cocycle_level"] = all(
    in_span(icob, [a - b for a, b in zip(sigma_star(sigma_star(r)), r)])
    for r in reps)
log(f"  L1: sigma*^2 = id mod coboundaries, 5/5: "
    f"{gates['sigma_sq_id_cocycle_level']}")
assert gates["sigma_sq_id_cocycle_level"]

# ===========================================================================
log("STEP 3: the sigma*-matrix M (exact, row convention "
    "sigma*(rep_i) = sum_j M[i][j] rep_j mod B^1)...")
basis = [r[:] for r in icob] + [list(r) for r in reps]
S = Solver(basis)
M = []
for r in reps:
    co = S.coords(list(sigma_star(r)))
    M.append(co[len(icob):])
for i, row in enumerate(M):
    log("  sigma*[%d] = " % i + " ".join(
        ("0" if x.is_zero() else str(x)) for x in row))

# L3: match against the B638 in-flight printout (transcribed verbatim
# from frontier/B638_swap_decomposition/b638_output.txt lines 15-19)
E = [
    [K(Fr(1, 2), Fr(1, 2)), K0, K0, K0, K0],
    [K(0, Fr(1, 24)), K(Fr(1, 2), Fr(-1, 2)), K0, K0, K0],
    [K(1256617152000, 1267793856000), K(268240896000, 0),
     K(Fr(-1, 2), Fr(-1, 2)), K0, K0],
    [K(Fr(-46189483200, 13), 465696000), K(11176704000, -11176704000),
     K0, K(Fr(-1, 2), Fr(1, 2)), K0],
    [K(1068480, -514080), K(-6652800, -6652800), K0, K0, K1],
]
gates["matches_b638_inflight"] = all(
    (M[i][j] - E[i][j]).is_zero() for i in range(5) for j in range(5))
log(f"  L3: M == the B638 in-flight printout (all 25 entries): "
    f"{gates['matches_b638_inflight']}")

# diagonal = the Eisenstein-unit spectrum (zeta6, conj zeta6, -zeta6,
# -conj zeta6, 1) -- banked B638 G2
Z6 = K(Fr(1, 2), Fr(1, 2))
spec = [Z6, kconj(Z6), K0 - Z6, K0 - kconj(Z6), K1]
gates["eisenstein_diagonal"] = all(
    (M[i][i] - spec[i]).is_zero() for i in range(5))
log(f"  diagonal = (z6, z6bar, -z6, -z6bar, 1): "
    f"{gates['eisenstein_diagonal']}")
gates["lower_triangular"] = all(
    M[i][j].is_zero() for i in range(5) for j in range(i + 1, 5))
log(f"  lower-triangular in the banked basis: {gates['lower_triangular']}")

# ===========================================================================
log("STEP 4: L2 -- the matrix-level real-structure identity "
    "(antilinear involution => conj(M).M = I = M.conj(M))...")


def kmatmul5(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(5)), K0)
             for j in range(5)] for i in range(5)]


Mc = [[kconj(x) for x in row] for row in M]
P1 = kmatmul5(Mc, M)
P2 = kmatmul5(M, Mc)
I5 = [[K1 if i == j else K0 for j in range(5)] for i in range(5)]
gates["conjM_M_eq_I"] = all((P1[i][j] - I5[i][j]).is_zero()
                            for i in range(5) for j in range(5))
gates["M_conjM_eq_I"] = all((P2[i][j] - I5[i][j]).is_zero()
                            for i in range(5) for j in range(5))
log(f"  conj(M).M = I exactly: {gates['conjM_M_eq_I']}")
log(f"  M.conj(M) = I exactly: {gates['M_conjM_eq_I']}")
assert gates["conjM_M_eq_I"] and gates["M_conjM_eq_I"]

# ===========================================================================
log("STEP 5: persist sigma_matrix_golden.json...")
out = {
    "artifact": "sigma_matrix_golden",
    "repairs": "L103 (B660/S2 deck_swap_accessible=false; B638 G2 computed "
               "in-flight, never persisted)",
    "object": "the golden (figure-eight) unbent weld double D: amalgam on "
              "a,b (side 1) and c,d (side 2 = U27 conj(.) U27^-1 letters), "
              "relators [REL(a,b), REL(c,d), aC, LONG(a,b)+LONG(c,d)]",
    "basis": "the five H^1(D;27) classes rep_0..rep_4 of "
             "b637_threeform.double_Y(None): the first five vectors of "
             "nullspace(rows_all) independent mod coboundaries, in "
             "construction order (deterministic; the SAME basis every "
             "banked Y[ijk] table uses)",
    "operator": "sigma* induced by the deck swap sigma: a<->c, b<->d with "
                "J = Ad(U27) o conj on coefficients; ANTILINEAR",
    "convention": "row i = coefficients of sigma*(rep_i): sigma*(rep_i) = "
                  "sum_j M[i][j] rep_j mod coboundaries; antilinearity => "
                  "sigma*^2 corresponds to conj(M).M",
    "field": "K = Q(sqrt(-3)); entry [a, b] means a + b*sqrt(-3), "
             "a,b rational strings",
    "matrix": [[[str(M[i][j].a), str(M[i][j].b)] for j in range(5)]
               for i in range(5)],
    "matrix_readable": [["0" if M[i][j].is_zero() else str(M[i][j])
                         for j in range(5)] for i in range(5)],
    "diagonal_spectrum": "(zeta6, conj zeta6, -zeta6, -conj zeta6, 1) -- "
                         "the Eisenstein-unit spectrum (B638 G2)",
    "laws_verified": {
        "sigma_sq_id_mod_coboundaries_5of5": True,
        "conjM_M_eq_I_exact": True,
        "M_conjM_eq_I_exact": True,
        "matches_b638_inflight_printout": gates["matches_b638_inflight"],
    },
    "provenance": "recomputed by frontier/B662_successor_campaign/cellC/"
                  "l103_repair.py from the B637 apparatus; format model: "
                  "frontier/B649_silver_holonomy/sigma_matrix_L.json",
}
JPATH = os.path.join(HERE, "sigma_matrix_golden.json")
with open(JPATH, "w") as f:
    json.dump(out, f, indent=1)
log(f"  saved {JPATH}")

# ===========================================================================
log("STEP 6: the golden-side invariant -- the B645 unit cross-ratio on "
    "the freshly recomputed Y table...")
Y023, Y134 = Yn[(0, 2, 3)], Yn[(1, 3, 4)]
Y034, Y123 = Yn[(0, 3, 4)], Yn[(1, 2, 3)]
Y024 = Yn[(0, 2, 4)]
gates["silent_024"] = Y024.is_zero()
log(f"  Y[024] = 0 (the 024-silent condition): {gates['silent_024']}")
for k_, v_ in sorted(Yn.items()):
    log(f"    Y[{k_}] = {'0' if v_.is_zero() else str(v_)}")
cross = (Y023 * Y134) * (Y034 * Y123).inv()
gates["unit_cross_ratio"] = (cross - K1).is_zero()
log(f"  (Y[023]*Y[134])/(Y[034]*Y[123]) = "
    f"{'1' if gates['unit_cross_ratio'] else str(cross)}  "
    f"[GATE: = 1 exactly]: {gates['unit_cross_ratio']}")
R24 = K(12, 12)  # 24*zeta6
gates["core_ratio_24z6"] = (Y023 - R24 * Y123).is_zero()
gates["spectator_ratio_24z6"] = (Y034 - R24 * Y134).is_zero()
log(f"  Y[023] = 24z6*Y[123]: {gates['core_ratio_24z6']};  "
    f"Y[034] = 24z6*Y[134]: {gates['spectator_ratio_24z6']}")

# ===========================================================================
log("STEP 7: the S4-side cross-check (B660/S4 sealed exact output; "
    "different presentation -- invariant level only)...")
log(f"  source: {os.path.normpath(S4JSON)}")
s4 = json.load(open(S4JSON))
S4M = [[K(Fr(s4["M_5x5"][i][j][0]), Fr(s4["M_5x5"][i][j][1]))
        for j in range(5)] for i in range(5)]


def parse_fmt(s):
    if s == "0":
        return K0
    m = re.match(r"^\((-?\d+(?:/\d+)?)([+-]\d+(?:/\d+)?)\*sqrt\(-3\)\)$", s)
    if m:
        return K(Fr(m.group(1)), Fr(m.group(2)))
    return K(Fr(s))


kap = [parse_fmt(x) for x in s4["kappas"]]
log(f"  kappas = {[str(x) for x in kap]};  M support (nonzero ij, i<j): "
    + str([(i, j) for i in range(5) for j in range(i + 1, 5)
           if not S4M[i][j].is_zero()]))

# (a) the S4 Y-type tensor: W = antisym(T), T(u_i,u_j;w_k) = kappa_k*M_ij;
# computed on ALL 10 triples (the sealed record sampled only 4, all of
# which happen to be zero -- W is NOT identically zero)
def antisym3(i, j, k):
    s = K0
    for p, sgn in [((i, j, k), 1), ((j, k, i), 1), ((k, i, j), 1),
                   ((j, i, k), -1), ((i, k, j), -1), ((k, j, i), -1)]:
        val = kap[p[2]] * S4M[p[0]][p[1]]
        s = s + (val if sgn > 0 else K0 - val)
    return s * K(Fr(1, 6))


W = {t: antisym3(*t) for t in it.combinations(range(5), 3)}
Wsup = [t for t, v in W.items() if not v.is_zero()]
for t in sorted(W):
    log(f"    W[{t}] = {'0' if W[t].is_zero() else str(W[t])}")
gates["s4_samples_reproduced"] = all(
    W[t].is_zero() for t in [(2, 3, 4), (0, 1, 2), (1, 2, 3), (0, 2, 4)])
log(f"  the 4 S4-sampled triples are 0 (sealed record reproduced): "
    f"{gates['s4_samples_reproduced']}")
gates["s4_W_support"] = (Wsup == [(0, 3, 4), (1, 2, 4), (1, 3, 4)])
log(f"  full W support = {Wsup} (all triples containing class 4 with "
    f"nonzero M-pair; kappa = e_4 kills every 4-free triple): "
    f"{gates['s4_W_support']}")

# (b) the normalization-free lattice of W's support: exponents n_s with
# sum_(s ni i) n_s = 0 for every mode i (kappa cancels identically in
# any balanced product; B645's construction)
inc = [[Fr(1) if m_ in t else Fr(0) for t in Wsup] for m_ in range(5)]
rows = [r[:] for r in inc]
rank, rr = 0, 0
for c in range(len(Wsup)):
    piv = next((r for r in range(rr, len(rows)) if rows[r][c] != 0), None)
    if piv is None:
        continue
    rows[rr], rows[piv] = rows[piv], rows[rr]
    pv = rows[rr][c]
    rows[rr] = [x / pv for x in rows[rr]]
    for r2 in range(len(rows)):
        if r2 != rr and rows[r2][c] != 0:
            f2 = rows[r2][c]
            rows[r2] = [x - f2 * y for x, y in zip(rows[r2], rows[rr])]
    rr += 1
    rank += 1
gates["s4_lattice_trivial"] = (rank == len(Wsup))
log(f"  W-support incidence rank = {rank} of {len(Wsup)} support triples "
    f"=> normalization-free lattice on the S4 side is "
    f"{'TRIVIAL' if gates['s4_lattice_trivial'] else 'NONTRIVIAL'}: the "
    "unit cross-ratio (a 4-slot balanced product) is NOT evaluable in "
    "the S4 presentation -- no normalization-free product exists there")

# (c) the ONE invariant evaluable on BOTH sides with no class
# identification: GL(5,C)-orbit genericity of the trivector (trivectors
# on 5-space classify by the rank of the dual 2-form B, B^{lm} =
# eps^{lmijk} Y_ijk; generic <=> B wedge B != 0)
def eps_perm(p):
    p = list(p)
    s = 1
    for a in range(len(p)):
        for b in range(a + 1, len(p)):
            if p[a] > p[b]:
                s = -s
    return s


def dual_wedge_nonzero(T3):
    B = {}
    for (i, j, k), v in T3.items():
        if v.is_zero():
            continue
        lm = tuple(sorted(set(range(5)) - {i, j, k}))
        e = eps_perm(lm + (i, j, k))
        val = v if e > 0 else K0 - v
        B[lm] = B.get(lm, K0) + val
    tot = {}
    prs = sorted(B)
    for p1 in prs:
        for p2 in prs:
            if set(p1) & set(p2):
                continue
            four = tuple(sorted(p1 + p2))
            e = eps_perm(p1 + p2)
            v = B[p1] * B[p2]
            tot[four] = tot.get(four, K0) + (v if e > 0 else K0 - v)
    return any(not v.is_zero() for v in tot.values())


gates["golden_generic_rank4"] = dual_wedge_nonzero(Yn)
gates["s4_generic_rank4"] = dual_wedge_nonzero(W)
log(f"  golden Y generic (dual B^B != 0): {gates['golden_generic_rank4']}"
    f"  [B660/S2 banked orbit type, recomputed here]")
log(f"  S4 W generic (dual B^B != 0): {gates['s4_generic_rank4']}")
log(f"  => the basis-free invariant AGREES across the presentations: "
    f"{gates['golden_generic_rank4'] == gates['s4_generic_rank4']}")

# (d) verdict of the invariant-level comparison
log("  CROSS-CHECK VERDICT: (i) golden side -- the unique normalization-"
    "free invariant, the B645 unit cross-ratio, = 1 exactly (STEP 6, "
    "recomputed live); (ii) S4 side -- W's support is 3 triples with "
    "trivial normalization-free lattice (rank = support), so the cross-"
    "ratio is NOT evaluable there: no invariant collision is possible "
    "at the product level (no banked class identification exists to "
    "sharpen it -- S4's own sealed NOTE); (iii) the fully basis-free "
    "invariant that IS evaluable on both -- GL(5,C)-orbit genericity -- "
    "AGREES exactly (both trivectors generic, dual-2-form rank 4).")

# (e) raw-ratio OBSERVATION (flagged: NOT normalization-free, recorded
# as HINT only): the spectator-pair ratio in the S4 presentation
r_obs = W[(0, 3, 4)] * W[(1, 3, 4)].inv()
hint_24z6 = (r_obs - R24).is_zero()
r_obs2 = W[(0, 3, 4)] * W[(1, 2, 4)].inv()
log(f"  HINT (raw-ratio, NOT the sealed check): S4 W[034]/W[134] = "
    f"{str(r_obs)} == 24*zeta6: {hint_24z6} -- the SAME 24*zeta6, in the "
    "SAME slot labels, as the banked golden spectator identity "
    "Y[034] = 24*zeta6*Y[134] (B645); W[034]/W[124] = "
    f"{str(r_obs2)} (= -zeta6). Ratios of this shape rescale under "
    "per-class normalization (c0/c1 resp. c0*c3/(c1*c2)), so this is "
    "recorded for the hint ledger, unjudged.")

# ===========================================================================
decisive = ["five_classes", "u_conj_u_plus1", "sigma_star_cocycles",
            "sigma_sq_id_cocycle_level", "conjM_M_eq_I", "M_conjM_eq_I",
            "matches_b638_inflight", "silent_024", "unit_cross_ratio",
            "s4_samples_reproduced", "s4_W_support", "s4_lattice_trivial",
            "golden_generic_rank4", "s4_generic_rank4"]
ok = all(gates[g] for g in decisive)
log("")
for g in decisive:
    log(f"  GATE {g}: {'PASS' if gates[g] else 'FAIL'}")
log(f"ALL DECISIVE GATES: {'PASS' if ok else 'FAIL'}")
log("OUTCOME: " + ("GAP REPAIRED (matrix persisted + laws verified + the "
                   "invariant cross-checked at the invariant level)"
                   if ok else "OBSTRUCTION -- see failed gates above"))
log("DONE.")
