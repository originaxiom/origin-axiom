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
