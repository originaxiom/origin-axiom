"""B1957: the web seat's foundations card W-F7 (the mixed faces of three distinctions), on main's own code.  Data-free.
A face says for each of a, b, c whether it is a mirror (M) or a half-turn (H).  A step (one of the 2,800 products of one
to four of the seven moves) must send mirrors to conjugates of mirrors, half-turns to conjugates of half-turns, and the
face's corners to its corners, up to conjugacy and inverse.  Corners: MMM: ab, bc, ca; HHH: abc; MMH with half-turn r and
mirrors p, q: pq and qrpr; MHH with mirror p and half-turns q, r: p qrprq.
A matrix on H_1 of the even part is hyperbolic when det = +1 and |trace| > 2, or det = -1 and trace != 0; parabolic when
det = +1, |trace| = 2 and it is not +-1; of finite order otherwise.
 X1  for each face: the steps, the matrices up to sign, and how many steps are hyperbolic, parabolic, of finite order.
 X2  the classes of the corners on the records (basis x = ab, y = bc), and the two steps the note names.
 X3  by enumeration in GL(2, Z) with entries to 12: a matrix fixing a non-zero integer vector up to sign is never
     hyperbolic (the note's hand argument for the faces with one mirror)."""
import functools, itertools, sys, pathlib
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import web_wf2_on_main as F
img, comp, conj, conj_pm, h1, MOVES, up_to_sign = F.img, F.comp, F.conj, F.conj_pm, F.h1, F.MOVES, F.up_to_sign


def kind(M):
    d = int(round(M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0])); t = int(M[0, 0] + M[1, 1])
    if (d == 1 and abs(t) > 2) or (d == -1 and t != 0): return "hyperbolic"
    if d == 1 and abs(t) == 2 and not ((M == np.eye(2, dtype=int)).all() or (M == -np.eye(2, dtype=int)).all()): return "parabolic"
    return "finite"
def letter_class(w):                                                    # the letter a reduced word is a conjugate of, or None
    c = F.cyc(w); return c if len(c) == 1 else None
def is_step(f, mirrors, corners):
    for L in "abc":
        k = letter_class(img(f, L))
        if k is None or ((L in mirrors) != (k in mirrors)): return False
    return all(any(conj_pm(img(f, c), d) for d in corners) for c in corners)
def ab(w):
    v = [0, 0]; s = 1
    for c in w:
        e = {"a": (1, 0), "b": (0, 0), "c": (0, -1)}[c]; v[0] += s * e[0]; v[1] += s * e[1]; s = -s
    return v

if __name__ == "__main__":
    prods = []
    for n in range(1, 5):
        for seq in itertools.product(MOVES, repeat=n): prods.append((seq, functools.reduce(comp, [MOVES[m] for m in seq])))
    mats = [h1(f) for _, f in prods]; faces = [("MMM", "abc", ("ab", "bc", "ca")), ("HHH", "", ("abc",))]
    for r in "abc":
        p, q = [l for l in "abc" if l != r]; faces.append(("MMH, half-turn %s" % r, p + q, (p + q, q + r + p + r)))
    for p in "abc":
        q, r = [l for l in "abc" if l != p]; faces.append(("MHH, mirror %s" % p, p, (p + q + r + p + r + q,)))
    for name, mirrors, corners in faces:
        idx = [i for i, (_, f) in enumerate(prods) if is_step(f, mirrors, corners)]; kinds = [kind(mats[i]) for i in idx]
        print("X1 %-18s corners %s: steps %d; matrices up to sign %d; hyperbolic %d (of determinant -1: %d); parabolic %d (of determinant -1: 0 by definition); finite order %d" % (
            name, list(corners), len(idx), len({up_to_sign(mats[i]) for i in idx}), kinds.count("hyperbolic"), sum(1 for i in idx if kind(mats[i]) == "hyperbolic" and round(np.linalg.det(mats[i])) == -1), kinds.count("parabolic"), kinds.count("finite")))
    print("X1 on the half-turn face, the sealed test |trace| > 2 alone counts %d (W-F2's figure) and files %d steps of determinant -1 and |trace| = 2 as parabolic" % (sum(1 for M in mats if abs(int(np.trace(M))) > 2), sum(1 for M in mats if round(np.linalg.det(M)) == -1 and abs(int(np.trace(M))) == 2)))
    print("X2: the corners' classes on the records: (abc)^2: %s; a bcacb: %s; ab and bcac: %s, %s; ab, bc, ca: %s" % (ab("abcabc"), ab("abcacb"), ab("ab"), ab("bcac"), [ab(w) for w in ("ab", "bc", "ca")]))
    half = comp(MOVES["swap b,c"], MOVES["c through b"]); tickf = comp(MOVES["swap a,b"], comp(MOVES["swap a,c"], MOVES["a through b"]))
    print("X2: the half-twist (swap b,c)(c through b) sends a, b, c to %s, is a step of the face with mirror a: %s, and acts as %s; (swap a,b)(swap a,c)(a through b) sends a, b, c to %s and acts on the records as %s (the tick: x -> xy, y -> x has matrix [[1, 1], [1, 0]])" % (
        [half[c] for c in "abc"], is_step(half, "a", ("abcacb",)), h1(half).tolist(), [tickf[c] for c in "abc"], h1(tickf).tolist()))
    bad = 0; tot = 0
    for a, b, c, d in itertools.product(range(-12, 13), repeat=4):
        if abs(a * d - b * c) != 1: continue
        M = np.array([[a, b], [c, d]]);
        if kind(M) != "hyperbolic": continue
        tot += 1
        # an integer eigenvector with eigenvalue +-1 exists exactly when det(M -+ 1) = 0
        if (a - 1) * (d - 1) - b * c == 0 or (a + 1) * (d + 1) - b * c == 0: bad += 1
    print("X3: of the %d hyperbolic matrices of GL(2, Z) with entries to 12, those with an eigenvalue +1 or -1: %d" % (tot, bad))
