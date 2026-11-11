#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_web_seat_relays.py

An independent re-derivation of the exact, data-free claims of two notes:

  note 1 (N1): relays/CHAT1_TO_CC_2026-11-11_THE_READ_OUT_AS_A_VALUE.md
  note 2 (N2): relays/CHAT1_TO_CC_2026-11-11_WHAT_SYMMETRY_ALLOWS_A_STATE_OF_THE_WHOLE.md

Everything below is written from the definitions in the notes' text.  The notes' own
scripts were neither run nor copied.  The numbers the notes claim (their text and
their committed result files) are embedded here as literals and printed beside the
values computed here.  Pure mathematics: integer matrices, continued fractions,
congruence subgroups of the modular group.  Nothing is measured and nothing is
compared with any measured value.

Run:     python3 -B verify_web_seat_relays.py
Writes:  verify_web_seat_relays_out.txt beside this script, and nothing else.

Method.  Heights of cyclic run sequences are computed exactly as elements
a + b*sqrt(D) of a real quadratic field (D an integer, a and b rational), so "the
apex is unique", "two copies tie" and "falls strictly" are decided by integer
comparisons; decimals are produced only for display and for differences between two
different fields, at 140 significant digits.  Statements about the level-5 groups
are decided on coset spaces and on Schreier generators (exact).  Modular functions
are evaluated from their q-products and Lambert series at 60 digits and identities
are then required to hold to better than 1e-45.  There are no assertions: every
claim prints the note's value, the value found here, and a status computed by a
comparison.
"""

import os
import sys
import math
import random
import itertools
from fractions import Fraction
from decimal import Decimal, getcontext, ROUND_HALF_EVEN

getcontext().prec = 140

try:
    import mpmath
    from mpmath import mp, mpf, mpc
    HAVE_MP = True
except Exception:                                    # pragma: no cover
    HAVE_MP = False
try:
    import sympy
    HAVE_SYMPY = True
except Exception:                                    # pragma: no cover
    HAVE_SYMPY = False

# ----------------------------------------------------------------------------------------
# output and the register of claims
# ----------------------------------------------------------------------------------------

OUT = []
CLAIMS = []
SELF = {}
NOTES = {}          # values kept for the remarks printed after the claims
AGREE, DISAGREE, NOTRE = 'AGREE', 'DISAGREE', 'NOT RECOMPUTED'


def out(s=''):
    OUT.append(str(s))


def st(ok):
    return AGREE if ok else DISAGREE


def claim(text, note_value, my_value, status, details=()):
    """Register one numbered claim and print it.  `text` is the claim in at most 20 words."""
    n = len(CLAIMS) + 1
    CLAIMS.append(dict(n=n, text=text, note=str(note_value), mine=str(my_value), status=status))
    out('[%3d] %s' % (n, text))
    out('      note : %s' % note_value)
    out('      here : %s' % my_value)
    for d in details:
        out('         . %s' % d)
    out('      => %s' % status)
    out()


# ----------------------------------------------------------------------------------------
# decimal helpers
# ----------------------------------------------------------------------------------------

def D_(fr):
    fr = Fraction(fr)
    return Decimal(fr.numerator) / Decimal(fr.denominator)


def round_sig(x, n):
    x = Decimal(x)
    if x == 0:
        return Decimal(0)
    e = x.adjusted()
    return x.quantize(Decimal(1).scaleb(e - n + 1), rounding=ROUND_HALF_EVEN)


def sigdigits(s):
    d = Decimal(s)
    if d == 0:
        return 1
    return len(d.as_tuple().digits)


def agree_printed(x, printed, nsig=None):
    """True when x, rounded to the significant digits the note printed, equals the printed number."""
    p = Decimal(printed)
    n = nsig if nsig is not None else sigdigits(printed)
    return round_sig(x, n) == p


def f8(x, n=8):
    """x to n significant digits, as a short string (fixed point down to 1e-4, as the notes print)"""
    x = Decimal(x)
    if x == 0:
        return '0'
    r = round_sig(x, n).normalize()
    e = r.adjusted()
    if -4 <= e <= 20:
        return format(r, 'f')
    mant, ex = format(r, 'E').split('E')
    if '.' in mant:
        mant = mant.rstrip('0').rstrip('.')
    return '%se%d' % (mant, int(ex))


SQRT5 = Decimal(5).sqrt()
PHI = (1 + SQRT5) / 2
PHI4 = PHI ** 4
FOUR_LN_PHI = 4 * PHI.ln()

# ----------------------------------------------------------------------------------------
# exact arithmetic: a + b sqrt(D) with D fixed;  Q(sqrt5);  Q(sqrt5)(i)
# ----------------------------------------------------------------------------------------


class Surd(object):
    """a + b*sqrt(D): a, b rational, D a positive integer that is not a square."""
    __slots__ = ('a', 'b', 'D')

    def __init__(self, a, b, D):
        self.a = Fraction(a)
        self.b = Fraction(b)
        self.D = D

    def _c(self, o):
        if isinstance(o, Surd):
            if o.D != self.D:
                raise ValueError('two different quadratic fields')
            return o
        return Surd(o, 0, self.D)

    def __add__(self, o):
        o = self._c(o)
        return Surd(self.a + o.a, self.b + o.b, self.D)
    __radd__ = __add__

    def __sub__(self, o):
        o = self._c(o)
        return Surd(self.a - o.a, self.b - o.b, self.D)

    def __neg__(self):
        return Surd(-self.a, -self.b, self.D)

    def __mul__(self, o):
        o = self._c(o)
        return Surd(self.a * o.a + self.b * o.b * self.D, self.a * o.b + self.b * o.a, self.D)

    def __truediv__(self, o):
        o = Fraction(o)
        return Surd(self.a / o, self.b / o, self.D)

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        lhs, rhs = a * a, b * b * self.D
        if a > 0:
            return (lhs > rhs) - (lhs < rhs)
        return (rhs > lhs) - (rhs < lhs)

    def __lt__(self, o):
        return (self - o).sign() < 0

    def __gt__(self, o):
        return (self - o).sign() > 0

    def __eq__(self, o):
        return (self - o).sign() == 0

    def __ne__(self, o):
        return (self - o).sign() != 0

    __hash__ = None

    def __abs__(self):
        return self if self.sign() >= 0 else -self

    def dec(self):
        return D_(self.a) + D_(self.b) * Decimal(self.D).sqrt()


class Q5(object):
    """a + b*sqrt(5), a and b rational."""
    __slots__ = ('a', 'b')

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    @staticmethod
    def of(x):
        return x if isinstance(x, Q5) else Q5(x)

    def __add__(self, o):
        o = Q5.of(o)
        return Q5(self.a + o.a, self.b + o.b)
    __radd__ = __add__

    def __sub__(self, o):
        o = Q5.of(o)
        return Q5(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return Q5.of(o) - self

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __mul__(self, o):
        o = Q5.of(o)
        return Q5(self.a * o.a + 5 * self.b * o.b, self.a * o.b + self.b * o.a)
    __rmul__ = __mul__

    def inv(self):
        n = self.a * self.a - 5 * self.b * self.b
        return Q5(self.a / n, -self.b / n)

    def __truediv__(self, o):
        return self * Q5.of(o).inv()

    def __rtruediv__(self, o):
        return Q5.of(o) * self.inv()

    def __pow__(self, n):
        r = Q5(1)
        base = self if n >= 0 else self.inv()
        for _ in range(abs(n)):
            r = r * base
        return r

    def __eq__(self, o):
        o = Q5.of(o)
        return self.a == o.a and self.b == o.b

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return hash((self.a, self.b))

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def sign(self):
        return Surd(self.a, self.b, 5).sign()

    def dec(self):
        return D_(self.a) + D_(self.b) * SQRT5

    def mp(self):
        return mpf(self.a.numerator) / self.a.denominator + (mpf(self.b.numerator) / self.b.denominator) * mp.sqrt(5)

    def __str__(self):
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return '(%s)*sqrt5' % self.b
        return '%s %s (%s)*sqrt5' % (self.a, '+' if self.b > 0 else '-', abs(self.b))
    __repr__ = __str__


class C5(object):
    """x + y*i with x, y in Q(sqrt5)."""
    __slots__ = ('re', 'im')

    def __init__(self, re=0, im=0):
        self.re = Q5.of(re)
        self.im = Q5.of(im)

    @staticmethod
    def of(x):
        return x if isinstance(x, C5) else C5(x)

    def __add__(self, o):
        o = C5.of(o)
        return C5(self.re + o.re, self.im + o.im)
    __radd__ = __add__

    def __sub__(self, o):
        o = C5.of(o)
        return C5(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return C5.of(o) - self

    def __neg__(self):
        return C5(-self.re, -self.im)

    def __mul__(self, o):
        o = C5.of(o)
        return C5(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    __rmul__ = __mul__

    def conj(self):
        return C5(self.re, -self.im)

    def inv(self):
        n = self.re * self.re + self.im * self.im
        return C5(self.re / n, (-self.im) / n)

    def __truediv__(self, o):
        return self * C5.of(o).inv()

    def __eq__(self, o):
        o = C5.of(o)
        return self.re == o.re and self.im == o.im

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return hash((self.re, self.im))

    def is_zero(self):
        return self.re.is_zero() and self.im.is_zero()

    def __str__(self):
        return '(%s) + (%s)*i' % (self.re, self.im)
    __repr__ = __str__


# ----------------------------------------------------------------------------------------
# 2 x 2 integer matrices
# ----------------------------------------------------------------------------------------

I2 = ((1, 0), (0, 1))


def mmul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def mdet(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def madj(A):
    return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))


def minv(A):
    """inverse of a matrix of determinant +1 or -1"""
    d = mdet(A)
    B = madj(A)
    return ((B[0][0] * d, B[0][1] * d), (B[1][0] * d, B[1][1] * d))


def mneg(A):
    return ((-A[0][0], -A[0][1]), (-A[1][0], -A[1][1]))


def mmod(A, m):
    return ((A[0][0] % m, A[0][1] % m), (A[1][0] % m, A[1][1] % m))


def mpow(A, n):
    R = I2
    for _ in range(n):
        R = mmul(R, A)
    return R


def flat(A):
    return [A[0][0], A[0][1], A[1][0], A[1][1]]


def rowact(v, A, m=5):
    return ((v[0] * A[0][0] + v[1] * A[1][0]) % m, (v[0] * A[0][1] + v[1] * A[1][1]) % m)


def colact(A, v, m=5):
    return ((A[0][0] * v[0] + A[0][1] * v[1]) % m, (A[1][0] * v[0] + A[1][1] * v[1]) % m)


def proportional(w, v, m=5):
    """w is a nonzero multiple of v modulo the prime m"""
    return (w[0] % m, w[1] % m) != (0, 0) and (w[0] * v[1] - w[1] * v[0]) % m == 0


# ========================================================================================
# PART 1.  cyclic run sequences, heights, departures
# ========================================================================================

def cf_prod(seq):
    """product of the matrices [[r,1],[1,0]] over seq, as (p, p', q, q') = [[p,p'],[q,q']]"""
    a, b, c, d = 1, 0, 0, 1
    for r in seq:
        a, b, c, d = a * r + b, a, c * r + d, c
    return a, b, c, d


def heights(runs):
    """The note's instrument, from its definition.

    For run i of the cyclic sequence, x_i = [0; r_{i+1}, r_{i+2}, ...] and y_i = [0; r_{i-1}, r_{i-2}, ...],
    both read cyclically, and H_i = (r_i + x_i + y_i)/2.
    A purely periodic xi = [s_1; s_2, ..., s_N, s_1, ...] is the positive root of q xi^2 + (q' - p) xi - p' = 0
    with [[p,p'],[q,q']] the product of the [[s_j,1],[1,0]];  x = 1/xi = (sqrt(D) - (p - q'))/(2p'),
    D = (p - q')^2 + 4 q p'.  Returns the list of (H_i, x_i, y_i), exact.
    """
    runs = list(runs)
    N = len(runs)
    dbl = runs + runs
    rev = runs[::-1]
    rdbl = rev + rev
    res = []
    for i in range(N):
        fwd = dbl[i + 1:i + 1 + N]
        j = N - 1 - i
        bwd = rdbl[j + 1:j + 1 + N]
        xs = []
        for seq in (fwd, bwd):
            p, pp, q, qp = cf_prod(seq)
            Dd = (p - qp) ** 2 + 4 * q * pp
            xs.append(Surd(Fraction(-(p - qp), 2 * pp), Fraction(1, 2 * pp), Dd))
        H = (xs[0] + xs[1] + runs[i]) / 2
        res.append((H, xs[0], xs[1]))
    return res


def heights_integer_form(runs):
    """A second, independent form: r_i + x_i + y_i is the difference of the two roots of the fixed-point
    equation of the cyclic word started at run i, so H_i = sqrt(D)/(2 q_i) with q_i the lower-left entry of
    prod_{j=0..N-1} [[r_{i+j},1],[1,0]] and D = trace^2 - 4(-1)^N.  Returns the list of (q_i, D)."""
    runs = list(runs)
    N = len(runs)
    dbl = runs + runs
    res = []
    for i in range(N):
        p, pp, q, qp = cf_prod(dbl[i:i + N])
        res.append((q, (p + qp) ** 2 - 4 * (-1) ** N))
    return res


def apex_fast(runs):
    """apex by the integer form: indices where q_i is least, and the apex height as a decimal"""
    qd = heights_integer_form(runs)
    qmin = min(q for q, _ in qd)
    idx = [i for i, (q, _) in enumerate(qd) if q == qmin]
    return idx, Decimal(qd[0][1]).sqrt() / (2 * qmin)


def cf_bruteforce(runs, i, depth):
    """x_i and y_i as rational convergents with `depth` partial quotients (a third, purely numerical route)."""
    N = len(runs)
    vals = []
    for sgn in (1, -1):
        seq = [runs[(i + sgn * j) % N] for j in range(1, depth + 1)]
        v = Fraction(0)
        for s in reversed(seq):
            v = 1 / (s + v)
        vals.append(v)
    return vals


def closed(D, g):
    """departure D closed by g golden periods: the note's L^n R (LR)^k is the run n, one run 1, then k pairs
    (1,1); L^6 R L R (runs 6,1,1,1) is "(6) closed by one period".  So: D followed by 2g+1 ones."""
    return list(D) + [1] * (2 * g + 1)


def composite(factors, k):
    """m factors at k: gaps of k, k+1, ..., k+m-1 golden periods, in that order.  Returns runs and the
    index spans of the factors."""
    runs, spans = [], []
    for j, D in enumerate(factors):
        a = len(runs)
        runs += list(D)
        spans.append((a, a + len(D)))
        runs += [1] * (2 * (k + j) + 1)
    return runs, spans


def analyse(factors, k):
    runs, spans = composite(factors, k)
    hs = heights(runs)
    best = hs[0][0]
    for H, _, _ in hs[1:]:
        if H > best:
            best = H
    apex_idx = [i for i, (H, _, _) in enumerate(hs) if H == best]
    per = []
    for (a, b) in spans:
        bi = a
        for i in range(a + 1, b):
            if hs[i][0] > hs[bi][0]:
                bi = i
        per.append(bi)
    return dict(runs=runs, spans=spans, hs=hs, best=best, apex_idx=apex_idx, per=per)


def span_of(idx, spans):
    for n, (a, b) in enumerate(spans):
        if a <= idx < b:
            return n
    return None


OWN_PERIODS = 60
_own_cache = {}


def own_value(D):
    """the note's own value: the apex height of D closed by 60 golden periods"""
    key = tuple(D)
    if key not in _own_cache:
        runs = closed(D, OWN_PERIODS)
        hs = heights(runs)
        bi = 0
        for i in range(1, len(hs)):
            if hs[i][0] > hs[bi][0]:
                bi = i
        ties = [i for i in range(len(hs)) if hs[i][0] == hs[bi][0]]
        _own_cache[key] = dict(dec=hs[bi][0].dec(), idx=bi, ties=ties,
                               offset=((hs[bi][1] - hs[bi][2]) / 2), inside=(bi < len(D)))
    return _own_cache[key]


def limit_heights(D):
    """heights of the runs of D standing in an infinite ground of ones, exact in Q(sqrt5)"""
    inv_phi = Q5(Fraction(-1, 2), Fraction(1, 2))          # [0; 1, 1, 1, ...] = (sqrt5 - 1)/2
    res = []
    for j in range(len(D)):
        x = inv_phi
        for d in reversed(D[j + 1:]):
            x = (Q5(d) + x).inv()
        y = inv_phi
        for d in D[:j]:
            y = (Q5(d) + y).inv()
        res.append((Q5(D[j]) + x + y) / 2)
    return res


def limit_own(D):
    hs = limit_heights(D)
    best = hs[0]
    for h in hs[1:]:
        if (h - best).sign() > 0:
            best = h
    return best


# The notes' matrices.  Note 2 (its fact R7) prints LR = [[1,1],[1,2]] = F^2 with F = [[0,1],[1,1]]; with words
# multiplied left to right that is L = [[1,0],[1,1]], R = [[1,1],[0,1]].
L_NOTE, R_NOTE = ((1, 0), (1, 1)), ((1, 1), (0, 1))
# The matrices as written in the request: L = [[1,1],[0,1]], R = [[1,0],[1,1]], LR = L.R = [[2,1],[1,1]].
L_REQ, R_REQ = ((1, 1), (0, 1)), ((1, 0), (1, 1))
V = (1, 3)


def word_matrix(runs, Lm, Rm):
    """the word of a run sequence, first run in L, letters multiplied left to right"""
    g = I2
    for i, r in enumerate(runs):
        X = Lm if i % 2 == 0 else Rm
        if X[0][1] == 0:                       # lower unipotent: its r-th power is [[1,0],[r,1]]
            Xr = ((1, 0), (r * X[1][0], 1))
        else:
            Xr = ((1, r * X[0][1]), (0, 1))
        g = mmul(g, Xr)
    return g


def keeps(runs, Lm=L_NOTE, Rm=R_NOTE, v=V):
    g = word_matrix(runs, Lm, Rm)
    gv = colact(g, v)
    vg = rowact(v, g)
    return dict(gv=gv, vg=vg, column=proportional(gv, v), row=proportional(vg, v))


# ---- the numbers note 1 claims (its text, out_value_not_place.json and postreview_checks_out.txt) ----

NOTE1_OWN = {"(6)": "3.6180339887498948482", "(11)": "6.1180339887498948482",
             "(2,1,2,1,2)": "1.7236067977499789696"}
B1857_APEX = {"(6)": "3.618034", "(2,1,2,1,2)": "1.723607"}     # the record's two apexes, six places
NOTE1_V1 = {      # per row: k, apex at a copy, spread, distance, offset
    '(6) x 2': dict(rate='1.924847303', rows=[
        (1, True, '0.0', '0.01910438', '0.014285714'),
        (2, True, '3.1115076e-61', '0.002754743', '0.0020542317'),
        (4, True, '3.1115076e-61', '5.8523989e-5', '4.3621643e-5'),
        (8, True, '0.0', '2.6516323e-8', '1.9764101e-8'),
        (16, True, '0.0', '5.4438833e-15', '4.0576311e-15')]),
    '(6) x 3': dict(rate='1.924847303', rows=[
        (1, True, '0.016335024', '0.019095226', '0.016344781'),
        (2, True, '0.0023532085', '0.0027545521', '0.0023534123'),
        (4, True, '4.9985625e-5', '5.8523903e-5', '4.9985717e-5'),
        (8, True, '2.2647644e-8', '2.6516323e-8', '2.2647644e-8'),
        (16, True, '4.6496315e-15', '5.4438833e-15', '4.6496315e-15')]),
    '(6) x 4': dict(rate='1.924847303', rows=[
        (1, True, '0.018693166', '0.0190946', '0.016643962'),
        (2, True, '0.0026960108', '0.0027545391', '0.0023970362'),
        (4, True, '5.7278191e-5', '5.8523897e-5', '5.0914211e-5'),
        (8, True, '2.5951891e-8', '2.6516323e-8', '2.3068347e-8'),
        (16, True, '5.3280036e-15', '5.4438833e-15', '4.7360032e-15')]),
    '(11) x 2': dict(rate='1.924847303', rows=[
        (1, True, '0.0', '0.022643042', '0.016949153'),
        (2, True, '0.0', '0.0032591373', '0.0024307244'),
        (4, True, '0.0', '6.921934e-5', '5.159373e-5'),
        (8, True, '0.0', '3.1362022e-8', '2.3375871e-8'),
        (16, True, '0.0', '6.4387203e-15', '4.7991388e-15')]),
    '(11) x 3': dict(rate='1.924847303', rows=[
        (1, True, '0.019377831', '0.022639238', '0.019381889'),
        (2, True, '0.002784439', '0.0032590583', '0.0027845234'),
        (4, True, '5.9120737e-5', '6.9219304e-5', '5.9120775e-5'),
        (8, True, '2.6786365e-8', '3.1362022e-8', '2.6786365e-8'),
        (16, True, '5.4993237e-15', '6.4387203e-15', '5.4993237e-15')]),
    '(11) x 4': dict(rate='1.924847303', rows=[
        (1, True, '0.022164321', '0.022638977', '0.019735688'),
        (2, True, '0.0031898318', '0.0032590529', '0.002836118'),
        (4, True, '6.7745952e-5', '6.9219301e-5', '6.0218945e-5'),
        (8, True, '3.0694443e-8', '3.1362022e-8', '2.7283949e-8'),
        (16, True, '6.3016642e-15', '6.4387203e-15', '5.6014793e-15')]),
    '(2,1,2,1,2) x 2': dict(rate='1.924847301', rows=[
        (1, True, '0.0', '0.0006942019', '0.00051777701'),
        (2, True, '0.0', '0.00010107303', '7.534281e-5'),
        (4, True, '1.5557538e-61', '2.1507203e-6', '1.6030556e-6'),
        (8, True, '0.0', '9.7449234e-10', '7.263437e-10'),
        (16, True, '0.0', '2.000663e-16', '1.4912062e-16')]),
    '(2,1,2,1,2) x 3': dict(rate='1.924847301', rows=[
        (1, True, '0.00059311529', '0.00069419342', '0.00059312435'),
        (2, True, '8.6330839e-5', '0.00010107285', '8.6331031e-5'),
        (4, True, '1.8369363e-6', '2.1507202e-6', '1.8369364e-6'),
        (8, True, '8.3231582e-10', '9.7449234e-10', '8.3231582e-10'),
        (16, True, '1.7087702e-16', '2.000663e-16', '1.7087702e-16')]),
    '(2,1,2,1,2) x 4': dict(rate='1.924847301', rows=[
        (1, True, '0.00067945074', '0.00069419284', '0.00060411257'),
        (2, True, '9.8922116e-5', '0.00010107284', '8.7934089e-5'),
        (4, True, '2.1049398e-6', '2.1507202e-6', '1.8710591e-6'),
        (8, True, '9.5374906e-10', '9.7449234e-10', '8.4777695e-10'),
        (16, True, '1.9580764e-16', '2.000663e-16', '1.7405124e-16')]),
}
NOTE1_V2 = {      # per row: k, distance (the file has "unique" and "at the deepest departure" True in every row)
    '(6) (11)': dict(deepest='(11)', rows=[
        (1, '0.019106208'), (2, '0.0027547811'), (4, '5.8524006e-5'), (8, '2.6516323e-8'), (16, '5.4438833e-15')]),
    '(6) (2,1,2,1,2)': dict(deepest='(6)', rows=[
        (1, '0.0091230274'), (2, '0.0013238191'), (4, '2.8153637e-5'), (8, '1.275627e-8'), (16, '2.6189019e-15')]),
    '(11) (2,1,2,1,2)': dict(deepest='(11)', rows=[
        (1, '0.0091230738'), (2, '0.0013238201'), (4, '2.8153637e-5'), (8, '1.275627e-8'), (16, '2.6189019e-15')]),
    '(6) (6) (11)': dict(deepest='(11)', rows=[
        (1, '0.0027602025'), (2, '0.00040134357'), (4, '8.5382782e-6'), (8, '3.8686794e-9'), (16, '7.9425188e-16')]),
    '(11) (6) (2,1,2,1,2)': dict(deepest='(11)', rows=[
        (1, '0.016860848'), (2, '0.0024290024'), (4, '5.1595765e-5'), (8, '2.3377173e-8'), (16, '4.799406e-15')]),
}
NOTE1_V3 = {      # n: (keeps line by columns, by rows, own value to 20 figures)
    6: (True, True, '3.6180339887498948482'),
    11: (True, True, '6.1180339887498948482'),
    16: (True, True, '8.6180339887498948482'),
    21: (True, True, '11.118033988749894848'),
    26: (True, True, '13.618033988749894848'),
    7: (False, False, '4.1180339887498948482'),
}
DEPARTURES = {'(6)': [6], '(11)': [11], '(2,1,2,1,2)': [2, 1, 2, 1, 2]}
KS = (1, 2, 4, 8, 16)


def part1():
    out('=' * 110)
    out('PART 1.   note 1: "THE READ-OUT AS A VALUE"   (cyclic run sequences; heights; departures)')
    out('=' * 110)
    out()
    out('Definitions used (the note, section 1): H_i = (r_i + x_i + y_i)/2 with x_i, y_i the continued fractions')
    out('read forward and backward round the cycle; the apex is the greatest H_i; the own value of a departure is')
    out('its apex when closed by 60 golden periods; the offset of a run is (x_i - y_i)/2.')
    out('"D closed by g golden periods" is read as D followed by 2g+1 runs of 1 (the note: L^n R (LR)^k, and')
    out('"L^6 R L R" = runs (6,1,1,1) for one period).  A composite of m factors at k has gaps k, k+1, ..., k+m-1.')
    out('The request describes a golden period as a pair of runs (1,1); read literally, "(6) closed by one period"')
    out('would be the run sequence (6,1,1).  Both readings are evaluated under the claim on L^6 R L R below.')
    out()

    # ---------------- self-checks of the instrument (not claims) ----------------
    rng = random.Random(20261111)
    samples = [[6, 1, 1, 1], closed([2, 1, 2, 1, 2], 1), composite([[6], [11]], 1)[0], [1, 1], [3, 2], [5]]
    for _ in range(40):
        n = rng.choice([2, 4, 6, 8, 10, 12, 3, 5, 7])
        samples.append([rng.randint(1, 7) for _ in range(n)])
    n_exact, n_exact_ok, worst = 0, 0, Decimal(0)
    for runs in samples:
        hs = heights(runs)
        qd = heights_integer_form(runs)
        for i, (H, x, y) in enumerate(hs):
            q, Dd = qd[i]
            n_exact += 1
            if Dd == H.D and H == Surd(0, Fraction(1, 2 * q), Dd):
                n_exact_ok += 1
            bx, by = cf_bruteforce(runs, i, 500)
            diff = abs((Decimal(runs[i]) + D_(bx) + D_(by)) / 2 - H.dec())
            if diff > worst:
                worst = diff
    out('self-check of the instrument on %d cyclic words (%d runs): the definition equals the integer form' % (len(samples), n_exact))
    out('   sqrt(D)/(2 q_i) exactly in %d of %d runs; largest difference from a 500-term numerical continued' % (n_exact_ok, n_exact))
    out('   fraction: %s' % f8(worst, 3))
    out()
    SELF['instrument_exact'] = (n_exact_ok == n_exact)
    SELF['instrument_numeric'] = (worst < Decimal('1e-100'))

    # the comparison itself: a claimed value changed by one unit in its last printed digit must be rejected
    probes = [(own_value([6])['dec'], NOTE1_OWN['(6)'], 20), (own_value([11])['dec'], NOTE1_OWN['(11)'], 20),
              (own_value([2, 1, 2, 1, 2])['dec'], NOTE1_OWN['(2,1,2,1,2)'], 20),
              (abs(analyse([[6], [6]], 1)['best'].dec() - own_value([6])['dec']), '0.01910438', 8),
              (abs(analyse([[6], [11]], 16)['best'].dec() - own_value([11])['dec']), '5.4438833e-15', 8)]
    accepted = rejected = 0
    for x, printed, nsig in probes:
        d = Decimal(printed)
        unit = Decimal(1).scaleb(d.as_tuple().exponent)
        if agree_printed(x, printed, nsig):
            accepted += 1
        for wrong in (d + unit, d - unit):
            if not agree_printed(x, str(wrong), nsig):
                rejected += 1
    out('self-check of the comparison: %d of %d claimed values accepted as printed; %d of %d rejected once their last'
        % (accepted, len(probes), rejected, 2 * len(probes)))
    out('   printed digit is changed by one unit')
    out()
    SELF['comparison'] = (accepted == len(probes) and rejected == 2 * len(probes))

    # ---------------- the ground ----------------
    g_ok = True
    g_vals = []
    for N in (2, 4, 10, 40):
        hs = heights([1] * N)
        for (H, x, y) in hs:
            sq = H * H
            if not (sq.b == 0 and sq.a == Fraction(5, 4) and H.sign() > 0):
                g_ok = False
        g_vals.append(hs[0][0].dec())
    claim('N1-s4: the ground (all runs 1) reads sqrt5/2.',
          'sqrt5/2', 'H^2 = 5/4 exactly at every run (cycle lengths 2, 4, 10, 40); H = %s' % f8(g_vals[0], 12), st(g_ok))

    # ---------------- LR's eigenvalue ----------------
    LR = mmul(L_NOTE, R_NOTE)
    phi = Q5(Fraction(1, 2), Fraction(1, 2))
    phi2 = phi * phi
    tr, det = LR[0][0] + LR[1][1], mdet(LR)
    eig_ok = (phi2 * phi2 - tr * phi2 + det).is_zero() and LR == ((1, 1), (1, 2))
    ok = eig_ok and agree_printed(PHI4, '6.8541') and agree_printed(FOUR_LN_PHI, '1.924847') and agree_printed(FOUR_LN_PHI, '1.9248473')
    claim("N1-s3: phi^2 is LR's eigenvalue; phi^4 = 6.8541; 4 ln phi = 1.924847.",
          'phi^4 = 6.8541; 4 ln phi = 1.924847 (result file 1.9248473)',
          'phi^2 is a root of the characteristic polynomial of LR: %s; phi^4 = %s; 4 ln phi = %s'
          % (eig_ok, f8(PHI4, 11), f8(FOUR_LN_PHI, 11)), st(ok), ['LR = %s (trace 3, determinant 1)' % flat(LR)])

    # ---------------- own values, V0 ----------------
    for name in ('(6)', '(11)', '(2,1,2,1,2)'):
        D = DEPARTURES[name]
        ov = own_value(D)
        lim = limit_own(D)
        d_lim = abs(ov['dec'] - lim.dec())
        NOTES.setdefault('own', {})[name] = (str(lim), d_lim)
        six = {'(6)': '3.618034', '(11)': '6.118034', '(2,1,2,1,2)': '1.723607'}[name]
        ok = agree_printed(ov['dec'], NOTE1_OWN[name], 20) and agree_printed(ov['dec'], six) and ov['inside'] and len(ov['ties']) == 1
        claim('N1-s2: own value of %s (apex when closed by 60 golden periods).' % name,
              '%s (text %s)' % (NOTE1_OWN[name], six),
              '%s' % f8(ov['dec'], 20), st(ok),
              ['apex at run %d of the departure, unique: %s; its offset (x-y)/2 is exactly zero: %s'
               % (ov['idx'] + 1, len(ov['ties']) == 1, ov['offset'].sign() == 0),
               'exact value in an infinite ground: %s = %s;  60-period value minus limit, in absolute value: %s'
               % (lim, f8(lim.dec(), 25), f8(d_lim, 3))])
    v0 = {}
    for name in ('(6)', '(2,1,2,1,2)'):
        v0[name] = abs(own_value(DEPARTURES[name])['dec'] - Decimal(B1857_APEX[name]))
    NOTES['v0'] = v0
    ok = all(v < Decimal('1e-6') for v in v0.values())
    claim("N1-V0: own values of (6) and (2,1,2,1,2) equal the record's two apexes to 1e-6.",
          'holds; the apexes are 3.618034 and 1.723607',
          'differences %s and %s' % (f8(v0['(6)'], 3), f8(v0['(2,1,2,1,2)'], 3)), st(ok),
          ["the two apexes are the record's printed six-place values (the findings of B1857 on the main line)"])

    # ---------------- V1 ----------------
    out('-' * 110)
    out('V1: copies of one departure.  Per row: k | apex at a copy | spread | distance | offset')
    out('  distance = greatest (copy height - own value) over the copies (it equals apex - own value: see each case);')
    out('  offset   = greatest absolute (x - y)/2 over the copies;  spread = greatest - least copy height.')
    out('-' * 110)
    v1_rule = True
    v1_rates = []
    v1_store = {}
    crossform_ok = True
    n_words = 0
    for name in ('(6)', '(11)', '(2,1,2,1,2)'):
        D = DEPARTURES[name]
        own = own_value(D)['dec']
        for m in (2, 3, 4):
            key = '%s x %d' % (name, m)
            note = NOTE1_V1[key]
            rows = []
            case_ok = True
            det_lines = []
            for (k, n_apex, n_spread, n_dist, n_off) in note['rows']:
                A = analyse([D] * m, k)
                n_words += 1
                hs = A['hs']
                idx_fast, _ = apex_fast(A['runs'])                 # cross-check with the integer form
                if sorted(idx_fast) != sorted(A['apex_idx']):
                    crossform_ok = False
                copies = [hs[i][0] for i in A['per']]
                cdec = [c.dec() for c in copies]
                hi, lo = copies[0], copies[0]
                for c in copies[1:]:
                    if c > hi:
                        hi = c
                    if c < lo:
                        lo = c
                spread_exact_zero = (hi == lo)
                spread = (hi - lo).dec()
                dist_copies = max(abs(c - own) for c in cdec)
                dist_apex = abs(A['best'].dec() - own)
                above = all(c > own for c in cdec)
                offs = [abs((hs[i][1] - hs[i][2]) / 2).dec() for i in A['per']]
                off_max = max(offs)
                off_apex = abs((hs[A['apex_idx'][0]][1] - hs[A['apex_idx'][0]][2]) / 2).dec()
                at_copy = all(span_of(i, A['spans']) is not None for i in A['apex_idx'])
                rows.append(dict(k=k, at_copy=at_copy, spread=spread, zero=spread_exact_zero, dist=dist_copies,
                                 dist_apex=dist_apex, off=off_max, off_apex=off_apex, above=above,
                                 n_apex=len(A['apex_idx'])))
                if m == 2:
                    sp_ok = spread_exact_zero and Decimal(n_spread) < Decimal('1e-45')
                    sp_txt = 'exactly 0' if spread_exact_zero else f8(spread)
                else:
                    sp_ok = agree_printed(spread, n_spread, 8)
                    sp_txt = f8(spread)
                r_ok = (at_copy == n_apex) and sp_ok and agree_printed(dist_copies, n_dist, 8) and agree_printed(off_max, n_off, 8)
                case_ok = case_ok and r_ok
                det_lines.append('k=%2d | here: %s | %s | %s | %s || note: %s | %s | %s | %s || %s'
                                 % (k, at_copy, sp_txt, f8(dist_copies), f8(off_max), n_apex, n_spread, n_dist, n_off,
                                    'same' if r_ok else 'DIFFERENT'))
            d8 = [r for r in rows if r['k'] == 8][0]['dist']
            d16 = [r for r in rows if r['k'] == 16][0]['dist']
            rate = (d8 / d16).ln() / 8
            v1_rates.append(rate)
            rate_ok = agree_printed(rate, note['rate'], 10)
            case_ok = case_ok and rate_ok
            det_lines.append('rate ln(d8/d16)/8: here %s, note %s; 4 ln phi = %s' % (f8(rate, 10), note['rate'], f8(FOUR_LN_PHI, 10)))
            det_lines.append('every copy reads above the own value: %s; distance at the apex equals the greatest over copies: %s'
                             % (all(r['above'] for r in rows), all(r['dist'] == r['dist_apex'] for r in rows)))
            falls = all(rows[i]['dist'] > rows[i + 1]['dist'] and rows[i]['off'] > rows[i + 1]['off'] for i in range(len(rows) - 1))
            small = rows[-1]['dist'] < Decimal('1e-12') and rows[-1]['off'] < Decimal('1e-12')
            within = abs(rate / FOUR_LN_PHI - 1) < Decimal('0.05')
            if m == 2:
                spr = all(r['zero'] for r in rows)
            else:
                spr = all(rows[i]['spread'] > rows[i + 1]['spread'] for i in range(len(rows) - 1))
            rule = all(r['at_copy'] for r in rows) and falls and small and within and spr
            v1_rule = v1_rule and rule
            det_lines.append('sealed rule for this case (apex at a copy; falls strictly; below 1e-12 at k=16; rate within 5%%; spread %s): %s'
                             % ('zero' if m == 2 else 'falls', rule))
            v1_store[key] = rows
            claim('N1-V1: %s: distance, offset, spread at k = 1,2,4,8,16 and the rate.' % key,
                  'distance %s; rate %s' % (', '.join(r[3] for r in note['rows']), note['rate']),
                  'distance %s; rate %s' % (', '.join(f8(r['dist']) for r in rows), f8(rate, 10)),
                  st(case_ok), det_lines)
    claim('N1-V1 cell: the sealed rule holds in all nine cases.',
          'holds, all 9', 'rule satisfied in all nine: %s' % v1_rule, st(v1_rule),
          ['apex positions agree with the integer form (least q_i) in every word: %s' % crossform_ok])

    # ---------------- V2 ----------------
    out('-' * 110)
    out('V2: different departures.  Per row: k | apex unique | at the deepest departure | distance from its own value')
    out('-' * 110)
    v2_rule = True
    v2_store = {}
    v2_facs = {}
    for key in ('(6) (11)', '(6) (2,1,2,1,2)', '(11) (2,1,2,1,2)', '(6) (6) (11)', '(11) (6) (2,1,2,1,2)'):
        note = NOTE1_V2[key]
        names = key.split(' ')
        facs = [DEPARTURES[n] for n in names]
        owns = [own_value(f)['dec'] for f in facs]
        deepest_val = max(owns)
        deepest_names = sorted(set(n for n, o in zip(names, owns) if o == deepest_val))
        v2_facs[key] = (facs, owns, deepest_val)
        rows = []
        det_lines = []
        case_ok = (deepest_names == [note['deepest']])
        for (k, n_dist) in note['rows']:
            A = analyse(facs, k)
            n_words += 1
            unique = len(A['apex_idx']) == 1
            sp = span_of(A['apex_idx'][0], A['spans'])
            at_deepest = sp is not None and owns[sp] == deepest_val
            dist = abs(A['best'].dec() - deepest_val)
            where = 'the run of %d' % A['runs'][A['apex_idx'][0]]
            rows.append(dict(k=k, unique=unique, at_deepest=at_deepest, dist=dist, where=where))
            r_ok = unique and at_deepest and agree_printed(dist, n_dist, 8)
            case_ok = case_ok and r_ok
            det_lines.append('k=%2d | here: %s | %s (%s) | %s || note: True | True | %s || %s'
                             % (k, unique, at_deepest, where, f8(dist), n_dist, 'same' if r_ok else 'DIFFERENT'))
        falls = all(rows[i]['dist'] > rows[i + 1]['dist'] for i in range(len(rows) - 1))
        rule = all(r['unique'] and r['at_deepest'] for r in rows) and falls and rows[-1]['dist'] < Decimal('1e-12')
        v2_rule = v2_rule and rule
        det_lines.append('sealed rule for this case (unique apex at the deepest; falls strictly; below 1e-12 at k=16): %s' % rule)
        v2_store[key] = rows
        claim('N1-V2: %s: apex unique at the deepest departure; distance at k = 1,2,4,8,16.' % key,
              'deepest %s; distance %s' % (note['deepest'], ', '.join(r[1] for r in note['rows'])),
              'deepest %s; distance %s' % ('/'.join(deepest_names), ', '.join(f8(r['dist']) for r in rows)),
              st(case_ok), det_lines)
    claim('N1-V2 cell: the sealed rule holds in all five composites.',
          'holds, all 5', 'rule satisfied in all five: %s' % v2_rule, st(v2_rule))
    claim('N1-s2: the card has 70 composites (14 cases at five values of k).',
          '70', '%d words evaluated for V1 and V2' % n_words, st(n_words == 70))

    # ---------------- V3 ----------------
    det_lines = []
    v3_keep_ok = True
    kept, notkept = [], []
    for n in (6, 11, 16, 21, 26, 7):
        ks = [keeps(closed([n], g)) for g in (0, 1, 2, 5, 60)]
        col = all(x['column'] for x in ks)
        row = all(x['row'] for x in ks)
        col_any = any(x['column'] for x in ks)
        row_any = any(x['row'] for x in ks)
        ok = (col == NOTE1_V3[n][0]) and (row == NOTE1_V3[n][1]) and (col == col_any) and (row == row_any)
        v3_keep_ok = v3_keep_ok and ok
        if col and row:
            kept.append(n)
        if not col_any and not row_any:
            notkept.append(n)
        det_lines.append('n=%2d: by columns %s, by rows %s (the same at closures 0, 1, 2, 5, 60: %s); note: %s, %s'
                         % (n, col, row, col == col_any and row == row_any, NOTE1_V3[n][0], NOTE1_V3[n][1]))
    claim('N1-V3: runs 6, 11, 16, 21, 26 keep the line (1,3); the control 7 does not.',
          'keep: 6, 11, 16, 21, 26; not: 7', 'keep: %s; not: %s' % (', '.join(map(str, kept)), ', '.join(map(str, notkept))),
          st(v3_keep_ok), det_lines)

    det_lines = []
    v3_val_ok = True
    worst = Decimal(0)
    prev = None
    incr = True
    for n in (6, 11, 16, 21, 26, 7):
        ov = own_value([n])['dec']
        formula = (Decimal(n) - 1) / 2 + SQRT5 / 2
        d = abs(ov - formula)
        if n != 7:
            worst = max(worst, d)
            if prev is not None and not ov > prev:
                incr = False
            prev = ov
        ok = d < Decimal('1e-40') and agree_printed(ov, NOTE1_V3[n][2], 20)
        v3_val_ok = v3_val_ok and ok
        det_lines.append('n=%2d: own value %s (note %s); distance from (n-1)/2 + sqrt5/2: %s'
                         % (n, f8(ov, 20), NOTE1_V3[n][2], f8(d, 3)))
    text_ok = all(agree_printed(own_value([n])['dec'], s) for n, s in ((6, '3.618'), (11, '6.118'), (16, '8.618'), (21, '11.118'), (26, '13.618')))
    claim('N1-V3: their own values are (n-1)/2 + sqrt5/2 to 1e-40, and increase.',
          '3.618, 6.118, 8.618, 11.118, 13.618; formula to 1e-40',
          '%s; greatest distance from the formula %s; increasing: %s'
          % (', '.join(f8(own_value([n])['dec'], 7) for n in (6, 11, 16, 21, 26)), f8(worst, 3), incr),
          st(v3_val_ok and incr and text_ok), det_lines)
    claim('N1-V3 cell: line kept, formula to 1e-40, increasing, control 7 fails.',
          'holds', 'line: %s; values: %s; increasing: %s' % (v3_keep_ok, v3_val_ok, incr), st(v3_keep_ok and v3_val_ok and incr))

    # ---------------- text numbers of section 2 ----------------
    txt = {1: '0.019', 2: '0.0028', 4: '5.9e-5', 8: '2.7e-8', 16: '5.4e-15'}
    ok = True
    det_lines = []
    for k in KS:
        vals = [[r for r in v1_store['(6) x %d' % m] if r['k'] == k][0]['dist'] for m in (2, 3, 4)]
        same2 = len(set(round_sig(v, 2) for v in vals)) == 1
        good = all(agree_printed(v, txt[k]) for v in vals)
        ok = ok and same2 and good
        det_lines.append('k=%2d: 2, 3, 4 copies: %s  -> to two figures all %s: %s' % (k, ', '.join(f8(v) for v in vals), txt[k], good and same2))
    claim('N1-s2: copies of (6): distance 0.019, 0.0028, 5.9e-5, 2.7e-8, 5.4e-15, same for 2, 3, 4 copies.',
          '0.019, 0.0028, 5.9e-5, 2.7e-8, 5.4e-15',
          ', '.join(f8([r for r in v1_store['(6) x 2'] if r['k'] == k][0]['dist'], 2) for k in KS) + ' in all three cases',
          st(ok), det_lines)

    a_off = [[r for r in v1_store['(6) x %d' % m] if r['k'] == 1][0]['off_apex'] for m in (2, 3, 4)]
    g_off = [[r for r in v1_store['(6) x %d' % m] if r['k'] == 1][0]['off'] for m in (2, 3, 4)]
    NOTES['off'] = (a_off, g_off)
    ok = all(agree_printed(v, '0.014') for v in a_off) and agree_printed(max(g_off), '0.017')
    claim("N1-s2: at k = 1 the apex's own offset is 0.014, the greatest over the copies 0.017.",
          '0.014; 0.017', "apex's own %s; greatest over copies %s (2, 3, 4 copies)"
          % (', '.join(f8(v, 5) for v in a_off), ', '.join(f8(v, 5) for v in g_off)), st(ok),
          ['0.017 is the four-copy case; with three copies the greatest is %s, with two it is the apex\'s own' % f8(g_off[1], 5)])

    d6 = [r for r in v1_store['(6) x 2'] if r['k'] == 1][0]['dist']
    d11 = [[r for r in v1_store['(11) x %d' % m] if r['k'] == 1][0]['dist'] for m in (2, 3, 4)]
    d2 = [[r for r in v1_store['(2,1,2,1,2) x %d' % m] if r['k'] == 1][0]['dist'] for m in (2, 3, 4)]
    ratio = d6 / d2[0]
    NOTES['ratio27'] = (ratio, d11[0] / d2[0])
    ok = all(agree_printed(v, '0.023') for v in d11) and all(agree_printed(v, '0.00069') for v in d2) and abs(ratio - 27) <= 1
    claim('N1-s2: copies of (11): 0.023 at k = 1; of (2,1,2,1,2): 0.00069, about 27 times closer.',
          '0.023; 0.00069; about 27', '%s; %s; ratio to copies of (6) %s'
          % (f8(d11[0], 5), f8(d2[0], 5), f8(ratio, 5)), st(ok),
          ['the ratio is %s: "about 27" is a truncation (it rounds to 28); against copies of (11) the ratio is %s'
           % (f8(ratio, 4), f8(d11[0] / d2[0], 4))])

    ok = all(agree_printed(r, '1.924847') for r in v1_rates) and agree_printed(FOUR_LN_PHI, '1.924847')
    claim('N1-s2: the rate between k = 8 and 16 is 1.924847 in all nine cases.',
          '1.924847 in all nine; 4 ln phi = 1.924847',
          'nine rates from %s to %s; 4 ln phi = %s' % (f8(min(v1_rates), 10), f8(max(v1_rates), 10), f8(FOUR_LN_PHI, 10)), st(ok))

    who = {}
    for key, rows in v2_store.items():
        who[key] = sorted(set(r['where'] for r in rows))
    want = {'(6) (11)': ['the run of 11'], '(11) (2,1,2,1,2)': ['the run of 11'], '(6) (6) (11)': ['the run of 11'],
            '(11) (6) (2,1,2,1,2)': ['the run of 11'], '(6) (2,1,2,1,2)': ['the run of 6']}
    d1 = [[r for r in rows if r['k'] == 1][0]['dist'] for rows in v2_store.values()]
    d16 = [[r for r in rows if r['k'] == 16][0]['dist'] for rows in v2_store.values()]
    ok = (who == want) and agree_printed(min(d1), '0.003') and agree_printed(max(d1), '0.019') and max(d16) < Decimal('6e-15')
    claim('N1-s2: different departures read the run of 11 (or 6); distance 0.003 to 0.019, then below 6e-15.',
          'run of 11 in four, run of 6 in (6)(2,1,2,1,2); 0.003 to 0.019 at k=1; below 6e-15 at k=16',
          'run of 11 in four, run of 6 in (6) (2,1,2,1,2): %s; k=1: %s to %s; k=16: greatest %s'
          % (who == want, f8(min(d1), 4), f8(max(d1), 4), f8(max(d16), 4)), st(ok),
          ['%s: %s' % (k, '/'.join(v)) for k, v in who.items()])

    # ---------------- section 3: the limit ----------------
    own6 = own_value([6])['dec']

    def dist2(D, k, ref):
        runs, spans = composite([D, D], k)
        _, apex = apex_fast(runs)
        return apex - ref

    dd = {k: dist2([6], k, own6) for k in range(1, 8)}
    ratios = [dd[k] / dd[k + 1] for k in range(1, 6)]
    note_r5 = ['6.93509', '6.86577', '6.8558', '6.85435', '6.85414']
    note_txt = ['6.935', '6.866', '6.856', '6.8543', '6.8541']
    ok_json = all(agree_printed(r, s, 6) for r, s in zip(ratios, note_r5))
    ok_txt = [agree_printed(r, s) for r, s in zip(ratios, note_txt)]
    claim('N1-s3: step ratios, two copies of (6): 6.935, 6.866, 6.856, 6.8543, 6.8541.',
          '6.935, 6.866, 6.856, 6.8543, 6.8541 (result file: %s); phi^4 = 6.8541' % ', '.join(note_r5),
          '%s; phi^4 = %s' % (', '.join(f8(r, 9) for r in ratios), f8(PHI4, 9)),
          st(ok_json and all(ok_txt)),
          ['equal to the result file\'s six figures: %s; to the text\'s figures: %s' % (ok_json, ok_txt)])

    lim_lines = []
    lim_ok = True
    for name in ('(6)', '(11)', '(2,1,2,1,2)'):
        D = DEPARTURES[name]
        ref = limit_own(D).dec()
        dk = {k: dist2(D, k, ref) for k in (5, 6, 10, 11, 20, 21, 30, 31)}
        devs = [abs(dk[k] / dk[k + 1] - PHI4) for k in (5, 10, 20, 30)]
        NOTES.setdefault('devs', {})[name] = devs
        mono = all(devs[i] > devs[i + 1] for i in range(3))
        lim_ok = lim_ok and mono and devs[-1] < Decimal('1e-20') and all(v > 0 for v in dk.values())
        lim_lines.append('two copies of %s: distance of d(k)/d(k+1) from phi^4 at k = 5, 10, 20, 30: %s' % (name, ', '.join(f8(v, 3) for v in devs)))
    for n in (6, 11):
        Cn = SQRT5 * (n - 1) * (1 + PHI ** -4) / (2 * (n - 1 + SQRT5) * PHI4)
        ref = limit_own([n]).dec()
        v30 = dist2([n], 30, ref) * PHI ** 120
        lim_ok = lim_ok and abs(v30 / Cn - 1) < Decimal('1e-20')
        NOTES.setdefault('Cn', {})[n] = Cn
        lim_lines.append('run of %d: d(30)*phi^120 = %s; closed form sqrt5 (n-1)(1+phi^-4)/(2 (n-1+sqrt5) phi^4) = %s'
                         % (n, f8(v30, 25), f8(Cn, 25)))
    claim('N1-head: the distance falls by a factor tending to phi^4 per golden period.',
          'factor tends to phi^4 = 6.8541', 'ratios converge to phi^4 = %s for all three departures: %s' % (f8(PHI4, 12), lim_ok),
          st(lim_ok), lim_lines + ['(derived here: [0;1^m,u] - 1/phi = (-1)^(m-1) (u - phi)/((F_(m+1) u + F_m) phi^(m+1)), with m = 2g+1 ones)'])

    deep_ok = True
    deep_lines = []
    for key, (facs, owns, deepest_val) in v2_facs.items():
        res = []
        for k in (20, 30, 31):
            runs, spans = composite(facs, k)
            idx, apex = apex_fast(runs)
            sp = span_of(idx[0], spans)
            res.append((len(idx) == 1 and sp is not None and owns[sp] == deepest_val, apex - deepest_val))
        good = all(r[0] for r in res) and res[1][1] > 0 and abs(res[1][1] / res[2][1] - PHI4) < Decimal('1e-15') and res[1][1] < Decimal('1e-24')
        deep_ok = deep_ok and good
        deep_lines.append('%s: unique apex at the deepest at k = 20, 30, 31: %s; distance at k = 30: %s; d(30)/d(31) = %s'
                          % (key, all(r[0] for r in res), f8(res[1][1], 4), f8(res[1][1] / res[2][1], 12)))
    claim('N1-head: with long gaps a history with several departures reads the deepest one.',
          'reads the deepest in the limit (card: gaps to 19 periods)',
          'the five composites at k = 20, 30, 31: unique apex at the deepest, distance still falling by phi^4: %s' % deep_ok,
          st(deep_ok), deep_lines)

    tie = all(r['zero'] and r['n_apex'] == 2 for m2 in ('(6) x 2', '(11) x 2', '(2,1,2,1,2) x 2') for r in v1_store[m2])
    sp_rates = []
    for name in ('(6)', '(11)', '(2,1,2,1,2)'):
        for m in (3, 4):
            rows = v1_store['%s x %d' % (name, m)]
            s8 = [r for r in rows if r['k'] == 8][0]['spread']
            s16 = [r for r in rows if r['k'] == 16][0]['spread']
            sp_rates.append((s8 / s16).ln() / 8)
    ok = tie and all(abs(r / FOUR_LN_PHI - 1) < Decimal('1e-6') for r in sp_rates)
    claim('N1-s3: two copies tie exactly; three and four differ by amounts falling at the same rate.',
          'exact tie; same rate', 'two copies: equal heights exactly, apex attained twice: %s; spread rates (k 8 to 16) %s to %s'
          % (tie, f8(min(sp_rates), 10), f8(max(sp_rates), 10)), st(ok),
          ["the note's result file prints 3.1e-61 and 1.6e-61 for three of the fifteen two-copy spreads; exact arithmetic gives 0 (rounding noise there)"])

    # ---------------- section 3: short gaps ----------------
    pct_card = d6 / own6 * 100
    claim("N1-s3: at the card's k = 1 the run of 6 reads half a percent off.",
          'half a percent', '%s percent' % f8(pct_card, 4), st(Decimal('0.45') <= pct_card < Decimal('0.55')))

    h61 = max(h for h, _, _ in heights(closed([6], 1)))
    h61d = h61.dec()
    pct6 = (h61d - own6) / own6 * 100
    alt = max(h for h, _, _ in heights([6, 1, 1])).dec()
    NOTES['one_period'] = (h61d, alt)
    ok = agree_printed(h61d, '3.6515') and agree_printed(h61d, '3.651483717') and agree_printed(own6, '3.6180') \
        and agree_printed(pct6, '0.9245') and Decimal('0.9') <= pct6 < 1
    claim('N1-s3: L^6 R L R reads 3.6515 against 3.6180, nearly one percent.',
          '3.6515 (3.651483717); 3.6180; 0.9245 percent', '%s; %s; %s percent' % (f8(h61d, 10), f8(own6, 10), f8(pct6, 4)), st(ok),
          ['exactly sqrt(40/3): H^2 == 40/3 is %s' % ((h61 * h61).b == 0 and (h61 * h61).a == Fraction(40, 3)),
           'the other reading of "one period" (runs 6,1,1, an odd cycle) gives %s, which is not the note\'s value' % f8(alt, 10)])

    h111 = max(h for h, _, _ in heights(closed([11], 1))).dec()
    own11 = own_value([11])['dec']
    pct11 = (h111 - own11) / own11 * 100
    ok = agree_printed(h111, '6.157651067') and agree_printed(pct11, '0.6475') and agree_printed(pct11, '0.65')
    claim('N1-s3: (11) with one period on both sides is 0.65 percent off.',
          '0.65 percent (6.157651067 against 6.118033989; 0.6475)', '%s against %s; %s percent' % (f8(h111, 10), f8(own11, 10), f8(pct11, 4)), st(ok))

    A12 = analyse([[6], [6]], 1)
    h12 = A12['best'].dec()
    ok = agree_printed(h12, '3.6371') and agree_printed(h12, '3.637138368') and h12 < h61d
    claim('N1-s3: (6)_1 (6)_2 reads 3.6371, below (6)_1 alone at 3.6515.',
          '3.6371 (3.637138368), below 3.6515', '%s, below %s: %s' % (f8(h12, 10), f8(h61d, 10), h12 < h61d), st(ok))

    Adep, Bdep = [2, 1, 1, 4, 4], [2, 1, 2, 4, 4]
    ownA, ownB = own_value(Adep), own_value(Bdep)
    kA = [keeps(closed(Adep, g)) for g in (1, 2, 3, 7)]
    kB = [keeps(closed(Bdep, g)) for g in (1, 2, 3, 7)]
    keep_ok = all(x['row'] and x['column'] for x in kA + kB)
    NOTES['AB'] = (str(limit_own(Adep)), str(limit_own(Bdep)))
    ok = keep_ok and agree_printed(ownA['dec'], '2.418183') and agree_printed(ownB['dec'], '2.423508') \
        and agree_printed(ownA['dec'], '2.41818304', 9) and agree_printed(ownB['dec'], '2.423507871') \
        and kA[0]['gv'] == (1, 3) and kA[0]['vg'] == (1, 3) and kB[0]['gv'] == (1, 3) and kB[0]['vg'] == (1, 3)
    claim('N1-s3: A = (2,1,1,4,4), B = (2,1,2,4,4) keep the line; own values 2.418183, 2.423508.',
          'both keep (g v = [1,3], v g = [1,3]); 2.41818304, 2.423507871',
          'both keep: %s (g v = %s, v g = %s for A_1; %s, %s for B_1); %s, %s'
          % (keep_ok, list(kA[0]['gv']), list(kA[0]['vg']), list(kB[0]['gv']), list(kB[0]['vg']),
             f8(ownA['dec'], 10), f8(ownB['dec'], 10)), st(ok),
          ['exact limits in an infinite ground: A %s = %s; B %s = %s'
           % (limit_own(Adep), f8(limit_own(Adep).dec(), 12), limit_own(Bdep), f8(limit_own(Bdep).dec(), 12)),
           'difference of the two own values: %s' % f8(ownB['dec'] - ownA['dec'], 5)])

    note_ab = {1: ('A', '2.425956224', '2.425956224', '2.424539515'), 2: ('B', '2.423658265', '2.419310441', '2.423658265'),
               4: ('B', '2.423511072', '2.418207014', '2.423511072'), 8: ('B', '2.423507873', '2.418183051', '2.423507873')}
    ab = {}
    for g in range(1, 31):
        A = analyse([Adep, Bdep], g)
        sp = span_of(A['apex_idx'][0], A['spans'])
        bestA = A['hs'][A['per'][0]][0].dec()
        bestB = A['hs'][A['per'][1]][0].dec()
        kk = keeps(A['runs'])
        ab[g] = dict(where=('A' if sp == 0 else 'B' if sp == 1 else 'ground'), apex=A['best'].dec(), bestA=bestA, bestB=bestB,
                     unique=len(A['apex_idx']) == 1, keeps=kk['row'] and kk['column'])
    ok = ab[1]['where'] == 'A' and agree_printed(ab[1]['apex'], '2.425956') and agree_printed(ab[1]['apex'], '2.425956224') \
        and agree_printed(ab[1]['bestB'], '2.424539515') and ab[1]['keeps']
    claim('N1-s3: in A_1 B_2 the apex is in A, the shallower, at 2.425956.',
          'apex in A at 2.425956224; best of B 2.424539515; the composite keeps the line',
          'apex in %s at %s; best of B %s; keeps the line: %s'
          % (ab[1]['where'], f8(ab[1]['apex'], 10), f8(ab[1]['bestB'], 10), ab[1]['keeps']), st(ok))
    ok = True
    det_lines = []
    for g in (2, 4, 8):
        w, apx, bA, bB = note_ab[g]
        r = ab[g]
        good = r['where'] == w and agree_printed(r['apex'], apx) and agree_printed(r['bestA'], bA) and agree_printed(r['bestB'], bB) and r['keeps']
        ok = ok and good
        det_lines.append('A_%d B_%d: apex in %s at %s; best of A %s; best of B %s; keeps the line %s || note: %s, %s, %s, %s'
                         % (g, g + 1, r['where'], f8(r['apex'], 10), f8(r['bestA'], 10), f8(r['bestB'], 10), r['keeps'], w, apx, bA, bB))
    claim('N1-s3: in A_2 B_3, A_4 B_5, A_8 B_9 the apex is in B.',
          'in B at 2.423658265, 2.423511072, 2.423507873', 'in %s at %s'
          % ('/'.join(ab[g]['where'] for g in (2, 4, 8)), ', '.join(f8(ab[g]['apex'], 10) for g in (2, 4, 8))), st(ok), det_lines)
    inB = [g for g in range(2, 13) if ab[g]['where'] == 'B' and ab[g]['unique']]
    claim('N1-s3: for every gap from 2 to 12 the apex of A_g B_(g+1) is in B.',
          'in B for g = 2..12', 'in B for g = %s; also for every g up to 30: %s'
          % (','.join(str(g) for g in inB), all(ab[g]['where'] == 'B' for g in range(2, 31))), st(inB == list(range(2, 13))))
    o6, o11, o2 = own_value([6])['dec'], own_value([11])['dec'], own_value([2, 1, 2, 1, 2])['dec']
    gaps = sorted([o11 - o6, o6 - o2, o11 - o2])
    claim("N1-s3: the card's departures are 1.89 or more apart in own value.",
          '1.89 or more', 'least difference %s (the others %s, %s)' % (f8(gaps[0], 7), f8(gaps[1], 7), f8(gaps[2], 7)),
          st(agree_printed(gaps[0], '1.89')))

    # ---------------- section 4 ----------------
    LRm = mmod(mmul(L_NOTE, R_NOTE), 5)
    powers = []
    P = I2
    for j in range(60):
        if P in powers:
            break
        powers.append(P)
        P = mmod(mmul(P, LRm), 5)
    order = len(powers)
    L5 = mmod(mpow(L_NOTE, 5), 5) == I2
    mismatches = 0
    tested = 0
    for n in range(1, 61):
        for k in range(0, 13):
            g = mmod(word_matrix([n] + [1] * (2 * k + 1), L_NOTE, R_NOTE), 5)
            tested += 1
            if (g in powers) != (n % 5 == 1):
                mismatches += 1
    seven = mmod(word_matrix(closed([7], 3), L_NOTE, R_NOTE), 5) in powers
    claim('N1-s4: L^n R (LR)^k is a power of LR mod 5 exactly when n = 1 mod 5.',
          'exactly when n = 1 mod 5 (L^5 = I mod 5); the control 7 is not',
          '%d pairs (n up to 60, k up to 12): %d exceptions; L^5 = I mod 5: %s; n = 7 a power: %s'
          % (tested, mismatches, L5, seven), st(L5 and mismatches == 0 and not seven),
          ['LR has order %d modulo 5' % order])

    fam_ok = True
    last = None
    big = []
    for n in list(range(6, 502, 5)) + [5 * 10 ** 6 + 1, 5 * 10 ** 12 + 1]:
        kk = keeps(closed([n], 1))
        _, val = apex_fast(closed([n], OWN_PERIODS))
        d = abs(val - ((Decimal(n) - 1) / 2 + SQRT5 / 2))
        if not (kk['row'] and kk['column'] and d < Decimal('1e-40') and (last is None or val > last)):
            fam_ok = False
        last = val
        if n > 10 ** 6:
            big.append((n, val))
    others = [n for n in range(2, 200) if n % 5 != 1 and (keeps(closed([n], 1))['row'] or keeps(closed([n], 1))['column'])]
    claim('N1-s4: allowed single runs have own values (n-1)/2 + sqrt5/2: no greatest.',
          'no greatest own value', 'n = 6, 11, ..., 501 and 5e6+1, 5e12+1 all keep the line and match the formula to 1e-40: %s' % fam_ok,
          st(fam_ok and not others),
          ['for example n = %d: own value %s' % (big[-1][0], f8(big[-1][1], 25)),
           'single runs n below 200 with n not 1 mod 5 that keep the line by rows or columns: %s' % (others if others else 'none')])

    lv_ok = True
    lv_lines = []
    for Sset in ([5], [5, 7], [3, 5, 11], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [5, 25, 125]):
        lcm = 1
        for N in Sset:
            lcm = lcm * N // math.gcd(lcm, N)
        good = True
        for j in (1, 2, 3):
            n = 1 + lcm * j
            for N in Sset:
                for k in (0, 1, 4):
                    lhs = mmod(word_matrix([n] + [1] * (2 * k + 1), L_NOTE, R_NOTE), N)
                    rhs = mmod(mpow(mmul(L_NOTE, R_NOTE), k + 1), N)
                    if lhs != rhs:
                        good = False
        n_bad = 2 + lcm
        bad_fails = any(mmod(word_matrix([n_bad, 1], L_NOTE, R_NOTE), N) != mmod(mmul(L_NOTE, R_NOTE), N) for N in Sset)
        lv_ok = lv_ok and good and bad_fails
        lv_lines.append('levels %s: lcm %d; runs 1 + lcm*j (j = 1, 2, 3) are powers of LR at every level: %s' % (Sset, lcm, good))
    claim('N1-s4: the same holds at any finite set of levels.',
          'holds at any finite set of levels', 'five sets of levels tested: %s' % lv_ok, st(lv_ok),
          lv_lines + ['(the general reason: L^m = [[1,0],[m,1]] is the identity mod N exactly when N divides m)'])

    cnt = 0
    viol = 0
    equal_cases = 0
    for N in range(1, 9):
        for runs in itertools.product((1, 2, 3, 4), repeat=N):
            if any(runs[i:] + runs[:i] < runs for i in range(1, N)):
                continue                                   # one rotation of each cyclic word
            cnt += 1
            qd = heights_integer_form(list(runs))
            q, Dd = min(qd)
            c = Fraction(Dd, 4 * q * q) - Fraction(5, 4)   # apex^2 - 5/4, exactly
            if c < 0:
                viol += 1
            if c == 0:
                equal_cases += 1
                if set(runs) != {1}:
                    viol += 1
    claim('N1-s4: every apex is at least sqrt5/2 (quoted from the record).',
          'every apex at least sqrt5/2', '%d cyclic words (runs 1 to 4, length up to 8): %d below sqrt5/2; equality only for the all-ones words (%d)'
          % (cnt, viol, equal_cases), st(viol == 0),
          ['elementary reason: a greatest run r >= 3 gives H > 3/2; r = 2 gives H > (2 + 2/3)/2 = 4/3; both exceed sqrt5/2 = 1.118...'])

    claim('N1-s2: eight of the 70 composites were already computed by an earlier card.',
          '8 of 70', "needs the earlier card's word list; a statement about provenance, not a number of this note", NOTRE)
    claim('N1-s4: at one common fibre area no lightest level is lowest.',
          'none is lowest (under one stated assumption)',
          "rests on the record's spectral model; only its input, no greatest height, is recomputed above", NOTRE)

    # ---------------- the convention for L and R ----------------
    out('-' * 110)
    out('Convention for L and R (an ambiguity, not a claim).')
    lr_req = mmul(L_REQ, R_REQ)
    for (nm, Lm, Rm) in (("the notes' (note 2, R7: LR = [[1,1],[1,2]])", L_NOTE, R_NOTE), ('as written in the request (LR = [[2,1],[1,1]])', L_REQ, R_REQ)):
        for v in ((1, 3), (1, 2)):
            res = []
            for n in (6, 11, 16, 21, 26, 7):
                good = [g for g in range(12) if (lambda kk: kk['row'] and kk['column'])(keeps(closed([n], g), Lm, Rm, v))]
                res.append('%d:%s' % (n, 'always' if len(good) == 12 else 'never' if not good else 'only at ' + ','.join(map(str, good))))
            lr = mmul(Lm, Rm)
            eig = proportional(rowact(v, lr), v)
            NOTES.setdefault('conv', []).append((flat(lr), v, eig, '  '.join(res)))
            out('  %-48s line %s is a line of LR: %-5s' % (nm, v, eig))
            out('       run:closures 0 to 11 at which it keeps that line, by rows and columns:  %s' % '  '.join(res))
    out('  With L = [[1,1],[0,1]], R = [[1,0],[1,1]] multiplied left to right, LR = %s and its line mod 5 is (1,2), not (1,3);' % flat(lr_req))
    out('  (1,3) is then the line of RL, and whether L^n R (LR)^k keeps (1,3) depends on k: it is not a property of the run.')
    out('  The two conventions differ by exchanging L and R (or the reading direction), and every line-keeping statement of')
    out("  note 1 is the same once the mark is taken as LR's own line.  Heights do not depend on it.")
    out()


# ========================================================================================
# PART 2.  level 5: the two groups, the dual involution, the mirror
# ========================================================================================

S_ = ((0, -1), (1, 0))
T_ = ((1, 1), (0, 1))
Ti_ = ((1, -1), (0, 1))
G_FRAME = ((0, -1), (1, 3))          # g with (0,1) g = v
W5 = ((0, -1), (5, 0))
W_MARK = ((-3, -14), (1, 3))
DELTA = ((-5, -6), (-4, -5))
F_TICK = ((0, 1), (1, 1))
M_MIRROR = ((-1, -1), (0, 1))


def canon_line(w):
    w = (w[0] % 5, w[1] % 5)
    lead = w[0] if w[0] else w[1]
    inv = pow(lead, -1, 5)
    return ((w[0] * inv) % 5, (w[1] * inv) % 5)


def canon_pm(w):
    w = (w[0] % 5, w[1] % 5)
    n = ((-w[0]) % 5, (-w[1]) % 5)
    return min(w, n)


def in_line(h, v=V):
    return mdet(h) == 1 and proportional(rowact(v, h), v)


def in_pm(h, v=V):
    w = rowact(v, h)
    return mdet(h) == 1 and (w == (v[0] % 5, v[1] % 5) or w == ((-v[0]) % 5, (-v[1]) % 5))


def cycles(perm):
    seen, cyc = set(), []
    for p in perm:
        if p in seen:
            continue
        c, x = [], p
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = perm[x]
        cyc.append(c)
    return cyc


def orbit_structure(v, canon):
    """The right cosets G\\SL(2,Z) of the stabiliser G of canon(v), as the orbit of canon(v) under right
    multiplication; the permutations of S, T and ST; coset representatives; Schreier generators of G."""
    start = canon(v)
    reps = {start: I2}
    queue = [start]
    while queue:
        p = queue.pop(0)
        for X in (S_, T_, Ti_):
            q = canon(rowact(p, X))
            if q not in reps:
                reps[q] = mmul(reps[p], X)
                queue.append(q)
    pts = sorted(reps)
    perm = {}
    for nm, X in (('S', S_), ('T', T_), ('ST', mmul(S_, T_))):
        perm[nm] = dict((p, canon(rowact(p, X))) for p in pts)
    gens = []
    for p in pts:
        for X in (S_, T_):
            q = canon(rowact(p, X))
            h = mmul(mmul(reps[p], X), minv(reps[q]))
            if h not in (I2, mneg(I2)) and h not in gens and mneg(h) not in gens and minv(h) not in gens and mneg(minv(h)) not in gens:
                gens.append(h)
    gens.append(mneg(I2))
    cT = cycles(perm['T'])
    cS = cycles(perm['S'])
    cU = cycles(perm['ST'])
    widths = sorted(len(c) for c in cT)
    e2 = sum(1 for c in cS if len(c) == 1)
    e3 = sum(1 for c in cU if len(c) == 1)
    mu = len(pts)
    genus = 1 + Fraction(mu, 12) - Fraction(e2, 4) - Fraction(e3, 3) - Fraction(len(cT), 2)
    genus_euler = Fraction(2 + mu - (len(cS) + len(cU) + len(cT)), 2)       # 2g - 2 = mu - (cycles of S, ST, T)
    return dict(points=pts, reps=reps, perm=perm, gens=gens, index=mu, widths=widths, e2=e2, e3=e3,
                genus=genus, genus_euler=genus_euler, S_fixed=[c[0] for c in cS if len(c) == 1])


def conj_by(Wm, h):
    """W h W^-1 for an integer W of non-zero determinant; returns the matrix when it is integral, else None"""
    d = mdet(Wm)
    N = mmul(mmul(Wm, h), madj(Wm))
    if any(x % d for x in flat(N)):
        return None
    return ((N[0][0] // d, N[0][1] // d), (N[1][0] // d, N[1][1] // d))


def mobius_c5(A, z):
    """(a z + b)/(c z + d) on an element of Q(sqrt5)(i)"""
    return (A[0][0] * z + A[0][1]) / (A[1][0] * z + A[1][1])


def reduce_form(A, B, C):
    """Gauss reduction of a positive definite form A x^2 + B x y + C y^2, with the move gamma in SL(2,Z)
    that carries the root tau = (-B + sqrt(B^2-4AC))/(2A) of the given form to the root of the reduced form."""
    g = I2
    for _ in range(100000):
        n = -((A - B) // (2 * A))                   # tau -> tau + n makes -A < B' <= A
        if n:
            B, C = B - 2 * A * n, A * n * n - B * n + C
            g = mmul(((1, n), (0, 1)), g)
        if A > C or (A == C and B < 0):
            A, B, C = C, -B, A                      # tau -> -1/tau
            g = mmul(S_, g)
            continue
        break
    return (A, B, C), g


def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n:
                ds.append(n // i)
        i += 1
    return sorted(ds)


# ---- polynomials with integer coefficients, lowest degree first ----

def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def padd(a, b, sb=1):
    n = max(len(a), len(b))
    r = [0] * n
    for i, x in enumerate(a):
        r[i] += x
    for i, y in enumerate(b):
        r[i] += sb * y
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r


def ppow(a, n):
    r = [1]
    for _ in range(n):
        r = pmul(r, a)
    return r


def pmod_monic_quadratic(a, b1, b0):
    """a mod (t^2 + b1 t + b0), returned as (c0, c1) meaning c0 + c1 t"""
    a = list(a)
    for i in range(len(a) - 1, 1, -1):
        c = a[i]
        a[i] = 0
        a[i - 1] -= c * b1
        a[i - 2] -= c * b0
    a += [0, 0]
    return a[0], a[1]


# ---- modular functions from their q-products and Lambert series (mpmath) ----

def _nterms(q):
    aq = float(abs(q))
    return int((mp.dps + 15) * math.log(10) / (-math.log(aq))) + 5


def _q(z):
    return mp.exp(2j * mp.pi * z)


def euler_prod(q):
    p = mpf(1)
    qn = mpf(1)
    for _ in range(_nterms(q)):
        qn *= q
        p *= (1 - qn)
    return p


def t_fn(z):
    """t = (eta(z)/eta(5z))^6 = q^-1 prod ((1-q^n)/(1-q^5n))^6"""
    q = _q(z)
    return (euler_prod(q) / euler_prod(q ** 5)) ** 6 / q


def s_fn(z):
    """s = the fifth power of the Rogers-Ramanujan continued fraction = q prod (1-q^n)^(5 (n|5))"""
    q = _q(z)
    p1 = mpf(1)
    p2 = mpf(1)
    qn = mpf(1)
    for n in range(1, _nterms(q) + 1):
        qn *= q
        r = n % 5
        if r in (1, 4):
            p1 *= (1 - qn)
        elif r in (2, 3):
            p2 *= (1 - qn)
    return q * (p1 / p2) ** 5


def lambert(z, f):
    q = _q(z)
    tot = mpc(0)
    qn = mpf(1)
    for n in range(1, _nterms(q) + 1):
        qn *= q
        c = f(n)
        if c != 0:
            tot += c * qn / (1 - qn)
    return tot


def j_fn(z):
    q = _q(z)
    e4 = 1 + 240 * lambert(z, lambda n: n ** 3)
    return e4 ** 3 / (q * euler_prod(q) ** 24)


def E2_fn(z):
    return 1 - 24 * lambert(z, lambda n: n)


def E2star(z):
    return E2_fn(z) - 5 * E2_fn(5 * z)


def chi_table(sign):
    i = mpc(0, 1)
    return {0: 0, 1: 1, 2: sign * i, 3: -sign * i, 4: -1}


def E1(z, sign):
    """weight 1, character chi mod 5 with chi(2) = sign*i:  L(0,chi)/2 + sum_n (sum_{d|n} chi(d)) q^n"""
    chi = chi_table(sign)
    c0 = -sum(chi[a] * a for a in range(1, 5)) / 10
    return c0 + lambert(z, lambda n: chi[n % 5])


def eta4eta4(z):
    q = _q(z)
    return q * (euler_prod(q) * euler_prod(q ** 5)) ** 4


def mob(A, z):
    return (A[0][0] * z + A[0][1]) / (A[1][0] * z + A[1][1])


def cstr(z, n=12):
    return mpmath.nstr(z, n)


def part2():
    out('=' * 110)
    out('PART 2.   note 2: "WHAT SYMMETRY ALLOWS A STATE OF THE WHOLE"   (level 5; facts Q1 to Q7 and R1 to R9)')
    out('=' * 110)
    out()
    out('Conventions (the note, section 1): a line of order 5 is a row mod 5; the mark is v = (1,3);')
    out('G_pm = {g in SL(2,Z): v g = +-v mod 5}; G_line = {g: v g = c v mod 5}.  Cosets G\\SL(2,Z) are the orbit of the')
    out('mark under right multiplication; cusps are the cycles of T, elliptic points the fixed cosets of S and of ST.')
    out('S = [[0,-1],[1,0]], T = [[1,1],[0,1]].  A matrix of determinant -1 acts by tau -> (a conj(tau) + b)/(c conj(tau) + d).')
    out()

    # ------------------------------------------------------------------ Q1
    Xpm = orbit_structure(V, canon_pm)
    Xln = orbit_structure(V, canon_line)
    for (label, X, note) in (('X_pm has index 12, cusp widths 1,1,5,5, no elliptic point, genus 0.', Xpm,
                              dict(index=12, widths=[1, 1, 5, 5], e2=0, e3=0, genus=0)),
                             ('X_line has index 6, cusp widths 1,5, two elliptic points of order 2, genus 0.', Xln,
                              dict(index=6, widths=[1, 5], e2=2, e3=0, genus=0))):
        ok = (X['index'] == note['index'] and X['widths'] == note['widths'] and X['e2'] == note['e2']
              and X['e3'] == note['e3'] and X['genus'] == note['genus'] and X['genus_euler'] == note['genus'])
        claim('N2-Q1: %s' % label,
              'index %d; widths %s; order-2 points %d; order-3 points %d; genus %d'
              % (note['index'], note['widths'], note['e2'], note['e3'], note['genus']),
              'index %d; widths %s; order-2 points %d; order-3 points %d; genus %s'
              % (X['index'], X['widths'], X['e2'], X['e3'], X['genus']), st(ok),
              ['genus from the cycle count of S, ST, T as well: %s; Schreier generators found: %d' % (X['genus_euler'], len(X['gens']))])
    out('   (classical formulas for Gamma_0(5), for comparison only: index 5(1 + 1/5) = 6; order-2 points 1 + (-1|5) = 2;')
    out('    order-3 points 1 + (-3|5) = 0; cusps = sum over d | 5 of phi(gcd(d, 5/d)) = 2)')
    out()

    X0 = orbit_structure((0, 1), canon_line)
    X1 = orbit_structure((0, 1), canon_pm)
    ginv = minv(G_FRAME)
    frame_ok = rowact((0, 1), G_FRAME) == V and mdet(G_FRAME) == 1
    a_ok = all(in_line(mmul(mmul(ginv, h), G_FRAME)) for h in X0['gens']) and all((mmul(mmul(G_FRAME, h), ginv))[1][0] % 5 == 0 for h in Xln['gens'])
    b_ok = all(in_pm(mmul(mmul(ginv, h), G_FRAME)) for h in X1['gens']) and \
        all((lambda m: m[1][0] % 5 == 0 and m[1][1] % 5 in (1, 4))(mmul(mmul(G_FRAME, h), ginv)) for h in Xpm['gens'])
    std_ok = X0['index'] == 6 and X0['widths'] == [1, 5] and X1['index'] == 12 and X1['widths'] == [1, 1, 5, 5]
    claim('N2-s1: they are the classical X_1(5) and X_0(5) in the frame g = [[0,-1],[1,3]].',
          'g with (0,1) g = v: [0,-1,1,3]', '(0,1) g = v: %s; g^-1 Gamma_0(5) g = G_line on generators, both ways: %s; same for +-Gamma_1(5) and G_pm: %s'
          % (frame_ok, a_ok, b_ok), st(frame_ok and a_ok and b_ok and std_ok))

    # ------------------------------------------------------------------ Q2
    i_unit = C5(0, 1)
    ell = []
    for p in Xln['S_fixed']:
        g = Xln['reps'][p]
        e = mmul(mmul(g, S_), minv(g))
        tau = mobius_c5(g, i_unit)
        ell.append(dict(line=p, g=g, e=e, tau=tau))
    lines_fixed = sorted(x['line'] for x in ell)
    want_lines = sorted([canon_line(V), canon_line(rowact(V, Ti_))])
    e2m = ((-1, -2), (1, 1))
    tau2 = C5(-1, 1)
    chk = []
    for (e, tau, img, vnote) in ((e2m, tau2, Ti_, (2, 1)), (S_, i_unit, I2, (3, 4))):
        sq = mmul(e, e) == mneg(I2)
        fix = mobius_c5(e, tau) == tau
        isimg = mobius_c5(img, i_unit) == tau and mmul(mmul(img, S_), minv(img)) == e
        ve = rowact(V, e)
        pm2 = ve in ((2, 1), (3, 4))                     # +-2v
        chk.append(sq and fix and isimg and in_line(e) and (not in_pm(e)) and ve == vnote and pm2)
    ok = lines_fixed == want_lines and len(ell) == 2 and all(chk)
    claim('N2-Q2: the elliptic points of X_line are tau = i and tau = -1+i.',
          'i: e = S, v e = [3,4]; -1+i: e = [-1,-2,1,1], image of i under T^-1, v e = [2,1]; e^2 = -1, e in G_line, not in G_pm, v e = +-2v',
          'the cosets fixed by S are the lines %s, that is v and v T^-1; both elliptic elements as in the note: %s' % (lines_fixed, all(chk)), st(ok),
          ['coset representatives found here give tau = %s' % ', '.join(str(x['tau']) for x in ell),
           'i and -1+i are inequivalent under G_line (different cosets): %s' % (want_lines[0] != want_lines[1])])
    RL = mmul(R_NOTE, L_NOTE)
    LRn = mmul(L_NOTE, R_NOTE)
    l2 = rowact(V, Ti_)
    ok = proportional(rowact(V, LRn), V) and proportional(rowact(l2, RL), l2) and canon_line(l2) == (1, 2)
    claim("N2-s1: they are i with LR's line and i with RL's.",
          "LR's line and RL's", 'v = (1,3) is a line of LR = %s: %s; v T^-1 = %s is a line of RL = %s: %s'
          % (flat(LRn), proportional(rowact(V, LRn), V), canon_line(l2), flat(RL), proportional(rowact(l2, RL), l2)), st(ok))

    # ------------------------------------------------------------------ Q3
    vd = rowact(V, DELTA)
    d2 = in_pm(mmul(DELTA, DELTA))
    cnt = 0
    bad = 0
    for a in range(-12, 13):
        for b in range(-12, 13):
            for c in range(-12, 13):
                if -a * a - b * c == 1:                          # trace 0, determinant 1
                    e = ((a, b), (c, -a))
                    if in_line(e):
                        cnt += 1
                        if rowact(V, e) not in ((2, 1), (3, 4)):
                            bad += 1
    swapped = 0
    for p in Xln['S_fixed']:
        above = [q for q in Xpm['points'] if canon_line(q) == p]
        if len(above) == 2 and Xpm['perm']['S'][above[0]] == above[1] and Xpm['perm']['S'][above[1]] == above[0]:
            swapped += 1
    cusps_unram = len(cycles(Xpm['perm']['T'])) == 2 * len(cycles(Xln['perm']['T']))
    ok = (mdet(DELTA) == 1 and vd == (3, 4) and in_line(DELTA) and not in_pm(DELTA) and d2 and bad == 0 and cnt > 0
          and swapped == 2 and Xpm['e2'] == 0 and cusps_unram)
    claim('N2-Q3: delta = [[-5,-6],[-4,-5]] exchanges the twins; it fixes only the two points over the elliptic points.',
          'v delta = [3,4]; delta^2 in G_pm; elliptic elements of G_line lie in delta G_pm; fixed points: those over the 2 elliptic points',
          'v delta = %s = 3v = -2v; delta^2 in G_pm: %s; the cover X_pm -> X_line branches over %d elliptic points and no cusp'
          % (list(vd), d2, swapped), st(ok),
          ['%d elements of G_line of trace 0 with entries up to 12; outside delta G_pm: %d' % (cnt, bad),
           'Riemann-Hurwitz for the double cover: 2*0 - 2 = 2*(2*0 - 2) + 2'])

    # ------------------------------------------------------------------ Q4 / R1: W
    Wsq = mmul(W_MARK, W_MARK)
    frame_W = mmul(mmul(ginv, W5), G_FRAME) == W_MARK
    norm_line = all((lambda m: m is not None and in_line(m))(conj_by(W_MARK, h)) for h in Xln['gens'])
    norm_pm = all((lambda m: m is not None and in_pm(m))(conj_by(W_MARK, h)) for h in Xpm['gens'])
    rng = random.Random(5)
    rnd_ok = 0
    for _ in range(100):
        h = I2
        for _ in range(rng.randint(1, 12)):
            x = rng.choice(Xln['gens'])
            h = mmul(h, x if rng.random() < 0.5 else minv(x))
        m = conj_by(W_MARK, h)
        if m is not None and in_line(m) and in_line(h):
            rnd_ok += 1
    rnd_pm = 0
    for _ in range(50):
        h = I2
        for _ in range(rng.randint(1, 12)):
            x = rng.choice(Xpm['gens'])
            h = mmul(h, x if rng.random() < 0.5 else minv(x))
        m = conj_by(W_MARK, h)
        if m is not None and in_pm(m) and in_pm(h):
            rnd_pm += 1
    ok = mdet(W_MARK) == 5 and Wsq == ((-5, 0), (0, -5)) and frame_W and norm_line and rnd_ok == 100
    claim('N2-Q4: W = [[-3,-14],[1,3]] has determinant 5, W^2 = -5, and normalises G_line.',
          'det 5; W^2 = [-5,0,0,-5]; normalises G_line on all 100 elements tested',
          'det %d; W^2 = %s; W h W^-1 is integral and in G_line for all %d Schreier generators: %s; 100 random words: %d'
          % (mdet(W_MARK), flat(Wsq), len(Xln['gens']), norm_line, rnd_ok), st(ok),
          ['W = g^-1 W5 g: %s' % frame_W,
           'W^2 is a scalar, so W G W^-1 inside G gives equality: the statement holds for the whole group, not a sample'])
    claim('N2-Q6: W normalises G_pm as well.',
          'true on all 50 elements tested', 'true on all %d Schreier generators of G_pm: %s; 50 random words: %d' % (len(Xpm['gens']), norm_pm, rnd_pm),
          st(norm_pm and rnd_pm == 50))

    def r1_holds(a, b, c, d, N=5):
        lhs_num = mmul(mmul(((0, -1), (N, 0)), ((a, b), (N * c, d))), madj(((0, -1), (N, 0))))      # = N * (W X W^-1)
        rhs = ((d, -c), (-N * b, a))
        return lhs_num == ((N * rhs[0][0], N * rhs[0][1]), (N * rhs[1][0], N * rhs[1][1]))
    r1_ok = all(r1_holds(*q) for q in ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)))
    r1_ok = r1_ok and all(r1_holds(rng.randint(-99, 99), rng.randint(-99, 99), rng.randint(-99, 99), rng.randint(-99, 99)) for _ in range(200))
    r1_N = all(r1_holds(rng.randint(-99, 99), rng.randint(-99, 99), rng.randint(-99, 99), rng.randint(-99, 99), N) for N in range(2, 40) for _ in range(5))
    sym_txt = 'sympy not available'
    sym_ok = True
    if HAVE_SYMPY:
        a, b, c, d, N = sympy.symbols('a b c d N')
        W5s = sympy.Matrix([[0, -1], [5, 0]])
        diff = (W5s * sympy.Matrix([[a, b], [5 * c, d]]) * W5s.inv() - sympy.Matrix([[d, -c], [-5 * b, a]])).applyfunc(sympy.simplify)
        WNs = sympy.Matrix([[0, -1], [N, 0]])
        diffN = (WNs * sympy.Matrix([[a, b], [N * c, d]]) * WNs.inv() - sympy.Matrix([[d, -c], [-N * b, a]])).applyfunc(sympy.simplify)
        sym_ok = diff == sympy.zeros(2, 2) and diffN == sympy.zeros(2, 2)
        sym_txt = 'symbolic check (level 5 and a general level N): %s' % sym_ok
    claim('N2-R1: W5 [[a,b],[5c,d]] W5^-1 = [[d,-c],[-5b,a]] with W5 = [[0,-1],[5,0]].',
          '[[d,-c],[-5b,a]]', 'holds on the four basis matrices (the map is linear) and on 200 random integer ones: %s' % r1_ok, st(r1_ok and sym_ok),
          [sym_txt, 'the same identity with any level N in place of 5 (the note: the same involution exists at every level): %s' % r1_N])

    z1 = C5(Fraction(2, 5), Fraction(1, 5))
    z2 = C5(Fraction(-2, 5), Fraction(1, 5))
    w1 = mobius_c5(W5, z1)
    w2 = mobius_c5(W5, z2)
    e_std = [((2, -1), (5, -2)), ((-2, -1), (5, 2))]
    ell_std = mobius_c5(e_std[0], z1) == z1 and mobius_c5(e_std[1], z2) == z2
    to_mark = (mobius_c5(mmul(mpow(T_, 5), ginv), z1) == C5(0, 1)) and (mobius_c5(ginv, z2) == C5(-1, 1))
    cusp = (W5[0][0] == 0 and W5[1][0] != 0) and (W5[1][1] == 0 and W5[0][1] != 0)      # W5(inf) = a/c = 0 ; W5(0) = b/d = infinity
    ok = w1 == z2 and w2 == z1 and ell_std and cusp
    claim('N2-Q4: W5 exchanges the elliptic points (2+i)/5, (-2+i)/5 and the cusps infinity, 0.',
          'W5((2+i)/5) = -2/5 + i/5; W5((-2+i)/5) = 2/5 + i/5; infinity to 0, 0 to infinity',
          'W5((2+i)/5) = %s; W5((-2+i)/5) = %s; cusps exchanged: %s' % (w1, w2, cusp), st(ok),
          ['(2+i)/5 and (-2+i)/5 are fixed by [[2,-1],[5,-2]] and [[-2,-1],[5,2]] in Gamma_0(5): %s' % ell_std,
           "in the mark's frame they are tau = i (after T^5, which lies in G_line) and tau = -1+i: %s" % to_mark])

    # ------------------------------------------------------------------ fixed points of W by class (Q4, Q6, R2)
    base = {}
    for nm, (a, c, d) in (('(1, 0, 5)', (1, 0, 1)), ('(2, 2, 3)', (2, -1, 3))):
        red, gam = reduce_form(5 * a, 10 * c, d)
        base[nm] = dict(acd=(a, c, d), red=red, gam=gam)
    base_ok = base['(1, 0, 5)']['red'] == (1, 0, 5) and base['(2, 2, 3)']['red'] == (2, 2, 3)

    def scan(C, amax=None):
        rows = []
        for c in range(-C, C + 1):
            n = 1 + 5 * c * c
            for a in divisors(n):
                if amax is not None and a > amax:
                    continue
                d = n // a
                M = ((-5 * c, -d), (5 * a, 5 * c))                    # = W5 . [[a, c],[5c, d]]
                red, gam = reduce_form(5 * a, 10 * c, d)
                rows.append(dict(a=a, c=c, d=d, M=M, red=red, gam=gam))
        return rows

    big = scan(200)
    classes = sorted(set(r['red'] for r in big))
    n_bad_sq = n_bad_ker = n_bad_orbit = n_bad_mark = n_bad_red = n_bad_twin = 0
    dres = {}
    d_std0 = mmul(mmul(G_FRAME, DELTA), ginv)              # the twin exchange in the standard frame
    for r in big:
        M = r['M']
        if mmul(M, M) != ((-5, 0), (0, -5)) or mdet(M) != 5:
            n_bad_sq += 1
        # the other point of X_pm over the same fixed point: conjugate by the twin exchange and read d again
        M2 = mmul(mmul(d_std0, M), minv(d_std0))
        g2 = mmul(madj(W5), M2)                             # = 5 * W5^-1 M2
        if any(x % 5 for x in flat(g2)) or (g2[1][0] // 5) % 5 != 0 or min((g2[1][1] // 5) % 5, (-(g2[1][1] // 5)) % 5) != min(r['d'] % 5, (-r['d']) % 5):
            n_bad_twin += 1
        ker = sorted((x, y) for x in range(5) for y in range(5) if rowact((x, y), M) == (0, 0))
        if ker != [(0, y) for y in range(5)]:
            n_bad_ker += 1
        A_, B_, C_ = r['red']
        if not (B_ * B_ - 4 * A_ * C_ == -20 and -A_ < B_ <= A_ <= C_):
            n_bad_red += 1
        nm = '(%d, %d, %d)' % r['red']
        dm = min(r['d'] % 5, (-r['d']) % 5)
        dres.setdefault(nm, set()).add(dm)
        if nm in base:
            h = mmul(minv(r['gam']), base[nm]['gam'])           # carries the base point to this fixed point
            if h[1][0] % 5 != 0 or mdet(h) != 1:
                n_bad_orbit += 1
        else:
            n_bad_orbit += 1
        Mm = mmul(mmul(ginv, M), G_FRAME)                       # in the mark's frame
        hm = mmul(madj(W_MARK), Mm)
        if rowact(V, Mm) != (0, 0) or any(x % 5 for x in flat(hm)) or not in_line(tuple(tuple(x // 5 for x in row) for row in hm)):
            n_bad_mark += 1
    ex1 = ((-20, -81), (5, 20))
    ex2 = ((-20, -27), (15, 20))
    ex_ok = []
    for (M, want, gam_note, vnote) in ((ex1, (1, 0, 5), ((1, 4), (20, 81)), (0, 1)), (ex2, (2, 2, 3), ((3, 4), (20, 27)), (0, 2))):
        a, c, d = M[1][0] // 5, M[1][1] // 5, -M[0][1]
        gam = ((a, c), (5 * c, d))
        red, _ = reduce_form(5 * a, 10 * c, d)
        ex_ok.append(mmul(W5, gam) == M and gam == gam_note and mdet(gam) == 1 and red == want and rowact((0, 1), gam) == vnote)
    ok = (classes == [(1, 0, 5), (2, 2, 3)] and n_bad_sq == 0 and n_bad_ker == 0 and n_bad_orbit == 0 and n_bad_mark == 0
          and n_bad_red == 0 and all(ex_ok) and base_ok)
    claim("N2-Q4: W's fixed points are two classes of discriminant -20, (1,0,5) and (2,2,3); kernel is the mark.",
          'classes: 2; kernel of every fixing matrix on the 5-torsion is the mark; examples [-20,-81,5,20] and [-20,-27,15,20]',
          '%d fixing matrices (all with c up to 200 in absolute value): classes %s; kernel not the mark: %d; both examples as in the note: %s'
          % (len(big), classes, n_bad_ker, all(ex_ok)), st(ok),
          ['a fixing matrix is W5.gamma with trace 5(b - c), and a fixed point in the upper half-plane needs trace^2 < 20: trace 0, so',
           '   M = [[-5c,-d],[5a,5c]] with a d - 5 c^2 = 1, and its fixed point is the root of the form (5a, 10c, d) of discriminant -20',
           'M^2 = -5 fails in %d cases; reduced form not reduced or of another discriminant in %d cases' % (n_bad_sq, n_bad_red),
           'each fixed point is Gamma_0(5)-equivalent to the base point of its class (i/sqrt5, or 1/2 + i/(2 sqrt5)): exceptions %d' % n_bad_orbit,
           'so W has exactly two fixed points on X_line, one for each class',
           "in the mark's frame every g^-1 M g kills v mod 5 and lies in W.G_line: exceptions %d" % n_bad_mark])

    c63 = scan(6)
    c4 = scan(4)
    c4a = scan(4, 50)

    def split(rows):
        return (sum(1 for r in rows if r['red'] == (1, 0, 5)), sum(1 for r in rows if r['red'] == (2, 2, 3)))
    amax_ok = [A for A in range(1, 130) if split(scan(4, A)) == (17, 16)]
    NOTES['samples'] = (len(c63), split(c4), (min(amax_ok), max(amax_ok)) if amax_ok else None, len(big))
    claim('N2-Q4/R2: sample sizes: 17 and 16 matrices found by class; 63 matrices examined.',
          '17, 16; 63', 'c up to 6: %d; c up to 4: %d + %d; c up to 4 with a up to 50: %d + %d'
          % (len(c63), split(c4)[0], split(c4)[1], split(c4a)[0], split(c4a)[1]), NOTRE,
          ['the note does not state the search boxes; these are sizes of samples, not mathematical claims',
           '63 is reproduced by all a d = 1 + 5c^2 with c from -6 to 6',
           '17 + 16 is reproduced by c from -4 to 4 with a <= a_max for any a_max from %d to %d; without that bound the box gives %d + %d'
           % (min(amax_ok) if amax_ok else -1, max(amax_ok) if amax_ok else -1, split(c4)[0], split(c4)[1])])

    ok = all(dres.get(k) == v for k, v in (('(1, 0, 5)', {1}), ('(2, 2, 3)', {2}))) and len(dres) == 2 and n_bad_twin == 0
    claim('N2-R2: d of gamma is +-1 mod 5 on the class (1,0,5), +-2 on (2,2,3).',
          '(1,0,5): [1]; (2,2,3): [2]', '%s, over %d matrices' % ('; '.join('%s: %s' % (k, sorted(v)) for k, v in sorted(dres.items())), len(big)), st(ok),
          ['so both points of X_pm over the first are fixed by W5, and over the second by W5 with the twin exchange (Q6)',
           '   ("both": conjugating a fixing matrix by the twin exchange gives W5.gamma\' with the same d up to sign: exceptions %d)' % n_bad_twin,
           '   consistent with R4 below: the twins over t = +5 sqrt5, the class (1,0,5), are the fixed points of the lift of W5',
           '(reason: x^2 + 5y^2 takes values +-1 mod 5 and 2x^2 + 2xy + 3y^2 values +-2 mod 5 on values prime to 5)'])

    A_, B_, C_ = W_MARK[1][0], W_MARK[1][1] - W_MARK[0][0], -W_MARK[0][1]
    red, _ = reduce_form(A_, B_, C_)
    tauW = C5(-3, Q5(0, 1))                       # -3 + i sqrt5
    fixW = mobius_c5(W_MARK, tauW) == tauW
    to_std = mobius_c5(G_FRAME, tauW) == C5(0, Q5(0, Fraction(1, 5)))          # i/sqrt5 = i sqrt5/5
    ok = (A_, B_, C_) == (1, 6, 14) and red == (1, 0, 5) and fixW and to_std
    claim("N2-Q4: in the mark's frame W fixes the root of (1,6,14), reduced form (1,0,5).",
          '(1, 6, 14); (1, 0, 5)', '%s; %s; W fixes -3 + i sqrt5 exactly: %s; g carries it to i/sqrt5: %s' % ((A_, B_, C_), red, fixW, to_std), st(ok))

    # ------------------------------------------------------------------ Q5: the mirror
    def mir(h):
        return ((h[0][0], -h[0][1]), (-h[1][0], h[1][1]))
    mir_ok = all(mir(h)[1][0] % 5 == 0 and mdet(mir(h)) == 1 for h in X0['gens']) and \
        all((lambda m: m[1][0] % 5 == 0 and m[1][1] % 5 in (1, 4))(mir(h)) for h in X1['gens'])
    mm_line = all(in_line(mmul(mmul(M_MIRROR, h), M_MIRROR)) for h in Xln['gens'])
    mm_pm = all(in_pm(mmul(mmul(M_MIRROR, h), M_MIRROR)) for h in Xpm['gens'])

    def mirror_pt(z):
        return -(z.conj())
    ex = mirror_pt(z1) == z2 and mirror_pt(z2) == z1
    f0 = C5(0, Q5(0, Fraction(1, 5)))                 # i/sqrt5
    f1 = C5(Fraction(1, 2), Q5(0, Fraction(1, 10)))   # 1/2 + i/(2 sqrt5)
    fix0 = mirror_pt(f0) == f0
    fix1 = mirror_pt(f1) == mobius_c5(Ti_, f1) and mirror_pt(f1).re == Q5(Fraction(-1, 2))
    w5fix = mobius_c5(W5, f0) == f0 and mobius_c5(((5, -3), (10, -5)), f1) == f1
    # in the mark's frame: m = T^-1 . diag(-1,1), tau -> -conj(tau) - 1
    Dm = ((-1, 0), (0, 1))
    m_is = mmul(Ti_, Dm) == M_MIRROR and mmul(M_MIRROR, M_MIRROR) == I2
    plain = rowact(V, Dm)

    def m_act(z):
        return -(z.conj()) - 1
    m_ell = m_act(C5(0, 1)) == C5(-1, 1) and m_act(C5(-1, 1)) == C5(0, 1)
    m_fixW = m_act(tauW) == mobius_c5(mpow(T_, 5), tauW) and in_pm(mpow(T_, 5))
    ok = mir_ok and ex and fix0 and fix1 and w5fix and mm_line and mm_pm and m_is and m_ell and m_fixW
    claim('N2-Q5: the mirror normalises the group, exchanges the elliptic points, fixes both fixed points of W.',
          'normalises; exchanges; fixes i/sqrt5; sends 1/2 + i/(2 sqrt5) to T^-1 of it',
          'normalises (on generators): %s; exchanges (2+i)/5 and (-2+i)/5: %s; fixes i/sqrt5: %s; second point goes to T^-1 of itself: %s'
          % (mir_ok, ex, fix0, fix1), st(ok),
          ['i/sqrt5 is fixed by W5 and 1/2 + i/(2 sqrt5) by W5.[[2,-1],[-5,3]] = [[5,-3],[10,-5]]: %s' % w5fix,
           "in the mark's frame the mirror with its restoring move is m = T^-1.diag(-1,1) = [[-1,-1],[0,1]], an involution: %s" % m_is,
           '   the bare mirror diag(-1,1) sends v to %s, on the line (1,2): it does not keep the mark; m does (v m = -v)' % (plain,),
           '   m normalises G_line and G_pm on generators: %s, %s' % (mm_line, mm_pm),
           '   m exchanges tau = i and tau = -1+i: %s; m sends -3 + i sqrt5 to T^5 of itself, and T^5 is in G_pm: %s' % (m_ell, m_fixW)])

    # ------------------------------------------------------------------ R7: the tick
    F2 = mmul(F_TICK, F_TICK)
    vF = rowact(V, F_TICK)
    Sinv = minv(S_)
    FeqSm = mmul(Sinv, M_MIRROR) == F_TICK
    vS = rowact(V, S_)
    vm = rowact(V, M_MIRROR)
    zt = C5(Fraction(3, 7), Fraction(5, 11))
    m_val = mobius_c5(M_MIRROR, zt.conj())
    F_val = mobius_c5(F_TICK, zt.conj())
    comp = mobius_c5(Sinv, m_val)
    ok = (F2 == ((1, 1), (1, 2)) and F2 == LRn and mdet(F_TICK) == -1 and vF == (3, 4) and vF == rowact((3, 9), I2) and FeqSm
          and vS == (3, 4) and vm == (4, 2) and mdet(M_MIRROR) == -1 and m_val == m_act(zt) and F_val == comp and in_line(S_))
    claim('N2-R7: F = [[0,1],[1,1]] has F^2 = LR, det -1, vF = 3v, and F = S^-1 m.',
          'LR = [1,1,1,2] = F^2; det F = -1; v F = [3,4] = 3v; F = S^-1 m; v S = [3,4]; v m = [4,2]; det m = -1',
          'F^2 = %s; det F = %d; v F = %s; F = S^-1 m: %s; v S = %s; v m = %s; det m = %d'
          % (flat(F2), mdet(F_TICK), list(vF), FeqSm, list(vS), list(vm), mdet(M_MIRROR)), st(ok),
          ['on tau: m is tau -> -conj(tau) - 1: %s; F is S^-1 after m: %s (exact, at a rational test point)' % (m_val == m_act(zt), F_val == comp),
           'v S = 3v: S keeps the line; v m = -v: m keeps the twin up to sign',
           'here LR = [[1,1],[1,2]] is L.R for L = [[1,0],[1,1]], R = [[1,1],[0,1]] (see the remark on conventions in part 1)'])

    # ------------------------------------------------------------------ numerics
    if not HAVE_MP:
        for tag in ('Q7', 'R3', 'R4', 'R5', 'R6', 'R9'):
            claim('N2-%s: identities for modular functions (numerical).' % tag, 'see the note', 'mpmath is not available here', NOTRE)
        return
    mp.dps = 60
    TOL = mpf(10) ** (-45)
    I = mpc(0, 1)
    r5 = mp.sqrt(5)
    z = mpc('0.137', '0.412')
    w = mpc('0.37', '0.23')

    v1 = t_fn(z) * t_fn(-1 / (5 * z))
    v2 = t_fn(I / r5) / (5 * r5)
    v3 = t_fn(mpf(1) / 2 + I / (2 * r5)) / (5 * r5)
    ok = abs(v1 - 125) < TOL and abs(v2 - 1) < TOL and abs(v3 + 1) < TOL
    claim('N2-Q7: t(z)t(-1/(5z)) = 125; t = +5sqrt5 at i/sqrt5, -5sqrt5 at 1/2+i/(2sqrt5).',
          '125.0; 1.0; -1.0 (errors below 1e-38)', 'errors %s, %s, %s'
          % (cstr(abs(v1 - 125), 3), cstr(abs(v2 - 1), 3), cstr(abs(v3 + 1), 3)), st(ok),
          ['t = (eta(z)/eta(5z))^6 evaluated as q^-1 prod((1-q^n)/(1-q^5n))^6 at 60 digits; z = 0.137 + 0.412 i as in the note',
           't(i/sqrt5)/(5 sqrt5) = %s; t(1/2 + i/(2 sqrt5))/(5 sqrt5) = %s' % (cstr(v2, 20), cstr(v3, 20))])

    jP = Q5(632000, 282880)
    jN = Q5(632000, -282880)

    def j_of_t(tv):
        return (tv * tv + 250 * tv + 3125) ** 3 / tv ** 5
    jt_plus = j_of_t(Q5(0, 5))
    jt_minus = j_of_t(Q5(0, -5))
    jn1 = j_fn(I * r5)
    jn2 = j_fn((1 + I * r5) / 2)
    j_num = abs(jn1 - jP.mp()) / abs(jn1) < TOL and abs(jn2 - jN.mp()) / abs(jn2) < TOL
    ok = jt_plus == jP and jt_minus == jN and j_num
    claim('N2-s4: those two points are the tori i*sqrt5 (principal class) and (1+i*sqrt5)/2.',
          'the two classes of discriminant -20; j = 632000 +- 282880 sqrt5',
          'j at t = +5 sqrt5: %s; at t = -5 sqrt5: %s (exact); equal to j(i sqrt5) and j((1 + i sqrt5)/2) numerically: %s'
          % (jt_plus, jt_minus, j_num), st(ok),
          ['the two points are conjugate over Q and lie in Q(sqrt5): t^2 = 125'])

    s_z = s_fn(z)
    err_ts = abs(t_fn(z) - (1 / s_z - 11 - s_z))
    d_std = mmul(mmul(G_FRAME, DELTA), ginv)
    NOTES['d_std'] = flat(d_std)
    deltas = [d_std, ((2, -1), (5, -2)), ((2, 1), (5, 3)), ((3, 1), (5, 2)), ((7, 3), (-5, -2))]
    d_errs = []
    d_valid = True
    s_w = s_fn(w)
    for dm in deltas:
        if not (mdet(dm) == 1 and dm[1][0] % 5 == 0 and dm[1][1] % 5 in (2, 3)):
            d_valid = False
        if dm == d_std:
            mp.dps = 75
            val = s_fn(mob(dm, w)) + 1 / s_fn(w)
            mp.dps = 60
        else:
            val = s_fn(mob(dm, w)) + 1 / s_w
        d_errs.append(abs(val))
    pm_errs = []
    for gm in (((1, 1), (5, 6)), ((1, 0), (5, 1)), ((4, 1), (15, 4)), ((6, 1), (5, 1))):
        pm_errs.append(abs(s_fn(mob(gm, w)) - s_w))
    err_m = abs(s_fn(-mp.conj(z)) - mp.conj(s_z))
    ok = err_ts < TOL and max(d_errs) < TOL and d_valid and err_m < TOL and max(pm_errs) < TOL
    claim('N2-R3: t = 1/s - 11 - s; s(delta w) = -1/s(w); s(-conj z) = conj s(z).',
          'errors 9.8e-39; 8.1e-40; 0.0', 'errors %s; %s (greatest over five delta); %s'
          % (cstr(err_ts, 3), cstr(max(d_errs), 3), cstr(err_m, 3)), st(ok),
          ['at w = 0.37 + 0.23 i; the delta used: g delta g^-1 = %s and four more elements of Gamma_0(5) with d = +-2 mod 5' % flat(d_std),
           's is unchanged by four elements with d = +-1 mod 5: greatest difference %s' % cstr(max(pm_errs), 3)])

    beta = Q5(Fraction(-11, 2), Fraction(-5, 2))
    over = []
    for tv in (Q5(0, 5), Q5(0, -5)):
        b1 = Q5(11) + tv                      # s^2 + (11 + t) s - 1 = 0: product of the roots is -1
        over.append((b1 * b1 + 4).sign() > 0)
    cm = C5(-11, 2)
    cp = C5(-11, -2)
    si_ok = True
    for (tv, sv) in ((cm, C5(0, -1)), (cp, C5(0, 1))):
        if not ((C5(1) / sv - 11 - sv) == tv and ((tv + 11) * (tv + 11) + 4).is_zero()):
            si_ok = False
    n1, n2 = s_fn((2 + I) / 5), s_fn((-2 + I) / 5)
    t1, t2 = t_fn((2 + I) / 5), t_fn((-2 + I) / 5)
    num_ok = abs(n1 - I) < TOL and abs(n2 + I) < TOL and abs(t1 - (-11 - 2 * I)) < TOL and abs(t2 - (-11 + 2 * I)) < TOL
    tm1 = t_fn(mob(G_FRAME, I))
    tm2 = t_fn(mob(G_FRAME, -1 + I))
    mark_ok = abs(tm1 - (-11 - 2 * I)) < TOL and abs(tm2 - (-11 + 2 * I)) < TOL
    ok = all(over) and si_ok and num_ok and mark_ok
    claim('N2-R3: over t = +-5sqrt5 s is real with product -1; over -11+2i, s = -i.',
          'real, product -1 (both); over -11+2i: -i; over -11-2i: i',
          'discriminant (11+t)^2 + 4 is positive at t = +-5 sqrt5: %s, product -1; s = -i, i are double roots over -11+2i, -11-2i: %s'
          % (all(over), si_ok), st(ok),
          ['numerically t((2+i)/5) = %s with s = %s; t((-2+i)/5) = %s with s = %s' % (cstr(t1, 8), cstr(n1, 8), cstr(t2, 8), cstr(n2, 8)),
           "in the mark's frame: t at tau = i is %s and at tau = -1+i is %s: %s" % (cstr(tm1, 8), cstr(tm2, 8), mark_ok)])

    bm = beta.mp()
    lift_errs = []
    for zz in (z, w, mpc('-0.21', '0.33')):
        sz = s_fn(zz)
        lift_errs.append(abs(s_fn(-1 / (5 * zz)) - (bm * sz + 1) / (sz - bm)))
    ok = max(lift_errs) < TOL
    claim('N2-s4: on X_pm, W is s -> (beta*s+1)/(s-beta), beta = (-11-5sqrt5)/2.',
          'beta = (-11 - 5 sqrt5)/2', 's(-1/(5z)) against (beta s + 1)/(s - beta) at three points: greatest error %s' % cstr(max(lift_errs), 3), st(ok),
          ['beta = -phi^5: %s' % ((Q5(Fraction(1, 2), Fraction(1, 2)) ** 5 + beta).is_zero())])

    # ------------------------------------------------------------------ R4: the group of order 8 on the s-sphere
    one, zero = Q5(1), Q5(0)

    def pnorm(M):
        for x in (M[0][0], M[0][1], M[1][0], M[1][1]):
            if not x.is_zero():
                return tuple(tuple(y / x for y in row) for row in M)
        raise ValueError('zero matrix')

    def qmul(A, B):
        return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
                (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))
    ID = pnorm(((one, zero), (zero, one)))
    dM = pnorm(((zero, -one), (one, zero)))                 # delta: s -> -1/s
    wM = pnorm(((beta, one), (one, -beta)))                 # W: s -> (beta s + 1)/(s - beta)

    def comp8(x, y):          # x after y; the matrices are real, so conjugation passes through them
        return (pnorm(qmul(x[0], y[0])), x[1] ^ y[1])
    table8 = {}
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                e = (ID, 0)
                if c:
                    e = comp8((ID, 1), e)
                if b:
                    e = comp8((wM, 0), e)
                if a:
                    e = comp8((dM, 0), e)
                name = '.'.join(n_ for n_, f in (('delta', a), ('W', b), ('mirror', c)) if f) or '1'
                table8[name] = e
    elems = set(table8.values())
    order8 = len(elems)
    closed8 = all(comp8(x, y) in elems for x in elems for y in elems)
    commuting = all(comp8(x, y) == comp8(y, x) for x in elems for y in elems)
    squares = all(comp8(x, x) == (ID, 0) for x in elems)

    def fixquad(M):          # the fixed points of s -> (a s + b)/(c s + d): c s^2 + (d - a) s - b = 0
        return (M[1][0], M[1][1] - M[0][0], -M[0][1])

    def prop3(u, v_):
        return all((u[i] * v_[j] - u[j] * v_[i]).is_zero() for i in range(3) for j in range(3))
    P_W = fixquad(wM)
    P_dW = fixquad(table8['delta.W'][0])
    P_d = fixquad(dM)
    quad_ok = prop3(P_W, (one, -2 * beta, -one)) and prop3(P_dW, (beta, Q5(2), -beta)) and prop3(P_d, (one, zero, one))

    def t_over(P, tv):
        # with s^2 = -(B s + C)/A:  1 - s^2 - (t + 11) s = (1 + C/A) + (B/A - (t + 11)) s
        A, B, C = P
        return (one + C / A).is_zero() and (B / A - (tv + 11)).is_zero()
    over_ok = t_over(P_W, Q5(0, 5)) and t_over(P_dW, Q5(0, -5))
    real_ok = (P_W[1] * P_W[1] - 4 * P_W[0] * P_W[2]).sign() > 0 and (P_dW[1] * P_dW[1] - 4 * P_dW[0] * P_dW[2]).sign() > 0
    sq = mp.sqrt(bm * bm + 1)
    pts6 = {'p1': bm + sq, 'p2': bm - sq, 'p3': (-1 + sq) / bm, 'p4': (-1 - sq) / bm, 'p5': -I, 'p6': I}

    def act8(e, p):
        M, cflag = e
        x = mp.conj(p) if cflag else p
        return (M[0][0].mp() * x + M[0][1].mp()) / (M[1][0].mp() * x + M[1][1].mp())

    def which(val):
        for nm, p in pts6.items():
            if abs(val - p) < TOL:
                return nm
        return None
    tab = {}
    for pn, p in pts6.items():
        stab = sorted(nm for nm, e in table8.items() if which(act8(e, p)) == pn)
        orb = sorted(set(str(which(act8(e, p))) for e in table8.values()))
        tab[pn] = (stab, orb)
    note_tab = {
        'p1': (['1', 'W', 'mirror', 'W.mirror'], ['p1', 'p2']), 'p2': (['1', 'W', 'mirror', 'W.mirror'], ['p1', 'p2']),
        'p3': (['1', 'mirror', 'delta.W', 'delta.W.mirror'], ['p3', 'p4']), 'p4': (['1', 'mirror', 'delta.W', 'delta.W.mirror'], ['p3', 'p4']),
        'p5': (['1', 'delta', 'W.mirror', 'delta.W.mirror'], ['p5', 'p6']), 'p6': (['1', 'delta', 'W.mirror', 'delta.W.mirror'], ['p5', 'p6'])}
    tab_ok = all(tab[p][0] == sorted(note_tab[p][0]) and tab[p][1] == sorted(note_tab[p][1]) for p in pts6)
    ii = C5(0, 1)

    def act8_exact(e, p):
        M, cflag = e
        x = p.conj() if cflag else p
        return (C5(M[0][0]) * x + C5(M[0][1])) / (C5(M[1][0]) * x + C5(M[1][1]))
    stab_i = sorted(nm for nm, e in table8.items() if act8_exact(e, ii) == ii)
    orb_i = set(act8_exact(e, ii) for e in table8.values())
    exact_i = stab_i == sorted(['1', 'delta', 'W.mirror', 'delta.W.mirror']) and orb_i == {ii, C5(0, -1)}

    def stab_real(P):
        # a holomorphic element other than 1 fixes a root of P only if its fixed-point quadratic is proportional
        # to P; an anti-holomorphic element acts on a real point as its matrix does
        return sorted(nm for nm, (M, cflag) in table8.items() if M == ID or prop3(fixquad(M), P))
    exact_real = stab_real(P_W) == sorted(['1', 'W', 'mirror', 'W.mirror']) and stab_real(P_dW) == sorted(['1', 'mirror', 'delta.W', 'delta.W.mirror'])
    fixed_by_all = [p for p in pts6 if len(tab[p][0]) == 8]
    orbits = sorted(set(tuple(v_[1]) for v_ in tab.values()))
    ok = (order8 == 8 and closed8 and commuting and tab_ok and exact_i and exact_real and quad_ok and over_ok and real_ok
          and not fixed_by_all)
    det = ['%s: stabiliser %s, orbit %s' % (p, tab[p][0], tab[p][1]) for p in sorted(pts6)]
    det.append('p1, p2 are the roots of s^2 - 2 beta s - 1 (over t = +5 sqrt5), p3, p4 of beta s^2 + 2 s - beta (over t = -5 sqrt5), p5 = -i, p6 = i: exact %s'
               % (quad_ok and over_ok and real_ok))
    det.append('exact stabilisers in Q(sqrt5) and Q(sqrt5)(i) agree with the 60-digit table: %s; every element is an involution: %s' % (exact_i and exact_real, squares))
    claim('N2-R4: delta, W, mirror generate a commuting group of 8; stabilisers and orbits of six points.',
          '8 elements, commuting; orbits [p1,p2], [p3,p4], [p5,p6]; no point fixed by the whole group',
          '%d elements, closed: %s, commuting: %s; orbits %s; stabilisers as in the note: %s; fixed by all: %s'
          % (order8, closed8, commuting, [list(o) for o in orbits], tab_ok, fixed_by_all if fixed_by_all else 'none'), st(ok), det)

    holo = ['delta', 'W', 'delta.W']
    subs4 = []
    nm_list = sorted(table8)
    for trio in itertools.combinations([n_ for n_ in nm_list if n_ != '1'], 3):
        grp = ['1'] + list(trio)
        vals = [table8[g_] for g_ in grp]
        if all(comp8(table8[x], table8[y]) in vals for x in grp for y in grp):
            subs4.append(sorted(grp))
    all_have_holo = all(any(h in g_ for h in holo) for g_ in subs4)
    distinct_quads = not prop3(P_W, P_dW) and not prop3(P_W, P_d) and not prop3(P_dW, P_d)
    pairs = [o for o in orbits if len(o) == 2]
    ok = len(subs4) == 7 and all_have_holo and distinct_quads and len(pairs) == 3 and all(len(tab[p][0]) == 4 for p in pts6)
    claim('N2-s4: on X_pm no point is fixed by every symmetry; exactly three pairs exist.',
          'none; exactly three pairs',
          'subgroups of order 4: %d, each with a holomorphic involution: %s; their six fixed points have stabilisers of order 4; pairs: %d'
          % (len(subs4), all_have_holo, len(pairs)), st(ok),
          ['twins over t = +5 sqrt5: fixed by W and the mirror; twins over t = -5 sqrt5: by delta.W and the mirror;',
           '   the points over i: fixed by delta, exchanged by W and by the mirror  (as the note says)'])

    Wi = act8_exact(table8['W'], ii)
    ok = act8_exact(table8['delta'], ii) == ii and Wi == ii.conj()
    claim('N2-s1: on X_pm modulo the mirror only the point over i is fixed by delta and W.',
          'the point over i', 'delta(s) = s only at s = +-i; delta(s) = conj(s) has no solution; W(i) = -i = conj(i): %s' % ok, st(ok),
          ['delta(s) = conj(s) would need s conj(s) = -1'])

    # ------------------------------------------------------------------ the symmetry groups are all there is
    def det2(u, v_):
        return u[0] * v_[1] - u[1] * v_[0]

    def cr(P):
        return (det2(P[0], P[2]) * det2(P[1], P[3])) / (det2(P[0], P[3]) * det2(P[1], P[2]))
    oneC, zeroC = C5(1), C5(0)
    P4 = [(zeroC, oneC), (oneC, zeroC), (C5(-11, 2), oneC), (C5(-11, -2), oneC)]        # cusps 0, infinity; cone points
    Pc = [P4[0], P4[1], P4[3], P4[2]]                                                  # their complex conjugates
    base_cr = cr(P4)
    hol = anti = 0
    for perm in itertools.permutations(range(4)):
        if set(perm[:2]) != {0, 1}:
            continue                                   # cusps to cusps, cone points to cone points
        if cr([P4[i] for i in perm]) == base_cr:
            hol += 1
        if cr([Pc[i] for i in perm]) == base_cr:
            anti += 1
    w_t_ok = (C5(125) / C5(-11, 2)) == C5(-11, -2)
    ok = hol == 2 and anti == 2 and w_t_ok
    claim('N2-s4: on X_line the symmetries are W, the mirror, their product, and no others.',
          'a group of order 4', '%d holomorphic and %d anti-holomorphic maps keep the cusps {0, infinity} and the cone points {-11+2i, -11-2i}'
          % (hol, anti), st(ok),
          ['t -> 125/t exchanges -11+2i and -11-2i: %s' % w_t_ok,
           'decided here as automorphisms of the sphere with two punctures and two cone points (cross-ratios, exact)'])
    s_plus = Q5(Fraction(-11, 2), Fraction(5, 2))
    s_minus = Q5(Fraction(-11, 2), Fraction(-5, 2))
    cusps_s = [(zeroC, oneC), (oneC, zeroC), (C5(s_plus), oneC), (C5(s_minus), oneC)]
    cusp_eq = (s_plus * s_plus + 11 * s_plus - 1).is_zero() and (s_minus * s_minus + 11 * s_minus - 1).is_zero()
    base_cr_s = cr(cusps_s)
    hol_s = sum(1 for perm in itertools.permutations(range(4)) if cr([cusps_s[i] for i in perm]) == base_cr_s)

    def img_proj(M, P):
        return (C5(M[0][0]) * P[0] + C5(M[0][1]) * P[1], C5(M[1][0]) * P[0] + C5(M[1][1]) * P[1])

    def same_proj(P, Q):
        return (P[0] * Q[1] - P[1] * Q[0]).is_zero()
    perm_ok = all(any(same_proj(img_proj(table8[nm][0], P), Q) for Q in cusps_s) for nm in ('delta', 'W', 'delta.W') for P in cusps_s)
    NOTES['aut'] = (hol, anti, hol_s)
    ok = hol_s == 4 and perm_ok and cusp_eq and base_cr_s.im.is_zero()
    claim('N2-s4: on X_pm the symmetries form a group of order 8.',
          'order 8, generated by delta, W and the mirror',
          '%d Moebius maps permute the four cusps s = 0, infinity, (-11 +- 5 sqrt5)/2; all four are real, so %d with the mirror'
          % (hol_s, 2 * hol_s), st(ok),
          ['delta, W and delta.W permute the four cusps: %s; cross-ratio of the cusps = %s (not -1, 2, 1/2)' % (perm_ok, base_cr_s.re)])

    fix_t = (Q5(0, 5) * Q5(0, 5) == Q5(125)) and (Q5(0, -5) * Q5(0, -5) == Q5(125))
    n125 = (C5(-11, 2) * C5(-11, -2)) == C5(125)
    claim('N2-s4: with the line as mark exactly two points are fixed by every symmetry, t = +-5sqrt5.',
          'two: t = +-5 sqrt5; the points over i are a mirror pair',
          'fixed by t -> 125/t: t^2 = 125, two real points, each fixed by the mirror: %s; -11+2i and -11-2i are exchanged by both: %s'
          % (fix_t, w_t_ok), st(fix_t and w_t_ok))
    arc_pt = C5(-11, 2)
    ok = fix_t and n125 and m_ell
    claim('N2-R6/R8: under the tick the fixed set is the arc of the circle of radius 5sqrt5 through -11+2i.',
          '(-11+2i)(-11-2i) = 125 = (5 sqrt5)^2; arc from +5 sqrt5 through the point over i to -5 sqrt5',
          '(-11+2i)(-11-2i) = 125: %s; (+-5 sqrt5)^2 = 125: %s; the mirror m exchanges tau = i and tau = -1+i: %s'
          % (n125, fix_t, m_ell), st(ok),
          ['t -> 125/t fixes the class of t modulo t ~ conj(t) exactly when 125/t = t or 125/t = conj(t): t^2 = 125 or t conj(t) = 125',
           'modulo the mirror that circle is its upper half: an arc from +5 sqrt5 to -5 sqrt5 through %s (imaginary part positive)' % arc_pt])

    e1_ = abs(t_fn(1 / (5 * mp.conj(z))) - 125 / mp.conj(t_fn(z)))
    e2_ = abs(t_fn(-mp.conj(z)) - mp.conj(t_fn(z)))
    claim('N2-R6: W with the mirror is t -> 125/conj(t); the mirror is t -> conj(t).',
          'errors 9.6e-40; 0.0', 'errors %s; %s' % (cstr(e1_, 3), cstr(e2_, 3)),
          st(e1_ < TOL and e2_ < TOL), ['t(1/(5 conj z)) against 125/conj(t(z)), and t(-conj z) against conj(t(z)), at z = 0.137 + 0.412 i'])

    # ------------------------------------------------------------------ R5
    num_poly = padd(ppow([3125, 250, 1], 3), pmul([0, 0, 0, 0, 1], ppow([5, 10, 1], 3)), -1)       # (t^2+250t+3125)^3 - t^4 (t^2+10t+5)^3
    jw_ok = ppow([15625, 31250, 3125], 3) == [x * 125 ** 5 for x in ppow([5, 10, 1], 3)]           # j(125/t) = (t^2+10t+5)^3/t
    facs = [[-125, 0, 1], [125, -14, 1], [125, 4, 1], [125, 18, 1], [125, 22, 1]]
    prod_ = [-1]
    for f in facs:
        prod_ = pmul(prod_, f)
    fact_ok = (prod_ == num_poly)
    jvals = {}
    j_ok = True
    for (b1, want) in ((-14, -884736), (4, 287496), (18, -32768), (22, 1728)):
        u0, u1 = pmod_monic_quadratic(ppow([3125, 250, 1], 3), b1, 125)
        w0, w1_ = pmod_monic_quadratic([0, 0, 0, 0, 0, 1], b1, 125)
        jv = Fraction(u1, w1_) if w1_ else None
        good = (jv is not None and u0 * w1_ == u1 * w0 and jv == want and b1 * b1 < 500)
        jvals[b1] = jv
        j_ok = j_ok and good
    sym_fact = 'sympy not available'
    if HAVE_SYMPY:
        tt = sympy.symbols('t')
        jt = (tt ** 2 + 250 * tt + 3125) ** 3 / tt ** 5
        numer = sympy.numer(sympy.together(jt - jt.subs(tt, 125 / tt)))
        fl = sympy.factor_list(numer)
        got = sorted((sympy.Poly(f, tt).all_coeffs(), m) for f, m in fl[1])
        want_f = sorted(([1, f[1], f[0]], 1) for f in facs)
        sym_fact = 'sympy factorisation gives the same five factors, each once: %s' % (got == want_f)
        fact_ok = fact_ok and (got == want_f)
    jz = j_fn(z)
    tz = t_fn(z)
    jerr = abs(jz - (tz * tz + 250 * tz + 3125) ** 3 / tz ** 5) / abs(jz)
    cm_pts = [('i', I, 1728), ('2i', 2 * I, 287496), ('(1 + i sqrt11)/2', (1 + I * mp.sqrt(11)) / 2, -32768), ('(1 + i sqrt19)/2', (1 + I * mp.sqrt(19)) / 2, -884736)]
    cm_ok = all(abs(j_fn(zz) - val) / abs(val) < TOL for _, zz, val in cm_pts)
    ok = fact_ok and jw_ok and j_ok and jerr < TOL and jt_plus == jP and jt_minus == jN
    claim('N2-R5: j(t) = j(125/t) at ten points, the roots of five given quadratics, all on that circle.',
          'numerator -(t^2-125)(t^2-14t+125)(t^2+4t+125)(t^2+18t+125)(t^2+22t+125); j: 632000+-282880 sqrt5, -884736, 287496, -32768, 1728',
          'that product equals (t^2+250t+3125)^3 - t^4 (t^2+10t+5)^3 coefficient by coefficient: %s; j at the roots: %s and %s, %s, %s, %s, %s'
          % (prod_ == num_poly, jt_plus, jt_minus, jvals[-14], jvals[4], jvals[18], jvals[22]), st(ok),
          [sym_fact, 'j(125/t) = (t^2 + 10t + 5)^3/t exactly: %s' % jw_ok,
           'j(z) against (t^2+250t+3125)^3/t^5 at z = 0.137 + 0.412 i: relative error %s (note: 1.7e-40)' % cstr(jerr, 3),
           'four quadratics t^2 + b t + 125 with b^2 < 500 have conjugate roots of product 125; t^2 = 125 has two real roots: ten points, all with t conj(t) = 125',
           'the pair over i (j = 1728, t^2 + 22t + 125) is among them; the four rational j are those of i, 2i, (1+i sqrt11)/2, (1+i sqrt19)/2 numerically: %s' % cm_ok])

    # ------------------------------------------------------------------ R9
    za, zb = (2 + I) / 5, (-2 + I) / 5
    a_p = (abs(E1(za, 1)), abs(E1(zb, 1)))
    a_m = (abs(E1(za, -1)), abs(E1(zb, -1)))
    ok = abs(a_p[0] - mpf('0.305236')) < mpf('5e-7') and a_p[1] < TOL and a_m[0] < TOL and abs(a_m[1] - mpf('0.305236')) < mpf('5e-7')
    claim('N2-R9: each weight-1 section vanishes at one elliptic point; its size at the other is 0.305236.',
          'chi(2) = +i: 0.305236 at (2+i)/5, 8e-42 at (-2+i)/5; chi(2) = -i: 8e-42, 0.305236',
          'chi(2) = +i: %s, %s; chi(2) = -i: %s, %s' % (cstr(a_p[0], 8), cstr(a_p[1], 3), cstr(a_m[0], 3), cstr(a_m[1], 8)), st(ok),
          ['E1_chi = L(0,chi)/2 + sum_n (sum over d dividing n of chi(d)) q^n, constant term (3 + i)/10 for chi(2) = i',
           '   (the normalisation is inferred: it reproduces both 0.305236 and the constant -40 below)',
           'forced by the elliptic element: at (2+i)/5, c z + d = i and chi(-2) i = -chi(2) i, which is -1 exactly when chi(2) = -i'])
    mir_err = max(abs(E1(-mp.conj(zz), 1) - mp.conj(E1(zz, -1))) for zz in (z, w))
    ratios = [E1(-1 / (5 * zz), 1) / (zz * E1(zz, -1)) for zz in (z, mpc('0.31', '0.27'))]
    ratios_m = [E1(-1 / (5 * zz), -1) / (zz * E1(zz, 1)) for zz in (z, mpc('0.31', '0.27'))]
    target = mpc('1.17557050458', '-1.90211303259')
    gauss = sum(chi_table(1)[a_] * mp.exp(2j * mp.pi * a_ / 5) for a_ in range(1, 5))
    ok = mir_err < TOL and all(abs(r - target) < mpf('1e-11') for r in ratios) and abs(ratios[0] - ratios[1]) < TOL
    claim('N2-R9: the mirror and W carry each weight-1 section to the other; the W ratio is constant.',
          'mirror error 0.0; ratio 1.17557050458 - 1.90211303259 i at two points',
          'mirror error %s; ratio %s and %s' % (cstr(mir_err, 3), cstr(ratios[0], 12), cstr(ratios[1], 12)), st(ok),
          ['ratio = E1_chi(Wz)/(z E1_chibar(z)) with W z = -1/(5z) and chi(2) = +i',
           'the constant is minus the Gauss sum of chi: distance %s' % cstr(abs(ratios[0] + gauss), 3),
           'for the other character the constant is %s' % cstr(ratios_m[0], 12)])
    e2v = (abs(E2star(za)), abs(E2star(zb)))
    rr = [E2star(zz) / (E1(zz, 1) * E1(zz, -1)) for zz in (z, mpc('0.31', '0.27'))]
    ok = e2v[0] < TOL and e2v[1] < TOL and all(abs(r + 40) < TOL for r in rr)
    claim('N2-R9: the weight-2 section vanishes at both elliptic points and is -40 times the product.',
          'size 1.1e-40 at both; ratio -40.0 at two points', 'size %s and %s; ratio -40 with errors %s and %s'
          % (cstr(e2v[0], 3), cstr(e2v[1], 3), cstr(abs(rr[0] + 40), 3), cstr(abs(rr[1] + 40), 3)), st(ok),
          ['E2* = E2(z) - 5 E2(5z), E2 = 1 - 24 sum sigma(n) q^n (normalisation inferred from the constant -40)'])

    # ------------------------------------------------------------------ statements of the literature
    g0, c0, e20, e30 = int(Xln['genus']), len(Xln['widths']), Xln['e2'], Xln['e3']

    def dimM_even(k):
        return (k - 1) * (g0 - 1) + (k // 4) * e20 + (k // 3) * e30 + (k // 2) * c0
    g1, c1, e31 = int(Xpm['genus']), len(Xpm['widths']), Xpm['e3']

    def dimM_odd_G1(k):
        return (k - 1) * (g1 - 1) + (k // 3) * e31 + Fraction(k, 2) * c1        # all four cusps regular
    dims = dict(M2=dimM_even(2), S4=dimM_even(4) - c0, S6=dimM_even(6) - c0, M1_each=Fraction(c1, 2) / 2, S5_each=(dimM_odd_G1(5) - c1) / 2)
    gens_std = [mmul(mmul(G_FRAME, h), ginv) for h in Xln['gens']]
    wt4 = max(abs(eta4eta4(mob(gm, w)) - (gm[1][0] * w + gm[1][1]) ** 4 * eta4eta4(w)) / abs(eta4eta4(w)) for gm in gens_std)
    claim('N2-s3: the listed spaces of forms (weights 1, 2, 4, 5, 6) are one-dimensional.',
          '1, 1, 1, 1, 1 (weight 1 each odd character; weight 2; cusp forms of weight 4 and 6; weight 5 each odd character)',
          'not derived here; the classical dimension formulas, fed with the invariants recomputed above, return %s, %s, %s, %s, %s'
          % (dims['M1_each'], dims['M2'], dims['S4'], dims['S6'], dims['S5_each']), NOTRE,
          ['these rest on Riemann-Roch (dimension formulas of the literature); only the invariants entering them are recomputed here',
           'eta(z)^4 eta(5z)^4 transforms with weight 4 under the generators of Gamma_0(5), numerically: greatest relative error %s' % cstr(wt4, 3),
           '"vanishes nowhere else" follows from the valence formula (weight x index / 12 zeros): 1/2 for weight 1, 1 for weight 2, with index 6'])
    claim('N2-s3: no eigenvalue below the continuous spectrum at level 5 (Selberg).',
          'lambda_1 at least 1/4, a theorem at small level', 'a statement of the literature', NOTRE)
    claim('N2-s1: closed geodesics of the quotient are the classes of hyperbolic elements.',
          'classical correspondence', 'a statement of the literature', NOTRE)
    claim('N2-s4: a symmetric C1 function is stationary at isolated fixed points of the symmetries.',
          'statement with proof (section 4)', 'a general lemma, not a finite computation; the fixed sets it is applied to are recomputed above', NOTRE)


# ========================================================================================
# summary
# ========================================================================================

def remarks():
    """Ambiguities met, and what was not recomputed.  The numbers quoted are the ones computed above."""
    out('=' * 110)
    out('REMARKS: DISAGREEMENTS AND AMBIGUITIES')
    out('=' * 110)
    nd = [c['n'] for c in CLAIMS if c['status'] == DISAGREE]
    out('Disagreements: %s' % (nd if nd else 'none.  Every number recomputed here equals the note\'s to every digit the note prints.'))
    out()
    out('A0. Sources.  The claimed values are those of the notes\' text and of their committed result files')
    out('    (out_value_not_place.json, postreview_checks_out.txt, whole_level5_facts_out.json, whole_level5_facts_2_out.json).')
    out('    The notes\' scripts were not run and their code was not read or copied.  A text search for the record\'s apexes')
    out('    displayed one docstring line of note 1\'s script and three of an earlier card\'s script (prose only).  The two')
    out('    apexes used for V0 were read from the record itself (the findings of B1857 on the main line).  For the convention')
    out('    on L and R (A1) the opening lines of the main line\'s own test of B1872 were read, after this script was written.')
    out()
    if 'conv' in NOTES:
        out('A1. Which matrices are L and R (a labelling point; no number depends on it).')
        out("    Note 2's fact R7 prints LR = [[1,1],[1,2]] = F^2, F = [[0,1],[1,1]]: that is L.R for L = [[1,0],[1,1]], R = [[1,1],[0,1]].")
        out('    The request gives L = [[1,1],[0,1]], R = [[1,0],[1,1]], for which L.R = [[2,1],[1,1]].  Computed with both:')
        for (lr, v, eig, res) in NOTES['conv']:
            out('      LR = %s, line %s, a line of LR: %-5s; run:closures (0 to 11) at which it is kept:  %s' % (lr, v, eig, res))
        out('    So with the request\'s matrices the mark (1,3) is not a line of LR: it is the line of RL, the line of LR is (1,2),')
        out('    and F^2 = RL.  Taken literally (those matrices with v = (1,3)), card cell V3 would fail: whether a run keeps the line')
        out('    then depends on the closure.  The two conventions differ by exchanging L and R; every statement survives once')
        out("    \"the mark\" is read as LR's own line.  \"LR's line is (1,3)\" and \"F^2 = LR\" are true only in the notes' convention.")
        out()
    if 'one_period' in NOTES:
        out('A2. "Closed by g golden periods".  The note writes L^n R (LR)^k, and L^6 R L R for one period: the departure, one run')
        out('    of 1, then g pairs (1,1), that is 2g+1 runs of 1.  A literal "g pairs (1,1)" would give 2g runs.  For (6) with one')
        out('    period: runs (6,1,1,1) give %s, the note\'s value; runs (6,1,1) give %s, which is not.' % (f8(NOTES['one_period'][0], 10), f8(NOTES['one_period'][1], 10)))
        out()
    if 'off' in NOTES:
        a_off, g_off = NOTES['off']
        out('A3. "Distance" and "offset" in the result file of V1 are the greatest over the copies.  The greatest distance is always')
        out("    the apex's own (every copy reads above the own value).  For the offset the two differ, as the note's text says:")
        out("    at k = 1 the apex's own offset is %s with 2, 3, 4 copies of (6); the greatest over copies is %s."
            % (', '.join(f8(v, 5) for v in a_off), ', '.join(f8(v, 5) for v in g_off)))
        out('    The text\'s "0.017" is the four-copy case.')
        out()
    out('A4. Two-copy spread.  Exact arithmetic gives 0 in all fifteen rows and the apex is attained exactly twice.  The result')
    out('    file prints 3.1e-61 and 1.6e-61 in three rows: rounding noise, far below the note\'s tolerance of 1e-45.')
    out()
    if 'ratio27' in NOTES:
        out('A5. "About 27 times closer".  The ratio of the k = 1 distances, copies of (6) to copies of (2,1,2,1,2), is %s'
            % f8(NOTES['ratio27'][0], 4))
        out('    (it rounds to 28).  Against copies of (11) it is %s.' % f8(NOTES['ratio27'][1], 4))
        out()
    if 'own' in NOTES:
        out('A6. Own values and their exact limits.  60-period own value minus the exact value in an infinite ground:')
        for name, (lim, d) in NOTES['own'].items():
            out('      %-12s limit %-22s difference %s' % (name, lim, f8(d, 3)))
        if 'AB' in NOTES:
            out('      A = (2,1,1,4,4): limit %s;  B = (2,1,2,4,4): limit %s' % NOTES['AB'])
        out()
    if 'devs' in NOTES and 'Cn' in NOTES:
        out('A7. The limit, beyond the card.  The distance of d(k)/d(k+1) from phi^4, two copies, at k = 5 and k = 30:')
        for name, devs in NOTES['devs'].items():
            out('      %-12s %s and %s' % (name, f8(devs[0], 3), f8(devs[-1], 3)))
        out('    Closed form derived here, for two copies of a single run n: d(k) phi^(4k) tends to')
        out('    sqrt5 (n-1)(1+phi^-4)/(2 (n-1+sqrt5) phi^4) = %s' % ', '.join('%s for n = %d' % (f8(c, 8), n) for n, c in NOTES['Cn'].items()))
        out()
    if 'v0' in NOTES:
        out("A8. V0 rests on the record: the comparison is with the record's printed six-place apexes 3.618034 and 1.723607;")
        out('    the differences are %s.' % ' and '.join(f8(v, 3) for v in NOTES['v0'].values()))
        out()
    if 'samples' in NOTES:
        n63, s4, am, nbig = NOTES['samples']
        out('A9. Sample sizes of note 2.  The note does not say which matrices were searched.  "63 matrices examined" is reproduced')
        out('    by every factorisation a d = 1 + 5c^2 with c from -6 to 6 (%d).  "17 and 16 found" is not reproduced by the same kind' % n63)
        out('    of box: c from -4 to 4 gives %d + %d.  It is reproduced when a is also bounded, by any bound from %s to %s.'
            % (s4[0], s4[1], am[0] if am else '?', am[1] if am else '?'))
        out('    The mathematical claim behind the counts was checked on %d matrices (all with c up to 200 in absolute value).' % nbig)
        out()
    out('A10. Normalisations in R9.  The note\'s text does not define E1_chi or E2*.  Used here: E1_chi = L(0,chi)/2 +')
    out('    sum_n (sum over d dividing n of chi(d)) q^n, constant term (3 + i)/10 for chi(2) = i; E2* = E2(z) - 5 E2(5z).')
    out('    They are inferred, and they reproduce both printed numbers (0.305236 and the constant -40).  The zeros, the')
    out('    constancy of the ratios and the mirror relation do not depend on them.')
    out()
    if 'd_std' in NOTES:
        out('A11. Unstated test elements.  R3 does not say which delta was used in the standard frame, nor R9 which two points.')
        out('    Here s(delta w) = -1/s(w) was checked for g delta g^-1 = %s and four other elements of Gamma_0(5) with' % NOTES['d_std'])
        out('    d = +-2 mod 5, and s was found unchanged by four elements with d = +-1 mod 5.')
        out()
    if 'aut' in NOTES:
        out('A12. "No others".  That the symmetries of X_line are four and those of X_pm eight was decided here as a statement about')
        out('    conformal and anti-conformal automorphisms of the sphere with its punctures and cone points, by exact cross-ratios:')
        out('    %d + %d for X_line, %d + %d for X_pm.  The note took this from its referee and the literature.'
            % (NOTES['aut'][0], NOTES['aut'][1], NOTES['aut'][2], NOTES['aut'][2]))
        out()
    out('A13. Error sizes.  Where the note prints the size of a numerical error (9.8e-39, 1.7e-40 and the like) the figure is')
    out('    noise at its working precision; here the same identities hold to about 1e-59.  They are compared as "the identity')
    out('    holds", not digit by digit.')
    out()
    out('A14. A bug of this script, found and fixed while it was written.  The translation step of the Gauss reduction used')
    out('    floor((B + A)/(2A)), which leaves B = -A unreduced: the second class came out as (2,-2,3).  It was noticed because')
    out('    that form is not reduced and a later step found no class named (2,2,3).  The step now gives -A < B <= A.')
    out('    Nothing was tuned to a number of the notes.')
    out()
    out('=' * 110)
    out('NOT RECOMPUTED, AND WHY')
    out('=' * 110)
    for c in CLAIMS:
        if c['status'] == NOTRE:
            out('[%3d] %s' % (c['n'], c['text']))
            out('      %s' % c['mine'])
    out('Outside the numbered list: the topic sweeps of the record, quotations from the record, priors and the review history')
    out('in both notes, and the notes\' readings of what the facts mean.  These are not mathematical claims.')
    out()


def summary():
    out('=' * 110)
    out('SUMMARY TABLE')
    out('=' * 110)
    out('Labels: N1, N2 = the note; s1, s2, ... = its section; head = its headline; V0 to V3 = the cells of note 1\'s sealed card;')
    out('Q1 to Q7 and R1 to R9 = the facts of note 2.  Each row is detailed above under the same number.')
    out()
    out('| # | claim (at most 20 words) | the note\'s value | value found here | status |')
    out('|---|---|---|---|---|')
    for c in CLAIMS:
        out('| %d | %s | %s | %s | %s |' % (c['n'], c['text'], c['note'], c['mine'], c['status']))
    out()
    long_ = [c['n'] for c in CLAIMS if len(c['text'].split()) > 20]
    piped = [c['n'] for c in CLAIMS if '|' in c['text'] + c['note'] + c['mine']]
    out('claims whose text exceeds 20 words: %s; table cells containing a bar: %s' % (long_ if long_ else 'none', piped if piped else 'none'))
    na = sum(1 for c in CLAIMS if c['status'] == AGREE)
    nd = sum(1 for c in CLAIMS if c['status'] == DISAGREE)
    nn = sum(1 for c in CLAIMS if c['status'] == NOTRE)
    n1 = [c for c in CLAIMS if c['text'].startswith('N1')]
    n2 = [c for c in CLAIMS if c['text'].startswith('N2')]
    out('self-checks of the instrument: exact forms agree: %s; numerical continued fractions agree: %s;'
        % (SELF.get('instrument_exact'), SELF.get('instrument_numeric')))
    out('self-check of the comparison (a last digit changed is rejected): %s' % SELF.get('comparison'))
    out('libraries: mpmath %s, sympy %s' % ('present' if HAVE_MP else 'absent', 'present' if HAVE_SYMPY else 'absent'))
    out()
    for nm, cs in (('note 1', n1), ('note 2', n2)):
        out('%s: %d claims; AGREE %d; DISAGREE %d; NOT RECOMPUTED %d'
            % (nm, len(cs), sum(1 for c in cs if c['status'] == AGREE), sum(1 for c in cs if c['status'] == DISAGREE),
               sum(1 for c in cs if c['status'] == NOTRE)))
    out('FINAL COUNT: %d claims listed; AGREE %d; DISAGREE %d; NOT RECOMPUTED %d' % (len(CLAIMS), na, nd, nn))
    if nd:
        out('DISAGREEMENTS: claims %s' % [c['n'] for c in CLAIMS if c['status'] == DISAGREE])


def main():
    out('verify_web_seat_relays.py -- independent re-derivation of the exact claims of two notes')
    out('(data-free mathematics; nothing here is measured or compared with a measured value)')
    out()
    part1()
    part2()
    remarks()
    summary()
    text = '\n'.join(OUT) + '\n'
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'verify_web_seat_relays_out.txt'), 'w') as fh:
        fh.write(text)
    sys.stdout.write(text)


if __name__ == '__main__':
    main()
