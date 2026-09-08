#!/usr/bin/env python3
"""THE V10 DIRECTION (B1350; L207 = main's L204): at the subregular sl2 point of the cusped object's E6 holonomy
(E6(a1), weighted Dynkin (2,2,2,0,2,2); e6 = V2+V4+V6+V8+V10+V10+V14+V16, 27 = 13+9+5) the pairing law of B1280 fails
along exactly one deformation direction -- the V10 inside the 42 (theta = -1, iota* = +1) -- so the net chirality
N(27) = h^1(M; 27) - h^1(M; 27bar) is not forced to vanish there.  Is it zero?

(0) the subregular triple (B1267's instrument) and its block decomposition of e6 (kernel of ad e on each weight space);
(1) rho_0 = exp(e), exp(u f) on the 27 (exact over Q(omega)); its cohomology and N at the point (self-dual: N = 0);
(2) the two exact cocycle classes in H^1(M; V10) (one per V10 block; B1268's construction generalised), and their
    restriction to the cusp torus (cusp-trivial or not, exactly);
(3) the theta-parity of the two-dimensional V10 class space from the FIRST-ORDER self-duality defect
    d/d eps [tr rho_eps(w) - tr rho_eps(w^-1)]: the even direction is its kernel, the odd direction breaks self-duality;
(4) Newton to genuine E6 representations along the odd, the even (control) and a mixed direction (400-bit ball
    arithmetic, B1268's machinery), and at each: h^1(27), h^1(27bar), h^0(dM), rank(res), N (60-digit ranks).
Pre-registered (main's price: about a day, prior 15 % for N != 0): the bound -h^0(dM; 27) <= N <= h^0(dM; 27bar)
(B1268) means N != 0 needs a cusp-fixed vector at the deformed point; a class with non-trivial cusp restriction
kills the fixed vectors and forces N = 0.  Stages selectable: python3 v10_direction.py 0123 | 4."""
from __future__ import annotations
import os, sys, time
from fractions import Fraction as F
import numpy as np
import mpmath as mp
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1268_cusped_net_chirality_bound', 'verification'))
import cusped_theta_odd_hp as H
from flint import acb_mat, acb, arb, fmpq
E, S = H.E, H.S
Qw = E.Qw
n = 27
STAGES = sys.argv[1] if len(sys.argv) > 1 else "0123"

# ------------------------------------------------------------------ (0) the subregular triple and its blocks
t0 = time.time()
e2, h2, f2, g2 = E.subregular_sl2()
C_SUB = (2, 2, 2, 0, 2, 2)
wt = lambda r: sum(C_SUB[i] * r[i] for i in range(E.N))
def hw_vectors_sub(weight):
    """kernel of ad(e2) on the root space of the given subregular weight: the highest-weight vectors of the V_weight blocks."""
    basis = [r for r in E.POS if wt(r) == weight]
    if not basis:
        return []
    A = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in E.br(e2, E.vec(E.N + E.IDX[r]))] for r in basis]).T
    out = []
    for coef in A.nullspace():
        lcm = 1
        for c in coef:
            lcm = sp.ilcm(lcm, int(sp.Rational(c).q))
        v = [F(0)] * E.DIM
        for i, r in enumerate(basis):
            q = sp.Rational(coef[i] * lcm)
            if q != 0:
                v[E.N + E.IDX[r]] = F(int(q.p), int(q.q))
        out.append(v)
    return out
blocks = {w: len(hw_vectors_sub(w)) for w in range(2, 18, 2)}
print(f"=== (0) the subregular sl2: [e,f] = h ok; block multiplicities by highest weight: {blocks} ===")
assert blocks == {2: 1, 4: 1, 6: 1, 8: 1, 10: 2, 12: 0, 14: 1, 16: 1}, blocks
HV10 = hw_vectors_sub(10)

# ------------------------------------------------------------------ (1) rho_0 exact and its cohomology
rho0 = S.build_rep(e2, f2)
S.check_rep(rho0, [1, 2], [S.REL])
h0x, h1x, _, _ = S.h0_h1(rho0, [1, 2], [S.REL])
h0d, h1d, _, _ = S.h0_h1(rho0.dualrep(), [1, 2], [S.REL])
print(f"=== (1) rho_0 (subregular, exact over Q(omega)): h0 = {h0x}, h1(27) = {h1x}; h1(27bar) = {h1d}  ({time.time() - t0:.0f} s) ===")
A0, B0 = H.to_acb(H.rescale(rho0.M[1])), H.to_acb(H.rescale(rho0.M[2]))
A0i, B0i = H.to_acb(H.rescale(rho0.I[1])), H.to_acb(H.rescale(rho0.I[2]))
M0, M0i = {1: A0, 2: B0}, {1: A0i, 2: B0i}
rep0 = H.cohomology_report(M0, M0i, n, "27 at the subregular point")
dm0, di0 = H.dual_of(M0, M0i)
rep0d = H.cohomology_report(dm0, di0, n, "27bar at the subregular point")
print(f"    N(27) at the point = {rep0['h1'] - rep0d['h1']}")

# ------------------------------------------------------------------ (2) the exact V10 cocycles and their cusp restrictions
def block_cocycle_sub(hv, m=5):
    v = hv; basis = [v]
    for k in range(2 * m):
        v = E.br(f2, v); basis.append(v)
    d = len(basis)
    Bm = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in b] for b in basis]).T
    def restrict(y):
        img = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in E.br(y, b)] for b in basis]).T
        return Bm.gauss_jordan_solve(img)[0]
    ade, adf = restrict(e2), restrict(f2)
    def qwm(M, c):
        out = E.qw_zeros(d)
        for i in range(d):
            for j in range(d):
                x = sp.Rational(M[i, j]); out[i, j] = Qw(F(int(x.p), int(x.q))) * c
        return out
    Aa = E.qw_expm_nilpotent(qwm(ade, E.ONE)); Aai = E.qw_expm_nilpotent(qwm(ade, Qw(-1)))
    Bb = E.qw_expm_nilpotent(qwm(adf, E.U_RILEY)); Bbi = E.qw_expm_nilpotent(qwm(adf, -E.U_RILEY))
    R = S.Rep({1: Aa, 2: Bb}, {1: Aai, 2: Bbi}); S.check_rep(R, [1, 2], [S.REL])
    d1 = np.hstack([R.fox(S.REL, 1), R.fox(S.REL, 2)])
    A = [[d1[i, j] for j in range(2 * d)] for i in range(d)]
    nn, mm = d, 2 * d; r = 0; pivcols = []
    for c in range(mm):
        piv = next((i for i in range(r, nn) if not A[i][c].is_zero()), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]; inv = A[r][c].inv(); A[r] = [x * inv for x in A[r]]
        for i in range(nn):
            if i != r and not A[i][c].is_zero():
                fct = A[i][c]; A[i] = [x - fct * y for x, y in zip(A[i], A[r])]
        pivcols.append(c); r += 1
    free = [c for c in range(mm) if c not in pivcols]
    kern = []
    for fc in free:
        vct = [E.ZERO] * mm; vct[fc] = E.ONE
        for i, pc in enumerate(pivcols): vct[pc] = -A[i][fc]
        kern.append(vct)
    I = E.qw_eye(d)
    cob = np.vstack([Aa - I, Bb - I]); rB = S.exact_rank_qw(cob)
    h1b = len(kern) - rB
    za = zb = None
    for vct in kern:
        test = np.hstack([cob, np.array([[x] for x in vct], dtype=object)])
        if S.exact_rank_qw(test) > rB:
            za, zb = vct[:d], vct[d:]; break
    # the restriction to the cusp torus <mu = a, lambda = LONG>: values z(mu) = za, z(lambda) by the cocycle rule;
    # coboundaries of the torus: (Aa - I) w, (Bl - I) w with Bl = R(lambda)
    def cocycle_along(word):
        acc = np.array([[E.ZERO] for _ in range(d)], dtype=object); cur = E.qw_eye(d)
        zg = {1: np.array([[x] for x in za], dtype=object), 2: np.array([[x] for x in zb], dtype=object)}
        for L in word:
            if L > 0:
                acc = acc + cur.dot(zg[L]); cur = cur.dot(R.M[L])
            else:
                cur = cur.dot(R.I[-L]); acc = acc - cur.dot(zg[-L])
        return acc
    Bl = R.ev(S.LONG)
    zmu = np.array([[x] for x in za], dtype=object); zlam = cocycle_along(S.LONG)
    torus_cob = np.vstack([Aa - I, Bl - I])                      # 2d x d
    rTB = S.exact_rank_qw(torus_cob)
    test = np.hstack([torus_cob, np.vstack([zmu, zlam])])
    cusp_trivial = (S.exact_rank_qw(test) == rTB)
    Za = [sum((Qw(F(int(sp.Rational(Bm[k, i]).p), int(sp.Rational(Bm[k, i]).q))) * za[i] for i in range(d)), E.ZERO) for k in range(78)]
    Zb = [sum((Qw(F(int(sp.Rational(Bm[k, i]).p), int(sp.Rational(Bm[k, i]).q))) * zb[i] for i in range(d)), E.ZERO) for k in range(78)]
    return Za, Zb, dict(dimZ1=len(kern), dimB1=rB, h1=h1b, cusp_trivial=cusp_trivial)

print(f"=== (2) the two V10 blocks' exact cocycle classes ===")
COC = []
for i, hv in enumerate(HV10):
    Za, Zb, info = block_cocycle_sub(hv)
    print(f"    block V10 #{i + 1}: dim Z1 = {info['dimZ1']}, dim B1 = {info['dimB1']}, h1 = {info['h1']}; restriction to the cusp torus trivial: {info['cusp_trivial']}")
    COC.append((Za, Zb, info))
# the joint restriction of the two classes to the cusp torus, in e6 coordinates (78): rank of [torus coboundaries | res z1 | res z2]
def ad_word_exact(word):
    """Ad rho_0(word) on e6 as an exact 78x78 Qw matrix: products of exp(ad e2), exp(u ad f2) and inverses."""
    ade = E.ad_matrix(e2); adf = E.ad_matrix(f2)
    def qwm(M, c):
        out = E.qw_zeros(78)
        for i in range(78):
            for j in range(78):
                x = sp.Rational(M[i, j])
                if x != 0: out[i, j] = Qw(F(int(x.p), int(x.q))) * c
        return out
    Ea, Eai = E.qw_expm_nilpotent(qwm(ade, E.ONE)), E.qw_expm_nilpotent(qwm(ade, Qw(-1)))
    Eb, Ebi = E.qw_expm_nilpotent(qwm(adf, E.U_RILEY)), E.qw_expm_nilpotent(qwm(adf, -E.U_RILEY))
    R = S.Rep({1: Ea, 2: Eb}, {1: Eai, 2: Ebi})
    return R
RAD = ad_word_exact(None)
def res_e6(Za, Zb):
    zg = {1: np.array([[x] for x in Za], dtype=object), 2: np.array([[x] for x in Zb], dtype=object)}
    def along(word):
        acc = np.array([[E.ZERO] for _ in range(78)], dtype=object); cur = E.qw_eye(78)
        for L in word:
            if L > 0:
                acc = acc + cur.dot(zg[L]); cur = cur.dot(RAD.M[L])
            else:
                cur = cur.dot(RAD.I[-L]); acc = acc - cur.dot(zg[-L])
        return acc
    return np.vstack([zg[1], along(S.LONG)])
I78 = E.qw_eye(78)
TCOB = np.vstack([RAD.M[1] - I78, RAD.ev(S.LONG) - I78])
rT = S.exact_rank_qw(TCOB)
R1, R2 = res_e6(COC[0][0], COC[0][1]), res_e6(COC[1][0], COC[1][1])
r_joint = S.exact_rank_qw(np.hstack([TCOB, R1, R2])) - rT
print(f"    restriction H^1(M; V10-isotype) -> H^1(dM; e6): rank {r_joint} on the two-dimensional class space (2 = no cusp-trivial direction; 1 = one cusp-trivial combination)")
Ys = [(H.e6_matrix([H.q2acb(z) for z in Za]), H.e6_matrix([H.q2acb(z) for z in Zb])) for Za, Zb, _ in COC]

# ------------------------------------------------------------------ (3) theta-parity from the first-order self-duality defect
def first_order_defect(Ya, Yb):
    out = []
    for word in ([1], [2], [1, 2], [1, 1, 2], [1, 2, -1, -2], [2, 1, 1]):
        vals = []
        for w in (word, [-x for x in reversed(word)]):
            Mw = H.ev(M0, M0i, w, n)
            D = H.adfox_apply(M0, M0i, w, 1, Ya, n) + H.adfox_apply(M0, M0i, w, 2, Yb, n)
            vals.append(H.trace(D * Mw))
        out.append(vals[0] - vals[1])
    return out
D1 = first_order_defect(*Ys[0]); D2 = first_order_defect(*Ys[1])
print(f"=== (3) first-order self-duality defects d/d eps [tr rho(w) - tr rho(w^-1)] on six words ===")
print(f"    class 1: {[x.str(4) for x in D1]}")
print(f"    class 2: {[x.str(4) for x in D2]}")
flat = max(float(abs(x).mid()) + float(x.rad()) for x in D1 + D2)
print(f"    all twelve first-order defects vanish (largest |.| {flat:.1e}): both classes are TRACE-FLAT at first order, so the theta-parity of the class space is read from finite deformations (stage 4), not from first order")
def combo(c):
    return (Ys[0][0] * c[0] + Ys[1][0] * c[1], Ys[0][1] * c[0] + Ys[1][1] * c[1])
print(f"    ({time.time() - t0:.0f} s)")

# ------------------------------------------------------------------ (4) Newton deformations and N
if "4" in STAGES:
    print(f"=== (4) Newton to genuine E6 representations along the odd, even and first-class directions; N(27) ===")
    # controls (environment): V10_STEP (default 0.02), V10_MU (Newton damping, default B1268's 1e-24), V10_CLASSES (comma list)
    STEP = float(os.environ.get("V10_STEP", "0.02")); MU = os.environ.get("V10_MU", "1e-50"); ITERS = int(os.environ.get("V10_ITERS", "40"))
    # default damping 1e-50: with B1268's 1e-24 the search stalls at |res| ~ 3.6e-13 along the V10 classes (v10_direction_run_stall.txt);
    # the directions it must correct along have singular values of order eps and are damped away; at 1e-50 it converges (probe_mu50.txt)
    WANT = os.environ.get("V10_CLASSES", "class 1,class 2,class 1 + class 2,class 1 - class 2").split(",")
    print(f"    controls: step {STEP}, damping mu {MU}, iterations {ITERS}, directions {WANT}")
    for name, c in (("class 1", (acb(1), acb(0))), ("class 2", (acb(0), acb(1))), ("class 1 + class 2", (acb(1), acb(1))), ("class 1 - class 2", (acb(1), acb(-1)))):
        if name not in WANT:
            continue
        Ya, Yb = combo(c)
        znorm = max(float(H.frob(Ya).mid()), float(H.frob(Yb).mid()))
        assert znorm > 0 and znorm == znorm, znorm
        # normalise the direction to Frobenius norm 1 (the rescaled e6 coefficients of a V10 class are large), then step STEP
        ce = acb(STEP) / acb(arb(str(znorm)))
        mats = {1: (Ya * ce).exp() * A0, 2: (Yb * ce).exp() * B0}
        invs = {1: A0i * (-(Ya * ce)).exp(), 2: B0i * (-(Yb * ce)).exp()}
        print(f"  -- {name}: |Y| = {znorm:.3e}, step {STEP}/|Y|, start residual {H.frob(H.ev(mats, invs, S.REL, n) - H.eye(n)).str(3)}")
        mats, invs, _, nr = H.newton(mats, invs, iters=ITERS, mu=MU, verbose=True)
        tt = H.selfduality_trace_test(mats, invs, n)
        print(f"     converged residual {nr:.1e}; self-duality defects {[x.str(3) for x in tt]} -> {'NOT self-dual' if max(float(x.mid()) for x in tt) > 1e-20 else 'self-dual'}")
        rep = H.cohomology_report(mats, invs, n, f"27 along {name}")
        dm, di = H.dual_of(mats, invs)
        repd = H.cohomology_report(dm, di, n, f"27bar along {name}")
        print(f"     ==> N(27) = h1(27) - h1(27bar) = {rep['h1'] - repd['h1']};  bound -{rep['h0t']} <= N <= {repd['h0t']}   ({time.time() - t0:.0f} s)")
print(f"\n[{time.time() - t0:.0f} s]")
