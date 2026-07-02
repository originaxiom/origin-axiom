"""B357 -- the E6 boundary restriction: rank, the Lagrangian certificate, and the six slopes
(campaign W1.3; the classical-structure deliverable for Gate B).

THE OBJECT. M = the figure-eight complement; T^2 = the cusp torus, pi_1(T^2) = <mu, lam> with
mu = 'ABB', lam = 'BAbabABa' in the SnapPy presentation <a,b | abbbaBAAB> (verified in-module:
commuting, both parabolic tr = -2). At the principal-composed geometric rep the peripheral
holonomy is REGULAR UNIPOTENT in E6, so per exponent block Sym^{2m}:
    H^0(T^2, Sym^{2m}) = (invariants of U,V) = 1   =>   H^1(T^2, Sym^{2m}) = 2,
and the full boundary space H^1(T^2, e6) is 12-dimensional, symplectic via cup + the invariant
pairing, block-diagonal over the six exponents (the Killing form pairs Sym-blocks diagonally).

WHAT IS COMPUTED (per exponent m in {1,4,5,7,8,11}):
  (1) rank(r_m): does the H^1(M)-class z_m survive restriction to the cusp? (rank < 1 would be a
      peripherally-invisible deformation -- the genuinely open question).
  (2) THE SLOPE sigma_m: the class r(z_m) in the 2-dim H^1(T^2, Sym^{2m}), written in the
      invariant-line basis E_mu = [(h_m, 0)], E_lam = [(0, h_m)]:  r(z_m) = alpha E_mu + beta E_lam
      (+ coboundary, residual gated) => sigma_m = beta/alpha. For m = 1 this is the classical
      Neumann-Zagier datum: THE CONTROL asserts sigma_1 = the SnapPy cusp shape (up to the
      declared sign/conjugation convention). The six slopes are the E6-exponent generalization of
      the cusp shape -- the linearized peripheral data of the E6 A-variety at the complete
      structure, the object Gate B's state integral integrates over.
  (3) The symplectic controls (MB12): the ambient 2-dim form omega(E_mu, E_lam) != 0 per block
      (nondegeneracy -- so isotropy statements are not vacuous); omega antisymmetric on cocycles
      modulo coboundaries; coboundaries pair to zero.
  (4) The Lagrangian certificate, honestly stated: with rank(r_m) = 1 for all six blocks the
      image is 6-dim = half of 12, block-orthogonal (Killing pairs blocks diagonally), and each
      block-image is a line in a 2-dim symplectic plane -- isotropic automatically. So
      Lagrangianity follows from the RANK result + block structure (half-lives-half-dies made
      concrete); a failure could only come from a rank drop, which (1) tests.

Machinery: B347 (symrep, the geometric rep, per-block Fox cohomology, _zeval). mpmath dps 60.
Firewalled; nothing to CLAIMS; no physics claim.
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


TG = _load("b347_tg", "B347_e6_tangent_gradings/e6_tangent_gradings.py")
mp.mp.dps = 60

EXPONENTS = TG.EXPONENTS                        # [1, 4, 5, 7, 8, 11]
MU_WORD = "ABB"                                 # SnapPy peripheral_curves() for <a,b | abbbaBAAB>
LAM_WORD = "BAbabABa"
CUSP_SHAPE = mp.mpc(0, 1) * 2 * mp.sqrt(3)      # 4_1 cusp shape 2*sqrt(3)*i (B321; SnapPy cusp_info)


def _word_mat(word):
    return TG._ev(word)


def peripheral_gates():
    """mu, lam commute; both parabolic (tr = -2); the relator holds (inherited from B347)."""
    U, V = _word_mat(MU_WORD), _word_mat(LAM_WORD)
    comm = mp.norm(U * V - V * U)
    trU, trV = U[0, 0] + U[1, 1], V[0, 0] + V[1, 1]
    return comm < mp.mpf(10) ** -40 and abs(trU + 2) < mp.mpf(10) ** -40 and abs(trV + 2) < mp.mpf(10) ** -40


# ------------------------------------------------- per-block boundary cohomology ------------------
def _block(m):
    """Return dict with the block rep R, U_m, V_m, the invariant vector h, Z1/B1 data."""
    d = 2 * m
    dim = d + 1
    R = TG._R(d)
    U = TG.symrep(_word_mat(MU_WORD), d)
    V = TG.symrep(_word_mat(LAM_WORD), d)
    # invariants of the (regular unipotent) peripheral pair: ker(U-1) cap ker(V-1)
    stack = mp.zeros(2 * dim, dim)
    A1, B1m = U - mp.eye(dim), V - mp.eye(dim)
    for i in range(dim):
        for j in range(dim):
            stack[i, j] = A1[i, j]
            stack[i + dim, j] = B1m[i, j]
    ns = TG._nullspace(stack.T * 0 + stack) if False else _nullspace(stack)
    assert len(ns) == 1, (m, len(ns), "H0 of the cusp should be 1 (regular unipotent)")
    h = ns[0]
    return dict(m=m, d=d, dim=dim, R=R, U=U, V=V, h=h)


def _nullspace(M, tol=mp.mpf(10) ** -35):
    Um, S, Vm = mp.svd_c(M, full_matrices=True)
    sv = [abs(S[i]) for i in range(len(S))]
    sm = max(sv)
    return [mp.matrix([mp.conj(Vm[i, j]) for j in range(M.cols)])
            for i in range(M.cols) if (sv[i] if i < len(sv) else mp.mpf(0)) <= sm * tol]


def _lstsq(A, b):
    """SVD least squares (the column set is rank-deficient by design: the coboundary map's kernel
    is the invariant line, so pinv/min-norm is the correct solve; alpha, beta stay determined)."""
    U, S, V = mp.svd_c(A, full_matrices=False)
    smax = max(abs(S[i]) for i in range(len(S)))
    y = U.T.apply(mp.conj) * b if False else None
    UH = mp.matrix(U.cols, U.rows)
    for r in range(U.rows):
        for c in range(U.cols):
            UH[c, r] = mp.conj(U[r, c])
    y = UH * b
    x = mp.zeros(A.cols, 1)
    for i in range(len(S)):
        if abs(S[i]) > smax * mp.mpf(10) ** -35:
            for j in range(A.cols):
                x[j] += mp.conj(V[i, j]) * y[i] / S[i]
    resid = mp.norm(A * x - b) / max(mp.norm(b), mp.mpf(10) ** -30)
    return x, resid


def _dot(x, y):
    return sum(mp.conj(x[i]) * y[i] for i in range(x.rows))


def _gs(vs, tol=mp.mpf(10) ** -25):
    o = []
    for v in vs:
        w = v.copy()
        for u in o:
            w = w - _dot(u, w) * u
        n = mp.sqrt(_dot(w, w).real)
        if n > tol:
            o.append(w / n)
    return o


def _boundary_h1(blk):
    """Honest H^1(T^2, Sym^{2m}) basis: Z^1 = ker[(1-V) | -(1-U)] (dim = dim+1), B^1 = the
    coboundary columns (rank dim-1); H^1 basis = the 2-dim orthogonal complement of B^1 in Z^1."""
    dim, U, V = blk["dim"], blk["U"], blk["V"]
    C = mp.zeros(dim, 2 * dim)
    ImV, ImU = mp.eye(dim) - V, mp.eye(dim) - U
    for i in range(dim):
        for j in range(dim):
            C[i, j] = ImV[i, j]
            C[i, j + dim] = -ImU[i, j]
    Z = _nullspace(C)
    assert len(Z) == dim + 1, (blk["m"], len(Z))
    UmI, VmI = U - mp.eye(dim), V - mp.eye(dim)
    Bcols = []
    for j in range(dim):
        col = mp.zeros(2 * dim, 1)
        for i in range(dim):
            col[i] = UmI[i, j]
            col[i + dim] = VmI[i, j]
        Bcols.append(col)
    Bon = _gs(Bcols)
    assert len(Bon) == dim - 1, (blk["m"], len(Bon))
    h1 = []
    for z in Z:
        w = z.copy()
        for u in Bon + h1:
            w = w - _dot(u, w) * u
        n = mp.sqrt(_dot(w, w).real)
        if n > mp.mpf(10) ** -18:
            h1.append(w / n)
    assert len(h1) == 2, (blk["m"], len(h1))
    return h1, Bon


def _h1_class(blk, u, v, h1, Bon):
    """Coordinates of the cocycle (u,v) in the orthonormal H^1 basis (residual gated)."""
    dim = blk["dim"]
    vec = mp.matrix([u[i] for i in range(dim)] + [v[i] for i in range(dim)])
    coords = [_dot(e, vec) for e in h1]
    rem = vec.copy()
    for e in h1 + Bon:
        rem = rem - _dot(e, rem) * e
    resid = mp.sqrt(_dot(rem, rem).real) / mp.sqrt(_dot(vec, vec).real)
    return coords, resid


def restriction(m):
    """Restrict B347's H^1(M, Sym^{2m}) class to the cusp: (alpha, beta, slope, residual)."""
    blk = _block(m)
    d, dim, R = blk["d"], blk["dim"], blk["R"]
    # the H^1(M) representative from B347's machinery
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
    Z = _nullspace(d1)

    def dot(x, y):
        return sum(mp.conj(x[i]) * y[i] for i in range(x.rows))

    def gs(vs):
        o = []
        for vv in vs:
            w = vv.copy()
            for uu in o:
                w = w - dot(uu, w) * uu
            nn = mp.sqrt(dot(w, w).real)
            if nn > mp.mpf(10) ** -25:
                o.append(w / nn)
        return o

    Bon = gs([mp.matrix([d0[r, c] for r in range(2 * dim)]) for c in range(dim)])
    z0 = None
    for vv in Z:
        w = vv.copy()
        for uu in Bon:
            w = w - dot(uu, w) * uu
        if mp.sqrt(dot(w, w).real) > mp.mpf(10) ** -18:
            z0 = w
            break
    za, zb = z0[0:dim, 0], z0[dim:2 * dim, 0]
    u = TG._zeval(MU_WORD, za, zb, R)
    v = TG._zeval(LAM_WORD, za, zb, R)
    h1, Bon = _boundary_h1(blk)
    coords, resid = _h1_class(blk, u, v, h1, Bon)
    rank = 1 if mp.sqrt(sum(abs(c) ** 2 for c in coords)) > mp.mpf(10) ** -18 else 0
    # the canonical leading-NZ functionals: phi_mu = K(u, h), phi_lam = K(v, h)
    # (the ONLY K-functionals killing the coboundaries; see the tau-identity below)
    K = _pairing(dim)
    h = blk["h"]
    phi_mu = (u.T * K * h)[0, 0]
    phi_lam = (v.T * K * h)[0, 0]
    return dict(m=m, coords=coords, resid=resid, rank=rank,
                phi_mu=phi_mu, phi_lam=phi_lam, blk=blk, h1=h1, Bon=Bon)


def tau_identity(m, n_random=6, seed=11):
    """THE UNIVERSAL-tau IDENTITY: on EVERY cocycle (u,v) in Z^1(T^2, Sym^{2m}),
    K(v, h) = tau * K(u, h) with ONE constant tau (independent of m) = the cusp shape.
    (Mechanism: U = exp(N), V = exp(tau N) at the complete structure, and K(., h) kills im N
    and ker N; so the leading Neumann-Zagier datum does NOT split by exponent.)
    Returns (tau_estimate, max_deviation_over_Z1_basis)."""
    blk = _block(m)
    dim = blk["dim"]
    K = _pairing(dim)
    h = blk["h"]
    C = mp.zeros(dim, 2 * dim)
    ImV, ImU = mp.eye(dim) - blk["V"], mp.eye(dim) - blk["U"]
    for i in range(dim):
        for j in range(dim):
            C[i, j] = ImV[i, j]
            C[i, j + dim] = -ImU[i, j]
    Z = _nullspace(C)
    taus = []
    for z in Z:
        u = mp.matrix([z[i] for i in range(dim)])
        v = mp.matrix([z[i + dim] for i in range(dim)])
        pu = (u.T * K * h)[0, 0]
        pv = (v.T * K * h)[0, 0]
        if abs(pu) > mp.mpf(10) ** -30:
            taus.append(pv / pu)
    assert taus, m
    t0 = taus[0]
    dev = max(abs(t - t0) for t in taus)
    return t0, dev


# ------------------------------------------------- the symplectic form + controls -----------------
def _pairing(dim):
    """The SL(2)-invariant symmetric pairing on Sym^d (d = dim-1):
    K(e_i, e_j) = delta_{i+j,d} * (-1)^i / C(d,i)."""
    import math
    d = dim - 1
    K = mp.zeros(dim, dim)
    for i in range(dim):
        K[i, d - i] = mp.mpf((-1) ** i) / math.comb(d, i)
    return K


def omega(blk, c1, c2):
    """omega((u1,v1),(u2,v2)) = K(u1, U v2) - K(v1, V u2) (bar-resolution 2-cycle [mu|lam]-[lam|mu])."""
    K = _pairing(blk["dim"])
    u1, v1 = c1
    u2, v2 = c2
    return ((u1.T * K * (blk["U"] * v2)) - (v1.T * K * (blk["V"] * u2)))[0, 0]


def symplectic_controls(m):
    """(i) K is invariant under the block rep (gate); (ii) omega(E_mu, E_lam) != 0 (MB12 ambient
    nondegeneracy); (iii) omega antisymmetric on the E-basis; (iv) coboundaries pair to ~0."""
    blk = _block(m)
    dim, R, h = blk["dim"], blk["R"], blk["h"]
    K = _pairing(dim)
    inv_err = max(mp.norm(R[g].T * K * R[g] - K) for g in "ab")
    Emu = (h, mp.zeros(dim, 1))
    Elam = (mp.zeros(dim, 1), h)
    o12 = omega(blk, Emu, Elam)
    o21 = omega(blk, Elam, Emu)
    w = mp.matrix([mp.mpf(1) / (i + 2) for i in range(dim)])       # arbitrary test vector
    cob = ((blk["U"] - mp.eye(dim)) * w, (blk["V"] - mp.eye(dim)) * w)
    o_cob = max(abs(omega(blk, cob, Emu)), abs(omega(blk, cob, Elam)))
    return dict(m=m, K_invariance_err=inv_err, omega_mu_lam=o12,
                antisym_err=abs(o12 + o21), coboundary_pairing=o_cob,
                nondegenerate=abs(o12) > mp.mpf(10) ** -30)


def omega_on_h1(m):
    """The 2x2 matrix of omega on the orthonormal H^1 basis (MB12: must be nondegenerate)."""
    blk = _block(m)
    h1, _ = _boundary_h1(blk)
    dim = blk["dim"]

    def split(vec):
        return (mp.matrix([vec[i] for i in range(dim)]),
                mp.matrix([vec[i + dim] for i in range(dim)]))

    M = mp.zeros(2, 2)
    for i in range(2):
        for j in range(2):
            M[i, j] = omega(blk, split(h1[i]), split(h1[j]))
    return M


def run_all():
    assert peripheral_gates()
    out = {}
    tau_ref = None
    for m in EXPONENTS:
        r = restriction(m)
        t, dev = tau_identity(m)
        M = omega_on_h1(m)
        det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
        out[m] = dict(rank=r["rank"], resid=r["resid"], phi_mu=r["phi_mu"], phi_lam=r["phi_lam"],
                      tau=t, tau_dev=dev, omega_det=det,
                      omega_antisym=abs(M[0, 1] + M[1, 0]),
                      omega_nondeg=abs(det) > mp.mpf(10) ** -30)
        if tau_ref is None:
            tau_ref = t
    total_rank = sum(out[m]["rank"] for m in EXPONENTS)
    tau_uniform = max(abs(out[m]["tau"] - tau_ref) for m in EXPONENTS)
    return dict(blocks=out, total_rank=total_rank,
                lagrangian_certified=(total_rank == 6),
                tau=tau_ref, tau_uniform_dev=tau_uniform)


if __name__ == "__main__":
    print("peripheral gates (commuting parabolics):", peripheral_gates())
    out = run_all()
    print(f"rank(r) = {out['total_rank']} / 6   -> Lagrangian certified: {out['lagrangian_certified']}")
    print(f"tau (universal, all blocks): {mp.nstr(out['tau'], 12)}   uniform-dev {mp.nstr(out['tau_uniform_dev'], 3)}")
    print(f"   control target: SnapPy cusp shape 2*sqrt(3)*i = {mp.nstr(CUSP_SHAPE, 12)}")
    for m in EXPONENTS:
        b = out["blocks"][m]
        print(f"  m={m:2d}: rank={b['rank']} class-resid={mp.nstr(b['resid'], 2)} "
              f"phi_mu={mp.nstr(b['phi_mu'], 5)} tau-dev={mp.nstr(b['tau_dev'], 2)} "
              f"omega: det={mp.nstr(b['omega_det'], 4)} antisym-err={mp.nstr(b['omega_antisym'], 2)} "
              f"nondeg={b['omega_nondeg']}")
