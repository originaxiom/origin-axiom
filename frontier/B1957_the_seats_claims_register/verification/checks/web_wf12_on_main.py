"""B1957: the web seat's foundations card W-F12 (the doublets' class index at odd golden levels), on main's own code.
Data-free; exact over F_p.  At an odd level n (w(t) = -1): the characters are the fibre torsion's times the 2e-th roots
of unity for t; an extension character l is one with a class of H^1(G; l) that is not a coboundary; the doublets are
[[alpha, c beta], [0, beta]], beta = alpha/l, for every character alpha and every extension character l.
The class index: I(V) = n(V) - n(V* w), n the interior classes.  The gap: h^1(V) - h^1(V* w).
 C1  levels 3, 5 (and 7 when run with the argument 7): |T|, the characters, the extension characters and which they are,
     the doublets, how many have I != 0, how many have n(V) = n(V* w) = 1, and the census of the gap.
Level 7 has 48,778 doublets and takes several minutes; run as `web_wf12_on_main.py 7`."""
import functools, sys, pathlib, collections
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import web_wf4_on_main as W
A, B, T, LAM = W.A, W.B, W.T, W.LAM


def level(n, p, gen):
    S = W.setup(1, n, p, gen); rels, mu = S["rels"], S["mu"]; cusp = [mu, LAM]; inv = lambda x: pow(x, p - 2, p); w = {A: 1, B: 1, T: p - 1}
    ext = []
    for l in S["chars"]:
        V1 = W.ch1(l, p); F = [[V1.fox(r, g)[0][0] for g in (A, B, T)] for r in rels]; Z = W.nullspace(F, p, 3); cob = [(l[i] - 1) % p for i in range(3)]
        c = next((z for z in Z if (any(z) if not any(cob) else any((z[i] * cob[j] - z[j] * cob[i]) % p for i in range(3) for j in range(3)))), None)   # for the trivial character every non-zero cocycle is a class
        if c is not None: ext.append((l, c))
    kinds = collections.Counter("trivial" if l == (1, 1, 1) else ("fibre-non-trivial, l(mu) = -1" if (l[:2] != (1, 1) and W.val(l, mu, p) == p - 1) else "other") for l, _ in ext)
    nz = 0; both1 = 0; gaps = collections.Counter(); nd = 0
    for l, c in ext:
        li = tuple(inv(x) for x in l)
        for al in S["chars"]:
            be = tuple(a * b % p for a, b in zip(al, li)); V = W.Rep({g: [[al[g - 1], c[g - 1] * be[g - 1] % p], [0, be[g - 1]]] for g in (A, B, T)}, p)
            a = W.cohom(V, rels, cusp); d = W.cohom(V.dual(w), rels, cusp); nd += 1; nz += a[2] != d[2]; both1 += (a[2] == 1 and d[2] == 1); gaps[a[1] - d[1]] += 1
    return dict(tor=S["tor"], chars=len(S["chars"]), ext=len(ext), kinds=dict(kinds), doublets=nd, nz=nz, both1=both1, gaps=dict(sorted(gaps.items())))


if __name__ == "__main__":
    levels = [3, 5] + ([7] if "7" in sys.argv[1:] else [])
    p = 1276 * 240 + 1
    while not all(p % r for r in range(2, int(p ** 0.5) + 1)): p += 1276
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in {f for f in range(2, 3000) if (p - 1) % f == 0 and all(f % r for r in range(2, int(f ** 0.5) + 1))} | {(p - 1) // f for f in range(1, 3000) if (p - 1) % f == 0 and (p - 1) // f > 1 and all(((p - 1) // f) % r for r in range(2, int(((p - 1) // f) ** 0.5) + 1))}))
    for n in levels:
        r = level(n, p, gen)
        print("level %d (prime %d): |T| = %d; characters %d; extension characters %d (%s); doublets %d; class index non-zero on %d; n(V) = n(V* w) = 1 on %d; the gap's census %s" % (n, p, r["tor"], r["chars"], r["ext"], r["kinds"], r["doublets"], r["nz"], r["both1"], r["gaps"]))
