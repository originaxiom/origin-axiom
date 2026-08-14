"""B925 THE SECOND CROSSING (R4b) -- computed per the sealed prereg (PREREGISTRATION.md).

Ladder under test (sealed): SM at M_Z -> [M3] D3-stage -> [M4] D4-stage -> [M5] D5-stage
-> [MU] E6, with the BANKED chain typings (B909 lane):
  D3-stage = su(4) + u(1)^3   (cross-shadow 18: derived 15 = su(4), center 3)
  D4-stage = so(8) + u(1)^2   (compact wall 30, CMT)
  D5-stage = so(10) + u(1)    (FMT wall 46)
and the banked inclusions su(3)_c, u(1)_{B-L} inside su(4) = D3's derived; D3 in D4 in D5.

PRE-STATED DECISIONS (fixed before any Part-1/Part-2 number is evaluated; the
anti-shopping clause is absolute):
 1. Matter table (three full 27-branchings per stage; complete reps at every rung):
    [M_Z, M5]: the SM stage runs the B915 content (three families = the SM part of
       three 16's; nu^c neutral; each 27's 10+1 acquires mass at the so(10)-breaking
       rung M5 -- survival-minimal), gauge b = (41/10, -19/6, -7), banked 2-loop matrix.
    [M5, MU]: three full 27's = 3 x (16 + 10 + 1) of so(10), X-charges (1, -2, 4)/(2 sqrt6).
    D3/D4 windows: branchings recorded (27 under so(8)+u(1)^2 = 8v+8s+8c+3x1;
       under su(4)+u(1)^3 = 6 + 2x(4+4bar) + 5x1); windows shown below to be forced closed.
 2. Scalar table (minimal set, stated first): [M_Z, M5]: one Higgs doublet (B915
    convention); [M5, MU]: one full complex scalar 27. Closed windows: none needed.
 3. Loop order: one-loop primary; the 1<->2-loop shift = sigma_th (B915 convention);
    matching one-loop, no threshold corrections.
 4. Inputs: the B915 values verbatim: 1/alpha_em(MZ) = 127.951(9), sin2thetaW(MZ)
    = 0.23122(4), alpha_s(MZ) = 0.1180(9); boundary: E6 unification, banked 3/8.
 5. THE MENU exactly as sealed (items a-f), values below. Orientation convention for
    ratio-type entries (a), (b), (d): a ratio is quoted in its banked orientation AND
    its reciprocal is recorded; matching distances are computed in |ln| space where
    orientation is a sign -- both reported, verdict text flags any orientation use.
 6. Match criterion (sealed): a required rho equals one menu entry or a product of at
    most TWO menu entries (repetition allowed) within sigma_th propagated to the ratio;
    distance metric |ln(rho/m)| / sigma_ln.
DATA CONTACT: no data beyond the three M_Z inputs already banked in B915.
"""
import json, math, os, itertools
from fractions import Fraction as Fr
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from mpmath import mp, mpf, polyroots

HERE = os.path.dirname(os.path.abspath(__file__))
mp.dps = 50
R = {"cell": "B925 R4b second crossing", "sealed_prereg": "PREREGISTRATION.md",
     "checks": {}, "notes": []}

def check(name, ok, detail=""):
    R["checks"][name] = {"pass": bool(ok), "detail": str(detail)}
    print(("PASS " if ok else "FAIL ") + name + (" -- " + str(detail) if detail else ""))
    return ok

# =====================================================================
# PART A -- THE ALGEBRAIC LADDER AUDIT (exact; the embedding indices and the
# obstruction certificates, computed from the algebra -- no chart citations)
# =====================================================================
print("\n== PART A: the algebraic ladder audit (exact) ==")
# so(10) on R^10, coordinates (x1..x5, y1..y5); z_k = x_k + i y_k.
# u(5) -> so(10): A = P + iQ (P antisym, Q sym) |-> [[P, -Q], [Q, P]].
def emb(P, Q):
    M = [[Fr(0)] * 10 for _ in range(10)]
    for i in range(5):
        for j in range(5):
            M[i][j] = Fr(P[i][j]); M[i][5 + j] = -Fr(Q[i][j])
            M[5 + i][j] = Fr(Q[i][j]); M[5 + i][5 + j] = Fr(P[i][j])
    return M

def Z5(): return [[Fr(0)] * 5 for _ in range(5)]
def comm(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] - B[i][k] * A[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]
def is_zero(M): return all(all(x == 0 for x in r) for r in M)

def P_rot(i, j):
    P = Z5(); P[i][j] = Fr(1); P[j][i] = Fr(-1); return P
def Q_sym(i, j):
    Q = Z5(); Q[i][j] = Fr(1); Q[j][i] = Fr(1); return Q
def Q_diag(d):
    Q = Z5()
    for i, v in enumerate(d): Q[i][i] = Fr(v)
    return Q

# su(3)_c on z1..z3 (the banked su(3)_c-in-su(4) block), su(2)_L on z4,z5, Y, B-L:
su3 = ([emb(P_rot(i, j), Z5()) for i in range(3) for j in range(i + 1, 3)] +
       [emb(Z5(), Q_sym(i, j)) for i in range(3) for j in range(i + 1, 3)] +
       [emb(Z5(), Q_diag([1, -1, 0, 0, 0])), emb(Z5(), Q_diag([1, 1, -2, 0, 0]))])
su2L = [emb(P_rot(3, 4), Z5()), emb(Z5(), Q_sym(3, 4)),
        emb(Z5(), Q_diag([0, 0, 0, 1, -1]))]
Ygen = emb(Z5(), Q_diag([Fr(-2, 3), Fr(-2, 3), Fr(-2, 3), 1, 1]))  # Y on 5=( D,D,D,Hu,Hu )-slots
BLgen = emb(Z5(), Q_diag([1, 1, 1, 0, 0]))  # the u(1) of u(3) in so(6): the B-L direction

def rot10(a, b):
    M = [[Fr(0)] * 10 for _ in range(10)]
    M[a][b] = Fr(1); M[b][a] = Fr(-1); return M

so6_coords = [0, 1, 2, 5, 6, 7]           # x1x2x3 y1y2y3: so(6) = su(4), the D3 derived
so8_coords = so6_coords + [3, 8]          # + x4 y4: the D4 core so(8)
so6 = [rot10(a, b) for a, b in itertools.combinations(so6_coords, 2)]
so8 = [rot10(a, b) for a, b in itertools.combinations(so8_coords, 2)]
so10 = [rot10(a, b) for a, b in itertools.combinations(range(10), 2)]
Rz4 = rot10(3, 8)   # so(2) on z4
Rz5 = rot10(4, 9)   # so(2) on z5
H = [rot10(5 + k, k) for k in range(5)]  # the so(10) Cartan (z_k phase rotations;
# sign chosen to agree with emb(0, e_kk): emb puts -1 at (k,5+k), +1 at (5+k,k))

check("su3c_in_su4_block_commutes_with_su2L_all_24_pairs",
      all(is_zero(comm(a, b)) for a in su3 for b in su2L))
check("su3c_commutes_with_BL", all(is_zero(comm(a, BLgen)) for a in su3))
check("Y_in_so10_Cartan_exact_Y_eq_sum_Yk_Hk",
      is_zero([[Ygen[i][j] - sum(c * h[i][j] for c, h in
                                 zip([Fr(-2, 3)] * 3 + [Fr(1), Fr(1)], H))
                for j in range(10)] for i in range(10)]),
      "Y = -2/3(H1+H2+H3) + H4 + H5 -> the E6/so(10) u(1)_X carries NO piece of Y")

# --- centralizer nullities: explicit kernel members (exact) + mod-p upper bounds ---
def centralizer_nullity_modp(sub, amb, p):
    # rank over F_p of the map X -> ([g,X])_{g in sub}, X in span(amb)
    rows = []
    for g in sub:
        cols = [comm(g, B) for B in amb]
        for i in range(10):
            for j in range(10):
                row = [int((c[i][j].numerator * pow(c[i][j].denominator, -1, p)) % p)
                       for c in cols]
                if any(row): rows.append(row)
    m = len(amb); rr = 0
    for c in range(m):
        pr = next((x for x in range(rr, len(rows)) if rows[x][c] % p), None)
        if pr is None: continue
        rows[rr], rows[pr] = rows[pr], rows[rr]
        iv = pow(rows[rr][c], -1, p)
        rows[rr] = [(e * iv) % p for e in rows[rr]]
        for x in range(len(rows)):
            if x != rr and rows[x][c]:
                f = rows[x][c]
                rows[x] = [(rows[x][j] - f * rows[rr][j]) % p for j in range(m)]
        rr += 1
    return m - rr

def members_rank_modp(members, p):
    rows = [[int((x.numerator * pow(x.denominator, -1, p)) % p) for row in M for x in row]
            for M in members]
    m = len(rows[0]); rr = 0
    for c in range(m):
        pr = next((x for x in range(rr, len(rows)) if rows[x][c] % p), None)
        if pr is None: continue
        rows[rr], rows[pr] = rows[pr], rows[rr]
        iv = pow(rows[rr][c], -1, p)
        rows[rr] = [(e * iv) % p for e in rows[rr]]
        for x in range(len(rows)):
            if x != rr and rows[x][c]:
                f = rows[x][c]
                rows[x] = [(rows[x][j] - f * rows[rr][j]) % p for j in range(m)]
        rr += 1
    return rr

def cert_centralizer(name, sub, amb, expected, members):
    ok_members = all(all(is_zero(comm(g, X)) for g in sub) for X in members)
    indep = members_rank_modp(members, 40127) == len(members)
    nulls = [centralizer_nullity_modp(sub, amb, p) for p in (40127, 40151)]
    ok = (ok_members and indep and all(n == expected for n in nulls)
          and len(members) == expected)
    check(name, ok, f"nullity mod p = {nulls}; {len(members)} exact commuting,"
                    f" independent members (lower bound meets upper => dim = {expected})")
    return ok

# The D3 stage: centralizer of the banked su(3)_c inside su(4) = so(6) is ONE u(1):
cert_centralizer("C(su3c, su4=so6)_dim_1_the_BL_line", su3, so6, 1, [BLgen])
# The D4 stage: centralizer of su(3)_c inside so(8) is u(1)^2 (B-L and the z4 phase):
cert_centralizer("C(su3c, so8)_dim_2", su3, so8, 2, [BLgen, Rz4])
check("C(su3c_so8)_is_ABELIAN", is_zero(comm(BLgen, Rz4)),
      "no su(2) fits: su(2)_L has NO home in so(8)+u(1)^2 above the banked su(3)_c")
# The nesting rungs themselves:
cert_centralizer("C(so6, so8)_dim_1", so6, so8, 1, [Rz4])
cert_centralizer("C(so8, so10)_dim_1", so8, so10, 1, [Rz5])
# The D5 stage hosts the SM: centralizer of su(3)_c in so(10) is dim 7 and contains su(2)_L:
cert_centralizer("C(su3c, so10)_dim_7_contains_su2L", su3, so10, 7,
                 [BLgen, Rz4, Rz5, rot10(3, 4), rot10(3, 9), rot10(8, 4), rot10(8, 9)])
# (basis: B-L + the so(4) on (x4,y4,x5,y5) which contains su(2)_L --
#  explicit membership of su2L is the certificate that matters:)
check("su2L_inside_C(su3c_so10)",
      all(all(is_zero(comm(g, X)) for g in su3) for X in su2L),
      "the D5 stage so(10)+u(1) is the FIRST rung that can hold the unbroken SM")

# --- the 27 traces (spinor 16 by weight combinatorics + vector 10 + singlet) ---
Y5 = [Fr(-2, 3)] * 3 + [Fr(1), Fr(1)]
T35 = [Fr(0)] * 3 + [Fr(1, 2), Fr(-1, 2)]
t3c5 = [Fr(1, 2), Fr(-1, 2), Fr(0), Fr(0), Fr(0)]     # canonical su(3) t3
spinor16 = [s for s in itertools.product((Fr(1, 2), Fr(-1, 2)), repeat=5)
            if math.prod(1 if q > 0 else -1 for q in s) == 1]
assert len(spinor16) == 16
def tr16(f): return sum(f(s) for s in spinor16)
def tr10(chg): return 2 * sum(c * c for c in chg)      # z_k and zbar_k
Ych = lambda s: sum(q * y for q, y in zip(s, Y5))
T3ch = lambda s: sum(q * t for q, t in zip(s, T35))
t3cch = lambda s: sum(q * t for q, t in zip(s, t3c5))
TrT3sq_27 = tr16(lambda s: T3ch(s) ** 2) + tr10(T35)
TrYhalfsq_27 = tr16(lambda s: (Ych(s) / 2) ** 2) + tr10([y / 2 for y in Y5])
TrT3Y_27 = tr16(lambda s: T3ch(s) * Ych(s)) + 0  # 10v: 2*sum(T35*Y5) added below
TrT3Y_27 += 2 * sum(a * b for a, b in zip(T35, Y5))
Trt3csq_27 = tr16(lambda s: t3cch(s) ** 2) + tr10(t3c5)
sin2W = TrT3sq_27 / (TrT3sq_27 + TrYhalfsq_27)
check("Tr27_T3sq_eq_3", TrT3sq_27 == 3, TrT3sq_27)
check("Tr27_YhalfSq_eq_5", TrYhalfsq_27 == 5, TrYhalfsq_27)
check("Tr27_T3Y_eq_0", TrT3Y_27 == 0)
check("sin2thetaW_MU_eq_3_8_banked_boundary", sin2W == Fr(3, 8), sin2W)
# GUT normalization factor derived: yhat = sqrt(3/5) Y/2 -> Tr27 yhat^2 = 3 = Tr27 T3^2:
check("GUT_norm_g1sq_eq_5_3_gprimesq_derived", Fr(3, 5) * TrYhalfsq_27 == TrT3sq_27)
# Embedding indices (ratio of same-rep traces of convention-normalized generators;
#  so(10) gens normalized to T(10)=1: h = H1/sqrt2 -> Tr27 h^2 = (16/4 + 2)/2 = 3):
Tr27_h2 = Fr(tr16(lambda s: s[0] ** 2) + 2, 2)
check("embedding_index_su3c_in_so10_eq_1", Trt3csq_27 == Tr27_h2,
      f"Tr27 t3c^2 = {Trt3csq_27} = Tr27 h_norm^2 = {Tr27_h2}")
check("embedding_index_su2L_in_so10_eq_1", TrT3sq_27 == Tr27_h2)
check("embedding_index_u1Y_GUT_in_so10_eq_1", Fr(3, 5) * TrYhalfsq_27 == Tr27_h2)
# su(3)_c in su(4): index computed on the 4 = spinor of so(6) (chirality +) --
# states (q1,q2,q3), q = +-1/2, product of signs +:
spinor4 = [s for s in itertools.product((Fr(1, 2), Fr(-1, 2)), repeat=3)
           if math.prod(1 if q > 0 else -1 for q in s) == 1]
Tr4_t3c = sum((s[0] / 2 - s[1] / 2) ** 2
              for s in spinor4)          # canonical su(3) t3 = diag(1/2,-1/2,0)
Tr4_BLraw = sum(sum(s) ** 2 for s in spinor4)     # raw B-L charge = q1+q2+q3
check("embedding_index_su3c_in_su4_eq_1_computed",
      Tr4_t3c == Fr(1, 2), f"Tr_4(t3^2) = {Tr4_t3c} = T(4) = 1/2 -> index 1;"
      f" B-L raw Tr_4 = {Tr4_BLraw} -> normalized t_BL has Tr_4 = 1/2: index 1"
      " (the D3-stage record; window closed below)")
# so(10) rep indices for the beta ladder (T(10)=1 units):
T16 = Fr(tr16(lambda s: s[0] ** 2), 2)          # = 2
T10 = Fr(tr10([1, 0, 0, 0, 0]), 2)              # = 1
adH1 = [comm(H[0], B) for B in so10]
# Tr_adj(H1_norm^2): sum over basis pairs -- use root counting: [H1,.] eigenvalues:
# count via mod-free exact: decompose ad(H1)^2 trace = sum_a <[H1,[H1,Ba]], Ba*>/<Ba,Ba*>
# with the rot-basis orthogonal under Tr(AB^T): Tr(A A^T) = 2 for each rot gen.
adsq = [comm(H[0], c) for c in adH1]
# hermitian generator = -i ad(H1); its square = -ad(H1)^2, so negate the real trace:
TrAdH1sq = -sum(Fr(sum(adsq[a][i][j] * so10[a][i][j] for i in range(10)
                       for j in range(10)), 2) for a in range(len(so10)))
C2G_so10 = Fr(TrAdH1sq, 2)                       # /2: h = H1/sqrt2 normalization
check("so10_indices_T16_2_T10_1_C2G_8", (T16, T10, C2G_so10) == (2, 1, 8),
      f"T(16)={T16}, T(10)={T10}, C2(adj)={C2G_so10}")
# X-charge pattern on the 27 forced by tracelessness + the two cubic couplings
# (16-16-10 and 10-10-1 in the E6 cubic): 2a+b=0, 2b+c=0, 16a+10b+c=0 -> (1,-2,4):
a_, b_, c_ = 1, -2, 4
check("X_pattern_1_m2_4_traceless_and_cubic_invariant",
      16 * a_ + 10 * b_ + 1 * c_ == 0 and 2 * a_ + b_ == 0 and 2 * b_ + c_ == 0)
TrX2raw = 16 * a_ ** 2 + 10 * b_ ** 2 + 1 * c_ ** 2      # = 72
xnorm2 = Fr(3, TrX2raw)                                   # X_N = X/(2 sqrt6)
check("X_GUT_normalization_TrX2_eq_3", xnorm2 * TrX2raw == 3, "X_N = X/(2*sqrt(6))")
# Y is so(10)-Cartan: Tr27(Y X) = a*Tr16(Y) + b*Tr10(Y) + c*0; the 10v trace of any
# Cartan direction vanishes by z/zbar conjugation; the 16 trace computed:
check("Tr27_YX_eq_0_Y_orthogonal_X", tr16(Ych) == 0,
      "Tr16(Y) = 0 (computed); Tr10(Y) = 0 (conjugation) => Tr27(YX) = 0")

# --- the beta-coefficient ladder (one-loop; zero freedom) ---
def b_one_loop(C2G, Tf_sum, Ts_sum):
    return Fr(-11, 3) * C2G + Fr(2, 3) * Tf_sum + Fr(1, 3) * Ts_sum
b_so10 = b_one_loop(8, 3 * (T16 + T10), (T16 + T10))          # 3 fermion 27s + scalar 27
b_X = b_one_loop(0, 3 * 3, 3)                                  # Tr27 X_N^2 = 3 per 27
b_so8 = b_one_loop(6, 3 * 3, 3)     # 27 -> 8v+8s+8c+3x1: T=1 each (record; window closed)
b_su4 = b_one_loop(4, 3 * 3, 3)     # 27 -> 6 + 2x(4+4bar) + 5x1: T = 1+4/2 = 3 (record)
check("beta_ladder_b_so10_m67_3__bX_7", (b_so10, b_X) == (Fr(-67, 3), 7),
      f"b_so10 = {b_so10}, b_X = {b_X}; closed-window records: b_so8 = {b_so8},"
      f" b_su4 = {b_su4}, each normalized u(1): 7")
R["algebra"] = {
 "chain_typings_used": "D3 = su(4)+u(1)^3 (18), D4 = so(8)+u(1)^2 (30), D5 = so(10)+u(1) (46) -- banked B909",
 "obstruction": "C(su3c, su4) = u(1)_{B-L} (dim 1); C(su3c, so8) = u(1)^2 abelian (dim 2)"
                " => no su(2)_L above M3 or M4: the D3/D4 windows are FORCED CLOSED"
                " (M3 = M4 = M5); first SM-compatible rung = D5 (C(su3c, so10) = 7, contains su(2)_L)",
 "Y_decomposition": "Y = -2/3(H1+H2+H3) + H4 + H5 in the so(10) Cartan; c_X = 0 exactly",
 "matching_at_M5": "index-1 chain: 1/alpha_i(M5) = 1/alpha_10(M5) for i = 1,2,3 (THREE conditions)",
 "embedding_indices": {"su3c_in_so10": 1, "su2L_in_so10": 1, "u1Y_GUT_in_so10": 1,
                       "su3c_in_su4": 1, "BL_in_su4_index": 1},
 "sin2thetaW_MU": "3/8 exact (Tr identities recomputed on the 27)",
 "beta_ladder_one_loop": {"SM": ["41/10", "-19/6", "-7"],
                          "so10_stage": {"b_so10": str(b_so10), "b_X": str(b_X)},
                          "closed_window_records": {"b_so8": str(b_so8),
                                                    "b_su4": str(b_su4),
                                                    "u1_normalized_each": "7"}},
 "branchings_27": {"D5": "16 + 10 + 1", "D4_record": "8v + 8s + 8c + 3x1",
                   "D3_record": "6 + 2x(4+4bar) + 5x1"},
}

# =====================================================================
# PART 0 -- THE CALIBRATION GATE: B915's two-loop desert curve, reproduced
# =====================================================================
print("\n== PART 0: B915 calibration gate ==")
MZ = 91.1876
INV_AEM = 127.951; S_INV_AEM = 0.009
SW2_EXP = 0.23122; S_SW2 = 0.00004
AS_EXP = 0.1180; S_AS = 0.0009
b1 = np.array([41 / 10, -19 / 6, -7.0])
B2 = np.array([[199 / 50, 27 / 10, 44 / 5],
               [9 / 10, 35 / 6, 12.0],
               [11 / 10, 9 / 2, -26.0]])

def run(alphas_mz, tmax, two_loop=True):
    def rhs(t, x):
        a = 1.0 / np.array(x)
        d = -b1 / (2 * math.pi)
        if two_loop: d = d - (B2 @ a) / (8 * math.pi ** 2)
        return d
    return solve_ivp(rhs, (0, tmax), list(1.0 / np.array(alphas_mz)),
                     rtol=1e-10, atol=1e-12, dense_output=True)

def alphas_from(sw2, als, inv_aem=INV_AEM):
    aem = 1.0 / inv_aem
    return [(5.0 / 3.0) * aem / (1.0 - sw2), aem / sw2, als]

def curve_point(MU, two_loop=True):
    t = math.log(MU / MZ)
    def f_sw(sw2):
        x = run(alphas_from(sw2, 0.118), t, two_loop).y[:, -1]
        return x[0] - x[1]
    sw2 = brentq(f_sw, 0.18, 0.30, xtol=1e-12)
    def f_as(als):
        x = run(alphas_from(sw2, als), t, two_loop).y[:, -1]
        return x[1] - x[2]
    als = brentq(f_as, 0.06, 0.30, xtol=1e-12)
    return sw2, als

MUs = np.logspace(np.log10(1e3), np.log10(1.22e19), 61)
C1 = []; C2c = []
for MU in MUs:
    try: C1.append(curve_point(MU, False))
    except Exception: C1.append((float("nan"),) * 2)
    try: C2c.append(curve_point(MU, True))
    except Exception: C2c.append((float("nan"),) * 2)
C1 = np.array(C1); C2c = np.array(C2c)
ds = []
for k in range(len(MUs)):
    if any(np.isnan(C2c[k])) or any(np.isnan(C1[k])): ds.append(np.inf); continue
    sth = np.abs(C2c[k] - C1[k])
    st_sw = math.sqrt(S_SW2 ** 2 + sth[0] ** 2)
    st_as = math.sqrt(S_AS ** 2 + sth[1] ** 2)
    ds.append(math.sqrt(((SW2_EXP - C2c[k][0]) / st_sw) ** 2 +
                        ((AS_EXP - C2c[k][1]) / st_as) ** 2))
kmin = int(np.argmin(ds)); dmin = float(ds[kmin])

def meet(i, j, two_loop=True):
    def g(t):
        x = run(alphas_from(SW2_EXP, AS_EXP), t, two_loop).y[:, -1]
        return x[i] - x[j]
    try: return MZ * math.exp(brentq(g, 1.0, math.log(1e22 / MZ), xtol=1e-9))
    except Exception: return None
M12_2, M13_2, M23_2 = meet(0, 1), meet(0, 2), meet(1, 2)
M12_1, M13_1, M23_1 = meet(0, 1, False), meet(0, 2, False), meet(1, 2, False)
BANKED = {"d": 15.97377227124076, "M12": 10873671676836.49,
          "M13": 171954461565153.3, "M23": 2.9140267474571724e16}
gate = (abs(dmin - BANKED["d"]) < 1e-6 * BANKED["d"] and
        abs(M12_2 - BANKED["M12"]) < 1e-6 * BANKED["M12"] and
        abs(M13_2 - BANKED["M13"]) < 1e-6 * BANKED["M13"] and
        abs(M23_2 - BANKED["M23"]) < 1e-6 * BANKED["M23"])
check("PART0_gate_B915_reproduced_d_and_triangle", gate,
      f"d_min = {dmin:.6f} (banked {BANKED['d']:.6f}); triangle 2-loop = "
      f"{M12_2:.4e}/{M13_2:.4e}/{M23_2:.4e}")
R["part0"] = {"d_min_sigma": dmin, "banked_d": BANKED["d"],
              "triangle_2loop_GeV": {"g1=g2": M12_2, "g1=g3": M13_2, "g2=g3": M23_2},
              "triangle_1loop_GeV": {"g1=g2": M12_1, "g1=g3": M13_1, "g2=g3": M23_1}}

# =====================================================================
# PART 1 -- THE REQUIRED SCALES (solve; the honest solution-set characterization)
# =====================================================================
print("\n== PART 1: the required (M3, M4, M5, MU) ==")
# (i) M3 = M4 = M5 FORCED (Part A: no su(2)_L in the D3/D4 stages): rho1 = rho2 = 1.
# (ii) M5: the composite matching is 1/alpha_1 = 1/alpha_2 = 1/alpha_3 at M5
#      (index-1 chain, c_X = 0): THREE conditions, ONE unknown -> over-determined.
#      Exact solution set: EMPTY (the banked B915 triangle: the three pairwise
#      meeting scales differ). Pairwise branches quantified below.
# (iii) MU: with Y inside so(10), the SM does not see the E6 rung: the unification
#      condition alpha_10(MU) = alpha_X(MU) is solvable for EVERY MU > M5 by the
#      free boundary alpha_X(M5) -- 1/alpha_X(M5) = 1/alpha_10(M5)
#      - (b10 - bX)/(2pi) ln(MU/M5) with b10 - bX = -88/3 < 0, so 1/alpha_X(M5) > 0
#      always: MU is UNCONSTRAINED. rho3 has NO required value.
def invalpha_at(scale, two_loop=True, sw2=SW2_EXP, als=AS_EXP, inv_aem=INV_AEM):
    t = math.log(scale / MZ)
    return run(alphas_from(sw2, als, inv_aem), t, two_loop).y[:, -1]

branches = {}
for tag, (i, j, k), M2L, M1L in [("g1=g2", (0, 1, 2), M12_2, M12_1),
                                 ("g1=g3", (0, 2, 1), M13_2, M13_1),
                                 ("g2=g3", (1, 2, 0), M23_2, M23_1)]:
    x2 = invalpha_at(M2L, True); x1 = invalpha_at(M1L, False)
    gap2 = x2[k] - x2[i]                      # third inverse-coupling mismatch, 2-loop
    gap1 = x1[k] - x1[i]
    s_th = abs(gap2 - gap1)
    # experimental sigma on the gap: propagate sw2 and alpha_s input errors (2-loop):
    d_sw = (invalpha_at(M2L, True, sw2=SW2_EXP + S_SW2)[k]
            - invalpha_at(M2L, True, sw2=SW2_EXP + S_SW2)[i]) - gap2
    d_as = (invalpha_at(M2L, True, als=AS_EXP + S_AS)[k]
            - invalpha_at(M2L, True, als=AS_EXP + S_AS)[i]) - gap2
    s_exp = math.sqrt(d_sw ** 2 + d_as ** 2)
    s_tot = math.sqrt(s_th ** 2 + s_exp ** 2)
    branches[tag] = {"M5_2loop_GeV": M2L, "M5_1loop_GeV": M1L,
                     "sigma_lnM5_th": abs(math.log(M2L / M1L)),
                     "third_coupling_gap_inv_alpha": gap2,
                     "gap_sigma_th": s_th, "gap_sigma_exp": s_exp,
                     "gap_distance_sigma": abs(gap2) / s_tot}
    print(f"branch {tag}: M5 = {M2L:.4e} GeV; third-coupling gap = {gap2:+.3f}"
          f" (1/alpha units) = {abs(gap2)/s_tot:.1f} sigma_tot")
check("M5_exact_solution_set_EMPTY",
      all(br["gap_distance_sigma"] > 3 for br in branches.values()),
      "every branch leaves the third coupling > 3 sigma away: no single M5 exists")
slope = float(Fr(-88, 3)) / (2 * math.pi)
R["part1"] = {
 "M3_M4": "FORCED equal to M5 (su(2)_L obstruction; Part A certificates): rho1 = rho2 = 1 exact",
 "M5_branches": branches,
 "M5_exact": "EMPTY (over-determined: 3 matching conditions, 1 unknown; the banked triangle)",
 "MU": {"status": "UNCONSTRAINED (under-determined)",
        "reason": "Y lies inside so(10) (c_X = 0): the E6 rung is invisible to the SM"
                  " matching; 1/alpha_X(M5) = 1/alpha_10(M5) + (88/3)/(2pi) ln(MU/M5) > 0"
                  " for all MU > M5 -- every MU in (M5, M_Pl] admits a solution",
        "d_invalphaX_dlnMU": -slope},
 "solution_set": "as posed: EMPTY at exact tier; near-solution structure = three pairwise"
                 " branches x (MU free): rho3 has NO required value",
}

# =====================================================================
# PART 2 -- THE SEALED MATCH
# =====================================================================
print("\n== PART 2: the sealed match ==")
mp.dps = 50
scales9 = {  # (a) the nine colorless scale ratios (banked B912/B914, ref atom S2 = 1)
 "S0": mpf("1.6803202716718931117598649584069485194926111536198"),
 "S1": mpf("19.142020743905498523723985498810106047939070995497"),
 "S2": mpf("1.0"),
 "A0": mpf("53.078638438636745051644351684315117196342743511944"),
 "A1": mpf("0.78626003406867602279393210822906931791997937914764"),
 "A2": mpf("3.0889357198937381812466251760330539656180351001646")}
colored = [mpf("1867.6882465382868116767089064696986"),
           mpf("702.46346123720135020146110813324478"),
           mpf("451.71617857652337422145995449875473")]
T_exact = mpf("4.775781328852112587377582312996804957776592668646e-32")
mu_roots = [mpf(x) for x in polyroots([500716339200, -2075673600, -4769856, 2197])]
ka_roots = [mpf(x) for x in polyroots([2771822592000, 3033676800, -56402640, -6859])]
lam = mpf(2304) / 953
menu = {}
for k, v in scales9.items(): menu[f"(a) scale {k}"] = v
menu["(b) colored r1/r2"] = colored[0] / colored[1]
menu["(b) colored r1/r3"] = colored[0] / colored[2]
menu["(b) colored r2/r3"] = colored[1] / colored[2]
menu["(c) sqrtT"] = T_exact ** mpf("0.5")
menu["(c) T"] = T_exact
for nm, roots in (("mu", mu_roots), ("kappa", ka_roots)):
    rr = sorted([abs(x) for x in roots], reverse=True)
    menu[f"(d) {nm} |r1/r2|"] = rr[0] / rr[1]
    menu[f"(d) {nm} |r1/r3|"] = rr[0] / rr[2]
    menu[f"(d) {nm} |r2/r3|"] = rr[1] / rr[2]
menu["(e) 13/19"] = mpf(13) / 19
menu["(e) 13^3/19^3"] = mpf(13 ** 3) / 19 ** 3
menu["(e) 953/2304"] = mpf(953) / 2304
menu["(e) N(d)=(953/2304)^2"] = (mpf(953) / 2304) ** 2
menu["(f) lambda"] = lam; menu["(f) lambda^2"] = lam ** 2; menu["(f) lambda^3"] = lam ** 3
menu["(f) lambda^-1"] = 1 / lam; menu["(f) lambda^-2"] = lam ** -2
menu["(f) lambda^-3"] = lam ** -3
menu["(f) 3!"] = mpf(6)
for n in (2, 3, 6, 27): menu[f"(f) {n}"] = mpf(n)
# reciprocals of the ratio-families recorded (orientation convention, pre-stated):
recip = {k + " (recip)": 1 / v for k, v in menu.items()
         if k.startswith(("(a)", "(b)", "(d)")) and v != 1}
menu_full = dict(menu); menu_full.update(recip)
R["menu"] = {k: mp.nstr(v, 20) for k, v in menu_full.items()}

def nearest(value, sigma_ln, topn=3):
    """distance of ln(value) to menu entries and 2-products, in sigma_ln units"""
    out = []
    items = list(menu_full.items())
    for k, v in items:
        out.append((abs(float(mp.log(value / v))), k))
    for (k1, v1), (k2, v2) in itertools.combinations_with_replacement(items, 2):
        out.append((abs(float(mp.log(value / (v1 * v2)))), k1 + " x " + k2))
    out.sort()
    return [{"entry": k, "abs_ln_distance": d,
             "distance_sigma": (d / sigma_ln if sigma_ln > 0 else float("inf"))}
            for d, k in out[:topn]]

# The required rho's:
rho1 = rho2 = 1.0   # forced exact (algebra); sigma = 0
one_products = [k for k, v in menu_full.items() if v == 1] + \
    [f"{k1} x {k2}" for (k1, v1), (k2, v2)
     in itertools.combinations_with_replacement(menu_full.items(), 2) if v1 * v2 == 1]
print("rho1 = rho2 = 1 (forced, degenerate rungs); exact menu products equal to 1:",
      one_products[:4], "...")
# rho3: NO required value (MU unconstrained) -> the sealed match cannot be satisfied
# non-vacuously: a menu match requires a REQUIRED value to match.
verdict = "OUTCOME B"
R["part2"] = {
 "rho1_required": "1 (exact, forced: M3 = M4)", "rho2_required": "1 (exact, forced: M4 = M5)",
 "rho1_rho2_menu_note": "products of two menu entries equal to 1 exist"
                        f" (e.g. {one_products[0]}; also (e) 953/2304 x (f) lambda):"
                        " formally inside the sealed <=2-product criterion, but they"
                        " certify DEGENERATE (absent) rungs, not object-owned scales",
 "rho3_required": "NONE -- M5 has no exact value (empty solution set) and MU is"
                  " unconstrained: the ladder does not DEMAND a third ratio",
 "MU_over_MPl": "unconstrained; recorded as the free interval (M5/M_Pl, 1], M_Pl = 1.22e19 GeV",
 "sealed_verdict": verdict,
}
# Transparency: near-misses for the DEFINED failure-geometry ratios (not required rho's):
trans = {}
for tag_pair in [("g1=g2", "g1=g3"), ("g1=g2", "g2=g3"), ("g1=g3", "g2=g3")]:
    a, b = tag_pair
    v = branches[a]["M5_2loop_GeV"] / branches[b]["M5_2loop_GeV"]
    s_ln = math.sqrt(branches[a]["sigma_lnM5_th"] ** 2 + branches[b]["sigma_lnM5_th"] ** 2)
    trans[f"triangle {a}/{b}"] = {"value": v, "sigma_ln": s_ln,
                                  "nearest": nearest(mpf(v), s_ln)}
for tag in branches:
    v = branches[tag]["M5_2loop_GeV"] / 1.22e19
    s_ln = branches[tag]["sigma_lnM5_th"]
    trans[f"{tag} / M_Pl"] = {"value": v, "sigma_ln": s_ln, "nearest": nearest(mpf(v), s_ln)}
R["transparency_near_misses"] = trans
for k, v in trans.items():
    n0 = v["nearest"][0]
    print(f"  {k}: {v['value']:.4e}; nearest menu object: {n0['entry']}"
          f" at {n0['distance_sigma']:.1f} sigma_ln")

print("\nSEALED VERDICT:", verdict,
      "-- the D-chain-with-banked-scales identification DIES;"
      " the banked deliverable is the required-scale table (part1).")
R["sealed_verdict"] = verdict
json.dump(R, open(os.path.join(HERE, "results.json"), "w"), indent=1, default=str)
print("results.json written")
