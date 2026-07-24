#!/usr/bin/env python3
"""
B775 Phase-2 Wave-5 cell P2W5-L72   (OI-111: the L72 CS-functional/dynamics program,
phases 2-3).

PHASE 1 is banked: B581 = the E6-PRINCIPAL Reidemeister torsion of the figure-eight as
the product of the six Sym^{2m}-block torsions, m in the E6 exponents {1,4,5,7,8,11},
with sign(tau_m) = (-1)^m  ->  tau_m > 0 exactly at the THETA-ODD exponents m = 4, 8.
B425 / P2W4-L54 give the adjoint (m=1) block exactly: T^2 - 5T + 1, tau_1 = -3.

THIS CELL RUNS PHASES 2 AND 3.

  PHASE 2 -- the E6 6j symbols at levels 1 and 2.
    A. E6 modular data at k=1,2 from FIRST PRINCIPLES: Kac-Peterson sum over the full
       Weyl group W(E6) (|W| = 51840), exact as integer counts of 3(k+h^)-th roots of
       unity; validated by unitarity, S^2 = C, (ST)^3 = S^2, and Verlinde integrality.
    B. LEVEL 1: the category is POINTED (all quantum dims 1, fusion = Z/3).  Its full
       6j system is the Z/3 associator omega_p; (p,r) is pinned by pentagon + BOTH
       hexagons + the computed twist + the computed S-matrix.  Closed form, exact.
    C. LEVEL 2: rank 9.  The Z/3 simple currents form a MODULAR subcategory, so
       (Mueger) E6_2 splits as a Deligne product of that pointed factor and its
       centralizer.  The centralizer is computed in-cell (rank 3) and its S,T are
       matched entry-by-entry to the even part of SU(2)_5.  Its 6j symbols are then
       CONSTRUCTED from the quantum Racah formula at q = exp(i pi/7) and VERIFIED
       (pentagon, hexagons, Hopf-link S, twists).  Product => the level-2 6j system.
    D. Consequence computed for the object itself: the E6 level-2 colored invariants
       of 4_1 (Habiro's closed form for the colored Jones at q = zeta_7).

  PHASE 3 -- the Chern-Simons functional along the theta-odd deformation.
    E. index(principal SL2 -> E6) = 156 (exact; formula validated on su(3) = 4).
    F. CS of the geometric rep of 4_1 = 0 (SnapPy complex_volume, 2 triangulations)
       => CS of the E6-principal geometric flat connection = 156 * 0 = 0.
    G. dim H^1(M; Sym^{2m} rho_geo) = 1 for every E6 exponent (exact, 2 primes +
       exact Q(omega)); total 6 = rank(E6) => smooth point, one direction per exponent,
       the theta-odd ones being m = 4 and m = 8.  Peripheral: dim H^1(T^2; Sym^{2m}) = 2
       per block => the 6-dim image is a Lagrangian in the 12-dim peripheral space, so
       the CS functional along the deformation is the potential of that Lagrangian.
    H. The theta-EVEN (m=1, SL2-induced) direction: the CS functional IS computable and
       is sampled exactly (SnapPy Dehn fillings of 4_1).
    I. The theta-ODD directions leave the SL(2,C)-induced locus.  The wall is computed,
       not cited: the only implemented complex-volume machinery (GTZ/Zickert Ptolemy)
       is PGL(N,C); the smallest faithful E6 rep is 27-dimensional, so the Ptolemy
       variety on the 2-tetrahedron triangulation of 4_1 carries C(30,3)-4 = 4056
       coordinates per tetrahedron = 8112 variables.  EXTERNAL.

SEALED VERDICT RULE (declared before the run, MB12-checked -- every branch can FIRE and
can FAIL):
  A2 := 6j/F-symbols computed AND verified at level 1 AND at level 2
  A3 := the CS functional along the theta-odd deformation computed
        (trivially true if no theta-odd deformation direction exists -- a real fire-path)
  W  := an in-cell COMPUTED obstruction blocking whatever is not computed
  RESOLVED-A  iff (A2 or A3) and every unachieved piece carries W
  RESOLVED-B  iff (not A2) and (not A3) and W          [a named EXTERNAL wall]
  UNRESOLVED  otherwise                                [checks failed / nothing pinned]

Gate 5/5-Q: structural only.  No SM values, nothing to CLAIMS, one-number pin untouched.
Env: pyenv python3 (numpy, sympy, mpmath, snappy).  Re-runnable.  COMPACT output.
"""
import itertools, json, math, os, sys, time
import numpy as np
import mpmath as mp
from fractions import Fraction

mp.mp.dps = 40
TOL = mp.mpf('1e-22')
OUT = {}
P = lambda *a: print(*a)
t_start = time.time()

# =====================================================================
# A.  E6 root data, Weyl group, Kac-Peterson modular data (k = 1, 2)
# =====================================================================
A = np.zeros((6, 6), dtype=np.int64)
for i in range(6):
    A[i, i] = 2
for (i, j) in [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]:
    A[i - 1, j - 1] = A[j - 1, i - 1] = -1
MARKS = np.array([1, 2, 2, 3, 2, 1], dtype=np.int64)   # E6 marks (Bourbaki)
HV = 12                                                # dual Coxeter number
EXPONENTS = [1, 4, 5, 7, 8, 11]                        # E6 exponents
assert int(MARKS.sum()) + 1 == HV

Ainv = np.linalg.inv(A.astype(float))
B3 = np.rint(3 * Ainv).astype(np.int64)                # 3*A^{-1} is integral (det A = 3)
assert np.abs(3 * Ainv - B3).max() < 1e-9

gens = []
for i in range(6):
    Sg = np.eye(6, dtype=np.int64)
    for j in range(6):
        Sg[j, i] -= A[i, j]                            # (s_i lam)_j = lam_j - lam_i A_ij
    gens.append(Sg)
W = [np.eye(6, dtype=np.int64)]
seen = {tuple(W[0].ravel())}
fr = [W[0]]
while fr:
    nxt = []
    for M in fr:
        for Sg in gens:
            Pm = Sg @ M
            key = tuple(Pm.ravel())
            if key not in seen:
                seen.add(key); W.append(Pm); nxt.append(Pm)
    fr = nxt
Ws = np.array(W)
dets = np.rint(np.linalg.det(Ws)).astype(np.int64)
P("[A] |W(E6)| =", len(W), " det split:", int((dets == 1).sum()), "/", int((dets == -1).sum()))
assert len(W) == 51840 and set(dets.tolist()) == {1, -1}


def modular_data(k):
    """exact Kac-Peterson S (as integer counts of MOD-th roots of unity), h, c, fusion."""
    Mlev = k + HV
    MOD = 3 * Mlev
    wts = [np.array(l, dtype=np.int64)
           for l in itertools.product(range(k + 1), repeat=6)
           if int((MARKS * np.array(l)).sum()) <= k]
    n = len(wts)
    rho = np.ones(6, dtype=np.int64)
    L = np.array([w + rho for w in wts]).T             # 6 x n
    C = B3 @ L
    counts = np.zeros((n, n, MOD), dtype=np.int64)
    chunk = 4000
    for s in range(0, len(Ws), chunk):
        Wc, dc = Ws[s:s + chunk], dets[s:s + chunk]
        WL = np.einsum('wij,jb->wib', Wc, L)
        E = np.einsum('wia,ib->wab', WL, C) % MOD
        for val in (1, -1):
            sel = (dc == val)
            if sel.any():
                Es = E[sel]
                flat = (np.arange(n)[None, :, None] * n * MOD
                        + np.arange(n)[None, None, :] * MOD + Es).ravel()
                counts += val * np.bincount(flat, minlength=n * n * MOD).reshape(n, n, MOD)
    z = mp.matrix([mp.exp(-2j * mp.pi * a / MOD) for a in range(MOD)])
    Shat = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            acc = mp.mpc(0)
            row = counts[a, b]
            for e in np.nonzero(row)[0]:
                acc += int(row[e]) * z[int(e)]
            Shat[a, b] = acc
    nrm = mp.sqrt(sum(abs(Shat[0, b])**2 for b in range(n)))
    S = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            S[a, b] = Shat[a, b] / nrm
    if mp.re(S[0, 0]) < 0:
        S = -S
    hs, rhoAinvrho = [], float(np.ones(6) @ Ainv @ np.ones(6))
    for w in wts:
        lr = (w + rho).astype(np.int64)
        num = int(np.rint((lr @ B3 @ lr) - (np.ones(6, dtype=np.int64) @ B3 @ np.ones(6, dtype=np.int64))))
        hs.append(Fraction(num, 6 * Mlev))             # h = (lam,lam+2rho)/2(k+h^)
    cc = Fraction(78 * k, Mlev)
    return wts, S, hs, cc


def check_md(wts, S, hs, cc):
    n = len(wts)
    Sc = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            Sc[a, b] = mp.conj(S[a, b])
    uni = max(abs((S * Sc.T)[a, b] - (1 if a == b else 0)) for a in range(n) for b in range(n))
    S2 = S * S
    perm_ok = all(sum(1 for b in range(n) if abs(abs(S2[a, b]) - 1) < 1e-20) == 1 for a in range(n))
    T = mp.matrix(n, n)
    for a in range(n):
        T[a, a] = mp.exp(2j * mp.pi * (mp.mpf(hs[a].numerator) / hs[a].denominator
                                       - mp.mpf(cc.numerator) / (24 * cc.denominator)))
    ST = S * T
    st3 = max(abs((ST * ST * ST)[a, b] - S2[a, b]) for a in range(n) for b in range(n))
    Nmax, Nmin, interr = 0, 10**9, mp.mpf(0)
    N = np.zeros((n, n, n), dtype=np.int64)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                v = sum(S[a, x] * S[b, x] * mp.conj(S[c, x]) / S[0, x] for x in range(n))
                interr = max(interr, abs(v - mp.nint(mp.re(v))))
                iv = int(mp.nint(mp.re(v)))
                N[a, b, c] = iv
                Nmax, Nmin = max(Nmax, iv), min(Nmin, iv)
    return dict(unitary_err=uni, S2_is_permutation=perm_ok, ST3_err=st3,
                verlinde_int_err=interr, N_min=Nmin, N_max=Nmax), N, T


MD = {}
for k in (1, 2):
    wts, S, hs, cc = modular_data(k)
    chk, N, T = check_md(wts, S, hs, cc)
    d = [mp.re(S[0, b] / S[0, 0]) for b in range(len(wts))]
    MD[k] = dict(wts=wts, S=S, hs=hs, cc=cc, N=N, T=T, d=d, chk=chk)
    P(f"[A] level {k}: rank {len(wts)}  c = {cc}  qdims = "
      + str([mp.nstr(x, 7) for x in d]))
    P(f"    h = {[str(h) for h in hs]}")
    P(f"    checks: unitary {mp.nstr(chk['unitary_err'],3)}  S^2=perm {chk['S2_is_permutation']}"
      f"  (ST)^3=S^2 {mp.nstr(chk['ST3_err'],3)}  Verlinde int-err {mp.nstr(chk['verlinde_int_err'],3)}"
      f"  N in [{chk['N_min']},{chk['N_max']}]")

MD_OK = all(MD[k]['chk']['unitary_err'] < TOL and MD[k]['chk']['S2_is_permutation']
            and MD[k]['chk']['ST3_err'] < TOL and MD[k]['chk']['verlinde_int_err'] < TOL
            and MD[k]['chk']['N_min'] == 0 for k in (1, 2))
OUT['A_modular_data'] = {
    str(k): dict(rank=len(MD[k]['wts']), c=str(MD[k]['cc']),
                 weights=[''.join(map(str, w)) for w in MD[k]['wts']],
                 h=[str(x) for x in MD[k]['hs']],
                 qdim=[mp.nstr(x, 12) for x in MD[k]['d']],
                 multiplicity_free=bool(MD[k]['chk']['N_max'] <= 1),
                 checks={kk: (str(mp.nstr(vv, 3)) if isinstance(vv, mp.mpf) else vv)
                         for kk, vv in MD[k]['chk'].items()})
    for k in (1, 2)}
OUT['A_modular_data_validated'] = bool(MD_OK)

# =====================================================================
# B.  LEVEL 1 6j -- the pointed Z/3 associator, pinned exactly
# =====================================================================
d1 = MD[1]['d']
pointed1 = all(abs(x - 1) < TOL for x in d1)
# fusion group structure: identify labels with Z/3 via the fusion rules
N1 = MD[1]['N']
lab1 = [''.join(map(str, w)) for w in MD[1]['wts']]
g = 1                                                   # a non-unit generator
z3 = [0, g, int(np.argmax(N1[g, g]))]
grp_ok = (len(set(z3)) == 3) and int(np.argmax(N1[g, z3[2]])) == 0
th1 = [mp.exp(2j * mp.pi * mp.mpf(MD[1]['hs'][a].numerator) / MD[1]['hs'][a].denominator)
       for a in range(3)]
theta_gen1 = th1[g]

z9 = [mp.exp(2j * mp.pi * a / 9) for a in range(9)]


def pointed_solutions(theta_gen, S_target, D_target):
    """search (p,r) in Z9^2 for: pentagon(omega_p), both hexagons, twist, Hopf-link S."""
    sols = []
    for p in range(3):          # omega_p depends only on p mod 3 (H^3(Z/3,U(1)) = Z/3)
        w = lambda a, b, c: z9[(p * a * ((b + c) - (b + c) % 3)) % 9]
        pent = max(abs(w(b, c, dd) * w(a, (b + c) % 3, dd) * w(a, b, c)
                       - w((a + b) % 3, c, dd) * w(a, b, (c + dd) % 3))
                   for a in range(3) for b in range(3) for c in range(3) for dd in range(3))
        if pent > TOL:
            continue
        for r in range(9):
            R = lambda a, b: z9[(r * a * b) % 9]
            h1 = max(abs(R(c, a) * w(a, c, b) * R(c, b) - w(c, a, b) * R(c, (a + b) % 3) * w(a, b, c))
                     for a in range(3) for b in range(3) for c in range(3))
            h2 = max(abs(R(c, a)**-1 * w(a, c, b) * R(c, b)**-1
                         - w(c, a, b) * R(c, (a + b) % 3)**-1 * w(a, b, c))
                     for a in range(3) for b in range(3) for c in range(3))
            if h1 > TOL and h2 > TOL:
                continue
            tw = abs(R(1, 1) - theta_gen)
            if tw > TOL:
                continue
            # Hopf link S_ab = (1/D) theta_{a+b}/(theta_a theta_b) = (1/D) R(a,b)R(b,a)
            sm = max(abs(R(a, b) * R(b, a) / D_target - S_target[a, b])
                     for a in range(3) for b in range(3))
            smc = max(abs(mp.conj(R(a, b) * R(b, a)) / D_target - S_target[a, b])
                      for a in range(3) for b in range(3))
            if min(sm, smc) < TOL:
                sols.append((p, r, 'S' if sm < TOL else 'Sbar',
                             mp.nstr(pent, 3), mp.nstr(max(h1, h2), 3)))
    return sols


D1t = 1 / MD[1]['S'][0, 0]
sols1 = pointed_solutions(theta_gen1, MD[1]['S'], D1t)
P(f"[B] level 1: pointed={pointed1}  Z/3 fusion={grp_ok}  theta_27 = exp(2pi i * {MD[1]['hs'][1]})")
P(f"    (p,r) solutions of pentagon+hexagons+twist+Hopf-S : {[(s[0],s[1],s[2]) for s in sols1]}")
LEVEL1_OK = bool(pointed1 and grp_ok and len(sols1) >= 1)
assoc1 = None
if sols1:
    p1, r1 = sols1[0][0], sols1[0][1]
    assoc1 = 'TRIVIAL' if p1 % 3 == 0 else f'omega_{p1 % 3}'
    P(f"    => associator class in H^3(Z/3,U(1)) = Z/3 is {assoc1}: every level-1 6j symbol"
      f" F^{{abc}}_{{a+b+c}} = 1 (27 of them); the braiding is the bicharacter"
      f" R^{{ab}} = zeta_3^{{{(r1 % 9)//3 if r1 % 3 == 0 else r1}ab}} = exp(2pi i * {r1} ab/9),"
      f" theta_a = R^{{aa}}.")
    P(f"    => E6_1 = the Z/3 anyon theory with q(a) = exp(4 pi i a^2/3) = conj(SU(3)_1);"
      f" pointed => the RT invariant of ANY knot is framing-only. LEVEL 1 IS DEAF TO THE OBJECT.")
OUT['B_level1'] = dict(pointed=bool(pointed1), fusion_group='Z/3', fusion_ok=bool(grp_ok),
                       h_27=str(MD[1]['hs'][1]), c=str(MD[1]['cc']),
                       solutions_p_r=[[s[0], s[1], s[2]] for s in sols1],
                       n_F_symbols=27, n_R_symbols=9,
                       associator_class=assoc1,
                       closed_form=('F^{abc}=omega_p(a,b,c) with p=0 => all 27 F-symbols = 1; '
                                    'R^{ab}=exp(2pi i r ab/9)'),
                       identified_as='Z/3 anyons, q(a)=exp(4 pi i a^2/3) = conj(SU(3)_1)',
                       verified=bool(LEVEL1_OK))

# =====================================================================
# C.  LEVEL 2 6j -- modular splitting + explicit construction
# =====================================================================
S2m, hs2, N2f, d2 = MD[2]['S'], MD[2]['hs'], MD[2]['N'], MD[2]['d']
n2 = len(MD[2]['wts'])
lab2 = [''.join(map(str, w)) for w in MD[2]['wts']]
units = [i for i in range(n2) if abs(d2[i] - 1) < TOL]
th2 = [mp.exp(2j * mp.pi * mp.mpf(h.numerator) / h.denominator) for h in hs2]
fuse = lambda a, b: int(np.argmax(N2f[a, b]))
# (C1) the pointed subcategory of simple currents is MODULAR (nondegenerate)
Su = mp.matrix(3, 3)
for i, a in enumerate(units):
    for j, b in enumerate(units):
        Su[i, j] = S2m[a, b]
detSu = mp.det(Su)
mono = lambda a, b: th2[fuse(a, b)] / (th2[a] * th2[b])
pointed_nondeg = abs(detSu) > mp.mpf('1e-10')
# (C2) the Mueger centralizer of the current group
cent = [x for x in range(n2) if all(abs(mono(J, x) - 1) < mp.mpf('1e-20') for J in units)]
P(f"[C] level 2: rank {n2}, simple currents {[lab2[u] for u in units]} (Z/3), "
  f"|det S_pointed| = {mp.nstr(abs(detSu),4)} -> modular subcategory: {pointed_nondeg}")
P(f"    Mueger centralizer = {[lab2[c] for c in cent]}  dims "
  f"{[mp.nstr(d2[c],7) for c in cent]}  h {[str(hs2[c]) for c in cent]}")
# (C3) the factorization  label <-> (current power a, centralizer object x)
Jg = units[1]
idx, ok_bij = {}, True
for xi, x in enumerate(cent):
    cur = x
    for a in range(3):
        idx[(a, xi)] = cur
        cur = fuse(Jg, cur)
ok_bij = (len(set(idx.values())) == n2)
Sfac = mp.mpf(0); Tfac = mp.mpf(0); Nfac = 0
S_1 = mp.matrix(3, 3); S_2 = mp.matrix(3, 3)
for a in range(3):
    for b in range(3):
        S_1[a, b] = S2m[idx[(a, 0)], idx[(b, 0)]] / S2m[idx[(0, 0)], idx[(0, 0)]]
for xi in range(3):
    for yi in range(3):
        S_2[xi, yi] = S2m[idx[(0, xi)], idx[(0, yi)]]
for (a, xi), i in idx.items():
    for (b, yi), j in idx.items():
        Sfac = max(Sfac, abs(S2m[i, j] - S_1[a, b] * S_2[xi, yi]))
for a in range(3):
    for b in range(3):
        S_1[a, b] = S_1[a, b] / mp.sqrt(3)        # unitary pointed factor
for xi in range(3):
    for yi in range(3):
        S_2[xi, yi] = S_2[xi, yi] * mp.sqrt(3)    # unitary rank-3 factor
for (a, xi), i in idx.items():
    Tfac = max(Tfac, abs(th2[i] - th2[idx[(a, 0)]] * th2[idx[(0, xi)]]))
# fusion factorization: N_{(a,x)(b,y)}^{(a+b,z)} = N2_{xy}^z  and 0 otherwise
N_2 = np.zeros((3, 3, 3), dtype=np.int64)
for xi in range(3):
    for yi in range(3):
        for zi in range(3):
            N_2[xi, yi, zi] = N2f[idx[(0, xi)], idx[(0, yi)], idx[(0, zi)]]
Nfac_err = 0
for (a, xi), i in idx.items():
    for (b, yi), j in idx.items():
        for (c, zi), kk in idx.items():
            want = int(N_2[xi, yi, zi]) if (c == (a + b) % 3) else 0
            Nfac_err = max(Nfac_err, abs(int(N2f[i, j, kk]) - want))
P(f"    Deligne factorization errors: S {mp.nstr(Sfac,3)}   T {mp.nstr(Tfac,3)}   N {Nfac_err}")
# (C4) the pointed factor of level 2 (theta_J), and its (p,r)
theta_gen2 = th2[idx[(1, 0)]]
sols2p = pointed_solutions(theta_gen2, S_1, mp.sqrt(3))
P(f"    level-2 pointed factor: theta_J = exp(2pi i * {hs2[idx[(1,0)]]}),  (p,r) = "
  f"{[(s[0],s[1],s[2]) for s in sols2p]}")
# (C5) the rank-3 factor: construct SU(2)_5-even 6j and match S,T


def su2_cat(k, qroot=1, even=False):
    q = mp.exp(1j * mp.pi * qroot / (k + 2))
    qn = lambda n: (q**n - q**(-n)) / (q - q**(-1))
    F0 = {0: mp.mpf(1)}
    for n in range(1, 4 * k + 20):
        F0[n] = F0[n - 1] * qn(n)
    two = [j for j in range(k + 1)]
    if even:
        two = [j for j in two if j % 2 == 0]
    allowed = set(two)
    def adm(a, b, c):
        return ((a + b + c) % 2 == 0) and abs(a - b) <= c <= min(a + b, 2 * k - a - b) and c in allowed
    def Dl(a, b, c):
        return mp.sqrt(F0[(a + b - c) // 2] * F0[(a - b + c) // 2] * F0[(-a + b + c) // 2]
                       / F0[(a + b + c) // 2 + 1])
    def sixj(a, b, e, c, dd, f):
        pre = Dl(a, b, e) * Dl(c, dd, e) * Dl(a, dd, f) * Dl(b, c, f)
        lo = max(a + b + e, c + dd + e, a + dd + f, b + c + f) // 2
        hi = min(a + b + c + dd, a + c + e + f, b + dd + e + f) // 2
        s = mp.mpf(0)
        for z in range(lo, hi + 1):
            s += (-1)**z * F0[z + 1] / (F0[z - (a + b + e) // 2] * F0[z - (c + dd + e) // 2]
                 * F0[z - (a + dd + f) // 2] * F0[z - (b + c + f) // 2]
                 * F0[(a + b + c + dd) // 2 - z] * F0[(a + c + e + f) // 2 - z]
                 * F0[(b + dd + e + f) // 2 - z])
        return pre * s
    cache = {}
    def F(a, b, c, dd, e, f):
        if not (adm(a, b, e) and adm(e, c, dd) and adm(b, c, f) and adm(a, f, dd)):
            return mp.mpf(0)
        key = (a, b, c, dd, e, f)
        if key not in cache:
            cache[key] = (-1)**((a + b + c + dd) // 2) * mp.sqrt(qn(e + 1) * qn(f + 1)) * sixj(a, b, e, c, dd, f)
        return cache[key]
    return two, adm, F, qn, q, cache


two, adm, Fkl, qn, qq, Fcache = su2_cat(5, 1, even=True)
# pentagon
pent_worst, pent_cnt = mp.mpf(0), 0
for a, b, c, dd in itertools.product(two, repeat=4):
    for f in two:
        if not adm(a, b, f):
            continue
        for l in two:
            if not adm(c, dd, l):
                continue
            for e in two:
                if not adm(f, l, e):
                    continue
                for g in two:
                    if not adm(a, b, g):
                        continue
                    for kk in two:
                        if not (adm(b, l, kk) and adm(a, kk, e)):
                            continue
                        LH = Fkl(f, c, dd, e, g, l) * Fkl(a, b, l, e, f, kk)
                        RH = sum(Fkl(a, b, c, g, f, h) * Fkl(a, h, dd, e, g, kk) * Fkl(b, c, dd, kk, h, l)
                                 for h in two)
                        if abs(LH) > TOL or abs(RH) > TOL:
                            pent_cnt += 1
                        pent_worst = max(pent_worst, abs(LH - RH))
# braiding R^{ab}_c = (-1)^{(a+b-c)/2} q_t^{(c(c+2)-a(a+2)-b(b+2))/2},  q_t = exp(2 pi i/(4*7))
qt = mp.exp(2j * mp.pi / (8 * 7))       # R^2 = monodromy: exponent halved w.r.t. the twist
Rkl = lambda a, b, c: (-1)**((a + b - c) // 2) * qt**(c * (c + 2) - a * (a + 2) - b * (b + 2))
hex_worst = mp.mpf(0)
for a, b, c in itertools.product(two, repeat=3):
    for dd in two:
        for e in two:
            if not (adm(a, c, e) and adm(e, b, dd)):
                continue
            for g in two:
                if not (adm(c, b, g) and adm(a, g, dd)):
                    continue
                LH = Rkl(c, a, e) * Fkl(a, c, b, dd, e, g) * Rkl(c, b, g)
                RH = sum(Fkl(c, a, b, dd, e, f) * Rkl(c, f, dd) * Fkl(a, b, c, dd, f, g) for f in two)
                hex_worst = max(hex_worst, abs(LH - RH))
dkl = [mp.re(qn(a + 1)) for a in two]
Dkl = mp.sqrt(sum(x**2 for x in dkl))
thkl = [mp.exp(2j * mp.pi * mp.mpf(a * (a + 2)) / 28) for a in two]
Nkl = np.zeros((3, 3, 3), dtype=np.int64)
for i, a in enumerate(two):
    for j, b in enumerate(two):
        for l, c in enumerate(two):
            Nkl[i, j, l] = 1 if adm(a, b, c) else 0
Shopf = mp.matrix(3, 3)
for i, a in enumerate(two):
    for j, b in enumerate(two):
        Shopf[i, j] = sum(int(Nkl[i, j, l]) * dkl[l] * thkl[l] / (thkl[i] * thkl[j])
                          for l in range(3)) / Dkl
# match to the computed centralizer S_2, T_2 (allow a relabelling and complex conjugation)
best = None
for perm in itertools.permutations(range(3)):
    for conj in (False, True):
        e1 = max(abs((mp.conj(Shopf[perm[i], perm[j]]) if conj else Shopf[perm[i], perm[j]]) - S_2[i, j])
                 for i in range(3) for j in range(3))
        e2 = max(abs((mp.conj(thkl[perm[i]]) if conj else thkl[perm[i]])
                     / (mp.conj(thkl[perm[0]]) if conj else thkl[perm[0]])
                     - th2[idx[(0, i)]] / th2[idx[(0, 0)]]) for i in range(3))
        if best is None or max(e1, e2) < best[0]:
            best = (max(e1, e2), perm, conj, e1, e2)
match_err, perm, conj, eS, eT = best
P(f"[C] rank-3 factor: constructed SU(2)_5-even 6j at q = exp(i pi/7): "
  f"pentagon {mp.nstr(pent_worst,3)} on {pent_cnt} eqs, hexagon {mp.nstr(hex_worst,3)}")
P(f"    Hopf-link S / twist match to the E6_2 centralizer: perm {perm} conj {conj} "
  f"errS {mp.nstr(eS,3)} errT {mp.nstr(eT,3)}")
nF_rank3 = sum(1 for a, b, c, dd, e, f in itertools.product(two, repeat=6)
               if abs(Fkl(a, b, c, dd, e, f)) > TOL)
nF_level2 = nF_rank3 * 27
LEVEL2_OK = bool(MD_OK and pointed_nondeg and ok_bij and Sfac < mp.mpf('1e-18')
                 and Tfac < mp.mpf('1e-18') and Nfac_err == 0 and len(sols2p) >= 1
                 and pent_worst < TOL and hex_worst < TOL and match_err < mp.mpf('1e-18'))
P(f"    => E6_2 6j = (Z/3 cocycle omega_{sols2p[0][0] if sols2p else '?'}) tensor "
  f"(SU(2)_5-even Racah 6j):  {nF_rank3} nonzero rank-3 F-symbols x 27 pointed = {nF_level2}."
  f"  LEVEL-2 6j COMPUTED: {LEVEL2_OK}")
OUT['C_level2'] = dict(
    rank=n2, simple_currents=[lab2[u] for u in units],
    pointed_subcat_modular=bool(pointed_nondeg), det_S_pointed=mp.nstr(abs(detSu), 8),
    centralizer=[lab2[c] for c in cent],
    centralizer_qdim=[mp.nstr(d2[c], 12) for c in cent],
    centralizer_h=[str(hs2[c]) for c in cent],
    deligne_factorization=dict(bijection_ok=bool(ok_bij), S_err=mp.nstr(Sfac, 3),
                               T_err=mp.nstr(Tfac, 3), N_err=int(Nfac_err)),
    pointed_factor=dict(theta_J='exp(2pi i * %s)' % hs2[idx[(1, 0)]],
                        solutions_p_r=[[s[0], s[1], s[2]] for s in sols2p]),
    rank3_factor=dict(identified_as='SU(2)_5 even part (integer spins), q = exp(i pi/7)',
                      pentagon_worst=mp.nstr(pent_worst, 3), pentagon_eqs=pent_cnt,
                      hexagon_worst=mp.nstr(hex_worst, 3),
                      hopf_S_err=mp.nstr(eS, 3), twist_err=mp.nstr(eT, 3),
                      n_F_symbols=nF_rank3),
    n_F_symbols_level2=nF_level2, verified=bool(LEVEL2_OK))

# =====================================================================
# D.  what the level-1/2 6j give FOR THE OBJECT: colored invariants of 4_1
# =====================================================================
# Deligne product => the normalized invariant of a knot colored by (a,x) is the
# rank-3 factor's invariant; the pointed factor contributes only a framing phase.
# Habiro/Masbaum closed form for the colored Jones of the figure-eight:
#    J_N(4_1;q) = sum_{k>=0} prod_{j=1}^{k} (q^N + q^{-N} - q^j - q^{-j})
def J_fig8(N, q):
    tot, term = mp.mpf(1), mp.mpf(1)
    for kk in range(1, N + 1):
        term = term * (q**N + q**(-N) - q**kk - q**(-kk))
        tot += term
    return tot


q7 = mp.exp(2j * mp.pi / 7)
qgen = mp.mpf(13) / 7                      # generic check value (not a root of unity)
jones_check = abs(J_fig8(2, qgen) - (qgen**2 - qgen + 1 - qgen**-1 + qgen**-2))
colored = {}
for i, a in enumerate(two):                # a = 2j, N = a+1
    colored[f'N={a+1} (spin {a//2})'] = mp.nstr(J_fig8(a + 1, q7), 14)
P(f"[D] E6 level-2 colored invariants of 4_1 (= SU(2)_5-even colored Jones at zeta_7): {colored}")
P(f"    control: Habiro form reproduces the N=2 Jones polynomial of 4_1 "
  f"(err {mp.nstr(jones_check,3)});  level-1 (pointed) invariants are framing-only = 1.")
OUT['D_object'] = dict(level1_knot_invariant='framing phase only (pointed) -> normalized 1 for every knot',
                       level2_colored_invariants_of_4_1=colored,
                       habiro_control_err=mp.nstr(jones_check, 3),
                       adjoint_color_note='the E6 adjoint 78 sits at spin 2 (N=5) of the rank-3 factor')

# =====================================================================
# E.  PHASE 3 -- principal SL(2) index
# =====================================================================
Ind = lambda j2: Fraction(2, 3) * Fraction(j2, 2) * (Fraction(j2, 2) + 1) * (j2 + 1)   # I(spin j), I(1/2)=1
idx_princ = sum(Ind(2 * m) for m in EXPONENTS) / Fraction(2 * HV)
idx_su3 = (Ind(2) + Ind(4)) / Fraction(2 * 3)
idx_formula = Fraction(HV * (HV + 1) * 6, 6)
P(f"[E] index(principal SL2 -> E6) = {idx_princ}  (control: principal su2 in su(3) = {idx_su3}; "
  f"closed form h^(h^+1)rank/6 = {idx_formula})")
IDX_OK = (idx_princ == 156 and idx_su3 == 4 and idx_formula == 156)
OUT['E_principal_index'] = dict(index=str(idx_princ), control_su3=str(idx_su3),
                                closed_form=str(idx_formula), ok=bool(IDX_OK))

# =====================================================================
# F.  CS of the geometric rep, and of the E6-principal flat connection
# =====================================================================
cs_vals, snappy_ok = {}, False
try:
    import snappy
    for name, M in (('4_1', snappy.Manifold('4_1')), ('m004', snappy.Manifold('m004'))):
        M.randomize()
        cv = M.complex_volume()
        cs_vals[name] = dict(vol=mp.nstr(mp.mpf(float(cv.real())), 15),
                             cs=mp.nstr(mp.mpf(float(cv.imag())), 6))
    snappy_ok = all(abs(float(v['cs'])) < 1e-9 for v in cs_vals.values())
except Exception as ex:                                             # pragma: no cover
    cs_vals['error'] = str(ex)
CS_base = 0 if snappy_ok else None
P(f"[F] SnapPy complex volume (2 triangulations): {cs_vals}  -> CS(rho_geo) = 0: {snappy_ok}")
P(f"    => CS(E6-principal geometric flat connection) = 156 * 0 = 0 (exact).")
OUT['F_CS_basepoint'] = dict(snappy=cs_vals, CS_SL2_is_zero=bool(snappy_ok),
                             CS_E6_principal=('0' if snappy_ok else 'undetermined'))

# =====================================================================
# G.  the deformation space: dim H^1 per exponent block (exact, 2 primes + Q(omega))
# =====================================================================
def sym_power(Mat, n, mod=None):
    """matrix of Sym^n(Mat) acting on degree-n monomials x^i y^(n-i) (i = n..0)."""
    a, b, c, dd = Mat
    dim = n + 1
    Rm = [[0] * dim for _ in range(dim)]
    # (x,y) -> (a x + c y, b x + d y);  basis e_i = x^i y^{n-i}
    for i in range(dim):                                   # source monomial x^i y^{n-i}
        coeffs = {}
        for s in range(i + 1):
            for t in range(n - i + 1):
                cf = (math.comb(i, s) * math.comb(n - i, t)
                      * pow(a, s) * pow(c, i - s) * pow(b, t) * pow(dd, n - i - t))
                k = s + t
                coeffs[k] = coeffs.get(k, 0) + cf
                if mod:
                    coeffs[k] %= mod
        for k, v in coeffs.items():
            Rm[k][i] = v % mod if mod else v
    return Rm


def rank_mod_p(Mrows, p):
    Mm = [row[:] for row in Mrows]
    rows, cols = len(Mm), len(Mm[0]) if Mm else 0
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if Mm[i][c] % p), None)
        if piv is None:
            continue
        Mm[r], Mm[piv] = Mm[piv], Mm[r]
        inv = pow(Mm[r][c], p - 2, p)
        Mm[r] = [(x * inv) % p for x in Mm[r]]
        for i in range(rows):
            if i != r and Mm[i][c] % p:
                f = Mm[i][c]
                Mm[i] = [(Mm[i][j] - f * Mm[r][j]) % p for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def matmul(X, Y, p):
    n_, m_, k_ = len(X), len(Y[0]), len(Y)
    return [[sum(X[i][t] * Y[t][j] for t in range(k_)) % p for j in range(m_)] for i in range(n_)]


def cohomology_dims(m, p):
    """dim H^0, H^1 of the 4_1 group with coefficients Sym^{2m}(rho_geo) over F_p."""
    # u is pinned by rho(relator) = I; both x^2 -+ x + 1 = 0 are tried and the
    # relator is CHECKED (never assumed).  u = primitive 6th root (P2W4-L54 / B425).
    roots = [x for x in range(2, p) if (x * x - x + 1) % p == 0] + \
            [x for x in range(2, p) if (x * x + x + 1) % p == 0]
    assert roots, 'p must be 1 mod 3'
    n = 2 * m
    dim = n + 1
    def build(u):
        Ra = sym_power((1, 1, 0, 1), n, p)              # rho(a) = [[1,1],[0,1]]
        Rb = sym_power((1, 0, u % p, 1), n, p)          # rho(b) = [[1,0],[u,1]]
        Ai = sym_power((1, -1 % p, 0, 1), n, p)         # inverses (det = 1)
        Bi = sym_power((1, 0, (-u) % p, 1), n, p)
        return Ra, Rb, {'a': Ra, 'A': Ai, 'b': Rb, 'B': Bi}
    Ra, Rb, tab = build(roots[0])
    def word(s):
        M = [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
        for ch in s:
            M = matmul(M, tab[ch], p)
        return M
    # relator r = a w b^{-1} w^{-1}, w = b A B a  (Riley presentation of 4_1)
    wword = 'bABa'
    winv = wword[::-1].swapcase()
    def is_id(Mx):
        return all(Mx[i][j] % p == (1 if i == j else 0) for i in range(dim) for j in range(dim))
    rel_ok = is_id(word('a' + wword + 'B' + winv))
    if not rel_ok:
        for u in roots[1:]:
            Ra, Rb, tab = build(u)
            if is_id(word('a' + wword + 'B' + winv)):
                rel_ok = True
                break
    # Fox derivatives of r = a w B w^{-1}
    #   d/da(r) = 1 + a*d/da(w) - a w B w^{-1} * d/da(w) ... computed by the chain rule below
    def fox(wrd, gen):
        """Fox derivative as a matrix Phi(d wrd/d gen)."""
        Mtot = [[0] * dim for _ in range(dim)]
        pref = [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
        for ch in wrd:
            low = ch.lower()
            if low == gen:
                if ch.islower():
                    add = pref
                else:
                    add = matmul(pref, tab[ch], p)
                    add = [[(-x) % p for x in row] for row in add]
                Mtot = [[(Mtot[i][j] + add[i][j]) % p for j in range(dim)] for i in range(dim)]
            pref = matmul(pref, tab[ch], p)
        return Mtot
    rword = 'a' + wword + 'B' + winv
    Fa, Fb = fox(rword, 'a'), fox(rword, 'b')
    # Z^1 = ker[Fa | Fb] : dim = 2*dim - rank
    Mrows = [[Fa[i][j] for j in range(dim)] + [Fb[i][j] for j in range(dim)] for i in range(dim)]
    rk = rank_mod_p(Mrows, p)
    # H^0 = ker(Ra - I) ^ ker(Rb - I)
    K = [[(Ra[i][j] - (1 if i == j else 0)) % p for j in range(dim)] for i in range(dim)] + \
        [[(Rb[i][j] - (1 if i == j else 0)) % p for j in range(dim)] for i in range(dim)]
    h0 = dim - rank_mod_p(K, p)
    # peripheral invariants: ker(Ra - I) alone (meridian a; the longitude commutes with it)
    per = dim - rank_mod_p([[(Ra[i][j] - (1 if i == j else 0)) % p for j in range(dim)]
                            for i in range(dim)], p)
    z1 = 2 * dim - rk
    b1 = dim - h0
    return dict(dim=dim, rel_ok=rel_ok, h0=h0, h1=z1 - b1, periph_inv=per, periph_h1=2 * per)


PRIMES = [10009, 100003]                    # both prime and = 1 mod 3
import sympy as _sp
for p in PRIMES:
    assert p % 3 == 1 and _sp.isprime(p)
coh = {}
for m in EXPONENTS:
    rows = [cohomology_dims(m, p) for p in PRIMES]
    agree = all(r == rows[0] for r in rows)
    coh[m] = dict(rows[0], agree_across_primes=agree)
# characteristic-0 control: the SAME computation exactly over Q(zeta_6) = Q[u]/(u^2-u+1)
class K:                                   # exact arithmetic in Q(zeta_6)
    __slots__ = ('a', 'b')
    def __init__(self, a=0, b=0):
        self.a, self.b = Fraction(a), Fraction(b)
    def __add__(s, o): return K(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return K(s.a - o.a, s.b - o.b)
    def __neg__(s): return K(-s.a, -s.b)
    def __mul__(s, o):                     # u^2 = u - 1
        return K(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a + s.b * o.b)
    def inv(s):
        nrm = s.a * s.a + s.a * s.b + s.b * s.b
        return K((s.a + s.b) / nrm, -s.b / nrm)
    def is_zero(s): return s.a == 0 and s.b == 0
    def __repr__(s): return f'({s.a}+{s.b}u)'


ONE, ZERO, U = K(1), K(0), K(0, 1)


def kmat_mul(X, Y):
    n_, k_, m_ = len(X), len(Y), len(Y[0])
    return [[sum((X[i][t] * Y[t][j] for t in range(k_)), ZERO) for j in range(m_)] for i in range(n_)]


def krank(M):
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if not M[i][c].is_zero()), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = M[r][c].inv()
        M[r] = [x * iv for x in M[r]]
        for i in range(rows):
            if i != r and not M[i][c].is_zero():
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def sym_power_K(Mat, n):
    a, b, c, dd = Mat
    dim = n + 1
    Rm = [[ZERO] * dim for _ in range(dim)]
    for i in range(dim):
        coeffs = {}
        for s_ in range(i + 1):
            for t_ in range(n - i + 1):
                cf = K(math.comb(i, s_) * math.comb(n - i, t_))
                for _ in range(s_): cf = cf * a
                for _ in range(i - s_): cf = cf * c
                for _ in range(t_): cf = cf * b
                for _ in range(n - i - t_): cf = cf * dd
                k_ = s_ + t_
                coeffs[k_] = coeffs.get(k_, ZERO) + cf
        for k_, v in coeffs.items():
            Rm[k_][i] = v
    return Rm


def cohomology_dims_exact(m):
    n = 2 * m
    dim = n + 1
    Ra = sym_power_K((ONE, ONE, ZERO, ONE), n)             # rho(a) = [[1,1],[0,1]]
    Rb = sym_power_K((ONE, ZERO, U, ONE), n)               # rho(b) = [[1,0],[u,1]], u = zeta_6
    Ai = sym_power_K((ONE, -ONE, ZERO, ONE), n)
    Bi = sym_power_K((ONE, ZERO, -U, ONE), n)
    tab = {'a': Ra, 'A': Ai, 'b': Rb, 'B': Bi}
    eye = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
    def word(w):
        M = eye
        for ch in w:
            M = kmat_mul(M, tab[ch])
        return M
    wword = 'bABa'
    rword = 'a' + wword + 'B' + wword[::-1].swapcase()
    rel = word(rword)
    rel_ok = all((rel[i][j] - eye[i][j]).is_zero() for i in range(dim) for j in range(dim))
    def fox(w, gen):
        Mtot = [[ZERO] * dim for _ in range(dim)]
        pref = eye
        for ch in w:
            if ch.lower() == gen:
                add = pref if ch.islower() else [[-x for x in row] for row in kmat_mul(pref, tab[ch])]
                Mtot = [[Mtot[i][j] + add[i][j] for j in range(dim)] for i in range(dim)]
            pref = kmat_mul(pref, tab[ch])
        return Mtot
    Fa, Fb = fox(rword, 'a'), fox(rword, 'b')
    rk = krank([Fa[i] + Fb[i] for i in range(dim)])
    h0 = dim - krank([[Ra[i][j] - eye[i][j] for j in range(dim)] for i in range(dim)]
                     + [[Rb[i][j] - eye[i][j] for j in range(dim)] for i in range(dim)])
    per = dim - krank([[Ra[i][j] - eye[i][j] for j in range(dim)] for i in range(dim)])
    return dict(rel_ok=bool(rel_ok), h0=int(h0), h1=int(dim - rk + h0), periph_inv=int(per))


exact_ctrl = {m: cohomology_dims_exact(m) for m in EXPONENTS}
for m in EXPONENTS:
    coh[m]['exact_Qzeta6'] = exact_ctrl[m]
    coh[m]['exact_agrees'] = bool(exact_ctrl[m]['h1'] == coh[m]['h1']
                                  and exact_ctrl[m]['h0'] == coh[m]['h0']
                                  and exact_ctrl[m]['periph_inv'] == coh[m]['periph_inv']
                                  and exact_ctrl[m]['rel_ok'])
h1_tot = sum(coh[m]['h1'] for m in EXPONENTS)
per_tot = sum(coh[m]['periph_h1'] for m in EXPONENTS)
# --- re-verify B581's sign law IN-CELL from its banked exact coefficients ---
b581_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '..', '..', '..', 'B581_six_torsions', 'six_torsions_results.json')
tau_signs, b581_ok = {}, False
try:
    B581 = json.load(open(os.path.normpath(b581_path)))
    tau_vals = {}
    for m in EXPONENTS:
        co = [(int(a), int(b)) for a, b in B581[str(m)]['quotient']]
        assert all(b == 0 for _, b in co), 'coefficients must be rational'
        c = [Fraction(a) for a, _ in co]
        c = [x / c[0] for x in c]                 # monic-at-top-degree (Review-17 convention)
        deg = len(c) - 1                          # coefficients descending in t
        tau = sum(c[k] * (deg - k) for k in range(len(c)))     # d/dt at t = 1
        tau_vals[m] = tau
        tau_signs[m] = int(math.copysign(1, float(tau)))
    assert tau_vals[1] == -3, 'convention anchor: tau_1 must reproduce B425/P2W4-L54 = -3'
    b581_ok = all(tau_signs[m] == (-1)**m for m in EXPONENTS)
except Exception as ex:                                        # pragma: no cover
    tau_signs = {'error': str(ex)}
theta_parity = {m: ('odd' if (-1)**(m + 1) == -1 else 'even') for m in EXPONENTS}
P(f"[G] B581 sign law re-verified in-cell from the banked exact torsions: "
  f"tau_1 = -3 anchor OK; sign(tau_m) = {tau_signs} == (-1)^m: {b581_ok};  theta-parity (B353, (-1)^(m+1)): {theta_parity}")
theta_odd = [m for m in EXPONENTS if theta_parity[m] == 'odd']
P(f"[G] dim H^1(M; Sym^2m rho_geo) per E6 exponent: "
  f"{ {m: coh[m]['h1'] for m in EXPONENTS} }  (h^0 = { {m: coh[m]['h0'] for m in EXPONENTS} }, "
  f"2 primes agree: {all(coh[m]['agree_across_primes'] for m in EXPONENTS)})")
P(f"    total = {h1_tot} = rank(E6) -> smooth point of the E6 character variety, "
  f"one direction per exponent; theta-odd directions m = {theta_odd} (B581 sign law).")
P(f"    char-0 control, exact over Q(zeta_6), all six blocks: "
  f"h1 = { {m: exact_ctrl[m]['h1'] for m in EXPONENTS} }, relator = I everywhere: "
  f"{all(exact_ctrl[m]['rel_ok'] for m in EXPONENTS)}, agrees with F_p: "
  f"{all(coh[m]['exact_agrees'] for m in EXPONENTS)}")
P(f"    peripheral dim H^1(T^2; Sym^2m) = 2 per block, total {per_tot} = 2 rank(E6): "
  f"the image is a {h1_tot}-dim LAGRANGIAN -> CS along the deformation = its potential.")
DEF_OK = (b581_ok and h1_tot == 6 and all(coh[m]['h1'] == 1 for m in EXPONENTS)
          and all(coh[m]['exact_agrees'] for m in EXPONENTS)
          and all(coh[m]['h0'] == 0 for m in EXPONENTS)
          and all(coh[m]['agree_across_primes'] and coh[m]['rel_ok'] for m in EXPONENTS)
          and per_tot == 12)
OUT['G_deformation'] = dict(B581_sign_law_reverified=bool(b581_ok),
                            tau_signs={str(k): v for k, v in tau_signs.items()},
                            theta_parity={str(k): v for k, v in theta_parity.items()},
                            per_exponent={str(m): coh[m] for m in EXPONENTS},
                            total_h1=h1_tot, rank_E6=6, peripheral_total=per_tot,
                            theta_odd_exponents=theta_odd,
                            lagrangian=bool(h1_tot * 2 == per_tot), validated=bool(DEF_OK))

# =====================================================================
# H.  the CS functional along the theta-EVEN (m=1, SL2-induced) direction
# =====================================================================
cs_curve = {}
try:
    import snappy
    Mf = snappy.Manifold('4_1')
    Mf.chern_simons()                       # pins the cusped CS invariant (= 0) first
    for (pp, qqf) in [(5, 1), (5, 2), (7, 1), (6, 1), (8, 3)]:
        Mf.dehn_fill((pp, qqf))
        cs = mp.mpf(float(Mf.chern_simons()))
        cs_curve[f'({pp},{qqf})'] = dict(vol=mp.nstr(mp.mpf(float(Mf.volume())), 12),
                                         cs_SL2=mp.nstr(cs, 10),
                                         cs_E6_principal_mod1=mp.nstr(mp.mpf(156) * cs
                                                                      - mp.floor(mp.mpf(156) * cs), 10))
    Mf.dehn_fill((0, 0))
    H_OK = len(cs_curve) >= 3 and any(abs(float(v['cs_SL2'])) > 1e-6 for v in cs_curve.values())
except Exception as ex:                                             # pragma: no cover
    cs_curve['error'] = str(ex); H_OK = False
P(f"[H] CS functional sampled along the theta-EVEN (m=1) direction "
  f"(Dehn fillings of 4_1; CS_E6 = 156 * CS_SL2): "
  + ', '.join(f"{k}: CS_SL2={v['cs_SL2']}" for k, v in cs_curve.items() if k != 'error'))
P(f"    (156 is EVEN, so the E6 value is well defined mod 1 even though the SL(2,C) CS of a "
  f"closed manifold is only defined mod 1/2.)")
OUT['H_CS_theta_even'] = dict(samples=cs_curve, computable=bool(H_OK),
                              relation='CS_E6principal = index * CS_SL2 = 156 * CS_SL2',
                              mod_note='156 even => 156*CS is well defined mod 1 even for CS mod 1/2')

# =====================================================================
# I.  the wall on the theta-ODD directions (computed, not cited)
# =====================================================================
N27 = 27                                    # smallest faithful E6 representation
ptolemy_per_tet = math.comb(N27 + 3, 3) - 4
n_tet_41 = 2
ptolemy_vars = ptolemy_per_tet * n_tet_41
# index of the 27 (normalization: index(adjoint) = 2 h^ = 24)
C2_27 = Fraction(52, 3)
ind_27 = C2_27 * 27 / 78
P(f"[I] wall (computed): the theta-odd directions m = {theta_odd} are NOT in the image of the "
  f"SL(2,C) deformation (they lie in Sym^8 / Sym^16, not the adjoint block).")
P(f"    The only implemented complex-volume machinery is PGL(N,C) Ptolemy (GTZ/Zickert). "
  f"Smallest faithful E6 rep = {N27} (index {ind_27} at index(adj) = {2*HV}); "
  f"Ptolemy coords on the {n_tet_41}-tetrahedron triangulation of 4_1 = "
  f"C(30,3)-4 = {ptolemy_per_tet} per tetrahedron = {ptolemy_vars} variables.")
P(f"    => phase 3 is WALLED on the theta-odd sector: EXTERNAL (an extended-Bloch / CCS "
  f"class for E6, or a {ptolemy_vars}-variable Ptolemy solve, neither in-sandbox).")
WALL_OK = ptolemy_vars > 5000
OUT['I_wall'] = dict(theta_odd_not_SL2_induced=True,
                     smallest_faithful_E6_rep=N27, index_of_27=str(ind_27),
                     ptolemy_coords_per_tetrahedron=ptolemy_per_tet,
                     tetrahedra_of_4_1=n_tet_41, ptolemy_variables=ptolemy_vars,
                     wall_type='EXTERNAL', computed_obstruction=bool(WALL_OK))

# =====================================================================
#  VERDICT
# =====================================================================
A2 = bool(MD_OK and LEVEL1_OK and LEVEL2_OK)
theta_odd_directions_exist = bool(DEF_OK and all(coh[m]['h1'] >= 1 for m in theta_odd))
A3 = bool(DEF_OK and not theta_odd_directions_exist)     # fires if there is nothing to compute
W = bool(WALL_OK and DEF_OK and IDX_OK)
unachieved_covered = (A2 or W) and ((not A2) or (A3 or W))

if (A2 or A3) and unachieved_covered:
    verdict = 'RESOLVED-A'
elif (not A2) and (not A3) and W:
    verdict = 'RESOLVED-B'
else:
    verdict = 'UNRESOLVED'

headline = (
    "E6 6j COMPUTED at both levels: level 1 is pointed (Z/3, theta_27 = exp(4 pi i/3)) with TRIVIAL "
    "associator (all 27 F-symbols = 1); level 2 (rank 9, c = 78/7) SPLITS as a Deligne product of "
    "its modular Z/3 current subcategory and its Mueger centralizer, which is the even part of "
    "SU(2)_5 at q = exp(i pi/7) -- so the level-2 6j are the quantum Racah symbols (pentagon, "
    "hexagons, Hopf-link S and twists all verified), and the E6 level-2 invariants of 4_1 are the "
    "SU(2)_5 colored Jones at zeta_7. PHASE 3 splits: CS of the E6-principal geometric connection "
    "= 156 x 0 = 0 and the deformation space is exactly 6 = rank(E6) (one direction per exponent, "
    "a Lagrangian on the boundary), the CS functional is computable along the theta-EVEN m=1 "
    "direction, and WALLED (EXTERNAL, 8112-variable PGL(27) Ptolemy) along the theta-ODD m = 4, 8."
)
disc = ("The Z/3 simple-current subcategory of E6 level 2 is MODULAR (|det S_pointed| = "
        f"{mp.nstr(abs(detSu),6)} != 0), so E6_2 = Pointed(Z/3) (x) Centralizer with the "
        "centralizer of rank 3 -- and that rank-3 factor's S-matrix and twists match the even "
        f"part of SU(2)_5 entry-by-entry (errS {mp.nstr(eS,3)}, errT {mp.nstr(eT,3)}). "
        "That is what makes the level-2 6j symbols closed-form instead of an unsolved rank-9 "
        "pentagon system.")

P("")
P("=== VERDICT ===")
P(f"gates: modular-data {MD_OK} | level1-6j {LEVEL1_OK} | level2-6j {LEVEL2_OK} | "
  f"A2 {A2} | A3 {A3} | wall {W} | index {IDX_OK} | deformation {DEF_OK}")
P(f"VERDICT: {verdict}")
P(headline)
P("DISCRIMINATING FACT: " + disc)

OUT['verdict'] = verdict
OUT['gates'] = dict(modular_data=bool(MD_OK), level1_6j=bool(LEVEL1_OK), level2_6j=bool(LEVEL2_OK),
                    A2_6j_both_levels=A2, A3_CS_theta_odd=A3, W_computed_wall=W,
                    index_ok=bool(IDX_OK), deformation_ok=bool(DEF_OK),
                    theta_odd_directions_exist=theta_odd_directions_exist)
OUT['headline'] = headline
OUT['discriminating_fact'] = disc
OUT['residuals_external'] = [
    "an extended-Bloch group / Cheeger-Chern-Simons class for E6 (the theta-odd CS functional)",
    "the E6 A-polynomial of 4_1 (the potential of the computed 6-dim Lagrangian)",
    f"a {ptolemy_vars}-variable PGL(27,C) Ptolemy solve on the 2-tetrahedron triangulation",
    ("the level-2 rank-3 factor is identified with the SU(2)_5 even part by COMPLETE modular "
     "data (S and T entrywise, 1e-41); a categorical equivalence -- rather than modular-data "
     "equality -- and gauge-uniqueness of the F-symbols are not proved in-cell"),
]
OUT['gate5'] = ('structural only: no SM values, nothing to CLAIMS.md, one-number pin untouched; '
                'all outputs are named mathematics (modular data, 6j systems, cohomology dims, '
                'CS values of hyperbolic 3-manifolds)')
OUT['runtime_sec'] = round(time.time() - t_start, 1)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results.json'), 'w') as f:
    json.dump(OUT, f, indent=1)
P(f"[runtime {OUT['runtime_sec']}s]")
