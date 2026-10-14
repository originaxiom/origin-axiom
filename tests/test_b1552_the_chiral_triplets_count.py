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


def test_w20_the_third_route_the_orbifold_index():
    """W20, third route: Brown's formula over the elliptic elements of SL(2, Z) (traces at the square and hexagonal tori)
    agrees with the amalgam and Eichler-Shimura on all 21 orbits; on every distinguished orbit tr(S) = 3, tr(U) = 0"""
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_weaves_count_orbifold.json").read_text(encoding="utf-8"))
    assert d["agrees with W20's two routes on all 21 orbits"]
    for name, r in d["the distinguished orbits"].items():
        t = r["traces on the 27 at the elliptic elements"]
        assert r["-chi(G; 27), Brown"] == 3, name
        assert (round(t["S"]), round(t["U"]), round(t["U^2"]), round(t["-I"])) == (3, 0, 0, 27), name


def test_w21_the_holomorphic_triplet_is_t():
    """W21: the recorded read-out (every control held; Q positive definite on T, negative on T-bar; one line per parity;
    T = mu (x) 3' through PSL(2, Z/4) = S4), and the controls and the sign recomputed in process (nothing written)"""
    import sys
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_holomorphic_triplet.json").read_text(encoding="utf-8"))
    assert d["controls"]["every control holds"]
    r = d["read-out"]
    assert r["(1) the holomorphic triplet (Q > 0)"] == "T"
    assert r["(1) Q on the triplets"]["T"]["sign"] == "+" and r["(1) Q on the triplets"]["T-bar"]["sign"] == "-"
    assert r["(1) the holomorphic triplet's rank in each parity's block"] == [1, 1, 1]
    assert sorted(x["(2) mu = chi_eta^j, j (mod 24)"] for x in r["per braid-consistent lift choice"]) == [9, 21]
    for x in r["per braid-consistent lift choice"]:
        assert x["(3) Z on the holomorphic triplet (turns)"] == 0.75
        assert x["(4) P = mu^-1 T_hol: order of its group"] == 24 and all(x["(4) P(L)^4 = 1, P(S)^2 = 1, (P(S) P(L))^3 = 1"])
    assert r["(4) P is S4's"].startswith("3'")
    sys.path.insert(0, str(here))
    import the_holomorphic_triplet as HT
    c = HT.controls()
    assert c["every control holds"]
    named, _ = HT.triplets()
    G = HT.gram_V()
    assert all(np.linalg.eigvalsh(named["T"].conj().T @ G @ named["T"]) > 1e-9)
    assert all(np.linalg.eigvalsh(named["T-bar"].conj().T @ G @ named["T-bar"]) < -1e-9)


def test_w21_second_route_the_actual_periods():
    """W21, second route (after the read-out): the holomorphic twisted forms theta_3(z | 2 tau) / sqrt(theta_1(z | tau))
    and their parity conjugates have periods spanning T at three tau, the same subspace each time; theta_3 alone has
    rho_Q's monodromy; Q on them is positive; the twisted Riemann bilinear relation holds"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_holomorphic_triplet_periods.json").read_text(encoding="utf-8"))
    assert d["the holomorphic subspace is T at every tau"] and d["the holomorphic subspace is the same at every tau"]
    assert d["theta_3(z | 2 tau) alone gives the monodromy at every tau"]
    assert d["the twisted Riemann bilinear relation at the first tau (relative error)"] < 1e-9
    assert len(d["rows"]) == 3
    for r in d["rows"]:
        assert all(e > 0 for e in r["Q on the holomorphic forms (eigenvalues)"])
        assert r["Q on the spin doublet's holomorphic form"] > 0


def test_w22_the_end_condition_the_weave_fixes():
    """W22: the lifts of L and R generate 2O (order 48), irreducible on the puncture's local solutions; the moves fixing
    any one parity act irreducibly too (order 16); one thread alone leaves a line; the odd spin structure is the only
    one every move fixes"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_puncture_condition.json").read_text(encoding="utf-8"))
    assert d["(1) the group of the lifts of L and R: order"] == 48
    assert d["(1) its commutant on the local solutions C^2 (1 = irreducible)"] == 1
    for b in d["(2) each parity block's stabilizer"].values():
        assert b["commutant on C^2"] == 1 and b["order of the group they generate"] == 16
    t = d["(3) threads to length 6 whose every lift has two distinct eigenlines (a line a vector-like condition can use)"]
    assert t["threads"] == 50 and t["with distinct eigenlines"] == 46
    assert d["(4) the fixed one is odd (Arf 1)"] and d["(4) fixed by every move"] == ["(1, 1)"]
    assert d["the weave fixes the condition up to the hand (Lambda_+ = 0 or C^2 in every block; index -3 or +3)"]


def test_w23_the_e8_frames_on_the_fibre():
    """W23: with W22's condition, every SU(n) bundle built from the common point's blocks gives at most one chiral 27
    (E6), two 16s (SO(10)), or SU(5)'s (1, 3) or (2, 2): never three complete generations; the weave's five reads (1, 3)"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_e8_frames_on_the_fibre.json").read_text(encoding="utf-8"))
    assert d["the most complete chiral generations each frame gives"] == {"E6": 1, "SO(10)": 2, "SU(5)": 2}
    assert not d["three complete generations in any of these frames"]
    assert set(d["SU(5) (10 with W, 5-bar with Lambda^2 W): (N(10), N(5-bar)) -> bundles"]) == {"(0, 0)", "(1, 3)", "(2, 2)"}
    assert d["the weave's five D + P (F-HE, W17): (N(10), N(5-bar))"] == [1, 3]
    assert d["SU(5) anomaly of the weave's five's bulk modes (N(10) - N(5-bar))"] == -2


def test_w24_the_six_dimensional_census():
    """W24 (the rule committed first): the character variety is forced but has no count; E^3/G gives 48, 16, 14, never
    three; W = rho_Q (x) C^3 with Q8's centraliser in E8 of dimension 55 (F4 x SU(2)), by two branchings; W21's triplet
    is the tangent space at the common point; and the audit of W22 (D0): the moves alone keep four end conditions, index
    -3, -1, +1, +3 (odd, never 0), and with the parity grading only +-3. The gauge-side numbers are recomputed in process"""
    import sys
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_six_dimensional_census.json").read_text(encoding="utf-8"))
    A, B, D = d["A the character variety"], d["B the local model at the common point"], d["D the gauge side"]
    assert A["A1 L and R preserve Omega = dx dy dz (Jacobian +1); P reverses it (-1)"]
    assert all(v["equals the record's table"] and v["preserves kappa"] for v in A["A1 the moves on the character variety"].values())
    assert A["A2 the points L and R both fix"] == [[0, 0, 0], [2, 2, 2]]
    assert A["A3 their group: order"] == 24 and A["A3 the same triplet (W21's flavour triplet is the tangent space at the common point)"]
    assert A["A4 Euler characteristic of the level sets (9 - nodes - 3)"] == {"generic": 6, "-2": 5, "2": 2}
    assert A["A4 consistent (no contribution from infinity)"]
    assert B["B1 on X_-2 each parity fixes only the common point"]
    assert B["B2 signed permutations preserving kappa: order"] == 24 and B["B2 ... with determinant 1: order"] == 12
    assert B["B2 ... the linear 3-cycle (x, y, z) -> (y, z, x)"]
    assert [v[0] for v in B["B3 the lifts to SU(2) (order; Du Val type by McKay)"].values()] == [8, 24, 48]
    b4 = B["B4 E^3 / G, any elliptic curve E"]
    assert [b4[k]["chi_orb"] for k in b4] == ["96", "32", "28"]
    assert [b4[k]["chi_orb with discrete torsion"] for k in b4] == ["-96", "-32", "-28"]
    assert not B["B4 three among them"]
    assert D["D0 commutant of the moves' lifts on the six local solutions"] == 2
    assert D["D0 the conditions every move keeps and their indices"] == [-3, -1, 1, 3]
    assert sorted(p["dimension"] for p in D["D0 the invariant pieces"]) == [2, 4]
    assert not any(p["a sum of parity blocks"] for p in D["D0 the invariant pieces"])
    assert D["D0 with the parity grading added: commutant"] == 1
    assert D["D1 every parity block is the spin doublet (W = rho_Q (x) C^3)"]
    assert D["D2 the two routes agree"] and D["D2 the centraliser's dimension (multiplicity of the trivial representation)"] == "55"
    assert D["D3 multiplicity of rho"] == "56" and D["D3 multiplicity of each parity character"] == "27"
    assert d["E the verdict"]["none passes"]
    # recomputed in process: the audit's commutants
    sys.path.insert(0, str(here))
    import the_six_dimensional_census as SC
    import the_common_point as CP
    lifts = [SC.blocks_action(CP.AUT[m], g) for m in ("L", "R") for g in CP.extend(CP.AUT[m])]
    assert SC.commutant(lifts, 6)[0] == 2
    grading = [np.kron(np.diag([SC.chi_word(u, [gen]) for u in SC.CT.PAR]), np.eye(2)) for gen in (1, 2)]
    assert SC.commutant(lifts + grading, 6)[0] == 1


def test_w25_the_weaves_bundles_are_self_conjugate():
    """W25 (the rule committed first): Q8's irreducibles are real or quaternionic; the weave's group on the six local
    solutions (order 192) is irreducible and quaternionic; T and T-bar are complex, the parity triplet real; centralisers
    in E8: Q8 55, one parity's element 82 (contains E6), the odd-trace extension 25 with omega fifteen times. The
    centraliser dimensions are recomputed in process from the characters"""
    import sys
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_self_conjugate_weave.json").read_text(encoding="utf-8"))
    f1 = d["F1 Frobenius-Schur indicators of the fibre's holonomy (Q8): +1 real, -1 quaternionic, 0 complex"]
    assert f1["rho_Q (the spin doublet)"] == -1.0 and f1["trivial"] == 1.0
    assert all(f1[k] == 1.0 for k in f1 if k.startswith("parity"))
    f2 = d["F2 the group on the six local solutions (moves' lifts, holonomy, grading)"]
    assert f2 == {"order": 192, "commutant (1 = irreducible)": 1, "Frobenius-Schur indicator": -1.0}
    f3 = d["F3 Frobenius-Schur indicators on the cohomology and the tangent space"]
    assert f3["order on V"] == 96 and f3["T"] == 0.0 and f3["T-bar"] == 0.0
    assert f3["the parity triplet (the moves' linear parts at the common point, the cube's rotations)"] == 1.0
    f4 = d["F4 centralisers in E8 (dimensions by characters)"]
    assert f4["Q8 (W's holonomy, all three parities)"]["centraliser dimension"] == 55.0
    assert f4["one parity's element alone, <W(a)>"]["centraliser dimension"] == 82.0
    ext = f4["the odd-trace extension: Q8 with the order-3 move's lift"]
    assert ext["order"] == 24 and ext["centraliser dimension"] == 25.0
    assert ext["multiplicity of the complex character omega (trivial on Q8)"] == 15.0
    assert all(d["F5 the verdict"].values())
    sys.path.insert(0, str(here))
    import the_self_conjugate_weave as SCW
    Q8 = SCW.closure([SCW.SC.W_of([1]), SCW.SC.W_of([2])], 6)
    assert SCW.average(Q8)[0] == 55.0
    assert SCW.average(SCW.closure([SCW.SC.W_of([1])], 6))[0] == 82.0


def test_w26_the_weave_is_mirror_symmetric():
    """W26 (the rule committed first): the weave is closed under the mirror (exact, 224 words to length 10); every
    thread to length 6 and its mirror have the same volume and opposite CS (SnapPy, recorded); the order-3 orientation
    flips at every tick on all 98 odd-trace words. The exact parts are recomputed in process"""
    import sys
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_weaves_mirror.json").read_text(encoding="utf-8"))
    n1 = d["N1 the weave is closed under the mirror"]
    assert n1["cyclic primitive words with both letters, to length 10"] == 224
    assert n1["S phi^-1 S^-1 = matrix of reverse(phi) with L <-> R, for every one"]
    assert n1["reverse(phi) = (P S) phi^-1 (P S)^-1, so M_reverse(phi) = M_phi"]
    assert n1["amphichiral (phi' or swap(phi) a rotation of phi)"] == 26
    n2 = d["N2 the orientation-odd invariants pair up (SnapPy)"]
    assert n2["threads read (both signs)"] == 42 and n2["every pair: same volume, opposite CS"]
    assert n2["isometries to the mirror reverse orientation (both kinds exist only when amphichiral)"]
    n3 = d["N3 the order-3 orientation on the parities, tick by tick"]
    assert n3["odd-trace cyclic words to length 10"] == 98
    assert n3["the 3-cycle's direction flips at every tick on all of them"] and n3["every odd-trace word has even length"]
    assert d["N5 neither candidate supplies a forced gauge-side complex structure at the weave level"]
    sys.path.insert(0, str(here))
    import the_weaves_mirror as WM
    r1, words = WM.n1(8)
    assert r1["S phi^-1 S^-1 = matrix of reverse(phi) with L <-> R, for every one"]
    assert WM.n3(words)["the 3-cycle's direction flips at every tick on all of them"]


def test_w27_the_link_tested():
    """W27 (the rule committed first): with the one stated link, three 27s are anomaly-free (exact), the count is +-3
    only under the parity grading, and the six-dimensional global SU(2) condition selects k = 0 mod 3 sectors. The
    anomaly sums are recomputed in process"""
    import sys
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_link_tested.json").read_text(encoding="utf-8"))
    assert all(d["verdict"].values())
    t1 = d["T1 anomalies"]
    assert t1["the 27's dimension (check)"] == 27 and t1["all free"]
    assert t1["three 27s"]["SU(2) doublets"] == 18
    t3 = d["T3 the six-dimensional reading (Dobrescu-Poppitz's global SU(2) condition)"]
    assert [k for k, v in t3["by the number of parity sectors k"].items() if v["= 0 mod 6"]] == ["3", "6"]
    assert (ROOT / "docs" / "THREE_GENERATIONS_GIVEN_ONE_LINK.md").exists()
    sys.path.insert(0, str(here))
    import the_link_tested as LT
    a = LT.anomalies(LT.TWENTY_SEVEN * 3)
    assert LT.free(a) and a["SU(2) doublets"] == 18


def test_w28_the_three_routes_and_the_qubit():
    """W28 (the rule committed first): the six local solutions are a vector-spinor (spin 1/2 + spin 3/2); the moves
    alone allow -3, -1, 1, 3, the flavor group alone -3, 0, 3, jointly and under locality only +-3; the common point is
    the qubit (Pauli, Clifford, SU(2)_1's projective modular data, the three global forms, the twist-eater). The index
    sets are recomputed in process"""
    import sys
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_three_routes_and_the_qubit.json").read_text(encoding="utf-8"))
    assert all(d["verdict"].values())
    e5 = d["Part I the end condition"]["E5 the index sets"]
    assert e5["the moves (the lifts of L and R)"]["index set"] == [-3, -1, 1, 3]
    assert e5["the flavor group"]["index set"] == [-3, 0, 3]
    assert e5["the moves and the flavor group"]["index set"] == [-3, 3]
    assert e5["locality: the commutant of the puncture's own holonomy"]["index set"] == [-3, 3]
    i4 = d["Part II the common point as the qubit"]["I4 the three global forms of su(2)"]
    assert i4["their number (|P^1(F2)|)"] == 3
    sys.path.insert(0, str(here))
    import the_three_routes_and_the_qubit as TQ
    lifts = TQ.lifts_of()
    hol = [TQ.SC.W_of([1]), TQ.SC.W_of([2])]
    _, F = TQ.SC.commutant(hol, 6)
    assert TQ.index_set(TQ.isotypic(lifts)) == [-3, -1, 1, 3]
    assert TQ.index_set(TQ.isotypic(F)) == [-3, 0, 3]
    assert TQ.index_set(TQ.isotypic(lifts + F)) == [-3, 3]


def test_w29_the_z6_twist_eater():
    """W29 (the rule committed first; a chosen object): the Z6 twist-eater's centraliser in E8 is exactly SU(3) x SU(2)
    (11), its 6 is complex with multiplicity 6, the moves split the 6 as 4 + 2 (quark generations -1, 1, 3, 5, each
    SU(3)^3-free with n(3b,1) = 2 n(3,2)), locality gives five; the lemma (no U(1) of SU(6)' commutes) recomputed"""
    import sys
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_z6_twist_eater.json").read_text(encoding="utf-8"))
    v = d["Z7 the verdict"]
    assert v["centraliser exactly SU(3) x SU(2) (11)"] and v["(a) U(1)_Y broken (the lemma)"]
    assert v["(b) three not forced"] and v["an echo, not a derivation"]
    assert d["Z2 centralisers in E8 [order, dimension]"]["the qutrit alone (1_2 (x) H3)"] == [27, 22.0]
    z6 = d["Z6 the anomalies"]
    assert z6["under the moves: the SU(3)^3-free (n(3,2), n(3b,1))"] == [[-1, -2], [1, 2], [3, 6], [5, 10]]
    assert z6["under locality: the free ones"] == [[5, 10]]
    post = json.loads((here / "the_z6_twist_eater_posthoc.json").read_text(encoding="utf-8"))
    assert post["P2 the lift of (L R^-1 L)^2 = -I composed with conjugation by a b^-1"][
        "the lifts of L and R keep them (they are the pieces)"]
    p3 = post["P3 which moves the index sets assume"]
    assert p3["Z6: ... of L, R and the bare -I"] == 1 and p3[
        "Z6: the 6-sector's index set with the bare -I a move (-1 + d1)"] == [-1, 5]
    assert p3["the qubit: ... of L, R and the bare -I"] == 2
    sys.path.insert(0, str(here))
    import the_z6_twist_eater as ZT
    assert np.allclose(ZT.A @ ZT.B @ np.linalg.inv(ZT.A) @ np.linalg.inv(ZT.B), ZT.ZETA * np.eye(6))
    assert ZT.SC.commutant([ZT.A, ZT.B], 6)[0] == 1
    H = ZT.SW.closure([ZT.A, ZT.B], 6, cap=1000)
    assert len(H) == 216 and ZT.SW.average(H)[0] == 11.0


def test_the_three_generations_state_page():
    """The state page of 2026-10-08 (the weave closed at W29) states main's grade and only numbers the record carries:
    each figure it quotes is read here from the arc's JSON, so the page and the record cannot drift apart silently"""
    page = (ROOT / "docs" / "THE_THREE_GENERATIONS_STATE_2026-10-08.md").read_text(encoding="utf-8")
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    assert "the flavour three is" in page and "the gauge three" in page and "0 of 19" in page
    w27 = json.loads((here / "the_link_tested.json").read_text(encoding="utf-8"))
    assert w27["T1 anomalies"]["all free"] and "anomaly-free" in page
    w28 = json.loads((here / "the_three_routes_and_the_qubit.json").read_text(encoding="utf-8"))
    e5 = w28["Part I the end condition"]["E5 the index sets"]
    assert e5["the moves and the flavor group"]["index set"] == [-3, 3] and "±3" in page
    w29 = json.loads((here / "the_z6_twist_eater.json").read_text(encoding="utf-8"))
    assert w29["Z2 centralisers in E8 [order, dimension]"]["H6 (qubit x qutrit)"][1] == 11.0
    assert "exactly SU(3) × SU(2)" in page
    p3 = json.loads((here / "the_z6_twist_eater_posthoc.json").read_text(encoding="utf-8"))[
        "P3 which moves the index sets assume"]
    assert p3["Z6: the 6-sector's index set with the bare -I a move (-1 + d1)"] == [-1, 5] and "only −1 or 5" in page
    for w in ("W1", "W21", "W22", "W25", "W27", "W28", "W29"):
        assert w in page


def test_w30_the_order_three_flux():
    """W30 (the rule committed first): no representation of the forced point carries an order-3 flux; the qutrit class
    is kept by L, R and -I and sent to its conjugate by the swap (kept by the swap with conjugation); the moves act on
    the qutrit through SL(2, F3). The swap's fork is recomputed in process"""
    import sys
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_order_three_flux.json").read_text(encoding="utf-8"))
    assert all(d["Q7 the verdict"].values())
    q5 = d["Q5 the moves on the qutrit's C^3"]
    assert q5["projective order of the lifts of L and R (SL(2, F3) = 2T: 24)"] == 24
    assert q5["with the bare -I added: commutant"] == 1
    sys.path.insert(0, str(here))
    import the_order_three_flux as OT
    A, B = OT.C3, OT.S3
    assert len(OT.intertwiners(A, B, B, A)) == 0
    assert len(OT.intertwiners(A, B, B.conj(), A.conj())) == 1
    assert len(OT.intertwiners(A, B, A, A @ B)) == 1
    assert np.allclose(OT.comm(A, B), OT.OMEGA * np.eye(3))


def test_w31_the_z5_flux():
    """W31 (the rule committed first): the Z5 flux keeps exactly SU(5)_g with complete generations, but no flux zeta^m
    gives an anomaly-free three, under the moves or under locality. The flux zeta's count is recomputed in process"""
    import sys
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_z5_twist_eater.json").read_text(encoding="utf-8"))
    assert all(v is True or v == "cited" for v in d["F7 the verdict"].values())
    assert d["F2 the centraliser in E8"]["the mean of chi248 at diag(h, 1) over the 125 (W25's chi248)"] == 24.0
    assert d["F6 the counts, every flux"]["as the rule's table"] is True
    assert d["F6 the counts, every flux"][
        "an anomaly-free three (|n| = 3 with n(10) = n(5-bar)) for some flux, under the moves or under locality"] is False
    f5 = d["F5 the moves at the puncture (flux zeta)"]
    assert f5["projective order of the lifts of L and R (SL(2, F5) = 2I: 120)"] == 120
    assert f5["with the bare -I added: projective order"] == 3000
    sys.path.insert(0, str(here))
    import the_z5_twist_eater as Z5
    A, B = Z5.C5, Z5.S5
    assert len(Z5.OT.intertwiners(A, B, B, A)) == 0                 # the swap sends zeta to zeta-bar
    uL, uR, _ = Z5.lifts(A, B)
    s5 = sorted((dd, m) for _, dd, m in Z5.Z.components([uL, uR], 5))
    s10 = sorted((dd, m) for _, dd, m in Z5.Z.components([Z5.Z.compound(uL, 2), Z5.Z.compound(uR, 2)], 10))
    assert s5 == [(2, 1), (3, 1)] and s10 == [(1, 1), (3, 1), (6, 1)]
    n10 = {-1 + x for x in Z5.Z.subset_sums(s5)}
    n5b = {-4 + x for x in Z5.Z.subset_sums(s10)}
    assert sorted(n10 & n5b) == [-1, 2]
    assert np.allclose(Z5.OT.comm(A, B), Z5.ZETA * np.eye(5))


def test_w32_the_puncture_content():
    """W32 (the rule committed first): over every rank-5 bundle from the common point's blocks that L and R keep, F-HE's
    anomaly-free counts under the end conditions the weave keeps are 0, 1, 4 and +-2, never three. The weave's five is
    recomputed in process"""
    import sys
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_puncture_content.json").read_text(encoding="utf-8"))
    assert all(v is True for v in d["P7 the verdict"].values())
    assert d["P2 the census"]["how many"] == 5
    assert d["P4 naturality: the anomaly-free counts"]["D + P"] == [1, 4]
    assert d["P4 a natural three (|n| = 3) for some bundle"] is False
    assert d["P5 a local three for some bundle"] is False
    sys.path.insert(0, str(here))
    import the_puncture_content as PC
    A, B = PC.direct_sum(["D", "c1", "c2", "c3"])
    UL = PC.generic(PC.OT.intertwiners(A, B, A, A @ B))
    UR = PC.generic(PC.OT.intertwiners(A, B, A @ B, B))
    assert UL is not None and UR is not None
    s10 = PC.sector(A, B, UL, UR)
    s5b = PC.sector(PC.Z.compound(A, 2), PC.Z.compound(B, 2), PC.Z.compound(UL, 2), PC.Z.compound(UR, 2))
    assert s10["index under naturality"] == [-1, 1, 2, 4]
    assert sorted(set(s10["index under naturality"]) & set(s5b["index under naturality"])) == [1, 4]
    assert [s10["index under W22's block rule"], s5b["index under W22's block rule"]] == [1, 3]


def test_w33_the_odd_spin_structure_across_frames():
    """W33 (the rule committed first): "three exactly when the odd spin structure is left out" is not a law; under the
    spinor rule a sector's count is +- its doublet blocks; the three parity doublets count +-3, with the zero parity's
    doublet +-4. The doublet sectors are recomputed in process"""
    import sys
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_odd_spin_structure_across_frames.json").read_text(encoding="utf-8"))
    assert all(v is True for v in d["T7 the verdict"].values())
    assert d["T2 the counts"]["E6"]["c0^3"]["counts under (N)"] == [0, 3]
    assert d["T4 under (S) every sector's count is +-(its doublet blocks), in every frame"] is True
    sys.path.insert(0, str(here))
    import the_odd_spin_structure_across_frames as OS
    for with_zero, k in ((False, 3), (True, 4)):
        A, B = OS.parity_doublets(with_zero)
        UL = OS.PC.generic(OS.OT.intertwiners(A, B, A, A @ B))
        UR = OS.PC.generic(OS.OT.intertwiners(A, B, A @ B, B))
        s, _ = OS.sector(A, B, UL, UR)
        assert s["(N)"] == [-k, k] and s["(S)"] == [-k, k]


def test_w34_the_observer_layer_on_the_weave():
    """W34 (the rule committed first): the observer layer's negatives on every thread and on the weave. No private states
    on the 758 states (747 at 60 digits, the other 11 post hoc at 120); at the common point private states 0, 4, 6 kept
    by no thread and not jointly; 536 names, the coincidences exactly the reversal pairs; the register inner and in no
    hand. Q2's table, the joint zeros and Q5's lemma are recomputed in process (exact)"""
    import sys
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_observer_layer_on_the_weave.json").read_text(encoding="utf-8"))
    q1 = d["Q1 the private states on every thread (B761's quantity)"]
    assert q1["errors"] == [] and q1["the control m004 (b++LR): B761's (1, 1, 0) in each block"] is True
    assert q1["per block (H1, rank, private) for k = 1, 2, 3 -> states"] == {"((1, 1, 0), (1, 1, 0), (1, 1, 0))": 747}
    assert len(q1["undecided (a rank between 1e-40 and 1e-25 relative)"]) == 11
    post = json.loads((here / "the_observer_layer_posthoc.json").read_text(encoding="utf-8"))
    assert post["every undecided state now (1, 1, 0) in every block"] is True and len(post["rows"]) == 12
    q2 = d["Q2 the private states at the common point (exact)"]
    assert q2["fiber_dim(n) at the common point, n = 2, 3, 4"] == [0, 4, 6]
    assert q2["thread by thread"]["states keeping a private state (predicted none)"] == []
    assert q2["thread by thread"]["every odd-trace state keeps (1, 1, 2) (predicted)"] is True
    q3 = d["Q3 the self-name among the threads"]
    assert (q3["distinct names"], q3["reversal pairs (a word and its reverse, same sign, different states)"]) == (536, 222)
    assert q3["shared names that are not reversal pairs"] == [] and q3["every + state is separated from its - state"]
    q5 = d["Q5 the register and the hands (exact)"]
    assert q5["the register keeps both hands"] is True and q5["the control: C flips the cyclic order (the McKay hand)"]
    sys.path.insert(0, str(here))
    import the_observer_layer_on_the_weave as OL
    for k, want in ((1, (3, 3, 0)), (2, (7, 3, 4)), (3, (8, 6, 2))):
        b = OL.Block(k)
        assert (b.h1, b.rank_res, b.private) == want
        assert b.kept([b.action(OL.CP.AUT["L"]), b.action(OL.CP.AUT["R"])]) == (0, 0)
    sigma, rev = {1: [1, 2], 2: [1]}, {1: [2, 1], 2: [1]}
    assert OL.CP.compose(OL.CP.inner([-1]), sigma) == rev
    assert OL.proportional(OL.lift(rev), OL.mmul(OL.RHO[-1], OL.lift(sigma)))


def test_w35_the_mixing_patterns_verified():
    """W35 (a verification of main's B1612, not blind): the weave's group on the holomorphic triplet, rebuilt from W21,
    has order 96, 11 eigenbases, six full patterns and five columns, with TM1 from RL against RRL's eigenline"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_mixing_patterns_verified.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True
    assert (d["the image on T (order)"], d["eigenbases"], d["the number of full patterns"], d["the number of columns"]) == (
        96, 11, 6, 5)
    assert [0.166667, 0.166667, 0.666667] in d["columns (sorted)"]


def test_w36_the_sm_centralizer_in_e8():
    """W36 (a review of the audit lane's step 1, exact): the roots of E8 orthogonal to SU(5)_g are an A4, so the SM's
    centralizer is (SU(5)_b x U(1)_Y)/Z5, connected. Recomputed in process"""
    import sys
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    sys.path.insert(0, str(here))
    import the_sm_centralizer_in_e8 as SC8
    R = SC8.e8_roots()
    su5g = [r for r in R if all(x == 0 for x in r[5:]) and sorted(r[:5]) == [-1, 0, 0, 0, 1]]
    orth = [r for r in R if all(SC8.dot(r, s) == 0 for s in su5g)]
    assert (len(R), len(su5g), len(orth)) == (240, 20, 20) and SC8.is_a4(orth)
    d = json.loads((here / "the_sm_centralizer_in_e8.json").read_text(encoding="utf-8"))
    assert d["the centralizer is (SU(5)_b x U(1)_Y)/Z5, connected"] is True


def test_w37_tm1_prediction_and_observer_layer_verified():
    """W37 (a verification of main's S92, not blind): TM1's cos(delta) = -0.1303 at B1613's inputs, J = +-0.03378; on the
    weave the doublet and the matter blocks are wholly private at the puncture, the adjoint and the parity lines visible.
    One local system recomputed in process"""
    import sys
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_tm1_prediction_and_observer_layer_verified.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True
    assert d["B1613"]["cos delta"].startswith("-0.13027")
    sys.path.insert(0, str(here))
    import the_tm1_prediction_and_observer_layer_verified as TV
    m = TV.local_system(TV.OL.mscale(TV.OL.QI, TV.OL.q(-1)), TV.OL.QJ)
    assert (m["dim H1"], m["visible (rank to the puncture)"], m["private"]) == (2, 0, 2)


def test_w38_the_couplings_verified():
    """W38 (a verification of main's S93 and S94, not blind): on the matter triplet the weave's group (order 96) leaves
    one invariant in T-bar (x) T and none in T (x) T or Sym^2 T; along RRL one triplet's fixed Dirac vacua obey
    m1 + m2 = m3 and no Majorana vacuum is fixed. The group and its invariants recomputed in process"""
    import sys
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_couplings_verified.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True
    assert d["Dirac (T-bar (x) T = End T)"]["piece dimensions"] == [1, 2, 3, 3]
    assert d["Majorana (Sym^2 T)"]["Sym^2 T: piece dimensions"] == [1, 2, 3]
    sys.path.insert(0, str(here))
    import the_couplings_verified as CV
    GT, _, el = CV.the_group()
    tr = [np.trace(g) for g in GT]
    tr2 = [np.trace(g @ g) for g in GT]
    assert len(GT) == 96
    assert abs(sum(abs(t) ** 2 for t in tr) / 96 - 1) < 1e-9
    assert abs(sum(t ** 2 for t in tr) / 96) < 1e-9 and abs(sum((t ** 2 + u) / 2 for t, u in zip(tr, tr2)) / 96) < 1e-9
    assert len(np.unique(np.round(np.linalg.eigvals(el["RL"]), 6))) == 3


def test_w38_exact_addendum():
    """W38's exact addendum (post hoc, for the audit lane): T is the cube's rotations twisted by a character; along RRL
    the off-diagonal symmetric piece's fixed matrices obey Heron's identity (tr X)^2 = 2 tr X^2, so m1 + m2 = m3 on the
    whole family; every residual-fixed Majorana matrix has a degenerate pair. Heron's polynomial recomputed in process"""
    import sympy as sp
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_couplings_exact.json")
                   .read_text(encoding="utf-8"))
    assert d["every check holds"] is True
    assert d["PGL(T) image: order and element orders"]["order"] == 24
    x, z, xb, zb = sp.symbols("x z xb zb")
    A = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    B = sp.Matrix([[0, 1, -1], [1, 0, 0], [-1, 0, 0]])
    assert [str(m.tolist()) for m in (A, B)] == d["Dirac: the RRL family (exact)"]["basis"]
    X = (xb * A + zb * B).T * (x * A + z * B)
    assert sp.expand(X.trace() ** 2 - 2 * (X * X).trace()) == 0
    S = sp.Matrix([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])          # RRL's signed permutation
    assert S * A * S.T == A and S * B * S.T == B
    assert all(r["every member has an exactly degenerate pair"]
               for r in d["Majorana: each residual's whole fixed space (all pieces at once)"].values()
               if r["fixed dimension (all pieces at once)"] > 0)


def test_w40_the_weave_at_omega_verified():
    """W40 (a verification of main's S95, not blind; given tau = omega): U (a -> b, b -> a^-1 b), the inner
    automorphisms and -I generate a group of order 48 on T, irreducible; the inner automorphisms are the parity signs and
    U a 3-cycle of order 12 on T. U's matrix and its fixed point recomputed in process"""
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_weave_at_omega_verified.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True
    assert d["the residual group's order on T"] == 48 and d["T's commutant under it (1 = irreducible)"] == 1
    assert d["U's eigen-turns on T"]["lift 1"] == [0.25, 0.583333, 0.916667]
    MU = np.array(d["U's H1 matrix"])
    w = np.exp(2j * np.pi / 3)
    assert abs((MU[0, 0] * w + MU[0, 1]) / (MU[1, 0] * w + MU[1, 1]) - w) < 1e-12
    assert np.array_equal(np.linalg.matrix_power(MU, 6), np.eye(2, dtype=int))


def test_w41_the_zero_modes_weight():
    """W41 (the rule committed first): the weave's zero modes have weight -3/4 as one-forms. g = N / (Im tau)^(3/4) is
    invariant under the moves, the numerator pair (theta_3, theta_2)(z | 2 tau) has weight 1/2 with a constant unitary W,
    and theta_1's multiplier is an eighth root of unity. The law under T recomputed in process with the tau-series:
    W(T) = diag(1, i) and eps1(T) = exp(i pi / 4)"""
    import sys
    import mpmath as mp
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_zero_modes_weight.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True
    assert d["the largest relative change of g"] < 1e-6
    sys.path.insert(0, str(here))
    import the_zero_modes_weight as ZW
    t, z = complex(0.23, 1.07), complex(0.13, 0.07)
    assert abs(ZW.th(3, z, 2 * (t + 1)) - ZW.th(3, z, 2 * t)) < 1e-12
    assert abs(ZW.th(2, z, 2 * (t + 1)) - 1j * ZW.th(2, z, 2 * t)) < 1e-12
    assert abs(ZW.th(1, z, t + 1) - mp.exp(1j * mp.pi / 4) * ZW.th(1, z, t)) < 1e-12


def test_w42_the_breaking_verified():
    """W42 (the rule committed first; Part A a verification of main's B1620, not blind): 68 subgroups in 26 classes, and
    57 / 24 / 16 viable under T-bar (x) T, T (x) T and Sym^2 T; every thread's own zero modes are parity-spanned or a body
    diagonal. In process, from the closed form G = {z S : z^8 = 1, z^4 = sgn S}: 96 elements, the elements of order at
    most 2 are the 8 diagonal sign matrices, and they have 16 subgroups (the Sym^2 T count)"""
    import itertools
    import numpy as np
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_breaking_verified.json")
                   .read_text(encoding="utf-8"))
    assert d["every check holds"] is True
    lat = d["A1: the subgroup lattice"]
    assert (lat["subgroups"], lat["conjugacy classes"], lat["abelian subgroups"]) == (68, 26, 57)
    viable = d["A2: viable under each tensor (exact; B1620's definition)"]
    assert [viable[t]["viable subgroups"] for t in ("T-bar (x) T", "T (x) T", "Sym^2 T")] == [57, 24, 16]
    assert d["Part B: the threads' own zero modes"]["how many"] == 745
    rots = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            S = np.zeros((3, 3), dtype=int)
            for i in range(3):
                S[p[i], i] = s[i]
            if round(np.linalg.det(S)) == 1:
                rots.append((S, sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2))
    G = [(k, S) for S, odd in rots for k in range(8) if k % 2 == odd]        # z = zeta_8^k, z^4 = (-1)^k = sgn S
    assert len(G) == 96
    small = [(k, S) for k, S in G if (2 * k) % 8 == 0 and np.array_equal(S @ S, np.eye(3, dtype=int))]
    assert len(small) == 8 and all(np.count_nonzero(S - np.diag(np.diag(S))) == 0 for _, S in small)
    key = lambda x: (x[0] % 8, tuple(x[1].ravel()))
    ident = (0, tuple(np.eye(3, dtype=int).ravel()))
    count = 0
    for r in range(8):
        for sub in itertools.combinations([x for x in small if key(x) != ident], r):
            H = {key(x) for x in sub} | {ident}
            mats = {key(x): x for x in sub}
            mats[ident] = (0, np.eye(3, dtype=int))
            if all(key(((a[0] + b[0]) % 8, a[1] @ b[1])) in H for a in mats.values() for b in mats.values()):
                count += 1
    assert count == 16


def test_w43_the_trimaximal_families():
    """W43 (the rule committed first): in the record's frame TM1 is allowed under T-bar (x) T only, the T (x) T family is
    TM2, and Sym^2 T has neither; where c is gauge TM1 returns under T (x) T but not under Sym^2 T. In process: an edge
    half-turn carries c with c^2 = i, so its square kills every T (x) T invariant; its axis against a 3-cycle's
    eigenbasis is TM1's column (2/3, 1/6, 1/6); a parity line against it is TM2's (1/3, 1/3, 1/3)"""
    import numpy as np
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_trimaximal_families.json")
                   .read_text(encoding="utf-8"))
    assert d["every check holds"] is True
    rec = d["F1: the record's frame"]
    assert rec["T (x) T"]["pairs with a fixed TM1 column, by family dimension"] == {}
    assert rec["T (x) T"]["TM2 allowed (a fixed column with family dimension 2)"] is True
    assert rec["T-bar (x) T"]["TM1 allowed (a fixed column with family dimension 2)"] is True
    gauge = d["F3: the frame where c is gauge (B3 = {+-1} x O acting by +-S)"]
    assert gauge["T (x) T"]["TM1 allowed (a fixed column with family dimension 2)"] is True
    assert gauge["Sym^2 T"]["TM1 allowed (a fixed column with family dimension 2)"] is False
    e = np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])                       # RRL's rotation, an edge half-turn
    g = np.exp(1j * np.pi / 4) * e
    g2 = g @ g
    assert np.allclose(g2, 1j * np.eye(3))
    M = np.random.default_rng(0).normal(size=(3, 3)) + 1j
    assert np.allclose(g2 @ M @ g2.T, -M)                                  # so no T (x) T invariant survives it
    w = np.exp(2j * np.pi / 3)
    tri = np.array([[1, 1, 1], [1, w, w * w], [1, w * w, w]]).T / np.sqrt(3)
    axis = np.array([0, 1, 1]) / np.sqrt(2)
    assert np.allclose(np.sort(np.abs(tri.conj().T @ axis) ** 2), [1 / 6, 1 / 6, 2 / 3])
    assert np.allclose(np.abs(tri.conj().T @ np.array([1, 0, 0])) ** 2, [1 / 3] * 3)


def test_w44_the_free_numbers_by_frame():
    """W44 (the rule committed first; one prediction failed and recorded): the CKM needs a four-dimensional family in both
    frames under every tensor, so the 13 are unreduced whatever the frame; the PMNS minimum is 2 / 2 / 4 in the record's
    frame and 2 / 2 / 3 where c is gauge (predicted 4). In process: the data file's hash, and the overlaps behind the
    one-relation families (an edge axis against a parity line, 1/2; against another edge axis, 1/4)"""
    import hashlib
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_free_numbers_by_frame.json").read_text(encoding="utf-8"))
    tensors = ("T-bar (x) T", "T (x) T", "Sym^2 T")
    assert [d["the minima, F_all"][t]["PMNS"] for t in tensors] == [2, 2, 4]
    assert [d["the minima, F_c"][t]["PMNS"] for t in tensors] == [2, 2, 3]
    assert all(d[f][t]["CKM"] == 4 for f in ("the minima, F_all", "the minima, F_c") for t in tensors)
    assert all(d[f][t]["CKM: below it, every orbit fails the block test"]
               for f in ("the minima, F_all", "the minima, F_c") for t in tensors)
    checks = d["checks"]
    assert checks["D1: F_all, the minima are PMNS 2 / 2 / 4 and CKM 4 / 4 / 4"] is True
    assert checks["D2: F_c, the same minima"] is False                     # the failed prediction, kept as failed
    assert hashlib.sha256((here / "received" / "B1612_data.json").read_bytes()).hexdigest() == (
        "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606")
    edge, edge2, line = np.array([1, 1, 0]) / np.sqrt(2), np.array([0, 1, 1]) / np.sqrt(2), np.array([1, 0, 0])
    assert np.isclose(abs(edge @ line) ** 2, 0.5) and np.isclose(abs(edge @ edge2) ** 2, 0.25)


def test_w45_the_index_on_the_weaves_surface():
    """W45 (the rule committed first; one run; E1 to E4 as predicted): given Lambda, the triplet's four-dimensional Dirac
    index on the weave's own surface is 0 for both hands at the weight the geometry forces (3/2 for rho_T; 1/2 and 5/2
    for its conjugate), with every space zero by the second route; T is a representation of the metaplectic cover, not
    a local system on M_{1,2}. In process: S~^4 = (L R^-1 L)^4 is conjugation by a b^-1 a^-1 b, and chi from the stored
    traces and exponents, with the closed form and the cusp divisor's step of 3"""
    import sys
    from fractions import Fraction
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_index_on_the_weaves_surface.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True and all(d["checks"].values())
    e1 = d["E1: the structure"]
    assert e1["S~^4 is inner: the conjugating word u"] == "a b^-1 a^-1 b"
    assert e1["u through the inner lifts: determinants"] == [1.0] and e1["the lifted S~^4: determinant"] == -1.0
    kept = d["E3: the kept identifications and their chi_k"]
    assert kept == {"S <-> S~, T <-> L^-1": {"3/2": 0.0, "7/2": 1.0, "11/2": 1.0, "15/2": 2.0},
                    "S <-> S~^-1, T <-> L": {"1/2": 0.0, "5/2": 0.0, "9/2": 1.0, "13/2": 1.0}}
    e4 = d["E4: the dimensions"]
    assert e4["S <-> S~, T <-> L^-1"]["3/2"]["dim M_k (null count, gap)"][0] == 0
    assert e4["S <-> S~, T <-> L^-1"]["3/2"]["dim S_(2-k) of the dual (null count, gap)"][0] == 0
    assert e4["S <-> S~^-1, T <-> L"]["1/2"]["dim M_k (null count, gap)"][0] == 0
    sys.path.insert(0, str(here))
    import the_common_point as CP
    St = {1: [1], 2: [2]}
    for a in (CP.AUT["L"], {1: [1, -2], 2: [2]}, CP.AUT["L"]):
        St = CP.compose(St, a)
    St4 = {1: [1], 2: [2]}
    for _ in range(4):
        St4 = CP.compose(St4, St)
    assert St4 == CP.inner([1, -2, -1, 2])

    def chi(k, trS, trST, lam):
        k = float(k)
        return (3 * (k - 1) / 12 + 0.25 * (np.exp(1j * np.pi * k / 2) * trS).real
                + 2 / (3 * np.sqrt(3)) * (np.exp(1j * np.pi * (2 * k + 1) / 6) * trST).real + 1.5 - sum(lam))
    for name, sign, lam in (("S <-> S~, T <-> L^-1", 1, (1 / 8, 3 / 8, 7 / 8)), ("S <-> S~^-1, T <-> L", -1, (1 / 8, 5 / 8, 7 / 8))):
        row = d["E3: the four identifications"][name]
        trS = complex(*row["tr rho(S)"])
        assert abs(trS - np.exp(sign * 1j * np.pi / 4)) < 1e-9 and row["tr rho(ST)"] == [0.0, 0.0]
        assert np.allclose(row["exponents of rho(T)"], lam)
        for k, v in kept[name].items():
            assert abs(chi(Fraction(k), trS, 0, lam) - v) < 1e-9
            m = int((Fraction(k) - (Fraction(3, 2) if sign == 1 else Fraction(1, 2))) / 2)
            closed = 0.25 + m / 2 - (-1) ** m / 4 if sign == 1 else -0.25 + m / 2 + (-1) ** m / 4
            assert abs(closed - v) < 1e-12
            assert abs(chi(Fraction(k) + 12, trS, 0, lam) - v - 3) < 1e-9   # one unit at the cusp on every component
    assert abs(chi(Fraction(23, 2), np.exp(1j * np.pi / 4), 0, (1 / 8, 3 / 8, 7 / 8)) - 3) < 1e-9


def test_w46_the_end_conditions_on_the_weaves_surface():
    """W46 (the rule committed first; one run; every cell as predicted): given Lambda, for every end condition the weave
    keeps on its own surface (W28's four at the puncture; n uniform units at the cusp) the four-dimensional index is n
    times the fibre's index, and every space is zero at n = 0, under both base spin structures. In process: the six
    local solutions' monodromy from W24's blocks_action with the record's lifts (rho6(S)^2 = -I; exponents the union of
    the two triplets'), and chi_1 = 0 on V2 and V4 from the formula"""
    import sys
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_end_conditions_on_the_weaves_surface.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True and all(d["checks"].values())
    want = {"0": -3, "V2": -1, "V4": 1, "L6": 3}
    for lab in ("the record's lifts", "the other overall sign"):
        r = d[lab]
        tab = r["H5: the four-dimensional index, by condition and cusp units n"]
        for name, f in want.items():
            assert [tab[name][k] for k in ("-1", "0", "1")] == [-f, 0.0, f]
        assert all(v[0] == 0 for v in r["H4: the second route (null count, gap)"].values())
    sys.path.insert(0, str(here))
    import the_mixing_patterns_verified as MV
    import the_six_dimensional_census as SC
    (_, gL, gR) = MV.H.lift_choices()[0]
    aL, aR = SC.blocks_action(MV.CP.AUT["L"], gL), SC.blocks_action(MV.CP.AUT["R"], gR)
    S6 = np.linalg.inv(aL @ np.linalg.inv(aR) @ aL)
    assert np.allclose(S6 @ S6, -np.eye(6), atol=1e-9)
    lam = sorted(round(float(np.angle(z) / (2 * np.pi)) % 1.0, 9) for z in np.linalg.eigvals(aL))
    assert lam == [0.125, 0.125, 0.375, 0.625, 0.875, 0.875]
    st = d["the record's lifts"]["H1: structure"]
    for i, (trS, trST) in enumerate(zip(st["tr rho(S): V2, V4"], st["tr rho(ST): V2, V4"])):
        ex = st["exponents: T, T-bar, six, V2, V4"][3 + i]
        chi1 = (0.25 * (1j * complex(*trS)).real + 2 / (3 * np.sqrt(3)) * (1j * complex(*trST)).real
                + len(ex) / 2 - sum(ex))
        assert abs(chi1) < 1e-9


def test_w47_the_unit_at_the_weaves_cusp():
    """W47 (main's named arc; the rule committed first; one run; every cell as predicted): nothing on the weave's surface
    forces the cusp's unit. The flat line bundles are the 24 characters of the metaplectic group, six keep the forced
    weights, every cusp exponent is an odd multiple of 1/24, the twisted index is 0 except -1 at r = 4 and r = 20, and
    |I| = 3 only with one cusp unit at a natural puncture condition. In process: the coinvariants, the exponents' parity
    and the formula's chi_{3/2} at r = 4"""
    import numpy as np
    import sympy as sp
    from sympy.matrices.normalforms import smith_normal_form
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_unit_at_the_weaves_cusp.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True and all(d["checks"].values())
    assert d["K1: the flat line bundles"]["the allowed r"] == [0, 4, 8, 12, 16, 20]
    t3 = d["K3: the twisted index"]["the twisted index at n = 0, by r and puncture condition"]
    nonzero = sorted((r, c) for r, row in t3.items() for c, v in row.items() if abs(v) > 1e-9)
    assert nonzero == [("20", "L6"), ("20", "V2"), ("4", "0"), ("4", "V4")]
    assert all(abs(t3[r][c] + 1) < 1e-9 for r, c in nonzero)
    assert len(d["K5: where |I| = 3"]) == 20 and all(c in ("0", "L6") for _, c, _ in d["K5: where |I| = 3"])
    snf = smith_normal_form(sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0]]), domain=sp.ZZ)   # [L - 1 | R - 1]
    assert [abs(int(snf[i, i])) for i in range(2)] == [1, 1]
    assert all((x + 4 * m) % 2 == 1 for x in (3, 9, 21) for m in range(6))
    lam = [((x + 4) % 24) / 24 for x in (3, 9, 21)]                                    # rho_T (x) eps_4 at the cusp
    trS = np.exp(1j * np.pi / 4) * np.exp(-1j * np.pi)                                  # tr rho_T(S) eps_4(S)
    chi = 3 * 0.5 / 12 + 0.25 * (np.exp(3j * np.pi / 4) * trS).real + 1.5 - sum(lam)
    assert abs(chi - 1) < 1e-12


def test_w48_the_outside_source_at_the_cusp():
    """W48 (the owner's outside source; the rule committed first; one run; every cell as predicted): a source of weight w
    turns the triplet's index into chi_{3/2 - w}; a c = 24 source with a lattice of rank l gives (24 - l)/8, one mode
    per eight lattice-free chiral bosons, so three needs 24 of them and the heterotic left-movers give one. In process:
    the law chi_{3/2 + 4j}(rho_T) = j from the stored data's traces, and E4^2's first coefficients"""
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_outside_source_at_the_cusp.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True and all(d["checks"].values())
    lat = d["S1: the lattice family"]
    assert [-v["0"] for v in lat.values()] == [3.0, 2.0, 1.0, 0.0]
    assert [-v["0"] for v in d["S2: the oscillator family"].values()] == [1.0, 1.0, 2.0, 3.0]
    dims = d["S3: the lattice family's dressed spaces"]
    assert [v["T"]["dim M (null count, gap)"][0] for v in dims.values()] == [3, 2, 1, 0]
    for j in range(-1, 7):
        k = 1.5 + 4 * j
        chi = 3 * (k - 1) / 12 + 0.25 * (np.exp(1j * np.pi * k / 2) * np.exp(1j * np.pi / 4)).real + 1.5 - 11 / 8
        assert abs(chi - j) < 1e-9
    c4 = [1, 240, 2160]
    assert np.convolve(c4, c4)[:3].tolist() == [1, 480, 61920]


def test_w49_the_generations_are_a_multiplicity():
    """W49 (the owner's turn to the free numbers; the rule committed first; one run; every cell as predicted): the
    weave's triplet is one zero mode three times, T = l (x) M. The intertwiners send T's three parity lines to one line
    of the spin doublet (Q = +2 on it), every lift is a scalar on l times a rotation of the three units (W42's 96), the
    Hodge-Riemann form is 2 I on M, and the puncture conditions that keep +-3 are exactly the products. In process: the
    quaternion twirl and V2's entanglement from the units alone"""
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_generations_are_a_multiplicity.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True and all(d["checks"].values()) and d["every control holds"] is True
    m1 = d["M1: one line"]
    assert m1["the dimension of T's intersection with each parity block"] == [1, 1, 1]
    assert m1["the three images span one line"] is True
    assert m1["Q(l^, l^)"] == [2.0, 0.0] and m1["Q on l's Q-orthogonal complement"][0] == -2.0
    assert d["M2: the lifts in the basis t_p"]["the group the lifts of L and R generate on T: elements"] == 96
    gram = d["M3: the Hodge-Riemann form on T"]["the Gram matrix of Q on T in the basis t_p"]
    assert all(abs(complex(*gram[i][j]) - (2 if i == j else 0)) < 1e-9 for i in range(3) for j in range(3))
    m4 = d["M4: the puncture conditions in rho_Q (x) M"]
    assert [m4[c]["a product X (x) Y"] for c in ("0", "V2", "V4", "L6")] == [True, False, False, True]
    e = d["extra read-outs (not predicted)"]
    assert e["E4: the fibre index by type"]["the fibre index f = I(n = 1) - I(n = 0), by condition"] == {
        "0": -3.0, "V2": -1.0, "V4": 1.0, "L6": 3.0}
    assert all(abs(x - np.sqrt(2)) < 1e-9 for x in e["E3: V2's singular values"][
        "s1 / s2 over 200 random vectors of V2: min, max"])
    units = [np.array([[0, 1], [-1, 0]], dtype=complex), np.array([[1j, 0], [0, -1j]]), np.array([[0, 1j], [1j, 0]])]
    rng = np.random.default_rng(0)
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    assert np.allclose(sum(u.conj().T @ A @ u for u in units), 2 * np.trace(A) * np.eye(2) - A)
    v = rng.normal(size=2) + 1j * rng.normal(size=2)
    s = np.linalg.svd(np.array([np.linalg.inv(u) @ v for u in units]).T, compute_uv=False)
    assert abs(s[0] / s[1] - np.sqrt(2)) < 1e-12


def test_w50_the_parity_grading_at_a_fixed_tau():
    """W50 (the rule first, corrected before the run; one run; every cell as predicted): the inner automorphisms are not
    words in L and R, so on the ruled branch the residual on T at a generic tau is four scalars and couplings in tau
    alone give mixing far from a permutation; T is eta^21 (theta_4^2, theta_2^2, theta_3^2). In process: the word
    identities on free words, the coupling dimensions from W45's formula, and Jacobi's identity"""
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_parity_grading_at_a_fixed_tau.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True and all(d["checks"].values()) and d["every control holds"] is True
    assert d["the rule's original N2 wording (every such word empty or for conj(u)^+-1), corrected before the run"] is False
    n2 = d["N2: the words with H1 matrix I"]
    assert n2["their automorphisms"] == {"the identity": 1944, "conj(u)": 196, "conj(u^-1)": 196}
    n3 = d["N3: the residuals on T"]
    assert n3["the ruled branch: generic tau (Delta^2)"] == {"order": 4, "commutant dimension": 9}
    assert n3["W40's frame (with the inner automorphisms and -I): omega"] == {"order": 48, "commutant dimension": 1}
    assert d["N6: the theta constants"]["the parity carried by each even theta constant"] == {
        "(1/2, 0)": "theta_4^2", "(0, 1/2)": "theta_2^2", "(1/2, 1/2)": "theta_3^2"}
    assert d["N5: the mixing at tau0"]["tau0"]["(a) O+ at k = 3 against D at k = 5"]["distance from the permutations"] > 0.5

    def red(w):
        out = []
        for x in w:
            if out and out[-1] == -x:
                out.pop()
            else:
                out.append(x)
        return out

    def app(f, w):
        out = []
        for x in w:
            out += f[x] if x > 0 else [-y for y in reversed(f[-x])]
        return red(out)

    def comp(*fs):
        g = {1: [1], 2: [2]}
        for f in fs:
            g = {x: app(g, f[x]) for x in (1, 2)}
        return g

    conj = lambda u: {x: red(u + [x] + [-y for y in reversed(u)]) for x in (1, 2)}
    L, Li, R, Ri = {1: [1], 2: [1, 2]}, {1: [1], 2: [-1, 2]}, {1: [1, 2], 2: [2]}, {1: [1, -2], 2: [2]}
    s, P = {1: [-1], 2: [-2]}, {1: [2], 2: [1]}
    assert comp(s, L, s, Li) == conj([-1]) and comp(s, R, s, Ri) == conj([2])
    assert comp(P, L, P, Ri) == conj([2]) and comp(P, R, P, Li) == conj([-1])
    D = comp(L, Ri, L)
    assert comp(D, D, D, D) == conj([1, -2, -1, 2])
    traces, sums = {"D": -1j, "O+": -1j, "O-": 1j}, {"D": 1.75, "O+": 0.75, "O-": 1.25}
    for name, want in (("D", [0, 1, 1, 2, 2]), ("O+", [1, 2, 2, 3, 3]), ("O-", [1, 1, 2, 2, 3])):
        chis = [3 * (k - 1) / 12 + 0.25 * (np.exp(1j * np.pi * k / 2) * traces[name]).real + 1.5 - sums[name]
                for k in (3, 5, 7, 9, 11)]
        assert np.allclose(chis, want)
    tau = 0.21 + 1.04j
    n = np.arange(-30, 31)
    t2 = np.sum(np.exp(1j * np.pi * (n + 0.5) ** 2 * tau))
    t3 = np.sum(np.exp(1j * np.pi * n ** 2 * tau))
    t4 = np.sum((-1.0) ** n * np.exp(1j * np.pi * n ** 2 * tau))
    assert abs(t3 ** 4 - t2 ** 4 - t4 ** 4) < 1e-12


def test_w51_the_weaves_functionals_on_tau():
    """W51 (the owner's 'look for what fixes tau'; the rule first; one run; every cell as predicted): the joint
    determinant of the three parity sectors is exactly 4 (Jacobi), so flat in tau; the symmetric sums and T's norm are
    minimized at omega and the untwisted determinant maximized there, with i a saddle and no other critical point. In
    process: the theta and eta series at random points, the AM-GM bound, and the closed forms at i and omega"""
    import math
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_weaves_functionals_on_tau.json").read_text(encoding="utf-8"))
    assert d["every check holds"] is True and all(d["checks"].values())
    cen = d["the census, by candidate"]
    assert {n: (c["i"]["type"], c["rho"]["type"]) for n, c in cen.items()} == {
        "e1": ("saddle", "minimum"), "e2": ("saddle", "minimum"), "D": ("saddle", "maximum"),
        "N_T": ("saddle", "minimum"), "P_T": ("saddle", "minimum")}
    assert all(not c["critical points in the interior"] for c in cen.values())

    def x(t):
        n = np.arange(-20, 21)
        q = np.exp(2j * np.pi * t)
        eta = np.exp(1j * np.pi * t / 12) * np.prod([1 - q ** m for m in range(1, 80)])
        th = [np.sum(np.exp(1j * np.pi * (n + 0.5) ** 2 * t)), np.sum(np.exp(1j * np.pi * n ** 2 * t)),
              np.sum((-1.0) ** n * np.exp(1j * np.pi * n ** 2 * t))]
        return [abs(v / eta) ** 2 for v in th]

    rng = np.random.default_rng(51)
    for _ in range(20):
        t = rng.uniform(-0.5, 0.5) + 1j * rng.uniform(0.9, 3.0)
        xs = x(t)
        assert abs(xs[0] * xs[1] * xs[2] - 4) < 1e-10
        assert sum(xs) >= 3 * 2 ** (2 / 3) - 1e-12
    assert abs(sum(x(1j)) - (2 + 2 * math.sqrt(2))) < 1e-10
    assert abs(sum(x(0.5 + 1j * math.sqrt(3) / 2)) - 3 * 2 ** (2 / 3)) < 1e-10


def test_w52_the_free_numbers_counted():
    """W52 (the owner's 'then we count free numbers'; the rule first; one run; C1 and C4 as predicted, C2 and C3 failed
    as worded and explained post hoc): at the geometry's weight the Standard Model frame leaves 11 of the 13 flavour
    numbers; a symmetric zero-diagonal coupling forces m3 = m1 + m2. In process: that identity on random matrices"""
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_free_numbers_counted.json").read_text(encoding="utf-8"))
    c = d["checks"]
    assert [c[k] for k in c] == [True, False, False, True] and d["every check holds"] is False
    assert d["C3: the geometry's weight (all k = 3)"]["T (x) T"]["ranks at three points"] == [11, 11, 11]
    assert d["C3: the geometry's weight (all k = 3)"]["Sym^2 T"]["ranks at three points"] == [4, 4, 4]
    scan = d["C2: the scan"]
    assert sum(v["ranks at three points"] != [v["predicted rank"]] * 3 for v in scan.values()) == 68
    assert all(scan[f"T (x) T: (3, 3, {k})"]["ranks at three points"] == [11] * 3 for k in (3, 5, 7))
    p = json.loads((here / "the_free_numbers_counted_posthoc.json").read_text(encoding="utf-8"))
    assert p["every check holds"] is True and p["P2: agreements"] == 128
    rng = np.random.default_rng(52)
    for _ in range(10):
        x, y, z = rng.normal(size=3) + 1j * rng.normal(size=3)
        m = np.sort(np.linalg.svd(np.array([[0, x, y], [x, 0, z], [y, z, 0]]), compute_uv=False))
        assert abs(m[2] - m[0] - m[1]) < 1e-12 * m[2]


def test_w53_the_fit_at_the_geometrys_weight():
    """W53 (the owner's choice: common-scale masses; the rule and its data first; one run; F2, F3 and F4 went the way
    their priors leaned, M0(e) and F1 failed as worded; post hoc P1 to P4): the weave's modular structure at the
    geometry's weight is excluded by the data, by the masses alone, and the quark masses alone exclude the other two
    rank-11 structures. In process: the transcription against the table as printed"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_fit_at_the_geometrys_weight.json").read_text(encoding="utf-8"))
    c = d["cells (as worded)"]
    assert [c[k] for k in c] == [False, False, True, False, True]
    m0 = d["M0"]
    assert m0["(d) the 13 x 11 Jacobian's rank at three random points"] == [11, 11, 11] and m0["(e) holds"] is False
    ranks = m0["(e) W52's assignments without an O+-alone sector: their recorded ranks"]
    assert sorted(k for k, v in ranks.items() if v != [13] * 3) == [f"T (x) T: (3, 3, {k})" for k in (3, 5, 7)]
    fits = d["the fits (global minimum found)"]
    assert fits["masses only, a = 0.10"]["chi^2"] > 100 and fits["13 observables, a = 0.10"]["chi^2"] > 1000
    assert fits["13 observables, a = 0.20"]["chi^2"] > 100 and fits["13 observables, a = 0.05"]["chi^2"] > 1000
    f1 = d["F1"]
    assert f1["d"]["the smallest residual"] < 1e-12 and f1["e"]["the smallest residual"] < 1e-12
    assert 1e-3 < f1["u"]["the smallest residual"] < 0.05 and abs(f1["u"]["its tau"][1] - 4.2) < 0.05
    lo, hi = d["F4"]["m1/m3 over the window: min, max"]
    assert 0.95e-3 <= lo and hi <= 1.2e-3 and d["F4"]["points in the window"] >= 20
    p = json.loads((here / "the_fit_at_the_geometrys_weight_posthoc.json").read_text(encoding="utf-8"))
    assert list(p["read-outs (post hoc, no prior)"].values()) == [True, True, True, False]
    q = p["P2, P3: the quark fits (global minimum found)"]
    assert q["quark masses only, a = 0.10"]["chi^2"] > 30
    assert all(p["consistency: the quark-only minimum does not exceed W53's 13-observable minimum"].values())
    hz = json.loads((here / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    printed = {}
    for row in hz["as_printed"].values():
        for item in row.split("; "):
            name, unit, rest = item.split(" ", 2)[0], item.split(" / ")[1].split(" ")[0], item.split(" ", 3)[3]
            value, sigma = (float(x) for x in rest.split(" +- "))
            scale = 1e-3 if unit == "MeV" else 1.0
            printed[name[1:]] = (value * scale, sigma * scale)
    got = hz["masses_GeV"]
    for n, (v, s) in printed.items():
        assert abs(got["value"][n] - v) < 1e-12 and abs(got["sigma"][n] - s) < 1e-12, n
    assert len(printed) == 9


def test_w54_the_rank_thirteen_structures():
    """W54 (the owner's choice: test the rank-13 structures; the rule first; one run; H0 and H2 as predicted, H1 and H3
    failed as worded and were explained post hoc): five of the 32 fit, every sector at weight 5 or 7 in T (x) T; every
    structure with a sector at weight 3 fails, and every Sym^2 T one. In process: the parameter counts"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_rank_thirteen_structures.json").read_text(encoding="utf-8"))
    c = d["cells (as worded)"]
    assert [c[k] for k in c] == [True, False, True, False]
    s = d["the structures (global minimum found)"]
    assert len(s) == 32
    assert sorted(d["the structures that fit"]) == sorted(
        f"T (x) T: {k}" for k in ((5, 5, 5), (5, 5, 7), (5, 7, 5), (5, 7, 7), (7, 7, 5)))
    for v in s.values():
        if 3 in v["weights (u, d, e)"] or v["frame"] == "Sym^2 T":
            assert v["chi^2_min"] > 90
    assert s["T (x) T: (5, 7, 5)"]["fits exactly"] and s["T (x) T: (5, 7, 7)"]["fits exactly"]
    h1 = d["H1: the span's closest approach to rank one"]
    mu = {k: [r["mu = m2/m3 there"] for r in rows] for k, rows in h1.items()}
    assert max(mu["k = 7"]) < 1e-10 and max(mu["k = 5"]) < 1e-10 and min(mu["k = 3"]) > 0.1
    p = json.loads((here / "the_rank_thirteen_structures_posthoc.json").read_text(encoding="utf-8"))
    assert all(p["read-outs (post hoc, no prior)"].values())
    assert p["P1: (7, 7, 7) from (7, 7, 5)'s tau"]["so chi^2(7, 7, 7) <="] < 1e-10
    dims = {"T (x) T": {3: 2, 5: 4, 7: 5}, "Sym^2 T": {5: 3, 7: 3}}
    for v in s.values():
        assert v["P"] == 2 + sum(2 * dims[v["frame"]][k] - 1 for k in v["weights (u, d, e)"]) >= 13


def test_w55_the_gauge_side_and_the_sectors():
    """W55 (the owner's choice (a); the rule first; one run; every cell as predicted): the gauge side on record either
    ties the down quarks to the charged leptons, which the data exclude, or splits them only with new free numbers.
    In process: the Kronecker lemma on random cases"""
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_gauge_side_and_the_sectors.json").read_text(encoding="utf-8"))
    assert d["every cell holds"] is True and len(d["cells (as worded)"]) == 4
    b = d["K1: the tie's bound"]
    assert b["a = 0.10"]["chi^2_min"] > 100 and b["a = 0.20"]["chi^2_min"] > 30
    assert 0.45 < d["K4: the allowance a* where the bound reaches 5.99"] < 0.5
    assert d["K3: those with k_d = k_e, and their P"] == {"T (x) T: (5, 5, 5)": 23, "T (x) T: (5, 7, 7)": 27,
                                                         "T (x) T: (7, 7, 7)": 29}
    rng = np.random.default_rng(55)
    for _ in range(10):
        lam = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        lam = lam + lam.T
        P = np.array([[rng.normal(), 0], [rng.normal(), rng.normal()]])
        prod = np.sort(np.outer(np.linalg.svd(P, compute_uv=False), np.linalg.svd(lam, compute_uv=False)).ravel())
        got = np.sort(np.linalg.svd(np.kron(P, lam), compute_uv=False))
        assert np.max(np.abs(got - prod) / prod) < 1e-10



def test_w56_the_higgs_and_the_generation_index():
    """W56 (the owner's request for a field compatible with the seed; the rule first; one run; every cell as
    predicted): the Higgs cannot copy a generation at its weight; in the dual triplet it fits the geometry's weight but
    predicts nothing; no Higgs content in 27s splits the down quarks from the charged leptons in the E6 cubic.
    In process: the E6 identity from the trinification cubic on random cases, and the multiplier's parity"""
    import numpy as np
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_higgs_and_the_generation_index.json").read_text(encoding="utf-8"))
    assert d["every cell holds"] is True and len(d["cells (as worded)"]) == 6
    ks = [f"{0.5 + i:g}" for i in range(8)]
    dims = d["K2: dim M_k (R_G, R_D)"]
    assert [dims["R_G"][k]["dim"] for k in ks] == [0, 1, 0, 5, 0, 10, 0, 14]
    assert [dims["R_D"][k]["dim"] for k in ks] == [0, 0, 3, 0, 8, 0, 12, 0]
    assert d["K2: the control T (x) T at k = 3, 5, 7"] == [2, 4, 5] and d["K2: n = dim M_9/2 (R_D)"] == 8
    c = d["K3: the census (Standard Model frame, the geometry's weight)"]
    assert [c[s]["P (effective)"] for s in ("(D, D)", "(B, D)", "(D, B)")] == [55, 39, 27]
    assert c["(D, D)"]["chi^2_min"] < 1e-10 and c["(B, D)"]["chi^2_min"] < 1e-10
    assert 25 < c["(D, B)"]["chi^2_min"] < 30
    assert all(r[0] == 13 for v in d["K4: rank and the 13th singular value over the largest, at three random points"]
               .values() for r in v)
    k1 = d["K1: the E6 identity"]
    assert abs(k1["the common ratio c (first case), and its largest relative spread across cases"][0] - 1) < 1e-12
    # the parity: rho_T(S)^2 = i, so (conj)^3 needs e^{-i pi k} = i and conj^2 (x) rho needs -i
    assert all(complex(d["rho_T(S)^2 (the convention read before the rule)"][i][j]) == (1j if i == j else 0)
               for i in range(3) for j in range(3))
    for k in (0.5 + i for i in range(8)):
        ph = np.exp(-1j * np.pi * k)
        if abs(ph - 1j) > 1e-12:
            assert dims["R_G"][f"{k:g}"]["dim"] == 0
        if abs(ph + 1j) > 1e-12:
            assert dims["R_D"][f"{k:g}"]["dim"] == 0
    # in process: the E6 identity from the trinification cubic
    def I3(x):
        QL, QR, L = x[:9].reshape(3, 3), x[9:18].reshape(3, 3), x[18:].reshape(3, 3)
        return np.linalg.det(QL) + np.linalg.det(QR) + np.linalg.det(L) - np.trace(QL @ L @ QR.T)

    def polar(X, Y, Z):
        return (I3(X + Y + Z) - I3(X + Y) - I3(X + Z) - I3(Y + Z) + I3(X) + I3(Y) + I3(Z)) / 6

    E = np.eye(27, dtype=complex)
    neutral = [18, 22, 23, 25, 26]
    down, lept = ([1, 2], [10, 11]), ([19, 20], [21, 24])
    rng = np.random.default_rng(56)
    for _ in range(4):
        Y = rng.normal(size=(3, 3, 3)) + 1j * rng.normal(size=(3, 3, 3))
        S = Y + Y.transpose(1, 0, 2)
        v = np.zeros((3, 27), dtype=complex)
        v[:, neutral] = rng.normal(size=(3, 5)) + 1j * rng.normal(size=(3, 5))
        mats = []
        for rows, cols in (down, lept):
            M = sum(np.kron(S[:, :, k], np.array([[polar(E[x], E[y], v[k]) for y in cols] for x in rows]))
                    for k in range(3))
            mats.append(np.sort(np.linalg.svd(M, compute_uv=False)))
        assert np.max(np.abs(mats[1] / mats[0] - 1)) < 1e-10


def test_w57_the_field_of_maximality():
    """W57 (the owner's framing of a field of maximality; the rule first; one run; T4 as predicted, T1 to T3 failed as
    worded, explained post hoc): the world is not a typical draw from the seed's own measure, though the seed makes
    deep hierarchy common where anarchy never does"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_field_of_maximality.json").read_text(encoding="utf-8"))
    assert d["every cell holds"] is False and len(d["cells (as worded)"]) == 4
    cells = list(d["cells (as worded)"].values())
    assert cells == [False, False, False, True]
    m = d["main (S_mix against anarchy, the data at M_Z)"]
    assert m["eps*"] == 64 and all(m["accepted on the ladder (seed, anarchy)"][str(e)] == [0, 0]
                                   for e in (2, 4, 8, 16, 32))
    marg = m["T3: two-sided marginal p of each datum"]
    assert [k for k, v in marg.items() if v < 0.01] == ["log m_c/m_t", "log m_s/m_b", "log m_mu/m_tau"]
    assert d["T4: anarchy's two-sided marginal p for log(m_u/m_t)"] < 1e-5
    c = d["controls"]
    assert c["(a) the vectorised k = 3 forms equal W53's"] is True
    frac = c["(b) the fraction of tau with y > 6, and the measure's 3/(6 pi)"]
    assert abs(frac[0] - frac[1]) < 0.002
    ph = json.loads((here / "the_field_of_maximality_posthoc.json").read_text(encoding="utf-8"))
    assert ph["the regenerated draws reproduce W57's stored count at 64 sigma"] is True
    p2 = ph["P2: typicality by nearest-neighbour distance"]
    assert p2["p_nn"] < 0.006 and p2["the data's d_min to S_mix"] > 30
    p4 = ph["P4: shares (all three m1/m3 < 1e-2; all six mass ratios within a factor 10 of the data's)"]
    assert p4["anarchy"] == [0.0, 0.0] and p4["('B', 'B')"][0] > 0.2 and all(v[1] == 0.0 for v in p4.values())


def test_the_double_ratio_target():
    """The double ratio (y_mu y_d)/(y_s y_e), recorded after W57 as C1's first target: the source's value, the two
    unified values it excludes, and the record's own value recomputed from W53's data"""
    import math
    rec = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "received"
    t = json.loads((rec / "AHS2026_double_ratio.json").read_text(encoding="utf-8"))
    dr = t["the double ratio"]
    assert (dr["value"], dr["sigma"]) == (10.58, 0.11) and "64e1d141" in t["sources"]["double ratio"]
    assert (dr["value"] - dr["Georgi-Jarlskog (c_e, c_mu) = (1/3, 3)"]) / dr["sigma"] > 14
    assert (dr["value"] - dr["the best rational pair (4/9, 9/2)"]) / dr["sigma"] > 4
    m = json.loads((rec / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))["masses_GeV"]
    v, s = m["value"], m["sigma"]
    r = v["mu"] * v["d"] / (v["s"] * v["e"])
    err = r * math.sqrt(sum((s[k] / v[k]) ** 2 for k in ("mu", "d", "s", "e")))
    own = t["the record's own value (HZ2021 at M_Z, W53's data; arithmetic)"]
    assert abs(r - own["value"]) < 1e-3 and abs(err - own["sigma"]) < 0.01


def test_w58_the_level_four_preprint_checked():
    """W58 (the level-four preprint, arXiv:2609.09262, checked; the rule first; one run; five cells as predicted, K4 and
    K7 failed as worded and traced post hoc): its triplet is the record's T up to eta^3's multiplier, its generations
    are T's eigenlines, its numbers reproduce, and its significance does not survive the families it drew from"""
    import math
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_level_four_preprint_checked.json").read_text(encoding="utf-8"))
    assert list(d["cells"].values()) == [True, True, True, False, True, True, False]
    k1 = d["K1"]["the k with chi_eta^(-k) rho_T a representation of Gamma_4"]
    assert sorted(k1) == ["15", "3"] and k1["3"]["T'-charges (quarter turns)"] == [0, 1, 3]
    g = d["K2"]["the preprint's generation lines in the record's basis"]
    assert g["generation 3"]["a parity line"] and not g["generation 1"]["a parity line"]
    k3 = d["K3"]
    assert k3["levels with a solution"] == [4] and k3["the shifts that are a character of S4 (T-charge 0 or 2)"] == [2]
    k4 = d["K4"]
    assert k4["claims checked"] == 41 and k4["the claims that do not reproduce"] == ["Table VII m_c", "Eq. 32"]
    assert abs(d["K5"]["the preprint's double ratio 2/eps"] - 150 / 14) < 1e-12
    k6 = d["K6"]
    assert 0.2 < k6["(b) the anchor's box: prefactors, coverage at 0.02%, hits"][1] < 0.3
    assert k6["(c) the product (the anchor's box, then the form-value family)"] > 0.1
    assert k6["the declared family's product (the text's 1e-6)"] < 1e-6
    assert abs(d["K7"]["(a) at M_Z"]["pulls (data - preprint) / sigma"]["the anchor m_tau/m_mu"]) > 2
    ph = json.loads((here / "the_level_four_preprint_checked_posthoc.json").read_text(encoding="utf-8"))
    assert ph["PH1"]["both reproduce to the printed digits"] is True
    t1 = ph["PH2"]["the preprint's Table I"]
    assert abs(t1["pull at K7's sigma (eps = 14/75)"]) < 0.1
    assert abs(t1["pull at the propagated sigma (eps from the data)"]) < 1
    assert 0.0013 < t1["the propagated relative error of T"] < 0.0016
    assert ph["PH3: the anchor's coverage at its propagated precision (Table I)"]["form-value"]["coverage"] > 0.4
    # in process: the selection theorem's scan, from its two hypotheses alone
    levels = sorted({n for n in range(3, 13) for a1 in range(n - 3) for c in range(n)
                     if ((a1 + 2 + c) % n) - ((a1 + c) % n) == -2 and ((a1 + 3 + c) % n) - ((a1 + 2 + c) % n) == 1})
    assert levels == [4] and math.isclose(2 / (14 / 75), 10.714285714285714)



def test_w59_the_one_loop_potential_on_the_fibre():
    """W59 (D1; the owner's ruling "D1 first"; the rule first; one run; K1, K2, K3, K5 as predicted, K4 failed as worded
    and checked post hoc): tau is omega, the cusp or flat in every closed-form sector; at omega a joint-parity boson's
    line goes to the 3-torsion points, which only coloured fields see"""
    import sys
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_one_loop_potential_on_the_fibre.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"K1": True, "K2": True, "K3": True, "K4": False, "K5": True}
    assert d["K1"]["the largest difference"] < 1e-12
    assert d["K2"]["zeta_Sigma(0) from the cone coefficients"] == "-3/2"
    k3 = d["K3"]
    assert k3["(a) log(y|eta|^4)"]["rho"]["type"] == "maximum" and k3["(b) E(tau, 3)"]["rho"]["type"] == "minimum"
    assert all(abs(r["joint / E(tau, 3)"] + 15 / 16) < 1e-12 for r in k3["(c) the joint parity sum against E(tau, 3)"])
    om = d["K4"]["omega, boson"]
    mins = sorted((p["value"], tuple(p["psi"])) for p in om if p["type"] == "minimum")
    assert len(om) == 12 and abs(mins[0][0] - mins[1][0]) < 1e-9 and mins[2][0] - mins[0][0] > 0.1
    assert {tuple(round(x, 6) for x in m[1]) for m in mins[:2]} == {(0.333333, 0.333333), (0.666667, 0.666667)}
    assert all(v == ["Q", "d^c", "u^c"] for v in d["K5"]["twisted at each nonzero 3-torsion line"].values())
    ph = json.loads((here / "the_one_loop_potential_on_the_fibre_posthoc.json").read_text(encoding="utf-8"))
    for N in ("48", "240"):
        assert min(ph["PH1"]["omega"]["at the symmetric points, by truncation N"][N]["(1/2, 0)"]
                   ["Hessian eigenvalues"]) > 2
    assert ph["PH2"]["d^c and e^c differ on every line"] is True
    # in process: the twisted determinant by both routes at one point, and the joint parity identity at s = 3
    sys.path.insert(0, str(here))
    import the_one_loop_potential_on_the_fibre as OP
    t = 0.21 + 1.05j
    assert abs(OP.logdet_cs(t, 0.3, 0.7) - OP.logdet_theta(t, 0.3, 0.7)) < 1e-12
    m, n, w = OP.lattice(t, 200)
    joint = float(sum(OP.np.sum(OP.np.cos(2 * OP.np.pi * (m * u + n * v)) * w) for u, v in OP.PARITIES))
    assert abs(joint / OP.E3(t) + 15 / 16) < 1e-8



def test_w60_the_quark_sector_and_the_line():
    """W60 (the owner's "W60: quark sector"; the rule first; one run; P2-P4 as predicted, P1 failed as worded, a 0/0,
    re-scored post hoc): the quarks resist the colour-centre line; post hoc, the full potential sits on a half-period
    line, where the matter sees nothing and one parity copy of the Higgs is untwisted"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_quark_sector_and_the_line.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"P1": False, "P2": True, "P3": True, "P4": True}
    rows = d["P1"]["N = 192"]["rows"]
    assert max(r["|diff|"] for r in rows) < 1e-8
    assert max(r["relative diff"] for r in rows if abs(r["exact"]) > 1e-6) < 5e-4
    f6 = d["P4"]["the fermion's six-dimensional potential (-Delta V6) at N = 192"]
    assert f6["0"] == 0.0 and f6["(1/6, 1/6)"] > f6["(1/4, 0)"] > 0.4
    assert abs(f6["(1/6, 1/6)"] - f6["(1/3, 1/3)"]) < 1e-9
    ph = json.loads((here / "the_quark_sector_and_the_line_posthoc.json").read_text(encoding="utf-8"))
    assert ph["PH2"]["the fit's largest residual on the grid"] < 1e-6
    for name, v in ph["PH3"].items():
        if "alone" in name:
            assert abs(v["its value"]) < 1e-6
            continue
        assert abs(v["its value"] + 147.6387) < 1e-3 and v["d^c and e^c see different twists"] is False
        assert all(abs(c - round(2 * c) / 2) < 1e-6 for c in v["the global minimum w"])



def test_w61_the_couplings_at_the_selected_state():
    """W61 (the owner's "W61: the couplings"; the rule first; one run; every cell as predicted): at W60's state the
    Yukawas vanish in the T (x) T reading and are three degenerate generations without mixing in the T-bar (x) T one"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_couplings_at_the_selected_state.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"Q1": True, "Q2": True, "Q3": True}
    for key, v in d["Q2"].items():
        if key == "holds":
            continue
        ys = [r["T-bar x T: Y"] for r in v.values()]
        assert all(y == ys[0] for y in ys)
        for r in v.values():
            assert r["T x T: largest |Y|"] < 1e-12
            sv = r["T-bar x T: singular values"]
            assert max(sv) - min(sv) < 1e-12
    n96, n48 = d["Q3"]["N(omega) with 96 and 48 points"]
    assert abs(n96 / n48 - 1) < 1e-10
    # in process: three distinct units of the quaternion group multiply to +-1
    import numpy as np
    i, j = np.array([[1j, 0], [0, -1j]]), np.array([[0, 1], [-1, 0]], dtype=complex)
    k = i @ j
    for prod in (i @ j @ k, j @ k @ i, i @ k @ j):
        assert np.allclose(prod, prod[0, 0] * np.eye(2)) and abs(abs(prod[0, 0]) - 1) < 1e-12


def test_w62_the_matter_and_the_shape():
    """W62 (the owner's "W62, as recommended"; the rule first; one run; A1 failed as worded at one sample point, where
    tau + 1 is omega's mirror): the matter's six-dimensional term is not a multiple of E(tau, 3) but keeps its critical
    points; the Higgs's copies at the selected line break the modular group; every content on record runs to a cusp"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_matter_and_the_shape.json").read_text(encoding="utf-8"))
    cells = {"M0": True, "M1": True, "M2": True, "M3": True, "M4": True, "M5": True, "M6": True, "A1": False,
             "A2": True, "A3": True}
    assert d["cells"] == cells and d["every cell holds"] is False
    big = d["the values (W59 units, against the reference)"]["4n"]
    for name, v in big.items():
        if name.startswith(("axis", "arc")):
            assert v["dD"] * v["dV_per exact"] < 0 and abs(v["dD"]) < abs(v["dV_per exact"])
    for content in d["read-outs"]["the contents"].values():
        for line, row in content.items():
            if not line.startswith("the lowest"):
                assert row["stable at that cusp"] is False
    ph = json.loads((here / "the_matter_and_the_shape_posthoc.json").read_text(encoding="utf-8"))
    assert ph["PH1"]["A1 holds at every point where T is not the mirror"] is True
    assert abs(ph["PH2"]["4n"]["E2 alone: coefficient / (31/1024)"] + 1) < 0.02
    # in process: the comb's cusp coefficient is -(31/512) zeta(6), and the Higgs's copies at w = (1/2, 1/2) sum to
    # E/16 - S_(1/2,1/2) term by term (1 + (-1)^m + (-1)^n + (-1)^(m+n) = 4 on even pairs)
    import math
    z6 = math.pi ** 6 / 945
    row = sum((2.0 if m % 4 == 0 else -2.0) / m ** 6 for m in range(-4000, 4001) if m != 0 and m % 2 == 0)
    assert abs(row + 31 / 512 * z6) < 1e-12
    for m in range(-3, 4):
        for n in range(-3, 4):
            assert 1 + (-1) ** m + (-1) ** n + (-1) ** (m + n) == (4 if m % 2 == 0 and n % 2 == 0 else 0)


def test_w63_b1644_verified():
    """W63 (the owner's "Verify B1644"; the rule first; one run; V1 failed as worded on its branch clause only, as the
    seat disclosed before the run): main's B1644 and B1645 hold on the seat's own instruments, and the record's Higgs is
    a real unit direction with m >= 1/2 (exactly 1/2 on the imaginary axis)"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "b1644_verified.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"V1": False, "V2": True, "V3": True, "V4": True, "V5": True, "V6": True}
    for name, v in d["V1"].items():
        if name == "holds":
            continue
        assert v["contour against closed forms (relative)"] < 1e-20 and v["R against main's table (relative)"] < 1e-20
        assert v["W21 continuation sign"] == 1 and len(set(v["W21 principal-root signs at 20 contour points"])) == 2
    for name in ("i", "1.5i", "2.0207i", "4i"):
        assert abs(d["V5"][name]["k"] - 0.5) < 1e-10
    assert all(r["largest difference"] < 1e-7 for r in d["V6"]["rows"])
    # in process: Jacobi's theta_3^4 = theta_2^4 + theta_4^4 makes the residue triplet isotropic, and B1645's form
    # follows from the units' table for any linear rho with rho(1) = 0
    import mpmath as mp
    q = mp.exp(-mp.pi * mp.mpf("1.3"))
    t2, t3, t4 = (mp.jtheta(n, 0, q) for n in (2, 3, 4))
    assert abs(t2 ** 4 + t4 ** 4 - t3 ** 4) < mp.mpf(10) ** -12
    import numpy as np
    qi, qj = np.array([[1j, 0], [0, -1j]]), np.array([[0, 1], [-1, 0]], dtype=complex)
    e = [qi, qj, qi @ qj]
    rng = np.random.default_rng(63)
    R = rng.normal(size=3) + 1j * rng.normal(size=3)

    def rho(X):  # linear, rho(1) = 0, rho(e_u) = R_u, read off X = c0 1 + sum c_u e_u
        return sum(R[u] * (np.trace(np.linalg.inv(e[u]) @ X) / 2) for u in range(3))

    a = rng.normal(size=3) + 1j * rng.normal(size=3)
    Y = np.array([[sum(a[u] * rho(-e[p] @ e[u] @ e[q]) for u in range(3)) for q in range(3)] for p in range(3)])
    assert np.allclose(Y, np.outer(a, R) + np.outer(R, a) - (a @ R) * np.eye(3), atol=1e-12)


def test_w64_the_cusp_unit_as_a_vector():
    """W64 (the owner's "follow that lead properly", "Both frames"; the rule first; one run; K2, K4 and K5 failed as
    worded on one instrument error, the theta_2 branch, and hold post hoc): the cusp's quarter-turn on M, R as the one
    section with a single unit on the cusp's isotropic eigenline, sections numbering sum(u), and the anisotropy's points
    on the cone"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_cusp_unit_as_a_vector.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"K1": True, "K2": False, "K3": True, "K4": False, "K5": False, "K6": True, "K7": True}
    assert d["K1"]["their orbits' sizes"] == [6, 8, 12] and d["K1"]["the special isotropic lines"] == 26
    ph = json.loads((here / "the_cusp_unit_as_a_vector_posthoc.json").read_text(encoding="utf-8"))
    assert ph["re-scored"] == {"K2": True, "K4": True, "K5": True}
    for key in ("PH3 (K4 re-scored)", "PH3 (K5 re-scored)"):
        for u, row in ph[key]["placements"].items():
            assert row["dimension (collocation)"] == sum(int(c) for c in u if c.isdigit())
    assert ph["PH3 (K4 re-scored)"]["R against the null vector (u = (0, 1, 0)), largest relative difference"] < 1e-10
    # in process: the record's L (a -> a, b -> ab) turns the units a quarter-turn about i, and its eigenline
    # v+ = e_j - sqrt(-1) e_k is isotropic with eigenvalue sqrt(-1)
    import numpy as np
    L = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    v = np.array([0, 1, -1j])
    assert np.allclose(L @ v, 1j * v) and abs(v @ v) < 1e-15


def test_w65_the_second_unit():
    """W65 (the goal "resume"; the rule first; one run after one disclosed failed launch; all six cells as predicted):
    the Higgs's direction as a section of weight -1/2 in rho_R; E, R and R' generate every placement with an integer
    Gram matrix in j and E4^2/eta^18; at omega every section lies on one 8-orbit line and m = 0; the cusp's e^{-pi y}"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_second_unit.json").read_text(encoding="utf-8"))
    assert d["cells"] == {f"H{k}": True for k in range(1, 7)}
    h2, ro = d["H2"], d["read-outs"]
    assert abs(h2["E.R'/Phi (fitted at 2i)"][0] - 112) < 1e-20
    assert abs(h2["E.E/Phi = a j + b: a"][0] - 1) < 1e-20 and abs(h2["E.E/Phi = a j + b: b"][0] + 1280) < 1e-20
    assert max(h2["largest relative error over the sample (relative to |f||g|)"].values()) < 1e-30
    assert d["H3"]["omega"]["R(omega)'s orbit size"] == 8 and d["H3"]["i"]["the two lines' orbit sizes"] == [12, 12]
    assert max(d["H4"]["m at omega (every placement's combination, E, R')"].values()) < 1e-30
    assert abs(ro["m_E along tau = iy, y = 1 to 8 by 0.25"][0] - 9 / 14) < 1e-12
    assert abs(abs(complex(*ro["tau_0 (E on the cone)"])) - 1) < 1e-12
    # in process: main's R at tau = i lies on the 12-orbit line of (1, 1, -sqrt(-1) sqrt 2), from the theta series
    import sys
    import mpmath as mp
    sys.path.insert(0, str(here))
    import the_cusp_unit_as_a_vector_posthoc as PH
    r = PH.Rdirect(mp.mpc(0, 1))
    line = [1, 1, -1j * mp.sqrt(2)]
    assert all(abs(r[k] * line[0] - r[0] * line[k]) < 1e-20 * abs(r[0]) for k in range(3))
    # and the Gram determinant of the integers: -4 (j - 1728), zero at i
    import sympy as sy
    j = sy.symbols("j")
    assert sy.expand(sy.Matrix([[j - 1280, 4, 112], [4, 0, 2], [112, 2, 0]]).det()) == -4 * j + 6912


def test_w66_the_parameter_free_census():
    """W66 (the goal "resume"; the rule first; one run; all three cells as predicted): B1644's form with the Higgs and
    the coupling among the one-unit sections, every assignment of the six pairs to the three sectors, fitted at one
    tau. None passes (the best chi^2 is 260 at a = 0.10), so the parameter-free sections do not fix tau by the data"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_parameter_free_census.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"C1": True, "C2": True, "C3": True} and d["instrument holds (10^-10)"]
    assert d["C3"]["the smallest chi2_min of all 216"] > 7.81
    ro = d["read-outs"]
    assert ro["assignments passing (chi2_min <= 7.81) at a = 0.10, 0.05, 0.20"] == {"0.1": 0, "0.05": 0, "0.2": 0}
    assert len(ro["the six permutations at a = 0.10"]) == 6 and ro["assignments refined at a = 0.10"] == 18
    # in process: for a non-isotropic E, Y = 2 E E^T - (E.E) 1 is (E.E) times a complex orthogonal matrix, so its
    # singular values satisfy m1 m3 = m2^2
    import numpy as np
    rng = np.random.default_rng(66)
    e = rng.normal(size=3) + 1j * rng.normal(size=3)
    s = np.linalg.svd(2 * np.outer(e, e) - (e @ e) * np.eye(3), compute_uv=False)
    assert abs(s[0] * s[2] / s[1] ** 2 - 1) < 1e-10


def test_w67_the_potential_fixes_tau():
    """W67 (the goal "resume"; the rule first; one run; F1 and F3 failed as worded on R' alone, F2 held; a labelled post
    hoc): the weave's quartic on the parameter-free Higgs sections fixes tau at omega for R (c > 0) or runs to the
    cusp (c < 0); R' also reaches the 8-orbit lines at j = 336 -+ 192 sqrt 7 (identified to 12 digits)"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_potential_fixes_tau.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"F1": False, "F2": True, "F3": False}
    assert d["F1"]["R"]["all at omega"] and not d["F1"]["R'"]["all at omega"]
    census = d["F3"]["census"]
    for key, row in census.items():
        name, rest = key.split(", ", 1)
        c = float(rest.split("c = ")[1])
        if name == "R":
            assert row["where"] == ("omega" if c > 0 else "runs to the cusp"), key
        if name == "E" and c > 0 and "lambda2 = 0.0" not in key:
            assert row["where"] == "omega", key
    ph = json.loads((here / "the_potential_fixes_tau_posthoc.json").read_text(encoding="utf-8"))
    assert ph["PH2 (1/2 - qA along tau = iy)"]["strictly below 1/2 and rising toward it, for both"]
    import math
    js = sorted(r["j at the root"][0] for r in ph["PH1 (R''s extra 8-orbit points)"])
    assert all(r["qA(R'(root)) - 1/3"] < 1e-25 for r in ph["PH1 (R''s extra 8-orbit points)"])
    assert abs(js[0] - (336 - 192 * math.sqrt(7))) < 1e-9 and abs(js[1] - (336 + 192 * math.sqrt(7))) < 1e-9
    # in process: the anisotropy's floor, qA >= 1/3 (Cauchy-Schwarz), with equality on the 8-orbit line (1, w, w^2)
    import numpy as np
    rng = np.random.default_rng(67)
    for _ in range(100):
        a = rng.normal(size=3) + 1j * rng.normal(size=3)
        assert np.sum(np.abs(a) ** 4) / np.vdot(a, a).real ** 2 >= 1 / 3 - 1e-15
    w = np.exp(2j * np.pi / 3)
    a = np.array([1, w, w * w])
    assert abs(np.sum(np.abs(a) ** 4) / np.vdot(a, a).real ** 2 - 1 / 3) < 1e-15 and abs(a @ a) < 1e-14


def test_w68_the_residual_charges_at_omega():
    """W68 (the goal "resume"; the rule first, G4 corrected before any code; one run; all four cells as predicted): the
    weights -1/2, 3/2 and 7/2 put the parameter-free sections at omega on the three eigenlines of its stabiliser, and
    the pairing fixes the powers of delta = |tau - omega|: delta^2 : delta : 1 for E with the weight 7/2 section"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_residual_charges_at_omega.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"G1": True, "G2": True, "G3": True, "G4": True}
    assert len(d["G1"]["the sections kept (distinct)"]) == 7
    pair = d["read-outs"]["every pair"]["k = -1/2, u = (1, 0, 0) | k = 7/2, u = (0, 0, 0)"]
    p1, p2 = pair["p1 (1e-4 to 1e-3), (1e-3 to 1e-2)"][0], pair["p2 (1e-4 to 1e-3), (1e-3 to 1e-2)"][0]
    assert abs(p1 - 2) < 1e-2 and abs(p2 - 1) < 1e-2
    c = pair["coefficients"]
    assert abs(c["m1/m3 / delta^p1 at 1e-4"] / c["m2/m3 / delta^p2 at 1e-4"] ** 2 - 15) < 1e-6
    # in process: the stabiliser's rotation M (e_i -> -e_j, e_j -> e_k, e_k -> -e_i) has eigenvalue
    # sqrt(-1) e^{-i pi k/3} on the line each weight lands on: omega at -1/2, 1 at 3/2, omega^2 at 7/2
    import numpy as np
    M = np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]])
    w = np.exp(2j * np.pi / 3)
    lines = {-0.5: np.array([-w, 1, w * w]), 1.5: np.array([1, -1, -1]), 3.5: np.array([-w * w, 1, w])}
    for k, v in lines.items():
        lam = 1j * np.exp(-1j * np.pi * k / 3)
        assert np.allclose(M @ v, lam * v)


def test_w69_the_weighted_census():
    """W69 (the goal "resume"; the rule first; one run; all three cells as predicted): every pair of the seven
    parameter-free sections at the weights -1/2, 3/2 and 7/2, 21 952 assignments, fitted at one tau: none passes"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_weighted_census.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"J1": True, "J2": True, "J3": True}
    ro = d["read-outs"]
    assert ro["assignments"] == 28 ** 3 and ro["assignments passing at a = 0.10"] == 0
    assert all(v["assignments passing"] == 0 for v in ro["a = 0.05 and 0.20"].values())
    assert 99 < d["J3"]["the smallest refined chi2_min"] < 101
    # W66's true best (259.9, a non-permutation) is the best over weight -1/2 alone here too
    w66 = json.loads((here / "the_parameter_free_census.json").read_text(encoding="utf-8"))
    assert abs(ro["the best chi2_min by weight (a = 0.10)"]["only weight -1/2"]
               - w66["C3"]["the smallest chi2_min of all 216"]) < 1e-6


def test_w70_the_cusp_condensate_charge_map():
    """W70 (the owner's "Cusp condensate"; P024's first test; the rule first; one run; all five cells as predicted): the
    admissible hypercharge in the audit lane's E8 embedding is unique up to permuting the three quaternion units, and
    under it the lane's cusp condensate is the neutral component of a Y = -1/2 doublet, leaving SU(3)_c x U(1)_em"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_cusp_condensate_charge_map.json").read_text(encoding="utf-8"))
    assert d["cells"] == {f"N{k}": True for k in range(1, 6)}
    assert sorted(map(tuple, d["N2"]["admissible"])) == sorted(
        tuple(p) for p in __import__("itertools").permutations(("1/6", "-5/6", "2/3")))
    assert d["N5"]["neutral under"] == ["1/6,2/3,-5/6"]
    ro = d["read-outs"]
    assert ro["the Standard Model roots kept by E_alpha (colour, weak)"] == {"colour": 6, "weak": 0}
    assert ro["the Standard Model Cartan directions kept (of colour 2, T3, Y)"] == 3
    # in process: the hand derivation behind N2 -- with block charges (y1, y2, y3) summing to zero, Q needs a 1/6,
    # u^c a pair sum -2/3, d^c a pair sum 1/3, L a triple sum -1/2 and e^c a difference 1
    from fractions import Fraction as Fr
    from itertools import combinations, permutations
    sols = set()
    for a in range(-12, 13):
        for b in range(-12, 13):
            y = (Fr(a, 6), Fr(b, 6), Fr(-a - b, 6))
            six = [y[0], y[0], y[1], y[1], y[2], y[2]]
            pairs = {six[i] + six[j] for i, j in combinations(range(6), 2)}
            triples = {six[i] + six[j] + six[k] for i, j, k in combinations(range(6), 3)}
            diffs = {six[i] - six[j] for i in range(6) for j in range(6) if i != j}
            if (Fr(1, 6) in six and Fr(-2, 3) in pairs and Fr(1, 3) in pairs and Fr(-1, 2) in triples
                    and 1 in diffs):
                sols.add(y)
    assert sols == set(permutations((Fr(1, 6), Fr(-5, 6), Fr(2, 3))))


def test_w70_posthoc_the_hypercharge_normalisation():
    """W70's post hoc (labelled; at main's S122 ask): the hypercharge the quaternion holonomies keep has k_Y = 14/3,
    and the standard SU(5)-type hypercharge (k_Y = 5/3) splits a block, so the holonomies break it"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_cusp_condensate_charge_map_posthoc.json").read_text(encoding="utf-8"))
    assert d["PN1"]["the distinct values"] == ["14/3"] and len(d["PN1"]["per admissible Y"]) == 6
    assert d["PN2"]["k_Y by the Cartan norms"] == "5/3" and d["PN2"]["block-scalar"] is False
    assert all(d["PN2"]["the five field conditions"].values())
    assert d["PN3"]["per k_Y"]["14/3"]["above M_Z"] is False
    # in process: with sum c = 0 and the 6's Gram matrix delta_ij - 1/6, |sum_k c_k ws_k|^2 = sum_k c_k^2
    from fractions import Fraction as Fr
    c = [Fr(1, 6), Fr(1, 6), Fr(-5, 6), Fr(-5, 6), Fr(2, 3), Fr(2, 3)]
    norm = sum(ci * cj * ((1 if i == j else 0) - Fr(1, 6)) for i, ci in enumerate(c) for j, cj in enumerate(c))
    assert norm == sum(x * x for x in c) == Fr(7, 3) and norm / Fr(1, 2) == Fr(14, 3)


def test_w71_the_field_free_end():
    """W71 (P024's second test; the rule first; one run; all five cells as predicted): on the weave's forced quaternion
    holonomies, flat end data that gap every channel exist (the double twist, a generic R-holonomy, a weak Wilson line);
    with SU(3)_c x U(1)_em kept and gauge data only, the end stays bare"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_field_free_end.json").read_text(encoding="utf-8"))
    assert d["cells"] == {f"E{k}": True for k in range(1, 6)}
    e1 = d["E1"]["per twist"]
    assert e1["0,0"]["gapless per spin line"] == [448] * 4 and e1["1,1"]["gapless per spin line"] == [0] * 4
    e2 = d["E2"]["per class"]
    assert [n for n, v in e2.items() if v["U(1)_em kept (all six admissible Y)"]] == ["trivial"]
    assert e2["trivial"]["gapless"] == 448 and e2["generic in F4's torus"]["gapless"] == 64
    assert d["E3"]["per twist and R class"]["0,0 / generic"]["gapless"] == 0
    assert d["E5"]["gauge-only classes that gap every channel and keep U(1)_em"] == []
    # in process: the cusp rule at the bare end -- an untwisted slot (half-integer s, so the bounding spin gives -1) on
    # a channel with p = -1 is periodic with zero drift; the p-odd channels are the weak doublets, 112 of the 240 roots
    from itertools import combinations, product
    roots = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-2, 2), repeat=2):
            v = [0] * 8
            v[i], v[j] = a, b
            roots.add(tuple(v))
    for signs in product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.add(signs)
    assert len(roots) == 240                                   # doubled coordinates
    doublets = [r for r in roots if abs(r[3] - r[4]) == 2]     # r.(e3 - e4) = +-1
    assert len(doublets) == 112 and 4 * len(doublets) == e1["0,0"]["gapless per spin line"][0]


def test_w72_the_surface_yukawa():
    """W72 (main's S122 assignment; the rule first; one run after one failed launch; X1 and X4 as predicted, X2, X3 and
    X5 failed as worded on instruments and were confirmed by two labelled post hocs): in the surface frame B1644's
    coupling has no residue at the cusp, and its Petersson pairing with the Higgs's surface mode has rank 3"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_surface_yukawa.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"X1": True, "X2": False, "X3": False, "X4": True, "X5": False, "X6": False}
    assert d["X3"]["null count"] == 1 and abs(d["X3"]["chi_5/2(rho')"] - 1) < 1e-9
    assert d["X4"]["agreement of the two settings"] < 1e-8 and d["X4"]["smallest over largest"] > 1e-6
    p1 = json.loads((here / "the_surface_yukawa_posthoc.json").read_text(encoding="utf-8"))
    assert p1["cells"] == {"PH1": False, "PH2": True, "PH3": True}
    p2 = json.loads((here / "the_surface_yukawa_posthoc2.json").read_text(encoding="utf-8"))
    assert p2["cells"] == {"PH4": True, "PH5": True}
    assert all(w.endswith(":R") for w, _, _ in p2["PH4"]["the small ones (what, deg, size)"])
    # in process: the multiplier class -- B[l].B[l'] is non-zero only on (e_i, e_i) and (v+, v-), whose exponents
    # (in eighths: e_i 1, v+ 7, v- 3) sum to 2 mod 8, so a quartic contraction sits at 4 mod 8 (no constant term)
    B = {"e_i": (1, 0, 0), "v+": (0, 1, -1j), "v-": (0, 1, 1j)}
    ex = {"e_i": 1, "v+": 7, "v-": 3}
    pairs = [(a, b) for a in B for b in B if abs(sum(x * y for x, y in zip(B[a], B[b]))) > 0]
    assert sorted(pairs) == [("e_i", "e_i"), ("v+", "v-"), ("v-", "v+")]
    assert all((ex[a] + ex[b]) % 8 == 2 for a, b in pairs)


def test_w73_the_end_normalisation():
    """W73 (H-end, chosen after W72 was read and disclosed; the rule first; one run; all four cells as predicted): the
    surface frame's three modes, normalised by the cusp's pairing of their units, give 1 : 0.019 : 0.0004; with one
    coupling W66's predicate fails, and the down sector's closeness is not significant"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_end_normalisation.json").read_text(encoding="utf-8"))
    assert d["cells"] == {f"Z{k}": True for k in range(1, 5)}
    assert d["Z2"]["chi2 (three m2/m3)"] > 7.81 and d["Z4"]["p"] > 0.05
    # in process: rescale W72's stored Y by K = diag(1, 2, 2) and recompute the two ratios
    import numpy as np
    w = json.loads((here / "the_surface_yukawa.json").read_text(encoding="utf-8"))
    Y = np.array([[complex(*z) for z in row] for row in w["X4"]["Y (Y0 = 2.0)"]])
    D = np.diag([1, 2 ** -0.5, 2 ** -0.5])
    sv = np.linalg.svd(D @ Y @ D, compute_uv=False)
    assert abs(sv[1] / sv[0] - d["Z1"]["m2/m3"]) < 1e-12 and abs(sv[2] / sv[0] - d["Z1"]["m1/m3"]) < 1e-12


def test_w74_the_surface_cp():
    """W74 (the rule first; one run; all three cells as predicted): the surface frame is CP-invariant, so its Yukawas
    are real; with one coupling arg det(M_u M_d) = 0 (theta-bar = theta) and J = 0"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_surface_cp.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"V1": True, "V2": True, "V3": True}
    # in process: the involution's matrix identities and the S-phase condition at the record's weights
    import cmath
    import numpy as np
    C = np.diag([1, 1, -1])
    Linv = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    P = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    assert (C @ np.linalg.inv(Linv) @ C == Linv).all() and (C @ P @ C == P).all()
    def ok(k, ph):
        return abs(cmath.exp(-1j * cmath.pi * (k + ph)) - cmath.exp(1j * cmath.pi * ph))
    assert all(ok(k, 0.25) < 1e-12 for k in (-0.5, 1.5, 3.5)) and ok(2.5, 0.75) < 1e-12
    assert ok(0.5, 0.25) > 0.1 and ok(1.0, 0.25) > 0.1


def test_w75_the_puncture_scale():
    """W75 (the rule first; one run; all four cells as predicted): the weave's chiral threads carry CS in mirror
    pairs (745 threads), and at weight zero the field at a genuine cusp is the uniformization, of size 1/(2R)"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_puncture_scale.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"U1": True, "U2": True, "U3": True, "U4": True}
    assert d["U1"]["threads"] == 745 and d["U1"]["K1 reproduced: threads with |CS| > 1e-6"] == 690
    assert d["U4"]["pointwise norm on unit vectors"] == "1/(2*R)"
    # in process: the linear branch solves u'' + e^(-2u) = 0, and N = [[-1/L, -1/L^2], [1, 1/L]] is nilpotent
    import sympy as sp
    s, L0, L = sp.symbols("s L0 L", positive=True)
    u = sp.log(s - L0)
    assert sp.simplify(sp.diff(u, s, 2) + sp.exp(-2 * u)) == 0
    N = sp.Matrix([[-1 / L, -1 / L ** 2], [1, 1 / L]])
    assert (N * N).applyfunc(sp.simplify) == sp.zeros(2, 2) and N.trace() == 0


def test_w76_the_weaves_bit():
    """W76 (the rule first; one run; all four cells as predicted): every mirror-symmetric thread to length 16 has
    Chern-Simons exactly 0, never pi^2/2"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_weaves_bit.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"B0": True, "B1": True, "B2": True, "B3": True}
    assert d["B0"]["threads"] == 8798 and d["B1"]["bits"] == {"0": 248}
    # in process: the mirror-symmetric words among the stored threads, recounted from the words alone
    def lr(w):
        return min(w[i:] + w[:i] for i in range(len(w)))
    sym = [w for w in d["threads"] if lr(w.translate(str.maketrans("LR", "RL"))) in (w, lr(w[::-1]))]
    assert len(sym) == 248 and max(abs(d["threads"][w]) for w in sym) < 1e-8


def test_w77_the_odd_form_review():
    """W77 (the rule first; one run; all five cells as predicted): the audit lane's odd form reviewed; the cross form
    {V, H} = K3 E3 + K4 E4, and K3, K4 of norm 1/ell reversing GammaV"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_odd_form_review.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"R1": True, "R2": True, "R3": True, "R4": True, "R5": True}
    assert d["R2"]["cubic c1c3c4 coefficient"] == "1/(4*ell)" and d["R5"]["largest identity residual"] < 1e-6
    # in process: K3 = (c2c3 - c1c4)/2 and K4 = -(c2c4 + c1c3)/2 at ell = 1, in the lane's own gamma matrices
    import numpy as np
    p1 = np.array([[0, 1], [1, 0]]); p2 = np.array([[0, -1j], [1j, 0]]); p3 = np.diag([1, -1]); i2 = np.eye(2)
    c1, c2, c3, c4 = (1j * np.kron(p1, i2), 1j * np.kron(p2, i2), 1j * np.kron(p3, p1), 1j * np.kron(p3, p2))
    gv = 1j * c3 @ c4
    for K in ((c2 @ c3 - c1 @ c4) / 2, -(c2 @ c4 + c1 @ c3) / 2):
        assert np.allclose(K.conj().T, -K) and np.allclose(gv @ K + K @ gv, 0)
        assert np.allclose(sorted(np.linalg.eigvalsh(K.conj().T @ K)), [0, 0, 1, 1])


def test_w78_the_weight_three_refined():
    """W78 (the rule first; one run; N1 and N2 failed as worded; a labelled post hoc): no structure with a sector at
    weight 3 fits on this seat's model up to Im tau = 10, and at main's tau the model stays far above main's fits"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_weight_three_refined.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"N0": True, "N1": False, "N2": False, "N3": True, "N4": True}
    table = d["the structures"]
    assert len(table) == 16 and not any(v["fits"] for v in table.values())
    ph = json.loads((here / "the_weight_three_refined_posthoc.json").read_text(encoding="utf-8"))
    assert ph["PH1 (5, 7, 3) at main's tau"]["total"] > 100
    assert ph["PH3 each sector alone at weight 3"]["u"]["chi^2_min"] > 1
    assert ph["PH3 each sector alone at weight 3"]["d"]["chi^2_min"] < 1e-12
    # in process: the sixteen structures are exactly those with a weight 3 and (k_u, k_d) != (3, 3)
    import itertools
    want = {str(ks) for ks in itertools.product((3, 5, 7), repeat=3) if 3 in ks and ks[:2] != (3, 3)}
    assert set(table) == want


def test_w79_the_two_seats_weight_three():
    """W79 (the rule first; one run; C3 as predicted, C1 and C2 failed as worded; two labelled post hocs): the two
    seats' triplets are isomorphic, and main's forms drift from this seat's like |eta|^-18 near the cusp"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_two_seats_weight_three.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"C1": False, "C2": False, "C3": True}
    assert d["C1"]["verdict"] == "isomorphic to rho_theta"
    ph = json.loads((here / "the_two_seats_weight_three_posthoc2.json").read_text(encoding="utf-8"))
    import math
    assert abs(ph["PH3"]["slope of log(angle) against Im tau"] - 1.5 * math.pi) < 0.01
    # in process: main's rho_theta T-exponents are 1/8, 3/8, 7/8
    import cmath
    import numpy as np
    P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    rT = cmath.exp(7j * math.pi / 4) * np.diag([1j, 1, 1]) @ P23
    ex = sorted(round(float(np.angle(z) / (2 * math.pi)) % 1.0, 9) for z in np.linalg.eigvals(rT))
    assert ex == [0.125, 0.375, 0.875]


def test_w80_the_main_fits_precise():
    """W80 (the rule first; one run; all five cells as predicted, Z3 only as worded): main's B1637 optimizer on this
    seat's precise forms keeps the control exact and loses every weight-3 fit main found near Im tau 6.7-7.1"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_main_fits_precise.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"Z0": True, "Z1": True, "Z2": True, "Z3": True, "Z4": True}
    assert d["main's code"]["ref"] == "60c5470ae" and d["main's code"]["NSTART"] == 60
    assert d["Z0"]["chi2_min"] < 1e-6 and 3.0 <= d["Z0"]["tau"][1] <= 3.8
    assert d["Z1"]["chi2_min"] > 300 and d["Z2"]["chi2_min"] > 800 and d["Z4"]["chi2_min"] > 300
    assert d["Z3"]["chi2_min"] < 1e-6 and d["Z3"]["tau"][1] > 8      # the up sector alone fits, beyond Im tau 8
    assert d["read-outs"]["(7, 7, 3) on all 13"]["chi2_min"] > 100
    assert all(j["P"] >= 21 for j in d["jobs"] if j["ckm"])
    note = (here / "NOTE.md").read_text(encoding="utf-8")
    assert "## W80." in note and note.count("Withdrawn the same day after") >= 3

def test_w81_the_lane_su2_branching():
    """W81 (the script first; one run; B1, B2, B4 as predicted, B3 failed as worded, a sign): the 248 under the
    continuous SU(2) of the quaternion Cartan is 55 + 52x2 + 27x3 + 2x4, and the condensate's root lies in the doublets"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_lane_su2_branching.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"B1": True, "B2": True, "B3": False, "B4": True}
    assert d["irreps (dimension: copies)"] == {"1": 55, "2": 52, "3": 27, "4": 2} and d["embedding index"] == 3
    assert d["H_Q(beta)"] == "1" and d["beta: the doublet test"]["in the doublets"] is True
    # in process: the H_Q weights of the 248 from the lane's weights of the 6, exactly
    import importlib.util
    from collections import Counter
    spec = importlib.util.spec_from_file_location("w81_cm", here / "the_cusp_condensate_charge_map.py")
    cm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cm)
    m = Counter([int(cm.dot(r, cm.HQ)) for r in cm.RR] + [0] * 8)
    assert {n + 1: m[n] - m[n + 2] for n in range(4)} == {1: 55, 2: 52, 3: 27, 4: 2}
    note = (here / "NOTE.md").read_text(encoding="utf-8")
    assert "## W81." in note and "Settled 2026-10-14 by that audit, dd2a54119" in note

def test_w82_the_tribunal_checks():
    """W82 (the script first; one run; every cell as predicted): lemma A needs both halves (V4 and S3); the 112's
    neutral |Y| = 1/2 condensates are one SU(2)_Q doublet and its conjugate under every admissible Y"""
    here = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((here / "the_tribunal_checks.json").read_text(encoding="utf-8"))
    assert d["cells"] == {"L1": True, "L2a": True, "L2b": True}
    assert d["L1"]["commutant dimensions"] == {"V4 and S3": 1, "S3 alone": 2, "V4 alone": 3,
                                              "V4 and one transposition (non-transitive)": 2}
    rows = d["L2"]["per admissible Y"]
    assert len(rows) == 6 and all(len(v) == 4 for v in rows.values())
    # in process: the four roots of every admissible Y are two +- pairs (one condensate and its conjugate)
    for v in rows.values():
        rs = {tuple(r["root"]) for r in v}
        neg = {tuple(("-" + x) if not x.startswith("-") and x != "0" else x.lstrip("-") for x in r) for r in rs}
        assert rs == neg
    note = (here / "NOTE.md").read_text(encoding="utf-8")
    assert "## W82." in note
    relay = (ROOT / "SM_TO_CC_AND_CODEX_2026-10-07_THE_CHIRAL_TRIPLETS_COUNT.md").read_text(encoding="utf-8")
    assert "## 101." in relay and "split the down quarks" in relay

def test_the_owners_rulings_page():
    """The owner's rulings of 2026-10-08 (four forks, in the order the seat proposed): each ruling is on the page with
    its tag, and the page keeps the forks it did not rule open"""
    page = (ROOT / "docs" / "THE_OWNERS_RULINGS_2026-10-08.md").read_text(encoding="utf-8")
    for choice in ('"Even ticks observed."', '"Tagged working postulate."', '"Flat counts only."', '"Keep positivity."'):
        assert choice in page, choice
    for tag in ('"on the even-tick branch"', '"given Λ"', '"a flat count"'):
        assert tag in page, tag
    assert "GENESIS FK11 stays formally open" in page and "0 of 19" in page
    state = (ROOT / "docs" / "THE_THREE_GENERATIONS_STATE_2026-10-08.md").read_text(encoding="utf-8")
    assert "THE_OWNERS_RULINGS_2026-10-08.md" in state
