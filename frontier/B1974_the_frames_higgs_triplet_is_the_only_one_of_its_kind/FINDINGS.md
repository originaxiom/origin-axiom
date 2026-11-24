# B1974 — The frame's Higgs triplet is the only one of its kind: both doublets must carry it (the shared mode is forced, given its weight, its representation, holomorphy and its growth at the cusp)

**Verdict: PROVED.**
- **The proof** is the elementary modular-form argument in § 2.
- **Its inputs are checked numerically on main's frame code:**
  - H1 and H3 at 30 to 40 digits;
  - F1 to F4 at 30 digits, F2 between heights 20 and 30.
- **The hypotheses** P1 to P3 are stated, and the theorem is conditional on them.

The idea and the identity are the agy lane's C13 (2026-11-21; harvest row 1993), credited here. C13's own argument
(Schur's lemma on M₂(Γ(2))) is corrected: η·c is not in M₂(Γ(2)) (H2), and the script asserted the uniqueness without
computing it. Main, 2026-11-24. Data-free. Identification I-37; register row P-847. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /weight 3/2|vector-valued modular|Halphen|Gamma_0\(2\)|shared fibre mode|shared mode|fibre triplet|D-1|one triplet/: 10 of 1714 arcs on main match (NEGATIVE 1, OPEN 2, PROVED 7); 2 register rows match`.
  - None proves a uniqueness.
  - B1970 enters I-37 with "both doublets carry one triplet".
  - B1971 uses it.
- **The seats:**
  - The web seat's W-D2 D-1 (harvest row 1984) types the shared mode as "a counted choice made after the look".
  - The agy lane's C13 claims Schur uniqueness of it. It was read at source by main, script included.
- **The literature (standard):**
  - Γ₀(2) has index 3, one elliptic point of order 2 at (1+i)/2, two cusps (∞ of width 1, 0 of width 2), and genus 0.
  - θ₂ and η have no zeros in H.
  - The valence formula; the Jacobi identity θ₃⁴ = θ₂⁴ + θ₄⁴.

## 1. The facts (`verification/c13_check.py`, `d1_facts.py`; frame C's Higgs coefficients c_k = te.ev(B[1][k]), B1940's frame)

| check | result |
|---|---|
| **H1:** C13's identity 24η³(c₀, c₁, −ic₂) = (−θ₂²(θ₃⁴+θ₄⁴), θ₄²(θ₂⁴+θ₃⁴), θ₃²(θ₂⁴−θ₄⁴)) | holds, worst relative residual 1e-40 over 5 τ |
| **H2:** whether η·c_k lies in M₂(Γ(2)) = span(θ₂⁴, θ₄⁴), as C13 states | **no**: least-squares residuals 0.13 to 0.21. Under T², η·c picks up e^{2πi/3} |
| **H3:** the transformation of c under T and S | c(τ+1) = R_T c(τ) and c(−1/τ) = τ^{3/2} e^{−3πi/4} R_S c(τ), with constant signed permutation matrices; residuals 5e-41 and 9e-33. **c is a vector-valued modular form of weight 3/2** for a monomial representation ρ |
| **F3:** the stabilizer of component 0 | R_T fixes component 0 (factor e^{iπ/4}), R_S exchanges 0 and 1, so T and ST²S fix 0: the stabilizer is Γ₀(2), of index 3 |
| **F2:** the cusp orders | \|c₀\| ~ \|q\|^{1/8}; \|c₁\|, \|c₂\| ~ \|q\|^{−1/8}, exact between heights 20 and 30 |
| **F1, F4:** the zeros of c₀ = −θ₂²(θ₃⁴+θ₄⁴)/(24η³) | E = θ₃⁴+θ₄⁴ vanishes at (1+i)/2 (to 5e-31). By the argument principle, c₀ has exactly one simple zero there, and none elsewhere in a box of Γ₀(2)'s domain |

## 2. The theorem and its proof

- **Hypotheses.** Let f = (f₀, f₁, f₂) be a second Higgs triplet that:
  - **(P1)** is a vector-valued modular form of weight 3/2 for the same representation ρ as the frame's S;
  - **(P2)** is holomorphic on H (B1970 and the web seat's W-H1: holomorphy, which excludes the conjugate reading);
  - **(P3)** is no more singular than S at the cusp: no q-exponent below −1/8.
- **Theorem.** Then f = λ·c for a constant λ.
- **Proof.**
  - Because ρ is monomial and Γ₀(2) is the stabilizer of component 0, f₀ and c₀ are forms of weight 3/2 on Γ₀(2) with
    the same character. So h = f₀/c₀ is a Γ₀(2)-invariant meromorphic function on H.
  - **In H,** c₀ vanishes only on the orbit of the elliptic point, where its zero is simple (F4). An invariant function's
    order at an elliptic point of order 2 is even, so h has no pole there.
  - **At ∞,** component 0's exponents are ≡ 1/8 mod 1 (F3: the factor e^{iπ/4}). P3 then forces f₀ to have order at
    least 1/8, which is c₀'s order (F2), so h is finite at ∞.
  - **At 0,** component 0 corresponds to component 1 at ∞, where c has the extreme order −1/8 that P3 allows, so h is
    finite at 0.
  - The valence formula checks the count of c₀'s zeros: 1/8 at ∞, −1/4 at 0 in the width-2 parameter, 1/2 at the
    elliptic point; the sum 3/8 = (3/2)·3/12.
  - So h is holomorphic on the compact genus-0 curve X₀(2), hence constant. The other components follow by ρ. ∎

## What it means

- **The shared fibre mode is forced, given P1 to P3:**
  - the web seat counted it as a choice;
  - B1970 states it as part of I-37;
  - B1971 uses it.
- **A second doublet** with the frame's Higgs's weight, representation, holomorphy and cusp growth can only be the same
  triplet. One counted choice leaves the menu. P1 to P3 are what remains of it: the second doublet is asked to be an
  object of the same kind as the first.
- **I-37 stays UNEARNED.**
  - Its clause "both doublets carry one triplet" is now derived given P1 to P3.
  - Still owed by its criterion: the triplet shown to be the 10's doublet pair within the dictionary, and a prediction.
- **C13's Schur argument** reaches the right conclusion by a step that does not hold as written. The uniqueness comes
  from Γ₀(2)'s genus and the cusp orders, not from Schur's lemma on M₂(Γ(2)).

## What is open

- *Dated note (2026-11-24, after landing).* **P1 in frame C holds by construction.**
  - Frame C's Higgs carries no line, so its triplet does not depend on the Higgs charge, and the two doublets of opposite
    hypercharge get the same triplet (B1970's wording).
  - In frame D1 the twist scales with q_H, so P1 fails there; B1962 found D1 deranged under every reading.
  - So "both doublets share one triplet" is the choice of frame C over D1, already counted as a frame choice. This arc
    adds only that frame C admits no alternative triplet of the same kind.
  - agy-002's WG96 (read at source) ties the holomorphic reading S to one chirality of the order-96 family group (W:T̄).
    That concerns the generations, not P1.
  - What I-37 still needs is that the frame's triplet is the 10's doublet pair. No seat has shown it.
- **Whether P1 can be derived:** why the second doublet's triplet should carry the same representation as the first.
  The 10's two doublets sit in one representation of the record's dictionary (B1253). Whether that forces one ρ is the
  next question.
- **The dimension for a looser P3** (a deeper pole at the cusp). It is larger, and then the mode is not forced.
