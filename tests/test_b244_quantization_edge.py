"""B244 locks -- the (1)<->(2) quantization edge: the SL(3,C) geometric component has Vol = 4*Vol(SL(2)) (the
Sym^2 (n^3-n)/6 factor, Ptolemy-confirmed); SU(3)_2 at level 2 is one number and the fundamental rep doesn't see
the volume. Firewall-clean; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B244_quantization_edge" / "quantization_edge.py"
_spec = importlib.util.spec_from_file_location("b244", _PATH)
b244 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b244)


def test_sym2_volume_factor():
    assert b244.sym_volume_factor(2) == 1                       # Sym^1 = identity: factor 1 (sanity)
    assert b244.sym_volume_factor(3) == 4                       # Sym^2: (27-3)/6 = 4
    # the Ptolemy geometric SL(3) volume = 4 * Vol(SL(2)) (the V0=Sym^2 identification, via volume)
    assert abs(b244.VOL_SL3_GEO - 4 * b244.VOL_SL2) < 1e-9


def test_three_distinct_saddles():
    vols = b244.SL3_COMPONENT_VOLS
    assert len(vols) == 3                                       # 3 components (B71)
    assert abs(vols[0] - 4 * b244.VOL_SL2) < 1e-9              # V0 geometric carries the volume
    assert vols[1] == 0 and vols[2] == 0                       # W1/W2 Dehn-filling: volume 0 (distinct saddles)


def test_su32_is_one_number_and_fundamental_sees_no_volume():
    assert abs(b244.su32_fundamental() - (-2 / b244.PHI)) < 1e-9    # SU(3)_2 fundamental: a single number
    assert abs(b244.fundamental_limit(3, 3000) - 1) < 1e-3          # fixed fundamental rep -> 1 (no vol growth)
