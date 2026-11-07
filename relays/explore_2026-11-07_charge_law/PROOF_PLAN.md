# THE CHARGE LAW (P-737) — the proof plan, written before its computation (the explore seat, 2026-11-07)

**For:** the owner's choice "1" (2026-11-07), proving P-737.

**P-737, as rowed by main:** "prove it for all defects (a single run of lcm(S) + 1 is the shortest word with E ≡ ±I mod
every level in S, and its excess length the least), or find the counterexample outside the ranges; then a LAW_MAP row".

**Kind:** data-free mathematics: SL(2, ℤ/N) arithmetic, exact identities, an exhaustive finite search. No frame value, no
data, no held-out quantity.
**Written before** `charge_law_proof.py` is run. Its output is committed unread, then read.

## Already visible, before any computation: the "shortest word" clause is false as stated

In main's own verified ladder (B1853; the explore seat's conservation_out.txt), (2, 1, 2, 4, 4) satisfies the charge
premise at {4, 5} with 13 letters, against 21 for the single run (21). (2, 1, 6, 3, 4, 2) satisfies it at {2, 3, 4, 5}
with 18 letters, against 61. So only the excess-length clause can be a law. The search below also reports the fewest
extra letters per S.

## Notation

- A defect has runs (r₁, …, r_m) at positions 1..m (L-start), with s_i = r_i − 1.
- E = D_S D_g⁻¹. The golden eigenvector is v = (1, φ): LR = [[1, 1], [1, 2]] is symmetric, with LR v = φ² v.
- The nontrivial runs are those with s_i ≥ 1.
- The charge premise at S is E ≡ ±I mod N for every N ∈ S, with L = lcm(S).

## The claims and how each is shown

- **Lemma A (exact; proof by the spectral projector of the symmetric LR).**
  - The statement: excess length(S) = 2 log Q(E), with Q(E) = vᵀ E v / vᵀ v.
  - The proof: tr(M (LR)^k) = (vᵀ M v / vᵀ v) φ^{2k} + O(φ^{−2k}) and D_S X = E (LR)^j.
  - Checked numerically on every R1 defect against the web seat's `excess` (k = 20).
- **Lemma B (exact; expansion of Π (T_i + s_i N_i), N_L = e₂e₁ᵀ, N_R = e₁e₂ᵀ).**
  - The statement: Q = Σ_A Π_{i∈A} s_i · q_A, over subsets A of the nontrivial runs, with q_∅ = 1 and
    q_A = (1/√5) Π_{consecutive a<b in A} w(b − a), where w(d) = F_d / φ^d.
  - Checked numerically against Lemma A on every R1 defect, and on a random sample of R2.
- **Lemma C (exact, Binet).**
  - The statement: w(d) ≥ φ⁻² for every d ≥ 1, with equality only at d = 2.
  - Hence Q ≥ B(s) = 1 + (φ²/√5)(Π_i (1 + s_i/φ²) − 1), with equality for one nontrivial run.
  - Checked for d = 1..300.
- **Lemma D (single runs).**
  - L^s ≡ ±I mod N ⟺ N ∣ s. So the cheapest single run satisfying the premise is s = L, the run lcm(S) + 1, with
    Q = 1 + L/√5.
  - Its apex is (n − 1)/2 + √5/2 by Perron's formula: at the run, the highest semicircle has radius
    (a₀ + [0; a₁, …] + [0; a₋₁, …])/2 = (n + 2/φ)/2. All other positions are lower.
  - Checked for n = 2..80 with `highest_cf`.
- **Lemma E (positions enter only mod the golden period).**
  - The statement: E = Π_i P(p_i)^{s_i}, with P(p) = D_g(p − 1) T_p D_g(p − 1)⁻¹. Golden runs do not change E.
  - So a run can follow at any phase mod 2·ord(LR mod L).
  - Hence the set of premise-satisfying multi-run E, and their least B, form a shortest-path problem on the finite group
    SL(2, ℤ/L), with cost Σ log(1 + s_i/φ²).

## The decisive computation (exhaustive; every length and every gap)

**Method.** For each nonempty S ⊆ {2, 3, 4, 5}:
- a Bellman–Ford search over SL(2, ℤ/L), from the first run at phase 1;
- moves P(p)^s for every phase p mod the period and 1 ≤ s ≤ L − 1, each costing log(1 + s/φ²);
- runs with s ≥ L are excluded, since one alone already costs the threshold.

**Reported per S:**
- the least B-cost over premise-satisfying states reached with at least two nontrivial runs, against the threshold
  θ_L = log(1 + L/φ²), with the margin and the minimizing sequence;
- the fewest extra letters σ over the same states, against L.

**HP (the law):** for every S, the least multi-run B-cost exceeds θ_L.
- If it holds for S, every multi-run defect satisfying the premise has Q ≥ B > 1 + L/√5. The single run lcm(S) + 1
  is then the unique least-excess departure, over all defects.
- **If it fails for some S,** the sequences with B ≤ θ_L are enumerated, and the exact Q is bounded over their gap
  realizations. A defect with exact Q < 1 + L/√5 is a counterexample, and it would be reported as one.

**Priors:**
- Lemmas A to E are near certain; they are proofs.
- HP for S = {5}: about even. The ranges reached distances of 7, and the golden period mod 5 is 20.
- HP for the larger S: less certain.

0 of 19.
