"""Main's own computation (no code of the web seat's is used): on the tick's bundles G_n = <a, b, t | t x t^-1 = sigma^n(x)>,
sigma: a -> ab, b -> a (abelianisation LP, det -1), level n = 1..8, can a 1-cocycle over a fibre-torsion character be
non-zero on the scar lambda = [a, b]?

EXPECTATION, written before the run (main's proof): at a level n, t lambda t^-1 = g lambda^((-1)^n) g^-1 for a word g,
and mu = g^-1 t gives mu lambda mu^-1 = lambda^((-1)^n). For a character l with l(mu) = 1 and a cocycle c
(c(xy) = c(x) + l(x) c(y)): c(mu lambda mu^-1) = c(lambda), while c(lambda^-1) = -c(lambda) (l(lambda) = 1). So at odd n,
2 c(lambda) = 0 and c(lambda) = 0 for every such l and c (p odd): no class can be normalised by c(lambda) = 1, so no
sector module V(l, alpha) exists. At even n there is no constraint, and at the levels where the web seat found sector
modules (4, 6, 8) some l must carry a cocycle with c(lambda) != 0.

Method: Fox calculus over F_p (p = 1 mod the exponents of the fibre torsion), characters enumerated through a root of
unity of the torsion's exponent; Z^1 as the null space of the relations' Fox matrix; c(lambda) as a linear functional
on it. A control: the same computation with l(mu) = -1 must find c(lambda) != 0 at an odd level, so that the zero is the
meridian's doing and not the code's. [The first design of the control took t's value from 1 to 40, missing the one value
the proof says matters (by the same algebra, (l(t) + l(g)) c(lambda) = 0 at odd n, so c(lambda) can be non-zero only at
l(mu) = -1); it found nothing, as it had to; disclosed, and replaced before the result was used.]"""
import json, pathlib
from math import gcd
HERE = pathlib.Path(__file__).resolve().parent

A, B, T = 1, 2, 3


def red(w):
    out = []
    for g in w:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return tuple(out)


def inv(w):
    return tuple(-g for g in reversed(w))


SIG = {A: (A, B), B: (A,)}


def sigma(w):
    out = []
    for g in w:
        out.extend(SIG[g] if g > 0 else inv(SIG[-g]))
    return red(out)


def sigma_n(w, n):
    for _ in range(n):
        w = sigma(w)
    return w


LAM = (A, B, -A, -B)


def find_g(n):
    """g and e with sigma^n(lambda) = g lambda^e g^-1, by the recursion g_1 = a, g_(k+1) = sigma(g_k) a, then checked"""
    target = sigma_n(LAM, n)
    g = (A,)
    for _ in range(n - 1):
        g = red(sigma(g) + (A,))
    for e in (1, -1):
        lam_e = LAM if e == 1 else inv(LAM)
        if red(g + lam_e + inv(g)) == target:
            return g, e
    raise RuntimeError("no conjugator found at level %d" % n)


def abel(w):
    v = [0, 0, 0]
    for g in w:
        v[abs(g) - 1] += 1 if g > 0 else -1
    return v


def char_val(ch, w, p):
    v = 1
    for g in w:
        x = ch[abs(g)]
        v = v * (x if g > 0 else pow(x, p - 2, p)) % p
    return v


def fox(w, gen, ch, p):
    """the Fox derivative d w / d gen, evaluated by the character ch, in F_p"""
    s, pre = 0, 1
    for g in w:
        x = ch[abs(g)]
        if g == gen:
            s = (s + pre) % p
        elif g == -gen:
            s = (s - pre * pow(x, p - 2, p)) % p
        pre = pre * (x if g > 0 else pow(x, p - 2, p)) % p
    return s


def nullspace(M, p, ncols):
    M = [list(r) for r in M]; piv = []; r = 0
    for c in range(ncols):
        k = next((i for i in range(r, len(M)) if M[i][c] % p), None)
        if k is None:
            continue
        M[r], M[k] = M[k], M[r]; iv = pow(M[r][c], p - 2, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]; M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        piv.append(c); r += 1
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * ncols; v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-M[i][f]) % p
        basis.append(v)
    return basis


def isprime(n):
    return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))


def torsion_exponent(n):
    M = [[1, 0], [0, 1]]
    for _ in range(n):
        M = [[M[0][0] + M[0][1], M[0][0]], [M[1][0] + M[1][1], M[1][0]]]   # columns: a -> a + b, b -> a
    a, b, c, d = M[0][0] - 1, M[0][1], M[1][0], M[1][1] - 1
    d1 = gcd(gcd(abs(a), abs(b)), gcd(abs(c), abs(d)))
    return abs(a * d - b * c) // d1 if d1 else 0, abs(a * d - b * c)


def run(n, p, keep_mu=True):
    g, e = find_g(n)
    ex, order = torsion_exponent(n)
    rels = [red((T, A, -T) + inv(sigma_n((A,), n))), red((T, B, -T) + inv(sigma_n((B,), n)))]
    if ex <= 1:
        return {"n": n, "e": e, "characters": 0, "with_c_lambda_nonzero": 0}
    z = next(x for x in range(2, p) if pow(x, (p - 1) // ex, p) != 1 and all(pow(pow(x, (p - 1) // ex, p), ex // q, p) != 1 for q in range(2, ex + 1) if ex % q == 0 and isprime(q)))
    zeta = pow(z, (p - 1) // ex, p)
    chars, nonzero = 0, 0
    for i in range(ex):
        for j in range(ex):
            x, y = pow(zeta, i, p), pow(zeta, j, p)
            if (x, y) == (1, 1):
                continue
            ch = {A: x, B: y, T: 1}
            if char_val(ch, sigma_n((A,), n), p) != x or char_val(ch, sigma_n((B,), n), p) != y:
                continue
            gv = char_val({A: x, B: y, T: 1}, g, p)
            ts = [gv] if keep_mu else [(-gv) % p]          # the control: l(mu) = -1, the character twisted by the orientation
            for tv in ts:
                ch = {A: x, B: y, T: tv}
                chars += 1
                F = [[fox(r, gen, ch, p) for gen in (A, B, T)] for r in rels]
                Z = nullspace(F, p, 3)
                lam_fun = [fox(LAM, gen, ch, p) for gen in (A, B, T)]
                if any(sum(a * b for a, b in zip(lam_fun, v)) % p for v in Z):
                    nonzero += 1
    return {"n": n, "e": e, "characters": chars, "with_c_lambda_nonzero": nonzero}


if __name__ == "__main__":
    L = 1
    for n in range(1, 9):
        L = L * torsion_exponent(n)[0] // gcd(L, torsion_exponent(n)[0]) if torsion_exponent(n)[0] > 1 else L
    p = next(q for q in range(L + 1, 10 ** 9, L) if isprime(q))
    out = {"p": p, "levels": [], "control_odd_without_mu": []}
    print("p = %d (1 mod the exponents' lcm %d)" % (p, L), flush=True)
    for n in range(1, 9):
        r = run(n, p)
        out["levels"].append(r)
        print("level %d: sigma^n(lambda) = g lambda^%+d g^-1 (orientable %s); fibre-torsion characters trivial on mu: %d; with a cocycle non-zero on lambda: %d"
              % (n, r["e"], r["e"] == 1, r["characters"], r["with_c_lambda_nonzero"]), flush=True)
    for n in (3, 5):
        r = run(n, p, keep_mu=False)
        out["control_odd_without_mu"].append(r)
        print("control, level %d with l(mu) = -1 (the orientation-twisted characters): characters %d, with c(lambda) != 0: %d" % (n, r["characters"], r["with_c_lambda_nonzero"]), flush=True)
    odd_zero = all(r["with_c_lambda_nonzero"] == 0 for r in out["levels"] if r["n"] % 2)
    even_some = all(r["with_c_lambda_nonzero"] > 0 for r in out["levels"] if r["n"] in (4, 6, 8))
    control = any(r["with_c_lambda_nonzero"] > 0 for r in out["control_odd_without_mu"])
    print("EXPECTATION: odd levels all zero: %s; levels 4, 6, 8 some non-zero: %s; the control finds non-zero: %s" % (odd_zero, even_some, control))
    out.update(odd_zero=odd_zero, even_some=even_some, control=control)
    (HERE / "odd_ticks_no_modules.json").write_text(json.dumps(out, indent=1))
