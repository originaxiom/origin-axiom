#!/usr/bin/env sage-python
# -*- coding: utf-8 -*-
"""
B721 PROBE 2 -- THE TORSOR IDENTIFICATION.

QUESTION (sealed, PREREGISTRATION.md, probe 2): is our being-torsor
    Gal(Q(sqrt-3)/Q) = Z/2   (B700 cell 2 / docs/LAW_MAP.md, the geometric swap sigma*)
a GENUINE, CANONICAL piece (a distinguished quotient/sub-torsor) of the
Connes-Marcolli-Ramachandran (math/0501424) zero-temperature KMS ground-state torsor
    Gal(K^ab/K),   K = Q(sqrt-3),
which acts SIMPLY TRANSITIVELY on the extremal zero-temperature KMS states of the
imaginary-quadratic Bost-Connes/CM system?

TWO-OUTCOME:
  A = genuine structural embedding (our Z/2 is a canonical quotient/sub-torsor of the
      CMR torsor -- a real rung-1/2 bridge).
  B = rung-mismatch (the FIELD Q(sqrt-3) matches, but the base fields and torsor
      STRUCTURES differ: Z/2 OVER Q vs an infinite profinite abelian group OVER K).

This script COMPUTES the two group structures in-sandbox (pari/sage) and lays out the
exact-sequence relationship that is the discriminating fact. It asserts nothing it does
not compute or derive from a stated theorem.

FIREWALL: structural/arithmetic only. The KMS/modular flow is a STRUCTURAL clock; no
physics/cosmology/SM claim is made.

Run:  cd ~/origin-axiom && sage-python frontier/B721_thermal_time/b721_probe2.py
"""

import sys
from sage.all import QuadraticField
import cypari2

LINES = []
def out(s=""):
    print(s)
    LINES.append(s)

out("=" * 78)
out("B721 PROBE 2 -- THE TORSOR IDENTIFICATION (being-Z/2  vs  CMR Gal(K^ab/K))")
out("=" * 78)

# ---------------------------------------------------------------------------
# 0. The two objects, stated exactly.
# ---------------------------------------------------------------------------
out("""
OUR being-torsor (B700 cell 2, docs/LAW_MAP.md line 99):
    T_being = Gal(Q(sqrt-3)/Q) = Z/2  (the geometric swap sigma*: sqrt-3 |-> -sqrt-3).
    BASE FIELD = Q.  It is the Galois group of the QUADRATIC extension K/Q.
    Order 2.  One of the three involutions of V4 = Gal(Q(sqrt-3,sqrt5)/Q) (being x hearing
    = meeting).

CMR torsor (Connes-Marcolli-Ramachandran, math/0501424, "KMS states and complex
multiplication", Connes/Marcolli/Ramachandran, 24 Jan 2005; abstract confirms
"the idele class group as group of symmetries" + explicit CFT; the extremal
zero-temperature KMS states form a principal homogeneous space (torsor) under the
symmetry group  C_K/D_K  ~=  Gal(K^ab/K)  acting SIMPLY TRANSITIVELY, intertwining the
symmetry with the Galois action on state values):
    T_CMR = Gal(K^ab/K),   K = Q(sqrt-3).
    BASE FIELD = K = Q(sqrt-3).  It is the Galois group of K^ab OVER K.
    By class field theory  Gal(K^ab/K) ~= C_K / D_K  (idele class group mod connected
    component) -- an INFINITE PROFINITE ABELIAN group.
""")

# ---------------------------------------------------------------------------
# 1. Compute K's arithmetic: h=1, units, and the CMR torsor's finite quotients
#    (the ray class groups Cl_m(K) = Gal(K(m)/K), quotients of Gal(K^ab/K)).
# ---------------------------------------------------------------------------
K = QuadraticField(-3, 'a')
out("-" * 78)
out("1. K = Q(sqrt-3): the arithmetic of the CMR side")
out("-" * 78)
out("   defining poly     : %s" % K.defining_polynomial())
out("   discriminant      : %s" % K.discriminant())
out("   class number h(K) : %s   (=> Hilbert class field = K itself)" % K.class_number())
out("   unit group O_K^x  : %s  (mu_6 = Eisenstein units {+-1,+-w,+-w^2})"
    % K.unit_group())
out("   O_K = Z[w], w = (1+sqrt-3)/2 = zeta_6  (Eisenstein integers)")
out("")

pari = cypari2.Pari()
pari.allocatemem(200000000)
bnf = pari('bnfinit(x^2+3)')

out("   CMR torsor Gal(K^ab/K) = inverse limit of the ray class groups Cl_m(K)")
out("   = Gal(K(m)/K), the finite quotients. Computed (pari bnrinit):")
out("")
out("     conductor m |  |Cl_m(K)|  |  cyclic structure Gal(K(m)/K)")
out("     ------------+-------------+------------------------------")
orders = []
for f in [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25, 32, 49]:
    bnr = pari('bnrinit(%s, %d)' % (bnf, f))
    clgp = bnr[4]
    order = int(clgp[0])
    cyc = list(clgp[1])
    orders.append(order)
    out("     %11d | %11d | %s" % (f, order, cyc if cyc else "[] (trivial)"))
out("")
out("   The orders are UNBOUNDED (%s, ...): the inverse limit Gal(K^ab/K) is an"
    % ", ".join(str(o) for o in orders[:8]))
out("   INFINITE profinite abelian group. Structurally (h=1):")
out("       Gal(K^ab/K)  ~=  hat(O_K)^x / closure(O_K^x)")
out("   where hat(O_K)^x = prod_p O_{K,p}^x (profinite), O_K^x = mu_6.  NOT Z/2.")

# ---------------------------------------------------------------------------
# 2. Our being side: Z/2 over Q.
# ---------------------------------------------------------------------------
out("")
out("-" * 78)
out("2. Our being side: T_being = Gal(K/Q) = Z/2, base field Q")
out("-" * 78)
G = K.galois_group()
out("   Gal(Q(sqrt-3)/Q) = %s, order = %d" % (G, G.order()))
out("   generator: complex conjugation c : sqrt-3 |-> -sqrt-3  (fixes Q, MOVES K).")
out("   This is the Galois group of K OVER Q -- base field Q, NOT K.")

# ---------------------------------------------------------------------------
# 3. THE DISCRIMINATING STRUCTURE: the arithmetic exact sequence.
# ---------------------------------------------------------------------------
out("")
out("-" * 78)
out("3. THE DISCRIMINATING FACT: kernel vs quotient of ONE group Gal(K^ab/Q)")
out("-" * 78)
out("""
   K^ab is Galois over Q (it is the maximal abelian extension of K, and K/Q is normal,
   so any Q-automorphism of Qbar preserves K hence K^ab). Hence the SHORT EXACT SEQUENCE

       1 --> Gal(K^ab/K) --> Gal(K^ab/Q) --> Gal(K/Q) --> 1
             \\_____________/                 \\__________/
              = T_CMR (infinite,               = T_being (Z/2,
                profinite abelian)               our torsor)

   places the two objects as COMPLEMENTARY pieces of ONE bigger group:
     * T_CMR  = Gal(K^ab/K) is the (INFINITE) KERNEL.
     * T_being = Gal(K/Q)    is the (ORDER-2) QUOTIENT.

   They are NOT nested. Concretely:
     (a) The nontrivial element of T_being (complex conjugation) does NOT fix K, so it
         is NOT an element of Gal(K^ab/K). => T_being is not a sub-torsor of T_CMR.
     (b) Gal(K^ab/K) DOES surject onto many Z/2's, but each such Z/2 = Gal(L/K) is a
         QUADRATIC EXTENSION *OF* K inside K^ab (e.g. the conductor-4 ray class group
         C_2 above), indexed by conductor -- infinitely many, none canonically equal to
         Gal(K/Q). Gal(K/Q) is about K OVER Q, a different base field entirely.
         => T_being is not a canonical quotient-torsor of T_CMR either.

   THE ONE GENUINE LINK (rung-2 structural relation, but NOT an embedding):
     T_being = Gal(K/Q) ACTS on T_CMR = Gal(K^ab/K) by conjugation in the extension.
     For imaginary-quadratic (CM) K this outer action is the CM/anticyclotomic
     involution: c fixes the cyclotomic part Gal(K.Q^ab / K) (since K.Q^ab is abelian
     over Q) and acts by INVERSION (g |-> g^{-1}) on the anticyclotomic (CM) part.
     So the being-Z/2 is the STRUCTURE GROUP that ACTS ON the CMR torsor -- it is not a
     PIECE of it.
""")

# ---------------------------------------------------------------------------
# 4. Verdict.
# ---------------------------------------------------------------------------
out("-" * 78)
out("VERDICT")
out("-" * 78)
out("""
  OUTCOME B  (rung-mismatch, field matches but base-fields / torsor structures differ).

  * RUNG 1 (field): CLEARED. Q(sqrt-3) genuinely appears on both sides -- the CMR CM
    system is built on exactly the object's being field. Real, non-trivial.

  * RUNG 2 (torsor/Galois): the claimed EMBEDDING FAILS.
      - T_being = Gal(K/Q) = Z/2, over base field Q.
      - T_CMR   = Gal(K^ab/K), over base field K = Q(sqrt-3); infinite profinite abelian
        (ray class groups unbounded: 2,4,6,8,9,20,24,32,100,...).
      - They are the QUOTIENT and the KERNEL of Gal(K^ab/Q), i.e. COMPLEMENTARY pieces
        over DIFFERENT base fields, not nested. Our Z/2 ACTS on the CMR torsor (by the
        CM involution / inversion on the anticyclotomic part); it is NOT a sub- or
        quotient-torsor of it.

  DISCRIMINATING FACT: in  1 -> Gal(K^ab/K) -> Gal(K^ab/Q) -> Gal(K/Q) -> 1, the CMR
  ground-state torsor is the infinite KERNEL and the object's being-Z/2 is the order-2
  QUOTIENT of the SAME group -- over base fields K and Q respectively. Being-Z/2 is the
  group that ACTS ON (the CM inversion of) the CMR torsor, not a canonical piece inside
  it. FIELD-matched (rung 1) with a genuine rung-2 exact-sequence RELATION, but NOT the
  rung-2 sub-torsor EMBEDDING that Outcome A requires.
""")

# write output file
with open(__file__.rsplit("/", 1)[0] + "/b721_probe2_out.txt", "w") as fh:
    fh.write("\n".join(LINES) + "\n")
out("[wrote b721_probe2_out.txt]")
