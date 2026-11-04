# Review 74: the cloud seat's 101 SCHEDULED harvest rows, read for load and for leads

*A reader for Review 74, 2026-11-04. Report only: no tracked file edited, nothing committed, no branch checked out.
Source: `docs/HARVEST_LEDGER.md` rows whose seat is `cloud seat` and whose disposition contains SCHEDULED (101 rows).
Items read with `git show e51afd6c:outside_bench/…` (the commit each row names). The branch is `origin/<v>/outside-bench`,
whose pin `13d2c5b6` descends from `e51afd6c`. The same files are on main under `outside_bench/` since the merge
`merged/outside-bench@8262c6ed` (2026-09-15). No `prescreen.json` existed, so I swept main myself:
`frontier/*/FINDINGS*.md`, `ADDENDUM*.md`, `docs/*.md` and `GENESIS.md` for each memo number, number range and file stem,
plus targeted greps listed per row. Firewall: no value, sign or bound for y_b/y_t, θ̄ or y_τ/y_b appears below. Nothing is
compared with data.*

## 0. The headline

1. **No game-changing lead is hidden in these 101 rows.** These are the cloud seat's memos 31–173, written between
   2026-08-25 and 2026-09-07. All of them predate the weave and the modular-flavour frame (B1600 onward, from 2026-10-07)
   in which every current open question is posed: the six ratios, D, the CKM–Higgs wall, the choice of τ, the towers and the
   gauge couplings.
   - Their physics is the August carrier frame (Ψ = ℂ²⊗27, the beat, E₆ kinematics), the observer-bit census, the
     Fricke-dynamics clocks, the cosmology ledger and the bench's own governance.
   - **None touches D, the six-ratio candidate, the CKM–Higgs wall, the selection of τ or the gauge couplings.**
2. **The strongest real lead is a cheap, data-free computation on the root.** Memos 61, 72, 76, 77 and 85 compute what
   discrete symmetry survives when the E₆ 27's only SM-preserving directions get vevs.
   - The answer is the SM's own ℤ/6 shadow plus 14 E₆ ℤ/2 gradings. None of them is a matter parity, and the ψ remnant
     is trivial.
   - This bears on GENESIS v1.12's "Computed nowhere yet: Dirac against Majorana … which no arc computes".
   - It also bears on THE_TOWERS § 8 and B1805's "still open in other frames: an E₆ meeting point".
   - All five certificates reproduce byte-for-byte on this bench (§ 1).
3. **Forty-one of the 101 rows are not unread at all.** Main reproduced, verified or adopted them in arcs that the
   generated slice-D grep (B1306) missed, or in later arcs that never moved the row: B1147, B1148, B1158, B1162, B1201,
   B1213, B1337, B1339, B1414, B1093, B496, B775/B778, B1117, B1193, and RELAY_LEDGER rows 121 and 126. The SCHEDULED
   count overstates the debt by about 40 % for this seat.
4. **Five items are owed checks, or correct a living statement on main** (§ 4):
   - GENESIS v1.12 and COSMOLOGY_LEDGER row 4 call memo 122 "unverified on main", although B1208's LEG 4 closed that row at
     character level on main's own code on 2026-08-29.
   - P-145 (memo 132).
   - P-317(b) (memo 143).
   - L173, the ★★★★ laboratory lead, still carries a 5-against-6 count that memos 144–147 call a detector artefact.
   - P-492 (memo 171's type-error reading of GC-6, which B1722's sealed W2 cell inherits).

## 1. Method and how much I read

- **Read in full or nearly in full:**
  - memos 31, 32, 36, 37, 59–67, 72, 74, 76, 77, 79, 83–103, 105, 106 and 108;
  - memos 132 and 168 (most of each);
  - memo 95 (its protocol and verdict table).
- **Read in part (head, then the mechanism or verdict section):**
  - memos 39, 40, 44, 58, 115–126, 131, 134–139, 142, 143, 148, 150–167, 171 and 173 (its retraction head note);
  - `Q1_REWRITE.md` (its structure and its Q1/Q2 sections).
- **Read at headline level only:**
  - memos 144–147: the opening and the mechanism paragraph, which is where each one's claim sits;
  - memos 109–114: the claim line, relying on B1201's byte-identical reproduction, which I read in
    `frontier/B1201_lee_verified_and_harvest/verification/cells.json`;
  - row 44, the relay: relying on B1305's FINDINGS_B.
- **Reproduced on this bench.** I ran the seat's code from a scratch copy with `python3 -I` and sympy 1.14.0. Each output
  matched the committed `outside_bench/outputs/*_out.txt` byte for byte:
  - `inflation_probe.py` (memo 132)
  - `dm_stability.py` (memo 122)
  - `breaking_chains.py` (memo 72)
  - `z2_census.py` (memo 76)
  - `psi_survival.py` (memo 77)
  - `script_chain.py` (memo 85)

  This is REPRODUCED grade (the seat's code), not VERIFIED. One point matters for B1162: the "deeper cloud stack" it gave
  as its reason to cite memo 72 rather than re-run it is `paper/verify/check_charge_bracket.py`. That file is on main, under
  `outside_bench/certificates/paper/verify/` and in B1147–B1150's `verification/`. The excuse no longer holds.
- **Numbering trap.** For rows 383–396 the ledger's memo numbers (taken from the INDEX) are one or two higher than the
  numbers printed in the files' own headers:
  - `LAW_DECLARATION_AUDIT.md` is row 383's "memo 134", but its header says memo 133, and B1213 cites it as memo 133;
  - `STRUCTURE_PROBE.md` is 135, header 134;
  - `L173_GAP_DETECTOR.md` through `GOLDEN_EXCESS_ENSEMBLE.md` are 144–147, headers 142–145.

  Rows 389 and 390 are one file (`Q1_REWRITE.md`; memo 141 is its Q2 section). Cite these items by file name.

## 2. The rows

Key: **A** = load (does main rest on it, or does it question a main result in use); **B** = lead; **C** = already handled.
"Retired frame" means the August carrier frame, the B928 sheet or the observer-bit census, which the weave era (B1600+)
and B1750's re-typing superseded and which no current debt names.

| row | item (≤ 25 words) | A | B | C | disposition |
|---|---|---|---|---|---|
| 44 | relay "Q1 is not open": colored-Jones ends, GM's c = ±1/24, "6 = 1 + 5" for L154 | no current load (σ/L154 line) | none beyond B1305 | B1305 FINDINGS_B: verified and verified-differs, banked. The row's disposition already reads BANKED; it is counted only because "SCHEDULED" survives in its "Was:" clause (`harvest_debt.py` l. 616 tests substring) | CLOSED-HANDLED (B1305 B) |
| 349 | memo 100: the longitude is a grammar word, baBAABab, giving cusp modulus 2√−3 and h(−48) = 2 | no | none; the cusp shape is banked (B486) and τ = the cusp shape was tested NEGATIVE (B1696) | B486 | CLOSED-NO-LOAD-NO-LEAD |
| 350 | memo 101: Fricke time-reversal R acts as the γ₅ Galois conjugation up to φ∓⁶; no banked involution swaps branches | no | none (retired observer-bit census) | — | CLOSED-NO-LOAD-NO-LEAD |
| 351 | memo 102: h(K) = 1 for the disc-6237 cubic field, with an explicit generator of norm 953 | no | none | **B1093 proved h(K) = 1 on main on 2026-08-20**, before the memo | CLOSED-HANDLED (B1093) |
| 352 | memo 103: h(K) = 1 re-proved by explicit generators below the Minkowski bound | no | none | B1093; B1337 used it as its first readable test | CLOSED-HANDLED (B1093) |
| 354 | memo 105: the tier-1 menu of 17 banked atoms has 11,720 values; denominator rule fixed before data | no | weak: a ready look-elsewhere denominator for closed-form matches in banked constants (not the frame fits of the current candidate) | — | CLOSED-NO-LOAD-NO-LEAD (see § 3, lead 5) |
| 355 | memo 106: κ − 2 = ω², ε selector-free, and the saddle equals the obstruction (Φ₃(κ−2) = 0) | no | none | B1200 verified Φ₃(κ−2) = 0 independently (uncredited); B1195's K1 | CLOSED-HANDLED (B1200, B1195) |
| 357 | memo 108: the mirror is the word automorphism a ↦ a, b ↦ ba⁻¹b⁻¹ | no | none | B1201 (read as memo 109's background); mirror = conjugation = c is B1174 and B1208 LEG 5 | CLOSED-HANDLED (B1201, B1174) |
| 358 | memo 109: the fence independence theorem | no | none | B1201 R52-2b: byte-identical | CLOSED-HANDLED (B1201) |
| 359 | memo 110: the mirror's kernel moves no magnitude and one sign | no | none | B1201: byte-identical | CLOSED-HANDLED (B1201) |
| 360 | memo 111: the one bit is spent once; the traces generate exactly ℤ[ω] | no | none | B1201: byte-identical | CLOSED-HANDLED (B1201) |
| 361 | memo 112: the occupant's type is forced; refutes the naive unit-norm law | no | none | B1201: an independent re-derivation of B1195/GC-24's refutation | CLOSED-HANDLED (B1201) |
| 362 | memo 113: the first beat law (traces are polynomials in (x, y, z); the second beat adds no invariant) | no | none | B1201: byte-identical; its GC-24 cross-link ruled vacuous; cited in B1203 | CLOSED-HANDLED (B1201) |
| 363 | memo 114: the pattern ladder (classes grow, values do not) | no | none | B1201: byte-identical | CLOSED-HANDLED (B1201) |
| 364 | memo 115: the owner's "shadow" predicate [X, gal X] ≠ 0 tested; its H2 fails | no | none (firewalled, H5) | — | CLOSED-NO-LOAD-NO-LEAD |
| 365 | memo 116: six admissible predicates; memo 115 downgraded | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 366 | memo 117: Thue–Morse layering adds structure, no information | no | none | **B496** (memo 121's own catch: a rediscovery) | CLOSED-HANDLED (B496) |
| 367 | memo 118: the layering map closes to (z, κ) and is not κ-preserving | no | none | B496's κ-factorization | CLOSED-HANDLED (B496) |
| 368 | memo 119: the trace maps' commutation table; L is the only κ-breaker; (RT)² = id | no | none | partly B496's Q1 | CLOSED-NO-LOAD-NO-LEAD |
| 369 | memo 120: the record has flows; only "the second" and the thermal arrow are missing | no | none (matches B716/B721) | — | CLOSED-NO-LOAD-NO-LEAD |
| 370 | memo 121: the bench caught itself re-deriving B496 uncited | no | none | points to B496 | CLOSED-HANDLED (B496) |
| 371 | memo 122: COSMOLOGY_LEDGER row 4 run; the root's forced gauge 2-torsion gives N1/N2 no stabiliser | **YES.** Cited in GENESIS v1.12 (l. 481, "unverified on main: row 371"), COSMOLOGY_LEDGER (l. 54 and § ROW 4, "never checked"), THE_FIFTH_FORCE_QUESTION, B1478's A5, and B1202's negative control (B1338 § 4) | none new | **B1208 LEG 4** verified the stronger census (memo 123) on main's own 27-weights, with an MB12 planted control: "row 4 closes at character level". Certificate reproduces here | **DEBT** (D1) |
| 373 | memo 124: the layer tower's level-1 coordinate is −(cusp modulus); real from level 2 on | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 374 | memo 125: PC04's residue is κ − 2 = ω² | no | none | B1195's K1; B1200 | CLOSED-HANDLED (B1195) |
| 375 | memo 126: kill_graph faces against atlas motifs: orthogonal axes, with a contingency table | no | none (process; could close a CHANGELOG blemish) | — | CLOSED-NO-LOAD-NO-LEAD |
| 380 | memo 131: LEAP-1's payment propagated through the bench's own documents | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 381 | memo 132: every tower map has Jacobian det −1, 0 or +1 identically, so "the object cannot inflate" | **YES.** P-145 (debt #31); B1202's inflation control false (B1338 § 4); COSMOLOGY_LEDGER row 2 "MISSING" | none | not verified on main; certificate reproduces here | **DEBT** (D2) |
| 383 | "memo 134" (header: memo 133) LAW_DECLARATION_AUDIT: `creates_law` empty on 89 % of the corpus | no | none | **B1213** verified it entry for entry ("harvests cloud memo 133") | CLOSED-HANDLED (B1213) |
| 384 | "memo 135" STRUCTURE_PROBE: cosmology rows 7/8 have exponential-class growth and no scale variable | weak: COSMOLOGY_LEDGER rows 7/8 still read "MISSING / never started" | none | — | **DEBT** (low; fold into P-145, D3) |
| 385 | "memo 136" θ-even designed crossing (the 27↔27̄ involution, not strong CP): not fireable, four pre-work items outstanding | no (old contact licensing, superseded by GENESIS v1.60–1.61) | none | B1217 read it | CLOSED-NO-LOAD-NO-LEAD |
| 386 | "memo 137": the mirror row's independent content is three values | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 387 | "memo 138" L173 seal path: J H J = H(reversed word) for any word, so isospectrality is an identity | no (see D5) | none | **B1414** recorded the clauses as word identities on L173 | CLOSED-HANDLED (B1414) |
| 388 | "memo 139": the send-queue readiness audit; Q1 stale by eight arcs | no; Q1's row on main (SPECIALIST_SEND_QUEUE l. 11) still carries the old status | none | — | CLOSED-NO-LOAD-NO-LEAD (process note) |
| 389 | "memo 140": Q1 rewritten (SEAM-A Gate 2) from B1198/B1201/B1209 | no | none | not adopted into the queue | CLOSED-NO-LOAD-NO-LEAD |
| 390 | "memo 141" (same file, Q2 section): Q2's staleness flag withdrawn | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 391 | "memo 142" (header 140): the lane's self-audit: 112 pairs, 0 failures, 1 drift | no | none (supports re-running the lane's certificates) | — | CLOSED-NO-LOAD-NO-LEAD |
| 392 | "memo 143" (header 141) V-NEG: the complex volume added to B1137's regulator basis; still no SM target involves a regulator | **YES.** P-317(b): B1137's PSLQ DISJOINT carries no information, and "B1217's V-NEG rests on it" | none | B1217 confirmed two sub-claims; the extended run is unreproducible as committed | **DEBT** (already inside P-317(b); D4) |
| 393 | "memo 144" (header 142): per-gap detector; the 6−5 remainder is a one-ended-detector artefact | **YES**: L173 (OPEN_LEADS l. 1922, ★★★★) still carries "5-vs-6 at ρ = α" | — | not on main (B1414 recorded only the clause identity) | **DEBT** (D5) |
| 394 | "memo 145" (header 143): reversal forces every two-ended count to tie (H_L = J H_R J) | YES, as above | — | not on main | **DEBT** (D5) |
| 395 | "memo 146" (header 144): the odd-index exception is real but generic to every Sturmian slope | YES, as above | — | not on main | **DEBT** (D5) |
| 396 | "memo 147" (header 145): the golden excess is a Fibonacci-window confound; closed negatively | YES, as above | — | not on main | **DEBT** (D5) |
| 397 | memo 148: the hostile read of P3 (six defects, mathematics intact) | no (P3 superseded by P9) | none | RELAY_LEDGER row 121 (accepted in full); `papers/P3_THE_PAPER/SPEC.md` l. 277 | CLOSED-HANDLED |
| 399 | memo 150: the paper-chain synthesis of memos 148–149 | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 400 | memo 151: Route A was tracked (L169) but absent from the send queue | no | none | **B1339** drafted Q7 into the queue | CLOSED-HANDLED (B1339) |
| 401 | memo 152: THE CHAIN, LINK BY LINK: what we do not have, in order | yes, as a living document | none | **ADOPTED by B1339** as `docs/THE_CHAIN_STATUS.md`, with a currency pass | CLOSED-HANDLED (B1339) |
| 402 | memo 153: currency pass on the bench's own gap documents (it adopted main's `already_banked.py`) | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 403 | memo 154: main's twelve `scripts/checks/` turned on the lane; 12 dead paths repaired | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 404 | memo 155: merge digest; a false positive in its own P3 certificate | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 405 | memo 156: Gate D's first numerics at κ = 1 + ω | no | none | **refuted before banking** (RELAY_LEDGER row 126: pixel artefacts; λ² = κ − 2 fixes a Galois orbit) | CLOSED-HANDLED (refuted) |
| 406 | memo 157: Gate C (three generations) closes on banked material it never cited | no current load; consistent with "three by selection" | none | main commit d7df9316 closed Gate C; sharpened by codex (RELAY row 126 items 3–4) | CLOSED-HANDLED |
| 407 | memo 158: self-correction: B632's cell 2 was run | no | none | RELAY row 126 (codex caught it the same day) | CLOSED-HANDLED |
| 408 | memo 159: a state-claim linter (claims about the record checked against the arc directory) | no | none (the B1338 / P-588 class; process) | — | CLOSED-NO-LOAD-NO-LEAD |
| 409 | memo 160 (Q7): Route A via Kneser–Platonov strong approximation; three of five hypotheses typed | no (L169 "compute closed — B1093"; Q7 drafted, unsent) | **LEAD (weak)**, see § 3 lead 4 | — | LEAD |
| 410 | memo 161: the generic stabiliser of a (27, 27̄) pair in e₆ is 𝔰𝔬(8), computed exactly over ℚ(√−3) | no | LEAD (weak), as above | — | LEAD |
| 411 | memo 162: the group is Spin(8); 27 = 1+1+1+8v+8s+8c; B969's pair pinned | no | LEAD (weak), as above; the triality pattern is standard and B299 has it | — | LEAD |
| 412 | memo 163: reading main: Gate C landed; P3's "finite menu terminal" drift stronger | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 414 | memo 165: chain-gap currency pass (λ's gate exists, Gate C closed, ℙ(B₀)) | no | none | B1339's own currency pass | CLOSED-HANDLED (B1339) |
| 415 | memo 166: paired-summary check, NOT ADOPTED by the seat (its control was empty) | no | none | the seat's own non-adoption | CLOSED-NO-LOAD-NO-LEAD |
| 416 | memo 167: Q7 ledger audit: ℚ-simple closed (centroid dim 1, Killing nondegenerate); Q7 at four of five | no | LEAD (weak), as above | — | LEAD |
| 417 | memo 168: "the whole thing is one number": σ, and 6 against 1 | no current load | none | B1305 (no cover with six cusps to degree 12; the σ fork); the B1025 floor itself superseded by B1750 | CLOSED-HANDLED (B1305) |
| 418 | memo 171: the σ bridge compares Virasoro c((E₆)₁) with c_eff of a unitary substitute η⁻¹; Ẑ/F_K are the boundary characters | **YES.** It questions B1190/GC-6's typing, which B1305 and **B1722's sealed W2 cell** ("the action weight at L154's c = 6") inherit; it is P-492's subject (debt #60) | none beyond P-492 | B1305 FINDINGS_B engaged the c_eff line (memos 174–178), never this memo's sentence | **DEBT** (input to P-492; D6) |
| 419 | memo 173: the GM paper arrived; §2(a) and §3 retracted the same day | no | none | the seat's retraction; § 1 survives and is memo 171's point; B1305 B read GM | CLOSED-HANDLED |
| 421 | memo 31: the beat on H₁(cusp) is diag(1, −1) | no | none | **B1147**: reproduced, byte-identical | CLOSED-HANDLED (B1147) |
| 422 | memo 32: the unique cubic on the 27 is ±1; no invariant bilinear ("no mass term") | no | none | B1147 | CLOSED-HANDLED (B1147) |
| 425 | memo 36: Pin above the fork (t² = a); the third derivation of the spin selection | no | none | B1147 | CLOSED-HANDLED (B1147) |
| 426 | memo 37: QP-1: the cusp character is one bit blind (β ≡ 0); the bit is the beat's mirror | no | none | B1147 | CLOSED-HANDLED (B1147) |
| 428 | memo 39: the Habiro tower; v_π of level differences = 2 universally | no | none | B1147 | CLOSED-HANDLED (B1147) |
| 429 | memo 40: the Ohtsuki bridge; every p-power place coheres with the one germ at q = 1 | no | none | B1147 | CLOSED-HANDLED (B1147) |
| 433 | memo 44: θ is inner (tr −2); one ℤ/2 class on both fork branches | no | none | **B1148** | CLOSED-HANDLED (B1148) |
| 447 | memo 58: the anomaly payment: the dark block 10⊕1 cancels the 16's u(1) anomalies | no | none | **B1158**: reproduced; "required" quarantined | CLOSED-HANDLED (B1158) |
| 448 | memo 59: the centre of the holonomy closure is C_Ψ, the lock (= B1146's ρ(−I)); commutant dim 297 | no | none | the same operator as B1146 and B1149 | CLOSED-HANDLED (B1146/B1149) |
| 449 | memo 60: the conserved pair (κ, tr ab⁻¹) solves X² − (x²−1)X + (x²−1); Eisenstein at x = 2, golden at x = 0 | no | none current (a law-harvest candidate under WORKING_RULES § 10; codex R008 gave a third derivation) | — | CLOSED-NO-LOAD-NO-LEAD |
| 450 | memo 61: the E₆ singlet vev keeps the matter parity and breaks the object's lock; five directions neutral to both | no | **LEAD**, part of § 3 lead 1 | — | LEAD |
| 451 | memo 62: E₈ portal family democracy per triple; exchange sign once the gauge is paid | no | none | B1158 (the 270 triples reproduce, cited only); B1185 | CLOSED-HANDLED (B1158) |
| 452 | memo 63: the three-family vertex is symmetric under the two spinor-family slots | no | none (E₈ possibility space; B1150) | — | CLOSED-NO-LOAD-NO-LEAD |
| 453 | memo 64: the beat induces the identity on gr₃ | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 454 | memo 65: peripheral fixed-space dimensions (12/15 resolved) | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 455 | memo 66: every nontrivial e₆ irrep has dim ≥ 27 (textbook) | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 456 | memo 67: E₆ nilpotent-orbit dimensions for all 20 characteristics (textbook tables) | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 461 | memo 72: the 27 has exactly two SM-safe vev directions (ν^c-like, S-like); the chain lands on the SM torus; lock and ψ-parity both die | **yes, weakly**: B1162 banks "the unique SM-preserving chain (D3)" as cited (B1162 has no dependents) | **LEAD**, § 3 lead 1 | B1162 cites it; certificate reproduces here | LEAD |
| 463 | memo 74: one 27 carries no family index; three-ness lives only in E₈'s (3, 27) | no | none | **B1162** (= B1161's generation-index NULL, own-verified); B1185 | CLOSED-HANDLED (B1162/B1161) |
| 465 | memo 76: the surviving ℤ/2s: one SM ℤ/6 shadow plus 14 E₆ extras, each odd on exactly 8 of 15 SM states; none is an R-parity | no | **LEAD**, § 3 lead 1 | certificate reproduces here | LEAD |
| 466 | memo 77: the surviving torus is exactly the SM's; the u(1)_ψ remnant is trivial (gcd(1, 2) = 1); the dark block is unprotected | **bears on GENESIS v1.12**, "computed nowhere yet: Dirac against Majorana … which no arc computes" | **LEAD**, § 3 lead 1 | certificate reproduces here | LEAD |
| 468 | memo 79: chirality is character-invisible (χ(w) = χ(w⁻¹)); orientation is visible | no | none | **B1337 § 3** read it and corrected the attribution (an SL₂ identity on every manifold) | CLOSED-HANDLED (B1337) |
| 472 | memo 83: the cosmogony typed; the forced couplings are rational, so no CP-odd rephasing invariant is forced | no (retired frame; the current frame's CP lines come from Re τ, B1799) | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 473 | memo 84: charge quantization and atom neutrality from the forced hypercharge | no | none (textbook consequence of B1160) | B1160 | CLOSED-NO-LOAD-NO-LEAD |
| 474 | memo 85: the 27³ coupling has no diagonal entry, so no Majorana-shaped ν^cν^cX term; the neutrino sector is Dirac-only in-record | bears on the same GENESIS v1.12 line; GENESIS already says "no field of the 27 or the 78 gives ν^c a Majorana mass" | **LEAD**, § 3 lead 1 | certificate reproduces here | LEAD |
| 475 | memo 86: tr[a, b] = κ; order is forced, direction is free three ways | no | none; its "direction is the observer's" is superseded by B1662/B1750's canonical arrow | — | CLOSED-NO-LOAD-NO-LEAD |
| 476 | memo 87: the N = p² dark-hyperbola law proved by Gauss lemmas | no | none | **B775/B778** proved it for all p (B1199 GC-29) | CLOSED-HANDLED (B775/B778) |
| 477 | memo 88: the dark tower for N = pᵉ, with spectrum {p^{a/2}} | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 478 | memo 89: closed-form shell counts of the dark tower | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 479 | memo 90: the beat is isometric; σ² is GL₂(ℤ)-conjugate to the fibre monodromy | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 480 | memo 91: Vol = 9√3 ζ_K(2)/π² in four dressings; R = −6; the systole | no | none | **B1117** (Vol as ζ_K(2), to 4e-32) | CLOSED-HANDLED (B1117) |
| 481 | memo 92: B928's hierarchy carrier D₂ᵗʷ is mirror-even, so object-side | cited as a "traveler" in B1193 and GRAND_COMPUTATION_v0 § 10 ("load-bearing for the value arc", the retired B928 arc); B1193 has no dependents | none current | — | CLOSED-NO-LOAD-NO-LEAD |
| 482 | memo 93: B928's Klein group splits under the mirror | as row 481 | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 483 | memo 94: H-theorem refuted; the arrow is branch-conditional on the Fricke unstable manifold | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 484 | memo 95: Stage 2 unsealed: the B928 sheet against measured CKM/PMNS shape (an owner-authorised look; all six readings miss) | no (retired frame; outside LOOK_LEDGER's B1656 scope) | none (note: a seat look at mixing data exists, for any joint-look accounting widened beyond B1656's frame) | B929's verdict stands | CLOSED-NO-LOAD-NO-LEAD |
| 485 | memo 96: the dimensional content is a rank-1 lattice; seconds cost one datum | no (consistent with "the observer supplies a unit") | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 486 | memo 97: no symmetry swaps the Fricke branches; R is an exact time-reverser | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 487 | memo 98: cc's K₄ founding torsor reproduced; P is character-invisible | no | none | B1193 (the founding-bit identity); this is its independent check | CLOSED-HANDLED (B1193) |
| 488 | memo 99: the unit trichotomy of ℚ(√−3), ℚ(√5), ℚ(√3); one bit per field | no | none (retired census; B1750) | — | CLOSED-NO-LOAD-NO-LEAD |

## 3. Totals, and the strongest leads

### Totals (101 rows)

| disposition | rows |
|---|---|
| CLOSED-HANDLED (pointer given) | **41** |
| CLOSED-NO-LOAD-NO-LEAD | **42** |
| LEAD | **9**, in two clusters: rows 450, 461, 465, 466, 474 and rows 409–411, 416 |
| DEBT | **9**, five items: rows 371, 381, 384, 392, 393–396, 418 |

### The strongest leads, ranked (honestly: one is worth doing now; the rest are small)

**1. The residual discrete symmetry of the root's 27-breaking (rows 450, 461, 465, 466, 474; memos 61, 72, 76, 77, 85).**

- *The idea.* The E₆ 27 has exactly two SM-preserving vev directions: the two neutral lepton-block states, ν^c-like and
  S-like (memo 72). The memos then work out what survives each choice of vevs:
  - With both vevs, the surviving torus is exactly the SM's.
  - The u(1)_ψ remnant is trivial, because the doors carry ψ-charges with gcd 1 (memo 77).
  - The surviving GF(2) gradings are one SM ℤ/6 shadow and 14 E₆ extras. None is odd on all 15 SM states, so none is a
    matter parity (memo 76).
  - The object's own group-paid ℤ/2 (the lock, memo 59) is broken by both doors.
  - A singlet-only vev keeps the matter parity but stops at rank five (memo 61).
  - The 27³ coupling has no Majorana-shaped entry (memo 85).
- *Why it matters.* GENESIS lists "Dirac against Majorana: decided by the discrete symmetry left when the extra abelian
  factor is broken, **which no arc computes** (A5)" under "Computed nowhere yet" (GENESIS l. 483–484; B1478's A5 "no arc
  computes the residual discrete symmetry"). These memos compute it for the root's 27-door breaking.
  - It also prunes THE_TOWERS. B1805 left P-414 "open in other frames … an E₆ meeting point with different localised
    content". For 27-type localised content the answer is the same dichotomy as B1805's SO(10) one:
    - the singlet keeps the parity but cannot reach rank four;
    - ν^c reaches the SM and kills the parity.
  - So an E₆ meeting point supplies a matter parity only with non-27 Higgs content.
  - The finding bears indirectly on P-157 (debt #7), the Dirac reading of P10 in the weave frame. It does not settle it:
    the frames differ.
- *The first computation.* All on main's own 27-weight generator (B299's `_weights_27`, as B1208's LEG 4 used it):
  1. list the 27's colour-, weak- and Y-singlet directions;
  2. for each vev set ({S}, {ν^c}, {both}), compute the unbroken subgroup of the rank-6 torus as a finite abelian group
     modulo the SM centre;
  3. test each element for matter-parity action (odd on the 15, even on the Higgs doublets) and for whether it forbids
     ν^cν^c at any operator dimension;
  4. redo the computation in GENESIS's own U1-η normalisation. GENESIS says both E₆-charged singlets carry the same η
     charge, so a singlet vev leaves ℤ_|q|, which must then be compared with hypercharge's centre. This case is not in the
     memos, because their ψ-frame is a different SO(10) (memo 72's filed frame error).

  Data-free, an hour of work.
- *What it changes.* A GENESIS "computed nowhere" item becomes a computed root-level fact (or is scoped). P-415's E₆ branch
  loses its 27-only version. The "dark block unprotected" kinematic statement gets main's grade.
- *Why main has not done it.* The rows were SCHEDULED unread. B1162 cited memo 72 rather than re-running it, on the ground
  that the "cloud stack" was needed, but that stack is on main. B1805's seen-first sweep (12 matter-parity arcs) did not
  surface these memos. The certificates reproduce byte-for-byte here.

**2. L173, the laboratory lead, loses its object-specific differential (rows 393–396, with 387).**

- *The idea.* The memos make four claims:
  - the 6−5 boundary-mode remainder at ρ = α is a one-ended-detector artefact (memo "144");
  - at reversal-closed windows H_L = J H_R J forces every two-ended count to tie, a theorem (memo "145");
  - the one exception, at odd Fibonacci index, is shared by every Sturmian slope (memo "146");
  - the apparent golden excess is a Fibonacci-window confound (memo "147").
- *Why it matters.* OPEN_LEADS L173 is still ★★★★ and still says "the banked prediction is a COUNT (ρ ↦ edge content,
  5-vs-6 at ρ=α)" and "commission a mode-count observable … to separate 5 from 6" (l. 1922). B1414 recorded only that the
  three sealed clauses are one identity.
- *The first computation.* Re-run `l173_gap_detector.py`, `reversal_forces_symmetry.py`, `odd_index_asymmetry.py` and
  `golden_excess_ensemble.py` (all on main under `outside_bench/certificates/`). Then re-derive the J H J tie with B1095's
  own Hamiltonian and a two-ended detector, against non-golden slopes at commensurate windows.
- *What it changes.* The programme's only laboratory prediction is re-graded: probably slope-specific at most, with no
  object-specific count. It is not an SM-parameter matter, which is why it ranks second.
- *Why main has not done it.* The memos are SCHEDULED; B1414 harvested only memos 185–233.

**3. The σ bridge's type error (rows 418, 419; memo 171).**

- *The idea.* GC-6's "six cusp-boson units against one" compares the Virasoro c of (E₆)₁ with the c_eff of η⁻¹, a unitary
  substitute that was never the object. Its script never runs the estimator on the object. The object's boundary
  characters would be the logarithmic Ẑ/F_K, for which c_eff ≠ c.
- *Why it matters.* This is the subject of P-492 (debt #60, "B1088's c = 6σ rests on a boundary assumption"). B1722's
  sealed W2 cell used "the action weight at L154's c = 6", so that negative's scope inherits whatever P-492 finds.
- *The first computation.* None new. Read memo 171 with B1034, B1088 and B1190/GC-6's script when P-492 is worked.
- *Why main has not done it.* B1305 slice B took the seat's c_eff measurements (memos 174–178) but never this memo's
  type-error sentence. Gravity's normalisation is not one of the 19, so it ranks below lead 2.

**4. Route A's strong-approximation chain (rows 409–411, 416; memos 160–162, 167). Weak.**

- *The idea.* Computed exactly:
  - the stabiliser of the object's canonical (27, 27̄) pair is Spin(8), simply connected and ℚ-simple;
  - 27 = 3·1 + 8v + 8s + 8c.

  That is four of the five Kneser–Platonov hypotheses. The fifth, that the orbit count equals the class set, remains. If it
  held, the integral orbit would be unique: a selection of a canonical point by arithmetic.
- *Why it ranks low.* Its object is the retired value-field frame (B969/B990/B1093, the disc-6237 cubic), not τ. The
  Spin(8) and triality facts are standard Jordan-algebra results (B299 has triality). L169 calls the remainder a literature
  residual. Q7 sits drafted and unsent in the send queue (B1339).
- *What it would change.* Little for the current questions. Keep it parked under L169.

**5. The menu-width denominator (row 354; memo 105). Weak.**

- *The idea.* A family-wise denominator fixed before data: 11,720 tier-1 values from 17 banked atoms, median gap ≈ 3.5e-5.
  Any hit resolved more coarsely than the local spacing is chance.
- *Where it would matter.* Only if a level-1 candidate ever appears as a closed form in banked constants. The current
  candidate is a frame fit, which THE_BAR's matched nulls already handle.

*Not ranked:* memo 60's one-polynomial identity, (κ−1)(tr ab⁻¹ − 1) = 1 on the component, is a LAW_MAP-harvest
candidate with no bearing on the open questions.

## 4. DEBT candidates

- **D1. Memo 122, and the claim that it is unverified.** Rows 371 and 384.
  - GENESIS v1.12 (l. 481) says "memo 122 [the seat's, unverified on main: row 371, scheduled; v1.51]".
  - COSMOLOGY_LEDGER row 4 says "SCHEDULED, not verified on main" (l. 54) and "has never been checked" (§ ROW 4,
    l. 231–237).
  - But **B1208's LEG 4 (2026-08-29)** re-ran memo 123's stronger census on main's own 27-weight generator:
    - no ℤ/n character for n = 2…6 stabilises any charged set of size ≤ 2;
    - its MB12 planted control finds 486;
    - it concludes: "the cosmology ledger's row 4 closes at character level".
  - Memo 122's own certificate reproduces here. Owed:
    - a dated note on the GENESIS bracket and on COSMOLOGY_LEDGER row 4, citing B1208's LEG 4 (and checking that its
      characters include memo 122's four Klein elements, one of which carries an affine sign);
    - an update to B1202's dark-matter negative control, which B1338 § 4 and § 6 found false and left alone.
  - This belongs in P-145 (debt #31) and in P-589's GENESIS screen.
- **D2. P-145 item 1 (row 381, memo 132).**
  - The certificate reproduces here, and its mathematics is a few lines: det J = −1 for (x, y, z) ↦ (z, x, zx−y), 0 for the
    Thue–Morse map, +1 for σ².
  - The decision owed is the identification "e-folds = net volume growth of a tower map". It must be typed on
    IDENTIFICATION_LEDGER before COSMOLOGY_LEDGER row 2 moves from MISSING.
  - B1202's inflation negative control is also false (B1338 § 4).
  - Row 384 (memo "135", rows 7/8) is the same kind of currency item; fold it in.
- **D3.** See D1 and D2: COSMOLOGY_LEDGER rows 7/8 still read "never started"; memo "135" ran their named probes.
- **D4. P-317(b) (row 392).** Memo "143"'s V-NEG is already named as resting on B1137's information-free PSLQ DISJOINT.
  The row should point to P-317(b) rather than read SCHEDULED, and V-NEG should be re-run once the tolerance is controlled.
- **D5. L173 (rows 393–396).** See lead 2. A new register row is owed. The living ★★★★ text and its "separate 5 from 6"
  observable rest on a count the cloud seat called an artefact and then showed tied by theorem.
- **D6. P-492 (row 418).** See lead 3. Add B1722's W2 cell to the row's scope.
- **D7. Ledger hygiene (process; no mathematics).**
  1. Forty-one rows are handled; re-disposition them with the pointers in § 2. B1306 slice D's grep (a seat-prefixed id
     with a verification verb on the same line) missed B1147, B1148, B1158, B1162 and B1201. B1337, B1339 and B1414 read
     items and never moved their rows.
  2. Row 44 is BANKED but counted, because `harvest_debt.py` l. 616 tests the substring `"SCHEDULED" in disp`; its
     "Was: …" clause inflates the count. The prescreen does the same.
  3. For rows 383–396 the INDEX memo numbers and the file-header numbers differ, so cite by file.
  4. Rows 389 and 390 are one file.
- **D8. GENESIS's "Computed nowhere yet: Dirac against Majorana … which no arc computes".** Rows 466, 465, 474.
  - Memos 76 and 77 compute the residual discrete symmetry for the root's 27-door breaking, and their certificates
    reproduce here.
  - Once main verifies (lead 1), the line owes a dated note, scoped to the frame difference: ψ-charges against GENESIS's
    U1-η and U1-Z′₉.
