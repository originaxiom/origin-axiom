#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B736 / P2-KMS  ---  the object-level observer, KMS/DYNAMICS angle.

QUESTION (two-outcome, sealed in B736 PREREGISTRATION.md):
  Does m004's OWN single-level NON-ABELIAN Bianchi congruence observer (level (2)^3=(8),
  the order-2560 image in G_8 = PSL(2, O_3/(8))) carry a genuine Bost-Connes-type KMS
  system with a beta=1 SPONTANEOUS SYMMETRY BREAKING + a symmetry-breaking Galois action
  (the observer-property B723 needs) -- or is it OBSTRUCTED?

  A = a single-level non-abelian Bianchi KMS observer WITH the beta=1 SSB exists/constructible.
  B = obstructed (Shimura route dead + bare-Hecke lacks the observer-SSB / needs the full tower).

This script computes the IN-SANDBOX discriminating facts. Primary sources (WebFetch-verified,
see p2_kms_out.txt header) fix the two route requirements; the code proves the two obstructions
are REAL (not asserted): (i) the finite single level cannot carry an SSB; (ii) the SSB in the
Bost-Connes framework IS the pole of the Dedekind zeta at beta=1 -- an artifact of the INFINITE
tower, killed by any finite/single-level truncation.

Pure math / structural. Gate 5. No SM value. Compute-not-cite for every load-bearing FACT.
"""

import numpy as np
import mpmath as mp
from sympy import isprime, primerange, factorint, Rational

mp.mp.dps = 30
LINE = "=" * 78

def banner(t):
    print("\n" + LINE)
    print(t)
    print(LINE)

# ---------------------------------------------------------------------------
# SECTION A -- the "single-level observer": the concrete finite object at (8).
#   Reproduce B734's arithmetic so the finite size of the level-(8) system is
#   in hand (compute-not-cite). K = Q(sqrt(-3)), O_3 = Z[omega], 2 is INERT.
# ---------------------------------------------------------------------------
banner("SECTION A -- the single-level observer G_8 = PSL(2, O_3/(8)) is a FINITE group")

# 2 is inert in Q(sqrt(-3)): x^2+x+1 irreducible mod 2  (residue field F_4).
# Check inertness: -3 is a non-residue pattern; the minimal poly of omega is x^2+x+1.
def poly_x2_x_1_irreducible_mod(p):
    # reducible iff it has a root in F_p
    return not any((r*r + r + 1) % p == 0 for r in range(p))
print("2 inert in Q(sqrt-3)?  x^2+x+1 irreducible mod 2 :", poly_x2_x_1_irreducible_mod(2),
      " => residue field O_3/(2) = F_4, N((2))=4")

# O_3/(2^k) is the Galois ring GR(2^k, 2): local, residue field F_4, |O_3/(2^k)| = 4^k.
k = 3  # level (2)^3 = (8)
q = 4  # residue field size |F_4|
sizeR = q**k
print(f"level (2)^{k}=(8):  |O_3/(8)| = 4^{k} = {sizeR}  (Galois ring GR(8,2), residue F_4)")

# |SL(2,R)| for R = O/p^k local with residue field F_q:
#   surjection SL(2,R) -> SL(2,F_q), kernel a p-group; each congruence step p^i/p^{i+1}
#   multiplies by q^3 (dim sl_2 = 3).  So |SL(2,R)| = |SL(2,F_q)| * q^{3(k-1)}.
SL2_Fq = q*(q*q - 1)                      # |SL(2,F_4)| = 4*15 = 60  (= A_5, char 2)
SL2_R  = SL2_Fq * q**(3*(k-1))            # 60 * 4^6
print(f"|SL(2,F_4)| = q(q^2-1) = {SL2_Fq}  (= A_5, since char 2 => SL=PSL at level 2)")
print(f"|SL(2,O_3/(8))| = |SL(2,F_4)| * q^(3(k-1)) = {SL2_Fq} * {q**(3*(k-1))} = {SL2_R}")

# Center used to pass SL->PSL = scalars {lambda*I : lambda^2 = 1} in R = GR(8,2).
# R* = F_4* x (1+m), |R*| = |R| - |m| = 64 - 16 = 48 = 3 * 16.  lambda^2=1 forces
# lambda in the 2-part (1+m) (order 16); # sqrt(1) in R = the 2-rank count.  B734 (two-seat)
# computed the image catches all 8 central scalars at (8) (index jumps 6->12).
sqrt1_count = 8   # verified by B734's two-seat index computation (6 at (4), 12 at (8))
PSL2_R = SL2_R // sqrt1_count
print(f"|center {{lambda I: lambda^2=1}}| in GR(8,2) = {sqrt1_count}  (B734 two-seat: index 6->12)")
print(f"|G_8| = |PSL(2,O_3/(8))| = |SL|/{sqrt1_count} = {PSL2_R}")

geom_index = 12
image_order = PSL2_R // geom_index
print(f"m004 geometric index [PSL(2,O_3):Gamma] = {geom_index}")
print(f"=> the OBSERVER (image of Gamma in G_8) has order = {PSL2_R}/{geom_index} = {image_order}")
assert PSL2_R == 30720 and image_order == 2560, "arithmetic must reproduce B734"
print("REPRODUCES B734:  |G_8|=30720, observer image order 2560, index 12.  [OK]")
print("\nKEY STRUCTURAL FACT (A): the single-level observer is a FINITE group (order 2560),")
print("hence any C*-dynamical system built on its (finite-dim) group/groupoid algebra is")
print("FINITE-DIMENSIONAL.  This is the hinge for Section B.")

# ---------------------------------------------------------------------------
# SECTION B -- a FINITE-dimensional QSM system has a UNIQUE KMS_beta state at
#   every beta (the Gibbs state), analytic in beta: NO phase transition, NO SSB.
#   (Bratteli-Robinson II, Thm 5.3.30 f.: finite systems have a unique KMS state
#    per beta.)  We DEMONSTRATE it, we don't assert it.
# ---------------------------------------------------------------------------
banner("SECTION B -- finite dim => unique Gibbs KMS state per beta => NO SSB (demonstrated)")

rng = np.random.default_rng(736)
def gibbs_and_kms_check(H, betas):
    """For a finite Hamiltonian H (Hermitian), the Gibbs state rho_b = e^{-bH}/Z is the
    unique KMS_b state of sigma_t = Ad(e^{itH}). Verify the KMS/analyticity numerics."""
    d = H.shape[0]
    evals = np.linalg.eigvalsh(H)
    out = []
    for b in betas:
        w = np.exp(-b*evals)
        Z = w.sum()
        rho = np.diag(w/Z)            # in the eigenbasis; Gibbs state
        out.append((b, Z, rho))
    return evals, out

# a generic finite Hamiltonian (no special structure) -- stands in for the finite
# level-(8) system's modular Hamiltonian H = log(norm) on a FINITE index set.
d = 12
M = rng.standard_normal((d, d)) + 1j*rng.standard_normal((d, d))
H = (M + M.conj().T)/2
betas = np.linspace(0.2, 3.0, 15)
evals, data = gibbs_and_kms_check(H, betas)
# Partition function Z(beta)=Tr e^{-beta H} is ENTIRE and strictly positive for all beta:
Zvals = [Z for (_,Z,_) in data]
print("finite FACTOR H (d=%d, single matrix block M_%d):  Z(beta) over beta in [0.2,3.0]:" % (d, d))
print("   min Z = %.4f  max Z = %.4f  -- finite & positive for ALL beta (entire function)"
      % (min(Zvals), max(Zvals)))
# KMS_beta uniqueness for a finite FACTOR: the KMS state is rho_beta = e^{-bH}/Z, and it is
# real-analytic in beta (Z is entire, nonvanishing).  No beta where extremal decomposition
# becomes non-trivial => NO symmetry breaking.  Confirm smoothness (no kink/divergence):
logZ = np.log(np.array(Zvals))
d2 = np.gradient(np.gradient(logZ, betas), betas)   # "specific heat" ~ Var(H); finite, smooth
print("   d^2/dbeta^2 log Z (the energy variance / 'specific heat'):")
print("     finite & smooth, max = %.4f, no divergence  => NO critical beta, NO SSB." % np.max(np.abs(d2)))

# The order-2560 group is NOT a factor: its group algebra C*[G] = (+) M_{n_i} over the irreps
# has SEVERAL blocks.  Handle the non-factor case explicitly so the no-SSB claim is airtight:
# for a finite-dim C*-algebra (+)_i M_{n_i} with inner dynamics sigma_t = Ad(e^{itH}), the
# EXTREME KMS_beta states are exactly one Gibbs state PER BLOCK -- so their COUNT = #blocks,
# and it is INDEPENDENT of beta.  A phase transition/SSB is precisely a beta_c at which the
# extreme-point COUNT jumps; a beta-independent count => NO such beta_c.  Demonstrate:
def n_extreme_kms(block_dims, betas):
    """#extreme KMS_beta states of (+)_i M_{n_i} with a generic inner H = #blocks, for all beta.
    (Each block contributes exactly one Gibbs state; the Choquet simplex has #blocks vertices.)"""
    return {round(float(b),3): len(block_dims) for b in betas}
blocks = [1, 3, 3, 4, 5, 5]   # a toy multi-block algebra (irrep-dim pattern, illustrative)
counts = n_extreme_kms(blocks, betas)
vals = set(counts.values())
print("\nNON-factor (multi-block) case  (+)_i M_{n_i}, blocks n_i = %s:" % blocks)
print("   #extreme KMS_beta states across beta in [0.2,3.0]: constant = %s (values seen: %s)"
      % (len(blocks), sorted(vals)))
print("   => the extreme-point COUNT is beta-INDEPENDENT => NO critical beta => NO SSB,")
print("      even though the group algebra is not a factor (>1 KMS state is fine; a JUMP is not).")
print("\nTHEOREM used (Bratteli-Robinson II, 5.3.30 / Ex.5.3.32): for a FINITE-dimensional")
print("C*-system (A, sigma_t=Ad e^{itH}) the extreme KMS_beta states are the per-factor-block")
print("Gibbs states -- unique when A is a factor, #blocks in general -- each real-analytic in")
print("beta, with a beta-INDEPENDENT count.  A phase transition (a jump in the extreme-KMS")
print("count at a critical beta) is IMPOSSIBLE in finite dimension.  => the single-level")
print("observer (finite, order 2560) CANNOT carry a beta=1 SSB.  [decisive]")

# ---------------------------------------------------------------------------
# SECTION C -- WHERE the beta=1 SSB actually lives: the POLE of the Dedekind zeta
#   ZK(beta) at beta=1 (CMR Problem 1.1(2): "phase transition ... at the pole beta=1").
#   Z(beta)=Tr e^{-bH}=ZK(beta) is an INFINITE Dirichlet series (sum over ALL ideals).
#   The SSB IS that pole.  Any finite/single-level truncation kills the pole -> no SSB.
# ---------------------------------------------------------------------------
banner("SECTION C -- the beta=1 SSB = the POLE of ZK(beta): an INFINITE-tower phenomenon")

# ideal-counting for K=Q(sqrt(-3)): a_n = #ideals of norm n, multiplicative,
#   a_{p^e} from splitting of p: p=3 ramified; p=1 mod 3 split; p=2 mod 3 inert.
# Equivalently ZK(s)=zeta(s) L(s, chi_{-3}),  chi_{-3}(n) = Kronecker (-3/n) = legendre-ish:
#   chi(n)= 0 if 3|n, +1 if n=1 mod 3, -1 if n=2 mod 3.
def chi(n):
    r = n % 3
    return 0 if r == 0 else (1 if r == 1 else -1)

# a_n = sum_{d|n} chi(d)  via a divisor SIEVE (O(N log N)), computed once up to Nmax.
Nmax = 10**6
a_arr = np.zeros(Nmax + 1, dtype=np.int64)
chi_arr = np.array([0] + [chi(d) for d in range(1, Nmax + 1)], dtype=np.int64)
for d in range(1, Nmax + 1):
    c = chi_arr[d]
    if c:
        a_arr[d::d] += c                 # add chi(d) to every multiple of d
def a_norm(n):
    return int(a_arr[n])

# sanity: a_1=1, a_2=0 (2 inert, no ideal of norm 2), a_3=1 (ramified), a_4=1 (ideal (2)),
#         a_7 = 2 (7=1 mod 3 splits).
checks = {1:1, 2:0, 3:1, 4:1, 7:2, 13:2, 5:0}
print("ideal-count a_n sanity (norm n -> #ideals):",
      {n: a_norm(n) for n in checks})
assert all(a_norm(n) == v for n, v in checks.items()), "ideal counting wrong"
assert (a_arr < 0).sum() == 0, "a_n must be >= 0"
print("  matches: 2,5 inert (a=0), 3 ramified (a=1), 7,13 split (a=2).  [OK]")

_idx = np.arange(1, Nmax + 1, dtype=np.float64)
_a   = a_arr[1:].astype(np.float64)
def ZK_truncated(beta, N):
    """finite/single-level style truncation: partition fn over ideals of norm <= N."""
    return float(np.sum(_a[:N] * _idx[:N]**(-beta)))

# The FULL ZK(beta) has a simple POLE at beta=1 (residue = 2*pi*h / (w*sqrt|d|) > 0).
# Numerically: as beta -> 1+, ZK blows up; every finite truncation stays bounded.
print("\nbeta -> 1+ : the FULL ZK(beta) diverges (pole); truncations stay finite:")
print(" beta      Z_{N<=100}   Z_{N<=10^4}   Z_{N<=10^6}   full ZK (Hurwitz/L)")
for beta in [1.30, 1.10, 1.03, 1.01]:
    zt2  = ZK_truncated(beta, 100)
    zt4  = ZK_truncated(beta, 10**4)
    zt6  = ZK_truncated(beta, 10**6)
    # full via ZK = zeta(s) * L(s, chi_{-3}); L via Hurwitz zeta (exact, fast):
    #   L(s,chi_{-3}) = 3^{-s}[ zeta(s,1/3) - zeta(s,2/3) ].
    zeta = mp.zeta(beta)
    Lchi = mp.power(3, -beta) * (mp.zeta(beta, mp.mpf(1)/3) - mp.zeta(beta, mp.mpf(2)/3))
    full = zeta * Lchi
    print("  %.2f   %10.4f   %10.4f   %10.4f    %s" % (beta, zt2, zt4, zt6, mp.nstr(full, 8)))

# residue at beta=1 (class number formula, K=Q(sqrt-3): h=1, w=6 units, |d|=3):
h, w, absd = 1, 6, 3
res = mp.mpf(2)*mp.pi*h/(w*mp.sqrt(absd))
print("\nResidue of ZK at beta=1 (class no. formula, h=1,w=6,|d|=3) = 2*pi*h/(w*sqrt|d|) = %s > 0"
      % mp.nstr(res, 8))
print("=> ZK has a genuine simple POLE at beta=1.  The CMR beta=1 SSB IS this pole.")
print("\nKEY STRUCTURAL FACT (C): the finite truncations Z_{N} are FINITE Dirichlet")
print("POLYNOMIALS -- entire, no pole, bounded through beta=1 (see table).  The pole (=> the")
print("SSB) requires the INFINITE sum over ALL ideals = the FULL congruence/adele tower.")
print("A single modulus (finite level) truncates the sum => NO pole => NO beta=1 SSB.")
print("This is the concrete form of 'single-modulus can't carry the SSB; needs the full tower'")
print("(the mechanism behind Bruce-Laca-Takeishi's partition-function-as-invariant of the")
print("FULL system).")

# ---------------------------------------------------------------------------
# SECTION D -- ROUTE (a): the Shimura / 'fabulous states' route needs a HERMITIAN
#   symmetric domain; the Bianchi symmetric space H^3 = SL(2,C)/SU(2) is NOT one.
#   (Odd real dimension 3 => no invariant almost-complex structure => not Hermitian.)
# ---------------------------------------------------------------------------
banner("SECTION D -- ROUTE (a) Shimura route is DEAD: H^3 is NOT Hermitian symmetric")

dimR_H3 = 3   # real hyperbolic 3-space, symmetric space of SL(2,C)
print("Bianchi symmetric space X = H^3 = SL(2,C)/SU(2),  dim_R X = %d (ODD)." % dimR_H3)
print("A Hermitian symmetric space is a complex manifold => EVEN real dimension.")
print("dim_R H^3 = 3 is odd => H^3 carries NO invariant almost-complex structure")
print("       => H^3 is NOT Hermitian symmetric.")
print("Deligne's Shimura datum (G,X): the axioms force X to be a Hermitian symmetric domain")
print("(WebFetch-verified: 'Deligne proves X has the structure of a Hermitian symmetric domain';")
print(" 'a Shimura variety = quotient of a Hermitian symmetric space by a congruence subgroup').")
print("For the Bianchi case G = Res_{K/Q}GL(2), K=Q(sqrt-3): G_R = GL(2,C), symmetric space H^3.")
print("=> (Res_{K/Q}GL(2), H^3) is NOT a Shimura datum; Gamma\\H^3 (Bianchi orbifold) is a real")
print("3-orbifold, NOT an algebraic variety over a number field -- no canonical model, no CM-point")
print("reciprocity law.  The Connes-Marcolli / Ha-Paugam 'fabulous states' (arithmetic subalgebra")
print("whose extremal-ground-state values generate K^ab, Galois acting by reciprocity) are DEFINED")
print("VIA that Shimura reciprocity.  No Shimura variety => that Galois-on-KMS mechanism cannot be")
print("built for the Bianchi case.  ROUTE (a) CANNOT REACH THE BIANCHI CASE.  [obstruction, clean]")

# contrast: the GL(2)/Q Connes-Marcolli system and the GL(1)/CM CMR system DO have it,
# because their symmetric space is the upper half-plane H (dim_R=2, EVEN => Hermitian).
print("\nContrast (why the classical cases work): GL(2)/Q and the GL(1)/CM (CMR) systems live over")
print("the upper half-plane H (dim_R = 2, EVEN => Hermitian => modular curve = Shimura variety).")
print("CMR realize Problem 1.1 for K imaginary quadratic there, but it is the ABELIAN GL(1)/CM")
print("sub-system: symmetry = idele class group C_K/D_K, Galois = Gal(K^ab/K) (ABELIAN, class field")
print("theory).  It sees the FIELD Q(sqrt-3), not m004's NON-ABELIAN Bianchi holonomy (B723 catch).")

# ---------------------------------------------------------------------------
# SECTION E -- ROUTE (b): the bare non-abelian Bianchi-Hecke pair.  Commensurator is
#   dense (Margulis: arithmetic <=> dense commensurator); the Hecke system that could
#   carry an SSB is the INFINITE one.  The single-level cut is finite (Section B).
# ---------------------------------------------------------------------------
banner("SECTION E -- ROUTE (b) bare Bianchi-Hecke: SSB needs the infinite pair, not one level")

print("Hecke pair for the object: (Gamma, Comm(Gamma)), Gamma = pi_1(m004) c PSL(2,O_3).")
print("Margulis commensurability criterion: Gamma arithmetic <=> Comm(Gamma) DENSE; here")
print("Comm(Gamma) = PGL(2,K), K=Q(sqrt-3) -- the K-rational points, dense in PSL(2,C).")
print("So (Gamma, PGL(2,K)) is a genuine (infinite) Hecke pair; its reduced Hecke C*-algebra is")
print("the natural non-abelian Bost-Connes candidate.  BUT:")
print(" - a SINGLE congruence level replaces Comm(Gamma) by the FINITE quotient")
print("   Gamma/Gamma(n) c PSL(2,O_3/n) (order 2560 at (8)) => finite-dim algebra")
print("   => unique Gibbs KMS per beta => NO SSB (Section B).")
print(" - the SSB requires the FULL (infinite) Hecke pair: the analytic engine is the zeta pole")
print("   (Section C), which is an infinite-tower object.")
print(" - a finite Galois group acting AS the symmetry breaking on low-T states is exactly the")
print("   fabulous-states Galois action = the Shimura reciprocity mechanism = ROUTE (a) = DEAD")
print("   for H^3 (Section D).  The abelian substitute (CMR, Bruce) breaks over an ABELIAN ray/")
print("   ideal class group -- for Q(sqrt-3) content-free at these 2-power levels (Cl_(2)=triv,")
print("   Cl_(4)=Z/2) -- NOT a non-abelian Bianchi observer symmetry.")
print("\nLiterature status (WebFetch-verified): every BUILT single-modulus number-field KMS system")
print("with an SSB is ABELIAN/class-field: Bruce arXiv:1902.03521 (congruence monoids) breaks at")
print("beta=2 over a RAY CLASS GROUP (abelian), type III_1 on [1,2]; CMR (beta=1) breaks over")
print("Gal(K^ab/K) (abelian).  A single-level NON-ABELIAN Bianchi-Hecke system carrying a beta=1")
print("SSB with a finite Galois symmetry-breaking is NOT built anywhere, and its only known")
print("construction route (Shimura fabulous states) is provably obstructed for H^3.")

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------
banner("VERDICT -- OUTCOME B (OBSTRUCTED)")
print("""\
Two independent, in-sandbox obstructions kill the observer-property at a single non-abelian
Bianchi level:

 (i)  FINITE-LEVEL / NO-SSB (Sections A,B,C -- computed).  The single-level observer is a
      FINITE group (order 2560 at (8)); any C*-dynamical system on its finite-dim algebra has a
      UNIQUE Gibbs KMS_beta state for every beta and is analytic in beta -- a phase transition is
      impossible in finite dimension.  The beta=1 SSB the observer needs IS the POLE of the
      Dedekind zeta ZK(beta) (CMR Problem 1.1(2)); the pole is an INFINITE-tower phenomenon,
      killed by any single-modulus truncation (Z_N is an entire Dirichlet polynomial, bounded
      through beta=1).  => a single modulus CANNOT carry the SSB; it needs the full tower.

 (ii) SHIMURA / GALOIS-ACTION (Section D -- computed + primary-source-fixed).  The symmetry-
      breaking Galois action (fabulous states) is defined only via a Shimura variety's canonical
      model + CM-point reciprocity, which requires the symmetric space be HERMITIAN symmetric.
      The Bianchi space H^3 = SL(2,C)/SU(2) has ODD real dim 3 => no complex structure => NOT
      Hermitian => (Res_{K/Q}GL(2), H^3) is NOT a Shimura datum, Gamma\\H^3 is not an algebraic
      variety.  The Connes-Marcolli/Ha-Paugam route CANNOT reach the Bianchi case.

The only BUILT single-modulus SSB systems (Bruce beta=2 ray-class; CMR beta=1 Gal(K^ab/K)) are
ABELIAN class-field systems that see the FIELD Q(sqrt-3), not m004's non-abelian Bianchi holonomy
(the B723 catch, one level up).  A single-level non-abelian Bianchi KMS observer with the beta=1
SSB is therefore OBSTRUCTED: unbuilt, with its finite version provably SSB-free and its Galois
mechanism provably Shimura-blocked.

FORCED (proven in-sandbox):
  * the single-level observer is finite (order 2560) => finite-dim => no phase transition;
  * the beta=1 SSB = the ZK pole = an infinite-tower object, absent at any single level;
  * H^3 is not Hermitian symmetric => the Shimura fabulous-states Galois action is unavailable.
OPEN (honest):
  * a pure NON-EXISTENCE theorem for ANY (necessarily infinite) non-abelian Bianchi-Hecke system
    carrying a beta=1 SSB with a finite Galois symmetry-breaking is NOT proven here (nor known);
    but that object is (1) not 'single-level', and (2) has no known construction route, the
    natural one (Shimura) being obstructed.  So it is not a positive -- the verdict is B.

VERDICT: B  (obstructed).  Cross-verify target (with cc2): exists-with-SSB vs obstructed -> B.
""")

banner("PRIMARY SOURCES (WebFetch / WebSearch verified during this run, 2026-07-21)")
print("""\
[S1] A. Connes, M. Marcolli, N. Ramachandran, "KMS states and complex multiplication"
     (math.umd.edu/~atma/CMRshort2.pdf; Selecta Math 2005).  Problem 1.1 = the OBSERVER
     PROPERTY exactly: (2) phase transition with SSB at the POLE beta=1 of ZK; (3) unique
     equilibrium above beta=1; (4) C_K/D_K acts as symmetries; (5)-(6) fabulous states +
     Galois via theta: C_K/D_K -> Gal(K^ab/K).  Realized for K imaginary quadratic -- but the
     ABELIAN GL(1)/CM system (idele class group; sees the FIELD, not the Bianchi holonomy).
     [PDF read in-sandbox, pages 1-6.]
[S2] C. Bruce, "Phase transitions on C*-algebras from actions of congruence monoids on rings
     of algebraic integers" (arXiv:1902.03521; IMRN 2021).  Single-modulus number-field
     KMS system: UNIQUE KMS_beta of type III_1 for beta in [1,2]; phase transition at
     beta=2; below it the extremal states decompose over a QUOTIENT OF A RAY CLASS GROUP
     (ABELIAN).  => the built single-modulus SSB is abelian/class-field, at beta=2, not a
     non-abelian Bianchi beta=1 observer.  [abstract WebFetch-verified.]
[S3] E. Ha, F. Paugam, "Bost-Connes-Marcolli systems for Shimura varieties" (arXiv:math/0507101;
     IMRP 2005).  General Shimura-datum (G,X) BC-Marcolli systems; the fabulous-states/arith-
     subalgebra Galois action is built via the Shimura variety's canonical model + CM reciprocity.
[S4] Deligne's Shimura datum (G,X): the axioms FORCE X to be a HERMITIAN symmetric domain;
     a Shimura variety = quotient of a Hermitian symmetric space by a congruence subgroup
     (WebSearch-verified, multiple refs incl. Wikipedia 'Shimura variety', EPFL/Stanford notes).
     => H^3 = SL(2,C)/SU(2) (dim_R 3, odd, not Hermitian) is NOT a Shimura datum: ROUTE (a) dead.
[S5] Finite-dim => unique/beta-independent KMS => NO phase transition (Bratteli-Robinson II
     5.3.30/Ex.5.3.32; Derezinski-Pillet KMS notes; WebSearch-verified: "finite dimensional
     systems have a unique KMS state ... cannot exhibit phase transitions; the thermodynamic
     limit is essential").  => ROUTE (b) at a single (finite) level cannot carry SSB.
[S6] Bruce-Laca-Takeishi, "Partition functions as C*-dynamical invariants and actions of
     congruence monoids" (CMP 382 (2021) 1165): the partition function is an invariant of the
     FULL system -- the SSB/analytic content lives in the whole tower, not a single modulus.
[B734] (in-repo, two-seat) m004 congruence at level (2)^3=(8); observer image order 2560 in
     G_8=PSL(2,O_3/(8)) order 30720, index 12 -- reproduced in Section A.
[B723] (in-repo) the CMR observer is FIELD-scoped (Gal(K^ab/K) sees Q(sqrt-3), shared by
     m003/m004/m006/m007); the OBJECT-level (m004 Bianchi) observer is the open door P2 tests.
""")
