"""B1664 -- the layers, OPEN: the sealed gate failed on the instrument's own cut-off. The sealed instrument unchanged; the
stored output (L0 False with a NaN phase error; the read-outs); the post-seal diagnosis (593 NaN threads, all starting
above the cut; 3.2e-10 elsewhere); live through the sealed instrument: LR's coherence and phase, and a thread starting
above the cut giving the NaN (the defect, reproduced); the bite -- LLRR's coherence differs from LR's."""
import hashlib, importlib.util, json, math, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1664_the_layers"
INSTR = A / "verification" / "the_layers.py"


def _load():
    spec = importlib.util.spec_from_file_location("b1664_lock", INSTR)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_sealed_stored_and_diagnosed():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at beaa42ff6")
    assert hashlib.sha256(open(INSTR, "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("20c39c08")
    d = json.load(open(A / "verification" / "the_layers.json"))
    assert d["L0"]["holds"] is False and d["L0"]["phase_err_max"] != d["L0"]["phase_err_max"]   # NaN
    assert d["L0"]["sizes_3_6"] == [1, 2, 2, 3] and d["n_threads"] == 30674 and d["all_hold"] is False
    assert abs(d["L1"]["top_quarter_mean"] - 0.3144) < 1e-3 and d["L2"]["per_thread_slope"] < 0
    g = json.load(open(A / "verification" / "after_the_seal" / "gate_diagnosis_output.json"))
    assert g["n_nan"] == 593 and g["all_nan_start_above_cut"] and not g["any_good_start_above_cut"] and g["max_phase_err_others"] < 1e-9
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "OPEN"


def test_live_threads_and_the_defect():
    m = _load()
    r = m.thread(("LR", 3)); assert abs(r["coh"] - 0.6368) < 1e-3 and r["ph_err"] < 1e-9 and r["chi1"]
    q = m.thread(("LLRR", 6)); assert abs(q["coh"] - r["coh"]) > 0.1                       # bite
    deep = m.thread(("L" + "R"*598, 600))
    assert not math.isfinite(deep["ph_err"])                                                  # the defect, reproduced
