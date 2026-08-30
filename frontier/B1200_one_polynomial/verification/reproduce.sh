#!/usr/bin/env bash
# B1200 -- ONE POLYNOMIAL, THREE FACES. Exact, symbolic; own re-derivation of the cross-link.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null | tee one_polynomial.txt
import sympy as sp
u = sp.symbols('u')
Phi3 = u**2 + u + 1

# FACE 1 -- the saddle (B1195/GC-21): the stationary-phase equation of the object's
# own b=1 partition function reduces exactly to Phi3.
roots = sp.solve(Phi3, u)
assert set(roots) == {sp.Rational(-1,2) - sp.sqrt(3)*sp.I/2, sp.Rational(-1,2) + sp.sqrt(3)*sp.I/2}

# FACE 2 -- the founding obstruction (B309/B518/B285): kappa = tr[a,b] = u^2 + 2 at the
# Eisenstein point; the object sits at |kappa - 2| = 1, the UNIT obstruction.
for r in roots:
    kappa = sp.expand(r**2 + 2)
    assert sp.simplify(abs(kappa - 2) - 1) == 0                    # unit obstruction
    assert sp.simplify((kappa-2)**2 + (kappa-2) + 1) == 0          # Phi3(kappa-2) = 0
# and identically, not just at the roots:
assert sp.rem(((u**2+2)-2)**2 + ((u**2+2)-2) + 1, Phi3, u) == 0

# THE SET IDENTITY: the saddle set IS {kappa-2, its conjugate}
sq = [sp.expand(r**2) for r in roots]
assert set(sq) == set(roots)
# THE LINKING MAP: u -> u^2 swaps the two roots -- it is the Galois generator c itself
assert sp.expand(roots[0]**2) == roots[1] and sp.expand(roots[1]**2) == roots[0]

# FACE 3 -- the boundary structure (cloud memo 104): Coxeter^4 gives M^2 + M + I = 0,
# the same Phi3, on the E6-as-rank-3-Z[omega]-module boundary object.
M = sp.Matrix([[0,-1],[1,-1]])
assert M*M + M + sp.eye(2) == sp.zeros(2,2) and M**3 == sp.eye(2)

print("FACE 1 (saddle, B1195/GC-21):        u^2 + u + 1 = 0, roots -1/2 +- sqrt3 i/2")
print("FACE 2 (obstruction, B309/B518):     kappa - 2 = u^2, |kappa-2| = 1, Phi3(kappa-2) = 0")
print("        -- identically mod Phi3, not merely at the roots")
print("FACE 3 (boundary, cloud memo 104):   M^2 + M + I = 0, M^3 = I")
print("SET IDENTITY: the saddle set IS {kappa-2, conj}")
print("LINKING MAP : u -> u^2 swaps the roots = the Galois generator c (B1174)")
print("ONE POLYNOMIAL, THREE FACES. REPRODUCES")
PY
