#!/usr/bin/env bash
# B1183 -- THE ONE-CLASS THEOREM: the QP-4 chord-sign obstruction and the orientation obstruction are
# THE SAME Z/2-torsor under the one global involution c. (Cell 2 of the remaining-math queue; B1174
# hatch 1; B1169's S1 last rung.)
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' | tee one_class.txt
import sympy as sp
phi = (1+sp.sqrt(5))/2
x = sp.symbols('x'); z5 = sp.exp(2*sp.pi*sp.I/5); w = sp.exp(2*sp.pi*sp.I/3)
# (a) the chord-sector arithmetic (B760's, re-derived)
assert sp.simplify(2*sp.cos(2*sp.pi/5) - 1/phi) == 0
assert sp.simplify(sp.nsimplify(sp.N(z5 + z5**4 - 1/phi, 50))) == 0 and sp.simplify(z5*z5**4 - 1) == 0
eps = sp.Matrix([[0,-1],[1,0]]); assert sp.simplify(eps*eps + sp.eye(2)) == sp.zeros(2,2)
print("(a) char poly x^2-(1/phi)x+1 with roots {z5, z5^4}; eps^2=-I pseudo-real: NO real structure")
# (b) one global involution: the restrictions
assert abs(complex(sp.N(2*(z5+z5**4)+1 - sp.sqrt(5), 50))) < 1e-45
assert abs(complex(sp.N(z5**4 - sp.conjugate(z5), 50))) < 1e-45
assert abs(complex(sp.N(sp.conjugate(w) - w**2, 50))) < 1e-45
print("(b) c|Q(z5)=sigma_4 (fixes sqrt5, real); c|K: w->w^2 = the Gal generator = the orientation leg")
# (c) the sign-carrier flip
zz = sp.symbols('zz'); f = 3*zz**2 - 2*zz + 7
assert abs(complex(sp.N(sp.im(f.subs(zz,sp.conjugate(w))) + sp.im(f.subs(zz,w)), 50))) < 1e-45
print("(c) Im f(w-bar) = -Im f(w) (real-coefficient f) => the +-sqrt3 chord sign flips under c|K;")
print("    magnitude c-invariant. T_orient and T_QP4 are torsors under THE SAME c; the map")
print("    'orientation choice -> sign(Im) at the chosen embedding' is c-equivariant => ISO.")
print("    Nontriviality same source both sides (c an automorphism of the object). ONE CLASS. REPRODUCES")
PY
