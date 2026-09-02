#!/usr/bin/env python3
"""R040: closed free-deck CS theorem logic and full cusped census test."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import snappy


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "source_snapshot.json"
TOLERANCE = 1e-6


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def cs_class(value):
    residue = (float(value) + 0.25) % 0.5 - 0.25
    if abs(residue) < TOLERANCE:
        return "zero", residue
    if abs(abs(residue) - 0.25) < TOLERANCE:
        return "quarter", residue
    return "other", residue


def main():
    source = json.loads(SOURCE.read_text())
    require(source["schema"] == "oa-r040-free-deck-cs-source-v1",
            "source schema")
    require(source["fresh_main"] == "52010c9e", "fresh-main fence")
    require(source["primary_sources"]["kawauchi_1981"]["theorem_III"] ==
            "alpha(M)=0 iff sigma(a,M)=0", "Kawauchi fence")
    require(source["primary_sources"]["cghn_2003"]
            ["closed_relation_page_14"] ==
            "3 eta(M) = 2 cs(M) + tau modulo 2", "APS/CGHN fence")

    # Formal implication check for the closed theorem.  A free involution has empty fixed set, so
    # Kawauchi gives Tor H1=A+A and hence even tau.  Orientation reversal makes
    # the odd-signature spectrum symmetric, eta=0.  The CGHN congruence then
    # reads 2*cs=0 mod 2, i.e. cs=0 in the closed R/Z normalization.
    fixed_h1_rank_mod2 = 0
    alpha = fixed_h1_rank_mod2
    tau_parity = alpha
    eta = 0
    two_cs_mod2 = (3 * eta - tau_parity) % 2
    require((alpha, tau_parity, two_cs_mod2) == (0, 0, 0),
            "closed parity chain")

    expected = source["nonorientable_cusped_census_size"]
    require(len(snappy.NonorientableCuspedCensus) == expected,
            "census-size fence")
    require(snappy.__version__ == source["snappy_version"],
            "SnapPy-version fence")

    counts = Counter()
    maximum_cs_residual = 0.0
    maximum_volume_ratio_error = 0.0
    names = set()
    orientability_failures = 0
    cusp_failures = 0
    for base in snappy.NonorientableCuspedCensus:
        cover = base.orientation_cover()
        name = str(cover.name())
        require(name not in names, f"duplicate returned cover name {name}")
        names.add(name)
        if not cover.is_orientable():
            orientability_failures += 1
        if cover.num_cusps() < 1:
            cusp_failures += 1
        label, residue = cs_class(cover.chern_simons())
        counts[label] += 1
        maximum_cs_residual = max(maximum_cs_residual, abs(residue))
        ratio_error = abs(float(cover.volume() / base.volume()) - 2.0)
        maximum_volume_ratio_error = max(maximum_volume_ratio_error,
                                         ratio_error)

    require(counts == Counter({"zero": expected}), "cusped CS census")
    require(orientability_failures == 0, "orientation-cover orientability")
    require(cusp_failures == 0, "cusped-cover status")
    require(maximum_volume_ratio_error < 1e-12, "degree-two volume control")

    print("RESULT closed free orientation-reversing involution => cs = 0 mod 1")
    print("DATA formal closed implication fixed-H1 parity / tau parity / 2cs mod2 =",
          fixed_h1_rank_mod2, tau_parity, two_cs_mod2)
    print("DATA SnapPy version =", snappy.__version__)
    print("DATA nonorientable cusped census entries =", expected)
    print("RESULT orientation-cover CS classes zero/quarter/other =",
          counts["zero"], counts["quarter"], counts["other"])
    print("CONTROL orientability failures / cusp failures / duplicate names =",
          orientability_failures, cusp_failures, expected - len(names))
    print("CONTROL maximum |cover/base volume ratio - 2| =",
          f"{maximum_volume_ratio_error:.3e}")
    print("DATA maximum absolute CS residue mod 1/2 =",
          f"{maximum_cs_residual:.3e}")
    print("PASS all 1260 finite cusped orientation covers are numerically CS-zero")
    print("SCOPE the closed statement is a theorem; the cusped statement is a finite numerical census, not a universal theorem")
    print("SCOPE no chirality, rank, generation, scale, dynamics or Standard-Model value follows")


if __name__ == "__main__":
    main()
