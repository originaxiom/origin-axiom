"""B1456 -- GENESIS v1.2 verified on main and adopted as v1.3."""
import hashlib, importlib.util, itertools, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1456_genesis_v1_2_verified_and_the_seats_reconciled")


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(A, rel))
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m); return m


def test_a_word_and_its_reverse_live():
    sys.argv = [sys.argv[0], "--quick"]
    V = load("verification/v1_2_own.py", "v1_2_own_b1456")
    ok, d = V.h1(); assert ok and d["words"] == 8190 and d["failures"] == 0
    ok, d = V.h5(); assert ok
    ok, d = V.h7(); assert ok and d["signed_even_power_triples"] == [("LR", 2, -1)]
    # the count by classes, to length nine live (the full run is recorded)
    states = classes = 0
    for L in range(2, 10):
        st = V.G.states(L); states += 2 * len(st); classes += 2 * len({V.canon(w, True) for w in st})
    assert (states, classes) == (130, 110), "2+2+4+6+10+18+32+56 states; 2+2+4+6+10+16+28+42 manifolds"
    # the bite: the swap alone does not merge a word with its reverse at length seven
    assert V.canon("LLLRLRR", False) != V.canon("LLLRRLR", False) and V.canon("LLLRLRR", True) == V.canon("LLLRRLR", True)


def test_the_recorded_run():
    d = json.load(open(os.path.join(A, "verification", "v1_2_own.json")))
    assert len(d) == 7 and all(v["ok"] for v in d.values())
    h2 = d["H2 758 states, 536 manifolds"]["data"]
    assert (h2["states"], h2["classes"], h2["states_in_pairs"]) == (758, 536, 444) and h2["isometry_signatures"] == 536
    assert h2["signature_partition_equals_reversal_partition"] is True and h2["orientation_preserving_isometry_found"] == h2["pairs_sampled"] == 30
    h3 = d["H3 main's census by manifold"]["data"]
    assert (h3["firing_states"], h3["firing_manifolds"], h3["pairs_split"]) == (95, 87, 0) and h3["by_sign"] == {"+": 49, "-": 46}
    h4 = d["H4 signed powers"]["data"]
    assert h4["bundle_of_minus_LRLR"] == "m207" and h4["bundle_of_plus_LRLR"] == "m206" and h4["double_covers_of_m207"] == ["t12839"]
    assert sorted(d["H6 the cusp action of m004's isometries"]["data"]["cusp_maps"].values()) == [2, 2, 2, 2]


def test_the_page_is_the_received_text_with_the_listed_changes():
    am = load("adoption/amend.py", "amend_b1456")
    raw = open(os.path.join(A, "received", "GENESIS_v1_2.md"), "rb").read()
    assert hashlib.sha256(raw).hexdigest() == am.SHA_V1_2
    t, n = am.build(); cur = open(os.path.join(ROOT, "GENESIS.md")).read()
    if "**Version 1.3 ·" in cur: assert cur == t
    assert len(am.CHANGES) == 8 and n == 3 and t.count("[v1.3]") >= 6
    for needle in ("- **v1.3 · 2026-10-02 · main B1456.**", "So a count needs three things together", "There are two signs, not one", "536 distinct manifolds"):
        assert needle in t, needle
    assert "`docs/THE_BAR.md`" not in t


def test_the_units_are_noted_where_the_census_lives():
    for d in ("B1439_the_census_by_slope", "B1434_the_architecture_census"):
        assert "536 manifolds" in open(os.path.join(ROOT, "frontier", d, "ADDENDUM_2026-10-02_the_unit_is_word_states.md")).read()
    v = json.load(open(os.path.join(A, "arc_verdict.json")))
    assert v["verdict"] == "PROVED" and v["scope"]["reach"] == "general"
