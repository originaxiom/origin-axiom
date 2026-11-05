"""Review 74 (S299b): the anchor follow-up -- the anchor line, the core fresh-clone line from the run at the review's
landing, and the seven hand-kept views refreshed (README is generated). Usage: apply4_anchor.py <review commit> <fresh-clone line>"""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]; C = sys.argv[1]; FC = sys.argv[2]
p = ROOT / "docs/progress/REVIEWS.md"; t = p.read_text(encoding="utf-8")
old = "fresh-clone: PASS @ FRESHCLONE (gates all PASS; belt ok; the review's landing, before this line)"
assert t.count(old) == 1 and FC.startswith("fresh-clone: ")
t = t.replace(old, FC + " (the review's landing, before its anchor line)")
last = "- [ ] R74-10: the owner's choice among the ranked leads of § 3 for the next work (owner: the owner)"
assert t.rstrip().endswith(last)
t = t.rstrip("\n") + "\n\n**anchor-commit: `%s`**\n" % C
p.write_text(t, encoding="utf-8")
BLOCK = """## ⟳ VIEW REFRESH — 2026-11-04 (Review 74)

Touched at the Review 74 anchor (`%s`). **The window (B1819–B1830; S264b–S298) ran THE FINAL ATTACK to its end and audited
the record's own grading; the review then read the whole backlog for leads at the owner's word.**

- **THE FINAL ATTACK:** Step A NEGATIVE as a compression (B1823); Step B, the nine from one address, NOT FOUND under its bar
  (B1825). The frame's matter metric is CHOSEN (B1822, H = I).
- **The bar in two levels** (GENESIS v1.60, v1.61): a fixed screen makes a CANDIDATE; only a held-out prediction makes a
  result. One candidate family, THE SIX ON THE STRIP: it rests on the small-cut end and sits about 3σ from the relation D.
- **This review:** every open relay, every old harvest row and every open lead read in full — nothing hidden derives a
  number; the leads that could change the direction are ranked for the owner (REVIEWS, Review 74 § 3). θ̄ is not a
  prediction of the frame without a chosen rule, so **the candidate's confirmation is one held-out target short (P-597)**.
  The review loop's carry rule, which could not fire, now does; main's own unbacked claims of 3 November carry instruments.
- **0 of 19.**

""" % C
anchor = "## ⟳ VIEW REFRESH — 2026-10-30 (Review 73)"
for v in ("ROADMAP.md", "docs/CAMPAIGN_STATUS.md", "docs/MASTERPLAN.md", "docs/LEAD_REGISTER.md", "docs/OPEN_PROBLEMS.md",
          "docs/PRICED_DOORS.md", "docs/OPEN_LEADS.md"):
    q = ROOT / v; s = q.read_text(encoding="utf-8"); assert s.count(anchor) == 1, v
    q.write_text(s.replace(anchor, BLOCK + anchor), encoding="utf-8")
print("anchor", C, "and seven views refreshed")
