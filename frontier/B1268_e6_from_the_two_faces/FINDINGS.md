# B1268 — E₆ FROM THE TWO FACES: the golden face gives E₈ (the icosians), the Eisenstein face cuts out E₆ as its orthogonal complement — with the 27, the ℤ/3 and θ falling out of the same cut — and the E₈ transport gives the 27 the slot B1267 said it lacked

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (the derivation, exact over ℚ(√5) and ℚ(ω)) + NEGATIVE (the count: the object's Eisenstein coefficient systems give one vector-like 27-pair and net zero) · **Price: unchanged at 14**

## Why this arc — the owner's correction

The assembly (B1265–B1267, `docs/THE_ASSEMBLY_2026-09-06.md`) took E₆ as handed over at link L4 — *McKay(2T) =
affine E₆* — from the **Eisenstein face alone**, and then found (B1267 §1) that with an E₆ singularity along Q
the 27 is not a field on Q. The owner's correction: *"you failed to derive E₆ from the program. Our object has
two faces, golden and Eisenstein."* The corpus has both faces as **two ends** — the product `RL` → ℚ(√5) →
2I = SL(2,𝔽₅) → E₈ (B206), the ratio `g = −RL⁻¹` → ℚ(√−3) → 2T = SL(2,𝔽₃) → E₆ (B210, K021's founding
identity), the Arnold trinity (B256), the two-ended unification (B258) — and states explicitly that *"neither
field forces the other"* (B258). **Nowhere does the corpus make E₆ a consequence of both faces at once.** This
arc does, exactly, and the consequence is not only E₆ but its 27, its ℤ/3, its outer automorphism θ, and the
transport in which the 27 lives on the manifold.

## 1. The theorem (`verification/e6_from_the_two_faces.py`, part 1; run record `verification/e6_from_the_two_faces_run.txt`)

**The golden face supplies E₈.** The 120 unit icosians — the ℤ[φ]-quaternions of norm 1, the binary
icosahedral group 2I — are generated exactly (element orders 1¹ 2¹ 3²⁰ 4³⁰ 5²⁴ 6²⁰ 10²⁴), and the icosian
ring under Conway–Sloane's Euclidean norm (EN(q) = x + y for QN(q) = x + y√5) has **240 vectors of norm 2**
(the units and φ⁻¹ times the units) spanning a lattice of **Gram determinant 1: E₈**. The two letters enter
here: **⟨R, L⟩ mod 5 = SL(2,𝔽₅), order 120**, and an explicit isomorphism SL(2,𝔽₅) → 2I is constructed
(R, L ↦ two unit icosians of order 5, the map checked well-defined on all 120 elements).

**The Eisenstein face supplies A₂ inside it.** The founding ratio **g = −RL⁻¹** (order 3, disc −3) maps under
that isomorphism to the order-3 unit icosian g_q = (−1/2, −φ/2, 0, φ⁻¹/2), and **g_q² + g_q + 1 = 0**: it
generates ℤ[ω] inside the icosians. The plane {1, g_q} has Gram [[2,−1],[−1,2]], determinant 3 — the A₂
root lattice, the Eisenstein integers.

> **E₆ = ℤ[g]^⊥ inside E₈.** Exactly **72** of the 240 roots are orthogonal to the Eisenstein plane; their
> simple roots have the **E₆ Cartan matrix** (Dynkin degrees [1,1,1,2,2,3] — one branch node, three legs),
> determinant **3**, and all 72 are integral combinations of them; **[E₈ : A₂ ⊕ E₆] = 3**, the Eisenstein
> prime.

**And the cut produces the rest of E₆'s structure:**

| | |
|---|---|
| the other 162 roots, sorted by their pairings (B(r,1), B(r,g_q)) with the Eisenstein plane | **six classes of 27**: (−1,0), (1,−1), (0,1) and (−1,1), (0,−1), (1,0) — the three weights of the **3** and the three of the **3̄** of the Eisenstein SU(3); the (27,3) ⊕ (27̄,3̄) of E₈ ⊃ E₆ × SU(3) |
| left multiplication by g_q (the founding ratio acting) | cycles each triple: (−1,0) → (1,−1) → (0,1) → (−1,0) — **the ℤ/3** |
| quaternion conjugation (the mirror) | swaps the two triples pairwise: **θ, the 27 ↔ 27̄ swap**, is the Eisenstein conjugation ω ↔ ω̄ — B576's *"the θ-odd plane is the imaginary axis of the object's own mirror"* made exact |

So the whole E₆ datum the programme has been using — the algebra, the 27, its ℤ/3 grading, its outer
automorphism — is **one cut of the golden lattice by the Eisenstein ratio**. E₆ is not handed over at one end;
it is what the two ends make together.

## 2. The transport it implies, and the count (part 2)

If the singularity along Q = m004 is the **golden E₈** (Γ = 2I, the object's own McKay-E₈ group) and the flat
connection is the **Eisenstein 2T inside the SU(3) that E₆ centralizes**, then E₈ ⊃ E₆ × SU(3) gives
248 = (78,1) + (1,8) + (27,3) + (27̄,3̄): **the 27 is a field on Q**, counted by h¹(Q; 3_ρ), the 27̄ by
h¹(Q; 3̄_ρ). This is the slot B1267 §1 said did not exist — B1267 considered only an E₆ singularity along Q,
and its statement is corrected at source (`frontier/B1267_transport_computed/ADDENDUM_2026-09-06_the_e8_transport.md`).

The object's SU(3) coefficient systems through its Eisenstein quotient (72 homomorphisms π₁(m004) → 2T,
48 surjective — B1263 reproduced a third time, now with 2T as unit quaternions over ℚ(ω)):

| 2T → SU(3) via | commutant in E₈ (by characters, exact) | 27s = h¹(Q;3) | 27̄s = h¹(Q;3̄) | net |
|---|---|---|---|---|
| **the 3** (irreducible, real) | **E₆ exactly** (no invariants in (1,8), (27,3), (27̄,3̄)) | **1** (B1267) | **1** | **0** |
| 2′ ⊕ ω (complex, the Eisenstein twist of the quaternionic 2) | E₆ × U(1) | h¹(2′) + h¹(ω) = **0 + 0** | h¹(2″) + h¹(ω̄) = **0 + 0** | **0** |
| 2 ⊕ 1 (quaternionic) | larger than E₆ (54 root vectors of (27,3) ⊕ (27̄,3̄) survive: the E₇ of E₈ ⊃ E₇ × SU(2)) | — | — | — |

For every one of the 48 surjections, in both Aut(2T)-classes (meridian of order 3 or 6): **h¹(m004; 2′) =
h¹(m004; 2″) = 0** with **no cusp invariants** (h⁰(∂M; 2′) = 0, so B1266's bound forces N = 0 outright), and
h¹(m004; 2) = 2 (order-6 class) or 0 (order-3 class). The non-self-dual Eisenstein systems carry nothing;
the real one carries one pair.

> **The two-face derivation yields, parameter-free, a 4d N=1 theory with gauge group exactly E₆, one adjoint
> chiral (b¹ = 1), one 27 and one 27̄, and two E₆-singlets (h¹(Q; 8|_{2T}) = h¹(ω) + h¹(ω̄) + 2h¹(3) = 2).**
> Vector-like; one generation-pair, not three. The 27 is now a field with a count, and the count is 1 = 1.

## 3. What this changes

- **L4 of the assembly is replaced.** E₆ is derived from both letters: the product's field puts the object in
  E₈ (2I = SL(2,𝔽₅) ⊂ icosians), the ratio's Eisenstein integers cut E₆ out of it. `docs/THE_ASSEMBLY_2026-09-06.md`
  §1 now carries this link; its §0 theorem 3 is scoped to the E₆-singularity transports.
- **I-6 re-read.** The row asks for *"a construction where the same 2T plays both roles"* (the π₁ quotient and
  the transverse ALE Γ). In the two-face transport the two roles are played by the **two faces**: the ALE Γ is
  the golden **2I**, the holonomy is the Eisenstein **2T**. The tension the row records dissolves; the row's
  identification as written (2T ≡ Γ) is not what the two faces do. Status left for the owner's seat.
- **I-26's price, sharpened again.** With the E₈ transport the 27 has a slot and a count: on this object, 1 = 1.
  The remaining price is unchanged in kind — net chirality needs isolated enhancement points or a non-self-dual
  unitary system with cusp invariants (B1266's bound), and the object's Eisenstein systems have none.

## Controls (MB12, both directions)

- The lattice pipeline **can fail**: the same code applied to the plane {1, i} (i of order 4, not Eisenstein)
  would give a complement of a different type; here the A₂ Gram, the 72-count, the E₆ Cartan and the index 3
  are each independent checks of one construction, and all four agree with E₆ (and with nothing else).
- The isomorphism SL(2,𝔽₅) → 2I is constructed, not assumed: well-definedness is checked on all 120 elements
  and the order-3 image satisfies its minimal polynomial exactly.
- Part 2 reproduces B1263's 72/48 in a third presentation and the h¹(2) = 2 rows show the pipeline is not
  returning zeros indiscriminately; the commutant computation distinguishes the three embeddings (E₆, E₆ × U(1),
  larger).

## Verification

`verification/e6_from_the_two_faces.py` (exact; ~5 min); run record `verification/e6_from_the_two_faces_run.txt`.
Lock: `tests/test_b1268_e6_from_the_two_faces.py` (the lattice theorem and the founding-ratio map fast; the
48-surjection table in the slow lane).

- **Feeds on:** B206 (golden → 2I → E₈), B210 (dual McKay), B256 (the trinity), B258 (the two ends), K021/B332
  (the founding identity g = −RL⁻¹), B315 (E₈ ⊃ E₆ × SU(3) scoped), B1263 (the 2T quotients), B1266 (the
  bound), B1267 (the transport; corrected), B576 (θ-odd = the mirror's imaginary axis).
- **Registers:** no status change; I-26 note corrected (the 27 has a slot in the E₈ transport); I-6 re-read.
