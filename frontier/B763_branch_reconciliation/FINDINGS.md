# FINDINGS — B763: the branch-reconciliation sweep — no lost conclusions; one standing rule minted

cc banking seat, 2026-07-22, owner directive ("mark this point... process each... resume
clean"). Marker tag: `pre-branch-reconciliation` on main. Full unmerged-branch inventory
run and classified. Nothing to CLAIMS.

## The classification (every unmerged ref, disposed)

**Stale refs of banked content — DELETED/PRUNED (6):** hunt/p2-spectral (banked #1255),
phenomenology/theorem-chain (#1263/#1266), qp-sequence-gate (#1266), r28-3-h-ear (#1265),
genesis/axiom-chain (local; #1243), + the codeberg mirror of hunt/p2-spectral. Squash-merge
leaves branch refs alive; deletion is their processing.

**Frozen-by-policy seat records — KEPT, now REGISTERED (3 + mirrors):**
- `closure/phase1-duels` (+24): the parallel-audit seat's frozen record (the Closure
  Campaign + the Origin Postulate adjudication). Its deliverables were ingested via
  integrate-don't-merge (PROGRESS_LOG 2026-07-12: THE_ORIGIN_POSTULATE.md on trunk);
  standing policy: the branch itself stays unmerged, a frozen seat record.
- `closure/phase0-hygiene` (+3): the same seat's earlier phase (lock tests for B477–B492,
  content banked via PRs #490–#500 per Review 4). Same frozen status.
- `audit/b739-negatives-hunt-p1` (+1): cc3's pre-renumbering negatives-hunt branch (the
  B737/B739 collision incident); the content is banked as B742 with the forensic trail
  preserved on main. Kept as the incident's frozen record.

**Live content — PROCESSED AND CLOSED (1):** `b666-addendum1` (+4, tip 1472c549,
last commit 2026-07-17 "cell1 in-flight snapshot"). Verified FULLY SUPERSEDED file-by-file:
main's B666 dir is a strict superset (main adds the later-sealed ADDENDUM 2, the
path-hygiene fixes from the committed-paths sweep, the completed cell1 logs + script
hashes, and the whole later campaign: cells 2–10/A2–C2/R/S/T/W31–35 + WAVE1–3 FINDINGS +
CAMPAIGN_SYNTHESIS); every differing file is main-newer. The branch's headline worry —
cell1's in-flight 2O/mod-8 computation vs the "open" L105 — dissolves: main's completed
cell1 ADJUDICATED L105 ("2O is a QUOTIENT, not the shadow", WAVE1_FINDINGS). Branch
deleted after this record (tip hash above = the recovery pin).

## The déjà-vu adjudication (the owner's question, answered honestly)

The feeling "we computed some of this before" was CORRECT about components and WRONG about
loss: QP-2 consumed the banked H¹ dimensions (B264, cited as its Method B); QP-4 built on
the banked non-canonicity (B711/B712); B756's DOOR3 derived its iff-law FROM the banked
B666 generating form; L105 was resolved by main's own cell1. The prior-art trail was
followed correctly in every case — because the priors were ON MAIN. The exposure was real
but structural: this seat reads main + gate-arrivals only, so an unmerged branch carrying
unbanked conclusions WOULD have been invisible. Hence:

## The standing rule (minted; the review checklist gains an item)

**Every decadal review runs the branch inventory** (`git branch -r --no-merged`, both
remotes) **and classifies every ref: stale (delete) / frozen-record (registry above) /
live (process before the review closes).** An unclassified unmerged branch is a review
blocker. Registered in REVIEW_TEMPLATE.md.
