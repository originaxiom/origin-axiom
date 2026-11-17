"""B1957: the web seat's W-F17 (second computations for four items of the foundation's 'computed nowhere yet'), the
parts main recomputes here on its own code.  Data-free, exact.
 Q1  item 1: homomorphisms and surjections from three bundle groups (m004 = +LR, m369 = -LLRLR, s639 = -LLLRLR) onto
     the binary polyhedral groups 2T = SL(2, 3), 2O (order 48, in SL(2, 7)) and 2I = SL(2, 5).
 Q3  item 3: the metallic trace maps phi_m = Ta^m Tb^m, Ta(x, y, z) = (x, z, xz - y), Tb(x, y, z) = (z, y, yz - x):
     the fixed equations Tb^m(p) = Ta^-m(p) are linear in z; the lines and curves the note lists are fixed; the
     projections of the main curves at m = 1, 2, 3; the lines {x = z = 0}, {y = z = 0} are fixed exactly when 4 | m;
     the number of components over Q at m = 1 to 6.
 Q4  item 4: E18 (matrices of SL(2, Z) with entries in [-5, 5]) and E19 (integer points of the trace surface)."""
import itertools, functools, collections
import numpy as np, sympy as sp
print = functools.partial(print, flush=True)


def sl2(p):
    els = [e for e in itertools.product(range(p), repeat=4) if (e[0] * e[3] - e[1] * e[2]) % p == 1]
    mul = lambda a, b: ((a[0] * b[0] + a[1] * b[2]) % p, (a[0] * b[1] + a[1] * b[3]) % p, (a[2] * b[0] + a[3] * b[2]) % p, (a[2] * b[1] + a[3] * b[3]) % p)
    return els, mul


def table(els, mul):
    idx = {e: i for i, e in enumerate(els)}; n = len(els); T = np.array([[idx[mul(a, b)] for b in els] for a in els], dtype=np.int64)
    e = next(i for i in range(n) if all(T[i, j] == j for j in range(n))); inv = np.array([int(np.where(T[i] == e)[0][0]) for i in range(n)]); return T, inv, e


def closure(gens, mul):
    S = set(gens); frontier = list(S)
    while frontier:
        new = []
        for a in frontier:
            for g in gens:
                c = mul(a, g)
                if c not in S: S.add(c); new.append(c)
        frontier = new
    return S


def binary_octahedral():
    els, mul = sl2(7); order = lambda a: next(k for k in range(1, 60) if functools.reduce(lambda u, _: mul(u, a), range(k - 1), a) == (1, 0, 0, 1))
    o8 = [a for a in els if order(a) == 8]; o3 = [a for a in els if order(a) == 3]
    for a in o8:
        for b in o3:
            S = closure([a, b], mul)
            if len(S) == 48: return sorted(S), mul
    raise RuntimeError


def counts(T, inv, e, word, sign):
    """(homomorphisms, surjections) from <a, b, t | t a t^-1 = phi(a), t b t^-1 = phi(b)> to the group with table T;
    phi the word's automorphism (L: b -> ab; R: a -> ba), composed with a -> a^-1, b -> b^-1 if sign = -1"""
    n = T.shape[0]; A, B = np.meshgrid(np.arange(n), np.arange(n), indexing="ij"); a, b = A.ravel(), B.ravel(); fa, fb = a.copy(), b.copy()
    for letter in word:                                              # apply the letters as substitutions on the images
        if letter == "L": fb = T[fa, fb]
        else: fa = T[fb, fa]
    if sign == -1: fa, fb = inv[fa], inv[fb]
    hom = 0; triples = []
    for t in range(n):
        ok = (T[t, a] == T[fa, t]) & (T[t, b] == T[fb, t]); hom += int(ok.sum()); triples += [(int(x), int(y), t) for x, y in zip(a[ok], b[ok])]
    epi = 0
    for (x, y, t) in triples:
        S = {e}; fr = [e]
        while fr:
            nw = []
            for u in fr:
                for g in (x, y, t):
                    c = int(T[u, g])
                    if c not in S: S.add(c); nw.append(c)
            fr = nw
        epi += len(S) == n
    return hom, epi


if __name__ == "__main__":
    groups = {"2T": sl2(3), "2O": binary_octahedral(), "2I": sl2(5)}; note = {("m004", "2T"): (72, 48), ("m004", "2O"): (96, 0), ("m004", "2I"): (600, 0), ("m369", "2T"): (288, 96), ("m369", "2O"): (864, 96), ("m369", "2I"): (2400, 480), ("s639", "2T"): (168, 96), ("s639", "2O"): (192, 0), ("s639", "2I"): (1920, 960)}
    states = {"m004": ("LR", 1), "m369": ("LLRLR", -1), "s639": ("LLLRLR", -1)}; same = True
    for gname, (els, mul) in groups.items():
        T, inv, e = table(els, mul)
        for sname, (w, sg) in states.items():
            c = counts(T, inv, e, w, sg); same &= c == note[(sname, gname)]; print("Q1: %s -> %s (order %d): homomorphisms %d, surjections %d (the note: %d / %d)" % (sname, gname, len(els), *c, *note[(sname, gname)]))
    print("Q1: all eighteen counts equal the note's: %s" % same)
    x, y, z, s = sp.symbols("x y z s"); Ta = lambda p: (p[0], p[2], sp.expand(p[0] * p[2] - p[1])); Tb = lambda p: (p[2], p[1], sp.expand(p[1] * p[2] - p[0])); Tai = lambda p: (p[0], sp.expand(p[0] * p[1] - p[2]), p[1])
    kap = x ** 2 + y ** 2 + z ** 2 - x * y * z - 2
    def eqs(m):
        p = q = (x, y, z)
        for _ in range(m): p = Tb(p); q = Tai(q)
        return [sp.expand(u - v) for u, v in zip(p, q)]
    lines = {2: [(0, 0)], 3: [(-1, -1)], 4: [(0, 0)], 6: [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)]}; comps = {}
    for m in range(1, 7):
        E = eqs(m); lin = all(sp.degree(e, z) <= 1 for e in E if e != 0); A = [sp.expand(e.coeff(z, 1)) for e in E]; Bc = [sp.expand(-e.coeff(z, 0)) for e in E]
        minors = [sp.expand(A[i] * Bc[j] - A[j] * Bc[i]) for i, j in ((0, 1), (0, 2), (1, 2))]; G = functools.reduce(sp.gcd, [mn for mn in minors if mn != 0]); fac = [f for f, _ in sp.factor_list(G)[1]]
        vert = sp.groebner(A + Bc, x, y, order="lex"); curves = [f for f in fac if not all(sp.rem(sp.expand(a_), f, *sorted(f.free_symbols, key=str)) == 0 for a_ in A)]
        # the vertical lines over Q: the Q-irreducible pieces of the zero-dimensional ideal <A_i, B_i>
        gb = list(vert.exprs); uni = next((g for g in gb if g.free_symbols <= {y}), None); nlines_Q = 0
        if uni is not None and gb != [1]:
            for f, _ in sp.factor_list(uni)[1]:
                sub = sp.groebner(A + Bc + [f], x, y, order="lex"); ux = next(g for g in sub.exprs if g.free_symbols <= {y}); xs = [g for g in sub.exprs if x in g.free_symbols]
                al = sp.CRootOf(f, 0) if sp.degree(f, y) > 1 else sp.solve(f, y)[0]                               # the x-equation's factors over the field Q[y]/(f): the pieces over Q
                nlines_Q += len(sp.factor_list(sp.Poly(xs[0].subs(y, al), x, extension=[al]))[1]) if xs and sp.degree(xs[0], x) > 1 else 1
        ok_lines = all(all(sp.expand(e.subs({x: a_, y: b_})) == 0 for e in E) for (a_, b_) in lines.get(m, []))
        if m == 5: ok_lines = all(sp.rem(sp.expand(e.subs({x: s, y: s})), s ** 2 + s - 1, s) == 0 for e in E) and all(sp.rem(sp.expand(e.subs({x: s, y: -1 - s})), s ** 2 + s - 1, s) == 0 for e in E)
        comps[m] = (len(curves), nlines_Q); print("Q3: m = %d: linear in z: %s; curve factors of the minors' gcd over Q: %d (%s); components of the vertical part over Q: %d; the note's lines are fixed: %s" % (m, lin, len(curves), ", ".join(str(sp.Poly(f, x, y).total_degree()) for f in curves), nlines_Q, ok_lines))
    print("Q3: components over Q, m = 1 to 6: %s (the note: 1, 2, 2, 4, 3, 6)" % [sum(comps[m]) for m in range(1, 7)])
    E1, E2, E3 = eqs(1), eqs(2), eqs(3); tt = sp.symbols("t")
    c1 = all(sp.simplify(e.subs({x: tt, z: tt, y: tt / (tt - 1)})) == 0 for e in E1); c2 = all(sp.simplify(e.subs({y: 2 * x / z}).subs({x: sp.sqrt(z ** 2 / 2 + 2)})) == 0 for e in E2)
    proj = {m: [f for f, _ in sp.factor_list(functools.reduce(sp.gcd, [sp.expand(a_ * b_ - c_ * d_) for (a_, b_, c_, d_) in [(sp.expand(e1.coeff(z, 1)), sp.expand(-e2.coeff(z, 0)), sp.expand(e2.coeff(z, 1)), sp.expand(-e1.coeff(z, 0))) for e1, e2 in itertools.combinations(eqs(m), 2)] if sp.expand(a_ * b_ - c_ * d_) != 0]))[1]] for m in (1, 2, 3)}
    want = {1: x * y - x - y, 2: x ** 2 * y ** 2 - 2 * x ** 2 - 2 * y ** 2, 3: x ** 2 * y ** 2 - x ** 2 * y - x ** 2 - x * y ** 2 + x * y + x - y ** 2 + y}
    print("Q3: the m = 1 curve {x = z, yz = y + z} is fixed: %s; the m = 2 curve {x^2 = z^2/2 + 2, yz = 2x} is fixed: %s; the projections' factors contain the note's polynomials at m = 1, 2, 3: %s" % (c1, c2, [any(sp.expand(f - want[m]) == 0 or sp.expand(f + want[m]) == 0 for f in proj[m]) for m in (1, 2, 3)]))
    div4 = {}
    for m in range(1, 13):
        E = eqs(m); div4[m] = (all(sp.expand(e.subs({x: 0, z: 0})) == 0 for e in E), all(sp.expand(e.subs({y: 0, z: 0})) == 0 for e in E))
    print("Q3: the lines {x = z = 0} and {y = z = 0} are fixed at m = %s (the note: exactly when 4 divides m)" % [m for m in div4 if all(div4[m])]); print("    kappa is invariant under both maps: %s" % (sp.expand(kap.subs(dict(zip((x, y, z), Ta((x, y, z)))), simultaneous=True) - kap) == 0 and sp.expand(kap.subs(dict(zip((x, y, z), Tb((x, y, z)))), simultaneous=True) - kap) == 0))
    box = [m_ for m_ in itertools.product(range(-5, 6), repeat=4) if m_[0] * m_[3] - m_[1] * m_[2] == 1]; tr = collections.Counter(m_[0] + m_[3] for m_ in box)
    k = lambda p: p[0] ** 2 + p[1] ** 2 + p[2] ** 2 - p[0] * p[1] * p[2] - 2; pts = collections.Counter(k(p) for p in itertools.product(range(-10, 11), repeat=3))
    print("Q4: E18: %d matrices; traces symmetric: %s; trace 1: %d, trace 3: %d (28 with |tr - 2| = 1). E19: integer points in [-10, 10]^3 with kappa = -2: %d; with kappa = +2: %d (the note: 308; 12, 16; 17; 134)" % (len(box), all(tr[t_] == tr[-t_] for t_ in tr), tr[1], tr[3], pts[-2], pts[2]))
