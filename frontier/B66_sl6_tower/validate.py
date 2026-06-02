"""B66 validation -- the identical inverse-word pipeline run on SL(3..6).

Task 1 of the post-merge validation: run the SAME pipeline (automatic QR-pivot
inverse-word selection -> DT(eps)=DX.pinv(Dx) high-precision extrapolation ->
Dickson identification) on n=3,4,5,6 and confirm mult(|k|=3) = 1,1,2,2. SL(5)=2
is the load-bearing check: it has the same fixed-line gauge degeneracy that makes
SL(6) hard, so if the gauge-handling cannot recover the known SL(5)=2, the SL(6)
result is suspect. Numerical, high-precision; not a symbolic proof.

Run:  python frontier/B66_sl6_tower/validate.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy.linalg as sla

sys.path.insert(0, str(Path(__file__).resolve().parent))
import probe as PR  # audited primitives: expm_mp, svd_pinv, _extrap0, _trace, _eig_vals, _near_count


# --------------------------------------------------------------------------- #
# words and bases (general n)
# --------------------------------------------------------------------------- #

def reduced_words(maxlen):
    """All freely-reduced words in {A,B,A^-1,B^-1} (a=A^-1, b=B^-1), length 1..maxlen."""
    inv = {"A": "a", "a": "A", "B": "b", "b": "B"}
    out = []

    def rec(cur):
        if cur:
            out.append(cur)
        if len(cur) == maxlen:
            return
        for c in "ABab":
            if cur and inv[cur[-1]] == c:
                continue
            rec(cur + c)

    rec("")
    return out


def basis_sl_np(n):
    B = []
    for i in range(n):
        for j in range(n):
            if i != j:
                e = np.zeros((n, n), dtype=complex)
                e[i, j] = 1.0
                B.append(e)
    for i in range(n - 1):
        e = np.zeros((n, n), dtype=complex)
        e[i, i], e[i + 1, i + 1] = 1.0, -1.0
        B.append(e)
    return B


def _word_np(s, mm):
    R = np.eye(next(iter(mm.values())).shape[0], dtype=complex)
    for c in s:
        R = R @ mm[c]
    return R


def select_words(n, maxlen, seed):
    """QR-pivot select n^2-1 words whose trace-gradients are independent at a
    NEAR-fixed-line representation (double precision; the same selection rule the
    hardcoded SL5/SL6 sets came from -- inverse words keep rank near the fixed line)."""
    dim = n * n - 1
    rng = np.random.default_rng(seed)

    def sl():
        Z = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        return Z - np.trace(Z) / n * np.eye(n)

    eps = 0.05
    A, B = sla.expm(eps * sl()), sla.expm(eps * sl())
    Ai, Bi = np.linalg.inv(A), np.linalg.inv(B)
    cands = reduced_words(maxlen)
    basis = basis_sl_np(n)
    h = 1e-6
    G = np.zeros((len(cands), 2 * dim), dtype=complex)
    col = 0
    for g in basis:
        Ap, Am = (np.eye(n) + h * g) @ A, (np.eye(n) - h * g) @ A
        mp_ = {"A": Ap, "B": B, "a": np.linalg.inv(Ap), "b": Bi}
        mm_ = {"A": Am, "B": B, "a": np.linalg.inv(Am), "b": Bi}
        for r, s in enumerate(cands):
            G[r, col] = (np.trace(_word_np(s, mp_)) - np.trace(_word_np(s, mm_))) / (2 * h)
        col += 1
    for g in basis:
        Bp, Bm = (np.eye(n) + h * g) @ B, (np.eye(n) - h * g) @ B
        mp_ = {"A": A, "B": Bp, "a": Ai, "b": np.linalg.inv(Bp)}
        mm_ = {"A": A, "B": Bm, "a": Ai, "b": np.linalg.inv(Bm)}
        for r, s in enumerate(cands):
            G[r, col] = (np.trace(_word_np(s, mp_)) - np.trace(_word_np(s, mm_))) / (2 * h)
        col += 1
    _, _, piv = sla.qr(G.T, pivoting=True, mode="economic")
    sel = [cands[piv[i]] for i in range(dim)]
    rank = np.linalg.matrix_rank(G[[piv[i] for i in range(dim)], :], tol=1e-7)
    assert rank == dim, f"SL({n}): selected word set rank {rank} != {dim}"
    return sel


# --------------------------------------------------------------------------- #
# mpmath pipeline (general n) -- mirrors probe._diff_matrix / fixed_line_spectrum
# --------------------------------------------------------------------------- #

def _basis_mp(n):
    return PR._basis_sl(n)


def _random_PQ(n, seed):
    rng = np.random.default_rng(seed)

    def mk():
        Z = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        Z -= np.trace(Z) / n * np.eye(n)
        out = mp.zeros(n, n)
        for i in range(n):
            for j in range(n):
                out[i, j] = mp.mpc(float(Z[i, j].real), float(Z[i, j].imag))
        return out

    return mk(), mk()


def _words_mp(words, A, B):
    mm = {"A": A, "B": B, "a": mp.inverse(A), "b": mp.inverse(B)}
    out = []
    for s in words:
        R = mp.eye(A.rows)
        for c in s:
            R = R * mm[c]
        out.append(R)
    return out


def _diff_matrix(words, A, B, substitute, pp, pm, h, dim):
    M = mp.zeros(dim, 2 * dim)
    col = 0
    for Pp, Pm in zip(pp, pm):
        Ap, Am = Pp * A, Pm * A
        wp = _words_mp(words, Ap * B, Ap) if substitute else _words_mp(words, Ap, B)
        wm = _words_mp(words, Am * B, Am) if substitute else _words_mp(words, Am, B)
        for r in range(dim):
            M[r, col] = (PR._trace(wp[r]) - PR._trace(wm[r])) / (2 * h)
        col += 1
    for Pp, Pm in zip(pp, pm):
        Bp, Bm = Pp * B, Pm * B
        wp = _words_mp(words, A * Bp, A) if substitute else _words_mp(words, A, Bp)
        wm = _words_mp(words, A * Bm, A) if substitute else _words_mp(words, A, Bm)
        for r in range(dim):
            M[r, col] = (PR._trace(wp[r]) - PR._trace(wm[r])) / (2 * h)
        col += 1
    return M


def fixed_line_spectrum(n, words, seed=20, dps=60, deg=7):
    dim = n * n - 1
    mp.mp.dps = dps
    epss = [mp.mpf(e) for e in ("0.006", "0.009", "0.012", "0.015", "0.018", "0.021", "0.024", "0.027")]
    h = mp.mpf(10) ** (-(dps // 3))
    basis = _basis_mp(n)
    pp = [PR.expm_mp(h * g) for g in basis]
    pm = [PR.expm_mp(-h * g) for g in basis]
    Pm, Qm = _random_PQ(n, seed)
    dts = []
    for eps in epss:
        A, B = PR.expm_mp(eps * Pm), PR.expm_mp(eps * Qm)
        dx = _diff_matrix(words, A, B, False, pp, pm, h, dim)
        dX = _diff_matrix(words, A, B, True, pp, pm, h, dim)
        dts.append(dX * PR.svd_pinv(dx))
    dt0 = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            dt0[i, j] = mp.re(PR._extrap0(epss, [d[i, j] for d in dts], deg))
    return sorted(PR._eig_vals(dt0, dim), key=lambda z: (mp.re(z), mp.im(z)))


def mult_k3(spec, tol=mp.mpf("0.05")):
    """|k|=3 multiplicity by direct root matching (m=1): char(M^3)={4.236,-0.236},
    char(-M^3)={-4.236,0.236}."""
    big, small = float(2 + mp.sqrt(5)), float(2 - mp.sqrt(5))
    return (PR._near_count(spec, big, tol) + PR._near_count(spec, small, tol)
            + PR._near_count(spec, -big, tol) + PR._near_count(spec, -small, tol)) / 2


def main():
    print("B66 validation (Task 1) -- identical inverse-word pipeline on SL(3..6)")
    print("expected mult(|k|=3): SL(3)=1, SL(4)=1, SL(5)=2, SL(6)=2\n")
    plan = [(3, 4), (4, 4), (5, 4), (6, 5)]
    ok = True
    for n, ml in plan:
        words = select_words(n, ml, seed=20)
        spec = fixed_line_spectrum(n, words, seed=20)
        m3 = mult_k3(spec)
        expected = {3: 1, 4: 1, 5: 2, 6: 2}[n]
        flag = "OK" if m3 == expected else "MISMATCH"
        if m3 != expected:
            ok = False
        print(f"  SL({n}): dim {n*n-1:2d}, {len(words)} words (len<={ml}), "
              f"mult(|k|=3) = {m3}  (expected {expected})  {flag}")
    print()
    print("RESULT:", "all match -- pipeline recovers the known tower" if ok else "MISMATCH -- investigate")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
