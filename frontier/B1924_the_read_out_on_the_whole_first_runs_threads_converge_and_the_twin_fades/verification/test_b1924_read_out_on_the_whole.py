"""The lock of B1924. Each test recomputes, and each has a planted case that must fail.

1. The channel norm's closed form (B1919) equals the frame's quadrature at random twists; a closed form with the shift
   u = c - (1/2, 1/2) dropped is caught.
2. A stored thread average is recomputed from its word (n = 10, the mark): the json's numbers are the code's; a stored
   number changed by 1e-6 is caught.
3. The mark is kept by the allowed words and refused otherwise (L alone does not keep it; LR does).
4. The twin fades, recomputed from the per-word rows by the paired jackknife: clearly distinct at n = 10, not resolved
   at n = 22; a planted difference of three sampling errors at n = 22 is caught.
5. The golden thread's ratio average converges in the trapezoid rule (32 against 64 nodes)."""
import json, math, pathlib, random, sys
import numpy as np
import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import thread_average as T          # noqa: E402
import fast_norm as FN               # noqa: E402
import whole_average as WA           # noqa: E402  (patches the frame's channel norm with the closed form)
import twin_compare as CMP           # noqa: E402

F = FN.F


def test_closed_form_equals_quadrature():
    rng = random.Random(1924)
    worst, worst_unshifted = 0.0, 0.0
    for _ in range(2):
        t = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 1.4))
        w = complex(rng.uniform(0, 1), 0) * t + rng.uniform(0, 1)
        x, yy = F.sector_twists(w, t, F.SIXY["Q"], F.SIXY["u"])
        R = F.residues(x, yy, t)
        ref = F.cA(x, yy, t, R)
        fast = FN.cA_fast(x, yy, t, R)
        ch = FN.kernel_chars(x, yy, "B1906")
        for s in F.UNITS:
            if ref[s] is not None and fast[s] is not None:
                worst = max(worst, abs(ref[s] - fast[s]))
                bad = FN.F_u(ch[s][0], ch[s][1], t) + math.pi * math.log(t.imag) + FN.CC      # the shift dropped
                worst_unshifted = max(worst_unshifted, abs(ref[s] - bad))
    assert worst < 1e-8
    assert worst_unshifted > 1e-3


def test_stored_thread_average_recomputed():
    D = json.loads((HERE / "whole_average_2.json").read_text())
    row = D["10 mark"]["rows"][0]
    T.MARK = (0.4, 0.8)
    A, ell, nodes = WA.thread_mean(row["word"])
    dev = lambda stored: max(float(np.max(np.abs(np.array(stored[k]) - A[k]))) for k in A)
    assert abs(ell - row["length"]) < 1e-12
    assert dev(row["A"]) < 1e-9
    planted = {k: list(v) for k, v in row["A"].items()}
    k0 = next(iter(planted)); planted[k0][0] += 1e-6
    assert dev(planted) > 1e-7


def test_mark_kept_and_refused():
    assert T.keeps_mark("LR") and T.keeps_mark("LLLLLLRLR")
    assert not T.keeps_mark("L") and not T.keeps_mark("R")


def test_twin_fades_paired():
    zp10, _ = CMP.paired(10)
    zp22, _ = CMP.paired(22)
    assert np.median(zp10) > 2.0 and np.mean(np.array(zp10) > 2) > 0.4
    assert np.median(zp22) < 1.0 and np.mean(np.array(zp22) > 2) < 0.05
    # planted: the twin's rows moved by three of the mark's sampling errors must be seen as different
    saved = CMP.D["22 twin"]
    try:
        rows = json.loads(json.dumps(saved["rows"]))
        se = CMP.D["22 mark"]["se"]
        for r in rows:
            for k in r["A"]:
                r["A"][k] = list(np.array(r["A"][k]) + 3 * np.array(se[k]))
        CMP.D["22 twin"] = dict(saved, rows=rows)
        zplant, _ = CMP.paired(22)
        assert np.median(zplant) > 2.0
    finally:
        CMP.D["22 twin"] = saved


def test_golden_ratio_average_converges():
    beta, betap, ell, g = T.geodesic("LR")
    zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
    s0 = -ell / 2
    if abs(g(zt(s0)) - zt(s0 + ell)) > 1e-7 * (1 + abs(zt(s0))):
        ell = -ell
    T.MARK = (0.4, 0.8)
    S = [T.outputs(zt(s0 + ell * j / 64)) for j in range(64)]
    a64 = {k: np.mean([np.array(o[k]) for o in S], 0) for k in S[0]}
    a32 = {k: np.mean([np.array(o[k]) for o in S[::2]], 0) for k in S[0]}
    assert max(float(np.max(np.abs(a64[k] - a32[k]))) for k in a64) < 1e-3
