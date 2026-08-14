"""Locks B889 -- the canonical dictionary."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B889_canonical_dictionary"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_the_canonical_blocks_and_bijection():
    assert RES["block_dims"] == [1, 1, 1, 8, 8, 8]
    assert sorted(RES["vacuum_frame_map"].values()) == [0, 1, 2]


def test_the_tables_shape_and_zero_count():
    for ri in ("0", "1", "2"):
        tab = RES["tables"][ri]
        assert sorted(t["dim"] for t in tab) == [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 6]
        zeros = sum(1 for t in tab for m in t["mass"] if m < 1e-12)
        assert zeros == 26


def test_own_vacuum_alignment_of_singlets():
    inv_map = {v: int(k) for k, v in RES["vacuum_frame_map"].items()}
    for ri in ("0", "1", "2"):
        own = inv_map[int(ri)]
        singles = [t for t in RES["tables"][ri] if t["dim"] == 1]
        onown = [t for t in singles if t["mass"][own] > 0.999999]
        assert len(onown) == 1


def test_sixteens_avoid_all_vacua():
    for ri in ("0", "1", "2"):
        for t in RES["tables"][ri]:
            if t["dim"] == 6:
                assert all(t["mass"][k] < 1e-12 for k in range(3))


def test_the_fence():
    assert "no identification with any physical mixing parameter" in _F
    assert "first naturally small invariant structural numbers" in _F.replace("*", "")
