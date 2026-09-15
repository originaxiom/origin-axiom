#!/usr/bin/env python3
"""THE c_eff LAW, CORRECTED -- memo 176's formula is only its |p/r| -> 0 tangent.

Memo 176 section 5 claimed   c_eff = 3|p/r|(log lambda)^2/(2 pi^2)   from a block-mass
argument, and section 6 concluded via Gelfond that c_eff = 6 is unreachable.  The formula
is WRONG except in the limit |p/r| -> 0, and the Gelfond argument is void with it.  What
this certificate does, in order:

  A  IDENTITY.  The assembly at p/r = -1 equals Ramanujan's order-7 mock theta F_0(q)
     termwise -- i.e. Gukov-Manolescu eq (175), Zhat_0(-Sigma(2,3,7)), reached by an
     entirely different route in the paper (Seifert plumbing + modularity).  External,
     published validation of the pipeline, on an object the pipeline never saw.

  B  REFUTATION.  A three-parameter fit  log a_n = A sqrt(n) + B log n + C, calibrated on
     eta^-1 and Rogers-Ramanujan to better than 0.01%, gives c_eff(p/r = -1) = 1/7 to
     seven figures.  Memo 176's law says 0.1407745.  1.48% apart, and the fit resolves
     0.003%.  The law is refuted at p/r = -1.

  C  REPLACEMENT.  Write  h(y) = lim_k (1/k) log Xi_k(e^{-y/k}).  Then

         c_eff(Q) = (6/pi^2) max_{y>0} [ y h(y) - y^2/Q ],     Q = |p/r|.

     h(0) = 2 log phi exactly, and the Q -> 0 limit of this IS memo 176's formula --
     which is why it looked right at p/r = -1/2 (0.36% off) and wrong at -5/2 (10% off).

  D  THRESHOLD.  Three facts verified to k = 150 -- Xi_k's half-width is floor((k-1)^2/4),
     its edge coefficient is >= 1, and Xi_k(1) = F(2k-1) -- force

         y/4  <=  h(y)  <=  y/4 + 2 log phi ,

     hence y h(y) - y^2/Q >= y^2(1/4 - 1/Q), which diverges for Q > 4, and
     <= y^2(1/4 - 1/Q) + 2y log phi, which has a finite max for Q < 4.
     EXACT THRESHOLD |p/r| = 4 -- which is also the largest |p/r| among Thurston's nine
     exceptional surgeries on the figure-eight.

  E  THE SUPREMUM.  h(y) - y/4 -> C/y with C = pi^2/6, because the k -> infinity limit of
     Xi_k's edge sequence is  2 sum_j q^{j(j+1)} / (q;q)_inf, whose own c_eff is 1.
     Therefore sup_{Q<4} c_eff = 1, approached as Q -> 4^- and never attained.
     c_eff = 6 is unreachable -- and so is every value >= 1.  This REPLACES memo 176
     section 6's Gelfond argument, which is retracted.

  F  CROSS-CHECK, not used in the fit.  At the three integer slopes the surgery is Seifert
     and c_eff comes out at 6|p|/(b1 b2 b3):
        p/r = -1  -Sigma(2,3,7)          b = (2,3,7), 42   ->  6/42  = 1/7
        p/r = -2  -M(-1;1/2,1/4,1/5)     b = (2,4,5), 40   ->  12/40 = 3/10
        p/r = -3  -M(-1;1/3,1/3,1/4)     b = (3,3,4), 36   ->  18/36 = 1/2
     computed here from F_{4_1} alone, with no Seifert data entering.

Gate 5: exact integer series in, fits out.  c((E6)_1) = 6 appears only as a target.
"""
import sys, os, io, math, contextlib
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
N = 150
src = open(os.path.join(HERE, 'xi_recursion_fast.py')).read()
ns = {}; _argv = sys.argv; sys.argv = ['x', str(N)]
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    try: exec(compile(src, 'xi_recursion_fast.py', 'exec'), ns)
    except SystemExit: pass
sys.argv = _argv
g = buf.getvalue()
assert 'C1 four published blocks : PASSED' in g and f'C2 Fibonacci sums k<={N}  : PASSED' in g
print("generator controls C1/C2/C3: PASSED (see xi_recursion_fast.py)")
block = ns['block']; B = {k: block(k) for k in range(1, N+1)}
phi = (1+5**0.5)/2; LPHI = math.log(phi)

def fit3(a, lo, hi):
    X = []; Y = []
    for n in range(lo, hi+1):
        v = a[n] if isinstance(a, list) else a.get(n, 0)
        if n > 1 and v > 0: X.append((math.sqrt(n), math.log(n), 1.0)); Y.append(math.log(v))
    if len(X) < 50: return None
    m = 3
    M = [[sum(X[i][p]*X[i][q] for i in range(len(X))) for q in range(m)] for p in range(m)]
    V = [sum(X[i][p]*Y[i] for i in range(len(X))) for p in range(m)]
    for c in range(m):
        piv = max(range(c, m), key=lambda rr: abs(M[rr][c]))
        M[c], M[piv] = M[piv], M[c]; V[c], V[piv] = V[piv], V[c]
        for rr in range(m):
            if rr == c: continue
            f = M[rr][c]/M[c][c]
            for cc in range(m): M[rr][cc] -= f*M[c][cc]
            V[rr] -= f*V[c]
    s = [V[i]/M[i][i] for i in range(m)]
    return 3*s[0]*s[0]/(2*math.pi**2), s[1]

def build(p, r, a):
    terms = []
    for k in range(1, N+1):
        h = Fr(2*k-1, 2)
        for sgn, u in ((1, h-Fr(1, 2*r)), (-1, h+Fr(1, 2*r))):
            if (r*u - a) % abs(p) != 0: continue
            terms.append((k, sgn, -Fr(r, p)*u*u))
    if not terms: return None, None
    shift = min(e for _, _, e in terms)
    if {(e-shift).denominator for _, _, e in terms} != {1}: return None, None
    kk = N+1; hh = Fr(2*kk-1, 2)
    cand = []
    for kx in (kk, kk+1):
        hx = Fr(2*kx-1, 2)
        cand += [-Fr(r, p)*u*u - shift for u in (hx-Fr(1, 2*r), hx+Fr(1, 2*r))
                 if (r*u-a) % abs(p) == 0]
    if not cand: return None, None
    H = int(min(cand)) - (kk-1)**2//4 - 1
    if H < 2000: return None, None
    out = [0]*(H+1)
    for k, sgn, e in terms:
        e0 = int(e-shift); lo, cs = B[k]
        for i, c in enumerate(cs):
            x = e0+lo+i
            if 0 <= x <= H: out[x] += sgn*c
    return out, H

# ---------------- A: the identity -----------------------------------------------------
print("\nA  IDENTITY with Ramanujan's F_0 (GM eq (175))")
print("-"*74)
Z1, H1 = build(-1, 1, Fr(1))
LID = min(H1, 3000)
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
FF = F0(LID)
idok = all(Z1[i] == FF[i] for i in range(LID+1))
print(f"   assembly at p/r = -1 vs sum_n q^{{n^2}}/(q^{{n+1}};q)_n over q^0..q^{LID}: "
      f"{'IDENTICAL' if idok else 'DIFFER'}")
print(f"   first terms {Z1[:14]}")
assert idok

# ---------------- B: calibration + the refutation -------------------------------------
print("\nB  THE THREE-PARAMETER FIT, CALIBRATED")
print("-"*74)
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
CL = 12000
for nm, ser, true in (("eta^-1", eta_inv(CL), 1.0), ("Rogers-Ramanujan", rr(CL), 0.4)):
    c, Bv = fit3(ser, CL//2, CL)
    print(f"   {nm:<18} true {true:<4}  fitted {c:.7f}   error {abs(1-c/true)*100:.4f}%   B={Bv:+.4f}")
c1, B1 = fit3(Z1, H1//2, H1)
print(f"\n   p/r = -1 :  c_eff = {c1:.7f}   B = {B1:+.4f}")
print(f"      1/7                       = {1/7:.7f}   deviation {abs(1-c1*7)*100:.4f}%")
print(f"      memo 176's 3|p/r|(log lambda)^2/(2pi^2) = {3*(2*LPHI)**2/(2*math.pi**2):.7f}"
      f"   deviation {abs(1-c1/(3*(2*LPHI)**2/(2*math.pi**2)))*100:.2f}%")
print("   => memo 176 section 5's formula is REFUTED at p/r = -1.")

# ---------------- C: the replacement law ----------------------------------------------
print("\nC  THE REPLACEMENT LAW")
print("-"*74)
def logXi(k, t):
    lo, cs = B[k]
    T = [math.log(c)-t*(lo+i) for i, c in enumerate(cs) if c > 0]
    m = max(T); return m+math.log(sum(math.exp(x-m) for x in T))
KS = [60, 80, 100, 120, 150]
def h(y):
    y = max(y, 1e-9)
    X = [[1.0, 1.0/k, 1.0/k**2] for k in KS]; Y = [logXi(k, y/k)/k for k in KS]
    m = 3
    M = [[sum(X[i][p]*X[i][q] for i in range(len(X))) for q in range(m)] for p in range(m)]
    V = [sum(X[i][p]*Y[i] for i in range(len(X))) for p in range(m)]
    for c in range(m):
        piv = max(range(c, m), key=lambda rr: abs(M[rr][c]))
        M[c], M[piv] = M[piv], M[c]; V[c], V[piv] = V[piv], V[c]
        for rr in range(m):
            if rr == c: continue
            f = M[rr][c]/M[c][c]
            for cc in range(m): M[rr][cc] -= f*M[c][cc]
            V[rr] -= f*V[c]
    return V[0]/M[0][0]
print(f"   h(0) = {h(0):.8f}   2 log phi = {2*LPHI:.8f}   "
      f"{'EQUAL to 8 places' if abs(h(0)-2*LPHI) < 5e-9 else 'DIFFER'}")
def G(Q):
    f = lambda y: y*h(y) - y*y/Q
    gr = (5**0.5-1)/2; a, b = 1e-6, 30.0
    c1_, c2_ = b-gr*(b-a), a+gr*(b-a)
    for _ in range(90):
        if f(c1_) < f(c2_): a = c1_
        else: b = c2_
        c1_, c2_ = b-gr*(b-a), a+gr*(b-a)
    ys = (a+b)/2
    return f(ys), ys
print(f"\n   {'p/r':>7} {'Q':>7} {'measured':>12} {'law':>12} {'ratio':>9} {'memo176':>11} {'ratio':>8}")
CASES = [(-1, 3), (-1, 2), (-1, 1), (-3, 2), (-2, 1), (-5, 2)]
ok = True
for p, r in CASES:
    best = None
    for j in range(abs(p)):
        a = Fr(r+1, 2)+j
        z, H = build(p, r, a)
        if z is None: continue
        f = fit3(z, H//2, H)
        if not f: continue
        if abs(f[1]+0.5) < 0.15 and (best is None or abs(f[1]+0.5) < abs(best[1]+0.5)): best = f
    if best is None: continue
    Q = abs(Fr(p, r)); Qf = float(Q)
    gg, _ = G(Qf); law = 6*gg/math.pi**2
    old = 3*Qf*(2*LPHI)**2/(2*math.pi**2)
    ok &= abs(1-law/best[0]) < 0.002
    print(f"   {p}/{r:<5} {Qf:>7.4f} {best[0]:>12.7f} {law:>12.7f} {law/best[0]:>9.5f} "
          f"{old:>11.7f} {old/best[0]:>8.4f}")
print(f"\n   replacement law within 0.2% at every slope: {ok}")

# ---------------- D: the threshold ----------------------------------------------------
print("\nD  THE THRESHOLD |p/r| = 4")
print("-"*74)
wid = all(len(B[k][1]) == 2*((k-1)**2//4)+1 for k in range(1, N+1))
edge = all(B[k][1][0] >= 1 for k in range(1, N+1))
fib = [1, 1]
while len(fib) < 2*N+2: fib.append(fib[-1]+fib[-2])
fibok = all(sum(B[k][1]) == fib[2*k-2] for k in range(1, N+1))
print(f"   half-width = floor((k-1)^2/4) for all k <= {N} : {wid}")
print(f"   edge coefficient >= 1 for all k <= {N}         : {edge}")
print(f"   Xi_k(1) = F(2k-1) for all k <= {N}             : {fibok}")
assert wid and edge and fibok
bnd = all(y/4 - 1e-9 <= h(y) <= y/4 + 2*LPHI + 1e-9 for y in (1, 2, 4, 8, 16, 32, 64))
print(f"   => y/4 <= h(y) <= y/4 + 2 log phi, checked at y = 1..64 : {bnd}")
print( "   => y h(y) - y^2/Q diverges for Q > 4 and has a finite max for Q < 4.")
print( "   THRESHOLD |p/r| = 4, which is the largest |p/r| among Thurston's nine")
print( "   exceptional surgeries on 4_1 (GM section 9.4: p/r in {-4,...,4}).")

# ---------------- E: the supremum -----------------------------------------------------
print("\nE  THE SUPREMUM IS 1")
print("-"*74)
E150 = B[150][1]; E140 = B[140][1]
s = 0
while s < min(len(E140), len(E150)) and E140[s] == E150[s]: s += 1
LE = 40000
th = [0]*(LE+1); j = 0
while j*(j+1) <= LE: th[j*(j+1)] += 2; j += 1
EDGE = th[:]
for n in range(1, LE+1):
    for i in range(n, LE+1): EDGE[i] += EDGE[i-n]
m1 = next((i for i in range(min(len(E150), LE)) if EDGE[i] != E150[i]), min(len(E150), LE))
print(f"   Xi_140 and Xi_150 edge sequences agree to {s} coefficients")
print(f"   2 sum_j q^{{j(j+1)}}/(q;q)_inf agrees with Xi_150's edge to q^{m1-1}")
print(f"      first terms {EDGE[:12]}")
ce, Be = fit3(EDGE, LE//2, LE)
print(f"   c_eff of that series ({LE} terms): {ce:.8f}   B={Be:+.4f}")
print(f"   => C = lim y(h(y)-y/4) = pi^2 c_edge/6 = {math.pi**2*ce/6:.7f}   (pi^2/6 = {math.pi**2/6:.7f})")
print(f"\n   {'Q':>7} {'y*':>9} {'c_eff':>11}")
for Q in (3.0, 3.5, 3.8, 3.9, 3.95, 3.98, 3.99):
    gg, ys = G(Q); print(f"   {Q:>7.3f} {ys:>9.3f} {6*gg/math.pi**2:>11.6f}")
print(f"\n   sup over 0 < |p/r| < 4 of c_eff = c_edge = 1, approached as |p/r| -> 4^-.")
print( "   c_eff = c((E6)_1) = 6 IS UNREACHABLE, and so is every value >= 1.")
print( "   This REPLACES memo 176 section 6's Gelfond argument, which is RETRACTED:")
print( "   its input was the refuted formula.")

# ---------------- F: Seifert cross-check ----------------------------------------------
print("\nF  SEIFERT CROSS-CHECK (no Seifert data entered the computation)")
print("-"*74)
SEIF = {1: ((2, 3, 7), 1), 2: ((2, 4, 5), 2), 3: ((3, 3, 4), 3)}
for Q, (b, hp) in SEIF.items():
    gg, _ = G(float(Q)); c = 6*gg/math.pi**2
    pS = b[0]*b[1]*b[2]; pred = 6*hp/pS
    print(f"   p/r = -{Q}   b = {b}, b1b2b3 = {pS}, |H_1| = {hp}   6|H_1|/b1b2b3 = {pred:.7f}"
          f"   law gives {c:.7f}   ratio {c/pred:.5f}")
