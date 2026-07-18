# CELL L2 — the inert-5 Bianchi rederivation (exact group theory)

Probe from the arithmetic meditation (B680): rebuild the hearing group as a
Bianchi congruence quotient at the inert prime 5, and test whether the
"bifocal picture is monofocal one level up" reading survives exact scrutiny.

All arithmetic below is exact (integers / finite fields). Verifier:
`verify_inert5.py`. Two-outcome discipline; a generic embedding is a NO-HIT.

## (a) 5 inert => residue field F_25 — CONFIRMED

- O_{-3} = Z[w], w=(1+√−3)/2, Eisenstein min poly x²−x+1.
- Legendre(−3 | 5) = **−1** ⇒ x²−x+1 is irreducible mod 5 (no roots mod 5)
  ⇒ (5) is **inert** ⇒ O_{-3}/(5) = F_5[x]/(x²−x+1) = **F_25**. ✓
- 3 ramifies (3 | disc = −3); level 15 = ramified(3) × inert(5) of the one
  being field. (Restates B680 fact 2; independently reproduced.)

## (b) A5 / 2I inside PSL2(F_25) — EMBEDS, but not by the golden mechanism

- |SL2(F_25)| = 25·24·26 = 15600; |PSL2(F_25)| = **7800** (=25·24·26/2).
- |A5| = 60 divides 7800 (quotient 130); |2I| = 120 divides 15600 (÷130).
- **Explicit embedding (exact, constructed):** ⟨S,T⟩ ⊂ SL2(F_5) closes to
  order **120**; mod ±I it is order **60 = A5**. Since F_5 ⊂ F_25, this A5
  sits in PSL2(F_25) as a **subfield subgroup**, and SL2(F_5) (order 120,
  center Z/2, quotient A5) **≅ 2I** — the binary icosahedral group lives in
  its OWN defining characteristic 5.

### The crux: sqrt5 in F_25 is DEGENERATE (the golden shadow fails at 5)

The "golden/hearing shadow" reading wants A5 to enter via √5 ∈ F_25
(the icosahedral golden ratio). At p = 5 this **degenerates**:
- char 5 ⇒ 5 ≡ 0 ⇒ √5 = 0 (not a genuine √5).
- golden poly x²−x−1 mod 5 has disc = 5 ≡ 0 ⇒ **double root φ = φ̄ = 3**:
  the two golden conjugates collide because **5 RAMIFIES in Q(√5)**.
So the mechanism the probe hopes for is exactly the one that collapses at 5.
A5 enters instead by the **defining-characteristic subfield** route
(PSL2(5) ⊂ PSL2(25)), which is a different — and arguably deeper — fact:
5 is the icosahedron's home prime.

## (c) Congruence quotient at (5) — A5 is a SUBGROUP, not the quotient

Reduction PSL2(O_{-3}) → PSL2(O_{-3}/(5)) = PSL2(F_25) is the level-(5)
congruence quotient; by strong approximation it is onto. So the congruence
quotient **is PSL2(F_25) (order 7800)**. A5 (60) is a **subgroup** of that
quotient, **not** the quotient itself. "The hearing group arises AS a
congruence quotient at 5" is therefore FALSE as stated; "arises as a
subgroup of the congruence quotient" is TRUE.

## BASE-RATE DISCIPLINE — the embedding is generic (NO-HIT)

A5 < PSL2(q) iff q ≡ 0, ±1 (mod 5) (Dickson). For q = p²: every prime p≠5
has p² ≡ ±1 (mod 5), and p=5 has the subfield route — so **A5 < PSL2(p²)
for EVERY prime p** (verified p = 2..31). The embedding carries ~0
discriminating information about 5 being the inert prime; it holds at every
p². What IS special to p = 5 is the *opposite* of the golden framing: the
√5 mechanism degenerates and only the defining-characteristic 2I ≅ SL2(5)
survives.

## VERDICT

- Exact group facts: **CONFIRMED** — 5 inert ⇒ F_25; |PSL2(F_25)| = 7800;
  A5 and 2I ≅ SL2(5) embed via the subfield F_5 ⊂ F_25.
- Interpretive "bifocal = monofocal one level up via the golden √5 shadow":
  **NOT SUPPORTED.** √5 = 0 is degenerate in char 5 (5 ramifies in Q(√5),
  golden ratio → double root 3); A5 embeds in PSL2(p²) for *all* p
  (base-rate zero); and A5 is a subgroup, not the congruence quotient
  (which is all of PSL2(F_25), order 7800).
- Salvage (genuinely special to 5, registered not overclaimed): 2I ≅ SL2(5)
  is the *defining-characteristic* icosahedral coincidence — 5 = the
  icosahedral prime. If the program wants a monofocal reading, this is the
  honest hook, distinct from and incompatible with the √5-shadow story.
