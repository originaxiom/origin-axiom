"""B1957: the web seat's foundations card W-F2 (mirrors or half-turns), on main's own code.  Data-free; exact.
W3 = Z/2 * Z/2 * Z/2 on a, b, c.  The seven re-descriptions: the three swaps, and 'a through b', 'b through a',
'c through b', 'b through c' (p through q sends p to q p q).  All products of 1 to 4 of them (2,800).
 M1  each carries (abc)^2 to a conjugate of (abc)^2 or of its inverse (the half-turn face's one cusp).
 M2  those carrying the three pair classes {ab, bc, ca} to themselves, up to conjugacy and inverse: how many, and the
     matrices they induce on H_1 of the even part, up to sign.
 M3  those with |trace| > 2; whether any of them keeps the pair classes; and how many of the 2,800 have determinant -1
     with a non-zero trace (hyperbolic too, as the note says).
 M4  (the note's hand remark on a mixed face, not computed by the seat) the step (swap b, c)(c through b): its matrix,
     and whether it keeps the cusps of the face with one mirror (a) and two half-turns."""
import functools, itertools, collections
import numpy as np
print = functools.partial(print, flush=True)
red = lambda w: functools.reduce(lambda s, c: s[:-1] if s and s[-1] == c else s + c, w, "")
def cyc(w):
    w = red(w)
    while len(w) >= 2 and w[0] == w[-1]: w = w[1:-1]
    return w
conj = lambda u, v: (lambda p, q: len(p) == len(q) and (not p or p in q + q))(cyc(u), cyc(v))
conj_pm = lambda u, v: conj(u, v) or conj(u, v[::-1])
ID = {"a": "a", "b": "b", "c": "c"}
MOVES = {"swap a,b": {**ID, "a": "b", "b": "a"}, "swap b,c": {**ID, "b": "c", "c": "b"}, "swap a,c": {**ID, "a": "c", "c": "a"},
         "a through b": {**ID, "a": "bab"}, "b through a": {**ID, "b": "aba"}, "c through b": {**ID, "c": "bcb"}, "b through c": {**ID, "b": "cbc"}}
img = lambda f, w: red("".join(f[c] for c in w)); comp = lambda f, g: {c: img(f, g[c]) for c in "abc"}          # g first, then f
def h1(f):                                                              # the action on H_1 of the even part, basis x = ab, y = bc
    def ab(w):
        v = [0, 0]; s = 1
        for c in w:
            e = {"a": (1, 0), "b": (0, 0), "c": (0, -1)}[c]; v[0] += s * e[0]; v[1] += s * e[1]; s = -s
        return v
    return np.array([ab(img(f, "ab")), ab(img(f, "bc"))]).T
PAIRS = ("ab", "bc", "ca")
keeps_pairs = lambda f: all(any(conj_pm(img(f, p), q) for q in PAIRS) for p in PAIRS)
up_to_sign = lambda M: min(tuple(M.ravel().tolist()), tuple((-M).ravel().tolist()))
def finite_order(M):
    P = np.eye(2, dtype=int)
    for _ in range(12):
        P = P @ M
        if (P == np.eye(2, dtype=int)).all() or (P == -np.eye(2, dtype=int)).all(): return True
    return False

if __name__ == "__main__":
    prods = []
    for n in range(1, 5):
        for seq in itertools.product(MOVES, repeat=n): prods.append((seq, functools.reduce(comp, [MOVES[m] for m in seq])))
    m1 = sum(conj_pm(img(f, "abcabc"), "abcabc") for _, f in prods); kp = [(s, f) for s, f in prods if keeps_pairs(f)]; mats = sorted({up_to_sign(h1(f)) for _, f in kp})
    print("products of 1 to 4 of the seven moves: %d; M1: those carrying (abc)^2 to a conjugate of itself or its inverse: %d" % (len(prods), m1))
    print("M2: those keeping the three pair classes: %d; the matrices they induce, up to sign: %d, %s; every one of finite order: %s" % (len(kp), len(mats), [list(m) for m in mats], all(finite_order(np.array(m).reshape(2, 2)) for m in mats)))
    hyp = [(s, f) for s, f in prods if abs(int(np.trace(h1(f)))) > 2]; dm = sum(1 for _, f in prods if round(np.linalg.det(h1(f))) == -1 and int(np.trace(h1(f))) != 0)
    ex = functools.reduce(comp, [MOVES[m] for m in ("a through b", "b through a", "b through c")])
    print("M3: with |trace| > 2: %d; of them keeping the pair classes: %d; the note's example (a through b)(b through a)(b through c): %s; products of determinant -1 and non-zero trace (hyperbolic too): %d, of which with |trace| <= 2: %d, and keeping the pair classes: %d" % (
        len(hyp), sum(keeps_pairs(f) for _, f in hyp), h1(ex).tolist(), dm, sum(1 for _, f in prods if round(np.linalg.det(h1(f))) == -1 and 0 < abs(int(np.trace(h1(f)))) <= 2), sum(keeps_pairs(f) for _, f in prods if round(np.linalg.det(h1(f))) == -1 and int(np.trace(h1(f))) != 0)))
    print("controls: swap a,b keeps the pair classes: %s; a through b: %s; the exact-word test on swap a,b at the half-turn cusp: %s, the conjugacy test: %s" % (keeps_pairs(MOVES["swap a,b"]), keeps_pairs(MOVES["a through b"]), img(MOVES["swap a,b"], "abc") in ("abc", "cba"), conj_pm(img(MOVES["swap a,b"], "abc"), "abc")))
    g = comp(MOVES["swap b,c"], MOVES["c through b"]); M = h1(g)
    # the face with a a mirror and b, c half-turns: cusps are the classes of elements fixing an ideal vertex; here tested on the candidates the seat's referee names
    P = np.eye(2, dtype=int); fin = False
    for _ in range(24):
        P = P @ M
        if (P == np.eye(2, dtype=int)).all() or (P == -np.eye(2, dtype=int)).all(): fin = True
    print("M4: (swap b, c)(c through b) acts on H_1 as %s (the note: [[1, 0], [1, 1]]), trace %d, of finite order within 24 steps: %s; it sends a, b, c to %s, and the classes of abc, bc and (abc)^2 to conjugates of themselves or their inverses: %s" % (
        M.tolist(), int(np.trace(M)), fin, [g[c] for c in "abc"], [conj_pm(img(g, w), w) for w in ("abc", "bc", "abcabc")]))
