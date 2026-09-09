# B1299 — THE PERIOD-2 DUALITY, VERIFIED, AND ITS ONE HOLE: DESIGN (pre-registered; sealed by sha256)

*MASTERPLAN v3.1 Phase 1, second harvest arc. Sources read in full before this file: sm:B1280 §1–§4 (Theorem 1 and its
numerical instantiation) and its L207 (@ 87a9004a), sm:B1281 §(a) refinement 1, main's B1267 (`deciding.py`), B71
(`peripheral.py`, the W1/W2 parametrisation), B1256 (the subregular labelling (2,2,2,0,2,2)), B1298 (the twelve exact signs).
Date 2026-09-08.*

## 1. The seat's claims (verbatim ≤ 25 words each) and what is verified here

- **sm:B1280 Theorem 1:** *"the elliptic SL(3) components W1, W2 are vector-like on every cusped cover (their cusp-fixed
  curve is the branch locus of the trace coordinates, where every representation is its own dual pulled back by the
  period-2 isometry)."* Mechanism: B71's identities `[A,B] = c μ³` (W1), `[A,B] μ³ = c` (W2) with **c = 1 exactly**, so
  `λ = μ^{±3}`; cusp-fixed vectors exist only on `K = {μ has an eigenvalue in μ₃}`; K is the branch locus of Lawton's
  trace coordinates; the other sheet is `ρ′ = (Aᵀ, Bᵀ) = τ*ρ*`, the dual pulled back by the period-2 τ; on K the two
  sheets coincide, so `V ≅ τ*V*` and `h¹(V) = h¹(V*)` on every cyclic cover; twists handled by 3 | n.
- **sm:B1281 refinement 1:** *"'W1 and W2 are rigid — h¹ = 0, no modes' is true at generic points and false on the
  curve K"* — a correction of main's B1267 to be applied at source.
- **sm:B1280's L207 (the hole):** at the SUBREGULAR sl₂ point (B1256's I-25 candidate) the θ-odd germ has *"exactly one
  unpaired direction, the V₁₀ of the 42 (θ′ = −1, ι* = +1)"* — the first place on the object where the θ-odd frame's
  net chirality is not forced to vanish by symmetry (bounded by B1268's |N| ≤ h⁰(∂M; 27)).

## 2. What is computed on this bench (rule 4: scripts run, then re-derived with main's code)

(a) The seat's `chirality_probe_w1w2.py` re-run in the pinned worktree (~22 min; receipt `sm_b1280_chirality_probe_w1w2_rerun.txt`).
(b) **c = 1 with main's own W1/W2:** B71's `peripheral.py` points (main's parametrisation, the same used by B1267)
pushed through `[A,B]μ^{∓3}` at ≥ 10 points per component; then the B1297/B1298 numeric engine on B71's fibred
presentation with its peripheral words: `(a₀, a₁, t₀, t₁, r₁, I)` at those generic points — B1267's "rigid" (a₁ = 0)
and `t₀ = 0 ⇒ I = 0` reproduced with independent code; and the transpose sheet's ninth trace `tr[Aᵀ,Bᵀ] = tr[B,A]`.
(c) **The hole located with B1298's exact signs:** the subregular labelling (2,2,2,0,2,2) on B1296's E₆ decomposes
`e₆` under its sl₂ by the h-eigenvalue multiset (expected V₂ V₄ V₆ V₈ V₁₀ V₁₀ V₁₄ V₁₆, tangent dim 8) and the 27
as 13 + 9 + 5 (B1256's row); the outer involution at that point has fixed algebra sp(8) whose principal-sl₂
decomposition is V₂ V₆ V₁₀ V₁₄ (C₄'s exponents 1,3,5,7 — cited, and checked by dimension: the complement is
V₄ V₈ V₁₀ V₁₆ = 42). With B1298's ι* signs `ε_S(k) = (−1)^{k/2+1}` on each `H¹(M; Sym^k)` (both V₁₀'s get +1), the
mismatch set θ′ ≠ ι* on the eight tangent directions is computed.

## 3. Pre-registered predictions

- **Q1:** c = 1 to ≤ 1e−9 at every W1/W2 point of main's parametrisation; `tr[Aᵀ,Bᵀ] = tr[B,A]` exactly (an identity);
  at generic points a₁ = 0, t₀ = 0, I = 0. PASS = all three; FAIL = any point with c ≠ 1 (then B71's identity, hence the
  theorem's step (a), fails on main's own points and the seat's script and main's disagree — the finding).
- **Q2:** the subregular decomposition is V₂ V₄ V₆ V₈ V₁₀² V₁₄ V₁₆ with the 27 = 13 + 9 + 5, and the mismatch set
  θ′ ≠ ι* is EXACTLY ONE direction, the V₁₀ of the 42. PASS = one mismatch there; FAIL = zero mismatches (then L207 is
  void and the subregular germ is vector-like by symmetry too) or more than one (then L207 is larger than the seat said).
- **Q3 (disposition):** if Q1 and Q2 pass, sm:B1280 Thm 1 is VERIFIED (the seat's proof adopted with the bench checks
  above; the K-locus solve is the seat's, re-run here, not re-implemented), B1267 gets a dated correction at source
  ("rigid off K; h¹ = 1 on K"), and L207 is mirrored on main as **L204** with the exact half already done (B1298's signs).

## 4. Not done here
No re-implementation of the seat's K-locus Newton solve in matrix space (its re-run is the receipt); no computation of
`N(27)` at the subregular point (that is L204's computation, priced: it needs the subregular E₆ local system's H¹ with
the 27 coefficients, ~a day); no new count.
