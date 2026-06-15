"""B153 -- rank-stratified degeneration of degree=rank (V142).

Locks the deterministic facts: the toolkit self-test (B89 n=4: L=-M^4, irreducible, slice tangent 19),
and the n=5 semisimple involution argument (A^2=I => B=tAt^-1 => B^2=I => dihedral => reducible).
The n=3 rigid component and the n=5 non-semisimple absence are numerical/Sage results recorded in
FINDINGS.md (not in this fast test).
"""
import importlib.util
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
B153 = ROOT / "frontier" / "B153_degree_rank_degeneration"


def _toolkit():
    spec = importlib.util.spec_from_file_location("sln_toolkit", B153 / "sln_toolkit.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def test_toolkit_selftest_n4_slice():
    tk = _toolkit()
    tk._selftest()  # asserts B89 n=4: L=-M^4, irreducible, tangent 19, spectrum moves (slice)


def test_n5_semisimple_is_dihedral_reducible():
    """A^2=I => B=A^-2 t A t^-1 = t A t^-1 => B^2 = t A^2 t^-1 = I, for ANY t."""
    tk = _toolkit()
    A = np.diag([1, 1, 1, -1, -1]).astype(complex)
    assert np.allclose(A @ A, np.eye(5))
    rng = np.random.default_rng(1)
    for _ in range(5):
        t = rng.standard_normal((5, 5)) + 1j * rng.standard_normal((5, 5))
        B = tk.Bfrom(A, t)
        assert np.allclose(B @ B, np.eye(5), atol=1e-8)  # B is an involution => <A,B> dihedral => reducible


def test_probe_runs():
    spec = importlib.util.spec_from_file_location("b153_probe", B153 / "probe.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    assert m.check_n4_slice() and m.check_n5_semisimple_dihedral()


def test_n5_nonss_irreducible_exists_but_degree_rank_fails():
    """B153 correction (2026-06-15): n=5 non-ss has IRREDUCIBLE reps (the old '0/120 absent' was a
    det t=0-drift artifact), but degree=rank L=(-1)^(n-1)M^n FAILS on them. Fast deterministic check on
    the [3]|[1,1] Jordan type using two independent irreducibility certificates (Burnside + commutant)."""
    n = 5

    def jblock(lam, k):
        M = lam * np.eye(k, dtype=complex)
        for i in range(k - 1):
            M[i, i + 1] = 1.0
        return M

    A = np.zeros((n, n), dtype=complex)
    A[:3, :3] = jblock(1, 3); A[3, 3] = -1; A[4, 4] = -1
    assert not np.allclose(A @ A, np.eye(n))          # genuinely non-semisimple
    assert abs(np.linalg.det(A) - 1) < 1e-12          # in SL(5)

    def star(t):
        return t @ np.linalg.inv(A @ A) @ t @ A - np.linalg.inv(A) @ t @ A @ t

    def Bof(t):
        return np.linalg.inv(A @ A) @ t @ A @ np.linalg.inv(t)

    def solve(rng, iters=400):
        t = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        for _ in range(iters):
            g = np.concatenate([star(t).reshape(-1), [np.linalg.det(t) - 1.0]])
            if np.max(np.abs(g)) < 1e-12:
                break
            h = 1e-7; tf = t.reshape(-1); J = np.zeros((g.size, n * n), complex)
            for k in range(n * n):
                tp = tf.copy(); tp[k] += h
                gp = np.concatenate([star(tp.reshape(n, n)).reshape(-1),
                                     [np.linalg.det(tp.reshape(n, n)) - 1.0]])
                J[:, k] = (gp - g) / h
            st, *_ = np.linalg.lstsq(J, g, rcond=None); t = (tf - st).reshape(n, n)
        return t

    def burnside_rank(B, rounds=4):
        gens = [A, B, np.linalg.inv(A), np.linalg.inv(B)]
        allm = [np.eye(n, dtype=complex)]; fr = [np.eye(n, dtype=complex)]
        for _ in range(rounds):
            fr = [g @ m for m in fr for g in gens]; allm += fr
        W = np.array([m.reshape(-1) for m in allm])
        W = W / np.maximum(np.linalg.norm(W, axis=1, keepdims=True), 1e-300)
        s = np.linalg.svd(W, compute_uv=False)
        return int(np.sum(s > 1e-6 * s[0]))

    def commutant_dim(B):
        I5 = np.eye(n)
        L = np.vstack([np.kron(A.T, I5) - np.kron(I5, A), np.kron(B.T, I5) - np.kron(I5, B)])
        s = np.linalg.svd(L, compute_uv=False)
        return int(np.sum(s < 1e-8 * s[0]))

    rng = np.random.default_rng(2026)
    found_irr = False
    for _ in range(40):
        t = solve(rng)
        if np.max(np.abs(star(t))) > 1e-9 or abs(np.linalg.det(t) - 1) > 1e-8:
            continue
        if np.linalg.cond(t) > 1e4:
            continue
        B = Bof(t)
        if burnside_rank(B) == n * n and commutant_dim(B) == 1:   # two independent certificates agree
            found_irr = True
            # degree=rank must FAIL on this irreducible rep (best match over n=2..8 is far from 0)
            mu = np.linalg.inv(A) @ t
            comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B); dt = np.linalg.det(t)
            best = min(np.max(np.abs(comm - ((-1) ** (k - 1)) * np.linalg.matrix_power(mu, k) / dt))
                       for k in (2, 3, 4, 5, 6, 7, 8))
            assert best > 1.0, f"degree=rank unexpectedly (nearly) holds at n=5: {best}"
            break
    assert found_irr, "expected an irreducible non-semisimple SL(5) rep with spectrum {1,1,1,-1,-1}"
