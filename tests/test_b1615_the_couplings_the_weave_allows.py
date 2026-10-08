"""B1615 -- THE COUPLINGS THE WEAVE ALLOWS: the sealed instrument unchanged; the counts, the spectra and the sum rule as recorded."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1615_the_couplings_the_weave_allows"


def test_sealed_and_recorded():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at c5d30c59a: ")
    assert hashlib.sha256(open(ARC / "verification" / "couplings_on_the_weave.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "couplings_on_the_weave.json"))
    assert d["C1"] == {"TbarT": 1, "TT": 0, "Sym2T": 0, "Alt2T": 0, "TTT": 0, "TTTbar": 0}
    assert d["C3"]["singular_values_normalised"] == [1.0, 1.0, 1.0] and d["C5"]["free_mass_parameters_at_residual_RL"] == 3
    s = json.load(open(ARC / "verification" / "post_seal_family_scan.json"))
    fam = list(s.values())[0]
    assert abs(fam["sum_rule_m1_plus_m2_over_m3"][0] - 1) < 1e-9 and abs(fam["sum_rule_m1_plus_m2_over_m3"][1] - 1) < 1e-9
    assert fam["m2_m3_range"][0] >= 0.5 - 1e-6 and fam["closest_to_charged_leptons"]["log10_distance"] > 1
