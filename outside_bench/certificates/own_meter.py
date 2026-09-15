#!/usr/bin/env python3
"""MEMO-91 CELL: THE OWN METER — the object's internal unit system,
verified exactly in-lane: the curvature normalization (Lambda = -1) as
a symbolic tensor identity, the volume as a special L-value of the
object's own arithmetic shadow in FOUR independent expressions agreeing
to 50 digits, the systole recomputed from its exact trace, and the
entropy standard from the exact spectral radius.  Campaign THE SECOND
HALF, lane B (ledger row W4).

THE UNIT SYSTEM (the convention this lane adopts, argued in the memo):
  PRIMARY length standard: the curvature radius = 1 — forced by the
  Einstein equation itself (B259; verified symbolically below), the
  convention every banked number already lives in.
  The object's canonical pure numbers in that unit:
    Vol      = 2.029883212819307250042405108...   (the action)
    systole  = 1.08707014499574...  (torsion 1.72276844987...)
    entropy  = 2 log phi = 0.96242365011920...    (per tick)
    kappa    = 1 + omega  (min poly X^2-3X+3; the conserved price)
    C0       = 3^(-1/4)   (Kashaev tower head; PINNED, not recomputed)

PREREGISTERED (two-outcome; any failure banks as an error):
  FACT 1 (symbolic): the hyperbolic metric g = (dx^2+dy^2+dz^2)/z^2 in
     3d has Ric = -2 g, R = -6, and solves the vacuum Einstein equation
     R_ij - (R/2) g_ij + Lambda g_ij = 0 with Lambda = -1 EXACTLY
     (sympy tensor computation from Christoffel symbols — B259's claim
     re-verified from scratch in-lane).
  FACT 2 (50 digits): FOUR expressions for the volume agree pairwise to
     50 decimal places:
       V1 = 9 sqrt3 zeta_K(2) / pi^2   with zeta_K(2) = zeta(2) L(2,chi_-3)
       V2 = (3 sqrt3 / 2) L(2, chi_-3)
       V3 = 2 Im Li2(e^{i pi/3})
       V4 = 6 Lob(pi/3) = 3 Im Li2(e^{2 i pi/3})
     (V1 = B1117's adelic form: the METER IS AN L-VALUE of K = Q(sqrt-3);
      V1 = V2 is an identity via zeta(2) = pi^2/6 — asserted symbolically
      too, so the two banked dressings are provably one equation.)
  FACT 3 (exact trace -> length): the systole's banked exact trace
     2 - omega (omega = the lane's q = e^{i pi/3}, q^2-q+1 = 0; Z[q] is
     the Eisenstein ring; memo 81, [ab^-1]) reproduces the banked
     complex length: l = 1.08707014499574 (13 digits, the B850
     positive-control value) and |torsion| = 1.72276844987...
  FACT 4 (exact): the fiber tick matrix [[0,-1],[1,3]] (memo 49) has
     spectral radius phi^2 EXACTLY (root of x^2-3x+1), so the entropy
     standard is 2 log phi; numeric cross-pin 0.9624236501192069.
  PINS: lane outputs (geodesic_tongue, trace_three, carrier) as listed.
FENCES: C0 = 3^(-1/4) and the tower coefficients C1, C2 are cited
(B1120), not recomputed here.  The anti-numerology fence stands: B743
(the four transcendental units vs 18 SM ratios: 0 hits) and B1126 (the
Kashaev RATIOS C1/C0..C3/C0 among 352 pairs: null) — the raw magnitudes
C0, C1, C2 themselves remain untested against B743's instrument (a
narrower gap than the wave-1 draft claimed; guard catch filed).  B291's
systole-vs-min-volume divergence is a statement about the DEHN FILLING
family, not about m004's own two meters (both finite here).  Gate 5
untouched: no measured value enters; the meter is the object's own.
"""
import os
import sympy as sp
from mpmath import mp, mpf, mpc, zeta, polylog, pi as mppi, exp as mpexp, mpmathify, acosh, sqrt as mpsqrt, log as mplog, phi as mpphi

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("BENCH_OUT") or os.path.join(HERE, "..", "outputs")

def has(fname, needle):
    with open(os.path.join(OUT, fname)) as f:
        assert needle in f.read(), f"PIN MISSING in {fname}: {needle!r}"
    return True

# ---------- FACT 1: curvature normalization, symbolic from scratch ----------
x, y, z = sp.symbols('x y z', positive=True)
coords = [x, y, z]
g = sp.diag(1/z**2, 1/z**2, 1/z**2)
ginv = g.inv()
n = 3
Gamma = [[[sp.S(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            s = sp.S(0)
            for d in range(n):
                s += ginv[a, d]*(sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b]) - sp.diff(g[b, c], coords[d]))
            Gamma[a][b][c] = sp.simplify(s/2)
Ric = sp.zeros(n, n)
for b in range(n):
    for c in range(n):
        s = sp.S(0)
        for a in range(n):
            s += sp.diff(Gamma[a][b][c], coords[a]) - sp.diff(Gamma[a][b][a], coords[c])
            for d in range(n):
                s += Gamma[a][a][d]*Gamma[d][b][c] - Gamma[a][c][d]*Gamma[d][b][a]
        Ric[b, c] = sp.simplify(s)
assert sp.simplify(Ric + 2*g) == sp.zeros(3, 3), Ric
Rscal = sp.simplify(sum(ginv[i, j]*Ric[i, j] for i in range(3) for j in range(3)))
assert Rscal == -6, Rscal
LAM = -1
Einstein = sp.simplify(Ric - sp.Rational(1, 2)*Rscal*g + LAM*g)
assert Einstein == sp.zeros(3, 3), Einstein
print("FACT 1: g = (dx^2+dy^2+dz^2)/z^2 gives Ric = -2g, R = -6, and the")
print("   vacuum Einstein equation holds with Lambda = -1 EXACTLY (symbolic,")
print("   from Christoffel symbols) — B259 re-verified from scratch in-lane.")
print("   => the curvature radius is the forced length standard; unit = 1.")

# ---------- FACT 2: the volume as an L-value, four expressions, 50 digits ----------
mp.dps = 60
# L(2, chi_-3) via Hurwitz zeta: L(s,chi) = 3^-s (zeta(s,1/3) - zeta(s,2/3))
L2 = 3**mpf(-2) * (zeta(2, mpf(1)/3) - zeta(2, mpf(2)/3))
zetaK2 = (mppi**2/6) * L2
V1 = 9*mpsqrt(3)*zetaK2/mppi**2
V2 = (3*mpsqrt(3)/2)*L2
V3 = 2*polylog(2, mpexp(1j*mppi/3)).imag
V4 = 3*polylog(2, mpexp(2j*mppi/3)).imag
vols = [V1, V2, V3, V4]
for i in range(4):
    for j in range(i+1, 4):
        assert abs(vols[i]-vols[j]) < mpf(10)**(-50), (i, j, abs(vols[i]-vols[j]))
# V1 == V2 symbolically: 9 sqrt3 (pi^2/6) L / pi^2 == (3 sqrt3/2) L
Ls = sp.symbols('L', positive=True)
assert sp.simplify(9*sp.sqrt(3)*(sp.pi**2/6)*Ls/sp.pi**2 - sp.Rational(3, 2)*sp.sqrt(3)*Ls) == 0
VOL = mp.nstr(V1, 50)
print(f"FACT 2: Vol = {VOL}")
print("   9*sqrt3*zeta_K(2)/pi^2 = (3 sqrt3/2) L(2,chi_-3)  [identity, symbolic]")
print("   = 2 Im Li2(e^(i pi/3)) = 6 Lob(pi/3): all four agree to 50 digits.")
print("   THE METER IS AN L-VALUE: the archimedean action equals a special")
print("   value of the object's own finite shadow K = Q(sqrt-3) (B1117 form).")

# ---------- FACT 3: systole from its exact trace ----------
omega = mpexp(1j*mppi/3)            # the lane's q (q^2 - q + 1 = 0): Z[q] = the Eisenstein ring
tr = 2 - omega                      # memo 81: [ab^-1], exact trace 2 - omega
cl = 2*acosh(tr/2)                  # complex length, principal branch
l, tors = abs(cl.real), abs(cl.imag)
assert abs(l - mpmathify('1.08707014499574')) < mpf(10)**(-13), l
assert abs(tors - mpmathify('1.72276844987')) < mpf(10)**(-10), tors
print(f"FACT 3: trace 2-omega => complex length {mp.nstr(l,15)} + {mp.nstr(tors,15)} i")
print("   reproducing the banked systole (memo 81 exact trace; B850's")
print("   positive-control value 1.08707014499574 to 13 digits).")

# ---------- FACT 4: the entropy standard, exact ----------
X = sp.symbols('X')
M = sp.Matrix([[0, -1], [1, 3]])
cp = M.charpoly(X).as_expr()
assert sp.expand(cp - (X**2 - 3*X + 1)) == 0
phis = (1 + sp.sqrt(5))/2
assert sp.simplify(phis**4 - 3*phis**2 + 1) == 0        # phi^2 is a root
ent = 2*mplog(mpphi)
assert abs(ent - mpmathify('0.9624236501192069')) < mpf(10)**(-15)
print(f"FACT 4: fiber tick [[0,-1],[1,3]] has spectral radius phi^2 exactly")
print(f"   (x^2-3x+1); entropy standard 2 log phi = {mp.nstr(ent,17)} per tick.")

# ---------- pins into the banked lane ----------
has("geodesic_tongue_out.txt", "exact trace 2+(-1)w")
has("geodesic_tongue_out.txt", "complex length 1.087070 + 1.722768 i")
has("trace_three_out.txt", "spectral radius phi^2")
has("trace_three_out.txt", "characteristic polynomial: x^2 - 3x + 1   trace 3, det 1, disc 5")
has("kappa_beat_out.txt", "X^2 - 3X + 3")
print("PINS: memo 81 (systole), memo 49 (tick polynomial), memo 41 (kappa) hold.")

print("""
THE OWN METER STANDS: with the curvature radius as the forced unit
(Lambda = -1, verified symbolically from scratch), the object's canon
is a short table of pure numbers — Vol (an exact L-value of its own
arithmetic shadow, four expressions to 50 digits), the systole (from
its exact Eisenstein trace), the entropy 2 log phi (exact), kappa
(min poly X^2-3X+3) — every one already dimensionless in the object's
own meter.  The grand computation speaks THIS unit system; converting
to ours is the bridge's job (deferred), guarded by the banked
anti-numerology nulls (B743; B1126 ratio sweep — raw C0/C1/C2
magnitudes remain the one untested corner).  Gate 5 untouched.""")
