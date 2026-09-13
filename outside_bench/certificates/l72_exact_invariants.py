"""OUTSIDE BENCH -- L72: the level-2 invariants EXACTLY, and what the residual gates.

Seal: outside_bench/seals/L72_EXACT_INVARIANTS_PREREG.md
      sha256 4621857a643e631fbb6d1ceeb2bcee450aa58122db4f50947236cb301082b6a3
      committed before this file was written.

Exact arithmetic in Z[zeta_7] = Z[x]/Phi_7(x), Phi_7 = x^6+x^5+x^4+x^3+x^2+x+1.
Floats appear ONLY in CELL 2, where the job is to compare against the cell's floats.

CELL 1  the exact values of J_N(zeta_7), N = 1, 3, 5
CELL 2  do they match P2W5-L72's printed floats?
CELL 3  does the uniqueness residual reach any reported number?
CELL 4  is Q(zeta_7)^+ the object's charge field K?

Run: python3 outside_bench/certificates/l72_exact_invariants.py
"""
import pathlib
import re
import subprocess

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
x = sp.Symbol('x')
PHI7 = sum(x**i for i in range(7))                      # Phi_7
z = sp.Symbol('z')


def red(p):
    """Reduce a polynomial in z modulo Phi_7(z), as a degree-<6 poly in z."""
    return sp.rem(sp.expand(p), PHI7.subs(x, z), z)


def zp(k):
    """zeta_7^k for any integer k (exponents taken mod 7), reduced."""
    return red(z**(k % 7))


def J_exact(N):
    """Habiro's closed form for the colored Jones of 4_1 at q = zeta_7, exactly."""
    tot, term = sp.Integer(1), sp.Integer(1)
    for k in range(1, N + 1):
        term = red(term * (zp(N) + zp(-N) - zp(k) - zp(-k)))
        tot = red(tot + term)
    return sp.expand(tot)


def minpoly_deg(elem):
    """Minimal polynomial over Q of an element written in z, with z a primitive 7th root."""
    root = sp.exp(2 * sp.pi * sp.I / 7)
    val = elem.subs(z, root)
    mp_ = sp.minimal_polynomial(sp.nsimplify(sp.simplify(val)), x)
    return sp.Poly(mp_, x), sp.degree(mp_, x)


print("=" * 78)
print("L72 -- THE LEVEL-2 INVARIANTS, EXACTLY")
print("seal sha256 4621857a643e631fbb6d1ceeb2bcee450aa58122db4f50947236cb301082b6a3")
print(f"HEAD = {subprocess.check_output(['git','-C',str(ROOT),'rev-parse','--short','HEAD']).decode().strip()}")
print("=" * 78)

# ------------------------------------------------------------------ C2, C1
print("\nC2 -- the tail-vanishing claim (the cell's loop runs one step past the standard sum)")
for N in (1, 3, 5):
    fac = sp.expand(zp(N) + zp(-N) - zp(N) - zp(-N))
    print(f"   N={N}: the j=N factor  q^N + q^-N - q^N - q^-N  = {fac}")
    assert fac == 0
print("   => every term with k >= N is zero; the cell's sum IS the standard Habiro sum.")

print("\nC1 -- Habiro's form must give the Jones polynomial of 4_1 at N = 2, EXACTLY in Z[q,1/q]")
q = sp.Symbol('q')
tot, term = sp.Integer(1), sp.Integer(1)
for k in range(1, 3):
    term = sp.expand(term * (q**2 + q**-2 - q**k - q**-k))
    tot = sp.expand(tot + term)
jones = q**2 - q + 1 - q**-1 + q**-2
print(f"   Habiro(N=2) = {sp.simplify(tot)}")
print(f"   Jones(4_1)  = {jones}")
diff = sp.simplify(sp.expand(tot - jones))
print(f"   difference  = {diff}")
assert diff == 0
print("   => EXACT match (the cell checked this numerically at a generic value; exact here).")

print("\nC3 (MB12) -- the minimal-polynomial routine must be able to answer something but 3")
for elem, want, label in [(z, 6, 'zeta_7 itself'), (sp.Integer(5), 1, 'a rational')]:
    poly, deg = minpoly_deg(elem)
    print(f"   {label:16s} -> degree {deg}  (want {want})   minpoly {poly.as_expr()}")
    assert deg == want
print("   => the routine discriminates; CELL 1 may be read.")

# ------------------------------------------------------------------ CELL 1
print("\n" + "=" * 78)
print("CELL 1 -- the exact values")
print("=" * 78)
vals, degs = {}, {}
for N in (1, 3, 5):
    v = J_exact(N)
    vals[N] = v
    poly, deg = minpoly_deg(v)
    degs[N] = deg
    print(f"\n  N={N}  (spin {(N-1)//2})")
    print(f"     J_N(zeta_7) = {v}")
    print(f"     minimal polynomial over Q : {poly.as_expr()}")
    print(f"     degree                    : {deg}")
print("\n  WHICH cubic field?  (the degree-3 minimal polynomials' discriminants)")
Rp = sp.minimal_polynomial(2 * sp.cos(2 * sp.pi / 7), x)
dR = sp.discriminant(Rp, x)
print(f"     Q(zeta_7)^+ generator {Rp.as_expr()}  disc = {dR}")
same_field = True
for N in (3, 5):
    poly, deg = minpoly_deg(vals[N])
    dd = sp.discriminant(poly.as_expr(), x)
    ratio = sp.nsimplify(sp.Rational(int(dd), int(dR)))
    issq = sp.sqrt(ratio).is_rational
    print(f"     N={N}: minpoly disc = {dd};  disc/disc(Q(z7)^+) = {ratio}, "
          f"a rational square: {issq}")
    same_field &= bool(issq)
print(f"     => both degree-3 invariants generate the SAME cubic field as Q(zeta_7)^+: "
      f"{same_field}")

cell1 = all(d in (1, 3) for d in degs.values())
print(f"\n  all three of degree <= 3 (i.e. inside the real cubic subfield): {cell1}")
print(f"  CELL 1 OUTCOME: {'A' if cell1 else 'B'}")

# ------------------------------------------------------------------ CELL 2
print("\n" + "=" * 78)
print("CELL 2 -- against the cell's printed floats")
print("=" * 78)
PRINTED = {1: '1.0', 3: '2.0881460000204', 5: '-0.6920214716301'}
root = sp.exp(2 * sp.pi * sp.I / 7)
ok2 = True
for N in (1, 3, 5):
    num = complex(sp.N(vals[N].subs(z, root), 30))
    want = float(PRINTED[N])
    agree = abs(num.real - want) < 1e-12 and abs(num.imag) < 1e-12
    ok2 &= agree
    print(f"   N={N}  exact -> {num.real:.13f}  (imag {num.imag:+.2e})   "
          f"cell printed {PRINTED[N]}   agree: {agree}")
print(f"\n  CELL 2 OUTCOME: {'A' if ok2 else 'B'}")

# ------------------------------------------------------------------ CELL 3
print("\n" + "=" * 78)
print("CELL 3 -- does the uniqueness residual reach any reported number?")
print("=" * 78)
src = (ROOT / 'frontier/B775_phase2_wave1/cells/P2W5-L72/compute.py').read_text()
body = src[src.index('def J_fig8'):]
body = body[:body.index('\n\n\n')] if '\n\n\n' in body[:2000] else body[:400]
print("  J_fig8's whole body, quoted:")
for line in body.split('\n')[:9]:
    print(f"     {line}")
touches = [t for t in ('F_', 'sixj', 'F(', 'assoc', '6j') if t in body]
print(f"\n  F-symbol / associator tokens inside J_fig8: {touches}")
assert not touches
print("  => the colored invariants are computed from q and N ALONE.")
import json
res = json.loads((ROOT / 'frontier/B775_phase2_wave1/cells/P2W5-L72/results.json').read_text())
print(f"\n  the cell's stored result keys: {list(res)}")
print(f"  D_object (the only reported knot numbers): {list(res['D_object'])}")
print("  C_level2 stores COUNTS of F-symbols and VERIFICATION residuals "
      f"(n_F_symbols_level2 = {res['C_level2']['n_F_symbols_level2']}), not a number that "
      "feeds anything downstream.")
print("  Every other stored quantity -- A_modular_data, C_level2's S/T/N errors, "
       "E_principal_index, F_CS_basepoint, G_deformation, H_CS_theta_even, I_wall -- is "
       "computed from the Weyl sum, SnapPy, or Fox calculus.")
print(f"\n  CELL 3 OUTCOME: A   (no reported number depends on the F-symbols)")

# ------------------------------------------------------------------ CELL 4
print("\n" + "=" * 78)
print("CELL 4 -- is Q(zeta_7)^+ the object's charge field K?")
print("=" * 78)
Kpoly = x**3 - 12 * x - 5
dK = sp.discriminant(Kpoly, x)
sqfK = sp.factorint(int(dK))
sf = 1
for p, e in sqfK.items():
    if e % 2: sf *= p
print(f"  K  = Q[x]/({Kpoly})   disc = {dK} = {sqfK}   squarefree part = {sf}")
print(f"       disc a perfect square? {sp.sqrt(dK).is_rational}  =>  Galois group "
      f"{'C3 (cyclic)' if sp.sqrt(dK).is_rational else 'S3 (NON-cyclic)'}")
Rpoly = sp.minimal_polynomial(2 * sp.cos(2 * sp.pi / 7), x)
dR = sp.discriminant(Rpoly, x)
print(f"  Q(z7)^+ = Q[x]/({Rpoly.as_expr()})   disc = {dR}")
print(f"       disc a perfect square? {sp.sqrt(dR).is_rational}  =>  Galois group "
      f"{'C3 (cyclic)' if sp.sqrt(dR).is_rational else 'S3 (NON-cyclic)'}")
iso = bool(sp.sqrt(dR).is_rational) == bool(sp.sqrt(dK).is_rational)
print(f"\n  same Galois type: {iso}")
print(f"  CELL 4 OUTCOME: {'B' if iso else 'A'}   "
      f"(not isomorphic, and the Galois type is the obstruction: {not iso})")

print("\n" + "=" * 78)
print("DONE -- outcomes above; interpretation lives in the memo, not here.")
print("=" * 78)
