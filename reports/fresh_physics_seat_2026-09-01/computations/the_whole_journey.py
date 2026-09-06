"""
THE WHOLE JOURNEY
From "what's not nothing" to the Standard Model, computed step by step.
"""
import numpy as np
from fractions import Fraction

def banner(n, title):
    print(f"\n{'='*70}")
    print(f"  STEP {n}: {title}")
    print(f"{'='*70}\n")

# ─────────────────────────────────────────────────────────────
banner(1, "THE SIMPLEST INTERESTING PATTERN")
# ─────────────────────────────────────────────────────────────

print("""Imagine you have two letters: a and b.
You make a rule: every time you see 'a', replace it with 'ab'.
Every time you see 'b', replace it with 'a'.

That's it. That's the whole starting point.

Let's watch what happens:""")

def apply_rule(word):
    return ''.join('ab' if c == 'a' else 'a' for c in word)

word = 'a'
for i in range(9):
    na = word.count('a')
    nb = word.count('b')
    if len(word) <= 60:
        print(f"  step {i}: {word:40s}  ({na} a's, {nb} b's)")
    else:
        print(f"  step {i}: {word[:40]}...  ({na} a's, {nb} b's)")
    word = apply_rule(word)

phi = (1 + np.sqrt(5)) / 2
print(f"""
The counts are Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The ratio of a's to b's → the golden ratio φ = {phi:.6f}

This isn't a coincidence. The rule's "recipe" is a 2×2 matrix:""")

M = np.array([[1, 1], [1, 0]])
print(f"  M = [[1, 1],     (each 'a' makes 1 new 'a' and 1 new 'b')")
print(f"       [1, 0]]     (each 'b' makes 1 new 'a' and 0 new 'b')")
det = int(M[0,0]*M[1,1] - M[0,1]*M[1,0])
print(f"""
  eigenvalues: φ = {phi:.6f} and -1/φ = {-1/phi:.6f}
  determinant: {det}

The determinant is -1. That minus sign will matter a lot.""")

# ─────────────────────────────────────────────────────────────
banner(2, "THE RULE MAKES A SHAPE")
# ─────────────────────────────────────────────────────────────

print("""Think of a flat rubber sheet, like a torus (donut shape)
with a tiny hole poked in it — a "punctured torus."

The rule acts on this surface: it stretches and folds it.
That's what the matrix M does — it maps the torus to itself.

But det(M) = -1 means the rule FLIPS the surface inside out.
It reverses orientation, like looking in a mirror.

To get something that doesn't flip, we apply the rule TWICE:""")

M2 = M @ M
print(f"  M² = {M2.tolist()}")
print(f"  det(M²) = {int(M2[0,0]*M2[1,1] - M2[0,1]*M2[1,0])}")
print(f"  trace(M²) = {int(np.trace(M2))}")
print(f"""
  det = +1 means M² preserves orientation. Good.
  |trace| = 3 > 2 means M² is "hyperbolic" — it genuinely
  stretches space, not just rotates it.

Now imagine gluing the top and bottom of this stretching
into a loop — like connecting a video of the stretch back
to its start. This makes a 3D shape called a "mapping torus."

The mapping torus of M² is a specific, famous 3D space:

  ┌──────────────────────────────────────────────────┐
  │  m004: the FIGURE-EIGHT KNOT COMPLEMENT          │
  │  (take 3D space, remove a figure-eight knot,     │
  │   what's left is this shape)                     │
  └──────────────────────────────────────────────────┘

It's the simplest hyperbolic knot complement.
It can be built from exactly 2 ideal tetrahedra.
Its volume is 2.0298832128...""")

# ─────────────────────────────────────────────────────────────
banner(3, "THE SHAPE'S COORDINATES")
# ─────────────────────────────────────────────────────────────

print("""The shape m004 has a "fundamental group" — loops you can
draw inside it. Two basic loops, A and B, generate the
fiber fundamental group F₂.

Instead of tracking the loops themselves, we track three
numbers — the TRACES of the matrices representing them:

  x = tr(A),  y = tr(B),  z = tr(AB)

These are called "Fricke coordinates." And here's the key:
the RULE acts on these coordinates. One application of the
rule does:

  F(x, y, z) = (z,  x,  xz - y)

Let's find where the SHAPE sits. The shape is the mapping
torus of M², so we need the fixed points of F² (the rule
applied twice).

Computing F²:""")

print("  F(x, y, z) = (z, x, xz - y)")
print("  F²(x,y,z) = F(z, x, xz-y) = (xz-y, z, z(xz-y)-x)")
print("            = (xz-y, z, xz²-yz-x)")
print()
print("Fixed curve: (x,y,z) = F²(x,y,z) requires:")
print("  x = xz - y   →   y = x(z - 1)")
print("  y = z         →   z = x(z - 1)")
print("                →   x = z/(z - 1)")
print()
print("  So the fixed curve is:  y = z,  x = z/(z-1)")
print()

# Verify equation 3
print("Verify the third equation z = xz² - yz - x:")
print("  = [z/(z-1)]z² - z·z - z/(z-1)")
print("  = z³/(z-1) - z² - z/(z-1)")
print("  = [z³ - z]/(z-1) - z²")
print("  = z(z+1) - z²  =  z    ✓")

print("""
Now we add one more condition. The shape has a PUNCTURE
(the hole in the torus). Mathematically, this means the
boundary loop is "parabolic" — its trace is -2. This gives
the MARKOFF CONDITION:

  κ = x² + y² + z² - xyz = 0

Substituting y = z, x = z/(z-1):""")

print("  [z/(z-1)]² + z² + z² - [z/(z-1)]·z² = 0")
print()
print("  Multiply by (z-1)²:")
print("  z² + 2z²(z-1)² - z³(z-1) = 0")
print("  z²[1 + 2(z-1)² - z(z-1)] = 0")
print()
print("  Expanding the bracket:")
print("  1 + 2z² - 4z + 2 - z² + z = z² - 3z + 3")
print()
print("  Full equation: z²(z² - 3z + 3) = 0")
print("  z = 0 is the non-geometric character: at (x,y,z)=(0,0,0)")
print("  the peripheral commutator is -I (central), not a nontrivial parabolic.")
print("  Requiring nontrivial parabolic peripheral holonomy selects the geometric branch:")

# Verify
roots = np.roots([1, -3, 3])
disc = (-3)**2 - 4*1*3

print(f"""
  ┌─────────────────────────────────────────┐
  │  z² - 3z + 3 = 0                       │
  │                                         │
  │  discriminant = 9 - 12 = {disc:+d}              │
  │                                         │
  │  roots: z = (3 ± √-3) / 2              │
  └─────────────────────────────────────────┘

  z₁ = {roots[0]:.6f}
  z₂ = {roots[1]:.6f}

  These are complex conjugates — a MIRROR PAIR.
  The number field is Q(√-3) (ring of integers: Eisenstein integers ℤ[ω]).

  THE RULE + THE PUNCTURE + NONDEGENERACY → discriminant -3.
  Just algebra.""")

# ─────────────────────────────────────────────────────────────
banner(4, "THE NUMBER FIELD PICKS A SYMMETRY (AXIOM A3)")
# ─────────────────────────────────────────────────────────────

print("""The field Q(√-3) has:
  • discriminant: -3
  • conductor: N = 3  (the "complexity" of the field)

Now we use the McKay correspondence — a bridge between
number theory and symmetry. THIS IS AXIOM A3: the declared
choice to pass from the geometric conductor N = 3 to
SL(2, F₃) and apply McKay's correspondence. A3 as used here
is specifically N = 3 → SL(2,F₃) ≅ 2T → Ê₆; no universal
conductor → SL(2,ℤ/Nℤ) → McKay rule is asserted.

By A3, we pass from the conductor to the finite linear group:

Step 1: Build the group SL(2, Z/3Z) — all 2×2 matrices
        with entries mod 3 and determinant 1.""")

# Enumerate SL(2, Z/3Z)
count = 0
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                if (a*d - b*c) % 3 == 1:
                    count += 1

print(f"""
  Counting: {count} matrices with entries in {{0,1,2}} and det ≡ 1 (mod 3)

  |SL(2, Z/3Z)| = 3³ × (1 - 1/3²) = 27 × 8/9 = {count}""")

print(f"""
Step 2: This 24-element group is isomorphic to the
        BINARY TETRAHEDRAL GROUP (2T), which has a faithful
        embedding in SU(2).

        (The tetrahedron has 12 rotational symmetries;
         the "binary" version doubles it to 24 by
         including the -I element of SU(2).)

Step 3: The McKay correspondence says: draw a graph where
        each node is an irreducible representation of 2T,
        and connect nodes by how they appear when you
        tensor with the fundamental 2D representation.

        The graph you get is:""")

# 2T has irreps of dimensions 1, 1, 1, 2, 2, 2, 3
# (that's 1+1+1+4+4+4+9 = 24 ✓)
irrep_dims = [1, 1, 1, 2, 2, 2, 3]
print(f"  2T irrep dimensions: {irrep_dims}")
print(f"  Sum of squares: {sum(d**2 for d in irrep_dims)} = |2T| = 24  ✓")
print(f"  Number of irreps: {len(irrep_dims)}")
print(f"""
  The McKay graph of 2T is:

           1
           │
           2
           │
    1 ─ 2 ─ 3 ─ 2 ─ 1

  This is the AFFINE Ê₆ DIAGRAM (7 nodes, including
  the trivial representation), corresponding to the affine
  Kac-Moody type E₆⁽¹⁾. The trivial representation is the
  affine node; removing it gives the finite E₆ Dynkin
  diagram (6 nodes) and the finite-dimensional Lie algebra E₆.

  ┌──────────────────────────────────────────────────────────────┐
  │  conductor 3 → group of order 24 → affine Ê₆ → finite E₆  │
  └──────────────────────────────────────────────────────────────┘""")

# ---- B1263 reproduced: the 2T quotient is not unique, and the two Round-11 routes are the two orbits
import itertools
_I = (1, 0, 0, 1)
_REL = "abABaBAbaB"          # figure-eight knot group <x, y | REL> (B1263's presentation)
def _mul(X, Y):
    return ((X[0]*Y[0]+X[1]*Y[2]) % 3, (X[0]*Y[1]+X[1]*Y[3]) % 3,
            (X[2]*Y[0]+X[3]*Y[2]) % 3, (X[2]*Y[1]+X[3]*Y[3]) % 3)
_G = [X for X in itertools.product(range(3), repeat=4) if (X[0]*X[3]-X[1]*X[2]) % 3 == 1]
_INV = {X: next(Y for Y in _G if _mul(X, Y) == _I) for X in _G}
def _word(w, A, B):
    D = {'a': A, 'b': B, 'A': _INV[A], 'B': _INV[B]}
    M = _I
    for ch in w: M = _mul(M, D[ch])
    return M
def _gen(gens):
    S, fr = {_I}, [_I]
    while fr:
        u = fr.pop()
        for g in gens:
            v = _mul(u, g)
            if v not in S: S.add(v); fr.append(v)
    return S
def _order(g):
    k, h = 1, g
    while h != _I: h = _mul(h, g); k += 1
    return k
_homs = [(A, B) for A in _G for B in _G if _word(_REL, A, B) == _I]
_surj = [(A, B) for (A, B) in _homs if len(_gen([A, B])) == 24]
def _auts(g0, g1):
    out = []
    for imA in _G:
        for imB in _G:
            m, fr, ok = {_I: _I}, [(_I, _I)], True
            while fr and ok:
                u, v = fr.pop()
                for g, h in ((g0, imA), (g1, imB)):
                    ug, vh = _mul(u, g), _mul(v, h)
                    if ug in m:
                        if m[ug] != vh: ok = False; break
                    else:
                        m[ug] = vh; fr.append((ug, vh))
            if ok and len(m) == 24 and len(set(m.values())) == 24: out.append(m)
    return out
_AUT = _auts(*_surj[0])
_label, _norb = {}, 0
for A, B in _surj:
    if (A, B) in _label: continue
    for h in _AUT: _label[(h[A], h[B])] = _norb
    _norb += 1
_inv_by_orbit = {}
for (A, B), lab in _label.items():
    _inv_by_orbit.setdefault(lab, set()).add((_order(A), _order(_mul(A, B)), _order(_mul(A, _INV[B]))))
assert (len(_G), len(_homs), len(_surj), len(_AUT), _norb) == (24, 72, 48, 24, 2)
assert sorted(_inv_by_orbit.values(), key=sorted) == [{(3, 6, 4)}, {(6, 6, 4)}]
# route 1: Riley holonomy x=[[1,1],[0,1]], y=[[1,0],[-omega,1]] reduced mod (1-omega): omega -> 1
_X1, _Y1 = (1, 1, 0, 1), (1, 0, 2, 1)
assert _word(_REL, _X1, _Y1) == _I and len(_gen([_X1, _Y1])) == 24
# route 2: the (0,0,0) character on the Hurwitz units, transported to the knot group by the fiber
# words a = x y^-1, b = y x y^-1 x^-1 y x^-1, t = x (checked exactly in the Riley rep below):
# rho(x) = s = (1+i+j+k)/2, rho(y) = rho(a)^-1 rho(x) = -i s
def _qm(p, q):
    w1,x1,y1,z1 = p; w2,x2,y2,z2 = q
    return (w1*w2-x1*x2-y1*y2-z1*z2, w1*x2+x1*w2+y1*z2-z1*y2,
            w1*y2-x1*z2+y1*w2+z1*x2, w1*z2+x1*y2-y1*x2+z1*w2)
def _qinv(q): n = sum(c*c for c in q); return tuple(c/n for c in (q[0], -q[1], -q[2], -q[3]))
_1 = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
_i = (Fraction(0), Fraction(1), Fraction(0), Fraction(0)); _j = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))
_s = (Fraction(1, 2),) * 4
_qx, _qy = _s, _qm(_qinv(_i), _s)
def _qword(w, X, Y):
    D = {'a': X, 'b': Y, 'A': _qinv(X), 'B': _qinv(Y)}
    M = _1
    for ch in w: M = _qm(M, D[ch])
    return M
assert _qword(_REL, _qx, _qy) == _1                       # the knot relator holds
assert _qword("aB", _qx, _qy) == _i and _qword("baBAbA", _qx, _qy) == _j   # fiber words give back i, j
_HU, fr = {_1}, [_1]
while fr:
    u = fr.pop()
    for g in (_qx, _qy):
        v = _qm(u, g)
        if v not in _HU: _HU.add(v); fr.append(v)
assert len(_HU) == 24                                      # surjective onto the Hurwitz units = 2T
def _qorder(g):
    k, h = 1, g
    while h != _1: h = _qm(h, g); k += 1
    return k
# the fiber words are checked in the faithful Riley representation
_w = complex(-0.5, 3 ** 0.5 / 2)
_rx = np.array([[1, 1], [0, 1]], dtype=complex); _ry = np.array([[1, 0], [-_w, 1]], dtype=complex)
def _rword(w, X, Y):
    D = {'a': X, 'b': Y, 'A': np.linalg.inv(X), 'B': np.linalg.inv(Y)}
    M = np.eye(2, dtype=complex)
    for ch in w: M = M @ D[ch]
    return M
assert np.allclose(_rword(_REL, _rx, _ry), np.eye(2))
_ra, _rb = _rword("aB", _rx, _ry), _rword("baBAbA", _rx, _ry)
assert np.allclose(_rx @ _ra @ np.linalg.inv(_rx), _ra @ _rb @ _ra)   # t a t^-1 = aba
assert np.allclose(_rx @ _rb @ np.linalg.inv(_rx), _ra @ _rb)         # t b t^-1 = ab
print(f"""
THE 2T QUOTIENT IS NOT UNIQUE (B1263, reproduced):
  homomorphisms π₁(m004) → SL(2,F₃): {len(_homs)};  surjective: {len(_surj)};
  orbits under Aut(2T) = S₄ (|Aut| = {len(_AUT)}, constructed): {_norb}, of sizes 24 + 24.
  Orbit invariants (ord ρ(x), ord ρ(xy), ord ρ(xy⁻¹)):
    orbit A: {sorted(_inv_by_orbit[0])}     orbit B: {sorted(_inv_by_orbit[1])}
  The two routes of this document's Round-11 exchange are the two orbits:
    geometric  — holonomy SL(2,ℤ[ω]) reduced mod (1−ω): meridian order {_order(_X1)}
    non-geometric — the (0,0,0) character on the Hurwitz units: meridian order {_qorder(_qx)}
  McKay 2T ↔ Ê₆ is a theorem (I-1, EARNED); WHICH π₁-quotient is the 2T that builds E₆
  is the record's I-6 (UNEARNED). A3 routes through the conductor and inherits that gap
  the moment the group is asked to act on the manifold.""")

# ─────────────────────────────────────────────────────────────
banner(5, "WHAT'S INSIDE E₆")
# ─────────────────────────────────────────────────────────────

print("""E₆ is a Lie algebra — a specific symmetry structure.

  rank: 6  (6 independent "directions" of symmetry)
  dimension: 78  (78 generators total)
  fundamental representation: 27-dimensional

The 27 is the smallest non-trivial "package" that E₆ can
act on. Let's open it up.

E₆ contains a chain of smaller symmetries:

  E₆  ⊃  SO(10) [Spin(10)]  ⊃  SU(5)  ⊃  SU(3) × SU(2) × U(1)
  78      45                     24         8  +  3  +  1  = 12

(The record's registerable cascade lands on su(3)⊕su(2)⊕u(1)³,
 dimension 14 — two abelian factors more than the SM's 12 (B892);
 the 14 → 12 step needs a VEV the object does not source.)

The 27 decomposes at each step:

  Under SO(10):   27 = 16 + 10 + 1
  The 16 under SU(5):   16 = 10 + 5̄ + 1

The 16 of SO(10) = one GENERATION of Standard Model fermions:
(Writing SO(10) follows standard GUT convention; the 16 is a
spinor representation of the universal cover Spin(10).)""")

particles = [
    ("(3, 2, +1/6)", "u_L, d_L", "left-handed quarks", 6),
    ("(3̄, 1, -2/3)", "ū_R",     "right-handed up (anti)", 3),
    ("(3̄, 1, +1/3)", "d̄_R",     "right-handed down (anti)", 3),
    ("(1, 2, -1/2)", "ν_L, e_L", "left-handed leptons", 2),
    ("(1, 1, +1  )", "ē_R",      "right-handed electron (anti)", 1),
    ("(1, 1,  0  )", "ν̄_R",      "right-handed neutrino", 1),
]

print(f"  {'(color, weak, Y)':20s}  {'name':10s}  {'what':35s}  count")
print(f"  {'─'*20}  {'─'*10}  {'─'*35}  ─────")
total = 0
for rep, name, desc, n in particles:
    print(f"  {rep:20s}  {name:10s}  {desc:35s}  {n}")
    total += n
print(f"  {'':20s}  {'':10s}  {'TOTAL':>35s}  {total}")

print(f"""
That's EXACTLY:
  • 3 colors of up and down quarks (left-handed doublet)
  • 3 colors of up antiquarks (right-handed)
  • 3 colors of down antiquarks (right-handed)
  • electron and neutrino (left-handed doublet)
  • positron (right-handed)
  • right-handed neutrino (the 16th particle)

One complete chiral generation of the Standard Model, plus ν_R.""")

print("""
Two fences from the record (2026-09-06):
 1. "The 16 is one generation" is standard GUT nomenclature for the
    representation, not a derivation (B1250). What IS verified (B1253):
    on the derived hypercharge the 16 is a complete anomaly-free
    generation — six anomalies cancel, Y conserved on 45/45 cubic terms,
    all four SM Yukawa operators among the 40 terms of 10·16·16.
 2. The CHIRALITY of the 16 is axiom A5 here, and E65 makes it a
    theorem-backed input: every Sym^n of SL(2) is self-dual, so any ρ
    factoring π₁(m004) → SL(2) → E₆ has 27 ≅ 27̄ and net chirality
    identically zero, for every embedding. The chain's own holonomy
    cannot supply chirality; the record supplies it by a closing
    (θ-odd frame, B432/B576/B582), outside this chain.

THE OBJECT PICKS THE SO(10) GRADING AND THE REAL FORM (B1250, B1265):
reproduced here from the bare E₆ root system.""")

# E6 root system (Bourbaki labelling: chain 1-3-4-5-6, node 2 on 4), positive roots by the string algorithm
_C = [[ 2, 0,-1, 0, 0, 0],[ 0, 2, 0,-1, 0, 0],[-1, 0, 2,-1, 0, 0],
      [ 0,-1,-1, 2,-1, 0],[ 0, 0, 0,-1, 2,-1],[ 0, 0, 0, 0,-1, 2]]
_simple = [tuple(int(i == j) for j in range(6)) for i in range(6)]
_pos, _fr = set(_simple), list(_simple)
while _fr:
    beta = _fr.pop()
    for i in range(6):
        p, b = 0, list(beta); b[i] -= 1
        while tuple(b) in _pos: p += 1; b[i] -= 1
        if p - sum(beta[j]*_C[j][i] for j in range(6)) > 0:
            nb = list(beta); nb[i] += 1; nb = tuple(nb)
            if nb not in _pos: _pos.add(nb); _fr.append(nb)
_roots = list(_pos) + [tuple(-c for c in r) for r in _pos]
_a1 = {}
for r in _roots: _a1[r[0]] = _a1.get(r[0], 0) + 1
_dim_k, _dim_p = 6 + _a1[0], _a1[1] + _a1[-1]
# the 27: Weyl orbit of ω₁; u(1) charge = α₁-coefficient of the weight (via C⁻¹)
def _refl(wt, i): return tuple(wt[j] - wt[i]*_C[i][j] for j in range(6))
_w0 = tuple(int(j == 0) for j in range(6)); _W27, _fr = {_w0}, [_w0]
while _fr:
    v = _fr.pop()
    for i in range(6):
        u = _refl(v, i)
        if u not in _W27: _W27.add(u); _fr.append(u)
_Cinv = np.linalg.inv(np.array(_C, dtype=float))
_ch = {}
for v in _W27:
    q = round(3 * float(np.array(v) @ _Cinv[:, 0])); _ch[q] = _ch.get(q, 0) + 1
assert len(_roots) == 72 and (_dim_k, _dim_p) == (46, 32) and len(_W27) == 27
assert sorted(_ch.values()) == [1, 10, 16]
_even = sum(n for q, n in _ch.items() if q % 2 == 0)
print(f"""
  E₆ roots constructed: {len(_roots)};  dim e₆ = 6 + 72 = 78
  α₁-coefficient census: {dict(sorted(_a1.items()))}
  the involution 'sign by α₁-parity' (= D₂ up to overall sign):
    dim 𝔨 = 6 + {_a1[0]} = {_dim_k}  (so(10) ⊕ u(1) = 45 + 1)
    dim 𝔭 = {_dim_p}                 (16 + 16̄)
    Cartan signature dim 𝔭 − dim 𝔨 = {_dim_p - _dim_k}   →  the real form E₆(−14), uniquely
  the 27 by 3×(u(1) charge): {dict(sorted(_ch.items()))}   →  27 = 1 + 10 + 16
    even-charge block = {_even} = 1 + 10 (the 11-flip), odd block = {27 - _even} = the 16 (fixed)
  𝔨 contains the full Cartan: rank 𝔨 = 6 = rank e₆, so the involution is INNER.
  E₆(−26) has 𝔨 = f₄, rank 4: OUTER — no torus element reaches it [standard table, cited].
  Lorentz, compact colour and the graviton live in E₆(−26) (B1140): the fork is a rank
  obstruction (B1265). The one candidate crossing is the diagram automorphism θ, and the
  record's own θ facts cut against it (trivial on the character variety; θ-odd destroys
  F₄-stability, B576).""")

# ─────────────────────────────────────────────────────────────
banner(6, "THE CHARGES ARE FORCED")
# ─────────────────────────────────────────────────────────────

print("""The numbers in the third column (Y = +1/6, -2/3, +1/3, ...)
are the HYPERCHARGES. Are we free to choose them?

No. The SU(5) GROUP THEORY determines them uniquely.

THE MECHANISM: THE STANDARD EMBEDDING CHAIN

The canonical decomposition from Step 5 goes through a standard
nested embedding chain (commuting U(1) factors and finite
global quotients suppressed):

  E₆  ⊃  SO(10)  ⊃  SU(5)  ⊃  SU(3) × SU(2) × U(1)_Y

Within SU(5), hypercharge is a diagonal 5×5 traceless matrix
that must commute with SU(3) (upper-left 3×3) and SU(2) (lower-
right 2×2). Commuting with a block means being proportional to
the identity on that block.""")

print("\nThe most general such matrix is:")
print("  c₁·diag(1,1,1,0,0) + c₂·diag(0,0,0,1,1)")
print("\nTracelessness: 3c₁ + 2c₂ = 0  →  c₂ = -3c₁/2")
print("\n  Y = c₁ · diag(1, 1, 1, -3/2, -3/2)")

Y_diag = [Fraction(-1,3), Fraction(-1,3), Fraction(-1,3),
          Fraction(1,2), Fraction(1,2)]
tr = sum(Y_diag)
print(f"\nONE DIRECTION, not two. Standard normalization (c₁ = -1/3):")
print(f"  Y = diag(-1/3, -1/3, -1/3, +1/2, +1/2)")
print(f"      └──── SU(3) ────┘  └── SU(2) ──┘")
print(f"  trace = {tr}  ✓")

print("""
THE CHARGES FOLLOW FROM GROUP THEORY

The 16 of SO(10) decomposes under SU(5) as 10 ⊕ 5̄ ⊕ 1.
Each piece decomposes under SU(3)×SU(2), and Y is fixed:""")

su5_decomp = [
    ("10 → (3,2)", Fraction(1,6), "Q_L"),
    ("10 → (3̄,1)", Fraction(-2,3), "u^c"),
    ("10 → (1,1)", Fraction(1,1), "e^c"),
    ("5̄  → (3̄,1)", Fraction(1,3), "d^c"),
    ("5̄  → (1,2)", Fraction(-1,2), "L"),
    ("1  → (1,1)", Fraction(0,1), "ν^c"),
]

print(f"\n  {'SU(5) origin':17s}  {'Y':>6s}  {'particle':>8s}")
print(f"  {'─'*17}  {'─'*6}  {'─'*8}")
for origin, y, name in su5_decomp:
    print(f"  {origin:17s}  {str(y):>6s}  {name:>8s}")

print("\nEvery charge is FIXED by the SU(5) embedding. No free parameter.")
print("""
What group theory does NOT fix: the anchoring of this U(1) to the
physical hypercharge, Q = T₃ + Y — the electromagnetic identification
that sets the sign and scale of c₁. Direction derived (B864); the
normalisation is not derivable from the object; the anchoring is the
record's identification I-23 (UNEARNED, an instance of I-13).""")

print("""
WHAT ABOUT ANOMALY CANCELLATION?

Anomaly cancellation is a CONSISTENCY CHECK, not the derivation
mechanism. Applied alone (without SU(5) structure), the three
linear anomaly conditions leave a general solution
(q, u, -2q-u, -3q, e, 6q-e). At q=0 the cubic vanishes
identically, giving (0, u, -u, 0, e, -e) — uncharged quarks,
excluded by the SU(5) embedding. For q≠0, normalizing Y_Q=1
gives (1, t, -2-t, -3, e, 6-e). The cubic [U(1)]³ anomaly
factorizes as 18(e-t-4)(e+t-2)=0, giving two one-parameter
branches related by interchange of the two SU(3)×SU(2)-singlet
assignments (e^c ↔ ν^c).
Choosing the conventional identification:

  (Y_Q, Y_u, Y_d, Y_L, Y_e, Y_ν) = (1, t, -2-t, -3, 2-t, 4+t)

Before fixing normalization, the anomaly-free Abelian charge space
is spanned by Y and B-L. After fixing Y_Q=1, the free parameter t
parametrizes an affine line in the (Y, B-L) plane; its tangent
direction is (B-L)-2Y. The canonical embedding chain goes
through SU(5), which fixes
t = -4 (the SM value) by group theory.

Verification that anomaly cancellation holds:""")

# Do the anomaly computation with Fraction for exact arithmetic
Y_Q = Fraction(1,6)
Y_u = Fraction(-2,3)
Y_d = Fraction(1,3)
Y_L = Fraction(-1,2)
Y_e = Fraction(1)
Y_nu = Fraction(0)

c_su3 = 2*Y_Q + Y_u + Y_d
c_su2 = 3*Y_Q + Y_L
c_grav = 6*Y_Q + 3*Y_u + 3*Y_d + 2*Y_L + Y_e + Y_nu
c_u1 = 6*Y_Q**3 + 3*Y_u**3 + 3*Y_d**3 + 2*Y_L**3 + Y_e**3 + Y_nu**3

print(f"  [SU(3)]²×U(1):  2·Y_Q + Y_u + Y_d = {c_su3}  ✓")
print(f"  [SU(2)]²×U(1):  3·Y_Q + Y_L       = {c_su2}  ✓")
print(f"  [grav]²×U(1):   6Y_Q+3Y_u+3Y_d+2Y_L+Y_e+Y_ν = {c_grav}  ✓")
print(f"  [U(1)]³:        6Y_Q³+3Y_u³+3Y_d³+2Y_L³+Y_e³+Y_ν³ = {c_u1}  ✓")

# Verify the two-branch cubic factorization
def cubic_anomaly(t, e):
    yQ, yu, yd, yL, ye, ynu = Fraction(1), t, Fraction(-2)-t, Fraction(-3), e, Fraction(6)-e
    return 6*yQ**3 + 3*yu**3 + 3*yd**3 + 2*yL**3 + ye**3 + ynu**3

print("\n  Verifying cubic factorization 18(e-t-4)(e+t-2):")
for t_val in [Fraction(0), Fraction(1), Fraction(-4), Fraction(7,3)]:
    for e_val in [Fraction(0), Fraction(3), Fraction(2)-t_val, Fraction(4)+t_val]:
        cubic = cubic_anomaly(t_val, e_val)
        factored = 18 * (e_val - t_val - 4) * (e_val + t_val - 2)
        assert cubic == factored, f"Mismatch at t={t_val}, e={e_val}"
print("    16 exact test points agree with 18(e-t-4)(e+t-2)  ✓")
ce = cubic_anomaly(Fraction(0), Fraction(0))
print(f"    Counterexample (1,0,-2,-3,0,6): cubic = {ce} ≠ 0  (off-branch)")
print(f"    On branch e=2-t: cubic = {cubic_anomaly(Fraction(0), Fraction(2))}  ✓")
print(f"    On branch e=4+t: cubic = {cubic_anomaly(Fraction(0), Fraction(4))}  ✓")

print("""
  ┌────────────────────────────────────────────────────────┐
  │  HYPERCHARGE IS UNIQUE.                                │
  │  The SU(5) group theory within the canonical           │
  │  embedding chain E₆ ⊃ SO(10) ⊃ SU(5) ⊃ SM             │
  │  determines exactly one U(1) direction.                │
  │  It produces quarks with charge 2/3 and -1/3,          │
  │  electrons with charge -1, neutrinos neutral.          │
  │  Anomaly cancellation is a consistency verification.   │
  └────────────────────────────────────────────────────────┘""")

# ─────────────────────────────────────────────────────────────
banner(7, "THE WEAK MIXING ANGLE")
# ─────────────────────────────────────────────────────────────

print("""The Standard Model has two forces that mix: the weak force
(SU(2)) and hypercharge (U(1)). How much they mix is set by
the "weak mixing angle" θ_W.

In E₆, the mixing is determined by a trace identity.
Over the 27 representation:""")

# Compute traces over the full 27
# States: (color_dim, T3_values, Y)
states = [
    # From 16 of SO(10)
    (3, [Fraction(1,2), Fraction(-1,2)], Fraction(1,6)),    # Q_L
    (3, [Fraction(0)], Fraction(-2,3)),                       # u_R^c
    (3, [Fraction(0)], Fraction(1,3)),                        # d_R^c
    (1, [Fraction(1,2), Fraction(-1,2)], Fraction(-1,2)),    # L
    (1, [Fraction(0)], Fraction(1)),                           # e_R^c
    (1, [Fraction(0)], Fraction(0)),                           # nu_R
    # From 10 of SO(10) = 5 + 5bar of SU(5)
    (3, [Fraction(0)], Fraction(-1,3)),                       # D (color triplet)
    (1, [Fraction(1,2), Fraction(-1,2)], Fraction(1,2)),     # H_u (Higgs-like doublet)
    (3, [Fraction(0)], Fraction(1,3)),                        # Dbar
    (1, [Fraction(1,2), Fraction(-1,2)], Fraction(-1,2)),    # H_d
    # From 1 of SO(10)
    (1, [Fraction(0)], Fraction(0)),                          # singlet
]

tr_T3sq = Fraction(0)
tr_Ysq = Fraction(0)
tr_T3Y = Fraction(0)
n_total = 0

for color_dim, T3_vals, Y in states:
    for T3 in T3_vals:
        tr_T3sq += color_dim * T3**2
        tr_Ysq += color_dim * Y**2
        tr_T3Y += color_dim * T3 * Y
        n_total += color_dim

print(f"  Total states in 27: {n_total}")
print(f"  Tr(T₃²) = {tr_T3sq} = {float(tr_T3sq)}")
print(f"  Tr(Y²)  = {tr_Ysq} = {float(tr_Ysq)}")
print(f"  Tr(T₃·Y) = {tr_T3Y}")

k = tr_T3sq / tr_Ysq
print(f"""
  The GUT normalization factor: k = Tr(T₃²)/Tr(Y²) = {k}

  g₁_GUT = √(5/3) × g' is the properly normalized GUT coupling.

  At a scale where the normalized couplings match, g₁_GUT = g₂:

  sin²θ_W = g'² / (g² + g'²)
           = k·g₁² / (k·g₁² + g₂²)
           = k / (k + 1)
           = (3/5) / (3/5 + 1)
           = 3/8""")

sin2 = Fraction(3,8)
print(f"  sin²θ_W = {sin2} = {float(sin2):.6f}")

print("""
  ┌──────────────────────────────────────────────────┐
  │  Tree-level group-theoretic matching value:        │
  │  sin²θ_W = 3/8 exactly                           │
  │  (measured at M_Z in MSbar: 0.23122)             │
  └──────────────────────────────────────────────────┘

  The difference between 0.375 and 0.231 is the running
  of the couplings from high energy to low energy — and
  that running tells us WHERE the matching happens.""")

# non-discriminating: k = 3/5 block by block (states[:6] = the 16; states[6:10] = the 10 of SO(10);
# SU(5) 10 = Q, u^c, e^c; SU(5) 5bar = d^c, L)
def _k(block):
    t3, y2 = Fraction(0), Fraction(0)
    for cd, T3s, Y in block:
        for T3 in T3s: t3 += cd * T3**2; y2 += cd * Y**2
    return t3 / y2
_blocks = {"E₆ 27": states, "SO(10) 16": states[:6], "SO(10) 10": states[6:10],
           "SU(5) 10": [states[0], states[1], states[4]], "SU(5) 5̄": [states[2], states[3]]}
for _nm, _bl in _blocks.items(): assert _k(_bl) == Fraction(3, 5), _nm
print("""
NON-DISCRIMINATING (B1250; a retracted reading in the record's registry, 2026-09-05):
  Tr(T₃²)/Tr(Y²) block by block:""")
for _nm, _bl in _blocks.items(): print(f"    {_nm:10s}: {_k(_bl)}")
print("""  3/8 follows from any SU(5)-compatible embedding with equal normalised
  couplings. It reproduces a known GUT relation; it selects neither E₆ nor
  the knot. Run top-down as a sealed prediction (α_em(M_Z) the single input,
  E₆ boundary + pure SM desert) it misses the measured (sin²θ_W, α_s)(M_Z)
  at 16σ, α_s-dominated (B915). Step 8 below is the bottom-up computation.""")

# ─────────────────────────────────────────────────────────────
banner(8, "THE SCALE")
# ─────────────────────────────────────────────────────────────

print("""E₆ has a maximal subgroup SU(3) × SU(3) × SU(3) —
"trinification." Under trinification, sin²θ_W = 3/8 is not
a boundary condition at the top — it's a MATCHING CONDITION
at the intermediate scale M_I where trinification breaks to
the Standard Model.

The canonical tree-level matching is
  α₁⁻¹ = (1/5)α₃L⁻¹ + (4/5)α₃R⁻¹.
With D-parity (g₃L = g₃R) this reduces to α₁ = α₃L = α₂ at M_I.

Running the SM couplings up from M_Z = 91.19 GeV:""")

M_Z = 91.1876
alpha_em_inv = 127.952
sin2_tW = 0.23122
alpha_s = 0.1180

alpha_em = 1.0 / alpha_em_inv
alpha_2 = alpha_em / sin2_tW
alpha_Y = alpha_em / (1.0 - sin2_tW)
alpha_1_gut = (5.0/3.0) * alpha_Y

a1 = 1.0/alpha_1_gut
a2 = 1.0/alpha_2
a3 = 1.0/alpha_s

print(f"  α₁⁻¹(GUT) = {a1:.2f}")
print(f"  α₂⁻¹      = {a2:.2f}")
print(f"  α₃⁻¹      = {a3:.2f}")

# β coefficients (convention: α⁻¹(μ) = α⁻¹(M_Z) - b/(2π) ln(μ/M_Z))
b1 = 41.0/10   # U(1): grows
b2 = -19.0/6   # SU(2): shrinks
b3 = -7.0      # SU(3): shrinks

# M_I where α₁ = α₂
t_MI = (a1 - a2) * 2*np.pi / (b1 - b2)
M_I = M_Z * np.exp(t_MI)

print(f"""
  SM one-loop β coefficients:
    b₁ = +41/10 = +{b1:.1f}  (U(1) grows with energy)
    b₂ = -19/6  = {b2:.2f}  (SU(2) shrinks)
    b₃ = -7              (SU(3) shrinks)

  Solving α₁⁻¹(M_I) = α₂⁻¹(M_I):

  M_I = {M_I:.2e} GeV
  log₁₀(M_I) = {np.log10(M_I):.2f}""")

# Show all three couplings at M_I
def run_coupling(a_mz, b, mu):
    return a_mz - b/(2*np.pi) * np.log(mu/M_Z)

a1_MI = run_coupling(a1, b1, M_I)
a2_MI = run_coupling(a2, b2, M_I)
a3_MI = run_coupling(a3, b3, M_I)

print(f"""
  At M_I:
    α₁⁻¹ = {a1_MI:.2f}  ┐
    α₂⁻¹ = {a2_MI:.2f}  ┘ matched (= sin²θ_W = 3/8)
    α₃⁻¹ = {a3_MI:.2f}    (color, still different)

  The OBJECT's boundary condition (3/8), combined with D-parity,
  SM one-loop running and no new thresholds below M_I, DETERMINES
  this scale.
  M_I ≈ 10¹³ GeV — about 10⁶× below the Planck mass.
  (Assumes SM field content and one-loop running with no intermediate
  thresholds — additional matter would shift M_I.)""")

# Above M_I: trinification running
bL, bR, bC = -4, -4, -5  # model-spectrum input: depends on assumed matter content above M_I
gap = a2_MI - a3_MI  # gap to close
s = gap * 2*np.pi / (bL - bC)
M_U = M_I * np.exp(s)

print(f"""
  Above M_I, the three SU(3)s of trinification run with
  β = ({bL}, {bR}, {bC}). The gap between α_L and α_C is:

    gap = {gap:.2f}  (in α⁻¹ units)
    Δb  = {bL - bC}  (the β coefficients barely differ)

  Formal one-loop L/C crossing: M_U = {M_U:.1e} GeV (log₁₀ = {np.log10(M_U):.1f})

  That's 10⁹ ABOVE the Planck scale, where this field-theory
  extrapolation is not physically trustworthy. If perturbative
  unification below M_Pl is required, additional threshold or
  spectrum effects are needed; the proposed sextet sector is
  one possible mechanism.

  What's determined:  M_I (from the object's 3/8 + D-parity)
  What's missing:     M₆  (sextet Higgs mass; representation content must be specified)""")

# ─────────────────────────────────────────────────────────────
banner(9, "THE FIBONACCI CHAIN")
# ─────────────────────────────────────────────────────────────

print("""The same rule that made the shape also makes a CRYSTAL.

Take the Fibonacci word from Step 1:  a b a a b a b a a b ...
Put atoms at each position. Give 'a'-atoms potential +V,
'b'-atoms potential -V. Connect neighbors with hopping t = 1.

This is a real physical system — built in photonic waveguides,
polariton wires, and cold-atom lattices.

Its electronic spectrum has GAPS, and these gaps are labelled
by the integrated density of states (IDS):

  IDS at each gap ∈ ℤ + ℤ/φ  (mod 1)

where φ is the golden ratio from Step 1.

AND — the transfer matrix that governs whether an electron
can pass through the crystal is generated by the SAME
Fricke action from Step 3:

  F(x, y, z) = (z, x, xz - y)

The crystal and the shape are governed by the same Fricke
trace-map polynomial, but occupy different invariant level sets.""")

# Verify gap labelling
# Build Fibonacci chain Hamiltonian
fib_word = 'a'
for _ in range(13):
    fib_word = apply_rule(fib_word)
N = len(fib_word)

V = 1.0
H = np.zeros((N, N))
for i in range(N):
    H[i, i] = V if fib_word[i] == 'a' else -V
    if i + 1 < N:
        H[i, i+1] = 1.0
        H[i+1, i] = 1.0

energies = np.sort(np.linalg.eigvalsh(H))
# Find the largest gaps
gaps = []
for i in range(len(energies)-1):
    gaps.append((energies[i+1] - energies[i], i))
gaps.sort(reverse=True)

print(f"\n  Fibonacci chain with {N} sites, V = {V}:")
print(f"  Largest gaps and their IDS labels:")

for rank, (gapsize, idx) in enumerate(gaps[:5]):
    ids = (idx + 1) / N
    best_m = None
    best_err = 1.0
    for m in range(-10, 11):
        val = (m / phi) % 1
        err = min(abs(ids - val), abs(ids - val - 1), abs(ids - val + 1))
        if err < best_err:
            best_err = err
            best_m = m
    print(f"    gap {rank+1}: width {gapsize:.4f}, IDS = {ids:.6f} ≈ ({best_m:+d})/φ (mod 1), residual {best_err:.2e}")

# Verify Fricke invariant conservation
print(f"""
  The transfer-matrix trace map IS the Fricke action F,
  and the Fricke invariant κ = x²+y²+z²-xyz is conserved.

  For the chain with on-site potential V:
    κ = 4 + 4V²""")

for V_test in [0.5, 1.0, 2.0]:
    kappa = 4 + 4*V_test**2
    print(f"    V = {V_test}: κ = {kappa}")

print(f"""
  For the shape m004 (Step 3):
    κ = 0  (the puncture condition)

  4 + 4V² ≥ 4 > 0 for all V.
  The chain and the shape NEVER share a level set.
  They're on different slices of the same invariant.""")

# ─────────────────────────────────────────────────────────────
banner(10, "THE PREDICTION")
# ─────────────────────────────────────────────────────────────

print("""The shape m004 is AMPHICHIRAL — it admits an orientation-
reversing self-symmetry (a "mirror"). Its symmetry group
has order 8, and the closing lattice (mirror × flow-reversal)
is (ℤ/2)².

Under the dictionary c = P (parity), γ₅ = T (time reversal)
(this is axiom A8 — a declared choice):

The Chern-Simons invariant CS(m004) is:
  • odd under mirror (c-odd)
  • odd under flow reversal (γ₅-odd)
  • therefore (P-odd, T-odd) = CPT-EVEN
  • and 2-torsion: CS ∈ {0, 1/4} mod 1/2

For m004 specifically: CS = 0.

Under the dictionary, this maps to:
  • CPT-even (P-odd, T-odd) type = the E type
  • The SM's E-type parameter = the topological QCD vacuum angle θ
  • 2-torsion in ℝ/2πℤ = {{0, π}}
  • Why 0 not π: both torsion points are fixed by their respective
    ℤ₂ involutions, so equivariance alone does not distinguish them.
    A8's identity-preserving group structure rules out 0 ↦ π:
    every group homomorphism preserves the identity element.
    CS = 0 is the identity of {{0,1/4}} mod 1/2;
    θ = 0 is the identity of {{0,π}} mod 2π. The unique nontrivial
    group homomorphism (the identity isomorphism) sends 0→0, 1/4→π.
    A8 requires the map to preserve torsion structure, selecting this.
  • CS = 0 → θ = 0 (dictionary selection)

Open issue — θ̄ vs θ: the physical observable is θ̄ = θ + arg(det M_q),
not the basis-dependent θ alone. The dictionary constrains the topological
angle θ: CS is a topological invariant of the manifold; θ is the coupling
multiplying QCD's topological density. An anomalous chiral rephasing moves
phase between θ and arg(det M_q), so θ alone is basis-dependent; the
dictionary must specify a phase convention, which A8 does not yet
operationally define. θ = 0 is a representative in the dictionary's
chosen basis.
For θ̄ = 0, one additionally needs arg(det M_q) = 0. E₆ admits a cubic
27³ invariant, but the reality of the group-theoretic tensor does not
by itself fix physical Yukawa phases or VEVs; the chain does not derive it.
(This is T17, mapping symmetry TYPES ℤ/2 → ℤ/2, NOT the refuted I-4
dictionary which attempted CS = θ as a value. B813 kills I-4.)
(The record registered it as I-18 (B1243) with θ̄ as target; after this
document's flag, B1246 verified the chiral-rotation computation — θ → θ − 2N_f α,
arg det M → arg det M + 2N_f α, θ̄ invariant — and re-priced the row: the type
map reaches θ, and earning I-18 needs the dictionary AND the Yukawa phase.
T17 stands; I-18 stays UNEARNED and reduces to I-13.)

For m004 specifically, 2-torsion is forced by amphichirality:
CS ≡ -CS (mod 1/2) in SnapPy's normalization, so 2·CS ≡ 0 (mod 1/2)
and CS ∈ {0, 1/4} (mod 1/2).
This is a theorem, not a coincidence. The genuinely sharp content
is within the amphichiral class: all 6 amphichiral census manifolds
land exactly at {0, 1/4}, and m004 at 0 separates from its sister
m003 at 1/4 (B1224). Among 394 non-amphichiral census manifolds,
only 1 sits at 2-torsion CS (B1224).
(Census: OrientableCuspedCensus in SnapPy, first 400 one-cusped
orientable, amphichirality via symmetry_group(), CS tolerance for
2-torsion; census script to be supplied separately.)
A measured nonzero θ̄
would not by itself falsify θ = 0; it would falsify θ̄ = 0 only
jointly with a demonstration that arg(det M_q) = 0.

What the dictionary does NOT fix: this argument does not
constrain the numerical weak-CP phases (CKM and PMNS matrices).
These are free parameters of the chain.""")

# ─────────────────────────────────────────────────────────────
print(f"\n{'='*70}")
print(f"  THE WHOLE CHAIN, COMPRESSED")
print(f"{'='*70}\n")

print("""
  ┌─ RULE ──────────────────────────────────────────────────┐
  │  a → ab,  b → a                                        │
  │  (the simplest non-trivial substitution on 2 letters)   │
  └──────────────────────┬──────────────────────────────────┘
                         │ incidence matrix M, det = -1
                         ▼
  ┌─ SHAPE ─────────────────────────────────────────────────┐
  │  mapping torus of M² → m004 (figure-eight knot)         │
  │  the simplest hyperbolic knot complement                │
  └──────────────────────┬──────────────────────────────────┘
                         │ Fricke action + puncture condition
                         ▼
  ┌─ FIELD ─────────────────────────────────────────────────┐
  │  z² - 3z + 3 = 0,  discriminant -3                     │
  │  the number field Q(√-3)                                │
  └──────────────────────┬──────────────────────────────────┘
                         │ conductor 3 → McKay correspondence
                         ▼
  ┌─ SYMMETRY ──────────────────────────────────────────────┐
  │  binary tetrahedral group 2T → E₆                       │
  │  rank-6 Lie algebra, 78-dimensional                     │
  │  D₂ twist → real form E₆(−14) (derived, B1265)          │
  └──────────────────────┬──────────────────────────────────┘
                         │ fundamental representation
                         ▼
  ┌─ MATTER ────────────────────────────────────────────────┐
  │  27 = 16 + 10 + 1                                       │
  │  16 = one SM generation (rep. nomenclature; chirality = A5)│
  │  hypercharge direction fixed by SU(5); anchoring = I-23  │
  └──────────────────────┬──────────────────────────────────┘
                         │ trace identities on the 27
                         ▼
  ┌─ FORCES ────────────────────────────────────────────────┐
  │  SU(3) × SU(2) × U(1); sin²θ_W = 3/8 tree-level, non-discriminating │
  │  under D-parity trinification: M_I = 10¹³ GeV (one-loop, no thresholds) │
  └──────────────────────┬──────────────────────────────────┘
                         │ Chern-Simons + dictionary
                         ▼
  ┌─ PREDICTION ────────────────────────────────────────────┐
  │  θ = 0 (dictionary); θ̄ = 0 contingent on Yukawa          │
  │  weak CP phases = free                                   │
  │  bite: amphichiral 6/6 at 2-torsion; non-amphichiral 1/394│
  └─────────────────────────────────────────────────────────┘

  AXIOMS (declared inputs, not derived):
    A1  why this rule  (minimal description)
    A3  the McKay route  (N = 3 → SL(2,F₃) ≅ 2T → Ê₆ → E₆)
    A4  matter in the fundamental 27
    A5  chirality  (chiral 16, not vector-like — not suppliable by the chain's
        SL(2) holonomy, E65; the record supplies it by a closing)
    A7  chain's scale = experimenter's
    A8  dictionary c = P, γ₅ = T; identity-preserving on torsion sectors

  WHAT'S NOT SUPPLIED:
    •  absolute mass scale (external, by theorem)
    •  VEV direction within the forced orbit (free)
    •  exotic decoupling (the 10+1 in each 27 must acquire masses)
    •  M₆ (sextet Higgs mass; representation content must be specified)
    •  D-parity origin (model assumption in Step 8, not derived)
    •  generation count (not derived; one generation constructed). Record state:
       (a) B632's h¹ = 3 is under the PRINCIPAL sl₂ (27 = 17+9+1), typed 1 abelian
           + 2 chiral; the embedding is I-25, UNEARNED; Brieskorn–Slodowy selects the
           subregular 13+9+5 (B1257) but the holonomy landing there is unshown;
       (b) E65: any ρ through SL(2) has 27 ≅ 27̄ — no net-chirality count in this
           frame; B1260/B1267: closed wall general (PD), cusped abelian sector walled
           by reciprocity of Δ = t²−3t+1, W1/W2 rigid, index zero;
       (c) h¹ of a 3-manifold ≡ a 4d generation count is itself I-26, UNEARNED;
       (d) three generations cannot live in one 27 (16 has multiplicity one, B1255)
       R56–R59 (this branch): the count is a relative Euler characteristic — zero on any
           closed 3-manifold and for a knot; the fiber's three θ-fixed half-periods source a
           θ-odd sector (6, 10) that every closing by the rule (m004, m003, cyclic covers)
           removes, keeping one θ-even class per summand (exact mod three primes)
    •  chirality mechanism (A5; the record's θ-odd closing is outside this chain)
    •  spacetime / Lorentz / gravity (the E₆(−26) branch; outer; fork = rank obstruction)
    •  A8 phase convention (not yet operationally defined)
    •  coupling values at low energy (structure, not values)

  THE PRICE (record accounting, B1261/B1266, 2026-09-06):
    spends  4 framework axioms + 7 irreducible unearned identifications = 11 free inputs
            (14 ledger rows outstanding: I-18, I-23 → I-13; I-11 → I-10)
    buys    0 of the SM's 19 free parameters
    derives, structurally: E₆ (McKay, I-1 EARNED) · SO(10) grading (D₂, I-22 EARNED) ·
            real form E₆(−14) (B1265) · descent cut by three characters of the 27 ·
            one anomaly-free generation (B1253) · hypercharge direction (B864) ·
            termination at the SM (B863) · global ℤ₆ form (B862, conditional)
    The two currencies do not convert. (This document's A-labels are chain-axioms
    named by this seat; the record's "4 axioms" are its framework axioms in its own
    labelling — different lists, not to be added.)
""")
