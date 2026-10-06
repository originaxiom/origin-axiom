"""B1485 -- the SM seat's one-generation members on the silver squares, read by main's instrument: the stored cells."""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1485_the_silver_members_by_a_second_route" / "verification"


def test_the_census_names_exactly_the_seats_members():
    for name in ("m135", "m136"):
        rows = json.load(open(HERE / f"census_{name}.json"))
        assert len(rows) == 8 and all(r["identity_ok"] and r["twin_agrees"] for r in rows)
        with_interior = sorted(tuple(sorted(r["nu"].items())) for r in rows if r["interior_classes"])
        members = sorted(tuple(sorted(r["nu"].items())) for r in rows if r["member"])
        assert with_interior == members and len(members) == 2
        assert all(r["interior_classes"] == 1 for r in rows if r["member"])


def test_the_members_read_minus_one_minus_one_at_the_interior_class():
    for name, n_boundary in (("m135", 1), ("m136", 0)):
        for m in json.load(open(HERE / f"members_{name}.json")):
            assert m["interior"] == 1 and m["boundary"] == n_boundary
            inter = [r for r in m["readings"] if r["cls"].startswith("interior")]
            assert inter and all((r["I_W1"], r["I_L2W1"]) == (-1, -1) and r["identities_ok"] and r["twin_agrees"] for r in inter)
            bdry = [r for r in m["readings"] if r["cls"].startswith("boundary")]
            assert all((r["I_W1"], r["I_L2W1"]) == (0, -1) and r["identities_ok"] and r["twin_agrees"] for r in bdry)
            assert m["split"] == {"I": 0, "I_L2": 0}
    # the failing path: a reading of (-3, -3) or of (0, 0) at an interior class would be a different world
    assert not any((r["I_W1"], r["I_L2W1"]) in ((-3, -3), (0, 0)) for name in ("m135", "m136")
                   for m in json.load(open(HERE / f"members_{name}.json")) for r in m["readings"] if r["cls"].startswith("interior"))


def test_the_controls_passed_before_the_seal():
    c = json.load(open(HERE / "controls.json"))
    assert c["all controls pass"] and c["C0 m010 banked identity"] and c["C1 twin on m010"]["agree"]
    assert c["C1 twin on m010"]["instrument"]["I"] == 1


def test_live_the_banked_identity_of_the_instrument():
    """the control re-run in a fresh interpreter (the instrument's own m010 witness, I = +1)"""
    code = "import sys; sys.path.insert(0, %r); import c2_reducible_index as CI; assert CI.control_m010()" % str(HERE.parents[2] / "frontier" / "B1418_the_family_as_the_object" / "verification")
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=600)
    assert r.returncode == 0, r.stdout[-800:] + r.stderr[-800:]
