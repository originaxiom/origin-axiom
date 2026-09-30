"""B1505 lock -- THE ORBIFOLD LINKS: in the known G2 cones whose links are orbifolds but not global quotients (AW section 2; AW
section 3's twistor cones over positive selfdual Einstein orbifolds, toric or Hitchin's; their isometric quotients), no ADE locus
is a cone over a torus of constant type.  T1: twistor loci are fibres (spheres) or sections over fixed surfaces of M.  T2:
e_orb(N_F) = chi_orb(F) - s area_orb(F)/24pi for totally geodesic F.  T3: an isometry of a compact positive toric selfdual
Einstein orbifold fixes spheres, or a real locus (chi = 4 - k) that meets the orbifold locus when k >= 4.  T4: the two sections
over a fixed surface carry opposite inflows +-(N/2)(2e - chi).  T5: AW section 2's strata are two coordinate lines and points."""
import importlib.util
import json
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1505_the_orbifold_links"
VER = ARC / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1505_orbifold_links", VER / "orbifold_links.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_census_live_k3_k4():
    """T3 on every datum with k = 3, 4: CS's inequality, smooth only at k = 3 (CP^2), no rotation fixes a principal orbit,
    no reflection fixes a torus, every real locus has chi = 4 - k and meets the orbifold locus unless M is CP^2"""
    O = _load()
    t = O.census(ks=(3, 4))["tally"]
    assert t["k=3 data"] == 606 and t["k=4 data"] == 3295
    assert t["k=3 smooth"] == 6 and t["k=4 smooth"] == 0
    assert t["k=3 rotations fixing a principal orbit"] == 0 and t["k=4 rotations fixing a principal orbit"] == 0
    assert not any("torus" in key for key in t)
    assert t["k=3 real loci chi=1, meeting the orbifold locus=False"] == 6
    assert t["k=4 real loci chi=0, meeting the orbifold locus=True"] == 3295
    assert not any(key.startswith("k=4 real loci") and key.endswith("False") for key in t)


def test_the_recorded_census():
    r = json.load(open(VER / "orbifold_links.json"))
    t = r["census"]["tally"]
    assert [t[f"k={k} data"] for k in (3, 4, 5, 6)] == [606, 3295, 13009, 40078]
    assert [t[f"k={k} smooth"] for k in (3, 4, 5, 6)] == [6, 0, 0, 0]
    assert not any("torus" in key for key in t)
    assert all(t.get(f"k={k} rotations fixing a principal orbit", 0) == 0 for k in (3, 4, 5, 6))
    for k in (4, 5, 6):
        assert t[f"k={k} real loci chi={4 - k}, meeting the orbifold locus=True"] == t[f"k={k} data"]


def test_the_curvature_identity_live():
    """T2 on the exceptional surfaces of CP^2 and of a symmetric k = 4 orbifold (labels 2, 8, 2, 4), from the closed forms:
    area_orb/2pi = chi_orb - e exactly (s = 12)"""
    O = _load()
    for name in ("CP2", "k4 symmetric, labels (2,8,2,4)"):
        data = O.IDENTITY_DATA[name]
        _, _, rows, _ = O.invariants(data)
        for row in rows:
            assert abs(O.edge_area_orb(data, row["edge"]) - float(row["chi"] - row["e"])) < 1e-10, (name, row)
    assert [str(r["chi"] - r["e"]) for r in O.invariants(O.IDENTITY_DATA["k4 symmetric, labels (2,8,2,4)"])[2]] == \
        ["1/48", "1/32", "1/48", "1/24"]


def test_the_recorded_identity():
    r = json.load(open(VER / "orbifold_links.json"))["identity"]
    surfaces = [s for d in r.values() if "surfaces" in d for s in d["surfaces"]]
    assert len(surfaces) == 15 and max(s["deviation"] for s in surfaces) < 1e-10
    for d in r.values():
        if "curvature" in d:
            assert d["closed_form_deviation"] < 1e-12
            for c in d["curvature"]:
                assert abs(c["s"] - 12) < 1e-12 and c["einstein"] < 1e-18 and c["minus_block_minus_s_over_12"] < 1e-18
                assert c["plus_block_minus_s_over_12"] > 1e-2           # W+ is not zero: selfdual, not conformally flat
    assert r["CP2 real locus (RP^2: chi 1, e -1)"]["deviation"] < 1e-8


def test_the_pairing_hitchin_and_aw2_live():
    O = _load()
    assert O.pair_degrees(2, 0) == ((-2, 0), (0, -2))                  # B1503's CP^3 pair
    for e in (-1, -4):
        p, m = O.pair_degrees(0, e)
        assert Fr(p[0] - p[1], 2) == e and Fr(m[0] - m[1], 2) == -e       # a torus: opposite inflows +-N e
    h = O.hitchin()
    assert [r["fixed_set_in_S4"] for r in h["rotations"]] == ["2-sphere"] + ["two points"] * 10
    assert h["singular_orbit"]["fixed_by_rotations_about_its_axis"] and h["singular_orbit"]["fixed_by_the_half_turn_swapping_the_axis"]
    a = O.aw2()
    assert set(a) == {"0-dimensional strata", "2-dimensional strata: the line (0, 1) (a 2-sphere)",
                      "2-dimensional strata: the line (2, 3) (a 2-sphere)", "cones (n, m, r)"}


def test_the_findings_and_the_verdict():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    for s in ("Not sealed", "Anguelova", "Calderbank", "real locus", "Hitchin", "constant type", "oppositely chiral", "0 of 19"):
        assert s in f, s
    v = json.load(open(ARC / "arc_verdict.json"))
    assert v["id"] == "B1505" and v["verdict"] == "PROVED" and "0 of 19" in v["claim_one_line"]
