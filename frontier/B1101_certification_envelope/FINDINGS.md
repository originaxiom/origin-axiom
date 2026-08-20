# B1101 — THE CERTIFICATION ENVELOPE (governance adoption; Review 47's methodology delta, owner-elected 2026-08-20)

**Date:** 2026-08-20 · **Verdict: PROVED (an adoption record; the rule's evidence is the window's three instances, each caught by the existing gate layer)**

## The rule (now in WORKING_RULES)

**During any certifying suite run, the working tree is read-only by convention:**
1. All landings stage in the scratchpad and land by explicit filename at bank time
   (never a glob; never a new arc dir mid-suite — the corpus head is computed from
   disk).
2. Pre-commit gate checks run on the STAGED state (`git add` first; the attribution
   gate scans tracked files).
3. Every ledger digest enters by command substitution (pipe, never retype) — with the
   `seal-digests` gate as the read-time backstop over every route.
4. On collision (tree moved mid-suite): fold-forward — bank the pending cells plus the
   head's currency reads in ONE commit, one suite; never re-run the stale certificate.

## The evidence (why this arrives pre-proven)

Three instances in one review window, one species (E46), all caught by E39's
exact-tree gate — the gate went three-for-three while the procedures failed under
load: the scratchpad-glob sweep (200+ files toward a public push; attribution gate),
mid-suite doc edits re-staling currency counters, an uncommitted arc dir shifting the
corpus head. Plus the digest routes (E47 write-time, E48 remap-time) closed by the
same envelope's line 3 + the recompute gate. Filed classes: E45–E48; practices:
PRACTICES.md's three lines, now consolidated here at the owner's election (Review 47,
optional methodology delta → GOVERNANCE §10 separate-arc procedure → this arc).

**Locks:** the stale-absence/practices surfaces carry the lines; the seal-digests gate
is live (16/16 on adoption day); this record is the citation target.
