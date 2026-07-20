#!/usr/bin/env python3
# =============================================================================
# B723 PROBE 3 -- THE EMISSIONS DICTIONARY  (CORRECTED, round 2)
#   What the observer supplies as a function of the chosen state omega.
# =============================================================================
#
# FIREWALL: origin-axiom program. Structural / operator-algebra / arithmetic ONLY.
# No SM value, no physics claim beyond the structural construction. The observer's
# CHOICE (the weight/state omega) is provably FREE (B701): we build the APPARATUS
# and compute the emissions GIVEN a state -- we NEVER derive the choice. Everything
# below is recomputed in-sandbox (verify-don't-trust). Primary operator-algebra
# facts are Tomita-Takesaki + Connes classification; the arithmetic KMS picture is
# Bost-Connes / Connes-Marcolli-Ramachandran (CMR, math/0501424); the thermal-time
# reading is Connes-Rovelli (gr-qc/9406019); the type dichotomy of the arithmetic
# KMS states is Neshveyev (arXiv:0907.1456) + Bost-Connes/Laca (WebFetched below).
#
# -----------------------------------------------------------------------------
# WHY THIS IS A CORRECTION (round-1 was REFUTED). The round-1 probe claimed a
# TIGHT POSITIVE CORE: channels (a) TIME, (b) CHIRALITY, (c-discrete) VALUES are
# jointly the canonical data of ONE chosen KMS state omega. That claim is FALSE
# for the very model the campaign names as its field-matched instantiation
# (Bost-Connes / CMR over Q(sqrt-3)). The factor TYPE of the arithmetic KMS
# states splits ACROSS the phase transition at beta = 1:
#     * 0 < beta <= 1 : a UNIQUE KMS state, TYPE III_1 -- the genuine thermal
#       clock (channel a) -- but Galois-SYMMETRIC: it carries NO extremal/sheet
#       label (channel b/c has nothing to read).
#     * beta > 1       : the extremal KMS states carry a FREE TRANSITIVE Galois
#       action (the sheet/embedding label, channels b/c) but are TYPE I -- hence
#       have TRIVIAL OUTER modular class (Connes) = the modular flow is INNER =
#       NOT the type-III thermal clock of channel (a).
# So the state that carries TIME (III_1, symmetric) and the state that carries
# CHIRALITY/VALUES (type I, symmetry-broken) are NECESSARILY TWO DIFFERENT STATES
# in TWO DIFFERENT TEMPERATURE PHASES of the same system -- never "the ONE chosen
# omega". The compatibility of the type-III role and the Galois-torsor role was
# never checked in B720/B721/B723-r1; checked here (WebFetch of the primary
# literature), it is FALSE. Outcome stays B; the positive core is downgraded to a
# more honest -- and more interesting -- PHASE-DIAGRAM picture (the seam IS a
# spontaneous-symmetry-breaking phase transition, matching the program's c-swap).
#
# THE THREE ROUND-1 SPECIFIC FIXES (all applied below):
#   (F1) Channel (a): the finite M_2(C) toy is TYPE I for EVERY state (Connes:
#        finite type-I => Aut = Inn => modular flow always INNER). It ILLUSTRATES
#        the modular-flow FORMULA + the KMS_1 identity; it does NOT exhibit a
#        type-III clock. The genuine III_1 upgrade is probe2's infinite ITPFI/CMR
#        construction (a SEPARATE state, at beta<=1). Not relabeled "type-III".
#   (F2) Channel (b): recompute B713's ACTUAL chirality field -- disc(-3),
#        y^2 - 3y + 3 over Q(sqrt-3) -- NOT B700's golden disc-5 pair. And state
#        correctly (per B721 probe 2) that the being-Z/2 = Gal(K/Q) is NOT the
#        CMR label Gal(K^ab/K): it is the order-2 QUOTIENT that ACTS ON the
#        (infinite profinite) CMR torsor by the CM/anticyclotomic INVERSION.
#   (F3) Channel (c): redo the dimension count with the CORRECT size of the
#        Galois label -- Gal(K^ab/K) is INFINITE PROFINITE = totally disconnected
#        = ZERO real (manifold) dimensions -- so the continuous state-freedom is
#        still just {temperature beta} = 1 real, vs the SM's R^{~19-26}.
#
# QUESTION (two-outcome, sealed, unchanged):
#   A = the dictionary holds: EVERY closing = a datum of the ONE chosen state
#       omega, so 'the observer' = one object (the state).
#   B = a channel does NOT fit the state-picture.

import sympy as sp
import mpmath as mp

mp.mp.dps = 40
out = []
def p(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

p("="*78)
p("B723 PROBE 3 (CORRECTED) -- THE EMISSIONS DICTIONARY: what the observer")
p("     supplies as a function of the chosen state omega")
p("="*78)
p("")
p("PRIMARY FACTS (operator algebra + arithmetic KMS; sources cited, WebFetched):")
p("  * Tomita-Takesaki: a faithful normal state omega on M gives S_omega=J Delta^{1/2};")
p("    Delta -> modular flow sigma^omega_t(a)=Delta^{it} a Delta^{-it}; J antilinear (M<->M').")
p("  * Connes (cocycle Radon-Nikodym / classification): the OUTER class of sigma^omega is a")
p("    state-INDEPENDENT invariant of M. Trivial outer class <=> SEMIFINITE (type I/II, a")
p("    trace exists; modular flow INNER) ; nontrivial <=> TYPE III (no trace).")
p("  * Connes-Rovelli gr-qc/9406019: 'thermal time' = the modular flow of a state.")
p("  * Bost-Connes / CMR math/0501424 + Neshveyev arXiv:0907.1456 (WebFetched this run):")
p("    for the arithmetic QSM there is a PHASE TRANSITION at beta=1 --")
p("      - 0 < beta <= 1 : a UNIQUE KMS_beta state, of TYPE III_1 (Galois-SYMMETRIC).")
p("      - beta > 1      : extremal KMS_beta states carry a FREE TRANSITIVE Galois action")
p("                        (Gal(K^ab/K); over Q it is Zhat^* = Gal(Q^ab/Q)), of TYPE I,")
p("                        partition function zeta(beta). SPONTANEOUS SYMMETRY BREAKING.")
p("    ==> the Galois SHEET/embedding label lives ONLY in the beta>1 (type I) phase; the")
p("        type-III_1 thermal clock lives ONLY in the beta<=1 (symmetric) phase. DISJOINT.")

# ============================================================================
# Reusable finite-dimensional Tomita-Takesaki machinery.
#   H = M_n(C) with Hilbert-Schmidt inner product <A,B> = Tr(A^* B).
#   pi(x)=left mult; Omega=rho^{1/2} (cyclic separating for faithful rho).
#   S(x Omega)=x^* Omega ; S=J Delta^{1/2}; Delta(xi)=rho xi rho^{-1};
#   Delta^{1/2}(xi)=rho^{1/2} xi rho^{-1/2}; J(xi)=xi^* (INDEPENDENT of rho).
# NOTE (F1): M_n(C) is TYPE I_n for EVERY faithful rho. Its modular flow is
#   IMPLEMENTED BY THE UNITARY rho^{it} WHICH LIES IN M_n -> the flow is INNER.
#   So this machinery ILLUSTRATES formulas; it can NEVER be type III.
# ============================================================================
def mat_pow_herm(rho, s):
    rho = mp.matrix(rho); E, V = mp.eig(rho); n = rho.rows
    D = mp.matrix(n, n)
    for k in range(n):
        lam = mp.mpf(mp.re(E[k])); D[k, k] = mp.e**(s * mp.log(lam))
    return V * D * V**-1

def modular_flow(rho, a, t):
    a = mp.matrix(a)
    return mat_pow_herm(rho, 1j*t) * a * mat_pow_herm(rho, -1j*t)

def omega_state(rho, a):
    M = mp.matrix(rho) * mp.matrix(a)
    return sum(M[i, i] for i in range(M.rows))

# ============================================================================
# (I) CHANNEL (a) TIME = the modular flow sigma^omega_t.
#     TIME is a datum of a state -- but the FINITE toy is type I (inner flow);
#     the genuine type-III clock is the beta<=1 UNIQUE (symmetric) CMR state.
# ============================================================================
p("\n" + "-"*78)
p("(I) CHANNEL (a) TIME = sigma^omega_t : datum of the chosen state -- of WHICH state?")
p("-"*78)

a_obs = [[0, 1], [2, 0]]

p("  -- TRACIAL omega (rho=I/2): the OBJECT's own state (B721: type II_1, Delta=1) --")
rho_tr = [[mp.mpf('0.5'), 0], [0, mp.mpf('0.5')]]
for t in [mp.mpf('0.7'), mp.mpf('2.9')]:
    at = modular_flow(rho_tr, a_obs, t)
    dev = max(abs(at[i, j] - a_obs[i][j]) for i in range(2) for j in range(2))
    p("     t=%s: max|sigma_t(a)-a| = %s  -> sigma_t = id" % (mp.nstr(t, 3), mp.nstr(dev, 3)))
p("     => tracial omega: TRIVIAL flow, NO clock. (The object supplies no time -- B721.)")

p("\n  -- NON-tracial omega (rho=Gibbs, beta=1, H=diag(0,1)): a thermal state --")
beta = mp.mpf('1.0'); E0, E1 = mp.mpf(0), mp.mpf(1)
Z = mp.e**(-beta*E0) + mp.e**(-beta*E1)
rho_th = [[mp.e**(-beta*E0)/Z, 0], [0, mp.e**(-beta*E1)/Z]]
p("     rho = diag(%s, %s)" % (mp.nstr(rho_th[0][0], 5), mp.nstr(rho_th[1][1], 5)))
for t in [mp.mpf('0.7'), mp.mpf('2.9')]:
    at = modular_flow(rho_th, a_obs, t)
    dev = max(abs(at[i, j] - a_obs[i][j]) for i in range(2) for j in range(2))
    p("     t=%s: max|sigma_t(a)-a| = %s ; a[0,1]->%s  (rotates at rate beta*(E1-E0)=%s)"
      % (mp.nstr(t, 3), mp.nstr(dev, 3), mp.nstr(at[0, 1], 4), mp.nstr(beta*(E1-E0), 3)))

# KMS_1 identity (SOUND, kept): omega(x sigma_{-i}(y)) = omega(y x). Also symbolic.
x = [[0, 1], [1, 0]]; y = [[0, 2], [3, 0]]
sig_mi_y = mat_pow_herm(rho_th, 1.0) * mp.matrix(y) * mat_pow_herm(rho_th, -1.0)
lhs = omega_state(rho_th, (mp.matrix(x) * sig_mi_y).tolist())
rhs = omega_state(rho_th, (mp.matrix(y) * mp.matrix(x)).tolist())
p("     KMS_1 (numeric): omega(x sigma_{-i}(y))=%s ; omega(y x)=%s ; |diff|=%s"
  % (mp.nstr(lhs, 6), mp.nstr(rhs, 6), mp.nstr(abs(lhs-rhs), 3)))
# symbolic identity for generic diag(a,b):
sa, sb = sp.symbols('a b', positive=True)
rho_s = sp.diag(sa, sb)
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, 2], [3, 0]])
sig = rho_s * Y * rho_s.inv()                       # sigma_{-i}(Y) = rho Y rho^{-1}
lhs_s = sp.trace(rho_s * (X * sig)); rhs_s = sp.trace(rho_s * (Y * X))
p("     KMS_1 (symbolic, generic diag(a,b)): omega(x sigma_{-i}y)-omega(yx) simplifies to %s"
  % sp.simplify(lhs_s - rhs_s))
assert sp.simplify(lhs_s - rhs_s) == 0

# (F1) the finite toy's modular flow is INNER: rho^{it} in M_2. Show it is unitary IN M_2.
Uit = mat_pow_herm(rho_th, 1j*mp.mpf('0.7'))
uni = (Uit * Uit.H)
uni_dev = max(abs(uni[i, j] - (1 if i == j else 0)) for i in range(2) for j in range(2))
p("     (F1) FINITE M_2 is TYPE I: the flow is IMPLEMENTED by rho^{it} IN M_2 (a unitary,")
p("          U U^*=I residual=%s) => the modular flow is INNER. A finite type-I algebra has"
  % mp.nstr(uni_dev, 3))
p("          Aut=Inn (Connes) => it is NEVER type III. So this toy ILLUSTRATES sigma_t and")
p("          KMS_1; it does NOT exhibit the type-III thermal clock.")
p("")
p("  WHERE THE GENUINE TYPE-III CLOCK ACTUALLY LIVES (probe2 + CMR, WebFetched):")
p("     the type-III_1 thermal clock is the UNIQUE KMS state at 0<beta<=1 of the CMR")
p("     system -- a SEPARATE, infinite-dim state. Crucially it is Galois-SYMMETRIC:")
p("     one state, no extremal simplex => it carries NO sheet/embedding label at all.")
p("")
p("  VERDICT (a): TIME = sigma^omega_t is a datum of a state; the type-III thermal arrow")
p("     is carried by the UNIQUE, SYMMETRIC beta<=1 state (type III_1). [rung: computed")
p("     formula + KMS_1; type-III_1 identity is CMR/Neshveyev-cited.] KEY: this state has")
p("     NO Galois label -- so it CANNOT also supply channels (b)/(c). (See section V.)")

# ============================================================================
# (II) CHANNEL (b) CHIRALITY.  (F2) recompute B713's disc-(-3) field; state the
#      being-Z/2 <-> CMR torsor relation CORRECTLY (per B721 probe 2).
# ============================================================================
p("\n" + "-"*78)
p("(II) CHANNEL (b) CHIRALITY = the being-Z/2 SHEET (B713): a datum of omega?")
p("-"*78)

# J is omega-INDEPENDENT (SOUND, kept): the c-swap FRAME is not a free datum of omega.
def tomita_J(rho):
    r12 = mat_pow_herm(rho, 0.5); rm12 = mat_pow_herm(rho, -0.5)
    basis = [[[1,0],[0,0]], [[0,1],[0,0]], [[0,0],[1,0]], [[0,0],[0,1]]]
    maxdev = mp.mpf(0)
    for xb in basis:
        xm = mp.matrix(xb); xi = xm * r12
        half = r12 * xi * rm12; JDhalf = half.H; target = (xm.H) * r12
        maxdev = max(maxdev, max(abs(JDhalf[i,j]-target[i,j]) for i in range(2) for j in range(2)))
    return maxdev

devA = tomita_J([[mp.mpf('0.5'),0],[0,mp.mpf('0.5')]])
devB = tomita_J([[mp.mpf('0.8'),0],[0,mp.mpf('0.2')]])
p("  Tomita J is omega-INDEPENDENT: verify S(xOmega)=x^*Omega with J(xi)=xi^*, for")
p("     rho=I/2 (residual=%s) and rho=diag(.8,.2) (residual=%s) => SAME antilinear J."
  % (mp.nstr(devA, 3), mp.nstr(devB, 3)))
p("     So CHIRALITY is NOT 'J of omega' (J is a fixed canonical c-swap FRAME, M<->M').")
p("")

# (F2) B713's ACTUAL chirality polynomial: y^2 - 3y + 3, disc -3, over Q(sqrt-3).
p("  (F2) The object's OWN chirality torsor (B713 probe 2), recomputed -- disc(-3),")
p("       NOT the golden disc-5 pair (that was B700, a DIFFERENT V4 leg):")
yy = sp.symbols('y')
cpoly = sp.Poly(yy**2 - 3*yy + 3, yy)
disc = cpoly.discriminant()
r0 = sp.Rational(3,2) - sp.sqrt(3)*sp.I/2
r1 = sp.Rational(3,2) + sp.sqrt(3)*sp.I/2
assert sp.simplify(r0**2 - 3*r0 + 3) == 0 and sp.simplify(r1**2 - 3*r1 + 3) == 0
conj_r0 = sp.conjugate(r0)     # Gal(Q(sqrt-3)/Q) generator = complex conjugation
p("       chirality min poly (fiber of X(4_1) over x=2): %s ; discriminant = %s (=> field Q(sqrt-3))"
  % (cpoly.as_expr(), disc))
p("       roots rho_geom, rhobar_geom = (3 -+ sqrt(-3))/2 = %s , %s (verified roots)."
  % (r0, r1))
p("       disc = -3 < 0 => NO real root => NO Q-rational point => a genuine Z/2 TORSOR.")
p("       Galois c (complex conjugation): c(rho_geom) = %s = rhobar_geom -> SWAPS the two"
  % conj_r0)
p("       roots, simply transitively, NO fixed point (verified: c(rho)!=rho).")
assert sp.simplify(conj_r0 - r1) == 0 and sp.simplify(conj_r0 - r0) != 0
p("       => being-Z/2 = Gal(Q(sqrt-3)/Q) is the object's OWN chirality torsor (B713).")
p("")

# (F2) the CORRECT relation to the CMR torsor (per B721 probe 2 -- do NOT conflate).
p("  (F2) RELATION to the CMR extremal-KMS torsor (per B721 probe 2 -- NOT identity):")
p("       CMR's beta>1 sheet label is Gal(K^ab/K), K=Q(sqrt-3): INFINITE PROFINITE abelian.")
p("       Our being-Z/2 = Gal(K/Q) is the ORDER-2 QUOTIENT, over base Q. In")
p("            1 -> Gal(K^ab/K) -> Gal(K^ab/Q) -> Gal(K/Q) -> 1")
p("       being-Z/2 is the QUOTIENT and the CMR torsor is the KERNEL -- COMPLEMENTARY, not")
p("       nested. Being-Z/2 does NOT embed in the CMR torsor; it ACTS on it by the")
p("       CM/anticyclotomic INVERSION (g -> g^{-1} on the anticyclotomic part). [B721]")
p("       So CHIRALITY = the being-Z/2 SHEET is the object's own torsor bit; it is the")
p("       SYMMETRY that the beta>1 phase spontaneously BREAKS (it acts on, is not, the label).")
p("")
p("  VERDICT (b): CHIRALITY = the being-Z/2 sheet (B713, disc-3 torsor). To be a datum of a")
p("     STATE it must be READ as a broken-symmetry (extremal) label -- which exists ONLY in")
p("     the CMR beta>1 phase, and there the states are TYPE I (not the type-III clock of a).")
p("     [rung 2: B713 torsor recomputed + B721 CM-inversion relation + CMR/Neshveyev type.]")

# ============================================================================
# (III) CHANNEL (c) VALUES.  (F3) dimension count with the CORRECT (profinite)
#       size of the Galois label.
# ============================================================================
p("\n" + "-"*78)
p("(III) CHANNEL (c) VALUES = the torsor BASEPOINT (B701): a datum of omega?")
p("-"*78)
p("  DISCRETE part: the object canonically fixes the torsor (the ambiguity), NOT a")
p("     basepoint (B701, OBSTRUCTED). Choosing an EXTREMAL beta>1 state = choosing the")
p("     basepoint in the Galois torsor. This is the SAME datum as (b), read in the value-")
p("     fiber -- and, like (b), it exists ONLY in the beta>1 TYPE-I (broken) phase.")
p("")
p("  (F3) CONTINUOUS part -- dimension count with the CORRECT label size:")
p("     the state freedom of the arithmetic KMS system is")
p("        { extremal Galois label in Gal(K^ab/K) }  x  { temperature beta in R_+ }.")
p("     Gal(K^ab/K) is INFINITE PROFINITE abelian = TOTALLY DISCONNECTED => ZERO real")
p("     (manifold) dimensions (no continuous parameter, though infinitely many points).")
dim_label_real = 0     # profinite: totally disconnected, 0 real dimensions
dim_beta = 1           # temperature, one real
dim_sm = "19..26"
p("     dim_R(Galois label) = %d (profinite, totally disconnected)" % dim_label_real)
p("     dim_R(temperature beta) = %d ;  total continuous state-freedom = %d real."
  % (dim_beta, dim_label_real + dim_beta))
p("     SM value freedom (B706) = R^{%s} (Yukawas/mixings) -- a %s-real MANIFOLD." % (dim_sm, dim_sm))
p("     => KIND + DIMENSION MISMATCH stands: a (profinite label) x (one real beta) does NOT")
p("        carry an R^{19-26} of continuous values. [B706 at the operator-algebra level.]")
p("")
p("  VERDICT (c): the DISCRETE value-basepoint = the extremal (beta>1, type I) label; the")
p("     SM's CONTINUOUS 19-26 values do NOT fit (profinite label x 1 real << R^{19-26}).")
p("     [rung 2: B701 torsor + B706 kind/dimension mismatch, corrected label size.]")

# ============================================================================
# (IV) CHANNEL (d) SPACE / MULTIPLICITY.  (SOUND, kept.)
# ============================================================================
p("\n" + "-"*78)
p("(IV) CHANNEL (d) SPACE/MULTIPLICITY = Dehn slope (B718) / covering degree (B719):")
p("     does it fit the state-picture?")
p("-"*78)
p("  A STATE omega is a positive normalized functional on a FIXED algebra M. A covering")
p("  (B719) is a finite-index SUBFACTOR N<M (degree=index); a Dehn slope (B718) is a choice")
p("  of QUOTIENT/representation. Both change the ALGEBRA -- not functionals on a fixed M.")
p("")
p("  DISCRIMINATOR (Jones): the unique trace tau on the hyperfinite II_1 factor R restricts")
p("  to subfactors of EVERY Jones index in {4cos^2(pi/n):n>=3} U [4,inf) -- ONE state, ALL")
p("  indices. So fixing omega leaves the covering degree/index completely FREE.")
jones = [4*mp.cos(mp.pi/n)**2 for n in range(3, 9)]
p("     Jones index 4cos^2(pi/n), n=3..8: %s , ... then the continuum [4,inf)."
  % ", ".join(mp.nstr(v, 5) for v in jones))
p("")
p("  VERDICT (d): SPACE/MULTIPLICITY does NOT fit the one-state picture -- it is a choice of")
p("     ALGEBRA/representation/subfactor (B718 slope, B719 degree), a DIFFERENT category of")
p("     freedom from a state ON a fixed algebra. [rung 2: Jones-index fact + B718/B719.]")

# ============================================================================
# (V) THE PHASE-TRANSITION OBSTRUCTION -- the corrected CORE.
#     TIME (III_1, symmetric) and CHIRALITY/VALUES (type I, broken) are
#     DIFFERENT STATES in DIFFERENT PHASES: no single omega carries both.
# ============================================================================
p("\n" + "-"*78)
p("(V) THE PHASE-TRANSITION OBSTRUCTION: is there ONE state carrying (a) AND (b)/(c)?")
p("-"*78)
p("  The named model (Bost-Connes / CMR over Q(sqrt-3)) has a phase transition at beta=1")
p("  (WebFetched: Neshveyev 0907.1456 + Bost-Connes/Laca). The factor TYPE and the Galois")
p("  label are on OPPOSITE sides of it:")
p("")
p("     phase        | # KMS states | Galois/sheet label      | factor TYPE | modular flow")
p("     -------------+--------------+-------------------------+-------------+--------------")
p("     0<beta<=1    | UNIQUE       | NONE (symmetric)        | III_1       | type-III (arrow)")
p("     beta>1       | simplex,     | FREE TRANSITIVE          | I           | INNER (trivial")
p("                  | Galois-torsor| (Gal(K^ab/K)) = the sheet|             |  outer class)")
p("")
p("  By Connes' OWN cited criterion (trivial outer class <=> semifinite/type I/II):")
p("     * the beta<=1 III_1 state HAS the type-III thermal arrow (channel a) but NO sheet.")
p("     * each beta>1 type-I state HAS the sheet (channels b,c) but its modular flow is")
p("       INNER (trivial outer class) => it is NOT the type-III thermal clock of channel a.")
p("  These are NECESSARILY TWO DIFFERENT STATES in TWO DIFFERENT TEMPERATURE PHASES.")
p("  => NO single chosen omega supplies BOTH (a) and (b)/(c). The round-1 'tight positive")
p("     core' (a,b,c-discrete = data of ONE omega) is FALSE for the named model.")
p("")
# small structural illustration of the SSB PATTERN (unique symmetric vs orbit of extremal),
# clearly labeled: it does NOT reproduce the III_1-vs-I type dichotomy (that is the infinite
# system's theorem; a finite algebra is type I for both, exactly why the toy can only show
# the SYMMETRY-BREAKING pattern, not the type jump).
p("  Structural illustration of the SSB PATTERN (finite, type-I both sides -- shows only the")
p("  symmetric-vs-torsor split, NOT the type jump, which is the infinite system's theorem):")
G_swap = mp.matrix([[0, 1], [1, 0]])          # Z/2 acting on M_2 by conjugation (basis swap)
rho_sym = mp.matrix([[mp.mpf('0.5'), 0], [0, mp.mpf('0.5')]])   # the SYMMETRIC (tracial) state
comm = G_swap * rho_sym * G_swap.H
sym_dev = max(abs(comm[i,j]-rho_sym[i,j]) for i in range(2) for j in range(2))
p("     high-T analog: the SYMMETRIC state rho=I/2 is G-invariant (g rho g^*=rho, residual=%s):"
  % mp.nstr(sym_dev, 3))
p("        one state, no label -- the symmetric (III_1-like) phase.")
e11 = mp.matrix([[1, 0], [0, 0]]); e22 = mp.matrix([[0, 0], [0, 1]])
swap = G_swap * e11 * G_swap.H
swap_dev = max(abs(swap[i,j]-e22[i,j]) for i in range(2) for j in range(2))
p("     low-T analog: the two EXTREMAL states e11,e22 form a G-torsor (g.e11=e22, residual=%s),"
  % mp.nstr(swap_dev, 3))
p("        NEITHER G-invariant -- the symmetry-BROKEN (type-I) phase; picking one = a sheet.")
p("     (This finite toy is type I on BOTH sides -- exactly why it can only exhibit the")
p("      symmetry-breaking PATTERN; the III_1-vs-I TYPE jump is the infinite CMR theorem.)")

# ============================================================================
# THE DICTIONARY + VERDICT
# ============================================================================
p("\n" + "="*78)
p("THE EMISSIONS DICTIONARY (choice <-> free-parameter map, CORRECTED)")
p("="*78)
p("")
p("  closing          omega-datum                          which state / level      rung")
p("  ---------------  -----------------------------------  -----------------------  ----")
p("  (a) TIME         modular flow sigma^omega (Delta)      UNIQUE beta<=1 state,    computed")
p("                   = type-III_1 thermal clock            TYPE III_1 (SYMMETRIC)   +CMR-cited")
p("  (b) CHIRALITY    being-Z/2 sheet (B713 disc-3);        an EXTREMAL beta>1        2 (B713+")
p("                   = broken-symmetry Galois label        state, TYPE I (BROKEN)   B721+CMR)")
p("  (c) VALUES disc  torsor BASEPOINT = the extremal label SAME beta>1 type-I state 2 (B701)")
p("      VALUES cont  SM's ~19-26 continuous reals          NO (profinite x 1 real)  2 (B706)")
p("  (d) SPACE/MULT   Dehn slope / covering degree          NOT a state: the ALGEBRA 2 (Jones+")
p("                   = a choice of the ALGEBRA/subfactor    (Jones: one trace,all i)  B718/719)")
p("")
p("  THE OBSTRUCTION (section V): channels (a) and (b)/(c) are carried by states in")
p("  DIFFERENT TEMPERATURE PHASES of the SAME arithmetic system -- (a) by the UNIQUE")
p("  symmetric type-III_1 state at beta<=1, (b)/(c) by the symmetry-BROKEN type-I extremal")
p("  states at beta>1. By Connes' outer-class criterion the type-I states have INNER modular")
p("  flow (no type-III arrow), and the III_1 state carries NO Galois label. So NO single")
p("  chosen omega supplies both. The 'observer = ONE chosen state' picture FAILS at its core.")
p("")
p("="*78)
p("VERDICT")
p("="*78)
p("OUTCOME = B  (channels do not fit ONE state -- now including the a-vs-(b,c) split).")
p("")
p("The emissions dictionary is a STRUCTURED PARTIAL fit, and the failures are precise:")
p("  1. (a) vs (b)/(c) -- TIME vs CHIRALITY/VALUES -- are NOT data of one state: they live")
p("     in the TWO DIFFERENT PHASES of the named CMR system (III_1 SYMMETRIC at beta<=1 vs")
p("     type-I BROKEN at beta>1), separated by the beta=1 SPONTANEOUS-SYMMETRY-BREAKING phase")
p("     transition. (WebFetched: Neshveyev 0907.1456 + Bost-Connes/Laca.) This REFUTES the")
p("     round-1 'one-state positive core'.")
p("  2. (c-continuous) -- the SM's R^{19-26} exceeds a (profinite Galois label) x (one real")
p("     beta): B706 at the state level, with the CORRECTED (profinite) label size.")
p("  3. (d) SPACE/MULTIPLICITY -- a choice of the ALGEBRA (subfactor/representation), a level")
p("     UP from a state on it (Jones index free of the state): B718/B719.")
p("")
p("SO 'the observer = ONE object, the state' is TOO SMALL. The observer is at least a")
p("  ( choice of ALGEBRA/representation : SPACE + SCALE, B718/B719 )")
p("    x ( choice of TEMPERATURE/PHASE beta : which side of the beta=1 transition )")
p("      x ( choice of STATE in that phase : the thermal clock OR the broken sheet/label ).")
p("The phase transition is itself part of the apparatus: it SEPARATES the observer's clock")
p("(type-III_1, symmetric) from the observer's HAND/sheet (type-I, broken). That seam is a")
p("SPONTANEOUS SYMMETRY BREAKING of the being-Z/2 (which ACTS on the CMR torsor by CM-")
p("inversion, B721) -- exactly the program's 'c-as-swap: the observer breaks the object's")
p("swap-symmetry by choosing a side' (B711/B713), now placed at a genuine KMS phase")
p("transition. Positive residue: honest, and SHARPER than round-1's false one-state core.")
p("")
p("FIREWALL: structural/operator-algebra + arithmetic only; no SM value; the choices")
p("(algebra, temperature/phase, state) are all FREE (B701) -- we built the apparatus and")
p("read the emissions GIVEN the choices; we did NOT derive any choice. Consistent with")
p("B685/B701/B706/B713/B717/B721. This CORRECTS the refuted round-1 positive core.")

# write the transcript
import os
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "b723_probe3_out.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
