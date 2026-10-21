"""B1690 -- GENESIS §5's F-FC column, sm:B1523 and B1652's FAILS cells on main (P-229): live, the free-cusp census and the
parity on the controls and on two of B1186's members (o10_150688's cusp open; o10_150684's closed only by orientation-
reversing isometries), the bite (with the sign +1 the identity closes every free cusp, o10_150688's included); live,
rigidity rel cusp at 60 digits on two word states and W81/W83's branching and commutants; stored, the 112, the 758 word
states, the 536 manifolds' rigidity and mirror census, W76's 8 798 threads and W74's identities."""
import importlib.util, io, contextlib, json, pathlib, sys
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1690_free_cusps_rigidity_and_the_tribunal_cells" / "verification"
sys.path.insert(0, str(A))


def _load(name):
    spec = importlib.util.spec_from_file_location(name + "_lock", A / (name + ".py"))
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def _j(name): return json.loads((A / name).read_text(encoding="utf-8"))


def test_free_cusps_and_parity_live_with_the_bite():
    m = _load("main_ffc")
    w = m.analyse("m129"); b = m.analyse("L6a4")
    assert (w["b1"], w["ranks"], w["aut"]) == (2, [1, 1], 8) and (b["b1"], b["ranks"], b["aut"]) == (3, [1, 1, 1], 48)
    o = m.analyse("o10_150688")
    assert o["cusps"] == 1 and o["b1"] == 2 and o["open_free_cusps"] == [0]
    r = m.analyse("o10_150684")
    assert r["open_free_cusps"] == [] and all(v["orientation_preserving"] == 0 for v in r["parity"].values())
    m.SIGN = +1                                                           # the bite: g = +1 is satisfied by the identity
    try:
        assert m.analyse("o10_150688")["open_free_cusps"] == []
    finally:
        m.SIGN = -1


def test_free_cusps_stored():
    s = _j("main_ffc_family.json")["summary"]
    assert (s["members"], s["with_free"], s["free_cusps"], s["members_closed"]) == (112, 35, 83, 108)
    assert sorted(map(tuple, s["open"])) == [("o10_150688", 0), ("o10_150708", 0), ("o10_150716", 0), ("o10_150725", 1)]
    words = _j("main_ffc_words.json")
    assert words["n"] == 758 and words["exceptions"] == []
    x = _j("main_s5_extra.json")
    assert all(l["cusps"] == 1 and l["b1"] == 1 for l in x["m004_levels"])
    assert x["m004_covers_le10"]["n"] == 88 and x["m004_covers_le10"]["with_hex_cusp"] == 14 and x["m003_hexagonal"] and not x["m004_hexagonal"]


def test_rigidity_live_and_stored():
    m = _load("rigidity_mp")
    for st in ("b++LLLLLR", "b++LLRLRRLLRRLR"):
        r = m.rigidity(st)
        assert r["rigid"] and r["h1_v"] == 1 and r["max_dropped"] < 1e-40 < r["min_kept"]
    s = _j("main_b1523_rigidity.json")["summary"]
    assert s["manifolds"] == 536 and s["rigid"] == 536 and s["h1_v"] == {"1": 536} and s["max_dropped"] < 1e-40 < s["min_kept"]
    mi = _j("main_b1523_mirror.json")["summary"]
    assert (mi["states"], mi["manifolds"], mi["mirror_broken"], mi["broken_chiral"], mi["broken_with_orientation_reversing"],
            mi["states_on_broken"]) == (758, 536, 262, 220, 42, 482)
    assert mi["broken_by_sign"] == {"+": 131, "-": 131}
    assert list(mi["broken_by_length_manifolds"].values()) == [2, 2, 8, 14, 36, 62, 138]


def test_tribunal_cells():
    with contextlib.redirect_stdout(io.StringIO()):
        d = _load("main_w81_w83").out
    assert d["commutant_dim"] == 35 and d["commutant_cartan_is_A5"] and d["centraliser_of_A2_roots"] == 72
    assert (d["Y_dim_moves_through_O"], d["Y_dim_through_S3"], d["Y_dim_trivial"]) == (0, 1, 8)
    assert d["W81_SU2q_multiplicities_by_dim"] == {"1": 55, "2": 52, "3": 27, "4": 2} and d["W81_rhoQ_multiplicity_on_Q8"] == 56
    w76 = _j("main_w76.json")["summary"]
    assert w76["threads"] == 8798 and w76["mirror_symmetric"] == 248 and w76["bits"] == {"0": 248, "0.5": 0, "neither": 0}
    w74 = _j("main_w74.json")
    assert w74["CLC_is_Linv"] and w74["CPC_is_P"] and w74["S_condition_rhoprime_5/2"]
    assert w74["S_condition_rhoR"] == {"-1/2": True, "3/2": True, "7/2": True, "1/2": False, "1": False}
    assert w74["Y_max_abs_im_over_max_abs"] < 1e-12 and abs(w74["arg_det_YY_over_pi"]) < 1e-12
