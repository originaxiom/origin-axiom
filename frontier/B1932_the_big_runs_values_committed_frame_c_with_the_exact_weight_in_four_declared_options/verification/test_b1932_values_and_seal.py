"""B1932's lock: the sealed values are the committed ones; the values file is the assembly of the committed runs; the
pre-seal findings hold in their kept outputs (the truncation moves four values by about 1 %; Theorem 90's form matches the
exact norm to about 1e-5); the comparison script passes matching synthetic data, fails mismatched data and refuses a
wrong values hash. It reads no measured data and writes nothing in the arc."""
import hashlib, json, pathlib, importlib.util, re, tempfile
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent


def _load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py")); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_seal_holds_the_committed_values():
    s = (HERE / "big_run_look.py").read_text()
    sealed = re.search(r'VALUES_SHA = "([0-9a-f]{64})"', s).group(1)
    assert sealed == hashlib.sha256((HERE / "BIG_RUN_VALUES.json").read_bytes()).hexdigest()


def test_the_values_are_the_assembly_of_the_kept_runs():
    v = json.loads((HERE / "BIG_RUN_VALUES.json").read_text())
    e = json.loads((HERE / "ergodic_both_worlds.json").read_text()); a = json.loads((HERE / "area_measure.json").read_text())
    assert np.allclose(v["options"]["W-|a (move count)"]["values"], e["R_exact_weight"][:7], rtol=0, atol=0)
    assert np.allclose(v["options"]["W+|a (move count)"]["values"], e["R_exact_weight"][7:], rtol=0, atol=0)
    assert len(v["options"]) == 4 and all(len(o["values"]) == 7 for o in v["options"].values())
    for k, f in v["inputs_from"].items():
        assert f == hashlib.sha256((HERE / k).read_bytes()).hexdigest(), k


def test_the_pre_seal_findings_hold_in_the_kept_outputs():
    tr = json.loads((HERE / "truncation.json").read_text()); t9 = json.loads((HERE / "t90.json").read_text())
    assert len(tr) == 8 and max(r["dln_max"] for r in tr) > 1e-2            # the truncation is material
    assert len(t9) == 3 and max(r["dln_max"] for r in t9) < 1e-4 and max(r["norm_gap_median"] for r in t9) < 1e-4
    assert min(r["dln_max"] for r in tr) > 100 * max(r["dln_max"] for r in t9)
    e = json.loads((HERE / "ergodic_t90.json").read_text())
    assert e["dln"][3] < -5e-3 and max(e["dln_se"]) < 1e-4                   # down m1/m3 moves, and the pairing is tight


def test_the_comparison_passes_matching_fails_mismatched_and_refuses_a_wrong_hash():
    L = _load("big_run_look"); tmp = pathlib.Path(tempfile.mkdtemp())
    m = {"u": 1.0, "c": 300.0, "t": 9e4, "d": 2.0, "s": 40.0, "b": 1500.0, "e": .5, "mu": 100., "tau": 1700.}
    (tmp / "m.json").write_text(json.dumps({"masses_GeV": {"value": m, "sigma": {k: .05 * x for k, x in m.items()}}}))
    (tmp / "c.json").write_text(json.dumps({"ckm_abs": {"value": [[.97, .22, .004], [.22, .97, .04], [.009, .04, .99]],
                                                         "sigma": [[.001, .001, .0002], [.001, .001, .001], [.0005, .001, .001]]}}))
    tgt = [300 / 9e4, 1 / 9e4, 40 / 1500, 2 / 1500, .22, .04, .004]
    def run(vals):
        V = {"options": {"A": {"values": vals}, "B": {"values": [x * 3 for x in vals]}, "C": {"values": [x / 3 for x in vals]}, "D": {"values": [x * 10 for x in vals]}}}
        p = tmp / "v.json"; p.write_text(json.dumps(V))
        L.VALUES, L.VALUES_SHA = p, hashlib.sha256(p.read_bytes()).hexdigest()
        L.DATA, L.SHA = tmp / "m.json", hashlib.sha256((tmp / "m.json").read_bytes()).hexdigest()
        L.CKMDATA, L.CKMSHA = tmp / "c.json", hashlib.sha256((tmp / "c.json").read_bytes()).hexdigest()
        L.HERE = tmp; L.main(); return json.loads((tmp / "big_run_output.json").read_text())
    assert run(tgt)["outcome"] == "PASS"
    assert run([x * 10 for x in tgt])["outcome"] == "FAIL"
    L.VALUES_SHA = "0" * 64
    try:
        L.main(); assert False, "a wrong values hash was not refused"
    except AssertionError as ex:
        assert "not the committed ones" in str(ex)
