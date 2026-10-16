"""B1609 -- THE EVEN SUBWEAVE: the counts on Gamma and at level 2, the puncture under 2T, as recorded; the sealed file kept;
GENESIS carries the reading."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1609_the_even_subweave"
V = ARC / "verification"


def test_the_sealed_instrument_is_kept():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at f8b9a8fea: ")
    sha = first.split()[4]
    assert hashlib.sha256(open(V / "sealed_run" / "even_subweave.py", "rb").read()).hexdigest() == sha


def test_the_counts():
    d = json.load(open(V / "even_subweave.json"))
    assert d["E1"]["shapiro_holds"] and d["E1"]["orders"] == {"S": 4, "U": 6, "SUS": 6}
    e2 = d["E2"]
    assert all(e2["minus_chi_Gamma"][n] == 9 and e2["minus_chi_SL"][n] == 3 and e2["minus_chi_SL_eps_twisted"][n] == 6 for n in ("E6 (principal)", "E6(a1)", "E6(a3)"))
    assert e2["minus_chi_Gamma"]["78 through the principal sl2"] == 30
    e3 = d["E3"]
    assert e3["shapiro_level2_holds"] and e3["level2_count_27"] == 27
    assert e3["S3_decomposition_of_27"] == {"trivial": 3, "sign": 6, "std (times 2)": 9}
    assert e3["Z3_sectors_on_Gamma"] == {"omega^0": 9, "omega": 9, "omega^2": 9} and e3["omega_sector_equals_std_sector"]
    p = json.load(open(V / "post_seal_78_sectors.json"))
    assert p["78 through the principal sl2"]["omega^0"] == 30 and p["78 through the principal sl2"]["omega"] == 24 == p["78 through the principal sl2"]["omega^2"]


def test_the_puncture_on_the_even_subweave():
    e4 = json.load(open(V / "even_subweave.json"))["E4"]
    assert e4["order_full"] == 48 and e4["order_even"] == 24 and e4["minus_one_in_even_group"]
    assert e4["commutant_even"] == 3 and e4["isotypic_dimensions"] == [2, 2, 2] and e4["kept_indices"] == [-3, -1, 1, 3]
    assert sorted(e4["deck_L_maps_pieces_to"]) == [0, 1, 2] and sum(1 for i, j in enumerate(e4["deck_L_maps_pieces_to"]) if i == j) == 1
    g = e4["even_and_grading"]
    assert g["commutant"] == 1 and g["kept_indices"] == [-3, 3]


def test_genesis_carries_the_reading():
    g = open(ROOT / "GENESIS.md", encoding="utf-8").read()
    assert int(g.split("**Version 1.")[1].split()[0]) >= 30 and "THE EVEN SUBWEAVE (main, B1609" in g   # a lower bound, never the header (E86)
    assert "the weave's three is the S₃-invariant part of a level-2 count" in g
