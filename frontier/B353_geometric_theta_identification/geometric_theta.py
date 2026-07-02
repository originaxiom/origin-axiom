"""B353 -- the geometric theta-identification: the hyperelliptic involution IS theta on the
E6 tangent, at the deformation-complex level (L52; closes B347's last open item).

Standalone Lie theory + twisted cohomology of the figure-eight; firewalled, nothing to CLAIMS.

B347 computed the sign pattern: the manifold's hyperelliptic involution (a->a^-1, b->b^-1) acts
on the six H^1(4_1, Sym^{2m}) lines by (-1)^{m+1}. B351 built the exact diagram involution theta
and showed its eigenvalue on each exponent LINE is the same (-1)^{m+1}. What remained (L52) is the
OPERATOR-level identification, through the module isomorphism e6 = (+)_m Sym^{2m}:

  (A) theta, transported from B351's exact root basis into the geometric chain basis via B352's
      S-intertwiner, IS the block-scalar operator (+)_m (-1)^{m+1} Id_{2m+1} -- Schur made exact.
      (theta commutes with the principal sl2 and each Sym^{2m} has multiplicity one, so theta must
      act as +-1 per block; here the whole 78x78 matrix identity is verified at dps 100.)
  (B) theta commutes with the FULL holonomy Ad-image (X_root(a), X_root(b)) -- theta fixes the
      principal SL2 subgroup pointwise, so the sigma-twisted and theta-twisted complexes coincide;
      Theta(z) = theta o z is a chain map of the same Fox complex.
  (C) the certificate: per exponent m, the hyperelliptic cocycle action J(z0) equals
      (-1)^{m+1} z0 + d0(v) with an EXPLICIT coboundary v (least-squares residual reported)
      -- J = Theta on H^1, gauge-certified line by line.

Together: the hyperelliptic involution induces exactly theta on the tangent space of the E6
character variety at the principal-geometric representation. The global (variety-level)
identification remains a scope note, not a claim.

Runs on the B351 (exact e6) + B352 (two-basis architecture) + B347 (Sym-block cohomology)
machinery, loaded from their probe directories.
"""
import importlib.util
import pathlib

import mpmath as mp

_FRONTIER = pathlib.Path(__file__).resolve().parent.parent


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _FRONTIER / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CP = _load("b352_cp", "B352_cup_product_obstruction/cup_product.py")   # loads B351 (CP.E6) + B347 (CP.TG)
E6 = CP.E6
TG = CP.TG
mp.mp.dps = 100

EXPONENTS = CP.EXPONENTS
DIM = CP.DIM
SIGN = {m: (-1) ** (m + 1) for m in EXPONENTS}


def _theta_root():
    """B351's exact theta as a 78x78 mp matrix in the root basis (entries in {0, +-1})."""
    th = E6.theta_map()
    T = mp.zeros(DIM, DIM)
    for j in range(DIM):
        for i, c in th[j].items():
            T[i, j] = mp.mpf(c)
    return T


THETA_ROOT = _theta_root()


# --- (A) theta in the geometric chain basis = the block-scalar (-1)^{m+1} ---------------------
def theta_chain_blockscalar_residual():
    """max |S^-1 theta_root S  -  (+)_m (-1)^{m+1} Id_{2m+1}| over all 78^2 entries."""
    Tc = CP.S_INV * THETA_ROOT * CP.S
    r = mp.mpf(0)
    for i in range(DIM):
        for j in range(DIM):
            expect = mp.mpf(SIGN[CP.COLS[i][0]]) if i == j else mp.mpf(0)
            r = max(r, abs(Tc[i, j] - expect))
    return r


# --- (B) theta commutes with the holonomy Ad-image -------------------------------------------
def theta_commutes_with_holonomy():
    """max ||theta X_root(ch) - X_root(ch) theta|| over the two holonomy generators.
    (theta fixes the principal sl2 pointwise (B351), hence the principal SL2 subgroup,
    hence Ad rho(w) for every word w -- verified here directly on the generators.)"""
    r = mp.mpf(0)
    for ch in "ab":
        X = CP.X_root(ch)
        r = max(r, mp.norm(THETA_ROOT * X - X * THETA_ROOT))
    return r


# --- (C) the gauge certificate per exponent line ----------------------------------------------
def hyperelliptic_certificate(m):
    """Solve J(z0) = lam*z0 + d0(v) on the Sym^{2m} block (B347 machinery) and return
    (lam, relative residual): lam must be (-1)^{m+1} and the residual ~0 -- the explicit
    coboundary v certifies J = Theta on this H^1 line."""
    d = 2 * m
    dim = d + 1
    R = TG._R(d)
    inv = TG._HYPER
    RD = TG.symrep(inv["D"], d)
    Da, Db = TG._foxmat("a", d, R), TG._foxmat("b", d, R)
    d1 = mp.zeros(dim, 2 * dim)
    for i in range(dim):
        for j in range(dim):
            d1[i, j] = Da[i, j]
            d1[i, j + dim] = Db[i, j]
    d0 = mp.zeros(2 * dim, dim)
    Aa, Bb = R["a"] - mp.eye(dim), R["b"] - mp.eye(dim)
    for i in range(dim):
        for j in range(dim):
            d0[i, j] = Aa[i, j]
            d0[i + dim, j] = Bb[i, j]
    Z = TG._nullspace(d1)

    def dot(x, y):
        return sum(mp.conj(x[i]) * y[i] for i in range(x.rows))

    def gs(vs):
        o = []
        for v in vs:
            w = v.copy()
            for u in o:
                w = w - dot(u, w) * u
            n = mp.sqrt(dot(w, w).real)
            if n > mp.mpf(10) ** -25:
                o.append(w / n)
        return o

    Bon = gs([mp.matrix([d0[r, c] for r in range(2 * dim)]) for c in range(dim)])
    z0 = None
    for v in Z:
        w = v.copy()
        for u in Bon:
            w = w - dot(u, w) * u
        if mp.sqrt(dot(w, w).real) > mp.mpf(10) ** -18:
            z0 = w
            break
    za, zb = z0[0:dim, 0], z0[dim:2 * dim, 0]
    ja = RD * TG._zeval(inv["sinv"]["a"], za, zb, R)
    jb = RD * TG._zeval(inv["sinv"]["b"], za, zb, R)
    Jz = mp.matrix([ja[i] for i in range(dim)] + [jb[i] for i in range(dim)])
    # least-squares solve Jz = lam*z0 + d0 v, then report lam and the certificate residual
    A = mp.zeros(2 * dim, 1 + dim)
    for r in range(2 * dim):
        A[r, 0] = z0[r]
        for c in range(dim):
            A[r, 1 + c] = d0[r, c]
    AH = mp.matrix(A.cols, A.rows)
    for r in range(A.rows):
        for c in range(A.cols):
            AH[c, r] = mp.conj(A[r, c])
    sol = mp.lu_solve(AH * A, AH * Jz)
    lam = sol[0]
    resid = mp.norm(A * sol - Jz) / mp.norm(Jz)
    return lam, resid


def run_all():
    a = theta_chain_blockscalar_residual()
    b = theta_commutes_with_holonomy()
    certs = {}
    for m in EXPONENTS:
        lam, resid = hyperelliptic_certificate(m)
        certs[m] = (lam, resid)
    return dict(blockscalar_residual=a, holonomy_commutator=b, certificates=certs)


if __name__ == "__main__":
    r = run_all()
    print("(A) theta_chain vs (+)_m (-1)^{m+1} Id  max residual:", mp.nstr(r["blockscalar_residual"], 3))
    print("(B) [theta, Ad rho(a|b)] residual              :", mp.nstr(r["holonomy_commutator"], 3))
    print("(C) per-line certificates  J(z0) = lam z0 + d0 v :")
    for m, (lam, resid) in r["certificates"].items():
        print(f"    m={m:2d}: lam={mp.nstr(lam, 6):>12}  expect {SIGN[m]:+d}   cert-residual {mp.nstr(resid, 3)}")
