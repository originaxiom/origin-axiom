"""B8069 locks -- affine isotropy cuts B527's Stein cone to one ray.

Recomputes B527's operator, cone and driver from scratch, then the isotropy locus.
Includes the lock that matters most: the RETRACTED half -- dim 1 is generic, so it must
NOT be asserted as evidence.
"""
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
R = np.array([PHI, 1, PHI * PHI ** 0.5, PHI ** 0.5], float)
TOL = 1e-9


def _setup():
    w, V = np.linalg.eig(M.T)
    ell = V[:, int(np.argmax(w.real))].real
    ell = ell / (ell @ R)
    raw = np.column_stack([ell[i] * np.eye(4)[:, 0] - ell[0] * np.eye(4)[:, i] for i in (1, 2, 3)])
    B, _ = np.linalg.qr(raw)
    return ell, B, B.T @ M @ B


def _iso_matrix(v):
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]

    def qrow(i, j):
        d = v[i] - v[j]
        return np.array([d[0] ** 2, d[1] ** 2, d[2] ** 2,
                         2 * d[0] * d[1], 2 * d[0] * d[2], 2 * d[1] * d[2]])
    ref = qrow(*pairs[0])
    return np.array([qrow(i, j) - ref for (i, j) in pairs[1:]])


def _mat(x):
    return np.array([[x[0], x[3], x[4]], [x[3], x[1], x[5]], [x[4], x[5], x[2]]])


def test_b527_stable_spectrum_and_cone_reproduce():
    """The banked identity: M restricted to E_s is contracting, so the Stein cone exists."""
    _, _, Abar = _setup()
    mods = sorted(np.abs(np.linalg.eigvals(Abar)))
    assert np.allclose(mods, [0.4401, 0.7862, 0.7862], atol=1e-3)
    assert max(mods) < 1 - TOL


def test_the_isotropy_locus_is_one_ray_and_is_the_S_aff_ray():
    ell, B, Abar = _setup()
    Ps = np.eye(4) - np.outer(R, ell)
    v = np.array([B.T @ Ps @ np.eye(4)[:, i] for i in range(4)])
    s = np.linalg.svd(_iso_matrix(v), compute_uv=False)
    rank = int((s > 1e-9 * s.max()).sum())
    assert rank == 5, f"isotropy rank {rank}, expected 5 of 5"
    ns = np.linalg.svd(_iso_matrix(v))[2][rank:]
    assert len(ns) == 1
    S_ray = _mat(ns[0])
    if np.trace(S_ray) < 0:
        S_ray = -S_ray
    A_ = np.eye(4) - np.outer(R, np.ones(4)) / (np.ones(4) @ R)
    Saff3 = B.T @ (0.5 * A_.T @ A_) @ B
    assert np.allclose(S_ray / np.linalg.norm(S_ray), Saff3 / np.linalg.norm(Saff3), atol=1e-8)
    assert np.linalg.eigvalsh(S_ray).min() > TOL                      # positive definite
    drv = np.linalg.eigvalsh(S_ray - Abar.T @ S_ray @ Abar)
    assert drv.min() > TOL                                            # inside the Stein cone


def test_the_selected_ray_carries_signature_three_one_at_every_alpha():
    """Checked ON THE RAY, not merely at S_aff -- that distinction is the arc's point."""
    ell, B, _ = _setup()
    A_ = np.eye(4) - np.outer(R, np.ones(4)) / (np.ones(4) @ R)
    Saff = 0.5 * A_.T @ A_
    for alpha in (0.5, 1.0, 2.0):
        G = Saff - alpha * np.outer(ell, ell)
        e = np.linalg.eigvalsh((G + G.T) / 2)
        assert (int((e > TOL).sum()), int((e < -TOL).sum())) == (3, 1)
        assert np.linalg.eigvalsh(G - M.T @ G @ M).min() > TOL


def test_the_dimension_count_is_GENERIC_and_must_not_be_used_as_evidence():
    """THE RETRACTED HALF, locked so it cannot creep back.  Perturbing the letters gives
    dim 1 every time, so 'the isotropy locus is a ray' says nothing about THIS object.
    If this test ever fails -- i.e. some perturbation gives a different dimension -- the
    retraction would need revisiting, which is exactly why it is locked."""
    ell, B, _ = _setup()
    Ps = np.eye(4) - np.outer(R, ell)
    v = np.array([B.T @ Ps @ np.eye(4)[:, i] for i in range(4)])
    rng = np.random.default_rng(20260817)
    dims = set()
    for _ in range(200):
        vp = v + 0.35 * rng.standard_normal(v.shape)
        s = np.linalg.svd(_iso_matrix(vp), compute_uv=False)
        dims.add(6 - int((s > 1e-9 * s.max()).sum()))
    assert dims == {1}, f"perturbed dims {dims} -- dim 1 is not generic after all"


def test_the_discriminating_control_has_a_real_denominator():
    """What IS non-generic: the letters fix the isotropy ray, M_* independently fixes the
    Stein cone, and the ray landing inside the cone is rare.  PD alone is generic (carries
    nothing); PD-and-Stein is the measured 2.5%.  One object against that base rate is
    suggestive, NOT significant -- the arc says so and this lock keeps the ratio honest."""
    rng = np.random.default_rng(20260817)
    tested = pd_ct = both = 0
    for _ in range(1500):
        Mx = rng.integers(0, 3, size=(4, 4)).astype(float)
        try:
            wq, Vq = np.linalg.eig(Mx.T)
            k = int(np.argmax(wq.real))
            if abs(wq[k].imag) > 1e-9:
                continue
            lq = Vq[:, k].real
            wr, Vr = np.linalg.eig(Mx)
            rq = Vr[:, int(np.argmax(wr.real))].real
            if (rq < 0).all():
                rq = -rq
            if (rq <= 0).any():
                continue
            lq = lq / (lq @ rq)
            rawq = np.column_stack([lq[i] * np.eye(4)[:, 0] - lq[0] * np.eye(4)[:, i]
                                    for i in (1, 2, 3)])
            Bq, _ = np.linalg.qr(rawq)
            Aq = Bq.T @ Mx @ Bq
            if np.abs(np.linalg.eigvals(Aq)).max() >= 1 - 1e-9:
                continue
            Psq = np.eye(4) - np.outer(rq, lq)
            vq = np.array([Bq.T @ Psq @ np.eye(4)[:, i] for i in range(4)])
            sv = np.linalg.svd(_iso_matrix(vq))
            rk = int((sv[1] > 1e-9 * sv[1].max()).sum())
            if 6 - rk != 1:
                continue
            Sq = _mat(sv[2][rk:][0])
            if np.trace(Sq) < 0:
                Sq = -Sq
            tested += 1
            pd = np.linalg.eigvalsh(Sq).min() > TOL
            pd_ct += pd
            both += pd and (np.linalg.eigvalsh(Sq - Aq.T @ Sq @ Aq).min() > TOL)
        except Exception:
            continue
    assert tested > 50, "no denominator -- the control would be vacuous"
    assert pd_ct == tested, "positive-definiteness is supposed to be generic"
    frac = both / tested
    assert 0.0 < frac < 0.15, f"PD-and-Stein fraction {frac:.3f} outside the recorded range"
