#!/usr/bin/env bash
# B1157 WF-2 the dynamics -- reproduce the DECIDABLE core two ways:
#  (A) H*(m004; Sym^{2m}C^2) is NEVER acyclic: (H0,H1,H2)=(1,1,0) at m=0, (0,1,1)
#      for m>=1 -- derived from the ONE computed fact (the peripheral invariant line)
#      + standard topology (half-lives-half-dies, chi=0, Poincare duality on T^2).
#      => cc3's B8142b closed-Fried antecedent is REFUTED; its reflection stays conditional.
#  (B) Vol is the same scalar on both sides (B1156 regulator = B8142b damping): the
#      "Vol coincidence" is the tautology Vol(M)=Vol(M), NOT an arithmetic crossing.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' | tee acyclicity_and_vol.txt
import sympy as sp, mpmath as mp

def sym_power(M, n):
    x, y = sp.symbols('x y')
    a, b, c, d = M
    X, Y = a*x + b*y, c*x + d*y
    cols = []
    for k in range(n + 1):
        poly = sp.Poly(sp.expand((X**(n-k))*(Y**k)), x, y)
        cols.append([poly.coeff_monomial(x**(n-j)*y**j) for j in range(n+1)])
    return sp.Matrix([[cols[k][r] for k in range(n+1)] for r in range(n+1)])

print("(A) ACYCLICITY OF H*(m004; Sym^{2m}) -- via the peripheral invariant line")
print("    m004 has ONE cusp; peripheral pi_1 = <mu,lambda>=Z^2, both PARABOLIC")
print("    (regular unipotent). Sym^{2m} of a regular unipotent is a single Jordan")
print("    block of size 2m+1 => exactly a 1-dim invariant line, SHARED by mu,lambda.")
P = (1, 1, 0, 1)  # a regular unipotent parabolic
print()
print("    m | dimV=2m+1 | H0(T^2)=dim joint-inv | H1(T^2)=2*H0 | H1(M)=half | (H0,H1,H2)(M)")
ok = True
for m in range(0, 6):
    n = 2*m
    if m == 0:
        # trivial rep: H*(M;C) of the figure-eight complement = (1,1,0)
        h0T2, h1T2, hM = 1, 2, 1
        triple = (1, 1, 0)
    else:
        S = sym_power(P, n)
        h0T2 = len((S - sp.eye(n+1)).nullspace())     # joint invariants (mu,lambda share the line)
        h1T2 = 2*h0T2                                   # T^2: chi=0, PD => H1 = 2*H0
        hM = h1T2 // 2                                  # half-lives-half-dies: H1(M)=(1/2)H1(T^2)
        # H0(M)=0 (rho irreducible, m>=1); chi_rho=(2m+1)*chi(M)=0 => H2(M)=H1(M); H3=0
        triple = (0, hM, hM)
    flag = "" if h0T2 == 1 else "  <-- UNEXPECTED"
    if h0T2 != 1:
        ok = False
    print(f"    {m} |    {n+1:2d}     |         {h0T2}          |      {h1T2}       |    {hM}     |   {triple}{flag}")
print()
print("    => H* is NEVER acyclic (H1=H2=#cusps=1 for all m>=1). The closed-manifold")
print("       Fried hypothesis rho(m) acyclic is REFUTED. Triply corroborated:")
print("       deformation dim H1(M;Ad)=1 (m004's unique cusp); Menal-Ferrer-Porti even")
print("       symmetric powers => H1=#cusps (banked B581); Fox calculus (WF-2 attempt).")

print()
print("(B) VOL IS THE SAME SCALAR ON BOTH SIDES -- the tautology, not a crossing")
mp.mp.dps = 25
z = mp.expjpi(mp.mpf(1)/3)
Vol = 2*mp.im(mp.polylog(2, z))
print("    Vol(4_1)          = 2*D(e^{i pi/3}) =", Vol)
print("    B1156 uses Vol as: the Borel/Bloch-Wigner REGULATOR of xi (archimedean summand)")
print("    B8142b uses Vol as: the geodesic-flow DAMPING exp(-4m Vol/pi)")
print("    exp(-4 Vol/pi)    =", mp.e**(-4*Vol/mp.pi), " (B8142b: 0.0754)")
print("    Both are functions of the ONE hyperbolic structure => Vol(M)=Vol(M).")

assert ok, "invariant line must be 1-dim at every m"
print()
print("REPRODUCES")
PY
