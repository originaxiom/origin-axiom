# B1602 — THE FORCED COVER ON EVERY THREAD: on the 74 signed threads to length eight the common point's cover carries members of the four on ±LR and on one more odd-trace thread, −LLRLRLRR, whose member counts the floor's value (+3, +1) with four live ends — and on 17 of 42 even-trace threads, not all; neither the ±LR exclusivity nor the even-trace genericity survives

**Verdict: NEGATIVE as sealed** (T2 and T3 fail; T1 holds; T4 half) — scoped to the forced covers at sign characters;
a weave result (every thread under the rule, none chosen). cc (main), 2026-10-07. Sealed `fee144f6b` before any thread
of length six to eight was read. The surprise is a carrier: the first odd-trace thread beyond ±LR with content on its
forced cover, found by the rule. No physical quantity; no three. **0 of 19.**

**Credit.** The SM seat's W6 census for the question and the two kinds of content it named on ±LR; its W7 for the
even-trace states whose symmetry exchanges a pair of parities (±LLR, ±LLLLR, ±LLRR), which are among the carriers
here; B1492 for the stacked index and B1545's floor (the seat's) for the value the new carrier takes.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /forced cover|A4 cover|tetrahedral cover|congruence cover|sign character|interior class|member/: 94 of 1374 arcs on main match (NEGATIVE 17, OPEN 4, PROVED 72, RETRACTED 1)`
— B1600, B1601, B1492–B1494; the seat's complete W6 census and its W7. Seen before the seal: ±LR, ±LLLR, +LLRR,
+LLR (the preregistration). The hypothesis "content ⟺ arithmetic" was killed before the seal by +LLR. **Literature:**
Johnson–Millson bending and Bader–Fisher–Miller–Stover were named as a candidate mechanism, not used.

## 1. The census (`census_8.jsonl`, `summary.json`; 74 threads, 10,142 s)

W3's cover on each thread — A₄ for the 32 odd-trace threads (one kernel each, 4 cusps), D₄ for the 26 fixing one
parity (two kernels, 2 or 4 cusps), V₄ for the 16 fixing all three (four kernels) — and the four at every sign character.

| | sealed prediction | prior | result |
|---|---|---|---|
| **T1** | the eight odd-trace threads of length six carry nothing | 85% | **HOLDS** 8/8 (±LLLLLR, ±LLLRLR, ±LLLRRR, ±LLRLRR) |
| **T2** | the twenty odd-trace threads of length eight carry nothing | 60% | **FAILS at one**: **−LLRLRLRR** (trace −39; H₁ = ℤ ⊕ ℤ/41; its cover H₁ = ℤ⁴ ⊕ ℤ/19 ⊕ ℤ/779, 4 cusps) carries one member among its 16 sign characters, at ν = (−1, 1, 1, 1, 1, 1), of shape (h¹, r¹, n) = (4, 3, 1) — one interior class beside three that reach the cusps. Its sign twin +LLRLRLRR carries nothing (64 characters). The other 18 carry nothing |
| **T3** | every even-trace thread carries on some forced kernel | 55% | **FAILS**: 17 of 42 carry, 25 do not. Carriers: the V₄ threads ±LLRR, ±LLLLRR, ±LLLLLLRR; the D₄ threads ±LLR, ±LLLLR, ±LLLLLLR, ±LLLRR, ±LLLLLRR and +LLLRLLR. Non-carriers: every even-trace thread of three or more syllables but +LLLRLLR (±LLRLR, ±LLLLRLR, ±LLLRLRR, ±LLLRRLR, ±LLRLLRR, ±LLRLRLR, ±LLLLRLLR, ±LLLRLRLR, ±LLLRRLRR, ±LLRLRRLR, −LLLRLLR) and the two-syllable ±LLLLRRR, ±LLLLRRRR |
| **T4** | no odd-trace thread but ±LR has an interior class of the four at the trivial character; at least half the even ones do | 60% | **first half HOLDS** (no odd-trace thread has one — ±LR included); **second half FAILS**: 8 of 42 (19%): ±LLR, ±LLRR, ±LLLLR, ±LLLLLLR, the shortest |

## 2. The new carrier, read (`read_carrier.py`; post-census, disclosed)

At the member of −LLRLRLRR's cover the extension W₁ by its interior class reads **(I(W₁), I(Λ²W₁)) = (+3, +1)**. The
class is alive on all four cusps and the character trivial on none (m_A = 0, k = 4, b0 = 1), so the seat's floor
I(W₁) ≥ k − m_A − b0 = 3 is attained exactly: **the value is the ends'**, the floor's, as B1492 saw the ends raise the
floor on the companions — there the value did not follow; here it does, on a cover the weave forces. It is not
generation-shaped (the 5̄′ side reads 1, not 3). The controls by the same script: +LR's members read (−1, −1) dead on
every cusp (the seat's generation shape), −LR's four interior classes read (0, −3) dead on every cusp (members without
generations, as the seat's W6 has it). Three kinds of content on the forced covers are now on the record: +LR's
(−1, −1), −LR's (0, −3) and −LLRLRLRR's (+3, +1).

What the carrier shares with ±LR, checked as the reading rule asked: B1601's ideal has norm 3 on it as on every
odd-trace thread, and 3 **ramifies** in its trace field (e = 2) as in LR's — but so it does on LLLRRR, LLRLRR,
LLLLLLLR and LLLRLRRR, which carry nothing; so ramification is not it. The sign: −LLRLRLRR is the twin W9's hand rule
calls chiral (n_L − n_R + 2[−] ≡ 2 mod 4), as −LR is; +LR, the vector-like twin, carries too, so the hand rule is not
it either on its own. No rule is claimed; the carrier is named.

## 3. What it says

- The ±LR exclusivity the seat's census found to length six does not hold at length eight: content on the forced A₄
  cover is rare on odd trace (3 of 32 threads) and not unique to the root's pair. Theorem G's three-or-nothing makes it
  rare; what lets ±LR and −LLRLRLRR through is open.
- Even-trace content is not generic: 17 of 42. The carriers are the two-syllable words L^k R and L^k R² with small
  exponents and the V₄ words L^{2k}R²; every word of three or more syllables but one carries nothing. The seat's W7 states
  (±LLR, ±LLLLR, ±LLRR) are carriers here too, by a different instrument.
- Interior classes of the four at the trivial character — the four's own room — appear only on the shortest even
  threads and on no odd-trace thread at all.
- Nothing here counts three; the owner's "did we derive three" stays no.

## 4. Disclosed

- The instrument is unchanged after the seal (the sealed hash on `ARTIFACT_HASHES.txt`); the census ran as four
  parallel workers over disjoint thread lists (`worker_*_run.txt`), assembled by `summary.py`.
- `read_carrier.py` (the count at the carrier's member, the ±LR controls) was written and run after the census,
  outside the sealed cells; its readings are B1492's instrument as banked.
- Every kernel of the forced type is read; the sign and choice variants of the extension are among them (not located
  in SnapPy's generators). Ranks numerical at 40 digits. Sign characters only. SnapPy's `b+-w` is the −w thread.
- The seat's W7 lists ±LLRR, ±LLR, ±LLLLR but not ±LLLRR, ±LLLLLLR, ±LLLLLRR, which carry here: the instruments differ
  (its resolving ticks, these forced covers) and the difference is recorded, not resolved.
- Not blind to the seat's census, to B1601 or to the six threads seen before the seal.

## 5. Files

`verification/forced_every.py` (sealed), `summary.py`, `read_carrier.py`, `census_8.jsonl`, `summary.json`, the 74
`forced_<thread>.json`, `read_*.json`, the run logs; `adoption/amend.py` (GENESIS v1.26, with the WM renaming).
Test: `tests/test_b1602_the_forced_cover_on_every_thread.py`.
