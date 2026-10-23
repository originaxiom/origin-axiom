"""B1738 -- W139 on main (P-338), PROVED.  Live: under E6's cubic the extended down-quark and charged-lepton matrices have
the same singular values at random symmetric couplings and neutral vevs, and doubling det L splits them (the control)."""
import importlib.util, pathlib
V = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1738_w139_on_main" / "verification"


def test_down_equals_lepton_live(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("b1738", V / "e6_down_equals_lepton.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    monkeypatch.setattr(m, "HERE", tmp_path)
    m.main()
    import json
    out = json.loads((tmp_path / "e6_down_equals_lepton.json").read_text(encoding="utf-8"))
    assert out["N_invariance_rel"] < 1e-12 and out["neutral_leptonic_components"] == 5
    assert out["down_type_pairs"] == [2, 2] and out["lepton_pairs"] == [2, 2]
    assert out["max_rel_singular_value_difference_E6"] < 1e-12 and out["control_detL_doubled_max_rel_difference"] > 0.5
