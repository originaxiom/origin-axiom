"""B1957: the web seat's foundations card W-F9 (the order at the scar), on main's own code.  Data-free; exact over F_p.
The record's modules at an orientable level: V(l, alpha) = [[alpha, c beta], [0, beta]], beta = alpha/l, l and alpha
non-trivial fibre-torsion characters with value 1 on mu, beta non-trivial, c the class of H^1(G; l) with c(lambda) = 1.
n(V) = the number of interior classes of H^1 (those that restrict to zero on the cusp).  I(V) = n(V) - n(V*).
 O1  (h^0, h^1, n) of the dual V* against that of V(l, l alpha^-1), on every module.
 O2  the numbers of modules with I = +1 and I = -1; I is odd under alpha -> l alpha^-1.
 O3  the 'wrong partner' V(l, alpha^-1): on how many of the modules where it exists do the invariants differ from V*'s.
 O4  (the referee's check, redone) at golden level 4: I on alpha = l^-1, on alpha = l^2, and on the fixed points.
Levels: golden 4, 6, 8; bronze 2.  Prime 1 mod the torsion's exponent, different from the seat's."""
import functools, sys, pathlib
from math import gcd
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import web_wf4_on_main as W
A, B, T, LAM = W.A, W.B, W.T, W.LAM


def census(m, n, p):
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in {f for f in range(2, 3000) if (p - 1) % f == 0 and all(f % r for r in range(2, int(f ** 0.5) + 1))} | {(p - 1) // f for f in range(1, 3000) if (p - 1) % f == 0 and (p - 1) // f > 1 and all(((p - 1) // f) % r for r in range(2, int(((p - 1) // f) ** 0.5) + 1))}))
    S = W.setup(m, n, p, gen); rels, mu = S["rels"], S["mu"]; cusp = [mu, LAM]; inv = lambda x: pow(x, p - 2, p)
    tors = sorted({ch for ch in S["chars"] if ch[:2] != (1, 1) and W.val(ch, mu, p) == 1})
    cmul = lambda x, y: tuple(a * b % p for a, b in zip(x, y)); cinv = lambda x: tuple(inv(a) for a in x)
    def module(l, c, al):
        be = cmul(al, cinv(l)); return W.Rep({g: [[al[g - 1], c[g - 1] * be[g - 1] % p], [0, be[g - 1]]] for g in (A, B, T)}, p)
    inv3 = lambda V: W.cohom(V, rels, cusp)
    mods = 0; o1 = True; Ival = {}; wrong_testable = wrong_fail = 0
    for l in tors:
        V1 = W.ch1(l, p); F = [[V1.fox(r, g)[0][0] for g in (A, B, T)] for r in rels]; Z = W.nullspace(F, p, 3)
        lamv = lambda c: sum(V1.fox(LAM, g)[0][0] * c[k] for k, g in enumerate((A, B, T))) % p
        c = next((z for z in Z if lamv(z)), None)
        if c is None: continue
        s = inv(lamv(c)); c = [x * s % p for x in c]; assert lamv(c) == 1
        for al in tors:
            if al == l: continue                                              # beta trivial
            V = module(l, c, al); d = inv3(V.dual()); mods += 1
            partner = module(l, c, cmul(l, cinv(al))); o1 &= inv3(partner) == d
            Ival[(l, al)] = inv3(V)[2] - d[2]
            if cinv(al) != l and cinv(al) in tors and cmul(cinv(al), cinv(l))[:2] != (1, 1):
                wrong_testable += 1; wrong_fail += inv3(module(l, c, cinv(al))) != d
    odd = all(Ival[(l, cmul(l, cinv(al)))] == -v for (l, al), v in Ival.items())
    return dict(tors=len(tors), mods=mods, o1=o1, plus=sum(v == 1 for v in Ival.values()), minus=sum(v == -1 for v in Ival.values()), zero=sum(v == 0 for v in Ival.values()), odd=odd, wt=wrong_testable, wf=wrong_fail, Ival=Ival, cmul=cmul, cinv=cinv)


if __name__ == "__main__":
    for name, m, n, e in (("golden 4", 1, 4, 5), ("golden 6", 1, 6, 4), ("bronze 2", 3, 2, 3), ("golden 8", 1, 8, 15)):
        q = 300000 - (300000 % (2 * e)) + 1
        while True:
            q += 2 * e
            if all(q % r for r in range(2, int(q ** 0.5) + 1)): break
        r = census(m, n, q)
        print("%s (prime %d): %d modules; the dual's (h^0, h^1, n) equals V(l, l/alpha)'s on every one: %s; I = +1 on %d, -1 on %d, 0 on %d; I odd under alpha -> l/alpha: %s; the wrong partner V(l, 1/alpha) exists for %d and differs on %d" % (name, q, r["mods"], r["o1"], r["plus"], r["minus"], r["zero"], r["odd"], r["wt"], r["wf"]))
        if name == "golden 4":
            cm, ci = r["cmul"], r["cinv"]; I = r["Ival"]
            print("   golden 4, the referee's lines: I on alpha = 1/l: %s; on alpha = l^2: %s; on the fixed points alpha^2 = l: %s" % (sorted({v for (l, al), v in I.items() if al == ci(l)}), sorted({v for (l, al), v in I.items() if al == cm(l, l)}), sorted({v for (l, al), v in I.items() if cm(al, al) == l})))
