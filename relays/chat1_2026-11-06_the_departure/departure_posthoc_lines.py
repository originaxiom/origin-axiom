"""The web seat, 2026-11-06: POST HOC to departure_check.py (6c284645b), written after the read-only referee's report
on the relay draft, committed before its run. Data-free (SL(2, Z) arithmetic mod 5; no frame value, no data, no
held-out quantity). It puts on record, with this seat's own code, the referee's points that the relay now states:

  (1) per line, in the line's own curve H/Gamma_{+-w}: the excursion ...1,1,n,1,1... leaves the golden lift G_in = RL
      and returns to G_out = T^n LR T^-n = T^(n-1) RL T^(1-n). For each of the twelve order-5 lines w: the periods of the
      two ends (least p with G^p in Gamma_{+-w}); whether the out-lift is the in-lift's closed geodesic, oriented
      (T^(n-1) in Gamma_{+-w} <G_in>) or not (also times S, the half-turn on RL's axis); lines shown in the apex marking;
  (2) the golden axis's stabiliser: S RL S^-1 = RL^-1 (S's fixed point i lies on RL's axis), the glide
      F = [[1, 1], [1, 0]] with F^2 = RL, and how S and F act on RL's pair;
  (3) the palindrome's reflection r = T^(2c) J0 in the apex marking, n = 1..12: the lines it fixes;
  (4) the mirror about Re tau = 1/2, r = T J0: the lines it fixes and the pairs it forms (P-717's menu at Re 1/2);
  (5) homomorphisms of the figure-eight group <x, y | y x^-1 y x y^-1 = x^-1 y x y^-1 x> to D5 (affine maps
      z -> +-z + t of Z/5): all, surjective, and surjective up to conjugacy.

    python3 departure_posthoc_lines.py
"""
import itertools

I2 = ((1, 0), (0, 1))
L = ((1, 0), (1, 1))
R = ((1, 1), (0, 1))
T = R
S = ((0, -1), (1, 0))
J0 = ((-1, 0), (0, 1))
F = ((1, 1), (1, 0))


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inv(A):
    (a, b), (c, d) = A
    e = det(A)
    assert e in (1, -1)
    return ((d * e, -b * e), (-c * e, a * e))


def pw(A, n):
    if n < 0:
        A, n = inv(A), -n
    P = I2
    for _ in range(n):
        P = mul(P, A)
    return P


RL, LR = mul(R, L), mul(L, R)
VEC = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]


def neg(w):
    return ((-w[0]) % 5, (-w[1]) % 5)


def pm(w):
    return min(w, neg(w))


LINES = sorted(set(pm(w) for w in VEC))


def act(w, G):
    return ((w[0] * G[0][0] + w[1] * G[1][0]) % 5, (w[0] * G[0][1] + w[1] * G[1][1]) % 5)


def in_stab(g, w):
    """g in Gamma_{+-w}: w g^-1 = +-w"""
    u = act(w, inv(g))
    return u in (w, neg(w))


def own(A):
    return frozenset(pm(w) for w in VEC if in_stab(A, w))


def show(w):
    return "(%d/5, %d/5)" % w


def to_apex(w, m):
    """the line under tau -> tau - m: w -> w (T^-m)^-1 = w T^m"""
    return pm(act(w, pw(T, m)))


if __name__ == "__main__":
    print("POST HOC: the lines in the excursion's own curves (the web seat, 2026-11-06)")

    print("\n(1) PER LINE, the excursion ...1,1,n,1,1...: periods of the two ends; out-lift = in-lift's closed geodesic")
    pair = own(RL)
    for n in range(1, 13):
        m = n // 2
        Gin, Gout = RL, mul(mul(pw(T, n), LR), pw(T, -n))
        rows, prim = [], []
        for w in LINES:
            pin = next(p for p in range(1, 11) if in_stab(pw(Gin, p), w))
            pout = next(p for p in range(1, 11) if in_stab(pw(Gout, p), w))
            ori = any(in_stab(mul(pw(T, n - 1), pw(Gin, -j)), w) for j in range(10))
            unori = ori or any(in_stab(mul(mul(pw(T, n - 1), pw(Gin, -j)), inv(S)), w) for j in range(10))
            rows.append((show(to_apex(w, m)), pin, pout, ori, unori))
            if ori and pin == 1:
                prim.append(show(to_apex(w, m)))
        ret = [r[0] for r in rows if r[3]]
        print("  n = %2d: return to the primitive (period-1) lift for %s; oriented return for %d of 12 lines %s; "
              "unoriented for %d" % (n, prim or "no line", len(ret), ret if len(ret) < 12 else "(all)",
                                     sum(1 for r in rows if r[4])))
        if n in (5, 6):
            for r in rows:
                print("      line %s (apex marking): periods in/out %d/%d, oriented return %s, unoriented %s" % r)

    print("\n(2) THE GOLDEN AXIS'S STABILISER")
    print("  S RL S^-1 = RL^-1: %s; F^2 = RL: %s; det F = %d" % (mul(mul(S, RL), inv(S)) == inv(RL), mul(F, F) == RL, det(F)))
    v, v2 = sorted(pair)
    for name, g in (("S", S), ("F", F)):
        print("  %s maps RL's pair: %s -> %s, %s -> %s" % (name, show(v), show(pm(act(v, inv(g)))), show(v2), show(pm(act(v2, inv(g))))))

    print("\n(3) THE PALINDROME'S REFLECTION r = T^(2c) J0 IN THE APEX MARKING: the lines it fixes")
    for n in range(1, 13):
        c2 = n % 2
        r = mul(pw(T, c2), J0)
        fixed = [show(w) for w in LINES if pm(act(w, inv(r))) == w]
        print("  n = %2d (Re tau = %s): %s" % (n, "1/2" if c2 else "0", fixed))

    print("\n(4) THE MIRROR ABOUT Re tau = 1/2 (r = T J0) ON THE TWELVE LINES")
    r = mul(T, J0)
    fixed = [show(w) for w in LINES if pm(act(w, inv(r))) == w]
    pairs = sorted(set(tuple(sorted((w, pm(act(w, inv(r)))))) for w in LINES if pm(act(w, inv(r))) != w))
    print("  fixed: %s; paired: %s; distinct outcomes %d" % (fixed, [(show(a), show(b)) for a, b in pairs], len(fixed) + len(pairs)))

    print("\n(5) THE FIGURE-EIGHT GROUP TO D5 (z -> e z + t on Z/5, e = +-1)")
    D5 = [(e, t) for e in (1, -1) for t in range(5)]

    def dm(g, h):  # g after h
        return (g[0] * h[0], (g[0] * h[1] + g[1]) % 5)

    def di(g):
        return (g[0], (-g[0] * g[1]) % 5)

    def word(*gs):
        out = (1, 0)
        for g in gs:
            out = dm(out, g)
        return out

    homs = [(x, y) for x in D5 for y in D5
            if word(y, di(x), y, x, di(y)) == word(di(x), y, x, di(y), x)]

    def generated(gens):
        grp, frontier = {(1, 0)}, [(1, 0)]
        while frontier:
            g = frontier.pop()
            for h in gens:
                k = dm(g, h)
                if k not in grp:
                    grp.add(k); frontier.append(k)
        return grp

    surj = [h for h in homs if len(generated(h)) == 10]
    classes = set()
    for (x, y) in surj:
        classes.add(min((dm(dm(g, x), di(g)), dm(dm(g, y), di(g))) for g in D5))
    print("  homomorphisms %d; surjective %d; surjective up to conjugacy %d" % (len(homs), len(surj), len(classes)))
    print("departure_posthoc_lines exit 0")
