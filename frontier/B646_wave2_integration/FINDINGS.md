# B646 — the cc2 wave-2 integration: three packets verified and banked (R20-10 first tranche)

**Received 2026-07-16: three packets + a triage index (the cross-seat
level-ladder campaign's residuals loop, next queue, and proof queue).
Processed in the mandated order (ERRATUM first). All verification
internal (PROVENANCE.md §0); the sending seat's materials archived
verbatim under `cc2_packets/` (ORIGINALS_MANIFEST.txt = sha256 of every
file as received; two disclosed privacy patches in FINDINGS headers;
zip hashes recorded — the triage index's third zip suffix "…57df65"
was an elision typo for …57d4df65, first-8 exact).**

## Verification performed on this seat (verify-don't-trust)

| check | result |
|---|---|
| All ELEVEN seals re-hashed (8 preregs + 3 run scripts/sealed docs) | **11/11 exact** (0c4df92d, 70a41662, 0982d8e0, aa47092d, 8393e404, 09fc3565, 09246f08, cbb83a82, f3b19098, a415f881, 287bfe86) |
| Q3 lemma battery rerun here | **L3 300/300 PASS**; L2 sectors reproduce (½ + ½ split) |
| The ERRATUM's decisive rungs rerun here (their pipeline, packet-local imports) | **Z(29) = 0, Z(31) = 0, Z(37) = +1** — matches jeffrey_decider.json |
| Independent arithmetic of the corrected law | (29,31 ≡ 4,1 mod 5: residues → silent; 37 ≡ 2: non-residue → unit) ✓; retro-check vs OUR banked ladder consistent on every rung (14: 0+resonance=1; 16: 0; 19: 0+Φ₉=2) |
| R5 proposed locks rerun here | **20/20 PASS** |
| N2 clock predictor rerun here | 12/19 rule-derived reproduced; the k=11 exception is documented in-packet; the "36" mis-relay was cc2-context-only — OUR bank carries no contaminated clock value (searched) |
| Q1 level-8 readouts spot-checked from disk | Z₈ = +1 (1.0 + 2.7e-15i), clock = 60, tr_odd ≈ 0 ✓ — 3/3 sealed predictions |
| Q2's mechanism arithmetic | A₁ mod 7: order 8 in SL(2,7), −I at 4 ⇒ order 4 in PSL ✓; PSL(2,7) 3-dim character on the order-4 class = +1 with eigenvalues {1,i,−i} ✓ (standard table) |
| Q2 vs banked B640 collision check | **NO COLLISION** — B640's 2I×ℤ/3 is the image of the WELD-LETTER subgroup ⟨R,L⟩; Q2's ρ_Fib⊗χ is a tensor factorization of the block (their Fibonacci-core clock 10 = our ρ(RL) order 10; their χ(A₁)=1 blindness is consistent with the letter-subgroup image) |

Not independently rebuilt here: the level-7/level-8 exact enumerations
(their pipeline, sealed + internally two-pipeline-verified 7/7; the k=8
exact-counts npz held on their seat, on request). Banked with that
provenance stated.

## What banks (per cell)

- **R1 (level 7, κ=19):** the splitting law's split-prime rung
  (cyclotomic cubic subfield of ℚ(ζ₁₉), no √19) + **Z₇ = 2** — the first
  ladder value outside {0,1}; Tr(Θρ) = 0 exactly ⇒ sectors (+1,+1). THE
  LADDER → {+1, +1, +1, 0, +1, +1, 2} (supersedes B600's four-rung line).
- **R2:** clock = 36 = ord(A₁ mod 228) CONFIRMED PREDICTION-FIRST (seal
  0982d8e0 pre-unblind) — the central-kill mechanism stands; L77/L81
  upgraded (mechanism prediction-confirmed).
- **R3:** the peak MECHANISM-CANDIDATE (plateau [0.8,1.5], κ* ≈ 1.1 ≈
  MST-gap max 1.2) — candidate only.
- **R4:** the V2b resonance lead **KILLED** (sealed; both predictors
  sign-flip out-of-sample) — closed permanently.
- **R5:** the 20-assert lock file ADOPTED
  (`tests/test_cc2_r5_adopted.py`); TWO LOCK-GAP TICKETS opened: the
  B544 headline and B480 are UNREPRODUCIBLE as banked (2 source scripts
  missing from disk) — registered in OPEN_LEADS.
- **R6:** deep-V NULL-EXTENDS (max 1.49σ); the a_C discriminator +
  (t/V)² salvage registered.
- **N1 + ERRATUM (applied at banking):** the counting mechanism (Z =
  signed Weyl-average of Gauss sums over twisted fixed-point sectors;
  det B_w = #Fix exact); the 16-zero = dyadic interference; the
  19-surplus = Φ₉ class saturation; **THE CORRECTED GENERIC-SILENCE
  LAW: for gcd(κ, 2·3·5·7·11·19) = 1, Z(κ) = (1 − (κ|5))/2 — the
  object's generic silence is the quadratic character of its own
  monodromy discriminant, 5 = disc(A₁)** (decided 29/31/37, rerun
  here). The packet's flat "generic ⇒ +1" line is WRONG and never
  entered the bank. PREDICTION BANK Z₈..Z₁₃ = 1,1,2,1,2,0 (Z₈ since
  confirmed).
- **N2:** the stage-split clock law (k=1 character rungs; k=2 anomaly
  rungs — now dissolved by Q2; k ≥ 3 clock = ord(A₁ mod ord(T_k)) with
  stage-typed central kills); verbatim-scored 12/19 with documented
  exceptions; SU(3)₁₃ prediction-first hit (12); E₆ k=8 pred 60 → HIT
  (Q1). The E₆ k=4 clock is 12 from disk (an in-context relay in their
  session mis-carried 36 — the MB13 class; our bank was never
  contaminated, verified).
- **N3:** one-organ-or-two **UNRESOLVED** (jitter floor ~1.3σ vs the 2σ
  bar; depth-15 gaps shrink) — the bound banks; their recommendation
  (a new statistic, not more depth) registered.
- **N4:** cc2's independent receipt of OUR B643/B644/B645: **all
  verified** (byte-faithful reruns + genuinely independent paths:
  sympy-over-ℚ(√−3) for B643's 172×3 system → nullspace exactly
  (0,0,1); their own engine rebuild for B644 → 120/120 elementwise,
  and the disclosed M3 bad tables score 96/120 and 72/120 —
  independently corroborating our sealing-error adjudication; B645's
  normal forms recomputed exactly). Their two reproducibility flags
  on us are FAIR and fixed in this arc: B644 and B645 now carry
  ARTIFACT_HASHES.txt and hash-verifying locks; B645's no-prereg
  status stated explicitly in its FINDINGS.
- **Q1 (level 8):** 3/3 prediction-first — Z₈ = +1 (the prediction
  bank's first forward confirmation), clock = 60 equality (the clock
  law's second fresh-rung hit), √5-only import (the splitting law's
  third inert rung); sectors (0,+1); inert⟺even-sector 3/3 (NOTICED,
  denominator sealed).
- **Q2:** the k ≤ 2 anomaly zone **DISSOLVED** — every anomalous rung is
  abelian character factors (proven A₁-blind by ab computation) around
  a non-abelian core that keeps the law: SU(3)₂ = ρ_Fib ⊗ χ₄ exactly
  (the Fibonacci core carries clock 10); E₆ k=2 = χ₄ ⊠ χ₃ ⊠ the 3-dim
  of PSL(2,7) (clock = 4 = ord_{PSL(2,7)}(A₁), derived); P-Q2-a
  honestly refuted (no conductor drop anywhere). The split-prime kill
  identified as PSL-factoring — the k ≥ 3 mechanism candidate.
- **Q3:** **THE UNIFORM JUMP LAW** — the per-class jump is
  Π p^{min(v_p(κ),a_p)/2} over the fixed-point group's elementary
  divisors; 300/300 (rerun here); the sector decomposition (trivial +
  (r|5)-twist); PROOF_SKETCH with Lemma 1 cited-standard
  (Milgram/Wall/Scharlau — no novelty claimed), L2/L3 verified, and
  four honestly-labeled promotion targets.

## Cross-packet NOTICED (banked as one structural note)

**The disc(A₁) = 5 triple shadow:** three independent manifestations of
the same arithmetic — (1) the ear hears mod 5 (B644, the congruence
shadow); (2) the SU(3)₂ hearing block's non-abelian core is the
golden/icosahedral Fibonacci (Q2; κ = 5's simple group); (3) the
generic ladder silence is the character (κ|5) (N1-ERRATUM/Q3). One
discriminant, three organs. Registered as the leading mechanism input
for the calibration campaign's grammar table (which slots are
disc-forced). Second NOTICED: κ = 5 and κ = 14 hear their own
conductor's simple groups (2I and PSL(2,7) = GL(3,2)).

**DATED CORRECTION (2026-07-16, B651):** the first NOTICED row (the
inert⟺even-sector correlate, 3/3) **DIED at r = 23** — cc2's P4,
prediction-first kill under its own sealed prereg (baed2eed): 23 inert
predicted even-carried, observed (1, 0); r = 24 violates the converse.
The 3/3 was small-sample. The second-silence anatomy replaces it
(a cancellation, not a sector rule).

## Honest status

The heavy enumerations rest on the sending seat's sealed two-pipeline
identity (7/7 exact where cross-checked); this seat re-ran the decisive
deciders, the lemma battery, the lock file, and the spot-checks above.
Novelty on all law-shaped statements NEEDS-SPECIALIST (their lit-gate
notes adopted; Lemma 1 explicitly cited-standard). No SM numbers; Gate
5 untouched; no physics readings.
