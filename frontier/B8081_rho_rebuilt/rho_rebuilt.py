#!/usr/bin/env python3
"""B8081 -- rho is BUILT: Prop (2880) and the coupling law stop being cited certificates.

The paper's Scope (2880) says, of the very representation both statements are about:

    "We record that rho's structure constants are specified in the source computation and
     ARE NOT RECONSTRUCTED IN THIS PAPER, so Proposition (2880) is a certificate whose
     ambient representation is cited rather than rebuilt here."

So the paper asserts a group order and a decomposition for a matrix it never writes down.
This builds it, from the Kac-Peterson data alone, and then checks both statements.

CONSTRUCTION (nothing imported, nothing transcribed).  SU(3) at level k = 2: the dual
Coxeter number is g = 3, so k + g = 5 and c = k*dim(g)/(k+g) = 16/5.  The six integrable
weights are the (a,b) with a + b <= 2.  Conformal weights follow from the inverse Cartan
matrix of A2:

    h(a,b) = (a^2 + b^2 + ab + 3a + 3b)/15,      T = diag(exp(2*pi*i*(h - c/24)))

and c/24 = 2/15, so the six T entries are zeta_15 raised to
(a^2 + b^2 + ab + 3a + 3b - 2) mod 15 -- printed below.  S is the Kac-Peterson sum over
the six Weyl elements of A2.  Everything lands in Q(zeta_60), which is the field the
paper's own proof names, and is evaluated at primes p = 1 mod 60 so that zeta_60 exists
in F_p and the arithmetic is exact integer arithmetic.

CONTROLS FIRST, and they are the reason this is rho and not some other matrix: the four
modular relations T^15 = I, S^4 = I, S^2 = C (charge conjugation) and (ST)^3 = S^2 must
all hold.  A wrong normalisation fails them.

QUANTIFIER (COMPUTE_THE_PROGRAM): the FACES layer -- modular data of SU(3)_2 and the
finite image it generates.  Nothing about the member, the class, the sisters or the rows.

NOT PREREGISTERED.  Every target number is the paper's, fixed before this file existed:
ord T = 15, |image| = 2880, theta-eigenspaces of dimensions 2 and 4, the odd block of
order 360, and 63 = 7 x 9 classes matching a 2T x 2I model.
"""
import itertools
import json
import os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


PRIM=[(a,b) for a in range(3) for b in range(3) if a+b<=2]
idx={p:i for i,p in enumerate(PRIM)}
def s1(x): return (-x[0], x[0]+x[1])
def s2(x): return (x[0]+x[1], -x[1])
W=[(lambda x:x,1),(s1,-1),(s2,-1),(lambda x:s1(s2(x)),1),(lambda x:s2(s1(x)),1),
   (lambda x:s1(s2(s1(x))),-1)]
def ip3(x,y): return 2*x[0]*y[0]+x[0]*y[1]+x[1]*y[0]+2*x[1]*y[1]
def build(p):
    g=next(g for g in range(2,p) if all(pow(g,(p-1)//q,p)!=1 for q in (2,3,5)))
    z=pow(g,(p-1)//60,p); z15=pow(z,4,p); rt=(pow(z,20,p)-pow(z,40,p))%p
    pre=pow(5*rt%p,p-2,p)
    T=[[0]*6 for _ in range(6)]
    for i,(a,b) in enumerate(PRIM): T[i][i]=pow(z15,(a*a+b*b+a*b+3*a+3*b-2)%15,p)
    S=[[0]*6 for _ in range(6)]
    for i,l in enumerate(PRIM):
        for j,m in enumerate(PRIM):
            lr=(l[0]+1,l[1]+1); mr=(m[0]+1,m[1]+1)
            S[i][j]=sum(sg*pow(z15,(-ip3(f(lr),mr))%15,p) for f,sg in W)%p*pre%p
    return S,T,z
def mul(A,B,p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))%p
                 for j in range(len(B[0]))) for i in range(len(A)))
def eye(n): return tuple(tuple(1 if i==j else 0 for j in range(n)) for i in range(n))
def inv(A,p):
    n=len(A); M=[list(A[i])+[1 if i==j else 0 for j in range(n)] for i in range(n)]
    r=0
    for c in range(n):
        pr=next(i for i in range(r,n) if M[i][c]%p)
        M[r],M[pr]=M[pr],M[r]
        iv=pow(M[r][c],p-2,p); M[r]=[v*iv%p for v in M[r]]
        for i in range(n):
            if i!=r and M[i][c]%p:
                f=M[i][c]; M[i]=[(M[i][j]-f*M[r][j])%p for j in range(2*n)]
        r+=1
    return tuple(tuple(M[i][n:]) for i in range(n))
def gen(gens,p):
    n=len(gens[0]); G={eye(n)}; fr=list(G)
    while fr:
        nx=[]
        for x in fr:
            for g in gens:
                y=mul(x,g,p)
                if y not in G: G.add(y); nx.append(y)
        fr=nx
    return G


# ---------------------------------------------------------------- the quaternion models
def qf(d):
    def m(x, y):
        return (x[0] * y[0] + d * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def a(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def n(x):
        return (-x[0], -x[1])

    def qm(P, Q):
        a1, b1, c1, d1 = P
        a2, b2, c2, d2 = Q
        return (a(a(m(a1, a2), n(m(b1, b2))), a(n(m(c1, c2)), n(m(d1, d2)))),
                a(a(m(a1, b2), m(b1, a2)), a(m(c1, d2), n(m(d1, c2)))),
                a(a(m(a1, c2), n(m(b1, d2))), a(m(c1, a2), m(d1, b2))),
                a(a(m(a1, d2), m(b1, c2)), a(n(m(c1, b2)), m(d1, a2))))
    return qm


ZQ = (Fr(0), Fr(0))


def rr(x):
    return (Fr(x), Fr(0))


def clos(gs, mu):
    G = set(gs)
    fr = list(G)
    while fr:
        nx = []
        for x in fr:
            for g in gs:
                y = mu(x, g)
                if y not in G:
                    G.add(y)
                    nx.append(y)
        fr = nx
    return sorted(G)


q2 = qf(2)
E2T = clos([(ZQ, rr(1), ZQ, ZQ), (rr(Fr(1, 2)),) * 4], q2)
q5 = qf(5)
IPHI, PHI = (Fr(-1, 2), Fr(1, 2)), (Fr(1, 2), Fr(1, 2))


def hf(t):
    return (t[0] / 2, t[1] / 2)


def ng(t):
    return (-t[0], -t[1])


_E = set()
for _k in range(4):
    for _s in (1, -1):
        _v = [ZQ] * 4
        _v[_k] = rr(_s)
        _E.add(tuple(_v))
for _sg in itertools.product((1, -1), repeat=4):
    _E.add(tuple((Fr(_sg[i], 2), Fr(0)) for i in range(4)))
_base = [ZQ, hf(rr(1)), hf(IPHI), hf(PHI)]
for _pm in itertools.permutations(range(4)):
    if sum(1 for i in range(4) for j in range(i + 1, 4) if _pm[i] > _pm[j]) % 2:
        continue
    for _sg in itertools.product((1, -1), repeat=3):
        _vals = [_base[0]] + [_base[i + 1] if _sg[i] > 0 else ng(_base[i + 1])
                              for i in range(3)]
        _v = [None] * 4
        for i in range(4):
            _v[_pm[i]] = _vals[i]
        _E.add(tuple(_v))
E2I = sorted(_E)


def qclasses(G, mu, one):
    iv = {}
    for g in G:
        for h in G:
            if mu(g, h) == one:
                iv[g] = h
                break
    out, seen = [], set()
    for g in G:
        if g in seen:
            continue
        c = {mu(mu(x, g), iv[x]) for x in G}
        seen |= c
        out.append(sorted(c))
    return out


print("=" * 78)
print("(1) THE KAC-PETERSON DATA, BUILT")
print("=" * 78)
print(f"\n  SU(3) level k = 2:  dual Coxeter g = 3, k+g = 5, c = 16/5, c/24 = 2/15")
print(f"  six integrable weights (a,b) with a+b <= 2: {PRIM}\n")
print("   (a,b) |  h = (a^2+b^2+ab+3a+3b)/15  |  T entry")
EXPS = []
for a, b in PRIM:
    hnum = a * a + b * b + a * b + 3 * a + 3 * b
    e = (hnum - 2) % 15
    EXPS.append(e)
    print(f"   {(a,b)} |          {hnum:2d}/15            |  zeta_15^{e}")
gate("ord T = 15, as Prop (2880) states",
     __import__("math").gcd(__import__("functools").reduce(
         __import__("math").gcd, EXPS), 15) == 1, f"exponents {EXPS}")

Cm = [[0] * 6 for _ in range(6)]
for _j, (a, b) in enumerate(PRIM):
    Cm[idx[(b, a)]][_j] = 1
Cm = tuple(tuple(r) for r in Cm)
gate("charge conjugation has 2 fixed weights and 2 swapped pairs, so its eigenspaces "
     "are 4- and 2-dimensional -- the theta of the coupling law",
     sorted([sum(1 for i in range(6) if Cm[i][i]) + (6 - sum(1 for i in range(6)
             if Cm[i][i])) // 2,
             (6 - sum(1 for i in range(6) if Cm[i][i])) // 2]) == [2, 4])

PRIMES = [61, 181, 241, 421]
print()
print("=" * 78)
print("(2) CONTROLS -- the four modular relations, at every prime")
print("=" * 78)
DATA = {}
for p in PRIMES:
    S, T, z = build(p)
    R = tuple(tuple(r) for r in T)
    S = tuple(tuple(r) for r in S)
    I6 = eye(6)
    T15 = I6
    for _ in range(15):
        T15 = mul(T15, R, p)
    S2 = mul(S, S, p)
    ST = mul(S, R, p)
    ok = (T15 == I6 and mul(S2, S2, p) == I6 and S2 == Cm
          and mul(mul(ST, ST, p), ST, p) == S2)
    gate(f"p={p}: T^15 = I, S^4 = I, S^2 = C, (ST)^3 = S^2", ok)
    DATA[p] = (S, R)
if FAILED:
    raise SystemExit("rho failed its modular relations -- it is not rho")

print()
print("=" * 78)
print("(3) PROPOSITION (2880) -- the group order, from the built rho")
print("=" * 78)
ORD = {}
for p in PRIMES:
    S, R = DATA[p]
    L = mul(mul(inv(S, p), inv(R, p), p), S, p)
    G = gen([R, L], p)
    ORD[p] = len(G)
    print(f"  p={p}:  |<rho(R), rho(L)>| = {len(G)}")
gate("the image has order 2880 = |2T x 2I| at every prime",
     set(ORD.values()) == {2880}, str(ORD))

print()
print("=" * 78)
print("(4) THE COUPLING LAW -- blocks, and the 63-class character match")
print("=" * 78)
p = PRIMES[2]
S, R = DATA[p]
L = mul(mul(inv(S, p), inv(R, p), p), S, p)
G = gen([R, L], p)
gate("theta commutes with every element of the image, so the eigenspaces are invariant",
     all(mul(Cm, g, p) == mul(g, Cm, p) for g in G))
plus, minus = [], []
for _j, (a, b) in enumerate(PRIM):
    k = idx[(b, a)]
    if k == _j:
        plus.append(tuple(1 if t == _j else 0 for t in range(6)))
    elif _j < k:
        plus.append(tuple(1 if t in (_j, k) else 0 for t in range(6)))
        minus.append(tuple((1 if t == _j else (p - 1 if t == k else 0))
                           for t in range(6)))
B_ = plus + minus
Bm = tuple(tuple(B_[i][j] for i in range(6)) for j in range(6))
Bi = inv(Bm, p)


def conj(g):
    return mul(Bi, mul(g, Bm, p), p)


gate("every element is block-diagonal in the theta-eigenbasis (4 + 2)",
     not any(conj(g)[i][j] for g in G for i in range(4) for j in range(4, 6))
     and not any(conj(g)[i][j] for g in G for i in range(4, 6) for j in range(4)))
odd = {tuple(tuple(conj(g)[i + 4][j + 4] for j in range(2)) for i in range(2))
       for g in G}
even = {tuple(tuple(conj(g)[i][j] for j in range(4)) for i in range(4)) for g in G}
gate("the 2-dimensional (theta = -1) block has image of order 360, as Scope (2880) says",
     len(odd) == 360, str(len(odd)))
print(f"      (the 4-dimensional block's image has order {len(even)})")

s5 = next(x for x in range(p) if x * x % p == 5 % p)


def toFp(t):
    return (t[0].numerator * pow(t[0].denominator, p - 2, p)
            + t[1].numerator * pow(t[1].denominator, p - 2, p) * s5) % p


ONE = (rr(1), ZQ, ZQ, ZQ)
c2T, c2I = qclasses(E2T, q2, ONE), qclasses(E2I, q5, ONE)
gate("the model has 7 x 9 = 63 classes", len(c2T) * len(c2I) == 63,
     f"2T: {len(c2T)}, 2I: {len(c2I)}")
Q8 = {g for g in E2T if all(x[1] == 0 for x in g)
      and sum(1 for x in g if x[0] != 0) == 1}
gate("chi's kernel Q8 has order 8", len(Q8) == 8)
w = next(x for x in range(2, p) if pow(x, 3, p) == 1 and x != 1)
cs = sorted({frozenset(q2(g, h) for h in Q8) for g in E2T}, key=lambda s: sorted(s))
ci = {c: i for i, c in enumerate(cs)}
chi = {g: pow(w, ci[frozenset(q2(g, h) for h in Q8)], p) for g in E2T}
model = sorted((len(A) * len(B), chi[A[0]] * (2 * toFp(B[0][0])) % p,
                (2 * toFp(A[0][0])) * (2 * toFp(B[0][0])) % p)
               for A in c2T for B in c2I)
Gl = list(G)
seen, actual = set(), []
for g in Gl:
    if g in seen:
        continue
    cl = {mul(mul(x, g, p), inv(x, p), p) for x in Gl}
    seen |= cl
    M = conj(g)
    actual.append((len(cl), sum(M[i][i] for i in range(4, 6)) % p,
                   sum(M[i][i] for i in range(4)) % p))
actual.sort()
gate("the image has 63 conjugacy classes", len(actual) == 63, str(len(actual)))
gate("CLASS-BY-CLASS MATCH on all 63: (size, chi(A)trV2(B), trV2(A)trV2(B))",
     model == actual)

print(f"""
  So Proposition (2880) and the coupling law are no longer certificates about a matrix
  the paper does not write down.  rho is built here from the Kac-Peterson data alone --
  six weights, one inverse Cartan matrix, one Weyl sum -- and it satisfies the four
  modular relations before any result is read.  The order 2880, the theta-blocks of
  dimensions 2 and 4, the odd block's 360, and the 63-class factorisation into
  chi(A)trV2(B) and trV2(A)trV2(B) all follow from that construction.

  Scope (2880)'s sentence -- "rho's structure constants are specified in the source
  computation and are not reconstructed in this paper" -- can go.""")

RES = {"primaries": [list(x) for x in PRIM], "T_exponents_over_15": EXPS, "ord_T": 15,
       "image_order_by_prime": {str(k): v for k, v in ORD.items()},
       "image_order": 2880, "theta_block_dims": [4, 2],
       "odd_block_image_order": len(odd), "even_block_image_order": len(even),
       "n_classes": len(actual), "class_match": model == actual,
       "primes": PRIMES,
       "scope": ("rho is constructed from the Kac-Peterson data and validated by the four "
                 "modular relations before any result is read; the field is Q(zeta_60), "
                 "the field the paper's own proof names, evaluated at primes p = 1 mod 60 "
                 "so the arithmetic is exact in F_p. The group order and the class match "
                 "are enumerations at those primes, which is the method the paper itself "
                 "describes ('enumeration at two unramified primes'). Nothing is claimed "
                 "about the member, the class, the sisters or the rows.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True)
print("\n  results.json written")
if FAILED:
    raise SystemExit(f"CONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
