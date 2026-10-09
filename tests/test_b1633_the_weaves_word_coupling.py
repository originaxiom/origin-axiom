"""B1633 -- the sealed instrument unchanged; the averaged word coupling tends to a scalar commuting with G on each coset;
odd lengths carry no zero modes; the zero-mode fraction near 5/16."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1633_the_weaves_word_coupling"


def test_sealed_and_recorded():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at ")
    assert hashlib.sha256(open(ARC / "verification" / "weave_word_coupling.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "weave_word_coupling.json"))
    lim = d["W3_limit_uniform_on_each_coset"]
    assert lim["even"]["commutes_with_all_of_G"] and lim["odd"]["commutes_with_all_of_G"] and lim["odd"]["trace"] == 0.0
    rows = {r["n"]: r for r in d["W1_W2_W4"]}
    assert rows[38]["distance_from_scalar"] < 1e-5 < rows[2]["distance_from_scalar"]
    assert abs(rows[40]["fraction_with_zero_modes"] - 0.3125) < 2e-3
