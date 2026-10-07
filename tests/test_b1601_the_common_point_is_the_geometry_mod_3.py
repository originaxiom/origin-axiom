"""B1601 -- THE COMMON POINT IS THE GEOMETRY MOD 3: the sealed census and the lemma as recorded, and the two harvest
controls on the forced cover (B1600's addendum) against the SM seat's census cells."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1601_the_common_point_is_the_geometry_mod_3" / "verification"
B1600 = HERE.parents[1] / "B1600_the_weave_verified" / "verification"


def test_the_lemma_as_recorded():
    d = json.load(open(HERE / "linear_part_8.json"))
    s = d["summary"]
    assert d["L_R_linear_parts_as_tabled"] and s["max_length"] == 8 and s["odd"] == 16 and s["even"] == 21
    assert s["all_det_one"] and s["odd_all_body_diagonal"] and s["odd_all_isotropic"]
    assert s["even_isotropic"] == ["LLLLRRRR"] and s["even_identity"] == ["LLLLRRRR"]


def test_odd_trace_meets_the_common_point_at_one_prime_of_norm_three():
    rows = json.load(open(HERE / "meets_odd_8.json"))
    assert len(rows) == 16 and all(r["trace"] % 2 == 1 for r in rows)
    for r in rows:
        assert r["geometric_hits"] >= 1 and len(r["geometric_components"]) == 1, r["word"]
        assert r["integral"], r["word"]
        assert r["norm"] == 3 and len(r["primes"]) == 1 and (r["primes"][0]["p"], r["primes"][0]["f"], r["primes"][0]["e_in_ideal"]) == (3, 1, 1), (r["word"], r["norm"], r["primes"])
        assert all(v == 1 for v in r["primes"][0]["valuations"].values())


def test_even_trace_never_meets_it_above_three():
    rows = json.load(open(HERE / "meets_even_8.json"))
    assert len(rows) == 21 and all(r["trace"] % 2 == 0 for r in rows)
    split = {"LLLRLRLR", "LLLRRLRR"}          # the geometric point's sign orbit spans two mirror factors, same ideal (FINDINGS M4)
    for r in rows:
        assert r["geometric_hits"] >= 1 and len(r["geometric_components"]) == (2 if r["word"] in split else 1) and r["integral"], r["word"]
        assert r["norm"] % 3 != 0 and r["norm"] in (4, 8, 64, 1024) and all(p["p"] == 2 for p in r["primes"]), (r["word"], r["norm"], r["primes"])
    assert next(r for r in rows if r["word"] == "LLLLRRRR")["norm"] == 1024


def test_the_seats_census_cells_on_main_forced_cover():
    for name, chars, members, structures in (("b++LR", 64, 24, [[1, 0, 1]]), ("b+-LR", 16, 6, [[4, 0, 4]]), ("b++LLLR", 16, 0, []), ("b+-LLLR", 64, 0, [])):
        d = json.load(open(B1600 / f"forced_cover_{name}.json"))
        assert d["cover_cusps"] == 4 and abs(d["cover_volume_ratio"] - 12) < 1e-9 and d["forced_candidates"] >= 1
        assert d["members"] == members and d["member_structures"] == structures, name
        if chars:
            assert d["sign_characters"] == chars, name
