# B399 (Wall W-A) — A3 BANKED: the two 1/12s are DIFFERENT objects

**Status: A3 complete (the registered "different" branch); A1's 1215 rung computing;
A2 pending A1. Prereg committed first. Firewalled.**

## A3 — the singles constant is purely GENERIC; the seam constant recruits the boundary

The singles are the l = 0 column of the pair table, so the P64 formula applies verbatim.
The det-class split of the single-seed constant (support cells a = 1 and a = 6, both
value 1/4): **class 1 carries the entire 1/4; classes 3, 5 sum to exactly zero** (class
counts along l = 0: {1: 5, 3: 5, 5: 10}; no class-15 cells). Contrast the seam's
1/12 = 1/16 (class 1) + 1/48 (class 5, the golden boundary).

**The distinction (banked):** the singles' (1+c)/12-normalizer is a purely generic
Hannay–Berry object; the seam's 1/12 is generic + golden-boundary. The twist's value
content is precisely the BOUNDARY RECRUITMENT — the seam exists where the golden-ramified
cells contribute, the classical channel where they cancel. (This also explains W2's
decoupling: the singles transport classically up the tower while the seam's pair channel,
boundary-dependent, does not.)

**Provenance.** a3_normalizer.py → a3_normalizer.json; locks tests/test_b399_wall.py.

---

# A1 BANKED: the 1215 rung — both candidates KILLED; the third form's data

Both primes unanimous (singles_1215.json): **24 cells** (CAND-FIX said 12, CAND-DEG said
36 — both dead as registered). Structure: support ≡ 31 (mod 45) — **the 45-residue FROZE**
between 405 and 1215; mod-135 classes doubled to {31, 121}; count walk 4,4,4,12,24. Only
FOUR distinct values: **the class-31 line (12 cells) carries exactly 1/12 — the third
independent appearance of 1/12 in the program** (seam constant; singles normalizer; now
the frozen deep-tower value). The class-121 triple (4 cells each, cycling mod 405) is NOT
the (1+c)/12 form nor c/12 (both tested); its exact identification is the named next step
(a third prime or the ζ₂₇⁺ 9-dim solve). Sum rule Σ = 1 ⟺ the triple sums to 0 — decided
by the identification.

**Provenance.** singles_1215.py (~2.5 h, 2 primes), the reconstruction session; locks
tests/test_b399_wall.py (A1 section).

---

# A2 BANKED — W-A closes: the tower is a resolution generator, not a scale generator

Exact envelope across the five rungs: max|v| = 1/4, 1/4, 1/4, (1+2cos40°)/12 ≈ 0.211,
1/12 (the exact known line at 1215; triple ID open, sum-rule-conditional). **Monotone
contraction; every value in [−1/12, 1/4]; the total is frozen at 1 while the support
Galois-splits.** The registered expectation (BOUNDED) is confirmed with the sharper law:
the singles tower refines the fixed measure into finer cyclotomic detail — it cannot
generate hierarchy. WALL-1 PRICING: any scale separation, if this object has one, must
come from the seam/boundary channel (the pair tables across levels) — the one channel
not yet tested for hierarchy; named as the next lever.

**Provenance.** a2_hierarchy.py → a2_hierarchy.json; locks tests/test_b399_wall.py.

---

# PHASE 1a BANKED: the sum rule holds at depth 5; the triple's field DEEPENS

Three primes unanimous (gate 0): **the 1215 triple sums to exactly ZERO** — with the
twelve exact 1/12-cells, Σ_support = 1 at the fifth rung: **the frozen total is confirmed
through the entire tested tower.** The triple itself RESISTS every affordable ansatz:
not ℚ(ζ₉)⁺ (conjugate-orbit and free-coefficient searches, denominators ≤ 2160,
coefficients ≤ 400), not ℚ(√5) — **the singles' value field deepens at 1215 beyond the
degree-3/golden span** (the home-growth pattern in the singles channel; a banked datum).
Exact identification = a degree-6 reconstruction: primes 4–6 launched (detached); on
landing, the ID adjudicates the 31-collision and the supersingular sentinels
AUTOMATICALLY (the sentinel protocol). Locks: tests (gate-0 section).

---

# THE 1215 TRIPLE (partial): sum rule EXACT; e₂ = −1/48 (the seam value recurs)

The 24 cells resolve as: **12 cells at exactly 1/12** (the frozen line) + a **ℤ/3 triple**
at the ζ₂₇ level (one class mod 135, splitting mod 405), 4 cells each. The triple's minimal
polynomial (symmetric functions reconstructed by 6-prime CRT, stable from 4 primes):

    t³ − (1/48)·t − e₃,   with  e₁ = 0 (EXACT), e₂ = −1/48 (EXACT), e₃ pending.

- **e₁ = 0 is now EXACT (not mod-p):** the sum rule Σ_support = 1 is PROVEN at depth 5 over
  ℚ, not merely per-prime.
- **e₂ = −1/48 is the SEAM COEFFICIENT** — the fourth independent appearance of the
  1/48-family (seam value; 1/12 normalizer; the 1/12 line; now the triple's second
  symmetric function). The deep-tower singles and the seam share the exact constant −1/48.
- **e₃ (the product) needs more primes** (its height exceeds 6-prime reach); primes 7–10
  launched. **The 31-collision + supersingular sentinel test is on e₃'s prime content —
  PENDING that reconstruction.**

**Provenance.** triple_cubic reconstruction (inline, 6 primes) → triple_id.json; locks
tests/test_b399_wall.py (triple section). Sentinel adjudication: OPEN pending e₃.
