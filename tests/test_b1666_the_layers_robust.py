"""B1666 -- the layers with a robust phase. The sealed instrument unchanged; the stored cells; live through the sealed
instrument: the period phase i^(#L - #R) on LR, LLR, LRR, LLLR and a deep cusp thread; the coherence of LR and LLRR; the
bite -- the phase of LLR is not that of LRR, and a coherence differs between threads."""
import hashlib, importlib.util, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1666_the_layers_robust"
INSTR = A / "verification" / "the_layers_robust.py"


def _load():
    spec = importlib.util.spec_from_file_location("b1666_lock", INSTR)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at aac14a72c")
    assert hashlib.sha256(open(INSTR, "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("df6f13d1")
    d = json.load(open(A / "verification" / "the_layers_robust.json"))
    assert d["all_hold"] is True and d["n_threads"] == 30674
    assert d["L0"]["phase_err_max"] < 1e-5 and not d["L0"]["failures"] and d["L0"]["sizes_3_6"] == [1, 2, 2, 3]
    assert abs(d["L1"]["top_quarter_mean"] - 0.31500491) < 0.03 and d["L2"]["per_thread_slope"] < -3*d["L2"]["slope_se"]
    assert abs(d["readouts"]["phase1_fraction"] - 0.25) < 0.01
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def test_live_phases_coherences_and_bite():
    m = _load()
    out = {w: m.thread((w, t)) for w, t in (("LR", 3), ("LLR", 4), ("LRR", 4), ("LLLR", 5), ("L" + "R"*598, 600))}
    for w, r in out.items():
        assert r["ph_err"] < 1e-6, w
    assert abs(complex(*out["LLR"]["phase"]) - 1j) < 1e-6 and abs(complex(*out["LRR"]["phase"]) + 1j) < 1e-6   # bite: mirror pair differ
    assert abs(out["LR"]["coh"] - 0.6368) < 1e-3 and abs(m.thread(("LLRR", 6))["coh"] - 0.2435) < 1e-3
