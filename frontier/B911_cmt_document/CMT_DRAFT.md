# B911 — THE COMPACT MEASUREMENT THEOREM (CMT) — DRAFT: the compact pencil's three walls carry so(8) ⊕ u(1)², nest branch-by-branch inside the noncompact D₅ walls, generate the classical D-chain flag by pure measurement combinatorics, and are Killing-orthogonal to the SMT block

B911 computation seat, 2026-08-05. **DRAFT for S1 banking review** (register item L4) — the compact
campaign's cornerstone document, companion to the banked FIRST MEASUREMENT THEOREM (B877) and the
verified SECOND MEASUREMENT THEOREM (B892). Source: the solo seat's structure ledger §§LV–LVIII
(compact campaign proper), §§LI–LIII (the frame), §XVIII (the noncompact pencil); §LIV is RETRACTED
and enters only through its correction. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.

**Tier discipline of this draft**: every claim carries its verification status. This seat
independently recomputed a large part of the suite on the banked B854 build
(`cmt_recompute.py`, `cmt_recompute2.py`, `cmt_frame_check.py`, results JSONs in this arc);
claims this seat could **not** reach are marked **[SOLO-TIER, VERIFICATION PENDING]** and await
the banking seat's rerun. Nothing here is banked until S1 passes.

---

## 0. Setting

Exact 𝔢₆ over ℚ (Chevalley basis, B854's cocycle — the build whose Jacobi/exponents/invariant
gates are banked in B854). The four superselection charges g₈, g₁₄, g₁₆, g₂₂ = the 2T-invariants,
one per block (B854; z(2T) = u(1)⁴, toral, banked). The frame facts this document stands on:

- **The orthogonal frame** (ledger LI): the Killing Gram of the four charges is **diagonal**,
  signature **(2,2)**: {g₈, g₁₆} noncompact (+), {g₁₄, g₂₂} compact (−). The compact/noncompact
  split of the frame IS the organizing split of the charge story.
  *Tier: solo exact; this arc: recomputed exactly (`cmt_frame_check.py`) — diagonal, signs
  (+,−,+,−), and the norms come out IDENTICAL to the ledger's KF1 values:
  +241532928, −317708697600, +988843239014400/13, −889958915112960000/19
  (the two builds share normalization on the nose); Gram determinant a rational square
  (KF3's all-even-exponent claim); the norm squarefree kernels carry 13 on g₈ and 19 on g₁₄,
  confirming CL2's prime addresses.*
- **The two-level lattice** (ledger LII CL1): z(any nonempty subset of {g₈,g₁₆}) = the **30-dim
  CORE**; z(any subset meeting {g₁₄,g₂₂}) = the **12-dim FLOOR** = z(torus). One compact
  measurement resolves the full superselection algebra to the floor.
  *Tier: solo exact; this arc: recomputed exactly — dim z(g₈) = dim z(g₁₆) = 30 with
  ad(g₁₆)·z(g₈) = 0 (so z(g₈) = z(g₁₆) = z(g₈,g₁₆) = core), dim z(g₁₄) = dim z(g₂₂) = 12 =
  dim ker(ad g₁₄|core) = floor, ad(g₂₂)·floor = 0. The remaining subsets follow by lattice
  monotonicity from these values — CL1 is fully discharged exactly.*
- **The noncompact pencil** (ledger XVIII L4–L6, banked lineage; FMT = B877): walls of
  x(ρ) = g₈ + ρ·g₁₆ at the roots of the irreducible cubic
  **μ = 500716339200ρ³ − 2075673600ρ² − 4769856ρ + 2197** (constant 13³), Galois S₃,
  z(x_i) = **so(10) ⊕ u(1)** (dim 46, derived 45, center 1). Banked, two-seat.
- **The core's type** (ledger XVIII L1; R1 two-prime): core = **so(8) ⊕ u(1)²** (dim 30,
  derived 28, center 2) — the D₄ Levi. Banked lineage; not re-typed in this arc.
- **The floor's type** (ledger XXVII X1; cc R3): complexified floor = **A₂ ⊕ u(1)⁴**
  (dim 12, derived 8; the u(1)⁴ = the torus itself). Banked lineage; not re-typed in this arc.

Normalization note (load-bearing, see §6): the raw B854 charges reproduce the **solo**
normalization exactly — this arc's compact cubic came out coefficient-identical to the solo
ledger's κ (rescale λ = 1). The banked B880-lane cubic `[500716339200, −159667200, −28224, 1]`
lives in a **different** (g₁₆-integralized) convention: μ_solo(ρ) = 13³ · CUBIC_banked(ρ/13),
verified exactly here. Walls computed on the raw build sit at μ_solo's roots, **not** at the
banked CUBIC's roots (this arc measured dim z = 30, i.e. no wall, at the banked roots — the
sharpest possible demonstration that the two conventions must never be mixed).

---

## 1. The theorem

**THE COMPACT MEASUREMENT THEOREM (CMT).** With the setting above:

**(i) The compact walls.** The compact pencil h(s) = g₁₄ + s·g₂₂ acts on core/floor (18-dim
quotient; the floor is pencil-invariant — in fact pencil-killed). Its degeneration polynomial is

> **ν(s) = c · κ(s)⁶**,  κ = **2771822592000·s³ + 3033676800·s² − 56402640·s − 6859**

with κ **irreducible**, constant term **−19³** (the compact prime cubed — the exact twin of μ's
13³), discriminant squarefree kernel **{7, 11}** ⟹ quadratic resolvent **ℚ(√77)**, discriminant
a non-square ⟹ **Galois group S₃**. Three compact walls, one irreducible Galois orbit —
mirroring the three noncompact walls exactly.
In this build, c = 2893269103566796895998909373006925818660773316877415443033898352640
00000000000000000 / 19¹⁸ — and κ(0)⁶ = (−19³)⁶ = 19¹⁸ cancels the denominator: ν(0) ∈ ℤ.

**(ii) One field.** κ factors with degrees **[1, 2]** over K = ℚ[ρ]/μ ⟹
**ℚ[s]/κ ≅ ℚ[ρ]/μ = K**: the compact and noncompact wall-triples live in ONE cubic field,
in canonical S₃-equivariant bijection. The bijection is **explicit**:

> **s\*(ρ) = −4997/1257360 − (198911/68107)·ρ + (560387520/885391)·ρ²**

satisfies κ(s\*(ρ)) ≡ 0 (mod μ) **exactly** (ledger LVII SST). Note the proof economy: SST +
irreducibility of κ over ℚ *proves* (ii) — s\* ∈ K is a root, so ℚ(s\*) ⊆ K is a degree-3
subfield, hence equal to K.

**(iii) The typing.** At each of the three compact walls s\*_j,

> **z(g₁₄ + s\*_j·g₂₂) = so(8) ⊕ u(1)²**  (dim 30, derived 28, center 2)

— **core-shaped, core-distinct**: z(h\*_j) ∩ core = **18 = floor + 6** at every wall
(3 walls × corank 6 = 18 closes the quotient bookkeeping). Typing route: h\* is semisimple
(element of the banked toral z(2T)) ⟹ z is reductive of full rank 6 [import I-1/I-2] ⟹
semisimple part has rank exactly 6 − 2 = 4; the exhaustive enumeration of semisimple algebras
of dim 28, rank 4 gives **{D₄, G₂⊕G₂}** (this arc — the ledger's "so(8) unique" import is
incomplete as recorded, see §5); G₂⊕G₂ does not embed in 𝔢₆ [import I-4] ⟹ **D₄ ⊕ u(1)²**.

**(iv) The pairing law and the core-shadow identity.** Across the two pencils' walls, all nine
combinations (matched via s\* = s\*(ρ)):

> dim z(x_i, h\*_j) = **30 if matched (i ↔ j), 18 if mismatched**;
> matched: z(h\*_i) ⊂ z(x_i) — **the NESTING**: the compact-wall so(8)⊕u(1)² is a subalgebra
> of the matched noncompact-wall so(10)⊕u(1); the mixed measurement adds nothing at matched
> branches;
> mismatched: z(x_i) ∩ z(h\*_j) = z(h\*_j) ∩ core — **the CORE-SHADOW**: nothing of a compact
> wall outside the core survives a mismatched noncompact measurement.

**(v) The D-chain flag.** The cross-shadow 18 is typed: derived 15, center 3, and the 15-dim
rank-3 semisimple enumeration is a singleton ⟹ **so(6) ⊕ u(1)³**. Hence the measurement
combinatorics of the two pencils produces, per Galois branch, the classical chain

> **A₂ ⊕ u(1)⁴ (floor, 12) ⊂ so(6) ⊕ u(1)³ (18) ⊂ so(8) ⊕ u(1)² (30) ⊂ so(10) ⊕ u(1) (46) ⊂ 𝔢₆ (78)**

— the D-series ladder E₆ ⊃ D₅ ⊃ D₄ ⊃ D₃ with abelian ranks descending 4, 3, 2, 1, 0 and
semisimple ranks ascending 2, 3, 4, 5, 6 (every member a full-rank-6 reductive centralizer —
the consistency the reductivity import demands). Matched vs mismatched wall choices select the
rung. The inclusions floor ⊂ 18 ⊂ 30 are definitional (centralizers of larger commuting sets);
the rung 30 ⊂ 46 is the nesting (iv).

**(vi) The invisible 12 = the SMT block.** The three compact-wall centralizers satisfy

> pairwise AND triple intersections = **the floor exactly**; span = **66**
> (inclusion–exclusion 3·30 − 3·12 + 12 = 66 closes);

their Killing-perp **M₁₂** (dim 12 = 78 − 66, canonical) is **torus-invariant**, meets the core
in **0**, carries **full-rank (12) action of all four charges**, and satisfies

> **dim ker((ad g₈ + ρ_i·ad g₁₆)|M₁₂) = 4 at each noncompact wall ρ_i** — the μ⁴ block of
> L4's det₁₂ = c·μ⁴, i.e. exactly the chamber where the SMT's second (SM-making) charge lives.
> (The ledger records this at "a μ-root"; this arc verified it at all three μ-roots.)

The three compact walls span everything **except** the SMT chamber and are Killing-orthogonal
to it. (Program-internal reading, fenced: "the compact hemisphere is structurally blind to the
SM chamber" — a statement about kernels and Killing complements, nothing more.)

**THE MIRROR** (the campaign's summary row): noncompact — 3 walls, S₃, 13³, so(10)⊕u(1);
compact — 3 walls, S₃, 19³, so(8)⊕u(1)²; ONE resolvent √77 over all. With κ, the √77 law now
counts **six** cubics (μ, the four 27-charge cubics of B888-lineage/Q77, and κ): the 7·11
sign-field is frame-wide, compact and noncompact alike.

---

## 2. The exact ingredient list

| # | ingredient | exact content |
|---|---|---|
| 1 | the charges | g₈, g₁₄, g₁₆, g₂₂ = B854's 2T-invariants (exact, banked build) |
| 2 | the frame | Killing Gram diagonal, signature (2,2); compact pair = {g₁₄, g₂₂} |
| 3 | core / floor | 30 / 12; core = z(g₈) = z(g₁₆); floor = z(torus) = z(g₁₄) = z(g₂₂) |
| 4 | μ (noncompact cubic) | 500716339200ρ³ − 2075673600ρ² − 4769856ρ + 2197; const 13³; disc kernel {7,11}; S₃ |
| 5 | κ (compact cubic) | 2771822592000s³ + 3033676800s² − 56402640s − 6859; const −19³; disc kernel {7,11}; S₃ |
| 6 | ν (compact degeneration) | ν(s) = c·κ(s)⁶ on core/floor, deg 18 exactly; c·19¹⁸ ∈ ℤ |
| 7 | one field + bijection | ℚ[s]/κ ≅ ℚ[ρ]/μ = K; s\*(ρ) as in §1(ii), exact root |
| 8 | wall typing | dim 30 / derived 28 / center 2 ⟹ so(8)⊕u(1)², all three walls |
| 9 | core-shadow / pairing | 3×3 table: diag 30 (nesting), off-diag 18 = z(h\*)∩core = floor+6 |
| 10 | the 18 typed | derived 15 / center 3 ⟹ so(6)⊕u(1)³ (D₃) |
| 11 | the D-chain | 12 ⊂ 18 ⊂ 30 ⊂ 46 ⊂ 78; abelian ranks 4,3,2,1,0 |
| 12 | the invisible 12 | M₁₂ = K-perp of the 66-span; ∩core = 0; torus-invariant; charge-rank 12; ker 4 at μ-walls |

---

## 3. Verification status per claim (the honest tier table)

Bound directions, stated once and used throughout: for an integral model at a good prime,
mod-p nullity ≥ char-0 nullity and mod-p rank ≤ char-0 rank. So a mod-p kernel of dim d
certifies **char-0 dim ≤ d**; a mod-p derived rank r certifies **char-0 derived ≥ r**;
multi-prime agreement is evidence, not a char-0 certificate. The FMT (B877) closed this gap
for the noncompact walls with exact restriction-of-scalars nullities; **the CMT has not yet
had that pass** — it is the top open belt (§7.1).

| claim | ledger tier (solo, §§LV–LVIII) | this arc's recomputation | remaining gap |
|---|---|---|---|
| ν = c·κ⁶ (deg 18, exact) | exact (19-pt interpolation of exact dets, post-LIV-retraction) | **exact, independent**: 19 nodes + 6 check nodes, degree bound proven structurally; identical κ, λ = 1 | none (two independent exact runs) |
| κ irreducible; const −19³; disc kernel {7,11}; S₃ | exact | **exact, independent** | none |
| μ facts (const 13³, kernel {7,11}, S₃); μ_solo = 13³·CUBIC(ρ/13) | exact / banked | **exact, independent** | none |
| one-field ℚ[s]/κ ≅ K | exact | **exact, two routes** (extension factoring [1,2]; SST+irreducibility argument) | none |
| SST s\*(ρ) exact root | exact (PSLQ-found, verified) | **exact, independent** (κ(s\*(ρ)) ≡ 0 mod μ) | none |
| wall dims 30/28/2, all 3 walls | mod-p, five (root,prime) pairs: two single-root primes (40013 the first; the second unnamed in the ledger) + the split prime 40039 | **mod-p, fresh split prime 40829**, all 3 walls: 30/28/2 replicated | char-0 exactification (FMT recipe) — dims currently ≤/≥ bounds + 8-pair agreement |
| z(h\*) ∩ core = 18 = floor + 6, per wall | mod-p | **mod-p 40829**, all 3 walls (incl. ∩floor = 12) | exactification |
| typing ⟹ so(8)⊕u(1)² | import "28-dim rank ≤ 4 unique" | **enumeration recomputed — import INCOMPLETE: {D₄, G₂⊕G₂}** (§5) | the G₂⊕G₂ exclusion import (I-4) must be pinned or computed |
| pairing law 3×3 (diag 30 / off 18) | two-prime (40123, 40639) | **third prime 40829**; matching discovered from the table itself is a perfect bijection | exactification |
| matching = SST bijection | matched-branch by construction | **verified directly at 40829**: s\*(ρ_i) mod p equals the table-matched κ-root, all three branches | none at mod-p tier |
| nesting z(h\*_i) ⊂ z(x_i) | two-prime (via BLT) | **third prime 40829** (rank([Z_i|W_j]) = 46 on matched pairs) | exactification |
| the 18 typed: derived 15 / center 3 ⟹ so(6)⊕u(1)³ | mod-p, prime coverage not stated in ledger — **flag** | **mod-p 40829**: 15/3 replicated; A₃ uniqueness enumeration exact | banking seat: confirm the solo primes; exactification |
| noncompact wall dims 46/45/1 (context, FMT) | banked two-seat (B877) | **mod-p 40829**: 46/45/1 replicated at all 3 walls (bonus FMT belt) | — (already banked exact) |
| GEO: pairwise ∩ = triple ∩ = floor; span 66 | one split prime (40039) | **second split prime 40829**, incl. "= floor" as subspace identity | exactification |
| M₁₂: dim 12, ∩core 0, torus-invariant, charge-ranks 12 | one prime (40039) | **second prime 40829** | exactification; module-level SMT-block pin |
| ker((ad g₈+ρ ad g₁₆)|M₁₂) = 4 at μ-walls | one prime | **second prime 40829**, all three μ-walls | exactification |
| frame: Gram diagonal, (2,2), compact split; KF1 norms | exact (LI) | **exact, independent**; norms IDENTICAL to KF1's values; det a rational square; CL2's 13/19 addresses confirmed in the norm kernels | none |
| two-level lattice CL1 (all 15 subsets) | exact Q-ranks | **exact, independent** (key values + lattice monotonicity) | none |
| core = so(8)⊕u(1)² (L1) | solo exact + cc two-prime (R1) | not re-typed here (dim 30 recomputed exactly) | — (banked lineage) |
| floor = A₂⊕u(1)⁴ (complexified) | banked lineage (R3, X1) | not re-typed here (dim 12 recomputed exactly) | — |
| W_frame = ℤ₂×ℤ₂ (FS4); J1a involution-genericity | solo | **not recomputed** | **[SOLO-TIER, VERIFICATION PENDING]** — context items, not load-bearing for §1 |
| six-cubic √77 law (the five prior cubics) | exact (Q77) + banked B888 lineage | κ's membership recomputed exactly; the other five not re-run here | banking seat: five-cubic disc kernels on rerun **[SOLO-TIER, VERIFICATION PENDING]** for the 27-cubics |

Fresh-prime detail (this arc): p = **40829**, split for both cubics, distinct from every prime
used in the ledger (40009, 40013, 40037, 40039, 40123, 40639); κ-roots mod p {9526, 26243,
36178}; μ-roots {11109, 20677, 37152} = the roots of N(t), the build's own quotient
determinant on 𝔢₆/core (deg-48 interpolation, 49 + 6 nodes; N = c·(cubic)¹⁶ verified at 8
random points) — derived from the build, not assumed. Pairing matching found by the table:
{x₁ ↔ h\*₃, x₂ ↔ h\*₂, x₃ ↔ h\*₁} in root-sorted order, and s\*(ρ_i) mod p reproduces exactly
this matching (SST). Scripts and JSONs in this arc.

---

## 4. What this arc independently recomputed (manifest)

- `cmt_recompute.py` / `cmt_recompute.log` / `cmt_recompute_results.json` — stages 0–5:
  build reproduction (b854 rerun results == banked results.json, byte-content equality),
  exact lattice dims, exact ν = c·κ⁶, ledger-polynomial exact checks, fresh-prime compact
  suite, enumerations. Also documents the normalization hazard: at the **banked** CUBIC's
  roots the raw build shows **no wall** (dim 30) — see §6.
- `cmt_recompute2.py` / `cmt_recompute2.log` / `cmt_recompute2_results.json` — the noncompact
  walls **derived from the build** (no normalization hypothesis): N(t) on 𝔢₆/core, deg-48
  interpolation, roots = μ_solo's roots = 13× banked roots; wall suite 46/45/1; the 3×3
  pairing table with discovered matching; SST-bijection check; nesting; M₁₂ kernel-4.
- `cmt_frame_check.py` / `cmt_frame.log` / `cmt_frame_results.json` — the exact Killing Gram
  of the frame: diagonality, signature, determinant-square, per-charge norm kernels.
- `b854_rerun_results.json` — the exec'd build's regenerated results (equal to banked).

All exact steps are Fraction/sympy-Rational; all mod-p steps are exact F_p arithmetic;
no floats anywhere in this arc.

---

## 5. Finding while drafting: the D₄-uniqueness import is incomplete as recorded

The ledger's typing step reads *"so(8) the unique 28-dim semisimple of rank ≤ 4 [import]"*.
The exhaustive enumeration (recomputed here, `stage5`) gives **two** entries:

> dim 28, rank ≤ 4: **D₄** and **G₂ ⊕ G₂**.

The conclusion so(8)⊕u(1)² survives, but the import must be repaired to: *"D₄ or G₂⊕G₂, and
G₂⊕G₂ does not embed in 𝔢₆"*. The exclusion is standard (the centralizer of a G₂ subalgebra
of 𝔢₆ is A₂, dim 8 < 14 — Dynkin's subalgebra tables), but it is an **import needing a
citation pin** (I-4), or a computation: exhibit the root system of the 28-dim derived algebra
directly (24 roots, simply-laced, D₄ diagram) mod p — recommended as part of the
exactification pass. The parallel enumerations are singletons and need no repair:
dim 15 rank ≤ 3 = {A₃} (the 18-typing), dim 45 rank ≤ 5 = {D₅} (the FMT typing),
dim 11 = {A₁⊕A₂} (the SMT typing).

Imports ledger for this document:
- **I-1** centralizer of a semisimple element is reductive of full rank [textbook].
- **I-2** z(2T) is toral, so its elements (over any extension) are semisimple [banked: B854
  exact abelian + nondegenerate restricted Killing + fixed-point reductivity, G1 lineage].
- **I-3** the simple-algebra dim/rank table [textbook; the enumeration over it is exhaustive
  and recomputed here].
- **I-4** G₂⊕G₂ ⊄ 𝔢₆ [Dynkin; **NEEDS-CITATION-CHECK** — flagged, see above].

---

## 6. The normalization law of the two builds (load-bearing bookkeeping)

Verified exactly in this arc:

- The raw B854 charges reproduce the **solo** ledger's polynomials on the nose: κ identical
  (λ = 1), and the noncompact walls at μ_solo's roots.
- The banked B880-lane cubic is the same field in the g₁₆-integralized convention:
  **μ_solo(ρ) = 13³ · CUBIC_banked(ρ/13)** (exact identity; CL2's "g₁₆ carries exactly 13"
  is the mechanism). Wall values transform ρ = 13t.
- Hazard, demonstrated: running the pairing suite with the banked roots on the raw build
  yields a degenerate all-18 table with **no** matching (cell 1) — structurally wrong, not
  noisily wrong. Any rerun mixing artifacts from the two lanes must transform wall values
  first. Recommended: a NORMALIZATION registry row in the banking PR (which convention each
  banked artifact uses).

---

## 7. Open belts (the queue this draft hands the banking seat)

1. **Char-0 exactification of the compact walls** on the FMT recipe: restriction of scalars
   over K for exact ℚ-nullities (dims 30), derived/center squeeze (28/2), per root. This is
   the single tier-upgrade separating the CMT from FMT grade.
2. **The I-4 import**: pin the G₂⊕G₂ ⊄ 𝔢₆ citation, or compute the D₄ root system of the
   wall's derived algebra directly.
3. **D₃-typing prime coverage**: the ledger does not state the primes behind derived 15 /
   center 3; this arc adds 40829; the banking rerun should state its coverage explicitly.
4. **M₁₂ exactification + module pin**: beyond the kernel-4 signature, pin M₁₂ as the SMT
   block at module level (its bracket with the wall charge y\*, its position in the SMT
   tower); exact pass queued.
5. **The full-78 compact degeneration beyond the core** (ledger NU3 part B) — never computed.
6. **The D₄-pair geometry** inside each D₅ (core's D₄ vs the compact wall's D₄, meeting in
   18): typing of the overlap, triality shadows — fenced and queued (D4P).
7. **Triality echo for the compact triple**: does the compact wall-triple induce a
   V-sector-style tiling (the L8 analogue)? In particular, do the three wall-shadows'
   extra-6's tile core/floor (span of the three z(h\*_j) ∩ core = the full core)? The
   "3 × corank 6 = 18" line in §1(iii) is arithmetic bookkeeping; the tiling itself is
   not yet computed. Open.
8. **Compact-side exact charge invariants** (the e₁,e₂ analogue of L11): queued for the
   exact pass.
9. **The √77 law's scope**: with six cubics on one resolvent, a completeness question (is
   there a seventh pencil cubic in the frame, and must it share the resolvent?) — register,
   do not chase.
10. **W_frame / J1a re-verification** (the two context rows marked [SOLO-TIER, VERIFICATION
    PENDING] in §3).

---

## 8. What this document does NOT say

- **No physics.** "Measurement", "charge", "wall", "invisible", "blind", "SM chamber" are the
  program's internal names with computed referents (kernels, centralizers, Killing
  complements, determinant loci). so(10)⊕u(1), so(8)⊕u(1)², su(3)⊕su(2)⊕u(1)³ are Lie-algebra
  isomorphism types. No physical identification is claimed; no value enters; Gate 5 untouched.
- **The mod-p tier is evidence, not certificate** (§3's bound directions). The FMT-grade
  exact pass is open belt #1 — until it lands, the wall dims are "≤ 30 exact + eight
  (root,prime) agreements", not "= 30 exact".
- **The three walls are one S₃ orbit** (disc non-square): no canonical labeling of the
  individual walls exists; per-wall statements are orbit statements.
- **§LIV is retracted** (the septic and its S₇ census were an interpolation-aliasing
  artifact). Nothing here depends on it; its lesson (proven degree bounds, surplus check
  nodes) is applied in every interpolation of this arc.
- **Fenced readings stay fenced**: "the two hemispheres' complementarity", "triality echo",
  and every physics-flavored gloss in the ledger are registered unweighted; none is part of
  the theorem.
- **Nothing to `CLAIMS.md`.**

## Provenance

The compact campaign (§§LV–LVIII: κ, ν = c·κ⁶, one-field, SST, the walls, the nesting and
pairing laws, the D-chain, the invisible 12) is the **solo seat's** work. The exact 𝔢₆ build
and the four charges are the **cc banking seat's** B854; the FMT recipe and its banking are
B875–B877; the SMT is the solo seat's theorem verified by the banking seat in B892. This
arc (B911 computation seat) contributed the independent recomputation manifest of §4, the
import repair of §5, and the normalization law of §6. Verification is internal to the
program's seats throughout (PROVENANCE.md discipline); the imports I-1–I-4 are the only
external mathematics relied on, and I-4 is the only one not yet pinned.

*Draft complete; awaiting the banking seat's suite rerun and S1 review.*
