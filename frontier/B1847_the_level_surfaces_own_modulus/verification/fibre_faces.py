"""P-727, the tube (data-free): the fibre group's elements as chi = 0 words in the FULL group's letters, with their period
classes in H_1(fibre) computed through the monodromy.

H_1(F) is a module over <c>: a letter a or b at height h (the net number of c's before it) contributes +-M^h e_letter,
where M is conjugation by c on H_1(F), read off the relators. Check, automatic: whenever two words give the same matrix
(up to sign) their classes must agree -- a wrong M or a wrong formula breaks it. Periods in the fibre generators' basis
(x, y) follow from [x], [y] written in ([a], [b])."""
import itertools
import numpy as np


def monodromy_from_relators(gens, rels, chi):
    """M on H_1(F) in the basis of the chi = 0 generators, solved from the relators' vanishing classes.
    Unknowns: M (2x2) on the two fibre generators f0, f1. Each relator's class sum_l s M^h e = 0 is linear in the entries
    of M^h; with heights in {-1, 0, 1} (true for these presentations, checked) it is linear in M and M^{-1} -- solved by
    a small search over integer M with det 1 satisfying every relator."""
    fib = [g for g in gens if chi[g] == 0]
    cg = [g for g in gens if chi[g] != 0]
    assert len(fib) == 2 and len(cg) == 1 and chi[cg[0]] == 1
    c = cg[0]
    def cls(word, M, Minv):
        v = np.zeros(2, dtype=object); h = 0
        for ch in word:
            low = ch.lower(); sgn = 1 if ch.islower() else -1
            if low == c:
                h += sgn; continue
            e = np.array([1, 0] if low == fib[0] else [0, 1], dtype=object)
            P = np.eye(2, dtype=object)
            for _ in range(abs(h)):
                P = P.dot(M if h > 0 else Minv)
            v = v + sgn * P.dot(e)
        return v
    sols = []
    R = range(-40, 41)
    for p, q, r in itertools.product(R, R, R):
        # M = [[p, q], [r, s]] with det 1: s = (1 + q r) / p
        if p == 0 or (1 + q * r) % p:
            continue
        s = (1 + q * r) // p
        M = np.array([[p, q], [r, s]], dtype=object)
        Minv = np.array([[s, -q], [-r, p]], dtype=object)
        if all(not any(cls(w, M, Minv)) for w in rels):
            sols.append(M)
    return fib, c, sols, cls


def bfs_fibre(G, M, fib, c, depth, rmin, normcap=400.0, keep_all=False):
    """BFS over the full group's letters carrying (matrix, chi, height, class); returns the chi = 0 elements' isometric
    spheres with classes, and the count of class conflicts between coinciding matrices (must be 0)."""
    Minv = np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]], dtype=object)
    pw = {0: np.eye(2, dtype=object)}
    def Mp(h):
        if h not in pw:
            P = np.eye(2, dtype=object)
            for _ in range(abs(h)):
                P = P.dot(M if h > 0 else Minv)
            pw[h] = P
        return pw[h]
    letters = []
    for g in G.gens:
        for ch in (g, g.upper()):
            X = G.wmat(ch)
            letters.append((ch, tuple(complex(v) for v in X.ravel())))
    def key(m):
        a, b, cc, d = m
        for v in (cc, d, a, b):
            if abs(v) > 1e-9:
                sg = 1 if (v.real > 1e-9 or (abs(v.real) <= 1e-9 and v.imag > 0)) else -1
                break
        return tuple(int(round(sg * x * 1e6)) for v in m for x in (v.real, v.imag)), sg
    I = (1 + 0j, 0j, 0j, 1 + 0j)
    k0, _ = key(I)
    seen = {k0: (0, (0, 0))}             # key -> (chi, class)
    frontier = [(I, 0, 0, (0, 0))]
    out = []; conflicts = 0
    for _ in range(depth):
        nxt = []
        for (a, b, cc, d), chi_, h, cl in frontier:
            for ch, (p, q, r, s_) in letters:
                Y = (a * p + b * r, a * q + b * s_, cc * p + d * r, cc * q + d * s_)
                if max(abs(Y[0]), abs(Y[1]), abs(Y[2]), abs(Y[3])) > normcap:
                    continue
                low = ch.lower(); sgn = 1 if ch.islower() else -1
                if low == c:
                    chi2, h2, cl2 = chi_ + sgn, h + sgn, cl
                else:
                    e = np.array([1, 0] if low == fib[0] else [0, 1], dtype=object)
                    v = Mp(h).dot(e) * sgn
                    chi2, h2, cl2 = chi_, h, (cl[0] + int(v[0]), cl[1] + int(v[1]))
                k, sg = key(Y)
                if k in seen:
                    if seen[k][0] == chi2 and seen[k][1] != cl2:
                        conflicts += 1
                    continue
                seen[k] = (chi2, cl2)
                nxt.append((Y, chi2, h2, cl2))
                if (keep_all or chi2 == 0) and abs(Y[2]) > 1e-9 and 1 / abs(Y[2]) > rmin:
                    out.append((np.array([[Y[0], Y[1]], [Y[2], Y[3]]]), cl2) if not keep_all else
                               (np.array([[Y[0], Y[1]], [Y[2], Y[3]]]), chi2, cl2))
        frontier = nxt
    return out, conflicts, len(seen)
