"""B187 -- the open/interacting many-body collective (V181). Fast locks.

B183's thresholdless arrow (single-particle, Hatano-Nelson g_c~0) PERSISTS with interactions: the
permanently-critical metallic chain's many-body point-gap threshold g_c(U) stays ~0 for all U (interaction
opens no protective gap), while the Aubry-Andre localized control stays protected (finite g_c) at all U.
Full version in interacting_open.py.
"""
import numpy as np
from itertools import combinations
np.seterr(over="ignore", invalid="ignore")

phi = (1 + 5**0.5)/2; alpha = 1/phi
def _V_met(L, lam=1.0):
    n = np.arange(1, L+1); return lam*(((n*alpha) % 1.0) >= 1.0 - alpha).astype(float)
def _V_aa(L, lam=4.0):
    n = np.arange(1, L+1); return 2*lam*np.cos(2*np.pi*alpha*n)


def _H(L, npart, V, g, U):
    basis = list(combinations(range(L), npart)); idx = {b: i for i, b in enumerate(basis)}
    D = len(basis); H = np.zeros((D, D), dtype=complex); f, b = np.exp(g), np.exp(-g)
    for bi, occ in enumerate(basis):
        occs = set(occ)
        H[bi, bi] += sum(V[s] for s in occ) + U*sum(1 for s in occ if ((s+1) % L) in occs)
        for s in occ:
            for nbr, amp in (((s+1) % L, f), ((s-1) % L, b)):
                if nbr in occs: continue
                new = tuple(sorted(occs - {s} | {nbr}))
                lo, hi = min(s, nbr), max(s, nbr); sign = (-1)**sum(1 for x in occ if lo < x < hi)
                H[idx[new], bi] += amp*sign
    return H


def _maximag(H): return float(np.max(np.abs(np.linalg.eigvals(H).imag)))
def _g_c(L, npart, V, U, tol=1e-6, gmax=2.5, steps=16):
    if _maximag(_H(L, npart, V, 1e-4, U)) > tol: return 0.0
    if _maximag(_H(L, npart, V, gmax, U)) < tol: return float("inf")
    lo, hi = 0.0, gmax
    for _ in range(steps):
        mid = (lo+hi)/2
        if _maximag(_H(L, npart, V, mid, U)) > tol: hi = mid
        else: lo = mid
    return hi


def test_metallic_arrow_thresholdless_with_interaction():
    L = 12
    for U in (0.0, 1.0, 2.0):
        assert _g_c(L, 2, _V_met(L), U) < 0.15      # interaction opens no protective gap


def test_localized_control_protected_with_interaction():
    L = 12
    for U in (0.0, 1.0, 2.0):
        gm = _g_c(L, 2, _V_met(L), U); ga = _g_c(L, 2, _V_aa(L), U)
        assert ga > 0.4                              # localized stays protected
        assert ga > 8 * max(gm, 1e-3)                # metallic far more fragile
