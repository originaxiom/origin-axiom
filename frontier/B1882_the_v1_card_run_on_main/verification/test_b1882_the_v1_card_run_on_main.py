"""B1882 lock -- the V1 card, run on main and read once.

What could fail: a sealed file of the card or an output of the run changing after the fact; the outputs having entered the
record together with their reading; a reading that does not follow from its counts by the card's rule; the arc saying more
than the cells read (a rarity re-read, a comparison made, or the margin left out)."""
import hashlib
import json
import math
import pathlib
import subprocess

import pytest

ARC = pathlib.Path(__file__).resolve().parents[1]
CARD = ARC / "card"
D = json.loads((CARD / "v1_null.json").read_text(encoding="utf-8"))
DECISIVE = (("N1", "wf|seat"), ("N2", "chi2|seat"), ("N2", "wf|seat"))
# the two outputs as they stood in the commit that held them unread
UNREAD = {"v1_null.json": "73b3d3e30a1692c45bc18ae033637a7e660dad6010225b3d86ab304a839bf88a",
          "v1_null_run.txt": "130c2e229b724810536c6c1ed6bb8c7aeed6f1848319e958c091ded6092b6000"}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _log_choose(n):
    return [math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1) for i in range(n + 1)]


_LOGC = {}


def _tail(k, n, p, upper):
    """P(X >= k) if upper, else P(X <= k), for X binomial(n, p): the terms summed directly, in logarithms"""
    if n not in _LOGC:
        _LOGC[n] = _log_choose(n)
    lc, lp, lq = _LOGC[n], math.log(p), math.log1p(-p)
    idx = range(k, n + 1) if upper else range(0, k + 1)
    return math.fsum(math.exp(lc[i] + i * lp + (n - i) * lq) for i in idx)


def exact_interval(k, n, alpha=0.05):
    """the exact binomial (Clopper-Pearson) interval, by bisection on the binomial tails themselves; main's own, and not
    the incomplete beta function the script uses"""
    def solve(f, rising):
        lo, hi = 1e-12, 1 - 1e-12
        for _ in range(48):
            mid = (lo + hi) / 2
            if (f(mid) < alpha / 2) == rising:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    low = 0.0 if k == 0 else solve(lambda p: _tail(k, n, p, True), True)          # P(X >= k) rises with p
    high = 1.0 if k == n else solve(lambda p: _tail(k, n, p, False), False)       # P(X <= k) falls with p
    return low, high


def reading(lost, n, r):
    """the card's section 6, for one end"""
    loss = lost / n
    lo, _ = exact_interval(lost, n)
    return "A" if (loss >= 2 * r and lo > r) else ("C" if loss < r / 2 else "B")


def test_the_sealed_files_and_the_unread_outputs_are_unchanged():
    listed = [l.split() for l in (CARD / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    assert sorted(name for _, name in listed) == ["PREREGISTRATION.md", "selftest_out.txt", "v1_card.py"]
    assert all(sha(CARD / name) == digest for digest, name in listed)
    assert all(sha(CARD / name) == digest for name, digest in UNREAD.items())
    run = (CARD / "v1_null_run.txt").read_text(encoding="utf-8")
    assert "this script sha256 beef66a2caa96fae" in run and "500 of 500 seeds" in run and run.rstrip().endswith("null exit 0")


def test_the_outputs_entered_the_record_before_their_reading():
    """gates read history: the commit that added the two outputs added nothing else, and the findings came later"""
    r = subprocess.run(["git", "-C", str(ARC), "log", "--format=%H", "--diff-filter=A", "--", "card/v1_null.json"], capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        pytest.skip("no git history here: the order of the two commits cannot be read")
    first = r.stdout.split()[-1]
    files = subprocess.run(["git", "-C", str(ARC), "show", "--format=", "--name-only", first], capture_output=True, text=True).stdout.split()
    assert sorted(pathlib.PurePosixPath(f).name for f in files) == ["v1_null.json", "v1_null_run.txt"], files
    later = subprocess.run(["git", "-C", str(ARC), "log", "--format=%H", "--diff-filter=A", "--", "FINDINGS.md"], capture_output=True, text=True).stdout.split()
    if later:                                           # once the findings are committed: their commit descends from the unread one
        anc = subprocess.run(["git", "-C", str(ARC), "merge-base", "--is-ancestor", first, later[-1]]).returncode
        assert anc == 0 and later[-1] != first


def test_every_reading_follows_from_its_counts_by_the_cards_rule():
    got = {}
    for inst in ("N1", "N2"):
        for cell, c in D["instruments"][inst]["cells"].items():
            for tail in ("best 0.1%", "best 1%"):
                lo = c["leave_out"][tail]
                ends = {}
                for end in ("bottom", "top"):
                    e = lo["%s layer 1" % end]
                    assert e["lost"] <= e["with_their_best_row_there"] <= e["n"] and abs(e["loss"] - e["lost"] / e["n"]) < 1e-12
                    ci = exact_interval(e["lost"], e["n"])
                    assert abs(ci[0] - e["ci95"][0]) < 1e-9 and abs(ci[1] - e["ci95"][1]) < 1e-9          # the script's interval is the exact one
                    ends[end] = reading(e["lost"], e["n"], e["rows_share"])
                got[(inst, cell, tail)] = "A" if "A" in ends.values() else ("C" if set(ends.values()) == {"C"} else "B"), ends
    assert len(got) == 18 and all(v[1]["bottom"] == "C" for v in got.values())                       # every bottom end reads C
    for inst, cell in DECISIVE:
        assert got[(inst, cell, "best 0.1%")] == ("B", {"bottom": "C", "top": "B"})
        assert D["decisive"]["%s %s" % (inst, cell)].startswith("B: an end is like other rows (bottom C, top B)")
    assert len(D["decisive"]) == 3 and D["q_decisive"] == 0.001
    # the read-outs: the first null reads B under every menu, the second reads A under its covariant and free menus, at both depths
    assert all(got[("N1", c, t)][0] == "B" for c in ("wf|seat", "wf|cov", "wf|free") for t in ("best 0.1%", "best 1%"))
    assert all(got[("N2", c, t)][0] == "A" for c in ("chi2|cov", "chi2|free", "wf|cov", "wf|free") for t in ("best 0.1%", "best 1%"))
    assert all(got[("N2", c, "best 1%")][0] == "B" for c in ("chi2|seat", "wf|seat"))


def test_the_counts_and_the_margins_the_page_prints():
    top = lambda i, c, t="best 0.1%": D["instruments"][i]["cells"][c]["leave_out"][t]["top layer 1"]
    bot = lambda i, c, t="best 0.1%": D["instruments"][i]["cells"][c]["leave_out"][t]["bottom layer 1"]
    assert [(bot(i, c)["lost"], top(i, c)["lost"]) for i, c in DECISIVE] == [(4, 109), (6, 134), (6, 132)]
    short = [2 * top(i, c)["rows_share"] * 1000 - top(i, c)["lost"] for i, c in DECISIVE]
    assert 24 < short[0] < 25 and 0 < short[1] < 1 and 2 < short[2] < 3                             # two cells read B by a hair
    ratios = [round(top(i, c)["ratio_to_rows_share"], 2) for i, c in DECISIVE]
    assert ratios == [1.64, 1.99, 1.96]
    assert [round(top(i, c, "best 1%")["ratio_to_rows_share"], 2) for i, c in DECISIVE] == [1.46, 1.90, 1.89]
    assert all(D["instruments"][i]["cells"][c]["all_seeds"]["targets"] == 1000000 for i, c in DECISIVE)
    assert D["instruments"]["N1"]["rows"] == 47880 and D["instruments"]["N2"]["rows"] == 21408


def test_the_audits_figure_is_reproduced_and_belongs_to_targets_that_fit_nothing():
    fig = D["the_audits_figure"]
    assert fig["reproduced"] is True and any(0.17 <= v <= 0.23 for v in fig["shares_of_all_targets"].values())
    assert abs(fig["shares_of_all_targets"]["N1 wf|seat | top layer 1 | all_seeds"] - 0.205881) < 1e-9
    for inst, cell in DECISIVE:
        pops = D["instruments"][inst]["cells"][cell]["all_seeds"]["populations"]
        m = lambda pop, k: pops[pop]["share"][k]["ratio_to_rows_share"]
        # among all targets the last layer stands far above its neighbour; among the well-fitted it is below it
        assert m("all", "top layer 1") > 1.3 * m("all", "top layer 2") and m("all", "top layer 1") > 2.5
        assert m("best 0.1%", "top layer 1") < m("best 0.1%", "top layer 2") and m("best 1%", "top layer 1") < m("best 1%", "top layer 2")
        assert m("best 0.1%", "bottom layer 1") < 0.15


def test_the_arc_says_what_the_cells_read_and_no_more():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("All three decisive cells read B", "Two of the three read B by a hair", "it is not about rarity", "reads A", "committed unread at 818d17f46",
              "No rarity is re-read", "nothing is compared with a", "P-786", "The later nulls", "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1882" and v["claim_one_line"].endswith("0 of 19.") and v["weave_or_thread"].startswith("n/a")
    for s in ("ALL THREE DECISIVE CELLS READ B", "less than one target", "No rarity is re-read"):
        assert s in v["claim_one_line"], s
    for d, word in (("B1726_the_two_ingredients_replicated", "about 1.5 times"), ("B1753_the_six_on_the_five_ality_lines", "about 2 times")):
        t = (ARC.parent / d / "FINDINGS.md").read_text(encoding="utf-8")
        assert "Dated note 2026-11-11 (B1882" in t and word in t and "whose two ends are a choice" in t
