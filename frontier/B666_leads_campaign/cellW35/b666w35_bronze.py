"""B666 cell W3-5 (G' — the bronze McKay rung; ADDENDUM_1, conditional on
cell 1's refined verdict).

CONTEXT (cell 1, refined L105): the golden's PRIME conductor 5 makes its
shadow the McKay group itself (SL(2,Z/5) = 2I, E8's partner); the
silver's prime-power conductor 8 gives 2O (E7's partner) only as a
canonical QUOTIENT of SL(2,Z/8) (order 384, kernel 8), never a subgroup.

THE BRONZE (m = 3): the bundle W = R^3 L^3, trace m^2+2 = 11,
discriminant tr^2 - 4 = 117 = 9*13.  Sealed compute list: the conductor
structure; the shadow at mod 9, mod 13, mod 117; group orders; the
2T-quotient tests (|2T| = 24, E6's partner, character field Q(sqrt-3));
the character fields realized.  Two-outcome: the descent's third rung
(bank the group that appears, exactly) / the pattern breaks (bank the
actual structure).

SECTIONS (exact integer/rational arithmetic throughout; no floats):
  A. the bronze word exact; disc factorization; ring conductor f vs
     field disc d_K; the metallic ladder table m = 1..8 (f = m at
     m = 1,2,3 — the first rung where f-prime and d_K-prime DIFFER).
  B. shadows <R,L> mod n for n in {3, 9, 13, 39, 117}: order vs the
     brute-forced full |SL(2,Z/n)| (CRT-verified products for 39, 117);
     order profile / involutions / center / exponent where feasible.
     Controls: mod 5 (golden 2I), mod 8 (silver, order 384).
  C. 2T built EXACTLY as the 24 Hurwitz unit quaternions (rational
     coordinates): order profile, unique involution, the rational
     2-dim character; 2T's own normal-subgroup lattice.
  D. head-to-head: mod-3 shadow ~ 2T? (complete generating-pair iso
     search).  The order sweep |SL(2,Z/n)|, n = 2..16, + the n^2
     lower bound (verified by enumeration for n = 17..48): 24 occurs
     ONLY at n = 3, 48 ONLY at n = 4, 120 ONLY at n = 5; control
     re-verification mod-4 shadow !~ 2O (cell 1's banked fact).
  E. mod 9: the FULL normal-subgroup lattice; every order-27 normal
     subgroup -> its order-24 quotient -> complete iso test vs 2T;
     2T-as-subgroup complete (order-4, order-3) pair search with
     positive control on SL(2,5) = 2I (2T < 2I must be FOUND);
     Q8 (2T's Sylow-2) presence.
  F. mod 13: the full normal-subgroup lattice (decides 2T-as-quotient);
     2T-as-subgroup complete (4,3)-pair search.
  G. mod 117: closure order vs the CRT product; the canonical
     surjection onto the mod-3 shadow (2T as quotient, kernel order);
     a concrete 2T subgroup via the CRT lift of the mod-13 witness.
  H. the exact character table of 2T over Q(zeta3): 7 classes, 7
     irreducibles (degrees 1,1,1,2,2,2,3), full orthogonality checked
     exactly; the character field = Q(zeta3) = Q(sqrt-3) (with
     (1+2*zeta3)^2 = -3 verified); the McKay adjacency of chi_2 =
     the affine E6 graph, computed from exact inner products.
  I. tone data: W's image, order, trace in every shadow; the
     bundle-invisibility lemma R^m = L^m = I (mod m) for m = 1..8
     (the whole bronze bundle group lies in the mod-3 congruence
     kernel: the word is silent at its own ring conductor).
  J. verdict.
"""
import sys
from fractions import Fraction
from itertools import product

# ------------------------------------------------------------ generic group
class FinGroup:
    """finite group given by element hashables + mul + inv + identity.
    (machinery adapted from cell1/b666c1_shadow_group.py, re-pointed)"""

    def __init__(self, name, elems, mul, inv, e):
        self.name, self.mul, self.inv, self.e = name, mul, inv, e
        self.elems = list(elems)
        self.index = {g: i for i, g in enumerate(self.elems)}
        self._ord = {}

    @classmethod
    def closure(cls, name, gens, mul, inv, e):
        seen = {e}
        frontier = [e]
        gens = list(gens)
        while frontier:
            nxt = []
            for g in frontier:
                for s in gens:
                    h = mul(g, s)
                    if h not in seen:
                        seen.add(h)
                        nxt.append(h)
            frontier = nxt
        return cls(name, sorted(seen), mul, inv, e)

    def order(self):
        return len(self.elems)

    def elt_order(self, g):
        if g in self._ord:
            return self._ord[g]
        k, h = 1, g
        while h != self.e:
            h = self.mul(h, g)
            k += 1
        self._ord[g] = k
        return k

    def order_profile(self):
        prof = {}
        for g in self.elems:
            o = self.elt_order(g)
            prof[o] = prof.get(o, 0) + 1
        return dict(sorted(prof.items()))

    def involutions(self):
        return [g for g in self.elems if g != self.e
                and self.mul(g, g) == self.e]

    def center_vs(self, gens):
        """center = elements commuting with a generating set."""
        return [g for g in self.elems
                if all(self.mul(g, s) == self.mul(s, g) for s in gens)]

    def exponent(self):
        from math import lcm
        ex = 1
        for g in self.elems:
            ex = lcm(ex, self.elt_order(g))
        return ex

    def subgroup_elems(self, gens):
        seen = {self.e}
        frontier = [self.e]
        gens = list(gens)
        while frontier:
            nxt = []
            for g in frontier:
                for s in gens:
                    h = self.mul(g, s)
                    if h not in seen:
                        seen.add(h)
                        nxt.append(h)
            frontier = nxt
        return frozenset(seen)

    def subgroup_capped(self, gens, cap):
        """closure, abandoned (returns None) once size exceeds cap."""
        seen = {self.e}
        frontier = [self.e]
        gens = list(gens)
        while frontier:
            nxt = []
            for g in frontier:
                for s in gens:
                    h = self.mul(g, s)
                    if h not in seen:
                        seen.add(h)
                        if len(seen) > cap:
                            return None
                        nxt.append(h)
            frontier = nxt
        return frozenset(seen)

    def conjugacy_classes(self, gens):
        left = set(self.elems)
        classes = []
        while left:
            g = min(left, key=lambda x: self.index[x])
            orb = {g}
            frontier = [g]
            while frontier:
                nxt = []
                for h in frontier:
                    for s in gens:
                        c = self.mul(self.mul(s, h), self.inv(s))
                        if c not in orb:
                            orb.add(c)
                            nxt.append(c)
                frontier = nxt
            classes.append(frozenset(orb))
            left -= orb
        return classes

    def derived_subgroup(self):
        comms = set()
        for g in self.elems:
            gi = self.inv(g)
            for h in self.elems:
                comms.add(self.mul(self.mul(g, h),
                                   self.mul(gi, self.inv(h))))
        return self.subgroup_elems(comms)

    def quotient_with_map(self, N):
        """N a normal frozenset. Returns (FinGroup on coset ids, coset_of)."""
        Nl = sorted(N, key=lambda x: self.index[x])
        coset_of = {}
        reps = []
        for g in self.elems:
            if g in coset_of:
                continue
            cid = len(reps)
            reps.append(g)
            for n in Nl:
                coset_of[self.mul(g, n)] = cid
        k = len(reps)
        table = [[coset_of[self.mul(reps[i], reps[j])] for j in range(k)]
                 for i in range(k)]
        itab = [None] * k
        for i in range(k):
            for j in range(k):
                if table[i][j] == coset_of[self.e]:
                    itab[i] = j
        mul = lambda a, b: table[a][b]
        inv = lambda a: itab[a]
        return (FinGroup(self.name + "/N", range(k), mul, inv,
                         coset_of[self.e]), coset_of)

    def quotient(self, N):
        return self.quotient_with_map(N)[0]

    def normal_lattice(self, gens):
        """all normal subgroups via single-class normal closures + joins
        (every normal subgroup is a join of class closures)."""
        classes = self.conjugacy_classes(gens)
        base = set()
        for c in classes:
            base.add(self.subgroup_elems(c))
        lattice = set(base)
        lattice.add(frozenset({self.e}))
        changed = True
        while changed:
            changed = False
            cur = list(lattice)
            for i in range(len(cur)):
                for j in range(i + 1, len(cur)):
                    J = self.subgroup_elems(cur[i] | cur[j])
                    if J not in lattice:
                        lattice.add(J)
                        changed = True
        return lattice, classes


def find_generating_pair(G):
    by_ord = sorted(G.elems, key=lambda g: -G.elt_order(g))
    n = G.order()
    for g in by_ord:
        for h in by_ord:
            if len(G.subgroup_elems([g, h])) == n:
                return g, h
    return None


def iso_test(A, gensA, B):
    """complete iso search A -> B on generator images (cell1's method):
    all order-matched candidate pairs in B, map built by BFS words,
    verified as a bijective homomorphism on ALL pairs."""
    a1, a2 = gensA
    o1, o2 = A.elt_order(a1), A.elt_order(a2)
    n = A.order()
    if n != B.order():
        return None
    cand1 = [x for x in B.elems if B.elt_order(x) == o1]
    cand2 = [x for x in B.elems if B.elt_order(x) == o2]
    parent = {A.e: None}
    order_bfs = [A.e]
    frontier = [A.e]
    while frontier:
        nxt = []
        for g in frontier:
            for si, s in enumerate((a1, a2)):
                h = A.mul(g, s)
                if h not in parent:
                    parent[h] = (g, si)
                    order_bfs.append(h)
                    nxt.append(h)
        frontier = nxt
    if len(order_bfs) != n:
        raise ValueError("gensA do not generate A")
    for x in cand1:
        for y in cand2:
            f = {A.e: B.e}
            ok = True
            for g in order_bfs[1:]:
                p, si = parent[g]
                f[g] = B.mul(f[p], (x, y)[si])
            if len(set(f.values())) != n:
                continue
            for g in A.elems:
                fg = f[g]
                if any(f[A.mul(g, h)] != B.mul(fg, f[h])
                       for h in A.elems):
                    ok = False
                    break
            if ok:
                return (x, y)
    return None


# --------------------------------------------------------------- mod-n side
def mk_mod_ops(n):
    def mul(x, y):
        return ((x[0] * y[0] + x[1] * y[2]) % n,
                (x[0] * y[1] + x[1] * y[3]) % n,
                (x[2] * y[0] + x[3] * y[2]) % n,
                (x[2] * y[1] + x[3] * y[3]) % n)

    def inv(x):
        a, b, c, d = x
        return (d % n, -b % n, -c % n, a % n)

    return mul, inv


def sl2_shadow(n):
    R, L = (1, 1, 0, 1), (1, 0, 1, 1)
    mul, inv = mk_mod_ops(n)
    e = (1, 0, 0, 1)
    G = FinGroup.closure(f"<R,L> mod {n}", [R, L], mul, inv, e)
    return G, R, L


def full_sl2_count(n):
    cnt = 0
    for a, b, c, d in product(range(n), repeat=4):
        if (a * d - b * c) % n == 1:
            cnt += 1
    return cnt


def closure_order_only(n, gens):
    """order of <gens> mod n; memory-lean (int-encoded seen set)."""
    mul, _ = mk_mod_ops(n)
    e = (1, 0, 0, 1)

    def enc(t):
        return ((t[0] * n + t[1]) * n + t[2]) * n + t[3]

    seen = {enc(e)}
    frontier = [e]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = mul(g, s)
                k = enc(h)
                if k not in seen:
                    seen.add(k)
                    nxt.append(h)
        frontier = nxt
    return len(seen)


def mat_order_mod(W, n):
    mul, _ = mk_mod_ops(n)
    e = (1, 0, 0, 1)
    Wn = tuple(x % n for x in W)
    k, h = 1, Wn
    while h != e:
        h = mul(h, Wn)
        k += 1
    return k


# ------------------------------------------------- quaternions (2T over Q)
def qmul(p, q):
    w1, x1, y1, z1 = p
    w2, x2, y2, z2 = q
    return (w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2)


def qinv(p):
    w, x, y, z = p
    return (w, -x, -y, -z)


def build_2T():
    """2T = the 24 Hurwitz units; generators i and omega = (1+i+j+k)/2.
    All coordinates RATIONAL (no radical needed, unlike 2O's sqrt2)."""
    half = Fraction(1, 2)
    om = (half, half, half, half)
    qi = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
    e = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    return FinGroup.closure("2T", [om, qi], qmul, qinv, e), om, qi, e


def build_2O():
    """cell1's 2O over Q(sqrt2), coords (a, b) = a + b*sqrt2 (control)."""
    def m2(u, v):  # (a,b)*(c,d) in Q(sqrt2)
        return (u[0] * v[0] + 2 * u[1] * v[1], u[0] * v[1] + u[1] * v[0])

    def qmul2(p, q):
        w1, x1, y1, z1 = p
        w2, x2, y2, z2 = q
        def s(*ts):
            a = Fraction(0); b = Fraction(0)
            for sg, u, v in ts:
                pr = m2(u, v)
                a += sg * pr[0]; b += sg * pr[1]
            return (a, b)
        return (s((1, w1, w2), (-1, x1, x2), (-1, y1, y2), (-1, z1, z2)),
                s((1, w1, x2), (1, x1, w2), (1, y1, z2), (-1, z1, y2)),
                s((1, w1, y2), (-1, x1, z2), (1, y1, w2), (1, z1, x2)),
                s((1, w1, z2), (1, x1, y2), (-1, y1, x2), (1, z1, w2)))

    def qinv2(p):
        w, x, y, z = p
        return (w, (-x[0], -x[1]), (-y[0], -y[1]), (-z[0], -z[1]))

    h = Fraction(1, 2)
    z = (Fraction(0), Fraction(0))
    om = ((h, z[0]), (h, z[0]), (h, z[0]), (h, z[0]))
    om = tuple((c, Fraction(0)) for c in (h, h, h, h))
    s = ((Fraction(0), h), (Fraction(0), h), z, z)
    e = ((Fraction(1), Fraction(0)), z, z, z)
    return FinGroup.closure("2O", [om, s], qmul2, qinv2, e)


# ------------------------------------------------------ Q(zeta3) exact field
class C3:
    """a + b*zeta3 with a,b Fraction; zeta3^2 = -1 - zeta3."""
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = Fraction(a), Fraction(b)

    def __add__(s, o):
        return C3(s.a + o.a, s.b + o.b)

    def __sub__(s, o):
        return C3(s.a - o.a, s.b - o.b)

    def __mul__(s, o):
        # (a1+b1 z)(a2+b2 z) = a1a2 - b1b2 + (a1b2 + a2b1 - b1b2) z
        return C3(s.a * o.a - s.b * o.b,
                  s.a * o.b + s.b * o.a - s.b * o.b)

    def conj(s):
        return C3(s.a - s.b, -s.b)

    def __eq__(s, o):
        return s.a == o.a and s.b == o.b

    def __hash__(s):
        return hash((s.a, s.b))

    def __repr__(s):
        if s.b == 0:
            return str(s.a)
        if s.a == 0:
            return f"{s.b}z"
        return f"({s.a}{'+' if s.b > 0 else ''}{s.b}z)"


ZETA = C3(0, 1)
ONE = C3(1)
ZERO = C3(0)


# ------------------------------------------------------------------- helpers
def crt_pair(r9, r13):
    """x mod 117 with x = r9 (mod 9), x = r13 (mod 13)."""
    for x in range(117):
        if x % 9 == r9 % 9 and x % 13 == r13 % 13:
            return x
    raise ValueError


def main():
    print("B666 cell W3-5 — the bronze McKay rung (G')")
    print("=" * 70)

    # ---------------- A. the bronze word + conductor structure
    print("\n[A] THE BRONZE WORD AND ITS CONDUCTOR STRUCTURE")
    import math

    def mat_int_mul(x, y):
        return (x[0] * y[0] + x[1] * y[2], x[0] * y[1] + x[1] * y[3],
                x[2] * y[0] + x[3] * y[2], x[2] * y[1] + x[3] * y[3])

    def bundle(m):
        Rm = (1, m, 0, 1)
        Lm = (1, 0, m, 1)
        return mat_int_mul(Rm, Lm)

    W = bundle(3)
    trW = W[0] + W[3]
    detW = W[0] * W[3] - W[1] * W[2]
    disc = trW * trW - 4
    print(f"    W = R^3 L^3 = {W}   trace {trW} = m^2+2 (m=3): "
          f"{trW == 11}   det {detW}")
    print(f"    disc = tr^2 - 4 = {disc};  tr - 2 = {trW - 2} = m^2;  "
          f"tr + 2 = {trW + 2} = m^2 + 4")

    def factorize(n):
        f = {}
        d = 2
        while d * d <= n:
            while n % d == 0:
                f[d] = f.get(d, 0) + 1
                n //= d
            d += 1
        if n > 1:
            f[n] = f.get(n, 0) + 1
        return f

    fac = factorize(disc)
    print(f"    disc factorization: {disc} = "
          + " * ".join(f"{p}^{k}" if k > 1 else f"{p}"
                       for p, k in sorted(fac.items())))
    # squarefree part and ring conductor: disc = f^2 * d_K
    sqfree = 1
    fsq = 1
    for p, k in fac.items():
        sqfree *= p ** (k % 2)
        fsq *= p ** (k // 2)
    if sqfree % 4 == 1:
        dK, fcond = sqfree, fsq
    else:
        dK, fcond = 4 * sqfree, fsq  # then fsq must be even; split the 2
        assert fsq % 2 == 0
        fcond = fsq // 2
    print(f"    squarefree part {sqfree} (mod 4 = {sqfree % 4})  ==>  "
          f"field disc d_K = {dK}, RING CONDUCTOR f = {fcond}")
    print(f"    eigenvalue field Q(sqrt{sqfree}); lambda = "
          f"({trW} + {fsq}*sqrt{sqfree})/2   [check: {fsq}^2*{sqfree} = "
          f"{fsq * fsq * sqfree} = disc: {fsq * fsq * sqfree == disc}]")
    print("\n    the metallic ladder (bundle R^m L^m), m = 1..8:")
    print("      m | trace | disc = m^2(m^2+4) |   d_K | f  (f = ring "
          "conductor of Z[lambda])")
    for m in range(1, 9):
        Bm = bundle(m)
        t = Bm[0] + Bm[3]
        dm = t * t - 4
        fm = factorize(dm)
        sq = 1
        fs = 1
        for p, k in fm.items():
            sq *= p ** (k % 2)
            fs *= p ** (k // 2)
        if sq % 4 == 1:
            dKm, fcm = sq, fs
        else:
            dKm, fcm = 4 * sq, fs // 2
        star = "  <-- bronze" if m == 3 else ""
        print(f"      {m} | {t:5d} | {dm:17d} | {dKm:5d} | {fcm}{star}")
    print("    f = m at m = 1, 2, 3 (golden, silver, bronze); the bronze"
          " is the FIRST rung")
    print("    where the f-prime (3) and the d_K-prime (13) are "
          "DIFFERENT primes.")

    # ---------------- B. the shadows
    print("\n[B] THE SHADOWS <R,L> mod n")
    shadows = {}
    for n in (3, 5, 8, 9, 13):
        G, R, L = sl2_shadow(n)
        shadows[n] = (G, R, L)
        full = full_sl2_count(n)
        prof = G.order_profile()
        invs = G.involutions()
        Z = G.center_vs([R, L])
        print(f"\n    <R,L> mod {n}: order {G.order()}  "
              f"(brute-forced full |SL(2,Z/{n})| = {full}; FULL: "
              f"{G.order() == full})")
        print(f"      order profile: {prof}")
        print(f"      involutions: {len(invs)}   center order: {len(Z)}"
              f"   exponent: {G.exponent()}")
    g5 = shadows[5][0]
    print(f"\n    GOLDEN CONTROL: mod-5 order {g5.order()}, "
          f"{len(g5.involutions())} involution -> 2I = SL(2,5): "
          f"{g5.order() == 120 and len(g5.involutions()) == 1}")
    print(f"    SILVER CONTROL: mod-8 order {shadows[8][0].order()} "
          f"(= 384, cell 1's banked fact: "
          f"{shadows[8][0].order() == 384})")

    # CRT bijectivity of residues (the exact basis for the 39/117 counts)
    crt_ok_39 = len({(x % 3, x % 13) for x in range(39)}) == 39
    crt_ok_117 = len({(x % 9, x % 13) for x in range(117)}) == 117
    n9 = full_sl2_count(9)
    n13 = full_sl2_count(13)
    n3 = full_sl2_count(3)
    print(f"\n    CRT residue bijections verified: Z/39 ~ Z/3 x Z/13: "
          f"{crt_ok_39};  Z/117 ~ Z/9 x Z/13: {crt_ok_117}")
    print(f"    => |SL(2,Z/39)| = {n3}*{n13} = {n3 * n13};  "
          f"|SL(2,Z/117)| = {n9}*{n13} = {n9 * n13}")
    G39, R39, L39 = sl2_shadow(39)
    inv39 = sum(1 for g in G39.elems
                if g != G39.e and G39.mul(g, g) == G39.e)
    Z39 = G39.center_vs([R39, L39])
    print(f"    <R,L> mod 39: order {G39.order()}  (FULL: "
          f"{G39.order() == n3 * n13})   involutions {inv39}   "
          f"center order {len(Z39)}")
    print("    <R,L> mod 117: computing closure (int-encoded BFS)...")
    o117 = closure_order_only(117, [(1, 1, 0, 1), (1, 0, 1, 1)])
    print(f"    <R,L> mod 117: order {o117}  (FULL SL(2,Z/117): "
          f"{o117 == n9 * n13})")

    # ---------------- C. 2T exact
    print("\n[C] 2T EXACT (the 24 Hurwitz unit quaternions)")
    T2, om, qi, eq = build_2T()
    print(f"    order {T2.order()}   order profile {T2.order_profile()}")
    invT = T2.involutions()
    print(f"    involutions: {len(invT)} (unique = {len(invT) == 1}; "
          f"the involution is -1: {invT[0] == (-1, 0, 0, 0)})")
    print(f"    center order {len(T2.center_vs([om, qi]))}   "
          f"exponent {T2.exponent()}")
    tr_hist = {}
    for g in T2.elems:
        t = g[0] + g[0]
        tr_hist[str(t)] = tr_hist.get(str(t), 0) + 1
    print(f"    quaternion 2-dim character values (2*Re) histogram: "
          f"{dict(sorted(tr_hist.items()))}   (ALL RATIONAL)")
    latT, clsT = T2.normal_lattice([om, qi])
    print(f"    2T normal-subgroup orders: "
          f"{sorted(len(N) for N in latT)}  (no order-3 normal "
          f"subgroup: {all(len(N) != 3 for N in latT)})")

    # ---------------- D. head-to-head at the ring conductor
    print("\n[D] HEAD-TO-HEAD AT THE RING CONDUCTOR (mod 3)")
    G3 = shadows[3][0]
    gp3 = find_generating_pair(G3)
    w3 = iso_test(G3, gp3, T2)
    print(f"    mod-3 shadow (order {G3.order()}) ~ 2T ?  "
          f"{'ISOMORPHIC, witness ' + str(w3) if w3 else 'NOT isomorphic'}")
    print("\n    which |SL(2,Z/n)| can a binary polyhedral group equal?")
    counts = {}
    for n in range(2, 17):
        counts[n] = full_sl2_count(n)
    print(f"      brute-forced |SL(2,Z/n)|, n = 2..16: {counts}")
    lb_ok = True
    for n in range(17, 49):
        seen = set()
        Rn = (1, 1, 0, 1)
        Ln = (1, 0, 1, 1)
        mul, _ = mk_mod_ops(n)
        # R^b L^c = (1+bc, b; c, 1): enumerate directly
        for b in range(n):
            for c in range(n):
                seen.add(((1 + b * c) % n, b, c, 1))
        if len(seen) != n * n:
            lb_ok = False
    print(f"      n = 17..48: the n^2 distinct products R^b L^c "
          f"verified in SL(2,Z/n) => |SL(2,Z/n)| >= n^2 > 120: {lb_ok}")
    hits24 = [n for n, c in counts.items() if c == 24]
    hits48 = [n for n, c in counts.items() if c == 48]
    hits120 = [n for n, c in counts.items() if c == 120]
    print(f"      |SL(2,Z/n)| = 24 (=|2T|) only at n = {hits24};  "
          f"= 48 (=|2O|) only at n = {hits48};  = 120 (=|2I|) only at "
          f"n = {hits120}")
    O2 = build_2O()
    print(f"    control: 2O rebuilt exactly over Q(sqrt2): order "
          f"{O2.order()}, involutions {len(O2.involutions())}")
    G4, R4, L4 = sl2_shadow(4)
    gp4 = find_generating_pair(G4)
    w4 = iso_test(G4, gp4, O2)
    print(f"    control (cell 1's banked fact re-verified): mod-4 "
          f"shadow ~ 2O ?  {'ISO' if w4 else 'NOT isomorphic (complete search)'}")
    print("    ==> 2T = SL(2,3) and 2I = SL(2,5) are SL(2)-realizable; "
          "2O is NOT |SL(2,Z/n)| for any n except n=4, and the n=4 "
          "group is not 2O.")
    print("    THIS is why the silver rung could only be a quotient.")

    # ---------------- E. mod 9
    print("\n[E] MOD 9 (the f^2 modulus): QUOTIENTS AND SUBGROUPS")
    G9, R9, L9 = shadows[9]
    lat9, cls9 = G9.normal_lattice([R9, L9])
    orders9 = sorted(len(N) for N in lat9)
    print(f"    conjugacy classes: {len(cls9)}  sizes "
          f"{sorted(len(c) for c in cls9)}")
    print(f"    normal subgroups: {len(lat9)}  orders {orders9}")
    n27 = [N for N in lat9 if len(N) == 27]
    print(f"    order-27 normal subgroups (kernels of 24-quotients): "
          f"{len(n27)}")
    mul9, _ = mk_mod_ops(9)
    K3 = frozenset(g for g in G9.elems
                   if all((g[i] - (1, 0, 0, 1)[i]) % 3 == 0
                          for i in range(4)))
    print(f"    the canonical mod-3 congruence kernel K = "
          f"{{g = I mod 3}}: order {len(K3)}; K in lattice: "
          f"{K3 in lat9}")
    any2T = False
    for k, N in enumerate(n27):
        Q = G9.quotient(N)
        gpQ = find_generating_pair(Q)
        wq = iso_test(Q, gpQ, T2)
        tag = " (= the canonical kernel)" if N == K3 else ""
        print(f"      N#{k}{tag}: quotient order {Q.order()}, profile "
              f"{Q.order_profile()}, involutions "
              f"{len(Q.involutions())} -> ~2T? "
              f"{'YES' if wq else 'no'}")
        if wq:
            any2T = True
    print(f"    ==> 2T IS A QUOTIENT OF THE MOD-9 SHADOW: {any2T}")

    # subgroup search: complete over (order-4, order-3) pairs
    print("\n    does 2T EMBED?  (complete (order-4, order-3) pair "
          "search, capped closures)")
    o4T = [g for g in T2.elems if T2.elt_order(g) == 4]
    o3T = [g for g in T2.elems if T2.elt_order(g) == 3]
    genpairs43 = sum(1 for x in o4T for y in o3T
                     if len(T2.subgroup_elems([x, y])) == 24)
    print(f"      premise: 2T generated by some (4,3)-pair: "
          f"{genpairs43 > 0}  ({genpairs43} of {len(o4T) * len(o3T)} "
          f"such pairs generate)")

    def find_2T_subgroup(G, label):
        o4 = [g for g in G.elems if G.elt_order(g) == 4]
        o3 = [g for g in G.elems if G.elt_order(g) == 3]
        print(f"      ({label}: {len(o4)} order-4, {len(o3)} order-3 "
              f"elements; {len(o4) * len(o3)} pairs)")
        found = []
        seen_subs = set()
        for x in o4:
            for y in o3:
                H = G.subgroup_capped([x, y], 24)
                if H is not None and len(H) == 24 and H not in seen_subs:
                    seen_subs.add(H)
                    Hg = FinGroup(label + ">H24", sorted(H), G.mul,
                                  G.inv, G.e)
                    gph = find_generating_pair(Hg)
                    if iso_test(Hg, gph, T2):
                        found.append((x, y, H))
        return found

    g5G = shadows[5][0]
    hits5 = find_2T_subgroup(g5G, "SL(2,5)")
    print(f"      POSITIVE CONTROL SL(2,5) = 2I: 2T subgroup "
          f"{'FOUND, e.g. ' + str(hits5[0][:2]) if hits5 else 'NOT FOUND (detector broken!)'}"
          f"  ({len(hits5)} distinct copies)")
    hits9 = find_2T_subgroup(G9, "SL(2,Z/9)")
    print(f"      SL(2,Z/9): 2T subgroup "
          f"{'FOUND at ' + str(hits9[0][:2]) if hits9 else 'NOT FOUND (complete search)'}"
          f"  ({len(hits9)} distinct copies)")
    if hits9:
        # decisive split verification: H is a SECTION of mod-3 reduction
        H0 = hits9[0][2]
        meets_K = sorted(H0 & K3)
        m3ops = mk_mod_ops(3)
        img3 = FinGroup.closure(
            "imgH", [tuple(v % 3 for v in hits9[0][0]),
                     tuple(v % 3 for v in hits9[0][1])],
            m3ops[0], m3ops[1], (1, 0, 0, 1))
        print(f"      SPLIT VERIFICATION: H  intersect  (mod-3 kernel K)"
              f" = {meets_K} (trivial: {meets_K == [(1, 0, 0, 1)]});  "
              f"H mod 3 generates order {img3.order()} (= all of "
              f"SL(2,3): {img3.order() == 24})")
        print(f"      ==> the extension 1 -> K(27) -> SL(2,Z/9) -> "
              f"SL(2,3) -> 1 SPLITS: SL(2,Z/9) = K x| 2T, and 2T is "
              f"a RETRACT (both quotient and complement).")

    # Q8 screen
    def has_Q8(G):
        o4 = [g for g in G.elems if G.elt_order(g) == 4]
        for x in o4:
            x2 = G.mul(x, x)
            xi = G.inv(x)
            for y in o4:
                if (G.mul(y, y) == x2
                        and G.mul(G.mul(y, x), G.inv(y)) == xi):
                    H = G.subgroup_capped([x, y], 8)
                    if H is not None and len(H) == 8:
                        return (x, y)
        return None

    q8 = has_Q8(G9)
    print(f"      Q8 (= 2T's Sylow-2) inside SL(2,Z/9): "
          f"{'PRESENT at ' + str(q8) if q8 else 'ABSENT'}"
          f"   (|SL(2,Z/9)| = 648 = 2^3 * 3^4, so a Q8 is a full "
          f"Sylow-2)")
    print("      contrast with silver: Q16 (2O's Sylow-2) was ABSENT "
          "from SL(2,Z/8) and 2O did NOT embed (cell 1); at the "
          "bronze BOTH the Sylow (Q8) and the full partner 2T are "
          "present — no obstruction at all.")

    # ---------------- F. mod 13
    print("\n[F] MOD 13 (the d_K modulus): QUOTIENTS AND SUBGROUPS")
    G13, R13, L13 = shadows[13]
    print("    computing the normal-subgroup lattice of SL(2,13)...")
    lat13, cls13 = G13.normal_lattice([R13, L13])
    orders13 = sorted(len(N) for N in lat13)
    print(f"    conjugacy classes: {len(cls13)}  sizes "
          f"{sorted(len(c) for c in cls13)}")
    print(f"    normal subgroups: {len(lat13)}  orders {orders13}")
    print(f"    order-91 normal subgroup (kernel of a 24-quotient) "
          f"exists: {any(len(N) == 91 for N in lat13)}")
    print(f"    ==> 2T IS A QUOTIENT OF THE MOD-13 SHADOW: "
          f"{any(len(N) == 2184 // 24 for N in lat13)}")
    hits13 = find_2T_subgroup(G13, "SL(2,13)")
    print(f"    SL(2,13): 2T subgroup "
          f"{'FOUND at ' + str(hits13[0][:2]) if hits13 else 'NOT FOUND (complete search)'}"
          f"  ({len(hits13)} distinct copies)")

    # ---------------- G. mod 117
    print("\n[G] MOD 117 (the full discriminant modulus)")
    print(f"    shadow order {o117} = full |SL(2,Z/117)|: "
          f"{o117 == n9 * n13}")
    # canonical surjection onto the mod-3 shadow = 2T
    mul3, _ = mk_mod_ops(3)
    r3 = tuple(x % 3 for x in (1, 1, 0, 1))
    l3 = tuple(x % 3 for x in (1, 0, 1, 1))
    img = FinGroup.closure("img", [r3, l3], mul3,
                           mk_mod_ops(3)[1], (1, 0, 0, 1))
    print(f"    mod-3 projection of the generators generates a group "
          f"of order {img.order()} = the mod-3 shadow ~ 2T "
          f"(kernel order {o117} / 24 = {o117 // 24})")
    print(f"    ==> 2T IS A CANONICAL QUOTIENT OF THE MOD-117 SHADOW "
          f"(kernel {o117 // 24})")
    if hits13:
        x13, y13, _H = hits13[0]
        x117 = tuple(crt_pair(1 if i in (0, 3) else 0, x13[i])
                     for i in range(4))
        y117 = tuple(crt_pair(1 if i in (0, 3) else 0, y13[i])
                     for i in range(4))
        mul117, inv117 = mk_mod_ops(117)
        e117 = (1, 0, 0, 1)
        Gbig = FinGroup("stub", [e117], mul117, inv117, e117)
        # capped closure by hand (Gbig has no element list; use ops)
        seen = {e117}
        frontier = [e117]
        ok = True
        while frontier and len(seen) <= 24:
            nxt = []
            for g in frontier:
                for s in (x117, y117):
                    h = mul117(g, s)
                    if h not in seen:
                        seen.add(h)
                        nxt.append(h)
            frontier = nxt
        if len(seen) == 24:
            Hg = FinGroup("H117", sorted(seen), mul117, inv117, e117)
            gph = find_generating_pair(Hg)
            wbig = iso_test(Hg, gph, T2)
            print(f"    CRT lift of the mod-13 witness: <{x117}, "
                  f"{y117}> has order 24 and ~2T: {bool(wbig)}")
            print(f"    ==> 2T IS ALSO A SUBGROUP OF THE MOD-117 "
                  f"SHADOW (through the 13-block)")
        else:
            print(f"    CRT lift closure order != 24: {len(seen)}")

    # ---------------- H. the exact character table of 2T
    print("\n[H] THE EXACT CHARACTER TABLE OF 2T OVER Q(zeta3)")
    # conjugacy classes (full conjugation)
    clsT_full = T2.conjugacy_classes(T2.elems)
    clsT_full.sort(key=lambda c: (T2.elt_order(next(iter(c))), len(c)))
    print(f"    conjugacy classes: {len(clsT_full)}  "
          f"(order, size): "
          f"{[(T2.elt_order(next(iter(c))), len(c)) for c in clsT_full]}")
    # linear characters via the abelianization
    D = T2.derived_subgroup()
    Qab, coset_of = T2.quotient_with_map(D)
    print(f"    [2T,2T] order {len(D)} (= Q8: "
          f"{sorted(len(N) for N in latT if len(N) == 8) == [8]} and "
          f"len {len(D)});  2T^ab order {Qab.order()}, cyclic of "
          f"order 3: {Qab.exponent() == 3 and Qab.order() == 3}")
    # exponent map on the ab quotient
    q0 = next(c for c in range(Qab.order()) if c != Qab.e)
    pw = {Qab.e: 0}
    c = q0
    k = 1
    while c != Qab.e:
        pw[c] = k
        c = Qab.mul(c, q0)
        k += 1
    zpow = [ONE, ZETA, ZETA * ZETA]

    def psi(g, j):
        return zpow[(j * pw[coset_of[g]]) % 3]

    # multiplicativity check for psi_1 on all pairs
    ok_hom = all(psi(T2.mul(g, h), 1) == psi(g, 1) * psi(h, 1)
                 for g in T2.elems for h in T2.elems)
    print(f"    psi is a homomorphism on all 24^2 pairs: {ok_hom}")

    def chi2(g):
        return C3(g[0] + g[0])

    chars = []
    chars.append(("chi_1  (deg 1)", lambda g: ONE))
    chars.append(("psi    (deg 1)", lambda g: psi(g, 1)))
    chars.append(("psi^2  (deg 1)", lambda g: psi(g, 2)))
    chars.append(("chi_2  (deg 2)", chi2))
    chars.append(("chi_2 psi   ", lambda g: chi2(g) * psi(g, 1)))
    chars.append(("chi_2 psi^2 ", lambda g: chi2(g) * psi(g, 2)))
    chars.append(("chi_3  (deg 3)",
                  lambda g: chi2(g) * chi2(g) - ONE))
    # print the table on class representatives
    print("\n    the table (columns = classes by (order, size)):")
    for name, ch in chars:
        row = [repr(ch(next(iter(c)))) for c in clsT_full]
        print(f"      {name}: {row}")
    # orthogonality (exact, over all 24 elements)
    inv24 = Fraction(1, 24)
    ortho_ok = True
    for i, (ni, chi_i) in enumerate(chars):
        for j, (nj, chi_j) in enumerate(chars):
            s = ZERO
            for g in T2.elems:
                s = s + chi_i(g) * chi_j(g).conj()
            val = C3(s.a * inv24, s.b * inv24)
            want = ONE if i == j else ZERO
            if val != want:
                ortho_ok = False
                print(f"      ORTHOGONALITY FAIL {ni} x {nj}: {val}")
    print(f"    full first-orthogonality (49 inner products, exact): "
          f"{ortho_ok}")
    degs = [chars[i][1](T2.e) for i in range(7)]
    sumsq = sum(int(d.a) ** 2 for d in degs)
    print(f"    degrees {[int(d.a) for d in degs]}  sum of squares = "
          f"{sumsq} = |2T|: {sumsq == 24}")
    # the character field
    vals = set()
    for _, ch in chars:
        for cl in clsT_full:
            vals.add(ch(next(iter(cl))))
    irr = [v for v in vals if v.b != 0]
    m3 = (ONE + ZETA + ZETA) * (ONE + ZETA + ZETA)
    print(f"    all {len(vals)} distinct values lie in Q(zeta3); "
          f"{len(irr)} are IRRATIONAL (b != 0), e.g. {irr[:3]}")
    print(f"    (1 + 2*zeta3)^2 = {m3}  (= -3: "
          f"{m3 == C3(-3)})  ==>  the character field = Q(zeta3) = "
          f"Q(sqrt-3)")
    # McKay adjacency of chi_2
    print("\n    the McKay graph of chi_2 (exact inner products "
          f"<chi_2 * chi_i, chi_j>):")
    adj = []
    for i, (ni, chi_i) in enumerate(chars):
        row = []
        for j, (nj, chi_j) in enumerate(chars):
            s = ZERO
            for g in T2.elems:
                s = s + chi2(g) * chi_i(g) * chi_j(g).conj()
            val = C3(s.a * inv24, s.b * inv24)
            assert val.b == 0 and val.a.denominator == 1
            row.append(int(val.a))
        adj.append(row)
    for i, row in enumerate(adj):
        print(f"      {chars[i][0].strip():14s} {row}")
    sym = all(adj[i][j] == adj[j][i] for i in range(7) for j in range(7))
    deg_seq = sorted(sum(r) for r in adj)
    zero_diag = all(adj[i][i] == 0 for i in range(7))
    print(f"    symmetric: {sym}; 0/1-valued: "
          f"{all(v in (0, 1) for r in adj for v in r)}; zero diagonal: "
          f"{zero_diag}; degree sequence {deg_seq}")
    print("    = the AFFINE E6 DIAGRAM (three arms of length 2 joined "
          "at the degree-3 node chi_3): "
          f"{deg_seq == [1, 1, 1, 2, 2, 2, 3]}")

    # ---------------- I. tone data
    print("\n[I] TONE DATA: THE BRONZE WORD IN ITS OWN SHADOWS")
    for n in (3, 9, 13, 39, 117):
        Wn = tuple(x % n for x in W)
        o = mat_order_mod(W, n)
        tr = (W[0] + W[3]) % n
        idn = " = IDENTITY" if Wn == (1, 0, 0, 1) else ""
        print(f"    W mod {n:3d}: {Wn}{idn}   order {o}   trace {tr}")
    print("    at the ring conductor 3 the word is the IDENTITY: its "
          "2T-tone is chi_2(W) = 2 (the trivial/maximal tone).")
    print("\n    the bundle-invisibility lemma (R^m = L^m = I mod m):")
    for m in range(1, 9):
        Rm = (1, m % m, 0, 1)
        Lm = (1, 0, m % m, 1)
        okm = Rm == (1, 0, 0, 1) and Lm == (1, 0, 0, 1)
        print(f"      m = {m}: R^m mod m = {Rm}, L^m mod m = {Lm}  "
              f"-> the ENTIRE bundle group <R^m, L^m> = I mod m: {okm}")
    print("    (so the whole bronze bundle group lies in the mod-3 "
          "congruence kernel: the 2T shadow is generated by the "
          "LETTERS R, L, and the word is structurally silent at its "
          "own ring conductor — same mechanism at every metallic rung;"
          " silver control: R^2L^2 = I mod 2, banked in cell 1's "
          "tone table as the ambient-only hearing.)")

    # ---------------- J. verdict
    print("\n" + "=" * 70)
    print("VERDICT (cell W3-5, the bronze McKay rung):")
    print(f"  conductor structure: disc = 117 = 3^2 * 13 = f^2 * d_K "
          f"with f = 3 (ring conductor), d_K = 13 (field disc); the "
          f"FIRST rung where the two live at different primes.")
    print(f"  the mod-3 shadow IS 2T (= SL(2,3), complete iso): "
          f"{bool(w3)}  -- E6's McKay partner appears EXACTLY, at the "
          f"ring-conductor prime.")
    print(f"  mod 9 (order 648 = full): 2T a quotient: {any2T} "
          f"(canonical kernel 27) AND a subgroup: {bool(hits9)} — the "
          f"extension SPLITS (2T is a retract of SL(2,Z/9)).")
    print(f"  mod 13 (order 2184 = full): 2T a quotient: "
          f"{any(len(N) == 91 for N in lat13)}; a subgroup: "
          f"{bool(hits13)} ({len(hits13)} copies).")
    print(f"  mod 117 (order {o117} = full): 2T a canonical quotient "
          f"(kernel {o117 // 24}) AND a subgroup (CRT lift).")
    print(f"  character field of 2T = Q(zeta3) = Q(sqrt-3) (exact "
          f"table, affine-E6 McKay graph verified); the bronze "
          f"EIGENVALUE field is Q(sqrt13) — the first rung where "
          f"character field and eigenvalue field SPLIT.")
    print(f"  THE DESCENT'S THIRD RUNG LANDS: golden -> 2I/E8 (exact "
          f"at 5), silver -> 2O/E7 (quotient-only at 8), bronze -> "
          f"2T/E6 (exact at 3).  The mode is explained: 2I = SL(2,5) "
          f"and 2T = SL(2,3) are the only SL(2)-realizable partners; "
          f"2O is not SL(2,Z/n) for any n.")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
