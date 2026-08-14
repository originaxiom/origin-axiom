# B882 — the tiling has a classical name: M(𝕆,ℂ), the magic square — and the novelty scoping that follows

cc banking seat, 2026-08-04. A five-angle prior-art workflow (10 agents, search + verify with
verbatim-quote discipline; structured findings preserved in `priorart_findings.json`), run the
moment the identification was suspected. Mathematics scope; nothing to `CLAIMS.md`.

## 1. CLASSICAL — cite, never claim

- **The decomposition is the Freudenthal–Vinberg magic square entry M(𝕆,ℂ)**:
  g = tri(𝕆) ⊕ tri(ℂ) ⊕ (𝕆⊗ℂ)₁ ⊕ (𝕆⊗ℂ)₂ ⊕ (𝕆⊗ℂ)₃ = so(8) ⊕ u(1)² ⊕ 3×16 = 78.
  Barton–Sudbery 2003 (Adv. Math. 180); **Landsberg–Manivel** math/0107032 — whose Vinberg-type
  form matches our tiling **verbatim** ("exactly the user's decomposition", per the verify
  agent); **Elduque 2007** (Rev. Mat. Iberoam. 23) gives the ℤ₂×ℤ₂-graded form with the bracket
  law **[ιᵢ(a⊗x), ιᵢ₊₁(b⊗y)] = ιᵢ₊₂((a∗b)⊗(x∗y))** — the published prototype of our cyclic law.
  Note for precision: the published law is ℤ/3-cyclic; the full S₃ statement rides on the
  triality automorphism and needs its own line.
- **tri(ℂ) = u(1)²** (dim 2). A secondary-source claim of "so(3)" was caught by the verify
  stage's own dimension arithmetic (28+3+48 ≠ 78) — recorded as the sweep's QC moment.
- **Even the fold is published**: Boyle 2006.16265 — fold one copy into so(10), and the other
  two copies together are "precisely the 16⊕16̄ of Spin(10)." Our clause (E) restated.
- **Triality ↔ three generations, as speculation, is old and live**: credited to **Ramond
  1977**; today Dubois-Violette–Todorov (J₃(𝕆) form), Boyle (magic square, "speculates SO(8)
  triality underlies exactly three generations" — his own framing), Boyle et al. 2409.17948
  (a different mechanism: Cartan factorizations in e₇/e₈), Furey (again different: ℂ⊗𝕆 acting
  on itself — not three sectors). None derives the frame; all postulate or speculate it.
- **The Galois-triality scaffolding is classical too**: trialitarian algebras over **cubic
  étale algebras** (Knus–Merkurjev–Rost–Tignol; Knus–Tignol "Triality and étale algebras" —
  triality acts on H¹(Γ, W(D₄)) permuting triples **cyclically**; Barry–Tignol 2023).

## 2. OURS — what no source in the sweep has

1. **The selection mechanism.** Prior art postulates the triality frame; the First Measurement
   Theorem **derives** it: the object's superselection torus stratifies e₆, and the
   enhancement structure of charge measurement *is* the magic-square frame — three
   Galois-conjugate first-breaking charges, one S₃ cubic, exact arithmetic (constant 13³,
   disc = 2³²·3¹⁰·5²·7³·11·13⁶). Nothing upstream of the algebra is assumed.
2. **The descent's two-sided verdict** (B876): within a breaking the matter is exactly ONE
   SM generation; the triple lives ACROSS breakings — sharper than the standing speculation
   and different from every mechanism found (Boyle-et-al's trio lives in e₇/e₈; Furey's in
   Cl(8); DVT's in J₃(𝕆)).
3. **The arithmetic question, now well-posed on classical ground**: our charge field
   K = ℚ[ρ]/μ is a non-cyclic cubic étale algebra — exactly the KMRT trialitarian setting.
   The conjecture "the arithmetic S₃ IS the geometric S₃" becomes: *the object's
   charge-measurement data defines a trialitarian structure over ℚ with underlying cubic
   étale algebra K*. A formalizable claim, queued.

## 3. Consequences

- **The paper strengthens**: cite Barton–Sudbery/Landsberg–Manivel/Elduque for the algebra and
  Ramond-through-Boyle for the physics lineage; claim the selection mechanism, the theorem
  packaging, and the descent. The tri(ℂ) identification also names our soft plane: **the
  chirality-switch charges span tri(ℂ)** — the two-chiralities crux (c-carried-into-θ) gains
  a concrete home: measuring the plane = choosing how ℂ sits in 𝕆⊗ℂ.
- **B880 (running)** supplies the module-level identification on our build (pairwise
  inequivalence of the sectors under so(8)); with it, the naming is computational, not only
  bibliographic.

## 4. Honest boundaries

- Two branching-table claims and the Barton–Sudbery §4.3 bracket page were NOT retrieved
  verbatim (paywall/decompression) — flagged UNCONFIRMED in the findings file; the Elduque and
  Landsberg–Manivel confirmations carry the identification regardless.
- One unattributed search snippet (an "E6^L×E6^R, three triality-related ways" paper, possibly
  arXiv 2508.10131) needs a proper read before the paper cites or contrasts it.
- No physics claim is made here; the lineage recital is bibliography, not endorsement.

`tests/test_b882_naming.py`
