# R56 — THE ENDPOINT THEOREM: the record's seven chirality walls are one Euler characteristic, and the object has none because it is a knot

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Against main @ 0ecd9557** · **Status:** seat report, not banked; every arithmetic statement is in `computations/r56_endpoint_theorem.py`; every literature statement is quoted from the source text extracted on this bench.

## 0. The verdict, first

**Not achieved: a fully derived Standard Model.** The record's sealed negatives (B915: 16σ; V-3: no object period is an SM ratio) stand and I did not try to argue around them.

**Achieved: the failure is now one theorem, with a formula, and the formula evaluates to zero on the object for a reason that can be stated in one sentence.** In the frame the record has been implicitly using since B632 — 7d E₆ super-Yang–Mills on a 3-manifold Q, which is M-theory on ℂ²/2T × Q, i.e. exactly the *"same 2T in both roles"* that I-6 asks for — the net number of chiral multiplets in any representation is a **relative Euler characteristic** (Pantev–Wijnholt 2009, eq. 3.40; Braun–Cizel–Hübner–Schäfer-Nameki 2018, eqs. 2.50 and 4.17). On a closed 3-manifold it is identically zero because the dimension is odd. On the cusped object it is the Euler characteristic of the *charge locus* of the Higgs field, and **a knot has Euler characteristic zero**: one component, one loop. Three generations require a charge locus with Euler characteristic three — three **endpoints**. The object is a loop; it has no endpoints. That is the H5 pattern ("every space, never a point") as a theorem: *a point is an endpoint, and a knot has none.*

Two further results fall out: (i) the record's I-25 candidate set is 2, not 4 — B1112's own projectivity criterion kills the three labellings with even-dimensional summands — and the two survivors are the principal (Dynkin index 156) and the subregular (84); the record has **banked the principal as EARNED** (I-19, B1242: E₆ CS contains 3d gravity at index 156) and **proposed the subregular** (B1257) in the same week; they are different subalgebras. (ii) The value problem (JOIN 2) changes shape in this frame: couplings are volumes and Yukawas are exponentials of *areas of gradient-flow disks* in T\*Q, not periods of the object — so V-3's negative is what the frame predicts, and it says where the numbers live instead.

---

## 1. The frame, and why it is the record's frame

The record's chain builds E₆ from 2T by McKay (I-1, EARNED) and then counts h¹(Q; 27_ρ) for flat connections ρ on Q = m004 (B632, B1036, B1086, B1253–B1267). The physics that licenses "h¹ = massless multiplets" on a 3-manifold — the thing I-26 says was never exhibited — is the following, and it is standard:

- M-theory on a G₂ 7-manifold X with an ADE singularity of type Γ ⊂ SU(2) along an associative 3-cycle Q ⊂ X is, at low energy, **7d super-Yang–Mills with gauge group of the ADE type of Γ on Q × ℝ^{3,1}** (Acharya–Witten, hep-th/0109152). For Γ = 2T the gauge group is E₆. *This is I-6's construction: the transverse ℂ²/2T and the McKay E₆ are the same 2T by definition of the setup.*
- The partial topological twist on Q turns the three 7d scalars into a **1-form Higgs field φ ∈ Ω¹(Q; ad)**, and supersymmetric vacua are **Higgs bundles on Q**: `F_A − φ∧φ = 0, d_Aφ = 0, d_A*φ = 0` (Pantev–Wijnholt, arXiv:0905.1968, §2). The record's flat E₆(ℂ) connections A + iφ on m004 are exactly these vacua. The hyperbolic structure itself is one: A = spin connection, φ = vielbein.
- **Massless charged matter** is counted by twisted cohomology of Q — PW §3.1, verbatim: *"the four dimensional chirality is correlated with the degree of the form … Morse index one (+,+,−) gives a chiral fermion, and Morse index two (+,−,−) gives an anti-chiral fermion"*; and in general (PW 3.39) `N_χ(R) = h¹(M, ∂⁺M), N_χ̄(R) = h²(M, ∂⁺M)` where ∂⁺M is *"the boundary of M where the Morse function is increasing"*.

So the record's h¹ IS the literature's chiral count, and the literature's anti-chiral count is h² — which on a closed 3-manifold is h¹ of the dual by Poincaré duality. **B1260's definition of net chirality, h¹(V) − h¹(V\*), is PW's (3.39) specialised to closed Q.** I-26 is not unearnable; it is *this* — with a boundary term the record never carried.

## 2. The theorem

> **PW (3.40):** `net chiral(R) = χ(M, ∂⁺M) = χ(M) − χ(∂⁺M)`.
> **PW (3.63)**, for Q = S³ with the Higgs field singular on charge graphs Δ⁺, Δ⁻ (n components, ℓ loops each), M = S³ ∖ (Δ⁺ ∪ Δ⁻):
> `net chiral = n⁻ − ℓ⁻ − n⁺ + ℓ⁺ = χ(Δ⁻) − χ(Δ⁺)`, *"independent of r"* (the linking).
> **Braun et al. (2.50):** *"The chiral index is then given by the usual Euler characteristic, which vanishes for odd dimensional closed manifolds."* **(7.14):** `χ(M₃) = χ(Σ⁺) = χ(Σ⁻) = 0` as a *constraint* on any compact model.

Every chirality wall the record built between 2026-07 and 2026-09-06 is an instance:

| record wall | the theorem's instance |
|---|---|
| **E65** — Sym^n of SL(2) self-dual, net h¹ = 0 for every embedding | V ≅ V\* ⇒ h¹ = h² ⇒ χ-type index 0; embedding-independent because χ is |
| **B1260 §1** — PD on any closed N forces h¹(V) = h¹(V\*) | Braun (2.50): odd-dimensional closed ⇒ index 0 |
| **B1260 §2** — cusped abelian sector walled by reciprocity of Δ(t) = t² − 3t + 1 | the abelian Higgs field on the knot complement: χ(Δ) = 0 for the knot (§3 below) |
| **B1267** — W1/W2 rigid, index 0 | h¹ = h² = 0 on the exhibited non-self-dual systems: PW (3.61) with a loop locus gives h¹ = h² = 0 (§3) |
| **B1086** — closed double: h¹ = 5 or 2, never chiral in counts | PW (3.40) on a closed manifold: χ = 0 whatever h¹ is |
| **B1259** — no flat G₂ orbifold isolates a point | the flat special case of "no codimension-7 point"; the general statement is χ, not flatness |
| **B1255** — three 16s cannot live in one 27 | not an instance; a representation-theoretic wall that the frame makes moot (generations are *points on Q*, not summands of the 27) |

The seven walls are one line. The record proved it seven times because it never carried the boundary term, so it kept meeting the closed case.

## 3. The object, evaluated

All numbers in `computations/r56_endpoint_theorem.py`; m004's triangulation data confirmed with SnapPy (2 tetrahedra, 2 edges, 1 cusp, H₁ = ℤ, symmetry group D₄).

**(a) The object as PW's charge locus.** PW's non-compact branes are *"singularities in the Higgs field … located on a graph Δ in S³"* with M = S³ ∖ Δ. The figure-eight complement is this with Δ = 4₁. A knot has n = 1, ℓ = 1: **χ(4₁) = 0**, so `net chiral = 0` for either sign of charge, and PW (3.61) gives h¹(M, ∂⁺M) = h²(M, ∂⁺M) = 0: **no localized matter at all.** The same holds for every knot and every link (χ = c − c = 0) — the entire metallic family is chirality-blind by Euler characteristic.

**(b) The cusp version.** χ(m004) = 0 (Betti 1,1,0,0), so `net = −χ(∂⁺)` with ∂⁺ a subsurface of the cusp torus. Annuli give 0; k disks give ∓k. **Three generations ⇔ exactly three disks of one sign on the cusp torus** — three points on the object's one end. The cusp torus is the *space*; the three disks are the *point*. This is H5's chirality instance as an equation.

**(c) The object's own graphs.** The only intrinsic graphs the object carries are its ideal triangulation's edge graph (knot + 2 arcs: χ = −2) and dual spine (2 vertices, 4 edges: χ = −2). |net| ∈ {0, 2}. **No intrinsic structure with χ = 3.** (B1086's θ-odd h¹ = 2 is *not* claimed to be this 2; noted so no one banks the rhyme — E64's lesson.)

**(d) What "the closing" does and does not do.** Dehn filling gives a *closed* Q, and χ(closed) = 0: a filling can make the *manifold* chiral (B432: CS ∉ {0, ½}, 31/31 slopes) but **cannot make the fermion spectrum chiral**. Those are two different "chiral"s; the record's C22 (the closing supplies the bit) is true for the CS bit and false for the generation count. The fermionic count needs the E₆ locus to pass through **codimension-7 conical points** of the ambient 7-manifold (Acharya–Witten), which in Higgs-bundle language are the endpoints of the charge locus of a *larger* group's Higgs field breaking to E₆. That is a datum in a 7-manifold; a 3-manifold cannot carry it. **H5's mechanism is a codimension gap: 3 versus 7.**

## 4. The two sl₂'s (I-25), sharpened and found in conflict

B1256 left four labellings typing h¹ = 3 as three chiral. B1112's criterion — the object's canonical holonomy is PSL(2,ℂ), so a composed holonomy is choice-free only if the sl₂'s H has even weights on the 27, i.e. **all summands odd-dimensional** — is decisive:

| labelling | 27 = | Dynkin index (via the 27, index 6) | projective |
|---|---|---|---|
| principal (2,2,2,2,2,2) | 17+9+1 | **156** | ✔ |
| subregular (2,2,2,0,2,2) | 13+9+5 | **84** | ✔ |
| (1,0,1,1,1,1) | 8+7+5+4+3 | 29 | ✘ |
| (1,1,1,0,1,1) | 7+6+5+4+3+2 | 21 | ✘ |
| (1,0,1,0,1,1) | 6+5+4+4+3+3+2 | 14 | ✘ |

Two survivors. And the record has already chosen between them without noticing: **I-19 is EARNED (B1242) with the principal sl₂ — index 156 by three routes — as the embedding through which E₆ CS contains 3d gravity**, while **B1257 selects the subregular (84)** for the generation typing. The object's SL(2,ℂ) is one subalgebra, not two. Either I-25 = principal (then B1257's selector is a mathematical fact about E₆ that the object does not realise, and the h¹ typing is 1 abelian + 2 chiral, as B1253 said), or I-19 must be re-derived at index 84. By §2 the choice never affected net chirality; it does affect I-19's coefficient.

## 5. What "three generations" costs, exactly

PW §3.6 exhibits the literature's version of the record's goal: E₇ on Q = S³ broken to SO(10) × U(1)² by abelian Higgs fields whose charge graphs (their figure 5) give `h¹(M,f₆) = 2, h¹(M,−f₁−f₆) = 1` — *"precisely three chiral generations in the 16, three Higgs fields"* — from **charge configurations of points and arcs chosen by hand**. Translated to the object: an E₇ (or E₈) Higgs field on Q with E₆ unbroken, `133 = 78 + 1 + 27 + 27̄`, and a U(1) charge locus with **χ(Δ⁻) − χ(Δ⁺) = 3**. That is the complete, explicit content of "the listener map" on the generation question: **three endpoints on the object.** Nothing in the object selects them (§3c), and E64 already recorded that every "three" the record found was a count without a list.

## 6. The path, stated so it can be walked or refuted

1. **JOIN 1 is closed as posed and reposed.** As posed (a net-chirality count on the 3-manifold): zero, by theorem, for the object and its whole family. Reposed: *exhibit a G₂ 7-manifold containing Q = m004 (or a closing of it) as an E₆ associative through three codimension-7 conical points* — equivalently a Higgs field of a larger group on Q whose charge locus has χ = 3. This is an existence question in G₂ geometry, not a computation on the object. I-26 is earned by §1 the moment such an X is exhibited; until then it is correctly UNEARNED, and now for a stated reason.
2. **JOIN 3 dissolves rather than crosses.** In this frame Lorentz is the ℝ^{3,1} of the 11d bulk, not a subgroup of E₆; E₆(−26)'s "spacetime branch" is a different question (an algebraic one about real forms) from where gravity comes from (the bulk). B1265's rank obstruction is a true theorem about E₆ and says the charge branch cannot *contain* gravity — which is what the frame says too. The interactions meet in 11d, on X, not inside E₆.
3. **JOIN 2 relocates.** Gauge couplings are `1/α ∝ Vol(Q)` in 11d Planck units (a scale the object does not supply: A7); Yukawas are `exp(−t·Area)` of gradient-flow disks between critical points (PW §3.7). Neither is a period of the object, so V-3's exhaustive negative is *expected*. The object's Vol = 2.0299 and CS = 0 enter as *inputs to* X, not as SM ratios.
4. **What would falsify this report:** a chirality mechanism in M-theory on G₂ that is not a codimension-7 singularity (none is known; flux does not do it in 7d); or an intrinsic graph on m004 with χ = 3 (none found; §3c); or a demonstration that I-19's containment holds at index 84 (then B1257 stands and §4 reverses).

## 7. The price, in the record's currency

Nothing earned, nothing refuted on the ledger by this report alone. What it supplies: **I-26's missing licence (§1)**, **I-25's candidate set cut 4 → 2 with a conflict named (§4)**, **the seven chirality walls as one theorem (§2)**, **the exact shape of the missing input for three generations (§3b, §5)**, and **a reframing of JOINs 2 and 3 (§6)**. The record's H5 — "every space, never a point" — is, in this frame, the statement that a knot has no endpoints.

---

*Sources read on this bench: Pantev–Wijnholt, arXiv:0905.1968 (text extracted; §§2.5, 3.1, 3.2, 3.5, 3.6); Braun–Cizel–Hübner–Schäfer-Nameki, arXiv:1812.06072 (text extracted; eqs. 2.49–2.50, 4.16–4.17, 5.20, 7.13–7.14); Acharya–Witten hep-th/0109152 (abstract); record arcs B632, B1036, B1084, B1086, B1112, B1242, B1253–B1267, E64, E65, OPEN_ITEMS H5, IDENTIFICATION_LEDGER rows I-6, I-19, I-25, I-26. Repo sweep before every absence claim: "Pantev|Wijnholt" occurs in the record only inside B962's scout files, never as a frame; "Kaluza|Freund–Rubin" never.*
