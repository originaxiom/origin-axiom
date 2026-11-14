"""B1882 lock -- the V1 card, run on main and read once.

What could fail: a sealed file of the card or an output of the run changing after the fact; the outputs having entered the
record together with their reading; a reading that does not follow from its counts by the card's rule; the arc saying more
than the cells read (a rarity re-read, a comparison made, or the margin left out)."""
import hashlib
import json
import re
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


def test_a_share_falls_in_the_window_written_for_the_audits_figure_and_the_pile_up_is_not_among_the_well_fitted():
    # RENAMED 2026-11-12 (Review 79).  The name said the audit's figure "is reproduced" and "belongs to targets that fit nothing".
    # Nothing of the audit's was run again, and no fit was measured.  "reproduced" below is the card's own field: a share fell in
    # the window the card wrote beforehand.  The last layer is compared with its neighbour at the two depths named here, no deeper.
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


def test_the_pages_numbers_are_the_runs():
    """Added 2026-11-12 (Review 79).  Two readings of this arc, by sessions that did not build it, found six numbers and three
    sentences of the page that the run does not give; the test above, which asks only that phrases be present, let all of them
    through.  Here every number the corrected page states is computed from the committed run and looked for in the page as it
    prints it.  What fails it: a threshold, an interval end, a range, a count or a margin on the page that is not the run's."""
    from decimal import Decimal, ROUND_HALF_UP
    from fractions import Fraction
    inst = json.loads((ARC / "card" / "v1_null.json").read_text(encoding="utf-8"))["instruments"]
    page = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    cells = [(n, k) for n in ("N1", "N2") for k in inst[n]["cells"]]
    assert len(cells) == 9
    end = lambda n, k, depth, which: inst[n]["cells"][k]["leave_out"][depth][which + " layer 1"]
    share = lambda x: Fraction(x["rows_share"]).limit_denominator(10 ** 6)                    # 1/15 and 15/223, exactly
    ratio = lambda x: Fraction(x["lost"], x["n"]) / share(x)

    def places(q, n):                                                                          # exact, rounded half up as the page was
        return str((Decimal(q.numerator) / Decimal(q.denominator)).quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP))

    # the rule's line: twice the rows' share of the thousand targets
    t1, t2 = (2 * share(end(n, k, "best 0.1%", "top")) * 1000 for n, k in (("N1", "wf|seat"), ("N2", "chi2|seat")))
    assert "%s targets for the first null and %s for the second" % (places(t1, 1), places(t2, 1)) in page
    # the table at ten times the depth
    for name, (n, k) in (("first null, worst factor, seat", ("N1", "wf|seat")), ("second null, χ², seat", ("N2", "chi2|seat")),
                         ("second null, worst factor, seat", ("N2", "wf|seat"))):
        x = end(n, k, "best 1%", "top"); s = float(share(x))
        assert "| %s | %s [%.2f, %.2f] |" % (name, places(ratio(x), 2), x["ci95"][0] / s, x["ci95"][1] / s) in page, name
    # the two ranges, under the seat's menu and over all nine cells
    tops = {c: float(ratio(end(*c, "best 0.1%", "top"))) for c in cells}
    bots = {c: float(ratio(end(*c, "best 0.1%", "bottom"))) for c in cells}
    seat = [c for c in cells if c[1].endswith("|seat")]
    assert "at %.1f to %.1f times the average rate, and from the first at %.2f to %.2f of it" % (
        min(tops[c] for c in seat), max(tops[c] for c in seat), min(bots[c] for c in seat), max(bots[c] for c in seat)) in page
    assert "the top end reads %.1f to %.1f and the bottom end %.2f to %.2f" % (min(tops.values()), max(tops.values()), min(bots.values()), max(bots.values())) in page
    assert max(bots.values()) > 0.1 and max(tops.values()) > 2                                # what the old sentence denied
    # the targets whose best row is in the top layer, by how well they are fitted
    pop = inst["N1"]["cells"]["wf|seat"]["all_seeds"]["populations"]
    hits = [pop[d]["share"]["top layer 1"]["hits"] for d in ("all", "best 5%", "best 1%", "best 0.1%")]
    assert "of the first null's {:,}, {:,} are in the best 5%, {:,} in the best 1% and {:,} in the best 0.1%".format(*hits) in page
    # the last layer against its neighbour: below it at three depths in all three decisive cells, and the counts at the deepest
    deep = []
    for n, k in (("N1", "wf|seat"), ("N2", "chi2|seat"), ("N2", "wf|seat")):
        P = inst[n]["cells"][k]["all_seeds"]["populations"]
        for d in ("best 5%", "best 1%", "best 0.1%"):
            assert P[d]["share"]["top layer 1"]["hits"] < P[d]["share"]["top layer 2"]["hits"], (n, k, d)
        deep.append((P["best 0.01%"]["share"]["top layer 1"]["hits"], P["best 0.01%"]["share"]["top layer 2"]["hits"]))
    assert "%d against %d in the first null; %d against %d and %d against %d in the second" % (deep[0] + deep[1] + deep[2]) in page
    assert deep[0][0] > deep[0][1]                                                             # so "below its neighbour" cannot stand with no depth
    # ... nor with no menu: under the other two menus it holds at 5% and 1% in every cell, and at 0.1% in all but one
    hits = lambda c, d, layer: inst[c[0]]["cells"][c[1]]["all_seeds"]["populations"][d]["share"][layer]["hits"]
    others = [c for c in cells if not c[1].endswith("|seat")]
    assert all(hits(c, d, "top layer 1") < hits(c, d, "top layer 2") for c in others for d in ("best 5%", "best 1%"))
    above = [c for c in others if hits(c, "best 0.1%", "top layer 1") > hits(c, "best 0.1%", "top layer 2")]
    assert above == [("N1", "wf|cov")]
    assert "the first null's covariant menu, %d against %d" % (hits(above[0], "best 0.1%", "top layer 1"), hits(above[0], "best 0.1%", "top layer 2")) in page
    # the margins of the read-outs that read A
    over = lambda n, k, depth: float(end(n, k, depth, "top")["lost"] - 2 * share(end(n, k, depth, "top")) * end(n, k, depth, "top")["n"])
    a = [over("N2", k, "best 0.1%") for k in ("chi2|cov", "chi2|free", "wf|cov", "wf|free")]
    b = [over("N2", k, "best 1%") for k in ("chi2|cov", "chi2|free", "wf|cov", "wf|free")]
    assert "%.1f and %.1f over it under χ² and %.1f and %.1f under the worst factor" % tuple(a) in page
    assert "%.1f, %.1f, %.1f and %.1f over it" % tuple(b) in page and all(v > 0 for v in a + b)
    x = end("N2", "wf|free", "best 1%", "top")
    assert "{:,} against a line at {:,.2f}, a ratio of {:.3f}".format(x["lost"], float(2 * share(x) * x["n"]), float(ratio(x))) in page
    # the sentences that were wrong stand once each, inside the dated correction
    # CORRECTED 2026-11-12 (Review 79's second round; found by two readings).  The line that stood here read
    # `assert A and B or old == "..."`, which Python takes as `(A and B) or C`: for the third sentence C was true and the line
    # could not fail.  And it asked only that the first correction banner stand somewhere before the sentence.  Now each old
    # sentence must stand exactly once, and that once inside a block that opens with a dated correction.
    raw = (ARC / "FINDINGS.md").read_text(encoding="utf-8")                        # with its line breaks: a block ends at an empty line
    blocks = [" ".join(b.split()) for b in re.split(r"\n\s*\n", raw)]

    def _inside_a_correction(sentence):
        holds = [b for b in blocks if sentence in b]
        if len(holds) != 1 or holds[0].count(sentence) != 1:
            return False
        b = holds[0]
        return bool(re.search(r"CORRECTED 20\d\d-\d\d-\d\d", b[:b.index(sentence)]))
    for old in ("Those are targets that fit nothing.", "At the bottom end, at less than a tenth of it.", "was reproduced on main in B1870"):
        assert _inside_a_correction(old), old
    assert not _inside_a_correction("ALL THREE DECISIVE CELLS") and not _inside_a_correction("no such sentence on the page")     # the check can fail
    # and the statements the second round found still standing each carry their correction in the same block or the next
    for old in ('"20% at the top edge" is reproduced', "A random target that fits nothing has its least bad row somewhere", "So the pile-up belongs to the targets that fit nothing",
                "bottom end would add almost none", "the finding as main reproduced it"):
        at = [n for n, b in enumerate(blocks) if old in b]
        assert at, old
        for n in at:
            assert "CORRECTED 2026-11-12" in " ".join(blocks[n:n + 2]), old
    line = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    # CHANGED 2026-11-12 (Review 80; the SM seat's finding 33, not checked by main, made again here).  Two lines stood here:
    #     i = line.index(old)
    #     assert "2026-11-12" in line[i:i + len(old) + 120], old
    # They asked that the day stand within 120 characters after each old phrase: any mention of the day, whatever it says.
    # What is asked now is what each correction says, in the bracket that opens right after the old phrase.
    said = {"THE AUDIT'S FIGURE IS REPRODUCED AND IS NOT ABOUT RARITY": ("[CORRECTED 2026-11-12", "nothing of the audit's was reproduced", "a share that falls in a window written beforehand"),
            "a lower bottom end almost none": ("0.06 to 0.08 of the average rate", "0.18 under the first null's covariant menu", "added 2026-11-12]")}

    def _corrected(text, old):
        i = text.index(old) + len(old)
        if not text[i:].startswith(" ["):
            return False
        return all(s in text[i:text.index("]", i) + 1] for s in said[old])
    as_it_asked = lambda text, old: "2026-11-12" in text[text.index(old):text.index(old) + len(old) + 120]
    for old in said:
        assert _corrected(line, old), old
        # planted: the bracket after the old phrase replaced by a bare mention of the day.  The two lines above pass it.
        i = line.index(old) + len(old)
        bare = line[:i] + " [see the note of 2026-11-12]" + line[line.index("]", i) + 1:]
        assert as_it_asked(bare, old) and not _corrected(bare, old), old
    assert "left open there" in page and "\"OPEN, not checked\"" in page
