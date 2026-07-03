# B402 — Q1 BANKED: the pair-requirement wall has TWO mechanisms, split by seed

**Status: Q1 banked; Q2 (the characteristic 3-orbit siblings) registered, queued. Prereg
committed first. Firewalled.**

## Q1 — cell-wise vs emergent single-reality (the verdict: BOTH, split by seed)

- **m = 1: LOCAL.** All 20 raw single traces tr(Par·W₁ʲ) are τ₃-real cell-wise — the
  golden seed's single channel is locally forbidden from imaginary content.
- **m = 2: EMERGENT.** Only 8/12 cells are real; j ∈ {1, 5, 7, 11} (the (ℤ/12)ˣ units!)
  carry (1/8)·(1, 1, ∓1, ∓1) — with the τ₃-conjugate pairing {1,5} ↔ {7,11} — yet every
  DFT window kills them: the silver seed's single-reality is aggregate-only, joining the
  emergent family.

**The refined statement of the single-object wall:** the object's inability to "see
itself alone" is enforced LOCALLY for the golden seed and EMERGENTLY for the silver seed —
the same m=1/m=2 dichotomy as the transport laws (identity vs coarsening). The imaginary
unit-power cells of W₂ are new exact data (q1_single_reality.json).

## Q2 (registered, queued)

The monodromy 3-cycles the nonzero half-characteristics; the twist address (1,1) is one
point of a ℤ/3 orbit. Pipeline registered in PREREGISTRATION.md: build sibling cocycles,
MEASURE each candidate's address via the trace-formula linear-part fit (the P64
instrument), then compare the three sibling sector theories. Orbit ⇒ spontaneous
selection; distinction ⇒ the address is forced — either banks.

**Provenance.** q1_single_reality.py → q1_single_reality.json; locks
tests/test_b402_mechanisms.py.

---

# Q2′ BANKED: the seam landscape — the canonical point is the unique null

All 15 D-side twist addresses computed (q2_landscape.json; every model ord 20×12):

- **r = 0 (canonical): NULL** — the P62 anchor reproduced from the landscape side.
- **All 14 nonzero addresses: BRIGHT**, with the s-cell count stratified EXACTLY by
  gcd(r, 15): units → 44 (the banked theory sits here, r = 7); 3-torsion {3,6,9,12} → 32;
  5-torsion {5,10} → 36.

**The law: seam intensity = f(gcd(address, 15)), f = {1: 44, 3: 32, 5: 36, 15: 0}.**
The reframe of P62: every twist opens the pair channel; the untwisted point is the UNIQUE
dark point of the whole address space — classicality is the exception, not the seam. The
"spontaneous choice" question dissolves: nothing is chosen; the intensity class is set by
the address's torsion type. (The registered mod-2 3-orbit framing was corrected in the
prereg before this run — odd N has no 2-torsion.)

**Provenance.** q2_landscape.py (~35 min) → q2_landscape.json; locks
tests/test_b402_mechanisms.py.
