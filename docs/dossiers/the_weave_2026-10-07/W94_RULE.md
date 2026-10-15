# W94 — the rule, recorded before the code

The SM-derivation seat, 2026-10-15. Committed before the code that reads it exists. Nothing here is a result.

## Why this arc

- **W93's read-out.** B1658's bound refutes one Higgs only through the up sector. If the up quarks' Higgs is not the
  one the down quarks and leptons share, the bound allows down/leptons (3.13, inside 4).
- **Then main's planned test is live again for that pair.** Main planned it for P-163 and set it aside because the bound
  made it moot for three sectors (B1658's notes, before the seal):
  - at ω the order-3 move fixes the identity channel and permutes i, j and k;
  - so its null symmetric Higgs quaternions are R(ω) and R̄(ω) in the (i, j, k) part, with s₀ = 0, and they carry no
    free parameter;
  - then the sectors' k_s on W59's lines are definite numbers.
- **The relation tested.** Under equal framed data (P4′), to first order in the Higgs's defect,
  m₂/m₃ = k_s·∣d_S∣ with k_s = 2∥S∥²∥M_s∥²/∥Y(S, M_s)∥² (B1658).
  - One Higgs shared by down quarks and leptons gives (m_μ/m_τ)/(m_s/m_b) = k_lep/k_down.
  - That is a relation with no free size. The data give 3.14 (HZ2021 at M_Z; seen).
- **The record's pattern:** every relation without a free size tested so far was refuted (W88). This is one more, and
  the most direct one available.

## Weave or thread?

- **A fibre-frame result at one τ (ω), on W59's eighteen lines: a frozen piece.** It is not a weave result.

## The objects (fixed here)

- **B1656's frame as W93 implemented it:** the quaternion units, the dual basis, M_s = Σ R_s E^s and
  Y(S, M) = ⟨C_aᵀ ε S C_b, M⟩. The residues come from analytic theta sums at 40 digits, at τ = ω.
- **The order-3 move** is γ: τ ↦ −1/(τ + 1), which fixes ω. Its action on the (i, j, k) channels is the matrix G with
  T(γτ)/(τ + 1) = G T(τ), where T = (c_i θ₂², c_j θ₄², c_k θ₃²). G is fitted at four points, as B1657 fits it.
- **The symmetric null Higgs.** S₀ = T_i(ω) QI + T_j(ω) QJ + T_k(ω) QK, null since T·T = 0 (Jacobi). Its partner
  S̄₀ is built the same way from G's eigenvector for the other non-real eigenvalue: B1657's R̄ in this basis.
  - *Pre-run correction (2026-10-15, before any code; the first commit of this rule, 2aaf5d271, said "built from
    the complex conjugate triplet"):* B1657's order-3 matrix is real only after its diagonal conjugation
    diag(−1, i, −1). In B1656's channel basis G has non-real entries, so the plain conjugate of T(ω) need not be an
    eigenvector. L1 checks that S̄₀ is null.
- **The sectors** are the dictionary's down (Q, d) and leptons (L, e). They share one S, as in B1656's coupling, with
  their twists in M_s. The up sector is computed for the record only.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **L1, the symmetric Higgs** | G³ = −1 (up to 10⁻¹²); T(ω) is an eigenvector of G with eigenvalue 1/(ω + 1) = e^{−iπ/3} to 10⁻²⁰; G's other non-real eigenvalue is e^{+iπ/3}, and its eigenvector is isotropic; det S₀ = det S̄₀ = 0 to 10⁻²⁵ | 90% |
| **L2, the coefficients** | on each of the 18 lines and for S₀ and S̄₀, k_s = 2∥S₀∥²∥M_s∥²/∥Y(S₀, M_s)∥² lies in [½, 2] for down and leptons (and up, for the record); the first-order law holds: for S = S₀ + 10⁻⁶·X with a random X, (m₂/m₃)/(k_s∣d_S∣) = 1 to 10⁻⁴ | 95% |
| **L3, the relation against the data** | the predicted k_lep/k_down on every line and Higgs misses the data's (m_μ/m_τ)/(m_s/m_b) = 3.14: z = ∣ln(pred/data)∣/√(r_data² + a²) > 2, with a = 0.10 (W88's allowance) and r_data the data's relative error | 85% |

**The read-outs (no prior).**
- The predicted k_lep/k_down, k_up/k_down and k_up/k_lep on every line class.
- How many (line, Higgs) cases lie within 2σ and 3σ of the data.

## What the outcomes would mean

- **L3 as predicted (every case misses):** the symmetric Higgs fails the down/lepton relation in this frame. One more
  relation without a free size is refuted.
- **L3 fails (some case within 2σ):** a parameter-free relation between m_μ/m_τ and m_s/m_b would pass in this frame.
  That would be a candidate for main to seal blind on the other line classes and for chat1's thread frame. It would not
  be a derivation by itself, since P4′, first order, the up sector's own Higgs and the choice of lines are stated
  inputs.

## After the run

- Record in the weave dossier's NOTE (section W94, the table) and the state page.
- Send a relay to main.
- Update CHANGELOG and PROGRESS_LOG.
- Add a test that reads the JSON.

0 of 19.
