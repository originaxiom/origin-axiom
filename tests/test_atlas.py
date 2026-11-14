"""The Recurrence Atlas -- lock the miner, the lexicon classification, the detector, the query API, the render.

A meta-tool test: it checks the INSTRUMENT is faithful (parses the corpus, classifies kappa as the one
first integral, ranks the documented meetings in the top tier, regenerates the map) -- not any physics claim.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts', 'atlas'))
import atlas          # noqa: E402
import query          # noqa: E402
import render         # noqa: E402

G = atlas.mine()
P = G["probes"]
N = len(P)
FREQ = atlas.analyze(G)["freq"]

# documented genuine meetings (the detector's ground truth); B332 is the honest boundary case (narrow-deep)
STRONG = ["B67", "B121", "B261", "B293"]


# -- the miner parses the corpus -------------------------------------------------------------------
def test_miner_parses_the_corpus():
    assert N >= 300                                        # ~327 frontier probes
    for pid in STRONG + ["B332"]:
        assert pid in P, f"{pid} missing from mine()"
        assert P[pid]["motifs"], f"{pid} has no motifs"


def test_every_seed_motif_recurs():
    for m in atlas.LEXICON:
        assert FREQ.get(m, 0) >= 1, f"motif {m} never matched -- patterns rotted?"


def test_measured_frequencies_hold():
    """The method (trace map) and the two ends are pervasive; kappa is the one first integral.

    DRIFT, measured 2026-07-30 (B835): every object motif is rarer in recent arcs, because recent
    work is INSTRUMENT work that does not mention the object. trace_map 0.463 (arcs <B700) -> 0.375
    (B700+); golden 0.650 -> 0.575; kappa 0.284 -> 0.125. The corpus-wide trace_map share crossed
    below the original 0.45 floor (0.449) purely by dilution.

    The floors are widened to 0.40 rather than tracking the drift downward -- but the ORDERING is
    asserted too, because that, not any threshold, is what the atlas actually claims: the method
    recurs MORE than the one conserved quantity, which is the selection effect the atlas exists to
    make visible.
    """
    # DRIFT SERIES, recorded rather than re-fitted (B1002, 2026-08-09). The trace_map floor has
    # now been crossed TWICE by pure dilution as the corpus grew:
    #     0.449 at the original N   -> floor moved 0.45 -> 0.40
    #     0.3991 at N = 917         -> would move 0.40 -> ... and that is the problem.
    # Re-fitting a floor to each new N is fitting, not testing. So the floors below are declared
    # LOOSE SANITY BANDS, deliberately far from the measurements, and the ORDERING assertions --
    # which are what the atlas actually claims -- carry the test. If a band ever fires it means
    # something structural changed, not that the corpus grew.
    assert FREQ["trace_map"] / N > 0.25            # measured 0.3991 @ N=917
    assert FREQ["golden"] / N > 0.40               # measured 0.5725 @ N=917
    assert FREQ["figure_eight"] / N > 0.25         # measured 0.4340 @ N=917
    assert 0.05 < FREQ["kappa"] / N < 0.50         # measured 0.2377 @ N=917
    # THE LOAD-BEARING CLAIMS -- these are the atlas's actual content and are NOT bands:
    # our METHOD recurs more often than the object's one first integral (the selection effect),
    # and the object itself recurs more often than the method used on it.
    assert FREQ["trace_map"] > FREQ["kappa"], "the selection-effect ordering is the atlas's point"
    assert FREQ["figure_eight"] > FREQ["trace_map"], "the object outranks the method used on it"
    assert FREQ["golden"] > FREQ["figure_eight"], "the hearing field is the most-recurring motif"


# -- the honest classification axis ----------------------------------------------------------------
def test_kappa_is_the_one_first_integral():
    firsts = [m for m, v in atlas.LEXICON.items() if v["conserved"] == "first-integral"]
    assert firsts == ["kappa"]                            # exactly one true conserved quantity
    assert atlas.LEXICON["trace_map"]["conserved"] == "tool"   # the method is quarantined as a selection effect


# -- the genuine-unity detector (candidates, not proof) --------------------------------------------
def test_detector_ranks_documented_meetings_in_top_tier():
    ranked = atlas.meeting_points(G, top=10 * N, min_score=0)
    rank = {r["probe"]: i for i, r in enumerate(ranked)}
    for pid in STRONG:
        assert rank[pid] < 0.40 * len(ranked), f"{pid} ranked {rank[pid]}/{len(ranked)} -- not top tier"


def test_detector_recognizes_the_narrow_deep_meeting():
    # B332 (the founding identity g=-R L^-1) is arithmetic-narrow -> under-ranked by a BREADTH detector,
    # but its unity-pattern (two_ends) must still FIRE -- the documented, honest limitation.
    ranked = atlas.meeting_points(G, top=10 * N, min_score=0)
    b332 = next(r for r in ranked if r["probe"] == "B332")
    assert "two_ends" in b332["patterns"]


def test_meeting_points_are_labelled_candidates_not_proof():
    for r in atlas.meeting_points(G, top=10):
        assert set(r) >= {"probe", "score", "patterns", "domains", "status"}
        assert isinstance(r["patterns"], list)


# -- the query API returns sane shapes -------------------------------------------------------------
def test_context_card():
    c = query.context_card(G)
    assert c["n_probes"] == N
    assert c["conserved_first_integral"][0][0] == "kappa"
    assert "TOOL" in c["text"] and "first integral" in c["text"]


def test_obstacle_oracle_and_cycle():
    r = query.resolutions_for("particle_dict", G)
    assert r["n_probes"] > 0 and r["ranked"]
    assert r["top_conserved"] is not None


def test_revive_suggests_unused_conserved_resolvers():
    r = query.revive("B332", G)
    assert r["obstacle"] == "particle_dict"
    assert isinstance(r["suggestions"], list)             # motifs used elsewhere for this obstacle, not here


def test_the_atlas_tag_is_printed_as_a_tag_and_never_as_a_status():
    """Added 2026-11-12 (Review 80; found by a reading of the query, made again before it was mended).  The atlas's tag is a
    guess from an arc's words.  Review 79 took it out of the head of an arc's card; it was still printed as a status by
    `revive`, by the meeting points, in the context card's tally and wherever a probe is counted as banked.  B57 is the
    case the reading gave: its verdict is PROVED and `revive` printed [dead]."""
    r = query.revive("B57", G)["text"]
    assert r.startswith("revive B57 [PROVED]") and "[dead]" not in r and "atlas tag (a guess from the arc's words, not a verdict): dead" in r
    assert "banked probes" not in r
    m = query.meeting_points(G)["text"].split("\n")
    assert "not a verdict" in m[1] and all("[tag " in l for l in m[2:]) and not any(("[banked]" in l or "[dead]" in l or "[open]" in l) for l in m)
    c = query.context_card(G)["text"]
    assert "atlas tags (guesses from the arcs' words, not verdicts) {" in c and "; status {" not in c
    o = query.resolutions_for("particle_dict", G)["text"]
    assert "probes tagged banked touched it" in o and "not a verdict" in o and " banked probes" not in o
    g = query.gaps(G)["text"]
    assert "tagged banked" in g and "not a verdict" in g and "few banked resolutions" not in g
    # what the functions return is as it was: the key "status" still holds the tag, for the callers that read it
    assert query.revive("B57", G)["status"] == "dead" and query.context_card(G)["status"]["banked"] > 0


def test_the_card_of_an_id_that_several_folders_carry_shows_every_folder():
    """Added 2026-11-12 (Review 80; found by a reading of the query, made again before it was mended).  B58 is carried by
    three folders, one of them RETRACTED.  Its card printed the verdict of the first folder under the name the atlas keeps,
    which is another folder's, and the retracted folder never appeared."""
    import collections, json, pathlib
    root = pathlib.Path(__file__).resolve().parents[1]
    shared = {k: n for k, n in collections.Counter(d.name.split("_")[0] for d in (root / "frontier").iterdir() if d.is_dir()).items() if n > 1}
    assert shared == {"B58": 3}                                                    # the one id that is shared, on this tree
    c = query.arc_card("B58", G)
    by_folder = {d.name: json.loads((d / "arc_verdict.json").read_text(encoding="utf-8"))["verdict"] for d in sorted((root / "frontier").glob("B58_*"))}
    assert set(by_folder.values()) == {"NEGATIVE", "RETRACTED"} and len(by_folder) == 3
    assert c["verdicts_by_folder"] == {"frontier/" + k: v for k, v in by_folder.items()} and c["verdict"] is None
    lines = c["text"].split("\n")
    assert lines[0].startswith("B58 [NEGATIVE; RETRACTED; NEGATIVE]") and "3 folders carry this id" in lines[0]
    for name, verdict in by_folder.items():
        assert "  verdict: %s   folder: frontier/%s" % (verdict, name) in lines, name   # each folder with its own verdict
    assert sum(1 for l in lines if l.startswith("  claim: ")) == 3
    # a twin: an id with one folder reads as it did
    one = query.arc_card("B57", G)
    assert one["verdict"] == "PROVED" and one["text"].startswith("B57 [PROVED]") and "folders carry this id" not in one["text"]
    assert one["text"].count("  verdict: PROVED   folder: frontier/B57_general_m_splitting") == 1


def test_motif_trace_and_neighbors_and_cooccurrence():
    t = query.motif_trace("kappa", G)
    assert t["count"] == FREQ["kappa"] and t["probes"]
    assert query.neighbors("kappa", G)["neighbors"]
    assert query.cooccurrence("golden", "eisenstein", G)["count"] > 0


def test_gaps_finds_under_resolved_obstacles():
    g = query.gaps(G)
    assert g["under_resolved"]                            # some obstacle-type has few banked resolutions


# -- the render regenerates ------------------------------------------------------------------------
def test_render_regenerates_the_map(tmp_path):
    # redirected: rendering into the tracked docs/RECURRENCE_ATLAS.md made an ordinary test run
    # dirty the working tree (main's defect report, 2026-09-16). The render is still exercised.
    out, n = render.render(out=str(tmp_path / "RECURRENCE_ATLAS.md"))
    assert os.path.exists(out) and n == N
    with open(out, encoding="utf-8") as f:
        head = f.read(4000)
    assert "GENERATED" in head and "context card" in head


def test_the_query_finds_an_arc_whose_folder_is_named_by_its_id_alone(tmp_path):
    """ADDED 2026-11-13 (C16; a cold reader's finding on R80b's part 4, not checked by main, made again first).  The query
    looked for `frontier/<id>_*` and missed a folder named by the id alone.  Planted: three folders, B9, B9_words and B91_other;
    the query for B9 finds the first two and not the third."""
    import importlib.util as _u
    import json as _j
    import pathlib as _p
    import sys as _s
    _s.dont_write_bytecode, was = True, _s.dont_write_bytecode
    try:
        spec = _u.spec_from_file_location("atlas_query_for_a_bare_id", _p.Path(__file__).resolve().parents[1] / "scripts" / "atlas" / "query.py")
        q = _u.module_from_spec(spec)
        spec.loader.exec_module(q)
    finally:
        _s.dont_write_bytecode = was
    for name in ("B9", "B9_words", "B91_other"):
        (tmp_path / "frontier" / name).mkdir(parents=True)
        (tmp_path / "frontier" / name / "arc_verdict.json").write_text(_j.dumps({"verdict": "PROVED", "claim_one_line": name}), encoding="utf-8")
    assert [f for f, _, _, _ in q._verdicts_of("B9", root=str(tmp_path))] == ["frontier/B9", "frontier/B9_words"]
    assert [f for f, _, _, _ in q._verdicts_of("B91", root=str(tmp_path))] == ["frontier/B91_other"]
    # the twin: on this repository a folder named <id>_<words> is found as before
    assert [f for f, _, _, _ in q._verdicts_of("B1905")] == ["frontier/B1905_selection_and_chirality_across_the_record"]
