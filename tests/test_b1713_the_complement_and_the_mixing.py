"""B1713 -- the complement and the mixing (P-261, P-129), sealed cd294dccf, NEGATIVE as sealed. Live: the comparison
re-run from the stored rows and the pinned data reproduces A-H1 and K1 holding, A-H2, A-H3, K2-K4 failing and the
controls holding; P-268's prediction read from the stored rows. Stored: the seal's hashes."""
import hashlib, importlib.util, io, contextlib, json, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1713_the_complement_and_the_mixing"


def test_the_cells_live():
    spec = importlib.util.spec_from_file_location("b1713_compare", A / "verification" / "compare.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    o = m.out
    a, b = o["A"], o["B"]
    assert a["H1_within_factor_3"] and not a["H2_specific_p_below_0.01"] and not a["H3_chi2_below_16.75"]
    assert b["K1_three_within_factor_3"] and not b["K2_specific_p_below_0.01"] and not b["K3_nine_within_factor_3"] and not b["K4_specific_p_below_0.01"]
    assert o["C1_holds"] and o["C2_holds"]
    assert abs(a["best_by_worst_factor"]["worst_factor"] - 2.326) < 0.002 and abs(b["best_three"]["worst_factor"] - 1.136) < 0.002
    assert abs(b["calibration_three"]["fraction_fit_as_well"] - 0.59525) < 1e-9 and abs(a["calibration"]["fraction_fit_as_well"] - 0.14775) < 1e-9


def test_the_p268_prediction():
    G = json.loads((A / "verification" / "the_complement_and_mixing.json").read_text(encoding="utf-8"))
    m1 = {}
    for r in G["rows"]:
        for k, v in r.items():
            if "|" in k and not k.startswith("ckm"):
                key = (r["line"], k.split("|")[0]); m1[key] = max(m1.get(key, 0.0), v[1])
    for (k, sec), v in m1.items():
        order = G["lines"][k][0]
        exact = order == "N=4" or (order == "N=12" and sec == "lep")
        assert (v < 1e-12) == exact, (G["lines"][k], sec, v)


def test_the_seal():
    for name in ("the_complement_and_mixing.py", "compare.py", "b1656_funcs.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("1cdf28e5")
