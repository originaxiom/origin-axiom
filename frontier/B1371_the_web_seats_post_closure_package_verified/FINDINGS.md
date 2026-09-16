# B1371 — THE WEB SEAT'S POST-CLOSURE PACKAGE, VERIFIED: chat1's four documents and thirteen scripts of 2026-09-15 re-derived on this bench with its own code, negatives included — the Bianchi indices and the class membership by shape field, the four-property table with the 2T and 2I doors, the census scans, the Lefschetz numbers L(g) = 3 of the order-3 isometries of m202 and s959, the non-semisimple Fox computations, the decision-table inputs, the covering negative, the Chern–Simons gate and the homology ladder all hold; one claim is refuted (the Sol boundary m004(0,1) has irreducible SU(2) representations, forty binary dihedral ones from det(A + I) = 5); two are scoped; the "no one- or three-cusped det = 3" observation is a theorem (fixed ends come in pairs); nothing in the package changes a verdict of the record

**Date:** 2026-09-16 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (every re-derivation exact or to stated precision) with one REFUTATION and two SCOPINGS of the package's claims · **Price: unchanged** · **Numbering:** B1371 (the owner's hand-over of chat1's unbanked work, 2026-09-16).

## 0. Seen from above

chat1 — the web seat: no branch, no arc numbers, limited compute — sent, through the owner, its post-closure work: a closure handoff
written as reasoning ("the worries are the payload"), post-closure findings, a second addendum of self-corrections, and the I-26
decision table, with thirteen small scripts. The owner asked for everything to be verified, negatives included. This arc re-derives
every checkable claim with this bench's own instruments (not the package's scripts): Humbert's formula, the class membership by the
shape field at 200 bits, the symmetry groups and their amphicheirality, surjection counts onto SL(2,3) and SL(2,5), the census scans
over the classic census, the action of the isometries on H₁ and H₂ from B1369's instrument, Fox calculus over F₃ and over ℚ(ω), the
low-degree covers, representations of the Sol manifold m004(0,1), the Chern–Simons gate and the slope law. The package holds up well
for a seat with its tools: the Bianchi picture (m004 and m003 at index 12, m202 at 24, s959 at 36, v3551 at 42, s596 at 30; v3461,
t10829, t12582 outside the class), the four-property table (m004 achiral with 48 surjections onto 2T; the Weeks manifold chiral with
none onto 2I; m129 and m125 chiral with 192; m202 and s959 chiral with 96 and 576 and two order-3 isometries), the census facts
(exactly m202, s776, s784, s959 chiral with a door and an order-3 among the m and s manifolds; exactly m202, s959, v3461, v3551 with
a cusp-fixing order-3 isometry of det(A − I) = 3 among the first 4 815), the Lefschetz numbers L(g) = 3 with H¹ = ω ⊕ ω² for the
order-3 isometries of both siblings, the non-semisimple witnesses (h¹ = 2 against 4 on m202), the decision-table inputs, the
covering negative, the Chern–Simons validity gate, the homology ladder and the cube root of unity in the commutator trace — all
reproduced. One claim is refuted: the Sol boundary m004(0,1) is not exhausted by reducible SU(2) connections; det(A + I) = 5 for the
figure-eight monodromy gives four characters with χ∘A = χ⁻¹ and forty homomorphisms with non-abelian image in the binary dihedral group
of order 20, i.e. irreducible SU(2) representations, which the package's count |det(A − I)| = 1 (the abelian ones) missed. Two are
scoped: the mod-3 Fox number on s959 depends on the homomorphism chosen (4 or 5, not 5), and the m + s census has 1 263 manifolds, not
1 400. One empirical observation becomes a theorem: an orientation-preserving isometry of finite order fixes geodesics that are closed
or proper arcs, so its fixed points on the cusp tori come in pairs, and a single cusp with three fixed points (or three cusps with
three each) is impossible. For the record's questions the package brings no new door: its §B (unitary ⇒ vector-like) is B1297's on
main and B1368/B1369's here, its §C (Chern–Weil: flat bundles are representation-blind in four dimensions) is correct and orthogonal
to the seven-dimensional frame in which the record's chirality lives, and its §4 (the arithmetic ℤ/3 of 2T/Q₈ is E₆'s centre, not the
trinification grading) is right and closes a joint the record never used.

## 1. The package's claims, one by one

`verification/verify_package.py` (about a minute; record `verify_package_run.txt`).

| # | claim (the package's) | this bench | verdict |
|---|---|---|---|
| 1 | Humbert: vol(ℍ³/PSL(2, O₃)) = 0.169156934 | |D|^{3/2} ζ_K(2)/(4π²) with L(2, χ₋₃) = 0.7813024129: **0.169156934402** | VERIFIED |
| 2 | indices: m004 12, m003 12, m202 24, s959 36, v3551 42, s596 30; v3461, t10829, t12582 non-integral | vol/v₀ = 12, 12, 24, 36, 42, 30 (integral to 10⁻⁶); 39.343, 41.260, 44.817 | VERIFIED |
| 3 | class membership by the shape field (every tetrahedron in ℚ(√−3)): m004, m003, m202, s959, v3551, s596 in; v3461, t10829, t12582 out | 200-bit shapes, PSLQ on Re z and Im z/√3: **6/6 in** (2/2, 2/2, 4/4, 6/6, 7/7, 6/6 shapes); v3461 4/7, t10829 2/8, t12582 5/8 out; m129 0/4 | VERIFIED (B1186's exact criterion agrees) |
| 4 | index 12 holds exactly m003 and m004; index 24 has 7, index 36 has 12 | census at 12v₀: {m003, m004}; at 24v₀: 7 (m202, m203, m206, m207, m208, s118, s119); at 36v₀: 12 through the 8-tetrahedron manifolds, **13** with o10_030703 | VERIFIED; the 12 SCOPED to the package's census depth |
| 5 | the four-property table: m004 (D₄, achiral, 48 onto 2T, no order-3); Weeks m003(−3,1) (chiral, 0 onto 2I, two order-3); m129/m125 (chiral, 192, none); m202/s959 (chiral, 96/576, two) | \|Sym\| 8, 12, 8, 8, 12, 12; amphicheiral only m004; order-3 elements 0, 2, 0, 0, 2, 2; surjections onto SL(2,3): 48, 0, 192, 192, 96, 576; Weeks onto SL(2,5): 0 | VERIFIED |
| 6 | census (m + s): exactly m202, s776, s784, s959 are chiral with a 2T door and an order-3 isometry; det(A − I) = 3 for m202/s959, 0 for s776/s784; fields ℚ(√−3) and ℚ(√−7) | the m + s census has **1 263** manifolds (not 1 400): the four hits exactly; surjections 96, 1 152, 336, 576; cusp-fixing order-3 maps with det 3 on m202/s959, none or det 0 on s776/s784 (their order-3 isometries permute cusps); shape fields as stated | VERIFIED, the size SCOPED |
| 7 | 2T: the order-3 elements of SL(2, F₃) have trace −1, are unipotent, none in Q₈; ℤ/3 = 2T/Q₈ acts on irreps by tensoring with a character, fixing the 3-dimensional one: the centre of E₆, not the Kac grading; det(Cartan E₆) = 3 | 8 order-3 elements, traces ≡ 2 = −1, (A − I)² = 0, none of order 1, 2, 4; on 2T ⊂ SU(2) built explicitly, 3 ⊗ χ = 3 and 2 ⊗ χ ≠ 2 as characters; det = 3 | VERIFIED |
| 8 | Lefschetz: the order-3 isometries of m202 and s959 have L(g) = 3, tr H₁ = −1 (eigenvalues ω, ω²), tr H₂ = 1 | from B1369's instrument on the canonical retriangulations (no finite vertices): the two order-3 automorphisms of each have (tr H₁, tr H₂, L) = (−1, 1, 3); the full tables: identity (2, 1, 0), the cusp-fixing involution (−2, 1, 4), the six cusp-swapping involutions (0, −1, 0), the order-6 elements (1, 1, 1) | VERIFIED |
| 9 | non-semisimple witnesses: over F₃ the unipotent module has h¹ = 2 on m202 (semisimplification 4) and 5 on s959 (6); over ℚ(ω) on m202, dims 2, 3, 4 give 2 against 4, 6, 8 | F₃: m202 h¹ = 2 for all 8 non-trivial homomorphisms, trivial 4; s959 h¹ ∈ {4, 5} over the 26 homomorphisms, trivial 6; ℚ(ω): m202 (2, 2, 4), (3, 2, 6), (4, 2, 8) | VERIFIED for m202; s959's 5 SCOPED (homomorphism-dependent) |
| 10 | the decision table's inputs: χ(M) = 0; order-3 fixed points [3, 3] on m202, s959; every det = 3 manifold has a cusp swap and hexagonal cusps; s596 is 2-cusped, hexagonal, D₄, without order-3 | χ = 0 on all; cusp-fixing det by order: m202, s959, v3551, v3461 all {2: (4, 4), 3: (3, 3), 6: (1, 1)}; cusp swaps present; shapes e^{iπ/3} or e^{2πi/3}; s596: D₄, orders {1, 2}, hexagonal, swap present | VERIFIED |
| 11 | rows A–F of the I-26 table; none promoted; row E closed by the cusp swap | arithmetic on the inputs (A/B/C 0; D −Σ fixed points; E one cusp; F −cusps); the swap makes a one-cusp condition non-invariant | VERIFIED as arithmetic (the conventions themselves are the bridge lane's R23) |
| 12 | the covering negative: m004's and m003's degree-2 and degree-3 covers are unique and one-cusped; m202 and s959 are not covers of either | degree 2: one cover each, 1 cusp, vol 4.059766, H₁ = ℤ/5 ⊕ ℤ; degree 3: one each, 1 cusp, vol 6.089650; not isometric to m202/s959 | VERIFIED |
| 13 | the Sol boundary: every SU(2) flat connection on m004(0,1) is reducible; \|det(RL − I)\| = 1 gives one abelian point | π₁ = ⟨a, b \| aaabABBAb, aBAbABab⟩, H₁ = ℤ; homomorphisms into the binary dihedral groups Dic_n, n = 2..6: **40 with non-abelian image in Dic₅**, none for n ≠ 5 — irreducible SU(2) representations exist; the reason: det(A + I) = 5 for the monodromy [[2,1],[1,1]], four characters with χ∘A = χ⁻¹ | **REFUTED** |
| 14 | the Chern–Simons gate: SnapPy returns cs for m004(p,1), p = 0..3, with flat tetrahedra and volume 0 (0, 0.0119, 0.025, 0.0417); p = 4 n/a; p = 5 the first hyperbolic filling (vol 0.9813688); the slope law CS(p, −q) = −CS(p, q) 8/8 on the hyperbolic slopes | reproduced line by line; slope law 8/8 to 10⁻⁸ | VERIFIED |
| 15 | the homology ladder H₁(m004(p,1)) = ℤ, 0, ℤ/2, …, ℤ/6 | reproduced | VERIFIED |
| 16 | κ − 2 = ω for m004's generating pair, presentation-independent | tr[a, b] = 1.5 + 0.866i, κ − 2 = ω; invariant under the Nielsen moves (b, a), (a⁻¹, b), (ab, b), (a, ab) | VERIFIED |
| 17 | det(A − I) = 3 family: m202, s959, v3461, v3551 in the first 6 000; the family grows with the census; no 1- or 3-cusped member; det = 3 forces hexagonal cusps; 11 hexagonal → 5 two-cusped → 4 with order-3 | first 4 815: exactly those four, all two-cusped; hexagonal 11, two-cusped 5, with order-3 4; the lattice fact is the classification of order-3 automorphisms of plane lattices | VERIFIED; the parity part PROVED (§2) |
| 18 | §B: a non-zero index needs a non-unitary local system (B1297's theorem on main) | consistent with B1351 (i), B1368, B1369 (unitary ⇒ no Higgs field ⇒ N = 0) | CONSISTENT |
| 19 | §C: Chern–Weil — a flat bundle on a spin 4-manifold has ind D = −rk·σ/8, representation-blind | correct; the record's index is Pantev–Wijnholt's on the 3-manifold with a boundary term, not a 4-dimensional flat-bundle index — orthogonal | CORRECT, ORTHOGONAL |
| 20 | §D: main has a certified Dirac operator on m004 with λ₁ = 2.974550580 | not re-derived here | NOT VERIFIED |

## 2. The parity theorem (the package's empirical "no 1- or 3-cusped det = 3")

An orientation-preserving isometry g of finite order of a cusped hyperbolic 3-manifold fixes a union of geodesics, each closed or a
proper arc with two ends at cusps. On a cusp fixed by g, its affine action on the torus has |det(A − I)| fixed points, each the end of
a fixed arc. So the total number of fixed points over the fixed cusps is even. One cusp with three fixed points is impossible; three
cusps with three each is impossible; two cusps with [3, 3] is what m202, s959, v3461, v3551 show, and Lefschetz then gives L(g) =
χ(three arcs) = 3, which is the tr H₁ = −1, tr H₂ = 1 of item 8. ∎

## 3. What the package brings the record

1. **Nothing that changes a verdict.** Its independent routes to zero (unitary local systems, Chern–Weil) are the record's or orthogonal
   to it; its census facts relocate nothing that B1186 and B1369 do not already hold (the family, the siblings' isometries, the
   count of three as B1321's order-3 rotation).
2. **One refutation of its own negative.** The Sol boundary m004(0,1) carries irreducible SU(2) representations (two conjugacy classes,
   binary dihedral of order 20), so "the character variety is empty" and the conclusions drawn from it in its addendum §6 fall.
3. **One theorem for its observation** (§2), and one useful scoping for future scans: cusp-permuting isometries have no fixed-point
   count on a cusp — the package caught this itself (addendum §2); this bench's instruments filter on the cusp permutation throughout.
4. **On the door-2 question** (B1372): the package's emphasis on non-unitary and non-semisimple local systems points where B1372 looks;
   its mod-3 witnesses are examples of the Alexander-module phenomenon over F₃, not physical sectors.

## 4. Caveats

1. The field test is numerical (200-bit shapes, PSLQ with coefficients up to 10⁹, a zero guard for purely real or imaginary shapes);
   B1186's exact criterion is the reference and agrees.
2. Symmetry groups and amphicheirality are SnapPy's; the automorphism counts of B1369's instrument agree on every member used here.
3. The 2T and 2I surjection counts are raw (not divided by automorphisms), as the package reports them.
4. Item 20 is left unverified; it is a main-branch claim outside this arc's scope.

## Verification

`verification/verify_package.py`: twelve sections as listed in its docstring. Lock: `tests/test_b1371_the_web_seats_post_closure_package_verified.py`
(the whole script, about a minute).

**Sources.** The package (chat1, 2026-09-15: the closure handoff, the post-closure findings, addendum 2, the I-26 decision table, thirteen
scripts), received from the owner. Humbert's formula; Neumann–Reid for the shape field; the Lefschetz fixed-point theorem; Riley for
two-bridge groups; B1186, B1281, B1282, B1351, B1368, B1369, B1372; main's B1297 and B1321.
