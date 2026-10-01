# B1434 PREREGISTRATION — THE ARCHITECTURE CENSUS: does the generated state space carry generation-shaped backgrounds that the root's own tower does not?

**Sealed 2026-10-01, before the census is run on any state other than the root. Seat: cc (main). Occasion: the owner's
direction of 2026-09-30 — "we have flaws in our genesis, were discriminate in our selection principles, and end up with
m004. the existence allows more than that … we must account for the whole allowed architecture, its relations and
interactions" — and the question that followed it: does the widened frame hold what the root withholds?**

## 0. The quantifier (P0)

For every signed cyclic word state s = (ε, w) with w of length 2 to 6 in L, R (both letters, primitive, up to rotation
and swap), and every level k = 1 … 6 whose fibre torsion is at most 330: the complete Standard-Model-frame doublet census
of the k-fold cyclic cover of the bundle with monodromy ε·A(w), lifted and non-lifted backgrounds alike. 24 states, 68
levels, 942 268 candidate modules. The scope sentence names no manifold.

## 1. What has been seen before the seal (disclosed)

- The root's tower, (+, LR) at k = 1 … 6: B1432's table (seen 2026-10-01 on two other presentations).
- **C1, the binding control, run before the seal on the instrument of this arc:** (+, LR), k = 1 … 5, in the mapping-torus
  presentation built here: 1/1/0/0, 5/25/8/0, 16/256/72/48 (none lifted, orbits of three), 45/2 025/488/256,
  121/14 641/2 200/400. Identical to B1432. Record `verification/control_m004_tower.json`.
- For every other level in the population only the monodromy trace, the torsion order and the torsion exponent have
  been computed (the sizing run). **No index has been computed on any state other than the root.**
- Read, not computed here: the sep16 lane's xB027 (the sister's tower, lifted backgrounds only: levels 2 and 3 give
  none, level 4 gives 384 lift data on 96 loci, every count ±1), the SM lane's B1385 (word states have one cusp and
  b₁ = 1) and B1506 (the root's census).

## 2. Conventions (declared before the run)

- **States, levels, presentation, deck:** exactly as in the docstring of `verification/architecture_census.py`
  (sha-256 below). τ_x: x ↦ x, y ↦ yx and τ_y: x ↦ xy, y ↦ y fix [x, y] exactly; the sign is ι: g ↦ c g⁻¹ c⁻¹ with
  c = yx; peripheral pair μ = t, λ = [x, y]; the deck of level k is x ↦ φ(x), y ↦ φ(y), t ↦ t.
- **Frame:** B1374's sectors Q(1,3), u^c(−4,3), e^c(6,3), d^c(2,1), L(−3,1), ν^c(0,−5); a background is (θ, ψ_Y, W)
  with λ = θ²/W and α_s = θ ψ_Y^{s_Y} W^{(s_γ−1)/2}, counted once by (λ, α_Q, …, α_{ν^c}); "lifted" means λ is a square.
  **Generation-shaped:** the five charged sectors have equal non-zero index.
- **Index:** main's B1297 class index, by B1427's `myindex.py`; characters trivial on μ with values in μ_N, N the torsion
  exponent; three primes ≡ 1 mod N above 3 000; every firing module re-checked at the second and third prime.
- **A level is discarded, and reported as discarded,** if any firing module differs at another prime; it is then re-run
  at three further primes. (B1432 found one bad prime.)
- **The frame is main's E₆/27 frame carried to every state as an instrument.** That the frame is the right one for a
  state other than the root is not claimed and not tested here.

## 3. Sealed predictions (each can come out either way)

| | prediction | prior |
|---|---|---|
| P1 | On every level computed, every generation-shaped background has \|count\| = 1 in each charged sector. | 85% |
| P2 | h¹(λ) = 1 at every locus on every level computed. (If 2 occurs anywhere, P1 loses its mechanism.) | 90% |
| P3 | **At least one state other than the root carries a generation-shaped background at its own level, k = 1.** The root has none (its fibre has no finite character). | 55% |
| P4 | **The three-fold cover of every state in range carries generation-shaped backgrounds in deck orbits of three.** (12 states have k = 3 in range.) The alternative: orbits of three at the three-fold level are special to some states. | 45% |
| P5 | Wherever orbits of three occur at a three-fold level, none of their backgrounds lifts. | 60% |
| P6 | Signs split equally on every level that has generation-shaped backgrounds. | 80% |
| P7 | On every level, every deck orbit of backgrounds has size dividing k and greater than 1. (A size-one orbit would be a background fixed by the whole deck: a count the state itself carries.) | 70% |

## 4. What each outcome would mean (written before the data)

- **P3 YES** would be the first generation-shaped background on a generated state at its own level: an ingredient the
  root's own level provably lacks, present elsewhere in the architecture. **P3 NO** on all 23 would say the own-level
  absence is structural across the grammar to length six, not a fact about the root.
- **P4 YES** would say three is the degree-three cover relation acting on any state, not a property of the root or of
  s961. **P4 NO** would name the states for which it holds, and that list is then a datum about the root's place.
- **P1 or P2 failing** would be the first count other than one per background, and would be re-run at six primes and in
  exact arithmetic before a word of it is written.
- None of the outcomes is a physical generation count. The fence is B1432's: main's class index on reducible non-split
  modules; non-semisimple backgrounds; the three members of an orbit are three backgrounds; no value.

## 5. Not in this arc

Covers other than cyclic ones dual to the fibre; fillings; states with the orientation-reversing half step (the
Gieseking parent); words longer than six; any reading of a deck as gauged or kept.

## 6. Hashes at seal

    architecture_census.py   see ARTIFACT_HASHES.txt
    B1432 cover_census.py    see ARTIFACT_HASHES.txt
