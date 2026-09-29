"""Shared E6 setup: roots, Weyl group, one A2+A1, the 27, branching tools."""
from fractions import Fraction as F
from rootsys import *
from collections import Counter, defaultdict

simple = E6_simple()
roots = generate_roots(simple)
idx = {r: i for i, r in enumerate(roots)}
gens = simple_reflection_perms(roots, simple)
order, group = weyl_group_order(roots, simple)
A = cartan_matrix(simple)


def solve_exact(M, b):
    n = len(M)
    Mx = [list(map(F, M[i])) + [F(b[i])] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if Mx[i][c] != 0)
        Mx[c], Mx[piv] = Mx[piv], Mx[c]
        pv = Mx[c][c]
        Mx[c] = [x / pv for x in Mx[c]]
        for i in range(n):
            if i != c and Mx[i][c] != 0:
                f = Mx[i][c]
                Mx[i] = [x - f * y for x, y in zip(Mx[i], Mx[c])]
    return [Mx[i][n] for i in range(n)]


def from_simple_coords(c):
    out = [F(0)] * 8
    for ck, a in zip(c, simple):
        out = [x + ck * y for x, y in zip(out, a)]
    return tuple(out)


def simple_coeffs(r):
    return solve_exact(A, [ip(r, simple[j]) for j in range(6)])


omegas = [from_simple_coords(solve_exact(A, [1 if k == i else 0 for k in range(6)]))
          for i in range(6)]


def weight_orbit(w):
    seen, q = {w}, [w]
    while q:
        x = q.pop()
        for a in simple:
            y = refl(x, a)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return sorted(seen)


W27 = weight_orbit(omegas[0])
assert len(W27) == 27

A2 = a2_subsystems(roots)
A2A1 = a2_a1_subsystems(roots, A2)
rep = A2A1[0]
a2part = [g for g in A2 if g <= rep][0]
a2roots = [roots[k] for k in a2part]
a1roots = [roots[k] for k in rep if k not in a2part]
b1 = a2roots[0]
b2 = next(r for r in a2roots if ip(b1, r) == -1)
gam = a1roots[0]
stab = [g for g in group if frozenset(g[k] for k in rep) == rep]


def lin_of_perm(g):
    images = [roots[g[idx[a]]] for a in simple]

    def act(v):
        c = simple_coeffs(v)
        out = [F(0)] * 8
        for ck, im in zip(c, images):
            out = [x + ck * y for x, y in zip(out, im)]
        return tuple(out)
    return act


stab_lin = [lin_of_perm(g) for g in stab]


def su3_orbit(lab):
    seen, q = {lab}, [lab]
    while q:
        a, b = q.pop()
        for y in ((-a, a + b), (a + b, -b)):
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen


LIB3 = {(0, 0): {(0, 0)}, (1, 0): su3_orbit((1, 0)), (0, 1): su3_orbit((0, 1))}
LIB2 = {0: [0], 1: [1, -1]}
NAME3 = {(0, 0): "1", (1, 0): "3", (0, 1): "3b"}
flip = {"3": "3b", "3b": "3", "1": "1"}

SM = sorted([("3", 2, F(1, 6)), ("3b", 1, F(-2, 3)), ("1", 1, F(1)),
             ("3b", 1, F(1, 3)), ("1", 2, F(-1, 2)),
             ("3b", 1, F(1, 3)), ("1", 2, F(-1, 2)),
             ("3", 1, F(-1, 3)), ("1", 2, F(1, 2)),
             ("1", 1, F(0)), ("1", 1, F(0))])


def vec_of(n):
    v = [F(0)] * 8
    for ni, w in zip(n, omegas):
        v = [x + ni * y for x, y in zip(v, w)]
    return tuple(v)


def branch(Y, weights=W27):
    bylevel = defaultdict(list)
    for w in weights:
        bylevel[ip(w, Y)].append((ip(w, b1), ip(w, b2), ip(w, gam)))
    out = []
    for y, ws in bylevel.items():
        M = Counter(ws)
        while sum(M.values()):
            dom = [t for t in M if t[0] >= 0 and t[1] >= 0 and t[2] >= 0]
            if not dom:
                return None
            hw = max(dom, key=lambda t: (t[0] + t[1] + t[2], t))
            l3, l2 = (hw[0], hw[1]), hw[2]
            if l3 not in LIB3 or l2 not in LIB2:
                return None
            for p in LIB3[l3]:
                for q in LIB2[l2]:
                    t = (p[0], p[1], q)
                    if M[t] <= 0:
                        return None
                    M[t] -= 1
                    if M[t] == 0:
                        del M[t]
            out.append((NAME3[l3], int(l2) + 1, y))
    return sorted(out, key=lambda t: (t[2], t[0], t[1]))


def canon_sig(s):
    m = max(abs(c) for _, _, c in s)
    def nm(sgn):
        return tuple(sorted((a, b, sgn * c / m) for a, b, c in s))
    return min(nm(1), nm(-1))


def is_sm(s):
    if s is None:
        return False
    qq = [c for a, b, c in s if b == 2 and a in ("3", "3b")]
    if len(qq) != 1 or qq[0] == 0:
        return False
    lm = F(1, 6) / qq[0]
    for f in (False, True):
        for sgn in (1, -1):
            t = sorted((flip[a] if f else a, b, sgn * lm * c) for a, b, c in s)
            if t == SM:
                return True
    return False
