# B1754 — GENESIS v1.58: THE LADDER'S RULE IN THE THREE SEATS' MERGED WORDING, AND THE AUDIT LANE'S QUALIFIER TO THE WEAVE'S BREAKING RULE (THE OWNER'S RULING ON P-385)

**Verdict: PROVED (a refinement of the foundation's wording at the owner's ruling; no status cell and no computation
changes).** cc (main), 2026-10-24. 0 of 19.

## 1. The ruling

The owner, 2026-10-24: "i acfept your recomendatipn on P-385". Main had recommended adopting both wordings the SM seat put
to the owner (its relay §271, harvest row 1389), each sharpening without widening.

## 2. What changed

- **The ladder (GENESIS F-MC, v1.58; `docs/THE_WEAVE.md`; WORKING_RULES).** The rungs are the moves' quotients by T^N,
  Γ/⟨⟨T^N⟩⟩ = Δ(2, 3, N), finite exactly for N = 2, 3, 4, 5, the end at 5 forced by the moves' orders 2 and 3 (W153).
  "Every finite rung" means these quotients, not every finite quotient of the moves: PSL(2, 𝔽₇), order 168 with T of
  order 7, is a quotient of the infinite Δ(2, 3, 7). The container, the least single simple algebra holding every rung's
  finite diagram, E₈, is a composition requirement adopted by ruling, not derived; the prime 5 enters with it. Main's
  second clause stays: the rule fixes the algebra, not its embedding or its fields. R2 is recorded with its hypothesis:
  invariance under every move selects a unimodular lattice only for one scalar holomorphic theta series, since for any
  even lattice of rank r, (Im τ)^{r/2} Σ∣Θ_μ∣² is invariant under every move.
- **THE WEAVE's breaking rule (`docs/THE_WEAVE.md`; WORKING_RULES).** Added: "Choosing a representative is a convention
  only when the declared equivalence preserves the full relational observables, including the reference/measuring
  sector." Under it the observer re-typing's sort stands (B1750): each convention named there acts on the whole relational
  description. A relative sign, J against another CP-odd quantity, stays physical.

## 3. What was not adopted

- The audit lane's proposal (its relay `PHYSICAL_TO_SM_MAIN_CHAT1_2026-10-24_THE_WEAVE_AND_THE_LADDER.md`, a9053eab7)
  carried a second sentence that the SM seat's relay did not quote and P-385 did not put to the owner: "Symmetry-related
  physical vacua remain allowed distinct states; the theory must specify their dynamics or statistical treatment where
  predictions depend on that distinction." It is recorded in `docs/THE_WEAVE.md` as the lane's gloss, not adopted text.
- The lane's ask to state E7's uniqueness for W135's specified conjugation action is noted on P-385 for W153's L4.

## 4. The facts behind the wording

The SM seat checked the web seat's and the audit lane's facts post hoc on its own code (its commit 4760bf686:
`the_ladder_web_seat_check.py`, `the_ladder_audit_lane_check.py`, outputs kept): the rungs' groups form no chain; the
finite diagrams nest (D₅ in E₆ twice, the others once) and the affine McKay graphs do not; Z_L for A₁ is invariant
under S to 2 × 10⁻³¹. Main relies on these as the seat's checked statements of classical facts (the (2, 3, N) triangle
groups, McKay, theta series of even lattices); no status cell rests on them.

## Seen first

`VERDICT topic-sweep /ladder.s rule|container|scalar theta|relational observables/ (full text)`: B1751, B1752 (PROVED).
The register: P-375, P-379, P-385. **Literature:** classical (the (2, 3, N) triangle groups; theta series of even
lattices, arXiv:2407.01205 as the audit lane cites it).

## Files

- `received/GENESIS_v1_57_main.md` (hash-pinned); `adoption/amend.py` (`--check`). The lock:
  `tests/test_b1754_genesis_v1_58.py`.
