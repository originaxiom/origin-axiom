"""B1524 lock -- THE BAR'S NULL CONTRACT (2026-10-03; not sealed: nothing about a frame, a state or a census outcome is computed).
The audit lane asked (24c039c8) under which law the bar's p is a probability. Locked here:
- the record (null_contract.json): C1-C5 all pass, with their numbers;
- live, small versions of each check:
  - C1, the finite exchangeable law by enumeration;
  - C2, r >= (k+1)/(n+1) against B1518's own null_model;
  - C3, the i.i.d. law's size at the 0.01 gate on a range of n;
  - C4, the scan's termwise identity and B1518's scan;
  - C5, Sidak's failure at the gate (N = 399, K = 2) in exact rationals, and Bonferroni's validity there;
- B1518's two sealed decisions under Bonferroni, from its banked numbers;
- the amended bar (docs/THE_BAR.md, docs/PRACTICES.md), hygiene, and the verdict.
The full run (null_contract.py, about three minutes) is not repeated here; its record is locked."""
import base64
import importlib.util
import itertools
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1524_the_bars_null_contract"
VER = ARC / "verification"
B1518 = ROOT / "frontier" / "B1518_the_bar" / "verification"


def _nm():
    """B1518's null_model, loaded from its own file (a module of the same name elsewhere must not shadow it)"""
    spec = importlib.util.spec_from_file_location("b1518_null_model", B1518 / "null_model.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _record():
    return json.loads((VER / "null_contract.json").read_text(encoding="utf-8"))


def test_the_record():
    d = _record()
    assert all(d["checks"].values()) and len(d["checks"]) == 7
    c2 = d["C2 THE BAR's r against the exact law"]
    m, where = c2["double precision, n <= 2000: same minimum"]
    assert 0.3679 < m < 0.3680 and where == [0, 2000]
    assert c2["exact (rationals), n <= 120: min P(Bin(n, (k+1)/(n+1)) <= k)"][1] == [0, 120]
    c3 = d["C3 the i.i.d. law"]
    assert abs(c3["0.01"]["max size over n <= 2000"] - 0.003685) < 1e-5 and c3["0.01"]["n with no gate at all"] == 367
    assert all(v["size <= alpha"] for v in c3.values())
    c4 = d["C4 the scan law"]
    assert c4["B1518 m369 and s639 (a scan of 24 at 87 of 536)"]["exact"] == 0.987142
    assert c4["B1518 m369 and s639 (a scan of 24 at 87 of 536)"]["binomial (banked)"] == 0.985745
    c5 = d["C5 several looks"]
    excess, (N, K) = c5["alpha = 0.01, worst over stratum sizes N <= 200000: (size - alpha, (N, K))"]
    assert (N, K) == (399, 2) and 1.24e-5 < excess < 1.25e-5
    assert c5["B1518's decisions unchanged"] is True


def test_c1_the_finite_law_by_enumeration():
    for N in range(1, 9):
        for K in range(N + 1):
            hits = sum(0 in c for c in itertools.combinations(range(N), K))
            assert Fraction(hits, math.comb(N, K)) == Fraction(K, N)


def test_c2_r_is_at_least_the_exact_p():
    nm = _nm()
    for n in range(1, 201):
        for k in range(n + 1):
            assert nm.clopper_pearson(k, n)[1] >= (k + 1) / (n + 1) - 1e-12, (k, n)
    # the certificate in exact rationals at the k = 0 corner, where it is smallest: (n/(n+1))^n > 1/e > 0.025
    for n in (1, 10, 100):
        assert Fraction(n, n + 1) ** n > Fraction(1, 40)


def test_c3_the_gate_under_the_iid_law():
    import numpy as np
    from scipy.stats import binom
    nm = _nm()
    worst = 0.0
    for n in (368, 500, 1000, 1500, 1964, 2000):
        r = [nm.clopper_pearson(k, n)[1] for k in range(40)]
        kstar = max(k for k in range(40) if r[k] <= 0.01)
        q = np.linspace(1e-6, 1, 20001)
        worst = max(worst, float((q * binom.cdf(kstar, n, q)).max()))
    assert worst < 0.004
    # below n = 368 the gate never passes: r(0, n) > 0.01
    assert nm.clopper_pearson(0, 367)[1] > 0.01 > nm.clopper_pearson(0, 368)[1]


def test_c4_the_scan():
    for N in (536, 758):
        for K in (1, 87, N // 2):
            for i in (0, 1, 23, 200):
                assert (N - K) * (N - i) - N * (N - K - i) == K * i
    exact = 1 - Fraction(math.comb(449, 24), math.comb(536, 24))
    bino = 1 - (1 - Fraction(87, 536)) ** 24
    assert bino < exact and round(float(exact), 4) == 0.9871 and round(float(bino), 4) == 0.9857


def test_c5_sidak_fails_at_the_gate_and_bonferroni_holds():
    N, K, alpha = 399, 2, Fraction(1, 100)
    c = Fraction(K, N)
    either = 1 - Fraction((N - K) * (N - K - 1), N * (N - 1))   # two fixed units of one stratum, under the finite law
    assert either == 2 * c - c * c + c * (1 - c) / (N - 1)
    # each look's p is K/N if its unit carries; Sidak rejects when 1 - (1 - K/N)^2 <= alpha
    assert 1 - (1 - c) ** 2 <= alpha
    assert either > alpha                                   # its size exceeds the gate
    # Bonferroni rejects when 2 K/N <= alpha, which fails here, so its size is 0 <= alpha; in general sum of valid p's
    assert 2 * c > alpha
    # Bonferroni is never below Sidak (Bernoulli's inequality)
    for m in (2, 5, 50):
        for p in (Fraction(1, 1000), Fraction(1, 100), Fraction(1, 7)):
            assert min(1, m * p) >= 1 - (1 - p) ** m


def test_b1518_decisions_under_bonferroni():
    br = json.loads((B1518 / "bar_run.json").read_text(encoding="utf-8"))
    t2 = br["tests"]["T2 AUC under S1 against its permutation null"]["p"]
    t3 = br["tests"]["T3 reversal-closed given S2: conditional permutation"]["p_greater"]
    assert min(1, 2 * t2) < 0.01 and min(1, 2 * t3) >= 0.01                  # T2 YES, T3 NO, as sealed
    assert br["predictions"]["P3 G predicts the hit beyond chance (AUC under S1, Sidak-corrected p < 0.01)"] is True
    assert br["predictions"]["P4 reversal enrichment survives G and sign (MH OR > 1, Sidak-corrected p < 0.01)"] is False


def test_the_amended_bar():
    bar = (ROOT / "docs" / "THE_BAR.md").read_text(encoding="utf-8")
    for s in ("Amended by B1524", "## The null contract (B1524, 2026-10-03)", "| **PASSED** |", "C(N − K, n)/C(N, n)",
              "Then Bonferroni over every look", "PASSED is a rarity grade", "0.0100125", "0.9871"):
        assert s in bar, s
    assert "| **DERIVED** |" not in bar and "Then Šidák over every look" not in bar
    pr = (ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8")
    assert "grades PASSED (a rarity screen, not a derivation)" in pr and "null contract B1524" in pr


def test_hygiene():
    """no vendor word, no private term, no Gate 5-Q word in the arc's text"""
    tokens = [base64.b64decode(t).decode() for t in ("Y2xhdWRl", "YW50aHJvcGlj", "b3B1cw==", "c29ubmV0", "ZmFibGU=")]
    private = bytes([98, 114, 97, 118, 101]).decode()
    files = list(ARC.glob("*.md")) + list(VER.glob("*.py")) + [ARC / "arc_verdict.json", ROOT / "docs" / "THE_BAR.md"]
    for f in files:
        t = f.read_text(encoding="utf-8")
        for w in tokens:
            assert not re.search(re.escape(w), t, re.I), (f.name, "vendor word")
        assert private not in t.lower(), f.name
        for w in ("qualia", "aware", "sees"):
            assert not re.search(r"\b" + w + r"\b", t, re.I), (f.name, w)


def test_the_verdict():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1524" and v["verdict"] == "PROVED" and v["creates_law"] is False
    assert v["prior_work"]["standing"] == "RE-DERIVED" and "B1518" in v["depends_on"]
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import prior_work
    assert prior_work.validate(v["prior_work"]) == []
