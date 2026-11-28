#!/usr/bin/env python3
"""The web seat's peer check of queue card Q0019 (fam3-v1-high-03): a second computation in other code, by other means.

The card verifies a two-register E_8 count on the figure-eight knot exterior: under the peripheral holonomy m = U(1),
l = Z U(-2d) in SL(2, F_25), carried into E_8 through the 13-dim even Weil module (Spin(13)) and a Spin(3) factor that
carries Z as -1, the torus spin kernel counts are (periodic, antiperiodic) = (8, 0), and with the dihedral sheet lift
m -> m j (j in BD_5) they are (0, 0). This script recomputes the counts in its own integer code and goes one step
further back: it derives m and l itself, from the figure-eight knot group's parabolic representations over F_25, rather
than taking them from the card. It imports nothing of the producer's and reads no file of theirs. Standard library only.

THE DEFINITIONS USED (the card's definitions field). k = F_25 = F_5[d]/(d^2 - 2); Tr(a + b d) = 2a mod 5; U(v) =
[[1, v], [0, 1]]; Z = -I. On the 13-dim even Weil module (basis e_0 and one vector per pair {x, -x}, x in k*), U(v)
has weight Tr(2 v x^2) in Z/5, written as the phase 4 Tr(2 v x^2) in Z/20; Z acts as +1 there (it is the identity on
this module: the check prints the reason, (-1) a square in k). 16 = 13 + 3; adjoint(E_8) = Lambda^2(16) + 64 (x) 2.
The 3 and the 2 of Spin(3): m -> 1 (geometric) or j (joined; on 3 eigenvalues +1, -1, -1, on 2 +i, -i); l -> -1 in
Spin(3) (trivial on 3, -1 on 2). The Spin(13) lift of each of m, l is the order-5 lift (the card's "unique order-5
lift"); this script finds it its own way: half-weights h with 2h = 4w mod 20 chosen as h = 2w, the 64 spinor weights
summed over the six planes with all signs, and each element's lift negated (its weights + 10) if 5 s = 0 mod 20 fails.
A count is the number of states of the 248 with (m, l) phases (0, 10) (periodic) or (10, 10) (antiperiodic) mod 20.
The figure-eight group as a 2-bridge knot group b(5, 3): <a, b | a w = w b>, w = b a^-1 b^-1 a; its longitude
lambda = w* w (w* = w read backwards; the exponent sum of w is 0). BD_5 = {j^e r^k}, r^5 = 1, j^4 = 1,
r^k j = j r^-k.

THE CONDITION, written before any of this was run. The card holds where this seat checks it if and only if all of:
  E1. In SL(2, F_25), U(1) has order 5, Z U(-2d) order 10, and they commute.
  E2. The parabolic representations a -> U(1), b -> [[1, 0], [t, 1]] (t in F_25, t != 0) of the figure-eight group
      exist, and at every one of them lambda commutes with U(1) and equals Z U(c) with c = 2d or c = -2d.
  E3. On the 13: e_0 has weight (0, 0) and the 12 pair-states fall into 6 planes of opposite (m, l) weights; the
      order-5 spinor lift has 64 weights, among them (0, 0) exactly 4 times; and its half-weights agree with the card's
      rule h = 4 (3w mod 5) mod 20.
  E4. Geometric: (periodic, antiperiodic) = (8, 0), with 0 of them in the 120 and 8 in the 128. Joined: (0, 0). Joined
      meridian-square phases on the 128: exactly {2, 6, 10, 14, 18}.
  E5. Of the four central elements (+-1, +-1) of Spin(13) x Spin(3), exactly (1, 1) and (-1, -1) act as +1 on all 248.
  E6. BD_5 has 20 elements and its relations; the homomorphisms of the figure-eight group onto BD_5 with a, b in the
      class of j number 20, and with a, b both in the class of j or both in that of j^-1 they number 40; every one of
      them sends lambda to 1 and a^2 to -1.
  Any one failing is a fault in the card as this seat reads it, or in this seat's reading; the note says which.

NOT CHECKED HERE: the SnapPy presentation as such (E6 counts the same homomorphisms in the 2-bridge presentation, with
the meridian condition the card states), the card's planted controls and float-literal count, and whether the C8 card
it verifies says what the card says it says.

    python3 relays/chat1_2026-11-28_peer/q0019_check.py            # the check; exits 0, prints the verdict
    python3 relays/chat1_2026-11-28_peer/q0019_check.py --control  # Z left off the Spin(3) factor; exits 1
"""
import itertools
import sys

CONTROL = "--control" in sys.argv


def say(text):
    print("DECISIVE: " + text)


# ---------------------------------------------------------------- F_25 = F_5[d]/(d^2 - 2), elements (a, b) = a + b d
def add(x, y):
    return ((x[0] + y[0]) % 5, (x[1] + y[1]) % 5)


def neg(x):
    return ((-x[0]) % 5, (-x[1]) % 5)


def mulk(x, y):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % 5, (x[0] * y[1] + x[1] * y[0]) % 5)


def tr(x):
    return (2 * x[0]) % 5


K = [(a, b) for a in range(5) for b in range(5)]
ZERO, ONE, D = (0, 0), (1, 0), (0, 1)


def inv(x):
    return next(y for y in K if mulk(x, y) == ONE)


def mm(A, B):
    return ((add(mulk(A[0][0], B[0][0]), mulk(A[0][1], B[1][0])), add(mulk(A[0][0], B[0][1]), mulk(A[0][1], B[1][1]))),
            (add(mulk(A[1][0], B[0][0]), mulk(A[1][1], B[1][0])), add(mulk(A[1][0], B[0][1]), mulk(A[1][1], B[1][1]))))


def minv(A):
    (a, b), (c, d) = A
    return ((d, neg(b)), (neg(c), a))          # det 1


I2 = ((ONE, ZERO), (ZERO, ONE))
Z2 = ((neg(ONE), ZERO), (ZERO, neg(ONE)))


def U(v):
    return ((ONE, v), (ZERO, ONE))


def order(A):
    n, P = 1, A
    while P != I2:
        P, n = mm(P, A), n + 1
    return n


def word(w, gens):
    P = I2
    for g in w:
        P = mm(P, gens[g])
    return P


# the figure-eight group as b(5, 3): letters a, A = a^-1, b, B = b^-1
W = "bABa"
WSTAR = W[::-1]
LONG = WSTAR + W


def relator_holds(gens):
    return word("a" + W, gens) == word(W + "b", gens)


def e1_e2():
    m, l = U(ONE), mm(Z2, U(neg(mulk((2, 0), D))))
    e1 = order(m) == 5 and order(l) == 10 and mm(m, l) == mm(l, m)
    say("E1 U(1) of order %d, Z U(-2d) of order %d, commuting: %s" % (order(m), order(l), e1))
    found, ok = [], True
    for t in K:
        if t == ZERO:
            continue
        a, b = U(ONE), ((ONE, ZERO), (t, ONE))
        gens = {"a": a, "A": minv(a), "b": b, "B": minv(b)}
        if not relator_holds(gens):
            continue
        lam = word(LONG, gens)
        c = mm(Z2, lam)   # Z lambda = U(c)?
        is_zu = c[0][0] == ONE and c[1][0] == ZERO and c[1][1] == ONE
        cval = c[0][1]
        good = mm(lam, a) == mm(a, lam) and is_zu and cval in (mulk((2, 0), D), neg(mulk((2, 0), D)))
        ok = ok and good
        found.append((t, cval if is_zu else None))
    e2 = bool(found) and ok
    say("E2 parabolic representations over F_25 at t = %s; lambda = Z U(c) there with c = %s; c in {2d, -2d}: %s"
        % ([fmt(t) for t, _ in found], [fmt(c) if c else None for _, c in found], e2))
    return e1 and e2


def fmt(x):
    return "%d+%dd" % x


# ---------------------------------------------------------------- the weights
def weights(c_l):
    """(m, l) weights in Z/5 on the 12 pair-states, m = U(1), l = Z U(c_l) (Z = +1 on the 13)"""
    pairs, seen = [], set()
    for x in K:
        if x == ZERO or x in seen:
            continue
        seen.add(x)
        seen.add(neg(x))
        x2 = mulk(x, x)
        pairs.append((x, (tr(mulk((2, 0), x2)), tr(mulk((2, 0), mulk(c_l, x2))))))
    return pairs


def planes(pairs):
    """pair the 12 states into 6 planes of opposite weights; None if they do not pair"""
    left = [w for _, w in pairs]
    out = []
    while left:
        w = left.pop(0)
        opp = ((-w[0]) % 5, (-w[1]) % 5)
        if opp not in left:
            return None
        left.remove(opp)
        out.append(w)
    return out


def spinor(pl):
    """the order-5 lift: half-weights h = 2w, all sign choices, negated as a whole if needed"""
    hs = [(2 * w[0], 2 * w[1]) for w in pl]
    ws = []
    for eps in itertools.product((1, -1), repeat=len(hs)):
        ws.append((sum(e * h[0] for e, h in zip(eps, hs)) % 20, sum(e * h[1] for e, h in zip(eps, hs)) % 20))
    for i in (0, 1):                                   # m's lift and l's lift, each on its own
        if not all((5 * s[i]) % 20 == 0 for s in ws):
            ws = [tuple((s[k] + 10) % 20 if k == i else s[k] for k in (0, 1)) for s in ws]
    card_rule = sorted(
        (sum(e * (4 * ((3 * w[0]) % 5)) for e, w in zip(eps, pl)) % 20,
         sum(e * (4 * ((3 * w[1]) % 5)) for e, w in zip(eps, pl)) % 20)
        for eps in itertools.product((1, -1), repeat=len(pl)))
    return ws, sorted(ws) == card_rule


def counts(c_l, joined, central=(1, 1)):
    pairs = weights(c_l)
    pl = planes(pairs)
    sp, rule_ok = spinor(pl)
    v13 = [(0, 0)] + [(4 * w[0] % 20, 4 * w[1] % 20) for w in pl] + [((-4 * w[0]) % 20, (-4 * w[1]) % 20) for w in pl]
    v3 = [(0, 0), (10, 0), (10, 0)] if joined else [(0, 0), (0, 0), (0, 0)]
    l_on_2 = 0 if CONTROL else 10                     # the control leaves Z off the Spin(3) factor
    s2 = [(5, l_on_2), (15, l_on_2)] if joined else [(0, l_on_2), (0, l_on_2)]
    v16 = v13 + v3
    adj120 = [((p[0] + q[0]) % 20, (p[1] + q[1]) % 20) for p, q in itertools.combinations(v16, 2)]
    adj128 = [((s[0] + t[0]) % 20, (s[1] + t[1]) % 20) for s in sp for t in s2]
    per = lambda ws: sum(1 for w in ws if w == (0, 10))
    anti = lambda ws: sum(1 for w in ws if w == (10, 10))
    return {"pl": pl, "sp": sp, "rule_ok": rule_ok, "n120": len(adj120), "n128": len(adj128),
            "per": (per(adj120), per(adj128)), "anti": (anti(adj120), anti(adj128)),
            "msq128": sorted({(2 * w[0]) % 20 for w in adj128}), "zero64": sum(1 for s in sp if s == (0, 0))}


def e3_e5():
    c_l = neg(mulk((2, 0), D))
    minus_one_square = any(mulk(x, x) == neg(ONE) for x in K)
    print("  -1 is a square in F_25: %s (so Z acts as +1 on the even Weil module)" % minus_one_square)
    g = counts(c_l, joined=False)
    jn = counts(c_l, joined=True)
    e3 = g["pl"] is not None and len(g["pl"]) == 6 and len(g["sp"]) == 64 and g["zero64"] == 4 and g["rule_ok"]
    say("E3 six opposite planes: %s; 64 spinor weights with (0, 0) %d times; the card's half-weight rule agrees: %s"
        % (g["pl"] is not None and len(g["pl"]) == 6, g["zero64"], e3))
    gp, ga = sum(g["per"]), sum(g["anti"])
    jp, ja = sum(jn["per"]), sum(jn["anti"])
    e4 = g["n120"] == 120 and g["n128"] == 128 and (gp, ga) == (8, 0) and g["per"] == (0, 8) and (jp, ja) == (0, 0) \
        and jn["msq128"] == [2, 6, 10, 14, 18]
    say("E4 geometric (periodic, antiperiodic) = (%d, %d), periodic in 120 and 128: %s; joined = (%d, %d); joined "
        "meridian-square phases on the 128: %s; as the card says: %s" % (gp, ga, g["per"], jp, ja, jn["msq128"], e4))
    print("  with c = +2d instead: geometric (%d, %d)" % tuple(
        sum(counts(mulk((2, 0), D), joined=False)[k]) for k in ("per", "anti")))
    # the centre: (s13, s3) with s13, s3 in {1, -1}; -1 in Spin(13) is +1 on the 13 and -1 on the 64; likewise Spin(3)
    trivial = []
    for s13, s3 in itertools.product((1, -1), repeat=2):
        on120 = True                                   # both act as +1 on the vector 16, hence on Lambda^2
        on128 = s13 * s3 == 1
        if on120 and on128:
            trivial.append((s13, s3))
    e5 = trivial == [(1, 1), (-1, -1)]
    say("E5 central elements acting trivially on the 248: %s: %s" % (trivial, e5))
    return e3 and e4 and e5


# ---------------------------------------------------------------- BD_5 and the dihedral lifts
def bmul(x, y):
    (e, k), (f, l) = x, y
    return ((e + f) % 4, (k * (1 if f % 2 == 0 else -1) + l) % 5)


BD = [(e, k) for e in range(4) for k in range(5)]
ONEB, J = (0, 0), (1, 0)


def binv(x):
    return next(y for y in BD if bmul(x, y) == ONEB)


def bword(w, gens):
    P = ONEB
    for g in w:
        P = bmul(P, gens[g])
    return P


def closure(gs):
    S = {ONEB}
    frontier = [ONEB]
    while frontier:
        new = []
        for x in frontier:
            for g in gs:
                y = bmul(x, g)
                if y not in S:
                    S.add(y)
                    new.append(y)
        frontier = new
    return S


def e6():
    R = (0, 1)
    p5 = ONEB
    for _ in range(5):
        p5 = bmul(p5, R)
    j2 = bmul(J, J)
    rel = len(BD) == 20 and p5 == ONEB and bmul(j2, j2) == ONEB and j2 != ONEB and \
        bmul(bmul(J, R), binv(J)) == binv(R) and all(bmul(j2, x) == bmul(x, j2) for x in BD) and \
        all(bmul(x, bmul(y, z)) == bmul(bmul(x, y), z) for x in BD for y in BD for z in BD)
    cls = lambda g: {bmul(bmul(h, g), binv(h)) for h in BD}
    cj, cjinv = cls(J), cls(binv(J))
    homs1, homs2, ok = 0, 0, True
    for pool, count_into in ((cj, 1), (cjinv, 2)):
        for a in pool:
            for b in pool:
                gens = {"a": a, "A": binv(a), "b": b, "B": binv(b)}
                if bword("a" + W, gens) != bword(W + "b", gens):
                    continue
                if len(closure([a, b])) != 20:
                    continue
                if bword(LONG, gens) != ONEB or bmul(a, a) != j2:
                    ok = False
                if count_into == 1:
                    homs1 += 1
                homs2 += 1
    e = rel and homs1 == 20 and homs2 == 40 and ok
    say("E6 BD_5 of order 20 with its relations: %s; onto homomorphisms with a, b in class(j): %d, with class(j^-1) "
        "too: %d; all send lambda to 1 and a^2 to -1: %s; as the card says: %s" % (rel, homs1, homs2, ok, e))
    return e


def main():
    a = e1_e2()
    b = e3_e5()
    c = e6()
    verdict = a and b and c
    if CONTROL:
        print("CONTROL: the checks %s the error made on purpose" % ("caught" if not verdict else "MISSED"))
        return 1 if not verdict else 0
    say("VERDICT: the card holds where this seat checks it (E1-E6): %s" % verdict)
    return 0


if __name__ == "__main__":
    sys.exit(main())
