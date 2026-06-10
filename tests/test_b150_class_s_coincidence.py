"""B150 -- class-S coincidence (L14). Locks the B148 anchor data (the comparison's verifiable LHS) AND the *honesty
structure* of the tagged comparison. It does NOT (and cannot) unit-test the literature claims themselves -- those are
cited prose, the honest boundary of a reading task; the discipline this test enforces is that no resemblance is tagged
FORCED without a primary-source citation."""
from frontier.B150_class_s_coincidence.probe import COMPARISON, TAGS, anchor_data, verdict


def test_anchor_data_all_true():
    """The B148 invariant data a FORCED coincidence must reproduce -- re-asserted, all must hold."""
    a = anchor_data()
    assert a["RmLm_hyperbolic_tr_m2plus2"] is True
    assert a["eigenvalue_is_metallic_squared"] is True
    assert a["fixed_slopes_t2_plus_mt_minus_1"] is True
    assert a["dehn_twists_preserve_kappa"] is True
    assert a["kappa_minus2_is_markov"] is True
    # m=1 and m=4 share Q(sqrt5); m=2 -> Q(sqrt2)
    fields = {r["m"]: r["field_radicand"] for r in a["trace_fields"]}
    assert fields[1] == 5 and fields[4] == 5 and fields[2] == 2


def test_every_comparison_row_is_well_formed():
    """Each row has a tag in {FORCED,PERMITTED,RHYME}, a non-empty source, a reason, both sides."""
    for c in COMPARISON:
        assert c["tag"] in TAGS, c
        for key in ("point", "unit_side", "classS_side", "source", "reason"):
            assert c[key].strip(), (c["point"], key)


def test_no_forced_tag_without_a_cited_source():
    """The binding discipline: a FORCED tag must carry a primary-source citation (arXiv id or a named published ref)."""
    for c in COMPARISON:
        if c["tag"] == "FORCED":
            assert ("arXiv" in c["source"]) or ("AIF" in c["source"]), c["point"]


def test_tau_modularity_is_rhyme_not_forced():
    """The user's binding distinction: 'SL(2,Z) acts modularly on tau' is the HOMONYM -> must be RHYME, never FORCED."""
    tau_rows = [c for c in COMPARISON if "tau" in c["point"] and "coupling" in c["point"]]
    assert tau_rows, "the tau-modularity comparison point must be present"
    assert all(c["tag"] == "RHYME" for c in tau_rows)


def test_overall_verdict_is_honest_mixed():
    v = verdict()
    assert v["overall"] in {"FORCED", "RHYME", "MIXED"}
    assert v["overall"] == "MIXED"          # FORCED on the character variety, RHYME on tau + physical magnitude
    assert "does NOT cross" in v["firewall"]
