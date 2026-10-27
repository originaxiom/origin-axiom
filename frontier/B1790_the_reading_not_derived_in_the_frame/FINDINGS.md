# B1790 — THE READING IS NOT DERIVED IN B1656'S FRAME (MAIN'S PLAN, STEP 3; DATA-FREE): EVERY MAP OF (τ, w) ON RECORD PRESERVES BOTH READINGS, SO THE EIGHT READING ASSIGNMENTS ARE PHYSICALLY DISTINCT AND THE GLOBAL FLIP IS NOT A CONVENTION; AN IMPORTED HYPERCHARGE SIGN RULE (AN UNEARNED IDENTIFICATION) WOULD REDUCE THE READING TO ONE BIT, AND THAT BIT IS GENUINE

**Verdict: NEGATIVE (frame-scoped).** In B1656's point coupling with the record's Higgs DR, the reading (up S̃,
down S, leptons S; S̃ = εS*εᵀ) is not forced. The study is data-free. cc (main), 2026-10-28, step 3 of main's plan
(docs/MAINS_PLAN.md, P-393; P-394 with P-295, P-365). Corrected before landing at its hostile referee (§ 5).
**0 of 19.**

## 1. What the record holds

- **The readings:** they are covariant, and S* is excluded (B1724, P-297). S̃ is S with conjugated components.
- **No doublet index:** the frame carries no electroweak doublet index (P-365). The Standard Model's H̃ was identified by
  hand (B1660).
- **B1744 (P-324, NEGATIVE):** the Higgs at its own hypercharge twist ±3w fails inside the point coupling. The residue
  quaternion is even, T0(3w) = T0(−3w), so H_u = H_d and the charge sign is erased.
- **B1739 (P-344):** at hierarchy-scale Im τ, with the record's nearly null Higgs, a split reading misaligns the light
  states. So the six's reading and an unmixed light generation exclude each other there.
- **B1726:** the six's specificity is similar under every covariant reading assignment. The reading matters for the nine.
- **B1742's pairs:** F₆/F₂₂ both read S, a third route besides the two below.

## 2. The mechanism and why the frame does not force it

**The hypercharge sign rule.** Each sector's net charge is q_L + q_R: up −3, down +3, leptons +3. A single-valued
coupling would pair up with the Higgs of one sign and down and leptons with the other. That is the Standard Model's
pattern, up opposite to down and leptons.

**Why nothing in the frame forces it** (the referee's structural argument, adopted):
- The coupling is complex-bilinear in the Higgs components and the matter weights.
- Both are holomorphic in τ, up to real norms.
- So every moduli map acts on the Higgs and the matter alike and cannot conjugate one relative to the other. S̃ needs
  exactly such a relative conjugation.

**Supporting computations** (`verification/referee/`):
- **The maps:** seven maps of (τ, w) on record preserve both readings to ≤ 7 × 10⁻¹². They are the mirror
  (τ, α, b) → (1 − τ̄, α, −α − b), τ → −τ̄, w → −w, w → w̄, the T-step, w → w + 1 and w → w + τ (`maps.py`). Half-periods are
  not symmetries. The modular S step is covered by B1724.
- **No flip partner on the lines:** a search over all 266 lines at τ = 0.35 + 2.9i and 0.5 + 2.9i finds no line whose
  spectrum under the flipped assignment matches the source's (best 1.52 in ln). The control finds the source at 0 and its
  mirror partner at 5 × 10⁻¹² (`flip_search.py`).
- **No slope with matching exponents:** no slope with denominator ≤ 60 has flipped leading exponents equal to (S̃, S, S)'s
  at 2/5 (`exponents.py`).
- **The identity behind S̃** (exact; `identity.py`, and the draft's `mirror.py`): conj(av_k(τ)) = av_k(−τ̄) for the I and J
  components and −av_K(−τ̄) for K.
  - The I and J coefficients are real, the K coefficient imaginary.
  - te.ev matches an independent jtheta evaluation to 10⁻³⁰ at three points.
  - Negating K is −Q_K S Q_K⁻¹, a proper rotation up to sign, not an orientation reversal. The mirror modulus −τ̄ here
    differs from the mirror map's 1 − τ̄ by ρ(T).
  - The identity needs a Higgs with this real structure. E₄R + iD²R breaks it at 2 × 10⁻² (`complex_higgs.py`).
- **Same-point differences** (`same_point.py`): the S/S̃ difference at a point and its mirror image agree to ≤ 2 × 10⁻¹¹.
  Per sector it ranges from 0.074 (up, (2/5, 3/10)) to 7.7 in ln.

**So the eight assignments are physically distinct, and the global flip (S̃, S, S) ↔ (S, S̃, S̃) is not a convention.**

## 3. Where the reading shows up (`reading_exponents.py`, `referee/exponents.py`; B1788's closed form)

- **On α = 2/5,** the second-generation exponent is reading-blind (B1788), and the reading moves the first:
  - up m₁/m₃: ½ under S, 4/5 under S̃ (B1788's 40-digit runs: 0.5000 and 0.8001);
  - down and leptons: 11/20 under S, 13/20 under S̃.
- **On other slopes this does not generalise.** At leading order the reading leaves m₁/m₃ unchanged on 7 slopes for up
  (1/10 and 3/10 among them), 3 for down and 9 for leptons, out of 1 102.
- **At finite height it moves more.** At Im τ ≈ 3, up's m₂/m₃ moves by a factor of 2.5–4 between readings. The frame
  gives about 900 for up's m₁/m₃ ratio at (2/5, 1/10), Im τ = 3, against the leading-order estimate of about 300.
- **The mixing depends on the reading** (B1739).

## 4. What is forced and what is chosen

- **Forced by nothing in the frame:** which sectors read S̃.
- **Reduced only by an import.** Adopting the hypercharge sign rule takes the reading from 3 bits (eight assignments) to
  1 bit (two). But it identifies the reading with the Higgs's charge sign, which the frame does not act on (B1744). That
  is an **UNEARNED identification** (IDENTIFICATION_LEDGER I-35), and this arc does not adopt it.
- **The remaining bit is genuine.** No symmetry exchanges the two signs (§ 2). The data's preference for up S̃ fixed it,
  post hoc.
- **Do not seal a test of the sign rule on the six.** It allows two assignments out of eight, a 1-in-4 chance, and the
  six's specificity is nearly reading-blind (B1726).
- **A derivation needs something the frame lacks:** an antiholomorphic or Hermitian Higgs slot (W59's Hermitian pairing,
  P-097), a non-point coupling, or an effective-action selection. Two holomorphic Higgs objects cannot do it, since the
  split needs H_u = εH_d*εᵀ, which no two holomorphic sections satisfy.
- **The question for the SM seat:** does it hold an antiholomorphic or Hermitian Higgs slot? (Its pairs on record, B1742
  and P-370, are holomorphic and read S.)
- **No input removed.**

**Not examined:** complex-coefficient or twisted Higgs sections beyond B1744's, non-point couplings, and effective-action
selection.

## 5. The referee (hostile, read-only, before landing; `audit/referee_s226_reading/`, kept in `verification/referee/`)

1. **BLOCKING, applied: the draft's evidence did not test what it claimed.** It inferred "no frame symmetry flips the
   reading" from one map, and its "flipped" column only re-measured the same-point S/S̃ difference (equal to ≤ 2e-11).
   Replaced by the structural argument and the computations in § 2.
2. **CORRECTION, applied:** "1.8–7.7" was a maximum over sectors; per sector the range starts at 0.074.
3. **CORRECTION, applied:** "the first generation carries the whole reading" holds on 2/5 only (§ 3).
4. **CORRECTION, applied:** the identity is exact; negating K is a rotation up to sign, not an orientation reversal; and
   the identity needs a real-structured Higgs.
5. **Citations checked**, and B1739's condition restored.
6. **CORRECTION, applied:** Seen first had missed B1742's F₆/F₂₂, P-370, P-383, W129, W131/W133 and W59's Hermitian
   pairing (P-097); the unexamined routes are now listed.
7. **CORRECTION, applied:** the 3 → 1 reduction is an unearned identification (I-35).
8. **CORRECTION, applied:** the draft's question to the SM seat (are its H_u and H_d mirror images?) was ill-posed, since
   the mirror preserves the readings. It is replaced by the slot question.

## Seen first

`VERDICT topic-sweep /reading rule|S tilde|conjugate Higgs|twisted Higgs|Higgs.s own twist|doublet index|P-295|P-365|P-394/ (full text): 34 of 1535 arcs on main match (NEGATIVE 9, PROVED 25); 15 register rows match (DONE 7, QUEUED 8)`.

Bearing on it:
- **Arcs:** B1660, B1691, B1724, B1726, B1739, B1742, B1744, B1786, B1788.
- **The register:** P-097, P-295, P-297, P-324, P-344, P-365, P-370, P-383, P-394.
- **The SM seat:** W59, W129, W131, W133.
- **Literature:** the holomorphic superpotential's need for two doublets (the MSSM's H_u, H_d) is the textbook analogue.
  Nothing on record derives a reading of this kind.

## Files

`verification/`:
- `mirror.py` → `mirror.json`; `reading_exponents.py` → `reading_exponents.json` (the draft).
- `referee/`:
  - `maps.py` → `maps.json`, `maps_run.txt`;
  - `flip_search.py` → `flip_search.json`, `flip_search_run.txt`;
  - `exponents.py` → `exponents.json`, `exponents_run.txt`;
  - `identity.py` → `identity_run.txt`;
  - `complex_higgs.py` → `complex_higgs_run.txt`;
  - `same_point.py` → `same_point_run.txt`;
  - `common.py`.

The lock: `tests/test_b1790_the_reading_not_derived_in_the_frame.py`.
