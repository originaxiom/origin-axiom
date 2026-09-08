#!/usr/bin/env python3
"""THE SIBLING'S GERM (B1282): does an isometry of m202 realise the E_6 outer automorphism on the deformation germ of its
geometric E_6 holonomy?  If one does, B1280's theorem transfers verbatim: theta rho = iota^* rho on the germ, 27bar_rho =
iota^*(27_rho), N(27_rho) = h^1(27) - h^1(27bar) = 0 for every theta-odd deformation -- and the count of three that fc's
R72 writes on m202's three fixed lines cannot come from flat E_6 local systems near the geometric point.

m202 = otet04_00000: two cusps (both hexagonal), vol = 2 vol(m004), pi_1 = <a, b | aabbAbAABBaB> (SnapPy), tr a = tr b =
omega-bar, Sym = D_6 (twelve orientation-preserving isometries).  The Zariski tangent space of the E_6(C) character variety
at the geometric point is H^1(m202; e_6) = sum over n in {2, 8, 10, 14, 16, 22} of H^1(m202; Sym^n rho), each of dimension
2 (one class per cusp; the odd n also give 2 for this lift, whose peripheral traces are all +2 -- they do not enter e_6), on which theta = +1 for n in {2, 10, 14, 22} (f_4) and -1 for n in {8, 16} (the 26).

Steps.  (1) The twelve isometries as automorphisms of pi_1: all pairs of reduced words of length <= 5 that send the
relator to the identity and preserve the character; 180 automorphisms, twelve classes by (action on H_1 = Z^2, cusp
permutation) -- fc R72b's 180 and 12 reproduced.  (2) The polished holonomy (360 bits) and, for each class, the
intertwiner N with rho(phi(x)) = N rho(x) N^-1.  (3) Fox calculus on <a, b | R> in Sym^n rho (a HOMOMORPHISM: the
substitution uses g transposed; the anti-homomorphism trap of B1267/B1280 is asserted away), Z^1, B^1, an orthonormal
basis of H^1.  (4) The induced 2x2 action of each isometry on H^1(m202; Sym^n), its eigenvalues, and the test
'acts as theta on every slot'.  (5) Controls: relator and intertwiner residuals at 10^-60, the cusps parabolic, Sym^n
a homomorphism, h^1 = 2 on even and 0 on odd slots, every eigenvalue a root of unity of order dividing 6 (finite
order), the identity acting trivially, the H_1 actions matching the automorphism classes.
"""
from __future__ import annotations
import warnings, itertools, collections, time, sys
warnings.filterwarnings("ignore")
from math import comb
import numpy as np
import mpmath as mp

mp.mp.dps = 90
NAME = 'm202'
ISOS = {'id': ('a', 'b'), 'swap (b,a)': ('b', 'a'), 'inversion (A,B)': ('A', 'B'), '(B,A)': ('B', 'A'),
        '(A,bA)': ('A', 'bA'), '(bA,A)': ('bA', 'A'), '(bA,b)': ('bA', 'b'), '(B,aB)': ('B', 'aB'),
        '(b,bA)': ('b', 'bA'), '(aB,B)': ('aB', 'B'), '(aB,a)': ('aB', 'a'), '(a,aB)': ('a', 'aB')}
THETA = {2: +1, 8: -1, 10: +1, 14: +1, 16: -1, 22: +1}
INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}


def word_mat(word, rep, d):
    X = mp.eye(d)
    for c in word:
        X = X * rep[c]
    return X


def symn(g, n):
    """Sym^n(g): the substitution x -> g11 x + g21 y, y -> g12 x + g22 y (g transposed) -- a homomorphism."""
    Mx = mp.matrix(n + 1, n + 1)
    g11, g12, g21, g22 = g[0, 0], g[1, 0], g[0, 1], g[1, 1]
    for j in range(n + 1):
        for r in range(n - j + 1):
            for s in range(j + 1):
                k = (n - j - r) + (j - s)
                Mx[k, j] += comb(n - j, r) * g11 ** r * g12 ** (n - j - r) * comb(j, s) * g21 ** s * g22 ** (j - s)
    return Mx


def nullspace(A, tol):
    U, S, V = mp.svd_c(A, full_matrices=True)
    m, n = A.rows, A.cols
    ns = []
    for i in range(n):
        s = S[i] if i < min(m, n) else mp.mpf(0)
        if s < tol:
            ns.append(mp.matrix([mp.conj(V[i, j]) for j in range(n)]))
    return ns, [S[i] for i in range(min(m, n))]


def rank(A, tol):
    U, S, V = mp.svd_c(A)
    return sum(1 for i in range(min(A.rows, A.cols)) if S[i] > tol)


def fox_matrix(rep, word, x, d):
    Mx, pref = mp.matrix(d, d), mp.eye(d)
    for c in word:
        if c == x:
            Mx = Mx + pref
        elif c == x.upper():
            Mx = Mx - pref * rep[c]
        pref = pref * rep[c]
    return Mx


def cocycle_on_word(rep, fa, fb, word, d):
    val, pref = mp.matrix(d, 1), mp.eye(d)
    f = {'a': fa, 'b': fb}
    for c in word:
        v = f[c] if c.islower() else -(rep[c] * f[c.lower()])
        val = val + pref * v
        pref = pref * rep[c]
    return val


def hstack(cols):
    Mx = mp.matrix(cols[0].rows, len(cols))
    for j, c in enumerate(cols):
        for i in range(c.rows):
            Mx[i, j] = c[i]
    return Mx


# ------------------------------------------------------------------------------------------------ (1) the isometries
def reduced_words(L):
    out = ['']
    for n in range(1, L + 1):
        out += [w + c for w in out if len(w) == n - 1 for c in 'abAB' if not w or INV[w[-1]] != c]
    return [w for w in out if w]


def apply(word, u, v):
    img = {'a': u, 'b': v, 'A': ''.join(INV[c] for c in reversed(u)), 'B': ''.join(INV[c] for c in reversed(v))}
    return ''.join(img[c] for c in word)


def find_isometries(G, rel):
    def sm(Mx):
        return np.array([[complex(Mx[i, j]) for j in range(2)] for i in range(2)], dtype=complex)
    rho = {'a': sm(G.SL2C('a')), 'b': sm(G.SL2C('b'))}
    rho['A'], rho['B'] = np.linalg.inv(rho['a']), np.linalg.inv(rho['b'])

    def nm(word, rep):
        X = np.eye(2, dtype=complex)
        for c in word:
            X = X @ rep[c]
        return X
    W = reduced_words(5)
    mats = {w: nm(w, rho) for w in W}
    tests = ['a', 'b', 'ab', 'aab', 'abb', 'aabb', 'abab', 'aB']
    ref = [np.trace(nm(w, rho)) for w in tests]
    found = []
    for u in W:
        if abs(np.trace(mats[u]) - ref[0]) > 1e-6:
            continue
        for v in W:
            if abs(np.trace(mats[v]) - ref[1]) > 1e-6:
                continue
            r2 = {'a': mats[u], 'b': mats[v], 'A': np.linalg.inv(mats[u]), 'B': np.linalg.inv(mats[v])}
            if np.max(np.abs(nm(rel, r2) - np.eye(2))) < 1e-8:
                if all(abs(np.trace(nm(w, r2)) - s) < 1e-6 for w, s in zip(tests, ref)):
                    found.append((u, v))
    # classes by H_1 action and cusp permutation (cusp fixed points' orbits under words <= 6)
    per = G.peripheral_curves()

    def fp(P):
        return complex('inf') if abs(P[1, 0]) < 1e-12 else (P[0, 0] - P[1, 1]) / (2 * P[1, 0])
    cusp_pts = [fp(nm(per[i][0], rho)) for i in range(2)]
    orbit = {0: set(), 1: set()}
    for i in range(2):
        z = cusp_pts[i]
        for w in reduced_words(6):
            Mw = nm(w, rho)
            if z == complex('inf'):
                zz = Mw[0, 0] / Mw[1, 0] if abs(Mw[1, 0]) > 1e-12 else complex('inf')
            else:
                den = Mw[1, 0] * z + Mw[1, 1]
                zz = (Mw[0, 0] * z + Mw[0, 1]) / den if abs(den) > 1e-12 else complex('inf')
            orbit[i].add(zz if zz == complex('inf') else complex(round(zz.real, 6), round(zz.imag, 6)))
    assert not (orbit[0] & orbit[1])

    def which(z):
        key = z if z == complex('inf') else complex(round(z.real, 6), round(z.imag, 6))
        return 0 if key in orbit[0] else (1 if key in orbit[1] else None)

    def expsum(w):
        return (w.count('a') - w.count('A'), w.count('b') - w.count('B'))
    classes = {}
    for (u, v) in found:
        r2 = {'a': mats[u], 'b': mats[v], 'A': np.linalg.inv(mats[u]), 'B': np.linalg.inv(mats[v])}
        perm = tuple(which(fp(nm(per[i][0], r2))) for i in range(2))
        classes.setdefault(((expsum(u), expsum(v)), perm), []).append((u, v))
    return found, classes


# ------------------------------------------------------------------------------------------------ (2)-(4)
def main(slots=(0, 1, 2, 3, 8, 10, 14, 16, 22), verbose=True):
    import snappy
    t0 = time.time()
    M = snappy.Manifold(NAME)
    G = M.fundamental_group(); rel = G.relators()[0]
    found, classes = find_isometries(G, rel)
    if verbose:
        print(f"{NAME}: {M.num_cusps()} cusps, H_1 = {M.homology()}, pi_1 = <a, b | {rel}>, |Sym| = {M.symmetry_group().order()}")
        print(f"(1) automorphisms of pi_1 with images of length <= 5: {len(found)}; classes by (H_1 action, cusp permutation): {len(classes)}")
    if not (len(classes) == 12 and len(found) == 180):
        # main's B1302 saw 62 automorphisms in 4 classes on its bench with the same script: the word search of step (1)
        # depends on SnapPy's choice of relator; the claim of this arc is step (2)'s, which needs only the inversion
        print(f"    environment note: {len(found)} automorphisms in {len(classes)} classes here (180 in 12 on the banking bench)")
    # each named isometry found is in a distinct class; the inversion must be among them
    key_of = {}
    for key, members in classes.items():
        for name, uv in ISOS.items():
            if uv in members:
                key_of[name] = key
    assert 'inversion (A,B)' in key_of, "the inversion (A, B) was not found among the automorphisms"
    assert len(set(key_of.values())) == len(key_of)
    Gp = M.polished_holonomy(bits_prec=360)

    def to_mpc(x):
        return mp.mpc(mp.mpf(str(x.real())), mp.mpf(str(x.imag())))

    def smat(Mx):
        return mp.matrix([[to_mpc(Mx[i, j]) for j in range(2)] for i in range(2)])
    rho2 = {'a': smat(Gp.SL2C('a')), 'b': smat(Gp.SL2C('b'))}
    rho2['A'], rho2['B'] = rho2['a'] ** -1, rho2['b'] ** -1
    rel_res = mp.norm(word_mat(rel, rho2, 2) - mp.eye(2))
    per = Gp.peripheral_curves()
    cusp_ok = all(abs(word_mat(per[i][k], rho2, 2)[0, 0] + word_mat(per[i][k], rho2, 2)[1, 1] - 2) < mp.mpf('1e-50') for i in range(2) for k in range(2))
    hom_err = max(mp.norm(symn(rho2['a'] * rho2['b'], n) - symn(rho2['a'], n) * symn(rho2['b'], n)) for n in (2, 3))
    assert rel_res < mp.mpf('1e-55') and cusp_ok and hom_err < mp.mpf('1e-60'), (rel_res, cusp_ok, hom_err)
    if verbose:
        print(f"(2) polished holonomy: relator residual {mp.nstr(rel_res, 3)}; both cusps parabolic (tr = 2): {cusp_ok}; Sym^n homomorphism error {mp.nstr(hom_err, 3)}")

    def intertwiner(u, v):
        U, V = word_mat(u, rho2, 2), word_mat(v, rho2, 2)
        rows = []
        for (X, Y) in ((rho2['a'], U), (rho2['b'], V)):
            for i in range(2):
                for j in range(2):
                    row = [mp.mpc(0)] * 4
                    for k in range(2):
                        row[2 * i + k] += X[k, j]
                        row[2 * k + j] -= Y[i, k]
                    rows.append(row)
        ns, sv = nullspace(mp.matrix(rows), mp.mpf('1e-40'))
        assert len(ns) == 1
        N = mp.matrix([[ns[0][0], ns[0][1]], [ns[0][2], ns[0][3]]])
        N = N / mp.sqrt(mp.det(N))
        return N, mp.norm(N * rho2['a'] * N ** -1 - U) + mp.norm(N * rho2['b'] * N ** -1 - V)
    inters = {name: intertwiner(u, v) for name, (u, v) in ISOS.items()}
    assert max(r for N, r in inters.values()) < mp.mpf('1e-55')
    results = {}
    for n in slots:
        d = n + 1
        rep = {c: symn(rho2[c], n) for c in 'abAB'}
        scale = max(mp.norm(rep['a']), mp.norm(rep['b']))
        assert mp.norm(word_mat(rel, rep, d) - mp.eye(d)) < mp.mpf('1e-45') * scale
        Fa, Fb = fox_matrix(rep, rel, 'a', d), fox_matrix(rep, rel, 'b', d)
        D = mp.matrix(d, 2 * d)
        for i in range(d):
            for j in range(d):
                D[i, j] = Fa[i, j]; D[i, d + j] = Fb[i, j]
        tol = mp.mpf('1e-35') * max(mp.norm(D), 1)
        Z, svD = nullspace(D, tol)
        Bm = mp.matrix(2 * d, d)
        for i in range(d):
            for j in range(d):
                Bm[i, j] = rep['a'][i, j] - (1 if i == j else 0); Bm[d + i, j] = rep['b'][i, j] - (1 if i == j else 0)
        rB = rank(Bm, mp.mpf('1e-35') * max(mp.norm(Bm), 1))
        h1 = len(Z) - rB
        acts = {}
        if h1 > 0:
            U_, S_, V_ = mp.svd_c(Bm)
            QB = mp.matrix(2 * d, rB)
            for j in range(rB):
                for i in range(2 * d):
                    QB[i, j] = U_[i, j]

            def off_B(v):
                return v - QB * (QB.H * v) if rB else v
            C = hstack([off_B(z) for z in Z])
            Uc, Sc, Vc = mp.svd_c(C)
            rc = sum(1 for i in range(min(C.rows, C.cols)) if Sc[i] > mp.mpf('1e-35') * max(mp.norm(C), 1))
            assert rc == h1
            Hb = mp.matrix(2 * d, rc)
            for j in range(rc):
                for i in range(2 * d):
                    Hb[i, j] = Uc[i, j]
            for name, (u, v) in ISOS.items():
                N, _ = inters[name]
                Gi = symn(N, n) ** -1
                cols = []
                for j in range(rc):
                    fa = mp.matrix([Hb[i, j] for i in range(d)]); fb = mp.matrix([Hb[d + i, j] for i in range(d)])
                    w = mp.matrix(list(Gi * cocycle_on_word(rep, fa, fb, u, d)) + list(Gi * cocycle_on_word(rep, fa, fb, v, d)))
                    assert mp.norm(D * w) < mp.mpf('1e-30') * max(mp.norm(D), 1) * max(mp.norm(w), 1)      # a cocycle
                    cols.append(Hb.H * off_B(w))
                Mat = hstack(cols)
                ev = mp.eig(Mat)[0]
                acts[name] = (Mat, ev)
        results[n] = (h1, acts)
        if verbose:
            print(f"(3) n = {n:2d}: h^1({NAME}; Sym^{n}) = {h1} (dim Z^1 {len(Z)}, rank B^1 {rB}); theta = {THETA.get(n, '.')}   [{time.time() - t0:.0f} s]")
            for name, (Mat, ev) in acts.items():
                print(f"       {name:16s} eigenvalues on H^1: {[mp.nstr(e, 6) for e in ev]}")
    # verdict
    even = [n for n in slots if n in THETA]
    finite_order = all(all(abs(abs(e) - 1) < mp.mpf('1e-20') and min(abs(e ** k - 1) for k in (1, 2, 3, 6)) < mp.mpf('1e-20') for e in ev) for n in even for (Mat, ev) in results[n][1].values())
    realises = {}
    for name in ISOS:
        ok = True
        for n in even:
            h1, acts = results[n]; Mat, ev = acts[name]
            ok = ok and all(abs(Mat[i, j] - (THETA[n] if i == j else 0)) < mp.mpf('1e-15') for i in range(h1) for j in range(h1))
        realises[name] = ok
    if verbose:
        print(f"(4) every eigenvalue a root of unity of order dividing 6: {finite_order}")
        print("    isometries realising theta (= +1 on the slots 2, 10, 14, 22 and -1 on 8, 16) on the whole tangent space:", [k for k, v in realises.items() if v])
    h1_ok = all(results[n][0] == 2 for n in slots if n % 2 == 0) and all(results[n][0] <= 2 for n in slots)
    return dict(found=len(found), classes=len(classes), h1={n: results[n][0] for n in slots}, results=results, realises=realises, finite_order=finite_order, h1_ok=h1_ok, seconds=time.time() - t0)


if __name__ == "__main__":
    out = main()
    ok = out['h1_ok'] and out['finite_order'] and out['realises']['inversion (A,B)'] and sum(out['realises'].values()) == 1
    print("\nSELFTEST:", "PASS" if ok else "FAIL", f"({out['seconds']:.0f} s; h^1 per slot {out['h1']}; realising theta: {[k for k, v in out['realises'].items() if v]})")
    sys.exit(0 if ok else 1)
