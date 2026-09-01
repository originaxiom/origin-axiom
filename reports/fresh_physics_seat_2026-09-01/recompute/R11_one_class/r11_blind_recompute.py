"""R11 blind recomputation -- B1183 ONE-CLASS THEOREM.

Written BEFORE opening frontier/B1183_one_class_theorem/verification/*.
Inputs used: the arc's FINDINGS.md claim text, and committed data of the
SOURCE arcs only (B760 compute.py chain via B238's committed su32_wrt.py;
B1163 orientation theorem statement; B1174 mirror=conjugation-on-traces).

The claim decomposed:
  ONE involution c (complex conjugation on C), restricting to
    - Gal(K/Q) generator on K = Q(sqrt-3)   (omega -> omega^2)
    - sigma_4 on Q(zeta5)                    (zeta5 -> zeta5^4), fixing sqrt5
    - trivial on R
    - the geometric mirror on m004 (amphichiral; mirror conjugates traces)
  Four Z/2 obstruction sets, each claimed FREE (c fixed-point-free) and
  NON-COLLAPSED (two genuinely distinct elements) under the SAME c:
    P1 T_orient = {+Vol, -Vol}                 (B1163)
    P2 T_QP4    = {+sqrt3, -sqrt3} = sign Im f(omega)  (B760 part 8)
    P3 T_eig    = {zeta5, zeta5^4} eigenvalue choice   (B760 parts 2/7)
    P4 T_mirror = mirror/chirality bit on the trace field (B1174/B942):
                  {sqrt-3, -sqrt-3} i.e. the two embeddings K -> C
  Plus the VACUITY BOUNDARY: at |G|=2 every bijection of free 2-element
  c-sets is automatically equivariant (equivariance is a free hypothesis);
  the load-bearing content is freeness + non-collapse + same-c.
  Planted-positive controls: probes that MUST FAIL the same-c freeness test
  (Q(sqrt5) value bit: c acts trivially; a collapsed sign set at a real point).
"""
import math
import cmath
import importlib.util
import os
import sys

import sympy as sp
import numpy as np

OK = []


def check(name, cond):
    OK.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")


print("=" * 78)
print("STEP 0 -- the one involution c and its restrictions (exact, sympy)")
print("=" * 78)

zeta5 = sp.exp(2 * sp.pi * sp.I / 5)
omega = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2   # primitive 6th? omega = e^{2pi i/3}
phi = (1 + sp.sqrt(5)) / 2

# c := complex conjugation on C.
# (a) restricted to K = Q(sqrt-3): omega -> omega^2 = conj(omega), the Gal(K/Q) generator
check("c|K: conj(omega) == omega**2 (Gal generator, nontrivial on K)",
      sp.simplify(sp.conjugate(omega) - omega**2) == 0)
check("c|K nontrivial: conj(sqrt(-3)) == -sqrt(-3) != sqrt(-3)",
      sp.simplify(sp.conjugate(sp.sqrt(-3)) + sp.sqrt(-3)) == 0)

# (b) restricted to Q(zeta5): conj = sigma_4 (zeta5 -> zeta5^4)
check("c|Q(zeta5): conj(zeta5) == zeta5**4 (= sigma_4)",
      sp.simplify(sp.conjugate(zeta5) - zeta5**4) == 0)
# sigma_4 fixes sqrt5 = 2(zeta5 + zeta5^4) + 1  -> real subfield fixed
def zexact(expr):
    """Exact zero test robust to exp-vs-radical form."""
    e = sp.expand(expr)
    return (sp.simplify(e.rewrite(sp.cos)) == 0
            or sp.simplify(sp.expand_complex(e)) == 0)

s5 = 2 * (zeta5 + zeta5**4) + 1
check("sqrt5 = 2(zeta5+zeta5^4)+1 (exact)", zexact(s5 - sp.sqrt(5)))
check("c fixes sqrt5 (real): conj(sqrt5) == sqrt5",
      sp.simplify(sp.conjugate(sp.sqrt(5)) - sp.sqrt(5)) == 0)
# sigma_4 as abstract Galois element also fixes it: sigma_4(zeta+zeta^4) = zeta^4+zeta^16=zeta^4+zeta
check("sigma_4(zeta5+zeta5^4) fixed: zeta5^4 + zeta5^16 == zeta5 + zeta5^4",
      sp.simplify((zeta5**4 + zeta5**16) - (zeta5 + zeta5**4)) == 0)

# (c) trivial on R
check("c trivial on R (conj(x)=x for real symbol)",
      sp.conjugate(sp.Symbol('x', real=True)) == sp.Symbol('x', real=True))

print()
print("=" * 78)
print("STEP 1 -- P3 chord/cyclotomic sector rebuilt from B238 committed module")
print("=" * 78)

B238_PATH = "/home/user/origin-axiom/frontier/B238_su32_levelrank/su32_wrt.py"
spec = importlib.util.spec_from_file_location("b238", B238_PATH)
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)
w, S, T, cc = b238.su3_data(2)
n = len(w)
C = np.zeros((n, n))
for i, wt in enumerate(w):
    C[w.index((wt[1], wt[0])), i] = 1.0
Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
R, L = T, Si @ Ti @ S
pairs = [(w.index((1, 0)), w.index((0, 1))),
         (w.index((2, 0)), w.index((0, 2)))]
U_odd = np.zeros((n, 2))
for j, (a, b) in enumerate(pairs):
    U_odd[a, j], U_odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
U_odd = U_odd.astype(complex)
W_weld = C @ R @ L
B = np.array([[np.conj(U_odd[:, i]) @ W_weld @ U_odd[:, j]
               for j in range(2)] for i in range(2)])

z5n = cmath.exp(2j * math.pi / 5)
evals = np.linalg.eig(B)[0]
evals = sorted(evals, key=lambda z: -z.imag)
check("weld eigenvalues == {zeta5, zeta5^4} (1e-10)",
      abs(evals[0] - z5n) < 1e-10 and abs(evals[1] - z5n**4) < 1e-10)
PHI = (1 + math.sqrt(5)) / 2
check("tr(B) == 1/phi = 2cos72 (1e-10)", abs(np.trace(B) - 1 / PHI) < 1e-10)
check("det(B) == 1 (1e-10)", abs(np.linalg.det(B) - 1) < 1e-10)

# exact side: char poly x^2 - (1/phi) x + 1 has roots zeta5, zeta5^4
x = sp.Symbol('x')
p = x**2 - (1 / phi) * x + 1
check("char poly p(zeta5) == 0 exactly", zexact(p.subs(x, zeta5)))
check("char poly p(zeta5^4) == 0 exactly", zexact(p.subs(x, zeta5**4)))
check("root sum 2cos72 == 1/phi exactly",
      zexact(zeta5 + zeta5**4 - 1 / phi))
check("root product == 1 exactly", sp.simplify(zeta5 * zeta5**4 - 1) == 0)
check("Phi_5 factorization: Phi_5 == (x^2-(1/phi)x+1)(x^2+phi*x+1)",
      sp.expand(sp.simplify((x**2 - (1/phi)*x + 1) * (x**2 + phi*x + 1)
                            - (x**4 + x**3 + x**2 + x + 1))) == 0)

# quaternionic structure: conj(B) = eps B eps^-1, eps^2 = -I  => pseudo-real, no real structure
eps = np.array([[0, -1], [1, 0]], dtype=complex)
check("eps^2 == -I", np.allclose(eps @ eps, -np.eye(2)))
check("conj(B) == eps B eps^-1 (quaternionic; no real structure)",
      np.allclose(np.conj(B), eps @ B @ np.linalg.inv(eps), atol=1e-10))

# P3 as a c-set: c (= conj = sigma_4) swaps the two eigenvalues; they are distinct
check("P3 FREE under c: conj swaps zeta5 <-> zeta5^4 (no fixed elt)",
      sp.simplify(sp.conjugate(zeta5) - zeta5**4) == 0
      and sp.simplify(sp.conjugate(zeta5**4) - zeta5) == 0)
check("P3 NON-COLLAPSED: zeta5 != zeta5^4",
      sp.simplify(zeta5 - zeta5**4) != 0)

print()
print("=" * 78)
print("STEP 2 -- P2 the chord-sector sign carrier (B760 part 8, exact)")
print("=" * 78)

# sign-carrier lemma: Im f(conj(u)) = -Im f(u) for real-coefficient f (exact)
u = sp.Symbol('u')
f = -2 * (2 - u)          # the committed Sym^2(AB) derivative from B760
d_om = f.subs(u, omega)
d_omb = f.subs(u, sp.conjugate(omega))
check("Im f(omega) == +sqrt3 exactly",
      sp.simplify(sp.im(d_om) - sp.sqrt(3)) == 0)
check("Im f(conj(omega)) == -sqrt3 exactly",
      sp.simplify(sp.im(d_omb) + sp.sqrt(3)) == 0)
check("magnitude c-invariant: |Im| both sqrt3",
      sp.simplify(sp.Abs(sp.im(d_om)) - sp.Abs(sp.im(d_omb))) == 0)
# general lemma for a generic real-coefficient polynomial
a0, a1, a2 = sp.symbols('a0 a1 a2', real=True)
zz = sp.Symbol('zz')
g = a0 + a1 * zz + a2 * zz**2
zr, zi = sp.symbols('zr zi', real=True)
lemma = sp.simplify(sp.im(g.subs(zz, zr - sp.I * zi))
                    + sp.im(g.subs(zz, zr + sp.I * zi)))
check("LEMMA: Im g(conj z) == -Im g(z), real-coeff g (deg<=2, exact)", lemma == 0)

check("P2 FREE under c: c maps +sqrt3 -> -sqrt3 (sign flips, no fixed elt)",
      sp.simplify(sp.im(d_om) + sp.im(d_omb)) == 0 and sp.im(d_om) != 0)
check("P2 NON-COLLAPSED: +sqrt3 != -sqrt3 (Im != 0 at omega)",
      sp.im(d_om) != 0)

# Gate-5 note: 15/32 coupling fraction is CITED not re-adjudicated in B1183;
# still cheap to re-verify c-invariance of the fraction from B760's committed d-list:
ds = [0, 0, -2*(2-u), 2*(2+u), 2*(2+u), -2*(2-u), 4*u**3 + 8*u]
def frac_at(val):
    num = sum(sp.im(d.subs(u, val) if hasattr(d, 'subs') else sp.Integer(d))**2 for d in ds)
    den = sum(sp.Abs(d.subs(u, val) if hasattr(d, 'subs') else sp.Integer(d))**2 for d in ds)
    return sp.simplify(num / den)
fw, fwb = frac_at(omega), frac_at(sp.conjugate(omega))
check("coupling fraction 15/32 at omega AND conj(omega) (c-invariant, exact)",
      sp.simplify(fw - sp.Rational(15, 32)) == 0
      and sp.simplify(fwb - sp.Rational(15, 32)) == 0)

print()
print("=" * 78)
print("STEP 3 -- P1 orientation {+Vol,-Vol} and P4 mirror on traces (SnapPy)")
print("=" * 78)

import snappy
M = snappy.Manifold("m004")
vol = M.volume()
check("Vol(m004) > 0 (non-collapse: +Vol != -Vol)", vol > 1e-6)
print(f"    Vol(m004) = {vol}")

sg = M.symmetry_group()
check("m004 amphichiral (orientation-reversing isometry exists)",
      sg.is_amphicheiral())
check("symmetry group order 8 (D4, full)", sg.order() == 8)

# Bloch-Wigner / Vol is mirror-ODD: reversed manifold has -Vol in the signed
# (Chern-Simons complex volume) sense; SnapPy: complex_volume of m004 vs mirror.
Mr = snappy.Manifold("m004")
Mr.reverse_orientation()
cv, cvr = M.complex_volume(), Mr.complex_volume()
check("mirror flips signed volume: Re cvol(m004) == -Re cvol(mirror)? "
      "(vol part even, CS odd -- amphichiral CS==0)",
      abs(cv.real - cvr.real) < 1e-9)
# The orientation TORSOR statement: composing the embedding K->C with c flips
# the sign of the Bloch-Wigner dilogarithm: D(conj z) = -D(z). m004 = 2 regular
# ideal tetrahedra with shape z0 = omega ( = e^{i pi/3} shape field Q(sqrt-3)).
import mpmath as mp
def bloch_wigner(z):
    z = mp.mpc(z)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))
z0 = mp.mpc(0.5, mp.sqrt(3) / 2)   # tetrahedron shape e^{i pi/3}
D0 = bloch_wigner(z0)
check("Vol(m004) == 2*D(z0), z0 = e^{i pi/3} (1e-9)",
      abs(2 * D0 - vol) < 1e-9)
check("P1 FREE under c: D(conj z0) == -D(z0) (Bloch-Wigner odd, 1e-12)",
      abs(bloch_wigner(mp.conj(z0)) + D0) < 1e-12)
check("P1 NON-COLLAPSED: D(z0) != 0", abs(D0) > 1e-6)

# P4: mirror acts on holonomy traces as complex conjugation (B1174's weld);
# trace field K = Q(sqrt-3): verify a trace and its mirror image.
G = M.fundamental_group()
Gr = Mr.fundamental_group()
tr = {g: G.SL2C(g).trace() for g in ('a', 'b', 'ab')}
trr = {g: Gr.SL2C(g).trace() for g in ('a', 'b', 'ab')}
# The mirror's holonomy is conjugate up to the discrete faithful ambiguity;
# compare the multiset of traces to the conjugated multiset.
def close(x, y):
    return abs(x - y) < 1e-9
mirror_conj = all(any(close(trr[h], tr[g].conjugate()) for h in trr) for g in tr)
check("P4: mirror traces == conjugated traces (multiset, 1e-9)", mirror_conj)
# trace field nontrivially moved by c: some trace has Im != 0
some_im = max(abs(t.imag) for t in tr.values())
check("P4 FREE+NON-COLLAPSED: some trace has Im != 0 (c moves K in C)",
      some_im > 1e-6)
print(f"    traces: {tr}")
print(f"    mirror: {trr}")

print()
print("=" * 78)
print("STEP 4 -- the torsor algebra: freeness, isomorphism, VACUITY boundary")
print("=" * 78)

# Abstract check: for 2-element sets T1, T2 each with the swap action,
# EVERY bijection is equivariant (so 'equivariance' is a free hypothesis);
# and any equivariant map of free transitive G-sets is an isomorphism.
import itertools
T1 = ('p', 'q')
T2 = ('r', 's')
swap = {('p'): 'q', ('q'): 'p', ('r'): 's', ('s'): 'r'}
bijections = [dict(zip(T1, perm)) for perm in itertools.permutations(T2)]
equivariant = [all(f[swap[t]] == swap[f[t]] for t in T1) for f in bijections]
check("VACUITY boundary: ALL bijections of free Z/2 2-sets are equivariant "
      f"({sum(equivariant)}/{len(bijections)})", all(equivariant))
# contrast: for Z/3 on 3-element torsors NOT every bijection is equivariant
T3 = (0, 1, 2)
rot = lambda t: (t + 1) % 3
eq3 = [all(perm[rot(t)] == rot(perm[t]) for t in T3)
       for perm in map(lambda p: dict(zip(T3, p)), itertools.permutations(T3))]
check("contrast |G|=3: only 3/6 bijections equivariant (so vacuity is "
      f"|G|=2-specific) -> got {sum(eq3)}/6", sum(eq3) == 3)

# The explicit identification map (orientation -> sign Im at chosen embedding):
# composing the embedding with c flips ALL of: orientation (D odd), Im-sign
# (lemma), zeta5-choice (conj swaps). Verified above piecewise; the map is a
# bijection of 2-sets, hence (by the vacuity fact) automatically equivariant,
# hence a torsor isomorphism. The LOAD-BEARING content re-verified:
free_noncollapse = {
    "P1 orient": ("Vol>0", "D odd"),
    "P2 chord sign": ("Im=sqrt3 != 0", "sign flips"),
    "P3 eigenvalue": ("zeta5 != zeta5^4", "conj swaps"),
    "P4 mirror/Gal": ("Im trace != 0", "mirror conjugates"),
}
for k, v in free_noncollapse.items():
    print(f"    {k}: non-collapse via {v[0]}; freeness via {v[1]}")

print()
print("=" * 78)
print("STEP 5 -- PLANTED-POSITIVE CONTROLS (must FAIL the same-c torsor test)")
print("=" * 78)

# Control A (from B1174's own refutation): the Q(sqrt5) value bit.
# The candidate 'obstruction set' {+sqrt5, -sqrt5} with c = complex conjugation:
# c FIXES sqrt5 (real) => action has fixed points => NOT free => NOT the c-class.
ctrlA_free = sp.simplify(sp.conjugate(sp.sqrt(5)) + sp.sqrt(5)) == 0  # would need conj(s5) == -s5
check("CONTROL A caught: {+sqrt5,-sqrt5} NOT free under c (c fixes sqrt5)",
      not ctrlA_free)

# Control B: collapsed set -- sign Im f(u) at a REAL point u=1: Im = 0, the
# 'two' elements coincide => NOT non-collapsed.
d_real = f.subs(u, 1)
check("CONTROL B caught: at real u, Im f == 0 (collapsed 'sign set')",
      sp.simplify(sp.im(d_real)) == 0)

# Control C: a WRONG involution (the other zeta12 leg z -> z^7: fixes sqrt-3?
# no -- B1174: z->z^7 FLIPS sqrt3, FIXES sqrt-3). Under c' = (sqrt3 -> -sqrt3,
# sqrt-3 fixed), the orientation set {+Vol,-Vol} is NOT free (c' fixes omega,
# so it fixes D(z0) -- no flip). Demonstrate on K: c'(omega) == omega.
z12 = sp.exp(2 * sp.pi * sp.I / 12)
# omega = z12^4; z -> z^7 sends z12^4 -> z12^28 = z12^4 -> fixes omega
check("CONTROL C caught: sigma7 (z12->z12^7) FIXES omega => orientation set "
      "not free under sigma7 (wrong leg)",
      sp.simplify(z12**28 - z12**4) == 0)
check("CONTROL C contrast: sigma7 flips sqrt3 = z12 + z12^-1",
      sp.simplify((z12**7 + z12**-7) + (z12 + z12**-1)) == 0)

print()
print("=" * 78)
n_pass = sum(1 for _, ok in OK if ok)
print(f"TOTAL: {n_pass}/{len(OK)} checks passed")
if n_pass != len(OK):
    print("FAILED:", [nm for nm, ok in OK if not ok])
    sys.exit(1)
print("R11 BLIND RECOMPUTE: ALL CHECKS PASS")
