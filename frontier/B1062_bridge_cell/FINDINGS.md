# B1062 — THE BRIDGE CELL: the control EXISTS (golden arithmetic vs both siblings, triple-derived), the tones are NOT gap labels (typed, exact), and both crossing lanes get their answer

*cc banking seat, 2026-08-13. Sealed ad8d60f1 + pre-compute addendum B1062-A1
(binding, honored throughout). Logs: `b1062_v2_block1.log` (geometric points, the
gate), `b1062_v2_block2.log` (the leading test m=1/m=2; its m=3 line SUPERSEDED —
spurious input), `b1062_v2_block3.log`/`b1062_v2_block3b.log` (the complete m=3
variety; the octic), `b1062_v2_block2n.log` (the numeric illustration on correct
orbits), `b1062_verify_battery.log` (the owner-ordered verification battery),
`b1062_v1_v3.log` (the exact V1/V3). Gate 5-Q: no measured value anywhere.*

## V0 — POSITIVE, verified from the source ON THIS BENCH

Hao (arXiv:2303.01395), Theorem A, read from the PDF here: for a non-uniform
lattice of PSL(2,ℝ) or PSL(2,ℂ), B-C ⟹ arithmetic; Gap > 0 ⟹ derived from a
quaternion algebra. Page 1: Luo–Sarnak's forward proof "indeed also works for
Kleinian groups." Page 3: nonuniform ⟺ parabolics — our objects by construction.
The unit-box definition and Maclachlan–Reid's Theorem 2.3 verified verbatim.
Riders standing: R1 (Hao's proof leaned on as published), R2 (Luo–Sarnak's half on
Hao's citation) — named, not silent.

## V2 — CONTROL-EXHIBITED, and the road there is half the result

**The verdict (exact, by field degree under Maclachlan–Reid's criteria, the
addendum's leading test):**

| m | geometric trace data | field | verdict |
|---|---|---|---|
| 1 golden | all-loxodromic; x ∈ roots of x²−3x+3 | **ℚ(√−3)** — imaginary quadratic, recovered from scratch (the pipeline gate) | **ARITHMETIC-side** (boundedness vacuous in degree 2) |
| 2 silver | all-loxodromic | ℚ(x) degree 4 (x⁴−4x²+8; x² = 2+2i), full field degree 8 — reconciled exactly | **NON-ARITHMETIC** (degree alone decides) |
| 3 bronze | the degree-8 irreducible component, all typed roots loxodromic | contains a degree-8 subfield | **NON-ARITHMETIC** (robust over the unidentified geometric root) |

**The arithmeticity axis separates {golden} from {silver, bronze} — the seal's
CONTROL-EXHIBITED branch. The genericity control for the aperiodic campaign
EXISTS, exact and window-free.**

**The road (recorded because it is the method's exhibit):** the first m=3 solve
returned only an elliptic component with field ℚ(√−7); the relay seat's
adversarial attack killed it (tr = −1 forces order-3 elliptics — impossible for a
faithful representation of a free group), independently re-derived on this bench;
the complete Gröbner variety exposed the missed degree-8 factor (the incomplete
`solve` had skipped an irreducible octic — no radical forms); the relay seat
re-derived the whole picture from scratch in the x-eliminant (their own first pass
had a convention error, caught against this bench's verified convention — "in the
wrong convention √−7 appears at m = 2, which is how a convention slip manufactures
a resonance"); both benches' degree-8 components and a blind numeric multistart
agree. **The spurious √−7 killed the compositum resonance and the incidental
answer to the cloud's bronze question — both would have been WRONG. Verify-
everything earned its keep in one afternoon.**

**The illustration (numeric, the addendum's demoted role, window declared at
length 10):** m=1 max 2 per box (lattice-flat — ENTAILED, the pipeline gate's
echo); **m=3 max 106 per box** (the B-C failure made visible); **m=2 ALSO FLAT in
this window despite being exactly non-arithmetic — the live demonstration of why
box-flatness certifies nothing and the field-degree test leads.**

## V1 — TYPED NEGATIVE: the tones are not gap labels

The Fibonacci gap-label module (K007/Bellissard — rider: cited, not re-derived) is
ℤ + φ⁻¹ℤ, integral. **Exactly: 1/(2φ), 1/2, φ/2 demand half-integer coefficients —
the tones (|χ|/2, the banked normalization) are NOT labels**; the mechanism is the
½ against the module's integrality. The un-halved character values lie in ℤ[φ] —
membership in a dense module, fenced as contentless (the B757 fence; clause IV
fails it). **The gap-label route to the doors' externality is CLOSED.**

## V3 — NOT-FOUND (a declared floor)

Enumerated observables: the IDS labels (V1: not the tones) and the band counts
(Fibonacci numbers — intersection with {90,72,120,72,6} EMPTY at every level).
Further observables may be enumerated by a future cell; this is a floor.

## What the cell decides

- **L161 (aperiodic): the gate OPENS** — the control exists (arithmetic golden vs
  non-arithmetic siblings, exact). The externality channel NARROWS: the
  literature read now unlocked (P0-1/P0-2) carries the sharpened question —
  *what observable of the m = 1 chain could carry 2I structure, given labels and
  band counts provably do not?*
- **L164 (the doors): the gap-label external side is closed** by V1's typed
  negative; the design finds externality elsewhere or states the door-crossing
  internal.
- The two-trace-fields TERMINOLOGY row (staged) banks with this arc; the
  compositum-resonance row is DEAD (spurious component) and recorded as the
  species exhibit.

## Riders and honest edges (complete list)

R1/R2 (Hao/Luo–Sarnak as published) · the specific geometric octic root
unidentified (robustness covers the verdict) · the exact bronze trace field
uncomputed beyond "contains degree 8" · K007's module statement on Bellissard's
authority · block 3b's remaining octic roots typing in background at bank time
(three of eight typed, all loxodromic; the x-side typed all eight independently) ·
"cusped arithmetic ⟹ imaginary quadratic" used as standard (Bianchi
commensurability). The prereg self-critique from B1043 applies here in reverse:
this cell's outcome space DID contain the branch that fired.

## Verdict

**PROVED** (mixed ledger per the seal: V0 positive · V2 CONTROL-EXHIBITED · V1
typed-negative · V3 not-found-floor — reported as the ledger, no averaging).
Locks: `tests/test_b1062_bridge.py`.
