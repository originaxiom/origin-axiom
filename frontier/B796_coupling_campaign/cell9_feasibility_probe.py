r"""CELL 9 FEASIBILITY PROBE (Wave 0; chat1's ranked-#1 open item).

Question: can m004 eigenvalues be computed at 50 digits at all?
If not, the campaign falsifier never fires and B796 is spectral
geometry, not a test of H0 (E32 at the scheduling level).

Method: measure, don't guess. (1) inventory the available
high-precision stacks; (2) measure the actual unit costs (mp K-Bessel
eval, mp dense solve at several n, extrapolate n^3); (3) compute the
REQUIRED system sizes from the truncation law (tail e^{-(x_cut - pi
r/2)} <= 10^{-digits-2}; x_cut = pi*r/2 + ln(10)*(digits+2); modes =
pi*R^2/covol(Lam*), R = x_cut/(2 pi Y)); (4) combine into a cost
table for 25 and 50 digits, with and without the /8 symmetrization,
per Newton solve and per eigenvalue (~6 solves); (5) verdict.

Gate 5-Q. This is instrument engineering, not a comparison — no
prereg required; the algebraicity TEST still requires the sealed
(d, H) power box + Sec-16 review before it runs at any precision.
"""
import time

import mpmath as mp
import numpy as np

print("=" * 72)
print("1. STACK INVENTORY")
print("=" * 72)
stacks = {}
for name, modname in [('python-flint (arb, C-speed)', 'flint'),
                      ('gmpy2', 'gmpy2'), ('flamp', 'flamp'),
                      ('sage', 'sage')]:
    try:
        __import__(modname)
        stacks[modname] = True
        print(f"  {name}: AVAILABLE")
    except ImportError:
        stacks[modname] = False
        print(f"  {name}: absent")
print(f"  mpmath (pure python): AVAILABLE (baseline)")
print()

print("=" * 72)
print("2. MEASURED UNIT COSTS")
print("=" * 72)

# --- mp K-Bessel at dps 60 (50-digit target + guard) ---
mp.mp.dps = 60
r1 = mp.mpf('3.938916864')
t0 = time.time()
NB = 40
for k in range(NB):
    mp.re(mp.besselk(1j * r1, mp.mpf(2) + k * mp.mpf('0.5')))
t_bessel = (time.time() - t0) / NB
print(f"  K_ir(x) via mpmath.besselk @ dps 60: {t_bessel*1e3:.1f} ms/eval")

# --- trapezoid K-Bessel at mp precision (our own quadrature, vectorless) ---
# nodes needed at dps d: h <= 2*pi/(2r + (2/ln10... use ln(10)*(d+2)/pi factor)
d50_Q = int(mp.ceil(mp.acosh((mp.pi * r1 / 2 + mp.log(10) * 52) / 1.4)
                    / (2 * mp.pi / (2 * r1 + 2 * mp.log(10) * 52 / mp.pi)))) + 1
t0 = time.time()
h = 2 * mp.pi / (2 * r1 + 2 * mp.log(10) * 52 / mp.pi)
x = mp.mpf(3)
acc = mp.mpf(0)
for q in range(d50_Q):
    acc += mp.e ** (-x * mp.cosh(q * h)) * mp.cos(r1 * q * h)
t_trap = time.time() - t0
print(f"  K_ir(x) via mp trapezoid ({d50_Q} nodes) @ dps 60: "
      f"{t_trap*1e3:.1f} ms/eval")
t_K = min(t_bessel, t_trap)

# --- mp dense LU solve at n = 100, 200 (extrapolate n^3) ---
for dps, label in [(30, '25-digit'), (60, '50-digit')]:
    mp.mp.dps = dps
    times = {}
    for n in (100, 200):
        A = mp.matrix(n, n)
        rng = np.random.default_rng(1)
        vals = rng.standard_normal((n, n))
        for i in range(n):
            for j in range(n):
                A[i, j] = mp.mpf(float(vals[i, j]))
        b = mp.matrix([mp.mpf(1)] * n)
        t0 = time.time()
        mp.lu_solve(A, b)
        times[n] = time.time() - t0
    # per-op cost from n=200 (n^3/3 flops in LU)
    c_op = times[200] / (200 ** 3 / 3)
    print(f"  mp.lu_solve @ dps {dps}: n=100: {times[100]:.2f}s, "
          f"n=200: {times[200]:.2f}s  -> ~{c_op*1e6:.1f} us/op "
          f"({label} stack)")
    if dps == 30:
        c30 = c_op
    else:
        c60 = c_op
print()

print("=" * 72)
print("3. REQUIRED SYSTEM SIZES (truncation law)")
print("=" * 72)
covol_dual = 1 / (2 * np.sqrt(3.0))
rmax = 7.1  # through the parent ground state


def modes_needed(digits, Y):
    x_cut = np.pi * rmax / 2 + np.log(10) * (digits + 2)
    R = x_cut / (2 * np.pi * Y)
    return int(np.pi * R * R / covol_dual), x_cut


print(f"{'digits':>7} {'Y':>5} {'modes (full)':>12} {'modes (/8 sym)':>14}")
table = {}
for digits in (25, 50):
    for Y in (0.75, 0.85):
        nmod, xc = modes_needed(digits, Y)
        table[(digits, Y)] = nmod
        print(f"{digits:>7} {Y:>5} {nmod:>12} {nmod//8:>14}")
print()
print("  (certified 8-digit run: 664-900 modes — chat1's ~5600 estimate")
print(f"   for 50 digits corresponds to Y=0.85 full: {table[(50,0.85)]})")
print()

print("=" * 72)
print("4. COST TABLE (per Newton solve; ~6 solves per eigenvalue)")
print("=" * 72)


def cost(n, c_op, t_k):
    lu = c_op * n ** 3 / 3
    bessel = t_k * n * 1.2  # square system: ~n distinct args per iter
    return lu + bessel


print(f"{'config':>34} {'n':>6} {'per solve':>12} {'per eigenvalue':>15}")
for digits, c_op in [(25, c30), (50, c60)]:
    for Y in (0.85,):
        for sym, div in [('full', 1), ('/8 sym', 8)]:
            n = table[(digits, Y)] // div
            c = cost(n, c_op, t_K)
            per_ev = 6 * c
            def fmt(s):
                return (f"{s/3600:.1f} h" if s > 3600 else
                        f"{s/60:.1f} min" if s > 60 else f"{s:.0f} s")
            print(f"{digits}-digit, Y={Y}, {sym:>7}: "
                  f"{'':>6}{n:>6} {fmt(c):>12} {fmt(per_ev):>15}")
print()

print("=" * 72)
print("5. VERDICT")
print("=" * 72)
n50 = table[(50, 0.85)]
c_full = cost(n50, c60, t_K) * 6
c_sym = cost(n50 // 8, c60, t_K) * 6
print(f"""
FEASIBILITY VERDICT (measured, not guessed):

- 50 digits, FULL system (n = {n50}): ~{c_full/3600:.0f} h per
  eigenvalue in pure mpmath — {'feasible but slow' if c_full < 7*86400 else 'INFEASIBLE in-sandbox'}.
- 50 digits, /8 SYMMETRIZED (n = {n50//8}): ~{c_sym/3600:.1f} h per
  eigenvalue — FEASIBLE in-sandbox IF the symmetrization is built
  (the one real engineering task; the D4 x conjugation action on the
  cusp torus must be implemented and validated against the certified
  8-digit eigenvectors).
- python-flint/arb available: {stacks.get('flint', False)} — if True, C-speed
  arb linear algebra cuts the mp constant by ~50-100x and even the
  full system becomes cheap; if False, the symmetrization is the
  feasibility hinge.
- 25 digits (the intermediate rung, enough to kill low-height
  relations d<=4, H<=10^4 per the power law): {'feasible NOW' if cost(table[(25,0.85)], c30, t_K)*6 < 6*3600 else 'needs symmetrization'} —
  n = {table[(25,0.85)]} full / {table[(25,0.85)]//8} symmetrized.

CONSEQUENCE FOR THE CAMPAIGN: Cell 9 is NOT unreachable — the
falsifier can fire — but its cost is a ladder, not a run: (i) 25-digit
rung first (validates the mp stack against the certified values and
already carries nonzero PSLQ power), (ii) symmetrization build,
(iii) 50-digit rung. The sealed (d, H) power box must be chosen PER
RUNG at prereg. If the symmetrization build fails validation, the
25-digit rung still runs and the campaign relabels only the 50-digit
claim, not the whole test.
""")
