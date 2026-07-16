# B649 stage 2b — TRACK S WAVE 3: the 27-lift over L (campaign a463c6aa)

**Foundation fact (verified pre-seal, this wave's scoping): B575's E₆
apparatus is RATIONAL — the cubic's 270 entries are ±1 and the
principal sl₂ (e_pr, f_pr, h_pr) has rational entries — so the silver
build runs over L = ℚ(s, i) alone (degree 8; no ℚ(√−3) compositum).**

## Conventions block

- Basis: B575's 27 weight basis, via the rational data dumped once to
  `e6_principal_rational.json` + `cubic_rational.json` (hashes in
  ARTIFACT_HASHES; the dump decouples the silver track from the
  100-second fig-8 prefix build).
- The lift: the Bruhat-decomposition formula (the b637 `lift_sl2`,
  ported verbatim to the L-class): lower = exp(r/p·f_pr), torus
  D = diag(t₂^{wgt/2}), upper = exp(q/p·e_pr); the p = 0 branch via
  the Weyl element. Inverse letters lifted from the 2×2 inverses
  directly (never a 27×27 inversion).
- L-class as stage 2a (s⁴ = 8s² + 16, basis {s^j i^k}); inversion by
  the 8×8 rational linear solve.
- Sample triples for G2: deterministic, seed 649, 25 triples of
  weight-basis unit vectors and small rational combinations.

## Gates

- **S2b-G1 (exact):** both silver relators (aBAbcc, aaCbcB) evaluate
  to I₂₇ EXACTLY in GL₂₇(L) on the lifted letters.
- **S2b-G2 (exact, sampled):** cubic preservation
  C(gx, gy, gz) = C(x, y, z) exactly for each lifted generator on the
  25 declared triples (the lift lands in E₆).
- **S2b-G3 (exact):** tr₂₇(μ-lift) = 27 = tr₂₇(λ-lift) (parabolic
  sources ⇒ unipotent 27-images; the −1 dies in even Sym powers).

Outcome: pass ⇒ the silver 27-letters exist exactly over L; stage 3
(the silver double: gluing solve, h¹, the Y-tensor — GATE B's blocker)
opens. Fail ⇒ the defect names the obstruction; GATE B keeps waiting.
