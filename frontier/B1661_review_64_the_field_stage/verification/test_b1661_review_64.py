"""B1661 -- Review 64's block is on the page with its anchor and core lines; Review 63's open items resolved or carried;
B1654's seal record recast (its seal check clean); B1660's repairs and post-seal files; the E80 and E65 instances; the
terms glossed."""
import hashlib, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]


def _t(*p):
    return ROOT.joinpath(*p).read_text(encoding="utf-8")


def test_review_64_block_anchor_core_lines_and_loop():
    t = _t("docs", "progress", "REVIEWS.md")
    i = t.index("# Review 64 (2026-10-16)"); blk = t[i:]
    assert "**anchor-commit: `bf44d9032`**" in blk
    assert "fresh-clone: PASS @ bf44d9032" in blk and "sample seed: 0bbbb6cab" in blk and "gate controls: 45 registered" in blk
    assert "@@SUITE@@" not in blk
    acts = blk.split("### Action items (Review 64)")[1]
    assert all(("R64-%d:" % n) in acts for n in range(1, 12))
    for carried in ("R63-1", "R63-2", "R63-4", "R63-5", "R63-6"):
        assert carried in acts, carried
    r63 = t[t.index("# Review 63 (2026-10-14)"):i]
    assert not re.search(r"^- \[ \]", r63.split("### Action items (Review 63)")[1], re.M)


def test_b1654_seal_record_is_in_the_checks_form():
    sys.path.insert(0, str(ROOT / "scripts" / "review")); import review_tools as rt
    A = ROOT / "frontier" / "B1654_the_norm_of_the_boundary_class"
    c = rt.seal_check((A / "ARTIFACT_HASHES.txt").read_text(), lambda rel: (A / rel).read_bytes() if (A / rel).exists() else None,
                      "155959126", "bf44d9032", lambda a, b: True, True, (A / "FINDINGS.md").read_text(), None)
    assert c["defects"] == [] and c["ok"] == c["lines"]
    assert _t("frontier", "B1654_the_norm_of_the_boundary_class", "ARTIFACT_HASHES.txt").count("# sealed at 155959126:") == 5
    assert "four reviewer helpers changed after the seal" in _t("frontier", "B1654_the_norm_of_the_boundary_class", "FINDINGS.md")


def test_b1660_repairs_and_post_seal_files():
    A = ROOT / "frontier" / "B1660_the_one_higgs_census"; f = _t("frontier", "B1660_the_one_higgs_census", "FINDINGS.md")
    assert "Every cell holds as predicted" not in f and "cannot reach five targets" not in f
    assert "Every cell's pass criterion held as sealed" in f
    h = (A / "ARTIFACT_HASHES.txt").read_text()
    for rel in ("verification/after_the_seal/ratio_ceiling.py", "verification/after_the_seal/down_lep_only_output.txt",
                "verification/the_one_higgs_census.json"):
        line = [l for l in h.splitlines() if l.endswith("  " + rel)][0]
        assert hashlib.sha256((A / rel).read_bytes()).hexdigest() == line.split()[0], rel
    assert "33.810" in (A / "verification" / "after_the_seal" / "ratio_ceiling_output.txt").read_text()


def test_the_filings():
    e = _t("docs", "ERROR_LEDGER.md")
    assert "PRE-SEAL HELPERS ROOTED IN THE DRAFT ROOM" in e and "A READING NARROWED BEFORE IT WAS COMPUTED" in e
    g = _t("TERMINOLOGY.md"); assert "## Added at Review 64 (2026-10-16)" in g
    b = _t("tests", "test_b1421_completeness_sweep.py"); assert "== 9 and int(m.group(2)) == 13" in b and "[Review 64, 2026-10-16]" in b
    for term in ("committed unread", "a scoreboard", "the joint law", "the arena"):
        assert "**%s**" % term in g, term
