#!/usr/bin/env python3
"""B666 cell R2 -- the symbolic Latin-square proof of the E6 level-2 odd
hearing matrix (L88 revival).

TARGET (banked, B629 cell J / SEALED_INTERACTION_VALUES.md section 1):
with A_k = (2/sqrt7) sin(2 pi k/7) and zeta = e^{i pi/7} = zeta_14,

    B = [ A1 z^10   A2 z^6   A3 z^4 ]
        [ A2 z^2    A3 z^5   A1 z^3 ]
        [ A3 z^12   A1 z^1   A2 z^6 ]      (rows/cols: 27, 351', 351 pairs)

banked at 1e-100 numerics.  THIS CELL upgrades it to a zero-numerics
computer-assisted THEOREM over the cyclotomic field Q(zeta_252), derived
from the Kac-Peterson S/T closed forms:

  S_ab  propto  sum_{w in W(E6)} eps(w) e^{-2 pi i (w(la+rho), lb+rho)/14}
  T_a   =  e^{2 pi i (h_a - c/24)},  c = 2*dim(E6)/14 = 78/7.

PROOF ARCHITECTURE
  Lemma 1 (odd-space reduction):  B_ij = -t_i^2 t_j (S_{a_i a_j} - S_{a_i abar_j})
     from (i) exact theta-covariance of the KP sum, (ii) exact T-pair equality
     h_a = h_{theta a}, (iii) CU = -U (combinatorial).
  Tier A (the nine exact identities): each entry, three exact field facts:
     (A1) delta_ij purely imaginary, (A2) modulus law
     7 * delta*conj(delta) = N^2 (2 - z7^{2k} - z7^{-2k}) with the banked
     Latin index k(i,j), (A3) the phase ray: X_ij = -t_i^2 t_j delta_ij
     zeta_14^{-m(i,j)} is real (exact), positive (sign pinned numerically,
     legitimate: a nonzero real algebraic bounded away from 0).
  Lemma 2 (the GALOIS DERIVATION of the Latin square): the Galois action
     sigma_t : zeta_126 -> zeta_126^t equals, on the KP sum, the level-14
     affine-Weyl reduction of t*(lambda+rho) (verified EXACTLY as raw
     integer-array identities).  Consequence, applied to the modulus law:
        k(i, pi_t(j)) = +- t * k(i,j)  (mod 7)
     which with the seed k(1,1)=1 FORCES k(i,j) = +- m_i m_j mod 7 --
     the Latin square IS the multiplication table of Z_7^x / {+-1}.
  Lemma 3 (the zeta_14-exponent law): exact monomial identities
        zeta_14^{m(i,j)} = -i * s_ij * t_i^2 t_j
     with s_ij the sine-sign; integrality of m derived; compact forms searched.

Everything decisive is exact: integer Weyl-sum bincounts -> integer
coefficient vectors on zeta_252 powers -> zero-tests by exact reduction
mod Phi_252 (int arithmetic).  Floats appear ONLY to pin signs of nonzero
real algebraics (with stated margins) and for progress prints.
"""
import itertools, json, sys, time
from fractions import Fraction as F

import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 60
t0 = time.time()
LOG = []
def out(s=""):
    print(s, flush=True)
    LOG.append(str(s))

def stamp(msg):
    out(f"[{time.time()-t0:7.1f}s] {msg}")

CHECKS = []  # (name, passed_bool)
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    out(f"  GATE {'PASS' if ok else '*** FAIL ***'}: {name}")
    if not ok:
        out("  !!!! decisive check failed -- see above; continuing to gather the full picture")

# ================================================================
# PART 0 -- exact stage data (identical construction to B629/hp_hearing.py,
# lineage B570/c3_e6_level2_monodromy.py; KP closed forms)
# ================================================================
out("="*78)
out("PART 0 -- exact E6 level-2 stage data from the Kac-Peterson closed forms")
out("="*78)

C6 = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
      [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
KH = 14                      # kappa = k + h_vee = 2 + 12
C_int = np.array(C6, dtype=np.int64)
Cs = sp.Matrix(C6)
assert Cs.det() == 3
Cinv3 = np.array([[int(x) for x in row] for row in (3 * Cs.inv()).tolist()],
                 dtype=np.int64)

PRIM = [(0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1),
        (2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 2), (1, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 1, 0)]
NAMES = ['1', '27', '27b', "351'", "351'b", '650', '78', '351', '351b']
theta = lambda w: (w[5], w[1], w[4], w[3], w[2], w[0])
TH = [PRIM.index(theta(p)) for p in PRIM]          # the conjugation permutation
out(f"theta permutation on primaries: {TH}")

ones6 = np.ones(6, dtype=np.int64)
shifted3 = [Cinv3 @ (np.array(p, dtype=np.int64) + ones6) for p in PRIM]  # 3(la+rho) root coords
lam3 = [Cinv3 @ np.array(p, dtype=np.int64) for p in PRIM]                # 3 la

# ---- W(E6), exact integer matrices ----
def weyl_group():
    n = 6
    gens = []
    for j in range(n):
        M = np.eye(n, dtype=np.int64)
        M[j, :] -= C_int[:, j]
        gens.append(M)
    I = np.eye(n, dtype=np.int64)
    seen = {I.tobytes(): 1}
    frontier = [(I, 1)]
    mats, signs = [I], [1]
    while frontier:
        new = []
        for M, s in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen[key] = -s
                    new.append((Mg, -s))
                    mats.append(Mg)
                    signs.append(-s)
        frontier = new
    return np.array(mats), np.array(signs, dtype=np.int64)

W, eps_signs = weyl_group()
assert len(W) == 51840
stamp(f"W(E6) built exactly: {len(W)} elements")

# ---- unnormalized KP numerators D_ab as EXACT integer coefficient arrays ----
# D_ab = sum_w eps(w) e^{-2 pi i (w(la+rho),(lb+rho))/14}
#      = sum_r c_ab[r] * e^{-2 pi i r/126},   c_ab integer (9*(...) trick)
MOD = 126
Cb3 = [C_int @ s for s in shifted3]
Wl3 = np.einsum('wij,lj->wli', W, np.array(shifted3))     # exact int64

Draw = [[None]*9 for _ in range(9)]
for a in range(9):
    for b in range(a, 9):
        ips9 = Wl3[:, a, :] @ Cb3[b]                       # = 9*(w(la+rho), lb+rho), exact
        pos = np.mod(ips9, MOD)
        cpos = np.bincount(pos[eps_signs == 1], minlength=MOD).astype(np.int64)
        cneg = np.bincount(pos[eps_signs == -1], minlength=MOD).astype(np.int64)
        Draw[a][b] = cpos - cneg                           # pure integers
        Draw[b][a] = Draw[a][b]                            # raw symmetry (w -> w^{-1})
stamp("D (unnormalized KP S) built as exact integer 126-arrays, all 45 pairs")

# raw-symmetry independent check on one asymmetric-looking pair
ips9_ba = Wl3[:, 7, :] @ Cb3[1]
pos = np.mod(ips9_ba, MOD)
c_ba = (np.bincount(pos[eps_signs == 1], minlength=MOD)
        - np.bincount(pos[eps_signs == -1], minlength=MOD)).astype(np.int64)
gate("raw S-symmetry D_{351,27} == D_{27,351} (independent bincount)",
     np.array_equal(c_ba, Draw[1][7]))

# ================================================================
# the exact cyclotomic workbench:  Z[zeta_252], integer vectors length 252
# convention: element = v with value sum_e v[e] * zeta_252^e, zeta_252 = e^{2 pi i/252}
# D_ab: e^{-2 pi i r/126} = zeta_252^{-2r}
# ================================================================
NF = 252
x = sp.symbols('x')
PHI = sp.Poly(sp.cyclotomic_poly(NF, x), x)
PHIdeg = PHI.degree()
assert PHIdeg == 72
phi_coeffs = [int(c) for c in PHI.all_coeffs()]           # degree..0
assert phi_coeffs[0] == 1
PHI_LOW = phi_coeffs[::-1]                                # index j = coeff of x^j, j=0..72

def red(v):
    """exact reduction of an integer (or Fraction) 252-vector mod Phi_252 ->
    canonical length-72 list; python ints/Fractions, no overflow."""
    c = [int(t) if isinstance(t, (int, np.integer)) else t for t in v]
    c = list(c) + [0]*(NF - len(c)) if len(c) < NF else list(c)
    for d in range(NF - 1, PHIdeg - 1, -1):
        cd = c[d]
        if cd:
            c[d] = 0
            base = d - PHIdeg
            for j in range(PHIdeg):
                pj = PHI_LOW[j]
                if pj:
                    c[base + j] -= cd * pj
    return c[:PHIdeg]

def iszero(v):
    return all(t == 0 for t in red(v))

def vec_from_c126(c):
    """D-array (126 ints, coeff of e^{-2 pi i r/126}) -> 252-vector."""
    v = [0]*NF
    for r in range(MOD):
        if c[r]:
            v[(-2*r) % NF] += int(c[r])
    return v

def fconj(v):
    w = [0]*NF
    for e in range(NF):
        if v[e]:
            w[(-e) % NF] += v[e]
    return w

def fmul(a, b):
    """exact product via int64 convolution (bounds checked) with mod-252 fold."""
    aa = np.array(a, dtype=np.int64); bb = np.array(b, dtype=np.int64)
    # overflow guard: max |conv coeff| <= 252 * max|a| * max|b|
    bound = 252 * int(np.abs(aa).max() or 0) * int(np.abs(bb).max() or 0)
    assert bound < 2**62, "int64 overflow risk"
    conv = np.convolve(aa, bb)
    w = [0]*NF
    for e in range(len(conv)):
        if conv[e]:
            w[e % NF] += int(conv[e])
    return w

def fadd(a, b): return [p + q for p, q in zip(a, b)]
def fsub(a, b): return [p - q for p, q in zip(a, b)]
def fscale(a, s): return [s*p for p in a]
def fmono(e, c=1):
    v = [0]*NF; v[e % NF] = c; return v
def fshift(v, e):
    """multiply by zeta_252^e"""
    w = [0]*NF
    for k in range(NF):
        if v[k]:
            w[(k + e) % NF] += v[k]
    return w

ROOTS60 = [mp.e**(2j*mp.pi()*e/NF) for e in range(NF)]
def feval(v):
    return sum(int(v[e])*ROOTS60[e] for e in range(NF) if v[e])

D = [[vec_from_c126(Draw[a][b]) for b in range(9)] for a in range(9)]

# ---- T data: exact fractions ----
rho_w3 = Cinv3 @ ones6
hs = []
for i, p in enumerate(PRIM):
    y3 = shifted3[i] + rho_w3
    num = int(lam3[i] @ (C_int @ y3))       # 9 * (la, la+2rho)
    hs.append(F(num, 9*2*KH))
cc = F(2*78, KH)                            # central charge 78/7
c24 = cc/24
hhat = [h - c24 for h in hs]                # T_a = e^{2 pi i hhat_a}
eT = []
ok252 = True
for j, hh in enumerate(hhat):
    e = hh*252
    ok252 &= (e.denominator == 1)
    eT.append(int(e) % NF if e.denominator == 1 else None)
out("conformal weights h_a and T-exponents (exact):")
for j in range(9):
    out(f"  {NAMES[j]:>6}: h = {hs[j]}   hhat = h - c/24 = {hhat[j]}   252*hhat = {hhat[j]*252}")
gate("T-integrality: 252*(h_a - c/24) integral for all 9 primaries", ok252)

# ================================================================
# PART 1 -- Lemma 1 (the odd-space reduction), each ingredient EXACT
# ================================================================
out("")
out("="*78)
out("PART 1 -- Lemma 1: B_ij = -t_i^2 t_j (S_{a_i a_j} - S_{a_i abar_j})")
out("="*78)

# (i) theta-covariance of the KP sum (raw integer-array identities)
ok_cov = all(np.array_equal(Draw[TH[a]][TH[b]], Draw[a][b]) for a in range(9) for b in range(9))
gate("theta-covariance  D_{theta a, theta b} == D_{a b}  (all 81, raw)", ok_cov)

def conj_c126(c):
    w = np.zeros(MOD, dtype=np.int64)
    for r in range(MOD):
        if c[r]:
            w[(-r) % MOD] += c[r]
    return w
ok_conj = all(np.array_equal(conj_c126(Draw[a][b]), Draw[a][TH[b]])
              for a in range(9) for b in range(9))
gate("conjugation law  conj(D_{a b}) == D_{a, theta b}  (all 81, raw)", ok_conj)

# (ii) T-pair equality on the three odd pairs
PAIRS = [(1, 2, '27'), (3, 4, "351'"), (7, 8, '351')]
okT = all(hs[a] == hs[b] for a, b, _ in PAIRS)
gate("T-pair equality  h_a == h_{theta a} on the three odd pairs (exact fractions)", okT)
out(f"  pair T-exponents e_j = 252*hhat: {[ (nm, eT[a]) for a,b,nm in PAIRS ]}")

# (iii) N^2 rationality + the S^2 = N^2 * C_theta identity (exact)
N2vec = [0]*NF
for b in range(9):
    N2vec = fadd(N2vec, fmul(D[0][b], fconj(D[0][b])))
N2red = red(N2vec)
okrat = all(t == 0 for t in N2red[1:])
N2 = N2red[0]
gate("N^2 := sum_b |D_{0b}|^2 is RATIONAL (Phi_252-reduction to a constant)", okrat)
out(f"  N^2 = {N2}  (so N = sqrt({N2}) = {mp.nstr(mp.sqrt(N2), 20)})")
gate("N^2 == 3 * 14^6 exactly (KP volume: kappa^rank * det(Cartan)); N = 14^3 sqrt3",
     N2 == 3 * 14**6)

# D * conj(D)^T = N^2 I  -- exact unitarity of normalized S
stamp("checking exact unitarity D Ddag = N^2 I (45 entries) ...")
ok_uni = True
for a in range(9):
    for b in range(a, 9):
        acc = [0]*NF
        for k in range(9):
            acc = fadd(acc, fmul(D[a][k], fconj(D[b][k])))
        tgt = fmono(0, N2) if a == b else [0]*NF
        ok_uni &= iszero(fsub(acc, tgt))
gate("EXACT unitarity: D conj(D)^T == N^2 * I  (all 45 independent entries)", ok_uni)

# D*D = N^2 * C_theta (the construction's Cm is intrinsic)
stamp("checking exact S^2 = C_theta (45 entries) ...")
ok_c = True
for a in range(9):
    for b in range(a, 9):
        acc = [0]*NF
        for k in range(9):
            acc = fadd(acc, fmul(D[a][k], D[k][b]))
        tgt = fmono(0, N2) if b == TH[a] else [0]*NF
        ok_c &= iszero(fsub(acc, tgt))
gate("EXACT  D*D == N^2 * C_theta  (the weld's Cm = S^2 is the theta permutation)", ok_c)

out("""
LEMMA 1 (proved): with C = C_theta the pair-swap permutation and U the
antisymmetric pair basis u_j = (e_{a_j} - e_{abar_j})/sqrt2, CU = -U holds
combinatorially (C swaps the two members of each pair, u_j is antisymmetric);
[T diag equal on pairs] and [theta-covariance + conjugation law] give
  (U^T S U)_ij = (1/2)(S_{a a'} - S_{a abar'} - S_{abar a'} + S_{abar abar'})
              = S_{a_i a_j} - S_{a_i abar_j}
hence  B = U^T C (T^2 S T) U = -U^T T^2 S T U,
  B_ij = -t_i^2 t_j (S_{a_i a_j} - S_{a_i abar_j}) = -t_i^2 t_j delta_ij / N.
""")

# ================================================================
# PART 2 -- TIER A: the nine exact entry identities
# ================================================================
out("="*78)
out("PART 2 -- TIER A: the nine entries as exact Q(zeta_252) identities")
out("="*78)

# banked target tables (SEALED_INTERACTION_VALUES.md section 1)
Kt = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]     # A-index Latin square
Mt = [[10, 6, 4], [2, 5, 3], [12, 1, 6]]   # zeta_14 exponents

# sign of the overall normalization (hp convention: S_00 > 0)
D00num = feval(D[0][0])
s0 = 1 if D00num.real > 0 else -1
out(f"D_00 numeric = {mp.nstr(D00num, 15)}  ->  s0 = {s0} (S_00>0 convention)")

Aidx = [1, 3, 7]           # odd letters 27, 351', 351
Abar = [2, 4, 8]
Ssign = [[0]*3 for _ in range(3)]      # s'_ij: delta_ij = s' * i * |...| * s0-side
Xnum = [[None]*3 for _ in range(3)]
allA1 = allA2 = allA3r = allA3s = True
for i in range(3):
    for j in range(3):
        a, abar = Aidx[i], Abar[i]
        bA, bB = Aidx[j], Abar[j]
        delta = fsub(D[a][bA], D[a][bB])
        # (A1) purely imaginary
        okA1 = iszero(fadd(delta, fconj(delta)))
        allA1 &= okA1
        # (A2) modulus law: 7*delta*conj(delta) == N^2 * (2 - z7^{2k} - z7^{-2k})
        k = Kt[i][j]
        rhs = fadd(fmono(0, 2*N2),
                   fadd(fmono((36*2*k) % NF, -N2), fmono((-36*2*k) % NF, -N2)))
        okA2 = iszero(fsub(fscale(fmul(delta, fconj(delta)), 7), rhs))
        allA2 &= okA2
        # (A3) phase ray: X = -t_i^2 t_j delta zeta14^{-m}  real, sign = s0
        m = Mt[i][j]
        esh = (126 + 2*eT[a] + eT[bA] - 18*m) % NF      # -1 = zeta_252^126
        Xv = fshift(delta, esh)
        okA3r = iszero(fsub(Xv, fconj(Xv)))
        allA3r &= okA3r
        Xn = feval(Xv)
        Xnum[i][j] = Xn
        okA3s = (s0 * Xn.real > 0) and abs(Xn.imag) < mp.mpf('1e-30')
        allA3s &= okA3s
        # the sine sign s'_ij: delta/N = 2i * Im S; s' = sign(Im S)*s0-free:
        dn = feval(delta)
        Ssign[i][j] = 1 if (dn.imag * s0) > 0 else -1
        out(f"  entry ({NAMES[a]:>5},{NAMES[bA]:>5}): k={k} m={m:>2}  "
            f"A1 imag-pure:{'ok' if okA1 else 'FAIL'}  A2 modulus:{'ok' if okA2 else 'FAIL'}  "
            f"A3 real-ray:{'ok' if okA3r else 'FAIL'}  sign s0*X={mp.nstr(s0*Xn.real, 8)} "
            f"(margin vs 0: exact |X|=N*A_k={mp.nstr(mp.sqrt(N2)*2/mp.sqrt(7)*mp.sin(2*mp.pi()*k/7), 8)})")
gate("(A1) all nine delta_ij purely imaginary (exact)", allA1)
gate("(A2) all nine modulus laws 7|delta|^2 = N^2(2 - z7^{2k} - z7^{-2k}) (exact)", allA2)
gate("(A3) all nine phase rays real (exact) ...", allA3r)
gate("(A3) ... and positive (signs pinned, margins ~ N*A_k >> 1e-30)", allA3s)

# the SHARPENED closed form of the unnormalized odd differences:
#   delta_ij = 392 * s0 * s'_ij * sqrt21 * beta_{k(i,j)},   beta_k = z7^k - z7^{-k},
# with sqrt21 = -(z3 - z3^2) g7  (both in the field), 392 = 2^3 7^2 = N sqrt7 / 7.
g7v = [0]*NF
for n in range(7):
    g7v[(36*(n*n)) % NF] += 1
sqrt21 = fscale(fmul(fsub(fmono(84), fmono(168)), g7v), -1)
ok_sharp = True
for i in range(3):
    for j in range(3):
        delta = fsub(D[Aidx[i]][Aidx[j]], D[Aidx[i]][Abar[j]])
        k = Kt[i][j]
        beta = fsub(fmono(36*k), fmono((-36*k) % NF))
        rhs = fscale(fmul(sqrt21, beta), 392*s0*Ssign[i][j])
        ok_sharp &= iszero(fsub(delta, rhs))
gate("SHARPENED closed form delta_ij == 392 s0 s'_ij sqrt21 beta_k (exact, all nine)", ok_sharp)

out("""
TIER A (proved): every X_ij is a real algebraic with X_ij^2 = N^2 A_k^2
exactly (A2+A3-real) and s0*X_ij > 0 (sign pinned; the number is +-N*A_k
with N*A_k >= sqrt(N^2)*A_3 -- a fixed nonzero algebraic -- so a 60-dps
evaluation with residual < 1e-30 is decisive).  Hence
    B_ij = -t_i^2 t_j delta_ij/(s0 N) = A_{k(i,j)} zeta_14^{m(i,j)}
EXACTLY, with the banked k- and m-tables.  The 1e-100 numeric fact is now a
theorem of the E6 level-2 Kac-Peterson data.""")

# ================================================================
# PART 3 -- the LAWS (derivation, not observation)
# ================================================================
out("="*78)
out("PART 3 -- Lemma 2: the Galois derivation of the Latin-square index law")
out("="*78)

# ---- exact level-14 affine-Weyl alcove reduction ----
nTH = np.array((0, 1, 0, 0, 0, 0), dtype=np.int64)   # highest root in n-coords (=78's labels)
marks3 = Cinv3 @ nTH
assert np.all(marks3 % 3 == 0)
marks = marks3 // 3                                   # root coords of theta (the marks)
out(f"marks (root coords of the highest root): {marks.tolist()}  sum={int(marks.sum())} (h-1=11)")
assert int(marks.sum()) == 11

def alcove_reduce(nvec):
    """reduce an integer weight (n-coords) into the level-14 fundamental alcove
    under the affine Weyl group; return (n_final, sign) or (None, 0) on a wall."""
    v = np.array(nvec, dtype=np.int64).copy()
    sgn = 1
    for _ in range(100000):
        neg = np.where(v < 0)[0]
        if len(neg) > 0:
            i = int(neg[0])
            if v[i] == 0:
                return None, 0
            v = v - v[i]*C_int[:, i]
            sgn = -sgn
            continue
        if np.any(v == 0):
            return None, 0
        L = int(v @ marks)
        if L < KH:
            return v, sgn
        if L == KH:
            return None, 0
        v = v - (L - KH)*nTH
        sgn = -sgn
    raise RuntimeError("alcove reduction did not terminate")

SH_N = [np.array(p, dtype=np.int64) + 1 for p in PRIM]   # shifted weights, n-coords
key2idx = {tuple(v.tolist()): i for i, v in enumerate(SH_N)}

# sanity: each shifted weight is already reduced
ok = all(alcove_reduce(SH_N[b])[0] is not None and
         tuple(alcove_reduce(SH_N[b])[0].tolist()) == tuple(SH_N[b].tolist()) and
         alcove_reduce(SH_N[b])[1] == 1 for b in range(9))
gate("alcove sanity: the 9 shifted weights are alcove-reduced fixed points", ok)

# the six Galois classes t == 1 mod 18, t == u mod 7
import math
TS = {}
for u in range(1, 7):
    t = next(t for t in range(1, 127) if math.gcd(t, 126) == 1
             and t % 18 == 1 and t % 7 == u)
    TS[u] = t
out(f"Galois representatives t (t=1 mod 18, t=u mod 7): {TS}")

PI = {}; EPS = {}
for u, t in TS.items():
    perm = []; sign = []
    for b in range(9):
        vf, s = alcove_reduce(t*SH_N[b])
        assert vf is not None, f"wall hit at t={t}, b={b} (would force D=0)"
        perm.append(key2idx[tuple(vf.tolist())])
        sign.append(s)
    PI[u] = perm; EPS[u] = sign
    out(f"  t={t:>3} (u={u}): pi_t = {perm}   eps_t = {sign}")

# ---- EXACT covariance: sigma_t(D_ab) == eps_t(b) * D_{a, pi_t(b)} ----
stamp("verifying exact Galois covariance on all 81 entries x 6 classes (raw arrays)")
ok_gal = True
for u, t in TS.items():
    for a in range(9):
        for b in range(9):
            c = Draw[a][b]
            cp = np.zeros(MOD, dtype=np.int64)
            for r in range(MOD):
                if c[r]:
                    cp[(t*r) % MOD] += c[r]      # sigma_t on e^{-2 pi i r/126}
            ok_gal &= np.array_equal(cp, EPS[u][b]*Draw[a][PI[u][b]])
gate("EXACT Galois covariance sigma_t(D_ab) == eps_t(b) D_{a,pi_t(b)} (81x6, raw)", ok_gal)

# pair structure: pi_t maps odd pairs to odd pairs coherently
pair_of = {1: 0, 2: 0, 3: 1, 4: 1, 7: 2, 8: 2}
ok_pair = True
PPERM = {}
for u in TS:
    pp = []
    for j, (a, b, _) in enumerate(PAIRS):
        pa, pb = PI[u][a], PI[u][b]
        ok_pair &= (pa in pair_of and pb in pair_of and pair_of[pa] == pair_of[pb])
        pp.append(pair_of[pa])
    PPERM[u] = pp
    out(f"  u={u}: induced pair permutation {pp}"
        f"   (pair members {'preserved' if all(PI[u][a] in (Aidx[pp[j]],Abar[pp[j]]) for j,(a,_,_) in enumerate(PAIRS)) else '?'})")
gate("pi_t maps theta-odd pairs to theta-odd pairs (all six classes)", ok_pair)

# ---- the labels: orbit coordinates of the 27-pair ----
labels = [None]*3
for u in TS:
    tgt = PPERM[u][0]                # image of the 27-pair
    cls = min(u % 7, (-u) % 7)       # class of +-u in {1,2,3}
    if labels[tgt] is None:
        labels[tgt] = cls
    else:
        assert labels[tgt] == cls, "label clash"
out(f"labels m_j from the Galois orbit of the 27-pair: {labels}  (pairs 27, 351', 351)")
gate("orbit labels m = (1,2,3) for (27, 351', 351) -- transitive Galois orbit",
     labels == [1, 2, 3] and sorted(set(labels)) == [1, 2, 3])

# ---- the multiplicative index law (DERIVED consequence, verified) ----
def cls7(z):
    z = z % 7
    return min(z, 7 - z)
ok_mult = True
for u in TS:
    for i in range(3):
        for j in range(3):
            ok_mult &= (Kt[i][PPERM[u][j]] == cls7(u*Kt[i][j]))
gate("index law k(i, pi_t(j)) == +-t*k(i,j) mod 7  (all t, all entries)", ok_mult)
ok_latin = all(Kt[i][j] == cls7(labels[i]*labels[j]) for i in range(3) for j in range(3))
gate("THE LATIN-SQUARE LAW  k(i,j) == +- m_i m_j (mod 7), m=(1,2,3)", ok_latin)

out("""
LEMMA 2 (the derivation).  sigma_t fixes N^2 (rational) and maps the exact
modulus identity  7|delta_ij|^2 = N^2(2 - z7^{2k(i,j)} - z7^{-2k(i,j)})  to
the same identity at (i, pi_t(j)) with z7^{2k} -> z7^{2tk}: therefore
    k(i, pi_t(j)) = +- t k(i,j)  (mod 7)   [verified exactly above].
The 27-pair's Galois orbit is transitive over the three odd pairs, with
orbit coordinate m_j = class(+-t) in {1,2,3}; the seed entry k(27,27)=1
then FORCES  k(i,j) = +- m_i m_j (mod 7): the banked Latin square
[[1,2,3],[2,3,1],[3,1,2]] IS the multiplication table of Z_7^x/{+-1},
with the three theta-odd pairs as the group elements.  Each row/column is
a bijection => Latin, and |B_ij|^2 doubly-stochastic circulant follows.""")

# ================================================================
# Lemma 3 -- the zeta_14-exponent law
# ================================================================
out("="*78)
out("PART 3b -- Lemma 3: the zeta_14-exponent law")
out("="*78)

# exact monomial identity: zeta_14^m = -i * s'_ij * t_i^2 t_j
ok_expo = True
for i in range(3):
    for j in range(3):
        a, bA = Aidx[i], Aidx[j]
        s = Ssign[i][j]
        # -i*s = zeta_252^{189} if s=+1 else zeta_252^{63}
        lhs = (18*Mt[i][j]) % NF
        rhs = ((189 if s == 1 else 63) + 2*eT[a] + eT[bA]) % NF
        ok_expo &= (lhs == rhs)
gate("EXACT exponent identities zeta_14^m == -i s'_ij t_i^2 t_j (all nine)", ok_expo)
out(f"  sine-sign table s'_ij (sign of Im S_(a_i a_j)): {Ssign}")

# integrality/law statement
out("")
out("the assembled exponent law (exact):")
out("  m(i,j) = [ 189 - 63*(1 - s'_ij) + 2*e_i + e_j ] / 18   (mod 14),")
out(f"  with e = 252*(h - c/24) on the pair letters: e_27={eT[1]}, e_351'={eT[3]}, e_351={eT[7]}")
for i in range(3):
    for j in range(3):
        s = Ssign[i][j]
        val = (189 if s == 1 else 63) + 2*eT[Aidx[i]] + eT[Aidx[j]]
        assert val % 18 == 0 or ((val - 18*Mt[i][j]) % NF == 0)
out("  (integrality: 189/63 + 2e_i + e_j == 18*m mod 252 verified above)")

# the s'-cocycle under Galois (completes 'every entry from the seed').
# DERIVATION: delta_ij = 392 s0 s'_ij sqrt21 beta_k (proved exactly above), so
#   sigma_t(delta_ij) = 392 s0 s'_ij (t|7) sqrt21 beta_{tk}
#     [sigma_t fixes z3 (t=1 mod 18) and sends g7 -> (t|7) g7, beta_k -> beta_{tk};
#      beta_{tk} = sgn7(tk) beta_{class(tk)},  sgn7(x) = +1 if x mod 7 in {1,2,3}]
# while covariance gives sigma_t(delta_ij) = eps_t(a_j) o_t(j) delta_{i,pi_t(j)}
# with o_t(j) = +1 if pi_t preserves the pair orientation (a->a), -1 if it swaps.
# Equating:  s'(i,pi_t(j)) = eps_t(a_j) o_t(j) (t|7) sgn7(t k(i,j)) s'(i,j).
out("")
out("s'-cocycle under sigma_t (DERIVED from the sharpened closed form + covariance):")
# eps equal on both pair members (needed to factor the covariance through pairs)
ok_epair = all(EPS[u][a] == EPS[u][b] for u in TS for a, b, _ in PAIRS)
gate("eps_t equal on the two members of each odd pair (all six classes)", ok_epair)
def legendre7(t):
    return 1 if (t % 7) in (1, 2, 4) else -1
def sgn7(z):
    return 1 if (z % 7) in (1, 2, 3) else -1
ORI = {}
for u in TS:
    ORI[u] = [1 if PI[u][Aidx[j]] == Aidx[PPERM[u][j]] else -1 for j in range(3)]
out(f"  orientation factors o_t(j): { {TS[u]: ORI[u] for u in TS} }")
ok_scoc = True
for u, t in TS.items():
    for i in range(3):
        for j in range(3):
            jp = PPERM[u][j]
            k = Kt[i][j]
            pred = (Ssign[i][j] * EPS[u][Aidx[j]] * ORI[u][j]
                    * legendre7(t) * sgn7(t*k))
            ok_scoc &= (Ssign[i][jp] == pred)
gate("s'-cocycle: s'(i,pi_t(j)) == eps_t(j) o_t(j) (t|7) sgn7(tk) s'(i,j) (all 54)", ok_scoc)

# compact-form search: m(i,j) =? alpha*mu_i*mu_j + beta (mod 14)
out("")
found = []
cands = {0: [1, 13, 8, 6], 1: [2, 12, 9, 5], 2: [3, 11, 10, 4]}  # +-m, +-m+7 mod 14
for mu1 in cands[0]:
    for mu2 in cands[1]:
        for mu3 in cands[2]:
            mus = [mu1, mu2, mu3]
            for al in range(14):
                for be in range(14):
                    if all((al*mus[i]*mus[j] + be - Mt[i][j]) % 14 == 0
                           for i in range(3) for j in range(3)):
                        found.append((al, be, tuple(mus)))
if found:
    out(f"compact multiplicative form FOUND: m(i,j) == a*mu_i*mu_j + b (mod 14) for {found}")
else:
    out("no symmetric compact form m == a*mu_i*mu_j + b (mod 14) exists "
        "(consistent: the m-table is NOT symmetric, m(2,3)=3 vs m(3,2)=1, "
        "while a*mu_i*mu_j is); the exponent law is the assembled affine law above")
# asymmetric compact search: m(i,j) == a*mu_i*mu_j + c*mu_i + d*mu_j + b, mu=labels
found2 = []
for mu1 in cands[0]:
    for mu2 in cands[1]:
        for mu3 in cands[2]:
            mus = [mu1, mu2, mu3]
            for al in range(14):
                for cc_ in range(14):
                    for dd in range(14):
                        for be in range(14):
                            if all((al*mus[i]*mus[j] + cc_*mus[i] + dd*mus[j] + be
                                    - Mt[i][j]) % 14 == 0 for i in range(3) for j in range(3)):
                                found2.append((al, cc_, dd, be, tuple(mus)))
if found2:
    out(f"compact affine-multiplicative form(s) FOUND: m == a mu_i mu_j + c mu_i + d mu_j + b: {found2[:6]}"
        + (f" ... ({len(found2)} total)" if len(found2) > 6 else ""))
else:
    out("no affine-multiplicative compact form in the labels exists mod 14; "
        "the T-assembled law is the exponent law")

# ================================================================
# PART 4 -- corollaries from the PROVEN closed form, all exact in-field
# ================================================================
out("")
out("="*78)
out("PART 4 -- corollaries of the proven closed form (exact in Q(zeta_252))")
out("="*78)

# build 7*B exactly: 7*A_k zeta^m = -g7 (z7^k - z7^{-k}) zeta14^m,  g7 = sum z7^{n^2} = i sqrt7
g7 = [0]*NF
for n in range(7):
    g7[(36*(n*n)) % NF] += 1
# check g7^2 = -7
gate("Gauss sum: g7^2 == -7 (exact)", iszero(fsub(fmul(g7, g7), fmono(0, -7))))

B7 = [[None]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        k, m = Kt[i][j], Mt[i][j]
        sk = fsub(fmono(36*k), fmono((-36*k) % NF))     # z7^k - z7^{-k}
        B7[i][j] = fshift(fscale(fmul(g7, sk), -1), 18*m)

# trace = -1  (x7)
tr = fadd(fadd(B7[0][0], B7[1][1]), B7[2][2])
gate("corollary: trace(B) == -1 (exact: tr(7B) + 7 == 0)", iszero(fadd(tr, fmono(0, 7))))

# unitarity of B from the closed form
okU = True
for i in range(3):
    for j in range(i, 3):
        acc = [0]*NF
        for k in range(3):
            acc = fadd(acc, fmul(B7[i][k], fconj(B7[j][k])))
        tgt = fmono(0, 49) if i == j else [0]*NF
        okU &= iszero(fsub(acc, tgt))
gate("corollary: B unitary (exact, from the closed form)", okU)

# charpoly (x+1)(x^2+1): e1=-1, e2=1, e3=-1
e2acc = [0]*NF
for (p, q) in [(0, 1), (0, 2), (1, 2)]:
    e2acc = fadd(e2acc, fsub(fmul(B7[p][p], B7[q][q]), fmul(B7[p][q], B7[q][p])))
gate("corollary: e2(B) == +1 (exact)", iszero(fsub(e2acc, fmono(0, 49))))
det = [0]*NF
det = fadd(det, fmul(B7[0][0], fsub(fmul(B7[1][1], B7[2][2]), fmul(B7[1][2], B7[2][1]))))
det = fsub(det, fmul(B7[0][1], fsub(fmul(B7[1][0], B7[2][2]), fmul(B7[1][2], B7[2][0]))))
det = fadd(det, fmul(B7[0][2], fsub(fmul(B7[1][0], B7[2][1]), fmul(B7[1][1], B7[2][0]))))
gate("corollary: det(B) == -1 (exact)  => charpoly (x+1)(x^2+1), B^4 = I", iszero(fadd(det, fmono(0, 343))))

# doubly-stochastic circulant of |B|^2: row sums
okDS = True
for i in range(3):
    acc = [0]*NF
    for j in range(3):
        acc = fadd(acc, fmul(B7[i][j], fconj(B7[i][j])))
    okDS &= iszero(fsub(acc, fmono(0, 49)))
for j in range(3):
    acc = [0]*NF
    for i in range(3):
        acc = fadd(acc, fmul(B7[i][j], fconj(B7[i][j])))
    okDS &= iszero(fsub(acc, fmono(0, 49)))
gate("corollary: |B_ij|^2 doubly stochastic (all row/col sums == 1, exact)", okDS)

# ================================================================
# verdict
# ================================================================
out("")
out("="*78)
nfail = sum(1 for _, okk in CHECKS if not okk)
out(f"CHECK SUMMARY: {len(CHECKS)-nfail}/{len(CHECKS)} passed, {nfail} failed")
for name, okk in CHECKS:
    out(f"  [{'PASS' if okk else 'FAIL'}] {name}")
out("="*78)
if nfail == 0:
    out("""
VERDICT: PROVEN.

THEOREM (E6 level-2 odd hearing matrix -- the Latin-square/sine-kernel/
zeta_14-exponent laws).  Let S, T be the Kac-Peterson modular data of
E6 at level 2 (kappa = 14), C = S^2 the conjugation permutation, and
B = U^T C T^2 S T U the twisted weld on the three theta-odd pairs
(27,27b), (351',351'b), (351,351b).  Then, EXACTLY,

    B_ij = A_{k(i,j)} zeta_14^{m(i,j)},   A_k = (2/sqrt7) sin(2 pi k/7),

where  k(i,j) == +- m_i m_j (mod 7)  with the pair labels m = (1,2,3)
given by the Galois-orbit coordinates of the 27-pair under
Gal(Q(zeta_7)/Q)/{+-1} acting through the level-14 alcove -- so the
A-index Latin square [[1,2,3],[2,3,1],[3,1,2]] is the multiplication
table of Z_7^x/{+-1} -- and the zeta_14 exponent obeys
    m(i,j) == [189 - 63(1 - s'_ij) + 2 e_i + e_j]/18  (mod 14),
    e_j = 252(h_j - c/24),  s'_ij = sgn Im S_{a_i a_j}
with the s'-cocycle law s'(i,pi_t(j)) = eps_t(j) o_t(j) (t|7) sgn7(tk) s'(i,j)
DERIVED from the sharpened closed form of the unnormalized differences
    delta_ij = 392 sqrt21 s'_ij (z7^k - z7^{-k}),   392 = 2^3 7^2,
itself proved exactly (N = 14^3 sqrt3 = KP volume).  Corollaries
(all exact): B unitary, trace -1, charpoly (x+1)(x^2+1) (order 4),
|B|^2 the doubly-stochastic circulant of (A_1^2, A_2^2, A_3^2).
All decisive steps are exact integer/cyclotomic arithmetic in
Z[zeta_252] (zero-tests by reduction mod Phi_252); floats only pin
signs of nonzero real algebraics with stated margins.""")
else:
    out("\nVERDICT: NOT fully proven -- the failed gates above name the exact resisting steps.")

with open(__file__.rsplit('/', 1)[0] + '/cellR2_output.txt', 'w') as f:
    f.write("\n".join(LOG) + "\n")

# machine-readable proven tables
res = {
    'theorem': 'B_ij = A_k(i,j) zeta14^m(i,j), E6 level 2 odd weld',
    'k_table': Kt, 'm_table': Mt, 'labels': labels,
    'latin_law': 'k(i,j) = class(+-m_i m_j mod 7), m=(1,2,3) Galois orbit coords',
    'N2': int(N2), 's0': s0,
    'h': {NAMES[j]: str(hs[j]) for j in range(9)},
    'T_exponents_252': {NAMES[j]: eT[j] for j in range(9)},
    'sine_sign_table': Ssign,
    'sharpened_form': 'delta_ij = 392 s0 s_ij sqrt21 (z7^k - z7^{-k}), N = 14^3 sqrt3',
    'cocycle': "s'(i,pi_t(j)) = eps_t(j) o_t(j) (t|7) sgn7(tk) s'(i,j)",
    'exponent_law': 'm = [189 - 63(1-s) + 2 e_i + e_j]/18 mod 14',
    'galois_reps': TS, 'pair_perms': {str(u): PPERM[u] for u in PPERM},
    'checks_passed': len(CHECKS) - nfail, 'checks_failed': nfail,
    'failed': [n for n, okk in CHECKS if not okk],
}
with open(__file__.rsplit('/', 1)[0] + '/r2_proven_tables.json', 'w') as f:
    json.dump(res, f, indent=1)
stamp("done")
