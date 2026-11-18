"""B1957: the web seat's W-C8 part 5, the two statements of its table that main had marked verified without
recomputing (the seat's section 8.2 of 2026-11-18): for the bronze pair, levels 1 to 3 of the tick tau_3
(a -> a^3 b, b -> a), beside the golden pair.  Main's own code; exact over F_p.  Data-free.
 R3  the free-cusp frame: b_1 = 1 and the cusp's rank in H_1 is 1, at levels 1 to 3, for both ticks.  Over F_p with p
     prime to the torsion: h^1 of the trivial character, and h^1 minus the classes that vanish on the cusp.
 R5  twisted duality h^2(V) = h^1_rel(V* w) on every character (t-values the 2e-th roots of unity) at levels 1 to 3,
     for both ticks; with w left out it fails on the odd levels and cannot differ on the even one.
     (h^2 = h^1 - h^0; h^1_rel(V') = interior classes + h^0 of the cusp - h^0.)
 Also the fibre torsion at levels 1, 2, 3 (golden 1, 1, 4; bronze 3, 9, 36) and the number of characters."""
import functools, sys, pathlib
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import web_wf4_on_main as W, web_wf19_on_main as N19, web_wf6_on_main as F6
A, B, T, LAM = W.A, W.B, W.T, W.LAM


def primitive_root(p):
    n = p - 1; fs = set(); d = 2
    while d * d <= n:
        while n % d == 0: fs.add(d); n //= d
        d += 1
    if n > 1: fs.add(n)
    return next(g for g in range(2, p) if all(pow(g, (p - 1) // q, p) != 1 for q in fs))

if __name__ == "__main__":
    for name, m in (("golden", 1), ("bronze", 3)):
        for n in (1, 2, 3):
            e0 = W.setup(m, n, 1000003, 2)["e"]; p = F6.prime_for(e0); gen = primitive_root(p); S = W.setup(m, n, p, gen); assert S["e"] == e0 and (p - 1) % (2 * e0) == 0 and S["tor"] % p != 0
            rels, cusp = S["rels"], [S["mu"], LAM]; w = {A: 1, B: 1, T: (p - 1) if n % 2 else 1}
            triv = W.ch1((1, 1, 1), p); h0, h1, interior = W.cohom(triv, rels, cusp)
            ok = True; fails_without = 0
            for ch in S["chars"]:
                V = W.ch1(ch, p); a0, a1 = W.cohom(V, rels)
                for use_w in (w, None):
                    Vp = V.dual(use_w) if use_w else V.dual(); d = W.cohom(Vp, rels, cusp); rel = d[2] + N19.h0P(Vp, cusp) - d[0]
                    if use_w: ok &= (a1 - a0) == rel
                    else: fails_without += (a1 - a0) != rel
            print("%s, level %d (prime %d): fibre torsion %d; b_1 = %d; the cusp's rank %d; %d characters; h^2(V) = h^1_rel(V* w) on every one: %s; with w left out it fails on %d" % (name, n, p, S["tor"], h1, h1 - interior, len(S["chars"]), ok, fails_without))
