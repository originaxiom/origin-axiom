"""
B787 Door D3 — Level-15 newform (15.a8 / Cremona 15a) at Fibonacci indices.

The weight-2 level-15 newform is the isogeny class 15.a (elliptic curve, conductor
15 = 3*5, non-CM). ALL curves in the class (15a1..15a8) share ONE L-function, hence
ONE coefficient sequence a_n. We compute a_n at Fibonacci indices and test for any
closed form / linear recursion / periodicity BEYOND what Hecke multiplicativity forces.

Hecke facts used (weight 2):
  a_1 = 1;  a_p = p+1-#E(F_p) for good p (p != 3,5);
  a_p in {+1 (split mult), -1 (non-split mult)} for the bad primes 3,5 (squarefree cond);
  a_{mn} = a_m a_n for gcd(m,n)=1;
  a_{p^k} = a_p a_{p^{k-1}} - p a_{p^{k-2}} for good p.

Run with sage-python (uses the elliptic-curve database) + an INDEPENDENT point-count
cross-check of a_p from a pure Weierstrass count over F_p.
"""
from sage.all import EllipticCurve, GF, primes, Integer
import sympy as sp

E = EllipticCurve('15a1')                 # representative of class 15.a
assert E.conductor() == 15 and not E.has_cm()
a_inv = E.a_invariants()

# ------------------------------------------------------------------ a_n
N = 100
an = E.anlist(N)                          # an[n] = a_n, an[0] is a padding 0

# ---- independent cross-check of a_p for good primes via naive point count ----
def naive_ap(p):
    """a_p = p + 1 - #E(F_p) counting affine points of y^2+a1xy+a3y=x^3+a2x^2+a4x+a6
    plus the point at infinity."""
    a1, a2, a3, a4, a6 = [int(c) for c in a_inv]
    F = GF(p)
    count = 1  # point at infinity
    for x in F:
        for y in F:
            lhs = y*y + a1*x*y + a3*y
            rhs = x**3 + a2*x*x + a4*x + a6
            if lhs == rhs:
                count += 1
    return p + 1 - count

good = [p for p in primes(90) if 15 % p != 0]
xcheck = {p: (int(an[p]), naive_ap(p)) for p in good}
xcheck_ok = all(v[0] == v[1] for v in xcheck.values())

# ------------------------------------------------------------------ Fibonacci indices
def fibs_upto(m):
    out, a, b = [], 1, 2
    out.append(1)  # F: 1,2,3,5,8,...  (we use the 1,2,3,5,8,13,... convention)
    while a <= m:
        out.append(a)
        a, b = b, a + b
    # dedupe/sort the requested set explicitly to match the door spec
    return out

FIB = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
seq = [int(an[n]) for n in FIB]

# ------------------------------------------------------------------ Hecke decomposition
# show every composite Fibonacci index is FORCED by prime a_p + Hecke (nothing new)
def factor_expl(n):
    f = sp.factorint(n)
    return f

hecke_lines = []
for n in FIB:
    f = sp.factorint(n)
    if n == 1:
        hecke_lines.append((n, int(an[n]), "a_1 = 1 (definition)"))
    elif len(f) == 1 and list(f.values())[0] == 1:
        p = n
        kind = "good" if 15 % p != 0 else "BAD (mult. reduction)"
        hecke_lines.append((n, int(an[n]), f"prime {p} ({kind}): a_{p} read off"))
    else:
        # reconstruct from prime-power Hecke + multiplicativity
        val = 1
        parts = []
        for p, k in f.items():
            # a_{p^k}
            seqpk = [1, int(an[p])]
            for j in range(2, k + 1):
                if 15 % p == 0:
                    # bad prime: a_{p^k} = a_p^k
                    seqpk.append(int(an[p])**j)
                else:
                    seqpk.append(int(an[p]) * seqpk[-1] - p * seqpk[-2])
            val *= seqpk[k]
            parts.append(f"a_{p}^^{k}={seqpk[k]}")
        hecke_lines.append((n, int(an[n]), "Hecke: " + " * ".join(parts) + f" = {val} (matches {int(an[n])}: {val==int(an[n])})"))

# ------------------------------------------------------------------ TESTS for structure beyond Hecke
# Test 1: Fibonacci-additive recursion a_{F_{k+1}} =? a_{F_k}+a_{F_{k-1}}
fib_add = all(seq[k+1] == seq[k] + seq[k-1] for k in range(1, len(seq)-1))
fib_add_detail = [(seq[k-1], seq[k], seq[k]+seq[k-1], seq[k+1]) for k in range(1, len(seq)-1)]

# Test 2: does ANY constant-coefficient linear recurrence of order r fit ALL terms?
# For order r we need >= 2r data to have any over-determination. We test r=1,2,3.
def fits_linear_recurrence(s, r):
    """Return (fits, coeffs) if there exist rationals c_0..c_{r-1} with
    s[i] = sum_j c_j s[i-r+j] for ALL i>=r, solving from the first r equations
    then verifying the rest. Over-determined when len(s) > 2r."""
    n = len(s)
    if n < 2*r + 1:            # need at least one *verification* equation beyond the r that fix coeffs
        return (None, None, "underdetermined")
    import sympy as _sp
    # build first r equations to solve for coeffs
    A = _sp.Matrix([[s[i - r + j] for j in range(r)] for i in range(r, 2*r)])
    bvec = _sp.Matrix([s[i] for i in range(r, 2*r)])
    if A.det() == 0:
        return (None, None, "singular window (indeterminate)")
    coeffs = A.solve(bvec)
    # verify on all remaining equations
    ok = True
    for i in range(2*r, n):
        pred = sum(coeffs[j]*s[i - r + j] for j in range(r))
        if _sp.nsimplify(pred) != s[i]:
            ok = False
            break
    return (ok, [str(c) for c in coeffs], "checked")

rec_results = {r: fits_linear_recurrence(seq, r) for r in (1, 2, 3, 4)}

# Test 3: periodicity of the raw sequence (values grow with sqrt(p) -> cannot be periodic)
hasse = [(n, int(an[n]), float(2*(n**0.5))) for n in FIB]  # |a_n| <= 2*sqrt(n) for prime n
raw_periodic = len(set(seq)) < len(seq) and (seq == seq[:len(seq)//2]*2)  # crude

# Test 4: periodicity mod m of a_{F_n} for small m
mod_period = {}
for m in (2, 3, 4, 5, 6, 7):
    r = [x % m for x in seq]
    # smallest period p dividing len that reproduces the list
    per = None
    for pcand in range(1, len(r)):
        if len(r) % pcand == 0 and r == (r[:pcand] * (len(r)//pcand)):
            per = pcand
            break
    mod_period[m] = (r, per)

# Test 5: prime-index subsequence vs Sato-Tate (descriptive base-rate)
prime_fibs = [n for n in FIB if sp.isprime(n)]
prime_sub = [(n, int(an[n]), 'good' if 15 % n else 'bad') for n in prime_fibs]

# ------------------------------------------------------------------ OUTPUT
lines = []
def P(*a):
    lines.append(" ".join(str(x) for x in a))

P("="*72)
P("B787 D3 — level-15 newform 15.a (Cremona 15a) at Fibonacci indices")
P("="*72)
P(f"curve rep 15a1  a-invariants={a_inv}  conductor={E.conductor()}  CM={E.has_cm()}")
P("all 8 curves 15a1..15a8 are isogenous -> identical L-function -> identical a_n")
P("")
P("INDEPENDENT CROSS-CHECK a_p (sage anlist) vs naive #E(F_p) count, good p<90:")
P("  p : (anlist, naive)")
for p in good:
    P(f"  {p:2d}: {xcheck[p]}")
P(f"  ALL MATCH: {xcheck_ok}")
P("")
P("FIBONACCI-INDEX COEFFICIENTS a_{F_n}, F in", FIB, ":")
P("  ", seq)
P("")
P("Per-index Hecke provenance (composite indices are FORCED, nothing new):")
for n, v, expl in hecke_lines:
    P(f"  a_{n:2d} = {v:3d}   {expl}")
P("")
P("-"*72)
P("STRUCTURE TESTS (is there a law BEYOND generic Hecke multiplicativity?)")
P("-"*72)
P(f"[T1] Fibonacci-additive a_(k+1)=a_k+a_(k-1) holds for all? {fib_add}")
P("     (a_{k-1}, a_k, sum, actual a_{k+1}):")
for t in fib_add_detail:
    P("      ", t)
P("")
P("[T2] Constant-coefficient linear recurrence fitting ALL 10 terms (over-determined):")
for r, (ok, coeffs, note) in rec_results.items():
    P(f"     order r={r}: fits={ok}  coeffs={coeffs}  [{note}]")
P("")
P("[T3] Raw-value periodicity? (Hasse bound |a_n|<=2 sqrt(n) grows -> impossible):")
for n, v, b in hasse:
    P(f"     a_{n:2d}={v:3d}   |a|<=2 sqrt(n)={b:.2f}")
P(f"     naive-periodic flag: {raw_periodic}")
P("")
P("[T4] Periodicity mod m of the a_{F_n} sequence (period=None means none <= len/2):")
for m,(r,per) in mod_period.items():
    P(f"     mod {m}: {r}   period={per}")
P("")
P("[T5] Prime-Fibonacci-index subsequence (the only 'free' draws):")
for n,v,kind in prime_sub:
    P(f"     a_{n:2d}={v:3d}  ({kind})   [F={n} is prime]")
P("     good-prime draws {2,13,89}: a_2,a_13,a_89 =",
  [int(an[p]) for p in prime_fibs if 15% p], "in Hasse intervals",
  [round(2*p**0.5,2) for p in prime_fibs if 15% p])
P("     bad-prime draws {3,5}: a_3,a_5 =",
  [int(an[p]) for p in prime_fibs if 15%p==0],
  "forced by reduction type (non-split@3=-1, split@5=+1), standard newform data")

print("\n".join(lines))
with open(__file__.rsplit('/',1)[0] + "/output.txt", "w") as f:
    f.write("\n".join(lines) + "\n")
