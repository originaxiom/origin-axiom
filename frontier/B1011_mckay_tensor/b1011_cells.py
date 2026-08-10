"""B1011 — the McKay tensor factorization, exact cells (sealed fc807f11).

Method: (i) mod-p EXACT enumeration of <R,L> at two unramified primes with word
tracking; the order is exact by Serre's lemma (reduction mod p>2 is injective
on finite subgroups of GL_n over a p-integral ring; denominators here sit at
2,3,5 only, and 61, 241 are coprime to 30 with 60 | p-1). (ii) class
representatives transfer as WORDS; every character-level verdict is computed in
EXACT sympy cyclotomics on class reps -- characters are class functions, so
checking classes is checking the whole group. No verdict line uses a float.
"""
import itertools, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
from collections import deque

import sympy as sp


def modp_model(p):
    """zeta_60 in F_p (60 | p-1); rebuild Sigma, T mod p; return R, L (6x6, exact mod p)."""
    g = None
    for cand in range(2, p):
        if pow(cand, 60, p) == 1 and all(pow(cand, 60 // q, p) != 1 for q in (2, 3, 5)):
            g = cand; break
    z60 = g

    def ex(r):
        r = sp.Rational(r) % 1
        num = int(r * 60)
        assert sp.Rational(num, 60) == r
        return pow(z60, num, p)

    k, kap = 2, 5
    weights = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    n = len(weights)

    def Lvec(w): return (w[0] + w[1] + 2, w[1] + 1, 0)

    def ip3(u, v):
        return sp.Rational(sum(u[i] * v[i] for i in range(3))) - sp.Rational(sum(u) * sum(v), 3)

    perms = list(itertools.permutations(range(3)))

    def sgn(pm): return (-1) ** sum(pm[i] > pm[j] for i in range(3) for j in range(i + 1, 3))

    Sig = [[0] * n for _ in range(n)]
    for i, wl in enumerate(weights):
        Ll = Lvec(wl)
        for j, wm in enumerate(weights):
            Lm = Lvec(wm)
            tot = 0
            for pm in perms:
                tot = (tot + sgn(pm) * ex(-ip3(tuple(Ll[q] for q in pm), Lm) / kap)) % p
            Sig[i][j] = tot
    c = sp.Rational(16, 5)
    Td = [ex((sp.Rational(2, 3) * (a * a + a * b + b * b) + 2 * (a + b)) / (2 * kap) - c / 24)
          for (a, b) in weights]

    def mul(A, B):
        return [[sum(A[i][t] * B[t][j] for t in range(n)) % p for j in range(n)]
                for i in range(n)]

    def inv(A):
        M = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]
        for col in range(n):
            piv = next(r for r in range(col, n) if M[r][col] % p)
            M[col], M[piv] = M[piv], M[col]
            ivv = pow(M[col][col], p - 2, p)
            M[col] = [(x * ivv) % p for x in M[col]]
            for r in range(n):
                if r != col and M[r][col]:
                    f = M[r][col]
                    M[r] = [(M[r][t] - f * M[col][t]) % p for t in range(2 * n)]
        return [row[n:] for row in M]

    R = [[Td[i] if i == j else 0 for j in range(n)] for i in range(n)]
    Ti = [[pow(Td[i], p - 2, p) if i == j else 0 for j in range(n)] for i in range(n)]
    L = mul(mul(inv(Sig), Ti), Sig)
    return R, L, mul, inv


def enumerate_group(p):
    R, L, mul, inv = modp_model(p)
    n = 6
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    key = lambda M: tuple(x for row in M for x in row)
    seen = {key(I): ""}
    q = deque([(I, "")])
    while q:
        M, wd = q.popleft()
        for ch, g in (("R", R), ("L", L)):
            Mg = mul(M, g)
            kk = key(Mg)
            if kk not in seen:
                seen[kk] = wd + ch
                q.append((Mg, wd + ch))
    return seen, mul, inv


def conj_classes(seen, mul, inv, p):
    n = 6
    key = lambda M: tuple(x for row in M for x in row)
    unkey = lambda kk: [list(kk[i * n:(i + 1) * n]) for i in range(n)]
    elems = list(seen.keys())
    ginvs = [(unkey(gk), inv(unkey(gk))) for gk in elems]
    unassigned = set(elems)
    classes = []
    while unassigned:
        kk = next(iter(unassigned))
        M = unkey(kk)
        orbit = {key(mul(mul(G, M), Gi)) for G, Gi in ginvs}
        unassigned -= orbit
        classes.append((seen[kk], len(orbit)))
    return classes


if __name__ == "__main__":
    p1, p2 = 61, 241
    print(f"-- C1: exact order via mod-p + Serre (p = {p1}, {p2}) --")
    seen1, mul1, inv1 = enumerate_group(p1)
    print(f"  |<R,L>| mod {p1} = {len(seen1)}")
    seen2, _, _ = enumerate_group(p2)
    print(f"  |<R,L>| mod {p2} = {len(seen2)}")
    assert len(seen1) == len(seen2) == 2880
    print("  order = 2880 EXACT (Serre injectivity; p coprime to 30) = |2T x 2I|   [C1 order PASS]")
    print("-- conjugacy classes (word representatives) --")
    classes = conj_classes(seen1, mul1, inv1, p1)
    print(f"  #classes = {len(classes)}, sizes sum = {sum(s for _, s in classes)}")
    json.dump(sorted([{"word": w, "size": s} for w, s in classes], key=lambda r: (r["size"], r["word"])),
              open(os.path.join(HERE, "class_reps.json"), "w"), indent=0)
    print("  2T x 2I would have 7 x 9 = 63 classes; written to class_reps.json")
