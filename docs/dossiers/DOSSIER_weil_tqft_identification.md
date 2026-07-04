# Specialist dossier — the full-level Weil-TQFT identification (NOT SENT; outreach dormant)

**The question.** Where does the level-15 THETA-TWISTED Weil representation (with its
Par-graded seam data) sit among known modular-data families (U(1)_k anyons, Weil/abelian
TQFTs, Deloup–Turaev-type invariants)?

**What is exact and banked (reproducers in-repo).**
1. The model: W_m = WR^m·D^m, D = diag ζ₁₅^{j(j−1)/2}, WR = F·D⁻¹·F⁻¹ (frontier/B367,
   step0_exact_matrices.py). The twist = the half-characteristic cocycle; the canonical
   model is seam-null (P62, frontier/B381).
2. The trace formula: tr(U_γXᵃZᵇ) = tr(U_γ)ζ₁₅^{½ω(v,(γ−I)⁻¹v) − ½ab − ½ω(v,(1,1))} —
   the twist is the half-characteristic term (P64, frontier/B382); |χ|² = #Fix(γ′).
3. The sector data: twist diagonal (e^{2πi·3/10}, e^{2πi·7/10}); the S-compression on the
   sector is TRIANGULAR (F(6,14) = 0 exactly) ⇒ NOT a 2-anyon block (frontier/B384,
   t3_block.json); g(15) = √−15 is the S-normalizer; tr(F|slot) = −(5/16φ)(3−√−3).
4. Dead ends already banked: tricritical-Ising dead at S (triangular) AND T (exponents
   {3/10, 7/10} ∉ TIM spectrum, frontier/B392); mechanical-240 refuted (P64).

**What a specialist is asked.** (i) Is the half-characteristic-twisted level-15 Weil datum
(items 1–2) a known object (metaplectic data à la Gelbart–Sally / theta-characteristic
TQFTs / spin refinements of abelian Chern–Simons)? (ii) Does any known family produce the
FULL 15-dim S/T pair with our Par-graded matrix elements (the ±1/48 table, P60)? (iii) Is
the triangular sector compression a known phenomenon (non-semisimple / logarithmic data)?

**Reproduce everything:** `pytest tests/test_b382_trace_formula.py tests/test_b384_kashaev.py`
(seconds; all exact).

**Citation anchor (sweep round 1):** Gelca–Uribe ("From classical theta functions to
TQFT") — abelian CS = Weil-rep theory; the closest published framework to this
construction. Our object extends it by (i) the half-characteristic twist (P62/P64) and
(ii) the Par-inserted PAIR channel (the seam) — neither present in their single-seed
setting. Kirillov Jr.–Ostrik (q-McKay) is the candidate technology for the CRT-phase
question. Niibo–Ueki (idelic CFT / Hilbert reciprocity on 3-manifolds): registered
reading — is the genus-character gating a special case?
