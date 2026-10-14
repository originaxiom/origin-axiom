"""Audit check of the [LIT] statement: for c > 0 and positive trace, eta(W tau) = exp(i pi Psi/12) (c tau + d)^{1/2} eta(tau)
(principal root), with Psi = #R - #L in L = [[1,0],[1,1]], R = [[1,1],[0,1]]; and Psi via Rademacher's formula equals
#R - #L on every rotation. Independent implementation (pentagonal series at 40 digits; own Dedekind sum)."""
import mpmath as mp
from fractions import Fraction
from math import floor
mp.mp.dps = 40
def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()
def mat(word):
    a, b, c, d = 1, 0, 0, 1
    for ch in word:
        p, q, r, s = (1, 0, 1, 1) if ch == "L" else (1, 1, 0, 1)
        a, b, c, d = a*p + b*r, a*q + b*s, c*p + d*r, c*q + d*s
    return a, b, c, d
def eta(tau):
    q = mp.exp(2j*mp.pi*tau); s = mp.mpc(0); n = 0
    while True:
        t1 = (-1)**n * q**(n*(3*n-1)//2); t2 = (-1)**n * q**(n*(3*n+1)//2) if n > 0 else 0
        s += t1 + t2
        if n > 3 and abs(t1) < mp.mpf(10)**-45: break
        n += 1
    return mp.exp(2j*mp.pi*tau/24) * s
def dedekind(h, k):  # independent: s(h,k) = sum_{r=1}^{k-1} r/k ((hr/k)), via the floor form
    tot = Fraction(0)
    for r in range(1, k):
        x = Fraction(h*r, k)
        saw = Fraction(0) if x.denominator == 1 else x - floor(x) - Fraction(1, 2)
        tot += Fraction(r, k) * saw  # ((r/k)) = r/k - 1/2, and sum_r saw(hr/k) = 0, so the -1/2 drops
    return tot
def psi(a, b, c, d):
    if c == 0: return Fraction(b, d)
    sg = 1 if c > 0 else -1
    phi = Fraction(a + d, c) - 12*sg*dedekind(d, abs(c))
    t = c*(a + d); return phi - 3*((t > 0) - (t < 0))
worst = 0; nchk = 0; bad = []
for w in (w for w in lyndon(9) if len(w) >= 2):
    a, b, c, d = mat(w); P = w.count("R") - w.count("L")
    for k in range(len(w)):
        A = mat(w[k:] + w[:k])
        if psi(*A) != P: bad.append((w, k))
    tau = mp.mpc(-mp.mpf(d)/c + mp.mpf('0.137'), mp.mpf(1)/c)   # c tau + d = 0.137 c + i
    z = c*tau + d
    lhs = eta((a*tau + b)/z) / (mp.sqrt(z) * eta(tau))
    rhs = mp.exp(1j*mp.pi*P/12)
    worst = max(worst, abs(lhs - rhs)); nchk += 1
    # -W, weight r = 1..6: nu_r(-W) = (-1)^r nu_r(W): eta^(2r)((-W)tau) = nu (-c tau - d)^r eta^(2r)(tau)
    for r in range(1, 7):
        nu_minus = eta((a*tau + b)/z)**(2*r) / ((-z)**r * eta(tau)**(2*r))
        worst = max(worst, abs(nu_minus - (-1)**r * mp.exp(1j*mp.pi*r*P/6)))
print("threads checked (Lyndon, length 2..9):", nchk, "| rotation failures of Psi = #R-#L:", len(bad),
      "| worst |multiplier - prediction|:", mp.nstr(worst, 5))
