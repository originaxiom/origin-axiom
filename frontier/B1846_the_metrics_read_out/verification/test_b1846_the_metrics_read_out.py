"""B1846 -- the metric's read-out: harmonic time, its energy (uniform, T1), its volume (atomless, T2; one hump on the
excursion member centred on the run's tube; flat on the golden m004). Data-free. Reads the committed outputs; the exact
facts (the cyclic palindromes, the tube word's chi) are checked directly."""
import json, math, pathlib
import numpy as np
import pytest
HERE = pathlib.Path(__file__).resolve().parent


def _j(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def test_the_words_are_cyclic_palindromes_so_sigma_exists():
    for w in ("LLLLLLRLR", "LLLLLLLLLLRLR", "LR"):
        r = w[::-1]
        assert any(w[k:] + w[:k] == r for k in range(len(w))), w


def test_the_instrument_reproduces_b1295_and_m004_is_flat():
    d = _j("step3_m004_R6.json")
    assert abs(d["control_c02"] - 4.260982635) < 1e-8               # B1295's known coefficient, the known answer
    assert abs(d["volume"] - d["snappy_volume"]) < 0.01
    assert d["info1"]["resid_rms"] < 1e-7 and d["info2"]["resid_rms"] < 1e-6
    assert d["chi2_E"] < 39 + 4 * math.sqrt(2 * 39)                 # T1: the energy is flat
    rho = np.array(d["rho"]); se = np.median(d["rho_se_rel"])
    assert rho.max() < 1 + 4 * se and rho.min() > 1 - 4 * se        # the golden control: no hump


def test_the_excursion_member_has_one_hump_on_its_tube():
    d = _j("step3_b++LLLLLLRLR_R12.json")
    assert abs(d["volume"] - d["snappy_volume"]) < 3 * 0.025
    assert d["info1"]["resid_rms"] < 1e-9 and d["gen_dev"]["face pairings"] < 1e-9
    assert d["chi2_E"] < 39 + 4 * math.sqrt(2 * 39)                 # T1 on the excursion member
    d10 = _j("step3_b++LLLLLLRLR_R10.json")                         # convergence in the mode cut: Rcut 10 vs 12
    assert np.abs(np.array(d10["rho"]) - np.array(d["rho"])).max() < 0.15
    rho = np.array(d["rho"]); nb = len(rho)
    assert rho.max() > 1.6 and rho.min() < 0.85
    peak = (np.argmax(rho) + 0.5) / nb
    assert min(peak, 1 - peak) < 0.05                               # the hump sits at s = 0
    se = np.array(d["rho_se_rel"]) * rho                            # sigma: rho(s) = rho(-s), a chi2 on 20 dof
    chi2_sym = float(np.sum((rho[:20] - rho[::-1][:20]) ** 2 / (se[:20] ** 2 + se[::-1][:20] ** 2)))
    assert chi2_sym < 20 + 4 * math.sqrt(2 * 20)
    assert np.abs(np.array(d["rho"]) - np.array(d["rho2"])).max() < 0.02   # two collocation heights
    t = _j("step5_b++LLLLLLRLR.json")
    assert abs(((t["tube_theta"] + 0.5) % 1) - 0.5) < 1e-3 and t["tube_spread"] < 1e-3   # theta == 0 on the core
    vol = sum(r["vol_bw"] for r in t["rows"]); assert abs(vol - 5.586362) < 1e-3
    for r in t["rows"]:
        assert abs(r["vol_mc"] - r["vol_bw"]) < 4 * r["vol_err"] + 0.01
    assert np.abs(np.array(t["rho"]) - rho).max() < 0.2             # the second method: tetrahedra vs the Ford domain
    mid = min(t["rows"], key=lambda r: r["vol_bw"])                 # the run's middle tetrahedron
    assert abs(((mid["theta_circmean"] + 0.5) % 1) - 0.5) < 0.01 and mid["concentration"] > 0.99


def test_the_tube_word_from_snappy():
    snappy = pytest.importorskip("snappy")
    import cmath
    M = snappy.Manifold("b++LLLLLLRLR"); G = M.fundamental_group()
    w = G.original_generators()[6]
    m = G.SL2C(w); tr = complex(m[0, 0]) + complex(m[1, 1])
    L = 2 * cmath.acosh(tr / 2)
    assert abs(abs(L.real) - 0.18486980451) < 1e-8
    assert sum((1 if ch.islower() else -1) for ch in w if ch.lower() == "c") == 0       # chi(core) = 0: a fibre curve


def test_the_hump_sharpens_with_the_run_and_stays_on_the_tube():
    d6 = _j("step3_b++LLLLLLRLR_R12.json"); d10 = _j("step3_b++LLLLLLLLLLRLR_R14.json")
    assert abs(d10["volume"] - d10["snappy_volume"]) < 3 * 0.035
    assert d10["chi2_E"] < 39 + 4 * math.sqrt(2 * 39) and d10["gen_dev"]["face pairings"] < 1e-8
    r6, r10 = np.array(d6["rho"]), np.array(d10["rho"])
    c6 = (r6[0] + r6[-1]) / len(r6); c10 = (r10[0] + r10[-1]) / len(r10)
    assert c10 > c6 > 0.05 + 0.02                                   # more of the volume at the tube as the run grows
    t = _j("step5_b++LLLLLLLLLLRLR.json")
    assert abs(((t["tube_theta"] + 0.5) % 1) - 0.5) < 1e-3 and t["tube_spread"] < 1e-3
    assert abs(sum(r["vol_bw"] for r in t["rows"]) - 5.750182) < 1e-3
    assert np.abs(np.array(t["rho"]) - r10).max() < 0.35             # the second method on the run of 10
