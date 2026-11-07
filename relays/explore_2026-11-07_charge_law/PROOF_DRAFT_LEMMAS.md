# THE CHARGE LAW (P-737) — the lemmas, written while the search runs (results not yet read)

## Notation

| symbol | meaning |
|---|---|
| L = [[1,0],[1,1]], R = [[1,1],[0,1]] | the two moves |
| LR = [[1,1],[1,2]] | symmetric, with eigenvalues φ^{±2} |
| v = (1, φ), v' = (φ, 1) | LR v = φ² v |
| D_S = L^{r₁} R^{r₂} ⋯ | the defect word, m runs, L-start |
| D_g | the golden word of m letters |
| X | R for odd m, I for even m |
| j = ⌈m/2⌉ | so that D_g X = (LR)^j |
| E = D_S D_g⁻¹ | the defect's difference |
| s_i = r_i − 1 | the extra letters of run i |
| N_L = L − I = e₂e₁ᵀ, N_R = R − I = e₁e₂ᵀ | nilpotent, so T^{r} = T + (r − 1)·N_T |

## Lemma A — the excess is a Rayleigh quotient

ΔS(S) = 2 log Q(E), where Q(E) = vᵀ E v / vᵀ v.

**Proof.**
1. LR is symmetric with eigenvalues φ^{±2} and orthogonal eigenvectors v and v̄ = (1, 1 − φ). So for every 2 × 2
   matrix M:
   tr(M (LR)^k) = φ^{2k} vᵀMv/vᵀv + φ^{−2k} v̄ᵀMv̄/v̄ᵀv̄.
2. D_S X = E D_g X = E (LR)^j, so tr(D_S X (LR)^k) = φ^{2(j+k)} Q(E) + O(φ^{−2k}).
3. The golden comparison is (LR)^{j+k}.
4. ℓ = 2 arccosh(tr/2) = 2 log tr + O(tr⁻²).
5. Therefore ΔS = lim_k 2 log[φ^{2(j+k)} Q(E) / φ^{2(j+k)}] = 2 log Q(E).
6. Q(E) > 0 because vᵀ D_S X v > 0 for the positive matrix D_S X. ∎

## Lemma B — the Fibonacci expansion

Q(E) = Σ_{A ⊆ {nontrivial runs}} Π_{i∈A} s_i · q_A, where:
- q_∅ = 1;
- q_A = (1/√5) Π_{consecutive a < b in A} w(b − a);
- w(d) = F_d / φ^d.

**Proof.**
1. Expand D_S X = Π_i (T_i + s_i N_i) X over the set A of runs that take N_i.
2. **The golden letters act as scalings that alternate between v and v':**
   - on rows: vᵀ L = φ v'ᵀ and v'ᵀ R = φ vᵀ;
   - on columns: L v' = φ v and R v = φ v'.
3. **The prefix.** The row vector arriving at run i is φ^{i−1} vᵀ (L-runs) or φ^{i−1} v'ᵀ (R-runs). Entering N_i
   multiplies it by the entry φ, so the first element of A contributes φ^{i₁}.
4. **The suffix.** The column leaving the last element of A carries φ^{m − i_t + x + 1}, where x = [m odd].
5. **Between consecutive elements a < b of A.** The golden word G of b − a − 1 letters contributes e_xᵀ G e_y, where x
   and y are fixed by N_a's exit and N_b's entry. This entry equals F_{b−a}, by induction on the alternating products:
   (RL)^k = [[F_{2k+1}, F_{2k}], [F_{2k}, F_{2k−1}]] and its neighbours.
6. **Dividing** by the golden term c_∅ = φ^{m+x}(2 + φ) = φ^{m+x}·√5·φ gives q_A. ∎

## Lemma C — the weights' floor

w(d) ≥ φ⁻² for every d ≥ 1, with equality only at d = 2. Hence Q ≥ B(s), where
B(s) = 1 + (φ²/√5)[Π_i (1 + s_i φ⁻²) − 1].
Equality holds when there is at most one nontrivial run, or exactly two at distance 2.

**Proof.**
1. **Binet:** w(d) = (1 − (−φ⁻²)^d)/√5.
2. **Odd d:** w(d) > 1/√5 > φ⁻².
3. **Even d = 2k:** w(d) = (1 − φ^{−4k})/√5. This increases with k, so its least value is at d = 2, which is
   (1 − φ⁻⁴)/√5 = φ⁻², because φ² − φ⁻² = √5.
4. **The bound:** replace every consecutive weight in Lemma B by φ⁻², then sum the multilinear series, Σ_{A≠∅}. ∎

## Lemma D — single runs, and the apex

**The run's congruence and cost.**
- For the single run n = s + 1, E = L^{n} R (LR)⁻¹ = L^{s} = [[1, 0], [s, 1]].
- L^{s} ≡ ±I mod N exactly when N ∣ s: for N ≥ 3 the sign must be +, and for N = 2 the two coincide.
- So the charge premise at S holds exactly when lcm(S) ∣ s.
- Q = 1 + s/√5 increases with s. Hence the run lcm(S) + 1 is the unique least single run, with
  ΔS = 2 log((L + √5)/√5).

**The apex (Perron's formula).**
1. A geodesic with cutting sequence (…, a₋₁, a₀, a₁, …) has a lift crossing the a₀-run at the cusp ∞. That lift's
   endpoints are x₊ = a₀ + [0; a₁, …] and x₋ = −[0; a₋₁, …].
2. So its apex height is (a₀ + [0; a₁, …] + [0; a₋₁, …])/2, and the highest apex is the supremum over positions.
3. At the run of n inside the golden background, this is (n + 2/φ)/2 = (n − 1)/2 + √5/2, using 1/φ = φ − 1.
4. At a golden position, a₀ = 1 and each tail is < 1, so the height is < 3/2. That is below (n − 1)/2 + √5/2 ≥ φ
   for every n ≥ 2.
5. The closed approximant differs from this by O(φ^{−4k}). ∎

## Lemma E — positions enter only modulo the golden period

**Golden runs leave E unchanged.** A golden run at position q multiplies D_S and D_g on the right by the same letter.

**A nontrivial run at position p** multiplies E on the right by P(p)^{s}, where P(p) = D_g(p − 1) T_p D_g(p − 1)⁻¹.

**The period.** Let o be the order of LR mod L. Then D_g(q + 2o) ≡ D_g(q) mod L, because the next 2o letters are
(LR)^o or (RL)^o = L⁻¹(LR)^o L, both ≡ I.
- So, with the first run at phase 1 (P = L), the reachable E mod L are exactly the products L^{s₁}·Π P(p_i)^{s_i}.
- The p_i range over all phases, since golden runs reach any phase.
- The premise depends only on E mod L. B depends only on the s_i.

**So the search is exhaustive.** The least Π(1 + s_i/φ²) over premise-satisfying multi-run defects equals the
shortest-path value on SL(2, ℤ/L), with:
- moves P(p)^{s} for 1 ≤ s ≤ L − 1;
- cost log(1 + s/φ²) per move.

A run with s ≥ L is excluded. Alone it already costs log(1 + L/φ²) = θ_L, and any second nontrivial run adds cost.

## The theorem (to be completed with the search's result)

**If** the least multi-run B-cost exceeds θ_L, then for every admissible defect satisfying the charge premise at S,
other than the single run lcm(S) + 1:

ΔS ≥ 2 log B > 2 log(1 + L/√5) = ΔS(lcm(S) + 1).

So the least-excess departure is the single run lcm(S) + 1, uniquely, at apex depth lcm(S)/2 + √5/2.

**Scope:**
- The theorem is about the 2D action (excess length).
- The volume statement (HL4) has no closed form, and stays a range result.
- R-start defects are the mirrors, covered by the L ↔ R symmetry (P-336).
