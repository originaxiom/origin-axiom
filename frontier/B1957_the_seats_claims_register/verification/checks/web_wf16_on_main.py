"""B1957: the web seat's foundations card W-F16 (the two-way choices settle each other), on main's own code.  Data-free.
 H1  J = [[m, 1], [1, 0]], K = [[0, 1], [-1, 0]], N = m^2 + 4, the mark v = (m, 2) mod N.  For every odd m to 41, n = 0
     to 7, e in {0, 1} and both signs: +-J^n K^e sends v to a multiple s v, and the hand (1 when s is not +-1) is
     (n + e) mod 2.
 H2  the mirror at an even level of the metallic tick: phi(a) = tau(a), phi(b) = tau(b), phi(t) = t.  Every record
     module pulled back by phi is a module, and I(V o phi) = I(V) (I as in W-F9), at golden 4, 6, 8 and bronze 2.
     The seat's plant (t -> t^-1) is also run: it must fail the relators.
 H3  the count of free bits among (hand h, tick parity o, undoing e, order r, Higgs reading q, hypercharge sign y) as
     the number of orbits of the symmetries on the solutions of the relations, by enumeration of all 64 assignments:
     J flips (o, h), K flips (e, h), D flips r, C flips (q, y)."""
import functools, sys, pathlib, itertools, math
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import web_wf4_on_main as W
A, B, T, LAM = W.A, W.B, W.T, W.LAM


def h1():
    ok = True; cases = 0
    for m in range(1, 42, 2):
        N = m * m + 4; v = (m % N, 2 % N); mm = lambda X, Y: [[sum(X[i][k] * Y[k][j] for k in range(2)) % N for j in range(2)] for i in range(2)]
        J, K = [[m % N, 1], [1, 0]], [[0, 1], [N - 1, 0]]
        for n in range(8):
            for e in (0, 1):
                for sg in (1, N - 1):
                    X = [[int(i == j) for j in range(2)] for i in range(2)]
                    for _ in range(n): X = mm(X, J)
                    if e: X = mm(X, K)
                    u = (sg * (X[0][0] * v[0] + X[0][1] * v[1]) % N, sg * (X[1][0] * v[0] + X[1][1] * v[1]) % N)
                    s = next((s for s in range(N) if (s * v[0] % N, s * v[1] % N) == u), None); cases += 1
                    ok &= s is not None and int(s not in (1, N - 1)) == (n + e) % 2
    return ok, cases


def h2(m, n, p):
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in {f for f in range(2, 3000) if (p - 1) % f == 0 and all(f % r for r in range(2, int(f ** 0.5) + 1))} | {(p - 1) // f for f in range(1, 3000) if (p - 1) % f == 0 and (p - 1) // f > 1 and all(((p - 1) // f) % r for r in range(2, int(((p - 1) // f) ** 0.5) + 1))}))
    S = W.setup(m, n, p, gen); rels, mu = S["rels"], S["mu"]; cusp = [mu, LAM]; inv = lambda x: pow(x, p - 2, p)
    tors = sorted({ch for ch in S["chars"] if ch[:2] != (1, 1) and W.val(ch, mu, p) == 1}); ta, tb = W.tau((A,), m), W.tau((B,), m)
    I = lambda V: W.cohom(V, rels, cusp)[2] - W.cohom(V.dual(), rels, cusp)[2]
    mods = 0; ismod = True; keeps = True; plant_fails = 0; nonzero = 0
    for l in tors:
        V1 = W.ch1(l, p); F = [[V1.fox(r, g)[0][0] for g in (A, B, T)] for r in rels]; Z = W.nullspace(F, p, 3); lamv = lambda c: sum(V1.fox(LAM, g)[0][0] * c[k] for k, g in enumerate((A, B, T))) % p
        c = next((z for z in Z if lamv(z)), None)
        if c is None: continue
        s = inv(lamv(c)); c = [x * s % p for x in c]; li = tuple(inv(x) for x in l)
        for al in tors:
            if al == l: continue
            be = tuple(x * y % p for x, y in zip(al, li)); V = W.Rep({g: [[al[g - 1], c[g - 1] * be[g - 1] % p], [0, be[g - 1]]] for g in (A, B, T)}, p)
            Vm = W.Rep({A: V.word(ta), B: V.word(tb), T: V.m[T]}, p); mods += 1; ismod &= Vm.is_module(rels); i0 = I(V); keeps &= I(Vm) == i0; nonzero += i0 != 0
            Vp = W.Rep({A: V.word(ta), B: V.word(tb), T: V.m[-T]}, p); plant_fails += not Vp.is_module(rels)
    return mods, ismod, keeps, nonzero, plant_fails


def h3(sym, rel):
    vec = {"h": 0, "o": 1, "e": 2, "r": 3, "q": 4, "y": 5}; flip = lambda bits, s: tuple(b ^ (i in [vec[c] for c in s]) for i, b in enumerate(bits))
    sols = [bits for bits in itertools.product((0, 1), repeat=6) if all(sum(bits[vec[c]] for c in r) % 2 == 0 for r in rel)]
    assert all(flip(b, s) in sols for b in sols for s in sym); seen = set(); orbits = 0
    for b in sols:
        if b in seen: continue
        orbits += 1; stack = [b]
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x); stack += [flip(x, s) for s in sym]
    return int(math.log2(orbits))


if __name__ == "__main__":
    ok, cases = h1(); print("H1: odd m = 1 to 41, n = 0 to 7, e, sign (%d cases): the matrix acts on the mark by a scalar and the hand is (n + e) mod 2: %s" % (cases, ok))
    J, K, D, C = "oh", "eh", "r", "qy"
    print("H3 (orbits of the symmetries on the solutions, all 64 assignments): {J, K, D, C} with h+o+e, q+y: %d free bits; {J, K, D}: %d; {J, K, D o C} with h+o+e, q+y, r+y: %d; {J, K, D o C} with h+o+e, q+y: %d (the seat: 0, 1, 0, 1)" % (
        h3([J, K, D, C], ["hoe", "qy"]), h3([J, K, D], ["hoe", "qy"]), h3([J, K, "rqy"], ["hoe", "qy", "ry"]), h3([J, K, "rqy"], ["hoe", "qy"])))
    for name, m, n, e in (("golden 4", 1, 4, 5), ("golden 6", 1, 6, 4), ("bronze 2", 3, 2, 3), ("golden 8", 1, 8, 15)):
        q = 400000 - (400000 % (2 * e)) + 1
        while True:
            q += 2 * e
            if all(q % r for r in range(2, int(q ** 0.5) + 1)): break
        mods, ismod, keeps, nonzero, pf = h2(m, n, q)
        print("H2 %s (prime %d): %d record modules (%d with I != 0); each pulled back by the mirror is a module: %s; the index is the same on every one: %s; the plant t -> t^-1 fails the relators on %d of them" % (name, q, mods, nonzero, ismod, keeps, pf))
