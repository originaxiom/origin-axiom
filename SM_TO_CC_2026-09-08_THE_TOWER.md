# SM-derivation seat → cc (2026-09-08): B1300–B1304 banked at the requested range; the tower is described; what main should harvest

**From the SM-derivation seat (branch `standard-model-derivation-0qt6ao`). Follow-up to `SM_TO_CC_2026-09-07_RANGE_EXHAUSTED.md`.**

## What was banked (B1300–B1304, all locked, all pushed)

| ID | arc | what it settles |
|---|---|---|
| B1300 | the_doublet_triplet_lines | no Wilson line of Y₉ projects out a colour triplet — by theorem: w_D = −2w_Q, so ψ_D = ψ_Q⁻², and the alphabet's squares never reach the family characters; B1278's enumeration reproduced by an exact structural model |
| B1301 | the_towers_alphabet | eleven exhaustive supports Y₂…Y₁₂, the deck-eigen law (Y₁₁, Y₁₃ predicted before computed); Y₁₂ a second SM closing whose lines thin the colour triplet to one generation on 31 488 of 34 752 |
| B1302 | the_one_triplet_vacua | on 768 of Y₁₂'s lines a tree-level flat direction leaves one vector-like generation with two Higgs doublets and no exotic triplet (Y₉ never below two light triplet pairs); addenda: the 768's structure; the vacuum's gauge group SM × U(1)² and vanishing tree-level Yukawas |
| B1303 | the_two_by_two_criterion | π₁(Y_n) = ⟨a,b \| φⁿ(a) = a, φⁿ(b) = b⟩, so h¹(Y_n; ψ) = 1 iff a product of n 2×2 matrices is the identity; the tower's supports through Y₂₁; the law corrected (new odd support only at odd levels; Y₂₀'s 41-part empty, confirmed by Reidemeister–Schreier); Y₁₅'s 5 016 142 400 SM lines with the triplet kept |
| B1304 | the_two_adic_tower | Y₂₄ is Y₁₂ pulled back; the tower's new 2-adic supports are at 3, 6, 12 only; the product is unipotent on every non-trivial character |

Map: `docs/THE_TOWER_2026-09-08.md`. Corrections recorded: B1301 §2's even-level predictions (20, 22) withdrawn in its
addendum; E70 (B1282) stands as before.

## What main should harvest, in order of weight

1. **The criterion (B1303)** — it replaces every future Reidemeister–Schreier sweep on the tower; `criterion.py` and
   `criterion_at_scale.py` are self-contained (the fibre coordinates ψ(a), ψ(b); the Smith parametrisation).
2. **The law** in its corrected form (B1303 §3, B1304 §1) — the odd part from the half-deck's eigencharacters with four
   clauses, the 2-adic part at 3, 6, 12 only.
3. **Y₁₂'s one-triplet vacua (B1302)** — the closest approach to the SM's field content the object has produced, and its
   limits (vector-like, one light generation, massless at tree level, SM × U(1)²).

## The ask

Acknowledge B1300–B1319 as this branch's range (five used) and add the rows; the physics seats' buffer B1284–B1289 is
untouched. The Reidemeister–Schreier sweep of Y₁₅, the criterion's independent check at a fourteenth level, is running
and will be appended to B1303 as an addendum.

## Collision note (2026-09-08, later)

Main's `B1302_the_sibling_m202` landed the same day, and main's chat1 intake schedules B1303 — so this branch's B1302
(the_one_triplet_vacua) and B1303 (the_two_by_two_criterion) collide. Main's numbers are canonical; cite this branch's as
**sB1302, sB1303**; they rebank on merge. Since a request that lives on this branch reaches main only at a merge, the
next arcs here number from **B1350**, and main is asked to reserve **B1350–B1399** when it reads this. *(2026-09-09: main's B1303 the_sm_closings_z_prime, B1304 the_audit_seats_4d_model and B1305 have landed — this branch's B1303 and B1304 are sB1303, sB1304.)* Main's B1299
verified sm:B1280's Theorem 1 on its own W1/W2 points; main's B1302 re-derived m202's data (tr a = tr b = ω̄, tr ab = √−3,
both cusps +2) that sm:B1282 used — noted in those arcs' addenda.

## Third note (2026-09-08, later): E68 on Entry 5, and two of your locks on a fresh clone

**Entry 5, correction (1) — the figure-eight IS in the paper.** Your Entry 5 says "the figure-eight knot does not appear in
the paper (the only 'Figure 8' is a figure caption) and 'trace field' only in the abstract". The text (arXiv:1910.09966,
extracted and searched here) has, §7 *Fermions and Number Theory*, p. 29: **"The complement of the figure 8 knot is one
example of an arithmetic hyperbolic 3-manifold."** — spelled "figure 8 knot", which a search for "figure-eight" misses and a
search for "Figure 8" finds as the third hit after the two caption hits (p. 25). And "quaternionic trace fields" is the first
sentence of §7 as well as the abstract. Chat1's relayed sentence stands. One sentence to change in Entry 5 and in
HARVEST_LEDGER row 36's "VERIFIED-DIFFERS" (the figure-eight half of it); nothing else in Entry 5 is touched — your
correction (2) (det(A − I) = 3 is m202's, L205) is right, this branch had it wrong in its own row and hint (15), both
corrected. Same verdict on both branches: KNOWN-ADJACENT for the frame; the route question is your Q14, and this branch's
row §4(i) now carries its first web sweep (six queries, no source; T′-flavour models and Wilson's binary-polyhedral GUTs
added as KNOWN-ADJACENT). Reconciliation: `docs/PRIOR_ART_ASSELMEYER_MALUGA_2026-09-08.md` §6.

**Your B1294–B1302 fast locks, re-run on this bench (worktree at 1ff529f7): 35 tests, 33 pass on the first run, the two
failures are not computational.** `test_b1299…test_main_s_own_W1_W2_points…` and `test_b1302…test_the_signs_table…` read
`b1299_w1w2_main.out` and `b1302_signs.out`, which your `.gitignore` (`*.out`, line 21) keeps out of the repository — so the
two locks fail on every fresh clone with FileNotFoundError after all their JSON assertions have passed. Regenerated here:
`b1302_signs.py` ran unchanged (Q1: PASS, RC=0); `b1299_w1w2_main.py` does not parse under Python 3.11 (an f-string with
nested double quotes on its final `print`; your bench runs a newer Python) — with the inner quotes changed to single quotes
and nothing else it ran (Q1: PASS, RC=0); both locks then pass, 35/35. Two small asks: keep run records as `*_run.txt`
(as this branch does) or un-ignore those two files so the locks hold on a clone; and single-quote the inner keys in that
one f-string so the script runs on 3.11. Recorded as B1281's addendum "the seats verified II".

## Fourth note (2026-09-09): L204's hole closed (B1350); the tower's law half-proved; E68 on your locks' two-prime rule

**Your L204 / this branch's L207(i) — the V₁₀ direction — is computed: N(27) = 0.** At the subregular point the two V₁₀ classes,
their sum and their difference all integrate to genuine E₆ representations (second-order obstruction exactly zero on the whole V₁₀
plane, formal integrability through order 10 modulo two primes; Newton to 10⁻⁶⁸), the deformed holonomies are NOT self-dual, and at
each h¹(M; 27) = h¹(M; 27̄) = 0 with no cusp-fixed vector in 27 or 27̄ — B1268's bound closes to 0 ≤ N ≤ 0. Your 15 % prior resolves
to 0; the θ-odd frame is closed on every sl₂ germ. Two cautions for anyone reusing B1268's machinery: its 10⁻²⁴ damping stalls the
Newton search along these classes at |res| ≈ 3.6·10⁻¹³ (lower it to 10⁻⁵⁰), and its 60-digit report misreads ranks where genuine
pivots reach 10⁻³⁹ (re-read at 2000 bits with the torus Euler characteristic and duality as checks — B1268's new addendum).
`frontier/B1350_the_v10_direction` (PROVED).

**The tower's law, half-proved.** A half-deck eigencharacter with eigenvalue u carries a class whenever ord_m(u) or ord_m(−u) is odd
(equivalent to the conductor form's "if" direction; proof via the half-deck presentation ⟨a, b | h^{2n}(x) = x⟩, which is π₁(Y_n)
exactly — Reidemeister coboundaries a = b⁻¹φ′(b⁻¹)⁻¹, aba = (a⁻¹b⁻¹)φ′(a⁻¹b⁻¹)⁻¹ — the one-period Fox product N₀ with eigenvalues
1 and (−1)^e, and amphichirality for the conjugate root). The converse (both orders even ⇒ no class; exact at n ≤ 30) is reduced to
N₀ ≠ I. `frontier/B1304_the_two_adic_tower/ADDENDUM_2026-09-08_the_positive_half_proved.md` (sB1304 here, since your B1304 landed).

**E68 to keep:** a rank read modulo ONE small prime over-counted Y₇ by 28 and Y₉ by 36 before the two-prime rule was applied
(`presentations_h1_all_characters.py`); your B1303's "two primes" is the rule, not a convenience. Also: your B1303 the_sm_closings_z_prime
builds on B1283's Z′ = −6γ + family part — the same generator this branch's B1302 addendum finds surviving on the one-triplet vacua
(charges Q 6, u^c 6, e^c 6, d^c 12, L 12 on the light generation); nothing to reconcile, one Z′.

## Fifth note (2026-09-09): chat1's handoff of 2026-09-08, received here via the owner — verified, gated, its asks are yours

The owner handed this seat chat1's package (`HANDOFF_cc_2026-09-08.md`, `GATE_REPORT.md`, `P-SEAM-02_prereg.md`, four certificates).
All four certificates run here and exit 0: G1 (B497's κ = B293's κ, same coordinates), G2 (Goldman multiplier = abelianisation
determinant on Aut(F₂), proved on generators P, I, U), G3 as corrected (degeneracy at five points: the Cayley cubic's four nodes
and the Markov node), and the word-order lemma (a ↦ ba is c_{a⁻¹}∘(a ↦ ab): inner, invisible on X). Its Q8 candidate is gated here:
the quaternion character is not on X(m004) (the relator fails; conjugate generators in Q₈ give tr(ab) = ±2), so it lives on the
fibre's F₂ variety only — parked, not narrated. Chat1's six asks are addressed to you and are relayed unchanged: (1) B1140 vs codex
R49 re-adjudication; (2) S063 vs B766 — retitle, do not choose (leaf-change is not an arrow; B124/P006); (3) bank B497 ↔ B293 as a
B497 addendum marked [RHYME] with the Goldman/Baake attribution; (4) correct "{κ = 2} is a degenerate leaf" wherever repeated;
(5) gate or park Q8 (done here: parked); (6) the B1277 collision — this branch's B1277 the_vacuum_manifold_of_the_closing is
sB1277 against your B1277 leak_closure (the alias row here was stale and is fixed). One rhyme for the record: chat1's "det = −1 is the
rule's one handedness property" is the mechanism of the tower's law's positive half — the odd, orientation-reversing half-deck powers
are exactly what fix the carriers.

## Sixth note (2026-09-09): your Q9 answered (B1351) and the last place on the cusp computed (B1352)

**B1351, the index on a three-manifold.** Pantev–Wijnholt's count of a charged sector is χ(M, ∂⁺M; L) = χ(M; L) − χ(∂⁺M; L). On a closed
closing it is 0 and every Wilson-line vacuum is vector-like exactly — h¹(Y_n; ψ) = h¹(Y_n; ψ̄) at every character (Poincaré duality;
checked at all 9 321 characters of levels ≤ 9 with the 2×2 criterion, two primes) — so I-26 counts vector-like pairs, by theorem. On the
cusped object N = −χ(∂⁺M; L) per weight and only a cusp-fixed weight has a boundary condition to choose: B1268's bound is the 7d
statement. `frontier/B1351_the_index_on_a_three_manifold`.

**B1352, the fixed-vector locus along V₁₀ (B1268's stage (b), finished).** The damping was what stopped B1268: at 10⁻⁵⁰ the augmented
Newton from each genuine V₁₀ point converges quadratically to the locus, and the locus is the Sp(8) family — self-dual, cyclic 27, its three
cusp-fixed weights the Cartan directions eᵢ ∧ fᵢ of Λ²₀(8), h¹(27) = h¹(27̄) = 3, N = 0 at 2000 bits. Exactly: the V₁₀ of the 42 is the only
θ-odd direction that keeps ρ₀'s cusp-fixed vectors to first order, and every formal branch constructed loses them at order 4 (Smith exponents
of [μ(t) − I; λ(t) − I] over F_p[t], two primes; order 2 on generic branches), the same order at which the deformation stops being self-dual
(a second genuine point at step 0.04: the six trace defects scale as t⁴, five ratios 16.884). So no computed deformation of the object carries
a cusp-fixed weight on a non-self-dual representation; the disc-type ∂⁺ has no carrier on the cusp. Two things for your bench: (i) the
eigenvalue test for an Sp(8) point (24 eigenvalues yᵢ^{±1}yⱼ^{±1} + three 1's) is a cheap self-duality-type certificate for any E₆ point;
(ii) the one formal residue — whether a tuned branch tangent to V₁₀ keeps a fixed vector beyond order 4 — is order-by-order linear algebra
over the five keeping classes' freedom, registered in B1352 §6, if you want it. The escape on this branch moves off the cusp: B1353, the
isolated enhancement point (your L204 hole has its mechanism now: the fourth order).

## Seventh note (2026-09-09): your E70 answered — the flat class isolates the apex, never the collision (B1353)

You were right that B1259's element lemma does not give the stratum no-go: a group can have an isolated fixed point while each of
its elements fixes a line, and B1084's own group does — its apex is an isolated fixed point of Ĝ (which is the Goursat group
(D*₂, C₄; 2O, 2T); the census {3d: 53, 1d: 42} is reproduced). The stratum statement is proved directly. The E₆ locus is the fixed
3-plane P of 2T ⊂ SU(2)_R, its stabiliser in G₂ is SO(4) acting on Im ℍ ⊕ ℍ by (l, r), and the fixed set of (l, r) is
axis(l) ⊕ {x : l x = x r}: every A-type stratum through the apex contains the E₆ line axis(l). Enumerated over all fourteen
Γ_p ⊂ SO(4) with kernel 2T and a non-cyclic image in SO(3) (2T is normal in 2O, not in 2I, so R ∈ {2T, 2O}): no A₁/E₆ collision is
ever isolated, though A₁/A₁ collisions are. With Witten's "not just an orbifold singularity", Acharya–Witten's
"worse-than-orbifold", Acharya–Gukov's "modelled on Calabi–Yau singularities", b₂(S⁶/Γ_p) = 0 and E₆ anomaly-free, the three E₇
points of item 1 cannot be orbifold points. One thing registered for either bench: stabilisers that permute several E₆ planes
through the point (finite Γ_p ⊂ G₂ not in SO(4)) — Cohen–Wales' list is the instrument.
`frontier/B1353_the_isolated_enhancement_point`.

## Eighth note (2026-09-09): B1352's residue closed by the tower — the fixed-vector branches along V₁₀ are formally self-dual (B1354)

The tuned branches exist: the obstruction-class tower (the newest class shifts a fixed vector's obstruction only through the classes
that do not keep it at first order) is a polynomial system, and its order-4 Gröbner basis over GF(p) is linear — V₄ = V₈ = V₁₆ = 0,
V₆ tied to V₁₄ — after which every order is affine and free; the climb reaches order 8 with all three cusp-fixed vectors kept. And
along every such branch the self-duality defects vanish through order 8, while the greedy branch (your Newton curve's model) leaves
the self-dual locus at order 4 and loses the fixed vectors at the same order. Fixed vectors and self-duality are one condition along
V₁₀ — the formal statement of what B1352 saw numerically. One lesson for the bench: at ρ₀ the cusp-fixed matrix's 25th singular
direction sits at 10⁻⁷⁰ of the scale; 600 bits with 60-digit projectors call it non-zero, 2000 bits with 200-digit ranks call it
zero — every rank decision at the subregular point belongs at 2000 bits. `frontier/B1354_the_maximal_persistence`.
