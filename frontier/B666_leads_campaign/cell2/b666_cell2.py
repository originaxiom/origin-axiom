"""B666 CELL 2 -- L106: the cup-class VALUES on the generation triple.

Prereg: frontier/B666_leads_campaign/CAMPAIGN_PREREGISTRATION.md, CELL 2
clause (sealed). Outcomes: a distinguishing structure (first past four
walls) / degenerate again (the fifth wall; the values bank regardless).

TASK (exact over K = Q(sqrt-3) throughout; zero floats):
 (1) the EXACT values (coordinates in the 5-dim H^2(D;27bar)) of all
     nonzero cup classes [u_i cup u_j];
 (2) their sigma*-behavior: the induced antilinear action sigma2 on
     H^2(D;27bar) + the cup-level swap law mirroring Y o sigma* = conj(Y),
     down to the scalar action s0 on H^2(D;C) and the MV0 swap scalar;
 (3) THE DISCRIMINATING QUESTION: natural 3x3 objects on the solo triple
     {2,3,4} from the cup values --
       (a) the H^2-functional slice family lam(C)|solo (all 5 coordinate
           slices + the v0-contraction MV0): forced ANTISYMMETRIC by the
           class-level graded commutativity, so spectrum {0,+mu,-mu};
       (b) the dual-class/PD slices through the banked alternating Y
           (the P-matrix): scalar or antisymmetric, forced by alternation;
       (c) the NATURAL OPERATOR O = thetabar o theta on H^1(D;27), where
           theta = cross(., v0) (the cubic contracted with the invariant
           vector: 27 -> 27bar) and thetabar = crossbar(., v0bar) (the
           DUAL cubic contracted with the dual invariant: 27bar -> 27).
           O is Gamma-equivariant and canonical up to ONE overall scalar
           (the four 1-dim choices C, CBAR, v0, v0bar), so its eigenvalue
           RATIOS and degeneracy pattern are basis-free.  Three distinct
           eigenvalues on the generation quotient?
 (4) field of definition of the values (subfield-theorem expectation
     k(Gamma) = Q(sqrt-3)); eigenvalue fields via the exact
     square-in-K test.

METHOD: exec the banked cellH machinery (massey_first.py) VERBATIM --
inheriting its decisive basis control G0, all coefficient-system gates,
the cup table, MV0, PL/PR -- then:
  * H^2(D;27bar) coordinates: the left-null functionals of the 27bar Fox
    matrix give exact coordinates on coker(Fox); the banked injectivity
    H^2(pi;M) -> H^2(presentation complex) makes them faithful on
    classes.  h^2(D;27bar) = 5 by Poincare duality on the closed
    oriented aspherical double (chi = 0, h^0 = 1, h^1 = 5, h^3 = dim
    coinvariants = h^0(27) = 1  =>  h^2 = 5).  A rank-5 cup span then
    gives a cup BASIS of H^2.
  * the banked-Y consistency: Y_alt[i,j,k] must factor through the cup
    coordinates as sum_m C_ij[m] P[m][k] (the PD pairing matrix P read
    off the banked unbent table); rank/kernels of P.
  * the dual cubic CBAR on 27bar: rebuilt from first principles by the
    b637 derivation-equation route with the dual generators -X^T;
    equivariance gated on all 8 letters.
  * sigma2 on H^2: (sigma2 c)(w1,w2) = J2(c(sigma w1, sigma w2)) with
    J2 the unique antilinear map satisfying cross(Jx, Jy) = J2 cross(x,y)
    (probed exactly; J = Ad(U27) o conj is the banked H^1 convention).
  * the swap law: [sigma* u_i cup sigma* u_j] = sum_kl M_ik M_jl [c_kl]
    (M = sigma_matrix_golden.json, re-derived here and gated against the
    persisted artifact), checked exactly in coker coordinates.

New files only, all under cell2/.  No model names.  No SM numbers.
"""
import json
import math
import os
import re
import time
from fractions import Fraction as Fr

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/dri/origin-axiom"
CELLH = os.path.join(REPO, "frontier", "B662_successor_campaign", "cellH")
CELLC = os.path.join(REPO, "frontier", "B662_successor_campaign", "cellC")
B637D = os.path.join(REPO, "frontier", "B637_corrected_cell3")
MF = os.path.join(CELLH, "massey_first.py")
SIGJSON = os.path.join(CELLC, "sigma_matrix_golden.json")

# ===========================================================================
log("STEP 0: exec the banked cellH machinery (massey_first.py VERBATIM; "
    "runs its full gated pipeline incl. G0 basis control)...")
M1 = {"__name__": "cellH_machinery", "__file__": MF}
exec(compile(open(MF).read(), "massey_first.py", "exec"), M1)
log("cellH machinery loaded (all its gates PASSED -- assertions live)")

K, K0, K1 = M1["K"], M1["K0"], M1["K1"]
freduce, inv = M1["freduce"], M1["inv"]
apply_ = M1["apply_"]
nullspace, rref = M1["nullspace"], M1["rref"]
meye, mmul = M1["meye"], M1["mmul"]
Solver = M1["Solver"]
transpose = M1["transpose"]
LET, DACT = M1["LET"], M1["DACT"]
mat, dmat = M1["mat"], M1["dmat"]
cross, dot, rvec = M1["cross"], M1["dot"], M1["rvec"]
v0, v0bar = M1["v0"], M1["v0bar"]
E_bar, E_triv, phi = M1["E_bar"], M1["E_triv"], M1["phi"]
CUP, ECUP, zero_class = M1["CUP"], M1["ECUP"], M1["zero_class"]
MV0, PL, PR = M1["MV0"], M1["PL"], M1["PR"]
UREP, UEV = M1["UREP"], M1["UEV"]
reps, reps_bar = M1["reps"], M1["reps_bar"]
cob, cob_bar = M1["cob"], M1["cob_bar"]
TRIPLE_WORDS = M1["TRIPLE_WORDS"]
FOXCOLS = M1["cols"]          # the 108 columns of the 27bar Fox matrix
MOD = M1["mod"]               # the b637 namespace
kconj = MOD["kconj"]
U27, U27i = MOD["U27"], MOD["U27i"]
CFULL = MOD["CFULL"]
SUPIDX = MOD["SUPIDX"]
E6_e, E6_f = list(MOD["ns"]["E6_e"]), list(MOD["ns"]["E6_f"])
SOLO = (2, 3, 4)


def kstr(x):
    return "0" if x.is_zero() else str(x)


def vzero(v):
    return all(x.is_zero() for x in v)


def kcvec(v):
    return [kconj(x) for x in v]


def proportional(u_, w_):
    """exact projective equality of two vectors (nonzero assumed)."""
    for t in range(len(u_)):
        if not u_[t].is_zero():
            if w_[t].is_zero():
                return False
            lam = w_[t] * u_[t].inv()
            return all((w_[s] - lam * u_[s]).is_zero()
                       for s in range(len(u_)))
    return vzero(w_)


def kmatmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(m)), K0)
             for j in range(p)] for i in range(n)]


# ===========================================================================
log("STEP 1: banked-value gates (fresh run vs the sealed cellH record)...")
BANKED_PATTERN = [[True, True, False, False, False],
                  [True, True, False, False, False],
                  [False, False, True, False, False],
                  [False, False, False, True, False],
                  [False, False, False, False, True]]
g_pat = all(zero_class[(i, j)] == BANKED_PATTERN[i][j]
            for i in range(5) for j in range(5))
log(f"  cup zero/nonzero table == banked cellH STEP 6 table: {g_pat}")
assert g_pat

BANKED_MV0 = [
    [K0, K0, K0, K(0, 2), K0],
    [K0, K0, K(0, 2), K(Fr(1, 8), Fr(1, 24)), K0],
    [K0, K(0, -2), K0, K(2524411008000, 2502057600000),
     K(51891840, 25280640)],
    [K(0, -2), K(Fr(-1, 8), Fr(-1, 24)),
     K(-2524411008000, -2502057600000), K0, K(2595600, -539280)],
    [K0, K0, K(-51891840, -25280640), K(-2595600, 539280), K0]]
g_mv0 = all((MV0[i][j] - BANKED_MV0[i][j]).is_zero()
            for i in range(5) for j in range(5))
log(f"  MV0 == banked cellH STEP 6 matrix (all 25 entries): {g_mv0}")
assert g_mv0

# ===========================================================================
log("STEP 2: H^2(D;27bar) coordinates -- the left-null functionals of "
    "the 27bar Fox matrix (coker coordinates)...")
QN = nullspace(FOXCOLS)       # y with y . (Fox column) = 0 for all columns
log(f"  coker(Fox) dimension = {len(QN)}  (= 108 - rank(PHIBAR); "
    f"rank = {108 - len(QN)})")


def qcoords(E):
    out = []
    for y in QN:
        s = K0
        for i in range(108):
            yi = y[i]
            if yi.is_zero() or E[i].is_zero():
                continue
            s = s + yi * E[i]
        out.append(s)
    return out


Qq = {}
for i in range(5):
    for j in range(5):
        Qq[(i, j)] = qcoords(ECUP[(i, j)])
g_equiv = all(vzero(Qq[(i, j)]) == zero_class[(i, j)]
              for i in range(5) for j in range(5))
log(f"  q-test (coker coords = 0) == banked solver class test, 25/25: "
    f"{g_equiv}")
assert g_equiv

g_anti = all(vzero([Qq[(i, j)][t] + Qq[(j, i)][t] for t in range(len(QN))])
             for i in range(5) for j in range(5))
log(f"  class-level graded commutativity [u_i cup u_j] = -[u_j cup u_i] "
    f"(all 25 pairs): {g_anti}")

log("  Poincare-duality dimension count for the closed oriented "
    "aspherical double: h^0(27bar)=1, h^1(27bar)=5 (both computed in "
    "cellH), h^3(27bar) = dim coinvariants = h^0(27) = 1 (computed) "
    "=> chi = 0 forces h^2(D;27bar) = 5.")

# greedy cup basis of H^2 (canonical lex order over ordered pairs)
BP = []
bas_rows = []
for i in range(5):
    for j in range(5):
        if zero_class[(i, j)]:
            continue
        cand = Qq[(i, j)]
        try:
            if bas_rows:
                Solver([r[:] for r in bas_rows]).coords(cand[:])
                continue
        except ValueError:
            pass
        BP.append((i, j))
        bas_rows.append(cand)
log(f"  greedy cup span: rank {len(BP)}; basis pairs {BP}")
CUP_SPAN_5 = (len(BP) == 5)
log(f"  cup product H^1 x H^1 -> H^2(D;27bar) SURJECTIVE "
    f"(rank 5 = h^2): {CUP_SPAN_5}")
SolQ = Solver(bas_rows)

CVEC = {}
for i in range(5):
    for j in range(5):
        CVEC[(i, j)] = SolQ.coords(Qq[(i, j)])
log("  EXACT cup-class coordinates in the cup basis "
    f"b_m = [u_p cup u_q], (p,q) in {BP}:")
for i in range(5):
    for j in range(5):
        if not zero_class[(i, j)]:
            log(f"    [u_{i} cup u_{j}] = (" +
                ", ".join(kstr(x) for x in CVEC[(i, j)]) + ")")

# the exact relation lattice among the 9 upper-triangle nonzero classes
UPPER = [(i, j) for i in range(5) for j in range(i + 1, 5)
         if not zero_class[(i, j)]]
relrows = [[Qq[p][r] for p in UPPER] for r in range(len(QN))]
RELS = nullspace(relrows)
log(f"  relation lattice among the {len(UPPER)} upper classes {UPPER}: "
    f"dim {len(RELS)}")
for rv in RELS:
    terms = [f"({kstr(rv[t])})*[{UPPER[t]}]" for t in range(len(UPPER))
             if not rv[t].is_zero()]
    log("    0 = " + " + ".join(terms))

# the radical of the H^2-valued cup form on H^1(D;27)
rad_rows = []
for j in range(5):
    for m in range(len(BP)):
        rad_rows.append([CVEC[(i, j)][m] for i in range(5)])
RADFULL = nullspace(rad_rows)
log(f"  radical of the H^2-valued cup form on H^1 (x with [x cup u_j] = 0 "
    f"for all j): dim = {len(RADFULL)}")
for v in RADFULL:
    log("    radical: [" + ", ".join(kstr(x) for x in v) + "]")
# the cellH distinguished class (ker MV0 = right radical of PL, banked)
DIST = [K(7560, 10920), K(12640320, -8648640), K0, K0, K1]
if len(RADFULL) == 1:
    g_rad_dist = proportional(RADFULL[0], DIST)
    log(f"  radical == the cellH distinguished class (ker MV0 = rad PL): "
        f"{g_rad_dist}")

# ===========================================================================
log("STEP 2b: the banked-Y consistency -- the PD pairing matrix P...")
YTAB = {}
ypat = re.compile(r"Y\[\((\d), (\d), (\d)\)\] = (.*)$")
tokpat = re.compile(r"^\((-?[0-9/]+)(?:\+(-?[0-9/]+)r)?\)$")
for line in open(os.path.join(B637D, "unbent_table.txt")):
    mm = ypat.search(line.strip())
    if not mm:
        continue
    i, j, k = int(mm.group(1)), int(mm.group(2)), int(mm.group(3))
    val = mm.group(4).strip()
    if val == "0":
        YTAB[(i, j, k)] = K0
    else:
        tm = tokpat.match(val)
        assert tm, f"Y parse fail: {val!r}"
        YTAB[(i, j, k)] = K(Fr(tm.group(1)),
                            Fr(tm.group(2)) if tm.group(2) else Fr(0))
assert len(YTAB) == 10, f"Y table has {len(YTAB)} rows"
log(f"  banked unbent Y table parsed ({len(YTAB)} rows; basis identity "
    "certified by cellH G0, re-run live in STEP 0)")


def perm_sign(p):
    p = list(p)
    s = 1
    for a in range(len(p)):
        for b in range(a + 1, len(p)):
            if p[a] > p[b]:
                s = -s
    return s


def Yalt(i, j, k):
    if len({i, j, k}) < 3:
        return K0
    v = YTAB[tuple(sorted((i, j, k)))]
    return v if perm_sign((i, j, k)) > 0 else K0 - v


P = [[Yalt(bp[0], bp[1], k) for k in range(5)] for bp in BP]
log("  P[m][k] = Y_alt[p_m, q_m, k] (the pairing of basis class b_m "
    "with u_k through the banked alternating Y):")
for m in range(len(BP)):
    log("    [" + ", ".join(kstr(x) for x in P[m]) + "]")
g_ycons = all(
    (Yalt(i, j, k) - sum((CVEC[(i, j)][m] * P[m][k]
                          for m in range(len(BP))), K0)).is_zero()
    for i in range(5) for j in range(5) for k in range(5))
log(f"  DECISIVE CONSISTENCY: Y_alt[i,j,k] == sum_m C_ij[m] P[m][k] for "
    f"ALL 125 ordered triples: {g_ycons}")
PK_right = nullspace([[P[m][k] for k in range(5)]
                      for m in range(len(BP))])
PK_left = nullspace([[P[m][k] for m in range(len(BP))]
                     for k in range(5)])
PRANK = 5 - len(PK_right)
log(f"  rank(P) = {PRANK}; right kernel (H^1 classes invisible to Y) dim "
    f"= {len(PK_right)}; left kernel (H^2 directions invisible to Y) dim "
    f"= {len(PK_left)}")
for v in PK_right:
    log("    right ker (H^1): [" + ", ".join(kstr(x) for x in v) + "]")
    if len(PK_right) == 1:
        log(f"    right ker == the distinguished class: "
            f"{proportional(v, DIST)}")
for v in PK_left:
    log("    left ker (H^2, cup-basis coords): ["
        + ", ".join(kstr(x) for x in v) + "]")

# ===========================================================================
log("STEP 3: the dual cubic CBAR on 27bar (from first principles; "
    "derivation equations with the dual generators -X^T)...")
support = sorted(SUPIDX, key=lambda t: SUPIDX[t])
eqs = {}
for gi, X in enumerate(E6_e + E6_f):
    # dual generator Xd[s][t] = -X[t][s]
    xrow = {}
    for s in range(27):
        ent = []
        for t in range(27):
            if not X[t][s].is_zero():
                ent.append((t, K0 - X[t][s]))
        if ent:
            xrow[s] = ent
    for (a, b, c) in support:
        k = SUPIDX[(a, b, c)]
        for (u, v, w) in ((a, b, c), (b, a, c), (c, a, b)):
            for (t, val) in xrow.get(u, ()):
                key = (gi,) + tuple(sorted((t, v, w)))
                row = eqs.setdefault(key, {})
                row[k] = row.get(k, K0) + val
rows_d = [[row.get(k, K0) for k in range(len(support))]
          for row in eqs.values()]
solD = nullspace(rows_d)
log(f"  dual-invariant cubic solutions: {len(solD)} (expect 1)")
assert len(solD) == 1
CBAR = {}
for (p, q, r_), k in SUPIDX.items():
    if not solD[0][k].is_zero():
        for perm in {(p, q, r_), (p, r_, q), (q, p, r_), (q, r_, p),
                     (r_, p, q), (r_, q, p)}:
            CBAR[perm] = solD[0][k]
log(f"  CBAR: {len(CBAR)} ordered entries; all rational: "
    f"{all(cv.b == 0 for cv in CBAR.values())}")
CBR = [[] for _ in range(27)]
for (p, q, r_), cval in CBAR.items():
    CBR[r_].append((p, q, cval))


def crossbar(x, y):
    out = []
    for r_ in range(27):
        s = K0
        for (p, q, cv) in CBR[r_]:
            xp = x[p]
            if xp.is_zero():
                continue
            yq = y[q]
            if yq.is_zero():
                continue
            s = s + cv * xp * yq
        out.append(s)
    return out


# gate: group-level equivariance crossbar(rhobar x, rhobar y) = rho crossbar
for ch in "abcdABCD":
    for sd in (13, 31):
        x, y = rvec(sd), rvec(sd + 100)
        lhs = crossbar(apply_(DACT[ch], x), apply_(DACT[ch], y))
        rhs = apply_(LET[ch], crossbar(x, y))
        assert all((lhs[t] - rhs[t]).is_zero() for t in range(27)), \
            f"crossbar equivariance FAILS at letter {ch}"
log("  crossbar equivariance PASS (8 letters x 2 seeds)")

# the two invariant-line cubic constants
t1 = cross(v0, v0)            # in (27bar)^Gamma = K.v0bar
t2 = crossbar(v0bar, v0bar)   # in (27)^Gamma  = K.v0
i1 = next(t for t in range(27) if not v0bar[t].is_zero())
muN = t1[i1] * v0bar[i1].inv()
assert all((t1[t] - muN * v0bar[t]).is_zero() for t in range(27))
i2 = next(t for t in range(27) if not v0[t].is_zero())
lamN = t2[i2] * v0[i2].inv()
assert all((t2[t] - lamN * v0[t]).is_zero() for t in range(27))
log(f"  cross(v0,v0) = muN * v0bar with muN = {kstr(muN)}")
log(f"  crossbar(v0bar,v0bar) = lamN * v0 with lamN = {kstr(lamN)}")
log(f"  dot(v0bar, v0) = {kstr(dot(v0bar, v0))}   (the invariant-line "
    "pairing; scale-dependent, recorded for completeness)")

# ===========================================================================
log("STEP 4: the natural operator O = thetabar o theta on H^1(D;27)...")


def theta(x):
    return cross(x, v0)


def thetabar(y):
    return crossbar(y, v0bar)


O27 = [[K0] * 27 for _ in range(27)]
for j in range(27):
    ej = [K1 if t == j else K0 for t in range(27)]
    col = thetabar(theta(ej))
    for i in range(27):
        O27[i][j] = col[i]
# gate: O27 commutes with all 8 letters (Gamma-equivariance)
for ch in "abcdABCD":
    P1 = mmul(O27, LET[ch])
    P2 = mmul(LET[ch], O27)
    assert all((P1[i][j] - P2[i][j]).is_zero()
               for i in range(27) for j in range(27)), \
        f"O27 does not commute with letter {ch}"
log("  O27 commutes with all 8 letters (equivariance) PASS")
Ov0 = apply_(O27, v0)
assert all((Ov0[t] - (muN * lamN) * v0[t]).is_zero() for t in range(27))
log(f"  O27 v0 = (muN*lamN) v0 = ({kstr(muN * lamN)}) v0  "
    "(consistency PASS)")

SolH = Solver([r[:] for r in cob] + [list(r) for r in reps])
SolB = Solver([r[:] for r in cob_bar] + [list(r) for r in reps_bar])

# OH: the induced 5x5 matrix on H^1(D;27) (row convention:
# O[u_i] = sum_j OH[i][j] u_j mod coboundaries)
OH = []
for i in range(5):
    flatv = []
    for gi in range(4):
        blk = reps[i][gi * 27:(gi + 1) * 27]
        flatv.extend(apply_(O27, blk))
    OH.append(SolH.coords(flatv)[27:])
log("  OH (the natural operator on H^1, banked basis, row convention):")
for i in range(5):
    log("    [" + ", ".join(kstr(x) for x in OH[i]) + "]")

# Theta: theta_* : H^1(27) -> H^1(27bar);  Psi: thetabar_* backwards
Theta = []
for i in range(5):
    flatv = []
    for gi in range(4):
        blk = reps[i][gi * 27:(gi + 1) * 27]
        flatv.extend(theta(blk))
    Theta.append(SolB.coords(flatv)[27:])
Psi = []
for t in range(5):
    flatv = []
    for gi in range(4):
        blk = reps_bar[t][gi * 27:(gi + 1) * 27]
        flatv.extend(thetabar(blk))
    Psi.append(SolH.coords(flatv)[27:])
log("  Theta (theta_* on H^1, rows = images in the zbar basis):")
for i in range(5):
    log("    [" + ", ".join(kstr(x) for x in Theta[i]) + "]")
log("  Psi (thetabar_* : H^1(27bar) -> H^1(27)):")
for t in range(5):
    log("    [" + ", ".join(kstr(x) for x in Psi[t]) + "]")

TP = kmatmul(Theta, Psi)
g_comp = all((TP[i][j] - OH[i][j]).is_zero()
             for i in range(5) for j in range(5))
log(f"  gate OH = Theta . Psi (composition through H^1(27bar)): {g_comp}")
assert g_comp
TPL = kmatmul(Theta, PL)
g_tpl = all((TPL[i][j] - MV0[i][j]).is_zero()
            for i in range(5) for j in range(5))
log(f"  gate Theta . PL = MV0 (the theta-pairing IS the v0-mediated "
    f"2-form): {g_tpl}")
assert g_tpl
kerT = nullspace([list(r) for r in Theta])
log(f"  rank(Theta) = {5 - len(kerT)}, "
    f"rank(Psi) = {5 - len(nullspace([list(r) for r in Psi]))}")
if len(kerT) == 1:
    log(f"  ker(Theta) == the distinguished class: "
        f"{proportional(kerT[0], DIST)}")

# block structure wrt the boundary-born subspace U_b = <u_0, u_1>
g_blk = all(OH[i][j].is_zero() for i in (0, 1) for j in (2, 3, 4))
log(f"  OH preserves the boundary-born subspace U_b = <u_0,u_1> "
    f"(rows 0,1 have no solo component): {g_blk}")

# ===========================================================================
log("STEP 5: sigma machinery -- the H^1 matrix M (gate vs the persisted "
    "artifact), J2, sigma2 on H^2, the swap law...")
SIG = str.maketrans("abABcdCD", "cdCDabAB")


def sigw(w):
    return w.translate(SIG)


def Jop(v):
    return apply_(U27, kcvec(v))


def sigma_star(z):
    za, zb, zc, zd = z[0:27], z[27:54], z[54:81], z[81:108]
    return (list(Jop(zc)) + list(Jop(zd)) + list(Jop(za)) + list(Jop(zb)))


Mrows = []
for r in reps:
    Mrows.append(SolH.coords(list(sigma_star(r)))[27:])
sj = json.load(open(SIGJSON))
MJ = [[K(Fr(sj["matrix"][i][j][0]), Fr(sj["matrix"][i][j][1]))
       for j in range(5)] for i in range(5)]
g_M = all((Mrows[i][j] - MJ[i][j]).is_zero()
          for i in range(5) for j in range(5))
log(f"  sigma* H^1 matrix M recomputed == sigma_matrix_golden.json "
    f"(all 25 entries): {g_M}")
assert g_M
M = Mrows

# J2: the unique antilinear map on 27bar with cross(Jx, Jy) = J2 cross(x,y)
U27iT = transpose(U27i)


def J2raw(y):
    return apply_(U27iT, kcvec(y))


nu = None
for sd in (3, 19, 57):
    x, y = rvec(sd), rvec(sd + 200)
    lhs = cross(Jop(x), Jop(y))
    rhs0 = J2raw(cross(x, y))
    i0 = next((t for t in range(27) if not rhs0[t].is_zero()), None)
    assert i0 is not None
    nu_c = lhs[i0] * rhs0[i0].inv()
    assert all((lhs[t] - nu_c * rhs0[t]).is_zero() for t in range(27)), \
        "cross(Jx,Jy) is NOT proportional to U27^-T conj cross(x,y)"
    if nu is None:
        nu = nu_c
    assert (nu - nu_c).is_zero(), "J2 scalar not constant across probes"
log(f"  J2 = nu * Ad(U27^-T) o conj with nu = {kstr(nu)}  "
    "(3 probe pairs, exact)")


def J2(y):
    return [nu * t for t in J2raw(y)]


# gate: J2 intertwines the deck swap on 27bar
for ch in "abcdABCD":
    yv = rvec(71)
    lhs = J2(apply_(DACT[sigw(ch)], yv))
    rhs = apply_(DACT[ch], J2(yv))
    assert all((lhs[t] - rhs[t]).is_zero() for t in range(27)), \
        f"J2 intertwining FAILS at {ch}"
log("  J2 rhobar(sigma g) = rhobar(g) J2 PASS (8 letters)")

# J fixes the invariant line: J(v0) = c0 v0 (needed for the MV0 scalar law)
jv0 = Jop(v0)
i3 = next(t for t in range(27) if not v0[t].is_zero())
c0 = jv0[i3] * v0[i3].inv()
assert all((jv0[t] - c0 * v0[t]).is_zero() for t in range(27))
g_c0unit = (c0 * kconj(c0) - K1).is_zero()
log(f"  J(v0) = c0 v0 with c0 = {kstr(c0)}; c0.conj(c0) = 1: {g_c0unit}")

# sigma2 pullbacks of all 25 cup cochains + the swap law in coker coords
def sigma_cup(i, j):
    c = CUP[(i, j)]

    def c2(s1, s2, c=c):
        return J2(c(sigw(s1), sigw(s2)))
    return c2


# cocycle spot-check for one sigma2-pullback
sc23 = sigma_cup(2, 3)
for (g, h, l) in TRIPLE_WORDS:
    t1_ = apply_(dmat(g), sc23(h, l))
    t2_ = sc23(freduce(g + h), l)
    t3_ = sc23(g, freduce(h + l))
    t4_ = sc23(g, h)
    assert all((t1_[t] - t2_[t] + t3_[t] - t4_[t]).is_zero()
               for t in range(27)), "sigma2 cup not a 2-cocycle?!"
log("  sigma2(u_2 cup u_3) 2-cocycle identity PASS (3 word triples)")

QS = {}
for i in range(5):
    for j in range(5):
        QS[(i, j)] = qcoords(E_bar(sigma_cup(i, j)))
law_ok = True
for i in range(5):
    for j in range(5):
        rhsv = [K0] * len(QN)
        for k in range(5):
            Mik = M[i][k]
            if Mik.is_zero():
                continue
            for l_ in range(5):
                f = Mik * M[j][l_]
                if f.is_zero():
                    continue
                qkl = Qq[(k, l_)]
                rhsv = [rhsv[t] + f * qkl[t] for t in range(len(QN))]
        if not vzero([QS[(i, j)][t] - rhsv[t] for t in range(len(QN))]):
            law_ok = False
            log(f"    swap-law MISMATCH at pair ({i},{j})")
log(f"  THE CUP-LEVEL SWAP LAW  [sigma2 c_ij] = sum_kl M_ik M_jl [c_kl] "
    f"(25/25 pairs, exact in coker coords): {law_ok}")

# S: the sigma2 matrix on H^2 in the cup basis (row convention:
# sigma2(b_m) = sum_n S[m][n] b_n; sigma2 ANTILINEAR)
S = [SolQ.coords(QS[bp]) for bp in BP]
log("  S (sigma2 on H^2(D;27bar), cup basis, row convention):")
for m in range(len(BP)):
    log("    [" + ", ".join(kstr(x) for x in S[m]) + "]")
Sc = [[kconj(x) for x in row] for row in S]
P1_ = kmatmul(Sc, S)
g_invol = all((P1_[i][j] - (K1 if i == j else K0)).is_zero()
              for i in range(5) for j in range(5))
log(f"  conj(S).S = I exactly (sigma2 is an antilinear involution on "
    f"H^2 -- the mirror of conj(M).M = I): {g_invol}")
# antilinearity consistency: sigma2[c_ij] = sum_m conj(CVEC_m) S[m][.]
g_alin = True
for i in range(5):
    for j in range(5):
        want = SolQ.coords(QS[(i, j)])
        got = [sum((kconj(CVEC[(i, j)][m]) * S[m][n] for m in range(5)),
                   K0) for n in range(5)]
        if not vzero([want[n] - got[n] for n in range(5)]):
            g_alin = False
log(f"  antilinear-expansion consistency on all 25 pairs: {g_alin}")

# the scalar s0 of tau -> conj o tau o sigma on H^2(D;C), and the MV0 law
s0 = None
for (i, j) in [(2, 3), (2, 4)]:
    c = CUP[(i, j)]

    def stau(s1, s2, c=c):
        return kconj(dot(c(sigw(s1), sigw(s2)), v0))

    val = phi(E_triv(stau))
    s0c = val * kconj(MV0[i][j]).inv()
    if s0 is None:
        s0 = s0c
    g_s0 = (s0 - s0c).is_zero()
log(f"  s0 (sigma* scalar on H^2(D;C), phi-normalized) = {kstr(s0)}; "
    f"well-defined across 2 independent samples: {g_s0}")
rho_pred = s0 * nu * c0.inv()
MMV0MT = kmatmul(kmatmul(M, MV0), transpose(M))
g_mv0law = all((MMV0MT[i][j] - rho_pred * kconj(MV0[i][j])).is_zero()
               for i in range(5) for j in range(5))
log(f"  MV0 SWAP LAW  M.MV0.M^T = rho * conj(MV0) with rho = s0*nu/c0 = "
    f"{kstr(rho_pred)}  (all 25 entries): {g_mv0law}")

# sigma-covariance of the natural operator
lhsM = kmatmul(M, OH)
rhsM = kmatmul([[kconj(x) for x in row] for row in OH], M)
g_cov = all((lhsM[i][j] - rhsM[i][j]).is_zero()
            for i in range(5) for j in range(5))
log(f"  sigma-covariance of the natural operator: M.OH = conj(OH).M "
    f"exactly: {g_cov}")

# ===========================================================================
log("STEP 6: THE DISCRIMINATING SLICES (exact eigen analysis)...")
import sympy as sp                                        # noqa: E402

r3 = sp.sqrt(3) * sp.I


def tosp(x):
    return sp.Rational(x.a) + sp.Rational(x.b) * r3


def eig_report(name, rowsK, invariant):
    A = sp.Matrix([[tosp(x) for x in row] for row in rowsK])
    lam = sp.symbols("lam")
    p = sp.expand(A.charpoly(lam).as_expr())
    fac = sp.factor(p, extension=r3)
    g = sp.gcd(sp.Poly(p, lam), sp.Poly(sp.diff(p, lam), lam))
    ndis = int(sp.degree(p, lam) - sp.degree(g.as_expr(), lam))
    log(f"  {name}:")
    log(f"    charpoly = {p}")
    log(f"    factored over K = Q(sqrt-3): {fac}")
    try:
        ev = A.eigenvals()
        log(f"    eigenvalues (value: multiplicity): "
            f"{ {sp.nsimplify(k_): v_ for k_, v_ in ev.items()} }")
    except Exception as e:                                # noqa: BLE001
        ev = {}
        log(f"    (eigenvalue radicals unavailable: {e})")
    log(f"    DISTINCT eigenvalue count = {ndis}"
        + ("  [conjugation-INVARIANT operator spectrum]" if invariant
           else "  [form/slice: basis-dependent congruence data]"))
    return ndis, ev, p


def qsqrt(fr):
    """exact rational square root or None."""
    if fr < 0:
        return None
    n, d = fr.numerator, fr.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    if rn * rn == n and rd * rd == d:
        return Fr(rn, rd)
    return None


def sqrt_in_K(delta):
    """an s in K with s^2 = delta, or None (exact)."""
    p_, b_ = Fr(delta.a), Fr(delta.b)
    if b_ == 0:
        r1 = qsqrt(p_)
        if r1 is not None:
            return K(r1, 0)
        r2 = qsqrt(p_ / Fr(-3))
        if r2 is not None:
            return K(0, r2)
        return None
    s_ = qsqrt(p_ * p_ + 3 * b_ * b_)
    if s_ is None:
        return None
    for cand in ((p_ + s_) / 2, (p_ - s_) / 2):
        x_ = qsqrt(cand)
        if x_ is not None and x_ != 0:
            return K(x_, b_ / (2 * x_))
    return None


# (A) THE natural operator on the generation quotient Q = H^1/U_b
if g_blk:
    OHQ = [[OH[i][j] for j in SOLO] for i in SOLO]
    ndA, evA, pA = eig_report(
        "OH on the generation quotient Q = H^1/<u_0,u_1> "
        "(3x3, NATURAL operator, eigenvalue ratios basis-free)",
        OHQ, True)
    if ndA == 3:
        try:
            Asp = sp.Matrix([[tosp(x) for x in row] for row in OHQ])
            for (val, mult, vecs) in Asp.eigenvects():
                log(f"    eigenline for {sp.nsimplify(val)}: "
                    f"{[sp.nsimplify(c) for c in vecs[0].T]}")
        except Exception as e:                            # noqa: BLE001
            log(f"    (eigenvectors unavailable: {e})")
else:
    ndA, evA = 0, {}
    log("  OH does NOT preserve U_b -- no natural quotient operator")
ndF, evF, pF = eig_report("OH on the full H^1 (5x5 natural operator)",
                          OH, True)

# (B) the functional-slice family lam(C)|solo -- ALL antisymmetric
log("  (B) the H^2-functional slice family lam(C)|solo, lam in (H^2)*:")
log("      class antisymmetry (STEP 2 gate) ==> EVERY functional slice "
    "is an antisymmetric 3x3 ==> spectrum {0, +mu(lam), -mu(lam)} for "
    "EVERY lam: the +-pair shape is FORCED across the whole 5-parameter "
    "family; no slice carries three independent values.")
slice_data = []
axes = []
for m in range(len(BP)):
    Tm = [[CVEC[(i, j)][m] for j in SOLO] for i in SOLO]
    if all(x.is_zero() for row in Tm for x in row):
        log(f"    slice T^{m+1} (coords along b_{m+1}): ZERO on solo")
        slice_data.append((f"T{m+1}", K0, K0, K0, K0, K0))
        continue
    assert all((Tm[i][j] + Tm[j][i]).is_zero()
               for i in range(3) for j in range(3))
    a_, b_, c_ = Tm[0][1], Tm[0][2], Tm[1][2]
    delta = K0 - (a_ * a_ + b_ * b_ + c_ * c_)
    axv = (c_, K0 - b_, a_)
    axes.append(axv)
    root = sqrt_in_K(delta)
    slice_data.append((f"T{m+1}", a_, b_, c_, delta, root))
    log(f"    slice T^{m+1}: entries (T_23,T_24,T_34) = ({kstr(a_)}, "
        f"{kstr(b_)}, {kstr(c_)})")
    log(f"      mu^2 = {kstr(delta)}; mu in "
        + (f"K (mu = {kstr(root)})" if root is not None
           else "the quadratic extension K(sqrt(mu^2)) -- NOT in K"))
    log(f"      axis (0-eigenvector) = ({kstr(axv[0])}, {kstr(axv[1])}, "
        f"{kstr(axv[2])})")
amv = (MV0[2][3], MV0[2][4], MV0[3][4])
delta_mv0 = K0 - (amv[0] * amv[0] + amv[1] * amv[1] + amv[2] * amv[2])
root_mv0 = sqrt_in_K(delta_mv0)
ax_mv0 = (amv[2], K0 - amv[1], amv[0])
log(f"    MV0-slice (v0-contraction): entries ({kstr(amv[0])}, "
    f"{kstr(amv[1])}, {kstr(amv[2])}); mu^2 = {kstr(delta_mv0)}; mu in "
    + (f"K (mu = {kstr(root_mv0)})" if root_mv0 is not None
       else "the quadratic extension K(sqrt(mu^2)) -- NOT in K"))
ndB, evB, pB = eig_report("MV0 solo block (3x3 antisymmetric form)",
                          [[MV0[i][j] for j in SOLO] for i in SOLO], False)
# axis geometry: common kernel across the slice family?
stack = []
for m in range(len(BP)):
    for i in range(3):
        stack.append([CVEC[(SOLO[i], j)][m] for j in SOLO])
common = nullspace(stack)
axrank = len(axes) - len(nullspace(
    [[axes[r][c2] for r in range(len(axes))] for c2 in range(3)])) \
    if axes else 0
log(f"    axis-matrix rank = {axrank} (of 3); common kernel of ALL "
    f"coordinate slices on solo: dim = {len(common)}"
    + ("" if common else "  (no distinguished generation direction)"))
for v in common:
    log(f"    COMMON AXIS: [{kstr(v[0])}, {kstr(v[1])}, {kstr(v[2])}]")

# closed-form wall for two-slice products: A.B has spectrum {0, -n.m, -n.m}
Amv0 = [[MV0[i][j] for j in SOLO] for i in SOLO]
m0 = next(m for m in range(len(BP))
          if not all(x.is_zero()
                     for x in (CVEC[(2, 3)][m], CVEC[(2, 4)][m],
                               CVEC[(3, 4)][m])))
Tm0 = [[CVEC[(i, j)][m0] for j in SOLO] for i in SOLO]
ABm = kmatmul(Amv0, Tm0)
nvec_ = ax_mv0
mvec_ = (Tm0[1][2], K0 - Tm0[0][2], Tm0[0][1])
nm = sum((nvec_[t] * mvec_[t] for t in range(3)), K0)
trAB = ABm[0][0] + ABm[1][1] + ABm[2][2]
detAB = (ABm[0][0] * (ABm[1][1] * ABm[2][2] - ABm[1][2] * ABm[2][1])
         - ABm[0][1] * (ABm[1][0] * ABm[2][2] - ABm[1][2] * ABm[2][0])
         + ABm[0][2] * (ABm[1][0] * ABm[2][1] - ABm[1][1] * ABm[2][0]))
g_prod = ((trAB + nm + nm).is_zero() and detAB.is_zero())
log(f"    two-slice products: MV0solo . T^{m0+1} has tr = -2(n.m) and "
    f"det = 0 (spectrum {{0, -n.m, -n.m}}, ALWAYS twofold degenerate): "
    f"{g_prod}")

# (C) the dual-class/PD slices through the banked Y
log("  (C) the dual-class (PD) slices from the banked alternating Y:")
cyc = {2: (3, 4), 3: (4, 2), 4: (2, 3)}
y234 = YTAB[(2, 3, 4)]
g_hodge = all(
    (Yalt(cyc[i2][0], cyc[i2][1], k2)
     - (y234 if i2 == k2 else K0)).is_zero()
    for i2 in SOLO for k2 in SOLO)
log(f"    Hodge slice G[i][k] = <w_i, u_k>_Y = Y[234].delta_ik (SCALAR "
    f"matrix, Y[234] = {kstr(y234)}): {g_hodge} -- ONE eigenvalue, "
    "threefold: maximal degeneracy, forced by the alternation of Y")
for spect in (0, 1):
    Gs = [[Yalt(i2, spect, k2) for k2 in SOLO] for i2 in SOLO]
    anti = all((Gs[i][j] + Gs[j][i]).is_zero()
               for i in range(3) for j in range(3))
    log(f"    spectator-{spect} slice Y_alt[i,{spect},k]: antisymmetric "
        f"{anti}; entries ({kstr(Gs[0][1])}, {kstr(Gs[0][2])}, "
        f"{kstr(Gs[1][2])}) -- the +-pair wall again")

# (D) the star classes w_i = [u_j cup u_k] (cyclic on the solo triple)
star_rows = []
log("  (D) the star classes w_i = [u_j cup u_k], (i,j,k) cyclic in "
    "(2,3,4):")
for i in SOLO:
    j, k = cyc[i]
    star_rows.append(CVEC[(j, k)])
    log(f"    w_{i} = [u_{j} cup u_{k}] = ("
        + ", ".join(kstr(x) for x in CVEC[(j, k)]) + ")"
        + f"   v0-contraction lambda(w_{i}) = {kstr(MV0[j][k])}")
star_rank = 3 - len(nullspace(
    [[star_rows[a][m] for a in range(3)] for m in range(5)]))
log(f"    rank of the 3 star classes in H^2 = {star_rank} "
    f"(3 = independent: one H^2 direction per generation)")
sv = [MV0[3][4], MV0[4][2], MV0[2][3]]
sv_dist = len({(x.a, x.b) for x in sv})
log(f"    the three v0-contracted star values: "
    f"({', '.join(kstr(x) for x in sv)}); distinct count = {sv_dist} "
    "[banked-basis values; they rescale as c_j c_k under per-class "
    "normalization u_i -> c_i u_i and mix under GL(solo) -- and the "
    "B645-style balanced-product lattice on supports {3,4},{4,2},{2,3} "
    "is TRIVIAL (incidence rank 3), so NO normalization-free product "
    "exists: values, not structure]")

# (E) kernels: MV0 full (5x5) vs the theta maps
kerM = nullspace([[MV0[i][j] for j in range(5)] for i in range(5)])
log(f"  ker(MV0 as 5x5 form) dim = {len(kerM)}; "
    f"ker(Theta) dim = {len(kerT)}")
if len(kerM) == 1 and len(kerT) == 1:
    log(f"    ker(Theta) == ker(MV0) as lines: "
        f"{proportional(kerT[0], kerM[0])}")

# ===========================================================================
log("STEP 7: field of definition...")
pool = []
for d in (CVEC, Qq):
    for v in d.values():
        pool.extend(v)
for rws in (OH, Theta, Psi, S, M, MV0, P):
    for row in rws:
        pool.extend(row)
pool.extend([muN, lamN, nu, c0, s0, rho_pred])
n_rat = sum(1 for x in pool if x.b == 0)
n_irr = sum(1 for x in pool if x.b != 0)
log(f"  every decisive value lies in K = Q(sqrt-3) EXACTLY (constructed "
    f"in K; zero floats): {len(pool)} values scanned, "
    f"{n_rat} rational, {n_irr} genuinely need sqrt(-3)")
log("  subfield-theorem expectation k(Gamma) = Q(sqrt-3): CONFIRMED for "
    "the values -- no larger field appears in the cup-value table, the "
    "sigma2 matrix, or the natural-operator matrix")
irr_cvec = any(x.b != 0 for v in CVEC.values() for x in v)
log(f"  the H^2 coordinates genuinely use sqrt(-3) (not defined over Q): "
    f"{irr_cvec}")
log("  eigenvalue fields: operator spectra read off the STEP 6 "
    "factorizations; slice eigenvalues +-mu with mu^2 in K -- mu itself "
    "in K only where the exact square-in-K test says so (STEP 6 lines)")

# ===========================================================================
log("STEP 8: VERDICT ASSEMBLY...")
log(f"  natural-operator spectrum on the generation quotient: "
    f"{ndA} distinct eigenvalue(s) of 3")
log(f"  natural-operator spectrum on the full H^1: {ndF} distinct of 5")
log(f"  cup basis rank: {len(BP)} (surjectivity {CUP_SPAN_5}); "
    f"relation-lattice dim {len(RELS)}; star-class rank {star_rank}")
log(f"  Y factors through the cup coordinates: {g_ycons}; rank(P) = "
    f"{PRANK}")
log(f"  swap law: {law_ok}; sigma2 involution: {g_invol}; MV0 scalar "
    f"law: {g_mv0law}; sigma-covariance of OH: {g_cov}")
if ndA == 3:
    log("  OUTCOME: DISTINGUISHING STRUCTURE -- the natural operator "
        "thetabar o theta has THREE DISTINCT eigenvalues on the "
        "generation quotient (basis-free ratios).")
elif ndA > 0:
    log(f"  OUTCOME: the FIFTH WALL -- the natural operator collapses "
        f"({ndA} distinct of 3 on the quotient), every H^2-functional "
        "slice is a forced antisymmetric {0,+mu,-mu}, the PD/Hodge "
        "slice is scalar, and the star values are normalization gauge. "
        "The exact cup-value table, the sigma2/swap laws, and the "
        "natural-operator spectrum bank as the new invariants.")
else:
    log("  OUTCOME: quotient operator not defined -- see block gate.")

# persist the machine-readable value table (data artifact for cell 7)
art = {
    "artifact": "b666_cell2_cup_values",
    "object": "golden (figure-eight) unbent weld double D; banked "
              "5-class H^1(D;27) basis (b637 double_Y(None))",
    "field": "K = Q(sqrt-3); [a,b] means a + b*sqrt(-3)",
    "h2_basis": [list(bp) for bp in BP],
    "h2_basis_meaning": "b_m = [u_p cup u_q] for (p,q) in h2_basis",
    "cup_class_coords": {f"{i},{j}": [[str(x.a), str(x.b)]
                                      for x in CVEC[(i, j)]]
                         for i in range(5) for j in range(5)},
    "class_antisymmetry_25of25": bool(g_anti),
    "cup_surjective_rank5": bool(CUP_SPAN_5),
    "radical_H2_valued_form": [[[str(x.a), str(x.b)] for x in v]
                               for v in RADFULL],
    "P_matrix_Y_pairing": [[[str(x.a), str(x.b)] for x in row]
                           for row in P],
    "P_rank": PRANK,
    "Y_factors_through_coords_125": bool(g_ycons),
    "MV0": [[[str(x.a), str(x.b)] for x in row] for row in MV0],
    "sigma2_matrix_cup_basis": [[[str(x.a), str(x.b)] for x in row]
                                for row in S],
    "swap_law": "sigma2[c_ij] = sum_kl M_ik M_jl [c_kl] (M = "
                "sigma_matrix_golden.json); verified 25/25",
    "sigma_scalars": {"nu_J2": [str(nu.a), str(nu.b)],
                      "c0_J_on_v0": [str(c0.a), str(c0.b)],
                      "s0_H2C": [str(s0.a), str(s0.b)],
                      "rho_MV0_law": [str(rho_pred.a), str(rho_pred.b)]},
    "natural_operator_OH": [[[str(x.a), str(x.b)] for x in row]
                            for row in OH],
    "Theta": [[[str(x.a), str(x.b)] for x in row] for row in Theta],
    "Psi": [[[str(x.a), str(x.b)] for x in row] for row in Psi],
    "muN_lamN": [[str(muN.a), str(muN.b)], [str(lamN.a), str(lamN.b)]],
    "quotient_operator_distinct_eigenvalues": ndA,
}
JP = os.path.join(HERE, "cell2_cup_values.json")
with open(JP, "w") as f:
    json.dump(art, f, indent=1)
log(f"  persisted {JP}")

log("CELL 2 COMPUTATION COMPLETE")
