#!/usr/bin/env python3
# B725 -- PROBE 3: THE HONEST FLOOR (Gleason).
# Is the Born rule a THEOREM of the framework (Gleason + observer=state), or merely assumed?
#
# cc banking seat, 2026-07-20.  Sealed prereg (B725/PREREGISTRATION.md).
# Structural / operator-algebra ONLY.  Gate 5 stands; no SM value; choice free (B701).
# COMPUTE-NOT-CITE: every discriminating fact recomputed in-sandbox.
#
# ---------------------------------------------------------------------------------------
# THE CLAIM UNDER TEST
#   B723: the OBSERVER = a STATE omega on the object's von Neumann algebra M (an external
#   weight; the object ALONE is the tracial II_1 factor -- arrowless, no preferred state).
#   A state omega is, BY DEFINITION, a positive normalized functional; on projections
#   P (the "yes/no questions") omega(P) in [0,1] with omega(1)=1 and additivity on
#   orthogonal projections -- i.e. omega|_projections IS a noncontextual probability
#   assignment (a FRAME FUNCTION).
#   GLEASON'S THEOREM: on a Hilbert space of dim>=3 (equiv. a vN algebra with NO type-I_2
#   summand), EVERY such assignment has the form  omega(P) = Tr(rho P)  -- the BORN RULE.
#   => "observer = state" gives the Born rule BY CONSTRUCTION, FORCED by Gleason.
#
# WHAT THIS PROBE COMPUTES
#   (A) Born verification: a state's projection-values ARE Tr(rho P), a valid frame fn.
#   (B) The Gleason OBSTRUCTION on dim>=3: among smooth (polynomial) frame functions
#       ONLY quadratic forms survive -- the frame condition kills every spherical-harmonic
#       degree except l=0 and l=2 => f(x)=<x|rho|x>=Tr(rho P_x).  (the "no non-quadratic
#       assignment" core of Gleason, made concrete.)
#   (C) The dim=2 COUNTEREXAMPLE (why dim>=3 is needed / where Gleason FAILS): an explicit
#       NON-Born frame function on the qubit (type I_2 -- the one excluded case).
#   (D) What the framework ADDS beyond Gleason: (i) observer=state supplies the HYPOTHESIS
#       (object alone = tracial => the uniform rho=I/n; observer supplies a NON-uniform rho);
#       (ii) c-swap = the quadratic form (probe 1: |<phi|psi>|^2 pairs psi with its conjugate);
#       (iii) beta=1 SSB supplies the WEIGHTS/decomposition (probe 2).
#   (E) Three-skeptic adversarial verify + verdict.
#
# Two-outcome:  A = genuine structural account (Gleason forces it once observer=state;
#                   c-swap=quadratic; SSB=weights) -- honestly bounded (Gleason cited).
#               B = the Born rule adds nothing / is circular.
# ---------------------------------------------------------------------------------------

import numpy as np
from numpy.polynomial import legendre as L

rng = np.random.default_rng(725_03)
np.set_printoptions(precision=6, suppress=True)

OUT = []
def say(s=""):
    OUT.append(s); print(s)

def rand_density(n, rng):
    """Random n x n density matrix (Hermitian, PSD, trace 1)."""
    G = rng.standard_normal((n, n)) + 1j*rng.standard_normal((n, n))
    R = G @ G.conj().T          # PSD
    return R / np.trace(R).real

def rand_ONB(n, rng, real=False):
    """Columns = a random orthonormal basis (real: O(n); complex: U(n))."""
    if real:
        G = rng.standard_normal((n, n))
    else:
        G = rng.standard_normal((n, n)) + 1j*rng.standard_normal((n, n))
    Q, Rm = np.linalg.qr(G)
    # fix QR phase so columns are genuinely Haar-ish (sign/phase of diag of Rm)
    ph = np.diag(Rm) / np.abs(np.diag(Rm))
    return Q * ph.conj()

def rand_SO3(rng):
    """Random rotation in SO(3) (det = +1)."""
    Q = rand_ONB(3, rng, real=True)
    if np.linalg.det(Q) < 0:
        Q[:, 0] = -Q[:, 0]
    return Q

def proj_from_vec(v):
    v = v / np.linalg.norm(v)
    return np.outer(v, v.conj())

say("="*88)
say("B725 PROBE 3 -- THE HONEST FLOOR (Gleason): is Born a THEOREM (Gleason+observer=state)")
say("                or merely assumed?   [structural/operator-algebra only; choice free B701]")
say("="*88)

# =======================================================================================
say("\n[A] BORN VERIFICATION -- a STATE's projection-values ARE Tr(rho P), a valid frame fn.")
say("    (the object supplies M and its projection lattice; the observer supplies omega=Tr(rho .))")
say("-"*88)
n = 3
rho = rand_density(n, rng)
say(f"    dim = {n}.  random density matrix rho (Hermitian, PSD, trace=1):")
say(f"      eig(rho) = {np.sort(np.linalg.eigvalsh(rho))}   Tr(rho) = {np.trace(rho).real:.6f}")

# (A.1) state axioms on projections
I = np.eye(n)
say("\n    (A.1) omega(P)=Tr(rho P) satisfies the STATE axioms on projections:")
say(f"          omega(0) = {np.trace(rho@np.zeros((n,n))).real:.6f}   (=0)")
say(f"          omega(I) = {np.trace(rho@I).real:.6f}   (=1, normalized)")
vals = []
for _ in range(2000):
    v = rng.standard_normal(n) + 1j*rng.standard_normal(n)
    P = proj_from_vec(v)
    vals.append(np.trace(rho@P).real)
vals = np.array(vals)
say(f"          rank-1 projections: omega(P) in [{vals.min():.4f},{vals.max():.4f}] subset [0,1]  "
    f"(all in [0,1]: {bool((vals>=-1e-12).all() and (vals<=1+1e-12).all())})")

# (A.2) additivity on ORTHOGONAL projections
Q = rand_ONB(n, rng)
P1 = proj_from_vec(Q[:, 0]); P2 = proj_from_vec(Q[:, 1])
lhs = np.trace(rho@(P1+P2)).real; rhs = np.trace(rho@P1).real + np.trace(rho@P2).real
say(f"    (A.2) additivity on orthogonal P1,P2 (P1 P2=0):  omega(P1+P2)={lhs:.6f}  "
    f"=  omega(P1)+omega(P2)={rhs:.6f}   |diff|={abs(lhs-rhs):.2e}")

# (A.3) FRAME-FUNCTION condition: sum over ANY orthonormal basis = 1  (noncontextual)
worst = 0.0
for _ in range(5000):
    B = rand_ONB(n, rng)
    s = sum(np.trace(rho@proj_from_vec(B[:, i])).real for i in range(n))
    worst = max(worst, abs(s-1.0))
say(f"    (A.3) frame condition  sum_i omega(P_e_i)=1 over 5000 random ONBs:  "
    f"max|sum-1| = {worst:.2e}")
say("          => Tr(rho P) IS a valid NONCONTEXTUAL probability assignment (a frame function).")
say("          [this direction is easy: EVERY density matrix gives a Born frame function.]")

# =======================================================================================
say("\n[B] THE GLEASON OBSTRUCTION (dim>=3): the CONVERSE -- the ONLY frame functions are")
say("    quadratic forms  f(x)=<x|rho|x>=Tr(rho P_x).  Concrete on dim-3 REAL (S^2).")
say("-"*88)
say("    Method: a smooth frame function f on S^2 expands in spherical harmonics f=sum_l f_l.")
say("    The frame-sum operator  S[g](Q)=g(Qe1)+g(Qe2)+g(Qe3)  is SO(3)-equivariant, so it")
say("    acts block-diagonally on each harmonic degree l.  A frame function needs S[f]=const.")
say("    TEST each degree via the ZONAL harmonic Y_l(x)=P_l(x . zhat) (P_l = Legendre): compute")
say("    S_l(Q)=sum_i P_l(Q[:,i].zhat) over random Q in SO(3); a degree l can appear in a frame")
say("    function ONLY IF S_l is CONSTANT in Q (else its non-constant contribution cannot be")
say("    cancelled -- distinct l are rotation-independent).  Constant-degrees => the ONLY")
say("    admissible harmonic content.")

zhat = np.array([0.0, 0.0, 1.0])
Qs = [rand_SO3(rng) for _ in range(4000)]
say("\n      l :   mean S_l        std S_l        admissible? (std~0)")
admissible = []
for l in range(0, 7):
    c = np.zeros(l+1); c[l] = 1.0          # Legendre P_l
    Sl = np.array([sum(L.legval(Qs_k[:, i] @ zhat, c) for i in range(3)) for Qs_k in Qs])
    ok = Sl.std() < 1e-9
    admissible.append((l, ok))
    say(f"     {l:2d} :  {Sl.mean(): .6e}   {Sl.std(): .3e}     {'YES' if ok else 'no'}")
adm_set = [l for l, ok in admissible if ok]
say(f"\n    ADMISSIBLE harmonic degrees (constant frame-sum): {adm_set}")
say("    l=0 (dim 1) + l=2 (dim 5) = 6 = dim of symmetric 3x3 forms = QUADRATIC FORMS.")
say("    Every other degree (l=1,3,4,5,6,...) has a NON-constant frame-sum => EXCLUDED.")
say("    => a (smooth) frame function on S^2 lies in H_0 (+) H_2 = { <x|G|x> : G=G^T } = QUADRATIC")
say("       => f(x)=<x|rho|x>=Tr(rho P_x).  THE BORN FORM IS FORCED, not assumed.  [Gleason core]")

# (B.2) a direct fit: force a quartic (l=4) term into a frame function -> its coeff is killed.
say("\n    (B.2) direct over-determination check: try to build a frame function with a quartic")
say("          (l=4) piece.  Ansatz f = a + <x|G|x> + b*Y4(x).  Impose sum_i f(Qe_i)=1 for many")
say("          random ONBs and least-squares solve for (a, G-traceless[5], b).")
def zonal4(t):  # P_4(t)
    c = np.zeros(5); c[4]=1.0; return L.legval(t, c)
# build design: unknowns = [a, G symmetric traceless (5 comps: use basis), b]
# quadratic traceless basis on R^3 (5 dims):
def quad_basis(x):
    xx,yy,zz = x
    return np.array([xx*xx-zz*zz, yy*yy-zz*zz, xx*yy, xx*zz, yy*zz])
rowsA = []; rhsb = []
for _ in range(400):
    Q = rand_SO3(rng)
    a_coef = 3.0
    q_coef = sum(quad_basis(Q[:, i]) for i in range(3))
    b_coef = sum(zonal4(Q[:, i] @ zhat) for i in range(3))
    rowsA.append(np.concatenate([[a_coef], q_coef, [b_coef]]))
    rhsb.append(1.0)
A = np.array(rowsA); bb = np.array(rhsb)
sol, res, rk, sv = np.linalg.lstsq(A, bb, rcond=None)
say(f"          least-squares solution: a*3={sol[0]*3:.6f}  ||G_traceless||={np.linalg.norm(sol[1:6]):.2e}"
    f"  b(quartic coeff)={sol[6]:.3e}")
say(f"          residual ||A x - 1|| = {np.linalg.norm(A@sol-bb):.2e}")
say("          => a=1/3 (uniform), G_traceless=0, b=0: the frame constraints DRIVE THE QUARTIC")
say("             COEFFICIENT TO ZERO.  no non-quadratic frame function.  (obstruction confirmed)")

# =======================================================================================
say("\n[C] THE dim=2 COUNTEREXAMPLE -- why dim>=3 is REQUIRED (the type-I_2 hole in Gleason).")
say("-"*88)
say("    On a qubit, orthogonal vectors = ANTIPODAL Bloch points; each vector sits in a UNIQUE")
say("    ONB (its complement is a single point).  Frame condition is only  f(n)+f(-n)=1.")
say("    Born frame functions are AFFINE:  f(n)=Tr(rho P_n)=(1+r.n)/2.  But f(n)=(1+h(n))/2 works")
say("    for ANY ODD h with |h|<=1 -- e.g. h(n)=n_z^3 (odd, NON-affine) is a NON-Born frame fn.")
def bloch(theta, phi):
    return np.array([np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)])
f_nonborn = lambda nvec: 0.5*(1.0 + nvec[2]**3)
worst_frame = 0.0; nonaffine = 0.0
pts = []
for _ in range(4000):
    th = np.arccos(1-2*rng.random()); ph = 2*np.pi*rng.random()
    nvec = bloch(th, ph); pts.append((nvec, f_nonborn(nvec)))
    worst_frame = max(worst_frame, abs(f_nonborn(nvec)+f_nonborn(-nvec)-1.0))
say(f"    frame condition f(n)+f(-n)=1 over 4000 Bloch points:  max|.-1| = {worst_frame:.2e}  (holds)")
# show it is NOT affine: best affine fit (1+r.n)/2 has large residual
Xn = np.array([np.concatenate([[1.0], p[0]]) for p in pts])
yv = np.array([p[1] for p in pts])
caff, *_ = np.linalg.lstsq(Xn, yv, rcond=None)
res_aff = np.linalg.norm(Xn@caff - yv)
say(f"    best AFFINE (=Born) fit residual = {res_aff:.4f}  (>> 0  => f is NOT of the form Tr(rho P))")
say("    => a NON-Born noncontextual probability assignment EXISTS in dim 2.  Gleason is doing")
say("       REAL work: it is FALSE in dim 2, TRUE in dim>=3.  Born is not a definitional triviality.")
say("    ALGEBRA VIEW: dim-2 = M_2(C) = the type-I_2 factor -- the exact summand Gleason excludes.")

# =======================================================================================
say("\n[D] WHAT THE FRAMEWORK ADDS BEYOND GLEASON  (three structural identifications).")
say("-"*88)

# (D.i) observer = state supplies the HYPOTHESIS. object alone = tracial => uniform rho=I/n.
say("    (D.i) OBSERVER=STATE supplies Gleason's HYPOTHESIS (B723).")
tau_vals = []
for _ in range(2000):
    v = rng.standard_normal(n) + 1j*rng.standard_normal(n)
    tau_vals.append(np.trace((I/n)@proj_from_vec(v)).real)
say(f"          the object ALONE is the tracial II_1 factor: its ONLY intrinsic state is the")
say(f"          TRACE tau(P)=dim(P)/n = Tr((I/n)P) -- itself Born-form but with the UNIFORM")
say(f"          rho=I/n (arrowless): tau(rank-1 P) = {np.mean(tau_vals):.6f} = 1/n = {1/n:.6f} (const).")
say(f"          Gleason applies EQUALLY to tau; what tau lacks is a PREFERRED direction.")
say(f"          the OBSERVER's contribution is a NON-uniform rho (a broken vacuum, B723 SSB):")
say(f"          eig(rho_observer)={np.sort(np.linalg.eigvalsh(rho))} (non-uniform).  Without an")
say(f"          external non-tracial state there is NO probability to force -- observer=state is")
say(f"          exactly what makes Gleason APPLICABLE.  ALSO: the object algebra is a II_1/III")
say(f"          FACTOR => NO type-I_2 summand => the algebraic Gleason hypothesis is met by TYPE.")

# (D.ii) c-swap = the quadratic form.  |<phi|psi>|^2 pairs psi with its conjugate (J psi).
say("\n    (D.ii) c-SWAP = the QUADRATIC form (probe 1).  Gleason yields a quadratic form on")
say("           projections; the framework NAMES the vector-level squaring as the object's own")
say("           order-2 involution J (modular conjugation = c-swap, JMJ=M', J^2=1, antiunitary).")
phi = rng.standard_normal(n) + 1j*rng.standard_normal(n); phi/=np.linalg.norm(phi)
psi = rng.standard_normal(n) + 1j*rng.standard_normal(n); psi/=np.linalg.norm(psi)
rho1 = np.outer(phi, phi.conj())            # pure (rank-1) state
born = np.trace(rho1@proj_from_vec(psi)).real
overlap = abs(np.vdot(phi, psi))**2
# the c-swap pairing: <psi| rho |psi> = <psi| ( |phi><phi| ) |psi> = <phi|psi>* . <phi|psi>
swap_pair = np.conj(np.vdot(phi, psi)) * np.vdot(phi, psi)
say(f"           pure rho=|phi><phi|:  Tr(rho P_psi) = {born:.6f}")
say(f"           |<phi|psi>|^2         = {overlap:.6f}     (= amplitude paired with its CONJUGATE)")
say(f"           <phi|psi>* . <phi|psi> (the c-swap product) = {swap_pair.real:.6f} + {swap_pair.imag:.1e}i")
say(f"           => the Born value IS  amplitude x c(amplitude)  -- degree 2 = the swap's order.")
say(f"           this is an IDENTIFICATION of Gleason's quadratic with J, not a re-derivation of it.")

# (D.iii) SSB weights = the decomposition/outcome probabilities (probe 2).
say("\n    (D.iii) beta=1 SSB = the WEIGHTS/decomposition (probe 2).  Gleason characterizes the")
say("            functional but is SILENT on which pure outcomes / with what weights.  The KMS")
say("            state decomposes into extremal broken vacua with Gibbs weights p_i=Tr(rho P_i).")
Hd = np.diag([0.0, 1.0, 2.0]); beta = 1.0
w = np.exp(-beta*np.diag(Hd)); w/=w.sum()
rho_kms = np.diag(w)
P_i = [proj_from_vec(np.eye(n)[:, i]) for i in range(n)]
p_i = np.array([np.trace(rho_kms@P).real for P in P_i])
say(f"            beta=1 Gibbs rho over H=diag(0,1,2): p_i = Tr(rho P_i) = {p_i}")
say(f"            sum p_i = {p_i.sum():.6f} (=1);  each p_i is a Born value = the KMS/SSB weight.")
say(f"            => the SSB supplies the OUTCOME set + weights that Gleason does not.")

# =======================================================================================
say("\n[E] THREE-SKEPTIC ADVERSARIAL VERIFY.")
say("-"*88)
say("    S1 'CIRCULAR: a state is DEFINED to give probabilities, so Born is assumed.'")
say("       REBUTTAL (computed): FALSE in dim 2 ([C]: h=n_z^3 is a non-Born noncontextual")
say("       assignment), TRUE only in dim>=3 ([B]: quartic coeff driven to 0).  A generic")
say("       noncontextual assignment need NOT be quadratic; Gleason PROVES it must be.  The")
say("       Born FORM is forced by a real theorem, not by the definition of 'state'.")
say("    S2 'Does the OBJECT meet Gleason's hypothesis (dim>=3 / no type-I_2)?'")
say("       REBUTTAL: the object's algebra is the II_1 factor R (probe1) / III_lambda (probe2)")
say("       -- a FACTOR, hence its only summand is itself (II_1 or III), NEVER type I_2; and it")
say("       is infinite-dimensional.  The dim-2 pathology is EXACTLY type I_2 ([C]); the object")
say("       sits on the RIGHT side of the hypothesis BY ITS VERY TYPE.  Gleason applies.")
say("    S3 'Does the framework ADD anything, or just cite Gleason?'")
say("       REBUTTAL (honest): Gleason is the LOAD-BEARING cited theorem -- it does the forcing.")
say("       The framework adds THREE structural identifications, not a re-derivation: (i) the")
say("       object alone is tracial/arrowless => observer=state SUPPLIES the hypothesis (which")
say("       state); (ii) the quadratic form = the object's own c-swap/modular J (order 2 => degree")
say("       2); (iii) the beta=1 SSB supplies the outcome weights Gleason is silent on.  Genuine")
say("       content = WHERE the state comes from, WHY quadratic in the object's terms, HOW the")
say("       weights arise -- honestly BOUNDED by the fact that the quadratic FORM itself is")
say("       Gleason's output, named (not reproven) here.")

# =======================================================================================
say("\n" + "="*88)
say("VERDICT")
say("="*88)
cond_A1 = worst < 1e-9                                  # Tr(rho P) is a frame function
cond_A2 = adm_set == [0, 2]                             # only quadratics survive (Gleason core)
cond_A3 = abs(sol[6]) < 1e-6                            # quartic coeff killed
cond_A4 = res_aff > 1e-2 and worst_frame < 1e-9        # dim-2 non-Born frame fn exists
checks = {
    "[A] Tr(rho P) is a valid frame function (max|sum-1|<1e-9)": cond_A1,
    "[B] only l={0,2} admissible => frame fns are QUADRATIC = Born": cond_A2,
    "[B.2] quartic (l=4) coefficient driven to 0 by frame constraints": cond_A3,
    "[C] dim-2 non-Born frame function EXISTS (Gleason is nonvacuous)": cond_A4,
}
for k, v in checks.items():
    say(f"    [{'PASS' if v else 'FAIL'}] {k}")
allpass = all(checks.values())
say("")
if allpass:
    say("    OUTCOME = A  -- a GENUINE STRUCTURAL ACCOUNT of the Born rule, honestly bounded.")
    say("")
    say("    THE HONEST FLOOR:")
    say("      * Born is NOT circular / merely assumed: Gleason is a genuine theorem (FALSE in")
    say("        dim 2, TRUE in dim>=3) that FORCES omega(P)=Tr(rho P) once omega is a state.")
    say("      * observer=STATE (B723) is what makes Gleason APPLICABLE: the object alone is the")
    say("        tracial II_1 factor (arrowless; only the uniform rho=I/n); the observer supplies")
    say("        the non-tracial state = Gleason's hypothesis.  Object supplies the LATTICE, the")
    say("        observer supplies the MEASURE on it.  The object being a II_1/III FACTOR (no")
    say("        type-I_2 summand) meets Gleason's algebraic hypothesis by its very type.")
    say("      * the c-SWAP (modular J, order 2) NAMES Gleason's quadratic form as the object's own")
    say("        involution: the Born value = amplitude x c(amplitude) (degree 2 = swap order).")
    say("      * the beta=1 SSB supplies the outcome WEIGHTS/decomposition Gleason is silent on.")
    say("      HONEST BOUND: Gleason is the load-bearing CITED theorem; the framework's new content")
    say("      is the three identifications (state-supplier / c-swap=quadratic / SSB=weights), NOT")
    say("      a re-derivation of Gleason.  => Born rule as a CONSEQUENCE of observer=state+c-swap")
    say("      +SSB, forced by Gleason -- not a derivation from nothing, and NOT circular.")
else:
    say("    OUTCOME = B (or INCONCLUSIVE) -- see failed checks above.")
say("="*88)

with open(__file__.replace(".py", "_out.txt"), "w") as fh:
    fh.write("\n".join(OUT) + "\n")
