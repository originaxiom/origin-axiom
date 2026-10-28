# B1792 — THE OFFSET RECURRENCE AT ORDER 60: R_a FAILS, R_b HOLDS — EVERY CARRIER AT ORDER 60 IS A +1/3 SHIFT OF AN ORDER-20 CARRIER AND NO OTHER LINE CARRIES, BUT ONE PREDICTED MIRROR PAIR (1/60 ↔ 7/12) DOES NOT CARRY; THE RECURRENCE IS A NECESSARY CONDITION, NOT A RULE — THE LEPTONS ARE EXACTLY SHIFT-INVARIANT, THE QUARKS ONLY APPROXIMATELY, AND m_u/m_t BREAKS THE PAIR

**Verdict: NEGATIVE for the sealed prediction R** (exact recurrence; R_a fails), **with R_b holding.** A READING, no grade
sought, as the seal stated. cc (main), 2026-10-28, the SM seat's W164 prediction (P-399), sealed and run by main at the
seat's word. The record:
- **sealed** 096c97e94;
- **census** 1741ae6ba;
- **the instrument's one-line fix** be216a281, after the first launch failed before any value;
- **comparison** 38c4a3bd6.

Each output was committed unread, then read once. **0 of 19.**

## 1. The cells, as sealed (`verification/compare_run.txt`, `comparison.json`)

| cell | prediction | outcome |
|---|---|---|
| **R_a, decisive** | every one of the eight predicted lines carries the six | **FAILS**: six carry. 47/60 ↔ 49/60 at 10.70, 7/60 ↔ 29/60 at 12.46, 41/60 ↔ 11/12 at 13.78. The pair 1/60 ↔ 7/12 does not (36.34) |
| **R_b, decisive** | none of the other twelve lines carries | **HOLDS**: the twelve's least is 19.97 (1/12 ↔ 31/60) |
| C1 | B1741's best row and B1755's rows on its order-20 carriers to 10⁻⁹; the T-law at order 60 to 10⁻⁶; twenty lines of exact order 60 | **holds** (0.0, 0.0, 3.2 × 10⁻¹¹, exact) |
| C2 | B1735's 3.0945633 | **holds** |

**Read-outs:**
- **The best row:** (2/5, 49/60) and its mirror, at Im τ 3.0375, the same strip point as at every order tested.
- **The predicted class:** 0.060% of random hierarchies reach as low (96 of 160 000, seeds 4501–4540). This figure reflects
  the pair 47/60 ↔ 49/60 alone, not the class (§ 3).

## 2. What it shows

- **The recurrence holds as a necessary condition.** Every line that carries the six at order 60 is a +1/3 or +2/3 shift
  of an order-20 carrier, and no other line carries.
- **It is not a rule.** One predicted pair fails robustly:
  - the pair's best row is 36.34, 2.2 times the bar (the next two rows 36.77 and 39.40; on L₂ 99.75);
  - the failing pair is the +2/3 shift of 7/20 and the +1/3 shift of 1/4. The other shift of each base carries.
- **The mechanism** (the referee, `verification/referee/`):
  - **The leptons are exactly shift-invariant.** Their charges (−3, 6) are multiples of 3, so w → w + 1/3 leaves their
    twists unchanged mod 1. Their ratios agree to 10⁻¹⁰ at every order step.
  - **The quarks are not exactly invariant.** Their charges 1, −4, 2 move their twists by q/3. Even where the recurrence
    held (10 → 30; the shifts of 3/20 and 9/20), their ratios move by up to 0.79 in log, about 4σ.
  - **On 7/20 → 1/60 the move is one ratio.** m_u/m_t moves by +1.45 to +1.83 in log at all seven strip apexes, about
    9σ; the down ratios move by at most 0.24.
  - **A direct comparison.** At 41/60's best apex, 1/60 has the same 3 Re w mod 1 and the same lepton part (7.27), yet
    gives 63.86: its m_u/m_t term is 52.50, against 2.18 for 41/60.
  - **At 5 → 15** the base lines themselves (0 and 3/5) do not carry (27.02), while both shifts do (9.17, 5.33).
- **So "the six nearly a function of 3 Re w"** (W164's post hoc phrase, the seal's Why) was already false on the record
  before the seal. Correctly stated: **the leptons exactly, the quarks approximately.** The offsets that carry are those
  where the quark part, not shift-invariant, stays inside the bar.

## 3. The odds and THE_BAR

- **A mirror-respecting null** with exactly three carrying pairs placed uniformly among ten: they fall inside the
  predicted four with probability C(4,3)/C(10,3) = 4/120 = 3.3%.
- **The base-rate null** (at every order from 10 to 30 exactly 40% of the slope-2/5 lines carry, 22 of 55; pairs treated
  as independent):
  - P(R_b) = 4.7%;
  - P(R_a) = 2.6%;
  - P(R) = 0.12%;
  - "R_b and at least three of four" = 0.84%, an event defined after the fact.
- **None of these comes near THE_BAR** at the ledger's m. As sealed, this is a structural check with no grade sought.
- **The 0.060% specificity read-out** comes from the 47/60 ↔ 49/60 pair alone:
  - in the random-subset control, 63 of the 210 mirror-respecting 4-pair classes reach as low;
  - every class containing that pair sits at 0.045–0.069%;
  - all 210 classes are under 1%.

## 4. The reading, against the one written before the run

**The pre-written branch for "R_a fails" applies:** the near-invariance under w → w + 1/3 breaks at order 60, because
the quark twists move.

**Its clause "a low-order coincidence" overreaches,** since R_b held. Post hoc, labelled: the recurrence still bounds
where the carriers can be — every carrier is a shift of a lower-order carrier. What it cannot say is which shifts carry.
That depends on the quark ratios, chiefly m_u/m_t.

**For the offset question (P-384, P-399):**
- the offset's role splits by sector: the leptons see it only through 3 Re w, and the quarks see it directly;
- an offset rule would have to come from the quark sector's twists, not from the Higgs's.
- **No input removed.**

## 5. The referee (hostile, read-only; `audit/referee_b1792/`, scripts kept in `verification/referee/`)

1. **NOTE, custody clean:**
   - every hash matches; the fix is exactly one line and changes no arithmetic;
   - the failed launch died before any χ²;
   - the census is unchanged;
   - an independent re-implementation (no B1741 import) reproduces all twenty per-line minima to ≤ 6 × 10⁻¹² and the
     class hits exactly.
2. **NOTE:** the failing pair is a robust fail, not a near miss.
3. **CORRECTION, applied:** the mechanism (§ 2).
4. **CORRECTION, applied:** the 0.060% is the 47/60 ↔ 49/60 pair's (§ 3).
5. **NOTE, applied:** the odds under the base-rate null.
6. **CORRECTION, applied:** "a low-order coincidence" is qualified (§ 4).
7. **NOTE:**
   - the seeds 4501–4540 are used by no other instrument;
   - the mirror is exact at every paired apex;
   - the unequal pairs 13/60 ↔ 23/60 and 43/60 ↔ 53/60 differ only through the Re τ = 0 apex (0, 3.1623);
   - the test is in sample in τ (the same seven strip apexes at every order) and out of sample in b only (disclosed).

## Seen first

As in the PREREGISTRATION:
`VERDICT topic-sweep /offset|recurrence|order 60|3 Re w|carrier|P-399|W164/ (full text): 143 of 1539 arcs on main match (NEGATIVE 20, OPEN 12, PROVED 110, RETRACTED 1); 12 register rows match (DONE 3, QUEUED 9)`.
**Literature:** none bears on this frame's offsets.

## Files

- **The seal:** `PREREGISTRATION.md`; `ARTIFACT_HASHES.txt` (the sealed hashes, and the fixed compare.py's under a dated
  note).
- **The instruments and their outputs:**
  - `verification/census.py` → `census.jsonl`, `control.json`, `census_run.txt`;
  - `verification/compare.py` → `comparison.json`, `compare_run.txt`, with `compare_run_failed_launch.txt`.
- **`verification/referee/`:** its intermediates are regenerable.

The lock: `tests/test_b1792_the_offset_recurrence_at_order_60.py`.
