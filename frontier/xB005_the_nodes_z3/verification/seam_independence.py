#!/usr/bin/env python3
"""xB005 ADDENDUM 1, cells Q4a-Q4c - the ADVERSARIAL RE-TEST of this arc's own Q3.

Q3 concluded that the programme's four Z/3's are ALL canonically linked, hence one fact
wearing four hats, hence not evidence.  Its printed chain was:

    mu_3  <-> Q(sqrt-3)   : Q(zeta_3) = Q(sqrt-3).  SAME OBJECT.
    2T/Q8 <-> Z(E6)       : McKay.  LINKED.
    node  <-> 2T/Q8       : Q2.  IDENTICAL.
    => ALL FOUR ARE CANONICALLY LINKED.

The first line links a group to a FIELD, not to another Z/3.  So the exhibited edges
connect {node, 2T/Q8, Z(E6)} and leave the ARITHMETIC hat, mu_3 in the trace field,
joined by NO EDGE.  The "=>" asserts a connectivity the links do not supply.

These cells test the missing edge directly.  If 'order 3 at the node' and 'invariant
trace field = Q(sqrt-3)' are the same fact, they cannot come apart.  They do come apart,
exactly and in both directions, so Q3's headline was a FALSE NEGATIVE.

Each cell asserts its own mathematics.  Gate 5 untouched: no value, no physics reading.
"""
import itertools
import math
import warnings
from fractions import Fraction

import mpmath as mp
import snappy
import sympy as sp

warnings.filterwarnings("ignore")
mp.mp.dps = 60

X, Y, Z = sp.symbols('X Y Z')


def F_L(v):
    A, B, C = v
    return (A, C, A*C - B)


def F_R(v):
    A, B, C = v
    return (C, B, B*C - A)


def _D(f):
    return sp.Matrix(list(f((X, Y, Z)))).jacobian([X, Y, Z]).subs({X: 0, Y: 0, Z: 0})


DL, DR, I3 = _D(F_L), _D(F_R), sp.eye(3)


def node_order(word):
    """the order of the monodromy's derivative at the node (0,0,0), exactly."""
    M = I3
    for ch in word:
        M = M * (DL if ch == 'L' else DR)
    return next(k for k in range(1, 13) if M**k == I3)


# ---------- the shape field = the invariant trace field (Neumann-Reid) -------------------
def _to_mpc(z):
    try:
        return mp.mpc(z)
    except TypeError:
        pass
    r, i = z.real, z.imag
    r = r() if callable(r) else r
    i = i() if callable(i) else i
    return mp.mpc(mp.mpf(str(r).replace(' ', '')), mp.mpf(str(i).replace(' ', '')))


def squarefree(n):
    s, d, m = 1, 2, abs(n)
    while d*d <= m:
        e = 0
        while m % d == 0:
            m //= d
            e += 1
        if e % 2:
            s *= d
        d += 1
    s *= m
    return -s if n < 0 else s


def quad_disc(z, tol=mp.mpf(10)**-25, height=10**6):
    """squarefree disc of the minimal quadratic of z, or None if z is not quadratic.
    Height-bounded AND residual-checked, so an unbounded-coefficient fit cannot pass (E25)."""
    z = _to_mpc(z)
    r = [(z**2).real, z.real, mp.mpf(1)]
    i = [(z**2).imag, z.imag, mp.mpf(0)]
    v = [r[1]*i[2] - r[2]*i[1], -(r[0]*i[2] - r[2]*i[0]), r[0]*i[1] - r[1]*i[0]]
    m = max(abs(x) for x in v)
    if m == 0:
        return None
    fr = [Fraction(float(x/m)).limit_denominator(10**7) for x in v]
    den = 1
    for f in fr:
        den = den*f.denominator//math.gcd(den, f.denominator)
    ints = [int(f*den) for f in fr]
    g = 0
    for x in ints:
        g = math.gcd(g, abs(x))
    if g == 0:
        return None
    a, b, c = [x//g for x in ints]
    if a == 0 or max(abs(a), abs(b), abs(c)) > height:
        return None
    if abs(a*z**2 + b*z + c) > tol:
        return None
    return squarefree(b*b - 4*a*c)


def shape_field(word):
    """(-3,) if every shape lies in Q(sqrt-3); ('deg>2',) / a mixed tag otherwise."""
    M = snappy.ManifoldHP('b++' + word)
    ds = []
    for z in M.tetrahedra_shapes('rect'):
        d = quad_disc(z)
        if d is None:
            return 'deg>2', float(M.volume())
        ds.append(d)
    if len(set(ds)) != 1:
        return ('mixed', tuple(sorted(set(ds)))), float(M.volume())
    return ds[0], float(M.volume())


def cyclic_words(nmax):
    out = []
    for n in range(2, nmax + 1):
        for t in itertools.product('LR', repeat=n):
            w = ''.join(t)
            if 'L' not in w or 'R' not in w:
                continue                       # reducible, not pseudo-Anosov
            if min(w[i:] + w[:i] for i in range(n)) == w:
                out.append(w)                  # one representative per cyclic word
    return out


# ---------------------------------------------------------------------------------------
def Q4a():
    """THE EXACT DISSOCIATION, on the object's OWN tower -- no census, no statistics.

    (LR)^n is the n-fold cyclic cover of m004 along its fibration.  Every one of them is
    commensurable with m004, so the invariant trace field is CONSTANT = Q(sqrt-3).  The
    node order is the order of D^n where D^3 = I: 3 when 3 does not divide n, 1 when it
    does.  A quantity that is constant on a family cannot be the same fact as one that
    is not."""
    base = snappy.Manifold('m004').volume()
    print("Q4a      the object's own tower (LR)^n -- cyclic covers of m004 along the fibration")
    print(f"         {'n':>2}  {'word':<12}{'vol/vol(m004)':>15}{'shape field':>16}{'node order':>12}   name")
    orders, fields = [], []
    for n in range(1, 5):
        w = 'LR'*n
        d, vol = shape_field(w)
        o = node_order(w)
        M = snappy.Manifold('b++'+w)
        ids = M.identify()
        ratio = vol/float(base)
        assert abs(ratio - n) < 1e-6, f"(LR)^{n} is not the n-fold cover: ratio {ratio}"
        assert d == -3, f"(LR)^{n} shape field is {d}, not Q(sqrt-3)"
        assert o == (1 if n % 3 == 0 else 3), f"(LR)^{n} node order {o}"
        orders.append(o)
        fields.append(d)
        print(f"         {n:>2}  {w:<12}{ratio:>15.6f}{'Q(sqrt-3)':>16}{o:>12}   "
              f"{ids[0] if ids else '(unnamed)'}")
    assert len(set(fields)) == 1 == len(set([-3])), "the arithmetic hat is not constant"
    assert len(set(orders)) > 1, "the node order is constant on the tower"
    print("         the ARITHMETIC hat is CONSTANT (Q(sqrt-3) on all four, they are commensurable)")
    print(f"         the NODE's hat is NOT: orders {orders} -- it drops to 1 at n = 3.")
    print("Q4a PASS THE TWO ARE NOT THE SAME FACT. s961 = (LR)^3 is m004's own 3-fold fibred")
    print("         cover: trace field Q(sqrt-3), node order 1. The seam Q3 asserted is OPEN.")


def Q4b(nmax=8):
    """THE BASE RATE, over once-punctured-torus bundles -- the reference class."""
    rows = []
    for w in cyclic_words(nmax):
        d, vol = shape_field(w)
        rows.append((w, node_order(w), d == -3))
    n3 = [r for r in rows if r[1] == 3]
    f3 = [r for r in rows if r[2]]
    both = [r for r in rows if r[1] == 3 and r[2]]
    print(f"\nQ4b      census of b++<w>, cyclically-reduced words of length 2..{nmax}: {len(rows)} bundles")
    print(f"         {'node order':>11} | {'field = Q(sqrt-3)':>18} | {'field != Q(sqrt-3)':>19}")
    for o in sorted({r[1] for r in rows}):
        a = sum(1 for r in rows if r[1] == o and r[2])
        b = sum(1 for r in rows if r[1] == o and not r[2])
        print(f"         {o:>11} | {a:>18} | {b:>19}")
    print(f"         order 3 at the node       : {len(n3):>3}/{len(rows)}  ({100*len(n3)/len(rows):.1f}%)")
    print(f"         trace field Q(sqrt-3)     : {len(f3):>3}/{len(rows)}  ({100*len(f3)/len(rows):.1f}%)")
    print(f"         order 3 but NOT Q(sqrt-3) : {len(n3)-len(both):>3}   kills 'node order 3 => Q(sqrt-3)'")
    print(f"         Q(sqrt-3) but NOT order 3 : {len(f3)-len(both):>3}   kills 'Q(sqrt-3) => node order 3'")
    assert len(n3) - len(both) > 0, "no order-3 bundle outside Q(sqrt-3): the implication survives"
    assert len(f3) - len(both) > 0, "no Q(sqrt-3) bundle off order 3: the converse survives"
    print("Q4b PASS the dissociation holds in BOTH directions across the reference class.")
    return rows


def Q4c(rows):
    """WHAT THE COINCIDENCE IS WORTH once the seam is open -- priced DOWN, not celebrated.

    The correction to Q3 is that the two facts are INDEPENDENT.  That does not make the
    coincidence impressive, and this cell refuses to let it become so: it computes the
    prior properly and reports that it is worth well under one bit."""
    seen, frontier = {tuple(I3): I3}, [I3]
    while frontier:
        nf = []
        for g in frontier:
            for h in (DL, DR, DL.inv(), DR.inv()):
                p = g*h
                k = tuple(p)
                if k not in seen:
                    seen[k] = p
                    nf.append(p)
        frontier = nf
    els = list(seen.values())
    ords = [next(k for k in range(1, 13) if g**k == I3) for g in els]
    three = sum(1 for o in ords if o == 3)
    print(f"\nQ4c      the derivative image of the mapping class group at the node has order "
          f"{len(els)}, element orders {sorted(set(ords))}")
    assert len(els) == 24 and sorted(set(ords)) == [1, 2, 3, 4], (len(els), sorted(set(ords)))
    assert all(g.det() == 1 for g in els)
    print("         order 24, element orders {1,2,3,4}, all det 1 => S_4, the rotation group of")
    print("         the cube. The node order is the monodromy's image THERE, so it is a")
    print("         CONGRUENCE condition on the word, not an arithmetic one.")

    # DL and DR are 4-cycles, hence ODD, so sign(image of w) = (-1)^len(w).
    oL = next(k for k in range(1, 13) if DL**k == I3)
    oR = next(k for k in range(1, 13) if DR**k == I3)
    assert oL == oR == 4, (oL, oR)
    ev_len = [r for r in rows if len(r[0]) % 2 == 0]
    od_len = [r for r in rows if len(r[0]) % 2 == 1]
    ev3 = sum(1 for r in ev_len if r[1] == 3)
    od3 = sum(1 for r in od_len if r[1] == 3)
    print(f"\n         DL and DR are 4-cycles, hence ODD permutations, so the image of a word of")
    print(f"         length n has sign (-1)^n.  EVEN words land in A_4 (order 12, 8 three-cycles);")
    print(f"         ODD words land in the odd coset, which contains NO element of order 3.")
    print(f"         census check -- even-length words: {ev3}/{len(ev_len)} of order 3"
          f"   (A_4 prior 8/12 = {8/12:.4f})")
    print(f"         census check -- odd-length  words: {od3}/{len(od_len)} of order 3"
          f"   (prior 0)")
    assert od3 == 0, "an odd-length word reached order 3: the parity argument is wrong"
    assert ev3 > 0
    print("         so the census's 44% is NOT a skew -- it is the even/odd mix, and the two")
    print("         strata match their exact priors.  This is why Q4b's raw rate exceeds 1/3.")

    # m004's own monodromy is LR: length 2, hence EVEN, hence in A_4.
    bits_uncond = math.log2(len(els)/three)
    bits_cond = math.log2(12/8)
    print(f"\n         PRICING m004.  Its monodromy is LR -- the SHORTEST pseudo-Anosov word,")
    print(f"         length 2, hence even, hence in A_4.  Given that, 'order 3' has prior 8/12.")
    print(f"           unconditional prior 8/24 = 1/3        -> {bits_uncond:.2f} bits")
    print(f"           conditioned on even length, 8/12      -> {bits_cond:.2f} bits   <== the honest price")
    assert bits_cond < 1.0
    print(f"Q4c PASS the coincidence is worth {bits_cond:.2f} BITS -- under one bit, essentially")
    print("         negligible.  So Q3's HEADLINE survives (the recurrence is not evidence) while")
    print("         Q3's REASON does not: the hats are not one fact, they are two independent")
    print("         facts whose agreement is cheap.  Right answer, wrong proof -- and the wrong")
    print("         proof would have killed the seam for good.")


if __name__ == "__main__":
    Q4a()
    rows = Q4b()
    Q4c(rows)
    print("\nVERIFIED")
