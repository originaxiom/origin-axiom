"""B662 CELL A -- L101: the (i1,i2) metallic-uniformity verification.

Claim (see PROOF_NOTE.md): for every metallic once-punctured-torus-bundle
member, with V = 27 = Sym16 + Sym8 + Sym0 of the principal SL(2) inside E6,
    i1 = dim V^{holonomy}        = 1
    i2 = dim V^{peripheral Z^2}  = 3.
This script verifies EXACTLY, on both banked members, every computational
hypothesis and every conclusion of the proof note:

fig-8 (golden member m=1), field K = Q(sqrt(-3)):
  F1  SL2 relator holds (record I or -I)
  F2  tr[rho(a),rho(b)] != 2          (irreducible pair)
  F3  rho(a) noncentral parabolic     (trace 2, != I)
  F4  rho(LONG) upper triangular, diag = (d,d), d^2=1, off-diag != 0
      (noncentral +-unipotent SHARING the fixed vector e1 with rho(a))
  F5  rho(a) rho(LONG) = rho(LONG) rho(a)   (matrix commutation)
  F6  group-level [LONG, a] = 1 in pi1 (van Kampen certificate, replayed)
  F7  sl2 brackets of (e_pr, f_pr, h_pr); h_pr diagonal, all weights even
  F8  Casimir commutes with e,f,h; eigen-dims (17,9,1) at (144,40,0)
      -> the 27 = V(16)+V(8)+V(0) as a principal-sl2 module
  F9  dim ker(e_pr) = 3 (one highest-weight line per block)
  F10 level tie: lift(rho2(a)) = A27, lift(rho2(b)) = B27,
      27-letter product over LONG = lift(rho2(LONG)), relator27 = I
  F11 i1 = dim [ker(A27-I) cap ker(B27-I)] = 1  (banked; recomputed)
  F12 the i1-line is the Sym0 block: e_pr v = f_pr v = 0;
      and dim [ker e_pr cap ker f_pr] = 1 (= V^{SL2} directly)
  F13 i2 = dim [ker(A27-I) cap ker(Mlam27-I)] = 3
  F14 27-level peripheral commutation
  F15 per-block joint fixed dims = (1,1,1) via Casimir-stacked kernels

silver (member m=2), field L = Q(s,i), s^4 = 8 s^2 + 16:
  S1  SL2 relators aBAbcc, aaCbcB hold (record I or -I)
  S2  some generator pair has tr[X,Y] != 2 (irreducible)
  S3  MU2 = rho2(CCB), LAM2 = rho2(caCA) noncentral parabolic (trace +-2)
  S4  MU2 LAM2 = LAM2 MU2
  S5  common fixed vector w: (MU2 - eps1) w = 0 = (LAM2 - eps2) w
  S6  sl2 brackets over L; h diagonal, even weights; Casimir dims (17,9,1)
  S7  dim ker(E_PR) = 3
  S8  level tie: S1[g] = lift(G2[g]) for g in abcABC;
      Mmu27 = lift(MU2), Mlam27 = lift(LAM2); relators27 = I
  S9  i1 = dim [cap_g ker(S1[g]-I), g=a,b,c] = 1  (banked h0=1; recomputed)
  S10 Sym0 check + dim [ker E_PR cap ker F_PR] = 1
  S11 i2 = dim [ker(Mmu27-I) cap ker(Mlam27-I)] = 3
  S12 27-level peripheral commutation
  S13 per-block joint fixed dims = (1,1,1)

Exact arithmetic throughout (Fraction pairs over K; Fraction 8-tuples over
L). No floats anywhere.
"""
import os
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
FRONTIER = os.path.abspath(os.path.join(HERE, "..", ".."))
B637 = os.path.join(FRONTIER, "B637_corrected_cell3")
B649 = os.path.join(FRONTIER, "B649_silver_holonomy")

T00 = time.time()
CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}   [{time.time()-T00:7.1f}s]",
          flush=True)
    return bool(ok)


# ============================================================================
print("=" * 76, flush=True)
print("PART 1: fig-8 (golden member m=1), K = Q(sqrt(-3))", flush=True)
print("=" * 76, flush=True)

mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
ns = mod["ns"]

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
A27, B27, A27i, B27i = mod["A27"], mod["B27"], mod["A27i"], mod["B27i"]
e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
nullspaceK = mod["nullspace"]
meyeK, mmulK = mod["meye"], mod["mmul"]
maddK, msubK, mscaleK, mzero_pK = (ns["madd"], ns["msub"], ns["mscale"],
                                   ns["mzero_p"])
mexp_nilK = ns["mexp_nil"]
applyK = mod["apply"]
lets2 = mod["lets2"]
LONG = mod["LONG"]
REL = ns["REL"]
freduce, invw = mod["freduce"], mod["inv"]
certify = mod["certify"]
lift_sl2K = mod["lift_sl2"]
wmat2 = mod["wmat2"]
print(f"\nfig-8 apparatus loaded [{time.time()-T00:.1f}s]", flush=True)
print(f"  REL = {REL}; LONG = {LONG}; peripheral pair = ('a', LONG)",
      flush=True)


def mm2K(X, Y):
    return [[X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)]
            for i in range(2)]


def adj2K(M):
    return [[M[1][1], -M[0][1]], [-M[1][0], M[0][0]]]


def tr2K(M):
    return M[0][0] + M[1][1]


def meqK(X, Y):
    return all((X[i][j] - Y[i][j]).is_zero()
               for i in range(len(X)) for j in range(len(X)))


def eye2K():
    return [[K1, K0], [K0, K1]]


Ag, Bg = lets2['a'], lets2['b']

# ---- F1: SL2 relator ------------------------------------------------------
relm = wmat2(REL)
rel_is_I = meqK(relm, eye2K())
rel_is_mI = meqK(relm, [[-K1, K0], [K0, -K1]])
check("F1  fig8 SL2: relator = +I or -I", rel_is_I or rel_is_mI)
print(f"      relator value: {'+I' if rel_is_I else ('-I' if rel_is_mI else 'NEITHER')}",
      flush=True)

# ---- F2: irreducibility ---------------------------------------------------
comm2 = mm2K(mm2K(Ag, Bg), mm2K(adj2K(Ag), adj2K(Bg)))
kappa = tr2K(comm2)
check("F2  fig8 SL2: tr[rho(a),rho(b)] != 2 (irreducible pair)",
      not (kappa - K(2)).is_zero())
print(f"      tr[a,b] = {kappa}", flush=True)

# ---- F3: meridian noncentral parabolic ------------------------------------
trA = tr2K(Ag)
check("F3  fig8 SL2: tr rho(a) = 2 and rho(a) != I (noncentral parabolic)",
      (trA - K(2)).is_zero() and not meqK(Ag, eye2K()))

# ---- F3b: a second noncentral parabolic, independent fixed vector ----------
trB = tr2K(Bg)
NA = [[Ag[0][0] - K1, Ag[0][1]], [Ag[1][0], Ag[1][1] - K1]]
NB = [[Bg[0][0] - K1, Bg[0][1]], [Bg[1][0], Bg[1][1] - K1]]


def fixvec2K(N):
    if not (N[0][0].is_zero() and N[0][1].is_zero()):
        return (N[0][1], -N[0][0])
    return (N[1][1], -N[1][0])


wA, wB = fixvec2K(NA), fixvec2K(NB)
detAB = wA[0] * wB[1] - wA[1] * wB[0]
ok3b = ((trB - K(2)).is_zero() and not meqK(Bg, eye2K())
        and all((NA[i][0] * wA[0] + NA[i][1] * wA[1]).is_zero()
                for i in range(2))
        and all((NB[i][0] * wB[0] + NB[i][1] * wB[1]).is_zero()
                for i in range(2))
        and not detAB.is_zero())
check("F3b fig8 SL2: rho(b) noncentral parabolic; fixed vectors of rho(a), "
      "rho(b) independent", ok3b)
print(f"      wA = ({wA[0]}, {wA[1]}), wB = ({wB[0]}, {wB[1]}), "
      f"det = {detAB}", flush=True)

# ---- F4: longitude shares the fixed vector e1 -----------------------------
lam2 = wmat2(LONG)
d_l = lam2[0][0]
ok4 = (lam2[1][0].is_zero() and (lam2[1][1] - d_l).is_zero()
       and (d_l * d_l - K1).is_zero() and not lam2[0][1].is_zero())
check("F4  fig8 SL2: rho(LONG) = d*(unipotent), d^2=1, upper-triangular, "
      "noncentral (shares fixed vector e1 with rho(a))", ok4)
print(f"      rho(LONG) = [[{lam2[0][0]}, {lam2[0][1]}], "
      f"[{lam2[1][0]}, {lam2[1][1]}]]", flush=True)

# ---- F5: SL2 commutation --------------------------------------------------
check("F5  fig8 SL2: rho(a) rho(LONG) = rho(LONG) rho(a)",
      meqK(mm2K(Ag, lam2), mm2K(lam2, Ag)))

# ---- F6: group-level commutation certificate ------------------------------
try:
    comm_w = freduce(LONG + "a" + invw(LONG) + "A")
    cert = certify(comm_w)
    check("F6  fig8 group: [LONG, a] = 1 in pi1 (van Kampen certificate, "
          "replay-verified)", True)
    print(f"      |commutator word| = {len(comm_w)}, certificate area = "
          f"{len(cert)}", flush=True)
except AssertionError as e:
    check("F6  fig8 group: [LONG, a] = 1 in pi1 (certificate)", False)
    print(f"      certificate FAILED: {e}", flush=True)


# ---- F7: sl2 triple + even weights ----------------------------------------
def brK(X, Y):
    return msubK(mmulK(X, Y), mmulK(Y, X))


ok7 = (mzero_pK(msubK(brK(e_pr, f_pr), h_pr))
       and mzero_pK(msubK(brK(h_pr, e_pr), mscaleK(K(2), e_pr)))
       and mzero_pK(msubK(brK(h_pr, f_pr), mscaleK(K(-2), f_pr))))
hdiag = all(h_pr[i][j].is_zero() for i in range(27) for j in range(27)
            if i != j)
wgts = [h_pr[i][i].a for i in range(27)]
heven = all(x.denominator == 1 and x.numerator % 2 == 0 for x in wgts)
check("F7  fig8 27: [e,f]=h, [h,e]=2e, [h,f]=-2f; h diagonal, all weights "
      "even integers", ok7 and hdiag and heven)
print(f"      weight multiset extremes: max = {max(wgts)}, min = {min(wgts)}",
      flush=True)

# ---- F8: Casimir block structure ------------------------------------------
CASK = maddK(maddK(mmulK(e_pr, f_pr), mmulK(f_pr, e_pr)),
             mscaleK(K(Fr(1, 2)), mmulK(h_pr, h_pr)))
ok_com = all(mzero_pK(brK(CASK, X)) for X in (e_pr, f_pr, h_pr))


def rowsK_minus(M, lam):
    return [[M[i][j] - (lam if i == j else K0) for j in range(27)]
            for i in range(27)]


dimsK = [len(nullspaceK(rowsK_minus(CASK, K(v)))) for v in (144, 40, 0)]
check("F8  fig8 27: Casimir central; eigen-dims (17,9,1) at (144,40,0) "
      "-> 27 = V(16)+V(8)+V(0)", ok_com and dimsK == [17, 9, 1])
print(f"      Casimir eigen-dims = {dimsK} (sum {sum(dimsK)})", flush=True)

# ---- F9: highest-weight count ---------------------------------------------
dim_ker_e = len(nullspaceK([row[:] for row in e_pr]))
check("F9  fig8 27: dim ker(e_pr) = 3 (one highest-weight line per block)",
      dim_ker_e == 3)

# ---- F10: level ties -------------------------------------------------------
lets1 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}


def word27K(w):
    M = meyeK(27)
    for ch in w:
        M = mmulK(M, lets1[ch])
    return M


ok10a = meqK(lift_sl2K(Ag), A27)
ok10b = meqK(lift_sl2K(Bg), B27)
Mlam27 = word27K(LONG)
ok10c = meqK(Mlam27, lift_sl2K(lam2))
rel27 = word27K(REL)
ok10d = meqK(rel27, meyeK(27))
check("F10 fig8 tie: lift(a)=A27, lift(b)=B27, prod27(LONG)=lift(rho2(LONG)),"
      " relator27 = I", ok10a and ok10b and ok10c and ok10d)


# ---- F11: i1 ---------------------------------------------------------------
def stackK(mats):
    rows = []
    for M in mats:
        rows += rowsK_minus(M, K1)
    return rows


i1_basis = nullspaceK(stackK([A27, B27]))
check("F11 fig8: i1 = dim V^{rho(pi1)} = 1", len(i1_basis) == 1)
print(f"      i1 = {len(i1_basis)}", flush=True)

# ---- F12: the invariant line is Sym0; V^{SL2} directly ---------------------
ok12 = True
if len(i1_basis) == 1:
    v0 = i1_basis[0]
    ok12 = (all(x.is_zero() for x in applyK(e_pr, v0))
            and all(x.is_zero() for x in applyK(f_pr, v0)))
sl2fix = nullspaceK([row[:] for row in e_pr] + [row[:] for row in f_pr])
check("F12 fig8: i1-line killed by e,f (Sym0 block); "
      "dim[ker e cap ker f] = 1 (= V^{SL2})", ok12 and len(sl2fix) == 1)

# ---- F13: i2 ---------------------------------------------------------------
i2_basis = nullspaceK(stackK([A27, Mlam27]))
check("F13 fig8: i2 = dim V^{rho(peripheral Z^2)} = 3", len(i2_basis) == 3)
print(f"      i2 = {len(i2_basis)}", flush=True)

# ---- F14: 27-level peripheral commutation ----------------------------------
check("F14 fig8 27: peripheral images commute",
      mzero_pK(msubK(mmulK(A27, Mlam27), mmulK(Mlam27, A27))))

# ---- F15: per-block joint fixed dims ----------------------------------------
blocksK = []
for lam_v, kk in ((144, 16), (40, 8), (0, 0)):
    rows = stackK([A27, Mlam27]) + rowsK_minus(CASK, K(lam_v))
    blocksK.append(len(nullspaceK(rows)))
check("F15 fig8: per-block joint peripheral fixed dims (Sym16,Sym8,Sym0) = "
      "(1,1,1)", blocksK == [1, 1, 1])
print(f"      per-block dims = {blocksK}", flush=True)

FIG8_OK = all(ok for _, ok in CHECKS)

# ============================================================================
print("", flush=True)
print("=" * 76, flush=True)
print("PART 2: silver (member m=2, monodromy RRLL), L = Q(s,i), "
      "s^4 = 8 s^2 + 16", flush=True)
print("=" * 76, flush=True)

src3a = open(os.path.join(B649, "b649_stage3a.py")).read()
head = src3a[:src3a.index('print("== S3a-G1')]
ns2 = {"__name__": "cellA_silver",
       "__file__": os.path.join(B649, "b649_stage3a.py")}
exec(compile(head, "b649_stage3a_head.py", "exec"), ns2)

L, Lc, L0, L1 = ns2["L"], ns2["Lc"], ns2["L0"], ns2["L1"]
meyeL, mmulL, mscaleL, maddL = (ns2["meye"], ns2["mmul"], ns2["mscale"],
                                ns2["madd"])
E_PR, F_PR, H_PR = ns2["E_PR"], ns2["F_PR"], ns2["H_PR"]
lift_sl2L = ns2["lift_sl2"]
S1L = ns2["S1"]
G2 = ns2["G2"]
word2 = ns2["word2"]
mm2L, adj2L = ns2["mm2"], ns2["adj2"]
MU2, LAM2 = ns2["MU2"], ns2["LAM2"]
MU_W, LAM_W = "CCB", "caCA"
print(f"\nsilver apparatus loaded [{time.time()-T00:.1f}s]", flush=True)
print(f"  relators: aBAbcc, aaCbcB; peripheral pair = ({MU_W}, {LAM_W})",
      flush=True)


def meqL(X, Y):
    return all((X[i][j] - Y[i][j]).is_zero()
               for i in range(len(X)) for j in range(len(X)))


def msubL(X, Y):
    return [[a - b for a, b in zip(rx, ry)] for rx, ry in zip(X, Y)]


def mzero_pL(M):
    return all(x.is_zero() for row in M for x in row)


def eye2L():
    return [[L1, L0], [L0, L1]]


def tr2L(M):
    return M[0][0] + M[1][1]


def lstr(x):
    return f"({x.re}|{x.im})"


def L_nullspace_basis(rows, ncols):
    A = [r[:] for r in rows]
    m = len(A)
    r = 0
    pivs = []
    for cidx in range(ncols):
        piv = next((k for k in range(r, m) if not A[k][cidx].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv_inv = A[r][cidx].inv()
        A[r] = [x * pv_inv for x in A[r]]
        for k in range(m):
            if k != r and not A[k][cidx].is_zero():
                f = A[k][cidx]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        pivs.append(cidx)
        r += 1
        if r == m:
            break
    free = [cx for cx in range(ncols) if cx not in pivs]
    basis = []
    for fc in free:
        v = [L0] * ncols
        v[fc] = L1
        for rr, pc in enumerate(pivs):
            v[pc] = L0 - A[rr][fc]
        basis.append(v)
    return basis


def applyL(M, v):
    return [sum((M[i][k] * v[k] for k in range(27) if not v[k].is_zero()),
                L0) for i in range(27)]


# ---- S1: SL2 relators ------------------------------------------------------
ok_s1 = True
for rw in ("aBAbcc", "aaCbcB"):
    rm = word2(rw)
    is_I = meqL(rm, eye2L())
    is_mI = meqL(rm, [[L0 - L1, L0], [L0, L0 - L1]])
    ok_s1 = ok_s1 and (is_I or is_mI)
    print(f"      SL2 relator {rw}: "
          f"{'+I' if is_I else ('-I' if is_mI else 'NEITHER')}", flush=True)
check("S1  silver SL2: both relators = +I or -I", ok_s1)

# ---- S2: irreducibility ----------------------------------------------------
irr_pair = None
for (x, y) in (("a", "b"), ("a", "c"), ("b", "c")):
    X, Y = G2[x], G2[y]
    cm = mm2L(mm2L(X, Y), mm2L(adj2L(X), adj2L(Y)))
    t = tr2L(cm)
    if not (t - Lc(2)).is_zero():
        irr_pair = (x, y, t)
        break
check("S2  silver SL2: some generator pair has tr[X,Y] != 2 (irreducible)",
      irr_pair is not None)
if irr_pair:
    print(f"      pair ({irr_pair[0]},{irr_pair[1]}): tr[X,Y] = "
          f"{lstr(irr_pair[2])}", flush=True)


# ---- S3: peripheral words noncentral parabolic ----------------------------
def parab_data(M, label):
    t = tr2L(M)
    if (t - Lc(2)).is_zero():
        eps = L1
    elif (t + Lc(2)).is_zero():
        eps = L0 - L1
    else:
        print(f"      {label}: trace NOT +-2: {lstr(t)}", flush=True)
        return None, None
    N = [[M[0][0] - eps, M[0][1]], [M[1][0], M[1][1] - eps]]
    nonzero = not all(x.is_zero() for row in N for x in row)
    return (eps if nonzero else None), N


eps_mu, N_mu = parab_data(MU2, "MU2")
eps_lam, N_lam = parab_data(LAM2, "LAM2")
check("S3  silver SL2: MU2 and LAM2 both noncentral parabolic (trace +-2, "
      "!= +-I)", eps_mu is not None and eps_lam is not None)
if eps_mu is not None:
    print(f"      tr MU2 = {lstr(tr2L(MU2))}; tr LAM2 = {lstr(tr2L(LAM2))}",
          flush=True)

# ---- S4: SL2 commutation ---------------------------------------------------
check("S4  silver SL2: MU2 LAM2 = LAM2 MU2",
      meqL(mm2L(MU2, LAM2), mm2L(LAM2, MU2)))

# ---- S5: common fixed vector -----------------------------------------------
ok_s5 = False
if eps_mu is not None and eps_lam is not None:
    if not (N_mu[0][0].is_zero() and N_mu[0][1].is_zero()):
        w = (N_mu[0][1], L0 - N_mu[0][0])
    else:
        w = (N_mu[1][1], L0 - N_mu[1][0])
    wnz = not (w[0].is_zero() and w[1].is_zero())
    kill_mu = all((N_mu[i][0] * w[0] + N_mu[i][1] * w[1]).is_zero()
                  for i in range(2))
    kill_lam = all((N_lam[i][0] * w[0] + N_lam[i][1] * w[1]).is_zero()
                   for i in range(2))
    ok_s5 = wnz and kill_mu and kill_lam
    print(f"      w = ({lstr(w[0])}, {lstr(w[1])}); "
          f"(MU2-eps)w=0: {kill_mu}; (LAM2-eps')w=0: {kill_lam}", flush=True)
check("S5  silver SL2: MU2, LAM2 share the fixed vector exactly", ok_s5)


# ---- S5b: a second noncentral parabolic, independent fixed vector ----------
ok_s5b = False
if ok_s5:
    for gname in "abc":
        g = G2[gname]
        wp = (g[0][0] * w[0] + g[0][1] * w[1],
              g[1][0] * w[0] + g[1][1] * w[1])
        det_wwp = w[0] * wp[1] - w[1] * wp[0]
        if not det_wwp.is_zero():
            q = mm2L(mm2L(g, MU2), adj2L(g))
            Nq = [[q[0][0] - eps_mu, q[0][1]], [q[1][0], q[1][1] - eps_mu]]
            kill_q = all((Nq[i][0] * wp[0] + Nq[i][1] * wp[1]).is_zero()
                         for i in range(2))
            nonc_q = not all(x.is_zero() for row in Nq for x in row)
            ok_s5b = kill_q and nonc_q
            print(f"      q = rho({gname}) MU2 rho({gname})^-1: noncentral "
                  f"parabolic, fixed vector g.w independent of w "
                  f"(det = {lstr(det_wwp)})", flush=True)
            break
check("S5b silver SL2: a second noncentral parabolic with independent fixed "
      "vector (conjugate of MU2)", ok_s5b)

# ---- S6: sl2 triple + Casimir over L ---------------------------------------
def brL(X, Y):
    return msubL(mmulL(X, Y), mmulL(Y, X))


ok_s6a = (mzero_pL(msubL(brL(E_PR, F_PR), H_PR))
          and mzero_pL(msubL(brL(H_PR, E_PR), mscaleL(Lc(2), E_PR)))
          and mzero_pL(msubL(brL(H_PR, F_PR), mscaleL(Lc(-2), F_PR))))
hdiagL = all(H_PR[i][j].is_zero() for i in range(27) for j in range(27)
             if i != j)
wgtsL = [H_PR[i][i].re[0] for i in range(27)]
hevenL = all(x.denominator == 1 and x.numerator % 2 == 0 for x in wgtsL)
CASL = maddL(maddL(mmulL(E_PR, F_PR), mmulL(F_PR, E_PR)),
             mscaleL(Lc(Fr(1, 2)), mmulL(H_PR, H_PR)))
ok_s6b = all(mzero_pL(brL(CASL, X)) for X in (E_PR, F_PR, H_PR))


def rowsL_minus(M, lam):
    return [[M[i][j] - (lam if i == j else L0) for j in range(27)]
            for i in range(27)]


dimsL = [len(L_nullspace_basis(rowsL_minus(CASL, Lc(v)), 27))
         for v in (144, 40, 0)]
check("S6  silver 27: sl2 triple; h diagonal, even weights; Casimir central;"
      " eigen-dims (17,9,1)", ok_s6a and hdiagL and hevenL and ok_s6b
      and dimsL == [17, 9, 1])
print(f"      Casimir eigen-dims = {dimsL} (sum {sum(dimsL)})", flush=True)

# ---- S7: highest-weight count ----------------------------------------------
dim_ker_eL = len(L_nullspace_basis([row[:] for row in E_PR], 27))
check("S7  silver 27: dim ker(E_PR) = 3", dim_ker_eL == 3)


# ---- S8: level ties ---------------------------------------------------------
def word27L(w):
    M = meyeL(27)
    for ch in w:
        M = mmulL(M, S1L[ch])
    return M


ok_s8 = True
for nm in "abcABC":
    ok_nm = meqL(lift_sl2L(G2[nm]), S1L[nm])
    ok_s8 = ok_s8 and ok_nm
    if not ok_nm:
        print(f"      letter {nm}: lift MISMATCH", flush=True)
Mmu27 = word27L(MU_W)
Mlam27L = word27L(LAM_W)
ok_s8b = meqL(Mmu27, lift_sl2L(MU2)) and meqL(Mlam27L, lift_sl2L(LAM2))
ok_s8c = (meqL(word27L("aBAbcc"), meyeL(27))
          and meqL(word27L("aaCbcB"), meyeL(27)))
check("S8  silver tie: 27-letters = lifts of SL2 letters; word products = "
      "lifts of MU2/LAM2; relators27 = I", ok_s8 and ok_s8b and ok_s8c)


# ---- S9: i1 ------------------------------------------------------------------
def stackL(mats):
    rows = []
    for M in mats:
        rows += rowsL_minus(M, L1)
    return rows


i1_basis_L = L_nullspace_basis(stackL([S1L["a"], S1L["b"], S1L["c"]]), 27)
check("S9  silver: i1 = dim V^{rho(pi1)} = 1", len(i1_basis_L) == 1)
print(f"      i1 = {len(i1_basis_L)}", flush=True)

# ---- S10: Sym0 + V^{SL2} -----------------------------------------------------
ok_s10 = True
if len(i1_basis_L) == 1:
    v0L = i1_basis_L[0]
    ok_s10 = (all(x.is_zero() for x in applyL(E_PR, v0L))
              and all(x.is_zero() for x in applyL(F_PR, v0L)))
sl2fixL = L_nullspace_basis([row[:] for row in E_PR]
                            + [row[:] for row in F_PR], 27)
check("S10 silver: i1-line killed by e,f (Sym0); dim[ker e cap ker f] = 1",
      ok_s10 and len(sl2fixL) == 1)

# ---- S11: i2 -----------------------------------------------------------------
i2_basis_L = L_nullspace_basis(stackL([Mmu27, Mlam27L]), 27)
check("S11 silver: i2 = dim V^{rho(peripheral Z^2)} = 3",
      len(i2_basis_L) == 3)
print(f"      i2 = {len(i2_basis_L)}", flush=True)

# ---- S12: 27-level peripheral commutation ------------------------------------
check("S12 silver 27: peripheral images commute",
      mzero_pL(msubL(mmulL(Mmu27, Mlam27L), mmulL(Mlam27L, Mmu27))))

# ---- S13: per-block joint fixed dims -----------------------------------------
blocksL = []
for lam_v, kk in ((144, 16), (40, 8), (0, 0)):
    rows = stackL([Mmu27, Mlam27L]) + rowsL_minus(CASL, Lc(lam_v))
    blocksL.append(len(L_nullspace_basis(rows, 27)))
check("S13 silver: per-block joint peripheral fixed dims (Sym16,Sym8,Sym0) "
      "= (1,1,1)", blocksL == [1, 1, 1])
print(f"      per-block dims = {blocksL}", flush=True)

# ============================================================================
print("", flush=True)
print("=" * 76, flush=True)
nfail = sum(1 for _, ok in CHECKS if not ok)
npass = sum(1 for _, ok in CHECKS if ok)
print(f"SUMMARY: {npass}/{len(CHECKS)} checks pass, {nfail} fail "
      f"[{time.time()-T00:.1f}s total]", flush=True)
for name, ok in CHECKS:
    if not ok:
        print(f"  FAILED: {name}", flush=True)
if nfail == 0:
    print("\nVERDICT: PROVEN+VERIFIED -- (i1, i2) = (1, 3) on both banked "
          "metallic members;\nevery hypothesis of the uniformity proof "
          "(PROOF_NOTE.md) verified exactly.", flush=True)
else:
    print("\nVERDICT: GAP -- see failed checks above.", flush=True)
