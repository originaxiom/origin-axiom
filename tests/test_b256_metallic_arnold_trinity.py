"""B256 locks -- the metallic Arnold trinity: discriminant field Q(sqrt(m^2+4)) gives E8 (m=1), E7 (m=2); with the
figure-eight trace field Q(sqrt-3)=E6, all three Arnold groups appear. E7 = silver discriminant (geometrically
homeless). FIREWALLED (arithmetic/McKay, not physics); nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B256_metallic_arnold_trinity" / "metallic_arnold_trinity.py"
_spec = importlib.util.spec_from_file_location("b256", _PATH)
b256 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b256)


def test_discriminant_is_m2_times_metallic():
    for m in range(1, 8):
        assert b256.discriminant(m) == m * m * (m * m + 4)


def test_silver_discriminant_is_E7():
    # the headline: m=2 silver discriminant field Q(sqrt2) -> 2O -> E7
    assert b256.discriminant_field_radicand(2) == 2
    assert b256.mckay_of_metallic(2) == ("2O", "E7")


def test_golden_discriminant_is_E8():
    assert b256.discriminant_field_radicand(1) == 5
    assert b256.mckay_of_metallic(1) == ("2I", "E8")
    assert b256.mckay_of_metallic(4) == ("2I", "E8")     # sqrt20 = sqrt5


def test_bronze_and_beyond_are_non_mckay():
    assert b256.mckay_of_metallic(3) is None             # Q(sqrt13)
    assert b256.mckay_of_metallic(5) is None             # Q(sqrt29)


def test_arnold_trinity_complete():
    # E6 (golden trace field, external) + E8 (golden disc) + E7 (silver disc) = all three
    appearing = {"E6"} | {b256.mckay_of_metallic(m)[1] for m in (1, 2)}
    assert appearing == {"E6", "E7", "E8"}
