"""QP-2 private states -- locks for the fiber dimension computation."""
import importlib.util
import math
import os

import numpy as np


T = (1 + 1j * math.sqrt(3)) / 2
A_MAT = np.array([[1, 1], [0, 1]], dtype=complex)
B_MAT = np.array([[1, 0], [T, 1]], dtype=complex)
BASE = {"a": A_MAT, "b": B_MAT,
        "A": np.linalg.inv(A_MAT), "B": np.linalg.inv(B_MAT)}
REL = "abABaBAbaB"


def _mul(poly, c0, c1):
    new = {}
    for yp, co in poly.items():
        new[yp] = new.get(yp, 0j) + co * c0
        new[yp + 1] = new.get(yp + 1, 0j) + co * c1
    return new


def symn(M, n):
    p, q, r, s = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    out = np.zeros((n + 1, n + 1), dtype=complex)
    for j in range(n + 1):
        poly = {0: 1.0 + 0j}
        for _ in range(n - j):
            poly = _mul(poly, p, q)
        for _ in range(j):
            poly = _mul(poly, r, s)
        for yp, co in poly.items():
            out[yp, j] = co
    return out.T


def _fox_data(k):
    n = 2 * k
    dim = n + 1
    S = {ch: symn(BASE[ch], n) for ch in "abAB"}
    seq = [(ch.lower(), 1 if ch.islower() else -1) for ch in REL]

    def fox(j):
        tot = np.zeros((dim, dim), dtype=complex)
        pre = np.eye(dim, dtype=complex)
        for g, s in seq:
            Mg = S[g] if s == 1 else S[g.upper()]
            if g == j:
                tot += pre if s == 1 else -(pre @ Mg)
            pre = pre @ Mg
        return tot

    fa, fb = fox("a"), fox("b")
    d1 = np.hstack([fa, fb])
    d0 = np.vstack([S["a"] - np.eye(dim, dtype=complex),
                    S["b"] - np.eye(dim, dtype=complex)])
    return d1, d0, S, dim


def test_riley_relator():
    P = np.eye(2, dtype=complex)
    for ch in REL:
        P = P @ BASE[ch]
    assert np.allclose(P, np.eye(2), atol=1e-12)


def test_symn_homomorphism():
    for n in [2, 4, 6]:
        AB = A_MAT @ B_MAT
        assert np.allclose(symn(A_MAT, n) @ symn(B_MAT, n), symn(AB, n), atol=1e-10)


def test_cocycle_identity():
    """d1 @ d0 = 0 (coboundaries are cocycles)."""
    for k in range(1, 4):
        d1, d0, _, _ = _fox_data(k)
        assert np.linalg.norm(d1 @ d0) < 1e-10


def test_dim_h1_is_one():
    """dim H^1(Sym^{2k}) = 1 for k = 1, 2, 3 (Menal-Ferrer-Porti)."""
    for k in range(1, 4):
        d1, d0, _, dim = _fox_data(k)
        rank_d1 = np.linalg.matrix_rank(d1, tol=1e-8)
        rank_d0 = np.linalg.matrix_rank(d0, tol=1e-8)
        dim_H1 = (2 * dim - rank_d1) - rank_d0
        assert dim_H1 == 1, f"k={k}: dim H^1 = {dim_H1}"


def test_last_row_sa_minus_i_zero():
    """Last row of (S_a - I) is zero in the transposed convention."""
    for k in range(1, 4):
        _, _, S, dim = _fox_data(k)
        last_row = (S["a"] - np.eye(dim, dtype=complex))[dim - 1, :]
        assert np.linalg.norm(last_row) < 1e-12


def test_fixed_vector_is_e0():
    """Fixed vector of S_a in the transposed convention is e_0."""
    for k in range(1, 4):
        _, _, S, dim = _fox_data(k)
        e0 = np.zeros(dim, dtype=complex)
        e0[0] = 1.0
        assert np.allclose(S["a"] @ e0, e0, atol=1e-12)


def test_phi_mu_nonzero():
    """K-functional phi_mu = f_a[last] is nonzero for all k = 1, 2, 3."""
    for k in range(1, 4):
        d1, _, _, dim = _fox_data(k)
        _, s_vals, Vh = np.linalg.svd(d1, full_matrices=True)
        tol = max(s_vals) * 1e-10
        null_vecs = [Vh[i] for i in range(Vh.shape[0])
                     if (s_vals[i] if i < len(s_vals) else 0) < tol]
        best = max(abs(nv[dim - 1]) for nv in null_vecs)
        assert best > 0.1, f"k={k}: max |phi_mu| = {best}"


def test_fiber_dim_zero():
    """fiber_dim(n) = 0 for n = 2, 3, 4."""
    for n in [2, 3, 4]:
        exps = list(range(1, n))
        dim_total = 0
        rank_total = 0
        for k in exps:
            d1, d0, _, dim = _fox_data(k)
            rank_d1 = np.linalg.matrix_rank(d1, tol=1e-8)
            rank_d0 = np.linalg.matrix_rank(d0, tol=1e-8)
            dim_H1 = (2 * dim - rank_d1) - rank_d0
            dim_total += dim_H1
            _, s_vals, Vh = np.linalg.svd(d1, full_matrices=True)
            tol = max(s_vals) * 1e-10
            null_vecs = [Vh[i] for i in range(Vh.shape[0])
                         if (s_vals[i] if i < len(s_vals) else 0) < tol]
            best = max(abs(nv[dim - 1]) for nv in null_vecs)
            if best > 1e-8:
                rank_total += 1
        assert dim_total - rank_total == 0, f"SL({n}): fiber_dim = {dim_total - rank_total}"


def test_d1_gap_clean():
    """Singular value gap ratios > 10^4 for all rank claims."""
    for k in range(1, 4):
        d1, _, _, _ = _fox_data(k)
        sv = sorted(np.linalg.svd(d1, compute_uv=False), reverse=True)
        rank = sum(1 for s in sv if s > 1e-8)
        if rank < len(sv):
            gap = sv[rank - 1] / max(sv[rank], 1e-300)
            assert gap > 1e4, f"k={k}: gap = {gap}"


def test_b264_cross_validation():
    """dim H^1 matches B264's mpmath computation for k = 1, 2, 3."""
    here = os.path.dirname(__file__) or "."
    b264_path = os.path.join(here, "..", "frontier",
                             "B264_e6_character_variety", "e6_charvar_tangent.py")
    spec = importlib.util.spec_from_file_location("b264", b264_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for k in range(1, 4):
        d1, d0, _, dim = _fox_data(k)
        rank_d1 = np.linalg.matrix_rank(d1, tol=1e-8)
        rank_d0 = np.linalg.matrix_rank(d0, tol=1e-8)
        dim_H1 = (2 * dim - rank_d1) - rank_d0
        assert dim_H1 == mod.H1_sym(k), f"k={k}: mismatch"
