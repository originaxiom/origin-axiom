#!/usr/bin/env python3
"""THE r=1 ASSEMBLY *IS* RAMANUJAN'S ORDER-7 MOCK THETA F_0 -- and that decides c_eff.

Gukov-Manolescu section 9.4, eq (175):   Zhat_0(-Sigma(2,3,7)) = -q^{-1/2} F_0(q),
   F_0(q) = sum_{n>=0} q^{n^2} / (q^{n+1};q)_n ,
computed there by a completely different route (the Seifert plumbing formula (41) plus
modularity, via [16] eq (7.21)) from the route used here (section 9.3's recursion for
F_{4_1}, then Thm 1.2's Laplace transform at p/r = -1).

  S^3_{-1}(4_1) = -Sigma(2,3,7),

so the two must agree.  IDENTITY CHECK below: they agree termwise.  That is an external,
published validation of this bench's entire pipeline -- generator, block placement, and
slope assembly -- by an object the pipeline never saw.

IT ALSO SETTLES A NUMBER.  Memo 176's law predicts, at p/r = -1 and lambda = phi^2,

      c_eff = 6 (log phi)^2 / pi^2 = 0.140775 ,

while F_0 is an order-7 mock theta whose coefficients are classically expected to grow with
c_eff = 1/7 = 0.142857.  These differ by 1.5%, which is INSIDE the 2-parameter estimator's
2.0% floor -- so the two-parameter fit cannot tell them apart, and memo 176 did not.
A three-parameter fit  log a_n = A sqrt(n) + B log n + C  can, and is calibrated here on
cases where A and B are both known exactly.

PREREGISTERED, two outcomes, fixed before the fit runs:
   OUTCOME 1/7   the fit selects 1/7  ->  memo 176's law has the WRONG CONSTANT and section 5
                 must be corrected: the golden ratio is not what sets c_eff.
   OUTCOME PHI   the fit selects 6(log phi)^2/pi^2  ->  the law stands and the 1/7 of memo 174
                 was estimator bias.
The two targets are 1.5% apart; the calibration below fixes whether the fit can resolve that.

Gate 5: exact integer series in, one fit out.
"""
import sys, os, io, math, contextlib
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200

# ---------- the assembly at p/r = -1 -------------------------------------------------
src = open(os.path.join(HERE, 'xi_recursion_fast.py')).read()
ns = {}; sys.argv = ['x', str(N)]
with contextlib.redirect_stdout(io.StringIO()):
    try: exec(compile(src, 'xi_recursion_fast.py', 'exec'), ns)
    except SystemExit: pass
block = ns['block']
r = 1; E = {}
for k in range(1, N+1):
    h = Fr(2*k-1, 2); base = r*h*h + Fr(1, 4*r); E[k] = (base-h, base+h)
shift = min(E[1]); out = {}
for k in range(1, N+1):
    lo, cs = block(k)
    for sgn, e in ((1, E[k][0]), (-1, E[k][1])):
        e0 = int(e - shift)
        for i, c in enumerate(cs): out[e0+lo+i] = out.get(e0+lo+i, 0) + sgn*c
kk = N+1; h = Fr(2*kk-1, 2)
H = int(r*h*h + Fr(1,4*r) - h - shift) - (kk-1)**2//4 - 1
ASM = [out.get(n, 0) for n in range(H+1)]
print(f"assembly at p/r = -1 from {N} blocks: exact to q^{H}")

# ---------- Ramanujan F_0, independently ---------------------------------------------
def F0(L):
    F = [0]*(L+1); n = 0
    while n*n <= L:
        cur = [0]*(L+1); cur[n*n] = 1
        for j in range(n+1, 2*n+1):
            nxt = [0]*(L+1)
            for i in range(L+1):
                if cur[i]:
                    m = i
                    while m <= L: nxt[m] += cur[i]; m += j
            cur = nxt
        for i in range(L+1): F[i] += cur[i]
        n += 1
    return F
LID = min(H, 3000)
FF = F0(LID)
same = all(ASM[i] == FF[i] for i in range(LID+1))
print(f"IDENTITY CHECK  assembly == F_0 termwise over q^0..q^{LID}: {same}")
print(f"   first terms: {ASM[:14]}")
print( "   paper eq (175): 1 + q + q^3 + q^4 + q^5 + 2q^7 + q^8 + 2q^9 + q^10 + 2q^11 + q^12 + 3q^13")
if not same: raise SystemExit("IDENTITY FAILS -- the pipeline is wrong, nothing else is reported")

# ---------- three-parameter fit, calibrated ------------------------------------------
def fit3(a, lo, hi):
    """log a_n = A sqrt(n) + B log n + C on the positive coefficients in [lo,hi]"""
    X = [[math.sqrt(n), math.log(n), 1.0] for n in range(lo, hi+1) if n > 1 and a[n] > 0]
    Y = [math.log(a[n]) for n in range(lo, hi+1) if n > 1 and a[n] > 0]
    m = len(X[0]); M = [[sum(X[i][p]*X[i][q_] for i in range(len(X))) for q_ in range(m)] for p in range(m)]
    V = [sum(X[i][p]*Y[i] for i in range(len(X))) for p in range(m)]
    for c in range(m):
        piv = max(range(c, m), key=lambda rr: abs(M[rr][c])); M[c], M[piv] = M[piv], M[c]; V[c], V[piv] = V[piv], V[c]
        for rr in range(m):
            if rr == c: continue
            f = M[rr][c]/M[c][c]
            for cc in range(m): M[rr][cc] -= f*M[c][cc]
            V[rr] -= f*V[c]
    sol = [V[i]/M[i][i] for i in range(m)]
    A, B, C = sol
    return 3*A*A/(2*math.pi**2), A, B

def eta_inv(L):
    p = [0]*(L+1); p[0] = 1
    for n in range(1, L+1):
        s = 0; k = 1
        while True:
            g1 = k*(3*k-1)//2; g2 = k*(3*k+1)//2
            if g1 > n and g2 > n: break
            sg = 1 if k % 2 else -1
            if g1 <= n: s += sg*p[n-g1]
            if g2 <= n: s += sg*p[n-g2]
            k += 1
        p[n] = s
    return p
def rr(L):
    o = [0]*(L+1); o[0] = 1
    for m in range(1, L+1):
        if m % 5 in (1, 4):
            for i in range(m, L+1): o[i] += o[i-m]
    return o

print("\nCALIBRATION of the three-parameter fit (A and B both known exactly)")
print("-"*74)
CL = min(H, 20000)
cal = []
for nm, ser, ct, At, Bt in (("eta^-1", eta_inv(CL), 1.0, math.pi*math.sqrt(2/3), -1.0),
                            ("Rogers-Ramanujan", rr(CL), 0.4, 2*math.pi*math.sqrt(0.4/6), None)):
    c, A, B = fit3(ser, CL//2, CL)
    cal.append(abs(1-c/ct))
    bt = f"{Bt:+.3f}" if Bt is not None else "  -  "
    print(f"   {nm:<18} true c_eff {ct:<5}  fitted {c:.6f} ({c/ct:.4f}x)   A {A:.5f} vs {At:.5f}"
          f"   B {B:+.3f} vs {bt}")
floor3 = max(cal)
print(f"   three-parameter fit accuracy floor at this order: {floor3*100:.2f}%")
print(f"   (the two-parameter fit's floor was 2.0% -- too coarse to separate the two targets)")

print("\nTHE DECISION")
print("-"*74)
c, A, B = fit3(ASM, H//2, H)
T17 = 1/7.0
phi = (1+5**0.5)/2
TPH = 6*math.log(phi)**2/math.pi**2
print(f"   fitted   c_eff = {c:.7f}      (A = {A:.6f}, B = {B:+.4f})")
print(f"   target 1/7            = {T17:.7f}   ratio {c/T17:.5f}   |dev| {abs(1-c/T17)*100:.2f}%")
print(f"   target 6(log phi)^2/pi^2 = {TPH:.7f}   ratio {c/TPH:.5f}   |dev| {abs(1-c/TPH)*100:.2f}%")
d17, dph = abs(1-c/T17), abs(1-c/TPH)
sep = abs(T17-TPH)/TPH
print(f"\n   the two targets are {sep*100:.2f}% apart; the fit resolves to {floor3*100:.2f}%")
if max(d17, dph) < floor3:
    print("   VERDICT: UNRESOLVED -- both targets sit inside the fit's own error. Report as open.")
else:
    pick = "1/7" if d17 < dph else "6(log phi)^2/pi^2"
    print(f"   VERDICT: the fit selects {pick}")
    print(f"   OUTCOME {'1/7 -- memo 176 section 5 needs its CONSTANT corrected' if d17 < dph else 'PHI -- the law stands; memo 174 1/7 was estimator bias'}")
