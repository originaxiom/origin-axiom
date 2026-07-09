"""B477 — sterile-class recon lock (law OPEN; nothing banked as law).

Recompute tier: the SL(2) Ptolemy obstruction-class counts for the three manifolds
(L6a4/s776/m129 give 8/8/4 classes = 2^cusps) via snappy — the frame the recon table
hangs on. The per-class fertile/sterile dims come from the banked B461 eliminations
(exact but heavy); those rows, and the honest verdict that s776's THREE fertile
classes refute the suggested linear law, are locked as a documentation-integrity
test (not a recompute) against FINDINGS.md.
"""
import pathlib

import pytest

FINDINGS = (pathlib.Path(__file__).resolve().parents[1] / "frontier"
            / "B477_sterile_classes" / "FINDINGS.md").read_text(encoding="utf-8")

# the banked recon table (B461 exact eliminations; see FINDINGS.md)
TABLE = {
    "L6a4": {"classes": 8, "fertile": {0, 2, 4, 7}, "sterile": {1, 3, 5, 6}},
    "s776": {"classes": 8, "fertile": {0, 4, 6}, "sterile": {1, 2, 3, 5, 7}},
    "m129": {"classes": 4, "fertile": {0, 3}, "sterile": {1, 2}},
}


def test_obstruction_class_counts_recomputed():
    """8/8/4 obstruction classes (= 2^cusps), recomputed live with snappy."""
    snappy = pytest.importorskip("snappy")
    for nm, row in TABLE.items():
        M = snappy.Manifold(nm)
        V = M.ptolemy_variety(2, obstruction_class="all")
        assert len(V) == row["classes"], nm
        assert len(V) == 2 ** M.num_cusps(), nm       # H^2(M, dM; Z/2) count


def test_table_is_a_partition_and_s776_refutes_the_linear_law():
    """Internal consistency: fertile/sterile partition each class set; s776 has
    THREE fertile classes (not a power of 2), the datum that kills the coset law."""
    for nm, row in TABLE.items():
        assert row["fertile"] | row["sterile"] == set(range(row["classes"])), nm
        assert not (row["fertile"] & row["sterile"]), nm
    n_fertile_s776 = len(TABLE["s776"]["fertile"])
    assert n_fertile_s776 == 3
    assert n_fertile_s776 not in (1, 2, 4, 8)  # not a power of 2 -> not a coset


def test_findings_table_rows_locked():
    """Documentation-integrity lock (not a recompute): the exact banked table rows."""
    assert "| L6a4 (Borromean) | 8 | 0 (dim 1), 2 (dim 1), 4, 7 (points, ℚ(i)) | 1, 3, 5, 6 |" in FINDINGS
    assert "| s776 (chain control) | 8 | 0, 4, 6 (points, ℚ(√−7)) | 1, 2, 3, 5, 7 |" in FINDINGS
    assert "| m129 (Whitehead) | 4 | 0, 3 (points, ℚ(i)) | 1, 2 |" in FINDINGS


def test_findings_honest_state_locked():
    """Documentation-integrity lock: the load-bearing verdict — the suggestive L6a4
    pairing is REFUTED as a universal linear law, and nothing is banked as law."""
    assert "refuted as a universal linear law by s776's count" in FINDINGS
    assert "Recon only — nothing banked as law" in FINDINGS
