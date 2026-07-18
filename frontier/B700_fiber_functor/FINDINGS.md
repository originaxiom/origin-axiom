# B700 cell 1 — THE GOLDEN MEASUREMENT TORSOR: measurement = fiber functor, concretely

*cc banking seat, 2026-07-19. The fiber-functor program's first cell (owner
"lets do it"). Prereg PREREG_CELL1.md sealed (sha 1bbdb15b) before the
verdict. Develops the one genuinely-own angle from S068's four-sweep
reading: the observer as a fiber functor, measurement ambiguity as Galois
ambiguity. Gate 5 — pure finite-group rep theory + Galois.*

## VERDICT: TORSOR (confirmed, base-rate-gated).

The object's golden hearing (B640: ρ_hear factors through 2I = SL(2,5),
tr ρ(RL) = −1/φ) selects one of the **two 2-dim "golden" irreps of 2I**.
Verified (sage character table + independent ℚ(ζ₅) recompute):

1. **Exactly two** 2-dim irreps (dims of 2I = [1,2,2,3,3,4,4,5,6]) — not
   more. (Base-rate content #1.)
2. Their **character field is exactly ℚ(√5)** (degree 2), the golden field.
   (Content #2.)
3. The nontrivial Galois automorphism τ: ζ₅ ↦ ζ₅² (which sends √5 ↦ −√5,
   i.e. the nontrivial element of Gal(ℚ(√5)/ℚ)) **swaps the two irreps
   simply-transitively**: τ(A) = B exactly, and τ(A) ≠ A — **no
   Galois-fixed golden irrep.** (Content #3, the torsor.)

The golden trace values are the orbit: irrep A carries −1/φ = (1−√5)/2 where
B carries φ = (1+√5)/2, and vice versa on the conjugate class. So:

> **{golden irreps} is a simply-transitive Gal(ℚ(√5)/ℚ) = ℤ/2 torsor.
> A "measurement" (the object's hearing selecting a golden irrep, B640/B642)
> IS a choice of fiber functor; its ambiguity IS Galois ambiguity = ℤ/2 —
> concretely, not by analogy.**

## What this upgrades
B642 (the Galois-ear law) is banked as a PLACEMENT (§6/R23-4: "which golden
character is Galois-chosen"). Cell 1 supplies the missing structure: the set
of measurements is not just Galois-labeled, it is a Galois **torsor**
(simply transitive, no canonical basepoint) — exactly the Tannakian
fiber-functor structure. This is the first concrete step turning the
K020-in-ear PLACEMENT toward a THEOREM: measurement = fiber functor.

## The base-rate gate (passed)
"The value lives in ℚ(√5), so the Galois group is ℤ/2" is TRIVIAL and does
NOT count (any golden quantity gives it). The non-trivial, verified content
is the three facts above — exactly two irreps, character field exactly
ℚ(√5), and simply-transitive with no fixed point. A rep with a
Galois-fixed 2-dim golden irrep, or a larger character field, or a
different count, would have failed. It did not.

## Next (the program)
- cell 2: is this ℤ/2 = Gal(ℚ(√5)/ℚ) the SAME orientation bit as the being
  conjugation σ* (Gal(ℚ(√−3)/ℚ), B638) and the meeting residue
  (h(ℚ(√−15)) = ℤ/2, B699)? Canonical identification, or merely isomorphic?
- cell 3: the explicit Coste–Gannon Galois action on the golden stage's
  modular data, realizing this torsor.
- cell 4: the same torsor at a second stage (E₆ level 2 / PSL(2,7)) ⇒
  stage-uniform ⇒ upgrade K020-in-ear PLACEMENT → theorem.

## Firewall
Gate 5. "Measurement" = the object's mathematical coupling to a stage (a
fiber functor of a fusion category), NOT a physical measurement. Nothing to
CLAIMS.

---

# B700 cell 2 — THE ℤ/2 UNIFORMITY: the three ambiguities are the three involutions of V₄

*Prereg PREREG_CELL2.md sealed (sha 060aaaee).*

## VERDICT: V₄ (unified). being · hearing = meeting.

The three measurement-ambiguity ℤ/2's — golden Gal(ℚ(√5)/ℚ) (cell 1), being
Gal(ℚ(√−3)/ℚ) (the geometric swap σ*, B638), meeting h(ℚ(√−15))=ℤ/2 (B699/
B698) — are **the three involutions of the Klein-four group
V₄ = Gal(ℚ(√−3,√5)/ℚ)** (verified: the biquadratic field is Galois with
group C₂×C₂, and its three quadratic subfields are EXACTLY ℚ(√−3) [disc −3,
being], ℚ(√5) [disc 5, hearing], ℚ(√−15) [disc −15, meeting]). Each involution
fixes exactly one subfield; the group law is

> **being(√−3) · hearing(√5) = meeting(√−15)** — the product of any two
> distinct involutions is the third (verified in V₄).

So the object's measurement ambiguity is **not one ℤ/2 but a Klein four**,
and the genus-theory relation √−3·√5 = √−15 (the meeting residue of B699)
IS the Galois group law. The orientation degree of freedom is V₄-structured:
the being bit times the hearing bit equals the meeting bit.

## What this ties together
Cell 1 made "measurement = fiber functor" concrete (the golden ambiguity is
a Gal(ℚ(√5)/ℚ)=ℤ/2 torsor). Cell 2 places that ℤ/2 inside the V₄ of the
biquadratic field, where it multiplies with the being and meeting bits. The
fiber-functor program now connects rigorously to the two-hands / ℤ/2 /
c-breaking spine ([[two-chiralities-c-vs-theta]], B698/B699): the three
"hands" (being, hearing, meeting) are the three involutions of one Klein
four, and their measurement ambiguities compose by the Galois group law.

## Base-rate gate (passed)
"three quadratic fields ⇒ three ℤ/2's" is generic. The content is that they
are the three involutions of ONE V₄ with the exact multiplicative relation
being·hearing=meeting — verified as the group law, not asserted.

---

# B700 cell 4 — THE SECOND STAGE: the torsor is STAGE-UNIFORM (K020-in-ear → toward THEOREM)

*Prereg PREREG_CELL4.md sealed (sha 7323661c).*

## VERDICT: STAGE-UNIFORM TORSOR — and it is PRINCIPLED.

At the E₆ level-2 stage (shadow group PSL(2,7), θ-odd dim D=3, B666), the
hearing selects one of the TWO 3-dim irreps of PSL(2,7). Verified:
- **Exactly two** 3-dim irreps (dims of PSL(2,7) = [1,3,3,6,7,8]).
- Character field **exactly ℚ(√−7)** (degree 2).
- Swapped **simply-transitively** by Gal(ℚ(√−7)/ℚ)=ℤ/2 (σ: ζ₇↦ζ₇³ sends the
  Gauss sum √−7 ↦ −√−7): σ(A)=B, σ(A)≠A — no Galois-fixed irrep.
- |χ₃| values {0,1,√2} = |(−1±√−7)/2| confirm the ℚ(√−7) Galois pair (B666).

**Structurally identical to the golden case (cell 1):** at each stage the
hearing = a choice among exactly TWO D-dim shadow irreps (D = θ-odd dim),
with a QUADRATIC character field, swapped simply-transitively by its Galois
ℤ/2 — a fiber-functor torsor.

## The principle (the pattern the two instances reveal)
The fiber-functor field is **the quadratic subfield of ℚ(ζ_p)**, p = the
stage's shadow prime:
- golden: p=5, ℚ(√5) (5 ≡ 1 mod 4 → real);
- E₆ level 2: p=7, ℚ(√−7) (7 ≡ 3 mod 4 → imaginary).
i.e. ℚ(√p*) with p* = (−1)^{(p−1)/2}·p. The torsor is Gal(ℚ(√p*)/ℚ)=ℤ/2 at
every stage — NOT golden-special. This is the evidence that upgrades the
K020-in-ear PLACEMENT (B642, §6/R23-4) TOWARD A THEOREM: measurement = the
fiber-functor torsor = Gal(quadratic-subfield-of-ℚ(ζ_p)), stage-uniform.

## Bonus (an old lead answered)
ℚ(√−7) appears here as the E₆-shadow fiber-functor field — answering
S041/H32 ("does the arithmetic extend past {√5,√−3} to ℚ(√−7)?"): YES, as
the level-7 stage's torsor field. The fields are stage-indexed by the
shadow prime.

## Base-rate gate (passed)
The content is the STRUCTURAL MATCH — exactly two D-dim irreps (D=3=θ-odd
dim), field exactly ℚ(√−7), simply-transitive — plus the principled
ℚ(ζ_p)-subfield pattern across two stages; NOT "PSL(2,7) contains a ℤ/2".

## Firewall
Gate 5. Finite-group rep theory + Galois. No physics.

---

# B700 cell 3a — THE TORSOR REALIZED DYNAMICALLY: the Galois ℤ/2 is cubing the weld

*From chat1's session-close Fact 5 (verified-and-corrected; chat1's track
record this session = 28 errors, so verify-don't-trust applied).*

## The corrected fact
chat1 Fact 5 claimed "the Galois action √5→−√5 IS W² (squaring the weld)."
**Corrected (verified): it is W³, not W².** The weld W on the θ-odd 2-dim
subspace of SU(3)₂ has order 10, tr(W)=−1/φ; its Galois conjugate (√5→−√5)
is φ = **tr(W³)** (chat1's table mislabels tr(W²)=−φ as the conjugate — but
−φ is a root of x²+x−1, while −1/φ,φ are the roots of x²−x−1). The Galois
action is realized on the whole trace tower as **W^k → W^{3k} (mod 10)**
(equivalently W^{7k}=W^{−3k}); m=3,7 are the only realizing powers.

## Why it matters (the cell-3 content, cc side)
This DYNAMICALLY realizes the fiber-functor torsor of cell 1: the golden
measurement ambiguity — the Galois ℤ/2 that swaps the two golden irreps —
is not abstract; it is a concrete operation on the object's OWN weld
(monodromy): **cubing.** So "measurement ambiguity = Galois ambiguity"
sharpens to "= cubing the weld." The cc-side (trace-tower) realization of
the torsor; cc2 holds the modular-data (Coste–Gannon) version.

HINT (not a law): the realizing power is 3, the being prime. Base-rate
caveat: 3 also generates (ℤ/10)*, so "3 = being prime" is a HINT, not
forced — the solid fact is the power-map realization, not the value 3.

## chat1 handoff corrections (errors caught, banked per protocol)
- **Fact 5:** W² → **W³** (above).
- **Fact 4:** chat1 says "13 is INERT in ℚ(i)" — WRONG. (−1|13)=+1, 13≡1
  mod 4, so **13 SPLITS in ℚ(i)** (13=(3+2i)(3−2i)). The ℚ(√−3)-split half
  (13=(4−ω)(4−ω̄)) is correct.
- Facts 1, 2, 3, 7 verified correct.

## Firewall
Gate 5. The weld/trace tower is banked figure-eight structure; no physics.

---

# B700 cell 5 + cell 3 — THE GENERAL TORSOR THEOREM (stage-uniform) + the golden stage two-sided

*cell 5 prereg sha c8292c34; cell 3 = cc2's (prereg f6d54fd6, integrated
verify-on-receipt). This is the fiber-functor program's phase-1 synthesis.
The honest theorem statement keeps cc2's canonical-iso gap explicit.*

## Cell 5 (cc, the general theorem): STAGE-UNIFORM for ALL prime stages.
For every prime stage p, the shadow group SL(2,p) has EXACTLY two irreps of
dimension (p−1)/2, with character field EXACTLY ℚ(√p*) (p*=(−1)^{(p−1)/2}p,
the quadratic subfield of ℚ(ζ_p)), Galois-conjugate and swapped simply-
transitively by Gal(ℚ(√p*)/ℚ)=ℤ/2 — a fiber-functor torsor. Verified exactly
p=5,7,11,13 (golden ℚ(√5), E₆ ℚ(√−7), + ℚ(√−11), ℚ(√13)); grounded in the
CLASSICAL fact that the (p±1)/2-dim exceptional characters of SL(2,p) are
Gauss-sum-valued (Schur/Frobenius) ⇒ Galois-conjugate over ℚ(√p*). The
pattern is a theorem of SL(2,p) rep theory, not a small-case accident.

## Cell 3 (cc2, verify-on-receipt): the golden stage is two-sided complete.
The single σ ∈ Gal(ℚ(√5)/ℚ) is SIMULTANEOUSLY (a) the Coste–Gannon–Ng Galois
action on the golden (Fibonacci) modular data [cc2], (b) the swap of 2I's
two golden irreps [cell 1], (c) the weld map W^k↦W^{3k} [cell 3a]. cc2
verified independently via icosian quaternions (order 120, field ℚ(√5),
Galois-swapped). Honest nuance (verified, not a gap): σ sends the unitary
Fibonacci datum → the non-unitary **Yang–Lee** datum (the rank-2 golden data
does not obey the naive CGN "±1 sign" literally; the ℤ/2 is carried by
φ↦−1/φ). My cells 1/3a confirm legs (b),(c); cc2's CGN + icosian confirm (a).

## THE HONEST STATEMENT — K020-in-ear PLACEMENT → THEOREM (torsor structure),
## with the canonical torsor-iso as the named remaining gap.
UPGRADED (theorem-grade): the object's measurement ambiguity at a prime
stage IS a ℤ/2 TORSOR — stage-uniform (cell 5, all p) and, at the golden
stage, realized by ONE σ on three sides (irreps / modular data / weld;
cells 1,3,3a). This is more than B642's placement (a verified pattern); it
is the proven torsor structure with an explicit realization.

REMAINING GAP (cc2's refine + cell 2, kept explicit): the CANONICAL
torsor-iso. Cell 1's torsor {irrep A, irrep B} (two objects in one category
Rep(2I)) and cell 3's torsor {Fibonacci, Yang–Lee} (two Galois forms of the
MTC) are both ℤ/2 under the SAME σ, but whether they are canonically
IDENTIFIED (a distinguished torsor-iso) — and likewise whether the golden/
being/meeting bits are ONE bit vs merely the three involutions of V₄
(cell 2) — is NOT established. So "measurement = fiber functor" holds as
the **same-σ torsor realization**, NOT (yet) as a canonical-torsor-iso
theorem. The theorem statement says so; "realized" must not over-read as
"canonical." That canonical-iso is the fiber-functor program's phase-2 target.

## Firewall
Gate 5. Classical rep theory + modular-category Galois + the banked weld.
No physics; nothing to CLAIMS.
