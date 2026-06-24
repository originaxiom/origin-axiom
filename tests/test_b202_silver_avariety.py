"""B202 -- the silver SL(3) A-variety has no tidy [A,B]=c*mu^k relation (V195). Fast pyenv locks.

Loads shipped reps (frontier/B202_silver_avariety/reps.json): the figure-eight W1 (the validated gate,
[A,B]=c*mu^3) and silver reps (correct commuting meridian mu=A^-2 t, but NO tidy matrix exponent).
Deterministic, numpy-only (no Sage/scipy). Standalone character-variety math; nothing to CLAIMS.md.
"""
import os
import json
import numpy as np

HERE = os.path.dirname(__file__)
REPS = os.path.join(HERE, "..", "frontier", "B202_silver_avariety", "reps.json")


def _mat(M):
    return np.array([[complex(a, b) for (a, b) in row] for row in M], dtype=complex)


def matexp_score(comm, mu, kmax=8):
    """best (k, score) with [A,B] ~ c*mu^k; score~0 <=> tidy matrix relation holds."""
    best = (None, 9e9)
    for k in range(-kmax, kmax + 1):
        if k == 0:
            continue
        muk = np.linalg.matrix_power(mu, k) if k > 0 else np.linalg.matrix_power(np.linalg.inv(mu), -k)
        Mm = comm @ np.linalg.inv(muk)
        off = max(abs(Mm[i, j]) for i in range(3) for j in range(3) if i != j)
        dsp = max(abs(Mm[i, i] - Mm[0, 0]) for i in range(3))
        if off + dsp < best[1]:
            best = (k, off + dsp)
    return best


def _data():
    return json.load(open(REPS))


def test_figure_eight_gate_W1_is_mu_cubed():
    # the validated gate: figure-eight W1 satisfies [A,B] = c*mu^3 (M^3=L)
    d = _data()
    assert d["figure_eight_W1"], "no figure-eight W1 reps shipped"
    for r in d["figure_eight_W1"]:
        A, B, mu = _mat(r["A"]), _mat(r["B"]), _mat(r["mu"])
        comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
        k, sc = matexp_score(comm, mu)
        assert k == 3 and sc < 1e-6, (k, sc)


def test_silver_commuting_meridian_but_no_tidy_exponent():
    # silver: mu=A^-2 t commutes with [A,B] (correct meridian) but NO tidy [A,B]=c*mu^k
    d = _data()
    assert d["silver"], "no silver reps shipped"
    for r in d["silver"]:
        A, B, t = _mat(r["A"]), _mat(r["B"]), _mat(r["t"])
        mu = np.linalg.matrix_power(np.linalg.inv(A), 2) @ t        # silver meridian (B154)
        comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
        cdev = np.max(np.abs(mu @ comm - comm @ mu))
        assert cdev < 1e-4                                          # meridian genuinely commutes
        k, sc = matexp_score(comm, mu)
        assert sc > 1e-3                                            # ...but NO tidy matrix exponent


if __name__ == "__main__":
    test_figure_eight_gate_W1_is_mu_cubed()
    test_silver_commuting_meridian_but_no_tidy_exponent()
    print("ALL CHECKS PASS")
