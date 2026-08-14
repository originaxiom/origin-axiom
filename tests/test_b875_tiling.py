"""Locks B875 -- the triality tiling verified on this seat's build."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B875_triality_tiling"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_tiling_verified():
    assert RES["tiling_verified"] is True


def test_skeleton():
    assert RES["kernel_dims"] == [46, 46, 46]
    assert set(RES["pairwise_intersections"].values()) == {30}
    assert RES["span"] == 78
    assert RES["sector_dims"] == [16, 16, 16]


def test_core_is_so8_u1u1_at_two_own_primes():
    assert RES["core_type_mod_p"] == {"40009": [30, 28, 2], "40037": [30, 28, 2]}
    assert RES["core_is_so8_u1u1"] is True


def test_the_cyclic_law():
    assert RES["law_ok"] is True
    # the diagonal lands in core; off-diagonals land in the foreign sector
    for k, v in RES["law"].items():
        big = [i for i, x in enumerate(v) if float(x) > 0.9]
        assert len(big) == 1, (k, v)
    assert float(RES["law"]["[V1,V1]"][0]) > 0.9
    assert float(RES["law"]["[V1,V2]"][3]) > 0.9
    assert float(RES["law"]["[V1,V3]"][2]) > 0.9
    assert float(RES["law"]["[V2,V3]"][1]) > 0.9


def test_the_nearly_parallel_trap_is_recorded():
    assert "oblique" in RES["nearly_parallel_note"]
    assert "orthogonal projections cannot separate the sectors" in _F
    assert "floating-point reruns are not" in _F


def test_the_generation_reading_stays_a_structure():
    assert "a structure, not a generations mechanism" in _F
    assert "unproven as generations" in _F
