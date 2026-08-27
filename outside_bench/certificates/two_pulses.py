#!/usr/bin/env python3
"""MEMO-90 CELL: THE TWO PULSES — the record's two squared steps, side by
side and exact: the beat's square is an ISOMETRY (it cannot drive
expansion — theorem, from banked pins), and the substitution's square is
the fiber MONODROMY with exact stretch phi^2 per tick (fresh exact
computation, including the GL2(Z) conjugacy to the banked memo-49 tick
matrix).  Then the expansion question is TYPED through the banked
parity x dimension law, with the unpaid weld (H90's LEAP-1) named as a
fence, not crossed.  Owner question (2026-08-27): "could the heartbeat
drive the expansion of the universe" — this cell is its register row's
certificate (THE_OWNER_REGISTER R13).

PREREGISTERED (two-outcome where fresh):
  FACT 1 (banked, re-pinned): beta^2 = meridian on the carrier (memo 46)
     and the beat preserves EVERY geodesic length (memo 81: mirror =
     length-even, torsion-odd).  A length-spectrum-preserving map cannot
     change any distance: the beat CANNOT drive expansion.  (Prose
     context, not machine: Mostow rigidity — the isometry class is the
     object; expansion is not in the beat's verb set.)
  FACT 2 (fresh, exact): sigma: a -> ab, b -> a abelianizes to
     S = [[1,1],[1,0]]; char poly x^2 - x - 1, Perron root phi.
     S^2 = [[2,1],[1,1]] EXACTLY; char poly x^2 - 3x + 1 with root
     phi^2 — the SAME trace-3/disc-5 golden polynomial banked in memo 49.
  FACT 3 (fresh, TWO-OUTCOME): the banked memo-49 fiber-tick matrix
     F = [[0,-1],[1,3]] is GL2(Z)-CONJUGATE to S^2 (expected FOUND:
     x^2-3x+1 has ring Z[phi], class number 1, so one conjugacy class);
     a failed search to the preregistered bound banks as a finding and
     the twin claim drops to "same char poly" — either outcome banks.
  FACT 4 (typing, printed as FENCES — no physical assertion):
     the pulse-driven expansion FORM (ratio phi per tick, exponential)
     is dimensionless -> conditionally object-side under the banked
     parity x dimension law (B1168); the RATE (per second) is a scale ->
     observer-side by the same law; H90's LEAP-1 (sigma-clock = cosmic
     clock) is UNPAID; the Lambda<0 (object, hyperbolic) vs Lambda>0
     (observed) tension is named.  None of these fences are crossed.
Gate 5 untouched (no measured value enters; the typing is by the banked
law, the numbers are phi and matrix entries).
"""
import os, sympy as sp
from sympy import Matrix, symbols, sqrt, Rational, expand, simplify

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.environ.get("BENCH_OUT") or os.path.join(HERE, "..", "outputs")

def has(fname, needle):
    with open(os.path.join(OUT, fname)) as f:
        txt = f.read()
    assert needle in txt, f"PIN MISSING in {fname}: {needle!r}"
    return True

# ---------- FACT 1: the isometric pulse (banked, re-pinned) ----------
has("carrier_out.txt", "beta_Psi^2 = rho_Psi(a) (the MERIDIAN on the carrier): True")
has("geodesic_tongue_out.txt", "lengths invariant, torsion negated")
has("geodesic_tongue_out.txt", "3.450219 vs 3.450219 (equal)")
has("geodesic_tongue_out.txt", "the LENGTH spectrum (the gravitational moduli) is\nmirror-even")
print("FACT 1: banked pins hold — beta^2 = meridian (memo 46) and the beat")
print("   preserves EVERY geodesic length (memo 81: length-even, torsion-odd).")
print("   A map that fixes the whole length spectrum changes no distance:")
print("   THE BEAT CANNOT DRIVE EXPANSION — its stretch factor is exactly 1.")

# ---------- FACT 2: the stretching pulse (fresh, exact) ----------
x = symbols('x')
S = Matrix([[1,1],[1,0]])            # sigma: a -> ab, b -> a, abelianized
cpS = S.charpoly(x).as_expr()
assert expand(cpS - (x**2 - x - 1)) == 0, cpS
phi = (1 + sqrt(5))/2
assert simplify(phi**2 - phi - 1) == 0                  # phi is the Perron root
assert all(v > 0 for v in [S[0,0]+S[0,1], S[1,0]+S[1,1]])
S2 = S*S
assert S2 == Matrix([[2,1],[1,1]]), S2                   # exact matrix identity
cpS2 = S2.charpoly(x).as_expr()
assert expand(cpS2 - (x**2 - 3*x + 1)) == 0, cpS2
assert simplify(phi**4 - 3*phi**2 + 1) == 0             # phi^2 is a root, exactly
has("trace_three_out.txt", "characteristic polynomial: x^2 - 3x + 1   trace 3, det 1, disc 5")
has("trace_three_out.txt", "spectral radius phi^2")
print("FACT 2: sigma abelianized S = [[1,1],[1,0]]; char poly x^2 - x - 1,")
print("   Perron root phi = (1+sqrt5)/2 (exact).  S^2 = [[2,1],[1,1]] exactly;")
print("   char poly x^2 - 3x + 1 with root phi^2 — the SAME golden trace-3")
print("   polynomial banked in memo 49 (pin verified).  Stretch per tick: phi.")

# ---------- FACT 3: the twin (two-outcome conjugacy search) ----------
F = Matrix([[0,-1],[1,3]])           # memo 49's abelianized fiber tick
assert expand(F.charpoly(x).as_expr() - (x**2 - 3*x + 1)) == 0
BOUND = 6
found = None
for a in range(-BOUND, BOUND+1):
    for b in range(-BOUND, BOUND+1):
        for c in range(-BOUND, BOUND+1):
            for d in range(-BOUND, BOUND+1):
                if a*d - b*c in (1, -1):
                    P = Matrix([[a,b],[c,d]])
                    if P*F == S2*P:
                        found = P
                        break
            if found: break
        if found: break
    if found: break
assert found is not None, "no GL2(Z) conjugator to bound 6 — bank the refusal"
assert found*F*found.inv() == S2
print(f"FACT 3: FOUND — P = {found.tolist()} (det {found.det()}) gives")
print("   P F P^-1 = S^2 exactly: the banked memo-49 fiber tick and the")
print("   substitution's square are ONE GL2(Z) conjugacy class — sigma^2 IS")
print("   the monodromy.  The record's two squared steps, exact:")
print("     beta^2  = meridian   : stretch 1      (isometric pulse, memo 46)")
print("     sigma^2 ~ monodromy  : stretch phi^2  (golden pulse, this cell)")
has("trace_three_out.txt", "hyperbolic (entropy 2 log phi) on the geometric fiber")
print("   entropy cross-check: log(phi^2) = 2 log phi = the banked fiber entropy.")

# ---------- FACT 4: the typing (fences printed, not crossed) ----------
print("""
FACT 4 — THE TYPING (through the banked parity x dimension law, B1168):
   FORM of a pulse-driven expansion law: 'lengths multiply by phi per
     sigma-tick' — a DIMENSIONLESS ratio, exponential in tick count.
     Object-side CONDITIONALLY: conditional on H90's LEAP-1 (that the
     sigma-clock is the cosmological clock), which is UNPAID.
   RATE of the observed expansion: a dimensionful scale (per second).
     Observer-side BY THEOREM (the dimension half of the law): the
     object prices no seconds.
   NAMED TENSION (not resolved here): the object's geometry is
     hyperbolic (Lambda < 0 flavor); the observed expansion is
     Lambda > 0.  The weld, if any, is the owner's to price.

THE TWO PULSES: the record carries exactly two squared steps on the one
object — the beat's (isometric: it CANNOT drive expansion, theorem) and
the substitution's (stretching: factor phi per tick, exact, and its
square IS the fiber monodromy in one GL2(Z) class with the banked
memo-49 tick).  If anything in this record drives expansion it is the
golden pulse, not the heartbeat — and only across LEAP-1, which remains
unpaid.  Gate 5 untouched.""")
