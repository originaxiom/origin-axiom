"""B896 locks: the S3-harmonic split of the banked frame-indexed tables."""
import json
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B896_s3_harmonics")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_dictionary_is_one_table_trivial_dominates():
    r = _res()
    assert r["b889_trivial_fraction"] > 0.999
    assert r["b889_standard_fraction"] < 1e-3
    # the frame-breaking content concentrates in the leakage rows:
    rows = r["b889_per_row_standard_fraction"]
    assert len(rows) == 11
    assert min(rows) < 1e-8          # law rows: exactly frame-symmetric
    assert max(rows) < 5e-3          # leakage rows: small, nonzero


def test_alignment_was_solved_jointly():
    r = _res()
    a1, a2 = r["alignment"]["1"], r["alignment"]["2"]
    # nontrivial block relabelings for both non-reference frames
    assert a1["octet_perm"] != [0, 1, 2]
    assert a2["octet_perm"] != [0, 1, 2]
    # rows permute too (the caught model error)
    assert a1["row_map"] != list(range(11)) or a2["row_map"] != list(range(11))
    # per-frame asymmetry visible in the residuals themselves
    assert a1["residual"] > 10 * a2["residual"]


def test_deviation_patterns_near_maximally_frame_breaking():
    r = _res()
    for key in ("b890_dev_split", "b891_dev_split"):
        sf = r[key]["std_fraction"]
        assert 0.5 < sf < 2.0 / 3.0   # bounded by 2/3 for nonnegative data


def test_sign_isotypic_placement():
    r = _res()
    assert "sign-class" in r["sign_isotypic"]
    # rep theory: C^3 has no sign component -- the statement is recorded
    assert "trivial + standard" in r["sign_isotypic"]
