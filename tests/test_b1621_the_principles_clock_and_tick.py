"""B1621 -- THE PRINCIPLE'S CLOCK AND TICK ON THE MATTER: the sealed instrument unchanged; the clock within the grading
(diagonal span, zero mean); the tick breaking it (rank-one democratic mean); equal masses from its means on forms under
every tensor; the leptons' heaviest state never the tick's."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1621_the_principles_clock_and_tick_on_the_matter"


def test_sealed_and_recorded():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at bded4d62e: ")
    assert hashlib.sha256(open(ARC / "verification" / "clock_and_tick.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "clock_and_tick.json"))
    k1 = d["K1"]
    assert k1["inner_lifts_diagonal_in_parity_basis"] and k1["inner_lifts_commute"] and k1["prefix_product_equals_diag_chi_to_N1"]
    assert sorted(map(tuple, k1["line_characters_(a,b)"])) == [(-1.0, -1.0), (-1.0, 1.0), (1.0, -1.0)]
    assert d["K2"]["span_is_the_diagonal_algebra"] and d["K3"]["max_abs_mean"] < 1e-3
    t1 = d["T1"]
    assert t1["eigen_turns"] == [0.0, 0.333333, 0.666667] and t1["cyclic"] and t1["order_on_T"] == 3
    t2 = d["T2"]
    assert t2["rank"] == 1 and not t2["commutes_with_the_clock"]
    assert all(abs(x - 1 / 3) < 1e-5 for row in t2["entry_moduli_in_parity_basis"] for x in row)
    for t in ("Tbar_x_T", "T_x_T", "Sym2_T"):
        assert d["T3"][t]["degenerate_or_zero"] and d["T3"][t]["max_singular_value"] > 1e-3   # equal, not zero
    p2 = d["P2"]
    assert not p2["tau_row_trimaximal_inside_3sigma"] and not p2["nu3_column_trimaximal_inside_3sigma"]
    assert [k for k, v in p2["every_row_and_column"].items() if v] == ["col_2"]               # bite: one placement passes
