"""B662 CELL E (L102) -- the CANONICAL boundary-restriction decomposition
on both doubles, and the portal re-expressed in it.

CANONICAL CONSTRUCTION (object-uniform, defined identically on the golden
fig-8 double and the silver m136 double, and identically on the primal 27
and dual 27-bar local systems):

  boundary-born   B    := ker( H1(D;V) -> H1(M_side1;V) (+) H1(M_side2;V) )
                          (restriction of the Fox cocycle to the two solo-side
                           subgroups; by Mayer-Vietoris exactness this equals
                           image(delta^0: H0(T^2;V) -> H1(D;V)) -- precisely
                           what B637's "coker-delta^0 pair" means on the golden)
  peripheral ker  K_T  := ker( H1(D;V) -> H1(T^2;V) )
                          (Fox-cocycle evaluation on the peripheral MU/LAM
                           words; functorially B is contained in K_T)

  Both subspaces are basis-free.  With B (primal) and B* (dual) canonical:
  in ANY pair of bases adapted to (B, B*), the lower-left block of the portal
  (the components of P(B) outside B*) is basis-independent; the upper-right
  block is complement-gauge.  Hence:

  THE DECISIVE CANONICAL TEST:  P(B) = B*
     holds  => adapted bases exist in which P is EXACTLY block-diagonal
               (2x2 (+) 3x3): sector-respecting.
     fails  => NO basis in the canonical construction removes the off-block
               entries: genuinely triangular / knot-specific.

Exact arithmetic throughout the decisive path: K = Q(sqrt(-3)) Fraction pairs
(golden), L = Q(s,i), s^4 = 8 s^2 + 16, Fraction 4-vectors (silver).  Floats
appear only in timing prints.

Machinery reused (read-only): frontier/B637_corrected_cell3/b637_threeform.py
(exec, the b658 pattern), frontier/B649_silver_holonomy/b649_stage3b_swap.py
prefix (exec, the w2a pattern), the B657 packet's w1/w2a portal code paths
(copied logic; '<repo>' placeholders replaced by the absolute repo path).
"""
import json
import os
import time
from fractions import Fraction as Fr

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

REPO = "/Users/dri/origin-axiom"
HERE = os.path.join(REPO, "frontier", "B662_successor_campaign", "cellE")
B637D = os.path.join(REPO, "frontier", "B637_corrected_cell3")
B649D = os.path.join(REPO, "frontier", "B649_silver_holonomy")
W2A_JSON = os.path.join(REPO, "frontier", "B657_invariant_line", "packet",
                        "w2_silver", "silver_portal.json")

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


d = 27

# ============================================================================
# generic exact linear algebra over a field element type supporting
# +, -, *, .inv(), .is_zero()   (K and L both do; no unary minus used)
# ============================================================================

def rrefF(rows, zero):
    A = [r[:] for r in rows]
    m = len(A)
    ncols = len(A[0]) if m else 0
    r = 0
    pivs = []
    for c in range(ncols):
        piv = next((k for k in range(r, m) if not A[k][c].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv_inv = A[r][c].inv()
        A[r] = [x * pv_inv for x in A[r]]
        for k in range(m):
            if k != r and not A[k][c].is_zero():
                f = A[k][c]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        pivs.append(c)
        r += 1
        if r == m:
            break
    return A, pivs


def rankF(rows, zero):
    if not rows:
        return 0
    _, pivs = rrefF(rows, zero)
    return len(pivs)


def rref_basisF(rows, zero):
    """canonical (RREF) basis of the row space."""
    if not rows:
        return []
    A, pivs = rrefF(rows, zero)
    return A[:len(pivs)]


def nullspaceF(rows, ncols, zero, one):
    A = [r[:] for r in rows]
    m = len(A)
    r = 0
    pivs = []
    for c in range(ncols):
        piv = next((k for k in range(r, m) if not A[k][c].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv_inv = A[r][c].inv()
        A[r] = [x * pv_inv for x in A[r]]
        for k in range(m):
            if k != r and not A[k][c].is_zero():
                f = A[k][c]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        pivs.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(ncols) if c not in pivs]
    basis = []
    for fc in free:
        v = [zero] * ncols
        v[fc] = one
        for rr, pc in enumerate(pivs):
            v[pc] = zero - A[rr][fc]
        basis.append(v)
    return basis


def in_spanF(base_rows, v, zero):
    if not base_rows:
        return all(x.is_zero() for x in v)
    return rankF(base_rows + [v], zero) == rankF(base_rows, zero)


def solve_squareF(cols_mat, b, zero):
    """solve M z = b with M given by COLUMNS cols_mat (list of column
    vectors), all length n; returns z or raises."""
    n = len(b)
    aug = [[cols_mat[j][i] for j in range(len(cols_mat))] + [b[i]]
           for i in range(n)]
    A, pivs = rrefF(aug, zero)
    ncols = len(cols_mat)
    z = [zero] * ncols
    for r_i, pc in enumerate(pivs):
        if pc < ncols:
            z[pc] = A[r_i][ncols]
        else:
            raise ValueError("inconsistent square solve")
    # residual check (exact)
    for i in range(n):
        acc = zero
        for j in range(ncols):
            if not z[j].is_zero():
                acc = acc + cols_mat[j][i] * z[j]
        if not (acc - b[i]).is_zero():
            raise ValueError("solve residual nonzero")
    return z


def matvecF(M, v, zero):
    n = len(v)
    return [sum((M[i][k] * v[k] for k in range(n) if not v[k].is_zero()),
                zero) for i in range(len(M))]


def meyeF(n, zero, one):
    return [[one if i == j else zero for j in range(n)] for i in range(n)]


def fox_rowsF(relators, gens, lets, zero, one, mmulF):
    prim = {g: g for g in gens}
    prim.update({g.upper(): g for g in gens})
    rows = []
    for w in relators:
        blocks = {g: [[zero] * d for _ in range(d)] for g in gens}
        P = meyeF(d, zero, one)
        for ch in w:
            g = prim[ch]
            if ch.islower():
                T = P
                B_ = blocks[g]
                for i in range(d):
                    Bi, Ti = B_[i], T[i]
                    for j in range(d):
                        Bi[j] = Bi[j] + Ti[j]
            else:
                T = mmulF(P, lets[ch])
                B_ = blocks[g]
                for i in range(d):
                    Bi, Ti = B_[i], T[i]
                    for j in range(d):
                        Bi[j] = Bi[j] - Ti[j]
            P = mmulF(P, lets[ch])
        for i in range(d):
            rows.append([blocks[g][i][j] for g in gens for j in range(d)])
    return rows


def cob_rowsF(gens, lets, zero, one):
    out = []
    for j in range(d):
        entry = []
        for g in gens:
            entry.extend([lets[g][i][j] - (one if i == j else zero)
                          for i in range(d)])
        out.append(entry)
    return out


class SpanF:
    def __init__(self, ncols):
        self.rows = []
        self.n = ncols

    def reduce(self, v):
        v = v[:]
        for (pc, w) in self.rows:
            f = v[pc]
            if not f.is_zero():
                v = [x - f * y for x, y in zip(v, w)]
        return v

    def add(self, v):
        v = self.reduce(v)
        pc = next((i for i in range(self.n) if not v[i].is_zero()), None)
        if pc is None:
            return False
        iv = v[pc].inv()
        v = [x * iv for x in v]
        self.rows.append((pc, v))
        return True


def cocycle_evalF(parts, word, lets, zero, one, mmulF):
    """u(word) for the crossed homomorphism u given on generators by parts
    (dict lowercase gen -> 27-vector); capitals = inverses."""
    val = [zero] * d
    P = meyeF(d, zero, one)
    for ch in word:
        u = parts[ch.lower()]
        if ch.islower():
            add = matvecF(P, u, zero)
            val = [val[i] + add[i] for i in range(d)]
        else:
            PM = mmulF(P, lets[ch])
            add = matvecF(PM, u, zero)
            val = [val[i] - add[i] for i in range(d)]
        P = mmulF(P, lets[ch])
    return val


def word_matF(word, lets, zero, one, mmulF):
    P = meyeF(d, zero, one)
    for ch in word:
        P = mmulF(P, lets[ch])
    return P


# ============================================================================
# the canonical analysis (one local system on one object)
# ============================================================================

def canonical_analysis(tag, reps, gens, side1, side2, side1_rels, side2_rels,
                       lets, mu_w, lam_w, zero, one, mmulF):
    """returns dict with B basis / K_T basis (class coordinates), torus dims,
    and gate results.  All exact."""
    res = {"tag": tag}
    nrep = len(reps)
    parts = [{g: rep[d * gi:d * (gi + 1)] for gi, g in enumerate(gens)}
             for rep in reps]

    # --- torus matrices + gates ---------------------------------------------
    M = word_matF(mu_w, lets, zero, one, mmulF)
    Lam = word_matF(lam_w, lets, zero, one, mmulF)
    ML = mmulF(M, Lam)
    LM = mmulF(Lam, M)
    res["gate_mu_lam_commute"] = all((ML[i][j] - LM[i][j]).is_zero()
                                     for i in range(d) for j in range(d))
    muv = [cocycle_evalF(p, mu_w, lets, zero, one, mmulF) for p in parts]
    lav = [cocycle_evalF(p, lam_w, lets, zero, one, mmulF) for p in parts]
    ok_compat = True
    for j in range(nrep):
        Mlam = matvecF(M, lav[j], zero)
        Lmu = matvecF(Lam, muv[j], zero)
        diff = [muv[j][i] + Mlam[i] - (lav[j][i] + Lmu[i]) for i in range(d)]
        if not all(x.is_zero() for x in diff):
            ok_compat = False
    res["gate_torus_cocycle_compat"] = ok_compat

    # --- torus cohomology dims ----------------------------------------------
    MmI = [[M[i][j] - (one if i == j else zero) for j in range(d)]
           for i in range(d)]
    LmI = [[Lam[i][j] - (one if i == j else zero) for j in range(d)]
           for i in range(d)]
    h0T = len(nullspaceF(MmI + LmI, d, zero, one))
    # Z1(T): (I - Lam) x + (M - I) y = 0   (x = u(mu), y = u(lam))
    z1t_rows = [[(one if i == j else zero) - Lam[i][j] for j in range(d)]
                + [M[i][j] - (one if i == j else zero) for j in range(d)]
                for i in range(d)]
    z1T = len(nullspaceF(z1t_rows, 2 * d, zero, one))
    rank_b1T = d - h0T
    res["h0_T"] = h0T
    res["z1_T"] = z1T
    res["h1_T"] = z1T - rank_b1T

    # --- B = ker( restriction to the two solo sides ) ------------------------
    # unknowns [x_0..x_{nrep-1}, v1 (27), v2 (27)]
    nun = nrep + 2 * d
    rows = []
    for g in side1:
        for i in range(d):
            row = [parts[j][g][i] for j in range(nrep)]
            row += [(one if i == k else zero) - lets[g][i][k]
                    for k in range(d)]          # -(rho(g) - I) v1
            row += [zero] * d
            rows.append(row)
    for g in side2:
        for i in range(d):
            row = [parts[j][g][i] for j in range(nrep)]
            row += [zero] * d
            row += [(one if i == k else zero) - lets[g][i][k]
                    for k in range(d)]          # -(rho(g) - I) v2
            rows.append(row)
    nsB = nullspaceF(rows, nun, zero, one)
    xproj = [v[:nrep] for v in nsB if any(not x.is_zero() for x in v[:nrep])]
    B_basis = rref_basisF(xproj, zero) if xproj else []
    res["dim_B"] = len(B_basis)
    res["B_basis"] = B_basis
    res["B_system_nullity"] = len(nsB)

    # --- K_T = ker( restriction to the peripheral torus ) --------------------
    nun2 = nrep + d
    rows2 = []
    for i in range(d):
        row = [muv[j][i] for j in range(nrep)]
        row += [(one if i == k else zero) - M[i][k] for k in range(d)]
        rows2.append(row)
    for i in range(d):
        row = [lav[j][i] for j in range(nrep)]
        row += [(one if i == k else zero) - Lam[i][k] for k in range(d)]
        rows2.append(row)
    nsK = nullspaceF(rows2, nun2, zero, one)
    xprojK = [v[:nrep] for v in nsK if any(not x.is_zero() for x in v[:nrep])]
    KT_basis = rref_basisF(xprojK, zero) if xprojK else []
    res["dim_KT"] = len(KT_basis)
    res["KT_basis"] = KT_basis
    res["KT_system_nullity"] = len(nsK)

    # --- functorial containment gate  B <= K_T -------------------------------
    res["gate_B_in_KT"] = all(in_spanF(KT_basis, bv, zero) for bv in B_basis) \
        if B_basis else True
    return res


def adapted_tests(portal, prim_res, dual_res, zero, one, fmt):
    """the decisive canonical tests + the re-expressed matrices."""
    out = {}
    nrep = len(portal)
    B = prim_res["B_basis"]
    Bs = dual_res["B_basis"]
    out["dim_B_primal"] = len(B)
    out["dim_B_dual"] = len(Bs)

    def apply_portal(x):
        return [sum((portal[i][j] * x[j] for j in range(nrep)
                     if not x[j].is_zero()), zero) for i in range(nrep)]

    # decisive: P(B) subset of B* (and equality by dimension when iso)
    per_vec = [in_spanF(Bs, apply_portal(bv), zero) for bv in B]
    out["P_of_B_in_Bstar_per_vector"] = per_vec
    PB_in = all(per_vec)
    out["P_of_B_in_Bstar"] = PB_in
    imgs = [apply_portal(bv) for bv in B]
    out["dim_P_of_B"] = rankF(imgs, zero) if imgs else 0
    out["P_of_B_equals_Bstar"] = (PB_in and out["dim_P_of_B"] == len(Bs))

    # refinement on the canonical flag with K_T
    KT = prim_res["KT_basis"]
    KTs = dual_res["KT_basis"]
    per_vec_kt = [in_spanF(KTs, apply_portal(bv), zero) for bv in KT]
    out["P_of_KT_in_KTstar_per_vector"] = per_vec_kt
    out["P_of_KT_in_KTstar"] = all(per_vec_kt)
    out["dim_KT_primal"] = len(KT)
    out["dim_KT_dual"] = len(KTs)

    # deterministic adapted bases: B-basis (canonical RREF) completed by the
    # first banked class vectors e_j that extend the span (same rule on both
    # sides and both objects)
    def complete(basis):
        cols = [list(b) for b in basis]
        for j in range(nrep):
            e = [one if t == j else zero for t in range(nrep)]
            if not in_spanF(cols, e, zero):
                cols.append(e)
            if len(cols) == nrep:
                break
        return cols

    Tpr = complete(B)        # rows are basis vectors; use as columns below
    Tdu = complete(Bs)
    out["adapted_primal_basis"] = [[fmt(x) for x in v] for v in Tpr]
    out["adapted_dual_basis"] = [[fmt(x) for x in v] for v in Tdu]
    # P_adapted[i][j] = coords of P(Tpr[j]) in the Tdu basis
    Tdu_cols = [list(v) for v in Tdu]
    P_ad = [[None] * nrep for _ in range(nrep)]
    for j in range(nrep):
        w = apply_portal(Tpr[j])
        z = solve_squareF(Tdu_cols, w, zero)
        for i in range(nrep):
            P_ad[i][j] = z[i]
    out["adapted_matrix"] = [[fmt(P_ad[i][j]) for j in range(nrep)]
                             for i in range(nrep)]
    kB, kBs = len(B), len(Bs)
    ll = [[fmt(P_ad[i][j]) for j in range(kB)] for i in range(kBs, nrep)]
    ur = [[fmt(P_ad[i][j]) for j in range(kB, nrep)] for i in range(kBs)]
    out["lower_left_block"] = ll
    out["lower_left_zero_CANONICAL"] = all(
        P_ad[i][j].is_zero() for i in range(kBs, nrep) for j in range(kB))
    out["upper_right_block_gauge"] = ur

    # gauge exhibition: if P(B) = B*, the dual adapted basis
    # (B*-rref, P(c_1), ..., P(c_k)) makes P literally block-diagonal
    if out["P_of_B_equals_Bstar"] and kB == kBs and kB > 0:
        Tdu2 = [list(b) for b in Bs] + [apply_portal(Tpr[j])
                                        for j in range(kB, nrep)]
        Tdu2_cols = [list(v) for v in Tdu2]
        P_g = [[None] * nrep for _ in range(nrep)]
        okg = True
        for j in range(nrep):
            w = apply_portal(Tpr[j])
            try:
                z = solve_squareF(Tdu2_cols, w, zero)
            except ValueError:
                okg = False
                break
            for i in range(nrep):
                P_g[i][j] = z[i]
        if okg:
            out["gauge_exhibited_matrix"] = [
                [fmt(P_g[i][j]) for j in range(nrep)] for i in range(nrep)]
            out["gauge_block_diagonal_exact"] = all(
                P_g[i][j].is_zero()
                for i in range(nrep) for j in range(nrep)
                if (i < kBs) != (j < kB))
    return out


# ============================================================================
# ============================  PART 1: GOLDEN  ==============================
# ============================================================================
log("PART 1 (GOLDEN): exec b637_threeform.py (B575 prefix + cubic + weld)...")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637D, "b637_threeform.py")}
exec(compile(open(os.path.join(B637D, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
log("  b637_threeform module loaded")

Kf = mod["K"]
K0, K1 = mod["K0"], mod["K1"]
A27, B27, A27i, B27i = mod["A27"], mod["B27"], mod["A27i"], mod["B27i"]
REL, LONG = mod["REL"], mod["LONG"]
mmulK = mod["mmul"]
CFULL = mod["CFULL"]
side2lets = mod["side2lets"]
bns = mod["ns"]
nullspaceK = bns["nullspace"]
rrefK = bns["rref"]
SolverK = bns["Solver"]
inv_word = mod["inv"]


def fmtK(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b > 0 else ''}{x.b}*sqrt(-3))"


GENS_G = "abcd"
lets_G = {'a': A27, 'A': A27i, 'b': B27, 'B': B27i,
          'c': side2lets['a'], 'C': side2lets['A'],
          'd': side2lets['b'], 'D': side2lets['B']}
RELS_G = [REL, REL.translate(str.maketrans("abAB", "cdCD")), "aC",
          LONG + LONG.translate(str.maketrans("abAB", "cdCD"))]
log(f"  golden double presentation: gens={GENS_G!r} relators={RELS_G}")

# relator gates
for w in RELS_G:
    Pw = word_matF(w, lets_G, K0, K1, mmulK)
    assert all((Pw[i][j] - (K1 if i == j else K0)).is_zero()
               for i in range(d) for j in range(d)), f"relator {w} != I"
log("  all 4 golden relators = I27 exactly (gate PASS)")

log("  golden primal Fox rows + Z1 + coboundaries + the 5 classes...")
t0 = time.time()
rowsG = fox_rowsF(RELS_G, GENS_G, lets_G, K0, K1, mmulK)
ZcG = nullspaceF(rowsG, 4 * d, K0, K1)
cobG = cob_rowsF(GENS_G, lets_G, K0, K1)
rank_cobG = rankF(cobG, K0)
h0_G = d - rank_cobG
h1_G = len(ZcG) - rank_cobG
log(f"  golden double: dim Z1 = {len(ZcG)}, rank B1 = {rank_cobG}, "
    f"h0 = {h0_G}, h1 = {h1_G}  ({time.time()-t0:.0f}s)")
assert (h0_G, h1_G) == (1, 5), "golden double dims gate FAILED"

spanG = SpanF(4 * d)
for cv in cobG:
    spanG.add(cv)
reps_G = []
for z in ZcG:
    if spanG.add(z):
        reps_G.append(z)
    if len(reps_G) == 5:
        break
assert len(reps_G) == 5
log(f"  extracted {len(reps_G)} golden primal class representatives")

# v0 golden
AmI = [[A27[i][j] - (K1 if i == j else K0) for j in range(d)] for i in range(d)]
BmI = [[B27[i][j] - (K1 if i == j else K0) for j in range(d)] for i in range(d)]
v0b = nullspaceF(AmI + BmI, d, K0, K1)
assert len(v0b) == 1, f"golden v0 dim {len(v0b)} != 1"
v0G_raw = v0b[0]
idx0 = next(i for i, x in enumerate(v0G_raw) if not x.is_zero())
sc = v0G_raw[idx0].inv()
v0G = [sc * x for x in v0G_raw]
for gch in ('c', 'd'):
    dv = [matvecF(lets_G[gch], v0G, K0)[i] - v0G[i] for i in range(d)]
    assert all(x.is_zero() for x in dv), f"v0 not invariant under {gch}"
log("  golden v0: dim 1, invariant under all four generators (gates PASS)")


def C3_G(u, v):
    cov = [K0] * d
    for (p, q, r_), cval in CFULL.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r_] = cov[r_] + cval * u[p] * v[q]
    return cov


# N invariance gate (all four generators, one deterministic triple)
u1 = [Kf(i % 5 - 2) for i in range(d)]
v1 = [Kf((2 * i) % 7 - 3) for i in range(d)]
w1 = [Kf((3 * i) % 4 - 1) for i in range(d)]


def dotK(f, v):
    return sum((f[t] * v[t] for t in range(d) if not v[t].is_zero()), K0)


for gch in GENS_G:
    Mg = lets_G[gch]
    lhs = dotK(C3_G(matvecF(Mg, u1, K0), matvecF(Mg, v1, K0)),
               matvecF(Mg, w1, K0))
    rhs = dotK(C3_G(u1, v1), w1)
    assert (lhs - rhs).is_zero(), f"golden N not invariant under {gch}"
log("  golden cubic N invariant under all four double generators (gate PASS)")

log("  golden dual system (contragredient) ...")
dacts_G = {}
for g in GENS_G:
    Gu = g.upper()
    dacts_G[g] = [[lets_G[Gu][j][i] for j in range(d)] for i in range(d)]
    dacts_G[Gu] = [[lets_G[g][j][i] for j in range(d)] for i in range(d)]

t0 = time.time()
rowsG_du = fox_rowsF(RELS_G, GENS_G, dacts_G, K0, K1, mmulK)
Z1G_du = nullspaceF(rowsG_du, 4 * d, K0, K1)
cobG_du = cob_rowsF(GENS_G, dacts_G, K0, K1)
rank_cobG_du = rankF(cobG_du, K0)
h1G_du = len(Z1G_du) - rank_cobG_du
log(f"  golden dual: dim Z1 = {len(Z1G_du)}, rank B1 = {rank_cobG_du}, "
    f"h1(dual) = {h1G_du}  ({time.time()-t0:.0f}s)")
assert h1G_du == 5, "golden dual h1 gate FAILED"

spanG_du = SpanF(4 * d)
for cv in cobG_du:
    spanG_du.add(cv)
duals_G = []
for z in Z1G_du:
    if spanG_du.add(z):
        duals_G.append(z)
    if len(duals_G) == 5:
        break
assert len(duals_G) == 5
log("  extracted 5 golden dual class representatives")

basisG = duals_G + cobG_du


def reduce_to_classes_G(target):
    aug = [list(col) + [target[r]] for r, col in enumerate(zip(*basisG))]
    Rr2, piv2 = rrefK([row[:] for row in aug])
    coeff = [K0] * len(basisG)
    for r_i, p_j in enumerate(piv2):
        if p_j < len(basisG):
            coeff[p_j] = Rr2[r_i][len(basisG)]
    resid = [target[r] - sum((coeff[k] * basisG[k][r] for k in range(len(basisG))
                              if not coeff[k].is_zero()), K0)
             for r in range(len(target))]
    return coeff[:5], all(x.is_zero() for x in resid)


def is_dual_cocycle_G(vec):
    for row in rowsG_du:
        s_ = K0
        for t in range(4 * d):
            if not vec[t].is_zero() and not row[t].is_zero():
                s_ = s_ + row[t] * vec[t]
        if not s_.is_zero():
            return False
    return True


def P_of_G(rep):
    parts = {g: rep[d * gi:d * (gi + 1)] for gi, g in enumerate(GENS_G)}
    out = []
    for g in GENS_G:
        out.extend(C3_G(v0G, parts[g]))
    return out


log("  THE GOLDEN PORTAL (my basis; the canonical facts are basis-free)...")
PORTAL_G = [[None] * 5 for _ in range(5)]
for j in range(5):
    tgt = P_of_G(reps_G[j])
    assert is_dual_cocycle_G(tgt), f"golden P(u_{j}) not a dual cocycle"
    coeffs, okr = reduce_to_classes_G(tgt)
    assert okr, f"golden class {j} residual not clean"
    for i in range(5):
        PORTAL_G[i][j] = coeffs[i]
rank_PG = rankF([[PORTAL_G[i][j] for j in range(5)] for i in range(5)], K0)
ker_PG = 5 - rank_PG
log(f"  golden portal rank = {rank_PG}, kernel dim = {ker_PG} "
    f"[GATE rank 5, kernel 0]")
assert rank_PG == 5 and ker_PG == 0
for i in range(5):
    log("    [" + ", ".join(fmtK(PORTAL_G[i][j]) for j in range(5)) + "]")

log("  golden canonical analysis (primal)...")
canG_pr = canonical_analysis("golden-primal", reps_G, GENS_G, "ab", "cd",
                             [RELS_G[0]], [RELS_G[1]], lets_G, "a", LONG,
                             K0, K1, mmulK)
log(f"    torus: h0(T;27) = {canG_pr['h0_T']} (= i2), z1_T = {canG_pr['z1_T']}, "
    f"h1(T;27) = {canG_pr['h1_T']}")
log(f"    gates: commute={canG_pr['gate_mu_lam_commute']} "
    f"compat={canG_pr['gate_torus_cocycle_compat']} "
    f"B_in_KT={canG_pr['gate_B_in_KT']}")
log(f"    dim B (boundary-born) = {canG_pr['dim_B']}; "
    f"dim K_T (peripheral kernel) = {canG_pr['dim_KT']}")
log("    B basis (class coords): " +
    str([[fmtK(x) for x in v] for v in canG_pr['B_basis']]))
log("    K_T basis (class coords): " +
    str([[fmtK(x) for x in v] for v in canG_pr['KT_basis']]))

log("  golden canonical analysis (dual)...")
canG_du = canonical_analysis("golden-dual", duals_G, GENS_G, "ab", "cd",
                             [RELS_G[0]], [RELS_G[1]], dacts_G, "a", LONG,
                             K0, K1, mmulK)
log(f"    torus(dual): h0 = {canG_du['h0_T']}, h1 = {canG_du['h1_T']}; "
    f"gates: commute={canG_du['gate_mu_lam_commute']} "
    f"compat={canG_du['gate_torus_cocycle_compat']} "
    f"B_in_KT={canG_du['gate_B_in_KT']}")
log(f"    dim B* = {canG_du['dim_B']}; dim K_T* = {canG_du['dim_KT']}")
log("    B* basis (class coords): " +
    str([[fmtK(x) for x in v] for v in canG_du['B_basis']]))

log("  GOLDEN DECISIVE TESTS (the control)...")
testG = adapted_tests(PORTAL_G, canG_pr, canG_du, K0, K1, fmtK)
log(f"    P(B) in B* per vector: {testG['P_of_B_in_Bstar_per_vector']}")
log(f"    P(B) = B*: {testG['P_of_B_equals_Bstar']}")
log(f"    P(K_T) in K_T*: {testG['P_of_KT_in_KTstar']}")
log(f"    adapted matrix (deterministic complement):")
for row in testG["adapted_matrix"]:
    log("      [" + ", ".join(row) + "]")
log(f"    lower-left block zero (CANONICAL, basis-free): "
    f"{testG['lower_left_zero_CANONICAL']}")
if "gauge_block_diagonal_exact" in testG:
    log(f"    gauge-exhibited block-diagonal exact: "
        f"{testG['gauge_block_diagonal_exact']}")
    for row in testG["gauge_exhibited_matrix"]:
        log("      [" + ", ".join(row) + "]")

golden_control_pass = (canG_pr["dim_B"] == 2 and canG_du["dim_B"] == 2
                       and testG["P_of_B_equals_Bstar"]
                       and testG["lower_left_zero_CANONICAL"])
log(f"  *** GOLDEN CONTROL (canonical construction reproduces the banked "
    f"block-diagonality): {'PASS' if golden_control_pass else 'FAIL'} ***")

json.dump({
    "object": "figure-eight weld double (B637 4-generator amalgam), K=Q(sqrt-3)",
    "presentation": {"gens": GENS_G, "relators": RELS_G,
                     "side1": "ab", "side2": "cd",
                     "mu": "a", "lam": LONG},
    "portal_matrix_readable": [[fmtK(PORTAL_G[i][j]) for j in range(5)]
                               for i in range(5)],
    "portal_rank": rank_PG, "portal_kernel": ker_PG,
    "canonical_primal": {k: ([[fmtK(x) for x in v] for v in canG_pr[k]]
                             if k in ("B_basis", "KT_basis") else canG_pr[k])
                         for k in canG_pr},
    "canonical_dual": {k: ([[fmtK(x) for x in v] for v in canG_du[k]]
                           if k in ("B_basis", "KT_basis") else canG_du[k])
                       for k in canG_du},
    "tests": {k: v for k, v in testG.items()},
    "control_pass": golden_control_pass,
}, open(os.path.join(HERE, "golden_canonical.json"), "w"), indent=2)
log("  saved golden_canonical.json")

# free the golden memory
del mod, rowsG, rowsG_du, ZcG, Z1G_du, cobG, cobG_du, basisG, spanG, spanG_du

# ============================================================================
# ============================  PART 2: SILVER  ==============================
# ============================================================================
log("PART 2 (SILVER): exec b649_stage3b_swap.py prefix (weld + double + reps)...")
SWAP = os.path.join(B649D, "b649_stage3b_swap.py")
src = open(SWAP).read()
cut = src.index("# ---- sigma* ---")
sns = {"__name__": "b649_double_prefix", "__file__": SWAP}
t0 = time.time()
exec(compile(src[:cut], SWAP, "exec"), sns)
log(f"  silver prefix exec complete ({time.time()-t0:.0f}s)")

Lf, Lc = sns["L"], sns["Lc"]
L0, L1 = sns["L0"], sns["L1"]
mmulL = sns["mmul"]
LETS_S = sns["LETS"]
RELS_S, GENS_S = sns["RELATORS"], sns["GENS"]
Z1_S = sns["Z1"]
cob_S = sns["cob"]
reps_S = sns["reps"]
nc_S = sns["nc"]
L_nullspace_basis = sns["L_nullspace_basis"]
SpanL = sns["Span"]
S1 = sns["S1"]

h0_S = d - nc_S
h1_S = len(Z1_S) - nc_S
log(f"  silver double: h0 = {h0_S}, h1 = {h1_S}  [GATE (1,5)]")
assert (h0_S, h1_S) == (1, 5), "silver double dims gate FAILED"
assert len(reps_S) == 5


def fmtL(x):
    if x.is_zero():
        return "0"

    def poly_str(coeffs, varname):
        terms = []
        for k, c in enumerate(coeffs):
            if c == 0:
                continue
            if k == 0:
                terms.append(f"{c}")
            elif k == 1:
                terms.append(f"{c}*{varname}")
            else:
                terms.append(f"{c}*{varname}^{k}")
        return "+".join(terms) if terms else "0"

    re_s = poly_str(x.re, "s")
    im_s = poly_str(x.im, "s")
    if im_s == "0":
        return re_s
    return f"({re_s}) + i*({im_s})"


# v0 silver
AmI_S = [[S1['a'][i][j] - (L1 if i == j else L0) for j in range(d)]
         for i in range(d)]
BmI_S = [[S1['b'][i][j] - (L1 if i == j else L0) for j in range(d)]
         for i in range(d)]
CmI_S = [[S1['c'][i][j] - (L1 if i == j else L0) for j in range(d)]
         for i in range(d)]
v0b_S = L_nullspace_basis(AmI_S + BmI_S + CmI_S, d)
assert len(v0b_S) == 1, f"silver v0 dim {len(v0b_S)} != 1"
v0S_raw = v0b_S[0]
idx0S = next(i for i, x in enumerate(v0S_raw) if not x.is_zero())
scS = v0S_raw[idx0S].inv()
v0S = [scS * x for x in v0S_raw]
for gch in ('d', 'e', 'f'):
    dv = [matvecF(LETS_S[gch], v0S, L0)[i] - v0S[i] for i in range(d)]
    assert all(x.is_zero() for x in dv), f"silver v0 not invariant under {gch}"
log("  silver v0: dim 1, invariant under d,e,f (gates PASS)")

CUB = {tuple(map(int, k.split(","))): Fr(v)
       for k, v in json.load(open(os.path.join(B649D,
                                               "cubic_rational.json"))).items()}


def C3_S(u, v):
    cov = [L0] * d
    for (p, q, r_), cval in CUB.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r_] = cov[r_] + Lc(cval) * u[p] * v[q]
    return cov


def dotL(f, v):
    return sum((f[t] * v[t] for t in range(d) if not v[t].is_zero()), L0)


u1s = [Lc(Fr(i % 5 - 2)) for i in range(d)]
v1s = [Lc(Fr((2 * i) % 7 - 3)) for i in range(d)]
w1s = [Lc(Fr((3 * i) % 4 - 1)) for i in range(d)]
for gch in GENS_S:
    Mg = LETS_S[gch]
    lhs = dotL(C3_S(matvecF(Mg, u1s, L0), matvecF(Mg, v1s, L0)),
               matvecF(Mg, w1s, L0))
    rhs = dotL(C3_S(u1s, v1s), w1s)
    assert (lhs - rhs).is_zero(), f"silver N not invariant under {gch}"
log("  silver cubic N invariant under all six double generators (gate PASS)")

log("  silver dual system (contragredient; 162x162 over L -- the heavy step)...")
dacts_S = {}
for g in GENS_S:
    Gu = g.upper()
    dacts_S[g] = [[LETS_S[Gu][j][i] for j in range(d)] for i in range(d)]
    dacts_S[Gu] = [[LETS_S[g][j][i] for j in range(d)] for i in range(d)]

t0 = time.time()
rowsS_du = fox_rowsF(RELS_S, GENS_S, dacts_S, L0, L1, mmulL)
log(f"  silver dual Fox rows built ({time.time()-t0:.0f}s)")
t0 = time.time()
Z1S_du = L_nullspace_basis(rowsS_du, 6 * d)
log(f"  dim Z1(dual) = {len(Z1S_du)}  ({time.time()-t0:.0f}s)")

cobS_du = cob_rowsF(GENS_S, dacts_S, L0, L1)
span_du = SpanL(6 * d)
rank_cobS_du = 0
for cv in cobS_du:
    if span_du.add(cv, None):
        rank_cobS_du += 1
h1S_du = len(Z1S_du) - rank_cobS_du
log(f"  silver dual: rank B1 = {rank_cobS_du}, h1(dual) = {h1S_du} [GATE 5]")
assert h1S_du == 5

span_cls = SpanL(6 * d)
for cv in cobS_du:
    span_cls.add(cv, None)
duals_S = []
for z in Z1S_du:
    if span_cls.add(z, None):
        duals_S.append(z)
    if len(duals_S) == 5:
        break
assert len(duals_S) == 5
log("  extracted 5 silver dual class representatives")

basisS = duals_S + cobS_du


def rrefL(rows):
    return rrefF(rows, L0)


def reduce_to_classes_S(target):
    aug = [list(col) + [target[r]] for r, col in enumerate(zip(*basisS))]
    Rr2, piv2 = rrefL(aug)
    coeff = [L0] * len(basisS)
    for r_i, p_j in enumerate(piv2):
        if p_j < len(basisS):
            coeff[p_j] = Rr2[r_i][len(basisS)]
    resid = [target[r] - sum((coeff[k] * basisS[k][r]
                              for k in range(len(basisS))
                              if not coeff[k].is_zero()), L0)
             for r in range(len(target))]
    return coeff[:5], all(x.is_zero() for x in resid)


def is_dual_cocycle_S(vec):
    for row in rowsS_du:
        s_ = L0
        for t in range(6 * d):
            if not vec[t].is_zero() and not row[t].is_zero():
                s_ = s_ + row[t] * vec[t]
        if not s_.is_zero():
            return False
    return True


def P_of_S(rep):
    parts = {g: rep[d * gi:d * (gi + 1)] for gi, g in enumerate(GENS_S)}
    out = []
    for g in GENS_S:
        out.extend(C3_S(v0S, parts[g]))
    return out


log("  THE SILVER PORTAL (recomputed; must match the banked w2a matrix)...")
PORTAL_S = [[None] * 5 for _ in range(5)]
for j in range(5):
    tgt = P_of_S(reps_S[j])
    assert is_dual_cocycle_S(tgt), f"silver P(u_{j}) not a dual cocycle"
    coeffs, okr = reduce_to_classes_S(tgt)
    assert okr, f"silver class {j} residual not clean"
    for i in range(5):
        PORTAL_S[i][j] = coeffs[i]
rank_PS = rankF([[PORTAL_S[i][j] for j in range(5)] for i in range(5)], L0)
ker_PS = 5 - rank_PS
log(f"  silver portal rank = {rank_PS}, kernel dim = {ker_PS} "
    f"[GATE rank 5, kernel 0]")
assert rank_PS == 5 and ker_PS == 0
for i in range(5):
    log("    [" + ", ".join(fmtL(PORTAL_S[i][j]) for j in range(5)) + "]")

# cross-check against the banked silver_portal.json (exact, entry-for-entry)
banked = json.load(open(W2A_JSON))
match = True
for i in range(5):
    for j in range(5):
        re_l = eval(banked["portal_matrix"][i][j][0], {"Fraction": Fr})
        im_l = eval(banked["portal_matrix"][i][j][1], {"Fraction": Fr})
        x = PORTAL_S[i][j]
        if list(x.re) != list(re_l) or list(x.im) != list(im_l):
            match = False
log(f"  banked-matrix cross-check (silver_portal.json, exact): "
    f"{'MATCH' if match else 'MISMATCH'}")

log("  silver canonical analysis (primal)...")
canS_pr = canonical_analysis("silver-primal", reps_S, GENS_S, "abc", "def",
                             RELS_S[:2], RELS_S[2:4], LETS_S, "CCB", "caCA",
                             L0, L1, mmulL)
log(f"    torus: h0(T;27) = {canS_pr['h0_T']} (= i2), z1_T = {canS_pr['z1_T']}, "
    f"h1(T;27) = {canS_pr['h1_T']}")
log(f"    gates: commute={canS_pr['gate_mu_lam_commute']} "
    f"compat={canS_pr['gate_torus_cocycle_compat']} "
    f"B_in_KT={canS_pr['gate_B_in_KT']}")
log(f"    dim B (boundary-born) = {canS_pr['dim_B']}; "
    f"dim K_T (peripheral kernel) = {canS_pr['dim_KT']}")
log("    B basis (class coords): " +
    str([[fmtL(x) for x in v] for v in canS_pr['B_basis']]))
log("    K_T basis (class coords): " +
    str([[fmtL(x) for x in v] for v in canS_pr['KT_basis']]))

log("  silver canonical analysis (dual)...")
canS_du = canonical_analysis("silver-dual", duals_S, GENS_S, "abc", "def",
                             RELS_S[:2], RELS_S[2:4], dacts_S, "CCB", "caCA",
                             L0, L1, mmulL)
log(f"    torus(dual): h0 = {canS_du['h0_T']}, h1 = {canS_du['h1_T']}; "
    f"gates: commute={canS_du['gate_mu_lam_commute']} "
    f"compat={canS_du['gate_torus_cocycle_compat']} "
    f"B_in_KT={canS_du['gate_B_in_KT']}")
log(f"    dim B* = {canS_du['dim_B']}; dim K_T* = {canS_du['dim_KT']}")
log("    B* basis (class coords): " +
    str([[fmtL(x) for x in v] for v in canS_du['B_basis']]))

log("  SILVER DECISIVE TESTS...")
testS = adapted_tests(PORTAL_S, canS_pr, canS_du, L0, L1, fmtL)
log(f"    P(B) in B* per vector: {testS['P_of_B_in_Bstar_per_vector']}")
log(f"    P(B) = B*: {testS['P_of_B_equals_Bstar']}")
log(f"    P(K_T) in K_T*: {testS['P_of_KT_in_KTstar']}")
log(f"    adapted matrix (deterministic complement):")
for row in testS["adapted_matrix"]:
    log("      [" + ", ".join(row) + "]")
log(f"    lower-left block zero (CANONICAL, basis-free): "
    f"{testS['lower_left_zero_CANONICAL']}")
if "gauge_block_diagonal_exact" in testS:
    log(f"    gauge-exhibited block-diagonal exact: "
        f"{testS['gauge_block_diagonal_exact']}")
    for row in testS["gauge_exhibited_matrix"]:
        log("      [" + ", ".join(row) + "]")

json.dump({
    "object": "m136 silver double (B649), L=Q(s,i), s^4=8s^2+16",
    "presentation": {"gens": GENS_S, "relators": RELS_S,
                     "side1": "abc", "side2": "def",
                     "mu": "CCB", "lam": "caCA"},
    "portal_matrix_readable": [[fmtL(PORTAL_S[i][j]) for j in range(5)]
                               for i in range(5)],
    "portal_rank": rank_PS, "portal_kernel": ker_PS,
    "banked_w2a_matrix_match": match,
    "canonical_primal": {k: ([[fmtL(x) for x in v] for v in canS_pr[k]]
                             if k in ("B_basis", "KT_basis") else canS_pr[k])
                         for k in canS_pr},
    "canonical_dual": {k: ([[fmtL(x) for x in v] for v in canS_du[k]]
                           if k in ("B_basis", "KT_basis") else canS_du[k])
                       for k in canS_du},
    "tests": {k: v for k, v in testS.items()},
}, open(os.path.join(HERE, "silver_canonical.json"), "w"), indent=2)
log("  saved silver_canonical.json")

# ============================================================================
# ================================  VERDICT  =================================
# ============================================================================
log("=" * 70)
silver_block = (testS["P_of_B_equals_Bstar"]
                and testS["lower_left_zero_CANONICAL"])
if not golden_control_pass:
    verdict = ("CONTROL-FAILURE: the canonical construction does NOT "
               "reproduce the banked golden block-diagonality -- the banked "
               "golden split was basis-luck at the canonical level; "
               "silver comparison reported but not upgraded.")
elif silver_block:
    verdict = ("BLOCK-DIAGONAL: the silver portal IS block-diagonal in the "
               "canonical boundary-restriction decomposition (P(B) = B* on "
               "both objects) => sector-respecting proposes FORCED "
               "(two objects).")
else:
    verdict = ("GENUINELY TRIANGULAR: no basis adapted to the canonical "
               "construction removes the silver off-block entries "
               "(P(B_silver) != B*_silver while the golden control passes) "
               "=> knot-specific geometry.")
log(f"*** CELL E VERDICT: {verdict} ***")
log(f"    golden: dim B = {canG_pr['dim_B']}, dim B* = {canG_du['dim_B']}, "
    f"P(B)=B*: {testG['P_of_B_equals_Bstar']}, "
    f"K_T dims {canG_pr['dim_KT']}/{canG_du['dim_KT']}, "
    f"P(K_T) in K_T*: {testG['P_of_KT_in_KTstar']}")
log(f"    silver: dim B = {canS_pr['dim_B']}, dim B* = {canS_du['dim_B']}, "
    f"P(B)=B*: {testS['P_of_B_equals_Bstar']}, "
    f"K_T dims {canS_pr['dim_KT']}/{canS_du['dim_KT']}, "
    f"P(K_T) in K_T*: {testS['P_of_KT_in_KTstar']}")

json.dump({
    "cell": "B662 CELL E (L102)",
    "verdict": verdict,
    "golden_control_pass": golden_control_pass,
    "silver_block_diagonal_canonical": silver_block,
    "runtime_s": time.time() - T0,
}, open(os.path.join(HERE, "cellE_verdict.json"), "w"), indent=2)
log("cellE_verdict.json saved.  DONE.")
