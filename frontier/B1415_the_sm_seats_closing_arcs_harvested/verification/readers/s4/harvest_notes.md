# s4 — the seat's two harvest-response commits, checked against main's own FINDINGS.md

Worktree: `<home>/origin-axiom/audit/wt-sm` @ f17dd84e. Main tree: `<home>/origin-axiom` (main branch).
Compared against `frontier/B1413_the_audit_lanes_r21_r31/FINDINGS.md` and
`frontier/B1414_the_outside_benchs_memos_185_233_harvested/FINDINGS.md` on main.

## Commit b661deae — "Harvest received from main (B1413)"

Main's B1413 (§"Two of main's own arcs are narrowed by this window") states exactly two things owed to the SM seat, plus
a documentary note on the audit lane's R15–R22 relay:
1. **B1355's "A-type only" claim is too broad** — the finite centraliser of 2T only obstructs the *explicit substitution*
   Γ → 2T in AW's eqs. (2.4)–(2.7); AW §2.3's general Kronheimer construction (any G ⊂ Ĝ with ĝ = g ⊕ u(1) ⊕ r ⊕ r̄) reaches
   E₆ ⊂ E₇ too, with one chiral 27 of charge 1 by their heterotic computation, topology undescribed.
2. **B1351 §2(ii)'s "H*(T²;L)=0 ⇒ N=0 whatever the Morse partition" is too broad** — R23 §4 exhibits an explicit disc-partition
   counterexample (H* = (0,k,0,0), χ = −k) even with the whole torus acyclic; the implication holds only for whole-torus and
   annular ∂⁺M conventions (rows A–C of chat1's I-26 table), not disc conventions (rows D–F).
3. Wording correction to the R15–R22 relay row (the seat's own file had written "a source curves the connection"; the audit
   lane's actual construction keeps F_A = 0, [A,φ] = 0 on the smooth complement — the source is a declared input on a
   lower-dimensional locus, not a curvature of the connection).

**Item 1 — RIGHT.** Verified against `<seat>/frontier/B1355_the_e7_point_made_explicit/FINDINGS.md` diff in b661deae: §0, §1, §4 and
the claim line were corrected in place, each edit is a scoping (not a retraction) matching main's language almost verbatim
("obstructs that restricted substitution, not AW's family as a whole"; "their §2.3 ... builds the cone for any pair G ⊂ Ĝ
... names E₆ ⊂ E₇ for the 27 explicitly, with a single chiral multiplet of charge 1 by the heterotic computation and 'a
useful way to describe the topology of X … not clear'" — this is main's own wording, correctly attributed and quoted). The
seat also propagated the correction downstream: `docs/THE_SM_VERDICT.md`, `<seat>/docs/THE_CLOSING_2026-09-15.md` (§0, §1 ledger
row added: "AW's E₇ Kronheimer unfolding as the apex ... CITED (AW §2.3; correction of record, main B1413)"), §3, §6.2 (the
doublet-parity note rescoped to "twistor model only"). No overclaim introduced; the seat kept "topology not described" as a
live gap at the time of this commit (later closed by its own B1360, checked in `closing.md`).

**Item 2 — RIGHT.** Verified against `<seat>/frontier/B1351_the_index_on_a_three_manifold/FINDINGS.md`: the added note reads "§2(ii)'s
implication ... holds for the whole-torus and annular conventions of ∂⁺M (rows A–C of the I-26 table) and fails for the disc
conventions (rows D–F): on explicit relative cochains a disc partition per source arc gives H* = (0,k,0,0) and χ = −k even
with the whole torus acyclic." This matches main's B1413 statement exactly, and the seat correctly notes the scoped claim
does not affect B1352's computed partitions ("annular... a direct computation") or B1356–B1359 ("do not use (ii)") — i.e.
it identified precisely which downstream arcs were and were not exposed, rather than blanket-flagging everything upstream.

**Item 3 (wording) — RIGHT.** Verified in `docs/RELAY_LEDGER.md` diff: the seat replaced "a source curves the connection"
with main's own corrected phrasing ("their construction keeps F_A = 0 and [A, φ] = 0 on the smooth source complement, the
source being a declared input on a lower-dimensional locus, not a curvature of the connection (wording corrected 2026-09-15
at the audit lane's request via main's B1413...)"), explicitly flagging it as "this seat's misdescription." Honest self-
correction, not buried.

**Nothing missed.** Main's B1413 names exactly these two corrections plus the wording note as "owed to the seat"; the
commit's own message lists three items and all three are present and each is a faithful, non-overclaiming, non-underclaiming
application. No partial items found.

## Commit f17dd84e — "Harvest of main's B1414 by citation"

Main's B1414 harvested the outside bench's memos 185–233; its item 8 (of the table in §1) concerns the SM seat directly:
*"B1355's escape clause forced (the ℤ/3 is 2T/Q₈), memo 233 v2 only; v1 vacuous (bench error #36)"* — graded REPRODUCED, with
main noting "(B1355 is the SM seat's arc, harvested B1411)" and, at the end of §4, explicitly: *"this is not progress toward
chirality... B1355 lives on the SM seat's branch and is harvested in B1411, which this arc points to."* Main's own §4 does
not ask anything new of the seat — it independently re-derives the same fact (H₁(Y₃) = ℤ/4 ⊕ ℤ/4 by Smith form, the deck
acting as a 3-cycle on the three non-zero classes of H₁/2H₁ = (ℤ/2)², hence "b₂ ≥ 2 with the ℤ/3 moving the harmonic forms"
is necessary for any closing realizing item 1) and states it agrees with B1356 §2 / B1357.

**The seat's response — RIGHT, and appropriately minimal.** The commit touches only `docs/RELAY_LEDGER.md` (a new row),
`docs/SM_SEAT_ALIAS_TABLE.md` (a currency note), `docs/views/REVIEWER.md` (auto-regenerated word count), and
`<seat>/frontier/B1356_the_three_on_y3/FINDINGS.md` (a "Currency 2026-09-16" note citing B1414 §4). Checked the added FINDINGS.md
note against main's actual B1414 §4 text: the seat's summary — "Q₈ ◁ 2T of index 3 with w=(1+i+j+k)/2 cycling i→j→k,
Δ = t²−3t+1, H₁(Y₃) = ℤ/4⊕ℤ/4 by Smith form, the deck a 3-cycle on the three non-zero classes of H₁/2H₁" — reproduces
main's computation line for line (main: "conjugation by w sends i → j → k → i"; "Smith form [1,4,4] ⟹ ℤ/4 ⊕ ℤ/4"; "the deck
... permutes its three non-zero classes in a 3-cycle"). The seat correctly declines to spend a new arc number or claim
anything beyond agreement ("nothing owed to this seat"), which matches main's own framing exactly — main did not ask
for anything back, it only pointed at B1356/B1357 as independently-derived agreement. No overclaim (the seat does not, e.g.,
claim B1414 "proves" or "verifies" B1356 — it says "agrees with," "independently derived," matching main's own phrasing
"the two benches agree, independently derived").

## Summary verdict

Both harvest-response commits are **right** in full: every correction main names is applied, scoped exactly as main scoped
it, propagated to the correct downstream files (and not over-propagated to files main did not flag), and no new overclaim
is introduced in the process. The one place where a claim was left temporarily open by b661deae (B1355's Kronheimer-model
topology, "not clear" per AW) was subsequently closed by the seat's own further work (B1360) rather than by a later harvest —
this is visible in the current HEAD's THE_CLOSING text (§6.2's "b₂(link) = 1 with ∫_U w ≠ 0 is now established (B1360)")
and is the seat's own computation, not something owed by main.
