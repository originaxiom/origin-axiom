"""B1461 -- every gate has a test that makes it FAIL (Review 58's governance delta, item 3a; R58-2's twelve and six more).

Each test plants a bad input through the gate's own seams (gates._read, gates.ROOT, gates._git, or a checker module's
ROOT / I-O helpers) and asserts the gate returns ok == False; where cheap it also shows the planted-good case passes.
The registry tests/GATE_CONTROLS.json names, for every gate, the test function that proves its failing path; the gate
`gate-controls` checks the registry is complete and every named function exists.
"""
import json, os, re, sys, pathlib
import pytest
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts", "gates")); sys.path.insert(0, os.path.join(ROOT, "scripts", "checks"))
import gates


def _reader(mapping):
    real = gates._read
    def rd(rel):
        return mapping[rel] if rel in mapping else real(rel)
    return rd


def _git_repo_with(root, *rels):
    """a throwaway git repository whose index holds `rels` (the checkers read `git ls-files`)"""
    import subprocess
    subprocess.run(["git", "init", "--quiet", str(root)], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(root), "add", "--"] + list(rels), check=True, capture_output=True)


def test_firewall_oneway_fails_on_a_speculation_row_in_proven(monkeypatch):
    monkeypatch.setattr(gates, "_read", _reader({"CLAIMS.md": "## Proven\n| C1 | speculations/x.md |\n"}))
    ok, _ = gates.gate_firewall_oneway(); assert ok is False
    monkeypatch.setattr(gates, "_read", _reader({"CLAIMS.md": "## Proven\n| C1 | frontier/B1_x/FINDINGS.md |\n"}))
    assert gates.gate_firewall_oneway()[0] is True


def test_append_only_fails_when_the_log_shares_no_suffix_with_head(monkeypatch):
    monkeypatch.setattr(gates, "_git", lambda *a: (0, "## 2026-01-01 -- A\n\nbody\n"))
    monkeypatch.setattr(gates, "_read", _reader({"PROGRESS_LOG.md": "something else entirely\n"}))
    ok, why = gates.gate_append_only(); assert ok is False, why
    monkeypatch.setattr(gates, "_read", _reader({"PROGRESS_LOG.md": "## 2026-01-01 -- A\n\nbody\n\n## 2026-01-02 -- B\n"}))
    assert gates.gate_append_only()[0] is True


def test_views_fresh_fails_when_no_view_moved_since_the_anchor(monkeypatch):
    monkeypatch.setattr(gates, "_read", _reader({gates.REVIEWS: "x\n\nanchor-commit: `0123456789ab`\n"}))
    monkeypatch.setattr(gates, "_git", lambda *a: (0, "0"))
    ok, why = gates.gate_views_fresh(); assert ok is False and "not refreshed" in why
    monkeypatch.setattr(gates, "_git", lambda *a: (0, "3"))
    assert gates.gate_views_fresh()[0] is True


def test_id_collisions_fails_on_two_arcs_with_one_number(tmp_path, monkeypatch):
    (tmp_path / "frontier" / "B99990_a").mkdir(parents=True); (tmp_path / "frontier" / "B99990_b").mkdir()
    monkeypatch.setattr(gates, "ROOT", str(tmp_path))
    ok, why = gates.gate_id_collisions(); assert ok is False and "B99990" in why


def test_knowledge_index_fails_on_an_unindexed_explainer(tmp_path, monkeypatch):
    k = tmp_path / "knowledge"; k.mkdir(); (k / "INDEX.md").write_text("# index\n"); (k / "K999_orphan.md").write_text("x")
    monkeypatch.setattr(gates, "ROOT", str(tmp_path)); monkeypatch.setattr(gates, "_read", lambda rel: open(rel if os.path.isabs(rel) else os.path.join(str(tmp_path), rel)).read())
    ok, why = gates.gate_knowledge_index(); assert ok is False and "K999" in why


def test_path_refs_fails_on_a_dangling_backticked_path(tmp_path, monkeypatch):
    import check_path_references as cpr
    (tmp_path / "docs").mkdir(); (tmp_path / "docs" / "a.md").write_text("see `scripts/does_not_exist.py` here\n")
    _git_repo_with(tmp_path, "docs/a.md")                                   # the checker reads git's index, not the disk
    monkeypatch.setattr(cpr, "ROOT", str(tmp_path))
    total, bad = cpr.scan(); assert bad and any("does_not_exist" in t for _, t in bad)
    assert gates.GATES["path-refs"] is gates.gate_path_refs                      # R60-4: the test names the gate it controls


def test_test_vacuity_fails_on_a_test_with_no_assert(tmp_path, monkeypatch):
    import check_test_vacuity as ctv
    (tmp_path / "tests").mkdir(); (tmp_path / "tests" / "test_planted.py").write_text("def test_nothing():\n    pass\n")
    _git_repo_with(tmp_path, "tests/test_planted.py")
    monkeypatch.setattr(ctv, "ROOT", str(tmp_path))
    total, no_assert, tautology, both = ctv.scan(); assert no_assert, (total, no_assert)
    assert gates.GATES["test-vacuity"] is gates.gate_test_vacuity                 # R60-4


def test_views_generated_fails_when_a_generator_is_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(gates, "ROOT", str(tmp_path))
    ok, why = gates.gate_views_generated(); assert ok is False and "generator missing" in why


def test_practices_register_fails_when_a_gate_has_no_row(monkeypatch):
    monkeypatch.setattr(gates, "_read", _reader({gates.PRACTICES: "# practices\n\nno gates named here\n"}))
    ok, why = gates.gate_practices_register(); assert ok is False and "absent from the register" in why


def _ledger_row(date, rel, digest):
    return f"| {date} | B0 | a seal | `{rel}` | `{digest}` |\n"



def test_seal_digests_fails_on_a_digest_that_does_not_recompute(monkeypatch):
    row = _ledger_row("2026-10-01", "README.md", "0" * 64)
    monkeypatch.setattr(gates, "_read", _reader({"docs/SEAL_LEDGER.md": row}))
    ok, why = gates.gate_seal_digests(); assert ok is False and "README.md" in str(why)


def test_lawmap_scope_fails_on_an_unscoped_row_over_a_heavily_scoped_arc(tmp_path, monkeypatch):
    heavy = "holds only for m004; the scope is level one; assumes the frame F-HE; conditional on a source; not established beyond it"
    assert gates._scope_count(heavy) >= gates.SCOPE_HEAVY, gates._scope_count(heavy)
    a = tmp_path / "frontier" / "B9991_x"; a.mkdir(parents=True)
    (a / "arc_verdict.json").write_text(json.dumps(dict(id="B9991", claim_one_line=heavy)))
    monkeypatch.setattr(gates, "ROOT", str(tmp_path))
    monkeypatch.setattr(gates, "_read", _reader({"docs/LAW_MAP.md": "| **A LAW** | it holds everywhere (B9991) | status | B9991 | x |\n"}))
    ok, why = gates.gate_lawmap_scope(); assert ok is False and "A LAW" in str(why)


def test_retraction_sweep_fails_on_a_retracted_phrase_in_a_living_file(tmp_path, monkeypatch):
    import retraction_sweep as rs
    (tmp_path / "docs").mkdir(); (tmp_path / "docs" / "live.md").write_text("we still say the forbidden claim here\n")
    monkeypatch.setattr(rs, "ROOT", str(tmp_path)); monkeypatch.setattr(rs, "_phrases", lambda: ["the forbidden claim"])
    monkeypatch.setattr(rs, "_tracked_md", lambda: ["docs/live.md"])
    v = rs.sweep(); assert v and v[0][0] == "docs/live.md"


def test_representation_sweep_fails_on_a_substantial_arc_cited_nowhere(monkeypatch):
    import representation_sweep as rsw
    monkeypatch.setattr(rsw, "substantial_arcs", lambda: [("B99992", "PROVED", 900)])
    monkeypatch.setattr(rsw, "_surfaces_text", lambda: ""); monkeypatch.setattr(rsw, "_triaged", lambda: set())
    assert rsw.sweep() == [("B99992", "PROVED", 900)]
    monkeypatch.setattr(rsw, "_triaged", lambda: {"B99992"}); assert rsw.sweep() == []
    assert gates.GATES["representation-sweep"] is gates.gate_representation_sweep   # R60-4


def test_seen_first_fails_on_an_arc_without_the_section(tmp_path):
    a = tmp_path / "frontier" / "B99993_x"; a.mkdir(parents=True); (a / "FINDINGS.md").write_text("# B99993\n\n## 1. No seen-first here\n")
    bad = gates.seen_first_missing(root=str(tmp_path)); assert bad and "B99993" in bad[0]
    (a / "FINDINGS.md").write_text("# B99993\n\n## 0. Seen first\n\n- topic-sweep run; literature: none needed.\n")
    assert gates.seen_first_missing(root=str(tmp_path)) == []


def test_genesis_cited_fails_on_a_page_that_lost_its_pointer(tmp_path):
    (tmp_path / "GENESIS.md").write_text("# GENESIS\n\n**Version 1.5 · x · canonical.**\n")
    for rel in gates.GENESIS_POINTERS:
        p = tmp_path / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text("# a page with no pointer\n")
    bad = gates.genesis_problems(root=str(tmp_path)); assert bad


def test_chain_locks_fails_on_a_theorem_link_with_a_prose_lock(monkeypatch):
    monkeypatch.setattr(gates, "_read", _reader({gates.CHAIN: "**C1 [THEOREM] a claim.** rests on the B730 locks.\n"}))
    ok, why = gates.gate_chain_locks(); assert ok is False and "C1" in str(why)


def test_law_map_provenance_fails_on_a_row_citing_no_arc(monkeypatch):
    monkeypatch.setattr(gates, "_read", _reader({gates.LAW_MAP: "| law | statement | status | source | tension |\n|---|---|---|---|---|\n| **X** | a law with no arc | status | none | - |\n"}))
    ok, why = gates.gate_law_map_provenance(); assert ok is False and "cite no arc" in str(why)


def test_framing_fails_on_a_banned_phrase_in_a_root_page(tmp_path, monkeypatch):
    (tmp_path / "PLANTED.md").write_text("intro " + gates.BANNED[0] + " outro\n")
    for d in gates.FRAMING_SCOPE_DIRS: (tmp_path / d).mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(gates, "ROOT", str(tmp_path)); monkeypatch.setattr(gates, "_read", lambda rel: open(os.path.join(str(tmp_path), rel)).read())
    ok, hits = gates.gate_framing(); assert ok is False and hits[0][0] == "PLANTED.md"


def test_claims_fails_on_a_missing_section_and_a_dead_evidence_path(monkeypatch):
    monkeypatch.setattr(gates, "_read", _reader({"CLAIMS.md": "## Proven\n| P1 | `tests/test_does_not_exist_9.py` |\n## Conditional\n## Open\n"}))
    ok, problems = gates.gate_claims(); assert ok is False
    assert any("missing section" in p for p in problems) and any("evidence missing" in p for p in problems)


def test_atlas_fresh_fails_when_an_arc_dir_is_not_in_the_atlas(tmp_path, monkeypatch):
    a = tmp_path / "frontier" / "B99994_x"; a.mkdir(parents=True); (a / "FINDINGS.md").write_text("# x\n")
    monkeypatch.setattr(gates, "ROOT", str(tmp_path)); monkeypatch.setattr(gates, "_read", _reader({"scripts/atlas/atlas_data.json": json.dumps({"probes": {}})}))
    ok, why = gates.gate_atlas_fresh(); assert ok is False and "B99994" in why


def test_arc_verdicts_fails_on_findings_without_a_verdict_file(tmp_path, monkeypatch):
    a = tmp_path / "frontier" / "B99995_x"; a.mkdir(parents=True); (a / "FINDINGS.md").write_text("# x\n")
    monkeypatch.setattr(gates, "ROOT", str(tmp_path))
    ok, why = gates.gate_arc_verdicts(); assert ok is False and "B99995_x" in why


def test_attribution_fails_on_a_vendor_token_above_baseline(monkeypatch):
    tok = gates._VENDOR_TOKS[0]
    monkeypatch.setattr(gates, "_git", lambda *a: (0, "docs/planted_note.md\n"))
    monkeypatch.setattr(gates, "_read", _reader({"docs/planted_note.md": "written with %s today\n" % tok}))
    ok, hits = gates.gate_attribution(); assert ok is False and "docs/planted_note.md" in str(hits)


def test_theorem_registry_fails_on_a_creates_law_arc_absent_from_the_registry(tmp_path, monkeypatch):
    a = tmp_path / "frontier" / "B99996_x"; a.mkdir(parents=True); (tmp_path / "docs").mkdir()
    (a / "arc_verdict.json").write_text(json.dumps(dict(id="B99996", verdict="PROVED", creates_law=True)))
    (tmp_path / "docs" / "THEOREM_REGISTRY.md").write_text("# registry\n\nnothing here\n")
    monkeypatch.setattr(gates, "ROOT", str(tmp_path))
    ok, why = gates.gate_theorem_registry(); assert ok is False and "B99996" in str(why)


def test_retraction_debt_fails_when_its_checker_exits_nonzero(tmp_path, monkeypatch):
    (tmp_path / "scripts" / "checks").mkdir(parents=True)
    (tmp_path / "scripts" / "checks" / "retraction_debt.py").write_text("import sys; print('planted debt'); sys.exit(1)\n")
    monkeypatch.setattr(gates, "ROOT", str(tmp_path))
    ok, why = gates.gate_retraction_debt(); assert ok is False and "planted debt" in why


def test_seal_provenance_fails_on_a_new_seal_without_the_two_halves(tmp_path):
    a = tmp_path / "frontier" / "B99997_x"; a.mkdir(parents=True)
    (a / "PREREGISTRATION.md").write_text("# sealed\n\n## 1. The claim\n\nno provenance halves here\n")
    bad = gates.seal_provenance_problems(root=str(tmp_path)); assert bad == ["frontier/B99997_x/PREREGISTRATION.md"]
    (a / "PREREGISTRATION.md").write_text("# sealed\n\n## 0. Seen first\n\nswept\n\n## 4. Disclosed\n\nknown before\n")
    assert gates.seal_provenance_problems(root=str(tmp_path)) == []
    (a / "PREREGISTRATION.md").write_text("# sealed\n\nBANKED IDENTITY: x\nPRIOR ART: y\n")
    assert gates.seal_provenance_problems(root=str(tmp_path)) == []
    b = tmp_path / "frontier" / "B1000_old"; b.mkdir(); (b / "PREREGISTRATION.md").write_text("# an old seal, in the frozen baseline\n")
    assert gates.seal_provenance_problems(root=str(tmp_path)) == []                       # baseline: listed, not repaired
    assert gates.seal_provenance_problems(root=str(tmp_path), baseline=frozenset()) == ["frontier/B1000_old/PREREGISTRATION.md"]


def test_seal_digests_reads_the_arc_first_row_shape_too(monkeypatch):
    row = "| B0 | `README.md` | `%s` | 2026-10-01 | an arc-first row |\n" % ("0" * 64)
    monkeypatch.setattr(gates, "_read", _reader({"docs/SEAL_LEDGER.md": row}))
    ok, why = gates.gate_seal_digests(); assert ok is False and "README.md" in str(why)
    rows = gates._seal_ledger_rows(row + "| 2026-10-02 | B1 | x | `GOVERNANCE.md` | `%s` |\n" % ("1" * 64))
    assert [r[1] for r in rows] == ["README.md", "GOVERNANCE.md"] and [r[0] for r in rows] == ["2026-10-01", "2026-10-02"]


def test_seal_ledger_current_fails_when_a_sealed_file_has_no_row(monkeypatch):
    monkeypatch.setattr(gates, "_read", _reader({"docs/SEAL_LEDGER.md": "# ledger\n\n| sealed document | sha8 |\n|---|---|\n"}))
    ok, why = gates.gate_seal_ledger_current(); assert ok is False and "not in the generated table" in why


def test_pretense_phrases_fails_on_a_claimed_external_verification_and_spares_the_disclaimer(tmp_path):
    (tmp_path / "docs").mkdir(); (tmp_path / "PLANTED.md").write_text("This result was externally verified by a lab.\n")
    hits = gates.pretense_hits(root=str(tmp_path)); assert hits == [("PLANTED.md", "externally verified", 1)]
    (tmp_path / "PLANTED.md").write_text("Nothing here is externally verified or peer-reviewed.\n")
    assert gates.pretense_hits(root=str(tmp_path)) == []


def test_seal_provenance_rejects_an_attestation_whose_quote_is_not_in_the_file(tmp_path, monkeypatch):
    a = tmp_path / "frontier" / "B99998_x"; a.mkdir(parents=True); (a / "PREREGISTRATION.md").write_text("# sealed\n\nwe reproduce the banked count first; the record was swept\n")
    (tmp_path / "tests").mkdir()
    import json as _json
    (tmp_path / "tests" / "SEAL_PROVENANCE_ATTESTATIONS.json").write_text(_json.dumps({"B99998": {"banked_identity": "we reproduce the banked count first", "prior_art": "the record was swept"}}))
    assert gates.seal_provenance_problems(root=str(tmp_path), baseline=frozenset()) == []
    (tmp_path / "tests" / "SEAL_PROVENANCE_ATTESTATIONS.json").write_text(_json.dumps({"B99998": {"banked_identity": "a sentence that is not in the file", "prior_art": "the record was swept"}}))
    assert gates.seal_provenance_problems(root=str(tmp_path), baseline=frozenset()) == ["frontier/B99998_x/PREREGISTRATION.md"]


def test_the_registry_is_complete_and_every_named_test_exists():
    reg = json.load(open(os.path.join(ROOT, "tests", "GATE_CONTROLS.json")))
    missing = sorted(g for g in gates.GATES if g not in reg); assert missing == [], missing
    for g, ref in reg.items():
        f, fn = ref.split("::"); src = open(os.path.join(ROOT, f)).read()
        assert re.search(r"^def %s\(" % re.escape(fn), src, re.M), (g, ref)
    assert gates.gate_gate_controls()[0] is True


def test_the_short_claim_lane_admits_a_depended_on_arc(monkeypatch):
    import representation_sweep as rsw
    monkeypatch.setattr(rsw, "_INDEG", {"B9": 2, "B8": 1})
    import json as _json, tempfile, pathlib
    d = pathlib.Path(tempfile.mkdtemp())
    for a, claim in (("B9", "short"), ("B8", "short too"), ("B7", "x" * 600)):
        (d / "frontier" / (a + "_x")).mkdir(parents=True); (d / "frontier" / (a + "_x") / "arc_verdict.json").write_text(_json.dumps(dict(id=a, verdict="PROVED", claim_one_line=claim)))
    monkeypatch.setattr(rsw, "ROOT", str(d))
    ids = sorted(i for i, _, _ in rsw.substantial_arcs())
    assert ids == ["B7", "B9"], ids            # the long claim and the depended-on short one; the in-degree-1 short one stays out


def test_member_scope_fails_on_a_new_negative_that_says_the_object_and_spares_a_named_member(tmp_path, monkeypatch):
    import json as _json
    mapping = {
        "frontier/B99996_x/arc_verdict.json": _json.dumps({"id": "B99996", "verdict": "NEGATIVE", "claim_one_line": "the object cannot carry a third generation"}),
        "frontier/B99997_y/arc_verdict.json": _json.dumps({"id": "B99997", "verdict": "NEGATIVE", "claim_one_line": "m004 cannot carry a third generation; the family is not tested"}),
        "frontier/B99998_z/arc_verdict.json": _json.dumps({"id": "B99998", "verdict": "PROVED", "claim_one_line": "the object cannot be anything but itself"}),
    }
    monkeypatch.setattr(gates.glob, "glob", lambda pat: [os.path.join(gates.ROOT, k) for k in mapping])
    hits = gates.member_scope_hits(reader=lambda rel: mapping[rel.replace(os.sep, "/")])
    assert hits == [("B99996", "the object cannot")]
    monkeypatch.setattr(gates, "MEMBER_SCOPE_BASELINE", 0)
    ok, msg = gates.gate_member_scope(reader=lambda rel: mapping[rel.replace(os.sep, "/")]); assert not ok and "B99996" in msg
    monkeypatch.setattr(gates, "MEMBER_SCOPE_BASELINE", 1)
    ok, _ = gates.gate_member_scope(reader=lambda rel: mapping[rel.replace(os.sep, "/")]); assert ok


def test_seat_positive_verified_fails_on_an_undeclared_or_unverified_seat_result(monkeypatch):
    """B1487: an arc that rests on a seat item without a VERIFIED harvest row fails; with the row it passes; a non-id fails."""
    import json as _json
    ledger = ("# ledger\n\n| # | seat | item | h | p | disposition | arc | date |\n|---|---|---|---|---|---|---|---|\n"
              "| 1 | SM-derivation seat | sm:B9001 | \"x\" | `p` @ 0 | **VERIFIED by re-run** | B9 | d |\n"
              "| 2 | SM-derivation seat | sm:B9002 | \"y\" | `p` @ 0 | **REGISTERED at headline level** | B9 | d |\n")
    mapping = {
        "docs/HARVEST_LEDGER.md": ledger,
        "frontier/B99990_a/arc_verdict.json": _json.dumps({"id": "B99990", "verdict": "PROVED", "rests_on_seat": ["sm:B9001"]}),
        "frontier/B99991_b/arc_verdict.json": _json.dumps({"id": "B99991", "verdict": "PROVED", "rests_on_seat": ["sm:B9002"]}),
    }
    monkeypatch.setattr(gates.glob, "glob", lambda pat: [os.path.join(gates.ROOT, k) for k in mapping if k.startswith("frontier/")])
    reader = lambda rel: mapping[rel.replace(os.sep, "/")]
    ok, msg = gates.gate_seat_positive_verified(reader=reader); assert not ok and "B99991" in msg and "sm:B9002" in msg
    mapping["frontier/B99991_b/arc_verdict.json"] = _json.dumps({"id": "B99991", "verdict": "PROVED", "rests_on_seat": ["sm:B9001"]})
    ok, msg = gates.gate_seat_positive_verified(reader=reader); assert ok and "2 declared" in msg
    mapping["frontier/B99991_b/arc_verdict.json"] = _json.dumps({"id": "B99991", "verdict": "PROVED", "rests_on_seat": ["not-an-id"]})
    ok, msg = gates.gate_seat_positive_verified(reader=reader); assert not ok and "not a seat item id" in msg
    assert "seat-positive-verified" in gates.GATES
    # R62-3: a dossier item (sm:W<n>) is checked against the SM seat's row for it by its bare name
    mapping["docs/HARVEST_LEDGER.md"] = ledger + ("| 3 | SM-derivation seat | W7 (a dossier item) | \"z\" | NOTE @ 0 | **VERIFIED on main** | B9 | d |\n"
                                                  "| 4 | SM-derivation seat | W8 (another) | \"w\" | NOTE @ 0 | **REGISTERED** | B9 | d |\n"
                                                  "| 5 | audit seat | W9 (not the SM seat's) | \"v\" | p @ 0 | **VERIFIED** | B9 | d |\n")
    mapping["frontier/B99991_b/arc_verdict.json"] = _json.dumps({"id": "B99991", "verdict": "PROVED", "rests_on_seat": ["sm:W7"]})
    ok, msg = gates.gate_seat_positive_verified(reader=reader); assert ok, msg
    for bad_w in ("sm:W8", "sm:W9", "sm:W70"):          # registered only; another seat's row; a different item sharing a prefix
        mapping["frontier/B99991_b/arc_verdict.json"] = _json.dumps({"id": "B99991", "verdict": "PROVED", "rests_on_seat": [bad_w]})
        ok, msg = gates.gate_seat_positive_verified(reader=reader); assert not ok and bad_w in msg, bad_w
