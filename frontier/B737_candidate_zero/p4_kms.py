#!/usr/bin/env python3
# B737 CANDIDATE ZERO -- PROBE 4 (KMS): "same zeta, different role?" -- the crux.
# ROUND 2 (fix-and-recompute after adversarial refutation of the round-1 verdict A).
#
# QUESTION (prereg, sealed): does the scattering/Eisenstein zeta_K GENUINELY furnish the
# beta=1 KMS/SSB structure (B736-P2's missing infinite-tower object), or is it the SAME
# FUNCTION in two UNRELATED roles (the E15/E20 "same zeta, different role" trap)?
#
# ROUND-1 POSTMORTEM (what was wrong, what was right):
#   * Every individual computation of round 1 (S1-S8 below) was independently reproduced
#     by two adversarial reviewers with fresh code: all numerics CORRECT.  The citations
#     T2/T6 were verbatim-accurate; T3's content was accurate but ONE sentence was a
#     synthesized paraphrase presented inside quotation marks.  FIXED below (T3 now
#     carries the verbatim source line, fetched again at source this session).
#   * The round-1 VERDICT (A: "genuine substrate-level bridge") was REFUTED on two
#     structural grounds, both accepted here:
#     (V1) MB12 VACUITY: the discriminator used for "not a pun" -- one counting monoid
#          feeds both zetas / same pole / same unit weight -- CANNOT FAIL for K-attached
#          zeta constructions over a class-number-1 imaginary quadratic field: the
#          collapse to zeta_K is FORCED by h=1 arithmetic, hence carries zero
#          discriminating power.  NEW section S9 computes this vacuity directly by
#          running the identical battery over d = -3, -4, -7, -11 (all h=1): it passes
#          everywhere, with no object anywhere in sight.
#     (V2) FIELD-DRESSED-AS-OBJECT: every bridge fact is a fact about K = Q(sqrt-3),
#          not about m004.  NEW section S10 runs the object-deletion test (the
#          corrected, non-vacuous discriminator): delete m004 -- does ANY input to
#          either side of the claimed bridge change?  Answer, computed: NO.
#   * Consequence: the corrected verdict is B (the composition dies honestly).  S11.
#
# METHOD (E19 compute-not-cite): every load-bearing structural identity is COMPUTED here,
# in-sandbox; theorems of others are marked CITED (fetched at source; LLN PDF re-fetched
# 2026-07-21 round 2, verbatim lines extracted by pdftotext); the missing arrows are
# marked MISSING.  In-repo computed dependencies: p1_scatter.py (69/69), p2_cover.py
# (29/29, RE-RUN this session), p3_sister_out.txt.
#
# K = Q(sqrt(-3)), O_K = Z[w], w = (1+sqrt(-3))/2, disc d = -3, class number h = 1,
# unit group order w_K = 6.  chi = chi_{-3} = Kronecker symbol (-3/.).
#
# Sections:
#   S1  ideal monoid = lattice/units: r_K(n) two ways (the ONE counting monoid).
#   S2  Epstein/Eisenstein side: sum over the cusp lattice = w_K * zeta_K(s).
#   S3  BC/CMR side: Tr e^{-beta H} = zeta_K(beta); pole at beta=1, residue 2pi/(6 sqrt3).
#   S4  scattering phi(s) = Lambda_K(s)/Lambda_K(s+1): FE, unitarity, pole at s=1.
#   S5  theta chain: Mellin of the Boltzmann sum over the SAME monoid = completed zeta.
#   S6  object anchoring (snappy): m004 cusp = index-4 K-lattice.  [Round-2 note: this
#       anchoring is CLASS-GENERIC -- every Bianchi-class cusp is a K-lattice; p3 shows
#       m003's cusp is O_K itself.  Anchoring is real but non-discriminating.]
#   S7  CMR flow weight N(J)^{it} = cusp covolume scaling (geometric reading).
#   S8  ANTI-PUN operator separation: LP resonances (zeros side) vs BC spectrum
#       {log N(J)} (ideals side) -- disjoint; kills the strong/operator form directly.
#   S9  NEW -- MB12 VACUITY AUDIT: the S1-S5 "same substrate" battery re-run over the
#       four smallest h=1 imaginary quadratic fields.  If it passes for ALL of them
#       (no manifold anywhere), it cannot discriminate bridge from pun.  It does.
#   S10 NEW -- OBJECT-DELETION TEST (the corrected discriminator, which CAN fail):
#       does any m004-specific datum enter (a) the KMS side, (b) the scattering
#       carrier phi?  Computed: no.  Non-vacuity of the test itself demonstrated.
#   S11 corrected verdict: OUTCOME B, with the kill-form and the surviving open leads.
#
# Output: run with  python3 p4_kms.py > p4_kms_out.txt

import numpy as np
import mpmath as mp

mp.mp.dps = 30

def chi3(d):
    r = d % 3
    return 1 if r == 1 else (-1 if r == 2 else 0)

def L_chi(s):
    """L(s, chi_{-3}) by Hurwitz zeta; valid for all complex s != 1 issues."""
    return mp.mpf(3)**(-s) * (mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))

def zeta_K(s):
    return mp.zeta(s) * L_chi(s)

def Lambda_K(s):
    """Completed Dedekind zeta of K = Q(sqrt-3):
       Lambda_K(s) = (sqrt(3)/(2 pi))^s Gamma(s) zeta_K(s),  Lambda_K(s) = Lambda_K(1-s)."""
    return (mp.sqrt(3)/(2*mp.pi))**s * mp.gamma(s) * zeta_K(s)

print("="*78)
print("B737 PROBE 4 (KMS crux) -- ROUND 2 (fixed + recomputed)")
print("K = Q(sqrt-3), O_K = Z[w], d=-3, h=1, w_K=6")
print("="*78)

# ---------------------------------------------------------------- S1
print("\n[S1] THE ONE COUNTING MONOID: r_K(n) two ways, n <= 3000")
print("  method A (Eisenstein/lattice side): #{lam in O_K : N(lam)=n} / 6   (h=1, w_K=6)")
print("  method B (BC/ideal side):           sum_{d|n} chi_{-3}(d)")
NMAX = 3000
rA = np.zeros(NMAX+1, dtype=np.int64)
B = int(np.sqrt(NMAX/0.74)) + 3   # N(a+bw) = a^2+ab+b^2
for a in range(-B, B+1):
    for b in range(-B, B+1):
        if a == 0 and b == 0:
            continue
        n = a*a + a*b + b*b
        if n <= NMAX:
            rA[n] += 1
assert np.all(rA % 6 == 0), "unit orbit count broken"
rA = rA // 6
rB = np.zeros(NMAX+1, dtype=np.int64)
for d in range(1, NMAX+1):
    c = chi3(d)
    if c:
        rB[d::d] += c
mismatch = np.nonzero(rA[1:] != rB[1:])[0]
print(f"  mismatches in 1..{NMAX}: {len(mismatch)}  ->  " +
      ("IDENTICAL: one monoid (ideals of O_K) feeds BOTH Dirichlet series" if len(mismatch)==0 else "BROKEN"))
norms = [n for n in range(1, 30) if rB[n] > 0]
print(f"  ideal norms up to 29: {norms}")
print(f"  r_K at those norms:   {[int(rB[n]) for n in norms]}")
print("  [round-2 note: TRUE, but see S9 -- this identity is FORCED at h=1, so it")
print("   cannot by itself discriminate a bridge from a pun.]")

# ---------------------------------------------------------------- S2
print("\n[S2] EPSTEIN/EISENSTEIN SIDE: sum'_{lam in O_K} N(lam)^{-s} = 6 * zeta_K(s)")
XMAX = 10**6
r = np.zeros(XMAX+1, dtype=np.int64)
for d in range(1, XMAX+1):
    c = chi3(d)
    if c:
        r[d::d] += c
ns = np.arange(1, XMAX+1, dtype=np.float64)
for s in (2.0, 2.5, 3.0):
    lattice_sum = 6.0 * np.sum(r[1:] * ns**(-s))
    exact = 6*float(zeta_K(s))
    print(f"  s={s}: lattice sum (X=1e6) = {lattice_sum:.10f}   6*zeta_K(s) = {exact:.10f}"
          f"   rel.err = {abs(lattice_sum-exact)/exact:.2e}")
print("  -> the cusp-lattice (Eisenstein unfolding) sum counts the SAME ideals, weight w_K=6.")

# ---------------------------------------------------------------- S3
print("\n[S3] BC/CMR SIDE: partition function Tr e^{-beta H}, H = log N on l^2(ideal monoid)")
print("  Tr e^{-beta H} = sum_J N(J)^{-beta} = zeta_K(beta)  [h=1: computed via S1 monoid]")
for beta in (2.0, 1.5, 1.2):
    part = np.sum(r[1:] * ns**(-beta))
    print(f"  beta={beta}: partial trace (X=1e6) = {part:.8f}   zeta_K(beta) = {float(zeta_K(beta)):.8f}")
print("  pole at beta=1 (critical temperature):")
for eps in (1e-3, 1e-5, 1e-7):
    val = (mp.mpf(eps)) * zeta_K(1+mp.mpf(eps))
    print(f"    (beta-1)*zeta_K(beta) at beta=1+{eps:g}: {float(val):.10f}")
res_exact = mp.pi/(3*mp.sqrt(3))
print(f"  exact residue  L(1,chi) = pi/(3 sqrt3) = {float(res_exact):.16f}")
print(f"  B736-P2 number 2pi/(6 sqrt3)           = {float(2*mp.pi/(6*mp.sqrt(3))):.16f}   SAME NUMBER")
print("  (class-number formula 2 pi h/(w_K sqrt|d|): the w_K=6 here is the SAME unit weight")
print("   that S2 puts in front of the Eisenstein lattice sum.)")

# ---------------------------------------------------------------- S4
print("\n[S4] SCATTERING SIDE: phi(s) = Lambda_K(s)/Lambda_K(s+1)   [EGM ch.8 / Sarnak form]")
s0 = mp.mpc(0.3, 1.7)
fe = Lambda_K(s0) - Lambda_K(1-s0)
print(f"  functional equation |Lambda_K(s)-Lambda_K(1-s)| at s=0.3+1.7i: {float(abs(fe)):.2e}")
def phi(s):
    return Lambda_K(s)/Lambda_K(s+1)
for t in (5.3, 9.7):
    print(f"  unitary axis |phi(i t)| at t={t}: {float(abs(phi(mp.mpc(0,t)))):.15f}   (Maass-Selberg: =1)")
s1 = mp.mpc(0.3, 2.1)
print(f"  phi(s)*phi(-s) at s=0.3+2.1i: {complex(phi(s1)*phi(-s1))}")
resphi = (mp.mpf('1e-8')) * phi(1+mp.mpf('1e-8'))
resphi_exact = (2*mp.pi/mp.sqrt(3)) * res_exact / zeta_K(2)
print(f"  (s-1)*phi(s) at s=1+1e-8: {float(resphi):.12f}")
print(f"  exact: (2pi/sqrt3)*L(1,chi)/zeta_K(2) = 2 pi^2/(9 zeta_K(2)) = {float(resphi_exact):.12f}")
print(f"  check 2 pi^2/(9 zeta_K(2)) = {float(2*mp.pi**2/(9*zeta_K(2))):.12f}")
print("  -> the SAME zeta_K pole at 1: scattering functor reads it as the residual point,")
print("     thermodynamic functor reads it as the critical temperature.")

# ---------------------------------------------------------------- S5
print("\n[S5] THETA CHAIN: completed zeta = Mellin transform of a literal Boltzmann sum")
print("  Theta(t) = sum_{lam in O_K} e^{-pi t N(lam)}  (heat/Gibbs weights on the SAME monoid)")
rlist = [int(x) for x in rB[1:501]]
def theta_direct(t):
    return 1 + 6*mp.fsum(rlist[n-1] * mp.e**(-mp.pi*t*n) for n in range(1, 501) if rlist[n-1])
def theta_poisson(t):
    dual = 1 + 6*mp.fsum(rlist[n-1] * mp.e**(-4*mp.pi*n/(3*t)) for n in range(1, 501) if rlist[n-1])
    return (2/(mp.sqrt(3)*t)) * dual
for tc in ('0.3', '0.5', '1.0'):
    tc = mp.mpf(tc)
    print(f"  Poisson consistency t={float(tc)}: direct {float(theta_direct(tc)):.12f}"
          f"  vs modular {float(theta_poisson(tc)):.12f}")
def Theta_minus1(t):
    t = mp.mpf(t)
    return (theta_direct(t) - 1) if t >= mp.mpf('0.7') else (theta_poisson(t) - 1)
s5 = mp.mpf('1.7')
mellin = mp.quad(lambda t: Theta_minus1(t) * t**(s5-1), [0, 0.35, 0.7, 1, 3, mp.inf])
exact5 = mp.pi**(-s5) * mp.gamma(s5) * 6 * zeta_K(s5)
print(f"  s=1.7: Mellin integral = {float(mellin):.12f}   pi^-s Gamma(s) 6 zeta_K(s) = {float(exact5):.12f}")
print(f"         rel. err = {float(abs(mellin-exact5)/exact5):.2e}")

# ---------------------------------------------------------------- S6
print("\n[S6] OBJECT ANCHORING (snappy) -- WITH ROUND-2 GENERICITY CAVEAT")
import snappy
M = snappy.Manifold('m004')
shape = complex(M.cusp_info()[0].shape)
print(f"  m004 cusp shape tau = {shape}   (2 sqrt(-3) = {complex(0, float(2*mp.sqrt(3)))})")
print(f"  |tau - 2 sqrt(-3)| = {abs(shape - 2j*float(mp.sqrt(3))):.2e}")
print("  cusp lattice L_c = Z + tau Z, tau = 2 sqrt(-3) = 4w - 2 in O_K = Z[w]:")
print("  basis change [[1,0],[-2,4]] (1 -> 1, tau -> -2+4w), det = 4")
print("  => [O_K : L_c] = 4: the cusp torus is an INDEX-4 SUBLATTICE of O_K.")
vol = M.volume()
humbert = float(3*mp.sqrt(3) * zeta_K(2) / (4*mp.pi**2))
print(f"  vol(m004) = {float(vol):.10f};  12 x Humbert |d|^{{3/2}} zeta_K(2)/(4 pi^2) = {12*humbert:.10f}")
print("  ROUND-2 CAVEAT (accepted from review): being a K-lattice point of the CMR")
print("  phase space is CLASS-GENERIC -- every cusp of every cover of PSL(2,O_3)\\H^3")
print("  is one by construction (p3: m003's cusp is O_K ITSELF, j=0).  The anchoring")
print("  is real but has NO discriminating power for the bridge question; it is")
print("  retired from the verdict inventory (see S10/S11).")

# ---------------------------------------------------------------- S7
print("\n[S7] TIME EVOLUTION GEOMETRICALLY: CMR flow weight = cusp covolume scaling")
import math
covol_OK = math.sqrt(3)/2
print("  covol(J)/covol(O_K) for principal ideals J=(lam)  [should equal N(J) exactly]:")
for (a, b, name) in [(2, 0, "(2)"), (1, -2, "(sqrt-3)"), (2, 1, "(2+w)"), (4, 1, "(4+w)")]:
    lam = complex(a + b*math.cos(math.pi/3), b*math.sin(math.pi/3))
    lam_w = lam * complex(math.cos(math.pi/3), math.sin(math.pi/3))
    covol_J = abs(lam.real*lam_w.imag - lam.imag*lam_w.real)
    Nlam = a*a + a*b + b*b
    print(f"    lam=a+bw a={a} b={b}: covol ratio = {covol_J/covol_OK:.10f}   N(lam) = {Nlam}")
print("  horotorus at height y has area covol(L)/y^2 => sublattice J O_K (deg-N(J)")
print("  isogeny) = radial displacement Delta(log y) = (1/2) log N(J); CMR sigma_t")
print("  weights the isogeny by N(J)^{it}.  [Round-2 note: this is basepoint-blind --")
print("  see S10(a): the SAME ratios hold with m004's L_c as basepoint, and with O_K;")
print("  covol(lam L) = N(lam) covol(L) for ANY lattice L.  Geometric reading, not an")
print("  object fingerprint.]")

# ---------------------------------------------------------------- S8
print("\n[S8] ANTI-PUN OPERATOR SEPARATION: the two 'Hamiltonians' are DIFFERENT operators")
print("  (a) BC/CMR Hamiltonian: spectrum {log N(J)} (ideals side)   -- computed above")
print("  (b) Lax-Phillips generator from the scattering phase: resonances at the ZEROS")
print("      of the completed zeta_K = zeta * L(chi)  (zeros side).  First ordinates:")
z1 = mp.zetazero(1)
print(f"    first zeta(s) critical zero:   t = {float(z1.imag):.6f}")
def Lambda_chi(s):
    return (mp.mpf(3)/mp.pi)**((s+1)/2) * mp.gamma((s+1)/2) * L_chi(s)
lam_test = Lambda_chi(mp.mpc(0.5, 3.7))
print(f"    reality of Lambda_chi on critical line (root number +1): Im/Re at t=3.7: "
      f"{float(abs(lam_test.imag)/abs(lam_test.real)):.2e}")
def f_real(t):
    return Lambda_chi(mp.mpc(0.5, t)).real
zeros_chi = []
tprev, fprev = 0.5, f_real(0.5)
t = 0.75
while t < 20 and len(zeros_chi) < 3:
    fv = f_real(t)
    if fv * fprev < 0:
        zeros_chi.append(float(mp.findroot(f_real, (tprev, t), solver='bisect')))
    tprev, fprev = t, fv
    t += 0.25
print(f"    first L(s,chi_-3) critical zeros: t = {[round(z,6) for z in zeros_chi]}")
print(f"  resonance ordinates {{8.04, 11.25, 14.13, ...}} vs BC spectrum {{1.099, 1.386, 1.946, ...}}:")
print("  DISJOINT sets: the scattering operator is NOT the KMS Hamiltonian.  This kills")
print("  the strong (operator-identification) form of the candidate directly.")

# ================================================================ S9  (NEW)
print("\n" + "="*78)
print("[S9] MB12 VACUITY AUDIT of the round-1 discriminator (NEW, round 2)")
print("="*78)
print("""  Round 1 used 'one monoid feeds both zetas + same pole/residue/unit weight'
  (S1-S5) as the not-a-pun discriminator.  MB12 standard: a criterion must be
  able to PASS and to FAIL.  Test: run the identical battery over the four
  smallest class-number-1 imaginary quadratic fields -- NO manifold, NO object,
  NO m004 anywhere.  If it passes everywhere, it is a theorem of h=1 arithmetic,
  not a discovered bridge, and it can carry NO weight toward outcome A.""")

# field data: disc D, unit count w, norm form N(a,b) = a^2 + p*a*b + q*b^2, character mod |D|
FIELDS = {
    -3:  dict(w=6,  form=(1, 1),  name="Q(sqrt-3)  [Eisenstein]"),
    -4:  dict(w=4,  form=(0, 1),  name="Q(i)       [Gauss; Picard PSL(2,Z[i]) = Sarnak's published case]"),
    -7:  dict(w=2,  form=(1, 2),  name="Q(sqrt-7)"),
    -11: dict(w=2,  form=(1, 3),  name="Q(sqrt-11)"),
}
def kron(D, n):
    """chi_D(n) for our four fundamental discriminants, via the standard residue tables."""
    q = abs(D)
    if D == -3:
        return chi3(n)
    if D == -4:
        r = n % 4
        return 1 if r == 1 else (-1 if r == 3 else 0)
    # D = -7, -11: D = 1 mod 4 => chi_D(n) = Legendre(n | q)
    r = n % q
    if r == 0:
        return 0
    sq = set((x*x) % q for x in range(1, q))
    return 1 if r in sq else -1

def L_chi_D(D, s):
    """L(s, chi_D) via Hurwitz zeta (entire for these nonprincipal characters)."""
    q = abs(D)
    return mp.mpf(q)**(-s) * mp.fsum(kron(D, a) * mp.zeta(s, mp.mpf(a)/q)
                                     for a in range(1, q) if kron(D, a))

def zeta_KD(D, s):
    return mp.zeta(s) * L_chi_D(D, s)

def Lambda_KD(D, s):
    return (mp.sqrt(abs(D))/(2*mp.pi))**s * mp.gamma(s) * zeta_KD(D, s)

NM9 = 2000
vac_all_pass = True
for D, F in FIELDS.items():
    q, w, (p_, q_) = abs(D), F['w'], F['form']
    print(f"\n  --- D = {D}: {F['name']}  (h=1, w_K={w}, N(a,b)=a^2{'+' if p_ else ''}"
          f"{str(p_)+'ab' if p_ else ''}+{q_}b^2) ---")
    # (i) one-monoid identity: lattice count / w  ==  sum_{d|n} chi_D(d)
    ra = np.zeros(NM9+1, dtype=np.int64)
    Bb = 80
    for a in range(-Bb, Bb+1):
        for b in range(-Bb, Bb+1):
            if a == 0 and b == 0:
                continue
            n = a*a + p_*a*b + q_*b*b
            if 0 < n <= NM9:
                ra[n] += 1
    assert np.all(ra % w == 0), f"unit orbit broken D={D}"
    ra //= w
    rb = np.zeros(NM9+1, dtype=np.int64)
    for d in range(1, NM9+1):
        c = kron(D, d)
        if c:
            rb[d::d] += c
    mm = int(np.sum(ra[1:] != rb[1:]))
    print(f"    (i)   one-monoid identity, n<=2000: mismatches = {mm}  "
          f"{'[PASS]' if mm == 0 else '[FAIL]'}")
    # (ii) Epstein = w * zeta_K: direct divisor sum to X=1e6 (same depth as S2;
    #      truncation tail at s=2.5 is ~X^{-1.5} ~ 1e-9)
    X9 = 10**6
    chi_tab = [kron(D, a) for a in range(q)]
    r9 = np.zeros(X9+1, dtype=np.int64)
    for d in range(1, X9+1):
        c = chi_tab[d % q]
        if c:
            r9[d::d] += c
    n9 = np.arange(1, X9+1, dtype=np.float64)
    s9 = 2.5
    eps_sum = w * np.sum(r9[1:] * n9**(-s9))
    eps_exact = w * float(zeta_KD(D, s9))
    rel = abs(eps_sum - eps_exact)/eps_exact
    print(f"    (ii)  Epstein sum (X=1e6) = w*zeta_K at s=2.5: rel.err = {rel:.2e}  "
          f"{'[PASS]' if rel < 1e-8 else '[FAIL]'}")
    # (iii) partition-function pole at beta=1 with class-number-formula residue
    with mp.workdps(50):
        eps = mp.mpf('1e-20')
        res_num = eps * zeta_KD(D, 1+eps)
        res_cnf = 2*mp.pi*1/(w*mp.sqrt(q))     # 2 pi h / (w sqrt|d|), h=1
        dres = abs(res_num - res_cnf)/res_cnf
    print(f"    (iii) residue of Tr e^(-beta H) at beta=1: {float(res_num):.12f}  "
          f"vs 2 pi h/(w sqrt|d|) = {float(res_cnf):.12f}  rel.diff {float(dres):.1e}  "
          f"{'[PASS]' if dres < 1e-15 else '[FAIL]'}")
    # (iv) scattering phi_D = Lambda(s)/Lambda(s+1): unitarity + Sarnak-form identity
    phiD = lambda s: Lambda_KD(D, s)/Lambda_KD(D, s+1)
    uni = abs(abs(phiD(mp.mpc(0, 6.1))) - 1)
    st = mp.mpc('1.37', '0.81')
    sar = (2*mp.pi/(mp.sqrt(q)*(st-1))) * zeta_KD(D, st-1)/zeta_KD(D, st)
    lam = Lambda_KD(D, st-1)/Lambda_KD(D, st)
    dphi = abs(sar - lam)/abs(lam)
    print(f"    (iv)  |phi_D(it)|-1 = {float(uni):.1e}; Sarnak-form == Lambda-ratio: "
          f"rel.diff {float(dphi):.1e}  {'[PASS]' if uni < 1e-20 and dphi < 1e-20 else '[FAIL]'}")
    if mm or rel > 1e-8 or dres > 1e-15 or uni > 1e-20 or dphi > 1e-20:
        vac_all_pass = False

print(f"""
  RESULT: the round-1 'same substrate' battery passes for ALL four h=1 fields
  ({'confirmed' if vac_all_pass else 'NOT confirmed -- investigate'}), including
  Sarnak's own published Picard case Q(i), with NO manifold in any of them.
  ==> the criterion CANNOT FAIL for K-attached zeta constructions at h=1: the
  collapse of (lattice count / unit weight / Epstein sum / theta Mellin /
  partition function / scattering numerator) onto the single function zeta_K is
  FORCED by class-number-1 arithmetic.  By MB12 it has ZERO discriminating
  power and cannot support 'a genuine bridge exists'.  (V1 accepted, computed.)""")

# ================================================================ S10  (NEW)
print("="*78)
print("[S10] OBJECT-DELETION TEST -- the corrected discriminator (NEW, round 2)")
print("="*78)
print("""  The candidate (prereg) needs the tower to live NATIVELY IN THE OBJECT's cusp
  scattering as the observer's SSB carrier.  Corrected test, which CAN fail:
  delete m004 (keep the bare field/orbifold, or swap in the sister m003) -- does
  ANY input to either side of the claimed bridge change?""")

print("\n  (a) KMS side inputs.  LLN Thm 2.1 system (re-fetched at source this session,")
print("      arXiv:0710.3452, pdftotext): built from (J_K^+, absolute norm N, Galois")
print("      data G(K^ab/K) x_{O^*} O-hat) -- FIELD data only; the construction has no")
print("      manifold parameter.  Verbatim source lines:")
print("        'In this situation the zeta function of the semigroup J_K is precisely")
print("         the Dedekind zeta function zeta_K(beta) = sum_{a in J_K^+} N(a)^{-beta};")
print("         it converges for beta > 1 and diverges for beta in (0, 1].'   [top p.6]")
print("        'the partition function of our system is the Dedekind zeta function.")
print("         More precisely, ... Tr(e^{-beta H_{beta,w}}) = zeta_K(beta).'  [Rem 2.2(ii)]")
print("      Basepoint-independence, computed: CMR flow weight covol(lam L)/covol(L)")
print("      for basepoint L = O_K (orbifold/m003 cusp class) AND L = L_c = Z+2sqrt(-3)Z")
print("      (m004 cusp):")
import cmath
tau_c = 2j*math.sqrt(3)
bases = {"O_K       ": (1+0j, complex(math.cos(math.pi/3), math.sin(math.pi/3))),
         "L_c (m004)": (1+0j, tau_c)}
test_lams = [(2, 0), (1, -2), (2, 1), (4, 1)]
for bname, (v1, v2) in bases.items():
    covol_L = abs(v1.real*v2.imag - v1.imag*v2.real)
    ratios = []
    for (a, b) in test_lams:
        lam = complex(a + b*math.cos(math.pi/3), b*math.sin(math.pi/3))
        w1, w2 = lam*v1, lam*v2
        covol_lamL = abs(w1.real*w2.imag - w1.imag*w2.real)
        ratios.append(covol_lamL/covol_L)
    print(f"        basepoint {bname}: ratios = {[round(x,10) for x in ratios]}"
          f"   N(lam) = {[a*a+a*b+b*b for (a,b) in test_lams]}")
print("      IDENTICAL for both basepoints (covol(lam L) = N(lam) covol(L) for ANY")
print("      lattice): the m004-specific index-4 lattice DROPS OUT of the flow weight.")
print("      The KMS/SSB structure (partition function, beta=1 pole, KMS_beta")
print("      classification, Galois torsor) consumes zero bits of m004.")

print("\n  (b) Scattering carrier.  p2_cover.py RE-RUN THIS SESSION: 29/29 checks pass;")
print("      its scalar-transfer lemma (L^2-rigidity, every ingredient verified")
print("      in-sandbox there) proves  phi_m004(s) = phi_orbifold(s)  IDENTICALLY")
print("      (= Lambda_K(s)/Lambda_K(s+1) in the 0-centered normalization).  The same")
print("      lemma applies verbatim to m003 (one cusp over one cusp, h=1).  So the")
print("      claimed carrier is BIT-IDENTICAL for m004, for m003, and for the bare")
print("      orbifold with no manifold chosen at all.  Deleting the object changes")
print("      nothing on this side either.")

print("\n  (c) Audit of the object-specific data p3 actually found (in-repo,")
print("      p3_sister_out.txt, exact arithmetic) -- does any of it reach the carrier?")
print("        * cusp lattice SHAPE (m004: j = 2835807690.42, disc -48 vs m003: j=0):")
print("          enters only the NON-CONSTANT Fourier modes of E(P,s) (the dual-lattice")
print("          frequencies); the constant term/phi is shape-blind (p2 exact identity).")
print("        * congruence LEVEL (4)/(8) vs (2) (ray-class palette 2/8 vs 1):")
print("          the beta=1 pole tower sits in the zeta_K factor, present at EVERY")
print("          level and for the bare orbifold; whether any nontrivial level-(4)")
print("          character enters m004's actual constant term with NONZERO coefficient")
print("          is p3's [5] caveat -- OPEN, and as computed by p2 the answer for the")
print("          scalar phi is 'no character terms at all'.")
print("        * H_1 marking (which slope dies homologically): no formula pathway to")
print("          phi (p3 part [4]).")
print("      ==> m004-specific bits reaching the SSB-carrying datum: ZERO.")

print("\n  (d) NON-VACUITY of this test (it can fail, in both directions):")
print("        * it would return 'object-specific carrier' if the cover's scattering")
print("          differed from the base's -- e.g. any k>1-cusped cover has a k x k")
print("          scattering MATRIX of partial zetas (only det controlled: Friedman")
print("          math/0702030, cited in p2), or a cusp field != K would break the")
print("          transfer hypotheses; p2's lemma itself lists the exact hypotheses")
print("          (ONE cusp over one cusp, h=1) without which equality fails.")
print("        * it would also return 'object-specific' if a level-(4) character")
print("          appeared with nonzero coefficient in the constant term (p3 [5]).")
print("      The test is capable of both outcomes; for m004 it returns: the object")
print("      contributes NOTHING to the claimed carrier.  (V2 accepted, computed.)")

# ================================================================ S11
print("\n" + "="*78)
print("[S11] CORRECTED VERDICT (round 2)")
print("="*78)
print("""
WHAT IS TRUE AND COMPUTED (unchanged from round 1, all independently re-verified):
  C1-C5  the substrate identities S1-S7 (one monoid, same pole, residue
         2pi/(6 sqrt3) = the B736-P2 number, theta/Mellin completion, flow-weight
         geometry) -- every numeric reproduced by two adversarial reviewers;
  C6     the operator separation S8: LP-resonance ordinates (zeta_K zeros
         {8.04, 11.25, 14.13, ...}) vs BC spectrum ({log N(J)} = {1.10, 1.39,
         1.95, ...}) are DISJOINT -- the scattering operator is not the KMS
         Hamiltonian;
  C7     (p1/p2, in-repo, re-run) the Bianchi-class scattering carries the
         COMPLETED zeta_K whole, and phi_m004 = phi_orbifold identically.

WHAT ROUND 2 ADDS (the two computations that decide the verdict):
  C8     VACUITY (S9): the round-1 'same substrate' discriminator passes for
         every h=1 imaginary quadratic field with no object present -- it is
         a theorem of class-number-1 arithmetic, has zero discriminating power
         (MB12), and is hereby retired as evidence;
  C9     OBJECT-DELETION (S10): both sides of the claimed bridge are invariant
         under deleting m004 (KMS side consumes field data only, verbatim at
         source; carrier side phi is proven identical for m004/m003/bare
         orbifold; the p3 object-specific data never reach the carrier).

CITED (fetched at source; round-2 re-fetch where marked):
  T1  Bost-Connes 1995: the Q-system, SSB at beta=1, partition zeta(beta);
  T2  Connes-Marcolli-Ramachandran [arXiv math/0501424, abstract verbatim]:
      imaginary quadratic K-lattice system, "admits the Dedekind zeta function
      as partition function and the Idele class group as group of symmetries";
  T3  Laca-Larsen-Neshveyev [arXiv:0710.3452, PDF RE-FETCHED 2026-07-21 round 2]:
      Thm 2.1: no KMS_beta for beta<0; UNIQUE KMS_beta for 0<beta<=1; for beta>1
      extremal KMS_beta indexed by G(K^ab/K) (free transitive action); Rem 2.2(ii)
      verbatim: "the partition function of our system is the Dedekind zeta
      function... Tr(e^{-beta H_{beta,w}}) = zeta_K(beta)"; and verbatim (top
      p.6): "it converges for beta > 1 and diverges for beta in (0, 1]".
      [CITATION FIX: round 1 presented a synthesized paraphrase ("the phase
      transition occurs at beta = 1, which is the location of the pole...") in
      quotation marks; that sentence is NOT in the paper.  The mathematical
      content stands (Thm 2.1 + the divergence line); the quotation is now
      verbatim and the synthesis is labeled as ours.]
  T4  Sarnak Acta 1983 / EGM ch.8 [p1: formula re-derived from the unfolding
      integral in-sandbox, 69/69]: phi(s) = Lambda_K(s-1)/Lambda_K(s) for the
      Bianchi cusp; S9(iv) verifies the same identity for D=-3,-4,-7,-11;
  T5  Faddeev-Pavlov / Lax-Phillips: LP semigroup spectrum = nontrivial zeros
      (the zeros-side operator of S8);
  T6  Connes [math/9811068, abstract verbatim]: spectral realization of the
      zeros on the adele class space (the two functors' meeting ground).
  NEGATIVE CONTROL (round-1 searches, corroborated by both reviewers'
  independent searches): NO construction in the literature makes the cusp
  scattering operator/phase a KMS flow or derives a BC/CMR system from the
  Eisenstein spectral decomposition.

STILL MISSING (unchanged; now correctly read as the ANSWER, not a footnote):
  M1  any construction making the scattering operator/phase itself a KMS
      modular flow (S8 shows the naive one fails: wrong side of the explicit
      formula);
  M2  any functor from the Eisenstein spectral decomposition to the CMR
      algebra (Connes' program territory; RH-adjacent difficulty).

VERDICT: B -- the composition dies honestly.
  The pre-registered candidate was: the infinite-tower zeta_K structure the
  observer needed (B736-P2, absent at every finite congruence level) lives
  NATIVELY in the OBJECT's cusp scattering, i.e. the object's voice IS the
  observer's SSB carrier.  Computed answer: NO --
    (1) the KMS/SSB structure is furnished entirely by the FIELD K (ideal
        monoid + Galois data); it consumes zero bits of m004 (S10a);
    (2) the object's voice does carry zeta_K whole (p1/p2), but in the
        spectral-parameter role, identically for every 1-cusped object in the
        class and for the bare orbifold with no object at all (S10b) -- the
        object supplies nothing the field does not;
    (3) the co-occurrence of zeta_K in the two roles carries zero evidential
        weight at h=1: every K-attached zeta construction collapses to zeta_K
        by class-number-1 arithmetic (S9, MB12);
    (4) the only construction that would make the voice BE the carrier
        (operator-level identification) does not exist in the literature and
        is blocked at the naive level by the disjoint-spectra computation (S8);
        what would be required is exactly M1/M2 -- explicit-formula/RH-class
        difficulty -- and that absence is the honest content of this probe.
  KILL-FORM (for the pathfinder's kill graph): "h=1 zeta-collapse: over a
  class-number-1 field, co-occurrence of zeta_K across K-attached
  constructions is forced and evidence-free; field-level structure dressed as
  object-level is the E15/E20 trap in its subtlest form."
  FACES: the two roles are NOT 'unrelated' (they share the field substrate,
  computed) -- but relation-through-the-field is precisely what outcome A was
  NOT allowed to mean: the prereg asked for the OBJECT as carrier.

SURVIVING OPEN LEADS (not killed by this verdict):
  L1  M1/M2 as a construction problem (Eisenstein <-> BC functor) -- open
      mathematics, no known route; NOT bankable as structure here;
  L2  p3's [5] caveat: whether m004's actual constant term at level (4)/(8)
      acquires nontrivial ray-class character terms (the only computed path by
      which object-specificity could re-enter the voice) -- probe-2
      continuation, currently answered 'no' for the scalar phi by p2's exact
      identity.

Firewall: pure math/structural throughout; no SM value; nothing to CLAIMS.
A clean kill of Candidate Zero's probe-4 leg, banked as RECONFIRMED negative
with the kill-form entering the campaign ledger (hunt-cell #1, width 1).
""")
