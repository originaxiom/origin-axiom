# B193 — the SL(3) sealing / field-content scouts: chirality ⊥ field; fusion is quantum

**Date:** 2026-06-23. **Status:** Masterplan III, **Track G** (the SL(3) scouts; closes the track). Two clean
scouts computed (L8, L10) + one honestly scoped to NEEDS-SPECIALIST (L5/L6, per the B192 lesson). **Firewall-side:**
emergent quantum-topology / character-variety math (`K010`); no scale/Λ; **nothing to `../../CLAIMS.md`**; P1–P16
frozen. Ledger V188. Reproducer `sealing_scouts.py` (`ALL CHECKS PASS`).

## Results

- **L8 — chirality and the eigenvalue field are INDEPENDENT.** For block words `W = R^{m₁}L^{m₁}…R^{m_k}L^{m_k}`,
  the bundle is amphichiral iff the block-length sequence is a **cyclic palindrome** (B128/B134), while the
  **SU(2)_k eigenvalue field** is the quantum mod-4 spin-content (B132). **All four (chirality, field) combinations
  occur** in a small sample:

  | seq | chirality | SU(2)₄ field |
  |---|---|---|
  | (1,) | amphi | Q(√−3) |
  | (2,) | amphi | Q(ζ₁₂) |
  | (1,2,3) | chiral | Q(ζ₁₂) |
  | (1,2,3,4) | chiral | Q(√−3) |

  At fixed chirality the field varies (amphi → both Q(√−3) and Q(ζ₁₂)); at fixed field the chirality varies
  (Q(√−3) → both amphi and chiral). So the field is **not** determined by chirality — it is the quantum spin-content
  (extends B133 across composition).
- **L10 — field-fusion is a QUANTUM phenomenon; classical trace-fields stay disjoint.** The SU(2)_k eigenvalue field
  reaches the **compositum** `Q(ζ₁₂) = Q(√−3, i)` (a single silver block `m=2` already does) — a quantum (SU(2)_k)
  effect. But the **classical** metallic seed trace-fields are **disjoint**: golden `Q(√−3)` and silver `Q(i)` are
  two distinct quadratic subfields of the quartic `Q(ζ₁₂)`, so `Q(√−3) ∩ Q(i) = Q` (exact, verified by the degrees
  2,2,4). So the "fusion" is quantum, not a classical trace-field phenomenon; whether classical *composites* fuse is
  SnapPy-gated (a scout, expected negative per K016).
- **L5/L6 — non-metallic SL(3) sealing: SCOPED NEEDS-SPECIALIST.** S031 sealing (the trace map fixes only the
  `Sym^{n−1}` image) is verified for metallic words at SL(3) (B129 m=1, B137 m=2); the SL(2) case is near-tautological
  (`Sym¹=id`). The genuine question — does sealing hold for **general non-metallic** once-punctured-torus words at
  SL(3)? — is the B137 off-sublocus scipy search, which needs the word's trace field (SnapPy-gated) and is exactly
  the intricate-numerics regime the **B192 refutation** warns about. Flagged **NEEDS-SPECIALIST** / careful dedicated
  work, deliberately **not rushed** here.

## What this means

The field/chirality scouts settle two clean facts: **chirality and the SU(2)_k field are orthogonal** (L8 — you can
vary either independently), and **the field-fusion to `Q(ζ₁₂)` is genuinely quantum** while the classical metallic
trace-fields remain disjoint (L10). Both reinforce K015/K016's "field content is quantum-group arithmetic, not
chirality." The deeper sealing generality (non-metallic words at SL(3)/SL(4)) stays the genuine open scout — and,
post-B192, it is *correctly* left as careful-dedicated/specialist work rather than a rushed intricate search.

## Scope / honesty
- L8/L10 reuse the validated B132 (SU(2)_k rep) and B134 (chirality palindrome) machinery, copied self-contained;
  the classical disjointness is exact field algebra (sympy degrees).
- L5/L6 deliberately **not** run as an intricate SL(3) search — the B192 lesson (cherry-picking / mismatched-control
  traps in deep context) makes that NEEDS-SPECIALIST-grade work; the metallic + SL(2) baselines stand.
- Emergent quantum-topology / character-variety mathematics (`K010` boundary); nothing to `../../CLAIMS.md`.

## Anchors
`B132_quantum_layer` (the SU(2)_k field / mod-4 spin-content), `B134_chirality_recursion_proved` (the cyclic-palindrome
amphichirality), `B128` (chirality recursion), `B133`/`K015`/`K016` (field = quantum-group arithmetic, not chirality;
classical fields disjoint), `B129`/`B137` (metallic SL(3) sealing), `S031` (the sealing capstone), `docs/OPEN_LEADS.md`
L5/L6/L8/L10. External: SU(2)_k / Reshetikhin–Turaev modular data; amphichirality of fibered bundles (GHH 2008);
cyclotomic field arithmetic.

## Reproduction
`python frontier/B193_sealing_field_scouts/sealing_scouts.py` — L8 the chirality×field cross-table (independent);
L10 the quantum-fusion-vs-classical-disjoint contrast; L5/L6 the scoped sealing note. Prints `ALL CHECKS PASS`.
Fast locks in `tests/test_b193_sealing_field_scouts.py` (2 tests, ~0.5s).
