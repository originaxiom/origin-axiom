"""B233 locks -- H17 (why 5): the exact arithmetic backbone of the partial-unification verdict.
Firewall: pure arithmetic/rep-theory; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B233_synthesis_split_and_five" / "verify_five.py"
_spec = importlib.util.spec_from_file_location("b233_five", _PATH)
b233 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b233)


def test_root_A_five_is_smallest_metallic_discriminant():
    assert b233.metallic_disc(1) == 5
    assert min(b233.metallic_disc(m) for m in range(1, 100)) == 5


def test_root_B_mckay_primes_and_E7_exclusion():
    """SL(2,F_3)=2T=E6, SL(2,F_5)=2I=E8 (largest McKay prime 5); E7=2O (order 48) never SL(2,F_p)."""
    m = b233.mckay_as_sl2fp()
    assert m["E6 (2T)"] == 3 and m["E8 (2I)"] == 5 and m["E7 (2O)"] is None
    from sympy import isprime
    assert 48 not in {b233.sl2_fp_order(p) for p in range(2, 200) if isprime(p)}


def test_cascade_is_partial_unification():
    """8/8 faces flow from root A; exactly one (E_8) also touches root B -> not a pile-up, one coincidence."""
    tbl = b233.cascade_table()
    assert len(tbl) == 8
    assert sum(r.startswith("A") for _, r in tbl) == 8       # all cascade from A
    assert sum("B" in r for _, r in tbl) == 1                # B contributes exactly once (the coincidence)
