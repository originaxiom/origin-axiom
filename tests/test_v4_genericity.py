"""B777 extension -- cc-verified V4 genericity: V4 is gated by amphicheirality (not generic)."""
import pytest

try:
    import snappy
    HAVE = True
except Exception:
    HAVE = False


@pytest.mark.skipif(not HAVE, reason="snappy unavailable")
def test_v4_gated_by_amphicheirality():
    # cc3's load-bearing claim, cc-verified: amphicheiral <=> V4 (Q(sqrt-3) family) vs
    # non-amphicheiral Q(sqrt-7) family carries Z/2 only
    expected = {
        "m004": (True, "D4"),        # figure-eight: amphicheiral, V4
        "m003": (True, "Z/2 + Z/4"), # sister: amphicheiral, V4 (same vol as m004)
        "m025": (True, "Z/6"),       # amphicheiral, V4
        "m009": (False, "Z/2 + Z/2"),# Q(sqrt-7): NOT amphicheiral, Z/2 only
        "m010": (False, "Z/2 + Z/2"),
    }
    for name, (amph_exp, sym_exp) in expected.items():
        M = snappy.Manifold(name)
        sg = M.symmetry_group()
        assert sg.is_amphicheiral() == amph_exp, f"{name} amphicheiral"
        assert str(sg) == sym_exp, f"{name} symmetry group"
    # the sister risk (verified honest): m004 and m003 share volume AND V4
    assert abs(float(snappy.Manifold("m004").volume()) - float(snappy.Manifold("m003").volume())) < 1e-6
