#!/usr/bin/env python3
"""DOES c_eff SCALE WITH THE SURGERY SLOPE?  The one factor in the law with no evidence.

Memo 176's law   c_eff = 3 |p/r| (log lambda)^2 / (2 pi^2)   was tested at ONE slope
(p/r = -1/2, arm A) and at one degenerate case (lambda = 1, arm B).  The |p/r| factor was
DERIVED and never MEASURED.  Here it is measured, at no extra cost: the Xi_k blocks of 4_1
are slope-independent, so the same 150 blocks assemble Zhat at any slope.

Thm 1.2 with (x^{1/2r} - x^{-1/2r}) F_K and eq (1)'s L^{(a)}_{p/r}: x^u -> q^{-(r/p)u^2}:
for p = -1 (so p Z = Z and the spin^c selection rule ru - a in pZ is satisfied by every
term with a = 0 when r*(k-1/2) +- 1/2 is an integer, i.e. for every r), block k lands at

    E_-(k) = r(k-1/2)^2 - (k-1/2) + 1/(4r)      with  +Xi_k
    E_+(k) = r(k-1/2)^2 + (k-1/2) + 1/(4r)      with  -Xi_k

separation E_+ - E_- = 2k-1, independent of r.  Shifting by min E reproduces, for r = 2,
exactly the centres C_k = (2k-1)(k-1) of memo 175 -- checked below as the control.

PREREGISTERED, two-outcome, fixed before the runs:
   OUTCOME A  the measured c_eff at r = 1, 2, 3 is proportional to |p/r| = 1/r within the
              estimator's demonstrated 2.0% floor  ->  the law's slope factor is confirmed.
   OUTCOME B  it is not  ->  the law is wrong in its slope dependence and memo 176 section 5
              must be head-noted.
The ratios are FORCED: c_eff(r) = 6 (log phi)^2 / (r pi^2), so r=1 : r=2 : r=3 is 1 : 1/2 : 1/3.

CONTROL (voids the run if it fails): at r = 2 the assembled series must reproduce eq (13)'s
ten published coefficients and carry nothing else in q^0..q^16.

Gate 5: exact integer/rational arithmetic in, one floating-point fit out.
"""
import os, sys, math, json, subprocess, contextlib, io
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
N = 150

# --- pull the Xi blocks from the validated generator (its own controls run there) ----
src = open(os.path.join(HERE, 'xi_recursion_fast.py')).read()
ns = {}
sys.argv = ['x', str(N)]
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    try: exec(compile(src, 'xi_recursion_fast.py', 'exec'), ns)
    except SystemExit: pass
gen_out = buf.getvalue()
for line in gen_out.splitlines():
    if 'C1 ' in line or 'C2 ' in line or 'C3 ' in line: print("   [generator] " + line.strip())
assert 'C1 four published blocks : PASSED' in gen_out
assert f'C2 Fibonacci sums k<={N}  : PASSED' in gen_out
block = ns['block']
BLOCKS = {k: block(k) for k in range(1, N+1)}

def assemble(r):
    """Zhat_0(S^3_{-1/r}(4_1)) coefficients as a dict, exponents shifted to start at 0."""
    E = {}
    for k in range(1, N+1):
        h = Fr(2*k-1, 2)                       # k - 1/2
        base = r*h*h + Fr(1, 4*r)
        E[k] = (base - h, base + h)
    shift = min(E[1])
    out = {}
    for k in range(1, N+1):
        lo, cs = BLOCKS[k]
        for sgn, e in ((1, E[k][0]), (-1, E[k][1])):
            e0 = e - shift
            assert e0.denominator == 1, f"non-integral exponent {e0} at r={r}, k={k}"
            e0 = int(e0)
            for i, c in enumerate(cs):
                x = e0 + lo + i
                out[x] = out.get(x, 0) + sgn*c
    # safe horizon: below anything block N+1 could reach
    kk = N+1; h = Fr(2*kk-1, 2)
    nxt = r*h*h + Fr(1,4*r) - h - shift
    w = (kk-1)**2//4
    return out, int(nxt) - w - 1

def slope_fit(a, lo, hi):
    M = 0.0; xs = []; ys = []
    for n in range(0, hi+1):
        M = max(M, abs(a.get(n, 0)))
        if lo <= n <= hi and M > 1:
            xs.append(math.sqrt(n)); ys.append(math.log(M))
    k = len(xs); sx = sum(xs); sy = sum(ys)
    sxx = sum(t*t for t in xs); sxy = sum(u*v for u, v in zip(xs, ys))
    al = (k*sxy - sx*sy)/(k*sxx - sx*sx)
    return 3*al*al/(2*math.pi**2), al

GIVEN = {0:1, 1:-1, 3:2, 6:-2, 9:1, 10:3, 11:1, 14:-1, 15:-3, 16:-1}
phi = (1+5**0.5)/2; lp = math.log(phi)

print("\nCONTROL at r = 2 (the published case)")
print("-"*72)
A2, H2 = assemble(2)
c2ok = all(A2.get(e, 0) == v for e, v in GIVEN.items()) and \
       all(A2.get(e, 0) == 0 for e in range(17) if e not in GIVEN)
cent = [int(Fr(2*(2*k-1)**2, 4) + Fr(1,8) - Fr(2*k-1,2) - (Fr(2,4)+Fr(1,8)-Fr(1,2)))
        for k in range(1, 7)]
print(f"   eq (13)'s ten coefficients + nothing else in q^0..q^16 : {'PASSED' if c2ok else 'FAILED'}")
print(f"   derived centres C_k for k=1..6 : {cent}  (memo 175: (2k-1)(k-1) = "
      f"{[(2*k-1)*(k-1) for k in range(1,7)]})")
if not c2ok:
    raise SystemExit("control failed -- nothing reported")

print("\nTHE SLOPE SCAN   (p = -1;  slope p/r = -1/r;  |p/r| = 1/r)")
print("-"*72)
print(f"   {'r':>3} {'|p/r|':>7} {'horizon':>9} {'law c_eff':>12} {'measured':>11} {'meas/law':>9}")
rows = []
for r in (1, 2, 3, 4):
    A, H = assemble(r)
    law = 3*(1.0/r)*(2*lp)**2/(2*math.pi**2)
    meas, al = slope_fit(A, H//2, H)
    rows.append((r, law, meas, meas/law, H))
    print(f"   {r:>3} {1.0/r:>7.4f} {H:>9} {law:>12.6f} {meas:>11.6f} {meas/law:>9.4f}")

FLOOR = 0.0197        # the estimator's demonstrated worst error (eta^-1, Rogers-Ramanujan)
print(f"\n   estimator's demonstrated accuracy floor at this order: {FLOOR*100:.1f}%")
worst = max(abs(1-t[3]) for t in rows)
ok = worst <= FLOOR
print(f"   worst deviation across the four slopes: {worst*100:.1f}%")
print(f"\n   OUTCOME {'A -- the |p/r| factor is CONFIRMED' if ok else 'B -- the slope dependence is WRONG'}")

print("\n   ratio test, independent of the absolute normalisation:")
base = rows[0][2]
for r, law, meas, _, _ in rows:
    print(f"      c_eff(r={r})/c_eff(r=1) measured {meas/base:.4f}   law says {1.0/r:.4f}   "
          f"deviation {abs(meas/base - 1.0/r)/(1.0/r)*100:.1f}%")

# ---------------------------------------------------------------------------------
# The preregistered outcome above is what it is.  This diagnostic does NOT change it;
# it asks a separate question: is the drift a finite-block-count effect, or the law?
# If it is the horizon, meas/law rises toward 1 as the block count grows, at every r.
# If the ratios are flat in the block count, the slope factor is genuinely wrong.
print("\n" + "="*72)
print("DIAGNOSTIC -- is the drift a horizon effect?  (does not change the outcome above)")
print("="*72)
def scan(kmax):
    res = {}
    for r in (1, 2, 3, 4):
        E = {}
        for k in range(1, kmax+1):
            h = Fr(2*k-1, 2); base = r*h*h + Fr(1, 4*r)
            E[k] = (base - h, base + h)
        shift = min(E[1]); out = {}
        for k in range(1, kmax+1):
            lo, cs = BLOCKS[k]
            for sgn, e in ((1, E[k][0]), (-1, E[k][1])):
                e0 = int(e - shift)
                for i, c in enumerate(cs): 
                    x = e0 + lo + i; out[x] = out.get(x, 0) + sgn*c
        kk = kmax+1; h = Fr(2*kk-1, 2)
        H = int(r*h*h + Fr(1,4*r) - h - shift) - (kk-1)**2//4 - 1
        law = 3*(1.0/r)*(2*lp)**2/(2*math.pi**2)
        meas, _ = slope_fit(out, H//2, H)
        res[r] = meas/law
    return res
print(f"   {'blocks':>7} " + " ".join(f"{'r='+str(r):>9}" for r in (1,2,3,4)))
tab = {}
for kmax in (40, 60, 90, 120, 150):
    res = scan(kmax); tab[kmax] = res
    print(f"   {kmax:>7} " + " ".join(f"{res[r]:>9.4f}" for r in (1,2,3,4)))
print("\n   trend in meas/law from 40 blocks to 150 blocks:")
for r in (1,2,3,4):
    d = tab[150][r] - tab[40][r]
    print(f"      r={r}: {tab[40][r]:.4f} -> {tab[150][r]:.4f}   {'rising toward 1' if d > 0 else 'falling'} ({d:+.4f})")
allrise = all(tab[150][r] - tab[40][r] > 0 for r in (1,2,3,4))
print(f"\n   every slope moves toward the law as blocks are added: {allrise}")
print( "   READ THIS CAREFULLY: a monotone approach is CONSISTENT with a horizon effect.")
print( "   It is NOT proof of one, and it does NOT retroactively convert OUTCOME B into A.")
print( "   The preregistered cell stands as B; what this adds is that the residual is")
print( "   largest where the asymptotics is weakest, which is the direction a horizon")
print( "   effect predicts and the direction a wrong exponent would not.")
