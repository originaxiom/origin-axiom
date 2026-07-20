#!/usr/bin/env python3
"""
B726 PROBE 3 (v2, corrected) -- does BEING (+) HEARING close the B725 Born-CONTENT gap,
and do the risky hooks survive base-rate?  (structural/operator-algebra/field-theory only)

Given (prereg B726, probes 1&2 = A):
  BEING  = Q(sqrt-3)=Q(zeta3) trace field, CMR/thermal KMS, DIAGONAL/decohered.
           B725: gives Born FORM (Gleason) + classical Gibbs weights; forced-UNIFORM Haar over
           vacua; NO interference, NO non-uniform pure-state |amp|^2.
  HEARING= Q(sqrt5) golden monodromy A=[[1,1],[1,0]], A^2=M=[[2,1],[1,1]] (cat map);
           the Fibonacci MTC (fusion tau x tau = 1 + tau).
  B725 CONTENT GAP = interference + non-uniform pure-state |amp|^2.

PROBE 3 adjudicates two hooks HONESTLY, base-rate-gated, REJECTING look-elsewhere:
  (i)  interference needs COMPLEX phases; Q(sqrt5) is REAL. Which face supplies the i?
  (ii) A^2=M (literal squaring) vs |psi|^2=psi*c(psi) (conjugation-norm): precise map or false match?

CORRECTION vs v1 (skeptic-caught, E19 compute-not-cite): v1 asserted "S-matrix and F-symbols are
REAL over Q(sqrt5)". That FIELD LABEL is FALSE and is now RECOMPUTED here: the S-entries and the
off-diagonal F-symbol phi^-1/2 are real but live in a REAL QUARTIC extension of Q(sqrt5)
(NOT the complex cyclotomic Q(zeta5), and NOT bare Q(sqrt5)). Only the PROBABILITY WEIGHTS
d_a^2/D^2, D^2=2+phi, and the DIAGONAL F-symbol phi^-1 actually reduce to Q(sqrt5). Every
field-membership statement below is a printed minimal_polynomial, not an assertion. The correction
SHARPENS outcome B: the bare hearing field owns the PROBABILITIES, not the AMPLITUDES.

Externally cross-checked (primary source: Wikipedia 'Fibonacci anyons', accessed 2026-07-20):
fusion tau x tau = 1 + tau; d_tau = phi; F-symbols phi^-1, phi^-1/2, -phi^-1; R_1^{tau,tau}=e^{-4pi i/5},
R_tau^{tau,tau}=e^{3pi i/5}; twist theta_tau = e^{4pi i/5}. All discriminating logic is COMPUTED here.
"""
import sympy as sp

def head(s): print("\n"+"="*78+"\n"+s+"\n"+"="*78)
def mp(e):   return sp.minimal_polynomial(e, x)
def deg(e):  return sp.degree(mp(e))

phi = (1+sp.sqrt(5))/2          # golden ratio, real
psi = (1-sp.sqrt(5))/2          # golden conjugate = -1/phi, real  (Galois image of phi)
x   = sp.Symbol('x')

# ---------------------------------------------------------------------------
head("PART A -- the two faces as NUMBER FIELDS (which one is complex?)")
# ---------------------------------------------------------------------------
# BEING = Q(sqrt-3) = Q(zeta3): imaginary quadratic (a CM field). Complex conjugation is a
#         NON-trivial automorphism (sqrt-3 -> -sqrt-3). It carries a genuine complex structure.
# HEARING= Q(sqrt5): totally REAL quadratic. Complex conjugation acts TRIVIALLY. No phase.
r3 = sp.sqrt(-3)
print("BEING  Q(sqrt-3)=Q(zeta3): imaginary/CM. conj(sqrt-3) != sqrt-3 ?", sp.conjugate(r3)!=r3,
      "  -> NON-TRIVIAL complex conjugation (the |.|^2 order-2 norm; B725 c-swap=J)")
print("       its roots of unity = zeta3 = e^{2 pi i/3} (3-fold phases)")
print("HEARING Q(sqrt5): totally REAL. conj(sqrt5)=sqrt5 ?", sp.conjugate(sp.sqrt(5))==sp.sqrt(5),
      "  -> complex conjugation TRIVIAL -> a bare golden amplitude has NO phase")
print("VERDICT A: among the two QUADRATIC faces the COMPLEX/imaginary one is the BEING,")
print("           the REAL one is the HEARING.  (naive 'hearing=complex content' is backwards")
print("           at the field level -- the being is the face with complex structure.)")

# ---------------------------------------------------------------------------
head("PART B -- HOOK (i): where does the interference phase e^{i theta} actually live?")
# ---------------------------------------------------------------------------
# Build the Fibonacci MTC modular data FROM THE FUSION RULES (Verlinde), not by citation.
Ntau = sp.Matrix([[0,1],[1,1]])                       # fusion matrix of tau (tau x tau = 1 + tau)
eN   = sorted([sp.nsimplify(e) for e in Ntau.eigenvals().keys()], key=lambda e: float(e))
print("fusion matrix N_tau =", Ntau.tolist(), " eig =", eN, " (Perron = phi = quantum dim d_tau)")

D2 = sp.simplify(1 + phi**2)                          # total quantum dim^2 = 1+phi^2 = 2+phi
D  = sp.sqrt(D2)
S  = sp.Matrix([[1, phi],[phi, -1]])/D                # normalized Verlinde S-matrix
Sreal = all(sp.im(sp.expand_complex(e))==0 for e in S)
print("S-matrix all-real?", Sreal, "  unitary?", sp.simplify(S*S.T-sp.eye(2))==sp.zeros(2),
      "  symmetric?", S==S.T)

print("\n--- FIELD MEMBERSHIP, RECOMPUTED (minimal polynomials; the v1 error is corrected here) ---")
# The PROBABILITY-level data that DOES reduce to Q(sqrt5):
print("D^2 = 2+phi        minpoly", mp(D2),   " deg", deg(D2),   " -> IN Q(sqrt5)")
p1, pt = sp.simplify(1/D2), sp.simplify(phi**2/D2)     # non-uniform Born-like weights
print("weight p_1  = d_1^2/D^2   =", p1, " minpoly", mp(p1), " deg", deg(p1), " -> IN Q(sqrt5)")
print("weight p_tau= d_tau^2/D^2 =", pt, " minpoly", mp(pt), " deg", deg(pt), " -> IN Q(sqrt5)")
print("   ratio p_tau/p_1 =", sp.simplify(pt/p1), "= phi^2 ?", sp.simplify(pt/p1-phi**2)==0,
      "  (the exact non-uniform 1:phi^2 weight -- REAL, Q(sqrt5))")
Fdiag = sp.simplify(1/phi)                             # F^{tttt}_{t;11} = phi^-1 = phi-1
print("F-symbol phi^-1 (diagonal)=", Fdiag, " minpoly", mp(Fdiag), " deg", deg(Fdiag), " -> IN Q(sqrt5)")

# The AMPLITUDE-level data that does NOT reduce to Q(sqrt5) (v1 wrongly labeled these 'Q(sqrt5)'):
print()
print("D = sqrt(2+phi)           minpoly", mp(D),      " deg", deg(D),
      " -> REAL QUARTIC, NOT Q(sqrt5)")
S01 = sp.simplify(phi/D)
print("S-entry phi/D             minpoly", mp(S01),    " deg", deg(S01),
      " -> REAL QUARTIC, NOT Q(sqrt5)")
S00 = sp.simplify(1/D)
print("S-entry 1/D               minpoly", mp(S00),    " deg", deg(S00),
      " -> REAL QUARTIC, NOT Q(sqrt5)")
Foff = sp.simplify(phi**sp.Rational(-1,2))            # F^{tttt}_{t;t1} = phi^-1/2 = 1/sqrt(phi)
print("F-symbol phi^-1/2 = 1/sqrt(phi)  minpoly", mp(Foff), " deg", deg(Foff),
      " -> REAL QUARTIC, NOT Q(sqrt5)")
print("   (v1 CALLED phi^-1/2 and the S-entries 'REAL, in Q(sqrt5)'. REAL: yes. In Q(sqrt5): NO --")
print("    they need the real quartic Q(sqrt(phi)) / Q(sqrt(2+phi)). Corrected.)")

# Is that real quartic the cyclotomic phase field?  NO -- it is REAL, Q(zeta5) is complex.
print()
print("Real quartic Q(sqrt(phi)) vs complex cyclotomic Q(zeta5):")
print("  deg[Q(sqrt(phi)):Q] =", deg(sp.sqrt(phi)), " and sqrt(phi) is REAL (>0) -> a REAL quartic.")
z5 = sp.exp(2*sp.I*sp.pi/5)
print("  deg[Q(zeta5):Q]     =", deg(z5), " and Q(zeta5) is COMPLEX/CM (its max real subfield is deg-2 Q(sqrt5)).")
print("  => the real quartic hosting S,F is NOT Q(zeta5): a real deg-4 field cannot sit inside the")
print("     complex Q(zeta5) except in its deg-2 real part Q(sqrt5) -- but S,F are deg-4. DISJOINT above Q(sqrt5).")

# Now the INTERFERENCE phase = braiding/twist, which is genuinely COMPLEX, in Q(zeta5):
theta = sp.exp(sp.I*4*sp.pi/5)                        # twist of tau (primary-source confirmed)
print("\ntwist theta_tau = e^{4 pi i/5} = zeta5^2 ?", sp.simplify(theta - z5**2)==0,
      "   COMPLEX, im =", float(sp.im(sp.simplify(theta))))
print("braiding R_1^{tau,tau}=e^{-4 pi i/5}, R_tau^{tau,tau}=e^{3 pi i/5}  (COMPLEX, in Q(zeta5))")

# The load-bearing field fact: Q(sqrt5) IS the real subfield fixed by complex conjugation on Q(zeta5)
fixed = sp.re(sp.expand_complex(z5 + z5**-1))         # zeta5 + conj(zeta5) = 2 cos(2pi/5), real
print("\ncomplex-conj fixed elt zeta5+zeta5^-1 = 2cos(2pi/5) =", float(fixed),
      "  minpoly", mp(fixed), " -> generates Q(sqrt5)")
print("  ==> Q(sqrt5) = Q(zeta5)^{c=1}: the HEARING is exactly the c-swap-FIXED (real) part of the")
print("      phase field. The interference phase (zeta5 vs zeta5^-1) is the c-swap-CONJUGATE pair")
print("      the hearing's realness has already QUOTIENTED OUT.")
print("  ==> the being's own phases are zeta3 (3-fold) -- WRONG ORDER for Fibonacci; zeta5 not in Q(sqrt-3).")
print()
print("HOOK (i) VERDICT: (c) JOINT-but-not-clean, and now SHARPER. Stratifying the golden data by field:")
print("  * PROBABILITY level (d_a^2/D^2, D^2=2+phi, diagonal F=phi^-1): REAL, IN bare Q(sqrt5).")
print("  * AMPLITUDE level  (S-entries 1/D, phi/D; off-diagonal F=phi^-1/2): REAL but need a REAL")
print("    QUARTIC extension Q(sqrt(phi)) / Q(sqrt(2+phi)) -- NOT bare Q(sqrt5), NOT Q(zeta5).")
print("  * PHASE level      (twist/braiding zeta5): COMPLEX, needs the CYCLOTOMIC Q(zeta5).")
print("  So the bare hearing Q(sqrt5) owns the WEIGHTS (probabilities), NOT the amplitudes or the phase.")
print("  The being supplies the complex CONJUGATION (order-2 |.|^2 norm = FORM, B725) but its phases are")
print("  zeta3 (wrong order). 'hearing=Q(sqrt5)=interference content' OVER-READS on BOTH counts:")
print("  the phase needs zeta5 (unbanked) AND even the real amplitudes need a further real quartic.")

# ---------------------------------------------------------------------------
head("PART C -- HOOK (ii): A^2=M  vs  |psi|^2=psi*c(psi)  -- precise map or false match?")
# ---------------------------------------------------------------------------
A = sp.Matrix([[1,1],[1,0]]); M = A*A
print("A =", A.tolist(), "  A^2 =", M.tolist(), "  == M=[[2,1],[1,1]] ?", M==sp.Matrix([[2,1],[1,1]]))
print("A symmetric (A=A^T=A*) ?", A==A.T, "  =>  A*A = A^2 = M ?", (A.T*A)==M)
print("  (base-rate: A*A=A^2 holds for EVERY real symmetric matrix -- NOT golden-special.)")

print("\nTwo distinct 'squares' on the golden amplitude a=phi (real, on Q(sqrt5)):")
print("  LITERAL square      phi * phi     =", sp.simplify(phi*phi), " = +%.3f  POSITIVE" % float(phi**2))
print("  CONJ(Galois) norm   phi * c(phi)  =", sp.simplify(phi*psi),
      "        = %d  NEGATIVE  (= N(phi) = det A = fundamental-unit norm)" % int(phi*psi))
print("  ==> on the REAL hearing field the LITERAL square and the CONJUGATION-norm DIVERGE:")
print("      +phi^2 (positive) vs -1 (negative unit). A probability CANNOT be the negative one,")
print("      and the two operations coincide only where c is trivial (i.e. nowhere golden-nontrivial).")
print("  ==> the Born norm |psi|^2=psi*c(psi) uses the ORDER-2 c-swap (being's complex conj);")
print("      A^2=A*A is literal multiplication (A is Galois-FIXED: integer entries, no sqrt5).")
print("      These are DIFFERENT operations -> the literal 'probability = hearing^2 = being' is FALSE.")

print("\nWhat IS genuine (the salvage, honestly bounded):")
eM = sorted([sp.nsimplify(e) for e in M.eigenvals().keys()], key=lambda e: float(e))
print("  eig(A) = {phi, -1/phi} = {d_tau, Galois(d_tau)};  eig(A^2=M) =", eM, "= {1/phi^2, phi^2}.")
print("  larger eig(M) = phi^2 =", sp.simplify(phi**2), "= d_tau^2 = the (unnormalized) fusion weight.")
print("  So A -> A^2 squares the eigenvalue phi -> phi^2 = d_tau^2 -- literal squaring of a POSITIVE")
print("  quantum dimension = the anyonic-fusion Born weight d^2/D^2. Real, no conjugation.")
print()
print("  A DISTINCT, HONEST field-theoretic 'square' (NOT the A^2=M hook): PART B showed the")
print("  amplitudes (S,F ~ sqrt(2+phi), sqrt(phi)) sit ONE QUADRATIC EXTENSION ABOVE the probability")
print("  field Q(sqrt5) (which holds d_a^2/D^2). Passing amplitude->probability is 'take the square /")
print("  descend the quadratic extension' -- a genuine amplitude|^2 -> probability structure. But that")
print("  is the S/F normalization tower, NOT A^2=M, and it still involves NO complex c-swap. It does")
print("  not rescue the hook; it just names the one real squaring the data actually exhibits.")
print()
print("HOOK (ii) VERDICT: 'A^2=M IS the Born square |psi|^2=psi*c(psi)' is a FALSE PATTERN-MATCH")
print("  (outcome B for this hook): norm(conjugation) != literal square, and on Q(sqrt5) the Galois-")
print("  norm of phi is -1 (negative unit), not phi^2. A*A=A^2 is trivial for symmetric matrices; the")
print("  only real residues are (a) squared quantum dims phi->phi^2 and (b) the amplitude->probability")
print("  quadratic-extension descent -- both REAL-positive squares, NEITHER the complex c-swap Born")
print("  norm. Interference (cross terms psi_i c(psi_j)) is not captured by A^2 at all.")

# ---------------------------------------------------------------------------
head("PART D -- BASE-RATE GATE and OVERALL VERDICT")
# ---------------------------------------------------------------------------
print("""
Base-rate rejections applied (no look-elsewhere rescue):
 - 'A real quadratic field has an S-matrix-like object' -> NOT auto-Born. Discriminator demanded:
   the object must supply BOTH (a) non-uniform |amp|^2 weights AND (b) complex interference phase.
 - 'A^2=M looks like |psi|^2' rejected: A*A=A^2 is generic to symmetric matrices; the conjugation-
   norm of the golden amplitude is -1 (unit), not phi^2 -- the operations are provably different.
 - 'hearing=Q(sqrt5) supplies the complex content' rejected AND SHARPENED: Q(sqrt5) is REAL; the
   phase lives in the cyclotomic upgrade Q(zeta5), and Q(sqrt5) is precisely its c-swap-FIXED
   subfield. Moreover (v1 correction) even the REAL S/F AMPLITUDES are not in bare Q(sqrt5): they
   need a REAL QUARTIC extension Q(sqrt(phi))/Q(sqrt(2+phi)) (deg 4, minpolys computed above,
   NOT the complex Q(zeta5)). Bare Q(sqrt5) cleanly owns only the PROBABILITY WEIGHTS.

Ingredient ownership (computed field-by-field, not analogized):
   FORM (|.|^2 = order-2 conjugation-norm, quadratic)     : BEING   (Q(sqrt-3) complex conj = J; B725)
   NON-UNIFORM WEIGHTS (d_a^2/D^2 = 1:phi^2, real)         : HEARING, bare Q(sqrt5) -- CLOSES this half
   AMPLITUDE NORMALIZATION (S,F entries; phi^-1/2, 1/D)    : REAL QUARTIC Q(sqrt(phi))/Q(sqrt(2+phi))
                                                             -- a real extension ABOVE Q(sqrt5). UNBANKED.
   INTERFERENCE PHASE (zeta5 braiding/twist, complex)      : Q(zeta5) = hearing's CYCLOTOMIC UPGRADE
                                                             -- NOT bare Q(sqrt5), NOT being(zeta3). UNBANKED.

OVERALL = OUTCOME B (honestly bounded partial closure):
 * The hearing genuinely CLOSES the non-uniform-weight half of the B725 gap: the being's forced-
   UNIFORM Haar over vacua is replaced by the golden 1:phi^2 quantum-dimension weights, and these
   are EXACTLY the part that reduces to bare real Q(sqrt5) (minpoly 5x^2-5x+1). The bare hearing
   field is the field of the PROBABILITIES.
 * But the two BARE quadratic faces do NOT together supply either the AMPLITUDES or the PHASE:
   - the interference phase needs the cyclotomic Q(zeta5) (the being's phases are zeta3, wrong order);
   - even the real S/F amplitudes need a real quartic Q(sqrt(phi))/Q(sqrt(2+phi)) above Q(sqrt5).
 * And the A^2=M / amplitude-square hook is an OVER-READ (false pattern-match; generic-to-symmetric).
 => The clean 'full observer = being(collapse) + hearing(unitary) = the two halves of QM' is
    PLAUSIBLE and sharper, but NOT closed: two unbanked field extensions (real quartic for the
    amplitudes, cyclotomic zeta5 for the phase) are owned by NEITHER bare face, and one supporting
    hook (A^2=M=Born-square) does not survive base-rate. The correction TIGHTENS the negative: bare
    Q(sqrt5) owns the probabilities but not the amplitudes.

Firewall: structural/operator-algebra/field-theory only. No SM value. No 'measurement problem solved'.
Observer's choice remains FREE (B701). Nothing to CLAIMS.
""")
print("DONE.")
