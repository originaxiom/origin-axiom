# FINDINGS — the listening log (PREREG sha256 5b5e70c6…, sealed before any tick was computed)
web seat, 2026-10-06. Three acts X_m = [[m,1],[1,0]] (golden m000, silver m001, bronze m005), ticks k = 1..10, native invariants
only. A1: `run.txt`, `log.json`. Instrument fault in the first run (wrong cyclic cover for silver/bronze, whose parents have
several) caught by E1–E3 failing; preserved in `run_FAILED_wrong_covers.txt`; fixed by building each tick as the bundle of X_m^k,
validated 10/10 against golden's unique covers. CS column: 0.5 is the rounding of 0.4999… — read as CS ≡ 0 (mod 1/2).

## A2 — the fixed analysis
**Expectations E1–E4: all PASS** (orientability alternates; p-rank = dim ker(X^k − I mod p) at every p and tick; ticks ≡ 2 mod 4
amphichiral; volume ratio 1).

| quantity | regularity found | determined by the clocks? | differs between acts? |
|---|---|---|---|
| orientability | alternates with k | yes (det = −1) | no |
| full p-layers (p-rank 2) | exactly at multiples of the clock ord(X_m mod p): golden 2@{3,6,9}, 3@{8}, 11@{10}; silver 2@even, 3@{8}, 7@{6}; bronze 2@{3,6,9}, 3@even, 11@{8} | yes (theorem) | yes — through the clock periods, the act's own data |
| half p-layers (p-rank 1) | (i) at every odd tick when p divides m (silver p=2, bronze p=3); (ii) at the discriminant prime m²+4 on multiples of the eigenvalue's order (golden p=5 @{4,8}; bronze p=13 @{4,8}) | yes: (i) X_m ≡ P (the bare swap) mod p when p ∣ m; (ii) a single eigenvalue mod a ramified prime | yes — golden has no case (i): m = 1 has no prime divisor |
| amphichirality | every orientable tick, all acts (k ≡ 0 mod 4 too) | k ≡ 2 mod 4 by theorem; k ≡ 0 mod 4 observed, not predicted | no |
| CS on orientable ticks | ≡ 0 at every one, all acts | no (consistent with amphichirality; 1/4 never occurs) | no |
| \|Sym\| | 2k at odd ticks, 4k at even ticks — identical for all three acts | no (observed) | no |
| 2T door | changes exactly at completions of the clocks at 2 and 3, the primes of \|2T\| = 24: golden 48 → 0 at {3,6,9} (2-clock), → 240 at 8 (3-clock); silver 0 except 768 at 8 (3-clock); bronze 96/240 shifting to 192 at {3,9} and 768 at 6 | partly: the change points are the clocks at 2 and 3; the counts themselves are not explained | yes, through the clocks |

## A3 — observed, unexplained (no interpretation)
- \|Sym\| = 2k (odd) / 4k (even) for all three acts.
- amphichirality and CS = 0 at ticks ≡ 0 mod 4.
- the 2T door's counts (48, 96, 192, 240, 768).

## What the log says, in the owner's terms
The act walks — mirror flipping each tick, the same for every act. Observed at a prime it becomes a clock, and its homology
opens a full new layer exactly when a clock comes home; the E6 door opens and closes on the clocks of the two primes of 2T.
Every regularity is shared by all three acts except the clock periods themselves and one thing the golden act alone lacks:
at a prime dividing m the act reduces to the bare swap P — pure mirror, no shear — and m = 1 has no such prime. **The golden
act is the only metallic act that is never only the mirror at any prime.** (Trivial once seen; recorded because the log found it.)
