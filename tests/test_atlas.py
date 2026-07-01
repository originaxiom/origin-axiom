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
    # the method (trace map) and the two ends are pervasive; kappa is the ~30% first integral
    assert FREQ["trace_map"] / N > 0.45
    assert FREQ["golden"] / N > 0.45
    assert FREQ["figure_eight"] / N > 0.40
    assert 0.20 < FREQ["kappa"] / N < 0.40


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


def test_motif_trace_and_neighbors_and_cooccurrence():
    t = query.motif_trace("kappa", G)
    assert t["count"] == FREQ["kappa"] and t["probes"]
    assert query.neighbors("kappa", G)["neighbors"]
    assert query.cooccurrence("golden", "eisenstein", G)["count"] > 0


def test_gaps_finds_under_resolved_obstacles():
    g = query.gaps(G)
    assert g["under_resolved"]                            # some obstacle-type has few banked resolutions


# -- the render regenerates ------------------------------------------------------------------------
def test_render_regenerates_the_map():
    out, n = render.render()
    assert os.path.exists(out) and n == N
    with open(out, encoding="utf-8") as f:
        head = f.read(4000)
    assert "GENERATED" in head and "context card" in head
