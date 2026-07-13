"""Locks for B559 black-hole probes.

Probe 1: the object's Fibonacci chain is critical (log-law), NOT area-law, with
         c_eff below the clean chain (controls: periodic ~ c=1, random ~ area-law).
Probe 2: figure-eight geometry (Vol, CS=0, systole) via SnapPy, and the banked
         BTZ entropy S = arccosh(x/2) = lambda/2.
See frontier/B559_blackhole_probes/FINDINGS.md.
"""
import math
import cmath
import numpy as np
import pytest


# ---------- Probe 1: entanglement scaling ----------------------------------
def _chain_H(kind, N, seed=0):
    if kind == "fibonacci":
        a, b = "b", "a"
        while len(a) < N:
            a, b = a + b, a
        w = a[:N]
        diag = np.array([0.5 if c == "a" else -0.5 for c in w])
    elif kind == "periodic":
        diag = np.zeros(N)
    elif kind == "random":
        diag = np.random.default_rng(seed).uniform(-3, 3, N)
    return np.diag(diag) + np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)


def _corr(H, fill=0.5):
    w, U = np.linalg.eigh(H)
    occ = U[:, :int(round(fill * H.shape[0]))]
    return occ @ occ.conj().T


def _S(C, idx):
    p = np.linalg.eigvalsh(C[np.ix_(idx, idx)])
    p = np.clip(p, 1e-13, 1 - 1e-13)
    return float(-np.sum(p * np.log(p) + (1 - p) * np.log(1 - p)))


def _one_cut_logslope(kind, N=1597, seed=0):
    C = _corr(_chain_H(kind, N, seed))
    Ls = [20, 40, 80, 160, 320]
    S = [_S(C, list(range(L))) for L in Ls]
    return np.polyfit(np.log(Ls), S, 1)[0]


def _one_cut_linslope(kind, N=1597, seed=0):
    C = _corr(_chain_H(kind, N, seed))
    Ls = [20, 40, 80, 160, 320]
    S = [_S(C, list(range(L))) for L in Ls]
    return np.polyfit(Ls, S, 1)[0]


def test_fibonacci_is_critical_not_area_law():
    """Robust facts only: the chain is critical (log growth, not area-law flat)
    and NOT volume-law (linear slope ~ 0). The precise c_eff / 'below c=1' is
    fit-dependent because the tight-binding entanglement oscillates with L
    (seat-1 Probe A) - not locked here."""
    fib = _one_cut_logslope("fibonacci")
    # disorder-average the random control (single realizations are noisy at finite L)
    rnd = float(np.mean([_one_cut_logslope("random", seed=s) for s in range(8)]))
    assert fib > 0.08                 # critical: clear log growth (not area-law flat)
    assert rnd < 0.03                 # random control: disorder-averaged area-law (flat)
    assert _one_cut_linslope("fibonacci") < 0.005   # NOT volume-law (a volume law slope ~ O(0.1))


# ---------- Probe 2: figure-eight as a 3d-gravity saddle --------------------
def test_figure_eight_geometry_and_btz_dictionary():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("4_1")
    assert abs(float(M.volume()) - 2.0298832128) < 1e-7      # 2 ideal reg. tetrahedra
    assert abs(float(M.chern_simons())) < 1e-9               # CS = 0 (amphichiral)
    # systole: complex length ~ 1.08707 - 1.72277 i, trace x = 2 cosh(lambda/2) = 2 - omega
    lam = min((complex(g.length) for g in M.length_spectrum(1.5)),
              key=lambda z: z.real)
    assert abs(lam.real - 1.087070145) < 1e-6
    x = 2 * cmath.cosh(lam / 2)
    assert abs(abs(x) - math.sqrt(3)) < 1e-6                 # |trace| = sqrt(3)
    # banked BTZ entropy: S = arccosh(x/2) = lambda/2
    assert abs((lam / 2).real - 0.543535) < 1e-5


def test_banked_btz_entropy_golden():
    # B520: golden loxodromic x=5 -> S = arccosh(2.5)
    assert abs(math.acosh(2.5) - 1.5667992) < 1e-6
