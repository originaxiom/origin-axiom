# B1323 — THE GENESIS UPGRADES: fork F9 prices the substrate count (ROBUST twice, and three records buy the plastic number as two buy the golden); the minimal three-record surface bundle is the Whitehead link complement, chiral by two methods, in the silver field — the A7 bit is remembered on the three-record carrier and forgotten on the two-record one, and the price of remembering it is the atom; C2 split into its theorem half and its criterion half with a census that can fail and is seen to; the two genesis axiomatisations joined by a machine-checked dictionary

**Date:** 2026-09-09 · **Seat:** cc (main) · **DESIGN sealed** `3e8282a2` before any of main's computations (`DESIGN.sha256`; the seal file unchanged) · **Status:** **PROVED** (three pre-registered computations, all PASS on their own terms; F9 ROBUST on both carriers; the mirror test PASS-A) · **Occasion:** the owner's "go" on this bench's assessment of C1–C3 and the owner's thesis *"the a·ab·ba initial principle defines chirality"*, with the instruction to read every A-axiom (P019 A0–A6/T3–T7, UNIQUENESS A1–A7, B979, B1083 — all read before the seal, §1 of the DESIGN). · **Number:** B1323; main's next free number is B1324.

## 0. What was asked, and the one-line answers

| item | question | answer |
|---|---|---|
| U1 (F9) | does A1's "not one, not three" carry weight? | **ROBUST twice.** Toral: no three-record closure has a hyperbolic carrier (χ = 0 for every T³-bundle; Gauss–Bonnet–Chern forbids it). Surface: the H₁ = ℤ³ carriers S₁,₂ and S₀,₄ give hyperbolic bundles, and **none keeps ℚ(√−3)**. |
| U1 (c′) | the owner's mirror test: does a third record make the object remember the A7 bit? | **YES, at the price of the atom.** The minimal three-record bundle, m129 (the Whitehead link complement), is chiral by two independent methods; the image of the record swap P is its mirror and no orientation-preserving isometry exists between them. Its shapes live in ℚ(i). |
| U1 (c″) | does the three-record genesis reach m202's class? | No member of the six-manifold three-line class appears (words to length 3). |
| U2 | is C2 "one criterion, one fixed point"? | Seven self-application criteria agree on φ with a unique minimiser; the eighth — the smallest Pisot number of any degree — picks the plastic number ρ = 1.3247… . C2 is split into C2a (theorem) and C2b (criterion). |
| U3 | are C1–C5 and A1–A6 one construction? | Yes, machine-checked: the Sturmian morphisms abelianise onto ⟨L, R, P⟩, the Fibonacci tick is L·P, orientation squares it to LR = A, the a·B bundle is m004, and A's eigenline cuts out the Fibonacci word. |
| U4 | hygiene | the C2 row's "there is NO F3 test" stood ten days after the lock landed (E53 #29); corrected at source. |

**The sentence the arc adds to the genesis:** *one record is nothing; two records are the golden ratio, the atom ℚ(√−3), and an object that forgets its own handedness; three records are the plastic number on the torus, where there is no geometry at all, and the Whitehead link on the surface, where the handedness is remembered and the atom is gone.*

## 1. U1 — FORK F9, THE SUBSTRATE COUNT (`verification/u1_substrate_count.py`, `.json`, `.out`; SnapPy 3.3.2 + twister, sympy, mpmath, python-flint)

**(a) One record.** GL(1,ℤ) = {±1}: no pair of primitive shears, no mixed closure, no hyperbolic element; the mapping torus is a torus or a Klein bottle. The degenerate control, recorded.

**(b) Three records, the toral carrier T³.** All words of length ≤ 4 in the six elementary transvections E_ij of SL(3,ℤ): 768 distinct products, 678 mixed (touching all three records), **162 mixed and hyperbolic**. The **minimal trace among them is 3**, attained by E₁₂·E₃₁·E₂₃ and its relabellings: characteristic polynomial **t³ − 3t² + 2t − 1**, eigenvalue moduli (0.655866, 0.655866, 2.324718), |det(B − I)| = 1 (torsion-free closure). **The real eigenvalue is ρ³ for ρ the plastic number** (x³ − x − 1; exact: the resultant of x³ − x − 1 and t − x³ is t³ − 3t² + 2t − 1; locked in the test) — the three-record analogue, letter for letter, of A = LR = (golden)²: *n records, the n-th power of the n-th minimal Pisot number.* And it has no geometry: every T³-bundle over S¹ has χ = 0 (computed from the Wang sequence for all 768; the two-record torus bundle under A returns χ = 0 through the same code path — F6's Sol), while a finite-volume hyperbolic 4-manifold has χ = 3 Vol/(4π²) > 0. **ROBUST by theorem, exhibited.**

**(c) Three records, the surface carriers.** H₁(S_{g,p}) = ℤ^{2g+p−1} = ℤ³ exactly for (g, p) ∈ {(0, 4), (1, 2), (2, 0)}; the closed genus-2 surface has no puncture (A5b) and is out of the fork's frame; the two punctured carriers were run. Control first: on S₁,₁ the word a·B returns **m004** (isometric; one cusp; shapes z² − z + 1, in ℚ(√−3); amphichiral; 8 self-isometries, 4 orientation-preserving and 4 reversing). Then:

| carrier | words tried | hyperbolic | classes | minimal class (first word) | volume | cusps | H₁ | field of the shapes | symmetry | amphichiral (two methods) | census name |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S₁,₂ | 252 (length 2–3 in a, b, c and inverses) | 36 | 2 | a·b·C (24 words) | 3.6638623767 = 4G | 2 | ℤ² | **ℚ(i)** (z² − 2z + 2, z² + 1, 2z² − 2z + 1) | order 8 | **NO / NO** | **m129 = 5²₁ = L5a1, the Whitehead link** (ooct01_00001) |
| S₁,₂ | | | | a·c·B (12 words) | 5.3334895669 | 2 | ℤ² | **ℚ(√−7)** (2z² − z + 1, z² − z + 2, 4z² − 5z + 2, 2z² − 3z + 2) | order 8 | NO / NO | s780 = 6²₃ = L6a1 |
| S₀,₄ | 80 (length 2–3 in a, b and inverses) | 28 | 2 | a·B (16 words) | 7.3277247534 = 8G | 4 | ℤ⁴ | **ℚ(i)** | **order 64** | **YES / YES** (32 + 32) | t12047 = 8⁴₂ = L8n7 (ooct02_00001) |
| S₀,₄ | | | | a·a·B (12 words) | 8.9293178231 | 4 | ℤ⁴ | cubic shapes (degree 3) | order 8 | NO / NO | o9_44206 = 10⁴₂₃ = L10n98 |

The two-loop words on S₁,₂ (a·B and its relatives) are **not hyperbolic**: SnapPy reports degenerate tetrahedra at volume 2.0299 with two cusps — the Anosov map A has one fixed point, so a second puncture cannot sit at a periodic point, the mapping class is reducible along the curve enclosing both punctures, and the bundle is m004 glued to a Seifert piece. The third record enters the geometry only through its own twist c.

**Verdict F9 = ROBUST on both carriers.** No three-record closure carries the atom: the toral world has no hyperbolic structure, and the surface world is the **silver field ℚ(i)** (m129, t12047 — the same field, and the same volume 4G, as F3's silver sibling m136) or the **chirality field ℚ(√−7)** (s780; the field B316 banked as the chirality field of the closings), never ℚ(√−3). A1's "not one, not three" now has a computed price, and the price is the atom.

**(c″)** None of the four classes is in B1321's three-line class {m202, s959, v3461, v3551, o9_40999, o9_43931}. The three-record genesis does not reach m202 at this depth; the sibling where the count of three lives is not a three-record object.

## 2. U1 (c′) — THE MIRROR TEST: the owner's thesis, computed

**The banked form first (B979, B1083, read before the seal).** The four-letter principle forces the object up to one bit, A7 = the order LR vs RL; that bit is the swap a ↔ b, the C-type bit of the founding torsor, and it is exactly where φ rather than −1/φ enters. LR and RL are conjugate by the record swap P, so every class invariant is blind to the bit; P reverses the fibre's orientation, so the two choices are the two mirror images of one object, and m004 is isometric to its mirror. **The a·ab·ba principle defines the chirality bit; the two-record object forgets it. That is the amphichirality wall in the genesis's own words.**

**What the third record does.** The DESIGN pre-registered two transforms of a twist word and, in its wording, conflated them; the computation separated them, and the separation is the finding:

- the **pure letter swap** (a ↔ b, c fixed) is induced by the *rotation* of the torus (a ↦ b, b ↦ a⁻¹), an orientation-preserving map — it returns **the same oriented manifold** (m129 → m129: 8 isometries, all orientation-preserving);
- the **reflection word** (each twist x ↦ h(x)⁻¹ under the reflection h exchanging a and b) is the surface-level image of the **record swap P** — it returns **the mirror image** (m129 → mirror: 8 isometries, all orientation-reversing, none preserving).

On the control S₁,₁ both transforms return m004 with 4 + 4 signs, because m004 is amphichiral and cannot tell them apart. On S₁,₂ the minimal bundle **m129 is chiral by two independent methods** — its 8 self-isometries are all orientation-preserving (symmetry group order 8, `is_amphicheiral` False), and every isometry to its orientation-reversed copy reverses orientation — so the image of P is a *different oriented manifold*. **PASS-A: on the three-record carrier the A7 bit is a class invariant.** The same holds for s780 and o9_44206; the S₀,₄ minimal bundle t12047 (symmetry order 64) is amphichiral and forgets the bit, so the statement is carrier-specific and the minimal one remembers.

**What this says about the thesis, exactly.** The owner is right about the origin: the bit is defined by the principle, at A7. The record is right about the two-record object: it does not carry the bit as a class invariant. The new statement is the fork: **a third record makes the object remember its handedness, and the object that remembers is not ours — its field is ℚ(i), its volume is the silver volume 4G, its faces are the silver faces (B749 F3: "the silver world is real and is not ours").** So at the genesis, as on the closed closings (B1294: "the 2 or the c-breaking, not both"), one may have the atom or the remembered bit, not both — at least among the carriers with H₁ = ℤ³ and words to length 3. The identification "mirror image = the record swap" is now exhibited on a manifold that can tell (the map is shown and shown to act, THE IDENTIFICATION RULE), which the amphichiral m004 could never do.

## 3. U2 — THE CRITERION CENSUS and the split of C2 (`verification/u2_criterion_census.py`, `.json`, `.out`)

C2 is two links wearing one label. **C2a [THEOREM — self-similarity]:** a Sturmian word fixed by a substitution has a quadratic slope (B749 F7a; Lagrange). **C2b [CRITERION — minimality]:** among the self-similar slopes, minimality selects φ. The census asked whether the natural formalisations of "the parameter minimally describes itself" agree, and whether any natural minimality criterion disagrees.

| K | criterion | computed | minimiser |
|---|---|---|---|
| K1 | Hurwitz — the least Lagrange value | L(α) exact from the period for all purely periodic α of period ≤ 2, quotients ≤ 5 | **√5 at [1; 1, 1, …] alone**; second value 2√2 at [2; 2, …] (Markov) |
| K2 | the least constant partial quotient | [1; 1, 1, …] | φ |
| K3 | the first hyperbolic trace in SL(2,ℤ) | trace 3; reduced indefinite forms of discriminant 5: {(−1,1,1), (1,1,−1)}, one cycle, **h⁺(5) = 1** | the one class [[2,1],[1,1]], eigenvalue φ² |
| K4 | torsion-free first mixed closure (A5) | |det(LᵃRᵇ − I)| = ab on the 12 × 12 grid | (1, 1) alone |
| K5 | the Markov tree's root | 21 triples to 10⁴; the fundamental triple (1,1,1), Fricke triple (3,3,3) with 27 = 27 | trace 3 |
| K6 | the smallest real quadratic discriminant | squarefree d < 60 | 5 = ℚ(√5) = ℚ(φ) |
| K7 | the smallest quadratic Pisot number | x² − ax − b, |a|, |b| ≤ 6 | x² − x − 1, **φ** |
| K8 | **the smallest Pisot number of any degree** (counter-criterion) | degree ≤ 4, coefficients ≤ 3 | **x³ − x − 1, ρ = 1.324717957… (the plastic number; Siegel 1944), below φ** |
| K9 | minimal description length of the word (counter-criterion) | recorded, not computed | a periodic word; excluded only by C3 (F2) |

**PASS as pre-registered.** "One criterion, one fixed point" is true of the seven self-application formalisations (K1–K7 are one fact seen seven ways — Hurwitz, Markov, the class number of 5, the torsion-free closure, the Markov root) and false of the eighth: *minimal algebraic growth* is a different criterion, and it selects the plastic number — which U1(b) then found as the three-record closure's own dilatation. The counter-criterion was not idle: it named the number the next fork produced. C2b's price is F3's silver world; C2a carries no price.

## 4. U3 — THE DICTIONARY LEMMA (`verification/u3_dictionary.py`, `.json`, `.out`; registry row T-GENESIS-DICTIONARY)

| step | statement | check |
|---|---|---|
| (i) C1 ↔ A2 + A4 | the Sturmian monoid St = ⟨E, G, G̃⟩ abelianises onto exactly the non-negative GL(2,ℤ) matrices = ⟨L, R, P⟩ | 3 280 morphisms to length 7 → 87 matrices, every one in GL(2,ℤ), non-negative, and a product of the two shears and the swap (Euclidean peeling); conversely **all 462** non-negative GL(2,ℤ) matrices with entries ≤ 13 are realised by an explicit morphism (L ↦ G, R ↦ EGE, P ↦ E); M(E) = P, M(G) = M(G̃) = L |
| (ii) A7 inside the tick | the Fibonacci morphism a ↦ ab, b ↦ a has matrix [[1,1],[1,0]] = **L·P** (det −1: A2 without A3); orientation (C5 ≡ A3) forces the square: **(LP)² = LR = A**, **(PL)² = RL**; PLP = R; LR and RL conjugate by P; the Möbius fixed-point polynomials z² − z − 1 (LR) and z² + z − 1 (RL) | all identities exact; B979's based invariant and B1083's double tick recovered in one line: **A7 is the placement of the swap inside the single tick** |
| (iii) C4 ↔ A1 | H₁(S₁,₁) = ℤ² and the a·B bundle is m004 | isometric to m004, one cusp, volume 2.0298832128 |
| (iv) A ⇒ the word | the cutting sequence of the expanding eigenline of A (eigenvector (φ, 1), slope 1/φ = [0; 1, 1, 1, …]) | equals the Fibonacci word for 600 letters, **letter for letter in the naming a = vertical crossing** — the swapped naming does not match, which is A7 read from the eigenline |

**PASS.** The two genesis stories are one construction in two presentations; the one non-trivial identification is C4 ↔ A1 (the carrier's homology is the substrate), and the statement "agreement between two axiomatizations, never two independent derivations" (B1243) is now a lemma with a lock rather than a caution.

## 5. U4 — hygiene, and what the arc does not claim

- **E53 instance #29:** THEOREM_LEDGER's C2 row said "There is NO F3 test … a citation to a test that does not exist" (2026-08-09, re-stamped CURRENT 2026-08-19) while `tests/test_b1003_f2_f8_locks.py` (2026-08-30) has asserted all seven fork verdicts including F3's. Corrected by a dated addendum on the row; the doc-currency stamp had certified staleness.
- **Not claimed:** that the genesis is unconditional (UNIQUENESS §6 stands verbatim: A1–A7 are not derived from anything weaker; the Kolmogorov Selector cell remains MISSING); that F9's ROBUST extends beyond words of length 3 on the two punctured carriers (a longer enumeration or a proof is the next step if anyone wants the general statement); that m129's chirality is new (it is classical; what is new here is its role as the image of the record swap on the three-record carrier); that the plastic number's appearance in U1(b) and U2(K8) is more than the identity it is (the minimal-trace closure's dilatation is ρ³; Siegel's theorem makes ρ the smallest Pisot number; the coincidence is that "n records" and "smallest Pisot of degree n" are the same enumeration at n = 2 and n = 3 — a hint, registered, not a law).
- **Scope of the mirror statement:** carrier-specific (S₁,₂ remembers, S₀,₄'s minimal bundle forgets) and depth-bounded; the statement "the atom or the remembered bit, not both" is a computed fork over the enumerated set, not a theorem about all carriers.

## 6. What changes on the surfaces

THEOREM_LEDGER Part I: the C2 row's addendum (the stale lock sentence, the C2a/C2b split, the census) and the C4 row's addendum (the dictionary, F9's price); THEOREM_REGISTRY: T-GENESIS-DICTIONARY; ERROR_LEDGER: E53 #29; B749's FINDINGS: the F9 addendum (verdict ROBUST, by pointer — B749's RESULTS.json is left at its seven forks, as its lock requires); HINT_LEDGER: four hints; FRESH_EYES: Q15 (is there a carrier that keeps the atom and remembers the bit?); MAIN_GOAL JOIN 1: the genesis-level fork under the chirality head; the alias table (B1323 taken, next B1324); CHANGELOG, PROGRESS_LOG, CAMPAIGN_STATUS. Lock: `tests/test_b1323_the_genesis_upgrades.py` (seal, the three JSON verdicts, the exact plastic-number identity, live re-runs of U2/U3 under OA_SLOW). No seat item, no harvest row, pins unchanged.
