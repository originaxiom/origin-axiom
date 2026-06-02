"""B66 validation Task 3 -- re-run the SL(6) pipeline at m=2 (and m=3).

The metallic substitution is phi_m(a)=a^m b, phi_m(b)=a; at m=2 the |k|=3 catalog
roots move to char(M^3)=t^2-L_3(2)t-1 with L_3(2)=14 (roots 7+-sqrt(50)), at m=3 to
L_3(3)=36.  Confirm the |k|=3 roots track L_3(m) and the multiplicity stays 2 --
this breaks any accidental m=1 (golden-ratio) root coincidence.  Same word set
(rep-level selection is m-independent), same DT extrapolation.  Numerical.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import probe as PR
import validate as V


def _diff_matrix_m(words, A, B, substitute, pp, pm, h, dim, m):
    """As validate._diff_matrix but with the general substitution A' = A^m B, B' = A."""
    M = mp.zeros(dim, 2 * dim)
    col = 0
    for Pp, Pm in zip(pp, pm):
        Ap, Am = Pp * A, Pm * A
        wp = V._words_mp(words, (Ap ** m) * B, Ap) if substitute else V._words_mp(words, Ap, B)
        wm = V._words_mp(words, (Am ** m) * B, Am) if substitute else V._words_mp(words, Am, B)
        for r in range(dim):
            M[r, col] = (PR._trace(wp[r]) - PR._trace(wm[r])) / (2 * h)
        col += 1
    for Pp, Pm in zip(pp, pm):
        Bp, Bm = Pp * B, Pm * B
        wp = V._words_mp(words, (A ** m) * Bp, A) if substitute else V._words_mp(words, A, Bp)
        wm = V._words_mp(words, (A ** m) * Bm, A) if substitute else V._words_mp(words, A, Bm)
        for r in range(dim):
            M[r, col] = (PR._trace(wp[r]) - PR._trace(wm[r])) / (2 * h)
        col += 1
    return M


def spectrum_m(n, words, m, seed=20, dps=60, deg=7):
    dim = n * n - 1
    mp.mp.dps = dps
    epss = [mp.mpf(e) for e in ("0.006", "0.009", "0.012", "0.015", "0.018", "0.021", "0.024", "0.027")]
    h = mp.mpf(10) ** (-(dps // 3))
    basis = V._basis_mp(n)
    pp = [PR.expm_mp(h * g) for g in basis]
    pm = [PR.expm_mp(-h * g) for g in basis]
    Pm, Qm = V._random_PQ(n, seed)
    dts = []
    for eps in epss:
        A, B = PR.expm_mp(eps * Pm), PR.expm_mp(eps * Qm)
        dx = _diff_matrix_m(words, A, B, False, pp, pm, h, dim, m)
        dX = _diff_matrix_m(words, A, B, True, pp, pm, h, dim, m)
        dts.append(dX * PR.svd_pinv(dx))
    dt0 = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            dt0[i, j] = mp.re(PR._extrap0(epss, [d[i, j] for d in dts], deg))
    return sorted(PR._eig_vals(dt0, dim), key=lambda z: (mp.re(z), mp.im(z)))


def lucas(k, m):
    return PR._trace(mp.matrix([[m, 1], [1, 0]]) ** k)


def main():
    print("B66 validation Task 3 -- SL(6) at m=2, m=3 (breaks m=1 coincidence)\n")
    n = 6
    words = V.select_words(6, 5, seed=20)
    for m in (2, 3):
        L3 = lucas(3, m)
        big = (L3 + mp.sqrt(L3 ** 2 + 4)) / 2     # char(M^3)=t^2-L_3 t-1, big root (isolated)
        # mult(|k|=3) = (#eigenvalues near char(M^3) big root +big) + (near char(-M^3) big root -big).
        # The BIG roots are well separated for all m; the SMALL roots of every char(M^k)
        # collapse toward 0 as m grows, so only the big roots give a reliable count.
        spec = spectrum_m(n, words, m)
        tol = mp.mpf("0.5")
        nb_pos = PR._near_count(spec, float(big), tol)   # char(M^3) copies
        nb_neg = PR._near_count(spec, float(-big), tol)   # char(-M^3) copies
        m3 = nb_pos + nb_neg
        near = sorted([float(mp.re(e)) for e in spec if abs(abs(mp.re(e)) - float(big)) < 1.0])
        print(f"  m={m}: L_3(m)={int(L3)}  char(M^3)/char(-M^3) big roots = +-{mp.nstr(big,9)}")
        print(f"        eigenvalues near +-big: {[round(x,6) for x in near]}  "
              f"(char(M^3) x{nb_pos}, char(-M^3) x{nb_neg})")
        print(f"        mult(|k|=3) = {m3}  (expected 2)\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
