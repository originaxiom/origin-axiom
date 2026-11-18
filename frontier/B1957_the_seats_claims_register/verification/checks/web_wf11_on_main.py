"""B1957: the web seat's foundations card W-F11 (five distinctions carry the frame's matter), on main's own code.
Data-free; exact over F_p.  W_n = n free involutions; the records E_n are free on x_i = s_i s_(i+1); the history
H_n = h_1 h_2^-1 h_3 ... (Hurwitz moves, W-F8) acts on the records by an automorphism phi that fixes the scar
lambda = p^2, p = s_1 ... s_n (n odd).  Level k: G = E_n x| <t>, t x t^-1 = phi^k(x); the cusp is <t, lambda>, mu = t.
The recipe: l a non-trivial character of the fibre torsion with l(t) = 1 and a class c with c(lambda) = 1;
V(l, alpha) = [[alpha, c beta], [0, beta]], beta = alpha/l non-trivial; I(V) = n(V) - n(V*), n the interior classes.
 V1  phi fixes lambda as a reduced word; lambda in the x_i at n = 5.
 V2  the fibre torsion at levels 1 and 2, n = 3 (the control) and n = 5.
 V3  at level 2: the record characters, each with h^1 = 1 and a class non-zero on lambda.
 V4  the sector modules and the numbers with I = +1, -1, 0 and |I| >= 2."""
import functools, sys, pathlib, itertools
import sympy as sp
print = functools.partial(print, flush=True)
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); import web_wf4_on_main as W, web_wf8_on_main as H8


def to_x(w, n):
    """an even word in the involutions s_1..s_n as a reduced word in x_1..x_(n-1) (letters +-i)"""
    out = []
    for a, b in zip(w[0::2], w[1::2]):
        if a < b: out += list(range(a, b))
        elif a > b: out += [-k for k in range(a - 1, b - 1, -1)]
    return W.red(tuple(out))
def apply(phi, w):
    out = []
    for g in w: out.extend(phi[abs(g)] if g > 0 else W.inv(phi[abs(g)]))
    return W.red(out)


def world(n, level, p):
    Hn = functools.reduce(H8.comp, [H8.hurwitz(i, n, inverse=(i % 2 == 0)) for i in range(1, n)])
    phi1 = {i: to_x(H8.img(Hn, (i, i + 1)), n) for i in range(1, n)}; phi = phi1
    for _ in range(level - 1): phi = {i: apply(phi, phi1[i]) for i in phi1}          # phi^level
    pw = tuple(range(1, n + 1)); lam = to_x(pw + pw, n); fixes = apply(phi, lam) == lam
    r = n - 1; t = n; ab = lambda w: [sum((1 if g > 0 else -1) for g in w if abs(g) == i) for i in range(1, n)]
    M = sp.Matrix([ab(phi[i]) for i in range(1, n)]).T; tor = abs((M - sp.eye(r)).det())
    rels = [W.red((t, i, -t) + W.inv(phi[i])) for i in range(1, n)]
    if tor <= 1: return dict(tor=tor, fixes=fixes, lam=lam, M=M)
    # the characters of the fibre torsion: exponent vectors a mod tor with a (M - 1) = 0 mod tor (the torsion is cyclic here: checked by the count)
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in {f for f in range(2, 3000) if (p - 1) % f == 0 and all(f % rr for rr in range(2, int(f ** 0.5) + 1))} | {(p - 1) // f for f in range(1, 3000) if (p - 1) % f == 0 and (p - 1) // f > 1 and all(((p - 1) // f) % rr for rr in range(2, int(((p - 1) // f) ** 0.5) + 1))}))
    z = pow(gen, (p - 1) // int(tor), p); Mi = (M - sp.eye(r)); T_ = int(tor)
    sols = [a for a in itertools.product(range(T_), repeat=r) if all(int(sum(a[i] * Mi[i, j] for i in range(r))) % T_ == 0 for j in range(r))] if T_ ** r <= 10 ** 6 else None
    chars = [tuple(pow(z, e, p) for e in a) + (1,) for a in sols if any(a)]              # l(t) = 1
    gens = list(range(1, n + 1)); mk1 = lambda ch: W.Rep({g: [[ch[g - 1]]] for g in gens}, p); cusp = [(t,), lam]; inv = lambda x: pow(x, p - 2, p)
    good = 0; mods = 0; Ic = {1: 0, -1: 0, 0: 0, "big": 0}; cmul = lambda x, y: tuple(a * b % p for a, b in zip(x, y)); cinv = lambda x: tuple(inv(a) for a in x)
    for l in chars:
        V1 = mk1(l); F = [[V1.fox(rr, g)[0][0] for g in gens] for rr in rels]; Z = W.nullspace(F, p, n); lamv = lambda c: sum(V1.fox(lam, g)[0][0] * c[k] for k, g in enumerate(gens)) % p
        h1 = W.cohom(V1, rels)[1]; c = next((zz for zz in Z if lamv(zz)), None)
        if h1 == 1 and c is not None: good += 1
        if c is None: continue
        s = inv(lamv(c)); c = [x * s % p for x in c]
        for al in chars:
            if al == l: continue
            be = cmul(al, cinv(l)); V = W.Rep({g: [[al[g - 1], c[g - 1] * be[g - 1] % p], [0, be[g - 1]]] for g in gens}, p); mods += 1
            I = W.cohom(V, rels, cusp)[2] - W.cohom(V.dual(), rels, cusp)[2]; Ic[I if I in (1, -1, 0) else "big"] += 1
    return dict(tor=tor, fixes=fixes, lam=lam, M=M, nsol=len(sols), chars=len(chars), good=good, mods=mods, I=Ic)


if __name__ == "__main__":
    p = 145 * 2000 + 1
    while not all(p % r for r in range(2, int(p ** 0.5) + 1)): p += 145
    for n in (3, 5):
        w1, w2 = world(n, 1, p), world(n, 2, p)
        print("n = %d: phi fixes the scar as a reduced word: %s; the scar in the x_i: %s; phi on H_1: %s" % (n, w1["fixes"] and w2["fixes"], list(w1["lam"]), w1["M"].tolist()))
        print("   level 1: fibre torsion %s; level 2: fibre torsion %s (%d solutions of a (M - 1) = 0: %s); record characters %d, of which with h^1 = 1 and a class non-zero on lambda: %d; sector modules %d; I = +1 / -1 / 0 / |I| >= 2: %d / %d / %d / %d (prime %d)" % (
            w1["tor"], w2["tor"], w2["nsol"], "cyclic" if w2["nsol"] == w2["tor"] else "not cyclic", w2["chars"], w2["good"], w2["mods"], w2["I"][1], w2["I"][-1], w2["I"][0], w2["I"]["big"], p))
