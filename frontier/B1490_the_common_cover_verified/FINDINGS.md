# B1490 — THE COMMON COVER VERIFIED: the LP seat's covers of m004 with o10_150726 and m202 rebuilt and measured by main's own code — degree 20 and 24, chiral, no three, as the seat found; the figure-eight group contains Γ(4) — congruence at level 4 in the standard sense, B731's "level 8" being the record's other convention, both counts right; and the three is absent on one cover with hexagonal cusps because no isometry of order three survives, not because the ends do

**Verdict: PROVED** — C1, C2, C3 hold and agree with LP01's table in every number; **C4 fails** (reported as failed);
the level is settled by recount in both conventions (§3). Scope: frame F-CI (B1418's definitions); objects the common covers of
m004 with o10_150726 (degree 20 over m004, 4 over the target) and with m202 (24, 12); reach single for the covers,
general for the level. cc (main), 2026-10-07. Sealed `080189f89` (sha256 93b5777e) before any cover was built. Review
60's R60-3. The LP seat (the owner's, hired 2026-10-07) found the covers; main rebuilt them. No physical quantity.
**0 of 19.**

**Credit.** The LP seat for the congruence sentence, the coset construction and the covers (LP01, sealed before it
ran); its level-4 claim is right in the standard sense, and the record's "level 8" is right in its own (§3). Its exact representations are the inputs here,
checked on this bench.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /common cover|congruence|coset action|covers both/: 21 of 1362 arcs on main match (NEGATIVE 4, PROVED 16, RETRACTED 1)`
— B731 (RETRACTED, 2026-07-20: "m004 is congruence at level (8)"; index 6 at levels 2 and 4 in PSL(2, ℤ[ω]/n) proper) and the E21 guard (`tests/test_e21_group_naming_guard.py`: |PSL(2, ℤ[ω]/4)| = 960), B1418 (the three on
the two-cusped members; no cover of m004 inside the 112 attains three), B1291 (three excluded on one cusp), B1333 (the
index on several boundary tori); the rest harvests or other senses. **Literature:** Riley's representation and the index
12 are classical and were recomputed, not assumed.

## 1. Results (`cover_o10_150726.json`, `cover_m202.json`, `subgroup_h1.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **C1** | π₁(o10_150726) has an orbit of size 4 through K's coset; the cover has volume 20·vol(m004) = 4·vol(o10_150726), 6 cusps, H₁ = ℤ/4 ⊕ ℤ⁶ | 85% | **HOLDS**: orbit 4; volume ratios 20.000 and 4.000; 6 cusps; ℤ/4 ⊕ ℤ⁶; 40 tetrahedra |
| **C2** | 16 isometries, chiral, cusp counts |det(X − I)| ∈ {0, 4} only — no three | 80% | **HOLDS**: 16, none orientation-reversing, values {0: 24, 4: 24}, no three |
| **C3** | π₁(m202): orbit 12; the cover has volume 24·vol(m004), 6 cusps, ℤ⁸, 12 isometries, chiral, no three | 75% | **HOLDS** in every number (values {0: 12, 4: 12}) |
| **C4** | every cusp of both covers is rectangular | 65% | **FAILS**: m202's cover has six rectangular cusps (shapes 2√3·i, three; (2/√3)·i, three — as the seat said), but **o10_150726's cover has four hexagonal cusps** (shape ½ + i√3/2) and two rectangular (i√3) |

**The subgroup, independently.** The stabiliser of K's coset under the left action of π₁(target) — that is
π₁(target) ∩ K — has abelianisation ℤ/4 ⊕ ℤ⁶ (o10_150726) and ℤ⁸ (m202) by a Reidemeister–Schreier computation written
here, matching the covers.

## 2. What it says for the ends (the reading sealed in §5 of the preregistration, corrected by C4)

The reading was: in F-CI a three is three lines of an order-3 symmetry running between two hexagonal ends (B1291:
det(A − I) = 3 only for the order-3 rotation; parity puts the fixed lines between two cusps), so the three does not lift
because the symmetry does not. **C4 shows the halves come apart:** m202's cover keeps an order-3 isometry (|Sym| = 12,
ℤ/2 × ℤ/6) but its cusps are rectangular, so no cusp carries the rotation; o10_150726's cover keeps four hexagonal cusps
but its isometry group has order 16 — no element of order three. Either way the three needs **both** — an isometry of
order three and a hexagonal end it fixes, with a second such end for its lines — and neither common cover has both.
Chirality lifts (both covers are chiral); the three does not. For FK14: a state with several ends is not enough in
F-CI; the ends must carry an order-3 symmetry of the whole manifold. m003 has the hexagonal cusp and no order-3
isometry; the generated states have one end. The question of FK14 stands, sharpened: *what move of the grammar adds
an end with a symmetry of order three?*

## 3. The level: two conventions, both counts right

Recounted (`level_recount.json`; `controls.json`), with Riley's matrices, by closure: the figure-eight group's image
in SL(2, ℤ[ω]/4) has order 320, containing ±I and not the other two central elements ±(1 + 2ω)·I. So **in
SL(2, ℤ[ω]/4)/{±I}, of order 1920, the image has order 160 and index 12; in PSL(2, ℤ[ω]/4) proper, of order 960 (the
centre of SL(2, ℤ[ω]/4) has four elements), the image has order 160 and index 6.** At level 2 the index is 6 (10 of 60),
at level 8 it is 12 in both quotients.

Two definitions, two levels. The principal congruence subgroup Γ(4) ⊂ PSL(2, ℤ[ω]) is, standardly, the image of
{g ∈ SL(2, ℤ[ω]) : g ≡ I mod 4}; PSL(2, ℤ[ω])/Γ(4) ≅ SL(2, ℤ[ω]/4)/{±I}, and K contains Γ(4) because its index there
is its index in PSL(2, ℤ[ω]) — **K is congruence of level 4 in the standard sense, as LP01 says.** B731/B734 (July)
used the kernel of PSL(2, ℤ[ω]) → PSL(2, ℤ[ω]/n) instead, a larger kernel at n = 4 (it contains the preimages of
±(1 + 2ω)·I), which K does not contain; in that convention the index is 6 at level 4 and 12 at level 8 — "level (8)".
Both counts are right; the sealed text of this arc said B731's was wrong and is amended in place with a note (the
E21 guard caught the sealed text calling the order-1920 group PSL(2, ℤ[ω]/4); the amendment is recorded in the seal
ledger). A clarifying addendum lands on B731; **no retraction**, and the paper's count of the retractions index is
unchanged.

## 4. Disclosed

- **A convention error in the sealed code, caught by the independent check.** SnapPy's `cover(perms)` composes
  permutations in word order (a right action); the sealed code passed the left-action permutations and so built the
  *other* stabiliser (for o10_150726: 4 cusps, ℤ/2 ⊕ ℤ⁶, also 16 isometries, chiral, no three — `sealed_run/`). The
  Reidemeister–Schreier abelianisation of the intended subgroup (ℤ/4 ⊕ ℤ⁶) decided it; the code now passes the inverse
  permutations, the sealed output is kept, both covers re-run. For m202 both stabilisers have the same invariants, so
  the error was invisible there.
- **The sealed preregistration is amended in place** (two bracketed notes, 2026-10-07): it called SL(2, ℤ[ω]/4)/{±I} "PSL(2, ℤ[ω]/4)" — the record's E21 class, which its guard forbids — and said B731's level-4 count was wrong; the original is the seal commit `080189f89`, and the seal ledger records the amendment. Nothing in the predictions or their priors changed.
- Not blind: LP01's table was read before the seal. The seat's exact representations are inputs, checked (determinant
  one, relators ±I, trace squares against SnapPy's holonomy). The cusp-count instrument is rewritten here on B1418's
  definition; the door is not computed (the covers have 7–8 generators).
