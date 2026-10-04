#!/usr/bin/env python3
"""The golden covers dossier (2026-10-04): design-time STRUCTURE only -- group theory of the fibre group F2 = <a, b> and the
states' monodromy. No homology rank and no twisted cohomology of any cover is computed here.

Reproduces every computed number in DOSSIER_golden_covers_and_room_for_three.md (section 1):
  1. the kernels of F2 -> SL(2,5) = 2I (generating pairs up to simultaneous GL(2,5) conjugation; Aut 2I = PGL(2,5)) and of
     F2 -> A5 (Hall's 19), and how each state's monodromy (sm:B1527's presentation, through sm:B1538's punct_covers) permutes them;
  2. at the fixed kernels: the order of the puncture loop [a,b] in SL(2,5), and whether the induced automorphism is inner or
     outer (conjugation by g in GL(2,5) with det g a square mod 5, or not);
  3. the fibre-direction A5 covers over the fixed kernels (cosets H\\Gamma <-> A5: a, b act by right multiplication, t by
     x -> ubar^-1 betabar^-1(x)), their equivalence classes, cusp orbit sizes, and the order of the automorphism tau induces
     on 2I;
  4. the comparison with the golden holonomy reduced mod 2 (Z[omega]/2 = F4, PSL(2,4) = A5; sm:B1530's exact Eisenstein
     holonomy), and the orders of the mod-2 images.

    python3 gc_icosian.py      (a few seconds; prints the record kept as gc_icosian_run.txt)"""
import itertools
import sys
import warnings
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier" / "B1538_the_puncture_characters" / "verification"))
sys.path.insert(0, str(ROOT / "frontier" / "B1530_the_interior_extensions" / "verification"))
import punct_covers as F          # noqa: E402  (sm:B1538's states: punct_covers.State, the monodromy images)

P = 5
I = (1, 0, 0, 1)
MINUS = (4, 0, 0, 4)


# ------------------------------------------------------------------------------------------------ SL(2,5), GL(2,5)
def mul(X, Y):
    return ((X[0] * Y[0] + X[1] * Y[2]) % P, (X[0] * Y[1] + X[1] * Y[3]) % P,
            (X[2] * Y[0] + X[3] * Y[2]) % P, (X[2] * Y[1] + X[3] * Y[3]) % P)


def inv(X):
    di = pow((X[0] * X[3] - X[1] * X[2]) % P, P - 2, P)
    return ((X[3] * di) % P, (-X[1] * di) % P, (-X[2] * di) % P, (X[0] * di) % P)


def order(X):
    k, Y = 1, X
    while Y != I:
        Y, k = mul(Y, X), k + 1
    return k


ALL = list(itertools.product(range(P), repeat=4))
SL = [m for m in ALL if (m[0] * m[3] - m[1] * m[2]) % P == 1]
GL = [m for m in ALL if (m[0] * m[3] - m[1] * m[2]) % P != 0]
assert len(SL) == 120 and len(GL) == 480


def ev(w, x, y):
    out = I
    for ch in w:
        out = mul(out, {"a": x, "b": y, "A": inv(x), "B": inv(y)}[ch])
    return out


def generated_order(gens):
    seen, fr = {I}, [I]
    while fr:
        nxt = []
        for g in fr:
            for h in gens:
                k = mul(g, h)
                if k not in seen:
                    seen.add(k)
                    nxt.append(k)
        fr = nxt
    return len(seen)


def proj(X):                                         # the A5 = PSL(2,5) image
    return min(X, mul(MINUS, X))


def kernels():
    """{canonical pair: orbit size} and the canonical form of every generating pair"""
    pairs = [(x, y) for x in SL for y in SL if generated_order([x, y]) == 120]
    canon, classes = {}, {}
    for (x, y) in pairs:
        if (x, y) in canon:
            continue
        orbit = {(mul(mul(g, x), inv(g)), mul(mul(g, y), inv(g))) for g in GL}
        rep = min(orbit)
        for o in orbit:
            canon[o] = rep
        classes[rep] = len(orbit)
    return pairs, canon, classes


def a5_classes(canon, classes):
    a5 = {}
    for (x, y) in classes:
        best = min(canon[(xx, yy)] for xx in (x, mul(MINUS, x)) for yy in (y, mul(MINUS, y)))
        a5.setdefault(best, []).append((x, y))
    return a5


def monodromy_permutation(st, canon, classes):
    return {r: canon[(ev(st.img["a"], *r), ev(st.img["b"], *r))] for r in classes}


def cycle_type(perm):
    seen, out = set(), []
    for r in perm:
        if r in seen:
            continue
        n, c = 0, r
        while c not in seen:
            seen.add(c)
            c, n = perm[c], n + 1
        out.append(n)
    return sorted(out)


# ------------------------------------------------------------------------------------------------ the A5 covers
def conjugator(x, y, nx, ny):
    return next(g for g in GL if mul(mul(g, x), inv(g)) == nx and mul(mul(g, y), inv(g)) == ny)


def word_perm(perm, w, n=60):
    out = list(range(n))
    invs = {g: [0] * n for g in perm}
    for g, p in perm.items():
        for i, j in enumerate(p):
            invs[g][j] = i
    for ch in w:
        q = perm[ch] if ch.islower() else invs[ch.lower()]
        out = [q[out[i]] for i in range(n)]
    return out


def covers_over(st, x, y, g):
    """the 60 twists ubar of the A5 cover over the fixed kernel (x, y), reduced to equivalence classes"""
    A5 = sorted({proj(e) for e in SL})
    idx = {e: i for i, e in enumerate(A5)}
    beta = {e: proj(mul(mul(g, e), inv(g))) for e in A5}
    beta_inv = {v: k for k, v in beta.items()}
    reps = []
    for ub in A5:
        perm = {"a": [idx[proj(mul(e, x))] for e in A5], "b": [idx[proj(mul(e, y))] for e in A5],
                "t": [idx[proj(mul(inv(ub), beta_inv[e]))] for e in A5]}
        for gname in "ab":                                    # Gamma's relations t g t^-1 = phi(g)
            assert word_perm(perm, "t" + gname + "T") == word_perm(perm, st.img[gname])
        same = False
        for r in reps:                                        # equivalent iff left multiplication by some h intertwines t
            for h in A5:
                sig = [idx[proj(mul(h, e))] for e in A5]
                if all(sig[perm["t"][i]] == r["perm"]["t"][sig[i]] for i in range(60)):
                    same = True
                    break
            if same:
                break
        if not same:
            reps.append({"ubar": ub, "perm": perm})
    for r in reps:
        pl, pt = word_perm(r["perm"], "abAB"), word_perm(r["perm"], st.tprime)
        seen, sizes = set(), []
        for s in range(60):
            if s in seen:
                continue
            orb, fr = {s}, [s]
            while fr:
                nxt = []
                for i in fr:
                    for p in (pl, pt):
                        if p[i] not in orb:
                            orb.add(p[i])
                            nxt.append(p[i])
                fr = nxt
            seen |= orb
            sizes.append(len(orb))
        r["cusps"] = sorted(sizes)
        ub2 = next(e for e in SL if proj(e) == r["ubar"])
        c = mul(g, ub2)                                       # tau acts on 2I by e -> c e c^-1
        det = (c[0] * c[3] - c[1] * c[2]) % P
        k, X = 1, c
        while not (X[1] == 0 and X[2] == 0 and X[0] == X[3]):
            X, k = mul(X, c), k + 1
        r["tau on 2I"] = {"det": det, "outer": det not in (1, 4), "order in PGL(2,5)": k}
    return reps


# ------------------------------------------------------------------------------------------------ mod 2
def _f4(x):
    """c0 + c4 zeta_6 in Q(zeta_24) (coordinates 0 and 4 only), zeta_6 = 1 + omega, reduced mod 2 into F4 = F2[omega]"""
    assert all(x.c[k] == 0 for k in (1, 2, 3, 5, 6, 7))
    c0, c4 = Fraction(int(x.c[0]), x.d), Fraction(int(x.c[4]), x.d)
    p, q = c0 + c4, c4
    assert p.denominator % 2 == 1 and q.denominator % 2 == 1
    return (p.numerator % 2, q.numerator % 2)


def _m4(x, y):
    a, b = x
    c, d = y
    return ((a * c + b * d) % 2, (a * d + b * c + b * d) % 2)


def _a4(x, y):
    return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)


def _mm4(X, Y):
    return (_a4(_m4(X[0], Y[0]), _m4(X[1], Y[2])), _a4(_m4(X[0], Y[1]), _m4(X[1], Y[3])),
            _a4(_m4(X[2], Y[0]), _m4(X[3], Y[2])), _a4(_m4(X[2], Y[1]), _m4(X[3], Y[3])))


def _n4(X):
    inv4 = {(1, 0): (1, 0), (0, 1): (1, 1), (1, 1): (0, 1)}
    s = inv4[next(e for e in X if e != (0, 0))]
    return tuple(_m4(s, v) for v in X)


def mod2_holonomy(sw):
    import exact_states as ES                                  # sm:B1530's exact Eisenstein holonomy
    h = ES.eisenstein_sl2(sw[0], sw[1:])
    return {g: _n4(tuple(_f4(h[g][i][j]) for i in range(2) for j in range(2))) for g in "abt"}


def closure(gens, mulf, one):
    seen, fr = {one}, [one]
    while fr:
        nxt = []
        for u in fr:
            for g in gens:
                k = mulf(u, g)
                if k not in seen:
                    seen.add(k)
                    nxt.append(k)
        fr = nxt
    return len(seen)


def main():
    pairs, canon, classes = kernels()
    a5 = a5_classes(canon, classes)
    print(f"generating pairs of SL(2,5): {len(pairs)}; kernels F2 -> 2I: {len(classes)} (orbit sizes "
          f"{sorted(set(classes.values()))}); kernels F2 -> A5: {len(a5)}, lifts each {sorted({len(v) for v in a5.values()})}")
    one4 = _n4(((1, 0), (0, 0), (0, 0), (1, 0)))
    for sw in ("+LR", "-LR", "+LLRR", "-LLRR"):
        st = F.State(sw)
        perm = monodromy_permutation(st, canon, classes)
        fixed = [r for r in classes if perm[r] == r]
        print(f"\n{sw}: 2I-kernels fixed {len(fixed)}; cycle type {cycle_type(perm)}")
        for kx, (x, y) in enumerate(fixed):
            nx, ny = ev(st.img["a"], x, y), ev(st.img["b"], x, y)
            g = conjugator(x, y, nx, ny)
            det = (g[0] * g[3] - g[1] * g[2]) % P
            comm = mul(mul(x, y), mul(inv(x), inv(y)))
            print(f"  kernel {kx}: [a,b] has order {order(comm)} in SL(2,5); phi acts by conjugation with det {det} "
                  f"({'outer' if det not in (1, 4) else 'inner'})")
            for r in covers_over(st, x, y, g):
                t2 = r["tau on 2I"]
                print(f"    cover: cusp orbit sizes {r['cusps']}; tau on 2I: det {t2['det']} "
                      f"({'outer' if t2['outer'] else 'inner'}), order {t2['order in PGL(2,5)']}")
            if sw in ("+LR", "-LR"):
                red = mod2_holonomy(sw)
                A = (red["a"], proj(x))
                B = (red["b"], proj(y))
                n = closure([A, B], lambda u, v: (_n4(_mm4(u[0], v[0])), proj(mul(u[1], v[1]))), (one4, proj(I)))
                print(f"    with the holonomy mod 2: <(a mod 2, a), (b mod 2, b)> has order {n} "
                      f"({'the same kernel' if n == 60 else 'a different kernel'})")
        if sw in ("+LR", "-LR"):
            red = mod2_holonomy(sw)
            fib = closure([red["a"], red["b"]], lambda u, v: _n4(_mm4(u, v)), one4)
            whole = closure([red["a"], red["b"], red["t"]], lambda u, v: _n4(_mm4(u, v)), one4)
            print(f"  mod-2 image (PGL(2,4)): fibre <a,b> order {fib}; whole group <a,b,t> order {whole}")


if __name__ == "__main__":
    main()
