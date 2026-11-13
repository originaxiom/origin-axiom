# SM-C6 E2 (second half) — the rank over 𝔽₂ of the three named bits, on the record's own observables

*Step card of SM-C6 (main's M13, M16, M18; SM-C5's entry E2 for GENESIS FK12 (ii)). Pushed before the run and before
B1915 is read, as M13 asks. Main at the head fetched 2026-11-13 evening. Data-free.*

## What is computed

- **The three named bits,** as involutions on (word state, level, sector module V(ℓ, α)):
  - **c, the mirror (the hand):** the state (ε, w) goes to (ε, w with L and R exchanged);
  - **X, the exchange of particle and antiparticle:** V(ℓ, α) goes to its conjugate V(ℓ⁻¹, α⁻¹);
  - **O, the order of the pieces:** V(ℓ, α), with sub α and quotient β, goes to the module with the pieces exchanged,
    V(ℓ⁻¹, β). Duality is D = O·X: V* ≅ V(ℓ, β⁻¹).
- **The observables,** all built from B1438's exact slopes:
  - (i) the state's slope multiset, up to the meridian's integer shift;
  - (ii) the based count (n(V), n(V*)) of SM-C6 E1;
  - (iii) the class count I = n(V) − n(V*).
- **The rank.** On each observable, each involution acts either trivially or not. The 𝔽₂-rank is the dimension of the
  group of actions that c, X and O generate on that observable. It is computed exactly on B1438's census levels (both
  signs), with the mirror states LLR ↔ RRL and LLLR ↔ RRRL at the same levels. LR is its own mirror up to rotation.

## The prediction, written before the run

From B1438's s(χ⁻¹) = s(χ), and the mirror sending s to −s:
- **(i) the slopes:** only c acts. Rank 1.
- **(ii) and (iii) the counts:** only O, and with it D, acts. c and X act trivially. Rank 1.
- **The joint observable:** rank 2.
  - X is invisible to every slope-built observable. It is not an independent bit there: D acts as O.
  - **So B1327's "over-count" holds:** of the three named bits, two are independent (the hand and the pieces' order);
    the exchange is carried by them.

## The outcomes

- **Rank 2 on the joint observable, with X trivial:** as predicted, and the over-count holds.
- **Rank 3:** X acts on some observable; three independent bits.
- **Rank 1 or less:** c and O coincide, or one of them is invisible. The record's two independent signs (GENESIS
  FK12 (iii)) collapse.

## Controls, which must fail

- **P1:** a planted wrong mirror, w mapped to its reverse in place of the L ↔ R swap. c must then act trivially on (i)
  on every level: E1 found the reverse invisible.
- **P2:** a planted wrong conjugation, ℓ inverted but α kept. X must then act non-trivially on (ii) on some level.
