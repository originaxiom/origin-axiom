# B731 — ADDENDUM (2026-10-07, B1490): the congruence level of the figure-eight group is 4 in the standard sense and 8 in this record's convention — two definitions, both counts right

**What B731/B734 say.** The index of π₁(m004)'s image in PSL(2, ℤ[ω]/n) is 6 at n = 2 and n = 4 and 12 at n = 8, so
m004 "is a congruence subgroup, at level (8)" — the index being taken in PSL(2, ℤ[ω]/n) proper, whose order at n = 4 is
960 (the centre of SL(2, ℤ[ω]/4) has four elements: ±I, ±(1 + 2ω)I; the record's E21 guard).

**What B1490 recounted** (Riley's matrices; `frontier/B1490_the_common_cover_verified/verification/level_recount.py`,
`controls.json`): at n = 4 the image in SL(2, ℤ[ω]/4) has order 320, containing ±I and not ±(1 + 2ω)I; so in
SL(2, ℤ[ω]/4)/{±I} (order 1920) the index is **12**, and in PSL(2, ℤ[ω]/4) (order 960) it is **6** — B731's number.

**The two definitions.** The principal congruence subgroup Γ(4) ⊂ PSL(2, ℤ[ω]) is, standardly, the image of the
kernel of SL(2, ℤ[ω]) → SL(2, ℤ[ω]/4); then PSL(2, ℤ[ω])/Γ(4) ≅ SL(2, ℤ[ω]/4)/{±I}, and K contains Γ(4) exactly because
its index there, 12, is its index in PSL(2, ℤ[ω]). **So K is a congruence subgroup of level 4 in the standard sense**
(the LP seat's LP01, 2026-10-06; used to read common covers off the twelve cosets). B731/B734's kernel is that of
PSL(2, ℤ[ω]) → PSL(2, ℤ[ω]/n), larger at n = 4; K does not contain it, and in that convention the level is 8. Neither
count is wrong. The record keeps both, named: "level 4 (Γ(4), the image of the SL kernel)" and "level 8 (the kernel of
the PSL reduction, B734)". B731's headline — the group is congruence — stands in both.
