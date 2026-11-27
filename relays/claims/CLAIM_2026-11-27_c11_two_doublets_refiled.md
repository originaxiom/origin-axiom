# CLAIM CARD — the two-doublet dictionary fixes neither C11's K nor B1674's k_u + k_d; I-31 stays priced, per frame

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 3372dd041787d8e874121937af041a1747bb9afa
- kind: computation
- touches: P-290 (the completion map's C11), I-31, I-37
- effect: conditions — I-31: priced per frame, neither earned nor excluded by the dictionary (P-290). In F_all, the
  Dedekind counterterm with k_u + k_d ≡ 2 (mod 4) if the moves are exact; in F_c, the same, and the gauged centre μ₄
  is anomaly-free for I-31; in F_S, I-31 is excluded by SU(3)_F³ (A = 16) unless fermions are added
- scope: frame: the record's three flat-bundle frames F_all, F_c and F_S (W44), with frame C's triplet for the Higgs;
  object: B1674's characters on the 64 dictionaries, restricted to each frame's K, and the gauge realisability of K;
  reach: class; hypotheses: B1253's 27 with B1252's hypercharge (B1970's H1); frame C's Higgs triplet (B1974; P1 by
  construction); the ρ-parts only, with weight factors left out (B1674's H-W leaves the matter's weights unfixed);
  the discrete anomaly criterion at the level of the character; tree level
- identifications: I-31 (the assignment tested, all s_f = +1); I-37 (the Higgs as the 10's doublet pair, used as
  B1970 states it); K_F here is W44's frame datum, K_W here is B1674's K
- definitions: s_f = +1 when the left-handed field f ∈ {Q, u^c, d^c, L, e^c, ν^c} carries T (ρ_T = χ_η²¹ ⊗ ρ_u, ρ_u
  the θ² triplet's representation: t ↦ [[i,0,0],[0,0,1],[0,1,0]], s ↦ [[0,0,−i],[0,−i,0],[−i,0,0]], with χ_η(t) =
  e^{2πi/24}, χ_η(s) = e^{−iπ/4}), −1 for T̄; n_G = 9 Σ_f w_G(f) s_f mod 24 with w: SU(3) Q 2, u^c 1, d^c 1; SU(2) Q 3,
  L 1; gravity Q 6, u^c 3, d^c 3, L 2, e^c 1, ν^c 1; m = −9(2s_Q + s_u + s_d) mod 24 and K_W = k_u + k_d with
  Dedekind cancellation iff 6K_W ≡ m (mod 24); ρ_H(t) = R_T, ρ_H(s) = e^{−3πi/4} R_S from c(τ+1) = R_T c and
  c(−1/τ) = τ^{3/2} e^{−3πi/4} R_S c, c frame C's Higgs triplet; K_F is the subgroup of U(M) the gauge group realises:
  trivial (F_all), the scalars Z = {g : ρ_T(g) = ζI} (F_c), K ⊇ SU(3)_F acting on M (F_S); the restricted phase on Z is
  ζ^{3 Σ_f w_G(f) s_f}; F_S's cubic is A = Σ_f s_f d_f with d = (6, 3, 3, 2, 1, 1); a uniform scalar ζ is realised by
  the Standard Model group when some (ω^a, (−1)^b, e^{2πi x 6Y}) acts by ζ^{s_f} on every f
- imports: E6's U(1)_ψ charges 27 → 16₁ + 10₋₂ + 1₄ (a positive control and a read-out only); the standard discrete
  anomaly criterion (Ibáñez–Ross type, the phase ζ^{Σ 2T·dim·q})
- premises on main: B1674, B1689 (W44's frames), B1970, B1974, B1253, B1252, B1945 and B1940 (frame C's Higgs
  coefficients); the seat's SM-C23 (read only, for the scope of frame C's own k_u + k_d, which is not claimed)
- decisive script: relays/claims/sm_refile/r290_decisive.py, SHA-256 2927daebbc9a7231, depends on the standard library,
  numpy and mpmath, run as python3 relays/claims/sm_refile/r290_decisive.py, output SHA-256 1f5c7e264c916b46
- decisive lines: 9 lines marked "DECISIVE:", SHA-256 f3837ef9cdb62e25
- failing control: python3 relays/claims/sm_refile/r290_control.py
- second computation: none
- already on main?: `grep -il "SU(3)_F\|horizontal SU(3)\|U(1)_ψ" frontier/*/FINDINGS.md` on be8c83d4f: 10 arcs
  (B298, B487, B1340 among them), none restricting B1674's characters to a frame's K; closest B1674, B1689
- what would make it fail: the Standard Model group realising a non-trivial uniform scalar with ν^c present; a
  scalar of ρ_T's image outside μ₄, or a non-trivial restricted phase for I-31 on Z; F_S's cubic for I-31 equal to 0;
  or I-31's QCD exponent other than 12 with K_W ≡ 2 (mod 4)
