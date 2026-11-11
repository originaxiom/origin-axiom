"""
W-C3, items W108 and W109 (arc B1679): the common point, computed by this seat's own route.

SOURCE OF THE DEFINITIONS.  The SM seat's W108_RULE.md and W109_PROOF.md as main received them (B1679's
verification/received/), read through the mask.  Neither the seat's scripts nor main's checking script is run or
opened.  Conventions, as the rule and the proof state them: a move phi acts on a tuple by composition,
(rho o phi)(a_i) = phi(a_i) evaluated on the tuple; R_ij is a_i -> a_i a_j and L_ij is a_i -> a_j a_i; at n = 2 the
record's moves are R: a -> ab and L: b -> ab.  The full moves are every a_i -> a_i a_j^{+-1} and a_i -> a_j^{+-1} a_i
(i != j), every inversion a_i -> a_i^-1, and the transpositions of the letters.  A class is an element of
Epi(F_n, G)/Aut(G); a character is the trace function through G in SU(2), read for n = 3 on the seven traces of a1, a2,
a3, a1a2, a1a3, a2a3, a1a2a3, and for n = 2 on those of a, b, ab.

WHAT IS COMPUTED, AND WHAT WOULD COUNT AS NOT REPRODUCING (written before the run)
  W108
  A0  2I has 120 elements and centre {+-1}; 21 maximal subgroups, five of order 24, six of order 20, ten of order 12;
      |Aut(2I)| = 120, |Inn(2I)| = 60; Aut acts freely on Epi(F_n, 2I).  Q8: |Aut| = 24; |Epi(F2, Q8)| = 24 in one
      class; |Epi(F3, Q8)| = 336 in 14 classes.
  H   |Epi(F_n, G)| by enumeration equals Hall's sum over the subgroup lattice, for G = 2I and Q8, n = 2 and 3.
  P   Q8's single class at n = 2 is fixed by every full move and by L and R, and so is its character (0, 0, 0).
  N2  2I at n = 2: no class and no character is fixed by every full move, nor by L and R.
  C1  2I at n = 3: no class is fixed by every full move (K), nor by the transvections alone (T); no character is
      fixed by every full move (X), nor by the transvections alone.
  CQ  Q8 at n = 3: no class is fixed by every full move.
  O   main's claim: Epi(F3, 2I)/Aut(2I) has 13 344 classes, one orbit under the full moves.  The transvections'
      orbits, and every orbit count at n = 2 and 3 for both groups, are reported.
  Any of A0, H, P, N2, C1, CQ, or the 13 344 and one orbit, coming out otherwise is NOT REPRODUCED.
  W109
  (ii) at n = 2, the characters (x, y, z) = (tr a, tr b, tr ab) fixed by R and L, solved exactly (sympy): exactly
      (2, 2, 2) and (0, 0, 0).  Otherwise NOT REPRODUCED.
  (iii) at n = 3, for G = Z/2, Z/3, Z/4, Z/6, Q8, the binary dihedral group of order 12, 2T, 2O and 2I: no class of
      Epi(F3, G)/Aut(G) is fixed by every R_ij.  A fixed class for any G is NOT REPRODUCED.
  (i) at n = 3 and n = 4, a numerical search (least squares from random starts) for a character of F_n in SL(2, C)
      fixed by every R_ij, and at n = 3 by every L_ij: every start that converges (residual below 1e-10) must reach the
      trivial character (every trace within 1e-6 of 2).  A converged non-trivial character is NOT REPRODUCED.  A search
      is evidence, not a proof; the proof is left to agy-exp.

CONTROLS (must come out as stated, or the code is broken)
  K1  the same search at n = 2 with R and L, from random starts: every converged start reaches (2, 2, 2) or
      (0, 0, 0), and (0, 0, 0) is reached at least once.
  K2  the quaternion representation a -> i, b -> j is a tuple of Epi(F2, Q8) whose traces are (0, 0, 0).

DISCLOSED.  The seat's and main's statements are known to this seat (main's claim line gives the 13 344 and the one
orbit); this is a check, not a blind test.
"""
import itertools
import json
import sys

import numpy as np

# ---------------------------------------------------------------------------------------------------------- groups


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
                     a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
                     a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2])


def key(q):
    return tuple(np.round(q, 9) + 0.0)


class Group:
    def __init__(self, elems, name):
        self.name = name
        self.q = [np.array(e, dtype=float) for e in elems]
        self.n = len(self.q)
        self.idx = {key(e): i for i, e in enumerate(self.q)}
        assert len(self.idx) == self.n, name
        self.mt = np.zeros((self.n, self.n), dtype=np.int64)
        for i, a in enumerate(self.q):
            for j, b in enumerate(self.q):
                self.mt[i, j] = self.idx[key(qmul(a, b))]
        self.e = self.idx[key(np.array([1.0, 0, 0, 0]))]
        self.inv = np.array([int(np.where(self.mt[i] == self.e)[0][0]) for i in range(self.n)])
        self.tr = np.array([2 * e[0] for e in self.q])
        self.m1 = self.idx.get(key(np.array([-1.0, 0, 0, 0])))


def closure(gens):
    elems = {key(np.array([1.0, 0, 0, 0])): np.array([1.0, 0, 0, 0])}
    frontier = list(elems.values())
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = qmul(x, g)
                k = key(y)
                if k not in elems:
                    elems[k] = y
                    nxt.append(y)
        frontier = nxt
    return list(elems.values())


PHI = (1 + 5 ** 0.5) / 2


def binary_icosahedral():
    """2T's 24 together with the even permutations of (0, +-1, +-phi^-1, +-phi)/2.  Which of the two orderings of
    (phi^-1, phi) is closed under the Hamilton product depends on the product's convention, so both are tried and the
    one that is closed is used; the run reports which."""
    base = []
    for i in range(4):
        for sgn in (1, -1):
            v = [0.0] * 4
            v[i] = sgn
            base.append(v)
    for signs in itertools.product((1, -1), repeat=4):
        base.append([s_ / 2 for s_ in signs])
    even = [p for p in itertools.permutations(range(4)) if
            sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0]
    for label, vals in (('(0, 1, 1/phi, phi)', (0.0, 1.0, 1 / PHI, PHI)), ('(0, 1, phi, 1/phi)', (0.0, 1.0, PHI, 1 / PHI))):
        el = list(base)
        for perm in even:
            for signs in itertools.product((1, -1), repeat=3):
                v = [vals[0], signs[0] * vals[1], signs[1] * vals[2], signs[2] * vals[3]]
                w_ = [0.0] * 4
                for pos in range(4):
                    w_[perm[pos]] = v[pos] / 2
                el.append(w_)
        keys = {key(np.array(e)) for e in el}
        closed = all(key(qmul(np.array(a), np.array(b))) in keys for a in el for b in el)
        if closed and len(keys) == 120:
            print('2I built from the even permutations of', label)
            return Group(el, '2I')
    raise SystemExit('2I: neither ordering is closed')


def group_from(gens, name):
    return Group(closure([np.array(g, dtype=float) for g in gens]), name)


def unit(angle):
    """The unit quaternion cos(angle) + i sin(angle), of order 2 pi / angle."""
    return [np.cos(angle), np.sin(angle), 0.0, 0.0]


# ---------------------------------------------------------------------------------------------------------- lattice


def subgroup_closure(G, gens):
    S = {G.e}
    frontier = [G.e]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = int(G.mt[x, g])
                if y not in S:
                    S.add(y)
                    nxt.append(y)
        frontier = nxt
    return frozenset(S)


def all_subgroups(G):
    subs = set()
    for a in range(G.n):
        for b in range(a, G.n):
            subs.add(subgroup_closure(G, [a, b]))
    return sorted(subs, key=len)


def mobius_to_top(subs, G):
    top = frozenset(range(G.n))
    mu = {top: 1}
    for H in sorted(subs, key=len, reverse=True):
        if H == top:
            continue
        mu[H] = -sum(mu[K] for K in subs if len(K) > len(H) and H < K)
    return mu


# ---------------------------------------------------------------------------------------------------------- Aut(G)


def words_tree(G, gens):
    """For each element, a word (list of generator indices) reaching it from e."""
    word = {G.e: []}
    frontier = [G.e]
    while frontier:
        nxt = []
        for x in frontier:
            for k, g in enumerate(gens):
                y = int(G.mt[x, g])
                if y not in word:
                    word[y] = word[x] + [k]
                    nxt.append(y)
        frontier = nxt
    return word


def automorphisms(G, gens):
    word = words_tree(G, gens)
    assert len(word) == G.n
    auts = []
    for imgs in itertools.product(range(G.n), repeat=len(gens)):
        f = np.full(G.n, -1, dtype=np.int64)
        for x, w in word.items():
            y = G.e
            for k in w:
                y = int(G.mt[y, imgs[k]])
            f[x] = y
        if len(set(f.tolist())) != G.n:
            continue
        ok = True
        for x in range(G.n):
            for k, g in enumerate(gens):
                if f[G.mt[x, g]] != G.mt[f[x], imgs[k]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            auts.append(f)
    return np.array(auts)


def generating_pair(G):
    for a in range(G.n):
        if len(subgroup_closure(G, [a])) == G.n:
            return [a]
    for a in range(G.n):
        for b in range(G.n):
            if len(subgroup_closure(G, [a, b])) == G.n:
                return [a, b]


# ---------------------------------------------------------------------------------------------------------- Epi


def epi_tuples(G, n, maximal):
    masks = np.zeros(G.n, dtype=np.int64)
    for k, M in enumerate(maximal):
        for x in M:
            masks[x] |= (1 << k)
    grids = np.meshgrid(*([np.arange(G.n)] * n), indexing='ij')
    T = np.stack([g.ravel() for g in grids], axis=1)
    m = masks[T[:, 0]]
    for i in range(1, n):
        m = m & masks[T[:, i]]
    return T[m == 0]


def codes(G, T):
    base = np.array([G.n ** (T.shape[1] - 1 - i) for i in range(T.shape[1])], dtype=np.int64)
    return T @ base


def canon(G, auts, T, chunk=20000):
    out = np.empty(len(T), dtype=np.int64)
    base = np.array([G.n ** (T.shape[1] - 1 - i) for i in range(T.shape[1])], dtype=np.int64)
    for s in range(0, len(T), chunk):
        Tc = T[s:s + chunk]
        imgs = auts[:, Tc]                 # (nauts, chunk, n)
        c = imgs @ base                    # (nauts, chunk)
        out[s:s + chunk] = c.min(axis=0)
    return out


def apply_move(G, T, move):
    """move: ('tr', i, j, eps, side) | ('inv', i) | ('swap', i, j) | ('R2',) | ('L2',)"""
    T2 = T.copy()
    kind = move[0]
    if kind == 'tr':
        _, i, j, eps, side = move
        gj = T[:, j] if eps == 1 else G.inv[T[:, j]]
        T2[:, i] = G.mt[T[:, i], gj] if side == 'right' else G.mt[gj, T[:, i]]
    elif kind == 'inv':
        T2[:, move[1]] = G.inv[T[:, move[1]]]
    elif kind == 'swap':
        i, j = move[1], move[2]
        T2[:, i], T2[:, j] = T[:, j], T[:, i]
    elif kind == 'R2':          # a -> ab
        T2[:, 0] = G.mt[T[:, 0], T[:, 1]]
    elif kind == 'L2':          # b -> ab
        T2[:, 1] = G.mt[T[:, 0], T[:, 1]]
    return T2


def move_sets(n):
    trans = [('tr', i, j, eps, side) for i in range(n) for j in range(n) if i != j for eps in (1, -1)
             for side in ('right', 'left')]
    full = trans + [('inv', i) for i in range(n)] + [('swap', i, j) for i in range(n) for j in range(i + 1, n)]
    Rij = [('tr', i, j, 1, 'right') for i in range(n) for j in range(n) if i != j]
    sets = {'full': full, 'transvections': trans, 'R_ij': Rij}
    if n == 2:
        sets['<L, R>'] = [('R2',), ('L2',)]
    return sets


def char_vec(G, T):
    n = T.shape[1]
    if n == 2:
        cols = [G.tr[T[:, 0]], G.tr[T[:, 1]], G.tr[G.mt[T[:, 0], T[:, 1]]]]
    else:
        a, b, c = T[:, 0], T[:, 1], T[:, 2]
        cols = [G.tr[a], G.tr[b], G.tr[c], G.tr[G.mt[a, b]], G.tr[G.mt[a, c]], G.tr[G.mt[b, c]],
                G.tr[G.mt[G.mt[a, b], c]]]
    return np.stack(cols, axis=1)


def analyse(G, auts, n, maximal, want_orbits=True, sets=None):
    T = epi_tuples(G, n, maximal)
    cc = canon(G, auts, T)
    uniq, first = np.unique(cc, return_index=True)
    reps = T[first]
    res = dict(epi=int(len(T)), classes=int(len(uniq)))
    free = (len(T) == len(uniq) * len(auts))
    res['aut_acts_freely'] = bool(free)
    if sets is None:
        sets = move_sets(n)
    X = char_vec(G, T)
    for name, mv in sets.items():
        images = []
        for m in mv:
            c2 = canon(G, auts, apply_move(G, reps, m))
            images.append(np.searchsorted(uniq, c2))
        images = np.array(images)                    # (moves, classes)
        fixed = int(np.sum(np.all(images == np.arange(len(uniq))[None, :], axis=0)))
        res['classes fixed by ' + name] = fixed
        # characters: tuples whose trace vector is kept by every move
        keep = np.ones(len(T), dtype=bool)
        for m in mv:
            keep &= np.all(np.abs(char_vec(G, apply_move(G, T, m)) - X) < 1e-9, axis=1)
        res['tuples whose character is fixed by ' + name] = int(keep.sum())
        if keep.any():
            res['fixed characters by ' + name] = sorted({tuple(np.round(r, 6)) for r in X[keep]})[:5]
        if want_orbits:
            parent = list(range(len(uniq)))

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            for row in images:
                for a, b in enumerate(row):
                    ra, rb = find(a), find(int(b))
                    if ra != rb:
                        parent[ra] = rb
            roots = {}
            for x in range(len(uniq)):
                r = find(x)
                roots[r] = roots.get(r, 0) + 1
            res['orbits under ' + name] = sorted(roots.values(), reverse=True)
    return res


# ---------------------------------------------------------------------------------------------------------- W109 (i)


def search(n, moves, starts, seed, near=None):
    from scipy.optimize import least_squares
    rng = np.random.default_rng(seed)
    words = [(k,) for k in range(n)] + [(k, l) for k in range(n) for l in range(n) if k < l] + \
            [(k, l, m) for k, l, m in itertools.permutations(range(n), 3)]

    def mats(p):
        gs = []
        for i in range(n):
            a = p[6 * i] + 1j * p[6 * i + 1]
            b = p[6 * i + 2] + 1j * p[6 * i + 3]
            c = p[6 * i + 4] + 1j * p[6 * i + 5]
            d = (1 + b * c) / a
            gs.append(np.array([[a, b], [c, d]]))
        return gs

    def image(gs, move):
        out = list(gs)
        kind, i, j = move
        out[i] = gs[i] @ gs[j] if kind == 'R' else gs[j] @ gs[i]
        return out

    def trw(gs, w):
        m = np.eye(2, dtype=complex)
        for k in w:
            m = m @ gs[k]
        return np.trace(m)

    def resid(p):
        gs = mats(p)
        r = []
        base = [trw(gs, w) for w in words]
        for mv in moves:
            g2 = image(gs, mv)
            for w, t0 in zip(words, base):
                d = trw(g2, w) - t0
                r += [d.real, d.imag]
        return np.array(r)

    found = []
    for s in range(starts):
        if near is not None:
            p0 = np.array(near) + 0.05 * rng.standard_normal(6 * n)
        else:
            p0 = rng.standard_normal(6 * n)
            for i in range(n):
                if abs(p0[6 * i] + 1j * p0[6 * i + 1]) < 0.2:
                    p0[6 * i] += 1.0
        try:
            sol = least_squares(resid, p0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        except Exception:
            continue
        rn = float(np.linalg.norm(sol.fun))
        gs = mats(sol.x)
        trs = [trw(gs, w) for w in words]
        found.append((rn, [complex(t) for t in trs]))
    conv = [f for f in found if f[0] < 1e-10]
    nontriv = [f for f in conv if max(abs(t - 2) for t in f[1]) > 1e-6]
    return dict(starts=starts, ran=len(found), converged=len(conv), converged_nontrivial=len(nontriv),
                max_dev_from_2=max((max(abs(t - 2) for t in f[1]) for f in conv), default=None),
                nontrivial_examples=[[complex(round(t.real, 6), round(t.imag, 6)) for t in f[1]]
                                     for f in nontriv[:3]])


# ---------------------------------------------------------------------------------------------------------- main


def main():
    out = {}
    # ------------------------------------------------ W108
    I2 = binary_icosahedral()
    Q8 = group_from([[0, 1, 0, 0], [0, 0, 1, 0]], 'Q8')
    centre = [x for x in range(I2.n) if all(I2.mt[x, y] == I2.mt[y, x] for y in range(I2.n))]
    subs = all_subgroups(I2)
    top = frozenset(range(I2.n))
    proper = [H for H in subs if H != top]
    maximal = [H for H in proper if not any(H < K for K in proper)]
    orders = sorted(len(H) for H in maximal)
    gens = generating_pair(I2)
    auts = automorphisms(I2, gens)
    inn = {tuple(I2.mt[I2.mt[g, :], I2.inv[g]].tolist()) for g in range(I2.n)}
    a0 = dict(order=I2.n, centre=sorted(float(I2.tr[c]) / 2 for c in centre), subgroups=len(subs),
              maximal=len(maximal), maximal_orders={o: orders.count(o) for o in sorted(set(orders))},
              aut=int(len(auts)), inn=len(inn))
    print('W108 A0  2I:', a0)
    out['A0_2I'] = a0
    subsQ = all_subgroups(Q8)
    properQ = [H for H in subsQ if H != frozenset(range(Q8.n))]
    maximalQ = [H for H in properQ if not any(H < K for K in properQ)]
    autsQ = automorphisms(Q8, generating_pair(Q8))
    print('W108 A0  Q8: order %d, subgroups %d, maximal %d, |Aut| %d' % (Q8.n, len(subsQ), len(maximalQ), len(autsQ)))
    out['A0_Q8'] = dict(order=Q8.n, maximal=len(maximalQ), aut=int(len(autsQ)))

    # H: Hall
    for G, sb, mx in ((I2, subs, maximal), (Q8, subsQ, maximalQ)):
        mu = mobius_to_top(sb, G)
        for n in (2, 3):
            hall = sum(mu[H] * len(H) ** n for H in sb)
            enum = len(epi_tuples(G, n, mx))
            print('W108 H   %s, n = %d: enumeration %d, Hall %d, %s' % (G.name, n, enum, hall,
                                                                       'equal' if enum == hall else 'DIFFER'))
            out['H_%s_%d' % (G.name, n)] = (enum, hall)

    # K2 and P
    i_, j_ = Q8.idx[key(np.array([0.0, 1, 0, 0]))], Q8.idx[key(np.array([0.0, 0, 1, 0]))]
    k2 = char_vec(Q8, np.array([[i_, j_]]))[0]
    print('W108 K2  traces of a -> i, b -> j:', k2.tolist())
    for G, a, mx, n in ((Q8, autsQ, maximalQ, 2), (Q8, autsQ, maximalQ, 3), (I2, auts, maximal, 2),
                        (I2, auts, maximal, 3)):
        r = analyse(G, a, n, mx)
        out['W108_%s_n%d' % (G.name, n)] = r
        print('W108 %s at n = %d:' % (G.name, n))
        for k, v in r.items():
            if k.startswith('orbits') and isinstance(v, list) and len(v) > 12:
                v = '%d orbits, sizes %s ...' % (len(v), v[:12])
            print('     %s: %s' % (k, v))

    # ------------------------------------------------ W109 (ii), exact
    import sympy as sp
    x, y, z = sp.symbols('x y z')
    # R: a -> ab: (x, y, z) -> (tr ab, tr b, tr abb) = (z, y, yz - x); L: b -> ab: (x, y, z) -> (x, z, tr a ab) = (x, z, xz - y)
    Rm = (z, y, y * z - x)
    Lm = (x, z, x * z - y)
    eqs = [Rm[k] - (x, y, z)[k] for k in range(3)] + [Lm[k] - (x, y, z)[k] for k in range(3)]
    sols = sp.solve(eqs, [x, y, z], dict=True)
    print('W109 (ii) characters fixed by R and L at n = 2:', sols)
    out['W109_ii'] = [str(s) for s in sols]

    # ------------------------------------------------ W109 (iii), classes fixed by every R_ij at n = 3
    groups = {
        'Z/2': group_from([unit(2 * np.pi / 2)], 'Z/2'),
        'Z/3': group_from([unit(2 * np.pi / 3)], 'Z/3'),
        'Z/4': group_from([unit(2 * np.pi / 4)], 'Z/4'),
        'Z/6': group_from([unit(2 * np.pi / 6)], 'Z/6'),
        'Q8': Q8,
        '2D3 (order 12)': group_from([unit(np.pi / 3), [0, 0, 1, 0]], '2D3'),
        '2T': group_from([[0, 1, 0, 0], [0.5, 0.5, 0.5, 0.5]], '2T'),
        '2O': group_from([unit(np.pi / 4), [0.5, 0.5, 0.5, 0.5]], '2O'),
        '2I': I2,
    }
    for name, G in groups.items():
        print('W109 (iii) group %s built with %d elements' % (name, G.n))
    for name, G in groups.items():
        sb = all_subgroups(G) if G.n <= 48 else subs
        prop = [H for H in sb if H != frozenset(range(G.n))]
        mx = [H for H in prop if not any(H < K for K in prop)]
        a = auts if G is I2 else automorphisms(G, generating_pair(G))
        r = analyse(G, a, 3, mx, want_orbits=False, sets={'R_ij': move_sets(3)['R_ij']})
        print('W109 (iii) %-15s order %3d, |Aut| %3d, Epi(F3) %8d, classes %6d, classes fixed by every R_ij: %d'
              % (name, G.n, len(a), r['epi'], r['classes'], r['classes fixed by R_ij']))
        out['W109_iii_' + name] = dict(order=G.n, aut=int(len(a)), epi=r['epi'], classes=r['classes'],
                                       fixed=r['classes fixed by R_ij'])

    # ------------------------------------------------ W109 (i), numerical
    k1 = search(2, [('R', 0, 1), ('L', 1, 0)], 60, 11, near=None)
    print('W109 K1  n = 2, R and L, random starts:', {k: v for k, v in k1.items() if k != 'nontrivial_examples'},
          'non-trivial points found:', k1['nontrivial_examples'][:2])
    out['W109_K1'] = k1
    for n, moves, starts, label in ((3, [('R', i, j) for i in range(3) for j in range(3) if i != j], 150, 'R_ij'),
                                    (3, [('L', j, i) for i in range(3) for j in range(3) if i != j], 80, 'L_ij'),
                                    (4, [('R', i, j) for i in range(4) for j in range(4) if i != j], 60, 'R_ij')):
        r = search(n, moves, starts, 7 + n)
        print('W109 (i) n = %d, every %s:' % (n, label), r)
        out['W109_i_n%d_%s' % (n, label)] = r
    json.dump(out, open(sys.argv[1], 'w'), indent=1, default=str)
    return 0


if __name__ == '__main__':
    sys.exit(main())
