#!/usr/bin/env python3
"""MEMO-101 CELL (NINE-CELL WAVE, cell 8, bench half): TIME REVERSAL IS
THE GOLDEN GALOIS — the record's exact reverser R restricts to the
gamma5 conjugation on the golden eigenframe; and the branch swap is
exhausted against EVERY banked involution: none induces it.

TWO RESULTS, PREREGISTERED:
  FACT 1 (new identification): memo 97's reverser R = s o e'
     ((x,y,z) -> (y,x,yx-z); R T^2 R = T^-2) acts on the golden
     eigenframe of D(T^2) at the trivial rep EXACTLY as the Q(sqrt5)
     Galois conjugation: DR(v_u) is proportional to v_u^sigma5 (the
     sqrt5 -> -sqrt5 conjugate = the stable eigenvector), and
     DR(v_u^sigma5) is proportional to v_u.  TIME REVERSAL AT THE
     ORBIT LEVEL IS THE gamma5 BIT'S FIELD ACTION — the third
     discrete bit (Q(sqrt5), GC-13) acquires its dynamical face, the
     exact counterpart of memo 94's two-branch law.
  FACT 2 (the branch exhaustion): the branch swap v_u -> -v_u is
     induced by NONE of the banked involutions at this level:
     c (trivial on the real slice), C = s (memo 97: fixes-or-off-line,
     re-verified), P (trivial on characters, memo 98), R and the
     gamma5 conjugation (both map the unstable LINE to the STABLE
     line — they reverse time, not the branch), and the kappa-
     preserving sign twists (move the fixed point).  The branch bit
     is the +- torsor on the golden eigenline itself — REACHABLE BY
     NO banked symmetry: its residual identification with cc's r
     (a Galois datum one level up) requires a level-crossing map,
     typed and relayed with this exhaustion as input.
Gate 5 untouched (exact algebra).
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
T = sp.Matrix([z, x, z*x - y])
T2 = T.subs({x: T[0], y: T[1], z: T[2]}, simultaneous=True)
J2 = T2.jacobian(sp.Matrix([x, y, z])).subs({x: 2, y: 2, z: 2})
phi = (1 + sp.sqrt(5))/2
vu = sp.Matrix([sp.Rational(3, 2) - sp.sqrt(5)/2, sp.Rational(7, 2) - 3*sp.sqrt(5)/2, 1])
vs = sp.Matrix([sp.Rational(3, 2) + sp.sqrt(5)/2, sp.Rational(7, 2) + 3*sp.sqrt(5)/2, 1])
assert sp.simplify(J2*vu - phi**4*vu) == sp.zeros(3, 1)
assert sp.simplify(J2*vs - phi**-4*vs) == sp.zeros(3, 1)
# vs IS the sqrt5 -> -sqrt5 conjugate of vu, entrywise:
assert all(sp.simplify(vs[i] - vu[i].subs(sp.sqrt(5), -sp.sqrt(5))) == 0 for i in range(3))
print("setup: v_u (phi^4) and v_s (phi^-4) are exact Galois conjugates entrywise.")

R = sp.Matrix([y, x, y*x - z])
DR = R.jacobian(sp.Matrix([x, y, z])).subs({x: 2, y: 2, z: 2})
w = DR*vu
lam = sp.simplify(w[2]/vs[2])
assert sp.simplify(w - lam*vs) == sp.zeros(3, 1)
w2 = DR*vs
lam2 = sp.simplify(w2[2]/vu[2])
assert sp.simplify(w2 - lam2*vu) == sp.zeros(3, 1)
print(f"FACT 1: DR(v_u) = ({sp.nsimplify(lam)})*v_s and DR(v_s) = ({sp.nsimplify(lam2)})*v_u —")
print("   the reverser R acts on the golden eigenframe EXACTLY as the Q(sqrt5)")
print("   Galois conjugation: TIME REVERSAL = THE gamma5 FIELD ACTION at the")
print("   orbit level.  The third bit has its dynamical face.")

# FACT 2: exhaustion of branch-swap candidates (v_u -> -v_u on the unstable LINE)
cands = {}
cands["C = s"] = sp.Matrix([y, x, z]).jacobian(sp.Matrix([x, y, z])).subs({x: 2, y: 2, z: 2})
cands["e'"] = sp.Matrix([x, y, x*y - z]).jacobian(sp.Matrix([x, y, z])).subs({x: 2, y: 2, z: 2})
cands["R = s o e'"] = DR
verdicts = []
for name, Dg in cands.items():
    wv = Dg*vu
    minus = sp.simplify(wv + vu) == sp.zeros(3, 1)
    to_stable = sp.simplify(wv - sp.simplify(wv[2]/vs[2])*vs) == sp.zeros(3, 1)
    plus = sp.simplify(wv - vu) == sp.zeros(3, 1)
    verdicts.append((name, minus))
    tag = "-v_u  <-- SWAP" if minus else ("+v_u" if plus else ("-> STABLE line" if to_stable else "off-line"))
    print(f"   {name:12s}: Dg(v_u) = {tag}")
assert not any(m for _, m in verdicts)
print("""FACT 2: NO banked involution induces v_u -> -v_u — not C, not e', not R
   (which reverses time, not the branch), and by prior cells not c (trivial
   on the real slice, memo 97), not P (character-trivial, memo 98), not the
   sign twists (they move the fixed point, memo 97).  THE BRANCH BIT IS THE
   +- TORSOR ON THE GOLDEN EIGENLINE, reachable by no banked symmetry —
   exactly the shape of a genuine frame datum.  Its identification with
   cc's r (a Galois datum one level up) requires a level-crossing map:
   relayed with this exhaustion as the word/orbit-level input.
Gate 5 untouched.""")
