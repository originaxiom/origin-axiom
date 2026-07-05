# B436 — C1: the child's identity card — the Borel identity EXACT (coefficient 12); the forced child is arithmetically special vs generic knots (but class-shared with 5₂ — B438)

**Status: banked (C1), then CORRECTED (B438, 2026-07-05 audit). The Borel identity and all
exact numbers stand; the "special field" reading is refined — the −283 field is a
commensurability-class property shared with 5₂(5,1), not figure-eight-unique. Firewalled.**

## The Borel identity (registered outcome: IDENTITY FOUND)

    vol(child) = 12 · |d_K|^{3/2} · ζ_K(2) / (4π²)³,   K = ℚ[x]/(x⁴−x−1), d_K = −283

verified to **|ratio − 12| = 4.5×10⁻⁶⁴** (snappy HP volume × sage Dokchitser ζ_K(2) at 260
bits). The child's volume IS its trace field's zeta value up to the rational 12 — the
arithmeticity of the Meyerhoff manifold verified computationally in-repo (prior art: Chinburg's
arithmetic Meyerhoff — flagged; the in-repo content is the exact verification + the pinned
coefficient). K has signature (2,1) — exactly one complex place, as arithmeticity requires.

## CS (registered outcome: NOT identified — honest)

CS(child) = 0.0770381802637702225443959018109… (HP). No small rational (best cheap candidate
103/1337 fails at 3.5×10⁻⁸); no closed form claimed. Recorded as the open C1 residue.

## The control (leg iv — SLOPE control passes; FOREIGN control corrects the reading — see B438)

The unforced sibling 4₁(7,1): trace-field search finds NO field through degree 14 (vs the
child's degree 4). The forced filling lands on an arithmetic child with a tiny field; the
unforced sibling is generic. The child's specialness is slope-specific — the bar's slope-control
leg passes.

**But this bud shipped with only the SLOPE control and skipped its own pre-registered FOREIGN
control** (a foreign hyperbolic knot at slope 5) — the exact omission that sank B437's "golden
return." The 2026-07-05 audit ran it (B438): **5₂(5,1) also gives x⁴−x−1, disc −283** — the
child's "arithmetically special" field is **shared with 5₂**, so it is a *commensurability-class*
property, not figure-eight-unique. 6₁(5,1), m003(5,1), m007(5,1) give different fields, so the
child is still special *relative to generic knots* — but "arithmetically special child" must
read "special vs generic, class-shared with 5₂," not "the figure-eight's fingerprint." The
distinction {4₁ special vs 6₁ generic} is real; the identification {−283 ⇔ figure-eight} is
retracted. See [[B438]].

## For the campaign

The child now has: H₁ = ℤ/5 (B435), 26 abelian E₆ vacua (25 nontrivial + trivial, B435), disc −283 quartic (B434),
the exact zeta-volume identity (this bud), CS unit recorded. Next floors: the abelian torsion
book (C2 — the parent's Alexander at ζ₅), the SL(2) vacuum book (C3).

**Provenance.** c1_card.sage / c1hp.sage / c1z.sage (snappy+sage); founding values in
founding.json (B435); lock tests/test_b436_child_identity.py (field facts via sympy; the
sage-side numbers locked from this bud's JSON).
