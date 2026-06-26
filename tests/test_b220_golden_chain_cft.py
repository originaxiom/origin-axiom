"""B220 -- L41 closed: the golden (Fibonacci anyon) chain CFT reproduced in-sandbox (B218 residual).
Nothing to CLAIMS.md.

Load-bearing locks: (1) the model is GAPLESS (kills the prior gapped artifact: gap*N ~ const, not
growing), and (2) the AFM entanglement central charge ~ 0.7 (= 7/10 tricritical Ising), clearly
distinct from 0 (gapped) and from 0.8 (Potts). Small sizes for test speed; the reproducer goes larger.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B220_golden_chain_cft"))
from golden_chain import build_H, entanglement_c, basis  # noqa: E402
from scipy.sparse.linalg import eigsh  # noqa: E402


def _ground(N, sign):
    H, states = build_H(N, sign)
    ev, evec = eigsh(H, k=2, which="SA")
    o = np.argsort(ev)
    return ev[o[0]], ev[o[1]], evec[:, o[0]], states


def test_hilbert_space_is_fibonacci():
    # cyclic no-two-adjacent-0 count = Lucas numbers
    lucas = {6: 18, 8: 47, 10: 123, 12: 322}
    for N, L in lucas.items():
        assert len(basis(N)) == L


def test_afm_is_gapless_not_the_gapped_artifact():
    # the prior failure was a constant gap (c~0). Here gap*N stays ~const (gap ~ 1/N => gapless).
    gN = []
    for N in (12, 16, 20):
        e0, e1, _, _ = _ground(N, -1.0)
        gN.append((e1 - e0) * N)
    # gap*N roughly constant (not growing); and the bare gap shrinks with N
    assert max(gN) / min(gN) < 1.3
    g_small = _ground(12, -1.0)
    g_large = _ground(20, -1.0)
    assert (g_large[1] - g_large[0]) < (g_small[1] - g_small[0])


def test_afm_central_charge_is_7_over_10():
    cs = []
    for N in (16, 18, 20):
        _, _, psi, states = _ground(N, -1.0)
        cs.append(entanglement_c(psi, states, N))
    c = float(np.mean(cs))
    # clearly tricritical Ising 0.7: distinct from gapped (0) and from Potts (0.8)
    assert 0.60 < c < 0.78
    assert abs(c - 0.7) < abs(c - 0.0)
    assert abs(c - 0.7) < abs(c - 0.8)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
