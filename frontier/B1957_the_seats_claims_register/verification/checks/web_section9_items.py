"""B1957: three statements of the web seat's that main's records held as verified without main's own computation
(the seat's section 9.2 of 2026-11-18, items 3, 4 and 5), computed on main.  Exact, or to 40 digits.  Data-free.
 I3  W-C8 part 5, 'twisted duality holds on every module': at bronze's level 2 the 56 non-split modules
     V(l, alpha) = [[alpha, c beta], [0, beta]] of the record; h^2(V) = h^1_rel(V*) on each (the level is even, so the
     twisting character is trivial).  h^2 = h^1 - h^0; h^1_rel(V') = interior classes + h^0 of the cusp - h^0.
     Each is non-split by construction: its class c has c(lambda) = 1, and a coboundary vanishes on lambda.
 I4  W-C8 part 2a, 'b_1 = 1 and the cusp's rank is 1 at levels 1 to 8' of the golden tick: from the group itself over
     F_p (h^1 of the trivial character; the classes that do not vanish on the cusp), and det(J^n - 1) = 2 - tr J^n for
     odd n, -tr J^n for even n, never zero: 1, 1, 4, 5, 11, 16, 29, 45 in absolute value, the fibre torsion.
 I5  W-C1: the index of the figure-eight group in PSL(2, O), O the Eisenstein integers, by volumes:
     vol(m004) / (3^(3/2) zeta_K(2) / (4 pi^2)) = 12 to 40 digits (vol = 3 Cl_2(2 pi/3); SnapPy's volume beside it);
     and the image of Riley's pair in SL(2, O/N) at N = 2, 4, 8, closed under multiplication without adding -1:
     orders 10, 320, 20,480, each holding -1; with the orders 60, 3,840, 245,760 of SL(2, O/N) the indices are 6, 12, 12.
 I6  the scale folder's sign control K4d: in the convention of main's own check of K4a (web_scale_census.py, C4:
     -d_zbar d_z log h1 + (h1/h2)|f|^2 = 0 for theta = E12 f dz, h = diag(e^u, e^-u)) the surface metric e^(2u)|f|^2|dz|^2
     has curvature -4, and with the opposite sign +4; the cusp metric solves the first and not the second, the round
     metric the second and not the first.
 I7  the T-ROOT check's tail beyond length 18, from its preregistered bound (Gueritaud and Futer's Vol >= 2 k v3 for k
     syllable pairs; at most C(n - 1, 2k - 1)/k threads of length n with k pairs): the sum to n = 4000 with a geometric
     remainder under the weights 2^-n and 3^-n, and x/18 under the per-length weight, x = exp(-c 2 v3/(6 pi)); at
     c = 6 with the root's shares of main's own run (web_scale_troot_tsign_run.txt), the intervals for the root's share
     and the tail against the sum under 3^-n."""
import functools, itertools, sys, pathlib
import mpmath as mp
import sympy as sp
import math, re
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import web_wf4_on_main as W, web_wf19_on_main as N19, web_wf6_on_main as F6, web_wc8_part5_bronze as BR
A, B, T, LAM = W.A, W.B, W.T, W.LAM

if __name__ == "__main__":
    # I3
    m, n = 3, 2; e0 = W.setup(m, n, 1000003, 2)["e"]; p = F6.prime_for(e0); gen = BR.primitive_root(p); S = W.setup(m, n, p, gen); rels, mu = S["rels"], S["mu"]; cusp = [mu, LAM]; inv = lambda x: pow(x, p - 2, p)
    tors = sorted({ch for ch in S["chars"] if ch[:2] != (1, 1) and W.val(ch, mu, p) == 1}); cmul = lambda x, y: tuple(a * b % p for a, b in zip(x, y)); cinv = lambda x: tuple(inv(a) for a in x)
    mods = holds = 0
    for l in tors:
        V1 = W.ch1(l, p); F = [[V1.fox(r, g)[0][0] for g in (A, B, T)] for r in rels]; Z = W.nullspace(F, p, 3)
        lamv = lambda c: sum(V1.fox(LAM, g)[0][0] * c[k] for k, g in enumerate((A, B, T))) % p
        c = next((z for z in Z if lamv(z)), None)
        if c is None: continue
        s = inv(lamv(c)); c = [x * s % p for x in c]
        for al in tors:
            if al == l: continue
            be = cmul(al, cinv(l)); V = W.Rep({g: [[al[g - 1], c[g - 1] * be[g - 1] % p], [0, be[g - 1]]] for g in (A, B, T)}, p); assert V.is_module(rels)
            a0, a1 = W.cohom(V, rels)[:2]; Vp = V.dual(); d = W.cohom(Vp, rels, cusp); rel = d[2] + N19.h0P(Vp, cusp) - d[0]
            mods += 1; holds += (a1 - a0) == rel
    print("I3: bronze, level 2 (prime %d): %d modules V(l, alpha); h^2(V) = h^1_rel(V*) on %d of them" % (p, mods, holds))
    # I4
    rows = []; J = ((1, 1), (1, 0)); P = ((1, 0), (0, 1)); mul = lambda X, Y: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    for n in range(1, 9):
        P = mul(P, J); det = (P[0][0] - 1) * (P[1][1] - 1) - P[0][1] * P[1][0]
        e0 = W.setup(1, n, 1000003, 2)["e"]; p = F6.prime_for(e0); gen = BR.primitive_root(p); S = W.setup(1, n, p, gen); assert S["tor"] % p != 0
        h0, h1, interior = W.cohom(W.ch1((1, 1, 1), p), S["rels"], [S["mu"], LAM]); rows.append((n, det, S["tor"], h1, h1 - interior)); assert abs(det) == S["tor"]
    print("I4: golden, levels 1 to 8: (level, det(J^n - 1), fibre torsion, b_1, the cusp's rank): %s" % rows)
    # I5
    mp.mp.dps = 45; vol = 3 * mp.clsin(2, 2 * mp.pi / 3); L2 = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9; cov = mp.mpf(3) ** mp.mpf("1.5") * mp.zeta(2) * L2 / (4 * mp.pi ** 2)
    try:
        import snappy; sv = float(snappy.Manifold("m004").volume())
    except Exception: sv = None
    print("I5: vol = %s (SnapPy's: %s); the covolume of PSL(2, O) = %s; the ratio minus 12 = %s" % (mp.nstr(vol, 22), ("%.15f" % sv) if sv else "not available", mp.nstr(cov, 22), mp.nstr(vol / cov - 12, 3)))
    def ring(N):
        mulr = lambda x, y: ((x[0] * y[0] - x[1] * y[1]) % N, (x[0] * y[1] + x[1] * y[0] - x[1] * y[1]) % N); addr = lambda x, y: ((x[0] + y[0]) % N, (x[1] + y[1]) % N); return mulr, addr
    out = []
    for N in (2, 4, 8):
        mulr, addr = ring(N); mm = lambda X, Y: tuple(tuple(addr(mulr(X[i][0], Y[0][j]), mulr(X[i][1], Y[1][j])) for j in range(2)) for i in range(2))
        one, zero = (1, 0), (0, 0); a = ((one, one), (zero, one)); b = ((one, zero), ((0, (-1) % N), one)); I = ((one, zero), (zero, one)); mI = ((((-1) % N, 0), zero), (zero, ((-1) % N, 0)))
        seen = {I}; todo = [I]
        while todo:
            X = todo.pop()
            for g in (a, b):
                Y = mm(X, g)
                if Y not in seen: seen.add(Y); todo.append(Y)
        if N <= 4:
            els = [(i, j) for i in range(N) for j in range(N)]; sl = sum(1 for w, x, y, z in itertools.product(els, repeat=4) if addr(mulr(w, z), tuple((-t) % N for t in mulr(x, y))) == one)
        else: sl = 60 * 64 ** 2                                              # the kernel of reduction modulo 4 has 64 elements
        out.append((N, len(seen), mI in seen, sl, sl // len(seen)))
    print("I5: (N, order of the image, it holds -1, order of SL(2, O/N), index): %s (at N = 8 the order of SL(2, O/N) is 64 times that at 4)" % out)
    # I6
    z, zb = sp.symbols("z zb"); curv = lambda rho: sp.simplify(-4 * sp.exp(-2 * rho) * sp.diff(rho, z, zb))           # K = -e^(-2 rho) Laplacian(rho), the Laplacian being 4 d_z d_zbar
    Lh = -sp.log(z * zb); u_c, f_c = -sp.log(Lh), 1 / z; u_r, f_r = -sp.log(1 + z * zb), sp.Integer(1)
    eq = lambda u, f, sign: sp.simplify(-sp.diff(u, z, zb) + sign * sp.exp(2 * u) * f * sp.conjugate(f).subs(sp.conjugate(z), zb))
    rho_c = u_c - sp.log(z * zb) / 2; rho_r = u_r
    print("I6: the cusp: this convention's equation %s, the opposite's %s, curvature %s; the round metric: this convention's %s, the opposite's %s, curvature %s" % (
        eq(u_c, f_c, 1), "zero" if eq(u_c, f_c, -1) == 0 else "not zero", curv(rho_c), "zero" if eq(u_r, f_r, 1) == 0 else "not zero", eq(u_r, f_r, -1), curv(rho_r)))
    # I7
    mp.mp.dps = 30; v3 = mp.clsin(2, mp.pi / 3); c = 6; x = mp.exp(-c * 2 * v3 / (6 * mp.pi)); y = mp.sqrt(x); tails = {}
    for key, beta in (("A", 2), ("B", 3)):
        tot = mp.mpf(0)
        for n in range(19, 4001):
            term = mp.mpf(1); inner = mp.mpf(0); bn = mp.binomial                                  # sum_k C(n-1, 2k-1) x^k / k
            for k in range(1, n // 2 + 1):
                t = bn(n - 1, 2 * k - 1) * x ** k / k
                inner += t
                if k > 40 and t < inner * mp.mpf(10) ** -28 and 2 * k > n * y / (1 + y) + 5: break
            tot += inner / mp.mpf(beta) ** n
            if inner / mp.mpf(beta) ** n < tot * mp.mpf(10) ** -27 and n > 60: break
        r = (1 + y) / beta; tails[key] = tot + (y / (1 + y)) * r ** (n + 1) / (1 - r)
    tails["C"] = x / 18
    run = (pathlib.Path(__file__).resolve().parent / "web_scale_troot_tsign_run.txt").read_text()
    share = {k: float(re.search(r"weight \(%s\) at c = 6: root share ([0-9.]+)" % k, run).group(1)) for k in "ABC"}
    rootw = {"A": mp.mpf(1) / 4 * x, "B": mp.mpf(1) / 9 * x, "C": mp.mpf(1) / 2 * x}                # the root has length 2 and is the one thread of its length
    out7 = {k: (mp.nstr(tails[k], 6), round(float(rootw[k] / (rootw[k] / share[k] + tails[k])), 3), share[k], mp.nstr(rootw[k] / share[k], 4)) for k in "ABC"}
    print("I7: at c = 6, (tail bound, lower end of the root's share, the share, the sum Z) under the three weights: %s; under 3^-n the tail is %s of Z" % (out7, mp.nstr(tails["B"] / (rootw["B"] / share["B"]), 3)))
