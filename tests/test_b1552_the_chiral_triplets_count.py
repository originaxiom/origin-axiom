"""sm:B1552 THE CHIRAL TRIPLET'S COUNT -- the lock on the banked record (reads only; writes nothing tracked).

The seal's hashes, the complete record (432 readings per route), the read-out's verdict, and the counts: every reading
(0, 0), the two routes and the draws agreeing.
"""
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1552_the_chiral_triplets_count"
VER = ARC / "verification"
SEAL_SHA = "556910b631c715867352057dad3401a50b41e949c077bdcf9ef58178f0c20e69"


def _rows(route):
    with gzip.open(VER / f"run_{route}.jsonl.gz", "rt") as f:
        return [json.loads(line) for line in f]


def test_seal_hash():
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEAL_SHA


def test_artifact_hashes():
    for line in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, name = line.split()
        assert hashlib.sha256((ARC / name).read_bytes()).hexdigest() == digest, name


def test_record_complete():
    for route in (1, 2):
        rows = _rows(route)
        done = {r["state"] for r in rows if r.get("done")}
        readings = [r for r in rows if "count" in r]
        assert len(done) == 12 and len(readings) == 432, (route, len(done), len(readings))


def test_every_count_zero_and_routes_agree():
    c1 = Counter(tuple(r["count"]) for r in _rows(1) if "count" in r)
    c2 = Counter(tuple(r["count"]) for r in _rows(2) if "count" in r)
    assert c1 == c2 == Counter({(0, 0): 432})


def test_read_out_verdict():
    d = json.loads((VER / "read_out.json").read_text(encoding="utf-8"))
    assert d["complete"] and d["P1"] and d["P2"] and d["P3"] and d["P4"]
    assert not any(v for m in d["P5"].values() for v in m.values())
    assert d["verdict"] == "NEGATIVE as sealed"


def test_identity_held():
    d = json.loads((VER / "identity.json").read_text(encoding="utf-8"))
    assert d["all held"] is True and d["I1"]["counts"] == [[-1, -1], [-1, -1]]


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1552" and d["verdict"] == "NEGATIVE" and d["instrument"] is False
    assert "|" not in d["claim_one_line"]


def test_w11_the_zero_is_a_theorem_checked():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_spin_zero.json").read_text(encoding="utf-8"))
    assert d["all held"] is True
    assert d["(1) T2 on sm:B1552's record"]["readings"] == 864
    assert d["(2) the act on V is in a finite group, every state to length 12"]["states"] == 758


def test_w12_the_joined_vacuum_has_no_interior_class():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_joined_vacuum.json").read_text(encoding="utf-8"))
    t = d["tally"]
    assert d["all held"] is True and t["(state, tick)"] >= 24
    assert t["readings with a class"] == t["n = 0 there"] == t["h1 = r1 = h0(T; A) there"] > 0


def test_w13_main_b1434_orbits_of_three_verified():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_class_index_orbits.json").read_text(encoding="utf-8"))
    assert d["all agree with B1434"] and d["every background in a deck orbit of three"]
    assert d["every count one in absolute value"] and d["signs split equally"]
    assert len(d["the states (odd trace, in B1434's range; the engine route), tick 3"]) == 4


def test_w14_the_slope_law_and_the_census():
    D = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((D / "the_slope_law.json").read_text(encoding="utf-8"))
    assert d["the law held at every candidate"] and d["every in-range row agrees with B1434"]
    assert d["(3) every class paired with its opposite"]
    rows = d["(2) the census, every odd-trace state to length 6, tick 3"]
    assert all(r["the parities"]["firing modules with a parity as the extension character"] == 0 for r in rows.values())
    assert sorted(k for k, r in rows.items() if r["the parities"]["their slope class has"] != 3) == ["+LLLRRR", "+LLRLRR"]
    assert len(rows) == 12
    assert sorted(k for k, r in rows.items() if r["generation_shaped"] == 0) == ["+LLRLRR", "-LLRLRR"]
    sample = json.loads((D / "the_slope_law_sample.json").read_text(encoding="utf-8"))
    assert sample["all agree"] and sample["sampled"] == 300 and sample["firing by the law"] > 0


def _trace(sw):
    """the trace of a signed word's matrix, L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]] (GENESIS §2)"""
    a, b, c, d = 1, 0, 0, 1
    for ch in sw[1:]:
        if ch == "L":
            a, b, c, d = a, a + b, c, c + d
        else:
            a, b, c, d = a + b, b, c + d, d
    return (a + d) * (1 if sw[0] == "+" else -1)


def test_w15_the_hand_theorem():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_hand_theorem.json").read_text(encoding="utf-8"))
    assert all(d["summary"].values()), d["summary"]
    assert d["(iv) det on T by generator (eighths, the two lifts)"] == {"L": [1, 5], "R": [3, 7], "-I": [2, 6]}
    direct = d["(iii) the direct tick-3 act, every odd-trace state to length 8 (both signs)"]
    assert direct["odd-trace states read"] == 32 == direct["tick-3 act = det(w|T) I on T"]
    hand = d["(v) the hand rule from the determinant, GENESIS's states to length 12"]
    assert hand["odd trace"] == 326 == hand["agrees with n_L - n_R + 2[sign -] = 2 mod 4"]
    assert hand["odd-trace words"] == 163 == hand["odd-trace words with exactly one twin apart"]


def test_w15_the_weaves_own_extensions_and_the_mod_16_law():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_weave_extension.json").read_text(encoding="utf-8"))
    summ = dict(d["summary"])
    summ.update(d["(c) length 8, reduced rule"]["summary"])
    assert len(d["summary"]) == 12 and len(d["(c) length 8, reduced rule"]["summary"]) == 20
    for sw, v in summ.items():
        assert v["readings"] > 0
        assert set(v["values"]) <= {1}                                # every firing reading is +1
        assert v["non-zero"] in (0, v["readings"])                     # three or nothing: all or none
        silent = v["non-zero"] == 0
        assert silent == (_trace(sw) % 16 in (1, 15)), sw              # the mod-16 law
    assert sorted(k for k, v in summ.items() if v["non-zero"] == 0) == ["+LLLLLRRR", "+LLRLRR", "-LLLLLRRR", "-LLRLRR"]
    for prime, rows in d["(b) two further primes"].items():
        assert rows["+LR"]["non-zero"] == rows["+LR"]["readings"] and rows["+LLRLRR"]["non-zero"] == 0, prime


def test_w15_the_prediction_recorded_and_its_second_part_failed():
    D = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    assert "t ≡ ±1 (mod 16)" in (D / "W15_PREDICTION.md").read_text(encoding="utf-8")
    d = json.loads((D / "the_prediction_test.json").read_text(encoding="utf-8"))
    assert d["the control carries some"] and not d["the predicted silent states carry none"] and not d["the prediction holds"]
    assert {s: r["generation_shaped"] for s, r in d["rows"].items()} == {"+LLLLLRRR": 3064, "-LLLLLRRR": 336,
                                                                         "+LLLLLLLR": 480, "-LLLLLLLR": 336}


def test_w15_the_weaves_five_is_not_generation_shaped():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_weaves_five.json").read_text(encoding="utf-8"))
    for sw, v in d["summary"].items():
        pairs = {tuple(x) for x in v["pairs for W"]}
        dual = {tuple(x) for x in v["pairs for W*"]}
        if sw in ("+LLRLRR", "-LLRLRR"):
            assert pairs == dual == {(0, 0)}, sw
        else:
            assert pairs <= {(1, 3), (2, 3)} and dual <= {(-1, -3), (-2, -3)} and (1, 3) in pairs, sw
        assert all(p[0] != p[1] for p in pairs | dual if p != (0, 0))   # never the shape n_5bar = n_10

# main's B1601 census (main's frontier/B1601_the_common_point_is_the_geometry_mod_3/verification/census_*_8_run.txt,
# cited): word -> (trace, degree of K, norm of (x, y, z), [(p, residue degree, exponent)])
MAIN_B1601 = {
    "LR": (3, 2, 3, [(3, 1, 1)]), "LLLR": (5, 4, 3, [(3, 1, 1)]), "LLLLLR": (7, 6, 3, [(3, 1, 1)]),
    "LLLRLR": (13, 8, 3, [(3, 1, 1)]), "LLLRRR": (11, 8, 3, [(3, 1, 1)]), "LLRLRR": (15, 14, 3, [(3, 1, 1)]),
    "LLLLLLLR": (9, 8, 3, [(3, 1, 1)]), "LLLLLRLR": (19, 12, 3, [(3, 1, 1)]), "LLLLLRRR": (17, 12, 3, [(3, 1, 1)]),
    "LLLLRLRR": (25, 24, 3, [(3, 1, 1)]), "LLLLRRLR": (25, 24, 3, [(3, 1, 1)]), "LLLRLLRR": (29, 28, 3, [(3, 1, 1)]),
    "LLLRLRRR": (27, 26, 3, [(3, 1, 1)]), "LLLRRLLR": (29, 28, 3, [(3, 1, 1)]), "LLRLLRLR": (37, 12, 3, [(3, 1, 1)]),
    "LLRLRLRR": (39, 38, 3, [(3, 1, 1)]),
    "LLR": (4, 4, 8, [(2, 1, 3)]), "LLRR": (6, 8, 64, [(2, 1, 6)]), "LLLLR": (6, 6, 4, [(2, 1, 2)]),
    "LLLRR": (8, 8, 8, [(2, 1, 3)]), "LLRLR": (10, 8, 4, [(2, 1, 2)]), "LLLLRR": (10, 12, 64, [(2, 1, 6)]),
    "LLLLLLR": (8, 8, 8, [(2, 1, 3)]), "LLLLLRR": (12, 12, 8, [(2, 1, 3)]), "LLLLRLR": (16, 12, 8, [(2, 1, 3)]),
    "LLLLRRR": (14, 12, 4, [(2, 1, 2)]), "LLLRLLR": (18, 14, 4, [(2, 1, 2)]), "LLLRLRR": (20, 20, 8, [(2, 1, 3)]),
    "LLLRRLR": (20, 20, 8, [(2, 1, 3)]), "LLRLLRR": (22, 12, 4, [(2, 1, 2)]), "LLRLRLR": (26, 14, 4, [(2, 1, 2)]),
    "LLLLLLRR": (14, 16, 64, [(2, 3, 2)]), "LLLLRLLR": (22, 20, 64, [(2, 1, 6)]),
    "LLLLRRRR": (18, 16, 1024, [(2, 1, 10)]), "LLLRLRLR": (34, 14, 4, [(2, 1, 2)]),
    "LLLRRLRR": (30, 12, 4, [(2, 1, 2)]), "LLRLRRLR": (38, 24, 64, [(2, 1, 6)]),
}


def test_w16_main_b1601_verified_on_every_word():
    """W16: the ideal (tr a, tr b, tr ab) at the geometric point, on all 37 geometries to length 8, by this seat's route
    (Newton at 1200 digits or more, the field and coordinates checked exactly, the ideal read at the primes of the
    norm gcd), against main's census row by row"""
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_common_point_mod_3.json").read_text(encoding="utf-8"))
    rows = {r["word"]: r for r in d["rows"]}
    assert set(rows) == set(MAIN_B1601) and d["main's law holds on every word"] and d["failed"] == []
    assert (d["odd-trace words"], d["even-trace words"]) == (16, 21)
    for w, (tr, deg, norm, primes) in MAIN_B1601.items():
        r = rows[w]
        assert r["exactly a fixed point on the cusp surface"] and all(r["x, y, z integral"]), w
        assert (r["trace"], r["degree of K"], r["norm of (x, y, z)"]) == (tr, deg, norm), w
        assert [(p["p"], p["residue degree"], p["exponent"]) for p in r["prime factors"]] == primes, w
        assert r["Newton residual (log10)"] < -500, w
        if tr % 2:
            assert r["prime factors"][0]["valuations of x, y, z"] == [1, 1, 1], w
            assert r["their gcd"] % 3 == 0 and r["order maximal at"] and 3 in r["order maximal at"], w


def test_w17_the_weaves_five_on_the_thread_reads_one_generation_on_the_vector_like_twins():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_weaves_five_tick1.json").read_text(encoding="utf-8"))
    summ = d["summary"]
    assert len(summ) == 32 and sum(v["readings"] for v in summ.values()) == 480
    shapes = Counter()
    for sw, v in summ.items():
        nL, nR = sw.count("L"), sw.count("R")
        vector_like = (nL - nR + (2 if sw[0] == "-" else 0)) % 4 == 0      # Theorem H's twin
        silent = _trace(sw) % 16 in (1, 15)                                  # W15's mod-16 law
        expect = (0, 0) if silent else ((1, 1) if vector_like else (0, 1))
        assert [tuple(x) for x in v["pairs for W"]] == [expect], sw
        assert [tuple(x) for x in v["pairs for W*"]] == [(-expect[0], -expect[1])], sw
        shapes[expect] += 1
    assert shapes == {(1, 1): 14, (0, 1): 14, (0, 0): 4}



def test_w18_the_five_on_each_parity_line_the_prediction_failed_at_special_classes():
    """W18: the five's sectors on the forced A4 cover (Shapiro). Predictions 2-5 held; 1 failed: on four carriers of sign
    minus the second basis class reads (0, 1) on each parity line; the generic class reads (1, 1) on every carrier"""
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_parity_generations.json").read_text(encoding="utf-8"))
    pred = d["the predictions"]
    assert [pred[k] for k in sorted(pred)] == [False, True, True, True, True]
    assert sorted(len(v) for v in d["by kind"].values()) == [4, 14, 14]
    mixed = set()
    for sw, st in d["states"].items():
        rows = st["rows (route A)"]
        assert len(rows) == st["readings (route A)"]
        nL, nR = sw.count("L"), sw.count("R")
        vector_like = (nL - nR + (2 if sw[0] == "-" else 0)) % 4 == 0
        silent = _trace(sw) % 16 in (1, 15)
        kind = "mod-16 word" if silent else ("carrier" if vector_like else "chiral twin")
        assert st["kind"] == kind, sw
        for r in rows:
            p = tuple(r["W"]["P"])
            if kind == "carrier":
                if r["class"] == "basis 1" and p == (0, 1):
                    mixed.add(sw)
                    assert tuple(r["W"]["forced cover"]) == (1, 6)
                else:
                    assert p == (1, 1) and tuple(r["W"]["forced cover"]) == (4, 6), (sw, r["class"])
            elif kind == "chiral twin":
                assert p == (0, 2) and tuple(r["W"]["forced cover"]) == (0, 9), sw
            else:
                assert p == (0, 0) and tuple(r["W"]["forced cover"]) == (0, 0), sw
            assert tuple(r["W*"]["P"]) == (-p[0], -p[1]), sw
        if "route B (tick 3)" in st:
            assert st["route B: the three parities alike"] and st["route B agrees with route A (Shapiro)"], sw
    assert mixed == {"-LLLR", "-LLLRLR", "-LLLLLLLR", "-LLLLRRLR"}
    assert sum("route B (tick 3)" in st for st in d["states"].values()) == 12


def test_w18_post_hoc_two_special_classes_on_every_carrier():
    """W18, post hoc: on the whole projective line of gluing classes, every carrier has exactly two classes at which each
    parity line's pair drops to (0, 1), at GF(73) and GF(97); the engine's basis met one of them on four carriers"""
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_parity_generations_special.json").read_text(encoding="utf-8"))
    rows = d["rows"]
    assert len(rows) == 28 and {r["p"] for r in rows} == {73, 97}
    for r in rows:
        assert r["classes read"] == r["p"] + 1
        assert r["I(W (x) P) tally"] == {"1": r["p"] - 1, "0": 2}, r["state"]
        assert [x["pair"] for x in r["the special classes"]] == [[0, 1], [0, 1]], r["state"]
    assert d["two special classes on every carrier at both primes"] and d["every special class reads (0, 1)"]
    assert d["the basis met a special class (s = inf) on"] == ["-LLLLLLLR", "-LLLLRRLR", "-LLLR", "-LLLRLR"]


def test_w20_the_weaves_count_in_e6_is_three_on_the_weave():
    """W20: -chi(Aut+(F2); 27) under every SL(2) in E6; three through the principal and every distinguished sl2; the
    census validated by E6's orbit dimensions and by two routes (the amalgam and Eichler-Shimura)"""
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_weaves_count_in_e6.json").read_text(encoding="utf-8"))
    assert d["the orbits' dimensions match E6's list"] and d["the two routes agree for every k to 60"]
    assert d["the routes agree on every orbit"] and len(d["rows"]) == 21
    count = d["-chi(G; 27) by orbit"]
    assert count["E6"] == count["E6(a1)"] == count["E6(a3)"] == 3
    assert d["rows"]["E6"]["27 = (k: multiplicity of Sym^k)"] == {"0": 1, "8": 1, "16": 1}
    assert d["the distinguished even diagrams (Bourbaki order)"]["E6(a1)"] == [2, 2, 2, 0, 2, 2]
    assert sorted(d["orbits with -chi(G; 27) = 3"]) == ["A4", "D4(a1)", "D5", "E6", "E6(a1)", "E6(a3)"]
    assert sum(1 for v in count.values() if abs(v) == 3) == 13
    assert all(r["27-bar the same"] for r in d["rows"].values())
    assert {d["rows"][n]["-chi(G; 78), route A"] for n in ("E6", "E6(a1)", "E6(a3)")} == {16}
    assert d["the SU(5) frame's principal counts (5, 10)"] == {"5": {"A": 1, "B": 1}, "10": {"A": 2, "B": 2}}
    # h1(SL(2, Z); Sym^k) is dim M_{k+2} + dim S_{k+2} for even k >= 2 (Eichler-Shimura): 3 at k = 16, 1 at k = 8
    h1 = d["h1(SL(2, Z); Sym^k), k = 0..24"]
    assert (h1["16"], h1["8"], h1["0"]) == (3, 1, 0)
