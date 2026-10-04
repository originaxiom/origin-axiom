# B1475 — PREREGISTRATION: THE SPIN SWAP, PHASE 1b — does the swap carry a quantity? The orientation-odd, spin-dependent invariant on the seven swap members, every spin structure, and whether any spin structure is mirror-invariant at all

**Sealed before any cell runs on the population.** cc (main), 2026-10-04. Lead L246 Phase 1b, after B1474 (Phase 1a:
seven GENUINE SWAP members, six FIX, both routes agreeing). The question: on a swap member, is there a continuous
(not 2-torsion) orientation-odd invariant of the pair (M, spin structure) — the thing B849 proves cannot exist for
invariants of m004 alone — and does any spin structure of a swap member survive the mirror?

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "spin structure|orientation-odd|2-torsion|Im R|mirror-invariant|amphichiral spin"`:
  /spin structure|orientation-odd|2-torsion|Im R|mirror-invariant|amphichiral spin/: 45 of 1347 arcs on main match (NEGATIVE 2, OPEN 1, PROVED 42). Read: **B849** (amphichirality forces every orientation-odd invariant to 2-torsion — its argument:
  X(M) = X(M̄) by the isometry and X(M̄) = −X(M) by oddness, so 2X = 0; it is an argument about invariants of M, not of
  (M, s)), **B1224/B1239** (CS ∈ {0, ¼} as the instance), **B279** (m004: both spin structures mirror-fixed, so for
  m004 the (M, s) version collapses to the M version), **B1474** (the swap table; η₀ and K per member; the τ words),
  **B1471** (odd-n: conj R_ρ(t) = R_{ρ⊗η₀}(t) with unit exactly 1 on the seven — the disclosed fact that fixes this
  arc's quantity). **Literature:** spin structures as a torsor over H¹(M;ℤ/2) with the isometry group acting affinely
  (standard); nothing else searched.

## 1. The objects and cells, fixed now

For each of the seven swap members (m003, m207, s955, s957, s960, t12838, o10_150695) and, as controls, three fix
members (m004, s961, t12839):
- **Spin(M)** = {ρ⊗χ : χ ∈ Hom(π₁, ±1)} (2^b lifts, b = dim H¹(M;ℤ/2)); the geometric lift s₀ = ρ.
- **C1 — the invariant.** R_n^{(s)}(t) at n = 1 and 3, t ∈ {2, 3, 0.6}, for every s. The mirror pairing: for each
  reversing τ of B1474, τ·s = s₀ + η_τ + τ*(χ) where s = s₀ + χ and τ* is τ's action on H¹(M;ℤ/2) (abelianise the τ
  words mod 2). **The quantity:** D_s(t) = Im R_1^{(s)}(t) at real t. Checks: R^{(τ·s)}(t) = conj R^{(s)}(t) for every s
  and τ (the symmetry step on every spin structure, not only s₀); D_{τ·s} = −D_s.
- **C2 — B849's bound, read on (M, s).** D_s is orientation-odd and spin-dependent; B849's argument gives 2·D_s = 0
  only when τ·s = s. Cell: D_{s₀}(t) ≠ 0 on the swap members (disclosed: known from B1471 at t = 2) and its magnitude
  across s and t — a continuous function, not a torsion class. On the fix controls D_{s₀} = 0.
- **C3 — mirror-invariant spin structures.** For each reversing τ: the set {χ : (1 + τ*)χ = η_τ} — the spin structures
  τ fixes. Union over τ = the mirror-invariant spin structures of M. On m003: H¹(M;ℤ/2) = ℤ/2 forces τ* = id, so
  1 + τ* = 0 and the equation has no solution since η₀ ≠ 0 — **no spin structure of m003 is mirror-invariant**
  (a hand theorem; the cell checks it and decides the other six, where H¹(M;ℤ/2) is (ℤ/2)² or (ℤ/2)³).
- **C4 — the index, where main's instrument reaches.** The class index (B1297/B1446 `index_num.index`) needs a fibred
  presentation; it exists on the record for the once-punctured-torus bundles: m003 = the −LR bundle (`mass_term.Level("-LR", 1)`),
  m004 = +LR level 1, t12839 = +LR level 4. On these three: I(ρ⊗χ) for every sign character χ (fibre characters (±1, ±1)
  and the meridian sign λ = ±1), with the parabolic point from `complete_points.Points` — does the index distinguish
  spin structures on the one swap member it can reach? Reported, not interpreted.

**Instruments at the seal:** `verification/spin_quantity.py` (sha256 3348d572d24a09bb; C1–C3) and `verification/spin_index.py` (sha256 26dfed94621d3b10; C4), compiled against the record's APIs and not run on any member.

## 2. Predictions, with priors

| | prediction | prior |
|---|---|---|
| P1 | R^{(τ·s)} = conj R^{(s)} for every spin structure of every member run (the symmetry step holds on all of Spin(M), not only s₀) | 85% |
| P2 | D_{s₀}(t) ≠ 0 at every t tried on all seven swap members, and D_{s₀} = 0 on the three fix controls | 90% |
| P3 | **m003 has no mirror-invariant spin structure**; at least one other swap member has none either | 90% / 60% |
| P4 | on s957 and s960 (K nontrivial) some spin structures off the K-orbit of s₀ are mirror-invariant | 55% |
| P5 | the class index I(ρ⊗χ) is 0 for every sign character χ on m003, m004 and t12839 (the geometric lifts are complete points — B1459's theorem covers ρ⊗ρ̄⊗χ; here the rank-two lift itself) | 80% |

**What a failure would mean.** P1 false: the matrix route and the torsion route disagree off s₀ — an instrument error
to be found. P2 false on a swap member: a genuine swap carrying no continuous quantity at s₀; the arc then reports D_s
on the other spin structures before any verdict. P3 false on m003: the hand theorem is wrong and the arc stops there.
P5 false: a count on a complete point — against B1459, which the arc would then have to confront (it would be the
most consequential outcome and the least expected).

## 3. Disclosed

Known before the seal: B1471's odd-n values at t = 2 on s₀ for all thirteen (complex on the seven, real on the six);
B1474's η₀, K and τ words; the hand argument for m003 in C3. Not computed: any spin structure other than s₀ and
s₀ ⊗ ε; any τ* on cohomology; any index on a twisted lift; D at t ≠ 2.

## 4. Scope

Frame F-CI; object the family's seven swap members and three fix controls at level one; reach *class*; hypotheses as
in B1474 (HP holonomy; the τ words found at length ≤ 7). Not a physics claim: D_s is a number attached to (M, s); the
sentence "a fermionic chirality carrier" is the thesis of L246, firewalled, and this arc only decides whether the
quantity exists and whether a mirror-invariant spin structure does.
