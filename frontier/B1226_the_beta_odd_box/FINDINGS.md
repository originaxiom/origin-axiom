# B1226 — THE β-ODD BOX

cc banking seat, 2026-08-31. Owner-directed: *"we need to count for four forces first, including
gravity, then Higgs boson, then leptons and quarks. i think were doing a category error on our
expectations and the way were saying 19 sm parameters or 26 sm parameters if they were all same
category."* **Gate 5 absolute — no measured physical value is asserted anywhere in this arc.**

## Why this arc exists

It began as a consequence-check on **B1224**, banked hours earlier the same day: amphichirality
forces CS to be **2-torsion**, `CS ∈ {0, ¼}` — not `CS = 0`. Nobody drew the consequence. Drawing it
breaks a banked chain, and the break turns out to be the same shape as the owner's category
correction, one level deeper.

## Cell 1 — the scale wall is not a symmetry theorem

**B1012 banked** (verified quote from its verdict): *"blind-to-k iff CS = 0 iff the object equals its
mirror"*, and on that equivalence upgraded H11's firewall to **"RELOCATED BEYOND THE OBJECT'S REACH
IN PRINCIPLE."**

The chain has two links:

| link | status |
|---|---|
| `blind-to-k ⟺ CS = 0` — the sympy identity `∂S/∂k = −CS` on Gukov's split `t = k + iσ` | **STANDS** |
| `CS = 0 ⟺ amphichiral` | **REFUTED, BOTH DIRECTIONS** |

Counterexamples, exhibited on the one-cusped orientable census (600 scanned):

| | CS ≡ 0 | CS ≡ ¼ |
|---|---|---|
| **amphichiral** | m004, m136, m206 | **m003, m135, m207** ← kills `amph ⇒ CS=0` |
| **chiral** | **m208** ← kills `CS=0 ⇒ amph` | 593 others |

**A methodological catch worth recording.** `M.is_isometric_to(mirror)` returns `True` for m208 — and
it is **not a chirality test**: it finds *orientation-reversing* isometries. The authoritative test is
`symmetry_group().is_amphicheiral()`, cross-checked here by cusp-map determinant: m208's isometries to
its mirror all have `det = −1`; m004's and m003's carry **both** `+1` and `−1`. A seat trusting the
convenient call would have concluded the opposite.

**A second catch.** `str()` on snappy's high-precision `Number` prints a value that disagrees with
`float()` of the same object (m136 → `2.0444…` vs `0.0`). This is a **display artifact, not a
disagreement**: standard and high precision agree on every exhibit. Recorded because it briefly looked
like B1224 — banked the same day — was wrong. It is not; B1224 stands 6/6 at both precisions.

**What survives.** *"No dimensionful quantity, by theorem"* **still holds for m004**: `CS = 0` is
exact (2-torsion leaves only `0` and `¼`, and numerics separate them decisively), so `∂S/∂k ≡ 0`.
What is corrected is the **reason**. The blindness is *not* a consequence of a symmetry the object
has. It is a **contingent datum**: which element of the symmetry-given ℤ/2 this object sits at. Its
equally-amphichiral sister m003 — same volume, same trace field ℚ(√−3), same `|Sym| = 8` — is **not**
blind to the level.

Stated cleanly, and better than the original:

> **blind-to-k ⟺ CS ≡ 0 ⟺ the object's complex volume `Vol + i·CS` is REAL.**

The three-tier form, matching B1165/B1170's template: **(i)** amphichirality ⇒ `CS ∈ ℤ/2` — *forced*;
**(ii)** m004 sits at `0` — *contingent, the object's own datum*; **(iii)** `CS = 0` ⇒ scale-blind —
*forced from (ii)*.

## Cell 2 — the category error, made computational

`19` / `26` is a flat list of things that are not the same **kind** of thing. Typed by this
programme's own law — **B1168**: object-canonical ⟺ β-even **and** dimensionless — the 28 split:

| box | n | members | supplier |
|---|---|---|---|
| **A** β-even, pure | 6 | CKM angles, PMNS angles | **NOBODY** — B1225 proves the object *cannot select* |
| **B** scale-anchored | 3 | g₁, g₂, g₃ (dimensionless but *running*) | **READER** — B811's H128 kill, on kind |
| **C** dimensionful | 16 | 9 fermion masses, v, m_H, 3 ν masses, G, Λ | **READER** — the scale wall (cell 1) |
| **D** **β-odd** | **3** | **θ_QCD, δ_CKM, δ_PMNS** | **OBJECT CONSTRAINS** — a ℤ/2 (B1224) |

MB12 bite: 4/4 boxes occupied, non-vacuous. A flat count occupies 1/4 — which is the category error,
exhibited.

The owner's ordering (forces → Higgs → matter) is what makes the split visible: gravity is not an
omission from a list of 19, it is **two more members of box C**, the box that was already closed. And
the *structure* — gauge group, reps, generation count, hypercharges, the Higgs slot — is not in this
table at all, because it is not numeric. That is the part the programme **derived**.

## Cell 3 — every probe into box D demanded the wrong type

Box D is the only box where the object has an output at all. That output is `CS`, forced 2-torsion:
**one bit**, cardinality 2.

| arc | asked | demanded | outcome |
|---|---|---|---|
| **B1027** | δ₁₃ = 120° or 240°? | **a value** (degrees) | MISS 11.4σ / 38.0σ, powered |
| **B1137** | is an SM value an algebraic combination of regulators? | **a value** (18 sealed targets) | DISJOINT |
| **B813** | CS(m004) = θ_QCD? | **a value** (a coefficient slot) | REFUTED ON TYPE |

**3/3 demanded a continuous value from a bit-valued channel. 0/3 asked the bit.**

A bit cannot answer a value question. Those three negatives therefore measure the **type mismatch at
the source**, not the object. B813 is the sharpest case: it correctly refuted `CS = θ` because θ is a
*coefficient* while CS is a *functional value* — and that refutation **stands untouched**. What it did
not test, and what nothing has tested, is the type-matched question:

> **Does the object's ℤ/2 fix the CP-conservation BIT — whether a phase sits at a CP-even point — as
> opposed to the phase's magnitude?**

**B303 is already at bit level** and was never connected to these three negatives: *"the CP sign is
literally the sign of Chern-Simons"* (PROVED). It sits on the correct side of the type boundary that
cell 2 draws, and no box-D probe ever used it.

## What is NOT claimed

No CP phase is derived. No measured value is asserted. Gate 5 intact. B813's refutation of the value
dictionary stands. Cell 3's forward question is **registered as a lead, not banked** — it is a
type-match, which is a licence to ask, not an answer.

## Reproduce

`sh frontier/B1226_the_beta_odd_box/reproduce.sh` — three independent cells; cell 1 needs snappy,
cell 3 reads the record and asserts each named arc's verdict from its own `arc_verdict.json`.
