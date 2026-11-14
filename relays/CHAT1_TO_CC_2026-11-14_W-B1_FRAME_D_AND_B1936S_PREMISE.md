# W-B1: B1936's premise is false in D1 and is the global bit restated in D2. S has no level-5 class of its own. In D1 every object is holomorphic, the up Higgs (class 1, odd) included. In D2 the premise holds exactly when the holomorphic Higgs has class 4. D1 and D2 represent charge conjugation by twist negation and by complex conjugation, which differ by the mirror (with b ↦ −b) and agree on its fixed slice when b = 0

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). This note answers M29 (W-B1) and
closes card W-B1 (`relays/cards/CHAT1_W-B1_frame_d_and_b1936s_premise.md`, 5261ff702). agy-exp is to check it (M29).

**How it was checked.** Computed once, on this seat's own code; expectations committed first; tested against planted
errors (1, caught).
- **The sealed run.** The script `relays/chat1_2026-11-14_wb1/wb1_checks.py` (sealed at 6aa625b3e) was run once. Its
  output was committed (ac4d9a1fa) before it was read. All five expectations were met.
- **No frame output was computed:** no coupling, ratio or mixing, and no named τ.
- **The firewall lift.** The author's lift of the overlap step for W-B1 (status file, 2026-11-14) was not needed for
  this note.

**What was read.**
- **Frame C's code, directly:** B1656's functions as copied in B1723; the Higgs as built in B1726's `census.py` and
  B1838's `exact_end_web_seat.py`; the header and definitions of B1691's `the_exponents.py`.
- **Through the mask:** the pairs programme's card P-Q1.

## 1. The two consistent frames, by their conjugations

- **Frame C.**
  - **Matter carries its charge q as a twist:** the kernel's theta characteristic is `twist_of(q·w, τ)`, linear in q.
  - **The Higgs carries its charge only as a reading.**
    - S = Σ (DR)ₖ Qₖ is built from the Serre derivative of B1691's triplet R = (−θ₂², −θ₄², iθ₃²)/(θ₂θ₃θ₄).
    - S̃ = ε conj(S) εᵀ conjugates S's values at τ. So S̃ is the pointwise conjugate, antiholomorphic in τ. This
      answers W-F20's R5 on the definition: S̃ is not the coefficient conjugate.
- **D1 (P-Q1).** Every field, the Higgs included, carries its charge as a twist. Charge conjugation is then
  N: θ[a, b] ↦ θ[−a, −b].
- **D2 (P-Q1).** Every field carries its charge as complex conjugation, as the Higgs does in frame C. Charge conjugation
  is then K: f ↦ conj f.

## 2. The results

| line | result |
|---|---|
| E1 | N: θ[−a, −b](u, T) = θ[a, b](−u, T), so N keeps holomorphy. K: conj θ[a, b](u, T) = θ[a, −b](−ū, −T̄) = θ[−a, b](ū, −T̄). So K = M ∘ β ∘ N, with M the mirror (u, T) ↦ (ū, −T̄) and β: b ↦ −b, and K is antiholomorphic. Both are identities of the series (K term by term, N after n ↦ −n). The residual at 40 random points is 0 because the two sides sum the same terms. The plant (K with +b) fails at all 40 |
| E2 | Under τ ↦ τ + 1, R and DR transform by T_R = [[w, 0, 0], [0, 0, w], [0, w⁻³, 0]], w = e^{iπ/4}. This matches the hand matrix to 2e-30 for R, DR transforms by the same matrix exactly, since d/dτ and E₂ commute with τ ↦ τ + 1 (residual 5e-22 with the numerical derivative). T_R is B1691's ρ_R(T) = e^{iπ/4}L⁻¹. Its eigenvalues are w, w³ and w⁻¹: all eighth roots of unity, none a fifth root. **S has no level-5 class of its own** |
| E3 | **D1.** Matter's classes are 2, 2, 4, 4, 2. The sectors' Higgs classes are up 1, down 4 and leptons 4. Every object is holomorphic (E1), so the holomorphic objects meet the classes {1, 2, 4}, of both parities. **B1936's premise is false in D1** |
| E4 | **D2.** Matter's frame fields have classes {2, 4} (even) and their conjugates {3, 1} (odd). If the holomorphic Higgs has class 4, the premise holds and charge gives (up S̃, down S, leptons S) = W₋. If it has class 1, the premise fails and charge gives (S, S̃, S̃) = W₊. **In D2 the premise is the global bit restated** |
| E5 | N and K coincide at mirror-fixed points (Re T = 0, b = 0, u real; residual 0). At 20 generic points they differ, by at least 1.6 % (relative). **On M's fixed slice (u real, Re T = 0) the two conjugates agree when b = 0 (more generally when 2b and 2ab are integers). At generic points they differ** |

## 3. What it means

**A clean refutation in D1.**
- When the Higgs carries its charge as matter does, its two charges are θ-twists of opposite sign. Both are holomorphic,
  as every kernel twisted on a fixed line is (its characteristic does not depend on τ).
- Holomorphy then cannot name a parity class. The up sector's Higgs (class 1, the 5) is holomorphic, and so is matter
  (classes 2 and 4).
- B1936's "conjugation flips holomorphy" holds for K, not for N, and D1's conjugation is N.

**D1 has no reading to choose. That is how D1 removes the bit, not parity.**
- Each sector's Higgs twist is fixed by charge conservation.
- Flipping the hypercharge sign negates every characteristic. On one theta function this is u ↦ −u (E1). On B1656's
  bilinear kernel, whose second leg sits at u + t, each such leg picks up the quasi-periodicity factor e^{2πi(b − u)}.
  These factors cancel against the kernel's phases e^{iπb} and its θ₁ denominators, and
  bil(−x, −y, u, t) = −bil(x, y, −u, t) exactly. That is the fibre's involution u ↦ −u, with an overall sign and no
  exchange of the two legs, and each channel's residue at u = 0 is unchanged.
- If the frame's fibre integrals and residues are symmetric under u ↦ −u, the hypercharge sign is a convention in D1,
  and no Higgs bit remains there. That symmetry is argued here, not computed. Matter's kernels obey the identity above, and the integration cell is
  symmetric under u ↦ −u. How the Higgs's twist enters D1's overlap (§ 5) must respect it too.
- Under this hypothesis nothing in D1's read-out changes with the hypercharge sign, J's sign included, because u ↦ −u
  involves no complex conjugation. P-Q1 expects J to flip in D1, and main's values will decide between the two.
- What D1's coupling gives, and whether it reproduces W₋, W₊ or neither, is a question about values. It is main's and
  agy-exp's (P-Q1). This seat's firewall holds those values.

**In D2 the premise fixes nothing.**
- D2 uses K, so holomorphy flips with charge conjugation, and matter's frame fields are all even (E4).
- The premise then says only that the holomorphic Higgs carries class 4. That is P-847's global bit.

**S's class.**
- Frame C's Higgs is built from a triplet on which T acts with eighth roots of unity (E2). So no level-5 class can be read
  from S's forms.
- In each of the three frames here, the Higgs's level-5 class comes from a twist (D1), or it is assigned (frame C,
  D2). Since 1 is not among T's eigenvalues, S's forms are not class 0 either. This settles W-F20's R2, and R4, for S's
  own forms.

**D1 against D2.**
- They differ by which conjugation represents charge conjugation, N or K.
- By E1, K = M ∘ β ∘ N on theta functions with real characteristics, with M the mirror (u, τ) ↦ (ū, −τ̄) and
  β: b ↦ −b. So the two frames are a mirror pair, as P-Q1 expected.
- Their conjugates agree pointwise on M's fixed slice (u real, Re τ = 0) when b = 0, and more generally when 2b and 2ab
  are integers. They differ at generic points (E5).
- As functions on the fibre they never coincide, since one is holomorphic in u and the other antiholomorphic. E5 does
  not exclude agreement at isolated points off the slice, and such points exist.
- Whether their read-outs on the whole agree depends on the read-out's mirror symmetry. P-Q2 found frame C's averaged
  frame mirror-symmetric, on one computation (a second is owed). For D1 and D2 that is a question about values, for main and agy-exp.

**For W-F16's ledger.**
- B1936's route, parity naming the holomorphic sector, does not settle the second block. It is false in D1 and
  circular in D2.
- D1 offers a different route: no reading at all, with the hypercharge sign a symmetry of the fibre. If main's values
  confirm it, the Higgs bit leaves the inputs by construction, not by a rule.

## 4. What would overturn this

- **In D1:** a field whose charge-conjugate is not holomorphic. That is impossible while charges enter as
  characteristics that do not depend on τ (each twist on a fixed line, as matter's is in frame C) and charge
  conjugation is N (E1). A Higgs twisted at a point of the fibre held fixed as τ moves would have characteristics
  depending on Im τ. Neither of its charges would then be holomorphic in τ, and the premise would be vacuous in D1
  rather than false.
- **For S:** a level-5 class read from S's forms. E2 excludes it.
- **In D2:** a definition under which the frame's matter fields are not all of one parity. The premise then fails
  outright.
- **The part not computed:** D1's coupling breaking the u ↦ −u symmetry. Then the hypercharge sign would be a bit in D1
  too. This is the open half, and it is in main's values.

## 5. If main wants D1's coupling built here

The lift allows the overlap step, so this seat can build D1's coupling. There is one design choice to name first: where
the Higgs's twist enters. The options are one leg, split between the two legs, or a third θ-factor in the overlap.
- With any choice, this seat can check D1's structure: the u ↦ −u symmetry and the absence of a reading.
- It computes no output, because the outputs are held values.

## 6. Typed

| statement | how checked |
|---|---|
| E1 to E5 | computed once; expectations committed first; tested against planted errors (1, caught); E1, E2 and E5 recomputed independently by the referee |
| bil(−x, −y, u, t) = −bil(x, y, −u, t), the hypercharge flip on the bilinear kernel | recomputed independently by the referee (20 random points; the derivation is by hand) |
| under the u ↦ −u hypothesis, J's sign does not change with the hypercharge sign in D1 | a prediction |
| the premise false in D1; the bit restated in D2; D1 and D2 a mirror pair | a reading, resting on E1 to E5 |
| the hypercharge sign a convention in D1 (u ↦ −u symmetry of the frame's integrals and of the Higgs's twist) | a hypothesis (argued, not computed) |

## 7. Files

`relays/chat1_2026-11-14_wb1/`: `wb1_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wb1_checks_out.txt`,
`wb1_checks_err.txt` (empty).

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
