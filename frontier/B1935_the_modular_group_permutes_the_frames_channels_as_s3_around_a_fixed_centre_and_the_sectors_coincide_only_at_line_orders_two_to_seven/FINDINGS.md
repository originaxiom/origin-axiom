# B1935 — The modular group permutes the frame's channels as S₃ around a fixed centre; the centre flips matter's charges and not the Higgs world; the Higgs triplet is of level 8; the sectors coincide only at line orders 2 to 7

**Verdict: PROVED** (exact or to machine precision; computed once by main; the lock plants a fault against each
claim). Main, 2026-11-14. Register rows P-845, P-846, P-847. 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /channel.*permut|S_3|Gamma\(2\)|theta_2|the centre|-I acts|sector.*coincid|lepton.*up/: 49 of 1675 arcs on main match (NEGATIVE 10, OPEN 7, PROVED 32); 44 register rows match (DECLINED 1, DONE 31, QUEUED 12)`.
  The nearest arcs:
  - B1724: the readings' covariance lies inside SL(2, ℤ)/Γ(2) = S₃, and the Higgs components' T-action.
  - B1906: the four channels in closed form, each residue a product of two theta constants.
  - B1728: the line's order as a quotient of hypercharge.
  - B1934: the lepton copy at orders dividing 5.
  - P-355: the order-10 identity up to half-periods.
- **The literature:** standard. Under SL(2, ℤ) the even thetas ϑ₂, ϑ₃, ϑ₄ are permuted (T swaps ϑ₃ and ϑ₄; S swaps
  ϑ₂ and ϑ₄), with ϑ₁ fixed up to a factor. The results below place that action on the frame's own channels.

## 1. The channels: S₃ around a fixed centre (`channels_and_centre.py`)

On the frame's channel residues R_s (s = 1, i, j, k), at three points, three lines and all three sectors (27 cases):
- **T** (τ → τ + 1, line (α, b) → (α, b − α)) fixes channels 1 and i and swaps j with k;
- **S** (τ → −1/τ, line (α, b) → (−b, α)) fixes channels 1 and k and swaps i with j.

The common modular factor agrees across channels to 3e-15, and the next-best permutation misses by at least 1.6e-2.
The two swaps generate S₃ on {i, j, k}; channel 1 is fixed by both. **The modular group acts on the frame's four
channels as S₃ permuting three, around one fixed centre.**

## 2. The centre: matter's charges, not the Higgs world

The centre −I = K², two undoings, sends every line w to −w, which flips every matter charge. On every reading and every
mixing pair the frame's outputs are unchanged to 3e-14, and no reading is exchanged with another. The centre ties the
undoing to matter's charge sign, which is a convention of the frame. It cannot reach the Higgs world (P-847; the GL(2, ℤ)
no-go).

## 3. The Higgs triplet is of level 8, not 5 (`higgs_triplet_level.py`)

From B1724's committed covariance, T's eigenphases on the Higgs direction's triplet are 1/8, 3/8 and 7/8, eighth roots.
The level-5 icosahedral triplets (B1934) have fifths. **So frame C's only modular triplets are its channels (S₃, of
level 2) and its Higgs direction (level 8). The level-5 icosahedral triplet plays no role in frame C as built.**

## 4. Which line orders make one sector copy another (`sector_coincidences.py`, exact, N ≤ 60)

With the frame's charges (6Y: Q 1, u −4, d 2, L −3, e 6), modulo N:
- **up and down:** equal at 2, 3, 6; negated at 2; negated and transposed at 3;
- **up and leptons:** equal at 2; negated at 2; **negated and transposed at 7**. Negation leaves the matter part
  unchanged (§ 2), so at orders dividing 7 the leptons copy the up quarks transposed;
- **down and leptons:** equal at 2 and 4; **transposed at 5** (B1934's lepton copy); negated at 2.

**Every coincidence happens at an order from 2 to 7, and orders above 7 identify no two sectors.** At the read-out's
order, 5, only the leptons and the down quarks coincide.

## Not claimed
No value is computed or compared. Which line orders the read-out may use stays the frame's question (P-845).
