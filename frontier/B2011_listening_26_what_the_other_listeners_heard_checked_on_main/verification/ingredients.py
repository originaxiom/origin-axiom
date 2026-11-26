"""B2011, A4 and A5 (main, 2026-11-26; data-free): the computed ingredients of agy's all-k halving argument (C60 section 2),
rebuilt on main's own code with numpy, at k = 2 to 8 (mod 9 to mod 6561).
A5: S_k = {v mod 3^k : every coordinate = 0 mod 3, abc != 0 mod 3 for v = 3(a, b, c), x^2 + y^2 + z^2 - xyz = 0 mod 3^(k+1)},
built by lifting S_(k-1) (each u + 3^(k-1) m, m in {0,1,2}^3, kept when the congruence holds); its size against 8 * 3^(2k-4);
whether it is one orbit of L and R containing (3,3,3) (scipy connected components on the graph of L and R).
A4 on the orbit: eps = abc mod 3 (1 for O+, 2 for O-); equal halves; every one of the six moves exchanges them; main's six
moves (L, R and their conjugates by C, C^-1) give the same images as the seat's six (L, R, L^-1, R^-1, X, X^-1); C's fixed
points and their side; gamma rising by 1 under C and under s2s3, s3s1, s1s2 on O-; the six gamma values around each point of
O+ being 0, 0, 1, 1, 2, 2; J_k (k >= 4) a bijection of O-, commuting with all six s_i s_j, and J_k C = tau C J_k.
    python3 -B ingredients.py > ingredients_run.txt"""
import time
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)
INV9 = np.zeros(9, dtype=np.int64)
for a in (1, 2, 4, 5, 7, 8):
    INV9[a] = pow(a, -1, 9)


def kappa(X, Y, Z):
    return X * X + Y * Y + Z * Z - X * Y * Z


def level(k, prev):
    N = 3 ** k
    if prev is None:
        g = np.array([3, 6]); X, Y, Z = [a.ravel() for a in np.meshgrid(g, g, g, indexing="ij")]
        keep = kappa(X, Y, Z) % (3 * N) == 0
        return X[keep], Y[keep], Z[keep]
    X0, Y0, Z0 = prev
    h = 3 ** (k - 1)
    m = np.array([(i, j, l) for i in range(3) for j in range(3) for l in range(3)], dtype=np.int64)
    X = (X0[:, None] + h * m[None, :, 0]).ravel(); Y = (Y0[:, None] + h * m[None, :, 1]).ravel(); Z = (Z0[:, None] + h * m[None, :, 2]).ravel()
    keep = kappa(X, Y, Z) % (3 * N) == 0
    return X[keep] % N, Y[keep] % N, Z[keep] % N


prev = None
for k in range(2, 9):
    N = 3 ** k
    X, Y, Z = level(k, prev); prev = (X, Y, Z)
    n = len(X)
    code = lambda A, B, Cc: (A * N + B) * N + Cc
    cs = code(X, Y, Z); order = np.argsort(cs); X, Y, Z, cs = X[order], Y[order], Z[order], cs[order]
    def find(A, B, Cc):
        c = code(A % N, B % N, Cc % N); i = np.searchsorted(cs, c); i = np.minimum(i, n - 1)
        return i, cs[i] == c
    mv = {
        "L": lambda A, B, Cc: (A, Cc, A * Cc - B), "R": lambda A, B, Cc: (Cc, B, B * Cc - A),
        "Li": lambda A, B, Cc: (A, A * B - Cc, B), "Ri": lambda A, B, Cc: (A * B - Cc, B, A),
        "X": lambda A, B, Cc: (B, B * Cc - A, Cc), "Xi": lambda A, B, Cc: (A * Cc - B, A, Cc),
    }
    Cf = lambda A, B, Cc: (B, Cc, A); Cif = lambda A, B, Cc: (Cc, A, B)
    imgs = {}
    for nm, f in mv.items():
        i, ok = find(*f(X, Y, Z)); assert ok.all(), (k, nm); imgs[nm] = i
    comps, lab = connected_components(csr_matrix((np.ones(2 * n), (np.r_[np.arange(n), np.arange(n)], np.r_[imgs["L"], imgs["R"]])), shape=(n, n)), directed=False)
    i333, ok333 = find(np.array([3]), np.array([3]), np.array([3]))
    log("A5 k = %d (mod %d): |S_k| = %d; 8 * 3^(2k-4) = %s; closed under the moves: True; components of L and R: %d; contains (3,3,3): %s" % (
        k, N, n, 8 * 3 ** (2 * k - 4) if k >= 2 else "-", comps, bool(ok333[0])))
    # main's six moves against the seat's six, as multisets of images
    main6 = []
    for f in (mv["L"], mv["R"], lambda A, B, Cc: Cf(*mv["L"](*Cif(A, B, Cc))), lambda A, B, Cc: Cf(*mv["R"](*Cif(A, B, Cc))),
              lambda A, B, Cc: Cif(*mv["L"](*Cf(A, B, Cc))), lambda A, B, Cc: Cif(*mv["R"](*Cf(A, B, Cc)))):
        i, ok = find(*f(X, Y, Z)); assert ok.all(); main6.append(i)
    seat6 = [imgs[nm] for nm in ("L", "R", "Li", "Ri", "X", "Xi")]
    same = (np.sort(np.stack(main6), axis=0) == np.sort(np.stack(seat6), axis=0)).all()
    a, b, c = X // 3, Y // 3, Z // 3
    eps = (a * b * c) % 3
    plus, minus = eps == 1, eps == 2
    swap = all(((eps[i] != eps).all()) for i in main6)
    fixed = (X == Y) & (Y == Z)
    log("    A4: |O+| = %d, |O-| = %d; every move exchanges them: %s; main's six moves = the seat's six: %s; C fixes %d, of which in O+: %d" % (
        plus.sum(), minus.sum(), swap, bool(same), fixed.sum(), (fixed & plus).sum()))
    if k >= 3:
        def gam(A, B, Cc):
            return ((((B % N) % 27) ** 2 - ((A % N) % 27) ** 2) // 27) % 3
        s1 = lambda A, B, Cc: ((B * Cc - A) % N, B, Cc); s2 = lambda A, B, Cc: (A, (A * Cc - B) % N, Cc); s3 = lambda A, B, Cc: (A, B, (A * B - Cc) % N)
        Xm, Ym, Zm = X[minus], Y[minus], Z[minus]
        g0 = gam(Xm, Ym, Zm)
        gC = (gam(*Cf(Xm, Ym, Zm)) - g0) % 3 == 1
        g23 = (gam(*s2(*s3(Xm, Ym, Zm))) - g0) % 3 == 1
        g31 = (gam(*s3(*s1(Xm, Ym, Zm))) - g0) % 3 == 1
        g12 = (gam(*s1(*s2(Xm, Ym, Zm))) - g0) % 3 == 1
        Xp, Yp, Zp = X[plus], Y[plus], Z[plus]
        around = np.sort(np.stack([gam(*f(Xp, Yp, Zp)) for f in mv.values()]), axis=0)
        nullv = (around == np.array([0, 0, 1, 1, 2, 2])[:, None]).all()
        log("    A4: gamma + 1 under C on O-: %s; under s2s3, s3s1, s1s2: %s, %s, %s; around each point of O+ the gamma values are 0,0,1,1,2,2: %s" % (
            gC.all(), g23.all(), g31.all(), g12.all(), bool(nullv)))
    if k >= 4:
        sc, top = 3 ** (k - 2), 3 ** (k - 1)
        Xm, Ym, Zm = X[minus], Y[minus], Z[minus]
        def J(A, B, Cc):
            a0, a1, a2 = (A // 3) % 9, (B // 3) % 9, (Cc // 3) % 9
            return ((A + sc * INV9[a0]) % N, (B + sc * INV9[a1]) % N, (Cc + sc * ((INV9[a2] - 3 * a2) % 9)) % N)
        def tau(A, B, Cc):
            return (A, (B + top * ((B // 3) % 3)) % N, (Cc + 2 * top * ((Cc // 3) % 3)) % N)
        jX, jY, jZ = J(Xm, Ym, Zm)
        ij, okj = find(jX, jY, jZ)
        keeps = okj.all() and (eps[ij] == 2).all() and len(np.unique(ij)) == len(ij)
        comm = True
        for f, g in ((s1, s2), (s2, s3), (s3, s1), (s2, s1), (s3, s2), (s1, s3)):
            lhs = J(*f(*g(Xm, Ym, Zm))); rhs = f(*g(jX, jY, jZ))
            comm = comm and all((l % N == r % N).all() for l, r in zip(lhs, rhs))
        lhs = J(*Cf(Xm, Ym, Zm)); rhs = tau(*Cf(jX, jY, jZ))
        jc = all((l % N == r % N).all() for l, r in zip(lhs, rhs))
        log("    A4: J_k a bijection of O-: %s; commutes with all six s_i s_j: %s; J_k C = tau C J_k: %s" % (keeps, comm, jc))
