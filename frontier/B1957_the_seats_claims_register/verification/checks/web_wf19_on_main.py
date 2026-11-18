"""B1957: the web seat's W-F19 (the class index is zero on every doublet at every odd level), on main's own code.
Data-free; exact over F_p.  Main read the proof's Step 1 line by line and its algebra holds (the seven sub-steps combine
to the formula).  Computed here, at odd levels of the golden, silver and bronze ticks, on every doublet
[[alpha, c beta], [0, beta]] (alpha any character, l = alpha/beta any character with a class that is not a coboundary):
 E1  Step 1's formula  I_w(V) = h^0(P; V') + h^0(G; V) - h^0(G; V') - r^1(V),  V' = V* w,  r^1 = h^1 - n,
     with every term computed directly; and on the record modules of golden level 4 (where w = 1).
 E2  I_w(V) = n(V) - n(V') = 0 on every doublet.
 E3  the doublets with n(V) = 1: their number against (|T| - 1)(|T| - 2), and that they are exactly those with l
     fibre-non-trivial and l(mu) = -1, beta fibre-non-trivial with beta(mu) = +1, and alpha != w.
 E4  the census of the gap h^1(V) - h^1(V').
Levels: golden 1, 3, 5; silver 1, 3; bronze 1 (and bronze 3, 46,656 doublets, with the argument `all`)."""
import functools, sys, pathlib, collections
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import web_wf4_on_main as W
A, B, T, LAM = W.A, W.B, W.T, W.LAM


def h0P(V, cusp):
    d, p = V.d, V.p; rows = []
    for w in cusp:
        M = V.word(w); rows += [[(M[i][j] - int(i == j)) % p for j in range(d)] for i in range(d)]
    return d - W.rank(rows, p)


def level(m, n, p, gen):
    S = W.setup(m, n, p, gen); rels, mu = S["rels"], S["mu"]; cusp = [mu, LAM]; inv = lambda x: pow(x, p - 2, p); odd = n % 2 == 1; w = {A: 1, B: 1, T: (p - 1) if odd else 1}; wch = (1, 1, p - 1)
    ext = []
    for l in S["chars"]:
        V1 = W.ch1(l, p); F = [[V1.fox(r, g)[0][0] for g in (A, B, T)] for r in rels]; Z = W.nullspace(F, p, 3); cob = [(l[i] - 1) % p for i in range(3)]
        c = next((z for z in Z if (any(z) if not any(cob) else any((z[i] * cob[j] - z[j] * cob[i]) % p for i in range(3) for j in range(3)))), None)   # for the trivial character every non-zero cocycle is a class
        if c is not None: ext.append((l, c))
    fn = lambda ch: ch[:2] != (1, 1); mv = lambda ch: W.val(ch, mu, p)
    nd = 0; formula = True; nzI = 0; n1 = 0; n1_as_predicted = True; gaps = collections.Counter()
    for l, c in ext:
        li = tuple(inv(x) for x in l)
        for al in S["chars"]:
            be = tuple(a * b % p for a, b in zip(al, li)); V = W.Rep({g: [[al[g - 1], c[g - 1] * be[g - 1] % p], [0, be[g - 1]]] for g in (A, B, T)}, p); Vp = V.dual(w)
            a = W.cohom(V, rels, cusp); d = W.cohom(Vp, rels, cusp); nd += 1; I = a[2] - d[2]; nzI += I != 0; gaps[a[1] - d[1]] += 1
            formula &= I == h0P(Vp, cusp) + a[0] - d[0] - (a[1] - a[2])
            pred = fn(l) and mv(l) == p - 1 and fn(be) and mv(be) == 1 and al != wch
            n1 += a[2] == 1; n1_as_predicted &= (a[2] == 1) == pred and a[2] in (0, 1)
    return dict(tor=S["tor"], e=S["e"], chars=len(S["chars"]), ext=len(ext), nd=nd, formula=formula, nzI=nzI, n1=n1, pred=(S["tor"] - 1) * (S["tor"] - 2), n1ok=n1_as_predicted, gaps=dict(sorted(gaps.items())))


if __name__ == "__main__":
    todo = [("golden 1", 1, 1), ("golden 3", 1, 3), ("golden 5", 1, 5), ("silver 1", 2, 1), ("silver 3", 2, 3), ("bronze 1", 3, 1)] + ([("bronze 3", 3, 3)] if "all" in sys.argv[1:] else [])
    M = 2 * 2 * 11 * 7 * 9                                                 # 2e for e in 1, 2, 11, 2, 14, 3, 18
    p = M * 150 + 1
    while not all(p % r for r in range(2, int(p ** 0.5) + 1)): p += M
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in {f for f in range(2, 3000) if (p - 1) % f == 0 and all(f % r for r in range(2, int(f ** 0.5) + 1))} | {(p - 1) // f for f in range(1, 3000) if (p - 1) % f == 0 and (p - 1) // f > 1 and all(((p - 1) // f) % r for r in range(2, int(((p - 1) // f) ** 0.5) + 1))}))
    tot = 0
    for name, m, n in todo:
        r = level(m, n, p, gen); tot += r["nd"]
        print("%s (prime %d): |T| = %d (exponent %d); characters %d; extension characters %d; doublets %d; Step 1's formula on every one: %s; I_w != 0 on %d; n = 1 on %d (predicted %d), and exactly on the predicted doublets: %s; the gap's census %s" % (name, p, r["tor"], r["e"], r["chars"], r["ext"], r["nd"], r["formula"], r["nzI"], r["n1"], r["pred"], r["n1ok"], r["gaps"]))
    print("doublets in all: %d" % tot)
    # golden level 4: the formula at an orientable level, on the record modules
    S = W.setup(1, 4, p, gen); rels, mu = S["rels"], S["mu"]; cusp = [mu, LAM]; inv = lambda x: pow(x, p - 2, p); tors = sorted({ch for ch in S["chars"] if ch[:2] != (1, 1) and W.val(ch, mu, p) == 1}); ok = True; Ic = collections.Counter()
    for l in tors:
        V1 = W.ch1(l, p); F = [[V1.fox(r, g)[0][0] for g in (A, B, T)] for r in rels]; Z = W.nullspace(F, p, 3); lamv = lambda c: sum(V1.fox(LAM, g)[0][0] * c[k] for k, g in enumerate((A, B, T))) % p
        c = next(z for z in Z if lamv(z)); li = tuple(inv(x) for x in l)
        for al in tors:
            if al == l: continue
            be = tuple(x * y % p for x, y in zip(al, li)); V = W.Rep({g: [[al[g - 1], c[g - 1] * be[g - 1] % p], [0, be[g - 1]]] for g in (A, B, T)}, p); Vp = V.dual()
            a = W.cohom(V, rels, cusp); d = W.cohom(Vp, rels, cusp); I = a[2] - d[2]; Ic[I] += 1; ok &= I == h0P(Vp, cusp) + a[0] - d[0] - (a[1] - a[2])
    print("golden level 4, the record modules: the formula holds on all %d: %s; I = +1, 0, -1 on %d, %d, %d" % (sum(Ic.values()), ok, Ic[1], Ic[0], Ic[-1]))
