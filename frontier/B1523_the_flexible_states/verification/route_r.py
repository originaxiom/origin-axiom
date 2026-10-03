#!/usr/bin/env python3
"""B1523 -- route R (the real form): infinitesimal projective rigidity rel cusp, and each isometry's sign on the family's line.

For a word state's bundle M (SnapPy 'b++w' or 'b+-w'), at its complete hyperbolic structure:
  - the holonomy is SnapPy's (ManifoldHP, about 63 digits) on SnapPy's simplified presentation, sent to SO(3,1) through the
    Pauli basis of 2x2 Hermitian matrices (det = the form J = diag(1, -1, -1, -1));
  - sl(4, R) = so(3,1) + v as Gamma-modules (Johnson-Millson), v = {J S : S symmetric, tr(J S) = 0}, 9-dimensional;
  - H^1(Gamma; V) for V = v, so(3,1) and the trivial line, by Fox calculus: Z^1 = the kernel of the Fox matrix, B^1 = the image of
    u -> (g u - u)_g; a singular value below TOL counts as zero, and every decision records its margin;
  - rigid rel cusp iff dim H^1(Gamma; v) = 1 (Heusener-Porti, Cor. 5.4; Daly, Lemma 2.1); dim H^1(Gamma; so(3,1)) = 2 and
    dim H^1(Gamma; R) = 1 are controls (Thurston; b1 = 1);
  - the cusp: P = <mu, lambda> = SnapPy's (meridian, longitude), the meridian being the fibre boundary (null-homologous; checked);
    the class's restriction to H^1(P; v) (2-dimensional) and whether it is nonzero there (injectivity);
  - each isometry beta (SnapPy's cusp map C: column j = the image of the j-th peripheral curve) acts on H^1(P; v) through the
    cusp normaliser: in the frame where the cusp is at infinity, beta is z -> alpha z (det C = +1) or z -> alpha conj(z)
    (det C = -1), with alpha fixed by the lattice; beta^* c (g) = Ad(Lambda_beta)^-1 c(beta g). The restriction is injective
    in the rigid case, so the eigenvalue of beta^* on the class's line is beta's sign eps on H^1(Gamma; v); the residual of
    that eigen-equation is recorded (a line not preserved would be a bug).
A family-dualising isometry is one with eps = -1 (then D o beta acts as +1 on the v-direction and fixes the family's vacua).
Usage: python3 route_r.py NAME [NAME ...]   (prints a record per manifold)"""
import json
import math
import sys

import mpmath as mp

mp.mp.dps = 60
TOL = mp.mpf(10) ** -30          # singular values below are zeros; the holonomy carries about 63 digits

I2 = mp.matrix([[1, 0], [0, 1]])
PAULI = [mp.matrix([[1, 0], [0, 1]]), mp.matrix([[0, 1], [1, 0]]), mp.matrix([[0, -1j], [1j, 0]]), mp.matrix([[1, 0], [0, -1]])]
J = mp.diag([1, -1, -1, -1])


def num(x):
    s = str(x).replace(" ", "")
    return mp.mpf(s)


def to_mp(S):
    return mp.matrix([[mp.mpc(num(S[i, j].real()), num(S[i, j].imag())) for j in range(2)] for i in range(2)])


def dagger(A):
    return mp.matrix([[mp.conj(A[j, i]) for j in range(A.cols)] for i in range(A.rows)])


def lorentz(A):
    """the SO(3,1) image of A in SL(2, C): X -> A X A^*, in the Pauli basis"""
    L = mp.matrix(4, 4)
    for mu in range(4):
        for nu in range(4):
            L[mu, nu] = mp.re(mp.fsum((PAULI[mu] * A * PAULI[nu] * dagger(A))[i, i] for i in range(2))) / 2
    return L


def mat_trace(A):
    return mp.fsum(A[i, i] for i in range(A.rows))


# ------------------------------------------------------------------ the modules v, so(3,1) and the trivial line
def module_bases():
    v, so = [], []
    for (i, j) in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]:
        S = mp.matrix(4, 4); S[i, j] = 1; S[j, i] = 1
        v.append(J * S)
        A = mp.matrix(4, 4); A[i, j] = 1; A[j, i] = -1
        so.append(J * A)
    for k in (1, 2, 3):
        S = mp.matrix(4, 4); S[0, 0] = 1; S[k, k] = 1
        v.append(J * S)
    return {"v": v, "so": so}


BASES = module_bases()
GRAM_INV = {k: mp.inverse(mp.matrix([[mat_trace(E * F) for F in B] for E in B])) for k, B in BASES.items()}


def ad(L, key):
    """the matrix of Y -> L Y L^-1 on the module `key`, in its basis"""
    if key == "triv":
        return mp.matrix([[1]])
    B, Gi = BASES[key], GRAM_INV[key]
    Linv = J * L.T * J
    n = len(B)
    out = mp.matrix(n, n)
    for l, E in enumerate(B):
        Y = L * E * Linv
        t = [mat_trace(F * Y) for F in B]
        for k in range(n):
            out[k, l] = mp.fsum(Gi[k, m] * t[m] for m in range(n))
    return out


# ------------------------------------------------------------------ linear algebra with recorded margins
def svals(A):
    if A.rows == 0 or A.cols == 0:
        return []
    return sorted([abs(s) for s in mp.svd_r(A, compute_uv=False)], reverse=True)


def null_space(A):
    """an orthonormal basis of ker A (columns) and the margin (smallest kept, largest dropped singular value)"""
    n = A.cols
    if A.rows < n:
        Z = mp.matrix(n, n)
        for i in range(A.rows):
            for j in range(n):
                Z[i, j] = A[i, j]
        A = Z
    U, S, V = mp.svd_r(A)
    s = [abs(S[i]) for i in range(min(A.rows, n))]
    rank = sum(1 for x in s if x > TOL)
    basis = [mp.matrix([V[i, j] for j in range(n)]) for i in range(rank, n)]
    kept = min([x for x in s if x > TOL], default=None)
    dropped = max([x for x in s if x <= TOL], default=mp.mpf(0))
    return basis, rank, kept, dropped


def rank_of(A):
    s = svals(A)
    r = sum(1 for x in s if x > TOL)
    return r, (min([x for x in s if x > TOL], default=None)), max([x for x in s if x <= TOL], default=mp.mpf(0))


def stack_cols(vecs, n):
    M = mp.matrix(n, len(vecs))
    for j, v in enumerate(vecs):
        for i in range(n):
            M[i, j] = v[i]
    return M


# ------------------------------------------------------------------ the group
class Group:
    def __init__(self, name):
        import snappy
        self.name = name
        M = snappy.ManifoldHP(name)
        G = M.fundamental_group()
        self.gens = G.generators()
        self.rels = G.relators()
        self.mer, self.lon = G.peripheral_curves()[0]
        self.sl2 = {g: to_mp(G.SL2C(g)) for g in self.gens}
        self.sl2_word = lambda w: to_mp(G.SL2C(w))
        self.L = {g: lorentz(A) for g, A in self.sl2.items()}
        for g in self.gens:
            self.L[g.upper()] = J * self.L[g].T * J
        self._ad = {}
        # validation: every relator is +-1 in SL(2, C), I in SO(3,1)
        self.relator_error = max(self.word_error(r) for r in self.rels)

    def lor(self, w):
        X = mp.eye(4)
        for c in w:
            X = X * self.L[c]
        return X

    def word_error(self, w):
        X = self.lor(w)
        return mp.mnorm(X - mp.eye(4), 1)

    def adm(self, key, X):
        return ad(X, key)

    def fox(self, key):
        """the Fox matrix of the relators (rows) in the generators (columns), as block matrices on the module"""
        n = {"v": 9, "so": 6, "triv": 1}[key]
        rows = []
        for r in self.rels:
            blocks = {g: mp.matrix(n, n) for g in self.gens}
            P = mp.eye(4)
            for c in r:
                g = c.lower()
                if c.islower():
                    blocks[g] += ad(P, key)
                    P = P * self.L[c]
                else:
                    P = P * self.L[c]
                    blocks[g] -= ad(P, key)
            rows.append(blocks)
        F = mp.matrix(n * len(self.rels), n * len(self.gens))
        for a, blocks in enumerate(rows):
            for b, g in enumerate(self.gens):
                for i in range(n):
                    for j in range(n):
                        F[a * n + i, b * n + j] = blocks[g][i, j]
        return F

    def coboundary(self, key):
        n = {"v": 9, "so": 6, "triv": 1}[key]
        B = mp.matrix(n * len(self.gens), n)
        for b, g in enumerate(self.gens):
            A = ad(self.L[g], key)
            for i in range(n):
                for j in range(n):
                    B[b * n + i, j] = A[i, j] - (1 if i == j else 0)
        return B

    def h1(self, key):
        n = {"v": 9, "so": 6, "triv": 1}[key]
        F = self.fox(key)
        Z, frank, fkept, fdrop = null_space(F)
        B = self.coboundary(key)
        brank, bkept, bdrop = rank_of(B)
        dim = len(Z) - brank
        out = {"dim": dim, "Z1": len(Z), "B1": brank, "H0": n - brank,
               "fox margin": [float(fkept) if fkept is not None else None, float(fdrop)],
               "coboundary margin": [float(bkept) if bkept is not None else None, float(bdrop)]}
        return out, Z, B

    def classes(self, key):
        """an orthonormal basis of a complement of B^1 inside Z^1 (vectors in the generators' coordinates)"""
        info, Z, B = self.h1(key)
        n = {"v": 9, "so": 6, "triv": 1}[key]
        N = len(self.gens) * n
        Zm = stack_cols(Z, N)
        # c with B^T Z c = 0
        K, _, _, _ = null_space(B.T * Zm)
        return info, [Zm * k for k in K]

    def cocycle_value(self, z, w, key="v"):
        """z(w) for a cocycle given by its values on the generators (a vector of length n * #gens)"""
        n = {"v": 9, "so": 6, "triv": 1}[key]
        val = {g: mp.matrix([z[b * n + i] for i in range(n)]) for b, g in enumerate(self.gens)}
        out = mp.matrix(n, 1)
        P = mp.eye(4)
        for c in w:
            g = c.lower()
            if c.islower():
                out += ad(P, key) * val[g]
                P = P * self.L[c]
            else:
                P = P * self.L[c]
                out -= ad(P, key) * val[g]
        return out


# ------------------------------------------------------------------ the cusp and the isometries
def cusp_frame(Gp):
    """T in SL(2, C) sending the cusp's fixed point to infinity, and the translations t_mu, t_lambda there"""
    Am = Gp.sl2_word(Gp.mer)
    a, b, c, d = Am[0, 0], Am[0, 1], Am[1, 0], Am[1, 1]
    if abs(c) < mp.mpf(10) ** -40:
        T = mp.eye(2)
    else:
        z0 = (a - d) / (2 * c)
        T = mp.matrix([[0, 1], [-1, z0]])
    Ti = mp.inverse(T)
    out = {}
    for key, w in (("mu", Gp.mer), ("lambda", Gp.lon)):
        X = T * Gp.sl2_word(w) * Ti
        out[key] = X[0, 1] / X[0, 0]
        out[key + " lower-left"] = abs(X[1, 0])
    return T, out


def abel_power_value(Amu, Alam, cmu, clam, p, q):
    """c(mu^p lambda^q) for a cocycle on the abelian group P, from c(mu), c(lambda) and the actions"""
    n = Amu.rows

    def power_val(A, c0, k):
        acc = mp.matrix(n, 1)
        if k >= 0:
            Pk = mp.eye(n)
            for _ in range(k):
                acc += Pk * c0
                Pk = Pk * A
        else:
            Ai = mp.inverse(A)
            Pk = Ai
            for _ in range(-k):
                acc -= Pk * c0
                Pk = Pk * Ai
        return acc
    Amu_p = mp.eye(n)
    if p >= 0:
        for _ in range(p):
            Amu_p = Amu_p * Amu
    else:
        Ai = mp.inverse(Amu)
        for _ in range(-p):
            Amu_p = Amu_p * Ai
    return power_val(Amu, cmu, p) + Amu_p * power_val(Alam, clam, q)


def record(name, isometries=True):
    Gp = Group(name)
    rec = {"name": name, "generators": len(Gp.gens), "relators": len(Gp.rels), "relator error": float(Gp.relator_error)}
    for key in ("triv", "so"):
        info, _, _ = Gp.h1(key)
        rec["H1 " + key] = info
    info, cls = Gp.classes("v")
    rec["H1 v"] = info
    rec["rigid rel cusp"] = info["dim"] == 1
    if info["dim"] != 1:
        return rec
    z = cls[0]
    # the cusp, in the frame where it sits at infinity
    T, tr = cusp_frame(Gp)
    assert tr["mu lower-left"] < TOL and tr["lambda lower-left"] < TOL, (name, "the frame does not put the cusp at infinity")
    LT = lorentz(T)
    LTi = J * LT.T * J
    rec["cusp"] = {"t_mu": [float(mp.re(tr["mu"])), float(mp.im(tr["mu"]))], "t_lambda": [float(mp.re(tr["lambda"])), float(mp.im(tr["lambda"]))],
                   "parabolic check": [float(tr["mu lower-left"]), float(tr["lambda lower-left"])],
                   "shape t_lambda / t_mu": [float(mp.re(tr["lambda"] / tr["mu"])), float(mp.im(tr["lambda"] / tr["mu"]))]}
    Lmu = LT * Gp.lor(Gp.mer) * LTi
    Llam = LT * Gp.lor(Gp.lon) * LTi
    Amu, Alam = ad(Lmu, "v"), ad(Llam, "v")
    AdT = ad(LT, "v")
    cmu = AdT * Gp.cocycle_value(z, Gp.mer)
    clam = AdT * Gp.cocycle_value(z, Gp.lon)
    # H^1(P; v): Z^1 from (1 - A_lam) c_mu + (A_mu - 1) c_lam = 0, B^1 = ((A_mu - 1) u, (A_lam - 1) u)
    n = 9
    Fp = mp.matrix(n, 2 * n)
    Bp = mp.matrix(2 * n, n)
    for i in range(n):
        for j in range(n):
            Fp[i, j] = (1 if i == j else 0) - Alam[i, j]
            Fp[i, n + j] = Amu[i, j] - (1 if i == j else 0)
            Bp[i, j] = Amu[i, j] - (1 if i == j else 0)
            Bp[n + i, j] = Alam[i, j] - (1 if i == j else 0)
    Zp, _, zk, zd = null_space(Fp)
    Zpm = stack_cols(Zp, 2 * n)
    Kp, _, _, _ = null_space(Bp.T * Zpm)
    Q = [Zpm * k for k in Kp]
    Q = [q / mp.norm(q) for q in Q]
    rec["cusp"]["H1(P; v)"] = len(Q)
    cvec = mp.matrix([cmu[i] for i in range(n)] + [clam[i] for i in range(n)])
    coords = mp.matrix([mp.fdot(q, cvec) for q in Q])
    rec["cusp"]["class in H1(P; v) (norm, relative)"] = float(mp.norm(coords) / mp.norm(cvec))
    rec["cusp"]["class coordinates"] = [float(x / mp.norm(coords)) for x in coords]
    # Heusener-Porti Def. 7.1: a slope g is rigid iff the class restricted to <g> is nonzero in H^1(<g>; v) = v / (Ad g - 1) v;
    # recorded as the relative residual of c(g) against the image of Ad g - 1 (zero iff the slope is not rigid)
    rec["cusp"]["slope residual"] = {"fibre boundary mu": float(slope_residual(Amu, cmu)),
                                     "section lambda": float(slope_residual(Alam, clam))}
    # Lemma S's check: every primitive slope mu^p lambda^q with |p| <= 3, 0 <= q <= 3, its residual and the angle of its translation
    # t = p t_mu + q t_lambda from t_mu (degrees mod 180); the zero slopes must lie in one coset theta_0 + 60 Z
    box = []
    Amu_inv = mp.inverse(Amu)
    for p in range(-3, 4):
        for q in range(0, 4):
            if (p, q) == (0, 0) or (q == 0 and p != 1) or math.gcd(abs(p), q) != 1:
                continue
            Ap = mp.eye(n)
            for _ in range(abs(p)):
                Ap = Ap * (Amu if p > 0 else Amu_inv)
            Aq = mp.eye(n)
            for _ in range(q):
                Aq = Aq * Alam
            cg = abel_power_value(Amu, Alam, cmu, clam, p, q)
            t = p * tr["mu"] + q * tr["lambda"]
            ang = float(mp.degrees(mp.arg(t / tr["mu"]))) % 180.0
            box.append([p, q, float(slope_residual(Ap * Aq, cg)), ang])
    rec["cusp"]["slope box"] = box

    def pull(qv, C, Lg):
        """beta^* of the P-cocycle with values (c(mu), c(lambda)) = qv, for the normaliser Lg and cusp map C"""
        Agi = ad(J * Lg.T * J, "v")
        qm = mp.matrix([qv[i] for i in range(n)])
        ql = mp.matrix([qv[n + i] for i in range(n)])
        bm = Agi * abel_power_value(Amu, Alam, qm, ql, C[0][0], C[1][0])
        bl = Agi * abel_power_value(Amu, Alam, qm, ql, C[0][1], C[1][1])
        return mp.matrix([bm[i] for i in range(n)] + [bl[i] for i in range(n)])

    def on_h1p(C, Lg):
        """the matrix of beta^* on H^1(P; v) in the basis Q, and the defect of its images from Z^1 (a check)"""
        Mb = mp.matrix(len(Q), len(Q))
        defect = mp.mpf(0)
        for j, qj in enumerate(Q):
            b = pull(qj, C, Lg)
            defect = max(defect, mp.norm(Fp * b))
            for i, qi in enumerate(Q):
                Mb[i, j] = mp.fdot(qi, b)
        return Mb, defect
    # control: a translation by a vector off the lattice commutes with the cusp group and must act as the identity on H^1(P; v)
    tshift = mp.mpf("0.37") * tr["mu"] + mp.mpf("0.81") * tr["lambda"]
    Ltr = lorentz(mp.matrix([[1, tshift], [0, 1]]))
    Mtr, _ = on_h1p([[1, 0], [0, 1]], Ltr)
    rec["cusp"]["translation acts trivially (defect)"] = float(mp.mnorm(Mtr - mp.eye(len(Q)), 1))
    if not isometries:
        return rec
    import snappy
    Mlo = snappy.Manifold(name)
    isos = Mlo.is_isometric_to(Mlo, return_isometries=True)
    out = []
    for I in isos:
        C = [[int(x) for x in row] for row in I.cusp_maps()[0]]
        det = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        tmu, tlam = tr["mu"], tr["lambda"]
        tau_mu = C[0][0] * tmu + C[1][0] * tlam
        tau_lam = C[0][1] * tmu + C[1][1] * tlam
        if det == 1:
            alpha = tau_mu / tmu
            check = abs(alpha * tlam - tau_lam)
            refl = mp.eye(4)
        else:
            alpha = tau_mu / mp.conj(tmu)
            check = abs(alpha * mp.conj(tlam) - tau_lam)
            refl = mp.diag([1, 1, -1, 1])
        s = mp.sqrt(alpha)
        Lg = lorentz(mp.matrix([[s, 0], [0, 1 / s]])) * refl
        Lgi = J * Lg.T * J
        Ag_inv = ad(Lgi, "v")
        # beta^* c (mu) = Ad(Lg)^-1 c(beta mu), beta mu = mu^C00 lambda^C10
        bmu = Ag_inv * abel_power_value(Amu, Alam, cmu, clam, C[0][0], C[1][0])
        blam = Ag_inv * abel_power_value(Amu, Alam, cmu, clam, C[0][1], C[1][1])
        # the normaliser must conjugate the cusp onto itself as C says
        conj_err = max(mp.mnorm(Lg * Lmu * Lgi - LT * Gp.lor(power_word(Gp, C[0][0], C[1][0])) * LTi, 1),
                       mp.mnorm(Lg * Llam * Lgi - LT * Gp.lor(power_word(Gp, C[0][1], C[1][1])) * LTi, 1))
        bvec = mp.matrix([bmu[i] for i in range(n)] + [blam[i] for i in range(n)])
        bcoords = mp.matrix([mp.fdot(q, bvec) for q in Q])
        eps = mp.fdot(bcoords, coords) / mp.fdot(coords, coords)
        resid = mp.norm(bcoords - eps * coords) / mp.norm(coords)
        Mb, zdef = on_h1p(C, Lg)
        # H^1(P; v) is 2-dimensional: the eigenvalues in closed form (mpmath's QR stalls on matrices this close to +-1)
        t2, d2 = Mb[0, 0] + Mb[1, 1], mp.det(Mb)
        disc = mp.sqrt(mp.mpc(t2 * t2 - 4 * d2))
        ev = [(t2 + disc) / 2, (t2 - disc) / 2]
        out.append({"cusp map": C, "det": det, "inverts the fibre boundary": C[0][0] == -1 and C[1][0] == 0,
                    "eps": float(eps), "residual": float(resid), "lattice check": float(check), "normaliser check": float(conj_err),
                    "on H1(P; v)": {"trace": float(mp.re(Mb[0, 0] + Mb[1, 1])), "det": float(mp.re(mp.det(Mb))),
                                    "eigenvalues": sorted([round(float(mp.re(e)), 12) for e in ev]),
                                    "eigenvalues imaginary part": float(max(abs(mp.im(e)) for e in ev)),
                                    "cocycle defect": float(zdef)}})
    rec["isometries"] = out
    rec["family-dualising isometry"] = any(abs(o["eps"] + 1) < 1e-6 for o in out)
    return rec


def slope_residual(A, c):
    """|c - (A - 1) u| / |c| minimised over u: zero iff c lies in the image of A - 1 (the class vanishes on the slope)"""
    n = A.rows
    B = A - mp.eye(n)
    U, S, V = mp.svd_r(B)
    rank = sum(1 for i in range(min(B.rows, B.cols)) if abs(S[i]) > TOL)
    # the image of B is spanned by the first `rank` columns of U; the residual is the part of c orthogonal to it
    proj = mp.matrix(n, 1)
    for k in range(rank):
        col = mp.matrix([U[i, k] for i in range(n)])
        proj += col * mp.fdot(col, c)
    return mp.norm(c - proj) / mp.norm(c)


def power_word(Gp, p, q):
    w = (Gp.mer if p >= 0 else inv_word(Gp.mer)) * abs(p) + (Gp.lon if q >= 0 else inv_word(Gp.lon)) * abs(q)
    return w


def inv_word(w):
    return "".join(c.swapcase() for c in reversed(w))


if __name__ == "__main__":
    for name in sys.argv[1:]:
        print(json.dumps(record(name), indent=1))
