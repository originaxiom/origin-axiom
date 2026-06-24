"""B200 -- chat1 handoff verification (V193). Fast locks.

Locks the two substantive verdicts: R2 VERIFIED (on-site uniquely preserves Sturmian) and
R1 REFUTED (the U=t doublon 'fixed point' is out-of-regime + the claimed verification was circular).
Standalone condensed-matter / symbolic-dynamics math; nothing to CLAIMS.md.
"""
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B200_chat1_handoff_verification"))
from sturmian_interaction import fib_word, complexity, _fib_potential  # noqa: E402
import numpy as np  # noqa: E402


def test_r2_onsite_unique_sturmian():
    w = fib_word(987)
    assert [complexity(w, L) for L in range(1, 6)] == [2, 3, 4, 5, 6]   # single Fibonacci IS Sturmian
    assert "11" not in w
    nn = "".join(str(int(w[i]) + int(w[i + 1])) for i in range(len(w) - 1))
    assert len(set(nn)) == 2                                            # NN has 2 values
    assert complexity(nn, 4) == 6                                       # ...but p(4)=6 -> NOT Sturmian
    nnn_vals = set(int(w[i]) + int(w[i + 2]) for i in range(len(w) - 2))
    assert len(nnn_vals) == 3                                           # NNN has 3 values


def test_r1_doublon_refuted():
    # the true 2-body Hubbard doublon does NOT match the t_eff=2t^2/U prediction at U=t (out of regime),
    # but does at U>>t -- so the handoff's 'exact fixed point at U=t' is vacuous/circular.
    N, t = 13, 1.0
    Vsite = _fib_potential(N)
    idx = lambda a, b: a * N + b

    def rms_and_gap(U):
        H = np.zeros((N * N, N * N))
        for a in range(N):
            for b in range(N):
                s = idx(a, b)
                H[s, s] = Vsite[a] + Vsite[b] + (U if a == b else 0.0)
                for ap in (a - 1, a + 1):
                    if 0 <= ap < N:
                        H[idx(ap, b), s] += -t
                for bp in (b - 1, b + 1):
                    if 0 <= bp < N:
                        H[idx(a, bp), s] += -t
        ev = np.sort(np.linalg.eigvalsh(H))
        band, below = ev[-N:], ev[-N - 1]
        teff = 2 * t ** 2 / U
        Hd = np.diag(2 * Vsite + U).astype(float)
        for i in range(N - 1):
            Hd[i, i + 1] = Hd[i + 1, i] = -teff
        pred = np.sort(np.linalg.eigvalsh(Hd))
        return float(np.sqrt(np.mean((band - pred) ** 2))), float(band[0] - below)

    rms_ut, gap_ut = rms_and_gap(1.0)     # U=t: out of regime
    rms_strong, _ = rms_and_gap(20.0)     # U>>t: PT valid
    assert rms_ut > 2.0 and gap_ut < 0.3  # no doublon band, huge mismatch at U=t
    assert rms_strong < 0.3               # the formula is a strong-coupling result


if __name__ == "__main__":
    test_r2_onsite_unique_sturmian()
    test_r1_doublon_refuted()
    print("ALL CHECKS PASS")
