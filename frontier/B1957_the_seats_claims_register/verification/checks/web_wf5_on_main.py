"""B1957: the web seat's foundations card W-F5 (a cone point is a relation among the three distinctions), on main's code.
Data-free.  O_K = <a, b, c | a^2, b^2, c^2, (abc)^K>; K = infinity is the free product; x = ab, y = bc; lambda = [x, y].
 F1  H_1(O_K) and whether the parity character (each distinction to -1) exists, K = 2 to 13 and infinity.
 F2  in the free product (abc)^2 = x (xy)^-1 y; for odd K, abc, c and a are words in x and y modulo (abc)^K.
 F3  H^1(O_K; chi) for every character, over two prime fields: the number of classes and how many are non-zero on lambda;
     the class of chi = (-1, -1, 1) with c = (1, 0, 0) at K = infinity.
 F4  on random points of the cubic X^2 + Y^2 + Z^2 = XYZ: tr[x, y] = -2, [x, y] + 1 a non-zero nilpotent, [x, y]^n never
     the identity for n to 24; on the level sets tr[x, y] = -2 cos(pi/k): [x, y]^(2k) = 1; at the origin [x, y] = -1.
 F5  at the common point lambda = -1: lambda^k = 1 exactly for even k."""
import functools, sys, pathlib, itertools
import mpmath as mp
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import web_wf4_on_main as W
red2 = lambda w: functools.reduce(lambda s, c: s[:-1] if s and s[-1] == c else s + c, w, "")          # the free product: letters are involutions

if __name__ == "__main__":
    import random; random.seed(1957)                      # mpmath's rand draws from Python's generator: seeded on 2026-11-18 so that a rerun gives the same digits (the web seat's section 8)
    def h1_group(K):                                                    # (Z/2)^3 modulo K(a + b + c): the number of invariant factors 2 of its relation matrix
        # CHANGED 2026-11-18 (the web seat's section 16.3): this returned a hard-coded parity rule; the rank is computed now
        import sympy as sp
        from sympy.matrices.normalforms import smith_normal_form
        rows = [[2, 0, 0], [0, 2, 0], [0, 0, 2]] + ([] if K is None else [[K, K, K]])
        d = smith_normal_form(sp.Matrix(rows), domain=sp.ZZ); inv = [abs(d[i, i]) for i in range(min(d.shape))]
        assert all(x in (1, 2) for x in inv), inv
        return sum(1 for x in inv if x == 2)
    parity_ok = lambda K: K is None or (-1) ** (3 * K) == 1                # the character a, b, c -> -1 kills K(a + b + c)
    print("F1: H_1(O_K) = (Z/2)^r with r = %s for K = 2 to 13, and 3 at K = infinity; the parity character needs (-1)^K = 1: it exists at K = %s and at infinity" % ([h1_group(K) for K in range(2, 14)], [K for K in range(2, 14) if parity_ok(K)]))
    x, y = "ab", "bc"; inv = lambda w: w[::-1]
    print("F2: x (xy)^-1 y = %s = (abc)^2: %s; x^-1 (abc) = %s (c); (abc) y^-1 = %s (a); and for odd K, (abc)^(1-K) = abc modulo (abc)^K, a word in (abc)^2 since 1 - K is even" % (red2(x + inv(x + y) + y), red2(x + inv(x + y) + y) == "abcabc", red2(inv(x) + "abc"), red2("abc" + inv(y))))
    lam = (1, 2, 2, 3, -2, -1, -3, -2)                                  # [x, y] = ab bc (ab)^-1 (bc)^-1, generators 1, 2, 3 = a, b, c
    for p in (1000033, 999983):                                          # two primes, neither the seat's
        rows = []
        for K in list(range(2, 14)) + [None]:
            rels = [(1, 1), (2, 2), (3, 3)] + ([(1, 2, 3) * K] if K else []); tot = nz = 0; chars = 0; special = None
            for s in itertools.product((1, p - 1), repeat=3):
                if K and pow(s[0] * s[1] * s[2] % p, K, p) != 1: continue
                chars += 1; V = W.Rep({1: [[s[0]]], 2: [[s[1]]], 3: [[s[2]]]}, p); h0, h1 = W.cohom(V, rels); tot += h1
                F = []
                for r in rels: F.append([V.fox(r, g)[0][0] for g in (1, 2, 3)])
                Z = W.nullspace(F, p, 3); cob = [(s[i] - 1) % p for i in range(3)]
                lamv = [sum(V.fox(lam, g)[0][0] * c[g - 1] for g in (1, 2, 3)) % p for c in Z]
                # classes non-zero on lambda: the rank of the functional c -> c(lambda) on Z^1 (it vanishes on coboundaries, chi(lambda) = 1)
                nz += 1 if any(lamv) else 0
                if K is None and s == (p - 1, p - 1, 1):
                    c = [1, 0, 0]; ok = all(sum(row[i] * c[i] for i in range(3)) % p == 0 for row in F); v = sum(V.fox(lam, g)[0][0] * c[g - 1] for g in (1, 2, 3)) % p; special = (ok, v if v < p // 2 else v - p)
            rows.append((K, chars, tot, nz, special))
        print("F3, prime %d: K: (characters, classes, characters with a class non-zero on lambda): %s; at infinity %s; the cocycle (1, 0, 0) of chi = (-1, -1, 1) is a cocycle with c(lambda) = %s" % (p, {r[0]: r[1:4] for r in rows if r[0]}, rows[-1][1:4], rows[-1][4]))
    mp.mp.dps = 40; rnd = lambda: mp.mpc(mp.rand() * 4 - 2, mp.rand() * 4 - 2); worst_tr = 0; least = mp.inf; nil = True
    def pair(X, Y, Z):                                                   # x = [[X, -1], [1, 0]], y = [[0, u], [-1/u, Y]]: tr x = X, tr y = Y, tr xy = u + 1/u = Z
        u = (Z + mp.sqrt(Z * Z - 4)) / 2; return mp.matrix([[X, -1], [1, 0]]), mp.matrix([[0, u], [-1 / u, Y]])
    def comm(X, Y, Z):
        a, b = pair(X, Y, Z); return a * b * a ** -1 * b ** -1, a, b
    n_pts = 0
    while n_pts < 200:
        X, Y = rnd(), rnd(); d = (X * Y) ** 2 - 4 * (X * X + Y * Y)
        Z = (X * Y + mp.sqrt(d)) / 2                                      # the cubic solved for Z
        C, a, b = comm(X, Y, Z)
        tr = C[0, 0] + C[1, 1]; worst_tr = max(worst_tr, abs(tr + 2)); N = C + mp.eye(2); nil &= mp.norm(N * N) < mp.mpf(10) ** -25 and mp.norm(N) > mp.mpf(10) ** -6
        P = mp.eye(2)
        for n in range(1, 25): P = P * C; least = min(least, mp.norm(P - mp.eye(2)))
        n_pts += 1
    print("F4: %d random points of the cubic (40 digits): max |tr[x, y] + 2| = %s; [x, y] + 1 is a non-zero nilpotent at every one: %s; the least |[x, y]^n - 1| over n = 1 to 24: %s" % (n_pts, mp.nstr(worst_tr, 3), nil, mp.nstr(least, 4)))
    okk = True
    for k in range(2, 7):
        for _ in range(40):
            X, Y = rnd(), rnd(); t = -2 * mp.cos(mp.pi / k)               # X^2 + Y^2 + Z^2 - XYZ - 2 = t
            Z = (X * Y + mp.sqrt((X * Y) ** 2 - 4 * (X * X + Y * Y - 2 - t))) / 2; C, a, b = comm(X, Y, Z)
            okk &= abs(C[0, 0] + C[1, 1] - t) < mp.mpf(10) ** -25 and mp.norm(C ** (2 * k) - mp.eye(2)) < mp.mpf(10) ** -20
    I2 = mp.matrix([[1j, 0], [0, -1j]]); J2 = mp.matrix([[0, 1], [-1, 0]]); C0 = I2 * J2 * I2 ** -1 * J2 ** -1
    print("F4: on the level sets tr[x, y] = -2 cos(pi/k), k = 2 to 6 (40 points each): the trace as set and [x, y]^(2k) = 1: %s; at the origin (the quaternion pair, traces 0, 0, 0): [x, y] = %s" % (okk, [[int(mp.re(C0[i, j])) for j in range(2)] for i in range(2)]))
    print("F5: lambda = -1: lambda^k = 1 for k = %s of 1 to 12" % [k for k in range(1, 13) if (-1) ** k == 1])
