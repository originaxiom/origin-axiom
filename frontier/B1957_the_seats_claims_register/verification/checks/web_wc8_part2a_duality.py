"""B1957: the web seat's W-C8 part 2a, its post hoc 1 (twisted duality on the tick's levels), on main's own code.
Data-free; exact over F_p.  For a module V of G_n and V' = V* w (w the orientation character):
    h^2(G; V) = h^1(G, P; V'),
with h^2 = h^1 - h^0 (the presentation's Euler characteristic is 0) and h^1(G, P; V') = n(V') + h^0(P; V') - h^0(G; V')
(the pair's exact sequence; n = interior classes, P = <mu, lambda>).
 H1  on every character at levels 3 to 8 (t-values the 2e-th roots of unity): the twisted identity holds; with w left
     out it fails on some character at every odd level and cannot differ at the even ones.
 E2  the fibre torsion at levels 1 to 8."""
import functools, sys, pathlib
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import web_wf4_on_main as W, web_wf19_on_main as N19
A, B, T, LAM = W.A, W.B, W.T, W.LAM

if __name__ == "__main__":
    tors = []
    for n in range(1, 9):
        e = {1: 1, 2: 1, 3: 2, 4: 5, 5: 11, 6: 4, 7: 29, 8: 15}[n]; p = 300000 - (300000 % (2 * e)) + 1
        while True:
            p += 2 * e
            if all(p % r for r in range(2, int(p ** 0.5) + 1)): break
        gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in {f for f in range(2, 3000) if (p - 1) % f == 0 and all(f % r for r in range(2, int(f ** 0.5) + 1))} | {(p - 1) // f for f in range(1, 3000) if (p - 1) % f == 0 and (p - 1) // f > 1 and all(((p - 1) // f) % r for r in range(2, int(((p - 1) // f) ** 0.5) + 1))}))
        S = W.setup(1, n, p, gen); tors.append(S["tor"]); assert S["e"] == e
        if n < 3: continue
        rels, cusp = S["rels"], [S["mu"], LAM]; w = {A: 1, B: 1, T: (p - 1) if n % 2 else 1}; ok = True; fails_without = 0
        for ch in S["chars"]:
            V = W.ch1(ch, p); h0, h1 = W.cohom(V, rels)
            for tw, use_w in ((True, w), (False, None)):
                Vp = V.dual(use_w) if use_w else V.dual(); d = W.cohom(Vp, rels, cusp); rel = d[2] + N19.h0P(Vp, cusp) - d[0]
                if tw: ok &= (h1 - h0) == rel
                else: fails_without += (h1 - h0) != rel
        print("level %d (prime %d): %d characters; h^2(V) = h^1_rel(V* w) on every one: %s; with w left out it fails on %d" % (n, p, len(S["chars"]), ok, fails_without))
    print("E2: the fibre torsion at levels 1 to 8: %s" % tors)
