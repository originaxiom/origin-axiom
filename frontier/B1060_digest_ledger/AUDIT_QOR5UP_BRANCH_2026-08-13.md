# THE CLOUD BRANCH AUDIT — pre-digest repo audit at 8a4d70b4 (owner-directed, 2026-08-13)

**Method: isolated worktree of their head; every claim below re-run or re-read
on this bench, not taken from their reports. Slots marked ⏳ fill when the two
running certificates land.**

## §1 — Repo shape: COMPLETE

31 arcs B1024–B1054 (their 30 + the review arc). Every arc has FINDINGS.md and
arc_verdict.json; every arc but B1025 has an instrument (B1025 is the
suite-collection repair — no instrument by nature). No missing files, no
stubs, no half-built arcs. **The arcs are finished in the file-completeness
sense.**

## §2 — Their self-audit's central claims, independently reproduced

1. **Verdict uniformity (their finding 2): CONFIRMED, digit-for-digit.**
   All 31 verdicts read PROVED. The atlas status field discriminates exactly
   as they reported: {banked 18 · dead 9 · dormant 1 · open 2}. My coarser
   body-language scan: 22 of 30 bodies carry retraction/refutation/decline
   vocabulary (their stricter count: 18 + 2 non-findings — consistent,
   mine is a superset filter). **The routing failure between the two
   metadata fields is real. The digest must grade from BODIES, exactly as
   its lane-0 rule already says.**
2. **The 72 mechanical checks: 70 of 72 PASS on re-run here.** The two
   failures are the R1-2 finding's own checks, which encode THEIR clone's
   remote-tracking state (their signature: branch -r under-reports 1-of-3;
   mine: over-reports 6-of-3). **Caveat for the digest: two of the 72 are
   environment-bound, not corpus facts — "re-runnable with no arguments" is
   true; "re-runnable with identical results anywhere" is not, for those
   two.** The 70 corpus-fact checks all hold.
3. **The B946 species (their finding 0): CONFIRMED ON MAIN and repaired** —
   verified earlier today (the four keys compute via (6237|p) = (77|p),
   byte-identical); main's total exposure: 1 of 2 cache-shape instruments.
4. **Their freshness pin: REPRODUCES 26 of 28 here, and the two deviations
   are INSTRUMENT-ENVIRONMENT-BINDING, not corpus errors.** B1054's two =
   the known remote-state checks. **B1041 STALE-GREEN, dissected on this
   bench: 3 of its 10 checks are environment-bound** — (a) the B511 probe's
   finite-fractions differ by PLATFORM NUMERICS (their container loses
   finiteness by step 240; this bench keeps 1.0 throughout — the doubling
   branch's norm explosion lands differently per float handling), and
   (b) the B616 census reads 2/378 in the clean worktree — THE ORIGINAL
   LOCKED COUNT — so their "moved to 3/390" was a container-local
   measurement (untracked files in their working dir). **The irony is
   typed: their finding "the lock pinned a census count that moved" itself
   pinned a container-relative count; the E6 species one level up.** The
   arc's process findings (red-locks-behind-the-slow-suite; the mechanism)
   stand untouched; row 1.18's disposition: ACCEPTED-WEAK with the
   environment-bound rider on the instrument. General rule for the digest:
   **"certifies instruments, not caches" is container-relative wherever an
   instrument measures platform numerics or working-tree state** — the
   sweep itself is sound; 26 of 28 fully green here.
5. **Their suite pin (4006/0 at 6be907e): ⏳** — queued to run in the
   worktree after main's review certificate frees the cores.

## §3 — Load-bearing arcs, first REBUILT-grade results

- **qB1024 (row 1.01): ACCEPTED — REBUILT, the strongest possible form.**
  Their B1024 and main's B1024 are THE SAME SEALED CELL — identical prereg
  sha-256 (`dc823e86…`) — executed independently on both benches. Both
  landed SAME (d = 2). The generator classes differ by exactly a
  coordinate swap ((0,1) vs (1,0) for conjugation; their map reads the
  τ-fixed nodes as (α₂, α₄)) — a node-ordering convention, and precisely
  the cross-presentation datum B1065's C3 control consumes. **The fork
  accidentally twin-derived the entire cell.** Row 1.01's "SAME as main
  B1024?" answers: same seal, same verdict, frame-convention delta, typed.
- **qB1039: CORRECTED-carrying, and the correction applies to MAIN.**
  Their defect 1 — B141 item 3's "finite image ⟹ reducible tower" is FALSE
  as stated — **re-derived from scratch on this bench** (independent
  quaternion construction, Burnside span: Q₈ → 3-of-9 reducible;
  SL(2,3) → 9-of-9 IRREDUCIBLE; the true bound is max-irrep-dimension,
  sharp at n = 3). Main's B141 carries the false form in FINDINGS.md:39
  and README.md:13. **Repair queued: addendum-beside on main's B141**
  (conclusion survives; mechanism corrected; the counterexample is 2T
  itself, which is almost poetic). Main's core docs are clean (the only
  "finite image" hit is B959's unrelated rank statement).
- qB1034 (two-κ), qB1027/qB1028 (the κ = 2 chain), qB1040 ([exact]-tag),
  qB1050 (Fricke–Vogt normalisations): next in the REBUILT queue —
  main already consumed qB1034's export (the TERMINOLOGY two-κ row), so
  its verification is a consistency check of something already load-bearing.

## §4 — What this audit does NOT yet establish

The 30 arcs' mathematical content arc-by-arc (lane 1 proper: ~26 rows
remain after §3's first pass); their retraction's re-grade (row 4.8's
core); the 12 remaining action items' dispositions; their suite's
green re-confirmed here. **"The arcs are finished" is TRUE at the
file/instrument level (§1) and at the spot-checked content level (§3);
the full content grade is the digest's remaining work, now with its
foundation laid.**

## §5 — Consequence for the repo split

Two findings bear directly on distillation inputs and are now CONTAINED:
the claim-lines-overstate species (grade from bodies — the digest rule) and
the B141 mechanism defect (repair queued before any curated chapter cites
the tower split). The split's gate remains: the digest closes or the scoped
subset (chain-relevant rows + the 72 checks ✓ done + the retraction
re-grade) completes.
