#!/usr/bin/env python3
"""SEARCH V3: the one-Higgs search for the holomorphic reading (A1: one direction h read S in every sector), with the
grid stage separated from the targets and a basin-hopping stage added.  Written after THE HOLOMORPHIC READING TEST's
power control (holo_c2.json: 33 of 36, short of its 34) and the data-free diagnoses e10 (the missed basins are narrower
than the grid's spacing) and e11 (hopping from the best solution recovers them); no target from the data is read here.
  stage 1  the A1 nine on sm_search's 112 800 directions, computed once per row (grid_logs) and shared by every target;
  stage 2  starts: the best 16 grid directions pairwise more than 0.05 rad apart, and the best 8 (by chi2) of the record's 26
           directions (its 13 forms at tau and their conjugates);
  stage 3  least squares from each start (one_higgs_search.refine: scipy trf, at most 400 evaluations);
  stage 4  basin hopping: rounds of 12 perturbations of the current best direction, three each at Fubini-Study angles
           0.01, 0.02, 0.04 and 0.08 rad, each refined; a round that lowers the best by more than 1e-6 is followed by
           another, at most 4 rounds.  The perturbations' random directions come from numpy's default_rng(seed).
    import search_v3; search_v3.search3(Uh, extra, T, SIG, L=None, seed=0) -> (grid minimum, (chi2, x))"""
import contextlib, importlib.util, io, math, sys, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
if "oh" in sys.modules:
    oh = sys.modules["oh"]
else:
    _argv = sys.argv; sys.argv = ["x"]
    _spec = importlib.util.spec_from_file_location("oh", HERE / "one_higgs_search.py"); oh = importlib.util.module_from_spec(_spec)
    sys.modules["oh"] = oh
    with contextlib.redirect_stdout(io.StringIO()):
        _spec.loader.exec_module(oh)
    sys.argv = _argv
HS = oh.HS
N_GRID, N_REC, SCALES, PER_SCALE, MAX_ROUNDS = 16, 8, (0.01, 0.02, 0.04, 0.08), 3, 4


def grid_logs(Uh):
    return oh.grid_logs(Uh, False)


def search3(Uh, extra, T, SIG, L=None, seed=0):
    """Returns (the grid's minimum chi2, (the refined minimum chi2, its 6-vector x)) for the A1 model at targets T."""
    if L is None:
        L = grid_logs(Uh)
    chis = np.sum(((L - T) / SIG) ** 2, axis=1)
    order = np.argsort(chis); keep = []
    for idx in order:
        if all(abs(np.vdot(HS[j], HS[idx])) < math.cos(0.05) for j in keep):
            keep.append(int(idx))
        if len(keep) == N_GRID:
            break
    ex = [q for q in extra] + [np.conj(q) for q in extra]
    ce = oh.nine_batch(Uh, np.array(ex), T, SIG, False)[1]
    ex = [ex[i] for i in np.argsort(ce)[:N_REC]]
    best = (float(chis[order[0]]), np.concatenate([HS[order[0]].real, HS[order[0]].imag]))
    for h in [HS[j] for j in keep] + ex:
        o = oh.refine(Uh, np.concatenate([h.real, h.imag]), T, SIG, False)
        if o is not None and o[0] < best[0]:
            best = o
    rng = np.random.default_rng(seed)
    for _round in range(MAX_ROUNDS):
        before = best[0]
        for sc in SCALES:
            for _k in range(PER_SCALE):
                hb = oh.vec(best[1]); hb = hb / np.linalg.norm(hb)
                z = rng.normal(size=3) + 1j * rng.normal(size=3); z -= np.vdot(hb, z) * hb; z /= np.linalg.norm(z)
                hn = math.cos(sc) * hb + math.sin(sc) * z
                o = oh.refine(Uh, np.concatenate([hn.real, hn.imag]), T, SIG, False)
                if o is not None and o[0] < best[0]:
                    best = o
        if best[0] > before - 1e-6:
            break
    return float(chis[order[0]]), best
