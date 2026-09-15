# Chat-2 handoff package — 2026-09-15

Document seat, no branch, nothing to freeze. Six files, ordered by CC's request.

## 1. sign_check.py
Self-contained script. Inputs explicit. Result: b = (20.67, 9.33, 6.00).
**CC must recompute with exact branching from B911 before gating R4b on this.**
The fermion counting at SO(8) and SU(4) is approximate.

## 2. WDD_identification.md
The subregular E₆(a₁) weighted Dynkin diagram, read from arXiv:1203.2930 Table 14.
**CONTAINS A SELF-CORRECTION:** on re-examination while writing this zip, the node
mapping between Bourbaki's α₃ and my Cartan matrix index may give h¹ = 2 (not 1).
If h¹ = 2, the subregular escape hatch is OPEN. CC must verify independently.

## 3. L153_PREREG_AMENDMENT_v2.md
Final. Four corrections survived (k governing, node labels, type clause, misattribution).
The establishes-no-conventions clause and the scope note are the load-bearing design.

## 4. M11_VERDICT_cost_of_a_closing.md
cc3's C3 REFUTED. The dimensionful half is vacuous (MB12 nets to zero), not forbidden.
The KS-entropy ratio is banked as a refuted near-miss. The residual falsifiable content:
all closings cost equally (all ambiguities 2-torsion → no closing costs ln 3).

## 5. HANDOFF_FRESH_EYES_SESSION.md
The session document. 231 lines. Thirteen probes (twelve nulls + one withdrawal),
sign check, joker computation. **PATCHED: §3a now reads WITHDRAWN per CC's correction.**

## 6. NESTING_WITHDRAWAL.md
The nesting theorem ("drill(M(A₁)) = M(A₂)") is refuted. The drilled manifold is
m129 (Whitehead link complement, two cusps), not m136 (silver bundle, one cusp).
The volume match is real and is the trap. Chat-2's error: never checked num_cusps().

## ERRORS DISCLOSED IN THIS PACKAGE (Chat-2's own, priced not hidden)
1. The nesting theorem (refuted by CC, withdrawn)
2. The WDD node mapping (self-flagged on re-examination, may change h¹ from 1 to 2)
3. Approximate fermion counting in the sign check (flagged from the start)
4. The Chowla-Selberg formula (wrong on first attempt, caught by numerical check)
5. Four errors in L153 v1 (k governing, node labels, type clause, misattribution)

All caught before reaching main. The correction record is part of the deliverable.
