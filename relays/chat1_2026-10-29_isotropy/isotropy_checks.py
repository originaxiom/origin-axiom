"""THE ISOTROPY CONTROL AND THE ARENA'S METRIC: the checks of THE_ISOTROPY_RULE.md (sealed 3a4daeaa5).

Free-group words are tuples of non-zero integers: 1 = a, 2 = b, -1 = a^-1, -2 = b^-1.  An automorphism of F2 is a dict
{1: word, 2: word}.  GENESIS's core letters: L = [[1,1],[0,1]] realised by a -> a, b -> b a; R = [[1,0],[1,1]] by
a -> a b, b -> b; lower case is the inverse; 'I' is -I, realised by a -> a^-1, b -> b^-1.  The matrix of an automorphism
is read on H1 with columns the images of a and b, so the matrix of a composite is the product in the same order.

Run from this folder:  python3 isotropy_checks.py --selftest     (synthetic inputs only)
                       python3 isotropy_checks.py                (writes isotropy_out.txt and isotropy.json)
"""
import itertools
import json
import sys

import sympy as sp

A_, B_ = 1, 2


# ---------------------------------------------------------------- free group
def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def inv(w):
    return tuple(-x for x in reversed(w))


def mul(*ws):
    return red(tuple(itertools.chain.from_iterable(ws)))


def apply(phi, w):
    out = []
    for x in w:
        out.extend(phi[x] if x > 0 else inv(phi[-x]))
    return red(tuple(out))


def compose(p, q):
    """(p o q)(x) = p(q(x))"""
    return {1: apply(p, q[1]), 2: apply(p, q[2])}


IDENT = {1: (A_,), 2: (B_,)}
LET = {"L": {1: (A_,), 2: (B_, A_)}, "l": {1: (A_,), 2: (B_, -A_)},
       "R": {1: (A_, B_), 2: (B_,)}, "r": {1: (A_, -B_), 2: (B_,)},
       "I": {1: (-A_,), 2: (-B_,)}}


def phi_of(word):
    p = dict(IDENT)
    for ch in word:
        p = compose(p, LET[ch])
    return p


def matrix_of(phi):
    def ab(w):
        return [sum(1 if x == A_ else -1 if x == -A_ else 0 for x in w),
                sum(1 if x == B_ else -1 if x == -B_ else 0 for x in w)]
    ca, cb = ab(phi[1]), ab(phi[2])
    return sp.Matrix([[ca[0], cb[0]], [ca[1], cb[1]]])


def power(phi, n):
    p = dict(IDENT)
    for _ in range(n):
        p = compose(phi, p)
    return p


def cyc_red(w):
    """w = u w' u^-1 with w' cyclically reduced; returns (u, w')"""
    w = red(w)
    u = []
    while len(w) >= 2 and w[0] == -w[-1]:
        u.append(w[0])
        w = w[1:-1]
    return tuple(u), tuple(w)


def conj_witness(x, y):
    """g with x = g y g^-1 (free reduction), or None"""
    ux, xc = cyc_red(x)
    uy, yc = cyc_red(y)
    if len(xc) != len(yc):
        return None
    for i in range(max(1, len(yc))):
        if yc[i:] + yc[:i] == xc:                 # xc = p^-1 yc p with p = yc[:i]
            p = yc[:i]
            g = mul(ux, inv(p), inv(uy))
            if mul(g, y, inv(g)) == red(x):
                return g
    return None


def inner_witness(psi):
    """g with psi(x) = g x g^-1 for x = a, b, or None"""
    ga = conj_witness(psi[1], (A_,))
    if ga is None:
        return None
    for k in range(-30, 31):
        g = mul(ga, (A_,) * k if k >= 0 else (-A_,) * (-k))
        if mul(g, (B_,), inv(g)) == psi[2] and mul(g, (A_,), inv(g)) == psi[1]:
            return g
    return None


# ---------------------------------------------------------------- permutations
def pmul(p, q):           # (p q)(i) = p(q(i))
    return tuple(p[i] for i in q)


def pinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p):
        r[x] = i
    return tuple(r)


def cycle_type(p):
    seen, ct = set(), []
    for i in range(len(p)):
        if i in seen:
            continue
        j, n = i, 0
        while j not in seen:
            seen.add(j); j = p[j]; n += 1
        ct.append(n)
    return tuple(sorted(ct))


def peval(w, imgs, n):
    r = tuple(range(n))
    for x in w:
        r = pmul(r, imgs[x] if x > 0 else pinv(imgs[-x]))
    return r


def closure(gens, n):
    e = tuple(range(n))
    seen, frontier = {e}, [e]
    while frontier:
        nxt = []
        for h in frontier:
            for g in gens:
                k = pmul(h, g)
                if k not in seen:
                    seen.add(k); nxt.append(k)
        frontier = nxt
    return seen


def finite_certificate(phi, w, nmax=5):
    """A hom psi: F2 x|_phi Z -> S_n (t x t^-1 = phi(x)) with psi(a) conjugate to no element of psi(<c, w^-1 t>)."""
    c = (A_, B_, -A_, -B_)
    for n in range(2, nmax + 1):
        perms = list(itertools.permutations(range(n)))
        for A in perms:
            for B in perms:
                imgs = {1: A, 2: B}
                A2, B2 = peval(phi[1], imgs, n), peval(phi[2], imgs, n)
                if cycle_type(A2) != cycle_type(A) or cycle_type(B2) != cycle_type(B):
                    continue
                for T in perms:
                    Ti = pinv(T)
                    if pmul(pmul(T, A), Ti) == A2 and pmul(pmul(T, B), Ti) == B2:
                        C = peval(c, imgs, n)
                        W = pmul(pinv(peval(w, imgs, n)), T)
                        P = closure([C, W], n)
                        if cycle_type(A) not in {cycle_type(p) for p in P}:
                            return {"n": n, "A": A, "B": B, "T": T, "peripheral_image_order": len(P),
                                    "a_cycle_type": cycle_type(A)}
    return None


# ---------------------------------------------------------------- self-test
def selftest():
    assert red((1, -1, 2, 1, -1)) == (2,)
    assert compose(LET["L"], LET["l"]) == IDENT and compose(LET["R"], LET["r"]) == IDENT
    assert matrix_of(phi_of("L")) == sp.Matrix([[1, 1], [0, 1]])
    assert matrix_of(phi_of("R")) == sp.Matrix([[1, 0], [1, 1]])
    assert matrix_of(phi_of("I")) == -sp.eye(2)
    assert matrix_of(phi_of("LR")) == sp.Matrix([[2, 1], [1, 1]])
    g = (2, 1, 1)
    assert conj_witness(mul(g, (1, 2, -1), inv(g)), (1, 2, -1)) is not None
    psi = {1: mul(g, (1,), inv(g)), 2: mul(g, (2,), inv(g))}
    gw = inner_witness(psi)
    assert gw is not None and mul(gw, (2,), inv(gw)) == psi[2]
    p = (1, 2, 0)
    assert pmul(p, pinv(p)) == (0, 1, 2) and cycle_type(p) == (3,)
    print("selftest: helpers pass on synthetic inputs (reduction, letters and matrices, conjugacy witnesses, permutations)")


# ---------------------------------------------------------------- the cells
def main():
    lines, out = [], {"rule": "3a4daeaa5"}

    def say(s=""):
        print(s)
        lines.append(s)

    say("THE ISOTROPY CONTROL AND THE ARENA'S METRIC: the checks of THE_ISOTROPY_RULE.md (sealed 3a4daeaa5)")
    say()

    # I1 -- elliptic classes: a central element
    elliptic = {"I (identity)": "", "-I": "I", "order 6 (LR^-1, trace 1, the trefoil)": "Lr",
                "order 6, inverse (RL^-1)": "Rl", "order 4 (LR^-1L, trace 0)": "LrL",
                "order 4, inverse (L^-1RL^-1)": "lRl", "order 3 ((LR^-1)^2, trace -1)": "LrLr",
                "order 3, inverse ((RL^-1)^2)": "RlRl"}
    i1 = {}
    for nm, word in elliptic.items():
        phi = phi_of(word)
        M = matrix_of(phi)
        n = next(k for k in range(1, 13) if M ** k == sp.eye(2))
        psi = power(phi, n)
        g = inner_witness(psi)
        ok = g is not None and apply(phi, g) == g
        i1[nm] = {"word": word, "matrix": [[int(v) for v in M.row(i)] for i in range(2)], "trace": int(M.trace()),
                  "order": n, "g": list(g) if g is not None else None, "phi(g) = g": bool(ok),
                  "central element": "g^-1 t^%d" % n}
        say("I1 %-40s M = %s, tr %+d, order %d: Phi^%d = conj(g), g = %s; Phi(g) = g: %s" % (
            nm, i1[nm]["matrix"], i1[nm]["trace"], n, n, list(g) if g is not None else None, ok))
    I1 = all(v["phi(g) = g"] for v in i1.values())
    out["I1"] = {"classes": i1, "holds": I1}
    say("I1 -> %s" % I1)
    say()

    # I2 -- parabolic classes: a non-peripheral Z^2
    i2 = {}
    for k in (1, 2, 3, 4):
        for sgn, pre in (("+", ""), ("-", "I")):
            for direc, letter in (("L^%d" % k, "L"), ("L^-%d" % k, "l")):
                nm = "%s%s" % ("" if sgn == "+" else "-", direc)
                phi = phi_of(pre + letter * k)
                M = matrix_of(phi)
                m = 1 if apply(phi, (A_,)) == (A_,) else (2 if apply(power(phi, 2), (A_,)) == (A_,) else None)
                c = (A_, B_, -A_, -B_)
                w = conj_witness(apply(phi, c), c)
                cert = finite_certificate(phi, w) if (m is not None and w is not None) else None
                i2[nm] = {"word": pre + letter * k, "matrix": [[int(v) for v in M.row(i)] for i in range(2)],
                          "trace": int(M.trace()), "m (Phi^m(a) = a)": m, "w (Phi(c) = w c w^-1)": list(w) if w else w,
                          "finite certificate": cert}
                say("I2 %-7s M = %s, tr %+d: Phi^%s(a) = a; Phi(c) = w c w^-1 with w = %s; certificate: %s" % (
                    nm, i2[nm]["matrix"], i2[nm]["trace"], m, list(w) if w else w,
                    ("S_%d, |psi(P)| = %d, psi(a) of type %s" % (cert["n"], cert["peripheral_image_order"],
                                                                cert["a_cycle_type"])) if cert else None))
    I2a = all(v["m (Phi^m(a) = a)"] in (1, 2) for v in i2.values())
    I2b = all(v["finite certificate"] is not None for v in i2.values())
    out["I2"] = {"classes": i2, "I2a": I2a, "I2b": I2b}
    say("I2a -> %s; I2b -> %s (%d of %d classes certified)" % (I2a, I2b, sum(v["finite certificate"] is not None
                                                                              for v in i2.values()), len(i2)))
    say()

    # I3 -- the closed torus bundle of LR (Sol)
    LR = matrix_of(phi_of("LR"))
    x = sp.symbols("x")
    cp = sp.factor_list(LR.charpoly(x).as_expr())
    inf_order = all(LR ** n != sp.eye(2) for n in range(1, 1001))
    disc = LR.trace() ** 2 - 4
    I3 = bool(inf_order and disc > 0 and not sp.sqrt(disc).is_integer)
    out["I3"] = {"LR": [[int(v) for v in LR.row(i)] for i in range(2)], "trace": int(LR.trace()), "charpoly": str(cp),
                 "LR^n != I for n <= 1000": inf_order, "discriminant": int(disc), "holds": I3}
    say("I3 LR = %s, trace %d, char. poly %s, discriminant %d (not a square), LR^n != I for n <= 1000: %s  -> %s" % (
        out["I3"]["LR"], LR.trace(), cp, disc, inf_order, I3))
    say()

    # I4 -- the hyperbolic sector (SnapPy, corroboration) and the excluded classes through twister
    import snappy
    from snappy import twister

    def necklaces(n):
        seen = set()
        for t in itertools.product("LR", repeat=n):
            if "L" not in t or "R" not in t:
                continue
            s = "".join(t)
            canon = min(s[i:] + s[:i] for i in range(n))
            seen.add(canon)
        return sorted(seen)

    i4 = {"states": 0, "positively oriented": 0, "other": []}
    for n in range(2, 12):
        for wd in necklaces(n):
            for sg in ("++", "+-"):
                M = snappy.Manifold("b%s%s" % (sg, wd))
                i4["states"] += 1
                st = M.solution_type()
                if st == "all tetrahedra positively oriented":
                    i4["positively oriented"] += 1
                else:
                    i4["other"].append(["b%s%s" % (sg, wd), st])
    S = twister.Surface("S_1_1")
    tw = {"order 6": "a*b", "order 6, inverse": "B*A", "order 4": "a*b*a", "order 4, inverse": "A*B*A",
          "order 3": "a*b*a*b", "order 3, inverse": "B*A*B*A", "-I": "a*b*a*a*b*a"}
    for k in (1, 2, 3, 4):
        tw["L^%d" % k] = "*".join("a" * k)
        tw["L^-%d" % k] = "*".join("A" * k)
        tw["-L^%d" % k] = "a*b*a*a*b*a*" + "*".join("a" * k)
        tw["-L^-%d" % k] = "a*b*a*a*b*a*" + "*".join("A" * k)
    tw_out = {}
    for nm, word in tw.items():
        try:
            M = S.bundle(monodromy=word)
            tw_out[nm] = [word, M.solution_type()]
        except Exception as e:                          # noqa: BLE001 -- reported, not hidden
            tw_out[nm] = [word, "error: %s" % str(e)[:80]]
    tw_pos = [nm for nm, v in tw_out.items() if v[1] == "all tetrahedra positively oriented"]
    I4 = i4["positively oriented"] == i4["states"] and not tw_pos
    i4["twister_excluded"] = tw_out
    i4["excluded_positively_oriented"] = tw_pos
    out["I4"] = dict(i4, holds=I4)
    say("I4 hyperbolic sector: %d of %d orientable states (word length 2-11, both signs) positively oriented; others: %s"
        % (i4["positively oriented"], i4["states"], i4["other"][:10]))
    say("   excluded classes through twister: %s" % {k: v[1] for k, v in tw_out.items()})
    say("   excluded classes with a positively oriented solution: %s  -> %s" % (tw_pos, I4))
    say()

    # I5 -- the trichotomy
    rng = range(-6, 7)
    counts = {"elliptic": 0, "parabolic": 0, "hyperbolic": 0, "+-I": 0}
    bad = []
    for a, b, c, d in itertools.product(rng, repeat=4):
        if a * d - b * c != 1:
            continue
        M = sp.Matrix([[a, b], [c, d]])
        t = a + d
        if M == sp.eye(2) or M == -sp.eye(2):
            counts["+-I"] += 1
            continue
        if abs(t) < 2:
            counts["elliptic"] += 1
            if M ** 12 != sp.eye(2):
                bad.append([a, b, c, d])
        elif abs(t) == 2:
            counts["parabolic"] += 1
            if (M - sp.sign(t) * sp.eye(2)) ** 2 != sp.zeros(2, 2):
                bad.append([a, b, c, d])
        else:
            counts["hyperbolic"] += 1
            ev = list(M.eigenvals().keys())
            if len(ev) != 2 or any((not e.is_real) or e in (1, -1) for e in ev):
                bad.append([a, b, c, d])
    I5 = not bad
    out["I5"] = {"counts": counts, "exceptions": bad, "holds": I5}
    say("I5 SL(2, Z) with entries in [-6, 6]: %s; exceptions: %s  -> %s" % (counts, bad, I5))
    say()

    # I6 -- the arena's metric
    p, q, r, s, xx, yy, zz = sp.symbols("p q r s x y z", real=True)
    H = sp.Matrix([[1, 0], [0, -1]]); E = sp.Matrix([[0, 1], [0, 0]]); F = sp.Matrix([[0, 0], [1, 0]])
    Q = lambda X: -X.det()
    Kil = lambda X: 4 * (X * X).trace()
    Xg = xx * H + yy * E + zz * F
    eq_killing = sp.simplify(Q(Xg) - Kil(Xg) / 8) == 0
    gram = sp.hessian(Q(Xg), (xx, yy, zz)) / 2
    ev = gram.eigenvals()
    sig = (sum(m for v, m in ev.items() if v > 0), sum(m for v, m in ev.items() if v < 0))
    g = sp.Matrix([[p, q], [r, s]])
    Y = sp.Matrix(2, 2, sp.symbols("y0:4", real=True))
    biinv = sp.simplify(Q(g * Y) - (g.det()) * Q(Y)) == 0 and sp.simplify(Q(Y * g) - (g.det()) * Q(Y)) == 0
    types = {"H (geodesic flow)": Q(H), "E (horocycle)": Q(E), "F (horocycle)": Q(F), "E - F (fibre)": Q(E - F)}
    th = sp.symbols("theta", real=True)
    rot = sp.simplify((th * (E - F)).exp())
    closed = sp.simplify(rot.subs(th, sp.pi) + sp.eye(2)) == sp.zeros(2, 2)
    tt, ss = sp.symbols("t s", real=True)
    def mob_is(m, z, target):
        """the Moebius image of z under m equals target: num - target * den expands to 0"""
        num, den = m[0, 0] * z + m[0, 1], m[1, 0] * z + m[1, 1]
        return sp.simplify(sp.expand(sp.expand_complex(num - target * den))) == 0, sp.simplify(num / den)

    ok_geo, geo = mob_is(sp.simplify((tt * H / 2).exp()), sp.I, sp.exp(tt) * sp.I)
    ok_hor, hor = mob_is(sp.simplify((ss * E).exp()), sp.I, ss + sp.I)
    ok_fix, fix = mob_is(sp.simplify((th * (E - F) / 2).exp()), sp.I, sp.I)
    I6 = bool(eq_killing and sig == (2, 1) and biinv and types["H (geodesic flow)"] > 0 and types["E (horocycle)"] == 0
              and types["F (horocycle)"] == 0 and types["E - F (fibre)"] < 0 and closed and ok_geo and ok_hor and ok_fix)
    out["I6"] = {"-det = Killing/8 on sl(2,R)": bool(eq_killing), "signature": list(sig),
                 "left and right invariant (det g = 1)": bool(biinv), "causal values": {k: str(v) for k, v in types.items()},
                 "exp(pi (E - F)) = -I": bool(closed), "exp(tH/2) . i": str(geo), "exp(sE) . i": str(hor),
                 "exp(theta (E - F)/2) . i": str(fix), "holds": I6}
    say("I6 -det on sl(2, R) = Killing/8: %s; signature (pos, neg) = %s; invariant under left and right multiplication"
        " by det-1 matrices: %s" % (eq_killing, sig, biinv))
    say("   -det on the generators: %s (positive: spacelike; 0: null; negative: timelike)" % {k: str(v) for k, v in types.items()})
    say("   exp(pi (E - F)) = -I: %s; exp(tH/2).i = %s (the geodesic); exp(sE).i = %s (the horocycle); exp(theta (E-F)/2).i = %s"
        " (the fibre fixes the point)  -> %s" % (closed, geo, hor, fix, I6))
    say()

    cells = {"I1": I1, "I2a": I2a, "I2b": I2b, "I3": I3, "I4": I4, "I5": I5, "I6": I6}
    out["cells"] = cells
    say("CELLS: " + ", ".join("%s %s" % (k, "holds" if v else "FAILS") for k, v in cells.items()))
    with open("isotropy_out.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    with open("isotropy.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, default=str)
        fh.write("\n")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()
