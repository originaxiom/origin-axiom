# B436 — C1: the child's identity card — the Borel identity EXACT (coefficient 12), and the forced child is arithmetically special

**Status: banked (C1). Two-outcome readings resolved as registered. Firewalled.**

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

## The control (leg iv — PASSES)

The unforced sibling 4₁(7,1): trace-field search finds NO field through degree 14 (vs the
child's degree 4). The forced filling lands on an arithmetic child with a tiny field; the
unforced sibling is generic. The child's specialness is slope-specific — exactly what the
bar's control leg demands.

## For the campaign

The child now has: H₁ = ℤ/5 (B435), 25 = 5² abelian vacua (B435), disc −283 quartic (B434),
the exact zeta-volume identity (this bud), CS unit recorded. Next floors: the abelian torsion
book (C2 — the parent's Alexander at ζ₅), the SL(2) vacuum book (C3).

**Provenance.** c1_card.sage / c1hp.sage / c1z.sage (snappy+sage); founding values in
founding.json (B435); lock tests/test_b436_child_identity.py (field facts via sympy; the
sage-side numbers locked from this bud's JSON).
