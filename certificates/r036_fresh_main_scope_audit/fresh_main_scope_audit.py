#!/usr/bin/env python3
"""R036: exact hostile scope audit of B1233--B1234 at main@a5138424."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def kappa(x, y, z):
    return x * x + y * y + z * z - x * y * z - 4


def gradient(x, y, z):
    return (2 * x - y * z, 2 * y - x * z, 2 * z - x * y)


def circle_point(t: F) -> tuple[F, F]:
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def main() -> None:
    sources = json.loads((HERE / "source_snapshot.json").read_text())
    assert sources["schema"] == "oa-r036-fresh-main-scope-audit-sources-v1"
    assert sources["source_commit"] == "a5138424e5712d11aad69d75fc921e3dbccae7fb"
    expected_blobs = {
        "b1233_findings": "b24802b33dcd883ecd5775ab46381d8bee13aa8e",
        "b1233_audit": "fa71c05fcc9c394409da4fa8f95a153f6e03afd6",
        "b1233_verdict": "3ac7929abfbe6f666f5c9964f1787c5e7f40b1e2",
        "b1234_findings": "51ce96cc1f4a24440cfafce772a1707b126a7487",
        "b1234_code": "c5a1f23c4ba6005a0c5b16a08c2384de85c2ea1d",
        "b1234_results": "48a958ac50c81e29994859244a21ba942975ee56",
        "b1234_verdict": "513d22002ce773eaff08f330e9c0f536607328dc",
        "b1234_test": "69990abf085b2ade5b3454fe67c68c1118d55d35",
        "b1224_findings": "89ba8c3e20f1f2b405e83862cd31b3c309d661f2",
        "b1226_findings": "dfc472371682c22bf5b17044aac2f99a6d86ba64",
        "identification_ledger": "859f1b85f0a49679937e9599f15a64f133afc3f6",
        "identification_baseline": "b1226569606b37e0efc89529ae0b0fd7a1ef4447",
        "relay_ledger": "c23bbb6ca0aad73dbe7b82805d9ba00f35654797",
    }
    assert {key: row["git_blob_sha1"] for key, row in sources["sources"].items()} == expected_blobs

    # B1233 checked K(0) and its Hessian.  That proves a strict local minimum,
    # not a global one on R^3.  The diagonal ray is an exact counterexample.
    assert kappa(0, 0, 0) == -4
    assert gradient(0, 0, 0) == (0, 0, 0)
    assert kappa(10, 10, 10) == -704 < -4
    for n in range(6, 50):
        assert kappa(n, n, n) == 3 * n * n - n**3 - 4
        assert kappa(n, n, n) < -F(n**3, 2)

    # Exact critical locus over the reals: the origin and four signed saddles.
    critical = [(0, 0, 0), (2, 2, 2), (2, -2, -2),
                (-2, 2, -2), (-2, -2, 2)]
    assert all(gradient(*point) == (0, 0, 0) for point in critical)
    assert [kappa(*point) for point in critical] == [-4, 0, 0, 0, 0]

    # A compact SU(2)-trace-box reading could rescue "global": for
    # a,b,c in [0,2], a^2+b^2+c^2-abc = (a-b)^2+c^2+ab(2-c) >= 0.
    # Check the polynomial identity exactly on a discriminating rational grid.
    grid = [F(0), F(1, 3), F(1), F(3, 2), F(2)]
    for a in grid:
        for b in grid:
            for c in grid:
                left = a*a + b*b + c*c - a*b*c
                right = (a-b)**2 + c*c + a*b*(2-c)
                assert left == right and right >= 0

    # "Arithmetic cannot emit a continuum" is false as a general principle:
    # this Z-defined circle has an injective real rational parametrization,
    # recovered by t=y/(1+x) for every finite t.
    for t in [F(-7, 3), F(-1), F(0), F(2, 5), F(9, 2)]:
        x, y = circle_point(t)
        assert x*x + y*y == 1
        assert y / (1 + x) == t

    # B1234's three computed cells stand; none computes the claimed joins.
    b1234 = sources["b1234_results_data"]
    assert b1234["orientation_covers_tested"] == b1234["orientation_covers_amphichiral"] == 40
    assert F(b1234["base_rate_num"], b1234["base_rate_den"]) == F(3, 100)
    assert b1234["cover_is_m004"] and b1234["volume_ratio"] == 2.0
    assert b1234["m000_surjections_onto_2T"] == b1234["m004_surjections_onto_2T"] == 48
    assert not b1234["trace_field_computed"]
    assert not b1234["cover_restriction_map_computed"]
    assert not b1234["wall_dependency_graph_computed"]

    # B1234's A6 -> amphichiral -> all-walls arrow also conflicts with the
    # immediately preceding bank: amphichirality gives 2-torsion, not CS=0.
    cs_values = {name: F(value) for name, value in
                 sources["banked_amphichiral_cs_values"].items()}
    assert set(cs_values.values()) == {F(0), F(1, 4)}
    assert cs_values["m003"] == F(1, 4) and cs_values["m004"] == 0

    # Machine ledger truth differs from the stale standing prose.
    counts = Counter(sources["identification_statuses"])
    assert counts == {"EARNED": 3, "REFUTED": 3, "UNEARNED": 3}

    print("REFUTED B1233 global-minimum claim on R^3: K(10,10,10) = -704")
    print("NARROW B1233 origin verdict: strict local minimum; compact trace-box global only if declared")
    print("REFUTED universal slogan 'arithmetic cannot emit a continuum' by a Z-defined circle")
    print("PRESERVED B1234 exact core: 40/40 covers, m000 cover=m004, 48/48 surjections")
    print("REFUTED B1234 amphichirality-to-all-walls arrow: banked CS has both 0 and 1/4")
    print("UNEARNED B1234 prose join: trace-field computation, cover-map inheritance and wall DAG absent")
    print("PRESERVED I-6 debt: formal McKay label does not earn the physical transverse-ALE identification")
    print("HYGIENE identification ledger actual counts = 3 EARNED / 3 REFUTED / 3 UNEARNED")


if __name__ == "__main__":
    main()
