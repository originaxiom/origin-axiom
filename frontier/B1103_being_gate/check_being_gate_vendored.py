"""VENDORED CERTIFICATE (B1103 bank, 2026-08-21) -- the outside session's own exact
certificate for the being gate, shipped in its handoff package with this sha256
stated and verified at vendoring: cabc174d5a7d8c133ffccb2abf204096bc72535a04fa91bab50c518d9f767462
Runs standalone (sympy only, Z[zeta_30] exact); exit 0 on success, 1 on drift;
negative-controlled at receipt (modulus 3->2 fails 484/1364 and DRIFTs).
The banking seat's own independent engines live beside it in this arc."""
#!/usr/bin/env python3
"""
check_being_gate.py  --  chat1, 2026-08-20

Self-contained exact certificate for THE BEING-GATE THEOREM.

    For a word w in the free group on {a,A,b,B} (A=a^-1, B=b^-1) acting through
    the SU(3)_2 modular representation, let h(w) be the theta-odd coupling.
    Write p = #a - #A and q = #b - #B (the abelianization). Then

        h(w) lies in Q(zeta_5)   <=>   p - q = 0 (mod 3)   or   h(w) = 0.

    Equivalently  h(w) = zeta_3^(p-q) * (an element of Q(zeta_5)):
    a BEING phase times a HEARING magnitude.

Everything is exact in Z[zeta_30]; no floating point enters any verdict.
Depends only on sympy + the standard library.  Exits non-zero on drift.
"""
import itertools, functools, sys
from sympy import Poly, cyclotomic_poly, QQ, Rational, symbols

x = symbols('x')
PHI = Poly(cyclotomic_poly(30, x), x, domain=QQ)
D   = PHI.degree()
RED = [-Rational(c) for c in [int(v) for v in PHI.all_coeffs()][1:]]

# ---------- exact arithmetic in Z[zeta_30] ----------
def norm(a):
    a = list(a) + [Rational(0)] * max(0, D - len(a))
    for i in range(len(a) - 1, D - 1, -1):
        c = a[i]
        if c:
            a[i] = Rational(0)
            for j, r in enumerate(RED):
                a[i - 1 - j] += c * r
    return tuple(a[:D])

ZERO = tuple([Rational(0)] * D)
ONE  = tuple([Rational(1)] + [Rational(0)] * (D - 1))
def add(u, v):  return tuple(p + q for p, q in zip(u, v))
def sub(u, v):  return tuple(p - q for p, q in zip(u, v))
def smul(r, u): return tuple(Rational(r) * p for p in u)
def mul(u, v):
    c = [Rational(0)] * (2 * D - 1)
    for i, p in enumerate(u):
        if p:
            for j, q in enumerate(v):
                if q:
                    c[i + j] += p * q
    return norm(c)
XV = norm([Rational(0), Rational(1)])
def zpow(k):
    k %= 30; r = ONE
    for _ in range(k): r = mul(r, XV)
    return r
def gal(u, k):
    r = ZERO
    for i, c in enumerate(u):
        if c: r = add(r, smul(c, zpow(i * k)))
    return r
def isz(u): return all(c == 0 for c in u)

# ---------- SU(3)_2 modular data, built from scratch ----------
LEVEL = 2
W = [(a, b) for a in range(LEVEL + 1) for b in range(LEVEL + 1 - a)]
n = len(W)
Lv    = lambda t: (t[0] + t[1] + 2, t[1] + 1, 0)
ip3   = lambda u, v: 3*sum(u[i]*v[i] for i in range(3)) - sum(u)*sum(v)
perms = list(itertools.permutations(range(3)))
sgn   = lambda p: (-1) ** sum(1 for i in range(3) for j in range(i+1,3) if p[i] > p[j])

S = [[ZERO]*n for _ in range(n)]
for i, wl in enumerate(W):
    Ll = Lv(wl)
    for j, wm in enumerate(W):
        Lm, acc = Lv(wm), ZERO
        for p in perms:
            e = ip3(tuple(Ll[t] for t in p), Lm)
            z = zpow(-2 * e)
            acc = add(acc, z if sgn(p) > 0 else smul(-1, z))
        S[i][j] = acc
T = [[ZERO]*n for _ in range(n)]
for i, (a, b) in enumerate(W):
    T[i][i] = zpow(2*(a*a + a*b + b*b) + 6*(a + b) - 4)
C = [[ONE if W[j] == (W[i][1], W[i][0]) else ZERO for j in range(n)] for i in range(n)]

def mm(A, B):
    return [[functools.reduce(add, [mul(A[i][t], B[t][j]) for t in range(n)], ZERO)
             for j in range(n)] for i in range(n)]

fail = []
def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    if not ok: fail.append(label)

print("check_being_gate.py -- exact certificate in Z[zeta_30]")
print("=" * 70)
print("STAGE 1: modular data")
S2 = mm(S, S)
s = next(S2[i][j] for i in range(n) for j in range(n) if not isz(C[i][j]))
check("S^2 = s*C exactly (theta = charge conjugation is the centre)",
      all(isz(sub(S2[i][j], smul(s[0], C[i][j]))) for i in range(n) for j in range(n)))
check("s = -75 (rational)", s[0] == -75 and all(c == 0 for c in s[1:]))

Sinv = [[smul(Rational(1,1)/s[0], mm(C, S)[i][j]) for j in range(n)] for i in range(n)]
Tinv = [[gal(T[i][j], 29) if i == j else ZERO for j in range(n)] for i in range(n)]
I6   = [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
check("S^-1 S = I", all(isz(sub(mm(Sinv,S)[i][j], I6[i][j])) for i in range(n) for j in range(n)))

R, L    = T, mm(Sinv, mm(Tinv, S))
Rin, Lin = Tinv, mm(Sinv, mm(T, S))
check("R R^-1 = I  (the capital A)", all(isz(sub(mm(R,Rin)[i][j], I6[i][j])) for i in range(n) for j in range(n)))
check("L L^-1 = I  (the capital B)", all(isz(sub(mm(L,Lin)[i][j], I6[i][j])) for i in range(n) for j in range(n)))
GEN = {'a': R, 'A': Rin, 'b': L, 'B': Lin}

pairs  = [(W.index((1,0)), W.index((0,1))), (W.index((2,0)), W.index((0,2)))]
a0, b0 = pairs[0]
def coupling(M):
    Mt = mm(C, M)
    return smul(Rational(1,2), add(sub(Mt[a0][a0], Mt[a0][b0]), sub(Mt[b0][b0], Mt[b0][a0])))

print("\nSTAGE 2: chi from the odd-plane determinant")
def odd2(M):
    o = [[ZERO, ZERO], [ZERO, ZERO]]
    for p, (aa, bb) in enumerate(pairs):
        for q, (cc, ee) in enumerate(pairs):
            o[p][q] = smul(Rational(1,2),
                           sub(sub(M[aa][cc], M[aa][ee]), sub(M[bb][cc], M[bb][ee])))
    return o
det2 = lambda A: sub(mul(A[0][0], A[1][1]), mul(A[0][1], A[1][0]))
z3   = [zpow(0), zpow(10), zpow(20)]
which = lambda c: next((i for i, z in enumerate(z3) if isz(sub(c, z))), None)
dR, dL = which(det2(odd2(R))), which(det2(odd2(L)))
check("det(odd R) = zeta_3^2", dR == 2)
check("det(odd L) = zeta_3^1", dL == 1)
# chi = (chi^2)^2 since chi^3 = 1
cR, cL = (2*dR) % 3, (2*dL) % 3
check("=> chi(a) = zeta_3,  chi(b) = zeta_3^-1  (exponent p-q)", (cR, cL) == (1, 2))

print("\nSTAGE 3: the gate on the free group {a,A,b,B}")
MAXLEN = int(sys.argv[1]) if len(sys.argv) > 1 else 5
lvl, tot, ok, zer = {"": I6}, 0, 0, 0
bad = []
for depth in range(1, MAXLEN + 1):
    nxt = {}
    for wd, M in lvl.items():
        for ch, g in GEN.items():
            w2, M2 = wd + ch, mm(M, g)
            nxt[w2] = M2
            h = coupling(M2)
            inQ5 = isz(sub(gal(h, 11), h))
            p = w2.count('a') - w2.count('A')
            q = w2.count('b') - w2.count('B')
            pred = ((p - q) % 3 == 0) or isz(h)
            tot += 1; ok += (inQ5 == pred); zer += isz(h)
            if inQ5 != pred and len(bad) < 8: bad.append((w2, p - q))
    lvl = nxt
    print("    through length %d: %5d words cumulative" % (depth, tot))
check("gate holds on every word (length <= %d): %d/%d, h=0 in %d"
      % (MAXLEN, ok, tot, zer), ok == tot)
if bad: print("    mismatches:", bad)

print("\nSTAGE 4: the commutator subgroup is inside the Q(zeta_5) locus")
inv = lambda w: "".join({'a':'A','A':'a','b':'B','B':'b'}[c] for c in reversed(w))
def wmat(wd):
    M = I6
    for ch in wd: M = mm(M, GEN[ch])
    return M
base = ["".join(t) for Lw in (1, 2) for t in itertools.product("aAbB", repeat=Lw)]
allin = True
for u in base[:12]:
    for v in base[:12]:
        if not isz(sub(gal(coupling(wmat(u+v+inv(u)+inv(v))), 11),
                       coupling(wmat(u+v+inv(u)+inv(v))))):
            allin = False
check("every sampled commutator [u,v] lies in Q(zeta_5) (chi kills commutators)", allin)
check("h(abAB) = h(ab) exactly (being phase = 1 on both)",
      isz(sub(coupling(wmat("abAB")), coupling(wmat("ab")))))

print("\n" + "=" * 70)
if fail:
    print("DRIFT: %d check(s) failed: %s" % (len(fail), fail)); sys.exit(1)
print("ALL CHECKS PASSED (%d words, exact arithmetic)" % tot); sys.exit(0)
