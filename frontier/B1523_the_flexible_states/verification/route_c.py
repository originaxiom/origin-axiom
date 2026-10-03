#!/usr/bin/env python3
"""B1523 -- route C (the complex form): the same two questions as route R, with no code in common.

  - presentation: SnapPy's UNSIMPLIFIED presentation (the face-pairing generators of the ideal triangulation);
  - the 4-dimensional representation: X -> A X A^dagger on M_2(C) = C^4 (basis E11, E12, E21, E22), i.e. the Kronecker
    product A (x) conj(A), which preserves q(X) = det X; complexified, sl(4, C) = so(q) + v(q) with
    v(q) = {Y : Y^T Q = Q Y, tr Y = 0} (Q the Gram matrix of q), 9-dimensional over C;
  - H^1 by Fox calculus written as right-to-left accumulation of the free derivative, ranks by complex SVD;
  - the cusp frame from the kernel of the parabolic meridian's nilpotent part (not from a closed formula), and the normaliser built in
    M_2(C): z -> alpha z is N (x) conj(N) with N = diag(sqrt(alpha), 1/sqrt(alpha)); z -> conj(z) is X -> X^T, the
    permutation of E12 and E21.
Dimensions over C of the complexified modules equal the real dimensions of route R's real modules.
Usage: python3 route_c.py NAME [NAME ...]"""
import json
import sys

import mpmath as mp

mp.mp.dps = 60
ZERO = mp.mpf(10) ** -30

Q = mp.matrix([[0, 0, 0, mp.mpf(1) / 2], [0, 0, -mp.mpf(1) / 2, 0], [0, -mp.mpf(1) / 2, 0, 0], [mp.mpf(1) / 2, 0, 0, 0]])
QI = mp.inverse(Q)
SWAP = mp.matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])


def parse(x):
    return mp.mpf(str(x).replace(" ", ""))


def sl2(S):
    return mp.matrix([[mp.mpc(parse(S[i, j].real()), parse(S[i, j].imag())) for j in range(2)] for i in range(2)])


def kron_bar(A):
    """X -> A X A^dagger on M_2(C), row-major vec: entry ((i,j),(k,l)) = A[i,k] conj(A[j,l])"""
    K = mp.matrix(4, 4)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    K[2 * i + j, 2 * k + l] = A[i, k] * mp.conj(A[j, l])
    return K


def tr(A):
    s = mp.mpc(0)
    for i in range(A.rows):
        s += A[i, i]
    return s


def basis(kind):
    out = []
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    if kind == "so":
        for (i, j) in pairs:
            A = mp.matrix(4, 4); A[i, j] = 1; A[j, i] = -1
            out.append(QI * A)
        return out
    # v(q): Q^-1 S, S symmetric with tr(Q^-1 S) = 0
    cands = []
    for (i, j) in pairs:
        S = mp.matrix(4, 4); S[i, j] = 1; S[j, i] = 1
        cands.append(QI * S)
    for i in range(4):
        S = mp.matrix(4, 4); S[i, i] = 1
        cands.append(QI * S)
    # impose tracelessness: the traces of the candidates; keep combinations with zero trace
    t = [tr(Y) for Y in cands]
    pivot = next(k for k, x in enumerate(t) if abs(x) > ZERO)
    for k, Y in enumerate(cands):
        if k == pivot:
            continue
        out.append(Y - (t[k] / t[pivot]) * cands[pivot])
    return out


BASIS = {"v": basis("v"), "so": basis("so")}
assert len(BASIS["v"]) == 9 and len(BASIS["so"]) == 6
for kind, B in BASIS.items():
    for Y in B:
        assert abs(tr(Y)) < ZERO
        if kind == "v":
            assert mp.mnorm(Y.T * Q - Q * Y, 1) < ZERO
        else:
            assert mp.mnorm(Y.T * Q + Q * Y, 1) < ZERO
GRAMI = {k: mp.inverse(mp.matrix([[tr(E * F) for F in B] for E in B])) for k, B in BASIS.items()}


def act(K, kind):
    if kind == "triv":
        return mp.matrix([[1]])
    B, Gi = BASIS[kind], GRAMI[kind]
    Ki = mp.inverse(K)
    n = len(B)
    M = mp.matrix(n, n)
    for col, E in enumerate(B):
        Y = K * E * Ki
        pair = [tr(F * Y) for F in B]
        for row in range(n):
            M[row, col] = mp.fsum(Gi[row, m] * pair[m] for m in range(n))
    return M


def dim_of(kind):
    return {"v": 9, "so": 6, "triv": 1}[kind]


def kernel(A):
    rows, cols = A.rows, A.cols
    if rows < cols:
        P = mp.matrix(cols, cols)
        for i in range(rows):
            for j in range(cols):
                P[i, j] = A[i, j]
        A = P
    U, S, V = mp.svd_c(A)
    s = [abs(S[i]) for i in range(min(A.rows, cols))]
    r = sum(1 for x in s if x > ZERO)
    vecs = [mp.matrix([mp.conj(V[i, j]) for j in range(cols)]) for i in range(r, cols)]
    return vecs, r, (min([x for x in s if x > ZERO], default=None)), max([x for x in s if x <= ZERO], default=mp.mpf(0))


def srank(A):
    if A.rows == 0 or A.cols == 0:
        return 0, None, mp.mpf(0)
    s = sorted([abs(x) for x in mp.svd_c(A, compute_uv=False)], reverse=True)
    r = sum(1 for x in s if x > ZERO)
    return r, (min([x for x in s if x > ZERO], default=None)), max([x for x in s if x <= ZERO], default=mp.mpf(0))


class Pres:
    def __init__(self, name):
        import snappy
        M = snappy.ManifoldHP(name)
        G = M.fundamental_group(simplify_presentation=False)
        self.G = G
        self.gens = list(G.generators())
        self.rels = list(G.relators())
        self.mer, self.lon = G.peripheral_curves()[0]
        self.K = {}
        for g in self.gens:
            A = sl2(G.SL2C(g))
            self.K[g] = kron_bar(A)
            self.K[g.upper()] = mp.inverse(self.K[g])
        self.err = max(mp.mnorm(self.word(r) - mp.eye(4), 1) for r in self.rels)

    def word(self, w):
        X = mp.eye(4)
        for c in w:
            X = X * self.K[c]
        return X

    def fox_rows(self, kind):
        """right-to-left: d(w)/dg = sum over occurrences of (prefix) * d(letter)/dg; accumulated as w is read backwards"""
        n = dim_of(kind)
        mats = []
        for r in self.rels:
            blocks = {g: mp.matrix(n, n) for g in self.gens}
            # prefixes, computed once
            pref = [mp.eye(4)]
            for c in r:
                pref.append(pref[-1] * self.K[c])
            for pos, c in enumerate(r):
                g = c.lower()
                if c.islower():
                    blocks[g] = blocks[g] + act(pref[pos], kind)
                else:
                    blocks[g] = blocks[g] - act(pref[pos + 1], kind)
            mats.append(blocks)
        F = mp.matrix(n * len(self.rels), n * len(self.gens))
        for a, blocks in enumerate(mats):
            for b, g in enumerate(self.gens):
                for i in range(n):
                    for j in range(n):
                        F[a * n + i, b * n + j] = blocks[g][i, j]
        return F

    def cob(self, kind):
        n = dim_of(kind)
        B = mp.matrix(n * len(self.gens), n)
        for b, g in enumerate(self.gens):
            A = act(self.K[g], kind)
            for i in range(n):
                for j in range(n):
                    B[b * n + i, j] = A[i, j] - (1 if i == j else 0)
        return B

    def cohomology(self, kind):
        n = dim_of(kind)
        Z, fr, fk, fd = kernel(self.fox_rows(kind))
        Bm = self.cob(kind)
        br, bk, bd = srank(Bm)
        info = {"dim": len(Z) - br, "Z1": len(Z), "B1": br, "H0": n - br,
                "fox margin": [float(fk) if fk is not None else None, float(fd)],
                "coboundary margin": [float(bk) if bk is not None else None, float(bd)]}
        return info, Z, Bm

    def value(self, z, w, kind="v"):
        n = dim_of(kind)
        gval = {g: mp.matrix([z[b * n + i] for i in range(n)]) for b, g in enumerate(self.gens)}
        acc = mp.matrix(n, 1)
        P = mp.eye(4)
        for c in w:
            g = c.lower()
            if c.islower():
                acc = acc + act(P, kind) * gval[g]
                P = P * self.K[c]
            else:
                P = P * self.K[c]
                acc = acc - act(P, kind) * gval[g]
        return acc


def cols(vs, n):
    M = mp.matrix(n, len(vs))
    for j, v in enumerate(vs):
        for i in range(n):
            M[i, j] = v[i]
    return M


def hdot(a, b):
    return mp.fsum(mp.conj(a[i]) * b[i] for i in range(a.rows))


def mpow(A, k):
    n = A.rows
    if k >= 0:
        X = mp.eye(n)
        for _ in range(k):
            X = X * A
        return X
    Ai = mp.inverse(A)
    X = mp.eye(n)
    for _ in range(-k):
        X = X * Ai
    return X


def geo_sum(A, k):
    """c(g^k) = S_k c(g): S_k = 1 + A + ... + A^(k-1) for k >= 0, -(A^-1 + ... + A^k) for k < 0"""
    n = A.rows
    S = mp.matrix(n, n)
    if k >= 0:
        for e in range(k):
            S = S + mpow(A, e)
    else:
        for e in range(1, -k + 1):
            S = S - mpow(A, -e)
    return S


def frame(P, name=""):
    """the cusp at infinity: S (det 1) with S(infinity) = the meridian's fixed point, and the translations t_mu, t_lambda there"""
    # the cusp frame: the meridian's fixed point (x : y) is the kernel of the nilpotent B = A - sgn 1, read from the larger of
    # B's two rows (a first row that vanishes -- a meridian fixing 0 -- must not be used: sm:B1523 ERROR_LEDGER); S is the
    # unitary-up-to-scale frame [[x, -conj(y)/n], [y, conj(x)/n]], n = |x|^2 + |y|^2, so S(infinity) = x / y and det S = 1
    Am = sl2(P.G.SL2C(P.mer))
    sgn = 1 if mp.re(Am[0, 0] + Am[1, 1]) > 0 else -1
    Bq = Am - sgn * mp.eye(2)
    if abs(Bq[0, 0]) + abs(Bq[0, 1]) >= abs(Bq[1, 0]) + abs(Bq[1, 1]):
        x, y = Bq[0, 1], -Bq[0, 0]
    else:
        x, y = -Bq[1, 1], Bq[1, 0]
    nrm = abs(x) ** 2 + abs(y) ** 2
    assert nrm > ZERO, "the meridian is not a parabolic"
    S = mp.matrix([[x, -mp.conj(y) / nrm], [y, mp.conj(x) / nrm]])
    Si = mp.inverse(S)
    trans = {}
    for key, w in (("mu", P.mer), ("lambda", P.lon)):
        X = Si * sl2(P.G.SL2C(w)) * S
        trans[key] = X[0, 1] / X[0, 0]
        trans[key + " check"] = abs(X[1, 0])
        assert abs(X[1, 0]) < ZERO and abs(abs(X[0, 0]) - 1) < ZERO, (name, key, "the frame does not put the cusp at infinity")
    return S, Si, trans


def pword(P, a, b):
    """the word mu^a lambda^b in the presentation's letters"""
    def inv(w):
        return "".join(ch.swapcase() for ch in w[::-1])
    return (P.mer if a >= 0 else inv(P.mer)) * abs(a) + (P.lon if b >= 0 else inv(P.lon)) * abs(b)


def record(name):
    import snappy
    P = Pres(name)
    out = {"name": name, "generators": len(P.gens), "relators": len(P.rels), "relator error": float(P.err)}
    for kind in ("triv", "so"):
        info, _, _ = P.cohomology(kind)
        out["H1 " + kind] = info
    info, Z, Bm = P.cohomology("v")
    out["H1 v"] = info
    out["rigid rel cusp"] = info["dim"] == 1
    if info["dim"] != 1:
        return out
    n = 9
    N = n * len(P.gens)
    Zm = cols(Z, N)
    K, _, _, _ = kernel(Bm.H * Zm)
    z = Zm * K[0]
    S, Si, trans = frame(P, name)
    KS = kron_bar(Si)
    KSi = mp.inverse(KS)
    Kmu = KS * P.word(P.mer) * KSi
    Klam = KS * P.word(P.lon) * KSi
    Amu, Alam = act(Kmu, "v"), act(Klam, "v")
    AS = act(KS, "v")
    cmu = AS * P.value(z, P.mer)
    clam = AS * P.value(z, P.lon)
    # H^1(P; v) in this frame
    Fp = mp.matrix(n, 2 * n)
    Bp = mp.matrix(2 * n, n)
    for i in range(n):
        for j in range(n):
            Fp[i, j] = (1 if i == j else 0) - Alam[i, j]
            Fp[i, n + j] = Amu[i, j] - (1 if i == j else 0)
            Bp[i, j] = Amu[i, j] - (1 if i == j else 0)
            Bp[n + i, j] = Alam[i, j] - (1 if i == j else 0)
    Zp, _, _, _ = kernel(Fp)
    Zpm = cols(Zp, 2 * n)
    Kp, _, _, _ = kernel(Bp.H * Zpm)
    Qb = [Zpm * k for k in Kp]
    Qb = [q / mp.sqrt(mp.re(hdot(q, q))) for q in Qb]
    cvec = mp.matrix([cmu[i] for i in range(n)] + [clam[i] for i in range(n)])
    coords = mp.matrix([hdot(q, cvec) for q in Qb])
    # the slopes (Heusener-Porti Def. 7.1), by a different test from route R's: c(g) is in the image of Ad g - 1 iff appending it
    # as a column does not raise the rank; recorded as the ratio of the new smallest singular value to |c(g)|
    def slope_test(A, c):
        B = A - mp.eye(n)
        r0, _, _ = srank(B)
        Aug = mp.matrix(n, n + 1)
        for i in range(n):
            for j in range(n):
                Aug[i, j] = B[i, j]
            Aug[i, n] = c[i]
        sv = sorted([abs(x) for x in mp.svd_c(Aug, compute_uv=False)], reverse=True)
        # rank r0 + 1 iff the (r0 + 1)-th singular value is nonzero
        return sv[r0] / mp.sqrt(mp.re(hdot(c, c)))
    out["slope test"] = {"fibre boundary mu": float(slope_test(Amu, cmu)), "section lambda": float(slope_test(Alam, clam))}

    def pullback(vec, C, Kg):
        Ai = act(mp.inverse(Kg), "v")
        a = mp.matrix([vec[i] for i in range(n)])
        b = mp.matrix([vec[n + i] for i in range(n)])
        im = Ai * (geo_sum(Amu, C[0][0]) * a + mpow(Amu, C[0][0]) * geo_sum(Alam, C[1][0]) * b)
        il = Ai * (geo_sum(Amu, C[0][1]) * a + mpow(Amu, C[0][1]) * geo_sum(Alam, C[1][1]) * b)
        return mp.matrix([im[i] for i in range(n)] + [il[i] for i in range(n)])

    def matrix_on_h1p(C, Kg):
        Mb = mp.matrix(len(Qb), len(Qb))
        for j, q in enumerate(Qb):
            w = pullback(q, C, Kg)
            for i, qq in enumerate(Qb):
                Mb[i, j] = hdot(qq, w)
        return Mb
    shift = mp.mpf("0.37") * trans["mu"] + mp.mpf("0.81") * trans["lambda"]
    Mt = matrix_on_h1p([[1, 0], [0, 1]], kron_bar(mp.matrix([[1, shift], [0, 1]])))
    out["translation acts trivially (defect)"] = float(mp.mnorm(Mt - mp.eye(len(Qb)), 1))
    out["cusp"] = {"H1(P; v)": len(Qb), "class in H1(P; v) (norm, relative)": float(mp.sqrt(mp.re(hdot(coords, coords)) / mp.re(hdot(cvec, cvec)))),
                   "parabolic check": [float(trans["mu check"]), float(trans["lambda check"])],
                   "shape t_lambda / t_mu": [float(mp.re(trans["lambda"] / trans["mu"])), float(mp.im(trans["lambda"] / trans["mu"]))]}
    Mlo = snappy.Manifold(name)
    res = []
    for I in Mlo.is_isometric_to(Mlo, return_isometries=True):
        C = [[int(v) for v in row] for row in I.cusp_maps()[0]]
        d = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        tm, tl = trans["mu"], trans["lambda"]
        img_mu, img_lam = C[0][0] * tm + C[1][0] * tl, C[0][1] * tm + C[1][1] * tl
        if d == 1:
            al = img_mu / tm
            lat = abs(al * tl - img_lam)
            Kg = kron_bar(mp.matrix([[mp.sqrt(al), 0], [0, 1 / mp.sqrt(al)]]))
        else:
            al = img_mu / mp.conj(tm)
            lat = abs(al * mp.conj(tl) - img_lam)
            Kg = kron_bar(mp.matrix([[mp.sqrt(al), 0], [0, 1 / mp.sqrt(al)]])) * SWAP
        Kgi = mp.inverse(Kg)
        # the normaliser must carry the frame's cusp group onto itself as the cusp map says
        norm_err = max(mp.mnorm(Kg * Kmu * Kgi - KS * P.word(pword(P, C[0][0], C[1][0])) * KSi, 1),
                       mp.mnorm(Kg * Klam * Kgi - KS * P.word(pword(P, C[0][1], C[1][1])) * KSi, 1))
        Agi = act(Kgi, "v")
        bmu = Agi * (geo_sum(Amu, C[0][0]) * cmu + mpow(Amu, C[0][0]) * geo_sum(Alam, C[1][0]) * clam)
        blam = Agi * (geo_sum(Amu, C[0][1]) * cmu + mpow(Amu, C[0][1]) * geo_sum(Alam, C[1][1]) * clam)
        bvec = mp.matrix([bmu[i] for i in range(n)] + [blam[i] for i in range(n)])
        bc = mp.matrix([hdot(q, bvec) for q in Qb])
        eps = hdot(coords, bc) / hdot(coords, coords)
        resid = mp.sqrt(mp.re(hdot(bc - eps * coords, bc - eps * coords)) / mp.re(hdot(coords, coords)))
        Mb = matrix_on_h1p(C, Kg)
        tr2, dt2 = Mb[0, 0] + Mb[1, 1], Mb[0, 0] * Mb[1, 1] - Mb[0, 1] * Mb[1, 0]
        res.append({"cusp map": C, "det": d, "inverts the fibre boundary": C[0][0] == -1 and C[1][0] == 0,
                    "eps": [float(mp.re(eps)), float(mp.im(eps))], "residual": float(resid), "lattice check": float(lat),
                    "normaliser check": float(norm_err),
                    "on H1(P; v)": {"trace": [float(mp.re(tr2)), float(mp.im(tr2))], "det": [float(mp.re(dt2)), float(mp.im(dt2))]}})
    out["isometries"] = res
    out["family-dualising isometry"] = any(abs(r["eps"][0] + 1) < 1e-6 and abs(r["eps"][1]) < 1e-6 for r in res)
    return out


if __name__ == "__main__":
    for name in sys.argv[1:]:
        print(json.dumps(record(name), indent=1))
