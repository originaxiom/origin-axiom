#!/usr/bin/env python3
"""c_eff OF Zhat_0(S^3_{-1/2}(4_1)) -- MEASURED on 39525 exact coefficients.

Supersedes the asymptotic argument of memo 175 addendum 2, which read c_eff off the
block structure (mass F(2k-1) at exponent C_k = (2k-1)(k-1)) and gave

      c_eff = 3 (log phi)^2 / pi^2 = 0.070387265 .

That argument used TOTAL block mass.  The blocks are not points: Xi_k has width
2*floor((k-1)^2/4)+1, which grows like k^2/2 -- the same order as the block spacing
C_k ~ 2k^2.  Whether the spreading is a log correction (leaving the limit alone) or
changes the exponent is not settled by the argument; it is settled here by measuring.

Input: certificates/xi_recursion_fast.py 150, whose three controls (published blocks,
Fibonacci sums, eq (13) reproduction) all fire.

CALIBRATION (memo 171): the same envelope estimator is run on eta^-1 (true c_eff = 1)
and on the Rogers-Ramanujan character (true c_eff = 2/5, a case with c = -22/5 != c_eff),
so the reported hyperbolic number carries its own error bar.

Gate 5: exact integer series in, floating-point fit out.  No measured physical input.
"""
import json, math, subprocess, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
N = 150
subprocess.run([sys.executable, os.path.join(HERE, 'xi_recursion_fast.py'), str(N)],
               check=True, stdout=subprocess.DEVNULL)
raw = json.load(open('/tmp/zhat41_series.json'))
A = [0]*(max(int(k) for k in raw)+1)
for k, v in raw.items(): A[int(k)] = v
print(f"Zhat_0(S^3_{{-1/2}}(4_1)): {len(A)} exact coefficients, q^0 .. q^{len(A)-1}")
nz = [n for n, v in enumerate(A) if v]
print(f"   {len(nz)} nonzero; largest |a_n| = {max(abs(v) for v in A)} at "
      f"q^{max(range(len(A)), key=lambda n: abs(A[n]))}")

def envelope_ceff(a, lo_frac=0.5):
    """M(n) = max_{m<=n} |a_m| is monotone; log M(n) ~ 2 pi sqrt(c_eff n / 6)
       => c_eff(n) = 3 (log M(n))^2 / (2 pi^2 n).  Report the tail."""
    M = 0.0; out = []
    for n, v in enumerate(a):
        M = max(M, abs(v))
        if n >= 8 and M > 1:
            out.append((n, 3*math.log(M)**2/(2*math.pi**2*n)))
    return out

def slope_ceff(a, lo, hi):
    """least-squares log M(n) = alpha sqrt(n) + beta on n in [lo,hi]; c_eff = 3 alpha^2/(2 pi^2)"""
    M = 0.0; xs = []; ys = []
    for n, v in enumerate(a):
        M = max(M, abs(v))
        if lo <= n <= hi and M > 1:
            xs.append(math.sqrt(n)); ys.append(math.log(M))
    k = len(xs); sx = sum(xs); sy = sum(ys)
    sxx = sum(t*t for t in xs); sxy = sum(x*y for x, y in zip(xs, ys))
    al = (k*sxy - sx*sy)/(k*sxx - sx*sx)
    return 3*al*al/(2*math.pi**2), al

# ---------------- calibration arms ----------------
print("\nCALIBRATION (same estimator, cases with known c_eff)")
print("-"*72)
LIM = len(A)
def eta_inv(L):
    """1/(q;q)_inf = partition generating function (Euler pentagonal recurrence); c_eff = 1"""
    p = [0]*(L+1); p[0] = 1
    for n in range(1, L+1):
        t = 0; k = 1
        while True:
            g1 = k*(3*k-1)//2; g2 = k*(3*k+1)//2
            if g1 > n and g2 > n: break
            sgn = 1 if k % 2 else -1
            if g1 <= n: t += sgn*p[n-g1]
            if g2 <= n: t += sgn*p[n-g2]
            k += 1
        p[n] = t
    return p

def rogers_ramanujan(L):
    """prod 1/((1-q^{5n+1})(1-q^{5n+4})) ; c_eff = 2/5 (c = -22/5)"""
    out = [0]*(L+1); out[0] = 1
    for m in range(1, L+1):
        if m % 5 in (1, 4):
            for i in range(m, L+1):
                out[i] += out[i-m]
    return out

CAL = []
for nm, ser, true in (("eta^-1", eta_inv(min(LIM, 12000)), 1.0),
                      ("Rogers-Ramanujan", rogers_ramanujan(min(LIM, 12000)), 0.4)):
    L = len(ser)-1
    c_env = envelope_ceff(ser)[-1][1]
    c_sl, _ = slope_ceff(ser, L//2, L)
    CAL.append((nm, true, c_env, c_sl))
    print(f"   {nm:<18} true {true:<5}  envelope {c_env:.4f} ({c_env/true:.3f}x)"
          f"   slope-fit {c_sl:.4f} ({c_sl/true:.3f}x)")

# ---------------- the object ----------------
print("\nTHE HYPERBOLIC SERIES")
print("-"*72)
env = envelope_ceff(A)
for frac in (0.05, 0.1, 0.25, 0.5, 0.75, 1.0):
    n, c = env[min(len(env)-1, int(frac*len(env))-1)]
    print(f"   envelope estimate at n={n:<6} c_eff = {c:.6f}")
c_sl, al = slope_ceff(A, len(A)//2, len(A)-1)
print(f"\n   slope fit on the upper half (n in [{len(A)//2}, {len(A)-1}]):")
print(f"      log M(n) = {al:.6f} sqrt(n) + const   ->  c_eff = {c_sl:.6f}")

phi = (1+5**0.5)/2; lp = math.log(phi)
derived = 3*lp*lp/math.pi**2
print(f"\n   derivation (memo 175 add.2): 3 (log phi)^2/pi^2 = {derived:.6f}")
print(f"      predicted slope alpha = sqrt(2) log phi     = {math.sqrt(2)*lp:.6f}")
print(f"      measured  slope alpha                       = {al:.6f}   "
      f"ratio {al/(math.sqrt(2)*lp):.4f}")

# The right way to use the calibration: NOT to rescale the answer (the subleading
# structure of this series is not the subleading structure of eta^-1 or RR), but as
# the estimator's own demonstrated accuracy floor at this order.
ratios = [c/t for _, t, _, c in CAL]
worst = max(abs(1-r) for r in ratios)
print(f"\n   the same estimator on cases with a known answer: measured/true = "
      f"{', '.join(f'{r:.4f}' for r in ratios)}")
print(f"   so its own accuracy floor at this order is {worst*100:.1f}%.")
print(f"   measured/derived = {c_sl/derived:.4f}  -> deviation {abs(1-c_sl/derived)*100:.1f}%,")
print(f"   which is {'INSIDE' if abs(1-c_sl/derived) <= worst else 'OUTSIDE'} that floor.")
print(f"\n   REPORTED VALUE: c_eff = {c_sl:.6f} measured, {derived:.6f} derived.")
print(f"   (Do NOT rescale the measurement by the calibration ratio: the two arms'")
print(f"    subleading corrections are 1/(q;q)_inf-type, this series' is a -log n from")
print(f"    block spreading.  The calibration bounds the error, it does not remove it.)")
print(f"\n   target c((E6)_1) = 6.")
