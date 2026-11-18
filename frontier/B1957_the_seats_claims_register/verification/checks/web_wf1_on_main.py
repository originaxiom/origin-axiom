"""B1957: the web seat's foundations card W-F1 (2026-11-14), on main's own code.  Data-free; exact.
Part A, the distinction layer (three involutions with no relations):
 A1  the Tits form of the universal Coxeter group of rank n: its signature for n = 1 to 6.
 A2  in Z/2 * Z/2 * Z/2 with x = ab, y = bc: a [x, y] a = (abc)^-2 as reduced words; with the Pauli triple the product is
     i, the reversed product -i, and [x, y] = -1.
 A4  the orbifold S^2(2, 2, 2, k): chi = 1/k - 1/2.
 A5  on H_1 of the even part (free on x, y): (swap a, b)(a through b), (swap b, c)(a through b) and (swap a, c) are L,
     R and P up to sign.
Part B, the census and the hand (words in L, R of length 2 to 12; a state is a primitive cyclic word up to rotation and
the exchange of the letters, with a sign):
 B0  758 states and 536 manifolds (classes under rotation, exchange and reversal, with a sign).
 B1  rev(w) = D w^-1 D and w^-1 = J w^T J^-1 for all 8,190 words of length 1 to 12.
 B2  the manifolds on which reversing the act is a symmetry (w conjugate to its inverse up to the bundle's homeomorphisms).
 B3  the odd-trace states; for each, with every rotation: the act's quaternion lift (unique up to sign) has order 3 or 6;
     its class (which way it cycles the three axes) flips under inversion and under conjugation by the lifts of L, R
     and P, and is kept by D, by -1 and by the inner automorphisms; so it takes both values across the rotations."""
import functools, itertools, sys, pathlib
from fractions import Fraction as Fr
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import physical_harmonic_draft as H      # main's exact quaternions and free-group words

Lm, Rm = np.array([[1, 1], [0, 1]], dtype=object), np.array([[1, 0], [1, 1]], dtype=object); Dm = np.array([[1, 0], [0, -1]], dtype=object); Jm = np.array([[0, -1], [1, 0]], dtype=object)
mat = lambda w: functools.reduce(lambda A, c: A.dot(Lm if c == "L" else Rm), w, np.eye(2, dtype=object))
rot = lambda w: [w[i:] + w[:i] for i in range(len(w))]; swap = lambda w: w.translate(str.maketrans("LR", "RL"))
canon = lambda w, ops: min(x for o in ops for x in rot(o(w)))
state = lambda w: canon(w, (lambda v: v, swap)); manifold = lambda w: canon(w, (lambda v: v, swap, lambda v: v[::-1], lambda v: swap(v[::-1])))
primitive = lambda w: all(w != w[:d] * (len(w) // d) for d in range(1, len(w)) if len(w) % d == 0)
glift = lambda w: functools.reduce(H.qmul, [H.gL if c == "L" else H.gR for c in w], H.ONE)
AX = (H.QI, H.QJ, H.QK)
def axis_perm(g):
    out = []
    for x in AX:
        y = H.ad(g, x); out.append([k for k, z in enumerate(AX) if y[:4] in (z[:4], H.qmul(H.MONE, z)[:4])][0])
    return tuple(out)
cls = lambda g: {(1, 2, 0): +1, (2, 0, 1): -1}.get(axis_perm(g), 0)          # +1 and -1: the two rotations of order 3 on the axes; 0: not of order 3


if __name__ == "__main__":
    for n in range(1, 7):
        ev = np.linalg.eigvalsh(2 * np.eye(n) - np.ones((n, n))); print("A1: rank %d: the Tits form 2 - J has (positive, negative, zero) = (%d, %d, %d)" % (n, (ev > 1e-9).sum(), (ev < -1e-9).sum(), (abs(ev) < 1e-9).sum()))
    red = lambda w: functools.reduce(lambda s, c: s[:-1] if s and s[-1] == c else s + c, w, "")          # Z/2 * Z/2 * Z/2: letters are their own inverses
    inv = lambda w: w[::-1]; x, y = "ab", "bc"; comm = red(x + y + inv(x) + inv(y))
    s1, s2, s3 = np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex); X, Y = s1 @ s2, s2 @ s3
    print("A2: [x, y] = %s; a [x, y] a = %s; (abc)^-2 = %s; equal: %s. Pauli: s1 s2 s3 = %s I, s3 s2 s1 = %s I, [x, y] = %s I (trace %s)" % (comm, red("a" + comm + "a"), red(inv("abc") * 2), red("a" + comm + "a") == red(inv("abc") * 2),
          (s1 @ s2 @ s3)[0, 0], (s3 @ s2 @ s1)[0, 0], (X @ Y @ np.linalg.inv(X) @ np.linalg.inv(Y))[0, 0].real, np.trace(X @ Y @ np.linalg.inv(X) @ np.linalg.inv(Y)).real))
    print("A4: chi of S^2(2, 2, 2, k) = 2 - 3/2 - (1 - 1/k): %s at k = 2, 3, 4, 12; at the puncture -1/2" % [str(Fr(1, k) - Fr(1, 2)) for k in (2, 3, 4, 12)])
    def on_h1(sub):                                                           # an automorphism of Z/2*Z/2*Z/2 given on a, b, c: its action on the even part's H_1 (x = ab, y = bc)
        ap = lambda w: red("".join(sub[c] for c in w))
        def ab(w):                                                            # an even word as exponents of (x, y): read it as a path, letters a, b, c with x = ab, y = bc, so a = +(1,0)... use the map a -> (1,0), b -> (0,0), c -> (0,-1) on alternating signs
            v = [0, 0]; sgn = 1
            for c in w:
                e = {"a": (1, 0), "b": (0, 0), "c": (0, -1)}[c]; v[0] += sgn * e[0]; v[1] += sgn * e[1]; sgn = -sgn
            return v
        return np.array([ab(ap(x)), ab(ap(y))]).T
    idm = {"a": "a", "b": "b", "c": "c"}; sw = lambda p, q: {**idm, p: q, q: p}; thr = {"a": "bab", "b": "b", "c": "c"}; comp = lambda f, g: {k: "".join(f[c] for c in g[k]) for k in "abc"}   # comp(f, g): g first
    assert on_h1(idm).tolist() == [[1, 0], [0, 1]]
    print("A5: on H_1 of the even part: (swap a, b)(a through b) = %s; (swap b, c)(a through b) = %s; (swap a, c) = %s (L = [[1,1],[0,1]], R = [[1,0],[1,1]], P = [[0,1],[1,0]], up to sign)" % (on_h1(comp(sw("a", "b"), thr)).tolist(), on_h1(comp(sw("b", "c"), thr)).tolist(), on_h1(sw("a", "c")).tolist()))
    words = ["".join(t) for n in range(1, 13) for t in itertools.product("LR", repeat=n)]
    ok1 = all((mat(w[::-1]) == Dm.dot(np.array([[mat(w)[1, 1], -mat(w)[0, 1]], [-mat(w)[1, 0], mat(w)[0, 0]]], dtype=object)).dot(Dm)).all() and (np.array([[mat(w)[1, 1], -mat(w)[0, 1]], [-mat(w)[1, 0], mat(w)[0, 0]]], dtype=object) == Jm.dot(mat(w).T).dot(-Jm)).all() for w in words)
    print("B1: %d words of length 1 to 12: rev(w) = D w^-1 D and w^-1 = J w^T J^-1 for every one: %s" % (len(words), ok1))
    prim = [w for w in words if len(w) >= 2 and primitive(w)]; states = sorted({state(w) for w in prim}); mans = sorted({manifold(w) for w in prim})
    print("B0: primitive cyclic words of length 2 to 12 up to rotation and exchange: %d, so %d states with the sign; up to reversal too: %d, so %d manifolds" % (len(states), 2 * len(states), len(mans), 2 * len(mans)))
    # an orientation-reversing self-map of the bundle: C A C^-1 = A with det C = -1, or C A C^-1 = A^-1 with det C = +1.  For a positive word,
    # conjugation in SL(2, Z) is rotation, conjugation by P exchanges the letters, and A^-1 = J A^T J^-1 with A^T the exchanged reversed word.
    rc = lambda v: canon(v, (lambda u: u,)); a1 = [m for m in mans if rc(m) == rc(swap(m[::-1]))]; a2 = [m for m in mans if rc(m) == rc(swap(m))]; amph = sorted(set(a1) | set(a2))
    print("B2: manifolds whose word is a rotation of its exchanged reversed word (A conjugate to its inverse in SL(2, Z)): %d; a rotation of its exchanged word (A fixed by a conjugation of determinant -1): %d; either: %d for each sign, %d in all; LR among them: %s; of the %d states, those with the same property: %d" % (
        len(a1), len(a2), len(amph), 2 * len(amph), "LR" in amph, len(states), sum(1 for m in states if rc(m) == rc(swap(m[::-1])) or rc(m) == rc(swap(m)))))
    odd = [s for s in states if int(mat(s).trace()) % 2 == 1]; cases = 0; bad = 0; both = 0
    gP = H.norm((0, 1, 1, 0, 1)); gD, gI = H.QI, H.QK                         # lifts: P (a <-> b) is Ad by (I+J)/sqrt2; D (b -> b^-1) is Ad by I; -1 is Ad by K
    for s in odd:
        vals = set()
        for r in rot(s):
            g = glift(r); c = cls(g); cases += 1; vals.add(c); o3 = H.qpow(g, 3) in (H.ONE, H.MONE)
            flips = [cls(H.qinv(g))] + [cls(H.ad(k, g)) for k in (H.gL, H.gR, gP)]; keeps = [cls(H.ad(k, g)) for k in (gD, gI, H.QJ)]
            if not (o3 and c != 0 and all(f == -c for f in flips) and all(k == c for k in keeps)): bad += 1
        both += vals == {1, -1}
    print("B3: odd-trace states: %d for each sign, %d in all; cases (a state, a sign, a rotation): %d; in every case the lift has order 3 or 6, its class flips under inversion and under conjugation by the lifts of L, R and P, and is kept by D, -1 and an inner automorphism: %s (failures %d); states on which the class takes both values across the rotations: %d of %d" % (len(odd), 2 * len(odd), 2 * cases, bad == 0, bad, both, len(odd)))
    print("B3: the group 2O generated by the lifts of L and R has %d elements" % len((lambda gens: (lambda S: [S.update({H.qmul(a, g) for a in list(S) for g in gens}) for _ in range(12)] and S)({H.ONE}))([H.gL, H.gR])))
