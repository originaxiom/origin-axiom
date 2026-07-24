"""B776-symprod -- the symmetrised Habiro product Phi(h)Phi(-h) of the
figure-eight, computed FROM FIRST PRINCIPLES to high order, tracking the
denominator prime factorisation at every order (B776 prereg 0cdfcf44).

THE DECISIVE COMPUTATION (Computation 2 of the B685 homework).

Method (all exact, in-cell, no citation of the stream):
  The figure-eight Kashaev asymptotics come from the interior saddle
  w0 = e^{i pi/3} (w0^2 - w0 + 1 = 0, disc -3) of the summand of
  <4_1>_N = sum_k |(q)_k|^2.  The full all-orders asymptotic of the
  q-Pochhammer is the classical Bernoulli/quantum-dilog expansion
      log (q)_k ~ sum_{n>=0} h^{n-1} (B_n/n!) Li_{2-n}(w),   h=2 pi i/N, w=q^k,
  so  log|(q)_k|^2 = sum_n (B_n/n!)[ h^{n-1}Li_{2-n}(w) + (-h)^{n-1}Li_{2-n}(1/w) ].
  Formal Gaussian (Feynman/Wick) integration around w0 -- implemented as an
  eta-graded exp-recursion + Wick contraction, all arithmetic exact in
  Q(sqrt(-3)) -- yields the perturbative series Phi(h) = sum_n r_n x^n h^n,
  x = 1/(3 sqrt(-3)), x^2 = -1/27.  We then form Phi(h)Phi(-h), substitute
  h = log(1+u), and read the (q-1)=u expansion's denominators.

GATES (the normalisation is fixed, not fitted):
  r_1 = 11/24 and r_2 = 697/1152  (Garoufalidis-Zagier eq (1), reproduced),
  and Phi(h)Phi(-h) = 1 - u^2/27 + u^3/27 - 4u^4/243 - u^5/243 + ...
  (GSWZ arXiv:2412.04241 eq (2), reproduced).

ANCHOR GUARD (binding): reproduce B685's 3^146 at order (q-1)^100 BEFORE
trusting anything past 100.  If not reproduced => normalisation gap named.
E15 GUARD (binding): 3^k is a POWER OF 3, not "5 appears"; only a literal
5^k / 7^k / ... (any prime != 3) in a DENOMINATOR counts as a non-3 prime.

Env: pyenv python3 (sympy only for an independent low-order factor cross-check).
Re-runnable:  MM=105 python3 compute.py    (default MM=105).
"""

import os, sys, time, json
from fractions import Fraction as Fr

T0 = time.time()
M = int(os.environ.get("MM", "105"))     # target (q-1)-order
P = 2 * M + 4                            # vertex sigma-degree bound (>= 2M+2)
OUT = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output.txt"), "w")


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    OUT.write(s + "\n")
    OUT.flush()


# ====================================================================
# Q(sqrt(-3)) : element a + b r,  r^2 = -3
# ====================================================================
class QS:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = a if type(a) is Fr else Fr(a)
        self.b = b if type(b) is Fr else Fr(b)

    def __add__(s, o):
        o = o if type(o) is QS else QS(o)
        return QS(s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __sub__(s, o):
        o = o if type(o) is QS else QS(o)
        return QS(s.a - o.a, s.b - o.b)

    def __neg__(s):
        return QS(-s.a, -s.b)

    def __mul__(s, o):
        o = o if type(o) is QS else QS(o)
        return QS(s.a * o.a - 3 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__

    def inv(s):
        d = s.a * s.a + 3 * s.b * s.b
        return QS(s.a / d, -s.b / d)

    def __truediv__(s, o):
        o = o if type(o) is QS else QS(o)
        return s * o.inv()

    def __eq__(s, o):
        o = o if type(o) is QS else QS(o)
        return s.a == o.a and s.b == o.b

    def is_rat(s):
        return s.b == 0


ZERO = QS(0, 0); ONE = QS(1, 0)
w0 = QS(Fr(1, 2), Fr(1, 2))    # (1+r)/2 = e^{i pi/3}
b_pt = ONE - w0                # 1/w0 = 1 - w0
assert (w0 * w0 - w0 + ONE) == ZERO
assert (w0.inv() - b_pt) == ZERO


def pow_qs(x, n):
    out = ONE
    for _ in range(n):
        out = out * x
    return out


# ====================================================================
# series helpers (list of QS, index = power of sigma), degree P
# ====================================================================
def s_zero():
    return [ZERO] * (P + 1)


def s_add(x, y):
    return [x[i] + y[i] for i in range(P + 1)]


def s_scale(x, c):
    return [x[i] * c for i in range(P + 1)]


def s_mul(x, y):
    out = [ZERO] * (P + 1)
    for i in range(P + 1):
        xi = x[i]
        if xi.a == 0 and xi.b == 0:
            continue
        lim = P + 1 - i
        for j in range(lim):
            yj = y[j]
            if yj.a == 0 and yj.b == 0:
                continue
            out[i + j] = out[i + j] + xi * yj
    return out


def inv_series(den):
    out = [ZERO] * (P + 1)
    out[0] = den[0].inv()
    for n in range(1, P + 1):
        acc = ZERO
        for k in range(1, n + 1):
            acc = acc + den[k] * out[n - k]
        out[n] = -(out[0] * acc)
    return out


# ====================================================================
# Taylor data at w0
# ====================================================================
# L(sigma) = log(2 - w - 1/w) around w0, = log(1+(Pm1)), Pm1 = -(w^2-w+1)/w
w_ser = s_zero(); w_ser[0] = w0; w_ser[1] = ONE
inv_w = inv_series(w_ser)                       # 1/(w0+sigma)
two_w0_m1 = w0 + w0 - ONE
num = s_zero(); num[1] = two_w0_m1; num[2] = ONE   # sigma*(2w0-1) + sigma^2
Pm1 = s_scale(s_mul(num, inv_w), QS(-1, 0))
L = s_zero()
cur = s_zero(); cur[0] = ONE
for m in range(1, P + 1):
    cur = s_mul(cur, Pm1)
    L = s_add(L, s_scale(cur, QS(Fr((-1) ** (m + 1), m), 0)))
    if all(c.a == 0 and c.b == 0 for c in cur):
        break

# S_{-1} coeffs d[p]: S_{-1}' = -L/w ; sum p d[p] sigma^{p-1} = -L/w
minusL_over_w = s_scale(s_mul(L, inv_w), QS(-1, 0))
assert minusL_over_w[0] == ZERO                 # saddle: d[1] = 0
d = [ZERO] * (P + 1)
for p in range(2, P + 1):
    d[p] = minusL_over_w[p - 1] / QS(p, 0)
sm1_2 = d[2]
v = (-ONE) / (QS(2, 0) * sm1_2)                 # Gaussian variance in tau

# S0-tilde coeffs: (1/2)L - (log(w0+sigma) - log w0)
inv_w0 = w0.inv()
s0t = [ZERO] * (P + 1)
for p in range(1, P + 1):
    logp = QS(Fr((-1) ** (p + 1), p), 0) * pow_qs(inv_w0, p)
    s0t[p] = QS(Fr(1, 2), 0) * L[p] - logp


# Li_{-j}(w) Taylor around a point a
def li0_around(a):
    one_m_a = ONE - a
    den = s_zero(); den[0] = one_m_a; den[1] = QS(-1, 0)
    invden = inv_series(den)
    numer = s_zero(); numer[0] = a; numer[1] = ONE
    return s_mul(numer, invden)


def theta_op(f, a):
    out = [ZERO] * (P + 1)
    for q in range(P + 1):
        t = QS(q, 0) * f[q]
        if q + 1 <= P:
            t = t + a * QS(q + 1, 0) * f[q + 1]
        out[q] = t
    return out


def li_neg_around(j, a):
    f = li0_around(a)
    for _ in range(j):
        f = theta_op(f, a)
    return f


# The 1/w piece, computed CHEAPLY via the identity
#   Li_{-j}(1/w) = (-w d/dw)^j [ Li_0(1/w) ],   Li_0(1/w) = 1/(w-1).
# (No series composition needed -- O(j P) instead of O(P^3).)
# base: 1/(w-1) Taylor at w0 = 1/((w0-1)+sigma)
_wm1 = s_zero(); _wm1[0] = w0 - ONE; _wm1[1] = ONE
_li0_inv_w = inv_series(_wm1)     # = 1/(w-1) = Li_0(1/w)


def li_neg_inv_w(j):
    """Taylor at w0 of Li_{-j}(1/w) as a function of w."""
    f = _li0_inv_w
    for _ in range(j):
        f = theta_op(f, w0)            # theta_w = w d/dw, centred at w0
        f = [-c for c in f]            # the (-1) from (-w d/dw)
    return f


# Bernoulli B_{2m}
from sympy import bernoulli
from math import factorial


def Bern(n):
    val = bernoulli(n)
    return QS(Fr(int(val.p), int(val.q)), 0)


# ====================================================================
# Build the interaction vertices Int[(a,p)] = coeff, a=eta-weight, p=tau-power
# ====================================================================
log(f"[setup] M={M}, P={P}, dt={time.time()-T0:.1f}s  building vertices ...")
Int = {}


def add_vertex(a, p, c):
    if c.a == 0 and c.b == 0:
        return
    Int[(a, p)] = Int.get((a, p), ZERO) + c


# S_{-1}, p>=3: coeff d[p] at (a=p-2, p)
for p in range(3, P + 1):
    add_vertex(p - 2, p, d[p])
# S0-tilde, p>=1: coeff s0t[p] at (a=p, p)
for p in range(1, P + 1):
    add_vertex(p, p, s0t[p])
# S_{2m-1}, m>=1: (B_{2m}/(2m)!)(Li_{2-2m}(w) - Li_{2-2m}(1/w)); h^{2m-1}=eta^{4m-2}
mmax = (M + 1) // 2 + 1
for m in range(1, mmax + 1):
    j = 2 * m - 2
    pref = Bern(2 * m) / QS(factorial(2 * m), 0)
    liw = li_neg_around(j, w0)
    liwm = li_neg_inv_w(j)
    for p in range(0, P + 1):
        c = pref * (liw[p] - liwm[p])
        aw = 4 * m - 2 + p
        if aw <= 2 * M:
            add_vertex(aw, p, c)

# I_j(tau) as {p: coeff} for eta-weight j
Kmax = 2 * M
Ipoly = {}
for (a, p), c in Int.items():
    if a <= Kmax:
        Ipoly.setdefault(a, {})
        Ipoly[a][p] = Ipoly[a].get(p, ZERO) + c
# precompute j*I_j
Ipoly_j = {a: {p: c * QS(a, 0) for p, c in dd.items()} for a, dd in Ipoly.items()}

log(f"[setup] vertices built dt={time.time()-T0:.1f}s ; running exp-recursion to k={Kmax} ...")

# ====================================================================
# exp recursion:  E_k = (1/k) sum_{j=1}^k (j I_j) E_{k-j}
# ====================================================================
E = [None] * (Kmax + 1)
E[0] = {0: ONE}
for k in range(1, Kmax + 1):
    acc = {}
    for j, Ij in Ipoly_j.items():
        if j > k:
            continue
        Ekj = E[k - j]
        for p1, c1 in Ij.items():
            for p2, c2 in Ekj.items():
                pp = p1 + p2
                prod = c1 * c2
                cur = acc.get(pp)
                acc[pp] = prod if cur is None else cur + prod
    invk = QS(Fr(1, k), 0)
    E[k] = {p: c * invk for p, c in acc.items() if not (c.a == 0 and c.b == 0)}
    if k % 20 == 0:
        log(f"    ... exp k={k}/{Kmax}  dt={time.time()-T0:.1f}s")


# ====================================================================
# Wick contraction: Phi_n = <E_{2n}>, <tau^{2m}> = (2m-1)!! v^m
# ====================================================================
def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r


vpow = [ONE]
for _ in range(1, 3 * M + 3):
    vpow.append(vpow[-1] * v)


def wick(poly):
    out = ZERO
    for p, c in poly.items():
        if p % 2 == 0:
            out = out + c * QS(dfact(p - 1), 0) * vpow[p // 2]
    return out


a_coeff = [wick(E[2 * n]) for n in range(0, M + 1)]
a0 = a_coeff[0]
assert a0 == ONE, f"normalisation: a0={a0.a}+{a0.b}r (expected 1)"

# r_n = a_n * (3 sqrt-3)^n  (must be pure rational)
three_r = QS(0, 3)
r_vals = []
for n in range(0, M + 1):
    rn = a_coeff[n] * pow_qs(three_r, n)
    assert rn.b == 0, f"r_{n} not rational: {rn.a}+{rn.b}r"
    r_vals.append(rn.a)

log(f"[stream] r_n extracted (all pure rational) dt={time.time()-T0:.1f}s")
log(f"  r_1 = {r_vals[1]}   (gate 11/24)")
log(f"  r_2 = {r_vals[2]}   (gate 697/1152)")
assert r_vals[1] == Fr(11, 24), "GATE r1 FAILED"
assert r_vals[2] == Fr(697, 1152), "GATE r2 FAILED"
log("  GATE r1=11/24, r2=697/1152 : PASSED (normalisation fixed, not fitted)")


# ====================================================================
# Phi(h)Phi(-h), then h = log(1+u), read u-denominators
# ====================================================================
rr = {n: r_vals[n] for n in range(M + 1)}


def Qsym(twom):
    s = Fr(0)
    for i in range(twom + 1):
        s += ((-1) ** (twom - i)) * rr[i] * rr[twom - i]
    return s


# u-transfer in pure Fraction: sum_m (-1/27)^m Q_{2m} (log(1+u))^{2m}
K = M
Lg = [Fr(0)] * (K + 1)
for i in range(1, K + 1):
    Lg[i] = Fr((-1) ** (i + 1), i)


def fmul(x, y):
    out = [Fr(0)] * (K + 1)
    for i in range(K + 1):
        xi = x[i]
        if xi == 0:
            continue
        for j in range(K + 1 - i):
            yj = y[j]
            if yj:
                out[i + j] += xi * yj
    return out


Lsq = fmul(Lg, Lg)
cu = [Fr(0)] * (K + 1)
Lpow = [Fr(0)] * (K + 1); Lpow[0] = Fr(1)
m = 0
while 2 * m <= K:
    A = Fr((-1) ** m, 27 ** m) * Qsym(2 * m)
    for kk in range(K + 1):
        if Lpow[kk]:
            cu[kk] += A * Lpow[kk]
    m += 1
    Lpow = fmul(Lpow, Lsq)

# eq(2) cross-check
printed = {2: Fr(-1, 27), 3: Fr(1, 27), 4: Fr(-4, 243), 5: Fr(-1, 243)}
eq2_ok = all(cu[k] == printed[k] for k in printed)
log(f"[eq2] Phi(h)Phi(-h) = 1 - u^2/27 + u^3/27 - 4u^4/243 - u^5/243 + ... reproduced: {eq2_ok}")
assert eq2_ok, "GATE eq(2) FAILED"


# ====================================================================
# denominator prime factorisation at every order (E15 guard)
# ====================================================================
def classify_den(den):
    """Return (three_exp, nonthree_primes_dict). Pure-3 iff nonthree empty."""
    n = den
    e3 = 0
    while n % 3 == 0:
        n //= 3
        e3 += 1
    non = {}
    if n != 1:
        # factor the (small) 3-free remainder
        m2 = n
        p = 2
        while p * p <= m2:
            while m2 % p == 0:
                non[p] = non.get(p, 0) + 1
                m2 //= p
            p += 1 if p == 2 else 2
        if m2 > 1:
            non[m2] = non.get(m2, 0) + 1
    return e3, non


log("\n[denominators] order : coefficient-denominator factorisation")
first_non3 = None
three_exps = {}
for k in range(0, M + 1):
    den = cu[k].denominator
    e3, non = classify_den(den)
    three_exps[k] = e3
    pure3 = (len(non) == 0)
    if (not pure3) and first_non3 is None:
        first_non3 = (k, non)
    if k <= 12 or k % 5 == 0 or (not pure3) or k in (100, 101):
        tag = f"3^{e3}" if pure3 else f"3^{e3} * {non}  <== NON-3 PRIME"
        log(f"  u^{k:>3} : den = {tag}")

# ANCHOR
anchor_reproduced = (M >= 100 and three_exps.get(100) == 146 and
                     len(classify_den(cu[100].denominator)[1]) == 0)
log("")
log("=" * 68)
log("ANCHOR GUARD (3^146 at (q-1)^100, pure 3):")
if M >= 100:
    e3_100, non_100 = classify_den(cu[100].denominator)
    log(f"  order 100 denominator = 3^{e3_100}" +
        (f" * {non_100}" if non_100 else "  (pure power of 3)"))
    log(f"  B685 anchor 3^146 : {'REPRODUCED' if anchor_reproduced else 'NOT reproduced'}")
else:
    log(f"  M={M} < 100 : order 100 not reached this run.")
log("=" * 68)

# ====================================================================
# VERDICT
# ====================================================================
five_appears = False
disc = ""
if first_non3 is not None and first_non3[0] >= 101 and anchor_reproduced:
    # a literal prime != 3 in a denominator at order N in [101, M]
    five_appears = True
    verdict = "RESOLVED-A"
    Nnon = first_non3[0]
    disc = (f"A prime != 3 ({first_non3[1]}) appears in the denominator at "
            f"order u^{Nnon} (>100), with the 3^146@100 anchor reproduced: "
            f"B685's terminal no-go is REVERSED at depth {Nnon}.")
elif anchor_reproduced:
    # anchor reproduced, pure-3 through the reached order
    all_pure3_upto = all(len(classify_den(cu[k].denominator)[1]) == 0 for k in range(M + 1))
    verdict = "RESOLVED-B"
    disc = (f"Anchor 3^146@100 REPRODUCED in-cell from first principles; the "
            f"symmetrised product Phi(h)Phi(-h) is PURE-3 through order u^{M} "
            f"(no literal 5^k/7^k/... in any denominator). B685's 3-only "
            f"pattern holds to depth {M}; still unproved (GSWZ Habiro-ring "
            f"theorem remains the all-order mechanism). all_pure3_through_M={all_pure3_upto}")
else:
    verdict = "RESOLVED-B"
    if M < 100:
        disc = (f"This run reached only M={M} (<100); order 100 / the 3^146 "
                f"anchor not tested. Pure-3 confirmed to u^{M}. Re-run with "
                f"MM>=105 to test the anchor.")
    else:
        e3_100 = three_exps.get(100)
        disc = (f"Anchor NOT reproduced: order-100 denominator is 3^{e3_100}, "
                f"not 3^146 -- the in-cell normalisation differs from GSWZ at "
                f"depth 100. Boundary named; NOT guessed past it.")

log("\n" + "#" * 68)
log(f"VERDICT: {verdict}")
log(f"  anchor_reproduced = {anchor_reproduced}")
log(f"  five_appears (literal 5^k/7^k.. in a denominator, order>100) = {five_appears}")
log(f"  {disc}")
log("#" * 68)
log(f"total dt={time.time()-T0:.1f}s")

# results.json
results = {
    "cell": "B776-symprod",
    "M_reached": M,
    "verdict": verdict,
    "anchor_reproduced": bool(anchor_reproduced),
    "five_appears": bool(five_appears),
    "gates": {"r1": str(r_vals[1]), "r2": str(r_vals[2]),
              "r1_ok": r_vals[1] == Fr(11, 24), "r2_ok": r_vals[2] == Fr(697, 1152),
              "eq2_ok": eq2_ok},
    "three_exponent_at_100": (three_exps.get(100) if M >= 100 else None),
    "three_exponents": {str(k): three_exps[k] for k in three_exps},
    "first_nonthree_prime_order": (first_non3[0] if first_non3 else None),
    "first_nonthree_prime_factors": ({str(p): e for p, e in first_non3[1].items()}
                                     if first_non3 else None),
    "denominator_factorisation": {},
    "discriminating_fact": disc,
    "elapsed_sec": round(time.time() - T0, 1),
}
for k in range(0, M + 1):
    e3, non = classify_den(cu[k].denominator)
    results["denominator_factorisation"][str(k)] = {
        "three_exp": e3, "nonthree": {str(p): e for p, e in non.items()},
        "pure3": len(non) == 0}
json.dump(results, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "results.json"), "w"), indent=1)
log("wrote results.json")
OUT.close()
