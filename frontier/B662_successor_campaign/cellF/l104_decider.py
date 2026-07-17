#!/usr/bin/env python3
# =====================================================================
# L104 — THE CP DECIDER: FORCED vs CONVENTION
# Question (B660/S2 honest partial): does there exist g in GL(5,K),
# K = Q(sqrt(-3)), with (Lambda^3 g) . Y = Ybar (the chord 3-form vs
# its Galois conjugate)?
#
# Exact arithmetic throughout: K elements are pairs (a,b) of Fractions
# meaning a + b*r, r = sqrt(-3)  (the banked source convention).
# Floats appear nowhere.
#
# Attack (in preregistered order):
#   1. CHEAP: the persisted wave-1 sigma matrix M (antilinear deck
#      swap sigma*: u -> M-combination of conj coords).  As a K-LINEAR
#      matrix, does +-M or +-M^T send Y to Ybar (or to a K-cube
#      scalar multiple of it)?
#   2. STABILIZER: dim_K of the Lie stabilizer of Y in gl(5,Kbar)
#      (K-linear system, so the Kbar-dimension = K-dimension).
#   3. CONSTRUCTIVE NORMAL FORM (replaces blind Groebner): a trivector
#      T on a 5-space whose flattening B(v,w) = T^v^w has rank 4
#      (= the banked GENERIC/OPEN type) satisfies T = v0 ^ S exactly,
#      v0 spanning ker B, S a nondegenerate 2-vector on the quotient;
#      Darboux over ANY field puts S into e1^e2 + e3^e4; hence the
#      generic type is a SINGLE GL(5,K)-orbit and an explicit g with
#      g.Y = Ybar is assembled from the two normal-form frames.
#   4. Exact verification of g, det g, and the descent datum
#      conj(g).g in Stab(Y).
# Mod-p evidence (prereg step 4) is superseded if an exact K-point is
# exhibited.
# =====================================================================
import json, itertools, sys
from fractions import Fraction as F

REPO = "/Users/dri/origin-axiom"
Y_JSON = REPO + "/frontier/B660_structure_campaign/packet/s2_cp/s2_results.json"
M_JSON = REPO + "/frontier/B662_successor_campaign/cellC/sigma_matrix_golden.json"

# ------------------------- K = Q(sqrt(-3)) ---------------------------
def k(a=0, b=0): return (F(a), F(b))
KZERO = k(); KONE = k(1)
def kadd(x, y): return (x[0] + y[0], x[1] + y[1])
def ksub(x, y): return (x[0] - y[0], x[1] - y[1])
def kmul(x, y): return (x[0]*y[0] - 3*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def kneg(x): return (-x[0], -x[1])
def kconj(x): return (x[0], -x[1])
def knorm(x): return x[0]*x[0] + 3*x[1]*x[1]
def kinv(x):
    n = knorm(x); assert n != 0, "division by zero in K"
    return (x[0] / n, -x[1] / n)
def kiszero(x): return x[0] == 0 and x[1] == 0
def kstr(x):
    if kiszero(x): return "0"
    if x[1] == 0: return str(x[0])
    if x[0] == 0: return f"{x[1]}r"
    return f"({x[0]} + {x[1]}r)"

# --------------------- matrices over K (dense) -----------------------
def meye(n): return [[KONE if i == j else KZERO for j in range(n)] for i in range(n)]
def mmulK(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[KZERO]*p for _ in range(n)]
    for i in range(n):
        for kk in range(m):
            a = A[i][kk]
            if kiszero(a): continue
            for j in range(p):
                if not kiszero(B[kk][j]):
                    C[i][j] = kadd(C[i][j], kmul(a, B[kk][j]))
    return C
def mtrans(A): return [list(r) for r in zip(*A)]
def mneg(A): return [[kneg(x) for x in r] for r in A]
def mconjK(A): return [[kconj(x) for x in r] for r in A]
def mscale(lam, A): return [[kmul(lam, x) for x in r] for r in A]

def rrefK(rows, ncols):
    """Row-reduce over K. Returns (rref_rows, pivot_cols)."""
    rows = [list(r) for r in rows]
    piv = []; r = 0
    for c in range(ncols):
        pr = None
        for rr in range(r, len(rows)):
            if not kiszero(rows[rr][c]): pr = rr; break
        if pr is None: continue
        rows[r], rows[pr] = rows[pr], rows[r]
        inv = kinv(rows[r][c])
        rows[r] = [kmul(inv, x) for x in rows[r]]
        for rr in range(len(rows)):
            if rr != r and not kiszero(rows[rr][c]):
                f_ = rows[rr][c]
                rows[rr] = [ksub(rows[rr][t], kmul(f_, rows[r][t])) for t in range(ncols)]
        piv.append(c); r += 1
        if r == len(rows): break
    return rows, piv

def nullspaceK(rows, ncols):
    R, piv = rrefK(rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [KZERO]*ncols
        v[fc] = KONE
        for ri, pc in enumerate(piv):
            v[pc] = kneg(R[ri][fc])
        basis.append(v)
    return basis

def minvK(A):
    n = len(A)
    aug = [list(A[i]) + list(meye(n)[i]) for i in range(n)]
    R, piv = rrefK(aug, 2*n)
    assert piv == list(range(n)), "matrix not invertible over K"
    return [R[i][n:] for i in range(n)]

def detK(A):
    n = len(A); A = [list(r) for r in A]
    det = KONE
    for c in range(n):
        pr = None
        for r in range(c, n):
            if not kiszero(A[r][c]): pr = r; break
        if pr is None: return KZERO
        if pr != c:
            A[c], A[pr] = A[pr], A[c]; det = kneg(det)
        det = kmul(det, A[c][c])
        inv = kinv(A[c][c])
        for r in range(c+1, n):
            if not kiszero(A[r][c]):
                f_ = kmul(A[r][c], inv)
                A[r] = [ksub(A[r][t], kmul(f_, A[c][t])) for t in range(n)]
    return det

# ------------------------- trivector tools ---------------------------
TRIPLES = list(itertools.combinations(range(5), 3))

def perm_sign(p):
    p = list(p); s = 1
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] > p[j]: s = -s
    return s

def full_tensor(Yc):
    """dict sorted-triple->K  ->  full antisymmetric 5x5x5 tensor."""
    T = [[[KZERO]*5 for _ in range(5)] for _ in range(5)]
    for (a, b, c), v in Yc.items():
        if kiszero(v): continue
        for p in itertools.permutations((a, b, c)):
            s = perm_sign(p)
            T[p[0]][p[1]][p[2]] = (v if s == 1 else kneg(v))
    return T

def act(g, Yc):
    """(Lambda^3 g).Y : out_{ijk} = sum_{abc ordered} g_{ia} g_{jb} g_{kc} Y_{abc}."""
    T = full_tensor(Yc)
    out = {}
    for (i, j, kk) in TRIPLES:
        s = KZERO
        for a in range(5):
            if kiszero_row(g[i]): pass
            ga = g[i][a]
            if kiszero(ga): continue
            for b in range(5):
                gb = g[j][b]
                if kiszero(gb): continue
                gab = kmul(ga, gb)
                for c in range(5):
                    y = T[a][b][c]
                    if kiszero(y): continue
                    gc = g[kk][c]
                    if kiszero(gc): continue
                    s = kadd(s, kmul(gab, kmul(gc, y)))
        out[(i, j, kk)] = s
    return out

def kiszero_row(r): return False  # placeholder (kept trivial)

def ybar(Yc): return {t: kconj(v) for t, v in Yc.items()}
def yneg(Yc): return {t: kneg(v) for t, v in Yc.items()}
def yeq(A, B): return all(A[t] == B[t] for t in TRIPLES)

def yscalar_ratio(A, B):
    """If A = lam*B for a single lam in K, return lam; else None."""
    lam = None
    for t in TRIPLES:
        a, b = A[t], B[t]
        if kiszero(b):
            if not kiszero(a): return None
            continue
        r = kmul(a, kinv(b))
        if lam is None: lam = r
        elif lam != r: return None
    return lam

def ystr(Yc):
    return "; ".join(f"{t}:{kstr(Yc[t])}" for t in TRIPLES if not kiszero(Yc[t])) or "0"

# ============================ load data ==============================
out_lines = []
def log(s=""):
    print(s); out_lines.append(str(s))

log("="*70)
log("L104 — THE CP DECIDER (cell F): does g in GL(5,K) with g.Y = Ybar exist?")
log("K = Q(sqrt(-3)); all arithmetic exact (Fraction pairs).")
log("="*70)

with open(Y_JSON) as f: s2 = json.load(f)
Y = {}
for kstr_, (a, b) in s2["Y_components"].items():
    t = tuple(int(x) for x in kstr_.strip("()").split(","))
    Y[t] = (F(a), F(b))
for t in TRIPLES: Y.setdefault(t, KZERO)
Yb = ybar(Y)

log("\n[load] Y (banked B660/S2 exact components):")
log("  " + ystr(Y))
log("[load] Ybar:")
log("  " + ystr(Yb))
log(f"[control] Y != Ybar: {not yeq(Y, Yb)} (must be True)")
assert not yeq(Y, Yb)

with open(M_JSON) as f: sig = json.load(f)
M = [[(F(a), F(b)) for (a, b) in row] for row in sig["matrix"]]
log("\n[load] sigma matrix M (wave-1, antilinear deck swap; row i = coeffs of sigma*(rep_i)):")
for r in M: log("  [" + ", ".join(kstr(x) for x in r) + "]")
CMM = mmulK(mconjK(M), M)
log(f"[control] conj(M).M == I (banked law): {CMM == meye(5)}")

# ========== STEP 1: the cheap sigma-matrix facts =====================
log("\n" + "="*70)
log("STEP 1 — what the deck swap's LINEAR matrix part does to Y (exact)")
log("="*70)
candidates = {
    "M":    M,
    "M^T":  mtrans(M),
    "-M":   mneg(M),
    "-M^T": mneg(mtrans(M)),
}
targets = {"Y": Y, "-Y": yneg(Y), "Ybar": Yb, "-Ybar": yneg(Yb)}
step1_g = None
for name, g in candidates.items():
    gY = act(g, Y)
    hit = [tn for tn, tv in targets.items() if yeq(gY, tv)]
    if hit:
        log(f"  act({name}, Y) = {hit[0]}   <-- EXACT")
        if hit[0] == "Ybar" and step1_g is None:
            step1_g = (name, g)
    else:
        # scalar multiple of Ybar?
        lam = yscalar_ratio(gY, Yb)
        lam2 = yscalar_ratio(gY, Y)
        if lam is not None:
            log(f"  act({name}, Y) = lam * Ybar with lam = {kstr(lam)}")
            log(f"    -> need mu in K with mu^3 = lam^(-1); cube roots of unity ARE in K (omega),")
            log(f"       so solvable iff lam is a cube in K.")
        elif lam2 is not None:
            log(f"  act({name}, Y) = lam * Y with lam = {kstr(lam2)} (stays on the Y side)")
        else:
            log(f"  act({name}, Y) = neither +-Y, +-Ybar, nor a K-scalar multiple of either")
            log(f"    components: {ystr(gY)}")
log("""
[reading] The banked B660 statement 'the deck swap gives -Y not Ybar' is the
ANTILINEAR statement (sigma* = M o conj as a map).  The K-linear matrix part
alone is a different animal — tested above.""")

# ========== STEP 2: the Lie stabilizer of Y ==========================
log("="*70)
log("STEP 2 — Lie stabilizer of Y in gl(5): X.Y = 0, X in 25 K-unknowns")
log("="*70)
Tfull = full_tensor(Y)
rows = []
for (i, j, kk) in TRIPLES:
    row = [KZERO]*25          # unknown X_{pq} at index 5p+q
    for a in range(5):
        # X_{ia} Y_{ajk} + X_{ja} Y_{iak} + X_{ka} Y_{ija}
        row[5*i + a] = kadd(row[5*i + a], Tfull[a][j][kk])
        row[5*j + a] = kadd(row[5*j + a], Tfull[i][a][kk])
        row[5*kk + a] = kadd(row[5*kk + a], Tfull[i][j][a])
    rows.append(row)
ns = nullspaceK(rows, 25)
dim_stab = len(ns)
log(f"  dim_K stab(Y) = {dim_stab}   (25 - rank of the 10x25 system)")
log(f"  orbit dimension = {25 - dim_stab} (open orbit in Lambda^3 K^5 <=> 10)")
log("  [structure] for the generic (rank-4 flattening) type the stabilizer is")
log("  the parabolic-type group {g : g v0 = a v0, induced gbar in GSp4(Bbar),")
log("  a = similitude^{-1}} = U(4-dim unipotent) x| GSp4  -> dim 4 + 11 = 15.")

# ========== STEP 3: constructive normal form over K ==================
log("="*70)
log("STEP 3 — constructive normal form over K (the decisive step)")
log("="*70)
log("""Theory (exact, all verified below in-sandbox):
  (i)   B(v,w) := T^v^w (5x5 skew flattening).  Banked type => rank B = 4,
        ker B = <v0>, a K-line.
  (ii)  In any basis (v0, w1..w4): T = v0 ^ S + T', T' in Lambda^3<w>;
        v0 in ker B forces  0 = T ^ v0 = v0 ^ T'  => T' = 0.  So T = v0 ^ S.
  (iii) S is a nondegenerate 2-vector on the 4-dim quotient; Darboux holds
        over ANY field: exists Q in GL(4,K), Q S Q^T = e1^e2 + e3^e4.
  (iv)  Hence EVERY trivector of the generic type is GL(5,K)-equivalent to
        N = e0^(e1^e2 + e3^e4): the generic type is ONE K-orbit; Y ~ Ybar.""")

def flattenB(Yc):
    """B_{ij} = coefficient of e_{01234} in T ^ e_i ^ e_j."""
    B = [[KZERO]*5 for _ in range(5)]
    for (a, b, c), v in Yc.items():
        if kiszero(v): continue
        for i in range(5):
            for j in range(5):
                if len({a, b, c, i, j}) == 5:
                    s = perm_sign((a, b, c, i, j))
                    B[i][j] = kadd(B[i][j], v if s == 1 else kneg(v))
    return B

def symplectic_frame(S4):
    """Given nondeg skew 4x4 S over K, return C (cols u1,v1,u2,v2) with
       C^T S C = J,  J = e12 + e34 pattern (J[0][1]=1=J[2][3], skew)."""
    def formS(u, v):
        s = KZERO
        for i in range(4):
            if kiszero(u[i]): continue
            for j in range(4):
                if not kiszero(S4[i][j]) and not kiszero(v[j]):
                    s = kadd(s, kmul(u[i], kmul(S4[i][j], v[j])))
        return s
    # work with an explicit basis of the current symplectic complement
    basis = [[KONE if i == j else KZERO for j in range(4)] for i in range(4)]
    cols = []
    while basis:
        u = basis[0]
        v = None
        for cand in basis[1:]:
            if not kiszero(formS(u, cand)): v = cand; break
        assert v is not None, "degenerate S — contradicts banked type"
        c = kinv(formS(u, v))
        v = [kmul(c, x) for x in v]           # S(u,v) = 1
        cols.append(u); cols.append(v)
        # complement: w -> w - S(w,v) u + S(w,u) v   (then S(u,.)=S(v,.)=0)
        newbasis = []
        for w in basis:
            a1 = formS(w, v); a2 = formS(w, u)
            w2 = [kadd(ksub(w[t], kmul(a1, u[t])), kmul(a2, v[t])) for t in range(4)]
            if any(not kiszero(x) for x in w2):
                newbasis.append(w2)
        # keep an independent set
        rowsw = [list(w) for w in newbasis]
        R, piv = rrefK(rowsw, 4)
        basis = [R[t] for t in range(len(piv))]
    C = [[cols[j][i] for j in range(4)] for i in range(4)]   # columns = cols
    return C

def normalize(Yc, tag):
    """Return u in GL(5,K) with act(u, Yc) = N = e0^(e12+e34). Exact."""
    B = flattenB(Yc)
    ker = nullspaceK(B, 5)
    log(f"  [{tag}] rank(B) = {5 - len(ker)}, ker dim = {len(ker)} (need 1)")
    assert len(ker) == 1
    v0 = ker[0]
    log(f"  [{tag}] v0 = ({', '.join(kstr(x) for x in v0)})")
    # basis P: columns = v0 then 4 standard vectors keeping P invertible
    for drop in range(5):
        cols = [v0] + [[KONE if i == e else KZERO for i in range(5)]
                       for e in range(5) if e != drop]
        P = [[cols[j][i] for j in range(5)] for i in range(5)]
        if not kiszero(detK(P)): break
    Pinv = minvK(P)
    Yp = act(Pinv, Yc)
    # exactness check of the decomposition T = f0 ^ S:
    resid = [t for t in TRIPLES if 0 not in t and not kiszero(Yp[t])]
    log(f"  [{tag}] decomposition check: Y'_(ijk)=0 for all i,j,k>=1: {not resid}")
    assert not resid, "T != v0^S — contradicts step-(ii) theorem"
    S4 = [[KZERO]*4 for _ in range(4)]
    for j in range(1, 5):
        for kk_ in range(1, 5):
            if j < kk_:
                v = Yp[(0, j, kk_)]
                S4[j-1][kk_-1] = v; S4[kk_-1][j-1] = kneg(v)
    dS = detK(S4)
    log(f"  [{tag}] det(S) = {kstr(dS)} (nondegenerate: {not kiszero(dS)})")
    C = symplectic_frame(S4)
    Q = mtrans(C)
    # J check
    J = mmulK(mtrans(C), mmulK(S4, C))
    Jstd = [[KZERO]*4 for _ in range(4)]
    Jstd[0][1] = KONE; Jstd[1][0] = kneg(KONE)
    Jstd[2][3] = KONE; Jstd[3][2] = kneg(KONE)
    assert J == Jstd, "Darboux frame failed"
    R = meye(5)
    for i in range(4):
        for j in range(4):
            R[1+i][1+j] = Q[i][j]
    u = mmulK(R, Pinv)
    Nu = act(u, Yc)
    Ntarget = {t: KZERO for t in TRIPLES}
    Ntarget[(0, 1, 2)] = KONE; Ntarget[(0, 3, 4)] = KONE
    assert yeq(Nu, Ntarget), "normal form not reached"
    log(f"  [{tag}] act(u, Y_{tag}) = N = e0^e1^e2 + e0^e3^e4   EXACT")
    return u

u1 = normalize(Y, "Y")
u2 = normalize(Yb, "Ybar")
g = mmulK(minvK(u2), u1)

log("\n  g := u2^{-1} u1  (entries in K, exact):")
for r in g: log("   [" + ", ".join(kstr(x) for x in r) + "]")

# ========== STEP 4: verification =====================================
log("="*70)
log("STEP 4 — exact verification of the certificate")
log("="*70)
gY = act(g, Y)
ok = yeq(gY, Yb)
log(f"  (Lambda^3 g).Y == Ybar, all 10 components exactly: {ok}")
assert ok
dg = detK(g)
log(f"  det g = {kstr(dg)}  (nonzero: {not kiszero(dg)}; g in GL(5,K))")
# descent datum: conj(g).g must stabilize Y (and does, formally); verify
h = mmulK(mconjK(g), g)
hY = act(h, Y)
log(f"  conj(g).g stabilizes Y (descent-datum candidate): {yeq(hY, Y)}")
log(f"  conj(g).g == I (would make u -> g.conj(u) an antilinear involution): {h == meye(5)}")
# cube roots of unity in K: the full scalar freedom on g
log("  scalar freedom: g, omega*g, omega^2*g all work (omega = (-1+r)/2 in K, omega^3=1);")
log("  full solution set = Stab_GL5(Y) . g, a 15-dimensional K-variety coset.")

if step1_g is not None:
    log(f"\n  NOTE: step 1 already produced a solution from the sigma matrix: {step1_g[0]}")

log("\n" + "="*70)
log("VERDICT: CONVENTION — an explicit g in GL(5,K) with (Lambda^3 g).Y = Ybar")
log("has been exhibited and verified exactly.  Moreover the constructive proof")
log("shows the generic trivector type is a SINGLE GL(5,K)-orbit (no arithmetic")
log("invariant survives over K): the Y vs Ybar asymmetry is a basis convention,")
log("not a forced (CP-like) distinction.  The B660 X^3 = c obstructions were")
log("artifacts of the monomial/diagonal ansatz — the general group absorbs the")
log("cube through the kernel-line scaling, no cube root ever needed.")
log("="*70)
log("prereg step 4 (mod-p evidence): SUPERSEDED — an exact K-point is exhibited;")
log("evidence gathering is moot.")

with open(REPO + "/frontier/B662_successor_campaign/cellF/cellF_output.txt", "w") as f:
    f.write("\n".join(out_lines) + "\n")

# persist the certificate
cert = {
    "claim": "(Lambda^3 g).Y = Ybar with g in GL(5,K), K = Q(sqrt(-3))",
    "convention": "(g.Y)_{ijk} = sum_{a,b,c ordered} g_{ia} g_{jb} g_{kc} Y_{abc}; entry [a,b] = a + b*sqrt(-3)",
    "Y_source": "frontier/B660_structure_campaign/packet/s2_cp/s2_results.json",
    "g": [[[str(x[0]), str(x[1])] for x in row] for row in g],
    "det_g": [str(dg[0]), str(dg[1])],
    "verified_exactly": True,
    "conj_g_times_g_stabilizes_Y": True,
    "stabilizer_dim_K": dim_stab,
    "verdict": "CONVENTION",
}
with open(REPO + "/frontier/B662_successor_campaign/cellF/g_certificate.json", "w") as f:
    json.dump(cert, f, indent=1)
log("certificate written: cellF/g_certificate.json")
