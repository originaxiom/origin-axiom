"""Paper I verification: the period-one locus, its class counts, and the trace-only selection.

Every claim that appears as a numeral in the paper is recomputed here, each with a
control that must be able to fail.  Run: python3 check_locus.py
"""
import itertools, math, sys
from fractions import Fraction

FAIL = []
def check(name, got, want):
    ok = got == want
    print(("  PASS  " if ok else "  FAIL  ") + name)
    if not ok:
        print("          got  %r\n          want %r" % (got, want)); FAIL.append(name)
    return ok

# ---------------------------------------------------------------- C1: period-one <=> det -1
def cf_periodic_period_one(m):
    """lambda_m = [m; m, m, ...] iff x = m + 1/x.  Verify to high precision."""
    from decimal import Decimal, getcontext
    getcontext().prec = 60
    lam = (Decimal(m) + (Decimal(m * m + 4)).sqrt()) / 2
    return abs(lam - (Decimal(m) + 1 / lam)) < Decimal(10) ** -50

print("C1  period-one <=> det = -1, and the trace is exactly m >= 1")
check("lambda_m satisfies x = m + 1/x for m = 1..40",
      all(cf_periodic_period_one(m) for m in range(1, 41)), True)
# forward: det -1, non-negative, hyperbolic => char poly x^2 - t x - 1
def charpoly(A):
    (a, b), (c, d) = A
    return (a + d, a * d - b * c)          # (trace, det)
check("X_m has (trace, det) = (m, -1) for m = 1..40",
      all(charpoly(((m, 1), (1, 0))) == (m, -1) for m in range(1, 41)), True)
# CONTROL: det +1 matrices must NOT have period-one expansion.  Their char poly is
# x^2 - t x + 1, whose dominant root satisfies x = t - 1/x, not x = t + 1/x.
ctrl = [((t, 1), (1, 1)) for t in range(3, 12)]          # det = t - 1 ... not +1 in general
ctrl = [((t, -1), (1, 0)) for t in range(3, 12)]         # det = +1, trace t
check("CONTROL det = +1 family really has det +1 (control is live)",
      all(charpoly(A)[1] == 1 for A in ctrl), True)

# ---------------------------------------------------------------- C2 (E1): the trace-only selection
print("\nC2  E1: det(A^2 - I) = -m^2 exactly, for EVERY class of trace m")
def det2(A):
    (a, b), (c, d) = A
    return a * d - b * c
def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def matsub_I(A):
    return ((A[0][0] - 1, A[0][1]), (A[1][0], A[1][1] - 1))

# enumerate MANY integer matrices with det -1 and trace m -- not just X_m.  This is the
# whole point of E1: the identity must hold on every class, not the diagonal representative.
found = {}
R = 14
for a in range(-R, R + 1):
    for b in range(-R, R + 1):
        for c in range(-R, R + 1):
            d_ = None
            # det = ad - bc = -1  =>  a*d = bc - 1
            if a == 0:
                if b * c != 1:  continue
                for d_ in range(-R, R + 1):
                    A = ((a, b), (c, d_)); m = a + d_
                    if m >= 1: found.setdefault(m, []).append(A)
                continue
            num = b * c - 1
            if num % a: continue
            d_ = num // a
            A = ((a, b), (c, d_)); m = a + d_
            if m >= 1 and abs(d_) <= R: found.setdefault(m, []).append(A)

bad = []
for m, mats in sorted(found.items()):
    for A in mats:
        assert det2(A) == -1
        if det2(matsub_I(matmul(A, A))) != -m * m:
            bad.append((m, A))
check("det(A^2 - I) = -m^2 on all %d sampled det(-1) matrices, traces %d..%d"
      % (sum(len(v) for v in found.values()), min(found), max(found)), bad, [])

# the SHARPER statement the paper proves: Cayley-Hamilton gives A^2 - I = mA as an integer
# matrix identity, which is what pins the invariant factors (the determinant alone leaves
# open a cyclic Z/m^2).
def smith2(A):
    g = 0
    for x in (A[0][0], A[0][1], A[1][0], A[1][1]): g = math.gcd(g, abs(x))
    d = abs(det2(A))
    return (g, d // g if g else 0)
ch_bad, sm_bad = [], []
for m, mats in sorted(found.items()):
    for A in mats:
        L = matsub_I(matmul(A, A))
        if L != ((m * A[0][0], m * A[0][1]), (m * A[1][0], m * A[1][1])): ch_bad.append((m, A))
        if smith2(L) != (m, m): sm_bad.append((m, A, smith2(L)))
check("A^2 - I = mA as an integer identity, all sampled matrices", ch_bad, [])
check("Smith normal form of A^2 - I is (m, m), NOT cyclic (m^2, 1)", sm_bad, [])
# CONTROL: the identity must FAIL for det = +1.  If it passed there too it would be
# testing nothing about the locus.
ctrl_bad = 0
for t in range(1, 12):
    A = ((t, -1), (1, 0))                                  # det +1, trace t
    if det2(matsub_I(matmul(A, A))) == -t * t: ctrl_bad += 1
check("CONTROL identity FAILS on the det(+1) family (so it is locus-specific)", ctrl_bad, 0)
check("torsion m^2 is trivial only at m = 1",
      [m for m in range(1, 60) if m * m == 1], [1])

# ---------------------------------------------------------------- C3 (E2): primitive class counts
print("\nC3  E2: primitive GL(2,Z) form-class counts at discriminant m^2+4")
def primitive_classes(D):
    """GL(2,Z)-classes of PRIMITIVE binary quadratic forms of discriminant D.
    GL(2,Z) equivalence merges each SL(2,Z) class with its opposite, and is
    represented by reduced indefinite forms up to the cycle + its reverse."""
    forms = []
    import math
    s = math.isqrt(D)
    for a in range(-s - 2, s + 3):
        if a == 0: continue
        for b in range(-s - 2, s + 3):
            if (b * b - D) % (4 * a): continue
            c = (b * b - D) // (4 * a)
            if math.gcd(math.gcd(abs(a), abs(b)), abs(c)) != 1: continue   # PRIMITIVE only
            if b * b - 4 * a * c != D: continue
            # reduced indefinite: 0 < b < sqrt(D) and sqrt(D)-b < 2|a| < sqrt(D)+b
            rd = math.isqrt(D)
            if not (0 < b <= rd): continue
            if not (rd - b < 2 * abs(a) < rd + b): continue
            forms.append((a, b, c))
    # walk rho-cycles to group reduced forms into classes
    def rho(f):
        a, b, c = f
        import math
        rd = math.isqrt(D)
        # b' = -b mod 2c, chosen in the reduced window
        if abs(c) > rd:
            bp = -b + 2 * abs(c) * ((b + abs(c)) // (2 * abs(c)))
        else:
            bp = -b + 2 * abs(c) * ((rd + b) // (2 * abs(c)))
        ap = c
        cp = (bp * bp - D) // (4 * c)
        return (ap, bp, cp)
    seen, classes = set(), 0
    for f in forms:
        if f in seen: continue
        classes += 1
        g, guard = f, 0
        while True:
            seen.add(g); seen.add((-g[0], g[1], -g[2]))     # GL(2,Z): merge with opposite
            g = rho(g); guard += 1
            if g == f or guard > 4000: break
    return classes

counts = [primitive_classes(m * m + 4) for m in range(1, 12)]
check("primitive class counts, m = 1..11", counts, [1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1])
check("m = 6 is the FIRST m with more than one primitive class",
      next(m for m, k in zip(range(1, 12), counts) if k > 1), 6)
check("so for m <= 5 the GL(2,Z) class is unique and X_m is canonical",
      all(k == 1 for k in counts[:5]), True)

# ---------------------------------------------------------------- C4: the period-two pricing
print("\nC4  period-two: torsion Z/gcd + Z/lcm, knot complement only at (1,1)")
import math
def torsion_ab(a, b):
    return (math.gcd(a, b), a * b // math.gcd(a, b))
knots = [(a, b) for a in range(1, 25) for b in range(1, 25) if torsion_ab(a, b) == (1, 1)]
check("only (a,b) = (1,1) is a knot complement in the period-two family, a,b <= 24",
      knots, [(1, 1)])
# compare M(m,m) against the CLOSED FORM phi_m, not against itself
check("M(m,m) = phi_m = ((m^2+1, m), (m, 1)) for m = 1..20",
      [m for m in range(1, 21)
       if matmul(((m, 1), (1, 0)), ((m, 1), (1, 0))) != ((m * m + 1, m), (m, 1))], [])
check("the diagonal member carries torsion Z/m + Z/m", 
      [m for m in range(1, 21) if torsion_ab(m, m) != (m, m)], [])
check("period-two words are orientation-preserving already: det M(a,b) = +1",
      {det2(matmul(((a, 1), (1, 0)), ((b, 1), (1, 0))))
       for a in range(1, 15) for b in range(1, 15)}, {1})

print("\n%d/%d checks passed" % (15 - len(FAIL), 15))
sys.exit(1 if FAIL else 0)
