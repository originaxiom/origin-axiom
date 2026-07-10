"""B500 lock -- Gate A class 2c: irregular covers of 4_1 at index 7-8 (horizon extension).

Locks the CONTROL (B349's index <= 6 census + B350's exact SNF/Lucas ladder extended to
n = 7, 8), the index-7 headline (9 covers, the banked canonical multiset, both x4
multiplicity groups collapsing to single isometry classes), the cyclic cross-check at 7-8
(SnapPy torsion == coker(A^n - I) SNF, two independent routes), the EXACT-tier index-8
separator (the degree-2 sub-cover censuses of the (3,3) class representatives differ), and
the banked JSON / FINDINGS integrity (verdict SEALED, within budget, firewall untouched).
The full index-8 partition recompute (signatures + symmetry groups for every cover) is
behind pytest.mark.slow -- the fast locks stay well under 60 s. SnapPy behind importorskip,
like the other SnapPy locks. CONDITIONAL per the C-guardrail (index <= 8 is a computational
horizon, not a theorem); nothing to CLAIMS.md."""
import importlib.util
import json
import pathlib

import pytest

snappy = pytest.importorskip("snappy")

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_DIR = _ROOT / "frontier" / "B500_irregular_covers_78"

_spec = importlib.util.spec_from_file_location("b500_probe", _DIR / "probe.py")
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)                       # loads b349 + b350 via importlib; no heavy work

R = json.load(open(_DIR / "b500_census.json"))


@pytest.fixture(scope="module")
def fig8():
    return snappy.Manifold("4_1")


# ---------------- (0) controls ----------------
def test_control_b350_exact_ladder_extends_to_7_8():
    # exact tier, sympy only: SNF of coker(A^n - I) and the Lucas orders L_2n - 2
    snf = P.b350.torsion_groups(8)
    assert snf[7] == (29, 29) and snf[8] == (21, 105)
    orders = P.b350.torsion_orders(8)
    for n, (tn, lucas) in orders.items():
        assert tn == lucas, f"n={n}: |det(A^n-I)| {tn} != L_2n - 2 {lucas}"
    assert orders[7][0] == 841 == 29**2
    assert orders[8][0] == 2205 == 21 * 105


def test_control_b349_census_and_collapse_reproduced(fig8):
    for k in (4, 5, 6):
        assert P.b349.cover_census(fig8, k) == P.b349.EXPECTED_CENSUS[k], f"index {k}"
    for k in (5, 6):
        res = P.b349.multiplicities_resolved_by_isometry(fig8, k)
        assert res and all(nc == 1 for _, nc in res.values()), f"index {k}"


# ---------------- (1) the index-7 headline ----------------
def test_index7_census_is_the_banked_canonical_multiset(fig8):
    covers = fig8.covers(7)
    assert len(covers) == 9
    census = {}
    for C in covers:
        key = P.cover_key(C)
        census[key] = census.get(key, 0) + 1
    assert census == P.EXPECTED_CENSUS_78[7]


def test_index7_multiplicity_groups_collapse_to_single_isometry_classes(fig8):
    groups = {}
    for C in fig8.covers(7):
        groups.setdefault(P.cover_key(C), []).append(C)
    mult = {k: v for k, v in groups.items() if len(v) >= 2}
    assert {k: len(v) for k, v in mult.items()} == {
        ("irregular", (), 3, 3): 4, ("irregular", (14,), 1, 1): 4}
    for key, cs in mult.items():
        assert all(cs[0].is_isometric_to(C) for C in cs[1:]), f"{key}: no collapse"


# ---------------- (2) the cyclic cross-check at 7 and 8 ----------------
def test_cyclic_covers_cross_validate_b350_at_7_8(fig8):
    snf = P.b350.torsion_groups(8)
    for n in (7, 8):
        cyc = [C for C in fig8.covers(n) if C.cover_info()["type"] == "cyclic"]
        assert len(cyc) == 1                       # knot in S^3: one cyclic cover per index
        h = cyc[0].homology()
        torsion = tuple(int(c) for c in h.coefficients if c != 0)
        assert torsion == snf[n] == P.EXPECTED_CYCLIC_SNF_78[n], f"n={n}"
        assert h.betti_number() == 1


# ---------------- (3) the index-8 exact-tier split (the new structural fact) ----------------
def test_index8_33_group_splits_2_1_with_exact_separator(fig8):
    grp = [C for C in fig8.covers(8) if P.cover_key(C) == ("irregular", (3, 3), 2, 2)]
    assert len(grp) == 3
    subs = {C.name(): P.subcensus2(C) for C in grp}    # exact: pi_1 invariant, no numerics
    from collections import Counter
    sizes = sorted(Counter(subs.values()).values())
    assert sizes == [1, 2], f"degree-2 sub-cover censuses give split {sizes}, not [2, 1]"
    # the isometry partition agrees with the exact separator:
    pairs = [n for n, s in subs.items() if list(subs.values()).count(s) == 2]
    a, b = [C for C in grp if C.name() in pairs]
    (single,) = [C for C in grp if C.name() not in pairs]
    assert a.is_isometric_to(b)
    assert not single.is_isometric_to(a)


# ---------------- (4) banked JSON + documentation integrity ----------------
def test_banked_verdict_budget_and_index8_headline():
    assert R["verdict"]["outcome"] == "SEALED"
    assert "horizon" in R["verdict"]["phrasing"] and "not a theorem" in R["verdict"]["phrasing"]
    assert R["budget"]["status"] == "WITHIN BUDGET"
    assert R["budget"]["total_seconds"] < R["budget"]["cap_seconds"]
    assert R["indexes"]["7"]["n_covers"] == 9 and R["indexes"]["8"]["n_covers"] == 10
    for k in ("7", "8"):
        assert R["indexes"][k]["routes_agree"] is True
        assert R["gate_a"][k]["checks"]["no_distinguished_member"] is True
        assert R["gate_a"][k]["checks"]["exact_subcensus_consistent"] is True
    # the honest refinement is banked, not smoothed over:
    assert R["gate_a"]["7"]["checks"]["all_multiplicities_collapse"] is True
    assert R["gate_a"]["8"]["checks"]["all_multiplicities_collapse"] is False
    cls = R["indexes"]["8"]["partition"]["('irregular', (3, 3), 2, 2)"]
    assert sorted(c["size"] for c in cls) == [1, 2]
    sigs = [c["signature"] for c in cls]
    assert len(set(sigs)) == 2                    # distinct classes, distinct signatures
    subs = [c["subcensus2"] for c in cls]
    assert len(set(subs)) == 2                    # ... and distinct EXACT sub-censuses
    # MB guard: chirality only via the gated symmetry group; both reps full-group:
    assert all(c["sym_full_group"] is True for c in cls)
    assert sorted([c["amphichiral"] for c in cls], key=str) == [False, True]
    assert R["mb_guard"]["base_amphichiral"] is True
    assert R["firewall"].startswith("untouched")


def test_findings_house_style_and_firewall():
    find = (_DIR / "FINDINGS.md").read_text(encoding="utf-8")
    assert "SEALED" in find
    assert "Nothing to `CLAIMS.md`" in find
    assert "not a theorem" in find                # the C-guardrail phrasing
    assert "TOOL-BLOCKED" in find                 # the Sage-gated verified tier, named
    assert "[2, 1]" in find                       # the index-8 refinement, named loudly
    readme = (_DIR / "README.md").read_text(encoding="utf-8")
    assert "SEALED" in readme and "BUDGET-CAPPED" in readme   # the committed enum


# ---------------- slow: the full index-8 recompute ----------------
@pytest.mark.slow
def test_slow_index8_full_partition_matches_banked(fig8):
    res = P.census_and_partition(fig8, 8, float(fig8.volume()))
    assert res["n_covers"] == 10
    assert {eval(k): v for k, v in R["indexes"]["8"]["census"].items()} == res["census"]
    assert res["routes_agree"] and res["signature_partition_consistent"]
    assert res["exact_subcensus_consistent"]
    assert res["max_vol_defect"] < P.VOL_TOL
    headline = {key: (sum(c["size"] for c in cls), len(cls),
                      tuple(sorted(c["size"] for c in cls)))
                for key, cls in res["partition"].items()
                if sum(c["size"] for c in cls) >= 2}
    assert headline == P.EXPECTED_PARTITION_78[8]
    for key, cls in res["partition"].items():
        for c in cls:
            assert c["sym_full_group"] is True    # the MB chirality gate held everywhere
