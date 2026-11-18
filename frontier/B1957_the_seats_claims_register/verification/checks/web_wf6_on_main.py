"""B1957: the web seat's foundations card W-F6 (the character gap law; the normaliser of the act's group), on main's code.
Data-free; exact.  Both theorems are proved by hand in the note; main read each step of both proofs (they hold) and
computes the checks here on its own code.
THE GAP LAW.  G = F x| <t>, F = <a, b>, t f t^-1 = phi(f); phi(lambda) = g lambda^s g^-1 with s = det of phi's
abelianisation; mu = g^-1 t.  For a character chi with fibre part theta != 1: h^1(G; chi) = [chi(mu) = s], and the class
is non-zero on lambda.  For theta = 1: h^1 = [chi = 1] unless chi(t) is an eigenvalue of the abelianisation mod p.
 G1  the law on every character (t-values the 2e-th roots of unity) of: the golden tick, levels 1 to 8; silver, 1 to 4;
     bronze, 1 to 3; a non-metallic monodromy of determinant +1 (trace 4), 1 to 3; and one the seat did not have, a
     non-metallic monodromy of determinant -1 (tau_1 tau_1 tau_2, levels 1 and 2).
 G2  the counts: at s = -1 the characters with gap +1 and with gap -1; at s = +1 the record's data, |T| - 1.
 GP  the law with -s in place of s (the seat's plant).
THE NORMALISER.  J = [[m, 1], [1, 0]], A = J^2, K = [[0, 1], [-1, 0]].
 N1  for m = 1 to 60 the integer solutions of a^2 + m a b - b^2 = +-1 in |a|, |b| <= 2000 are exactly the +-x^k there.
 N2  K J K^-1 = -J^-1 and K A K^-1 = A^-1; among +-J^k, |k| <= 20, only J and -J^-1 have trace m and determinant -1."""
import functools, sys, pathlib, itertools
from math import gcd
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import web_wf4_on_main as W
A, B, T, LAM, red, inv = W.A, W.B, W.T, W.LAM, W.red, W.inv


def apply(phi, w):
    out = []
    for g in w: out.extend(phi[abs(g)] if g > 0 else inv(phi[abs(g)]))
    return red(out)
compose = lambda f, g: {A: apply(f, g[A]), B: apply(f, g[B])}                    # g first, then f
power = lambda f, n: functools.reduce(compose, [f] * n)
tick = lambda m: {A: (A,) * m + (B,), B: (A,)}
Lf, Rf, Pf = {A: (A,), B: (A, B)}, {A: (A, B), B: (B,)}, {A: (B,), B: (A,)}


def conj_of_lambda(phi):
    """g and s with phi(lambda) = g lambda^s g^-1"""
    w = list(apply(phi, LAM)); g = []
    while len(w) >= 2 and w[0] == -w[-1]: g.append(w[0]); w = w[1:-1]
    w = tuple(w)
    for s in (1, -1):
        l = LAM if s == 1 else inv(LAM)
        for k in range(4):
            if l[k:] + l[:k] == w:                                              # w = q p with lambda^s = p q, q = l[k:]: w = q lambda^s q^-1
                gg = red(tuple(g) + l[k:]); assert red(gg + l + inv(gg)) == apply(phi, LAM); return gg, s
    raise RuntimeError("phi(lambda) is not a conjugate of lambda or its inverse")


def prime_for(e):
    q = 200000 - (200000 % (2 * e)) + 1
    while True:
        q += 2 * e
        if all(q % r for r in range(2, int(q ** 0.5) + 1)): return q


def case(phi):
    ab = lambda w: W.abel(w); M = [[ab(phi[A])[0], ab(phi[B])[0]], [ab(phi[A])[1], ab(phi[B])[1]]]; det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    tor = abs((M[0][0] - 1) * (M[1][1] - 1) - M[0][1] * M[1][0]); g1 = gcd(gcd(M[0][0] - 1, M[0][1]), gcd(M[1][0], M[1][1] - 1)); e = max(tor // g1, 1)
    g, s = conj_of_lambda(phi); assert s == det; p = prime_for(e); mu = red(inv(g) + (T,))
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in {f for f in range(2, int(p ** 0.5) + 2) if (p - 1) % f == 0 and all(f % r for r in range(2, int(f ** 0.5) + 1))} | {(p - 1) // f for f in range(1, 2000) if (p - 1) % f == 0 and all(((p - 1) // f) % r for r in range(2, int(((p - 1) // f) ** 0.5) + 1)) and (p - 1) // f > 1}))
    z = pow(gen, (p - 1) // (2 * e), p)
    fib = [(a1, a2) for a1 in range(e) for a2 in range(e) if (a1 * M[0][0] + a2 * M[1][0] - a1) % e == 0 and (a1 * M[0][1] + a2 * M[1][1] - a2) % e == 0]
    rels = [red((T, A, -T) + inv(phi[A])), red((T, B, -T) + inv(phi[B]))]; law = plant = True; nchar = 0; gp = gm = data = 0; eig_exc = 0
    sm = s % p
    for a1, a2 in fib:
        for j in range(2 * e):
            ch = (pow(z, 2 * a1, p), pow(z, 2 * a2, p), pow(z, j, p)); nchar += 1; V = W.ch1(ch, p); h0, h1 = W.cohom(V, rels); cm = W.val(ch, mu, p)
            if (a1, a2) != (0, 0):
                want = int(cm == sm); ok = h1 == want
                if h1:
                    F = [[V.fox(r, x)[0][0] for x in (A, B, T)] for r in rels]; Z = W.nullspace(F, p, 3); ok &= any(sum(V.fox(LAM, x)[0][0] * c[k] for k, x in enumerate((A, B, T))) % p for c in Z)
                law &= ok; plant &= h1 == int(cm == (-s) % p)
                gap = int(cm == sm) - int(cm == 1); data += int(s == 1 and cm == 1)
            else:
                t = ch[2]; is_eig = (t * t - (M[0][0] + M[1][1]) * t + det) % p == 0; eig_exc += is_eig
                law &= (h1 == int(ch == (1, 1, 1)) + (W.rank([[1]], p) * 0)) if not is_eig else True
                gap = (1 if (ch == (1, 1, 1) and s == -1) else (-1 if (ch == (1, 1, sm) and s == -1) else 0))
            # the gap itself, computed and not taken from the law
            w = {A: 1, B: 1, T: sm}; t1 = W.cohom(V.dual(w), rels)[1]; law &= (h1 - t1 == gap); gp += (h1 - t1) == 1; gm += (h1 - t1) == -1
    return dict(s=s, tor=tor, e=e, p=p, n=nchar, law=law, plant_passes=plant, gap_plus=gp, gap_minus=gm, data=data, eig=eig_exc, M=M)


if __name__ == "__main__":
    fams = [("golden", tick(1), 8), ("silver", tick(2), 4), ("bronze", tick(3), 3), ("R L L (trace 4, determinant +1, not metallic)", compose(Rf, compose(Lf, Lf)), 3),
            ("tau_1 tau_1 tau_2 (determinant -1, not metallic; not in the seat's run)", compose(tick(1), compose(tick(1), tick(2))), 2)]          # its level 3 has 234 x 468 characters: left out for time
    for name, phi, top in fams:
        rows = [case(power(phi, n)) for n in range(1, top + 1)]
        print("G1 %s, levels 1 to %d: abelianisation at level 1 %s; the law (h^1, the class on lambda, and the gap computed against V* w) on every character: %s (characters per level %s); the plant with -s passes at: %s" % (name, top, rows[0]["M"], all(r["law"] for r in rows), [r["n"] for r in rows], [i + 1 for i, r in enumerate(rows) if r["plant_passes"]]))
        print("   G2: |T| per level %s; determinant %s; characters with gap +1 / -1: %s; the record's data at s = +1: %s" % ([r["tor"] for r in rows], [r["s"] for r in rows], [(r["gap_plus"], r["gap_minus"]) for r in rows], [r["data"] if r["s"] == 1 else None for r in rows]))
    okN1 = True; okN2 = True; Km = np.array([[0, 1], [-1, 0]], dtype=object); rng = np.arange(-2000, 2001, dtype=np.int64); Aa, Bb = np.meshgrid(rng, rng, indexing="ij")
    for m in range(1, 61):
        N = Aa * Aa + m * Aa * Bb - Bb * Bb; sol = set(zip(Aa[np.abs(N) == 1].tolist(), Bb[np.abs(N) == 1].tolist()))
        units = set(); a, b = 1, 0
        while abs(a) <= 2000 and abs(b) <= 2000: units |= {(a, b), (-a, -b)}; a, b = b, a + m * b                  # x (a + b x) = b + (a + m b) x
        a, b = 1, 0
        while abs(a) <= 2000 and abs(b) <= 2000: units |= {(a, b), (-a, -b)}; a, b = b - m * a, a                  # x^-1 (a + b x) = (b - m a) + a x
        okN1 &= sol == units
        J = np.array([[m, 1], [1, 0]], dtype=object); Ji = np.array([[0, 1], [1, -m]], dtype=object); okN2 &= (Km.dot(J).dot(-Km) == -Ji).all() and (Km.dot(J.dot(J)).dot(-Km) == Ji.dot(Ji)).all()
        hits = []; P = np.eye(2, dtype=object); Q = np.eye(2, dtype=object)
        for k in range(0, 21):
            for sg in (1, -1):
                for label, X in ((k, P), (-k, Q)):
                    Y = sg * X
                    if Y[0, 0] + Y[1, 1] == m and Y[0, 0] * Y[1, 1] - Y[0, 1] * Y[1, 0] == -1: hits.append((sg, label))
            P = P.dot(J); Q = Q.dot(Ji)
        okN2 &= sorted(set(hits)) == [(-1, -1), (1, 1)]
    print("N1: m = 1 to 60: the solutions of a^2 + m a b - b^2 = +-1 in the box are exactly the +-x^k there: %s | N2: K J K^-1 = -J^-1, K A K^-1 = A^-1, and among +-J^k only J and -J^-1 have trace m and determinant -1: %s" % (okN1, okN2))
