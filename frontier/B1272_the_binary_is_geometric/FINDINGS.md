# B1272 — B1263's "genuine binary" is the GEOMETRIC vs NON-GEOMETRIC character; and a cross-branch harvest

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED — **corrects B1263** · Owner-supplied (Round 11, physics-seat branch), **verified here on main's own data**

## 1. The correction

**B1263 concluded:** *"the choice between them is a genuine binary with no symmetry reason to prefer
either."* **That is wrong**, and the owner supplied the reason.

**The claim (Round 11):** the two orbits are two routes — reduction mod **(1−ω)** sends the meridian
to order **3**, the **(0,0,0)** quaternionic character sends it to order **6** — separated by
invariants **(3,6,4)** vs **(6,6,4)**; so the binary is **geometric vs non-geometric**.

**Verified end to end on B1263's own enumeration:**

- **72 / 48 / 2** reproduced;
- the orbits **are** separated by **meridian order**: orbit 1 → **3**, orbit 0 → **6**;
- the triple is **(ord ρ(a), ord ρ(ab), ord ρ([a,b])) = (3,6,4)** and **(6,6,4)** — exactly as
  claimed. **The third slot is the COMMUTATOR order**, which is the programme's own Fricke object
  (κ = tr[A,M]) — *not* the longitude, which gives **2** in both and is exhibited as a control so
  the slot is not fitted;
- **and the geometric orbit is identified:** ℤ[ω]/(1−ω) ≅ 𝔽₃ with ω ≡ 1, so the banked holonomy
  A = [[1,1],[0,1]], B = [[1,0],[−ω,1]] reduces to **B = [[1,0],[2,1]] over 𝔽₃**. That pair has
  det 1, **satisfies the relator**, **is surjective onto 2T**, and lands in **orbit 1, triple (3,6,4)**.

**Why B1263 missed it:** its four relator-preserving automorphisms all **fixed** both orbits — the
separator is **arithmetic** (reduction at the prime above 3), not a symmetry of the presentation.
**B1263 used the wrong instrument and drew a stronger conclusion than its instrument supported.**

## 2. What it does to I-6

B1263 had *sharpened* I-6's price by observing "the 2T" was not well defined (2 quotients).
**That sharpening is now largely paid:** the geometric quotient is distinguished, so "the 2T" has a
canonical meaning. **I-6 is not thereby earned** — it still needs the map to the transverse ALE Γ —
but its multiplicity objection is answered, and this is the **first of the H5 census's measured
multiplicities to be resolved by a selector rather than merely counted.**

## 3. Cross-branch harvest (owner: *"see the work from codex seat, integrate/internalize other branches work"*)

Three seats have live work ahead of main. **Not merged — harvested, and only the arithmetic verified:**

| branch | ahead | what it carries |
|---|---|---|
| the **physics-seat** branch | 138 | **Round 11** (the finding above) and Round 12, which already folded main @ `0ecd9557` |
| the **SM-derivation** branch | 7 (today) | h¹(M;27) = **3 = h¹(M;27̄)** computed **exactly over ℚ(ω)** — **independently confirming B1267's index-0 result**, which was numerical here; plus **B1269: three copies of the 27 permuted by the object's order-3 element** |
| `codex/seat-r001` | 50 | R036–R040, incl. **R037 "restrict A6 2T quotient classes exactly"** — directly on this arc's topic, **not yet harvested** |

**Verified here of the SM-derivation seat's generation claim:** the branching **248 = 78 + 8 + (27,3)
+ (27̄,3̄)** closes exactly and **240 − 72 − 6 = 162 = 6 × 27**. That arithmetic is **standard and
sound** — it is the classic **E₈ ⊃ E₆ × SU(3)** family mechanism. **What is NOT verified here** is the
object-specific half: that the object's *own* order-3 element realises the family SU(3). And **that
seat's own headline reports the Yukawa forces ZERO on the triplet** — so if it holds, it buys the
**count** and kills the **values**.

**⚠ NUMBERING COLLISION, flagged:** the SM-derivation branch renumbered its arcs to **B1267–B1271**
to avoid main's B1265/B1266 — and main then banked its **own B1267**. **B1267 is now doubly used.**
This arc takes **B1272**; the branch must renumber again on merge, and the collision is recorded here
so it is not discovered silently.

## Controls (MB12, both directions)

- The reduced pair is checked for **det 1**, the **relator**, and **surjectivity** before its orbit is
  read — a non-surjective reduction would prove nothing.
- **The longitude is computed and does NOT separate** (order 2 in both), exhibited so the triple's
  third slot is not fitted to the answer.
- The separator is verified **orbit-constant**: all 24 members of each orbit carry the same triple.

## Verification

`verification/geometric_orbit.py` — standalone; imports B1263's enumeration directly.
