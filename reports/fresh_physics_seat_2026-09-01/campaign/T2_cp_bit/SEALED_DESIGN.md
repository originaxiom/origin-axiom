# SEALED DESIGN — the L192 type-matched comparison (WRITTEN AND HELD)

**Cell:** T2_cp_bit (outside evaluation seat, 2026-09-01)
**Status: SEALED. NOT EXECUTED. Execution only on the owner's election.**
**Gate 5: no measured Standard Model value is named, looked up, or implied anywhere in this
document.** The reader-side inputs below are *abstract classification labels*; producing them from
measurement is the reader's act, outside this cell, after election.

---

## D0 — What L192 licenses, and only that

The object's entire output into box D (β-odd, dimensionless: the CP sector) is **one bit**: the
element of the amphichirality-forced ℤ/2 at which the object sits (B1224: `2·CS ≡ 0`, so
`CS ∈ {0, ¼}` in `ℝ/(½)ℤ`; B303: the CP sign is the sign of CS, and `CS = 0` is the CP-symmetric
point). The only type-matched question is therefore:

> **Does the measured CP sector sit at a CP-even point — AS A BIT (yes/no)?**

Never as a phase magnitude. Any execution that extracts, names, or fits a *value* from the
measured side is outside this design and is refused by it.

## D1 — The exact object-side prediction (computed, HALF 1 of this cell)

Object-side reading rule (frozen; identical to `compute_cp_bit.py`):
for an **amphichiral** cusped orientable hyperbolic manifold M, compute `CS(M) mod ½`
(SnapPy normalization, representatives in `[0, ½)`, TOL `1e-6`); output **CP-EVEN** if `CS ≡ 0`,
**CP-ODD** if `CS ≡ ¼`, **NOT-2-TORSION** otherwise (a failure); for a non-amphichiral manifold
the bit is **UNDEFINED-CHIRAL** (the ℤ/2 is symmetry-given and does not exist without the
symmetry — m208 has `CS = 0` yet carries no bit).

**Computed result (results.json): the object m004 sits at the identity element.**

> **PREDICTION P: bit(object) = CP-EVEN.**

The discriminating sibling m003 (same volume, same trace field ℚ(√−3), same |Sym|) sits at the
other element: bit(m003) = CP-ODD — computed, not assumed. The prediction is therefore contingent
(tier (ii) of B1226's three-tier form): the symmetry forces the ℤ/2, the object's datum selects
the element.

## D2 — The two-outcome criterion (reader side, abstract)

The reader-side bit is read **per channel** from the measured CP-sector configuration, at a
significance threshold **fixed before any value is consulted**: `Z* = 5` (the community-standard
discovery threshold; frozen here so it cannot be tuned after seeing data).

For a designated CP channel, the measured configuration is classified as exactly one of:

| label | meaning | bit |
|---|---|---|
| `CONSISTENT-WITH-CP-EVEN-POINT` | the measurement is compatible (within `Z*`) with the sector sitting at some CP-conserving point of its configuration space | **CP-EVEN** |
| `EXCLUDES-ALL-CP-EVEN-POINTS` | the measurement excludes every CP-conserving point of the sector at ≥ `Z*` | **CP-ODD** |
| `UNRESOLVED` | neither of the above at `Z*` | **no bit; comparison VOID for that channel** |

"CP-conserving point" means the set of configurations invariant under the CP transformation of
that sector, characterized **invariantly** (for flavor channels: the vanishing of the sector's
rephasing-invariant CP-odd quantity; for the gauge-topological channel: the CP-invariant points
of the vacuum-angle circle). No element of these sets is named numerically here, and this design
does not state — and its author has not consulted for this purpose — which label any real channel
currently earns.

**Both outcomes are reachable** (MB12): the label set contains both bit-bearing labels, nothing
in the design privileges either, and `bite_control_design.py` (run, PASS) exhibits the criterion
returning each element on hypothetical inputs, plus the abstain path.

**Channel designation, made on type grounds only.** The object emits ONE bit; the design must say
what it is compared against, and must choose *before* execution, *without* consulting measured
status:

- **Primary channel: the gauge-topological (θ-type) CP sector.** Type grounds: B813's Cell 0
  established that the one *legitimate* bridge between Chern–Simons quantities and 4d physics is
  the θ-vacuum construction, where a CS functional grades the vacuum sector — i.e., the
  gauge-topological channel is the channel whose CP-even/CP-odd structure is *natively* a
  statement about a CS-graded configuration space. The bit question "does the sector sit at a
  CP-even point" is a vacuum-configuration question there, matching the object's bit in kind.
- **Secondary readings (recorded, not primary): the two flavor-mixing CP channels**, each read as
  the bit "does the sector's rephasing-invariant CP-odd quantity vanish", with the same
  three-label criterion. Recorded because box D has three members and suppressing two would be a
  post-hoc choice; secondary because "CP-even point" is only basis-independent there via the
  invariant, one type-conversion step away from the object's bit.
- The primary/secondary split is frozen now. An executed comparison reports all three labels but
  the *verdict-bearing* comparison is the primary channel. Disagreement between primary and
  secondary channels is reported as-is, not reconciled.

**Verdict rule at execution:** MATCH if bit(reader, primary) = CP-EVEN (= prediction P);
MISMATCH if bit(reader, primary) = CP-ODD; VOID if UNRESOLVED. A MISMATCH is a *powered negative
against the type-matched question* — the design commits to reporting it as such, not to
reinterpreting it.

## D3 — The B813 clause: why this does not re-enter the refuted coefficient slot

B813 refuted `CS(m004) = θ_QCD` on three independent type mismatches: **kind** (computed
invariant vs free coupling), **group** (PSL(2,ℂ) vs SU(3)), **slot** (in `e^{iθW(A)}` the CS
object occupies the *functional* slot, so a CS quantity cannot also be the *coefficient*). That
refutation is the governing theorem of this design and stands untouched. This design does not
re-enter the refuted slot, for three matching reasons:

1. **No value crosses.** The comparison equates no number with no number. It compares an element
   of an abstract two-element set (the coset of the torsion subgroup that `CS` lies in) with an
   element of another abstract two-element set (CP-even/CP-odd configuration class), under the
   stated correspondence *identity element ↔ CP-conserving*. In particular a MATCH would **not**
   imply any value of any coupling — `CS ≡ 0` maps to "some CP-even point", a *set*, not a
   number. The coefficient slot is never written to.
2. **The groups never meet.** No map PSL(2,ℂ) → SU(3) is invoked or needed: the object-side bit
   is read entirely on the manifold side, the reader-side bit entirely on the physics side; only
   the two ℤ/2 labels are compared. B736's equivariance wall is not crossed because nothing
   equivariant is asserted.
3. **Kind is respected, per B303.** The bit is not the coupling; it is the *sign/parity datum* of
   the CP sector, and B303 proved that datum is carried by the sign of CS on the object side. The
   design connects parity-datum to parity-datum — the connection B1226 Cell 3 noted was "never
   used" — not invariant to coupling, which is the connection B813 closed.

Failure mode retained honestly: if a future audit shows the bit-level correspondence *itself*
smuggles a value (e.g., if "CP-even point" cannot be characterized without naming a coefficient
value), the design is VOID, not patched.

## D4 — The Gate 5 clause

- This design is **HELD**. It is executed **only on the owner's explicit election**, by a reader
  seat, not by this cell.
- No measured value is named, looked up, or used anywhere in this cell (scripts included). The
  reader-side inputs are the three abstract labels of D2; assigning a label to a real channel
  requires consulting measurement and is therefore, by definition, execution.
- The object side (D1) was computed **before** this design was written, and the design's
  prediction P is copied from that computation — the B1224/B303-mandated ordering (object first,
  world never, until election).
- At execution, the reader must record the label assignment *with citations* and apply D2's
  frozen `Z*` and the frozen primary-channel designation. Any change to `Z*`, the labels, the
  channel designation, or the correspondence after seeing measured status voids the execution.

## D5 — The bite control (RUN, in this cell, on hypotheticals)

Named control: **the same criterion applied to a hypothetical object at `CS = ¼` must output
CP-ODD.** Run in `bite_control_design.py`: `object_bit(0.25) = CP-ODD` — **PASS**. (And realized
non-hypothetically by m003 in HALF 1: the actual sibling reads CP-ODD, 0.250000000 at both
precisions.) Additional two-sidedness controls, all PASS: object side can also fail
(NOT-2-TORSION at 0.1; UNDEFINED-CHIRAL for a chiral input), reader side reaches both bits and
the abstain, and the comparison expresses both MATCH and MISMATCH.

A criterion under which the m003-shaped hypothetical could not read CP-ODD, or under which
MISMATCH were unreachable, would be vacuous; this one is not.

---

*Sealed by cell T2_cp_bit, 2026-09-01. Any execution must cite this file verbatim.*
