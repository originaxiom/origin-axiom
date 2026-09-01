#!/usr/bin/env python3
"""R034: source-locked Phase-C adjudication of two legacy spin seams.

This checks the type distinction and the status implied by B1231's rule.  It
does not recompute B1141/B1145's exact internal matrices or B359--B364's theta
tables; those results remain intact and are pinned by their source blobs.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    data = json.loads((HERE / "source_snapshot.json").read_text(encoding="utf-8"))
    assert data["schema"] == "oa-r034-spin-identification-phase-c-v1"
    assert data["source_commit"] == "864c6b758e2bbd0e0921f5e36af47df68b3c99ca"

    sources = data["sources"]
    expected = {
        "identification_ledger": (
            "docs/IDENTIFICATION_LEDGER.md",
            "326f3955b6c9490a4950e20b1909a015ecc27c52",
        ),
        "b1112": (
            "frontier/B1112_projective_hatch/FINDINGS.md",
            "390fbb4c033e78dffdde843ecfcdf75e4fd51275",
        ),
        "b1141": (
            "frontier/B1141_spin_payment/FINDINGS.md",
            "e98731a518ae70502d8a02cf9848c913d2c863ae",
        ),
        "b1145": (
            "frontier/B1145_sp2_fermion_seat/FINDINGS.md",
            "bbfc235ced367c9294c02e72907506abd6039c24",
        ),
        "b1140": (
            "frontier/B1140_the_64_organized/FINDINGS.md",
            "afc9ab82404efda8d3dfc0f1eb3df425b14f96c4",
        ),
        "b366": (
            "frontier/B366_invariant_spin_sector/FINDINGS.md",
            "07a1d84b193a627aef82a4cd6aa99e8bf89ade89",
        ),
        "b1218": (
            "frontier/B1218_open_claim_sweep/FINDINGS.md",
            "b2b61f9dcaa526d559ac75eab73681d217c51968",
        ),
    }
    for key, (path, blob) in expected.items():
        assert sources[key]["path"] == path
        assert sources[key]["git_blob_sha1"] == blob
    assert sources["b359_b363_b364"]["paths"] == [
        "frontier/B359_seam_form/FINDINGS.md",
        "frontier/B363_seam_lift_anatomy/FINDINGS.md",
        "frontier/B364_theta_polarization/FINDINGS.md",
    ]
    assert sources["b359_b363_b364"]["git_blob_sha1"] == [
        "449cc3e7880b8843da9a239b467b9d7f92684784",
        "fdd127582c98c3677c9f7280bd292752a06814da",
        "4b40ddfcf05b2549f2af5a3a352e9fabba18751b",
    ]

    b1145 = " ".join(sources["b1145"]["facts"])
    assert "internal to E6" in b1145 and "not the 4d Lorentz group" in b1145
    assert "no Pin structure" in b1145 and "Dirac operator" in b1145
    b1218 = " ".join(sources["b1218"]["facts"])
    assert "not identified" in b1218 and "3-manifold spin structure" in b1218
    theta = " ".join(sources["b359_b363_b364"]["facts"])
    assert "T-stability selects neither" in theta
    b366 = " ".join(sources["b366"]["facts"])
    assert "level-15 geometric-quantization premise" in b366
    assert "does not identify" in b366

    rows = data["adjudications"]
    assert [row["proposed_row"] for row in rows] == ["I-8", "I-9"]
    assert all(row["status"] == "UNEARNED" for row in rows)
    assert all(row["map"] is False and row["acts"] is False for row in rows)
    assert all(row["side_a"] != row["side_b"] for row in rows)
    assert all(row["earning_test"] and row["not_refuted"] for row in rows)

    # The status is not REFUTED: each source-side mathematical construction
    # remains certified.  What is absent is the cross-type physical map.
    assert "remains proved" in rows[0]["not_refuted"]
    assert "remain proved" in rows[1]["not_refuted"]

    # Controls: matching the word "spin" or an affine Z/2 count cannot meet
    # the ledger's two requirements.  Supplying both would change the status.
    def status(has_map: bool, faithful_action: bool) -> str:
        return "EARNED" if has_map and faithful_action else "UNEARNED"

    assert status(False, False) == "UNEARNED"
    assert status(True, False) == "UNEARNED"
    assert status(True, True) == "EARNED"

    print("PASS B1145 exact internal beat/A1 closure is preserved")
    print("PASS B1145 itself separates internal A1 from 4d Lorentz spin")
    print("PASS B1218 itself says boundary theta is not identified with B1141 spin")
    print("CONTROL a map without faithful action remains UNEARNED")
    print("RESULT I-8 internal-A1 to 4d-spacetime-spin = UNEARNED")
    print("RESULT I-9 boundary-theta to bulk/observer-spin = UNEARNED")
    print("SCOPE two legacy identifications; no algebraic theorem is retracted")


if __name__ == "__main__":
    main()
