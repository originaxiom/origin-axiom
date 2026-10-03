# B1528 — GENESIS v1.8: MAIN'S v1.7 AS THE HEAD, ITS ONE CORRECTED SENTENCE MADE EXACT (A MERIDIAN TWIST ENTERS SQUARED; P FIXES BALLAS' FAMILY), AND sL-10 ITEM 8 RECORDED AS ANSWERED

**Date:** 2026-10-03. **Verdict: PROVED.** Six checks, C1–C6 (`verification/genesis_v18_checks.py`, about 100 s), all pass.
- C1–C5 were run and passed before GENESIS.md was written. The pre-write log is kept (`genesis_v18_checks_prewrite_run.txt`).
- The run after writing (`genesis_v18_checks_run.txt`, `genesis_v18_checks.json`) adds C6: GENESIS.md is the generator's
  output, byte for byte, with its four [v1.8] marks.

**Not sealed.** Each check reads a banked record, re-derives a fact a record states, or compares texts. No open outcome is
computed. **creates_law is false.** 0 of 19 Standard-Model parameters; I-26 stays UNEARNED.

**Source.**
- **Main's ask.** Its relay of 2026-10-03 (`CC_TO_SM_AND_CODEX_2026-10-03_YOUR_SIX_ARCS_HARVESTED_GENESIS_V1_7.md`, main's
  B1462, kept as received in `received/`): *"Please take v1.7 as head"*.
- **The owner's two decisions** (main's B1460) are unchanged: GENESIS FK1 CONFIRMED as written; GENESIS FK12 framed as the
  register question.
- **The owner's instruction of 2026-10-02**, still binding: nothing load-bearing ignored, the experiential question included.
  It stays in GENESIS FK12 under Gate 5-Q, kept apart from the register question; nothing here bears on it.

## Seen first (the repo sweep and the literature)

**The repo sweep**, before any GENESIS text was written.
- `git fetch --all` at sm:B1527's bank: main had moved to `7ccae5a2` (S45, B1462). The other heads had not moved. None was
  merged.
- **Main's B1462**, read in full: FINDINGS, `adoption/amend.py`, its received copy of this seat's v1.6, its relay.
  - Main's received v1.6 is byte-identical to this branch's GENESIS.md at `df3f809b` (sha-256 `59ef40a6…`).
  - Main's v1.7 is that text with exactly the changes its amend.py lists: the version line, one intro sentence, FK12 (ii)'s
    sentence on P, the v1.7 log entry, and one path written in prose (C1).
- **Main's B1459**, read for the sentence main corrected. Its theorem (§1): for V = ρ_ℓ ⊗ ρ_η ⊗ χ, with SL(2) factors
  irreducible on the fibre and χ a fibre character, ι̃*V ≅ V* ⊗ ε. The sign ε comes from Schur's lemma on each SL(2)
  factor's own meridian. These modules carry no further twist on the meridian.
- **Main's B1462 §1–2**: P fixes ρ_q, the strong inversion dualises it; on the levels, "for ε = +1 the free part forces
  ∣λ∣ = 1". Both bear on the sentence and agree with C2–C3 below.
- `scripts/checks/prior_work.py` ran on six terms: "GENESIS v1.8", "Version 1.8", "meridian sign", "take v1.7 as head",
  "not self-dual", "rotoreflection". The first two are on no head. The others hit B1459, B1462, the GENESIS versions and
  sm:B1279, all read as above.

**The literature:** none bears. Every item is a statement about the record's own texts, or a finite computation on m004's
complete point and Ballas' family, both already on the record (sm:B1527's libraries, Ballas arXiv:1805.09274 as cited
there).

## 1. What v1.8 is

Main's v1.7, kept as received, with four marked additions and a log entry (`verification/merge_genesis_v18.py`; every change
an exact string of the received text, asserted to occur once):
- **the version line and one intro sentence**;
- **GENESIS FK12 (ii)**: main's [v1.7] sentence on P, made exact (§3);
- **GENESIS FK9**: sL-10 item 8 recorded as answered near the hyperbolic point (sm:B1527); its open remainder is item 9;
- **§8's frontier**: the same, with what stays open there;
- **§10**: the v1.8 log entry, with main's offered remark answered (§4).

Nothing of main's v1.7 is deleted or reworded. No status changes: GENESIS FK1 and FK12 stay as the owner decided.

## 2. The checks

| | check | result |
|---|---|---|
| C1 | main's amend.py, run on this branch's v1.6, gives main's v1.7 | byte for byte (4 changes, 1 path relabel); main's received v1.6 is this branch's |
| C2 | P at m004's complete point (+LR, own code) | P = (a ↦ A, b ↦ B, t ↦ bab·t), the only extension word to length 6; P fixes ρ_hyp; P*V ≅ V* ⊗ (t ↦ λ²) at all six λ tested; a sign only at λ = 1, −1, i |
| C3 | P on Ballas' family (q = 2, and q = 1 as control) | P fixes ρ_q; ρ_2 is not self-dual (character gap 14.3), so P does not carry it to its dual; ρ_1 is self-dual |
| C4 | main's remark on the order-four symmetries | sm:B1279's two rotoreflections square to the period-2 swap T and have order four on the cusp torus |
| C5 | sm:B1527 as v1.8 cites it | PROVED; T-THE-CUSP-DECIDES; kill record, reach class; sL-10 item 9 registered |
| C6 | GENESIS.md after writing | the generator's output, byte for byte; four [v1.8] marks |

Isomorphism in C2–C3 is read from characters: the traces of every word up to length 4 in a, b, t and their inverses agree
to 10⁻⁴⁰ at 60 digits, or differ on some word by more than 10⁻⁶. Every case fell on one side or the other. Both
representations are checked to satisfy the relators, ρ ∘ P included.

## 3. GENESIS FK12 (ii), made exact

- **Main's v1.7 sentence:** "the fibre's period-2 involution P carries a module to its dual up to a meridian sign — it
  reverses the order by itself, and followed by dualising it fixes the module (B1297; [v1.7] main's B1459 …)". In B1459's
  scope this is right, and it corrects the earlier wording, which this seat had carried since v1.3.
- **Why the sign is special.** B1459's modules carry no twist on the meridian, and the sign is the SL(2) factors' own. A
  twist t ↦ λ is inverted by dualising but kept by P, which preserves the meridian. So it enters squared.
  - C2, at m004's complete point: P*(ρ_hyp ⊗ (t ↦ λ)) ≅ (ρ_hyp ⊗ (t ↦ λ))* ⊗ (t ↦ λ²), for all six λ tested.
  - So P carries V to its dual up to a sign exactly when λ² = ±1. For a generic twist it does not.
  - This agrees with main's B1462 §2: for a count-odd map with ε = +1, "the free part forces ∣λ∣ = 1".
- **On Ballas' family P is not a dualising map.** P fixes ρ_q (main's B1462 §1; sm:B1526 C3). For q ≠ 1, ρ_q is not self-dual
  (C3: character gap 14.3 at q = 2), so P does not carry it to its dual. There the dualising symmetry is the strong inversion,
  as GENESIS FK9 already says.
- **v1.8 adds, after main's parenthesis:** "that sign is the SL(2) factors' own, for modules with no meridian twist, as in
  B1459; a meridian twist t ↦ λ enters squared: at m004's complete point, for V = ρ_hyp twisted by t ↦ λ,
  P*V ≅ V* ⊗ (t ↦ λ²), so P carries V to its dual up to a sign exactly when λ² = ±1; and on Ballas' family P fixes ρ_q,
  which is not self-dual for q ≠ 1, so P does not carry it to its dual (sm:B1528 C2–C3, own code)".
- Nothing of main's sentence is withdrawn. Its scope is stated.

## 4. Main's offered remark

Main's relay: "the four orientation-reversing classes act on T₂ = ℤ/5 as ×2 or ×3 — order four — which is the figure-eight's
amphichirality realised by an order-four symmetry whose square is P. Your B1279 may already say this".
- sm:B1279 §1 has the two rotoreflections, of order four, with cusp maps (μ, λ) ↦ (−μ, λ) + (½, ¼) and + (½, ¾).
- C4 composes them exactly: each squares to (μ, λ) + (0, ½). That is the period-2 swap T of the same table, which is P (main's
  B1462 §1; sm:B1521 C1). So an order-four symmetry whose square is P is on the record in sm:B1279's table, though the square
  was not stated there.
- sm:B1279's other two orientation-reversing classes, the glide involutions, have order two on m004. Their lifts to the
  levels square to the deck transformation (sm:B1279 §3).
- The action of the four classes on M₂'s ℤ/5 is main's computation. It was not computed here, so main's "order four" for all
  four classes is read, not checked.

## 5. sL-10 item 8 in GENESIS

- **GENESIS FK9** asked whether a vacuum of a mirror-broken word state's family is count-carrying near the hyperbolic point:
  "Whether it is nonzero is the SM seat's sL-10 item 8, sealed first".
- v1.8 records sm:B1527's answer: near the hyperbolic point, in finite volume (cusp types 0 and 1), no vacuum ν ⊗ ρ or
  ν ⊗ Λ²ρ has a non-zero index, on every word state to length 12, mirror-broken or not.
- §8's frontier keeps what stays open there: the eigenvalue-one locus of the infinite-volume part (sL-10 item 9), the
  non-split extensions, and the deformations far from the hyperbolic point.
- Main's L242 (e), a blind second route on ±LLRLRR and ±L³RLR², is answered in sm:B1527's relay: the seal was pushed before
  main's relay, and the sixty type-one points are exported without readings.

## 6. The locks

- `tests/test_b1528_genesis_v18.py`: the received texts by sha-256; GENESIS.md as the generator's output; the record; C2–C4
  live; v1.8's text; Gate 5-Q, vendor words and the private term; the ledgers.
- **B1526's lock, repointed.** It read v1.6 from GENESIS.md. v1.6 is kept byte-identical in this arc's `received/`
  (`GENESIS_v1_6_sm.md`, sha-256 `59ef40a6…`, the text main received), and the tests that read v1.6 read it there. This is
  B1526's own pattern for B1525's lock. The README test accepts v1.6 or v1.8.

## 7. What this arc does not do

- It does not re-derive main's B1459 or B1462. It reads them, and checks the corrected sentence's content where it bears.
- It changes no status in GENESIS. FK1 and FK12 stay as the owner decided.
- **0 of 19.** I-26 stays UNEARNED.

## Files

- `received/`: `GENESIS_v1_7_main.md` (main's GENESIS.md at `7ccae5a2`), `GENESIS_v1_6_sm.md` (this branch's v1.6, the text
  main received), `CC_TO_SM_AND_CODEX_2026-10-03_YOUR_SIX_ARCS_HARVESTED_GENESIS_V1_7.md` (main's relay).
- `verification/`: `genesis_v18_checks.py` (`genesis_v18_checks.json`, `genesis_v18_checks_prewrite_run.txt`,
  `genesis_v18_checks_run.txt`), `merge_genesis_v18.py`.
- Lock: `tests/test_b1528_genesis_v18.py`.
