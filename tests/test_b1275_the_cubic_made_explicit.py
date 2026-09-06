"""B1275 — the E6 cubic solved from rep27.json (unique, values +-1) and the Jordan ranks of the 27-lattice vectors."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
for arc in ("B1267_spectrum_law_rebuilt", "B1275_the_cubic_made_explicit"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))


def test_the_cubic_is_unique_with_values_pm1_and_rank3_is_the_zero_sum_triples(capsys):
    import cubic_explicit as C
    assert C.main()
    out = capsys.readouterr().out
    assert "invariance nullspace dimension: 1" in out
    assert "Jordan rank of a single weight: {1: 27}" in out
    assert "Jordan rank of a zero-sum triple w1 + w2 + w3: {3: 45}" in out
    assert "Jordan rank of a non-zero-sum triple: {1: 720, 2: 2160}" in out
