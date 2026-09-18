"""B1400 — the six sweeps intaken: the numbers this bench recomputed, pinned.

The SnapPy slices are pinned from the recorded results (re-running 2400 manifolds is a
~10-minute job, not a unit test); the stratification arithmetic and every non-SnapPy sweep
are recomputed here.
"""
import json
import math
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1400_the_six_sweeps_intaken"
V = ARC / "verification"


def _slice(k):
    return json.loads((V / f"slice_{k}.json").read_text(encoding="utf-8"))


def test_sweep6_slices_reproduce_the_reported_numbers():
    """Their three rates and mean volumes, to the digit."""
    want = {0: (34.25, 4.183), 20000: (29.38, 4.767), 80000: (5.650 and 21.12, 5.650)}
    for k, (rate, vol) in want.items():
        d = _slice(k)
        assert d["n"] == 800, (k, d["n"])
        assert abs(d["rate"] - rate) < 0.005, (k, d["rate"], rate)
        assert abs(d["meanvol"] - vol) < 0.0005, (k, d["meanvol"], vol)


def test_the_skip_confound_does_not_arise():
    """Their instrument skips >3-generator presentations and reports neither n nor the skip
    count; generator count correlates with complexity, which is the variable under study.
    Measured: nothing was skipped, so the confound cannot be driving the decline."""
    for k in (0, 20000, 80000):
        d = _slice(k)
        assert d["skipped"] == 0, (k, d["skipped"])
        assert sum(v[0] for v in d["bygen"].values()) == d["n"]
        assert set(d["bygen"]) <= {"2", "3"}, d["bygen"]


def _z(h1, n1, h2, n2):
    p = (h1 + h2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    return (h1 / n1 - h2 / n2) / se


def test_the_decline_is_entirely_in_the_two_generator_stratum():
    """THE REFINEMENT: 2-gen collapses (z > 7), 3-gen is flat (z < 1), and the growing
    3-gen share props the aggregate up -- so the headline UNDERSTATES the effect."""
    a, b, c = (_slice(k)["bygen"] for k in (0, 20000, 80000))
    r = lambda g, k: 100 * g[k][1] / g[k][0]
    # 2-generator: monotone collapse to under half the front rate
    assert r(a, "2") > 34 and r(b, "2") < 29 and r(c, "2") < 16
    assert r(c, "2") < r(a, "2") / 2, "the 2-gen rate must more than halve"
    z2 = _z(a["2"][1], a["2"][0], c["2"][1], c["2"][0])
    assert z2 > 7, z2
    # 3-generator: flat, and NOT significant
    z3 = _z(a["3"][1], a["3"][0], c["3"][1], c["3"][0])
    assert abs(z3) < 1.0, z3
    assert 32 < r(c, "3") < 34, r(c, "3")
    # the aggregate decline is real but SMALLER than the 2-gen one
    agg = _z(_slice(0)["hit"], 800, _slice(80000)["hit"], 800)
    assert 5 < agg < z2, (agg, z2)
    # and the mix shifts, which is what dilutes it
    share = [100 * s["bygen"]["3"][0] / s["n"] for s in (_slice(0), _slice(20000), _slice(80000))]
    assert share[0] < 8 < share[1] < 20 < share[2], share
    # CONTROL: the z-test itself must report no effect when there is none
    assert abs(_z(100, 300, 100, 300)) < 1e-9, "z must be 0 for identical proportions"


def test_sweep1_claims_md_counts():
    """Their four numbers are LINE counts, not occurrence counts, though they say "occurrences".

    Three of the four are identical either way; only "generic" separates them -- 7 occurrences
    on 4 lines -- and their 4 is the line count. Immaterial to the sweep's conclusion (which is
    that "base rate" and "prereg" are both zero), but pinned so the distinction is on record.
    """
    t = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    assert len(t.splitlines()) == 231
    lines = lambda term: sum(1 for l in t.splitlines() if re.search(re.escape(term), l, re.I))
    occ = lambda term: len(re.findall(re.escape(term), t, re.I))
    for term, n in (("base rate", 0), ("prereg", 0), ("control", 3), ("generic", 4)):
        assert lines(term) == n, (term, lines(term), n)
    # the one that distinguishes the two readings
    assert occ("generic") == 7 and lines("generic") == 4
    for term in ("base rate", "prereg", "control"):
        assert occ(term) == lines(term), term


def test_sweep3_no_orphan_arcs():
    verd = {}
    for p in ROOT.glob("frontier/*/arc_verdict.json"):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(d.get("id"), str):
            verd[d["id"]] = p
    cited = set()
    for p in list(ROOT.glob("frontier/*/*.md")) + list(ROOT.glob("frontier/*/arc_verdict.json")):
        try:
            t = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        cited |= {"B" + m.group(1) for m in re.finditer(r"\bB(\d{1,4})\b", t)}
    assert set(verd) - cited == set(), sorted(set(verd) - cited)[:8]
    assert len(verd) > 1200


def test_sweep4_unique_claims_declare_their_class():
    t = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    rows = {m.group(1): m.group(0) for m in re.finditer(r"^\| (P\d+) .*$", t, re.M)}
    for pid, frag in (("P53", "among the ten exceptional fillings"),
                      ("P48", "imaginary-quadratic trace fields"),
                      ("P10", "not** an independent proof"),
                      ("P43", "CORRECTED 2026-07-15"),
                      ("P46", "SPLIT 2026-07-15")):
        assert frag in rows[pid], (pid, frag)


def _nfiles(term, ref):
    out = subprocess.run(["git", "grep", "-il", term, ref, "--", "*.md"],
                         cwd=ROOT, capture_output=True, text=True).stdout
    return len([l for l in out.splitlines() if l.strip()])


def test_sweep5_hyphen_flag_correction_and_the_absent_list():
    """-ilw returns 0 for hyphenated terms; their -il was the right flag. And the absent
    list is right on main while eight terms are already present on this branch."""
    # REWRITTEN 2026-09-18 (B1425): this asserted the literal count 16, which grows as the record does
    # (it is 18 today). The FINDING is the flag comparison -- -il matches a hyphenated term and -ilw does
    # not -- and that is what is pinned now. A lock on a corpus statistic that is expected to grow reports
    # growth as breakage.
    assert _nfiles("L-space", "origin/main") >= 16, "their -il count"
    w = subprocess.run(["git", "grep", "-ilw", "L-space", "origin/main", "--", "*.md"],
                       cwd=ROOT, capture_output=True, text=True).stdout
    nw = len([l for l in w.splitlines() if l.strip()])
    # REWRITTEN 2026-09-18 (B1425). This asserted -ilw returns EXACTLY 0, which held only because every
    # occurrence then was the plural "L-spaces": the trailing s is a word character, so -w could not match.
    # Today two files write the singular with punctuation after it and -w matches them. The finding that
    # survives is the one the sweep was for -- on a hyphenated term the two flags DISAGREE, so -w silently
    # under-reports and -il is the right flag -- and a count that depends on how the corpus happens to
    # inflect a noun is not a fact about the flags.
    assert nw < _nfiles("L-space", "origin/main"), (
        "-w no longer under-reports on a hyphenated term: %d vs %d" % (nw, _nfiles("L-space", "origin/main")))
    # REWRITTEN 2026-09-18 (B1425). B1400's "absent list" was a true measurement of what the record did
    # NOT contain on 2026-09-13. Asserting the absence CONTINUES is asserting the record never grows in
    # those directions, which is the wrong thing to lock -- and four of the seven have since entered, by
    # way of a handoff intake and the paper's later citations. What is kept: the terms still absent are
    # still absent, and any that entered must be NAMED here, so the drift is recorded instead of silent.
    ENTERED_SINCE = {            # term -> where it first appears now (checked 2026-09-18)
        "Gabriel's theorem": "docs/handoffs/",
        "cluster algebra": "docs/handoffs/",
        "exceptional divisor": "docs/handoffs/",
        "Jorgensen inequality": "docs/views/",
        "Heegaard Floer": "docs/handoffs/",
    }
    for t in ("Milnor fibration", "Gabriel's theorem", "cluster algebra", "exceptional divisor",
              "simple singularity", "Jorgensen inequality", "Heegaard Floer"):
        n = _nfiles(t, "origin/main")
        if t in ENTERED_SINCE:
            continue             # named above; its entry is recorded, not asserted away
        assert n == 0, "%s entered the record and is not named in ENTERED_SINCE" % t
    # Also rewritten: this compared HEAD against origin/main to show eight terms had "entered on this
    # branch". Once the branch merged, the comparison became degenerate -- and it goes red the moment the
    # work is pushed, i.e. exactly when it has succeeded. The durable fact is that the terms are in the
    # record at HEAD.
    for term in ("Kronheimer", "ADHM", "Nakajima", "quiver variety", "elliptic surface",
                 "minimal resolution", "waist size"):
        assert _nfiles(term, "HEAD") > 0, "%s left the record" % term


def test_the_jorgensen_diacritic_is_a_different_person():
    """The near-miss: o-slash Jorgensen returns 9 files on main, and ALL are Andersen-Jorgensen
    (TQFT), not Troels Jorgensen of the Kleinian-group inequality. Their absence holds."""
    ref = "origin/main"
    oslash = "J" + chr(248) + "rgensen"
    assert _nfiles(oslash, ref) >= 9, "the diacritic spelling IS present"
    out = subprocess.run(["git", "grep", "-ih", oslash, ref, "--", "*.md"],
                         cwd=ROOT, capture_output=True, text=True).stdout
    lines = [l for l in out.splitlines() if oslash.lower() in l.lower()]
    assert lines, "must find the context lines"
    # REWRITTEN 2026-09-18 (B1425). This asserted that EVERY occurrence is the Andersen-Jorgensen pair,
    # i.e. that Troels Jorgensen of the Kleinian-group inequality is absent from the record. That was true
    # when B1400 measured it and is deliberately false now: the paper's later upgrades cite his work
    # directly. The finding was that the two are DIFFERENT PEOPLE and must not be conflated, so what is
    # pinned is that both kinds occur and are distinguishable -- not that one of them is missing.
    pair = [l for l in lines if re.search(r"Andersen[-–—]\s*" + oslash, l, re.I)]
    assert pair, "the Andersen-Jorgensen (TQFT) occurrences have gone"
    other = [l for l in lines if l not in pair]
    assert other, ("no occurrence outside the Andersen-Jorgensen pair: if the Kleinian-group citations "
                   "have left the record, this lock's premise has changed again")


def test_the_retracted_statistic_never_entered_our_record():
    hits = []
    for p in list(ROOT.glob("frontier/*/*.md")) + list(ROOT.glob("frontier/*/arc_verdict.json")) \
            + list(ROOT.glob("docs/*.md")) + [ROOT / "CLAIMS.md"]:
        # B1400 itself quotes the number in order to say it never entered the record; a check
        # that counted its own report would be self-defeating (the same self-reference that
        # tripped the placeholder row in ERROR_LEDGER.md).
        if "B1400" in str(p):
            continue
        try:
            t = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if re.search(r"(?<![\d.])3427(?![\d])", t):
            hits.append(str(p.relative_to(ROOT)))
    assert hits == [], hits
    # CONTROL: the pattern must actually fire on the number it is looking for
    assert re.search(r"(?<![\d.])3427(?![\d])", "1 in 3427 manifolds")
    assert not re.search(r"(?<![\d.])3427(?![\d])", "0.0342784"), "must not match inside a decimal"
