# B600 — the level-ladder campaign (seat cc2), adjudicated: the verified subset banked

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities.
Provenance: cc2's campaign artifacts (prereg sha 2c9dea54…, blind readouts sha
95a0e861…) live in their packet, NOT in this repo; per verify-don't-trust this
bank contains ONLY what was independently reproduced here, plus the
adjudicated register updates. Locks `tests/test_b600_level_ladder.py`
(OA_SLOW).**

## VERIFIED HERE (independent pipeline, `verify_level4.py` — my own level-N
generalization of the c3 builder; output hashed)

- **The headline: Z₄ = Tr ρ₄(A₁) = 0 at E₆ level 4 (κ = 16), and
  Tr(Θρ₄) = 0** — both to 1e-10 in my pipeline (cc2 additionally holds an
  exact mod-Φ₁₉₂ integer certificate in their packet; my run is the
  independent cross-check). **H133 dies at its own registered gate.**
- The full ladder gates: N = 3, 9, 20, 42 primaries; Z = +1, +1, +1, 0;
  odd-pair dimensions 1, 3, 8, 17; the parity-hop ladder
  (tr_odd, tr_even) = (+1,0), (+1,0), (0,+1), (0,0) reproduced via Θ-traces.
- **The P4 t-tower 11-locus {5, 10, 15, 20} verified exactly** (integer
  computation; and for BOTH matrix conventions F and A₁ = F² — the
  convention-drift suspicion checked and dismissed).
- cc2's scope note verified: the level-4 zero is NOT forced by B599's
  selection rule (traces are not odd-factor-count contractions; the k ≤ 3
  traces are nonzero) — a genuine structured zero, mechanism open.

## RELAYED-PENDING (cc2's packet; not reproduced here yet)

The exact level-4 odd-block arithmetic (the ℚ(√2) import, the quartics, the
{2,3}-ramification data), the clock table's level-4 rows, the e-tower exact
values to n = 6 and the mod-11 locus n ≡ 1 (mod 3), the n ≡ 10 (mod 15)
DOUBLE-11 interlock (their e₄ factorization matches the banked 11²-echo —
consistent, unverified in full), the L73 one-pager locks, and the wide scan.
These bank when the packet lands in-repo or on independent reproduction.

## Register updates applied (the adjudicated subset)

- **H133 → TESTED-NEGATIVE at its gate** (verified here); the residual hint
  registered: the Z-ladder {+1, +1, +1, 0, ?} — does Z return at the prime
  conductor κ = 17? (cc2's decisive level-5 follow-on, with the ℚ(√17)
  splitting-law prediction, REGISTERED as their campaign's next cell.)
- L74's law reframe (saturation-of-odd-primes with splitting-typed form:
  split → sine kernel, inert → real-quadratic import, two instances) —
  registered at hint/frontier grade as cc2 states it; the level-4 instance's
  field data is packet-pending.
- The four NOTICED rows (norm echoes 7²/7⁴/17²; the sector-organization
  asymmetry; the parity hop; the clock ratio) — registered as cc2-proposed,
  verification status marked per row.

## Method note

cc2's campaign discipline (frozen prereg hashes, blind readouts, the PRED-2
demotion recorded as a self-correction) meets the Review-18 provenance
standard; all verification remains internal to the project's seats.

## PACKET INTEGRATED (2026-07-15) — the pending items upgraded

cc2's packet delivered and integrated in-repo (`packet/`; the declared prereg
and readout hashes VERIFIED on arrival — 2c9dea54… and 95a0e861… exact;
re-hashed at integration in `packet/INTEGRATION_HASHES.txt`). Their own lock
suite EXECUTED GREEN in this environment (7/7, 4.8 s — adopted into the repo
suite as `tests/test_b600_cc2_locks.py`, ungated): the EXACT mod-Φ₁₉₂ integer
certificates for Z₄ = 0 and Tr(Θρ₄) = 0 (upgrading my 1e-10 cross-check to
exact), the 42/8/17 dimension ledger, the orders 12/12, the ℚ(√2) odd-block
import with the rationals {4/3, 8/3, 4, 16/3}, the two odd quartics with
even-exponent disc primes, the k = 1..3 ladder context, and the L73 lemma.
The L73 one-pager locks also green here (662/662 cyclic theaters). The P4
wide scan (in-packet log): **only 11 divides any e_n across primes 3..79,
n ≤ 10** — the banked charge-prime uniqueness retested; exact e_n to n = 6 in
the log with the banked cross-checks (e₁ = −11; the e₄ factorization with the
11²-echo). Status upgrades: the level-4 field arithmetic, the clock row, and
L73 move from relayed-pending to VERIFIED-IN-SANDBOX; the e-tower/interlock
values stand at packet+cross-check tier (their exact logs + the banked
anchors + my independent t-locus verification; a full in-repo e-tower
recompute remains available via packet/scripts/p4_towers.py).
