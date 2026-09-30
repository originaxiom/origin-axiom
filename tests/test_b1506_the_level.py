"""B1506 lock -- THE LEVEL (sealed at 58e3f28f, PREREGISTRATION sha256 664f8192...; run as sealed, P1-P8 all YES).  One
background has one count on every level (Shapiro and a pullback keep the index).  B1378's M6 triplet is the orbit of its seed under
the root's whole deck: tau^3 acts by the Z/2 kernel of SL(2) x SU(6) -> E6, so the triplet descends to s961 (the root's unique 3-fold
cover) as the deck orbit of one generation-shaped background that does not lift to SL(2)_beta x U(1)^2, and the root object Ind D0
has count -gcd(n, 3) on M_n (an orbit of size k: gcd(n, k)).  s961's complete Standard-Model-frame census: 48 generation-shaped
backgrounds, none lifted, in 16 orbits of three, their extension characters pairwise different by order-4 characters.  M6's: 2 160
(336 lifted, 1 824 not), in 16 orbits of three (s961's, pulled back) and 352 of six."""
import importlib.util
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1506_the_level"
VER = ARC / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1506_the_level", VER / "the_level.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_deck_and_the_word_map_live():
    """the RS deck is conjugation by a in closed form; B1378's TAU and TAU2 are not homomorphisms (its generators are a^5 b, not
    a^5 b a^-6); the MT deck (phi, phi, t) is an automorphism with tau^n inner"""
    T = _load()
    F = T.IL.GF(601)
    for n in (3, 6):
        gens, words, rewrite, rels, mu, lam = T.rs_cover(n)
        tau = T.rs_conj(n, 1)
        assert tau == {g: T.red(w) for g, w in T.rs_closed_form(n).items()}
        base, G = T.geometric_rs(F, n)
        assert all(G.word(T.subst(tau, r)) == F.eye(2) for r in rels)
        assert all(G.word(tau[g]) == F.mul(F.mul(base.M["a"], G.M[g]), base.M["A"]) for g in gens)
    gens, words, rewrite, rels, mu, lam = T.rs_cover(6)
    base, G = T.geometric_rs(F, 6)
    assert not all(G.word(T.subst(T.B1378_TAU, r)) == F.eye(2) for r in rels)
    assert not all(G.word(T.subst(T.B1378_TAU2, r)) == F.eye(2) for r in rels)
    for n in range(1, 5):
        assert T.mt_formal_identity(n) and T.apply(T.PHI, T.MT_LAM) == T.MT_LAM


def test_the_loci_lemma_live():
    """T1: a finite-order locus with non-trivial fibre part has t -> 1; with trivial fibre part only phi^(+-2n)"""
    T = _load()
    rows = T.part_c_exact(3, 4)
    got = {}
    for r in rows:
        got[r["gcd"]] = got.get(r["gcd"], 0) + 1
    assert got == {"s**2 - 18*s + 1": 1, "s - 1": 15}
    assert [r["gcd"] for r in T.part_c_exact(1, 1)] == ["s**2 - 3*s + 1"]


def test_s961_complete_census_live():
    """the liftable part of s961 is silent (B1375); the complete census fires only on the 12 non-square loci; 48 generation-shaped
    backgrounds, none lifted, all orbits of three, signs 24/24, every sector of each (nu^c included) with one sign; two
    presentations agree; the fence: each orbit's three extension characters are distinct, pairwise different by order 4"""
    T = _load()
    out = []
    for kind, N in (("RS", T.N6), ("MT", None)):
        P = T.Pres(kind, 3, N=N)
        C = T.Census(P, primes=T.primes_for(P.N, k=2), verbose=False)
        row, classes = T.census_summary(C)
        assert row["loci"] == 16 and row["loci_non_square"] == 12 and row["t1_exceptions"] == 0
        assert row["candidates"] == 256 and row["firing"] == 72 and row["firing_non_square"] == 72
        assert row["non_square_loci_firing"] == 12 and row["differing"] == 0
        assert row["generation_shaped"] == 48 and row["generation_shaped_lifted"] == 0
        assert row["background_orbit_sizes"] == {"3": 48} and row["background_max_abs"] == 1
        assert sorted(row["background_signs"].items()) == [(-1, 24), (1, 24)]
        assert all(len(set(Is)) == 1 for Is in classes.values())
        for lam, als in classes:
            lams = [P.pull(lam, j) for j in range(3)]
            assert len(set(lams)) == 3
            for other in lams[1:]:
                d = P.add(other, lams[0], coeffs=[1, -1])
                assert P.N // math.gcd(P.N, *d) == 4
        out.append(row)
    assert out[0]["module_orbit_sizes"] == out[1]["module_orbit_sizes"] == {"3": 72}


def test_the_loci_are_the_characters_of_y3_live():
    """section 9: Y3 is s961 with its meridian filled, H1(Y3) = (Z/4)^2 (B1273); s961's 16 loci are exactly the characters of
    H1(Y3); the deck permutes them in five orbits of three and the trivial character (B1273's three sign characters are one orbit,
    B1364's twelve order-4 characters the other four)"""
    T = _load()
    gens, words, rewrite, rels, mu, lam = T.rs_cover(3)
    assert T.h1_of(gens, rels + [mu]) == ([4, 4], 0)
    P = T.Pres("RS", 3, N=T.N6)
    C = T.Census(P, primes=T.primes_for(P.N, k=2), verbose=False)
    assert set(C.loci) == {c for c in P.chars if P.val(c, P.mu_ex) == 0}
    orbits = {frozenset(P.pull(c, j) for j in range(3)) for c in C.loci}
    assert sorted(len(o) for o in orbits) == [1, 3, 3, 3, 3, 3]
    order = lambda c: P.N // math.gcd(P.N, *c) if any(c) else 1
    assert sorted(order(c) for c in C.loci) == [1] + [2] * 3 + [4] * 12


def test_the_seed_descends_to_s961_live():
    """T6 and D1-D3, D5 on one prime: the seed's root-deck orbit has three members; four descents to s961, exactly one with every
    sector a T5-candidate, and it is (-1)^6; it does not lift; its orbit pulls back to the triplet; the root object's counts on
    M1..M6 are -gcd(n, 3)"""
    T = _load()
    res, (P3, lam3, D0) = T.part_f(primes=(601,))
    assert res["distinct_translates"] == 3 and res["tau3_fixes_seed"] and res["tau2_lambda_twist_order"] == 4
    assert res["e6_descents"] == 4 and not res["lam3_square"]
    good = [d for d in res["descents"] if d["all_candidates"]]
    assert len(good) == 1 and good[0]["indices"] == (-1,) * 6
    assert all(d["indices"][:5].count(-1) < 5 for d in res["descents"] if not d["all_candidates"])
    assert res["D0_orbit_on_s961"] == 3 and res["D0_orbit_pulls_back_to_the_triplet"]
    row = res["by_prime"][0]
    assert row["members"] == [(-1,) * 6] * 3 and row["triplet_sum"] == (-3,) * 6
    assert all(c == [-1, -1, -3, -1, -1, -3] for c in row["root_object_counts_M1_to_M6"].values())


def test_the_recorded_run():
    """the full run (after the three-prime fix of the loci check): covers, the loci lemma, every level's census, P4-P8, the pullbacks,
    the s961 / M6 correspondence"""
    r = json.load(open(VER / "the_level.json"))
    a = r["A"]
    assert a["unique_2_and_3"] and a["det_4_1"] == 5
    c = r["C"]
    assert c["exact"]["4"]["gcds"] == {"s**2 - 47*s + 1": 1, "s - 1": 44}
    for n, loci, first_only in (("5", 120, 2), ("6", 319, 0)):
        row = c["numeric"][n]
        assert len(row["primes"]) == 3 and row["loci"] == loci and row["exceptions"] == 0
        assert row["meridian_exponents"] == [0] and row["first_prime_only"] == first_only
    d = r["D"]
    assert d["RS2"]["firing"] == 8 and d["RS2"]["generation_shaped"] == 0
    assert d["RS4"]["firing"] == 488 and d["RS4"]["generation_shaped"] == 256 and d["RS4"]["lift_data_total"] == 12800
    assert d["RS4"]["background_orbit_sizes"] == {"4": 256} and d["RS4"]["module_orbit_sizes"] == {"2": 8, "4": 480}
    assert d["RS3"]["generation_shaped"] == 48 and d["MT3"]["generation_shaped"] == 48
    m5 = d["RS5"]
    assert (m5["loci"], m5["candidates"], m5["firing"], m5["generation_shaped"], m5["lift_data_total"]) == (121, 14641, 2200, 400, 800)
    assert m5["background_orbit_sizes"] == {"5": 400}
    m6 = d["RS6"]
    assert (m6["loci"], m6["loci_non_square"], m6["candidates"], m6["firing"], m6["firing_non_square"]) == (320, 240, 102400, 12536,
                                                                                                          11184)
    assert m6["non_square_loci_firing"] == 240 and m6["module_orbit_sizes"] == {"2": 8, "3": 72, "6": 12456}
    assert m6["generation_shaped"] == 2160 and m6["generation_shaped_lifted"] == 336 and m6["lift_data_total"] == 67200   # P4, P6
    assert m6["background_orbit_sizes"] == {"3": 48, "6": 2112}                                                            # P8
    assert m6["background_signs"] == {"-1": 1080, "1": 1080}
    for key in ("RS1", "RS2", "RS3", "RS4", "RS5", "RS6", "MT1", "MT2", "MT3", "MT4"):
        assert d[key]["t1_exceptions"] == 0 and d[key]["differing"] == 0 and d[key]["deck_invariant_index"]
        assert d[key]["background_max_abs"] <= 1
    for row in r["E"]:
        assert row["index_kept"] == row["candidates"] == row["shapiro_twist_sum"]
    assert [row["firing_pullbacks"] for row in r["E"]] == [0, 0, 0, 0, 0, 8, 8, 72]
    h = r["H"]
    assert set(h.values()) == {48}                                                                                         # P5, P7


def test_the_post_run_checks():
    """the fence on s961 and M6; B1375's M6 singlet split is the orbit split; the level law gcd(n, k) on two backgrounds of every
    orbit size"""
    r = json.load(open(VER / "post_run_checks.json"))
    assert r["RS3"]["fence"] == {"(3, 3, (4, 4))": 48}
    f6 = r["RS6"]["fence"]
    assert f6["(3, 3, (4, 4))"] == 48 and sum(f6.values()) == 2160
    assert all(k.startswith("(6, 6, ") for k in f6 if not k.startswith("(3, "))
    s6 = r["RS6"]["singlets"]
    assert s6["(3, True, 1)"] == {"backgrounds": 48, "lift_data": 9600}
    assert s6["(6, True, 0)"] == {"backgrounds": 288, "lift_data": 57600}
    assert sum(v["backgrounds"] for k, v in s6.items() if ", False, " in k) == 1824
    for level in ("RS3", "RS4", "RS5", "RS6"):
        rows = [row for rs in r[level]["root_objects"].values() for row in rs]
        assert rows and all(row["gcd_law"] for row in rows)
    assert sorted(r["RS6"]["root_objects"]) == ["3", "6"]


def test_the_findings_and_the_verdict():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    for s in ("s961", "does not lift", "gcd", "Shapiro", "three distinct vacua", "0 of 19", "sealed"):
        assert s in f, s
    v = json.load(open(ARC / "arc_verdict.json"))
    assert v["id"] == "B1506" and v["verdict"] == "PROVED" and v["instrument"] and "0 of 19" in v["claim_one_line"]
