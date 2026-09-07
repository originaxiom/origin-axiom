"""THE DIVISOR LAW for the cusp coefficients of m004's harmonic generator (conjectural, numerically found).

Modes:  nu = a + b*sqrt(-3) in Z[sqrt-3]   (mode (m1,m2) <-> a = m2/2, b = -m1; odd m2 is symmetry-forbidden)
"even" := nu in 2Z[omega]  <=>  a+b even;   "odd" otherwise.
Over ordered factorizations nu = d*e in Z[sqrt-3] (pairs counted up to the common sign):
   S(nu) = (1/|nu|) * sum_{d e = nu} w(d,e),
   w(d,e) = Re(d*conj(e))                 if d odd  and e odd
          = +(1/sqrt3) Im(d*conj(e))      if d odd  and e even
          = -(1/sqrt3) Im(d*conj(e))      if d even and e odd
          = 0                             if d even and e even
Prediction: c(nu) = c0 * S(nu),  c0 = c(1) = -4.260982633 i  (meridian period 1, maximal cusp at t=1).
"""
import numpy as np, json, sys
S3 = np.sqrt(3.0)
def mul(x,y): return (x[0]*y[0]-3*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def norm(x): return x[0]**2+3*x[1]**2
def divides(d, n):
    q = mul(n, conj(d)); N = norm(d)
    return q[0] % N == 0 and q[1] % N == 0
def quotient(n, d):
    q = mul(n, conj(d)); N = norm(d); return (q[0]//N, q[1]//N)
def divisors(n):
    N = norm(n); out = []
    A = int(np.sqrt(N))+1
    for a in range(-A, A+1):
        for b in range(0, int(np.sqrt(N/3))+2):
            d = (a,b)
            if d == (0,0) or (b == 0 and a < 0): continue
            if norm(d) <= N and divides(d, n): out.append(d)
    return out
def even(x): return (x[0]+x[1]) % 2 == 0          # x in 2Z[omega]
def S(n):
    if n == (0,0): return 0.0
    tot = 0.0
    for d in divisors(n):
        e = quotient(n, d)
        de = mul(d, conj(e))
        re, im = de[0], de[1]*S3
        if not even(d) and not even(e): tot += re
        elif not even(d) and even(e):   tot += im/S3
        elif even(d) and not even(e):   tot -= im/S3
    return tot/np.sqrt(norm(n))

def compare(coeffs, c0, nmax, tol_abs):
    """coeffs: {(m1,m2): complex}. Returns (n_tested, n_fail, worst, table)."""
    rows = []
    for (m1,m2), v in coeffs.items():
        if m2 % 2: continue
        n = (m2//2, -m1)
        if norm(n) > nmax: continue
        s = S(n); obs = v/c0
        rows.append((norm(n), (m1,m2), n, s, obs.real, obs.imag, abs(obs - s)))
    rows.sort()
    fails = [r for r in rows if r[6] > tol_abs]
    worst = max(r[6] for r in rows) if rows else 0
    return len(rows), len(fails), worst, rows

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else 'cusp_coefficient.json'
    key = sys.argv[2] if len(sys.argv) > 2 else 'coefficients_final'
    nmax = int(sys.argv[3]) if len(sys.argv) > 3 else 108
    tol = float(sys.argv[4]) if len(sys.argv) > 4 else 2e-3
    J = json.load(open(src))
    coeffs = {tuple(int(x) for x in k.split(',')): complex(*v) for k, v in J[key].items()}
    c0 = coeffs[(0,2)]
    nt, nf, worst, rows = compare(coeffs, c0, nmax, tol)
    print(f"source {src}[{key}]  c0 = {c0:.9f}")
    print(f"modes tested (N(nu) <= {nmax}): {nt}   failures (|obs - S| > {tol}): {nf}   worst |obs - S| = {worst:.2e}")
    print("  N   mode      nu=(a,b)     S(nu)      obs Re     obs Im     |diff|")
    for r in rows:
        flag = "  <-- FAIL" if r[6] > tol else ""
        print(f"{r[0]:4d}  {str(r[1]):9s} {str(r[2]):10s} {r[3]:+9.5f}  {r[4]:+9.5f}  {r[5]:+8.5f}   {r[6]:.1e}{flag}")
