#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B721 / PROBE 1 -- Marcolli-Xu QSM for the figure-eight: BEING (Q(sqrt-3)) or GOLDEN (Q(sqrt5))?
================================================================================================

FIREWALL: structural / arithmetic / operator-algebra ONLY. The QSM ("thermal time")
is a STRUCTURAL clock (Bost-Connes-type), not a cosmology/physics claim.

SOURCE (WebFetched + confirmed real, 2026-07):
  arXiv:1602.04890  "Quantum statistical mechanics in arithmetic topology"
  Matilde Marcolli & Yujie Xu, submitted 16 Feb 2016.
  Published: J. Geom. Phys. (DOI 10.1016/j.geomphys.2016.11.029), math-ph.

  What the construction actually is (verbatim-quoted fragments from the paper body):
    * Algebra of observables = a NONCOMMUTATIVE BERNOULLI CROSSED PRODUCT
          (x)_{g in G_K} C*_r(pi) >< G_K
      where (K,#) is the knot semigroup under connected sum and G_K its Grothendieck group.
    * The ABELIAN-EXTENSION analog (the role played by Q^ab / cyclotomic fields and the
      Galois symmetry Gal(Q^ab/Q) = Zhat^* in Bost-Connes) is played by the CYCLIC BRANCHED
      COVERS of S^3 along the knot, encoded by a homomorphism  rho : pi -> Q/Z  and the
      profinite limit  pihat_rho .  (I.e. "knots replace primes; cyclic branched covers
      replace abelian extensions of Q".)
    * Hamiltonian:      H . eps_K = (Cr(K) + g(K)) . log(q) . eps_K
      Partition fn:     Z_a(beta) = Tr(e^{-beta H}) = sum_{K} q^{-beta (Cr(K)+g(K))}
      -> the DYNAMICS uses crossing number Cr and Seifert genus g. It does NOT use the
         hyperbolic invariant trace field, and it does NOT use the Alexander polynomial.
    * The paper does NOT develop an explicit number-field-valued "fabulous"/arithmetic
      subalgebra: the knot-specific ARITHMETIC that stands in for the abelian extensions is
      carried entirely by the cyclic-branched-cover homology.

CONSEQUENCE for the two-outcome question:
  The QSM's knot-specific arithmetic input = cyclic-branched-cover homology of the knot.
  So "which field does the fig-8 QSM ground-state data live over" reduces to:
  which field governs the branched-cover homology of 4_1 ?

  A = Q(sqrt-3)  (matches CMR's imaginary-quadratic BEING domain = invariant trace field)
  B = golden / Fibonacci Q(sqrt5)   (branched-cover homology; MISMATCH with CMR)

This probe computes BOTH candidate fields from first principles and reports the discriminator.
"""

import cmath
import sympy as sp

LINES = []
def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LINES.append(s)

out("="*88)
out("B721 PROBE 1 -- Marcolli-Xu QSM for 4_1 : BEING Q(sqrt-3) vs GOLDEN Q(sqrt5)")
out("="*88)

# ---------------------------------------------------------------------------
# PART A. The QSM arithmetic side = cyclic branched cover homology of 4_1.
#   Fox/Reidemeister-torsion formula:  |H_1(Sigma_n)| = |prod_{j=1}^{n-1} Delta(zeta_n^j)|
#   with Delta = Alexander polynomial (when the product is nonzero).
# ---------------------------------------------------------------------------
out("")
out("[A] CYCLIC BRANCHED-COVER HOMOLOGY OF THE FIGURE-EIGHT  (the QSM 'abelian extension' analog)")
out("-"*88)

t = sp.symbols('t')
Delta = t**2 - 3*t + 1          # Alexander polynomial of 4_1 (symmetric normalization)
out("Alexander polynomial Delta(t) =", Delta, "  (Mahler measure = phi^2, larger root)")

phi = (1 + sp.sqrt(5))/2
r1, r2 = phi**2, phi**-2         # roots of Delta: (3 +/- sqrt5)/2 = phi^{+/-2}
out("roots of Delta:", sp.nsimplify(r1), "=", float(r1), " , ", sp.nsimplify(r2), "=", float(r2))
out("  => Delta splits over  Q(sqrt5)  (golden field).  minimal poly of phi^2:",
    sp.minimal_polynomial(phi**2, t))

def order_numeric(n):
    p = 1.0 + 0j
    for j in range(1, n):
        z = cmath.exp(2j*cmath.pi*j/n)
        p *= (z*z - 3*z + 1)
    return abs(p)

def order_exact(n):
    # prod_{j=1}^{n-1} Delta(zeta^j) = prod_{root r} (r^n - 1)/(r - 1)
    val = 1
    for r in (r1, r2):
        val *= (r**n - 1)/(r - 1)
    return sp.simplify(sp.expand(val))

# Fibonacci / Lucas closed forms for the identification
def fib(n):  # F_n
    return int(sp.fibonacci(n))
def luc(n):  # L_n
    return int(sp.lucas(n))

out("")
out(" n | |H_1(Sigma_n(4_1))| (exact) | numeric | closed form (Fibonacci/Lucas)")
out(" --+-----------------------------+---------+-------------------------------")
for n in range(2, 13):
    ex = order_exact(n)
    num = order_numeric(n)
    if n % 2 == 1:
        cf = f"L_{n}^2 = {luc(n)}^2 = {luc(n)**2}"
        ok = (int(ex) == luc(n)**2)
    else:
        cf = f"5*F_{n}^2 = 5*{fib(n)}^2 = {5*fib(n)**2}"
        ok = (int(ex) == 5*fib(n)**2)
    out(f" {n:2d}| {str(int(ex)):27s} | {num:7.1f} | {cf}   [{'OK' if ok else 'MISMATCH'}]")

out("")
out("  => branched-cover homology orders are EXACTLY  L_n^2 (n odd) and 5*F_n^2 (n even):")
out("     the Fibonacci/Lucas sequence. The recurrence eigenvalues are phi^{+/-2}; the")
out("     growth rate / Mahler entropy is phi^2. This arithmetic LIVES OVER  Q(sqrt5).")
out("     (These are exactly the Fibonacci manifolds: Sigma_n(4_1) = Helling-Kim-Mennicke.)")

# ---------------------------------------------------------------------------
# PART B. CMR's BEING domain = invariant trace field of the 4_1 complement.
#   Computed independently (snappy find_field is run separately; here we certify the
#   arithmetic: the shape z = exp(i pi/3) satisfies z^2 - z + 1 = 0  =>  Q(sqrt-3).)
# ---------------------------------------------------------------------------
out("")
out("[B] INVARIANT TRACE FIELD OF THE 4_1 COMPLEMENT  (CMR's BEING domain)")
out("-"*88)
z = cmath.exp(1j*cmath.pi/3)                 # regular-ideal-tetrahedron shape
out("figure-eight tetrahedron shape z = exp(i*pi/3) =", z)
out("  z^2 - z + 1 =", z*z - z + 1, " (== 0)  => z is a primitive 6th root of unity")
# snappy find_field (run under sage-python) returns defining poly x^2 + 8x + 28:
disc = 8**2 - 4*28
out("  snappy invariant_trace_field_gens -> find_field poly:  x^2 + 8x + 28")
out("  discriminant =", disc, "= -48 = -3 * 16  =>  Q(sqrt(-48)) = Q(sqrt-3)")
out("  => invariant trace field = Q(sqrt-3) = Q(omega), omega = exp(2 pi i/3).  [BEING]")

# ---------------------------------------------------------------------------
# PART C. Discriminator.
# ---------------------------------------------------------------------------
out("")
out("[C] DISCRIMINATOR")
out("-"*88)
out("  Marcolli-Xu QSM dynamics: H = (Cr + g) log q  -> integer combinatorial, field-agnostic.")
out("  Marcolli-Xu arithmetic side (abelian-extension analog): CYCLIC BRANCHED COVERS.")
out("  For 4_1 that arithmetic = Fibonacci/Lucas homology = Q(sqrt5)  (GOLDEN).")
out("  The hyperbolic invariant trace field Q(sqrt-3) (BEING/CMR) is NOT used by the QSM.")
out("")
out("  Two disjoint quadratic fields sit on the SAME knot:")
out("     * branched-cover / Alexander arithmetic  ->  Q(sqrt5)   [the QSM sees THIS]")
out("     * hyperbolic invariant trace field        ->  Q(sqrt-3) [CMR/BEING; QSM ignores it]")
out("  Q(sqrt5) and Q(sqrt-3) are linearly disjoint (real vs imaginary quadratic; disc 5 vs -3).")
out("")
out("  OUTCOME = B :  the fig-8 Marcolli-Xu QSM data lives over GOLDEN Q(sqrt5),")
out("                 a field-MISMATCH with CMR's imaginary-quadratic Q(sqrt-3).")
out("")
out("  RUNG GRADE: this clears RUNG 1 (FIELD) -- which number field the knot-specific QSM")
out("  arithmetic lives over. It does NOT clear rung 2 (torsor/Galois): Marcolli-Xu do not")
out("  build an explicit number-field-valued 'fabulous'/Galois-torsor ground state (unlike")
out("  genuine Bost-Connes with its Zhat^* torsor over Q^ab). The cyclic deck symmetry Z/n")
out("  is knot-INDEPENDENT; the knot-specific content is the golden HOMOLOGY = a field fact.")
out("="*88)

if __name__ == "__main__":
    import os, io
    here = os.path.dirname(os.path.abspath(__file__))
    with io.open(os.path.join(here, "b721_probe1_out.txt"), "w") as f:
        f.write("\n".join(LINES) + "\n")
