"""B631 lock — the matrix comparison run (sealed protocol).

Fast: both seals in the ledger; D_obs and the 0/9 tier counts
recomputed deterministically. OA_SLOW=1: the seeded 10^6 Haar null
reproduced exactly (p_D count 700004).
"""
import hashlib
import itertools
import math
import os

import numpy as np
import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
FRONTIER = os.path.join(HERE, "..", "frontier")


def _seals():
    ledger = open(os.path.join(
        FRONTIER, "B598_l85_campaign", "ARTIFACT_HASHES.txt")).read()
    return ledger


def test_both_seals_in_ledger():
    ledger = _seals()
    for rel in ("B629_interaction_values/SEALED_INTERACTION_VALUES.md",
                "B630_matrix_comparison_design/COMPARISON_DESIGN.md"):
        h = hashlib.sha256(
            open(os.path.join(FRONTIER, rel), "rb").read()).hexdigest()
        assert h in ledger, rel


def _setup():
    A2 = np.array([(4 / 7) * math.sin(2 * math.pi * k / 7) ** 2
                   for k in (1, 2, 3)])
    B2 = A2[np.array([[0, 1, 2], [1, 2, 0], [2, 0, 1]])]
    s12, s23, s13 = map(math.sqrt, (0.307, 0.546, 0.0220))
    c12, c23, c13 = (math.sqrt(1 - v * v) for v in (s12, s23, s13))
    e = complex(math.cos(1.19 * math.pi), math.sin(1.19 * math.pi))
    U = np.array([
        [c12 * c13, s12 * c13, s13 * e.conjugate()],
        [-s12 * c23 - c12 * s23 * s13 * e,
         c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * e,
         -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])
    PM = np.abs(U) ** 2
    perms = list(itertools.permutations(range(3)))
    base = np.arange(9).reshape(3, 3)
    idx = np.array([T[np.ix_(p, q)].ravel()
                    for T in (base, base.T) for p in perms for q in perms])
    return B2, PM, idx


def test_d_obs_and_tier_counts():
    B2, PM, idx = _setup()
    variants = B2.ravel()[idx]
    d = np.sqrt(((variants - PM.ravel()) ** 2).mean(axis=1))
    D_obs = float(d.min())
    assert abs(D_obs - 0.13407059) < 1e-7
    best = variants[d.argmin()]
    dev = np.abs(best - PM.ravel())
    assert int((dev <= 0.01).sum()) == 0
    assert int((dev <= 0.001).sum()) == 0


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="10^6-sample seeded null (OA_SLOW=1)")
def test_seeded_null_reproduces_exactly():
    B2, PM, idx = _setup()
    variants = B2.ravel()[idx]
    d = np.sqrt(((variants - PM.ravel()) ** 2).mean(axis=1))
    D_obs = float(d.min())
    rng = np.random.default_rng(20260715)
    pm_flat = PM.ravel()
    N, CHUNK, count = 10 ** 6, 20000, 0
    done = 0
    while done < N:
        n = min(CHUNK, N - done)
        Z = (rng.standard_normal((n, 3, 3))
             + 1j * rng.standard_normal((n, 3, 3))) / math.sqrt(2)
        Q, R = np.linalg.qr(Z)
        ph = np.einsum('nii->ni', R)
        Q = Q * (ph / np.abs(ph))[:, None, :]
        P = (np.abs(Q) ** 2).reshape(n, 9)
        dm = np.sqrt(((P[:, idx] - pm_flat) ** 2).mean(axis=2)).min(axis=1)
        count += int((dm <= D_obs).sum())
        done += n
    assert count == 700004, count


def test_pipeline_controls_fast():
    """Trimmed C1/C2/C5 from b631_controls.py (the full run is banked in
    controls_output.txt): self-match gives D=0 and the minimum p; a
    near-PMNS unitary scores far below the sealed D; paths agree."""
    B2, PM, idx = _setup()
    pm_flat = PM.ravel()

    def stat(flat9):
        return float(np.sqrt(((flat9[idx] - pm_flat) ** 2).mean(axis=1)).min())

    assert stat(pm_flat) < 1e-12                      # C1: self-match D = 0
    rng = np.random.default_rng(7)
    K = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    K = (K + K.conj().T) / 2
    w, V = np.linalg.eigh(K)
    s12, s23, s13 = map(math.sqrt, (0.307, 0.546, 0.0220))
    c12, c23, c13 = (math.sqrt(1 - v * v) for v in (s12, s23, s13))
    e = complex(math.cos(1.19 * math.pi), math.sin(1.19 * math.pi))
    U = np.array([
        [c12 * c13, s12 * c13, s13 * e.conjugate()],
        [-s12 * c23 - c12 * s23 * s13 * e,
         c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * e,
         -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])
    Ue = U @ (V @ np.diag(np.exp(1j * 0.02 * w)) @ V.conj().T)
    D_near = stat((np.abs(Ue) ** 2).ravel())
    D_obs = stat(B2.ravel())
    assert D_near < 0.02 < D_obs                      # C2: power ordering
    flat = B2.ravel()
    d_loop = min(math.sqrt(sum((flat[i] - pm_flat[k]) ** 2
                               for k, i in enumerate(row)) / 9)
                 for row in idx)
    assert abs(d_loop - D_obs) < 1e-15                # C5: path consistency
