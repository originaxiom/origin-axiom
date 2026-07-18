"""B683 cell L1 — verify the divided-power non-cancellation law and its PROOF
mechanism for (q;q)_inf^{-3/5}.

Claim (theorem): let c_n = [q^n] (q;q)_inf^{-3/5}. Then for all n >= 0,
    v5(c_n) = -(n + v5(n!)) exactly            (no cancellation),
equivalently v5(den c_n) = n + v5(n!) = n + (n - s5(n))/4.

Proof mechanism verified here (term-by-term):
  Write g = (q;q)_inf, h = g - 1 in q*Z[[q]].  Binomial series
      c_n = sum_{m=1..n} binom(-3/5, m) * b_{n,m},   b_{n,m} = [q^n] h^m in Z.
  Facts:  (A) v5(binom(-3/5,m)) = -(m + v5(m!))   [each numerator factor a unit];
          (B) b_{n,m} in Z so v5(b_{n,m}) >= 0;
          (C) b_{n,n} = (-1)^n  (unit), giving term m=n valuation exactly -(n+v5(n!));
          (D) phi(m)=m+v5(m!) strictly increasing => m=n term is the UNIQUE 5-adic min.
  Ultrametric strict-min => v5(c_n) = -(n+v5(n!)).
This script checks (A),(B),(C),(D) and the final equality directly, to n=NMAX.
"""
from fractions import Fraction

NMAX = 400


def s5(n):
    s = 0
    while n:
        s += n % 5
        n //= 5
    return s


def v5_factorial(n):
    return (n - s5(n)) // 4


def v5_frac(x):
    """5-adic valuation of a nonzero Fraction (can be negative)."""
    if x == 0:
        return None
    num, den = x.numerator, x.denominator
    v = 0
    while num % 5 == 0:
        num //= 5
        v += 1
    while den % 5 == 0:
        den //= 5
        v -= 1
    return v


# --- g = (q;q)_inf truncated to degree NMAX, integer coeffs ---------------
g = [0] * (NMAX + 1)
g[0] = 1
for k in range(1, NMAX + 1):
    # multiply current g by (1 - q^k)
    for j in range(NMAX, k - 1, -1):
        g[j] -= g[j - k]
assert g[0] == 1 and g[1] == -1  # pentagonal: 1 - q - q^2 + q^5 + ...

# h = g - 1  (integer power series, lowest term -q)
h = g[:]
h[0] = 0

# --- direct power series f = g^{-3/5} via J.C.P. Miller recurrence ---------
s = Fraction(-3, 5)
f = [Fraction(0)] * (NMAX + 1)
f[0] = Fraction(1)
for n in range(1, NMAX + 1):
    acc = Fraction(0)
    for k in range(1, n + 1):
        acc += ((s + 1) * k - n) * g[k] * f[n - k]
    f[n] = acc / n

# --- (A) binom(-3/5,m) valuation ------------------------------------------
def binom_s(m):
    b = Fraction(1)
    for j in range(m):
        b *= (s - j) / (j + 1)
    return b


for m in range(0, min(NMAX, 200) + 1):
    assert v5_frac(binom_s(m)) == -(m + v5_factorial(m)), ("A", m)

# --- powers h^m up to needed diagonal, check (B),(C) and reconstruct c_n ---
# We verify b_{n,n} = (-1)^n and integrality of all b_{n,m}, and that the
# binomial reconstruction reproduces f exactly, and the strict-min property.
# Build h^m incrementally; keep only coeffs up to NMAX.
def mul(a, b):
    out = [0] * (NMAX + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for jdx in range(0, NMAX - i + 1):
            bj = b[jdx]
            if bj:
                out[i + jdx] += ai * bj
    return out


phi = [m + v5_factorial(m) for m in range(NMAX + 1)]
# check (D): phi strictly increasing
assert all(phi[m] < phi[m + 1] for m in range(NMAX)), "D"

hp = [0] * (NMAX + 1)
hp[0] = 1  # h^0
recon = [Fraction(0)] * (NMAX + 1)
binoms = [binom_s(m) for m in range(NMAX + 1)]
bnn_ok = True
integ_ok = True
strict_ok = True
recon[0] += binoms[0]
for m in range(1, NMAX + 1):
    hp = mul(hp, h)  # now h^m
    if hp[m] != (-1) ** m:            # (C)
        bnn_ok = False
    for n in range(m, NMAX + 1):
        bnm = hp[n]
        if bnm == 0:
            continue
        if not isinstance(bnm, int):
            integ_ok = False
        recon[n] += binoms[m] * bnm
        # strict-min bookkeeping: term valuation
        # (only need for the diagonal check below)

# reconstruction must equal direct series
assert all(recon[n] == f[n] for n in range(NMAX + 1)), "reconstruction mismatch"

# --- FINAL: the equality v5(c_n) = -(n+v5(n!)) for all n ------------------
banked = {1: 1, 10: 12, 40: 49, 80: 99, 119: 146}
all_ok = True
first_fail = None
for n in range(1, NMAX + 1):
    got = -v5_frac(f[n])            # v5(den)
    want = n + v5_factorial(n)
    if got != want:
        all_ok = False
        first_fail = (n, got, want)
        break

print(f"(A) binom(-3/5,m) valuation = -(m+v5(m!)):  PASS (m<= {min(NMAX,200)})")
print(f"(B) b_(n,m) integrality:                     {'PASS' if integ_ok else 'FAIL'}")
print(f"(C) b_(n,n) = (-1)^n (unit diagonal):        {'PASS' if bnn_ok else 'FAIL'}")
print(f"(D) phi(m)=m+v5(m!) strictly increasing:     PASS")
print(f"reconstruction (binomial series == f):       PASS")
for n, tgt in banked.items():
    print(f"  banked n={n}: v5(den)={-v5_frac(f[n])} target={tgt} "
          f"{'OK' if -v5_frac(f[n])==tgt else 'MISMATCH'}")
print(f"FINAL equality v5(c_n) = -(n+v5(n!)) for 1<=n<={NMAX}: "
      f"{'PASS' if all_ok else 'FAIL '+str(first_fail)}")
