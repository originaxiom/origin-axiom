"""B1507 lock -- THE RECORD REREAD (2026-10-01).  The sweep's load-bearing items, recomputed here with own code:
the deck on the closed tower (B350 (iv) and B521's Gate C as B1506's fence: det(phi - 1) = -1, Y3's scalar omega, orbits 1 + 5 x 3);
the cohomological three on m004 (one class per principal block of the 27); the July flavour cluster read against B1362 (a
deck-invariant matrix is a circulant: generic three distinct, symmetric a degenerate pair; B345's texture is circ(x, y, y) in the
charge basis); the physics seat's R64 and R68 on B1270's icosian E8 (one element = family rotation x trinification; exactly one of 40
trinification frames is two-sided, mirror-invariant); s961's deck-inverting isometries (SnapPy); the audit lane's R60/R61 against
B1504 (the root-line orbit is one 3-cycle of many; complex rotation-invariant lines pass the combined reality with zero current)."""
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1507_the_record_reread"
VER = ARC / "verification"


def _load(name):
    spec = importlib.util.spec_from_file_location(f"b1507_{name}", VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_deck_on_the_tower_live():
    """H_1(Y_n) and the deck's orbit sizes for n = 2..6: one fixed element (zero) on every level; Y3 = (Z/4)^2 with orbits 1 + 5 x 3
    (B1506's loci orbits); phi^2 + phi + 1 = 0 on Y3; Gate C's det(T - 1) = 3 is det(phi - 1) = -1 mod 4; (phi - 1)v keeps the order
    of v; the Klein 2-torsion is 3-cycled with no fixed element; Delta = Phi_3 mod 4"""
    T = _load("deck_on_the_tower")
    want = {2: ([1, 5], {1: 1, 2: 2}), 3: ([4, 4], {1: 1, 3: 5}), 4: ([3, 15], {1: 1, 2: 2, 4: 10}),
            5: ([11, 11], {1: 1, 5: 24}), 6: ([8, 40], {1: 1, 2: 2, 3: 5, 6: 50})}
    for n, (smith, sizes) in want.items():
        r = T.tower(n)
        assert r["smith"] == smith and r["fixed"] == 1 and r["orbit_sizes"] == sizes, r
    y = T.y3_details()
    assert y["det_phi_minus_1"] == -1 and y["omega_scalar"] and y["difference_same_order"]
    assert y["gate_c_det"] == 3 and y["gate_c_det_mod4"] == y["unit_mod4"] == 3
    assert sorted(y["klein"]) == [(0, 0), (0, 2), (2, 0), (2, 2)] and y["klein_fixed"] == []
    assert y["phi3_irreducible_mod2"] and y["delta_is_phi3_mod4"]


def test_the_principal_blocks_live():
    """h^1(m004; V17) = h^1(V9) = h^1(V1) = 1 at three primes: the cohomological three, one class per block (B657)"""
    P = _load("principal_blocks")
    res = P.main()
    assert set(res) == set(P.PRIMES)
    assert all(row == {"V17": 1, "V9": 1, "V1": 1} for row in res.values()), res


def test_the_flavour_cluster_live():
    """B335's 'exactly degenerate' needs no inter-generation coupling; B325's generic split and B1362's symmetric pair; B345's
    allowed set is the support of circ(x, y, y) in the charge basis"""
    Fc = _load("flavour_cluster")
    a = Fc.circulant_facts()
    assert a["commutes"] and a["diagonal_in_charge_basis"]
    assert a["symmetric_eigenvalues"] == ["c0 + 2*c1", "c0 - c1", "c0 - c1"] and a["symmetric_pair_degenerate"]
    assert a["all_equal_only_if"] == [{"c1": "0", "c2": "0"}]
    assert a["generic_three_distinct_50_of_50"] and a["symmetric_pair_50_of_50"]
    b = Fc.b345_texture()
    assert b["allowed"] == [(0, 0), (1, 2), (2, 1)] and b["support_equals_allowed"]
    assert b["circulant_in_charge_basis"] == [["x + 2*y", "0", "0"], ["0", "0", "x - y"], ["0", "x - y", "0"]]


def test_the_founding_ratio_frames_live():
    """R64: for two order-3 units, E6 = Z[g]^perp has 72 roots, no fixed root, 24 free orbits, B(r, gr) = -1; the principal
    order-3 element's centraliser is A2^3 (9 positive roots of height 0 mod 3, components 6, 6, 6).  R68: 120 A2's, 40 frames,
    4 left-stable, 4 right-stable, 1 two-sided; right-g on the left frames is a 3-cycle and a fixed point; mirror-invariant"""
    Fr = _load("founding_ratio_frames")
    res = Fr.main()
    assert res["e8_roots"] == 240 and res["unit_icosians"] == 120 and res["order3_units"] == 20
    for label in ("unit_0", "unit_7"):
        r = res[label]
        assert (r["e6_roots"], r["fixed_roots"], r["free_orbits"]) == (72, 0, 24)
        assert [int(x) for x in r["pairing_r_gr"]] == [-1]
        assert (r["a2"], r["frames"], r["left"], r["right"], r["both"]) == (120, 40, 4, 4, 1)
        assert r["right_on_left_cycle_type"] == [(1, 1), (3, 1)] and r["two_sided_mirror_invariant"] == [True]
    p = res["principal_order3"]
    assert p["simple"] == 6 and p["height_0_mod_3_positive"] == 9 and p["centraliser_dim"] == 24 and p["components"] == [6, 6, 6]


def test_the_deck_inverting_isometry_live():
    """m004: four of eight isometries negate the meridian, two orientation-preserving.  s961: the only cyclic 3-fold cover; Isom of
    order 24, nonabelian, centre Z/2, abelianization (Z/2)^2; exactly two elements of order 3, cusp-trivial, normal (the deck);
    twelve elements invert it, six orientation-preserving, all negating the meridian"""
    pytest.importorskip("snappy")
    D = _load("deck_inverting")
    M, G, rows = D.m004_isometries()
    assert G.order() == 8
    neg = [r for r in rows if r["meridian"] == -1]
    assert len(neg) == 4 and sum(r["det"] == 1 for r in neg) == 2
    s = D.s961_group()
    assert "s961(0,0)" in s["identify"] and s["cusps"] == 1 and s["vol_ratio"] == 3.0
    assert s["order"] == 24 and not s["abelian"] and s["centre"] == "Z/2" and s["abelianization"] == "Z/2 + Z/2"
    assert s["order_3"] == 2 and s["order_3_cusp_maps"] == [[[1, 0], [0, 1]], [[1, 0], [0, 1]]] and s["deck_normal"]
    assert s["inverting"] == 12 and s["inverting_orientation_preserving"] == 6 and s["inverting_meridian_signs"] == [-1]


def test_the_end_lines_live():
    """R60: the root lines are one rotation orbit and (1, 3)'s is another; no line is fixed.  R61: both complex eigenlines are
    invariant under rotations of order 3, 4, 6, pass C u = u with their phase, and carry zero current"""
    E = _load("end_lines")
    a = E.lines()
    assert a["root_orbit"] == [(1, 0), (0, 1), (1, 1)] and a["orbit_1_3"] == [(1, 3), (3, 2), (2, -1)]
    assert a["disjoint"] and a["fixed_lines"] == []
    for name, r in E.complex_lines().items():
        assert r["rotation_invariant"] == {3: True, 4: True, 6: True} and r["C_invariant"] and r["current"] == "0", (name, r)


def test_findings_verdict_and_hygiene():
    """the verdict is PROVED with I-14 declared UNEARNED; the findings carry the corrections and the leads; B342 now points to B343"""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1507" and v["verdict"] == "PROVED"
    assert [(i["row"], i["status"]) for i in v["identifications"]] == [("I-14", "UNEARNED")]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for needle in ("B335:9", "Gate C", "det(φ − 1) = −1", "R64", "R68", "85 (B1264) → 40", "deck-inverting",
                   "exactly degenerate", "N = +3", "R60/R61", "B1430", "B719", "## 10. Leads registered", "0 of 19"):
        assert needle in f, needle
    b342 = json.loads(next((ROOT / "frontier").glob("B342_*/arc_verdict.json")).read_text(encoding="utf-8"))
    assert b342["superseded_by"] == "B343"
    for name in ("deck_on_the_tower", "principal_blocks", "flavour_cluster", "founding_ratio_frames", "deck_inverting", "end_lines"):
        assert (VER / f"{name}_run.txt").exists(), name
