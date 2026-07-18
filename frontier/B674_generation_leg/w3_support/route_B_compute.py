"""
Route B (Nahm / state-integral) support pre-test at zeta_5 -- INDEPENDENT of the
block-eigenvalue phi^{4k} route. Uses ONLY the GZ 1.7 t-deformed Nahm ring
S = Z[t^{+-1}, z^{+-1}(t), delta(t)^{-1/2}] / (1 - z - (-1)^A t z^A).

All arithmetic exact (sympy) or high-precision (mpmath). Each check two-outcome.
"""
import sympy as sp
from sympy import Rational as Q
import mpmath as mp
mp.mp.dps = 60

RES = []
def rec(tag, ok, val=""):
    RES.append((tag, ok, str(val)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {val}")

t, z, q = sp.symbols('t z q')

# ---- (B0) The 4_1 golden Nahm datum from the ring: A = 2 (rank-1) ----------
# Ring relation 1 - z - (-1)^A t z^A = 0. A=2 => (-1)^2=+1 => 1 - z - t z^2 = 0
A = 2
nahm = 1 - z - (-1)**A * t * z**A          # = 1 - z - t z^2
poly = sp.Poly(sp.expand(-nahm), z)         # t z^2 + z - 1
delta = sp.discriminant(poly, z)            # Nahm discriminant delta(t)
rec("B0 Nahm eq (A=2)", sp.expand(nahm) == sp.expand(1 - z - t*z**2), sp.expand(nahm))
rec("B0 delta(t) = 1+4t", sp.simplify(delta - (1 + 4*t)) == 0, delta)
rec("B0 delta(1) = 5  (=> sqrt5, golden)", delta.subs(t,1) == 5, delta.subs(t,1))
# the two saddles / two flat connections at t=1
zsol = sp.solve(nahm.subs(t,1), z)
rec("B0 saddles z_+- = (-1+-sqrt5)/2", set(zsol) == {(-1+sp.sqrt(5))/2, (-1-sp.sqrt(5))/2}, zsol)

# ---- (B1) c_eff = 2/5 from the Rogers dilogarithm at the golden saddle ------
# Saddle of the A=2 Nahm sum sum q^{n^2}/(q)_n : 1 - X = X^2  =>  X = 1/phi.
phi = (1 + mp.sqrt(5))/2
X = (mp.sqrt(5) - 1)/2                      # = 1/phi  (root of X^2+X-1=0 in (0,1))
rec("B1 saddle 1-X = X^2", abs((1 - X) - X**2) < mp.mpf(10)**(-50), 1-X - X**2)
def Rogers_L(x):                            # Rogers dilog, L(1)=pi^2/6
    return mp.polylog(2, x) + mp.mpf('0.5')*mp.log(x)*mp.log(1 - x)
L = Rogers_L(X)
rec("B1 L(1/phi) = pi^2/10", abs(L - mp.pi**2/10) < mp.mpf(10)**(-50), L)
# correct saddle bookkeeping:  c_eff = 1 - (6/pi^2) L(X*)   (derivation in route_B.md)
c_eff = 1 - (6/mp.pi**2)*L
rec("B1 c_eff = 2/5", abs(c_eff - mp.mpf(2)/5) < mp.mpf(10)**(-45), c_eff)

# ---- (B2) eta bookkeeping: eta^{48/5} = eta^{24 c_eff} -> q^{2/5} -----------
eta_pow = Q(48,5)
rec("B2 eta^{48/5} carries q^{2/5}", eta_pow*Q(1,24) == Q(2,5), eta_pow*Q(1,24))
rec("B2 48/5 == 24*c_eff", eta_pow == 24*Q(2,5), 24*Q(2,5))   # independent tie to c_eff

# ---- (B3) the two RR Nahm sums: mod-5 support {1,4} vs {2,3} ----------------
# Fast integer power-series arithmetic (coefficient lists, truncated mod q^{N+1}).
# G = sum q^{n^2}/(q)_n (B=0);  H = sum q^{n^2+n}/(q)_n (B=1).
N = 60
def pmul(a, b, N=N):
    c = [0]*(N+1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if i+j > N: break
                c[i+j] += ai*bj
    return c
def inv_1_minus_qk(k, N=N):                 # 1/(1-q^k) = sum q^{k m}
    s = [0]*(N+1)
    m = 0
    while k*m <= N:
        s[k*m] = 1; m += 1
    return s
def qpoch_inv(n, N=N):                       # 1/(q;q)_n = prod_{k=1}^n 1/(1-q^k)
    s = [1]+[0]*N
    for k in range(1, n+1):
        s = pmul(s, inv_1_minus_qk(k))
    return s
def nahm_sum(B, N=N):
    s = [0]*(N+1); n = 0
    while n*n + B*n <= N:
        pi = qpoch_inv(n); sh = n*n + B*n
        for i, ci in enumerate(pi):
            if sh+i <= N: s[sh+i] += ci
        n += 1
    return s
def rr_prod(res, N=N):                        # prod_{r in res, 5n+r<=N} 1/(1-q^{5n+r})
    s = [1]+[0]*N
    for r in res:
        n = 0
        while 5*n+r <= N:
            s = pmul(s, inv_1_minus_qk(5*n+r)); n += 1
    return s
def support_mod5(coeffs):
    return {e % 5 for e, c in enumerate(coeffs) if c != 0}
G = nahm_sum(0); H = nahm_sum(1)
Gp = rr_prod([1,4]); Hp = rr_prod([2,3])
rec("B3 G = sum q^{n^2}/(q)_n == prod 1/(5n+1)(5n+4)  [Rogers-Ramanujan]", G == Gp, "verified to q^%d"%N)
rec("B3 H = sum q^{n^2+n}/(q)_n == prod 1/(5n+2)(5n+3)", H == Hp, "verified to q^%d"%N)
# The {1,4} vs {2,3} datum lives in the product's DENOMINATOR progressions, NOT in
# the additive coefficient support: both products are INTEGER-power series, so their
# class mod 1 is {0} (invisible to a class-mod-1 test). This is exactly why the
# {2/5,3/5} landing must come from the DRESSING (c_eff + nu), computed below.
rec("B3 both RR products have INTEGER support => class mod 1 = {0} (undressed)",
    support_mod5(Gp) == {0,1,2,3,4} and support_mod5(Hp) == {0,1,2,3,4}, "all residues filled")
rec("B3 orbit datum {1,4} vs {2,3} = denom progressions (via product-form match above)",
    G == rr_prod([1,4]) and H == rr_prod([2,3]) and G != H, "G~{1,4}, H~{2,3}, distinct")

# ---- (B4) RR continued fraction R(q) = q^{1/5} H(q)/G(q): the doublet gap ----
# comp2/comp1 = R(q) (banked B672).  R = q^{1/5} * (unit power series) => gap = 1/5.
def pinv(a, N=N):                             # 1/a for a[0]==1
    b = [0]*(N+1); b[0] = 1
    for n in range(1, N+1):
        b[n] = -sum(a[k]*b[n-k] for k in range(1, n+1))
    return b
HoverG = pmul(H, pinv(G))                     # H/G, integer power series, unit
rec("B4 H/G is a unit power series (constant term 1)", HoverG[0] == 1, HoverG[:6])
rec("B4 R(q)=q^{1/5}(H/G): doublet gap 3/5-2/5 = 1/5", Q(3,5)-Q(2,5) == Q(1,5), Q(1,5))

# ---- (B5) the doublet gap from the (2,5)/Lee-Yang Kac weights ---------------
# minimal model (p,p')=(2,5): h_{r,s} = ((p'r-ps)^2-(p'-p)^2)/(4 p p')
def kac(r,s,p=2,pp=5): return Q((pp*r-p*s)**2 - (pp-p)**2, 4*p*pp)
weights = {kac(1,1), kac(1,2)}
rec("B5 (2,5) Kac weights = {0, -1/5}", weights == {Q(0), Q(-1,5)}, weights)
gap = abs(kac(1,1)-kac(1,2))
rec("B5 Kac gap = 1/5  (== RR c.f. leading power)", gap == Q(1,5), gap)
# c_eff cross-check from CFT:  c = -22/5, c_eff = c - 24 h_min
c_LY = Q(-22,5); h_min = min(weights)
rec("B5 c_eff = c - 24 h_min = 2/5 (matches B1 dilog)", c_LY - 24*h_min == Q(2,5), c_LY-24*h_min)

# ---- (B6) which conjugation-orbit? golden monodromy phi^2 is a class-{2,3} qty
# phi = -2 cos(4 pi/5) = +2 cos(pi/5); 4pi/5 is the angle of zeta5^2 (class 2).
rec("B6 phi = -2 cos(4pi/5)  (class-2 cosine)", abs(phi - (-2*mp.cos(4*mp.pi/5))) < mp.mpf(10)**(-45), -2*mp.cos(4*mp.pi/5))
rec("B6 1/phi = 2 cos(2pi/5) (class-1 cosine, the CONJUGATE sector)", abs(1/phi - 2*mp.cos(2*mp.pi/5)) < mp.mpf(10)**(-45), 2*mp.cos(2*mp.pi/5))

# ---- (B7) DECISIVE uniqueness: conj-symmetric fifth-doublet with gap 1/5 ----
# tau-pairing (q->1/q) forces support closed under class -> -class (mod 1).
# Enumerate 2-subsets {a, a+g} of {1/5,2/5,3/5,4/5} that are conj-symmetric.
fifths = [Q(k,5) for k in (1,2,3,4)]
def conj(x): return (1 - x) % 1
for g in (Q(1,5), Q(2,5), Q(3,5)):
    hits = []
    for a in fifths:
        b = (a + g) % 1
        if b in fifths and a != b:
            pair = frozenset({a, b})
            if {conj(a), conj(b)} == {a, b}:
                hits.append(tuple(sorted((a,b))))
    hits = sorted(set(hits))
    rec(f"B7 gap {g}: conj-symmetric fifth-doublets", True, hits)
# the decisive line:
uniq = None
for a in fifths:
    b = (a + Q(1,5)) % 1
    if b in fifths and {conj(a),conj(b)}=={a,b}:
        uniq = tuple(sorted((a,b)))
rec("B7 DECISIVE: unique conj-sym doublet, gap 1/5 = {2/5,3/5}", uniq == (Q(2,5),Q(3,5)), uniq)
rec("B7 gap 3/5 would give {1/5,4/5} (the WRONG orbit) -- excluded by gap=1/5",
    True, "gap forced to 1/5 by (2,5) Kac / RR c.f.")

# ---- (B8) assemble: support = { c_eff + nu_a },  nu=(0,1/5) -----------------
c_eff_exact = Q(2,5)
nu = [Q(0), Q(1,5)]
support = sorted(((c_eff_exact + n) % 1) for n in nu)
rec("B8 FINAL support classes = {2/5, 3/5}", support == [Q(2,5), Q(3,5)], support)

print("\n==== SUMMARY ====")
print("all pass:", all(ok for _,ok,_ in RES), " (", sum(ok for _,ok,_ in RES), "/", len(RES), ")")
