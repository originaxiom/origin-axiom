# CROSS-SEAT PACKET — THE LEVEL-LADDER CAMPAIGN (seat cc2 → banking seat)

**Provisional ID:** CC2-LL (B-number assigned at banking). **Seat:** cc2 (read-only clone;
nothing in the repo touched; nothing applied to any register — §Proposed updates in
FINDINGS.md are proposals only). **Date:** 2026-07-15.
**Sources:** jewel veins L73/L74/L76/L77 (owner directive 2026-07-14) + hint gate H133.

## What this packet claims, in one line each

1. **Z = Tr ρ(A₁) = 0 EXACTLY at E₆ level 4** — H133 killed at its own gate; both parity
   sectors vanish exactly (integer reduction mod Φ₁₉₂ over ℤ; no floats in the certificate).
2. **Level 4 is new exact data:** 42 primaries, odd dim 17, clock 12 (both sectors),
   the ℚ(√2)/silver import in the magnitudes, everything {2,3}-ramified.
3. **The splitting law survives reframed:** odd-prime saturation of κ with splitting-typed
   form; inert-prime import now has two instances (√5 at 15, √2 at 16); level-5 ℚ(√17)
   registered as the decisive prediction.
4. **The import is sector-blind, the organization is chiral** (level-3 even block is
   √5-ramified too, but sprawls to degree > 16; the odd sector is one clean octic).
5. **L73's anchor is a theorem with locks** (det(A₁−I) = −1 ⇒ abelian invisibility;
   662/662 independent cyclic theaters).
6. **L76's towers computed** (exact to the stated rungs + mod-p extensions; the n = 10
   interlock decided — see outputs/P4_TOWERS.log verbatim).

## Files

| File | Role |
|---|---|
| `CAMPAIGN.md` | the prereg (frozen; sha256 in `outputs/P1_FREEZE_HASHES.txt`) |
| `FINDINGS.md` | the verdict document (outcome B), scored prediction sheet, proposed register updates |
| `scripts/engine.py` | the generic-k E₆ engine: exact ζ_{6κ} integer-count pipeline + banked-style float build + gate battery + readouts |
| `scripts/p2_certify.py` | exact-Z certificates, order certificates, minimal polynomials, Pisano sets, T-content |
| `scripts/p3_verdict.py` | sector-trace certificates, disc exponent-parity (F2), cross-level parity comparison, the ladder table |
| `scripts/p3b_unidentified.py` | degree ≤ 16 identification sweep; prices out the residuals |
| `scripts/p4_towers.py` | L76: t_n exact (n ≤ 24), e_n exact (n ≤ 6, Bareiss), mod-p to n = 12/10 |
| `scripts/p_proof_lock.py` | L73 locks (lemma exhaustive to 4096; 662 cyclic theaters) |
| `outputs/P0_REPORT.md` | gate report: the engine reproduces banked k = 1,2,3 exactly (incl. the D7 octic integer-for-integer) |
| `outputs/level4_readouts.json`, `level4_blocks.npz` | the blind-banked level-4 data (hashes recorded pre-comparison) |
| `outputs/P2_CERTIFY.log`, `P3_VERDICT.log`, `P3B_UNIDENTIFIED.log`, `P4_TOWERS.log`, `P_PROOF_LOCK.log` | run logs, numbers verbatim |
| `outputs/L73_ONE_PAGER.md` | the abelian-invisibility proof page |

## Verify-don't-trust checklist (for the banking seat)

1. `python3 -m venv .venv && pip install numpy sympy mpmath` (versions in P0_REPORT.md).
2. `python scripts/engine.py gates` — must print ALL P0 GATES GREEN (reproduces B569/B570-C3/
   B578-D7 exactly; hard-stops otherwise). This is the convention lock (B569 lesson).
3. `python scripts/engine.py level4` — regenerates the level-4 readouts; diff against the
   banked JSON (hashes in `outputs/P1_FREEZE_HASHES.txt`).
4. `python scripts/p2_certify.py` and `scripts/p3_verdict.py` — the Z₄ = 0 and sector-zero
   certificates are integer-arithmetic (`Poly.rem` mod cyclotomic); check the `zero-poly =
   True` lines; spot-check any minimal polynomial by direct substitution at dps 50.
5. Adversarial angles we already ran: two-word monodromy at every level; float-vs-exact-counts
   cross-gate (< 1e−13); banked-value reproduction before the new rung; order certificates
   with proper-divisor separation; disc exponent-parity rather than naive prime lists.
   Angles we did NOT run (honest): an independent Weyl-group build (ours is the same BFS
   pattern as the banked scripts); a second magnitude-dedupe convention; level 5.

## Firewall statement

Pure stage-side arithmetic throughout; no physics reading anywhere; the words "law/import/
silver" name arithmetic of modular data only. Nothing here promotes; CLAIMS.md untouched.
