"""B1660 -- the one-Higgs census under the canonical end condition (a scoreboard). The sealed instrument unchanged; the
stored cells (C0, C1 per reading, C2's 54 cells all excluded and reliable); live, through the sealed instrument on three
lines only: the stored best points reproduce their chi2_min (same and bar on line 2, tilde on line 5); the bite -- the
bar reading's best point read as the same S, or with L moved by 10%, is no longer its minimum."""
import hashlib, importlib.util, json, math, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1660_the_one_higgs_census"
INSTR = A / "verification" / "the_one_higgs_census.py"


def _load():
    spec = importlib.util.spec_from_file_location("b1660_lock", INSTR)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at f798b2368")
    assert hashlib.sha256(open(INSTR, "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("f0f9518c")
    d = json.load(open(A / "verification" / "the_one_higgs_census.json"))
    assert d["NST"] == 160 and d["threshold"] == 11.07 and d["floor"] == 0.05
    assert d["C0"]["holds"] is True and d["C0"]["fast_vs_B1656_and_joint_law_max"] < 1e-12
    assert d["C1"]["holds"] is True and all(d["C1"]["holds_by_reading"][r] for r in ("same", "tilde", "bar"))
    for r in ("same", "tilde", "bar"):
        assert len(d["C1"]["plants"][r]) == 5 and all(p["recovered_chi2"] < 0.1 for p in d["C1"]["plants"][r])
        cells = d["C2"]["census"][r]
        assert len(cells) == 18 and all(c["excluded"] and c["reliable"] and c["n_failed"] == 0 for c in cells)
        assert min(c["within_5pct"] for c in cells) > 2 and d["C2"]["unreliable_cells"][r] == []
    assert d["C2"]["all_excluded"] is True
    lo = {r: min(c["chi2_min"] for c in d["C2"]["census"][r]) for r in ("same", "tilde", "bar")}
    assert abs(lo["same"] - 85.352) < 1e-3 and abs(lo["tilde"] - 542.806) < 1e-3 and abs(lo["bar"] - 34.400) < 1e-3
    run = open(A / "verification" / "the_one_higgs_census_run.txt").read()
    assert "'all_excluded': True" in run and "resum" not in run.lower()
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "NEGATIVE"


def test_live_best_points_and_bite():
    m = _load(); d = json.load(open(A / "verification" / "the_one_higgs_census.json"))
    picks = [("same", 2), ("bar", 2), ("tilde", 5)]
    full = m.LINES18; m.LINES18 = sorted({full[i] for _, i in picks}); m.build(); m.LINES18 = full
    chi = lambda p, var, i: float(np.sum(m.resid(np.asarray(p, dtype=float), var, full[i], m.DMU)**2))
    for var, i in picks:
        e = d["C2"]["census"][var][i]
        assert abs(chi(e["x"], var, i) - e["chi2_min"]) < 1e-6*e["chi2_min"], (var, i)
    xb = np.array(d["C2"]["census"]["bar"][2]["x"]); c0 = d["C2"]["census"]["bar"][2]["chi2_min"]
    assert chi(xb, "same", 2) > c0 + 1.0                                                  # bite: the reading matters
    xl = xb.copy(); xl[8] += math.log(1.1); assert chi(xl, "bar", 2) > c0 + 1e-3        # bite: a minimum in L
    xs = d["C2"]["census"]["bar"][2]["ratios"]                                            # the read-out pattern
    assert xs["lep"][1] < 1e-12 and 0.02 < xs["down"][0] < 0.04 and 0.04 < xs["lep"][0] < 0.06
