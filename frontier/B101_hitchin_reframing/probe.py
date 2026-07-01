"""B101 -- the Hitchin-component reframing of V0 (the SL(3,R) higher-Teichmuller picture).

REFRAMING (mathematics; the physics chain is firewalled to PHYSICS_RESONANCES.md). The project's geometric
component V0 (B71 -- Sym^2 of the Fuchsian SL(2,R) rep of the once-punctured torus) IS the Fuchsian locus of
the Hitchin / Fock-Goncharov positive component of the SL(3,R) character variety. The principal embedding
PSL(2,R) -> SL(3,R) is exactly the Sym^2 irrep, so V0 = Sym^2(Fuchsian) is by definition the Fuchsian locus,
which Hitchin (1992) places in the Hitchin component. Cite: Hitchin 1992 (Teichmuller component); Labourie
(Anosov representations); Fock-Goncharov (positivity, punctured surfaces); Choi-Goldman, Marquis (convex
projective structures, incl. cusped).

FOUR RESULTS (each re-derived here; verify-don't-trust):

  R1  V0 = the Fuchsian locus (STRUCTURAL + computer-assisted).  v0_anosov_hallmark(): every non-peripheral
      word is loxodromic (3 distinct positive reals), the cusp [a,b] is unipotent, none complex; an elliptic
      generator gives a complex spectrum (genuinely off V0).  v0_so21_certificate(): the UNIQUE invariant
      symmetric form has signature (2,1) -> SO(2,1), exact to machine precision.

  R2  the symmetric-space ladder + the SPACETIME-TOWER KILL (dead, first-class negative).
      ladder_signatures(): the principal sl(2) invariant form lands in SPLIT real forms -- Sp(k+1,R) (odd k),
      SO(p,p+-1) (even k).  Lorentzian (one timelike) occurs at EXACTLY k=2 (SO(2,1)) and does NOT climb
      (k=4->SO(3,2), k=6->SO(4,3), k=8->SO(5,4), all balanced split).  There is no "tower of spacetimes up
      the ranks"; Sp(4,R)=Spin(3,2)/SO(3,2) appear (k=3,4 = real AdS4 / 2+1-conformal) but their symmetric
      spaces are higher-rank (dim 6), not the rank-1 spacetimes a universe needs.

  R3  the cubic-differential structure (computer-assisted).  principal_sl3_branching(): under the principal
      sl(2), sl(3) = V2 (+) V4 (ad(h) weights {+-4,+-2,+-2,0,0}; irreps of dim 3 and 5; highest weights 2,4
      => differentials of degree 2 (quadratic) and 3 (cubic)).  V0 is the {cubic = 0} slice (the V2 /
      quadratic = Teichmuller directions).

  R4  the cubic-differential deformation OFF V0 (the genuinely-new computation).
      (a) tangent_space_split(): H^1(F_2, sl(3)_Ad) at the Fuchsian rep splits, under the principal sl(2),
          into H^1 = V2-part (3, Teichmuller, tangent to V0) (+) V4-part (5, CUBIC, transverse to V0).
      (b) cubic_deformation_witness(): an explicit real one-parameter family rho_t (rho_0 Fuchsian, moving in
          a V4 cubic direction) that for small t (>= 2 Fuchsian seeds x 2 cubic directions) stays Anosov
          (loxodromic, 3 distinct positive reals), LEAVES V0 (x1 != x4), and BREAKS the SO(2,1) form (no
          invariant symmetric form survives).  Honest scope: an unconstrained cubic deformation also moves
          the puncture holonomy off unipotent (fixing the boundary is a codimension constraint, not done
          here); the decisive content is "the cubic directions exist, stay Anosov, and leave the Fuchsian
          locus."

Neutral higher-Teichmuller / Lie theory; NO physics claim; the Hitchin->Higgs->geometric-Langlands->N=4
chain is CITED context only (PHYSICS_RESONANCES.md), with the ceiling stated; the "tower of spacetimes" is
recorded as DEAD.  No Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import expm, null_space

# ---------------------------------------------------------------------------
# Sym^2 : SL(2) -> SL(3), the standard {e1^2, e1 e2, e2^2} convention.
# (B71.sym2 is the same representation in a conjugate basis; R1's "V0" is the B71 component, basis-free.)
# ---------------------------------------------------------------------------
def sym2(M):
    (a, b), (c, d) = M
    return np.array([[a * a, a * c, c * c],
                     [2 * a * b, a * d + b * c, 2 * c * d],
                     [b * b, b * d, d * d]], dtype=float)


# ---------------------------------------------------------------------------
# sl(3) machinery: a basis, the principal sl(2), the V2/V4 isotypic projectors (R3), and Ad.
# ---------------------------------------------------------------------------
def _sl3_basis():
    """8 traceless 3x3 matrices: the 6 off-diagonal E_ij and 2 Cartan generators."""
    B = []
    for i in range(3):
        for j in range(3):
            if i != j:
                E = np.zeros((3, 3)); E[i, j] = 1.0; B.append(E)
    B.append(np.diag([1.0, -1.0, 0.0])); B.append(np.diag([0.0, 1.0, -1.0]))
    return B


_BASIS = _sl3_basis()
_BMAT = np.array([b.flatten() for b in _BASIS]).T          # 9x8


def _vec(X):
    return np.linalg.lstsq(_BMAT, np.asarray(X, float).flatten(), rcond=None)[0]


def _mat(v):
    return sum(c * b for c, b in zip(v, _BASIS))


def _ad(X):
    return np.array([_vec(X @ b - b @ X) for b in _BASIS]).T


def _sl2_std_gens(k):
    """The (k+1)-dim irrep generators (h,e,f) of sl(2); k=2 is the principal sl(2) acting on R^3 = std SL(3)."""
    n = k + 1
    h = np.diag([float(k - 2 * i) for i in range(n)])
    e = np.zeros((n, n)); f = np.zeros((n, n))
    for i in range(n):
        if i - 1 >= 0: e[i - 1, i] = i
        if i + 1 < n:  f[i + 1, i] = (k - i)
    return h, e, f


def _principal_casimir():
    """The principal-sl(2) Casimir acting on sl(3) (8x8); its eigenvalues separate V2 (=8) from V4 (=24)."""
    h, e, f = _sl2_std_gens(2)
    adh, ade, adf = _ad(h), _ad(e), _ad(f)
    return adh @ adh + 2 * (ade @ adf + adf @ ade)


_CAS = _principal_casimir()
_CAS_EV = np.linalg.eigvals(_CAS).real
_CAS_UNIQ = sorted(set(np.round(_CAS_EV, 1)))
_CAS_DIM = {u: int(np.sum(np.abs(_CAS_EV - u) < 1e-6)) for u in _CAS_UNIQ}


def _isotypic_projector(dim_block):
    """Spectral projector of the Casimir onto the isotypic block of the given dimension (3=V2, 5=V4)."""
    target = [u for u in _CAS_UNIQ if _CAS_DIM[u] == dim_block][0]
    P = np.eye(8)
    for u in _CAS_UNIQ:
        if abs(u - target) > 1e-6:
            P = P @ (_CAS - u * np.eye(8)) / (target - u)
    return P


_P2 = _isotypic_projector(3)        # V2  (quadratic / Teichmuller, tangent to V0)
_P4 = _isotypic_projector(5)        # V4  (cubic, transverse to V0)


def _Ad(g):
    gi = np.linalg.inv(g)
    return np.array([_vec(g @ b @ gi) for b in _BASIS]).T


# ---------------------------------------------------------------------------
# Fuchsian once-punctured-torus seeds (Markov triples => tr[A,B] = -2, the parabolic cusp).
# ---------------------------------------------------------------------------
def fuchsian_seed(a, b, c):
    """An SL(2,R) once-punctured-torus rep with (tr A, tr B, tr AB)=(a,b,c). A Markov triple
    a^2+b^2+c^2=abc forces tr[A,B]=-2 (parabolic puncture), the Fuchsian/Teichmuller condition."""
    A = np.array([[a, -1.0], [1.0, 0.0]])
    # B=[[p,1],[a p+1-c, b-p]] has det 1, tr b, tr(AB)=c when p solves p(b-p)-(a p+1-c)=1
    # p^2 + (a-b) p + (1-c+... ) ; solve the quadratic explicitly:
    # p(b-p) - (a p + 1 - c) = 1  =>  -p^2 + (b-a) p + (c-2) = 0  =>  p^2 - (b-a)p - (c-2) = 0
    disc = (b - a) ** 2 + 4 * (c - 2)
    p = ((b - a) + np.sqrt(disc)) / 2
    B = np.array([[p, 1.0], [a * p + 1 - c, b - p]])
    return A, B


# the two locking seeds: the modular torus (3,3,3) and a mild asymmetric Markov torus (3, 3.5, 2.7376)
_C2 = (10.5 - np.sqrt(10.5 ** 2 - 4 * (9 + 12.25))) / 2     # = 2.7376..., Markov(3,3.5,*)
SEEDS = {"markov_333": (3.0, 3.0, 3.0), "markov_3_3.5": (3.0, 3.5, _C2)}
_WORDS = ["ab", "aB", "aab", "abb", "aabb", "abAb"]         # non-peripheral, moderate length


def _grp(A, B):
    return {"a": A, "b": B, "A": np.linalg.inv(A), "B": np.linalg.inv(B)}


def _word(g, W):
    M = np.eye(g["a"].shape[0])
    for ch in W:
        M = M @ g[ch]
    return M


def _is_anosov(g):
    """Every word in _WORDS loxodromic: 3 distinct positive real eigenvalues."""
    for W in _WORDS:
        e = np.linalg.eigvals(_word(g, W))
        es = np.sort(e.real)
        if not (np.allclose(e.imag, 0, atol=1e-6) and np.all(es > 1e-7)
                and (es[1] - es[0]) > 1e-5 and (es[2] - es[1]) > 1e-5):
            return False
    return True


def _invariant_form_nulldim(g):
    """Dimension of the space of Ad-invariant symmetric bilinear forms (1 on V0 = SO(2,1); 0 off it)."""
    rows = [np.kron(m.T, m.T) - np.eye(9) for m in (g["a"], g["b"])]
    return null_space(np.vstack(rows), rcond=1e-9).shape[1]


# ===========================================================================
# R1 -- V0 = the Fuchsian locus of the Hitchin component
# ===========================================================================
def v0_anosov_hallmark():
    """The Anosov hallmark on V0 (Sym^2 of the (3,3,3) Fuchsian rep): per-word (real, 3-distinct, positive);
    the cusp [a,b] unipotent; the elliptic control complex. Returns a dict of findings."""
    A0, B0 = fuchsian_seed(*SEEDS["markov_333"])
    g = _grp(sym2(A0), sym2(B0))
    per_word = {}
    for W in _WORDS:
        e = np.sort(np.linalg.eigvals(_word(g, W)).real)
        per_word[W] = bool(np.all(e > 1e-7) and (e[1] - e[0]) > 1e-5 and (e[2] - e[1]) > 1e-5)
    # [a,b] -> unipotent. Certify structurally via nilpotency, (M - I)^3 = 0:
    # the eigenvalues of a defective (single-Jordan-block) matrix are
    # ill-conditioned -- an entry perturbation eps moves them by eps^(1/3)
    # (~4e-5 at machine precision here), so np.allclose(eigvals, 1, atol=1e-6)
    # is LAPACK-version-dependent and false-negatives on a genuinely unipotent
    # cusp. (Audit fix 2026-07-01; same failure family as the B129/B2 MB guard:
    # eigenvalue data is the wrong certificate near a non-diagonalizable point.)
    Mc = _word(g, "abAB")
    nil = np.linalg.matrix_power(Mc - np.eye(3), 3)
    cusp_unipotent = bool(np.max(np.abs(nil)) < 1e-8)
    th = 0.7
    Ae = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    ell = np.linalg.eigvals(sym2(Ae))
    elliptic_complex = bool(np.max(np.abs(ell.imag)) > 1e-3)
    return {"all_loxodromic": all(per_word.values()), "per_word": per_word,
            "cusp_unipotent": cusp_unipotent, "elliptic_control_complex": elliptic_complex}


def v0_so21_certificate():
    """The unique Ad-invariant symmetric form on V0 has signature (2,1) -> SO(2,1). Returns
    (null_dim, (p, q), invariance_residual)."""
    A0, B0 = fuchsian_seed(*SEEDS["markov_333"])
    A, B = sym2(A0), sym2(B0)
    rows = [np.kron(m.T, m.T) - np.eye(9) for m in (A, B)]
    N = null_space(np.vstack(rows), rcond=1e-9)
    nd = N.shape[1]
    Q = N[:, 0].reshape(3, 3); Q = (Q + Q.T) / 2
    ev = np.linalg.eigvalsh(Q / np.max(np.abs(Q)))
    p = int(np.sum(ev > 1e-8)); q = int(np.sum(ev < -1e-8))
    inv = float(np.max(np.abs(A.T @ Q @ A - Q)))
    return nd, (max(p, q), min(p, q)), inv


# ===========================================================================
# R2 -- the symmetric-space ladder + the spacetime-tower KILL
# ===========================================================================
def _invariant_form_of_irrep(k):
    """The (unique) invariant bilinear form on the (k+1)-dim sl(2) irrep; symmetric for even k, else skew."""
    h, e, f = _sl2_std_gens(k)
    n = k + 1
    rows = [np.kron(np.eye(n), X.T) + np.kron(X.T, np.eye(n)) for X in (h, e, f)]
    B = null_space(np.vstack(rows), rcond=1e-9)
    return B[:, 0].reshape(n, n)


def ladder_signatures(kmax=8):
    """For k=1..kmax: (kind, ambient split form, signature, lorentzian?) of the principal sl(2) in the
    invariant form of Sym^k. Lorentzian (min(p,q)=1) only at k=2 (SO(2,1))."""
    out = []
    for k in range(1, kmax + 1):
        B = _invariant_form_of_irrep(k)
        if np.allclose(B, B.T):
            ev = np.linalg.eigvalsh(B / np.max(np.abs(B)))
            p = int(np.sum(ev > 1e-8)); q = int(np.sum(ev < -1e-8))
            out.append((k, "symmetric", f"SO({max(p,q)},{min(p,q)})", (max(p, q), min(p, q)),
                        min(p, q) == 1))
        else:
            out.append((k, "symplectic", f"Sp({k+1},R)", None, False))
    return out


def lorentzian_rungs(kmax=8):
    """The k at which the ladder is Lorentzian (one timelike). Returns the list (should be exactly [2])."""
    return [k for (k, kind, amb, sig, lor) in ladder_signatures(kmax) if lor]


# ===========================================================================
# R3 -- the cubic-differential structure: sl(3) = V2 (+) V4 under the principal sl(2)
# ===========================================================================
def principal_sl3_branching():
    """Returns (ad(h) weight multiset, {block_dim: differential_degree}). sl(3)=V2(+)V4: weights
    {+-4,+-2,+-2,0,0}; dims 3 (quadratic, deg 2) and 5 (cubic, deg 3)."""
    h = np.diag([2.0, 0.0, -2.0])
    weights = sorted(int(round(w)) for w in np.linalg.eigvals(_ad(h)).real)
    # block dim d = 2j+1 (highest weight 2j) => differential degree j+1
    degree = {d: (d - 1) // 2 + 1 for d in (3, 5)}           # {3:2 (quadratic), 5:3 (cubic)}
    return weights, degree


# ===========================================================================
# R4 -- the cubic-differential deformation OFF V0
# ===========================================================================
def tangent_space_split(seed="markov_333"):
    """H^1(F_2, sl(3)_Ad) at the Fuchsian rep, split under the principal sl(2) into the V2 (Teichmuller,
    tangent to V0) and V4 (cubic, transverse) parts. Returns (dim H^1, dim V2-part, dim V4-part)."""
    A0, B0 = fuchsian_seed(*SEEDS[seed])
    A, B = sym2(A0), sym2(B0)
    AdA, AdB, I = _Ad(A), _Ad(B), np.eye(8)
    # Z^1 = sl(3)^2 (free, 16); B^1 = image of delta: xi -> ((AdA-I)xi,(AdB-I)xi); H^1 = 16 - rank(delta).
    delta = np.vstack([AdA - I, AdB - I])
    h1 = 16 - np.linalg.matrix_rank(delta, tol=1e-9)
    # Ad(A),Ad(B) preserve the V2,V4 blocks (A,B lie in the principal SL(2,R)), so H^1 splits blockwise:
    # dim H^1_k = 2*dim(V_k) - rank(delta restricted to the V_k domain).
    def block(P, dk):
        d = np.vstack([(AdA - I) @ P, (AdB - I) @ P])
        return 2 * dk - np.linalg.matrix_rank(d, tol=1e-9)
    return int(h1), int(block(_P2, 3)), int(block(_P4, 5))


def _cubic_dir(idx):
    """A deterministic unit cubic (V4) direction in sl(3)."""
    e = np.zeros(8); e[idx] = 1.0
    m = _mat(_P4 @ e)
    return m / np.linalg.norm(m)


def cubic_deformation_witness(t=0.05):
    """Deform every (seed x cubic-direction) by rho_t(a)=exp(t u_a) Sym^2(A0), likewise b, with u in V4.
    Returns a list of dicts: stays Anosov, leaves V0 (|x1-x4|>0), breaks the SO(2,1) form (nulldim 0)."""
    results = []
    for sname, (a, b, c) in SEEDS.items():
        A0, B0 = fuchsian_seed(a, b, c)
        A, B = sym2(A0), sym2(B0)
        for d in (0, 1):
            ua, ub = _cubic_dir(d), _cubic_dir(d + 2)
            g = _grp(expm(t * ua) @ A, expm(t * ub) @ B)
            x1, x4 = np.trace(g["a"]), np.trace(g["A"])
            results.append({"seed": sname, "dir": d,
                            "off_V0": float(abs(x1 - x4)),
                            "anosov": _is_anosov(g),
                            "so21_nulldim": _invariant_form_nulldim(g),
                            "cusp_tr": float(np.real(np.trace(_word(g, "abAB"))))})
    return results


def main():
    print("B101 -- the Hitchin-component reframing of V0\n")
    print("R1  V0 = Fuchsian locus of the SL(3,R) Hitchin component")
    h = v0_anosov_hallmark()
    print(f"    Anosov hallmark: all loxodromic={h['all_loxodromic']}, cusp unipotent={h['cusp_unipotent']}, "
          f"elliptic control complex={h['elliptic_control_complex']}")
    nd, sig, inv = v0_so21_certificate()
    print(f"    SO(2,1) certificate: unique form (nulldim {nd}), signature {sig}, invariance {inv:.1e}")
    print("\nR2  the symmetric-space ladder (Lorentzian only at k=2 -> spacetime-tower KILL)")
    for (k, kind, amb, sig, lor) in ladder_signatures():
        print(f"    k={k}: {amb:9} {'LORENTZIAN' if lor else ''}")
    print(f"    Lorentzian rungs: {lorentzian_rungs()}  (no tower of spacetimes up the ranks)")
    print("\nR3  the cubic-differential structure: sl(3) = V2 (+) V4")
    w, deg = principal_sl3_branching()
    print(f"    ad(h) weights {w}; block dims->differential degree {deg} (V0 = {{cubic=0}})")
    print("\nR4  the cubic deformation OFF V0")
    for s in SEEDS:
        print(f"    tangent split [{s}]: H^1 = {tangent_space_split(s)} (= V2 Teichmuller (+) V4 cubic)")
    for r in cubic_deformation_witness():
        print(f"    witness [{r['seed']} dir{r['dir']}]: offV0|x1-x4|={r['off_V0']:.3f} "
              f"Anosov={r['anosov']} SO21nulldim={r['so21_nulldim']} (cusp_tr={r['cusp_tr']:.2f})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
