"""B1024 / L153 locks — the torsor generators' shadows generate H^1; and the B939 prose transposition.

These recompute the mathematics (WORKING_RULES rule 7) rather than asserting a transcript.
"""
import importlib.util
import json
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b1024", _ROOT / "frontier" / "B1024_l153_bits" / "compute.py")
c = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c)

_B936 = json.loads((_ROOT / "frontier" / "B936_cohomology_reading" / "results.json").read_text())


def test_class_map_reproduces_all_sixteen_banked_classes():
    """Our independent class map must reproduce B936's own table, or it is not the same object."""
    for row in _B936["Q_D_class_table"]:
        assert list(c.h1(tuple(row["signs"]))) == row["H1_class"], row["signs"]


def test_conjugation_shadow_carries_class_0_1():
    assert c.h1(c.CHI_C) == (0, 1)


def test_reversal_shadow_carries_class_1_1():
    """Reversal = the 27<->27bar contragredient (THE CHAIN C21) = the E6 diagram flip = B936's
    tau, i.e. the census element at trivial character."""
    assert c.h1(c.ALL_ONES) == (1, 1)


def test_the_two_generators_span_H1():
    """The sealed SAME outcome: deficit 2."""
    span = {tuple((a * c.h1(c.CHI_C)[i] + b * c.h1(c.ALL_ONES)[i]) % 2 for i in range(2))
            for a in (0, 1) for b in (0, 1)}
    assert span == {(0, 0), (0, 1), (1, 0), (1, 1)}


def test_the_criterion_can_fail__K4_is_the_witness():
    """MB12. The wall Klein's four members span only Z/2, so 'generates (Z/2)^2' is a real
    condition and not satisfied by any four census elements."""
    k4 = {c.h1(x) for x in (c.ALL_ONES, c.CHI_P, c.CHI_M, c.ALL_MINUS)}
    assert len(k4) == 2
    assert _B936["Q_B"]["Klein_to_H1"] == "kernel {I, D2}, image Z/2 = <[D]>"


def test_b939_prose_is_transposed_against_the_computed_flip_counts():
    """The blocker this cell had to resolve before it could run.

    B939's FINDINGS prose reads 'sigma_-1 -> D (12 flips) . sigma_chi- -> D2 (the ELEVEN)'.
    B939's CODE builds by character (`g_sm1 = inner_gmap(ALL_MINUS)`), and B936's class table
    records D_flips per character: ALL_MINUS carries 11, chi- carries 12 — the reverse. B939's
    mathematics is untouched; its prose line is transposed.
    """
    flips = {c.sgn(tuple(r["signs"])): r["D_flips"] for r in _B936["Q_D_class_table"]}
    assert flips[c.sgn(c.ALL_MINUS)] == 11
    assert flips[c.sgn(c.CHI_M)] == 12
    # and B936's own Q_B coordinates agree with the character reading
    assert tuple(_B936["Q_B"]["D_coordinate"]) == c.coord(c.CHI_M)
    assert tuple(_B936["Q_B"]["D2_coordinate"]) == c.coord(c.ALL_MINUS)


def test_every_check_in_the_cell_passes():
    assert all(v["pass"] for v in c.R["checks"].values())
    assert c.R["outcome"]["verdict"] == "SAME"
    assert c.R["outcome"]["deficit"] == 2
