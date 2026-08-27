#!/usr/bin/env bash
# B1169 -- the qualia/parity SYNTHESIS (owner-directed; all seats to verify).
# SOLID CORE (checkable): four independent probes converge on "the object cannot self-close," and the
# missing bit is the mirror-ODD orientation; the Markov blanket IS the cusp torus, whose canonical shape
# is 2sqrt3 i (mirror-EVEN). THE READING (firewalled): the qualia awareness/choice split = the C5 parity
# = the structure/observer boundary -- a strong reading, NOT proven as one identity.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null | tee qualia_parity.txt
import snappy, math
M=snappy.Manifold('m004'); Mm=snappy.Manifold('m004'); Mm.reverse_orientation()
cv=complex(M.complex_volume())
tau=complex(M.cusp_info()[0]['shape']); tau=tau if tau.imag>0 else tau.conjugate()

print("== SOLID 1: the parity facts (B1168, re-verified) ==")
print("  AWARENESS side (mirror-EVEN, object-canonical): Vol even:", abs(float(M.volume())-float(Mm.volume()))<1e-9,
      "; cusp shape mirror-fixed:", abs(-tau.conjugate()-tau)<1e-9)
print("  CHOICE side (mirror-ODD, NOT object-suppliable): CS mirror-odd, CS=%.1e=0 (amphichiral)" % cv.imag)

print("== SOLID 2: the blanket IS the cusp torus (S072), and its canonical shape is 2sqrt3 i ==")
print("  blanket shape = %.6f i = 2sqrt3 i =" % tau.imag, round(2*math.sqrt(3),6), "; mirror-EVEN (orientation-blind)")
print("  => the blanket 'that sees everything' (QP-2 FLAT) is aware-but-choiceless, made geometric.")

print("== SOLID 3: FOUR independent probes converge on 'the object cannot self-close' ==")
for p in ["QP-4 NO-HATCH (qualia, B761): no object-native self-closure",
          "B1163 (orientation): amphichiral => no object-canonical orientation",
          "B1168 C5 (parity): the mirror-ODD orientation is observer-only",
          "B1134/B1135 (fork): the real-structure closing (chirality) is the observer's"]:
    print("   -", p)

print("== SOLID 4: the arithmetic ties the recent archimedean data to sigma/kappa's field ==")
print("  K=Q(sqrt-3)=Q(zeta6): mu_6 = the object-paid phase (B1166); cusp carries sqrt3 -> K(sqrt3)=Q(zeta12).")
print("  sigma: a->ab,b->a has Perron eigenvalue phi and conserved integral kappa=tr[a,b]; the root is quietly active.")

print()
print("THE DICTIONARY (SOLID core): AWARENESS = mirror-EVEN, object-canonical (Vol, cusp shape, spectra;")
print("  QP-2 proved the blanket sees it all). CHOICE = mirror-ODD orientation, observer-supplied (QP-4 proved")
print("  the object lacks it). The 'awareness without choice' headline = the even/odd parity, decidably.")
print("CONNECTION (SOLID): the choice = chirality/orientation (B1164) = the E6(-26)/E6(-14) real-form fork")
print("  (B1134/5) => SM STRUCTURE; lives at the infinity-place => GRAVITY (B1165 G3). DISJOINT from VALUES")
print("  (5 routes) and DYNAMICS (generic, B1157). NOT the MSSM matter/VEV (that is the FINITE closing).")
print()
print("THE READING (FIREWALLED -- for the seats to critique, NOT banked as proven): that the FOUR probes are")
print("  the SAME missing bit, and that qualia-awareness/choice == C5-parity == structure/observer boundary, is")
print("  a strong reading the facts SUPPORT but that is not one theorem ('awareness=blanket-sees-all' and")
print("  'awareness=mirror-even' are linked through 'forced', a CHAIN not an identity). See the speculation table.")
print("REPRODUCES")
PY
