"""B1937's lock: version 2 of the big run's comparison, on synthetic data only (it reads no measured data and writes
nothing in the arc). Planted cases: values equal to the targets pass, and only that option is listed; values a factor 10
off fail; values a factor 2 off are a pattern match, not a pass; lepton rows that differ from the down rows fail the
reported six but leave the governing seven untouched; a wrong values hash, wrong positions and a missing option are
refused. Also: the script's seal is the one FINDINGS states, and it pins B1932's committed values."""
import hashlib, json, pathlib, importlib.util, re, tempfile
HERE = pathlib.Path(__file__).resolve().parent


def _load():
    spec = importlib.util.spec_from_file_location("brl2", HERE / "big_run_look_v2.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m


L = _load()
M = {"u": 1.0, "c": 300.0, "t": 9e4, "d": 2.0, "s": 40.0, "b": 1500.0, "e": 2.0 * 1700 / 1500, "mu": 40.0 * 1700 / 1500, "tau": 1700.}
CK = {"ckm_abs": {"value": [[.97, .22, .004], [.22, .97, .04], [.009, .04, .99]],
                  "sigma": [[.001, .001, .0002], [.001, .001, .001], [.0005, .001, .001]]}}
TGT = [300 / 9e4, 1 / 9e4, 40 / 1500, 2 / 1500, .22, .04, .004]      # the seven at the synthetic data


def _run(vals, masses=M, positions=None, drop=None):
    tmp = pathlib.Path(tempfile.mkdtemp())
    (tmp / "m.json").write_text(json.dumps({"masses_GeV": {"value": masses, "sigma": {k: .05 * x for k, x in masses.items()}}}))
    (tmp / "c.json").write_text(json.dumps(CK))
    opts = {L.OPTIONS[0]: {"values": vals}, L.OPTIONS[1]: {"values": [x * 3 for x in vals]},
            L.OPTIONS[2]: {"values": [x / 3 for x in vals]}, L.OPTIONS[3]: {"values": [x * 10 for x in vals]}}
    if drop:
        opts.pop(drop)
    (tmp / "v.json").write_text(json.dumps({"positions": positions or L.POSITIONS, "options": opts}))
    return L.look(tmp / "v.json", tmp / "m.json", tmp / "c.json", tmp / "o.json")


def test_matching_values_pass_and_only_that_option_is_listed():
    o = _run(TGT)
    assert o["outcome_governing_seven"] == "PASS" and o["passing_options_none_preferred"] == [L.OPTIONS[0]]
    assert o["reported_P341_six_and_nine"]["any_option_chi2_nine_below_bar"]     # the synthetic leptons equal the downs


def test_values_ten_times_off_fail():
    assert _run([x * 10 for x in TGT])["outcome_governing_seven"] == "FAIL"


def test_values_twice_off_are_a_pattern_match_not_a_pass():
    o = _run([x * 2 for x in TGT])
    assert o["outcome_governing_seven"] == "PATTERN MATCH" and o["passing_options_none_preferred"] == []


def test_leptons_unlike_the_downs_fail_the_reported_six_only():
    m = dict(M); m["mu"] *= 5; m["e"] /= 5
    o = _run(TGT, masses=m)
    assert o["outcome_governing_seven"] == "PASS"
    assert not o["reported_P341_six_and_nine"]["any_option_chi2_six_below_bar"]
    assert not o["reported_P341_six_and_nine"]["any_option_chi2_nine_below_bar"]


def test_the_lepton_rows_are_the_down_rows():
    assert L.nine_from_option([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 3, 4, 5, 6, 7]


def test_wrong_positions_and_a_missing_option_are_refused():
    for kw, msg in (({"positions": list(reversed(L.POSITIONS))}, "positions"), ({"drop": L.OPTIONS[3]}, "four declared")):
        try:
            _run(TGT, **kw); assert False, "not refused"
        except AssertionError as ex:
            assert msg in str(ex)


def test_a_wrong_values_hash_is_refused():
    keep = L.VALUES_SHA; L.VALUES_SHA = "0" * 64
    try:
        L.main(); assert False, "a wrong values hash was not refused"
    except AssertionError as ex:
        assert "not the committed ones" in str(ex)
    finally:
        L.VALUES_SHA = keep


def test_the_seal_is_the_one_findings_states_and_it_pins_b1932s_values():
    f = (HERE.parent / "FINDINGS.md").read_text()
    stated = re.search(r"big_run_look_v2\.py`?, sha256 `([0-9a-f]{64})`", f).group(1)
    assert stated == hashlib.sha256((HERE / "big_run_look_v2.py").read_bytes()).hexdigest()
    assert L.VALUES_SHA == hashlib.sha256(L.VALUES.read_bytes()).hexdigest()


def test_the_second_computation_kept_agrees_and_discriminates():
    t = (HERE / "second_computations_run.txt").read_text()
    assert "worst |d ln| / tolerance: 0.34 -> AGREE" in t
    rms = {m.group(1): float(m.group(2)) for m in re.finditer(r"W- seat (\S+)\s+rms z\s+([\d.]+)", t)}
    assert rms["exact_T90"] < rms["old_small_cut"]
