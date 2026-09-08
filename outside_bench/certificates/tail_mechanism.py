#!/usr/bin/env python3
"""WHY c_edge = 1: THE EDGE OF F_K IS THE INVERSE OF THE COLORED JONES TAIL.

Memo 177 section 5 established sup_{|p/r|<4} c_eff = c_edge = 1 for the figure-eight, by
identifying the k -> infinity limit of Xi_k's edge sequence as

     E(q) = 2 sum_{j>=0} q^{j(j+1)} / (q;q)_inf ,        c_eff(E) = 1,

and addendum 2 offered the mechanism as a guess: "which smells like Garoufalidis-Le stability
of the colored Jones tail".  It is not a guess.  It is checkable from the same equation the
whole pipeline started from.

GM eq (166):   J_n(4_1) = 1 + sum_{m=1}^{n-1} prod_{j=1}^{m} (q^n + q^-n - q^j - q^-j).

Reading each J_n UP from its lowest degree, the coefficient sequence STABILISES in n -- that is
Garoufalidis-Le stability for this alternating knot -- and the stable limit, the TAIL, is

     Phi_{4_1}(q) = (q;q)_inf                      (Armond-Dasbach; reproduced below)

exactly the reciprocal of the factor in E(q).  So:

     colored Jones tail      Phi_K   =  (q;q)_inf          c_eff( Phi_K )   = 0
     F_K block edge          E       =  2 theta / (q;q)_inf  c_eff( E )     = 1

F_K is an INVERSION of the Habiro/cyclotomic expansion (the "inverted Habiro series" of the
literature), so its stable head carries 1/Phi_K where the colored Jones tail carries Phi_K.

THE MECHANISM, STATED SO IT CAN BE WRONG:

     c_edge(K)  =  c_eff( 1 / Phi_K(q) ),   Phi_K = the colored Jones tail,

and therefore the ceiling on c_eff over all convergent surgeries on K is c_eff(1/Phi_K).
For 4_1, Phi = (q;q)_inf and the ceiling is 1.

WHAT THIS DOES TO MEMO 177's "UNIVERSAL CEILING" QUESTION -- it sharpens it AND it removes the
reason to expect the answer to be yes.  Tails of alternating links are NOT all (q;q)_inf: by
Armond-Dasbach the tail is that of the reduced all-A state graph, and richer graphs give higher
products and Andrews-Gordon-type series.  So the ceiling is a knot-by-knot quantity, and

     c_eff = 6 on this route requires a knot with c_eff(1/Phi_K) >= 6.

That is a QUESTION ABOUT COLORED JONES TAILS, a developed subject (Armond-Dasbach,
Garoufalidis-Le, Hajij), not about F_K -- which is a much cheaper question to answer than
"compute F_K for a second hyperbolic knot".  It is stated here, not answered.

Gate 5: exact integer Laurent arithmetic.
"""
import sys, os, io, math, contextlib

L = 220

def J(n):
    """eq (166), exact, as {exponent: coefficient}"""
    total = {0: 1}; cur = {0: 1}
    for m in range(1, n):
        fac = {n: 1, -n: 1}
        fac[m] = fac.get(m, 0) - 1
        fac[-m] = fac.get(-m, 0) - 1
        fac = {k: v for k, v in fac.items() if v}
        nxt = {}
        for e1, c1 in cur.items():
            for e2, c2 in fac.items():
                nxt[e1+e2] = nxt.get(e1+e2, 0) + c1*c2
        cur = {k: v for k, v in nxt.items() if v}
        for k, v in cur.items(): total[k] = total.get(k, 0) + v
    return {k: v for k, v in total.items() if v}

print("STABILITY OF THE COLORED JONES HEAD  (GM eq (166), computed exactly)")
print("-"*76)
heads = {}
for n in range(2, 17):
    d = J(n); lo = min(d)
    heads[n] = [d.get(lo+i, 0) for i in range(30)]
    if n >= 12: print(f"   n={n:<3} lowest q^{lo:<6} {heads[n][:15]}")
s = 0
a, b = heads[15], heads[16]
while s < len(a) and a[s] == b[s]: s += 1
print(f"\n   J_15 and J_16 heads agree in {s} coefficients (stability window grows with n)")

qq = [0]*(L+1); qq[0] = 1
for n in range(1, L+1):
    for i in range(L, n-1,-1): qq[i] -= qq[i-n]
inv = [0]*(L+1); inv[0] = 1
for n in range(1, L+1):
    for i in range(n, L+1): inv[i] += inv[i-n]
th = [0]*(L+1); j = 0
while j*(j+1) <= L: th[j*(j+1)] += 2; j += 1
edge = th[:]
for n in range(1, L+1):
    for i in range(n, L+1): edge[i] += edge[i-n]

print(f"\n   stable head       : {heads[16][:s]}")
print(f"   (q;q)_inf         : {qq[:s]}")
same = heads[16][:s] == qq[:s]
print(f"\n   TAIL OF 4_1 IS (q;q)_inf, over the whole stable window: {same}")
assert same

print("\nTHE TWO SEQUENCES SIDE BY SIDE")
print("-"*76)
print(f"   colored Jones tail   Phi   = (q;q)_inf          : {qq[:12]}")
print(f"   F_K block edge       E     = 2 theta/(q;q)_inf  : {edge[:12]}")
print(f"   1/(q;q)_inf (partitions)                        : {inv[:12]}")
# NOT a check of E against itself: compare 2 theta/(q;q)_inf against Xi_150's ACTUAL edge.
import io as _io, contextlib as _cl
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'xi_recursion_fast.py')).read()
_ns = {}; _sa = sys.argv; sys.argv = ['x', '150']
with _cl.redirect_stdout(_io.StringIO()):
    try: exec(compile(_src, 'xi_recursion_fast.py', 'exec'), _ns)
    except SystemExit: pass
sys.argv = _sa
E150 = _ns['block'](150)[1]; E140 = _ns['block'](140)[1]
m1 = next((i for i in range(min(len(E150), L+1)) if edge[i] != E150[i]), min(len(E150), L+1))
w  = next((i for i in range(min(len(E140), len(E150))) if E140[i] != E150[i]),
          min(len(E140), len(E150)))
print(f"\n   2 theta/(q;q)_inf vs Xi_150's ACTUAL edge sequence: agree to q^{m1-1}")
print(f"   Xi_140 vs Xi_150 edge sequences: agree to q^{w-1} (the window grows with k)")

def fit3(a, lo, hi):
    X = []; Y = []
    for n in range(lo, hi+1):
        if n > 1 and a[n] > 0: X.append((math.sqrt(n), math.log(n), 1.0)); Y.append(math.log(a[n]))
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
    return 3*s[0]*s[0]/(2*math.pi**2)

BIG = 40000
inv2 = [0]*(BIG+1); inv2[0] = 1
for n in range(1, BIG+1):
    for i in range(n, BIG+1): inv2[i] += inv2[i-n]
print(f"\n   c_eff(1/(q;q)_inf) on {BIG} terms = {fit3(inv2, BIG//2, BIG):.7f}  -> c_edge(4_1) = 1")

print("\nTHE MECHANISM, AND WHAT IT COSTS MEMO 177's UNIVERSALITY HOPE")
print("-"*76)
print("   c_edge(K) = c_eff( 1 / Phi_K ),  Phi_K the colored Jones tail;")
print("   so the ceiling on c_eff over all convergent surgeries on K is c_eff(1/Phi_K).")
print("   For 4_1: Phi = (q;q)_inf, ceiling 1.")
print("   Tails of alternating links are NOT all (q;q)_inf -- by Armond-Dasbach the tail is")
print("   that of the reduced all-A state graph, and richer graphs give higher products and")
print("   Andrews-Gordon-type series.  So THE CEILING IS KNOT-BY-KNOT, and memo 177's hope")
print("   that c_edge = 1 universally has no support beyond this one knot.")
print("   c_eff = 6 on this route needs a knot with c_eff(1/Phi_K) >= 6 -- A QUESTION ABOUT")
print("   COLORED JONES TAILS, which is a developed subject, and far cheaper to settle than")
print("   computing F_K for a second hyperbolic knot.  Stated here, not answered.")
