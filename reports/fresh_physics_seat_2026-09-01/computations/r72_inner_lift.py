"""R72 (part 1) -- the inner lift, and the count on n fixed lines.

The manifold's symmetry g acts on the SL(2) local system by Ad(N), N in SL(2,C) normalising the holonomy.  On the E6
local system (principal embedding iota: SL2 -> E6) it lifts to Ad(iota(N)) [INNER] or to Ad(iota(N)) o theta_D
[OUTER], because the diagram automorphism theta_D commutes with the principal SL2 (B353 (B)).  Facts checked here:

 (a) For the involution (N = diag(i,-i) up to conjugacy): iota(N) = exp(pi i rho^vee) acts on the root alpha by
     (-1)^{ht alpha}; fixed roots 32, fixed algebra dim 38 = A5 + A1.  Its fixed Cartan is ALL of h: every u is even.
 (b) For an order-3 symmetry (N elliptic, rotation 2 pi/3): iota(N) = exp(2 pi i rho^vee / 3) acts by e^{2 pi i ht/3};
     fixed roots 18, fixed algebra dim 24 = A2 + A2 + A2.  Again the whole Cartan is fixed.  An order-3 symmetry has
     no consistent outer lift (Out(E6) = Z/2 and Z/3 -> Z/2 is trivial), so the inner lift is forced.
 (c) With a trivial twist, R69's count on n fixed lines with equal signs gives, for every direction u in h,
        S_n(u) = n (+)_{q>0} 27_q  (+)  n (+)_{q<0} conj(27_q)     (up to overall conjugation)
     Scan of all u = sum c_k omega_k^vee with small integer c_k: which are chiral under C(u)' AND free of SU(N>=3)
     cubic anomalies, with the C(u)'-content of S_1(u).  In particular omega_1^vee: 16 + 10 + 1 of D5 (SO(10)).
"""
import itertools, collections
from fractions import Fraction as Fr
import sympy as sp
import io, contextlib
_src = open('r71_theta_even_pairing.py').read().split('print("\\n== all other theta-even directions')[0]
with contextlib.redirect_stdout(io.StringIO()): exec(_src)      # E6 data, analyse(), decompose(), factors(), cubic_anomaly()
# --- (a), (b): heights
ht = {a: sum(RC[a]) for a in ROOTS}
fixed_inv = [a for a in ROOTS if ht[a] % 2 == 0]; fixed_3 = [a for a in ROOTS if ht[a] % 3 == 0]
print(f"(a) Ad(exp(pi i rho^vee)): fixed roots {len(fixed_inv)} -> fixed algebra dim {6 + len(fixed_inv)} (A5+A1 = 35+3 = 38)")
print(f"(b) Ad(exp(2 pi i rho^vee/3)): fixed roots {len(fixed_3)} -> fixed algebra dim {6 + len(fixed_3)} (A2^3 = 24)")
assert len(fixed_inv) == 32 and len(fixed_3) == 18
# root systems of the fixed algebras: check simple-root types by the Cartan matrices of the positive fixed roots
def fac_types(cu):
    pos_, simple_ = cu_simple(cu); return sorted(t for t, _ in factors(simple_))
print("    types:", fac_types(fixed_inv), fac_types(fixed_3))
assert fac_types(fixed_inv) == ['A1', 'A5'] and fac_types(fixed_3) == ['A2', 'A2', 'A2']
print("    the fixed Cartan of either is all of h (the elements lie in the torus): every direction u is 'even'.")

# --- (c): the untwisted count, all directions
def content(c):
    c = tuple(Fr(x) for x in c)
    q = {l: dot(c, RC27[l]) for l in W27}
    S = []
    for l in W27:
        if q[l] > 0: S.append(l)
        elif q[l] < 0: S.append(neg(l))
    cu = [a for a in ROOTS if dot(c, RC[a]) == 0]
    pos_, simple_ = cu_simple(cu); fac = factors(simple_)
    simple, out, chiral = decompose(c, S)
    anom = {f"{t}": cubic_anomaly(S, simple_, (t, ch)) for t, ch in fac}
    return S, cu, fac, out, chiral, anom
seen = set(); rows = []
for c in itertools.product([-1, 0, 1, 2], repeat=6):
    if all(x == 0 for x in c): continue
    g = 0
    for x in c: g = sp.gcd(g, x)
    cn = tuple(x // g for x in c)
    if cn in seen or neg(cn) in seen: continue
    seen.add(cn)
    S, cu, fac, out, chiral, anom = content(cn)
    typ = '+'.join(sorted(t for t, _ in fac)) or '-'
    rows.append((cn, typ, len(cu), bool(chiral), any(v != 0 for v in anom.values()), out, chiral))
byT = collections.defaultdict(list)
for r in rows: byT[(r[1], r[2])].append(r)
print(f"\n(c) untwisted count S_1(u) = (+)_{{q>0}} 27_q (+) (+)_{{q<0}} conj(27_q), all directions with coefficients in {{-1,0,1,2}} ({len(rows)} up to scale/sign):")
print(f"{'C(u)prime':16} {'roots':6} {'#dirs':6} {'vector-like':12} {'chiral+anomalous':17} {'chiral+anomaly-free'}")
for key in sorted(byT, key=lambda k: (-k[1], k[0])):
    L = byT[key]
    nvl = sum(1 for r in L if not r[3]); nca = sum(1 for r in L if r[3] and r[4]); ncf = sum(1 for r in L if r[3] and not r[4])
    print(f"{key[0]:16} {key[1]:<6} {len(L):<6} {nvl:<12} {nca:<17} {ncf}")
free = [r for r in rows if r[3] and not r[4]]
print(f"\nchiral AND anomaly-free directions: {len(free)}; by centralizer type: {collections.Counter(r[1] for r in free)}")
# show the content for the fundamental coweights and for the anomaly-free ones with the largest centralizers
def fmt(out): return " + ".join(f"{m} x {d}{lab}" for (lab, d), m in sorted(out.items(), key=lambda kv: -kv[0][1]))
print("\nfundamental coweights (n = 1 copy shown; n fixed lines give n copies):")
for k in range(6):
    c = tuple(1 if i == k else 0 for i in range(6))
    S, cu, fac, out, chiral, anom = content(c)
    print(f"  omega_{k+1}^vee: C(u)' = {'+'.join(t for t, _ in fac)} ({len(cu)} roots); S_1 = {fmt(out)}; chiral: {bool(chiral)}; anomalies {dict((k_, str(v)) for k_, v in anom.items())}")
print("\nanomaly-free chiral directions, largest centralizers first:")
for r in sorted(free, key=lambda r: -r[2])[:12]:
    print(f"  u = {r[0]}: C(u)' = {r[1]} ({r[2]} roots); S_1 = {fmt(r[5])}; chiral part {fmt(r[6]) if r[6] else 0}")
print("\none example per anomaly-free chiral centralizer type (smallest |c| first):")
for typ in sorted({r[1] for r in free}):
    r = min((r for r in free if r[1] == typ), key=lambda r: (sum(abs(x) for x in r[0]), r[0]))
    print(f"  {typ:10} u = {r[0]}: S_1 = {fmt(r[5])};  chiral part = {fmt(r[6])}")
print("\nSELFTEST: PASS")
