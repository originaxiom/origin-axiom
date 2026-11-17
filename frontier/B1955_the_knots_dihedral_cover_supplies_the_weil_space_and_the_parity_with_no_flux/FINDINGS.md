# B1955 — The knot's dihedral cover supplies the Weil space and the parity with no flux; the frame does not see the Weil class, and the knot's own is x²/5; the up coupling as the top wedge is invariant at level 5

**Verdict: PROVED** (the computed statements; exact group theory, SnapPy for the covers' homology; the web seat's W-A3
recomputed on main's own code, with the facts main found first). Main, 2026-11-17. What it means for the count of
inputs is a reading, stated as such. No measured number is used. Register rows P-866 and P-863. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /dihedral|deck group|deck transformation|linking form|discriminant form|top wedge|Seifert form|Seifert matrix|double branched|Hecke.s period|Humbert/: 15 of 1695 arcs on main match (NEGATIVE 2, OPEN 1, PROVED 12); 3 register rows match (DONE 1, QUEUED 2)`.
- **What the record already holds:**
  - **B1884, B1943, B1952:** the act fixes exactly one line of order 5, and at no other prime.
  - **B1733:** the lines a thread fixes up to sign are the points of coker(A ∓ I), which one of its readers gave as the
    first homology of the thread's double branched cover. So the link between the fixed line and that cover is on
    record; its use as the source of the module is not.
  - **B1951, B1952:** the Weil space of level 5, its centre's split, the lines as its Weyl operators; postulate D as four
    counted bits, the first of them the flux bit.
  - **B1953:** the down coupling as one covariant operator; the up sector's phases of order 25.
  - **THE_FRAMEWORK:** the ℤ/2 orbifold of the figure-eight is spherical, with L(5, 2). **B794:** the knot group is
    congruence of level 4.
- **What is new here:** the dihedral cover as the source of the module (main's hypothesis F-A of P-866, tested by the web
  seat's W-A3, harvest row 1866); which Weil class the object carries and that the frame does not see it; the up
  coupling as the top wedge.
- **The literature:** a knot has a dihedral representation onto D_p exactly when p divides its determinant, and it
  factors through the first homology of the double branched cover (Fox); the irregular dihedral cover of a two-bridge
  knot has (p + 1)/2 boundary components over the knot, with branching 1, 2, …, 2 (Perko; Burde); the Weil
  representation of a finite quadratic module (standard). Nothing here is new as mathematics.

## The results (`verification/wa3_on_main.py`)

| part | result |
|---|---|
| A, the prime | the figure-eight's group maps onto the dihedral group of order 2p only at **p = 5**, among the odd primes to 31. It does not map onto the dihedral group of order 50 |
| B, the cover | on the five sheets the longitude acts trivially and the meridian is an involution fixing one sheet. **The cusp has three preimages, of degrees 1, 2, 2** |
| B, the deck groups | the 5-sheeted cover of m004 has **no deck transformations** (the image's centraliser in S₅ is trivial). Over the double cover the five rotations commute with themselves: **the shifts, a group of order 5** |
| C, homology | the double cover: ℤ/5 + ℤ. The 3-cusped 5-sheeted cover: ℤ³, no torsion, five times the volume; SnapPy identifies it as the complement of the link 8³₄ |
| D, the two Weil classes | for T = diag ψ(x²) and for T = diag ψ(2x²): 120 elements, **determinant 1 on all**, ρ(−I) = P. An element in the act's class is never a scalar times P (least distance 0.553). **Every exterior power's T-spectrum is in fifth roots** |
| D, does a class show in the frame | the signature tr R(T²)/tr R(T)² is +1/5 for a class with its own conjugate and −1/5 for mixed classes. **On the frame's 25 lines it is +1/5** |
| E, the knot's form | V + Vᵀ = [[2, 1], [1, −2]], determinant −5, signature 0. Its discriminant form is **q = x²/5**; its bilinear form is 2x²/5. B1951's ρ(T) = diag ψ(2x²) is the other class |
| F, level 25 | x² − 3x + 1 has one root mod 5 and **none mod 25**. Frame C's up phases are of order 25, its down phases of order 5 (B1953). q_L² + q_R² mod 5 is 0 for down and leptons and 2 for up |

## What it means

**1. The cover replaces the flux, for the module and the gauge group.**
- W is the functions on the five sheets. The shifts are the deck transformations over the double cover. The clocks are
  the characters of that group, which are twists by the act's fixed line. They commute up to ζ as a group and its
  characters do, with no magnetic field.
- The meridian acts as the parity P, which is all B1951's gauge group uses. The 3 is the functions on the three
  preimages of the cusp.
- The cover exists only at p = 5, the knot's determinant. So the level, the module and the split 3 + 2 are one
  topological fact about the knot.
- **Three limits (the web seat's, confirmed):**
  - the shifts are deck transformations over the double cover, not over m004 itself;
  - the clocks are twists over the double cover only, since the act inverts the fixed line's character;
  - the cover supplies the parity and not the act's own Weil operator: it sees the act's semisimple part, −1, and not
    its unipotent part.

**2. The frame does not see the Weil class, and the knot's own is x²/5.**
- The frame's lines transform as End(W) does, and End(W) is the same in both classes. So B1953's statement that the
  operator transforms by B1951's representation fixes an identification of the labels, not a class. With the other
  identification the same operator transforms by the other class.
- The class belongs to the quadratic form on the shift group. That group is the first homology of the double branched
  cover, and it carries the knot's own form, x²/5, of signature 0.
- B1951's convention, 2x²/5, is the class of SU(5) at level one and of the flux-5 modes. It differs from the knot's by
  a factor of 2. B1951's split, commutant and hypercharges are the same in both classes. Its T-phases on the 3 change
  from 0, 2/5, 3/5 to 0, 1/5, 4/5.

**3. The up coupling, wedged to the top degree, is invariant at level 5.**
- Two fields in Λ² and the Higgs in Λ¹ wedge to Λ⁵, which transforms by the determinant, and the determinant is 1 on
  the whole group. So the coupling closes at level 5, in either class.
- Frame C's up sector has 25th roots only because frame C puts each field's charge into its theta characteristic. In
  the exterior algebra the charge is the centre's eigenvalue and not a multiplier on the level-5 label.
- The object supplies nothing of level 25: the act keeps no line mod 25, and there is no dihedral group of order 50.
- **So B1953's "specification" for the up sector is answered:** the up coupling needs no structure of level 25 if it is
  the top wedge. It needs it only inside frame C's construction.

## The web seat's W-Z1, on where ζ sits in the object (harvest row 1867; `verification/wz1_checks.py`)

Opened at the author's request to that seat. Read in full; two of its identities checked by main.

| its statement | main's check |
|---|---|
| Hecke's period of the Eisenstein series along the act's closed geodesic is 5^(s/2)·Γ(s/2)²/Γ(s)·ζ(s)L(s, χ₅)/ζ(2s) | at s = 2, by a direct lattice sum integrated over one period: 11.616695 against 11.616712 (1.5e-6, the sum's cut) |
| m004's volume is 12·3^(3/2)·ζ_K(2)/(4π²), K = ℚ(√−3) | 2.029883212819307250042 on both sides (4e-31) |
| the knot group is congruence of level exactly 4 | on record (B794); not recomputed here |
| the cusp's scattering is governed by ζ(s)L(s, χ₋₃) | its reading, not computed by it or by main |

- **Its own verdict, which main shares:** ζ is built into the object in two classical places, the act's geodesic and
  the cusp, so a zeta value or a zero in a frame output is first to be suspected of being Hecke's formula. Neither of
  the recent preprints it read touches the object.
- **Not verified by main:** the preprints it cites. They are later than anything main can check, and unrefereed by its
  own account.
- **Its proposed control** (name the property that separates the object from its rivals, and run each step on a rival
  without it) is the control B1951 and B1952 already used. It is taken as a standing check, not as a result.

## What it does to the count (a reading)

- B1952 left postulate D as four counted bits. The first was the flux, with the reading that the modes' Fock space
  labels matter.
- **The flux is replaced by the cover**, which is the knot's own. **The Fock-space reading is not replaced:** with flux
  it came with the fermion zero modes; with the cover it stands alone, as the statement that the exterior algebra of
  the functions on the sheets is the matter space. It stays counted.
- The chirality, the gauging and the Higgs's place stay counted. The scoreboard is not changed by this arc.

## What is open

- **Two descriptions of the couplings, not yet joined.** In the exterior algebra the level-5 part of a coupling is an
  invariant tensor and carries no hierarchy. In frame C the coupling varies over the 24 points and assembles into an
  operator on families ⊗ W with a non-trivial part on W (B1953). Whether frame C's operator is the first with a
  further field in the adjoint, or a different construction, is not known.
- **The Fock-space reading** has no source in the cover.
- **B1951's convention** is not re-based here. A dated note there records the knot's class.

## Not claimed

- That the count of inputs has fallen.
- That the cover's three cusps are colour in any sense beyond the split of the parity.
- That frame C's up sector is wrong. It is a different construction from the top wedge, and which the object uses is
  open.
- Any value, and any comparison with data.
