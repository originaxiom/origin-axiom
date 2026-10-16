"""B1665 -- the layers re-sealed, OPEN: the gate failed at omega. The sealed instrument unchanged; the stored output (L0
False, the read-outs equal to B1664's); the post-seal diagnosis (22 one-point failures; the least-squares phase right
on all 30 674 threads to < 1e-6)."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1665_the_layers_resealed"


def test_sealed_stored_and_diagnosed():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 043c90b6a")
    assert hashlib.sha256(open(A / "verification" / "the_layers_resealed.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(A / "verification" / "the_layers_resealed.json"))
    b = json.load(open(ROOT / "frontier" / "B1664_the_layers" / "verification" / "the_layers.json"))
    assert d["L0"]["holds"] is False and d["L0"]["phase_err_max"] > 1e3
    assert abs(d["L1"]["top_quarter_mean"] - b["L1"]["top_quarter_mean"]) < 1e-7
    assert abs(d["L2"]["per_thread_slope"] - b["L2"]["per_thread_slope"]) < 1e-6
    g = json.load(open(A / "verification" / "after_the_seal" / "gate_diagnosis_output.json"))
    assert g["n"] == 30674 and g["n_sealed_fail"] == 22 and g["robust_fail"] == 0 and g["robust_max_err"] < 1e-6
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "OPEN"
