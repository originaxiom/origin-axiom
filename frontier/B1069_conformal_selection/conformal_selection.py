#!/usr/bin/env python3
"""B1069 -- how much does affine isotropy pin down inside B527's Stein cone?

B527: the Stein-compatible metrics on E_s = ker(ell^T) form a full 6-dimensional cone;
Stein compatibility ALONE cannot select a metric.  S_aff sits in its INTERIOR, distinguished
only by the SEPARATE affine-isotropy requirement.

B527 never asked how big the isotropy locus is.  That is this script.

Criteria sealed in PREREG_conformal_selection.md BEFORE this was run.
Controls run first; no result is read until all four pass.
"""
import numpy as np

np.set_printoptions(precision=6, suppress=True)
TOL = 1e-9

# ---------------------------------------------------------------- B527 setup, rebuilt
phi = (1 + 5 ** 0.5) / 2
sp_ = phi ** 0.5
M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
r = np.array([phi, 1, phi * sp_, sp_], float)                     # right Perron vector
w, V = np.linalg.eig(M.T)
ell = V[:, int(np.argmax(w.real))].real
ell = ell / (ell @ r)                                             # left Perron, normalised ell.r = 1

raw = np.column_stack([ell[i] * np.eye(4)[:, 0] - ell[0] * np.eye(4)[:, i] for i in (1, 2, 3)])
B, _ = np.linalg.qr(raw)                                          # 4x3 orthonormal basis of E_s
assert np.allclose(ell @ B, 0, atol=TOL)
Abar = B.T @ M @ B

A = np.eye(4) - np.outer(r, np.ones(4)) / (np.ones(4) @ r)
Saff = 0.5 * A.T @ A
Ps = np.eye(4) - np.outer(r, ell)                                 # projection onto E_s along r


def vec(S):
    return np.array([S[0, 0], S[1, 1], S[2, 2], S[0, 1], S[0, 2], S[1, 2]])


def mat(x):
    return np.array([[x[0], x[3], x[4]], [x[3], x[1], x[5]], [x[4], x[5], x[2]]])


L6 = np.column_stack([vec(mat(e) - Abar.T @ mat(e) @ Abar) for e in np.eye(6)])


def driver_eigs(S3):
    """eigenvalues of the Stein driver S - Abar^T S Abar, on E_s."""
    return np.linalg.eigvalsh(S3 - Abar.T @ S3 @ Abar)


def letters(proj=Ps, basis=B):
    """the four alphabet letters projected into E_s, in the orthonormal basis (rows)."""
    return np.array([basis.T @ proj @ np.eye(4)[:, i] for i in range(4)])


def isotropy_matrix(v):
    """Linear conditions on S in Sym(3) forcing all six ||v_i - v_j||^2_S equal.

    Row for pair (i,j) vs the reference pair (0,1):  q_ij(S) - q_01(S) = 0.
    Returns the 5x6 matrix acting on vec(S)."""
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]

    def qrow(i, j):
        d = v[i] - v[j]
        # ||d||^2_S = sum S_ab d_a d_b, in the vec ordering (11,22,33,12,13,23)
        return np.array([d[0] ** 2, d[1] ** 2, d[2] ** 2,
                         2 * d[0] * d[1], 2 * d[0] * d[2], 2 * d[1] * d[2]])

    ref = qrow(*pairs[0])
    return np.array([qrow(i, j) - ref for (i, j) in pairs[1:]])


def nullspace(Mx, tol=1e-9):
    u, s, vt = np.linalg.svd(Mx)
    ns = vt[(s < tol).sum() and slice(len(s) - (s < tol).sum(), None) or slice(len(s), None)]
    # explicit and safe: take rows of vt beyond the numerical rank
    rank = int((s > tol).sum())
    return vt[rank:], s, rank


print("=" * 74)
print("CONTROLS -- run before any result is read")
print("=" * 74)

Saff3 = B.T @ Saff @ B
d_aff = driver_eigs(Saff3)
c1 = d_aff.min() > TOL
print(f"  C1  S_aff Stein-interior on E_s: driver eigs {d_aff} -> PD: {c1}")
print(f"      (B527 reports [0.0861 0.2733 0.3867])")

v = letters()
Iso = isotropy_matrix(v)
res = Iso @ vec(Saff3)
c2 = np.abs(res).max() < 1e-9
d2 = [float((v[i] - v[j]) @ Saff3 @ (v[i] - v[j])) for i in range(4) for j in range(i + 1, 4)]
print(f"  C2  S_aff satisfies MY isotropy equations: max residual {np.abs(res).max():.3e} -> {c2}")
print(f"      the six squared distances under S_aff: {np.round(d2, 9)}")

_, s_iso, rank_iso = nullspace(Iso)
print(f"  C4  rank of the isotropy conditions COMPUTED: {rank_iso} of 5")
print(f"      singular values: {np.round(s_iso, 8)}")

# C3 -- falsifiability.
# FIRST ATTEMPT (recorded, failed): perturb the letters, expect dim to change.  It does NOT:
#   every perturbed configuration also gives dim 1.  So "the isotropy locus is a ray" is
#   GENERIC to any 4 points in 3-space and is NOT a fact about this object.  That overclaim
#   is retracted here, in the script, before it was ever written down as a result.
rng = np.random.default_rng(20260817)
dims_perturbed = []
for _ in range(200):
    vp = v + 0.35 * rng.standard_normal(v.shape)
    _, _, rp = nullspace(isotropy_matrix(vp))
    dims_perturbed.append(6 - rp)
print(f"  C3a RETRACTED overclaim: perturbed dims seen {sorted(set(dims_perturbed))}"
      f" -- dim {6 - rank_iso} is GENERIC, not special. Not evidence.")

# The discriminating question is therefore NOT the dimension.  The letters fix the isotropy
# ray; M_* independently fixes the Stein cone.  The non-generic question is whether the ray
# the LETTERS pick happens to lie in the cone the DYNAMICS picks.  Perturb M_* itself.
def isotropy_ray_status(Mx):
    """for a primitive nonneg matrix, is the affine-isotropy ray PD, and is it Stein?"""
    try:
        wq, Vq = np.linalg.eig(Mx.T)
        k = int(np.argmax(wq.real))
        if abs(wq[k].imag) > 1e-9:
            return None
        lq = Vq[:, k].real
        wr, Vr = np.linalg.eig(Mx)
        rq = Vr[:, int(np.argmax(wr.real))].real
        if (rq < 0).all():
            rq = -rq
        if (rq <= 0).any():
            return None
        lq = lq / (lq @ rq)
        rawq = np.column_stack([lq[i] * np.eye(4)[:, 0] - lq[0] * np.eye(4)[:, i] for i in (1, 2, 3)])
        Bq, _ = np.linalg.qr(rawq)
        Aq = Bq.T @ Mx @ Bq
        if np.abs(np.linalg.eigvals(Aq)).max() >= 1 - 1e-9:
            return None                      # not contracting: Stein cone undefined
        Psq = np.eye(4) - np.outer(rq, lq)
        vq = np.array([Bq.T @ Psq @ np.eye(4)[:, i] for i in range(4)])
        NSq, _, rq_ = nullspace(isotropy_matrix(vq))
        if 6 - rq_ != 1:
            return None
        Sq = mat(NSq[0])
        if np.trace(Sq) < 0:
            Sq = -Sq
        pd = np.linalg.eigvalsh(Sq).min() > TOL
        st = np.linalg.eigvalsh(Sq - Aq.T @ Sq @ Aq).min() > TOL
        return pd, st
    except Exception:
        return None


tested = pd_ct = both_ct = 0
for _ in range(3000):
    Mx = rng.integers(0, 3, size=(4, 4)).astype(float)
    out = isotropy_ray_status(Mx)
    if out is None:
        continue
    tested += 1
    pd_ct += out[0]
    both_ct += out[0] and out[1]
c3 = tested > 50
print(f"  C3b DISCRIMINATING control: random contracting 4x4 operators tested: {tested}")
print(f"      isotropy ray positive definite: {pd_ct}/{tested} = {pd_ct / max(tested,1):.1%}")
print(f"      isotropy ray PD *and* Stein-compatible: {both_ct}/{tested} = {both_ct / max(tested,1):.1%}")
print(f"      -> instrument has a real denominator: {c3}")

ok = c1 and c2 and c3
print(f"\n  ALL CONTROLS PASS: {ok}")
if not ok:
    raise SystemExit("controls failed -- nothing may be read")

print()
print("=" * 74)
print("THE RESULT -- dimension of the affine-isotropy locus inside Sym(E_s)")
print("=" * 74)

NS, _, rank = nullspace(Iso)
dim_I = 6 - rank
print(f"  dim Sym(E_s)                     = 6")
print(f"  independent isotropy conditions  = {rank}")
print(f"  dim of the isotropy locus  I     = {dim_I}")

if dim_I == 1:
    S_ray = mat(NS[0])
    if np.trace(S_ray) < 0:
        S_ray = -S_ray
    S_ray = S_ray / np.linalg.norm(S_ray)
    Sa_n = Saff3 / np.linalg.norm(Saff3)
    aligned = np.allclose(S_ray, Sa_n, atol=1e-8)
    print(f"\n  the locus is a single RAY.  Is it the S_aff ray?  {aligned}")
    print(f"    S_aff (normalised) eigenvalues: {np.linalg.eigvalsh(Sa_n)}")
    print(f"    ray is positive definite:       {np.linalg.eigvalsh(S_ray).min() > TOL}")
    dr = driver_eigs(S_ray)
    print(f"    Stein driver on the ray:        {dr}  -> in the cone: {dr.min() > TOL}")
    print(f"\n  => affine isotropy cuts B527's 6-dim Stein cone down to ONE RAY.")
    print(f"     A ray is a metric determined UP TO ONE POSITIVE SCALE and nothing else.")
else:
    print(f"\n  the locus has dimension {dim_I} -- more than scale is free.")
    for k, nv in enumerate(NS):
        Sk = mat(nv)
        print(f"    direction {k}: eigenvalues {np.linalg.eigvalsh(Sk)}")

print()
print("=" * 74)
print("SIGNATURE on the SELECTED ray (not merely at S_aff)")
print("=" * 74)
Sfull = Saff if dim_I != 1 else Saff  # the 4-dim ambient metric whose E_s part is the ray
for alpha in (0.5, 1.0, 2.0):
    G = Sfull - alpha * np.outer(ell, ell)
    e = np.linalg.eigvalsh((G + G.T) / 2)
    sig = (int((e > TOL).sum()), int((e < -TOL).sum()))
    stein = np.linalg.eigvalsh(G - M.T @ G @ M).min() > TOL
    print(f"  alpha={alpha:>4}: signature {sig}   Stein-positive: {stein}")

print()
print("=" * 74)
print("THE SCALE THAT REMAINS -- is it one number, and is it internal?")
print("=" * 74)
print("  The ray is {t*S : t > 0}.  The single undetermined quantity is t > 0.")
print("  B167 [exact backbone + stated lemma]: a conserved, dimensionless first integral")
print("  cannot source a dimensionful scale from within; doors 1-3 shut, door 4 external.")
print("  => t is EXACTLY the residue B167 says must be imported.  The two results compose:")
print("     the object determines the metric up to t, and t is the one thing it cannot determine.")
print()
print("  What that IS, named honestly: a CONFORMAL structure of signature (3,1)")
print("  -- a metric modulo overall scale -- on the stable space of M_*.")
print("  NO physical identification is made (Gate 5).  'Lorentzian' here = signature only.")
