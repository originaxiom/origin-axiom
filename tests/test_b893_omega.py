"""B893 locks: omega transverse to C; the signature census; the wall complex at all roots."""
import json
import os

ARC = os.path.join(os.path.dirname(__file__), "..",
                   "frontier", "B893_omega_vs_measurement")


def _load(name):
    with open(os.path.join(ARC, name)) as f:
        return json.load(f)


def test_omega_is_automorphism_but_charges_not_eigen():
    res = _load("results.json")
    assert res["automorphism"] is True
    # none of the four charges is an omega-eigenvector: transversality
    assert all(v == "NOT-EIGEN" for v in res["charges"].values())
    assert set(res["charges"]) == {"x8", "x14", "x16", "x22"}


def test_signature_dichotomy_measured_split_unmeasured_compact():
    sig = _load("signature_results.json")["signature"]
    # measured plane: all nonzero eigenvalues real, none imaginary
    for c in ("x8", "x16"):
        assert sig[c]["real"] == 48
        assert sig[c]["imag"] == 0
    # unmeasured slots: all nonzero eigenvalues imaginary, none real
    for c in ("x14", "x22"):
        assert sig[c]["imag"] == 66
        assert sig[c]["real"] == 0
    # float-borderline complex counts stay small (flagged in FINDINGS)
    assert all(sig[c]["complex"] <= 7 for c in sig)


def test_wall_complex_at_all_three_roots():
    res = _load("signature_results.json")
    assert res["wall_complex_at_all_roots"] is True
    dets = res["det14_at_roots"]
    assert len(dets) == 3
    # det14 > 0 at every Galois root => a^2 = -det14 < 0 => a imaginary
    assert all(d > 0 for d in dets)
