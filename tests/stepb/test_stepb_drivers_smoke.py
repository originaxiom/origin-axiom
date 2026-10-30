"""The drivers end to end on a synthetic census written in the refined census's exact format on the full 991-point grid
(the fifth review's N3: p2_driver.main, calibration_driver.main and run_stepb.main had never run).  The guard is replaced
by a stub that returns the manifest (the guard has its own tests), the targets by a synthetic world, the fresh evaluation
by a stub; everything else is the real code path: load_compact, Choices, CellIndex, the forked pools, the checkpoints, the
outputs, the legs and the reading."""
import pytest
pytestmark = pytest.mark.slow
import gzip, hashlib, json, math, pathlib, sys
import numpy as np
import pytest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import stepb_core as C
from census_io import line_key
from synth import PTS

LABELS = ["".join("S~" if r else "S" for r in (u, d, l)) for u in (0, 1) for d in (0, 1) for l in (0, 1)]


def write_census(tmp, lines=(("2/5", "1/10"), ("2/5", "9/10")), seed=0):
    rng = np.random.default_rng(seed); per = {}
    A = rng.normal(0, 1, (13, 2, 8, 10, 3))
    base = np.array([-4.2, -9.5, -4.4, -9.0, -5.2, -10.0, -1.5, -3.2, -5.6, -10.0])     # the six well inside B1741's box
    for li, (a, b) in enumerate(lines):
        name = "N10_%s_%s.jsonl.gz" % (a.replace("/", "-"), b.replace("/", "-"))
        with gzip.open(tmp / name, "wt", encoding="utf-8") as fh:
            for (x, y) in PTS:
                rows = []
                for d in range(13):
                    dd = 1 if d == 6 else d                                     # F_-2 equals a0 (B1824)
                    for r in range(2):
                        for k, lab in enumerate(LABELS):
                            c = A[dd, r, k]
                            f = base + 0.6 * np.sin(2 * np.pi * (c[:, 0] * x + 0.4 * c[:, 1] * y + 0.3 * li)) - 0.25 * np.tanh(c[:, 2]) * (y - 2)
                            f = np.minimum(f, -0.05); v = np.exp(f)
                            J = v[9] * np.sin(5 * x + c[9, 0] + y)
                            rows.append([d, r, lab, [float(v[1]), float(v[0])], [float(v[3]), float(v[2])], [float(v[5]), float(v[4])],
                                         [float(v[6]), float(v[7]), float(v[8])], float(J), True])
                fh.write(json.dumps({"line": [a, b], "order": 10, "tau": [x, y], "rows": rows}) + "\n")
        per[name] = hashlib.sha256((tmp / name).read_bytes()).hexdigest()
    h = hashlib.sha256("".join("%s  %s\n" % (v, n) for n, v in sorted(per.items())).encode()).hexdigest()
    man = tmp / "MANIFEST.json"; man.write_text(json.dumps({"per_file": per, "sha256_of_the_manifest": h}))
    return man, h, per


@pytest.fixture(scope="module")
def census(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("census")
    man, h, per = write_census(tmp)
    sig = tmp / "SIGMA.json"; sig.write_text(json.dumps({"sigma_natural_log": [0.1038, 0.1979, 0.1327, 0.1231, 0.1, 0.1, 0.1, 0.1018, 0.1029, 0.1077]}))
    return tmp, man, h, per, sig


def stub_guard(monkeypatch, per):
    import p2_driver as P2
    monkeypatch.setattr(P2, "require_pushed_manifest", lambda m, e: {"manifest_commit": "stub", "files": len(per), "per_file": per})


def test_p2_driver_end_to_end(census, monkeypatch):
    tmp, man, h, per, sig = census
    import p2_driver as P2
    stub_guard(monkeypatch, per)
    out = tmp / "p2.json"
    P2.main(str(tmp), str(man), h, str(sig), str(out), N="3000", seed="1", batch="1500", workers="2")
    r = json.loads(out.read_text())
    assert r["complete"] and r["N_drawn"] == 3000 and r["N"] + r["dropped_nonfinite"] == 3000
    assert r["choices"] == 2 * 12 * 2 * 8 and r["rows_defined"] == r["rows"]
    lo, hi = r["p2_cp95"]; assert 0 <= lo <= r["p2"] <= hi <= 1
    assert json.loads(out.with_suffix(".checkpoint.json").read_text())["N_done"] == 3000


def test_calibration_driver_end_to_end(census, monkeypatch):
    tmp, man, h, per, sig = census
    import p2_driver as P2, calibration_driver as CD
    stub_guard(monkeypatch, per)
    p2 = tmp / "p2_for_cal.json"; p2.write_text(json.dumps({"p2_cp95": [1e-3, 1e-2]}))
    out = tmp / "cal.json"
    CD.main(str(tmp), str(man), h, str(sig), str(p2), str(out), M="2", M0="2", P="3", seed="2", workers="2")
    r = json.loads(out.read_text())
    assert r["complete"] and r["vacuity"]["supported"] <= 2 and "all_ok" in r["markov"]
    assert r["planted_chi2_0"]["n"] >= 1 and r["leg_size"]["n"] >= 1
    assert r["planted_chi2_0"]["S"] >= 1                                 # a world planted at chi2 = 0 is in the support


def test_run_end_to_end(census, monkeypatch):
    tmp, man, h, per, sig = census
    import p2_driver as P2, run_stepb as RS
    stub_guard(monkeypatch, per)
    p2 = tmp / "p2_for_run.json"; p2.write_text(json.dumps({"p2_cp95": [0.0, 1e-5]}))
    ci, s_, meta = P2.build(str(tmp), str(man), h, str(sig))
    import compression as K
    rng = np.random.default_rng(7)
    while True:                                                           # a world the frame makes, at c = 3, inside the box
        rows, xs, ys = ci.sample_prior(rng, 1)
        t = ci.interp_many(rows, xs, ys)[0] + C.c_shift(3.0)
        if K.in_box(t[:6]): break
    monkeypatch.setattr(RS, "targets", lambda J: t)
    monkeypatch.setattr(RS, "fresh_chi2", lambda ci, g, t10, refined: {"defined": True, "stub": True})
    out = tmp / "run.json"
    RS.main(str(tmp), str(man), h, str(sig), str(p2), "53", "3.12e-5", str(out))
    r = json.loads(out.read_text())
    assert r["status"] == "DONE" and r["S"]["in_support"] is True and r["S"]["least_chi2_ten"] < 1e-3   # global_min's tolerance
    assert r["legs"]["K_grade"] == "JUDGED" and r["K"]["converged"] is True and 0 <= r["p"]["p_K"] <= 1 and 0 <= r["p"]["p_CKM"] <= 1
    assert r["CKM"]["clause"]["clause"] in (True, False)
    assert set(r["legs"]) >= {"S", "X2", "K", "CKM"} and isinstance(r["reading"], str) and r["T"]["area"]["grade"] in ("CONSISTENT", "NEGATIVE")
