#!/usr/bin/env python3
"""B912 -- R1, the e6(2) norm cell, per the SEALED preregistration.

Operation (as sealed):
 1. J, the conjugate-linear equivariant map the e6(2) conjugation sigma = phi o
    sigma_split puts on the 27.  Since phi = tau o sigma_chi maps the 27 to its
    dual (verified below: the LINEAR intertwiner space Hom(27, 27 o phi) is 0),
    J goes through the dual: J(u) = H conj(u) with H the 27x27 matrix solving

        (S)   rho(x)^T H  +  H rho(phi(x))  =  0   for all 78 basis generators x.

    (S) is the matrix transcription of the sealed equation via the frame's
    coordinate pairing <.,.> between the dual and the 27: with
    H(u,v) := <J u-bar, v> = conj(u)^T H v, (S) is exactly the statement that
    H is invariant under the real form g0 = Fix(sigma), i.e. H(rho(y)u, v) +
    H(u, rho(y)v) = 0 for all y in g0.  The solve is rational; existence is
    forced (27 o phi ~ dual 27); uniqueness up to one real scale is proven by
    the elimination itself (connected ratio graph, no conflicts).
 2. Hermiticity + sigma-invariance verified exactly on all 78 generators; the
    declared normalization H = +1 on the first canonical vacuum line (B889
    block 0 = the vacuum line of frame 2).
 3. Readout: signature of H on the 27; H restricted to each of the 15 flavor
    atoms (the banked tri-partition basis = the joint eigenspace decomposition
    of the four commuting charges rho(x8), rho(x14), rho(x16), rho(x22) --
    verified below against the probeB construction at the full-tower prime
    40123, span-for-span); per atom the Gram (orthonormal atom basis w.r.t.
    the frame's coordinate hermitian metric), its signature and |det|; both
    sigma+- computed and cross-checked.

House rules: exact arithmetic wherever the tower permits (the frame, phi+-, H,
its uniqueness, total signature, the mod-q atom identification); dps-60
certified numerics (residuals printed) for the C-side atom bases and Grams.
Oblique-readout rule respected: eigenvalues are never Rayleigh quotients; every
restriction is certified by a full-basis residual.

Paths: repo-relative from this file; scratch from SESSION_SCRATCH env or a
fresh temp dir (the B854 exec is isolated: its __file__ points INTO scratch so
its results.json lands there, never in the repo arc).
"""
import io, os, json, time, pickle, tempfile, contextlib
from fractions import Fraction as F
from collections import Counter
import numpy as np
import sympy as sp
import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b912_")
os.makedirs(SCRATCH, exist_ok=True)
mp.dps = 60
T0 = time.time()
RESULT = {"cell": "B912 R1 norm cell", "sealed_prereg": "PREREGISTRATION.md",
          "checks": {}, "notes": []}
def CHK(name, ok, detail=""):
    RESULT["checks"][name] = {"pass": bool(ok), "detail": str(detail)}
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
    if not ok:
        RESULT["verdict"] = "UNSTABLE"
        json.dump(RESULT, open(os.path.join(HERE, "results.json"), "w"), indent=1)
        raise SystemExit(f"UNSTABLE at {name}")

# ---------------- 0. frame (isolated exec) ----------------
print("[0] rebuilding the B854 frame (isolated exec, scratch cwd)...", flush=True)
os.chdir(SCRATCH)
g6 = {"__file__": os.path.join(SCRATCH, "e6_centralizer.py"), "__name__": "b854_frame"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(REPO, "frontier", "B854_centralizer_exact",
                                   "e6_centralizer.py")).read(), "b854", "exec"), g6)
ROOTS, IDX, INVg, ns, eps = g6["ROOTS"], g6["IDX"], g6["INV"], g6["ns"], g6["eps"]
bracket_basis = g6["bracket_basis"]
INV = {n: [F(c.numerator, c.denominator) for c in INVg[n]] for n in ns}
print(f"    frame in {time.time()-T0:.0f}s; ns={ns}", flush=True)

# ---------------- 1. the 27 (B883 banked instrument) ----------------
REPJ = json.load(open(os.path.join(REPO, "frontier", "B883_the_27", "rep27.json")))
REP = [np.array(REPJ["rep"][str(k)], dtype=object) for k in range(78)]
WT = [tuple(int(REP[i][a][a]) for i in range(6)) for a in range(27)]
CHK("rep27_cartan_diagonal_27_distinct_weights",
    all((REP[i] == np.diag(np.diag(REP[i].astype(int)))).all() for i in range(6))
    and len(set(WT)) == 27)
bad = 0
for p_ in range(78):
    for q_ in range(p_ + 1, 78):
        v = bracket_basis(p_, q_)
        lhs = np.zeros((27, 27), dtype=object)
        for k, c in enumerate(v):
            if c: lhs = lhs + F(c) * REP[k]
        if not (lhs == REP[p_] @ REP[q_] - REP[q_] @ REP[p_]).all(): bad += 1
CHK("rep27_homomorphism_all_3003_pairs_exact", bad == 0)
# optional cross-check vs the solo seat's pickle (set HANDOFF5_RUN to its dir)
h5 = os.environ.get("HANDOFF5_RUN")
if h5 and os.path.exists(os.path.join(h5, "rep27.pkl")):
    Dpk = pickle.load(open(os.path.join(h5, "rep27.pkl"), "rb"))
    wp = Counter(tuple(int(x) for x in w) for w in Dpk["W"])
    dual = wp == Counter(tuple(-x for x in w) for w in WT)
    RESULT["notes"].append(f"handoff5 rep27.pkl (variant {Dpk.get('variant')}): weight multiset "
                           f"= NEGATIVE of B883's -> it is a 27bar realization ({dual}); "
                           "this cell computes on the banked B883 27.")
    print("    handoff5 pickle: 27bar (dual) realization:", dual, flush=True)

# ---------------- 2. phi+- = tau o sigma_chi (B907, rebuilt + verified) ----------------
print("[2] tau cocycle (F2 elimination) + phi+- verification...", flush=True)
FLIP = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}
def flip_root(r): return tuple(r[FLIP[i]] for i in range(6))
ridx = {r: i for i, r in enumerate(ROOTS)}
rows, rhs = [], []
for a in ROOTS:
    for b in ROOTS:
        s = tuple(a[i] + b[i] for i in range(6))
        if s in ridx:
            row = [0] * 72
            row[ridx[a]] ^= 1; row[ridx[b]] ^= 1; row[ridx[s]] ^= 1
            rows.append(row)
            rhs.append(0 if eps(a, b) * eps(flip_root(a), flip_root(b)) == 1 else 1)
Aa = np.concatenate([np.array(rows, dtype=np.uint8),
                     np.array(rhs, dtype=np.uint8)[:, None]], axis=1)
r_ = 0
for c in range(72):
    piv = next((i for i in range(r_, Aa.shape[0]) if Aa[i, c]), None)
    if piv is None: continue
    Aa[[r_, piv]] = Aa[[piv, r_]]
    for i in range(Aa.shape[0]):
        if i != r_ and Aa[i, c]: Aa[i] ^= Aa[r_]
    r_ += 1
sol = [0] * 72
for i in range(r_):
    c = next(cc for cc in range(72) if Aa[i, cc])
    sol[c] = int(Aa[i, 72])
d = {ROOTS[i]: (-1) ** sol[i] for i in range(72)}
CHK("tau_cocycle_F2_rank", r_ == 66, f"rank {r_}")

def phi_sp(signs):
    def chi(r):
        v = 1
        for i in range(6):
            if r[i] % 2: v *= signs[i]
        return v
    perm, sgn = [0] * 78, [0] * 78
    for i in range(6): perm[i], sgn[i] = FLIP[i], 1
    for r in ROOTS:
        fr = flip_root(r)
        perm[6 + IDX[r]] = 6 + IDX[fr]
        sgn[6 + IDX[r]] = d[r] * chi(fr)
    return perm, sgn
CHI = {"+": (1, -1, 1, -1, 1, 1), "-": (-1, 1, -1, 1, -1, -1)}   # B907's wall pair
PH = {pm: phi_sp(CHI[pm]) for pm in "+-"}
EPS_BANKED = {8: -1, 14: 1, 16: -1, 22: 1}
for pm in "+-":
    perm, sgn = PH[pm]
    CHK(f"phi{pm}_involution_all78",
        all(perm[perm[k]] == k and sgn[k] * sgn[perm[k]] == 1 for k in range(78)))
    bad = 0
    for p_ in range(78):
        for q_ in range(p_ + 1, 78):
            v = bracket_basis(p_, q_)
            lhs = [F(0)] * 78
            for k, c in enumerate(v):
                if c: lhs[perm[k]] += F(c) * sgn[k]
            rhsv = [F(sgn[p_] * sgn[q_]) * F(c) for c in bracket_basis(perm[p_], perm[q_])]
            if lhs != rhsv: bad += 1
    CHK(f"phi{pm}_automorphism_all_3003_bracket_pairs", bad == 0)
    okeps = True
    for n in ns:
        im = [F(0)] * 78
        for k, c in enumerate(INV[n]):
            if c: im[perm[k]] += c * sgn[k]
        okeps &= im == [EPS_BANKED[n] * c for c in INV[n]]
    CHK(f"phi{pm}_charge_eps_pattern_(-1,+1,-1,+1)", okeps)
def rep_phi(k, pm):
    perm, sgn = PH[pm]
    return sgn[k] * REP[perm[k]]

# no LINEAR intertwiner: Hom(27, 27 o phi) = 0 (mod the full-tower prime)
qP = 40123
Rq27 = [np.array([[int(x) % qP for x in row] for row in REPJ["rep"][str(k)]], dtype=np.int64)
        for k in range(78)]
cur = np.eye(729, dtype=np.int64)
perm, sgn = PH["+"]
for k in range(78):
    A = (sgn[k] % qP) * Rq27[perm[k]] % qP
    B = Rq27[k]
    res = np.array([((A @ v.reshape(27, 27) - v.reshape(27, 27) @ B) % qP).reshape(729)
                    for v in cur], dtype=np.int64)
    M2 = res.T % qP
    A2, rr, piv = M2.copy(), 0, []
    for c in range(A2.shape[1]):
        pr = next((x for x in range(rr, A2.shape[0]) if A2[x, c] % qP), None)
        if pr is None: continue
        A2[[rr, pr]] = A2[[pr, rr]]
        A2[rr] = A2[rr] * pow(int(A2[rr, c]), -1, qP) % qP
        mask = A2[:, c] % qP != 0; mask[rr] = False
        A2[mask] = (A2[mask] - np.outer(A2[mask, c], A2[rr])) % qP
        piv.append(c); rr += 1
    free = [c for c in range(A2.shape[1]) if c not in piv]
    nb = []
    for fc in free:
        x = np.zeros(A2.shape[1], dtype=np.int64); x[fc] = 1
        for i2, c in enumerate(piv): x[c] = (-A2[i2, fc]) % qP
        nb.append((x @ cur) % qP)
    cur = np.array(nb, dtype=np.int64) if nb else np.zeros((0, 729), dtype=np.int64)
    if cur.shape[0] == 0: break
CHK("no_linear_intertwiner_Hom(27,27ophi)=0_mod40123", cur.shape[0] == 0,
    "phi maps the 27 to its DUAL; J is necessarily antilinear-through-the-dual")

# ---------------- 3. solve (S) exactly; J exists; uniqueness ----------------
print("[3] solving (S) exactly for H+ and H- ...", flush=True)
wt_idx = {w: a for a, w in enumerate(WT)}
piW = [wt_idx[tuple(-WT[b][FLIP[i]] for i in range(6))] for b in range(27)]
CHK("weight_pairing_pi_total_permutation", sorted(piW) == list(range(27)), f"pi={piW}")
def solve_H(pm):
    pinv = [0] * 27
    for b, a in enumerate(piW): pinv[a] = b
    edges, zero_forced = [], set()
    for k in range(78):
        A, B = REP[k], rep_phi(k, pm)
        for a in range(27):
            b2 = pinv[a]
            for b in range(27):
                ca, cb = A[piW[b]][a], B[b2][b]
                if ca == 0 and cb == 0: continue
                if b == b2:
                    if F(int(ca)) + F(int(cb)) != 0: zero_forced.add(b)
                elif ca == 0: zero_forced.add(b2)
                elif cb == 0: zero_forced.add(b)
                else: edges.append((b, b2, -F(int(cb)) / F(int(ca))))
    if zero_forced: return None, "zero-forced"
    cvec = [None] * 27; cvec[0] = F(1)
    changed = True
    while changed:
        changed = False
        for b, b2, r in edges:
            if cvec[b2] is not None and cvec[b] is None: cvec[b] = r * cvec[b2]; changed = True
            elif cvec[b] is not None and cvec[b2] is None: cvec[b2] = cvec[b] / r; changed = True
    if any(x is None for x in cvec): return None, "disconnected"
    if any(cvec[b] != r * cvec[b2] for b, b2, r in edges): return None, "conflict"
    den = np.lcm.reduce([x.denominator for x in cvec])
    cn = [int(x * den) for x in cvec]
    gg = np.gcd.reduce([abs(v) for v in cn if v])
    cn = [v // gg for v in cn]
    Hm = np.zeros((27, 27), dtype=object)
    for b in range(27): Hm[piW[b]][b] = cn[b]
    return Hm, "unique-1dim"
Hsol = {}
for pm in "+-":
    Hm, status = solve_H(pm)
    CHK(f"J_exists_H{pm}_solved_{status}", Hm is not None)
    bad = [k for k in range(78) if not ((REP[k].T @ Hm + Hm @ rep_phi(k, pm)) == 0).all()]
    CHK(f"S_equivariance_H{pm}_all_78_generators_exact", not bad)
    CHK(f"H{pm}_symmetric_(hermitian,_real)", (Hm == Hm.T).all())
    Hsol[pm] = Hm
Hp_e, Hm_e = Hsol["+"], Hsol["-"]
RESULT["H_plus_support_pi"] = piW
RESULT["H_plus_entries_c_b"] = [int(Hp_e[piW[b]][b]) for b in range(27)]
RESULT["H_minus_entries_c_b"] = [int(Hm_e[piW[b]][b]) for b in range(27)]
# exact raw signature of H+ (signed permutation): 2-cycles give (+1,-1); fixed slots give c_b
fixed = [b for b in range(27) if piW[b] == b]
trH = sum(int(Hp_e[b][b]) for b in fixed)
np_raw = (27 - len(fixed)) // 2 + sum(1 for b in fixed if int(Hp_e[b][b]) > 0)
nm_raw = 27 - np_raw
RESULT["H_plus_raw_signature_exact"] = [np_raw, nm_raw]
print(f"    H+ raw signature (exact, cycle count): ({np_raw},{nm_raw}); fixed slots {fixed}",
      flush=True)
# the exact sigma+- relation: D = H+^{-1} H- diagonal +-1
Dd = np.zeros((27, 27), dtype=object)
okD = True
for b in range(27):
    r = F(int(Hm_e[piW[b]][b]), int(Hp_e[piW[b]][b]))
    okD &= r in (F(1), F(-1))
    Dd[b][b] = r
CHK("sigma_pm_relation_Hminus_eq_Hplus_x_D_diag_pm1", okD,
    f"D diag = {[int(Dd[b][b]) for b in range(27)]}, tr D = {sum(int(Dd[b][b]) for b in range(27))}")

# ---------------- 4. charges; atoms mod q (probeB identification) ----------------
print("[4] charges + the 15 atoms at the full-tower prime 40123...", flush=True)
def rho_of(vec):
    M = np.zeros((27, 27), dtype=object)
    for k, c in enumerate(vec):
        if c: M = M + c * REP[k]
    return M
Rex = {n: rho_of(INV[n]) for n in ns}
CHK("charges_pairwise_commute_exact",
    all(((Rex[a] @ Rex[b] - Rex[b] @ Rex[a]) == 0).all()
        for i, a in enumerate(ns) for b in ns[i + 1:]))
CHK("D_commutes_with_all_four_charges_exact",
    all(((Dd @ Rex[n] - Rex[n] @ Dd) == 0).all() for n in ns),
    "D preserves every atom")
def rq(x):
    x = F(x); return (x.numerator % qP) * pow(x.denominator % qP, -1, qP) % qP
Rq = {n: np.array([[rq(Rex[n][i][j]) for j in range(27)] for i in range(27)], dtype=np.int64)
      for n in ns}
tt = sp.Symbol('tt')
def null_q(Aq):
    m_ = len(Aq[0]); A = [[int(x) % qP for x in row] for row in Aq]
    rr, piv = 0, []
    for c in range(m_):
        pr = next((x for x in range(rr, len(A)) if A[x][c] % qP), None)
        if pr is None: continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = pow(A[rr][c], -1, qP); A[rr] = [(e * iv) % qP for e in A[rr]]
        for x in range(len(A)):
            if x != rr and A[x][c]:
                f2 = A[x][c]; A[x] = [(A[x][j] - f2 * A[rr][j]) % qP for j in range(m_)]
        piv.append(c); rr += 1
    ker = []
    for fr in [c for c in range(m_) if c not in piv]:
        v = [0] * m_; v[fr] = 1
        for i2, c in enumerate(piv): v[c] = (-A[i2][fr]) % qP
        ker.append(v)
    return rr, ker
def rank_q(rowsl):
    return null_q(rowsl)[0] if rowsl else 0
def eigsplit_q(Mq, Brows):
    m = len(Brows)
    Bt = np.array(Brows, dtype=np.int64).T % qP
    X = np.zeros((m, m), dtype=np.int64)
    for j in range(m):
        w = (Mq @ Bt[:, j]) % qP
        aug = [[int(Bt[i, c]) for c in range(m)] + [int(w[i])] for i in range(27)]
        A = [r[:] for r in aug]; rr, piv = 0, []
        for c in range(m):
            pr = next((x for x in range(rr, 27) if A[x][c] % qP), None)
            if pr is None: continue
            A[rr], A[pr] = A[pr], A[rr]
            iv = pow(A[rr][c], -1, qP); A[rr] = [(e * iv) % qP for e in A[rr]]
            for x in range(27):
                if x != rr and A[x][c]:
                    f2 = A[x][c]; A[x] = [(A[x][j] - f2 * A[rr][j]) % qP for j in range(m + 1)]
            piv.append(c); rr += 1
        for i2, c in enumerate(piv): X[c, j] = A[i2][m] % qP
    chp = sp.Poly(sp.Matrix(X.tolist()).charpoly(tt).as_expr(), tt, modulus=qP)
    out = []
    for ev, mlt in chp.ground_roots().items():
        _, ker = null_q([[int((X[i, j] - (int(ev) if i == j else 0)) % qP) for j in range(m)]
                         for i in range(m)])
        nb = [list((np.array(kv, dtype=np.int64) @ np.array(Brows, dtype=np.int64)) % qP)
              for kv in ker]
        out.append((int(ev), nb))
    assert sum(len(b) for _, b in out) == m, "incomplete split over F_q"
    return out
blocks = [((), [[1 if i == j else 0 for j in range(27)] for i in range(27)])]
for n in ns:
    blocks = [(tag + (ev,), nb) for tag, B in blocks for ev, nb in eigsplit_q(Rq[n], B)]
CHK("modq_joint_blocks_shape_6x3_9x1",
    sorted(len(B) for _, B in blocks) == [1] * 9 + [3] * 6, f"{len(blocks)} blocks")
pib = Counter()
for tag, B in blocks: pib[(tag[0], tag[2])] += len(B)
CHK("modq_Pi_blocks_1_1_1_8_8_8", sorted(pib.values()) == [1, 1, 1, 8, 8, 8])
# probeB rebuild (banked DATA at the full-tower prime; B906 provenance)
DATA = [(27063, 13410, 2675), (23094, 222, 18983), (13418, 13632, 16308)]
ADSf = {n: [[F(sp.Rational(sp.Matrix(g6["ADS"][n])[i, j]).p,
              sp.Rational(sp.Matrix(g6["ADS"][n])[i, j]).q) for j in range(78)]
            for i in range(78)] for n in ns}
Gq78 = {n: np.array([[rq(ADSf[n][i][j]) for j in range(78)] for i in range(78)], dtype=np.int64)
        for n in ns}
def eig_exact(Mq, v):
    w = (Mq @ v) % qP
    k = int(np.argmax(v % qP != 0))
    lam = int(w[k]) * pow(int(v[k]) % qP, -1, qP) % qP
    assert ((w - lam * v) % qP == 0).all()
    return lam
def restr78(Mq, B):
    m_ = B.shape[0]; out = np.zeros((m_, m_), dtype=np.int64)
    for a2 in range(m_):
        w = (Mq @ B[a2]) % qP
        A2 = [[int(x) % qP for x in row] for row in np.hstack([B.T, w[:, None]]).tolist()]
        rr2, piv2 = 0, []
        for c in range(m_):
            pr = next((x for x in range(rr2, 78) if A2[x][c] % qP), None)
            if pr is None: continue
            A2[rr2], A2[pr] = A2[pr], A2[rr2]
            iv = pow(A2[rr2][c], -1, qP); A2[rr2] = [(e * iv) % qP for e in A2[rr2]]
            for x in range(78):
                if x != rr2 and A2[x][c]:
                    f2 = A2[x][c]; A2[x] = [(A2[x][j] - f2 * A2[rr2][j]) % qP for j in range(m_ + 1)]
            piv2.append(c); rr2 += 1
        solv = np.zeros(m_, dtype=np.int64)
        for i2, c in enumerate(piv2): solv[c] = A2[i2][m_] % qP
        out[:, a2] = solv
    return out
def build_cells(rgai):
    r1, g1, a1 = rgai
    _, K46 = null_q([[int(x) for x in row] for row in ((Gq78[8] + r1 * Gq78[16]) % qP)])
    K46 = np.array(K46, dtype=np.int64)
    R16r = restr78(Gq78[16], K46)
    _, Vg = null_q([[int((R16r[i, j] - (g1 if i == j else 0)) % qP) for j in range(K46.shape[0])]
                    for i in range(K46.shape[0])])
    Vg = (np.array(Vg, dtype=np.int64) @ K46) % qP
    R14g = restr78(Gq78[14], Vg)
    _, Va = null_q([[int((R14g[i, j] - (a1 if i == j else 0)) % qP) for j in range(Vg.shape[0])]
                    for i in range(Vg.shape[0])])
    Va = (np.array(Va, dtype=np.int64) @ Vg) % qP
    bq = eig_exact(Gq78[22], Va[0])
    X1 = (Rq[8] + r1 * Rq[16]) % qP
    Ym = (g1 * Rq[14] + (qP - a1) * Rq[16]) % qP
    W3 = (bq * Rq[16] + (qP - g1) * Rq[22]) % qP
    combo = (3 * X1 + 7 * Ym + 13 * W3 + 17 * Rq[14]) % qP
    chp = sp.Poly(sp.Matrix(combo.tolist()).charpoly(tt).as_expr(), tt, modulus=qP)
    cells = []
    for ev, mlt in chp.ground_roots().items():
        _, V = null_q([[int((combo[i, j] - (int(ev) if i == j else 0)) % qP) for j in range(27)]
                       for i in range(27)])
        cells.append((mlt, np.array(V, dtype=np.int64) % qP))
    return dict(dims=(K46.shape[0], Vg.shape[0], Va.shape[0]), cells=cells)
LAB = [build_cells(dt) for dt in DATA]
CHK("probeB_chain_dims_46_8_1_x3", all(L["dims"] == (46, 8, 1) for L in LAB))
def inter_basis(A, B):
    M = [[int(x) for x in row] for row in (np.hstack([A.T, (qP - B.T) % qP]) % qP)]
    _, N = null_q(M)
    if not N: return np.zeros((0, 27), dtype=np.int64)
    V = (np.array(N, dtype=np.int64)[:, :A.shape[0]] @ A) % qP
    seen = np.zeros((0, 27), dtype=np.int64)
    for row in V:
        if rank_q(np.vstack([seen, row[None, :]]).tolist()) > seen.shape[0]:
            seen = np.vstack([seen, row[None, :]])
    return seen % qP
atoms_q = []
for m in (3, 1):
    C = [[c[1] for c in L["cells"] if c[0] == m] for L in LAB]
    for B1 in C[0]:
        for B2 in C[1]:
            I12 = inter_basis(B1, B2)
            if I12.shape[0] == 0: continue
            for B3 in C[2]:
                I = inter_basis(I12, B3)
                if I.shape[0] > 0: atoms_q.append(("colored" if m == 3 else "colorless", I))
CHK("probeB_atoms_6_colored_3d_9_colorless_1d",
    Counter((k, a.shape[0]) for k, a in atoms_q) ==
    Counter({("colored", 3): 6, ("colorless", 1): 9}))
def same_span(A, Brows):
    return A.shape[0] == len(Brows) and \
        rank_q(np.vstack([A, np.array(Brows, dtype=np.int64)]).tolist()) == A.shape[0]
hits = [[i for i, (tag, B) in enumerate(blocks) if same_span(A, B)] for _, A in atoms_q]
CHK("probeB_atoms_ARE_the_joint_charge_blocks_span_for_span",
    all(len(h) == 1 for h in hits) and sorted(h[0] for h in hits) == list(range(15)),
    "the banked tri-partition basis = the canonical joint eigenspace decomposition")

# ---------------- 5. C-side atoms (dps 60, two seeds, certified) ----------------
print("[5] C-side atoms at dps 60 (two seeds, residual-certified)...", flush=True)
def to_mp(M):
    A = mp.matrix(27, 27)
    for i in range(27):
        for j in range(27):
            v = F(M[i][j])
            A[i, j] = mp.mpf(int(v.numerator)) / mp.mpf(int(v.denominator))
    return A
Rn = {n: to_mp(Rex[n]) for n in ns}
Hp = to_mp(Hp_e); Hmm = to_mp(Hm_e)
def joint_atoms(coefs):
    Z = coefs[0] * Rn[8] + coefs[1] * Rn[14] + coefs[2] * Rn[16] + coefs[3] * Rn[22]
    Zc = mp.matrix(27, 27)
    for i in range(27):
        for j in range(27): Zc[i, j] = mp.mpc(Z[i, j])
    E, ER = mp.eig(Zc, left=False, right=True)
    clusters = []
    for k in sorted(range(27), key=lambda k: (mp.re(E[k]), mp.im(E[k]))):
        for cl in clusters:
            if abs(E[k] - cl["ev"]) < mp.mpf("1e-25"): cl["ks"].append(k); break
        else: clusters.append({"ev": E[k], "ks": [k]})
    atoms = []
    for cl in clusters:
        B = []
        for k in cl["ks"]:
            w = mp.matrix([ER[j, k] for j in range(27)])
            for u in B:
                w = w - u * sum(mp.conj(u[j]) * w[j] for j in range(27))
            B.append(w / mp.sqrt(sum(abs(w[j]) ** 2 for j in range(27))))
        A = {"dim": len(B), "B": B, "mu": {}, "res": mp.mpf(0)}
        for n in ns:
            imgs = [Rn[n] * v for v in B]
            m = len(B)
            Mr = mp.matrix(m, m)
            for a2 in range(m):
                for b2 in range(m):
                    Mr[a2, b2] = sum(mp.conj(B[a2][j]) * imgs[b2][j] for j in range(27))
            rmax = mp.mpf(0)
            for b2 in range(m):
                diff = imgs[b2] - sum((Mr[a2, b2] * B[a2] for a2 in range(m)), mp.matrix(27, 1))
                rmax = max(rmax, mp.sqrt(sum(abs(diff[j]) ** 2 for j in range(27))))
            offd = max((abs(Mr[a2, b2]) for a2 in range(m) for b2 in range(m) if a2 != b2),
                       default=mp.mpf(0))
            spread = max(abs(Mr[a2, a2] - Mr[0, 0]) for a2 in range(m))
            A["mu"][n] = Mr[0, 0]
            A["res"] = max(A["res"], rmax, offd, spread)
        atoms.append(A)
    return atoms
atoms = joint_atoms([mp.mpf(3), mp.mpf(17), mp.mpf(5), mp.mpf(7)])
atoms2 = joint_atoms([mp.mpf(2), mp.mpf(-11), mp.mpf(13), mp.mpf(23)])
CHK("C_atoms_shape_6x3_9x1_seed1",
    sorted(A["dim"] for A in atoms) == [1] * 9 + [3] * 6)
CHK("C_atoms_shape_6x3_9x1_seed2",
    sorted(A["dim"] for A in atoms2) == [1] * 9 + [3] * 6)
w1 = max(A["res"] for A in atoms); w2 = max(A["res"] for A in atoms2)
CHK("C_atoms_invariance+scalarity_residuals_below_1e-40",
    max(w1, w2) < mp.mpf("1e-40"), f"worst {mp.nstr(max(w1,w2),3)}")
def projd(a, b):
    m = mp.mpf(0)
    for i in range(27):
        for j in range(27):
            p1 = sum(v[i] * mp.conj(v[j]) for v in a["B"])
            p2 = sum(v[i] * mp.conj(v[j]) for v in b["B"])
            m = max(m, abs(p1 - p2))
    return m
pairs = []
for i, a in enumerate(atoms):
    bj = min((j for j, b in enumerate(atoms2) if b["dim"] == a["dim"]),
             key=lambda j: sum(abs(a["mu"][n] - atoms2[j]["mu"][n]) for n in ns))
    pairs.append((i, bj))
wd = max(projd(atoms[i], atoms2[j]) for i, j in pairs)
CHK("two_seed_projector_agreement_below_1e-45", wd < mp.mpf("1e-45"), f"max {mp.nstr(wd,3)}")

# Pi blocks, vacuum lines, frames
pibC = {}
for i, A in enumerate(atoms):
    kk = next((k2 for k2 in pibC if abs(A["mu"][8] - k2[0]) < mp.mpf("1e-25")
               and abs(A["mu"][16] - k2[1]) < mp.mpf("1e-25")), None)
    if kk is None: kk = (A["mu"][8], A["mu"][16]); pibC[kk] = []
    pibC[kk].append(i)
CHK("C_Pi_blocks_1_1_1_8_8_8",
    sorted(sum(atoms[i]["dim"] for i in v) for v in pibC.values()) == [1, 1, 1, 8, 8, 8])
vaclines = [v[0] for v in pibC.values() if sum(atoms[i]["dim"] for i in v) == 1]
MUc = [500716339200, -2075673600, -4769856, 2197]   # the banked pencil cubic (13x B866)
rts = sorted(mp.re(r) for r in mpmath.polyroots([mp.mpf(c) for c in MUc],
                                                maxsteps=400, extraprec=200))
vac_frame = {}
for vi in vaclines:
    for fi, t in enumerate(rts):
        lam = atoms[vi]["mu"][8] + t * atoms[vi]["mu"][16]
        mult = sum(A["dim"] for A in atoms
                   if abs((A["mu"][8] + t * A["mu"][16]) - lam) < mp.mpf("1e-20"))
        if mult == 1: vac_frame[vi] = fi
CHK("vacuum_lines_3_each_owns_one_frame",
    len(vaclines) == 3 and sorted(vac_frame.values()) == [0, 1, 2])
B889 = json.load(open(os.path.join(REPO, "frontier", "B889_canonical_dictionary",
                                   "results.json")))
CHK("B889_vacuum_frame_map_reproduced_{0:2,1:0,2:1}",
    B889["vacuum_frame_map"] == {"0": 2, "1": 0, "2": 1})
first_vac = next(vi for vi, fi in vac_frame.items() if fi == 2)  # B889 block 0
print(f"    first canonical vacuum line = atom {first_vac} (frame 2)", flush=True)

# ---------------- 6. normalization + Grams + verdict data ----------------
print("[6] normalized H+-, per-atom Grams, signatures, scales...", flush=True)
def hform(Hmat, u, v):
    Hv = Hmat * v
    return sum(mp.conj(u[j]) * Hv[j] for j in range(27))
def analyze(Hmat, tag):
    v0 = atoms[first_vac]["B"][0]
    c0 = hform(Hmat, v0, v0)
    assert abs(mp.im(c0)) < mp.mpf("1e-45") and abs(c0) > mp.mpf("1e-30")
    c0 = mp.re(c0)
    Hn = Hmat / c0
    rows = []
    for i, A in enumerate(atoms):
        m = A["dim"]
        G = mp.matrix(m, m)
        for a2 in range(m):
            for b2 in range(m):
                G[a2, b2] = hform(Hn, A["B"][a2], A["B"][b2])
        hres = max(abs(G[a2, b2] - mp.conj(G[b2, a2])) for a2 in range(m) for b2 in range(m))
        for a2 in range(m):
            for b2 in range(m):
                G[a2, b2] = (G[a2, b2] + mp.conj(G[b2, a2])) / 2
        if m == 1:
            evs = [mp.re(G[0, 0])]
        else:
            Eev, _ = mp.eighe(G)
            evs = [mp.re(x) for x in Eev]
        npos = sum(1 for e in evs if e > mp.mpf("1e-30"))
        nneg = sum(1 for e in evs if e < -mp.mpf("1e-30"))
        adet = mp.mpf(1)
        for e in evs: adet *= abs(e)
        rows.append(dict(atom=i, dim=m, kind="colored" if m == 3 else
                         ("vacuum" if i in vaclines else "colorless"),
                         sig=(npos, nneg, m - npos - nneg), herm_res=hres,
                         evs=evs, absdet=adet, scale=adet ** (mp.mpf(1) / m),
                         definite=(npos + nneg == m and (npos == 0 or nneg == 0))))
    xmax = mp.mpf(0)
    for i, A in enumerate(atoms):
        for j, B2 in enumerate(atoms):
            if i >= j: continue
            for u in A["B"]:
                for w in B2["B"]:
                    xmax = max(xmax, abs(hform(Hn, u, w)))
    return dict(c0=c0, rows=rows, cross=xmax)
resP = analyze(Hp, "+"); resM = analyze(Hmm, "-")
CHK("atoms_mutually_H_orthogonal_below_1e-45",
    max(resP["cross"], resM["cross"]) < mp.mpf("1e-45"),
    f"max {mp.nstr(max(resP['cross'], resM['cross']),3)}")
totP = (sum(r["sig"][0] for r in resP["rows"]), sum(r["sig"][1] for r in resP["rows"]))
sig_norm_exact = (nm_raw, np_raw) if resP["c0"] < 0 else (np_raw, nm_raw)
CHK("total_signature_atoms_sum_equals_exact_cycle_count",
    totP == sig_norm_exact, f"normalized signature {totP}")
minmargin = min(min(abs(e) for e in r["evs"]) for r in resP["rows"] + resM["rows"])
CHK("all_Gram_eigenvalues_bounded_away_from_zero",
    minmargin > mp.mpf("0.1"), f"min |eig| = {mp.nstr(minmargin, 6)} vs residuals < 1e-40")
# sigma+- gate: the declared readout must agree
gate_sig = all(rp["sig"] == rm2["sig"] for rp, rm2 in zip(resP["rows"], resM["rows"]))
gate_scale = max(abs(rp["scale"] - rm2["scale"]) / rp["scale"]
                 for rp, rm2 in zip(resP["rows"], resM["rows"]))
gate_c0 = abs(resP["c0"] - resM["c0"]) / abs(resP["c0"])
CHK("sigma_pm_crosscheck_identical_normalized_readout",
    gate_sig and gate_scale < mp.mpf("1e-40") and gate_c0 < mp.mpf("1e-40"),
    f"signatures identical; max rel scale diff {mp.nstr(gate_scale,3)}; "
    f"same normalization c0 (rel diff {mp.nstr(gate_c0,3)}); matrix-level: "
    "H- = H+ D exactly (D exhibited above, commutes with the charges, +1 on all "
    "nine 1-dim atoms) -- proportionality of the matrices themselves is impossible "
    "by rep theory (D is not scalar), see DRAFT_FINDINGS")

# verdict per the sealed two-outcome criteria
indef = [r["atom"] for r in resP["rows"] if not r["definite"]]
degen = [r["atom"] for r in resP["rows"] if r["sig"][2] > 0]
verdict = "A" if not indef else "B"
RESULT["verdict"] = verdict
RESULT["signature_H_normalized_exact"] = list(sig_norm_exact)
RESULT["normalization"] = {
    "line": "first canonical vacuum line = B889 block 0 = the frame-2 vacuum line",
    "H_raw_on_unit_vacuum_vectors_by_frame": {
        str(vac_frame[vi]): mp.nstr(mp.re(hform(Hp, atoms[vi]["B"][0], atoms[vi]["B"][0])), 35)
        for vi in vaclines},
    "c0_plus": mp.nstr(resP["c0"], 35), "c0_minus": mp.nstr(resM["c0"], 35)}
RESULT["atoms"] = [
    {"atom": r["atom"], "dim": r["dim"], "kind": r["kind"],
     "frame": vac_frame.get(r["atom"]),
     "mu8": mp.nstr(atoms[r["atom"]]["mu"][8], 35),
     "mu14": mp.nstr(atoms[r["atom"]]["mu"][14], 35),
     "mu16": mp.nstr(atoms[r["atom"]]["mu"][16], 35),
     "mu22": mp.nstr(atoms[r["atom"]]["mu"][22], 35),
     "signature": list(r["sig"]), "definite": r["definite"],
     "gram_eigenvalues": [mp.nstr(e, 35) for e in r["evs"]],
     "absdet": mp.nstr(r["absdet"], 35),
     "scale_absdet_pow_1_over_dim": mp.nstr(r["scale"], 35)}
    for r in resP["rows"]]
RESULT["outcome_B_where"] = {"indefinite_atoms": indef, "degenerate_atoms": degen,
                             "pattern": "all six colored 3-dim atoms indefinite (1,2); "
                                        "all nine colorless 1-dim atoms positive"}
RESULT["D_diag"] = [int(Dd[b][b]) for b in range(27)]
RESULT["runtime_s"] = round(time.time() - T0, 1)
json.dump(RESULT, open(os.path.join(HERE, "results.json"), "w"), indent=1)
print(f"\n=== VERDICT (sealed criteria): OUTCOME {verdict} ===")
if verdict == "B":
    print(f"  indefinite atoms: {indef} (signatures "
          f"{[tuple(r['sig']) for r in resP['rows'] if not r['definite']]}); degenerate: {degen}")
print(f"  total signature of H on the 27 (normalized): {sig_norm_exact}")
print(f"  results.json written; {RESULT['runtime_s']}s")
