"""B1722 -- which thread? (P-285), sealed a9a5d46f9, NEGATIVE as sealed. Stored: the cells and the measures' weights.
Live: the uniform measure and the misfit statistic re-derived from B1720's stored rows (no SnapPy needed), reproducing
E_uniform(data); after the read, the walk's limit digits (a short run of the labelled check). Seal: the hashes."""
import hashlib, json, math, pathlib, importlib.util
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1722_which_thread"


def test_stored():
    d = json.loads((A / "verification" / "which_thread.json").read_text(encoding="utf-8"))
    assert not d["W1_uniform_specific_p_below_0.01"] and not d["W2_action_specific_p_below_0.01"]
    assert abs(d["calibration_uniform"]["fraction_as_good"] - 0.2535) < 1e-9 and abs(d["calibration_action"]["fraction_as_good"] - 0.21) < 1e-9
    assert d["data"]["best_class"] == "LLLLLRLRR" and d["data"]["best_class_mu_uniform"] < 0.01


def test_live_uniform_statistic():
    spec = importlib.util.spec_from_file_location("b1722", A / "verification" / "which_thread.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    G = json.loads(m.B1720.read_text(encoding="utf-8")); words = [c["word"] for c in G["classes"]]
    R = m.rows_by_class(G)
    d = json.loads(m.DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]
    tgt = np.log(np.array([d["c"] / d["t"], d["u"] / d["t"], d["s"] / d["b"], d["d"] / d["b"], d["mu"] / d["tau"], d["e"] / d["tau"]]))
    muU = np.array([len(w) * 2.0 ** -len(w) for w in words]); muU /= muU.sum()
    EU = float(np.sum(muU * m.f_of(R, tgt)))
    stored = json.loads((A / "verification" / "which_thread.json").read_text(encoding="utf-8"))["data"]["E_uniform"]
    assert abs(EU - stored) < 1e-9


def test_the_seal():
    h = hashlib.sha256((A / "verification" / "which_thread.py").read_bytes()).hexdigest()
    assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("120707ad")


def test_after_the_read_walk_is_uniform():
    d = json.loads((A / "verification" / "after_the_read" / "walk_digits.json").read_text(encoding="utf-8"))
    for r in d["runs"]:
        assert max(abs(x - y) for x, y in zip(r["marginals_1_to_4_and_5plus"], d["geometric_1_to_4_and_5plus"])) < 0.005
        assert r["max_pair_deviation_from_independent_geometric"] < 0.005
    spec = importlib.util.spec_from_file_location("b1722w", A / "verification" / "after_the_read" / "walk_digits.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    r = m.run(0.5, 200, 600, 1)
    assert abs(r["marginals_1_to_4_and_5plus"][0] - 0.5) < 0.02 and abs(r["marginals_1_to_4_and_5plus"][1] - 0.25) < 0.02
