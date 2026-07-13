from cell1b_localized_charge_carriers import run_all


def test_all_nonzero_residues():
    result = run_all()
    assert set(map(int, result["witnesses"])) == set(range(1, 11))


def test_first_witness_lengths():
    assert run_all()["minimal_core_lengths"] == {
        "1": 3, "2": 9, "3": 3, "4": 16, "5": 14,
        "6": 14, "7": 16, "8": 3, "9": 9, "10": 3,
    }


def test_inflation_preserves_charge():
    result = run_all()
    for residue, records in result["scale_transport"].items():
        assert all(r["delta_charge"] == int(residue) for r in records)


def test_charge_does_not_fix_spectral_moments():
    result = run_all()
    assert set(result["residues_with_multiple_spectral_moment_pairs"]) >= {3, 8}
