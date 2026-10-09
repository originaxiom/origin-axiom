# The weave: what the joint action of every allowed move forces on every thread at once

cc (the SM-derivation seat), 2026-10-07. **Structure and proofs only. No count is read.** Written for the owner's rule,
stated daily for a year and given a fixed name today, **the weave** (`docs/THE_WEAVE.md`). The rule: reality comes from
the interaction of all the objects the principle allows, together, and not from single objects or from covers of one.
- A **thread** is one allowed object, a closed path of moves through the shared fibre.
- **The weave** is the joint action of all the moves on that fibre, and what it forces.

Nothing below is read off one thread. Each step is PROVED here and checked by the scripts beside this note, unless it is
marked READING or OPEN. Nothing is promoted, and 0 of 19 stands.

**CLOSED on 2026-10-08 at W29, by the owner's plan.**
- The state is `docs/THE_THREE_GENERATIONS_STATE_2026-10-08.md`.
- Main's grade (GENESIS v1.28): the flavour three is derived; the gauge three is a selection.
- Two checks followed the close, and both ran on 2026-10-08. W30: an order-3 flux is allowed on the swap's fork, not
  forced. W31: no ℤ₅ flux gives an anomaly-free three.
- W32 (the owner's "do as u recomend on all"): in F-HE the puncture's end condition does not make three.
- W33: "three exactly when the odd spin structure is left out" is not a law; under the spinor rule three needs rank six.
- W34 (the owner's question about the observer layer): its negatives belong to every thread, not to m004; the
  register carries no hand; it supplies no missing ingredient.
- W35 (the owner's goal: the full Standard Model): main's B1612 mixing patterns verified with this seat's code.
- W36: the audit lane's Standard Model centralizer in E₈ verified; no SU(5)_g chirality from any SU(5)_b bundle on a
  two-dimensional object.
- W37: main's S92 verified: TM1's forward prediction (δ = 262.5° or 97.5°) and the observer layer on the weave.
- **The owner's rulings of 2026-10-08** (`docs/THE_OWNERS_RULINGS_2026-10-08.md`): even ticks observed (GENESIS
  GM5c); Λ a tagged working postulate (GENESIS FK11 open); naturality for flat counts only (GENESIS FK10
  open); positivity kept. On the ruled branch the results for L and R alone apply.
- W38: main's B1615 and B1616 verified: the weave's group fixes no mass, charged or neutrino.
- W39 (a reading given Λ): the masses' tensor is T ⊗ T; at weight 0 a Higgs without flavour gives no mass.
- W40: main's B1617 verified, given τ = ω: the residual group (order 48) keeps T irreducible.
- W41: the weave's zero modes have modular weight −¾ (f has weight ¼, index 0); the input main asked for.
- The assurance round (2026-10-08): the exact results survived independent re-derivation; conventions and readings corrected (relay §42).
- W42: main's B1620 verified exactly (68 subgroups in 26 classes; 57 / 24 / 16 viable), from one closed form of the
  group; every thread's own zero modes break the parity grading only along a body diagonal (main's ask 2).
- W43: B1620's "TM1 allowed under T ⊗ T" does not hold in its frame (the family is TM2); given Λ, TM1 needs a
  frame where c is gauge and an antisymmetric Yukawa, and under Sym² T no trimaximal family appears in any frame.
- W44: the 13 are unreduced in every frame on record (the CKM needs the full four everywhere); the lepton sector
  allows at most two relations, and under Sym² T where c is gauge one (a failed prediction: 3, not 4).
- W45 (given Λ): on the weave's own surface the triplet's four-dimensional Dirac index is 0 for both hands at the
  weight the geometry forces, with no zero modes at all; T lives on the metaplectic cover. Post hoc: only end data at
  the cusp moves the index, by 3n for n units on every component.
- W46 (given Λ): for every end condition the weave keeps on its own surface, the four-dimensional index is n times the
  fibre's index, n the cusp's units; with the natural cusp condition there is no zero mode at all. The record's ±3
  becomes four-dimensional only with one unit of end data at the cusp (GENESIS FK10).
- W47 (main's named arc, given Λ): nothing on the weave's surface forces the cusp's unit. The natural cusp conditions
  coincide (no integer exponent), and the 24 flat line bundles move the index by at most one. Three needs a non-flat
  source at the cusp (GENESIS FK10).
- W48 (the owner's outside source, given Λ): a c = 24 source gives one chiral mode per eight lattice-free chiral bosons,
  so three needs the 26-dimensional bosonic string's 24, and the heterotic string gives one. GENESIS FK10 stays open.
- W49 (the owner's turn to the free numbers): the weave's three generations are one zero mode three times, T = ℓ ⊗ M,
  with M the three imaginary quaternion units; the end conditions that keep three are exactly the ones blind to M
  (three or split). Post hoc: the inner automorphisms are not words in L and R, so on the ruled branch whether the
  parity grading holds at a fixed τ is W50's question.

## The setting

- **The shared fibre** is the two records, F₂ = ⟨a, b⟩, with puncture loop [a, b] (GENESIS GM1, GM4).
- **The moves.**
  - L and R are GENESIS GM2.
  - The swap P is GENESIS GM5c, OPEN.
  - The sign −I is filed under GM5b in this branch's GENESIS (v1.10). Main's GENESIS v1.14 (B1482) makes it a move of its
    own, which positivity (GM5d, CHOSEN) excludes. Either way the − threads are an extension of the grammar.
  - The weave below uses all four. Where L and R alone give a different answer, both answers are stated. The triplet's
    structure (W1–W4) needs neither the sign nor P: the sign acts on it as a fibre translation, and P only doubles its
    group (`the_weaves_laws.py`).
- **The words and the threads.**
  - The words are every hyperbolic word in the moves, with either sign, up to rotation. To length 8 there are 2,554, and
    1,308 of them have odd trace.
  - They are words, not threads: LPLP and LR are one matrix (m004), and powers such as LRLR are counted. W1–W3 are
    statements about each word's matrix mod 2, so they hold word by word.
  - The threads are GENESIS's states (758 to length 12), with the orientation-reversing bundles if P is legal. m000 (LP,
    the Gieseking manifold), m003 (−LR), m004 (+LR) and +LLLR are among them. None is derived from another.

## W1. The three (`moves_and_parities.py`)

- **The parities.** Mod 2 the records have three non-zero parities: (1, 0), (0, 1) and (1, 1).
- **Each single move fixes exactly one of them and swaps the other two.**
  - L fixes (1, 0), R fixes (0, 1) and P fixes (1, 1).
  - −I fixes all three.
- **Any two of L, R and P generate all six permutations of the three** (GL(2, F₂) = S₃), and their product cycles all
  three.
- **So the three belongs to no single move.** It appears as three parities permuted with none distinguished only when
  moves act together.
- **Which threads cycle the three.** A thread cycles them exactly when its trace is odd (sm:B1550's parity lemma). That is
  1,308 of the 2,554 words, and 326 of GENESIS's 758 states to length 12, m000, m003 and m004 among them.
- **Along the wave (the trichotomy, `the_weaves_laws.py`).** At tick n a thread acts on the parities as (φ mod 2)ⁿ. An
  odd-trace thread has one orbit at ticks 1, 2, 4 and 5, and fixes all three at ticks 3 and 6. Of the 758 states, 268 act
  as an involution (a line and a pair) and 164 fix all three at every tick.
- **GENESIS's SE1** (∣2 − tr φ∣ = 1, so tr φ is 1 or 3) admits only odd-trace threads.

## W2. The common point (`the_common_point.py`, part 1)

- **The moves act on the fibre's characters** (x, y, z) = (tr a, tr b, tr ab) by polynomial maps that keep tr [a, b].
- **One point is fixed by every move.**
  - The puncture is parabolic: tr [a, b] = −2, which is the Markov surface x² + y² + z² = xyz.
  - The ideal of points fixed by every move is then (x, y, z), so there is exactly one such point: the origin.
  - The origin is the quaternion representation a ↦ i, b ↦ j, ab ↦ k, [a, b] ↦ −1.
  - Without the cusp condition the moves fix one more point, (2, 2, 2), where the puncture is trivial.
- **Each thread fixes the origin and its own geometric points besides** (exact Gröbner bases):
  - ±LR: two points, the roots of z² − 3z + 3, the same two for m004 and m003, since the sign acts trivially on
    characters;
  - +LLR, +LLLR and +LLRR: four points each;
  - an orientation-reversing thread such as m000: its geometric point is fixed by the map followed by complex
    conjugation. The map itself fixes only the origin.
- **So the threads' geometries differ, and the one structure they all share is the quaternion point.**
  - A single shear already fixes only the origin on the Markov surface, so the point's uniqueness is not the joint
    action's. That every thread shares it is.
- **From the principle (exact; sharpened 2026-10-07).**
  - On the whole character variety, with no puncture condition, L and R fix exactly two characters. The Gröbner basis
    of the fixed-point ideal is (x − z, y − z, z² − 2z), and the swap adds nothing.
  - The two are the quaternion point (κ = tr [a, b] = −2) and the trivial character (κ = 2).
  - GENESIS PF1's mathematical reading, non-cancellation as κ ≠ 2, removes the trivial character, where the cancellation
    completes. GENESIS v1.1 calls that reading motivation, not a premise.
  - So the weave's vacuum is forced by the principle and the joint action together.
- **On record.**
  - Main's B141 has the quaternion point as the unique irreducible fixed point of the metallic map.
  - Main's B148 places it on the Markov surface.
  - This seat's sm:B1538 has its character ζ_H invariant under every Anosov monodromy.
  - **New here:** it is the only point every move fixes.

## W3. The common point on every thread (part 2)

- **The quaternion point extends to every thread.**
  - t ↦ g in the binary octahedral group 2O, with g i g⁻¹ = ρ(φ(a)) and g j g⁻¹ = ρ(φ(b)).
  - There are two choices, ±g.
- **On all 2,554 threads to length 8 the image is the binary tetrahedral group 2T = SL(2, F₃), of order 24, exactly when
  the trace is odd.**
  - It is Q₁₆ when φ fixes one parity, and Q₈ when φ fixes all three.
  - Modulo ±1 it is the fibre-parity group: A₄, D₄ or V₄.
- **So the tetrahedral cover and the spin cover built on m004 are not m004's.** They are sm:B1550's and the held
  sm:B1551's.
  - They are the kernels of this common structure on one thread.
  - m000, m003, +LLLR and every odd-trace thread carry the same A₄ and the same 2T.

## W4. The triplet (part 3)

- **The shared fibre carries a three-dimensional space with one axis for each non-zero parity.**
  - The space is the parity-twisted cohomology ⊕_χ H¹(F₂; χ), summed over the three non-trivial parity characters.
  - Each axis is one-dimensional, because the punctured torus has Euler characteristic −1.
- **The moves and the fibre's own inner automorphisms act on it by signed permutations.**
  - The group they generate has order 48 and acts irreducibly: Σ tr² / ∣G∣ = 1.
  - L, R and the fibre alone generate a group of order 24, also irreducible. It is T_d, which is S₄: L and R act as
    reflections, and −1 is not in it (`the_weaves_laws.py`).
  - The sign acts as the fibre translation by ab and adds nothing. The swap P doubles the group to O_h.
  - Every element is conjugate to its inverse, so all the characters are real: the weave's group carries no hand.
- **Every odd-trace thread acts on it as an irreducible triplet.**
  - The group of the thread's monodromy and the fibre is A₄, of order 12, for m004, m003 and +LLLR. A₄ has a complex pair
    of characters, but which is which is a marking: conjugating by L (LR → RL, one manifold) carries the monodromy into
    the class of its inverse.
  - For the orientation-reversing m000 it is A₄ × ℤ/2, of order 24.
- **Even-trace threads split it.** +LLRR splits it into three axes, and +LLR into 1 + 2.
- **It matches the quaternion axes thread by thread, not on the weave as a whole.**
  - On m004, m003 and +LLLR it is the same representation as the axes i, j, k under the common point, with equal traces on
    all 12 elements.
  - On m000 it is the same up to m000's orientation sign.
  - On the weave as a whole the two triplets are different representations. Together they generate 192 pairs.
- **Prior: the A₄ triplet of flavour physics.**
  - The triplet of A₄ flavour models: Ma and Rajasekaran (hep-ph/0106291); Altarelli and Feruglio (hep-ph/0504165).
  - Altarelli, Feruglio and Lin obtain the A₄ from the four fixed points of T²/ℤ₂ (hep-ph/0610165). Their ℤ/3 comes from a
    hexagonal torus.
  - Here no torus is special. The ℤ/3 is the monodromy mod 2 of any odd-trace thread, and the triplet is the weave's.
- **Prior: the mathematics.**
  - Looijenga's Prym representations, Geom. Dedicata 64 (1997), study the mapping class group on such twisted cohomology.
  - Goldman, Geom. Topol. 7 (2003), studies the modular group on the one-holed torus's characters.

## W6. What each parity carries (`the_lines_census.py`, `the_lines.py`, `the_lines_content.py`)

**Theorem G, the parities carry alike (PROVED).**
- **Setting.** On an odd-trace thread M, N is its forced A₄ cover (W3) and M₃ = N/V₄ its third level.
- **A member's parity** is the non-zero parity of the edge the member lives on, or of the one translation t_p that fixes it.
- **For an orbit of the deck group A₄ in which every member has a parity:**
  - every member of a V₄ orbit has the same parity;
  - the weave's 3-cycle carries parity p to parity φ(p);
  - a third of the orbit sits on each parity;
  - on M₃ the orbit gives one sector per parity, Ind from N of the member, cycled by the weave, each carrying the member's
    count.
- *Proof.*
  - V₄ is abelian, so a translation keeps a member fixed by t_p fixed by t_p.
  - Translations keep an edge's direction. An edge fixed by t_q has direction q, so the two labels agree.
  - The 3-cycle acts on V₄ by conjugation as φ mod 2 acts on the parities.
  - Shapiro's lemma carries the count to M₃. □
- **Scope.**
  - The proof uses only W3, so it holds on every odd-trace thread.
  - An orbit fixed by all of V₄ (size 3) sits on no single parity.
  - The theorem does not say that any thread has members.

**The census (design-time structure, no count; the rule named before the run).**
- **The rule:** every odd-trace state of GENESIS to word length 6, twelve threads. On each thread, every A₄ orbit of
  characters of order dividing 4 (and, as a second pass, 3) on the forced cover, with the structure (h¹, r¹, n) of ν ⊗ ρ in
  route P.
- **A member** is a character with n > 0. A generation-shaped count needs one: Theorem C bounds I(Λ²W₁) between −n and 0.
  It also needs ν⁴ = 1 or a trivial end, by Lemma F′ (I(W₁) ≥ k − m_A − b0).
- **Precision.** The banked library runs unchanged, with its precision raised from the script: holonomy at 160 digits,
  modules at 100.
  - At 50 digits −LLLLLR's cover failed the library's own relator guard, and no reading was taken there.
  - At 100 digits the script reproduces sm:B1550's banked census of ±LR and ±LLLR exactly (54 and 6 members).

| thread | trace | order 4: characters, members | order 3: characters, members |
|---|---|---|---|
| +LR | 3 | 1024, 54 in 8 orbits | 81, 6 (m_A = 0) |
| −LR | −3 | 256, 6 in 1 orbit | 81, 6 (m_A = 0) |
| +LLLR | 5 | 256, none | 729, none |
| −LLLR | −5 | 1024, none | 81, none |
| +LLLLLR | 7 | 4096, none | 81, none |
| −LLLLLR | −7 | 256, none | 729, none |
| +LLLRLR | 13 | 256, none | 81, none |
| −LLLRLR | −13 | 1024, none | 729, none |
| +LLLRRR | 11 | 1024, none | 729, none |
| −LLLRRR | −11 | 256, none | 81, none |
| +LLRLRR | 15 | 4096, none | 81, none |
| −LLRLRR | −15 | 256, none | 81, none |

**Status: complete.** All twelve threads are read at order 4 and at order 3, one pass each. The last, +LLRLRR at order 4
(4,096 characters in 416 orbits), took 2 h 39 min (9,526 s) and has no member.

- **Among the threads read, members appear only on the golden pair ±LR.**
  - The order-3 members there have m_A = 0 and ν⁴ ≠ 1, so Lemma F′ keeps them from being generations.
- **Generations, by sm:B1550's sealed two-route counts, appear only on +LR among the threads read.**
- **±LR are the only arithmetic odd-trace primitive threads** (Bowditch–Maclachlan–Reid, as reported by
  Goodman–Heard–Hodgson). Members fall exactly there: a pattern on twelve threads, not a theorem.

**What each parity carries** (`the_lines_content.py`: the census, the parities and sm:B1550's banked counts joined; no count
computed). **This is a thread result:** the frame reads one thread's own holonomy, and the content found is +LR's.
- **+LR: every parity carries six sectors on the third level,** each reading (−1, −1).
  - That is one generation of each of six types: two sign types, edge-labelled, and four order-4 types, fixed by t_p.
  - Up to the other order (complex conjugation) and the spin twist the six are three classes.
  - The two orbits fixed by all of V₄ read (1, 0), on no single parity.
- **−LR: every parity carries one sector reading (0, −3).** It is not a generation.
- **Every other thread read: nothing.**
- **In main's two standards (S79), +LR's three is the orbifold standard.** Per type it is three sectors of index one,
  distinguished by the parity characters and cycled by an order-3 symmetry.
  - The cover is forced by the parities, not chosen by a character, and three is never selected. Main still counts a
    three on a cover's own characters as a selection until its FK14 is ruled. This seat's answer, that the cover is
    forced, is not in GENESIS.
  - Summed, the three sectors are the pullback of one module on +LR itself (B1384, B1390; sL-7). That is one generation
    at tick 1 and three at tick 3 (the gcd law). Which is physical is GENESIS FK7, the deck kept or gauged: B1506's one
    bit, now shown to be the same bit on every odd-trace thread (`docs/THE_WEAVES_LAWS.md`, Theorem S).
- **Graded by THE BAR**, "only +LR carries" is a positive on one state, with p ≈ 0.29 on twelve threads. It is not
  claimed as a selection.

**The mixing (READING, group theory only; `the_mixing.py`).**
- **The weave's group on the triplet is O_h** with P, and T_d (which is S₄) without it.
- **With the golden thread's 3-cycle as one sector's residual symmetry:**
  - the swap P, or L·a, R·b or LPL, as the other's fixes the TM1 column (L·a and R·b need no P);
  - the sign or a fibre translation fixes the TM2 column;
  - a single shear gives θ₁₃ = 0;
  - Klein groups give tri-bimaximal or democratic mixing.
- **Mod 2 the golden thread is ST,** the rotation fixing τ = ω, and the swap is S, fixing τ = i.
- **No comparison with data is made here.** The fences are in `docs/THREE_GENERATIONS_AND_THE_WEAVE.md` §3. Which sector
  keeps which subgroup is not forced.

## W7. What the parities carry at the tick where the weave separates them (`the_parity_sectors.py`)

**The census in Theorem S's sense** (design-time structure, no count; the rule named in the script before the run).
- **The rule.**
  - Every state of GENESIS to length 6 (24) is read at its resolving tick: 3 at odd trace, 2 for an involution mod 2, 1
    at φ ≡ I mod 2.
  - The characters read are those of the tick whose fibre restriction is a parity, with κ ∈ μ₁₂.
  - At each, the structure of ν ⊗ ρ in route P is read. A member has n > 0.
- **The control** is sm:B1530's banked silver pair.
  - +LLRR at κ = −1 has members at (½, 0) and (0, ½) and none at (½, ½), as banked.
  - −LLRR has the same two members, with h¹ = 2 and one interior class, as banked. They are read at κ = −1 where
    sm:B1530 reads κ = 1.
  - At (0, 0) and (½, ½), h¹ = 1 at κ = 1, as sm:B1530's simple members.
  - This is consistent with the library's stable letter for a − state differing from sm:B1530's by ab mod 2.
- **The record:** `the_parity_sectors.json`; the raw lines are in `the_parity_sectors.jsonl.gz` (sha-256 in
  `the_parity_sectors_sha256.txt`).

| class | states | tick | members |
|---|---|---|---|
| odd trace | ±LR, ±LLLR, ±LLLLLR, ±LLLRLR, ±LLLRRR, ±LLRLRR | 3 | none |
| an involution mod 2 | ±LLR, ±LLLLR | 2 | on the two parities the deck exchanges, at κ = 1, (h¹, r¹, n) = (2, 1, 1), trivial on the one cusp; none on the parity it fixes |
| an involution mod 2 | ±LLLRR, ±LLRLR | 2 | none |
| φ ≡ I mod 2 | ±LLRR | 1 | on the two parities the isometries exchange, at κ = −1; none on (½, ½), which they fix |
| φ ≡ I mod 2 | ±LLLLRR | 1 | none |

**What it shows.**
- **Members sit only on pairs.** In this sense the parities carry members on six states. On each, the members are on
  exactly the two parities the state's own symmetry carries into one another, and never on the one it fixes.
- **On no odd-trace state are they on all three.** At tick 3 the three are one orbit of the deck, and none of the
  twelve carries a member at a parity character.
- **No member at the zero parity anywhere.**
- **What is and is not a generation.**
  - These are members, not counts. sm:B1530's counts make each of ±LLRR's two a generation, (−1, −1).
  - The members on ±LLR and ±LLLLR at tick 2 have no count yet. A count needs a sealed arc.
- **The two constructions disagree on +LR.** Theorem G's sense (W6, the forced cover's own characters) finds the
  three alike on +LR. This sense finds nothing on +LR at tick 3.

## W8. The frame at the weave's own vacuum (`the_weaves_vacuum.py`)

**Why.** Main's S80: W6 needs a weave instrument, defined by the joint action and read on all threads at once, and every
frame on record is a thread instrument. The record's frames read a thread's own vacuum, its hyperbolic holonomy ρ, through
four(ρ): X ↦ gXg* on Hermitian matrices. The weave has one vacuum of its own, the common point ρ_Q (W2), which every move
fixes and every thread carries (W3).

**The module (PROVED).**
- four(ρ_Q) = 1 ⊕ 3. The 3 is the adjoint, which is W4's parity triplet thread by thread, and it does not see the sign
  ±g of the extension.
- So ν ⊗ four(ρ_Q) is a sum of rank-one lines. By Shapiro each is a character of the thread's resolving tick:
  - ν on the thread itself;
  - ν·λ_p on the tick, one for each parity orbit.

**Lemma V (PROVED): no rank-one line on a once-punctured-torus bundle is interior.**
- **The statement.** Let ν be a character of a hyperbolic once-punctured-torus bundle, of finite order when it is
  trivial on the fibre. Then h¹(ν) ≤ 1. When h¹(ν) = 1, ν is trivial on the cusp and the class restricts to it
  injectively, so n(ν) = 0.
- **Proof.**
  - **u = ν∣F trivial.** The Wang sequence gives h¹ = 1 only for the trivial character: the act's eigenvalues on H¹(F)
    are not roots of unity. That class, the fibration's, is non-zero on the cusp.
  - **u non-trivial: the fibre.** H⁰(F; u) = 0, so H¹(M; ν) injects into H¹(F; u), which is one-dimensional
    (χ(F) = −1).
  - **u non-trivial: the puncture.** H¹(F; u) → H¹(∂F) is onto, because the next term H²(F, ∂F; u) ≅ H₀(F; u) is 0. So
    it is an isomorphism, and a class of M restricts non-trivially to the puncture loop.
  - **u non-trivial: the cusp.** That loop lies on the cusp torus. If ν were non-trivial on the cusp, H¹ of the torus
    would vanish and so would the restriction. So ν is trivial on the cusp, and the class restricts injectively. □
- **Every tick is such a bundle.** So the lemma holds on every state at every tick: WEAVE + WAVE.

**The census, by rule** (every state to length 6 at its resolving tick; one pass; exact over ℚ(i)).
- **The parity lines.** Each of the three parities carries exactly one line on every one of the 24 states: h¹ = 1 at
  one κ = ±1. The line is trivial on the cusp and restricts to it injectively. That is 72 lines, none interior.
- **Every character of order dividing 4.** 768 were read on the 24 ticks. None has n > 0.

**What it shows.**
- **At the weave's own vacuum the three parities are alike on every thread, of every class.** At the resolving tick
  each carries one line.
- **All three lines are on the end.** They are main's T-COMPANION-NO-ROOM lines, and none is interior.
- **The frame at the weave's vacuum has no members on any state at any tick (Lemma V).** So, if Theorem C's bound
  I(Λ²W₁) ≥ −n holds at this vacuum (to be checked, since four(ρ_Q) is reducible), it reads no generation anywhere.
- **The three's content needs something else.** It needs a thread's own geometry (the hyperbolic vacuum, where W6 and
  W7 find members) or the vacuum's spin part, which four(ρ_Q) does not contain. W9 shows the spin part carries
  interior classes on every thread. On the forced spin cover (W3's 2T kernel, fibre genus 3) those are the cover's own
  lines, which is where main's T-ROOM-NEEDS-GENUS puts room.

## W9. The weave's spin doublet (`the_spin_room.py`)

**The object.**
- **The space.** H¹(F₂; ρ_Q) is the fibre's cohomology with coefficients in the common point itself: the
  two-dimensional spin representation a ↦ i, b ↦ j. It is two-dimensional, because H⁰ = 0 on the free group of rank two,
  and it is the same space for every thread.
- **Every thread's classes in it are interior.** ρ_Q([a, b]) = −1, so the cusp carries no invariant vector and its H¹
  vanishes.
- **The extension condition.** A thread's class extends exactly at the κ where the act S: [z] ↦ [g⁻¹ (z ∘ φ)] has
  eigenvalue κ, with g the lift of W3 (±g changes S to −S).

**The joint action (COMPUTED).**
- **With L and R.** With their lifts they act as commuting rotations, by 45° and 135°, and the sign as one by 90°. The
  group is cyclic of order 8, with two characters.
- **With the swap.** It becomes Q₁₆, of order 16, irreducible, with real characters.

**Every thread has room here (COMPUTED; two routes).**
- **Route 1.** On all 24 states to length 6, every lift acts on the doublet with finite order (1, 2, 4 or 8). So every
  thread has interior classes at its own tick: h¹ = 2 at one κ = ±1, or 1 + 1 at a conjugate pair of κ.
- **Route 2.** Fox calculus on the bundle group reproduces the dimensions on five states: ±LR, +LLR, −LLRR and +LLLR.

**With the parities (COMPUTED).**
- **The modules.** At each state's resolving tick the parity-twisted doublets H¹(F₂; χ_p ⊗ ρ_Q) are read with the
  deck-compatible tick, the act's own k-th power, and the inherited lift gᵏ. A marking that differs by an inner
  automorphism shifts κ by χ_p of it: the same shift as W7's − states.
- **The three are alike for every lift on 22 states.** That is all 12 odd-trace states at tick 3 and all 8 involution
  states at tick 2.
- **The two exceptions split 2 + 1.** These are +LLRR and −LLLLRR at tick 1.
- **On the thread itself.** On an odd-trace thread, 3 ⊗ ρ_Q = 2 ⊕ 2′ ⊕ 2″, the three spin representations of 2T. So the
  three sectors are one module of the thread, whose three summands carry the same content at three values of κ that
  differ by a cube root of unity.

**What it shows.**
- **Only the abelian part of the weave's vacuum is empty (Lemma V).** Its spin part carries interior classes on every
  thread.
- **With the parities it gives three alike interior sectors on every odd-trace thread at its third tick,** not only
  on +LR.
- **Whether they are generations needs a frame for the spin module.** One is F-HE read on the forced spin cover, where
  these classes are the cover's own rank-one lines (Shapiro). That is not sealed; main reviews it first.
- **READING, the hand.**
  - Without the swap the joint action is abelian. So the doublet splits into two complex-conjugate lines, and every
    L,R-thread keeps them apart: a candidate for a hand that is not a marking.
  - The swap exchanges them, as charge conjugation would. That fits GENESIS FK3, where B1083 types the swap as the
    C-type bit.
  - With the swap the group's characters are real.

**The hand rule (COMPUTED on all 758 states to length 12; `the_spin_hand.py`).**
- **The rule.** The doublet's two conjugate lines sit at different κ exactly when n_L − n_R + 2·[sign −] ≢ 0 (mod 4).
- **The check.** The act's eigenvalues computed directly agree on 758 of 758: 513 states keep the lines apart and 245
  keep them together.
- **On the states that are their own mirror** (the 34 words whose swap is a rotation of the word or of its reverse, 68
  states), every + state keeps the lines together and every − state keeps them apart.
- **That matches main's B1479 from a different object.** Main finds that on every amphichiral word to length 12 the −
  state is the one on which a hand can be registered. Here it is read off the weave's spin doublet.

## W10. The chiral triplet (`the_chiral_triplet.py`)

**The space.**
- V is the sum of W9's three parity-twisted spin doublets, H¹(F₂; χ_p ⊗ ρ_Q) over the three parities. It is
  six-dimensional and the same for every thread.
- A move m with a lift g carries the χ-doublet to the (χ ∘ m)-doublet by z ↦ g⁻¹ (z ∘ m). So the moves act on V,
  permuting the parities.
- Every thread's class in V is interior.

**The joint action (COMPUTED).**
- **With L and R (the sign adds nothing): a group of order 96.**
  - Its commutant on V is two-dimensional, and V = T ⊕ T̄: two irreducible triplets, complex conjugate to each other.
  - Their characters are not real. That is a three with a hand: B356's "chiral candidate" exists on V.
- **What the group is.** It is the fibre product of S₄ and ℤ/8 over the sign, A₄ ⋊ ℤ/8. Its derived subgroup is A₄
  (order 12), its center is ℤ/4, its abelianization is ℤ/8, and it has 20 classes.
  - Each move is odd on both factors at once: a reflection on the parity triplet (T_d) and a rotation by an odd
    multiple of 45° on the spin doublet. So the weave glues the real S₄ of the triplet to the phase of the spin line.
  - T is S₄'s triplet times a faithful character of ℤ/8, and that is why it is complex.
- **With the swap: a group of order 192, and V is irreducible.** The swap exchanges T and T̄. This group has 19
  classes, center ℤ/2 and derived subgroup of order 48.
- **The group is finite.** So every thread at every tick acts on V with finite order and carries interior classes
  there.

**Every state at its resolving tick (COMPUTED, 24 states; the deck-compatible act, the inherited lift).**
- **On every odd-trace state at tick 3 the act is a scalar on T and on T̄.** T's three classes, one per parity, sit at
  one κ, and T̄'s at the conjugate κ̄.
- **When κ ≠ κ̄ (eighths 2 and 6, κ = ±i), one vacuum character carries T alone.** It is three alike, separate,
  interior and chiral.
- **That happens on exactly one sign twin of every odd-trace word: the twin with n_L − n_R + 2·[sign −] ≡ 2 (mod 4)**
  (W9's hand rule; odd-trace words have even length).
  - To length 6 those twins are −LR, +LLLR, −LLLLLR, +LLLRLR, −LLLRRR and −LLRLRR.
  - The other twin carries T and T̄ together at κ = ±1, which is vector-like.
- **The root's pair.** m004 (+LR) carries T ⊕ T̄ together. m003 (−LR), its sign twin, carries T alone at κ = i and T̄
  alone at κ = −i.
  - That fits main's GENESIS v1.23 reading that "both of the physics' mechanisms need what the sign-twin's side has", and
    main's B1479.
- **Elsewhere at the resolving tick.**
  - On three involution states (+LLR, −LLLLR, +LLLRR at tick 2) and on −LLRR (tick 1), the two triplets also sit apart
    at single κ.
  - On the other even-trace states the act is not a scalar on T, and the triplets share values of κ.

**What it shows, and what it does not.**
- **What the weave carries.** Without any one thread chosen, the parities of the shared records tensored with the
  weave's own spin vacuum carry, under the joint action of L and R, a chiral triplet: three alike, cycled by the deck at
  the third tick, interior, with complex character.
- **Where it sits alone.** On exactly one sign twin of every odd-trace word, one vacuum character carries it alone.
- **Each of the three is not a generation in F-HE's frame.** sm:B1552 read it, sealed: (0, 0) at all 864 readings. W11
  proves the zero on every thread at every tick.
- **Not shown: that the third tick counts.** That is GENESIS FK7, the deck kept.
- **The swap.** If the swap were a legal move it would join T and T̄ into one real six (GENESIS GM5c). The hand on V
  needs the swap to stay outside the moves, or a vacuum that tells κ from κ̄.

## W11. The frame's count at the spin vacuum is zero (sm:B1552; `the_spin_zero.py`)

**The sealed count (sm:B1552, NEGATIVE as sealed).**
- F-HE's count was read on W10's chiral triplet: the twelve odd-trace states to length 6 at tick 3, two candidate modules,
  both lifts, every κ with room, two draws, two routes.
- All 864 readings are (0, 0). The routes, the draws and the three parities agree everywhere.
- It was sealed on the owner's ruling, ahead of main's review.

**The theorem behind it (PROVED; WEAVE + WAVE).** At the weave's spin vacuum, I(W₁) = 0 for every non-zero class.
- **Scope.** Every state at every tick, every κ, every sum of twists λ ρ_Q.
- **The proof** is sm:B1509's T2 and T3 (this seat, 2026-10-01) read at the common point:
  - the puncture acts on A by −1, so A has no cusp cohomology;
  - Q₈ fixes no vector, so A has no fibre invariants;
  - T2: I(W₁) = −r₁, with r₁ = 1 exactly when e ∪ c = 0. Its proof does not use h¹(A) = 1;
  - T3: e ∪ c = 0 needs a Jordan block of S_A at eigenvalue 1;
  - S_A is κ times an element of W10's finite group (W9's ℤ/8 on the doublet), so it is semisimple.
- **So the frame reads no generation and no anti-generation at the weave's spin vacuum,** on any thread, at any tick, in
  any rank.

**The checks (COMPUTED).**
- (1) T2's quantities on sm:B1552's record hold at all 864 readings: r₁(W₁) = 0, h⁰(W₁*) = 1, r₁(W₁*) = 2, and
  n(W₁) = n(W₁*) = n(A) − 1.
- (2) The act on V of every state to length 12 (758, both lifts) has 96th power the identity.
- (3) On the states to length 6 at ticks 1–3 (every resolving tick), the tick's act is the k-th power of the state's act.

**What it means.**
- The weave's spin vacuum gives the three, alike, separate and with a hand, but no content in this frame.
- **A count needs one of two things:**
  - cusp cohomology of A, as at the hyperbolic vacuum's parabolic puncture (sm:B1530, sm:B1550);
  - or a Jordan block of the stable letter at eigenvalue 1 (sm:B1509).
- **The vacuum that joins a thread's geometry to the spin part, λ ⊗ ρ_hyp ⊗ ρ_Q, was named next. It is empty (W12).**
  Its puncture fixes a vector, but none of its classes is interior.
- **What the seat got wrong.** W11 could be read before sm:B1552's seal. The run confirmed the theorem; it was not needed
  to learn the answer.

## W12. The joined vacuum has no interior class (`the_joined_vacuum.py`)

**The module.** A = λ ⊗ ρ_hyp ⊗ ρ_Q: a thread's own holonomy, lifted to SL(2, ℂ), tensored with the weave's common point
and a character.
- The relay THE CHIRAL TRIPLET'S COUNT named it as the next read. Its puncture acts by (−U) ⊗ (−1) = U, which fixes a
  vector, so W11 does not apply.

**The theorem (PROVED, from the literature; WEAVE + WAVE).** No class of H¹(M; A) is interior, on any state at any tick.
So F-HE, which extends by an interior class, reads nothing there.
- **Shapiro.** H*(M; A) is a summand of H*(N; ρ_hyp), where N is the finite cover on which λ ⊗ ρ_Q is trivial.
  Restriction to the boundary respects the splitting.
- **Menal-Ferrer and Porti** (Osaka J. Math. 49, 2012). On a complete hyperbolic 3-manifold of finite volume,
  H¹(N; ρ_n) → H¹(∂N; ρ_n) is injective for the n-dimensional representation composed with any lift of the holonomy.
  ρ_hyp is the case n = 2.
- **So the interior part of H¹(M; A) is zero.**

**The check (COMPUTED, 50 digits).**
- The population: all 24 states to length 6, at tick 1 and at the resolving tick, both signs of the stable letter, both
  lifts of the common point, every parity that is a character there.
- 44 (state, tick) pairs. 736 readings carry a class: every κ in μ₂₄ where the peripheral torus fixes a vector. At
  every one, n = 0 and h¹ = r¹ = h⁰(T; A), so half lives and none of it is interior.
- At the 992 controls (κ = e^{2πi/7} and κ = 2), h¹ = 0.

**What it means.**
- **Where F-HE's content can live.** The frame's own module at a thread's geometry is the balanced four
  ρ_hyp ⊗ ρ̄_hyp, whose interior (cuspidal) classes need not vanish. The record's members live there, on covers, and thread
  by thread (sm:B1550; main's B1602: +LR, −LR and −LLRLRLRR to length 8).
- **The weave's own vacua carry none.** The spin vacuum reads zero (W11). The joined vacuum has no interior class (W12).
- **So in F-HE the content of a generation is a thread's, not the weave's.** That is a law about the frame, and it puts
  the open step at the frame (GENESIS FK11), not at another vacuum of this kind.

**Main's F-CI frame, read for comparison (READING, cited).**
- At the three-fold level, main's B1434 finds generation-shaped backgrounds in deck orbits of three on every odd-trace
  state in its range (±LR, ±LLLR, ±LLLLLR), each counting one.
- On the root those orbits sit on the twelve order-4 fibre characters, the square roots of the parities, not on the
  parities (sm:B1506). On other threads they sit on other characters.
- So F-CI's three is the deck's ℤ/3 at the weave's resolving tick on every odd-trace thread in range. Read with the deck
  kept (GENESIS FK7), an orbit's deck-invariant sum counts three. That is the record's closest approach to three alike
  generations from the weave, and it needs F-CI's dictionary (UNEARNED) and FK7.

## W13. Main's F-CI orbits of three, read with this seat's code (`the_class_index_orbits.py`)

**What is read.** Main's B1434 carries the E₆/27 frame (F-CI) to every signed state to length six. At the three-fold
level it finds generation-shaped backgrounds in deck orbits of three. Its six odd-trace rows in range are ±LR, ±LLLR and
±LLLLLR.

**The engine.**
- It is sm:B1506's census, built on sm:B1374's index library, carried from m004's tower to any state's mapping torus in
  the weave's marking: ⟨a, b, t ∣ t x t⁻¹ = φⁿ(x)⟩, with peripheral pair (u⁻¹t, [a, b]) and deck x ↦ φ(x).
- The rest is unchanged: the loci, every candidate module, the index at three primes, the generation-shaped backgrounds,
  their lifts and deck orbits.

**The result (VERIFIED).** On the engine route the four rows ±LR and ±LLLR agree with B1434 exactly: the backgrounds, those that lift, and those with ν^c of the generation's sign. Every background sits in a deck orbit of three, every count is one in absolute value, the signs split equally, and no firing module differs at another prime. W14's slope-law route reads all six rows, ±LLLLLR included, and agrees with every one.

| state | backgrounds | lift | with ν^c | + : − | seconds |
|---|---|---|---|---|---|
| +LR | 48 | 0 | 48 | 24 : 24 | 1.5 |
| -LR | 96 | 0 | 0 | 48 : 48 | 2.6 |
| +LLLR | 72 | 0 | 24 | 36 : 36 | 145.3 |
| -LLLR | 48 | 0 | 48 | 24 : 24 | 112.3 |


**What it means for the weave.**
- At the weave's resolving tick, on every odd-trace thread in range, F-CI's generation-shaped backgrounds come in threes
  cycled by the deck, and each counts one generation in all five charged sectors.
- The three is the trichotomy's 3-cycle at tick 3. The content per background is F-CI's.
- This is link c of the chain in the synthesis (`docs/THREE_GENERATIONS_AND_THE_WEAVE.md` §4a).

**Not shown.**
- **The six longer odd-trace threads** (±LLLRLR, ±LLLRRR, ±LLRLRR; tick-3 torsion 1 296 to 3 332). On this engine they
  would cost about a day each: the square of the torsion times the relator's length. W14's slope law reaches them in
  minutes.
- **That an orbit's three vacua are three generations of one world** (GENESIS FK7; B1384's fence).
- **F-CI's dictionary** (GENESIS FK11).

## W14. The slope law for F-CI's index, and F-CI's census on every odd-trace thread to length 6 (`the_slope_law.py`)

**The slope law (PROVED; checked against sm:B1506's engine at every candidate module on ±LR and ±LLLR).**
- **Slopes.** Each non-trivial character χ trivial on the cusp has a one-dimensional H¹. Its class takes a non-zero value
  on the fibre's boundary [a, b]. Its slope s(χ) is its value on u⁻¹t divided by its value on [a, b].
- **The index.** F-CI's doublet [[α, c_λ β], [0, β]] (β = α − λ) has class index
  [s(α) = s(λ)] − [s(β) = s(λ)], and 0 when λ, α or β is trivial.
- **The proof.**
  - main's B1297 identity;
  - restriction of H²(M; α) to the cusp is an isomorphism, so a cup product of two classes vanishes exactly when their
    slopes agree;
  - sm:B1509's T3 for the degenerate cases.
- **Corollary: the signs.** (λ, α) ↦ (−λ, α − λ) reverses the index. So every background pairs with one of opposite
  sign, and main's B1434 P6 (signs split equally on every level) is a theorem.
  - The pair differ in the order of the extension: which character is the sub and which the quotient. That is main's
    "the count is the order" (B1466, B1486, B1499), here exact in F-CI.

**The census (COMPUTED; all twelve odd-trace states of GENESIS to length 6, at tick 3).**

| state | order of G | slopes | backgrounds | lift | deck orbits | + : − | B1434 |
|---|---|---|---|---|---|---|---|
| +LR | 16 | 3 | 48 | 0 | 48 in orbits of 3 | 24 : 24 | yes |
| −LR | 20 | 5 | 96 | 0 | 96 in orbits of 3 | 48 : 48 | yes |
| +LLLR | 108 | 13 | 72 | 0 | 72 in orbits of 3 | 36 : 36 | yes |
| −LLLR | 112 | 18 | 48 | 0 | 48 in orbits of 3 | 24 : 24 | yes |
| +LLLLLR | 320 | 35 | 720 | 240 | 720 in orbits of 3 | 360 : 360 | yes |
| −LLLLLR | 324 | 41 | 360 | 0 | 360 in orbits of 3 | 180 : 180 | yes |
| +LLLRLR | 2156 | 217 | 144 | 72 | 144 in orbits of 3 | 72 : 72 | — |
| −LLLRLR | 2160 | 198 | 2776 | 1216 | 16 in orbits of 1, 2760 in orbits of 3 | 1388 : 1388 | — |
| +LLLRRR | 1296 | 115 | 1584 | 288 | 1584 in orbits of 3 | 792 : 792 | — |
| −LLLRRR | 1300 | 139 | 720 | 408 | 720 in orbits of 3 | 360 : 360 | — |
| +LLRLRR | 3328 | 553 | 0 | 0 | none | — | — |
| −LLRLRR | 3332 | 555 | 0 | 0 | none | — | — |

The law against the engine: +LR: 256 modules, 0 mismatches; −LR: 400 modules, 0 mismatches; +LLLR: 11664 modules, 0 mismatches; −LLLR: 12544 modules, 0 mismatches.

**What it means.**
- **The law makes the census cheap.** A level costs one cocycle per character. Main's range limit (torsion 330) is gone.
- **F-CI's content at the weave's resolving tick is common but not universal.**
  - Ten of the twelve odd-trace threads to length 6 carry generation-shaped backgrounds.
  - All of them sit in deck orbits of three, except −LLLRLR's sixteen deck-fixed ones. Those are main's own-level
    backgrounds of s639 (B1434's P3), pulled back.
  - **±LLRLRR carry none:** both signs of one word, the two longest traces (±15). +LLRLRR's tick-3 group has 3 328
    characters in 553 slope classes, and −LLRLRR's has 3 332. The slope law was checked against the engine on a sample
    of +LLRLRR's modules (all 300 agree, 60 firing; `the_slope_law_sample.json`).
- **So in F-CI, too, a generation's content is not a weave law.** The three is the weave's; the content is ten
  threads' of twelve, not every thread's. By the owner's rule this is not the weave's answer.
- **The parities never serve as an extension character that fires,** on all twelve (check (4)). On ten their slope class
  is exactly the three, which is closed under differences, and that proves it. On +LLLRRR and +LLRLRR the class is
  larger (67 and 15), and the zero is observed. The content sits on characters of higher order, in threes cycled by the
  same deck.
- **What decides content (READING, with a route to a theorem).**
  - The slope classes are unions of orbits of the deck together with χ ↦ −χ (checked on the six in-range threads). On
    ±LR they are exactly those orbits; elsewhere further coincidences merge orbits.
  - The tick-3 group has order |t − 2|·(t + 1)², with t the trace. On its (t + 1)-part the deck acts as an Eisenstein
    cube root of unity.
  - So when the classes are the orbits, the five sectors' conditions become kernels of small Eisenstein integers on
    ℤ[ω]/(t + 1). Whether a thread carries content is then a question about the arithmetic of its trace.
  - +LLRLRR (t + 1 = 16; 553 slope classes against 559 orbits, and −LLRLRR likewise near its 561) is nearly the case
    where the forced orbits alone decide, and they give nothing. +LLLRRR, with 115 classes against 219 orbits, carries
    1 584.

## W15. The hand theorem, the weave's own extensions and their mod-16 law, and the weave's five (`the_hand_theorem.py`, `the_weave_extension.py`, `the_prediction_test.py`, `the_weaves_five.py`)

**The occasion.** Main's S83 (B1603) named what would earn the dictionary, GENESIS FK11:
- a module and a count on the weave;
- the shape identity n_5̄ = n_10 built in;
- a chirality handle other than the index (main's B1487: the class index is mirror-even for every module).

W15 takes the three in turn, on the weave's own modules.

**Theorem H, the hand (PROVED for every odd-trace word; checked).**
- **(i)** W10's triplet T is the sum of three lines, one in each parity's doublet; so is its conjugate T̄.
- **(ii)** So a move with a lift acts on T by a monomial matrix. It permutes the lines as the move permutes the
  parities mod 2.
- **(iii)** A monomial 3 × 3 matrix whose permutation is a 3-cycle has its cube equal to its determinant times the
  identity. An odd-trace word cycles the parities, so at tick 3 it acts on T as the scalar det(w|T), and on T̄ as the
  conjugate.
- **(iv)** det(w|T) is a character of the moves. In eighths of a turn, with the two lifts: L 1 or 5, R 3 or 7, the sign
  2 or 6. Mod 4 it does not depend on the lifts.
- **(v)** So T and T̄ sit at different κ exactly when det(w|T) = ±i, that is, when n_L − n_R + 2·[sign −] ≡ 2 (mod 4).
  That is W9's hand rule, now a theorem. Exactly one sign twin of each odd-trace word has it, since the sign adds 2.
- **(vi)** The swap carries T to T̄, so a thread's mirror sits at the conjugate κ: the hand is mirror-odd.
- **The checks.**
  - (i), (ii) and (iv) on the generators, with both lifts.
  - (iii) against the tick-3 act computed directly on all 32 odd-trace states to length 8: 32 of 32.
  - (v) on all 326 odd-trace states of GENESIS to length 12: 326 of 326. On each of the 163 odd-trace words exactly one
    twin is chiral.
- **What it gives.** The hand is the determinant of the weave's triplet: a character of the moves, read on each thread
  at its resolving tick. It is mirror-odd and it is not an index. That is main's third condition, met on every
  odd-trace thread.
- **What it does not give.**
  - Which of T and T̄ is left-handed: one bit, a dictionary's.
  - Index chirality at the weave's vacuum. That vacuum is unitary and every class there is interior, so a count of zero
    modes pairs κ with κ̄ and is vector-like; W11 is one case of this.

**The weave's own extensions (the index formula PROVED on the page; the census COMPUTED by rule).**
- **The module.**
  - For each non-zero parity p, B_p is the parity character made trivial on the cusp (W8). h¹(B_p) = 1, and its class
    ℓ_p is on the end.
  - A = ρ_Q ⊗ χ_q ⊗ κ is a twisted spin doublet (W9): acyclic on the cusp, every class interior.
  - A class c ∈ H¹(A ⊗ B_p*), a weave class, gives the rank-three module X = [[A, c B_p], [0, B_p]].
  - Every ingredient is the weave's, so X is defined on every odd-trace thread at once.
- **The formula.** By main's B1297 identity: h⁰ vanishes for X and X*, A is acyclic on the cusp, and B_p is trivial on
  it. So I(X) = 1 − r₁(X), and r₁(X) = 1 exactly when ℓ_p lifts to X, that is, when c ∪ ℓ_p = 0. Hence
  **I(X) = [c ∪ ℓ_p ≠ 0] and I(X*) = −I(X).**
- **The census, by rule** (sm:B1374's engine over GF(p), p ≡ 1 mod 24, with its two identity checks on every reading).
  - **(a) Every odd-trace state to length 6 at tick 3.** Every p; q ∈ {0, p₁, p₂, p₃}; every 24th root of unity κ where
    H¹(A ⊗ B_p*) ≠ 0; every basis class and one generic combination. Of 360 readings, 300 are +1: every reading on ten
    threads. The 60 readings of ±LLRLRR (traces ±15) are all 0: there ℓ_p lifts to every extension.
  - **(b) Two further primes**, 50 329 and 90 073, on ±LR and ±LLRLRR: the same.
  - **(c) Every odd-trace state of length 8** (twenty; odd trace forces even length), under the reduced rule q = 0, κ a
    fourth root of unity. The rule cuts nothing: at tick 3, ρ_Q ⊗ χ_q is conjugate to ρ_Q by a unit quaternion (the
    stable letter acts by a scalar), and (a) confirms it; by Theorem H the eigenvalues at tick 3 are fourth roots of
    unity. Of 150 readings, 135 are +1, on eighteen states. The 15 readings of ±LLLLLRRR (traces ±17) are all 0.
  - **At every resolving tick.** By Shapiro a later tick 3k reduces to tick 3 at other κ, all read. So the silent
    threads are silent at every tick 3k.
- **The mod-16 law (COMPUTED, 32 of 32; the proof OPEN).**
  - A thread's weave extensions are silent exactly when its trace satisfies t ≡ ±1 (mod 16).
  - By Cayley–Hamilton φ³ = (t² − 1)φ − tI, and φ is not scalar mod 2 when t is odd. So t ≡ ±1 (mod 16) exactly when
    **φ³ ≡ ±I (mod 16)**: the resolving tick's monodromy is ±1 on the fibre's homology mod 16.
  - Every odd-trace thread has φ³ ≡ ±I mod 4. The firing threads stop there or at mod 8 (t ≡ ±7 mod 16). The silent
    ones reach mod 16.
- **The prediction, and its test** (`W15_PREDICTION.md`, committed at `7c79b8c7` before either run).
  - **Part 1 held.** The rest of length 8 was predicted to fire (traces ±25, ±27, ±29, ±37, ±39), and every reading did.
  - **Part 2 failed.** F-CI at tick 3 carries on ±LLLLLRRR: 3 064 generation-shaped backgrounds on +LLLLLRRR (16
    deck-fixed, 3 048 in deck orbits of three) and 336 on −LLLLLRRR (`the_prediction_test.json`). The control
    ±LLLLLLLR carries 480 and 336.
  - So the shared silence of the two instruments on ±LLRLRR was a coincidence, not a common cause. The mod-16 law is the
    weave's extensions' alone, as the prediction said it would be in that case.
- **What it shows.**
  - **A module and a count on the weave (main's first condition).** On every odd-trace thread with φ³ ≢ ±I (mod 16),
    each parity's line, extended by the weave's spin doublet along any weave class, has index exactly one: three alike
    units cycled by the deck. That is the skeleton of main's orbifold standard (three sectors of index one,
    distinguished by characters), on every such thread, not only on +LR's forced cover.
  - **Three or nothing.** No thread carries one or two: Theorem G, read on the weave's own extensions.
  - **A weave law of the weave's content, with a criterion.** It takes every odd-trace thread, its module is the joint
    action's, and its claim is about all threads at once: three units where φ³ ≢ ±I (mod 16), none where φ³ ≡ ±I. It
    is a census law to length 8, not a theorem. Content is not on every thread: the silent class is a quarter of the
    odd residues mod 16.

**The weave's five (COMPUTED by rule; read with F-HE's pair, no dictionary claimed).**
- **The module.** The spin doublet A = ρ_Q ⊗ κ (rank two) extended by the three parity lines (rank three) along weave
  classes: W = [[A, (c₁B₁, c₂B₂, c₃B₃)], [0, B₁ ⊕ B₂ ⊕ B₃]]. It has the Standard Model's 5 = 2 + 3 shape, built only
  from the weave.
- **The rule.** Every odd-trace state to length 6 at tick 3; every κ at which all three H¹(A ⊗ B_p*) are non-zero; every
  combination of basis classes and one generic; W and its dual, the other order.
- **The result.**
  - On the ten firing threads, (I(W), I(Λ²W)) = (1, 3), or (2, 3) for some classes on the vector-like twins. The dual
    reads (−1, −3) or (−2, −3).
  - On ±LLRLRR it reads (0, 0).
  - det W is trivial on the vector-like twins and −1 on the chiral ones.
- **Read in F-HE's dictionary** (N(10′) = −I(W), N(5̄′) = −I(Λ²W)), the dual is one 10 and three 5̄: one 5̄ per parity,
  and one 10 for the shared doublet. That is anomalous (n_5̄ ≠ n_10).
- **So the shape identity is not built into the class index.** The weave's own 2 + 3 reads the anomalous shape on every
  firing thread. Main's second condition is not met by any count on record applied to the weave's modules.

**What W15 settles, against main's three conditions.**
- **(1) A module and a count on the weave: met.** The weave's extension has index one per parity, three or nothing,
  with the mod-16 law deciding which.
- **(3) A chirality handle other than the index: met.** Theorem H: the determinant of T, mirror-odd, on every
  odd-trace thread.
- **(2) The shape identity built in: not met** by the class index (the weave's five).
- **A frame that would meet (2), stated as a READING, not claimed.**
  - The weave hands over E₆ on every odd-trace thread (McKay of the common 2T; F-MC, link b), and F-MC's matter is the
    27.
  - Suppose each index-one weave unit carries one complete 27, with E₆ unbroken by the weave's vacuum. Then the shape
    identity holds by group theory (27 ⊃ 10 + 5̄, net).
  - A thread with φ³ ≢ ±I (mod 16) then carries three generations of 27, one per parity, cycled by the deck, with the
    hand of Theorem H.
  - What it takes: that reading (the dictionary, GENESIS FK11), the deck kept (FK7), and the mod-16 criterion.
  - The weave's five is evidence against F-HE's dictionary on the weave's modules, not evidence for this reading.

## W16. Main's B1601 and B1604 verified, and B1602's third carrier withdrawn by main (`the_common_point_mod_3.py`)

**B1604 (main's T-NO-INDEX-IN-THREE): VERIFIED.**
- **The theorem.** For a flat module E on a cusped 3-manifold, or on a finite cover of one, χ(N; E) = 0 and
  h²(E) = n(E*) + Σt₀(E*) − h⁰(E*). So the class index I(E) = n(E) − n(E*) is the interior rank in degree one minus
  that in degree two, and it is not an Euler characteristic.
- **The proof, re-derived.**
  - The presentation complex of ⟨a, b, t ∣ t x t⁻¹ = φ(x)⟩ has one vertex, three edges and two faces, and it is a
    model of the thread. So χ(M; E) = rank(E)·(1 − 3 + 2) = 0.
  - Poincaré–Lefschetz duality and the exact sequence of the pair give h².
- **Its control is already in this seat's engine.**
  - Main's E1 reads a0(E) − a1(E) + n(E*) + t0(E*) − a0(E*) = 0. sm:B1374's engine asserts the B1297 identity at
    every index it computes, and the two differ by an identity (checked symbolically).
  - So every reading of W13–W18 passed E1; a failure would have stopped the run.
- **What it does here.** W15's, W17's and W18's pairs are laws of the class index, not counts. GENESIS FK11 is
  unearnable on threads and their covers.

**B1602's third carrier.**
- Main withdrew it (S84). It was an artifact of 40-digit Fox matrices on a 12-fold cover whose relators run to 720–902
  letters, and E1 caught it. There is nothing to verify.
- This seat's forced-cover census at 160 digits (W6, to length 6) never had a carrier beyond ±LR.

**B1601 (main's T-COMMON-POINT-MOD-3): VERIFIED, 37 of 37.**
- **The law.** For every primitive word in L and R with both letters to length 8 (37 geometries), take the ideal
  (x, y, z) = (tr a, tr b, tr ab) at the geometric point.
  - On odd trace it is one prime of norm 3, and x, y and z each have valuation one there.
  - On even trace it is a power of one prime above 2.
- **The route,** independent of main's code:
  - the geometric point from sm:B1527's family_lib (sm:B1523's route F), polished by Newton on the Fricke
    fixed-point equations with the cusp condition, at 1 200 digits, more where a field needs it;
  - PARI: the minimal polynomial of θ = x + 2y + 3z, either degree by degree (algdep, required to agree at two
    precisions) or as the irreducible factor at θ of one relation of degree 64;
  - x, y and z in θ's power basis (lindep), then an EXACT check in K that they are a fixed point of the state's
    Fricke map on the cusp surface;
  - the ideal read at the primes q of g = gcd(N(x), N(y), N(z)), with the order made maximal at each q; the exponent
    at each prime above q is the least of the three valuations.
- **The result.** Every row agrees with main's census: the trace, the field's degree, the norm, and each prime's
  residue degree and exponent.
  - **Odd trace, 16 of 16:** norm 3, residue degree one, exponent one, valuations (1, 1, 1).
  - **Even trace, 21 of 21:** one prime above 2. The norm is 4 on eight words, 8 on seven, 64 on five (LLLLLLRR's of
    residue degree three) and 1 024 on LLLLRRRR.
  - Every field and every coordinate was checked exactly in K, and x, y and z are integral on every word.
  - The fields run from degree 2 to degree 38.
  - The precision used: 1 200 digits on 27 fields (degree by degree); 2 400 on 4 and 4 800 on 6 (the factored
    relation).
- **Three instrument notes.**
  - PARI's full maximal order factors the polynomial discriminant. On LLLLRLRR's degree-24 field it was still
    factoring after 25 minutes; main's run stalled the same way. The norm argument makes it unnecessary: an element
    with a unit norm at ℓ is a unit in any order at ℓ, so the ideal lives at the primes of g.
  - PARI's idealfactor on an order maximal only at g's primes does not serve either. x, y and z carry index
    denominators in θ's basis, and PARI then factors at primes where the order is not maximal. The run reads each
    prime of g by its valuations alone.
  - On LLRLRLRR (trace 39, degree 38) y is exactly the complex conjugate of x. θ's polynomial is found, but x, y and z
    then need coordinates of more than a hundred digits in θ's power basis. The coordinate x alone generates the
    field with a small polynomial, and with θ = x the row is main's.
- **For this dossier:** link a of the synthesis's chain is VERIFIED. Every odd-trace thread to length 8 reduces, at a
  prime of norm three, to the common point. So W3's forced cover is each thread's own congruence cover there.

## W17. The weave's five on the thread itself: F-HE's generation shape on the vector-like twin of every carrier word (`the_weaves_five_tick1.py`)

**The idea.** By Shapiro, W15's five at tick 3 is the thread-level module summed over the three deck twists. At
tick 1, on the thread itself, the weave's two modules are irreducible:
- the spin doublet D = ρ_Q (the 2 of 2T);
- the parity triplet P = Ad(ρ_Q) (W4's triplet, the 3 of 2T).

**The module.**
- F-HE reads a rank-five module as the 5 of SU(5)′, so W must have trivial determinant. Twisting D by ν^a and P by
  ν^b for a character ν of the base needs 2a + 3b = 0. The choice a = 3, b = −2 is the hypercharge ratio of the 5.
- An extension class c ∈ H¹(M; Hom(Pν⁻², Dν³)) glues them:
  **W(ν, c) = [[Dν³, c·Pν⁻²], [0, Pν⁻²]].**
- It is the weave's: the common point's two modules, the determinant condition, and a class of the joint data.

**The rule** (named before the run): every odd-trace state of GENESIS to length 8 (32 states), tick 1; both lifts of t;
every 24th root of unity ν at which the gluing group is non-zero; every basis class and one generic combination; W and
its dual. sm:B1374's engine over GF(p) reads F-HE's pair (I(W), I(Λ²W)): 480 readings.

**The result (COMPUTED, 32 of 32, every reading).**

| class of state | how many | (I(W), I(Λ²W)) | dual | read in F-HE's dictionary |
|---|---|---|---|---|
| the vector-like twin of a word with φ³ ≢ ±I (mod 16) | 14 | (1, 1) | (−1, −1) | **one generation: N(10′) = N(5̄′) = 1** |
| the chiral twin of such a word | 14 | (0, 1) | (0, −1) | a lone 5̄ |
| a word with φ³ ≡ ±I (mod 16) (±LLRLRR, ±LLLLLRRR) | 4 | (0, 0) | (0, 0) | nothing |

- **The two named laws decide the readings.** The twin is Theorem H's, n_L − n_R + 2·[sign −] ≡ 0 or 2 (mod 4). The
  silence is W15's mod-16 law. Every state's reading matches the prediction from the two rules.
- +LR (m004) reads one generation; −LR (m003), its sign twin, reads a lone 5̄.
- **The vacua.** On the vector-like twins ν runs over the sixth roots of unity, on the chiral ones over the odd
  twelfth roots.
  - ν and νω give isomorphic modules, since P ⊗ ω ≅ P for the deck character ω.
  - Changing ν's sign is the other lift of t.
  - So up to isomorphism a thread has one such five, and every vacuum and class reads the same.

**What it shows.**
- **Main's second condition, on the weave's own module.**
  - The natural weave five, with the hypercharge ratio forced by the determinant, has n_5̄ = n_10 on every reading of
    every vector-like carrier thread.
  - The shape is not found by search: the module is canonical, and every class and vacuum reads it.
  - It is "built in" in the sense of a law on a stated class, not an identity like ch₃(Λ²V) = (n − 4)ch₃(V). The
    chiral twins read (0, 1), which is not the shape.
- **With W15, main's three conditions all have answers on the weave's modules:**
  - the module and count (W15, W17);
  - the shape on the vector-like carriers (W17);
  - the chirality handle (Theorem H), which here also decides which twin carries the generation.
- **The count is one, not three.**
  - At the thread's own level the five carries one generation, and the three parities sit inside it as the triplet
    P: the internal SU(3)′ of SU(5)′.
  - Restricted to the resolving tick (deck kept) it reads W15's (1, 3), one 10 and three 5̄, which is anomalous.
  - So in F-HE's dictionary the parities are the five's triplet, not three generations.
- **Where a three can come from.** The deck-related vacua ν, νω, νω² are three sectors distinguished by the deck
  characters, each of index one: main's orbifold standard.
  - They are isomorphic modules. Reading them as three generations rather than one is GENESIS FK7, the deck kept.
- **Still open.**
  - A proof of the law (a census to length 8).
  - Whether F-HE's dictionary is the physical one (I-26).
  - FK7.
- **Read under main's B1604 (verified in W16).**
  - On a thread, and on any finite cover of one, every twisted Euler characteristic vanishes. So I(W) and I(Λ²W) are
    interior ranks in degrees one and two, and no characteristic class ties them to each other.
  - The (1, 1) law is therefore a law of the class index on the weave's five, not a count of generations.
  - W17 answers main's S83 conditions without earning the dictionary: GENESIS FK11 is unearnable on threads and their
    covers (main's v1.27).

## W18. The five carried by each parity line: a prediction that failed at special classes (`the_parity_generations.py`; `W18_PREDICTION.md`)

**The question.** W17's five reads one generation's pair on the thread itself. At the resolving tick the three parity
lines of W8 separate (Theorem S). Does each line carry one copy of that pair?

**The quantity.**
- On the forced A₄ cover, the pulled-back five's count splits over A₄'s irreducibles R ∈ {1, ω, ω², P}, each with
  weight dim R (Shapiro). The sector's pair is (I(W⊗R), I(Λ²W⊗R)) on the thread.
- The parity lines are A₄'s three characters restricted to the resolving tick: B_p(t³) = 1 on all 32 states. So the
  P-sector's pair is also the pair carried by each parity line, W|M₃ ⊗ B_p.
- The zero parity's part is the five pulled back to the resolving tick, the sum of the sectors 1, ω and ω².

**The prediction** (committed before the run, b5223cbb):
1. every reading's P-sector is (1, 1) on the carriers;
2. (0, 2) on the chiral twins;
3. (0, 0) on the mod-16 words;
4. the singlets as the probe read them;
5. the two routes agree.

**The rule:** W17's 480 readings by route A (tick 1, Shapiro), and route B directly at tick 3 on the twelve states to
length 6, at 72 readings.

**The result (COMPUTED; 32 states).**

| class of state | how many | each parity line (the P-sector) | 1, ω, ω² | the forced cover |
|---|---|---|---|---|
| carriers: the generic class and the first basis class | 14 | (1, 1) | (1, 1), (0, 1), (0, 1) | (4, 6) |
| carriers: the second basis class | 14 | (1, 1) on ten; **(0, 1)** on −LLLR, −LLLRLR, −LLLLLLLR, −LLLLRRLR | as above | (4, 6); (1, 6) on those four |
| chiral twins | 14 | (0, 2) | (0, 1) each | (0, 9) |
| mod-16 words | 4 | (0, 0) | (0, 0) each | (0, 0) |

- **Predictions 2 to 5 held; prediction 1 failed.**
  - On ten carriers, every reading's P-sector is (1, 1).
  - On four carriers, all of sign −, the second basis class of the gluing group reads (0, 1). On those four the
    first basis class and the generic combination read (1, 1).
  - The four are not a trace class: −LLLLRRLR is among them, and −LLLLRLRR, of the same trace −25, is not.
- **The routes.** Route B agrees with route A at every reading they share, and its three parities agree with each
  other at every reading (Theorem G).

**What it shows.**
- **At the generic class** each of the three parity lines carries the five's pair (1, 1), on every carrier. This was
  seen after the run; it is not the prediction.
  - That gives three sectors, distinguished by the weave's own characters, alike, and cycled by the deck. It is the
    shape of main's orbifold standard on the weave's own modules.
- **Not at every class, and not on four threads only** (post hoc, `the_parity_generations_special.py`).
  - The basis comes from row reduction, so it is not random. The whole projective line of the gluing group was
    therefore read on every carrier: lift 0, the first ν with a two-dimensional group, every class over GF(73)
    and GF(97).
  - **On all 14 carriers, at both primes, exactly two classes drop each line's pair to (0, 1); every other class
    reads (1, 1).** The engine's second basis class is one of the two exactly on the four carriers above.
  - So "one generation's pair per parity line" is a law of the five away from two classes, on every carrier.
    What singles out the two is open.
- **The zero parity and the whole cover do not have the shape.** The zero parity's part reads (1, 3). The forced
  cover's total reads (4, 6), and (1, 6) at the special classes.
- **Under main's B1604 (W16)** all of these are class-index pairs on a cover of a thread, not counts.
  - The sectors are selected by characters the weave forces. That is the honest form of the orbifold standard in
    main's FK11: a selection.
  - Whether the three sectors are three generations stays GENESIS FK7 and FK11.

## W19. The weave's own surface: the even-dimensional object that main's GENESIS FK11 asks for (READING; the facts classical)

**Main's condition.** B1604 (W16): no flat count on a thread, or on a cover of one, is an index. A dictionary needs "an
even-dimensional object the weave forces, carrying a non-flat bundle whose index is the count".

**The object.** The weave is the joint action of every allowed move on the shared records. Here are its group and its
space.
- **The group.**
  - The moves act as automorphisms of the fibre's group F₂ = ⟨a, b⟩. Together with the fibre's own group (the inner
    automorphisms) they generate Aut⁺(F₂), the automorphisms that act on H₁ with determinant +1.
  - Every thread's group sits inside it. The map π₁(M_w) = F₂ ⋊_φ ℤ → Aut⁺(F₂), x ↦ (conjugation by x), t ↦ φ̃_w, is
    injective: φ_w has infinite order in Out(F₂), and F₂ has trivial centre.
  - Two threads already generate it: M(LLR)·M(LR)⁻¹ = L.
- **The space.**
  - Aut⁺(F₂) is the pure mapping class group of the torus with two marked points (Birman's exact sequence with
    Dehn–Nielsen–Baer).
  - So the weave's space is the moduli space M₁,₂: the universal punctured elliptic curve over M₁,₁, the moduli of
    the shared fibre. It is a complex surface, of real dimension four.
- **The threads inside it.** Over the closed geodesic of M₁,₁ that a word's monodromy determines (with the lift that
  the sign chooses), the universal punctured curve is the thread's mapping torus. So the surface is every thread at
  once, joined along the shared fibre, and no thread is chosen.

**What it has that the threads lack.**
- Its orbifold Euler characteristic is χ(M₁,₂) = χ(F₂)·χ(SL(2, ℤ)) = (−1)·(−1/12) = 1/12 (Harer–Zagier), not 0.
- Its rational cohomology is ℚ in degree zero. This follows from the Lyndon–Hochschild–Serre sequence over
  SL(2, ℤ) = ℤ/4 ∗_{ℤ/2} ℤ/6, where −I acts by −1 on H¹(F₂; ℚ).
- So the vanishing that B1604 proves on every thread does not hold on the weave.

**Where the three parities sit.**
- The elliptic involution x ↦ −x acts on every fibre. Its fixed points other than the puncture are the three non-zero
  points of order two: W1's three parities.
- The fourth parity, zero, is the puncture, which the fibre omits.
- Over M₁,₁ the three form one connected curve Z ≅ Y₀(2), of degree 3. The moves permute its sheets through
  SL(2, 𝔽₂) ≅ S₃: mod 2, L and R are transpositions and LR is a 3-cycle.
- So W1's three, and its one exception, are the fixed-point structure of the weave's own surface: its orbifold locus,
  with stabiliser ℤ/2.

**Bundles on it.**
- The Hodge bundle λ and the cotangent lines ψ₁ and ψ₂ at the two marked points are non-flat.
- The common point's own bundles stay flat: its modules have finite monodromy (W3, W9).

**The dimension a count needs (elementary; checked by the splitting principle).**
- For an SU(5) bundle V whose lower Chern characters vanish, ch_k(Λ²V) = (5 − 2^(k−1))·ch_k(V).
- So the index of Λ²V is three times that of V on a four-dimensional object, up to the rank's Â-term. The two are
  equal only on a six-dimensional one, which is the Calabi–Yau threefold's identity.
- So on this four-dimensional surface an SU(5) count has the shape one to three. The physical shape needs the E₆
  frame, where one generation is one 27 and the shape is in the representation, or a six-dimensional object.
- **An observation, not built on.** The class-index pairs read so far have the six-dimensional shape (1, 1) on the
  thread itself (W17). At the resolving tick they have the four-dimensional shape (1, 3): W15's five, and W18's
  zero-parity part. Main's B1604 says they are not indices, so this may be a coincidence.

**What is not done.**
- No bundle is named as the matter's, and no index is read.
- Naming one by principle, before any count, is the next step. It is a ruling for the owner and main (GENESIS FK11),
  not a search.

**Seen first.**
- **Sweep:** neither branch carries M₁,₂ or the universal curve as the weave's object (both branches searched,
  2026-10-08). Main's B1604 names the condition.
- **Literature:** Birman (1969); Harer and Zagier (1986), for χ(M₁,ₙ); Culler and Vogtmann (1986), for the virtual
  cohomological dimension of Out(Fₙ), 2n − 3. For Aut⁺(F₂) the value 2 follows from its free kernel F₂ over SL(2, ℤ).

## W20. The weave's count in E₆: three on the weave, zero on every thread (`the_weaves_count_in_e6.py`; `W20_RULE.md`)

**Route 1** (the owner's standing instruction; this seat's recommendation after W19): E₆'s frame on the weave's
even-dimensional object, with everything named by principle before the census.

**The objects** (the rule, committed first, ed43731d):
- **the weave's group** G = Aut⁺(F₂), which every thread's group generates (W19);
- **the weave's own SL(2):** the moves acting on the two records through SL(2, ℤ) in its standard representation H;
- **E₆ and the 27:** E₆ is the common point's, by McKay (F-MC). One generation is one 27. The record's E₆/27 frame
  reads the 27 through E₆'s principal sl₂ (main's B1257 flags that as "a choice nobody derived or varied");
- **the count:** −χ(G; 27) = h¹ − h⁰ − h².

**The principal count (seen by hand before the rule; now computed two ways).**
- Under the principal sl₂, 27 = Sym¹⁶ ⊕ Sym⁸ ⊕ Sym⁰.
- The weave's cohomology with these coefficients has h⁰ = 1, h¹ = 4 and h² = 0.
  - The 4 is h¹(SL(2, ℤ); Sym¹⁶) = 3 (M₁₈ ⊕ S̄₁₈) plus h¹(Sym⁸) = 1 (M₁₀).
  - The fibre adds nothing: H ⊗ Symᵏ is odd for these k, and −I kills it.
- So **−χ(G; 27) = 3**: net three classes of the 27 in odd degree. On every single thread the same count is 0, since
  every flat Euler characteristic of a cusped 3-manifold vanishes (B1604, W16).
- The three is therefore the weave's in the owner's sense: no thread carries it, and the joint action does. It comes
  from the torsion the threads generate together, the square and hexagonal tori and the elliptic involution. On a
  torsion-free subgroup of index n the Euler characteristic is instead the rank times the orbifold value, 27n/12.

**The census (the trial budget: every SL(2) in E₆, 21 orbits; two routes, the amalgam ℤ/4 ∗_{ℤ/2} ℤ/6 and
Eichler–Shimura, agreeing on every orbit; every orbit's dimension equal to E₆'s list).**

| orbits | −χ(G; 27) |
|---|---|
| **the three distinguished ones, E6, E6(a₁), E6(a₃)** (not in any proper Levi) | **+3 each** (27 = 16 + 8 + 0, 12 + 8 + 4, 8 + 6 + 4 + 4 + 0) |
| A4, D4(a₁), D5 | +3 |
| 3A1, A2, A2+2A1, A3+A1, D4, A5, D5(a₁) | −3 |
| A2+A1, 2A2+A1, A4+A1 | −1 |
| 2A2 | +7 |
| 2A1, A3, A1, the zero orbit | −7, −13, −15, −27 |

- **Controls.**
  - The 78 reads 16 on all three distinguished orbits, not 3.
  - The 27̄ reads as the 27 under every SL(2).
  - The SU(5) frame through its principal SL(2) reads (1, 2) for (5, 10): not the shape.
- **So the record's own choice gives three, and so does every SL(2) that fills E₆.** But ±3 is common: it appears on
  13 of the 21 orbits.

**A third route, and the count as an orbifold index** (`the_weaves_count_orbifold.py`, after the census).
- Brown's formula for a group with a torsion-free subgroup of finite index uses only the elements of finite order. The
  count is a sum over the elliptic elements of SL(2, ℤ), each weighted by the orbifold Euler characteristic of its
  centralizer and by its trace on the module. The fibre's term is taken with the records' traces.
- It agrees with both routes on all 21 orbits.
- On every distinguished orbit the 27 has trace 3 at S (the square torus), 0 at U and U² (the hexagonal torus), and 27
  at −I. So −χ = 27/6 − 3/2 = 3: a bulk term less the square torus's twisted sector. That is the shape of an orbifold
  index.

**The count is the index of a non-flat bundle** (proved here, in a few lines).
- The records' variation of Hodge structure Symᵏ H has, on the compactified moduli X̄ of the shared fibre, the Higgs
  bundle E = λᵏ ⊕ λ^(k−2) ⊕ … ⊕ λ^(−k), with λ the records' Hodge line.
- Its Higgs field λ^(k−2p) → λ^(k−2p−2) ⊗ Ω¹(log ∞) is Kodaira–Spencer's isomorphism Ω¹(log ∞) ≅ λ² on every piece
  but the two ends. So the Higgs complex is quasi-isomorphic to λ^(−k) ⊕ λ^(k+2)[−1], and
  χ(SL(2, ℤ); Symᵏ) = χ(X̄, λ^(−k)) − χ(X̄, λ^(k+2)).
- These are Riemann–Roch indices of powers of a non-flat line bundle: dim M_(k+2) + dim S_(k+2) = h¹, as
  Eichler–Shimura has it.
- So −χ(G; 27) = 3 is the index of a non-flat bundle on an even-dimensional object that the weave forces. That is the
  form main's GENESIS FK11 condition names.

**The hand: an erratum (the same morning; it withdraws the paragraph that stood here in e51785a1).** That paragraph
called the net count chiral. It is not, and cannot be.
- Complex conjugation is an antilinear isomorphism H^q(G; R) → H^q(G; R̄). So no count of group cohomology tells a
  representation from its conjugate. A chiral index must change sign under conjugation.
- In the established heterotic dictionary, generations come from H¹ of the bundle in the 27 and anti-generations from
  H¹ in the 27̄. A self-conjugate structure then gives vector-like matter: here four 27 and four 27̄ in degree one, net
  zero. It is the same reason an SU(2) bundle gives non-chiral matter.
- **So W20's three is the weave's Euler characteristic in the 27, not a count of chiral generations.** The weave's
  SL(2) is self-dual, and its flat cohomology, or the Hodge structure on it, cannot carry a hand.
- What could carry one is a structure that is not self-conjugate, read by an index that changes sign under
  conjugation. The weave has such a structure: Theorem H's complex triplet T (W10, W15), on which the moves act
  through a group of order 96 with T ≇ T̄. A holomorphic index on the weave's orbifold can tell T from T̄, because the
  local monodromies at the orbifold points enter conjugated. That is the next step, not a result.


**Status.**
- **COMPUTED, and exact:**
  - χ(Aut⁺(F₂); 27) = −3 through the principal sl₂, and through each distinguished one;
  - the census.
- **The reading "three generations" (READING; GENESIS FK11 on the weave)** rests on four named links:
  - E₆ from the weave (F-MC, a theorem with hypotheses);
  - one 27 per generation (a dictionary);
  - the principal sl₂ (canonical, and the record's own; now varied: every distinguished one agrees);
  - the count by the weave's Euler characteristic (the analogue of an index; by Eichler–Shimura it is a sum of
    Riemann–Roch indices of powers of the records' Hodge line λ, so a non-flat bundle carries it).
- **What is not fixed:**
  - the hand: the 27 and the 27̄ read alike, and the count is not chiral (see the erratum above; GENESIS FK4, GAP3);
  - whether the weave's group with its torsion, rather than a torsion-free cover, is the physical object (GENESIS
    FK7's question in another form);
  - the swap's action (GENESIS GM5c), which may exchange the 27 and the 27̄.
- **Not the parities' three.** This three comes from modular forms of weights 18 and 10, not from the three parities
  of W1. Whether the two threes are one is open. (W21 gives a chiral three that is the parities' own.)

## W21. The hand by Hodge type: the weave's chiral three is holomorphic (`the_holomorphic_triplet.py`; `W21_RULE.md`)

**Why.** W20's count is not chiral (its erratum), so a chiral count needs a holomorphic quantity. The weave has a
complex structure of its own: the shared fibre's. The rule was committed before the code ran (72fbab31).

**The objects** (from the rule):
- the fibre F₂ with puncture loop [a, b], so a·b = +1 and τ = ∫_b dz / ∫_a dz lies in the upper half-plane;
- the common point ρ_Q;
- the three parities. On the fibre they are its three even spin structures, the non-trivial square roots of K_E = O.
  The zero parity is the odd one;
- V = H¹(F₂; ⊕_p χ_p ⊗ ρ_Q), as in W10;
- T and T̄, named by Z = S², the braid lift of −I: T is where Z = −i. W10's T is this T.

**The theorem (proved in the rule).**
- **The count.** For every complex structure τ, V splits by Hodge type, one line of each type per parity.
  - By Riemann–Roch: the parabolic extension has degree −1, because the puncture's holonomy is −1.
  - By Chevalley–Weil on the genus-3 cover w⁴ = cubic(x): its odd holomorphic forms are dx/w³ and x dx/w³.
  - So dim V^(1,0) = 3. Read as spinors, with the extension that has square-root poles at the puncture, V^(1,0) is the
    kernel of the fibre's Dirac operator for the three even spin structures, with the common point as gauge field:
    an index of one each. (The extension is a choice for spinors; see the qualification below.)
- **The invariance.** The moves act on V through a finite group (order 96). So the period map is constant, and V^(1,0)
  is the same subspace for every τ and invariant under every move. So it is T or T̄.
- **What decides.** The Hodge–Riemann form Q = i ∫ u ∧ v̄ is topological, and it is positive exactly on V^(1,0). Its
  sign on T decides.

**The read-out (one run; every control first).**
- **The controls all hold:**
  - the Riemann bilinear calibration;
  - Q hermitian and independent of the cocycles chosen;
  - three chains of the puncture loop agree;
  - Q invariant under L, R and −I with every lift, and the swap reverses it;
  - signature (3, 3) on V and (1, 1) on the spin doublet M;
  - T ⊥ T̄, and the group's order is 96.
- **Q is positive definite on T and negative definite on T̄.** So T is holomorphic and T̄ antiholomorphic, as the
  theorem requires, with the sign now read. T meets each parity's block in one line.
- **Z acts on the holomorphic triplet as −i.**
- **The spin doublet M.**
  - Its holomorphic line μ also has Z = −i.
  - With the lifts (0, 1), μ(L) is 7/8 of a turn, so μ = χ_η²¹ = χ_η⁻³. With the lifts (1, 0) it is 3/8 of a turn,
    so μ = χ_η⁹.
  - The two differ by χ_η¹², the lifts' overall sign. And μ(R) = μ(L)⁻¹.
- **T = μ ⊗ P.**
  - P has order 24, with P(L)⁴ = P(S)² = (P(S)P(L))³ = 1, and traces −1, 1, 0 at S, L, SL.
  - So P is S₄'s 3′, the cube's rotations: the common point's own triplet of directions (main's B1601 lemma, quarter
    turns about the parity axes).
  - W10's "S₄'s triplet times a character of ℤ/8" is the same statement, since 3 ⊗ sign = 3′ and χ_η¹² is the sign.

**A second route, after the read-out: the actual periods** (`the_holomorphic_triplet_periods.py`). This route uses
no sign convention of Q. It writes down the holomorphic forms and integrates them.
- **The form.** For the common point, F = (f(z), f(z + τ)) dz with f(z) = θ₃(z | 2τ) / √θ₁(z | τ).
  - Continued along the segments that represent a and b, it has exactly ρ_Q's monodromy. Of the four theta
    numerators only θ₃(z | 2τ) does this, at every τ tried.
  - It is holomorphic, with square-integrable square-root poles at the puncture. So it spans the holomorphic line.
  - In each parity's block the form is C_p F, with C_p = j, i, ij in Q₈.
- **At three values of τ** (0.23 + 1.07i, −0.41 + 0.83i, 0.12 + 2.31i, with one marking), the periods of the three
  holomorphic forms span T and meet T̄ only in 0. The subspace is the same at all three: the period map is constant,
  as the theorem says.
- **The twisted Riemann bilinear relation.** At the first τ, Q on the holomorphic form equals 2 ∫_E |F|², computed
  directly in polar coordinates about the puncture, to a relative error of 8 × 10⁻¹⁵. So the cup-product formula,
  sign included, is the Hodge–Riemann form.

**A second proof, found while writing up, and what it says the hand is.**
- On the genus-3 cover w⁴ = 4x³ − g₂x − g₃ of every fibre, J: w ↦ iw is a spin lift of the elliptic involution,
  that is, of the sign move −I.
  - By pullback it acts on both odd holomorphic forms by i, for every τ.
  - So the holomorphic part is one eigenspace of J. It is constant, and invariant under every move, because −I is
    central.
  - The read-out fixes which lift the braid's Z is: the one that acts on holomorphic forms by −i.
- **So the hand is the eigenvalue of the sign move's spin lift.** The rotation by π about the puncture acts on spinors
  by ±i, and its sign is the chirality. That is what chirality is on a surface.
- **Where the weave enters.**
  - J is a scalar on T because T is irreducible under the weave's group (Schur).
  - On one thread alone the holomorphic part is three lines, which the thread's cyclic group moves separately: not
    one triplet.
  - So "three alike and chiral" is the weave's. The Hodge type of each zero mode is the fibre's.

**What it shows.**
- **Three holomorphic zero modes on the weave's fibre, one per parity, spanning one triplet T, with T ≇ T̄.** The
  antiholomorphic ones span T̄. The count is h^(1,0) of the L² twisted cohomology: three.
- **What it settles from W20's open items:**
  - **the same three as the parities:** yes, one holomorphic mode per parity;
  - **the hand under the weave's own group,** relative to the records' orientation: the holomorphic modes are T. The
    swap reverses the orientation and exchanges T and T̄. So W10's "the swap must stay outside the moves" says that
    the moves keep the orientation.
- **No choice enters this statement.**
  - For twisted 1-forms the L² condition is conformally invariant, and the classes are interior (the puncture's
    holonomy is −1). So the Hodge decomposition is canonical, with no end condition.
  - The bundle is unitary, so no source is needed (GENESIS GAP3 does not arise).

**A qualification (the same afternoon).** It withdraws three phrases of the paragraph that stood here in 0a1b13bb:
"a chiral three", the count read as "the fibre's Dirac index", and "the form of main's FK11 earning condition ...
chiral", with "GENESIS GAP2 does not arise". The chirality shown is under the weave's group, not under a gauge group.
- **Why gauge chirality is not shown.**
  - The common point is self-conjugate: ρ_Q is quaternionic and the χ_p are real, so 𝕎̄ ≅ 𝕎 as local systems on
    the fibre.
  - In any dictionary where matter in a gauge representation r comes with 𝕎 and matter in r̄ with 𝕎̄, the canonical
    count gives three holomorphic modes to each. That is vector-like in r.
  - Each set transforms as T under the weave's group, and T ⊗ T has no invariant. So the weave's group forbids the
    pairs' mass terms while it is unbroken, but the modulus breaks it.
- **Where an unequal count would come from.**
  - Read as spinors, the zero modes depend on the extension at the puncture. The extension with square-root poles
    gives index +1 per block, and its dual gives −1.
  - Choosing them differently for r and r̄ is an end condition (GENESIS GAP2). For spinors, then, GAP2 does arise.
- **So W21 gives the flavor structure of three generations, not their chirality as the Standard Model has it.**
  - That structure is three alike, one per parity, all holomorphic, in a triplet of the weave's group that is not
    self-conjugate. It is the matter assignment of modular S₄ flavor models.
  - Gauge chirality needs a bundle that is not self-conjugate, read by an index that changes sign under conjugation.
    The flat bundle T on the weave's moduli is one such bundle, through its orbifold corrections. A six-dimensional
    object would be another (GENESIS FK11).
- **Superseded in part by W22 (later the same day).** The last two bullets were too strong. The end condition is not
  free: the weave fixes it up to the hand, and then the index is ±3. A vector-like spectrum needs a mirror field in
  the content, not a choice at the puncture (GENESIS GAP2). See W22.
- **The literature (read in abstract only).**
  - Modular S₄ ≅ Γ₄ flavor models put the three lepton doublets in an S₄ triplet, 3 or 3′ (Penedo–Petcov, Nucl. Phys.
    B 939 (2019) 292, arXiv:1806.11040; Novichkov–Penedo–Petcov–Titov, JHEP 04 (2019) 005, arXiv:1811.04933). There
    the lowest-weight level-4 forms are a doublet and a 3′. Here the weave gives the triplet itself: 3′ times a
    metaplectic character.
  - On magnetized tori the chiral zero modes are as many as the flux, and they transform under the double cover of
    SL(2, ℤ) with weight 1/2 (Kikuchi, Kobayashi et al., arXiv:2005.12642). Three generations there need three units
    of flux. Here the cusp's −1 on each of the three even spin structures gives one zero mode each.
  - In the ℤ₂ × ℤ₂ orbifold (Faraggi; the synthesis after W20), three twisted sectors give one generation each. Here
    they are the three non-trivial parities.

**What it does not show (the links that stay readings).**
- **Gauge chirality** (the qualification above): the common point is self-conjugate, so matter in r and r̄ comes in
  equal numbers unless an end condition at the puncture is chosen (GENESIS GAP2).
- **The dictionary:** that holomorphic zero modes on the internal fibre are the left-handed matter. This is the
  standard compactification reading (GENESIS FK11, I-26).
- **The gauge content of each generation:** one 27 of E₆, by F-MC and the dictionary.
- **The zero parity.** The odd spin structure adds one more holomorphic zero mode, μ, a singlet of the weave's group.
  With it the holomorphic zero modes are 3 + 1. Its role is not read; in the orbifold reading it is the untwisted
  sector.
- **The absolute hand.** It is the records' orientation: the puncture loop is [a, b], not [b, a]. The mirror
  exchanges the hands.

**Status.** PROVED (the theorem, by two proofs) and COMPUTED (the sign, with every control, and again from the actual
periods at three τ): a WEAVE result for the flavor structure. Gauge chirality is not shown. The reading "three
generations" rests on the dictionary and on a source of gauge chirality.

## W22. The end condition the weave fixes: the parities' three is chiral, up to the hand (`the_puncture_condition.py`)

**Why.** W21's qualification said that an unequal count of r and r̄ needs an end condition at the puncture (GENESIS
GAP2). This asks whether the weave leaves that condition free.

**The setup (proved here).**
- **The local solutions.** The fibre's Dirac operator twisted by 𝕎 needs a condition at the puncture, where the
  holonomy is −1. Because −1 is central, each parity block has a two-dimensional space ℂ² of local solutions.
- **The conditions.** A self-adjoint condition that keeps the 2d chirality is a subspace Λ₊ ⊂ ℂ²: the directions
  allowed a |z|^(−1/2) singularity in chirality +, the rest allowed it in chirality −.
- **The index.** The block's index is dim Λ₊ − 1, that is −1, 0 or +1 (Riemann–Roch: the degree of the extension).
  - Λ₊ = ℂ² is the extension whose holomorphic sections are W21's forms.
  - Λ₊ = 0 is its mirror.
  - A line gives index 0: a vector-like block.

**What the weave fixes (COMPUTED).**
- **Irreducible at the puncture.** The lifts of L and R generate 2O, of order 48, and act on ℂ² irreducibly. So do the
  lifts of the moves that fix any one parity: a group of order 16 in each block.
- **So the only conditions every move keeps are Λ₊ = 0 or Λ₊ = ℂ² in every block.** The index is −3 or +3, never 0.
- **One thread alone does leave a line.** Of the 50 threads to length 6, 46 have lifts with two eigenlines and the
  other 4 have scalar lifts. So on one thread a vector-like condition exists. The chirality is the weave's.
- **The spin structure is fixed too.** The odd spin structure is the only one every move fixes. With it, the three
  blocks see the three even ones.

**What it shows.**
- **The parities' three is chiral, by the weave's own symmetry.**
  - With a condition the moves allow, the fibre's Dirac operator on 𝕎 has index ±3: three zero modes of one
    chirality, one per parity.
  - With Λ₊ = ℂ² they are W21's holomorphic triplet T. The other choice is its mirror.
- **GENESIS GAP2 is closed for this operator, up to the hand.** The end condition is not chosen: the weave fixes it
  except for its sign, which is the records' orientation.
- **The qualification to W21 was too strong.** It applied the same L² rule to 𝕎 and to 𝕎̄ as two independent
  sectors. For one field and its CPT conjugate the conditions are conjugate. The index is then ±3. A vector-like
  spectrum needs a mirror field in the content, not a choice at the puncture.
- **In four dimensions:** a six-dimensional chiral fermion in a gauge representation r that carries 𝕎 gives exactly
  three chiral fermions in r, one per parity, in the weave's triplet.

**What it does not show.**
- **Which fields carry 𝕎.** That is the dictionary (GENESIS FK11).
- **Complete generations in the record's E₈ frames.** On the two-dimensional fibre:
  - F-HE with the weave's five W = D ⊕ P reads N(5̄) = 3, from D ⊗ P, which is 𝕎. But it reads N(10) = 1, from D.
    That is the two-dimensional shape, one to three (W19's dimension rule), and it is anomalous on its own.
  - The E₆ frame, with 27 ⊗ (2 ⊕ 1), gives one 27.
  - Three complete generations need every matter field to carry 𝕎: a six-dimensional frame, which is a dictionary.
- **The sign of the hand.** That is the orientation.

**Status.** PROVED (the classification of the conditions; the index by Riemann–Roch) and COMPUTED (the
irreducibility, the threads' eigenlines, the spin structure): a WEAVE result.

**Qualified by W24's audit cell D0 (2026-10-08, the rule committed before the run).**
- **What was missed.** W22 read the condition block by block. But each parity block is the same doublet: χ_p ⊗ ρ_Q ≅
  ρ_Q, by conjugation with a quaternion unit (W24, D1). So a condition may mix the blocks. It is any subspace of the six
  local solutions.
- **What the moves alone keep (COMPUTED).** Under the moves' lifts the six local solutions split as 2 ⊕ 4 (commutant 2).
  So four conditions are kept: 0, the 2, the 4 and all six. Their indices are −3, −1, +1 and +3.
- **What stands: the index is never 0, and it is odd.**
  - −1 is among the lifts and acts as −1 on the local solutions. So every condition the moves keep is a sum of
    spinor representations of 2O, which have dimension 2 or 4.
  - The index, dim Λ₊ − 3, is therefore odd. Chirality is forced. That is a weave result.
- **What needs one more condition: the magnitude three.**
  - It holds when the end condition keeps the parity grading, the block-diagonal signs χ_p(x). Equivalently here, it
    holds when the condition keeps the flavor symmetry U(3) of 𝕎 ≅ ρ_Q ⊗ ℂ³, which commutes with the Dirac operator.
  - With the grading added the commutant is 1 (computed). Only 0 and all six remain: ±3.
- **So the sentence "the index is −3 or +3, never 0" becomes:** never 0, always odd, and ±3 when the condition keeps the
  parity blocks apart (or the operator's flavor symmetry). GENESIS GAP2 is closed for this operator, up to the hand, under that
  condition. With the moves alone it is closed up to four choices, none of them vector-like.

**Added by W28 (2026-10-08, the rule committed first).**
- **What the two middle conditions are.** The six local solutions are a vector-spinor, spin ½ ⊗ spin 1 = spin ½ ⊕
  spin 3/2 under 2O. The index −1 condition is the diagonal {(v, v, v)}, and the index +1 condition is its complement.
  Both couple the three parity sectors at the puncture, and both break the flavor group U(3) to a phase.
- **Three natural requirements each give ±3:** the end condition keeps the flavor group, or the parity grading (part
  of it), or it is local (the puncture's own holonomy is −1, so its symmetry is all of U(6)).
- **The joint action.** The moves alone allow −3, −1, +1, +3. The flavor group alone allows −3, 0, +3. Together they
  allow only ±3.

## W23. The record's E₈ frames on the weave's fibre give at most two complete generations (`the_e8_frames_on_the_fibre.py`)

**Why.** W22 left one link open: which matter fields carry the parity-twisted spin bundle. The record's standard
dictionaries are its E₈ frames. This reads them on the weave's fibre with W22's end condition.

**The rule** (in the script's header, a census with none chosen):
- **The frames.** E₈ ⊃ G × SU(n), with matter E₆'s 27 ⊗ V (n = 3), SO(10)'s 16 ⊗ V (n = 4), and SU(5)'s 10 ⊗ W
  and 5̄ ⊗ Λ²W (n = 5; F-HE).
- **The bundles.** Every bundle of rank n with trivial determinant, built from the common point's blocks: the four
  characters (the zero parity and the three parities) and the four spin doublets χ ⊗ ρ_Q.
- **The index (W22).** Each spin-doublet block counts +1; each character block counts 0.

**The census (COMPUTED).**

| frame | chiral matter, over every bundle |
|---|---|
| E₆ (27) | 0 or 1 |
| SO(10) (16) | 0, 1 or 2 |
| SU(5) ((10, 5̄)) | (0, 0), (1, 3) or (2, 2) |

- **So the most complete chiral generations any of these frames gives on the fibre is two.** Three is impossible.
- **The reason.** Each spin doublet has rank two, so an SU(n) bundle holds at most n/2 of them. The weave's three
  needs rank six.
- **The weave's own five** (D ⊕ P, W17) reads (1, 3). The three 5̄ are the parities' T; the one 10 is the zero
  parity's spin line μ.
  - Its bulk modes are anomalous by −2, so the puncture must carry localized matter with anomaly +2.
  - Two localized 10s would complete three generations, but the anomaly alone does not fix that content.

**What it shows.**
- **The standard dictionary does not finish the derivation on the fibre.** With the weave's forced structures, the
  record's E₈ frames give one 27, or two 16s, or SU(5)'s (1, 3) or (2, 2). They never give three complete generations.
- **Three complete generations need one of three things:**
  - matter that carries the six-dimensional parity-twisted spin bundle, which these SU(n) cannot hold;
  - the puncture's localized content (GENESIS GAP2's place), which the anomaly asks for but does not determine;
  - a six-dimensional object (W19's dimension rule).

**Status.** COMPUTED (a census; the index rule from W22): a WEAVE result, and a negative one for the E₈ frames on the
fibre (GENESIS FK11).

**Added by W24 (D4).** In each frame the bundle's holonomy is only Q₈, so its centraliser in E₈ is larger than the
frame's G. The counts above hold once the end condition has broken that centraliser down to G. That breaking is the
choice of the frame.

## W24. The six-dimensional census: no object the weave forces in dimension six gives three (`the_six_dimensional_census.py`; `W24_RULE.md`)

**Why.**
- **The owner's choice** (2026-10-08): search for a six-dimensional object the weave forces, where the heterotic
  dictionary applies.
- **Main's B1604** asks for an even-dimensional object with a non-flat bundle.
- **W23** showed that the fibre's E₈ frames stop at two complete generations.
- **The web seat's A1** makes six the next dimension in which a bundle can be told from its conjugate.

**The rule** (`W24_RULE.md`, committed d39778dd before the run).
- **Five criteria.**
  - S1, forced.
  - S2, a complex threefold with trivial canonical class.
  - S3, a count exists: compact, or with ends the weave fixes.
  - S4, a forced non-flat bundle whose holonomy has complex representations.
  - S5, net generations = the index.
- **Four candidates,** and every cell with a prior.

**The census (COMPUTED, exact, one run; every cell as predicted).**
- **K1, the fibre's character variety 𝒳 = ℂ³,** with (x, y, z) = (tr a, tr b, tr ab).
  - **The action.** The moves act by polynomial maps that preserve κ = tr [a, b]. The maps were computed two ways, from
    the record's table and from traces of 2 × 2 matrices, and agree.
  - **The volume form.** L and R have Jacobian +1 and P has −1. So the weave acts on a complex threefold whose volume
    form the orientation-preserving moves keep.
  - **The fixed points.** The points every move fixes are (0, 0, 0), the common point (κ = −2), and (2, 2, 2), the
    trivial character (κ = 2).
  - **The tangent space at the common point.** The linear parts there generate the cube's rotations (order 24). Their
    character at (S, L, SL) is (−1, 1, 0), which is W21's P. So **W21's flavor triplet is the tangent space of the
    character variety at the common point**, T₀𝒳 = ⊕_p H¹(F₂; χ_p).
  - **The topology of the level sets.** κ has five Morse points: the common point (κ = −2) and the four central
    characters (±2, ±2, ±2) with xyz = 8 (κ = 2). The level sets have Euler characteristic 6 generically, 5 at κ = −2
    and 2 at κ = 2. Summed over the fibration they give χ(ℂ³) = 1, as they must.
  - **Verdict.** Forced, and of the right kind (S1, S2). But it is contractible and non-compact, the moves act on it
    with no quotient, and its tangent bundle is trivial. It fails S3 and S4.
- **K2, the weave's local model at the common point.**
  - **The parities' fixed loci.** Each parity fixes one axis of 𝒳. On the Markov surface X₋₂ it fixes only the common
    point.
  - **The finite linear symmetries.** Those of 𝒳 that keep κ form T_d ≅ S₄, of order 24: the parities and the
    permutations.
    - The determinant-1 part is A₄. It is generated by the parities and the move L⁻¹RL⁻². That move has the matrix of
      a ↦ b, b ↦ (ab)⁻¹ and acts as the 3-cycle (x, y, z) ↦ (y, z, x).
    - The swap P is the transposition.
  - **The singularities.** The quaternion units i, j, k act as the three parities.
    - X₋₂ divided by the parities is, at the common point, ℂ²/Q₈: the D₄ singularity.
    - Divided by A₄, which acts linearly and on the whole space, it is ℂ²/2T: the E₆ singularity.
    - The moves' linear parts would give 2O, the E₇ singularity, but they act linearly only to first order.
  - **The compact orbifolds E³/G, for any curve E.**
    - χ_orb = 96, 32 and 28 for V₄, A₄ and O. With discrete torsion: −96, −32 and −28.
    - Net generations under the standard embedding: 48, 16 and 14. Never three.
  - **Verdict.** The group is the weave's, but E³ and E are chosen (fails S1), and the count is not three (S5).
  - **The nearest known mechanism.** The three parities are the ℤ₂ × ℤ₂ whose three twisted sectors give one
    generation each in the realistic free-fermionic models (Faraggi, hep-ph/9311312, hep-ph/9501288).
    - On E³ each sector has sixteen fixed tori, and symmetric shifts do not reduce them to one (Donagi–Faraggi,
      hep-th/0403272).
    - On the weave's own 𝒳 each parity fixes exactly one line, but 𝒳 is not compact.
- **K3, main's frame spaces** (L250; stated in the rule, nothing computed).
  - They are complex parallelizable, with K trivial.
  - Heterotic solutions of the Strominger system exist on compact quotients (Fei–Yau, arXiv:1407.7641).
  - But TX is trivial and bundles from Γ are flat, so ch = rank. Every compact quotient has index 0.
  - The threads' quotients have cusps. Only cusp terms could count (main's open cell (a)).
- **K4, the universal families.**
  - Kuga–Sato fails S1, for a free twist.
  - The isomonodromic total space (ℍ × X₋₂)/SL(2, ℤ) fails S2: dτ has weight 2, so K is the modular curve's weight-2
    bundle. It fails S3 too.

**The gauge side (COMPUTED; the reason for the negative).**
- **D1: each parity block is the spin doublet.**
  - χ_p ⊗ ρ_Q = u_p ρ_Q u_p⁻¹, with u_p = j, i and k for the parities (½, 0), (0, ½) and (½, ½).
  - So 𝕎 ≅ ρ_Q ⊗ ℂ³: three copies of one doublet, with the parities labelling the copies.
- **D2: the centraliser.**
  - 𝕎 has rank 6 and determinant 1, so it fits SU(6)′ ⊂ E₈. The commutant of SU(6)′ is SU(3) × SU(2), the Standard
    Model's non-abelian group.
  - But 𝕎's holonomy is only Q₈. The 248's character on Q₈ is 248, 24 and 28 (at 1, at −1 and at the order-four
    elements). It is the same through SU(3) × SU(2) × SU(6)′ and through G₂ × F₄.
  - The centraliser has dimension 55: F₄ × SU(2).
- **D3: the multiplicities.** ρ appears 56 times ((26, 2) + 2(1, 2)), and each parity character 27 times ((26, 1) +
  (1, 1)). The check: 55 + 2·56 + 3·27 = 248.
- **D4 (PROVED from these).**
  - ρ is quaternionic and the 248 is real, so ρ's multiplicity space is pseudoreal under F₄ × SU(2).
  - A chiral reading needs W22's condition on the gauge factor too. The reality of the 248 sends that condition to its
    conjugate, so the condition must be a Lagrangian half of the multiplicity space.
  - The (26, 2) is irreducible. So no condition is at once move-invariant, real and F₄ × SU(2)-invariant.
    - Keeping the moves forces a Lagrangian half that breaks F₄ by a choice.
    - Keeping F₄ forces a line in each doublet: index 0, which the moves do not keep.
  - **That choice is the dictionary** (GENESIS FK11). The frame (E₆, SO(10) or SU(5)) is the choice of the Lagrangian
    half. W23's counts hold in each frame once that choice is made.
- **D0, the W22 audit:** given above, under W22.

**What it shows.**
- **Among the four candidates, no six-dimensional object the weave forces gives three generations by the heterotic
  dictionary.** The forced one (𝒳) has no count. The ones with a count (E³/G) are not forced, and give 48, 16 and 14.
- **Why the fibre's bundle cannot repair it.**
  - The weave's local systems have quaternionic holonomy: Q₈ and its characters.
  - In any E₈ frame their hand is the weave's, never a gauge group's, unless a frame is chosen (D4).
  - What a six-dimensional object must supply is a bundle whose holonomy has complex representations, such as SU(3),
    SU(4) or SU(5): a complex structure on the gauge side. None of the four supplies one by force.
- **What is new and positive.**
  - W21's flavor triplet is the tangent space of the weave's six-dimensional object at the common point (A3). The
    flavor directions of the three are the three ways the common point can be deformed, one per parity.
  - The weave's net chirality on the fibre is odd (D0): one or three, never zero.
  - The common point's node, divided by the weave's finite symmetries, is the D₄ singularity (the parities) or the E₆
    singularity (with the order-three move) (B3).

**Status.** COMPUTED (exact, one run after the rule, every cell as predicted) and PROVED (D4). A WEAVE census, NEGATIVE
for the six-dimensional route on these four candidates. The owner's goal, three generations derived, is not met by it.

## W25. The weave's bundles are self-conjugate: no gauge reading of them is chiral without a choice (`the_self_conjugate_weave.py`; `W25_RULE.md`)

**Why.** The stop hook's objection after W24: three generations are not derived with their gauge content. W24's D4
found the reason in one E₈ frame. This asks whether it is general, and where chirality could enter.

**The lemma** (standard; Frobenius–Schur).
- A gauge group commuting with a bundle's holonomy H has chiral matter only if some multiplicity space Hom_H(σ, 248) is
  a complex representation of it.
- The 248 is real. So if σ is real, its multiplicity space is real; if σ is quaternionic, quaternionic. Only a complex
  σ, with σ̄ ≇ σ, can give a multiplicity space that is not self-conjugate.
- So if every irreducible of H in the 248 is real or quaternionic, every gauge reading is self-conjugate. Chirality
  then needs a choice: a Lagrangian half (W24's D4), or a complex character added by hand.

**The read-out (COMPUTED; the rule committed first, 2068244e; one run; every cell as predicted).**
- **F1, the fibre's holonomy.** Q₈'s indicators are +1 for the trivial character and the three parities, and −1 for
  ρ_Q. Every irreducible is real or quaternionic.
- **F2, the six local solutions.**
  - The group the weave forces there has order 192: the moves' lifts, the fibre's holonomy and the parity grading.
  - It is irreducible on ℂ⁶ and quaternionic (indicator −1).
  - The moves' lifts alone (order 48) give 2 ⊕ 4, both quaternionic (indicator −2 on the six).
- **F3, the cohomology and the tangent space.**
  - On V the moves' group has order 96. Its triplets T and T̄ have indicator 0: complex.
  - The parity triplet, the cube's rotations, has +1: real.
  - So the weave's complex structure lives on the zero modes (the flavor triplet T), not on the local systems.
- **F4, the centralisers in E₈** (by characters, through SU(3) × SU(2) × SU(6)′).
  - **Q₈, 𝕎's holonomy with all three parities:** 55, F₄ × SU(2), as in W24. All its multiplicity spaces are
    self-conjugate.
  - **One parity's element alone,** ⟨𝕎(a)⟩ or ⟨𝕎(b)⟩, of order 4: 82 = 78 + 3 + 1. Its centraliser contains E₆, whose
    27 is complex. So a reading with one parity singled out can be chiral.
  - **The odd-trace extension:** Q₈ with the lift of the order-3 move L⁻¹RL⁻², a group of order 24 (2T, the image of
    every odd-trace thread, B1601).
    - Its centraliser has dimension 25.
    - The complex character ω occurs in the 248 fifteen times, and ω² fifteen times.
    - Read by the branching (ℂ⁶ = 2 ⊕ 2′ ⊕ 2″, and Λ²ℂ⁶ has two invariants), its Lie algebra is
      su(3) ⊕ su(2) ⊕ u(1)² ⊕ 2(3 + 3̄): so(7) ⊕ u(1) ⊕ su(2). The identification is by dimension, rank and
      branching; the dimension is computed.
    - The complex characters ω and ω² are what a chiral reading could use.

**What it shows (F5, PROVED from F1–F4).**
- **On the fibre, every gauge reading of the weave's forced bundles is self-conjugate.**
  - The fibre is the even-dimensional object where the index lives (W21, W22), and its forced holonomy is Q₈.
  - Every irreducible of Q₈ is real or quaternionic.
  - So the three zero modes of W22 sit in self-conjugate gauge representations, under any gauge group commuting with
    the bundle.
- **A gauge group that can be chiral appears in only two places.**
  - **When one parity is singled out.** The centraliser of ⟨e_p⟩ contains E₆. That is a selection, which the weave's
    rule forbids, and GENESIS FK11 names it as the alternative to an index.
  - **When the order-3 move is part of the holonomy.** Its eigenvalues ω and ω² are complex. That happens on an
    odd-trace thread, an odd-dimensional object, where B1604 rules out an index. On the weave the moves generate the
    cube's rotations S₄, in which every 3-cycle is conjugate to its inverse. So the weave exchanges ω and ω², and
    their difference, the chirality, is not the weave's. Only A₄ would keep ω and ω² apart, and the quarter turns L
    and R are not in A₄.
- **So no even-dimensional frame built from the weave's forced local systems gives gauge-chiral generations without a
  choice.**
  - The dictionary (GENESIS FK11) is not a gap that more computation on these structures can close.
  - It needs an input the weave does not force: a selected parity, a thread's own order-3 orientation, or a structure
    outside the common point's local systems.
- **What the weave does force, all of it on the record:**
  - three, the parities' (W1);
  - alike (Theorem G);
  - an odd net chirality on the fibre, three when the parity grading is kept (W22 as qualified);
  - a complex flavor triplet T = μ ⊗ 3′, which is the tangent space of the character variety at the common point (W21,
    W24);
  - the hand, which is the records' orientation.

**Status.** COMPUTED (exact characters, numerical closures of groups of at most 192 elements) and PROVED (the lemma and
F5). A WEAVE theorem, and the precise form of the dictionary's status: three chiral generations with gauge content
cannot be derived from the weave's forced local systems alone.

## W26. The search beyond the weave: the weave is mirror-symmetric, and F-MC's order-3 orientation flips at every tick (`the_weaves_mirror.py`; `W26_RULE.md`)

**Why.** The owner's choice after W25: search beyond the weave, for a forced structure outside the common point's local
systems that fixes the gauge half. The owner named two candidates:
- the threads' hyperbolic holonomies, which are complex and flip under the mirror;
- main's F-MC arithmetic route: the prime of norm three gives 2T (every odd-trace thread, B1601), and McKay gives E₆,
  whose 27 against 27̄ is the ℤ₃ = 2T/Q₈ character ω against ω².

**The read-out (COMPUTED; the rule committed first, 186cb3d0; one run; every cell as predicted).**
- **N1, the weave is closed under the mirror (exact).**
  - For all 224 primitive cyclic words with both letters to length 10: S φ⁻¹ S⁻¹ is the matrix of φ′ = reverse(φ)
    with L and R exchanged. So M_φ′ = −M_φ, and the mirror of every thread is a thread.
  - Also exact: reverse(φ) = (PS) φ⁻¹ (PS)⁻¹, so M_reverse(φ) = M_φ.
  - 26 of the 224 are amphichiral: φ′ or swap(φ) is a rotation of φ. To length 6 they are LR, LLRR, LLLRRR, LLRLRR
    and LLRRLR.
  - Disclosed: the amphichirality criterion was widened from "φ′ a rotation of φ" during code review, before the run.
    The reason is the identity M_reverse(u) = M_u.
- **N2, the orientation-odd invariants pair up** (SnapPy 3.3.2, all 42 hyperbolic threads to length 6, both signs).
  - Every thread and its mirror have the same volume and opposite Chern–Simons invariant (mod ½).
  - SnapPy's isometries to the mirror reverse orientation (cusp-map determinant −1). An orientation-preserving one
    exists only for the amphichiral threads.
  - The amphichiral threads have CS 0 (the + signs) or ¼ (the − signs; m003 is −LR, at ¼, as in THE_CLAIM's B1226).
- **N3, the order-3 orientation alternates at every tick (exact).**
  - L and R are each a transposition of the three parities mod 2. L fixes (1, 0); R fixes (0, 1).
  - So on all 98 odd-trace words to length 10, the direction of the 3-cycle the monodromy induces on the parities
    (in the shared basis) flips at every tick.
  - Every odd-trace word has even length, so the flips close up around the circle.
- **N4 (a record fact).** F-MC's chirality is a declared input in main's own hypothesis list. THE_CLAIM §1 counts "two
  𝔽₂ bits (time's arrow; chirality — the conjugation bit, = τ)" among the five typed external data.

**What it shows (N5).**
- **The hyperbolic holonomies give no hand to the weave.** Every orientation-odd structure a thread carries
  (holonomy, cusp shape, Chern–Simons) has its complex conjugate on the mirror thread, which the weave also contains.
  Across the weave they cancel in pairs.
- **F-MC's McKay chirality is not a property of a thread.**
  - The ℤ₃ character of 2T (ω or ω²), which decides 27 against 27̄, is a property of a tick, and it flips at every
    tick.
  - F-MC itself counts chirality as an input.
  - So neither named candidate supplies a forced complex structure on the gauge side.
- **The weave's only hand is the records' orientation on the shared fibre** (W21). It is forced only if the swap P is
  not a move (GENESIS GM5c, OPEN). In physics, the name of a hand is a convention.
- **The record's best statement of the derivation is now this:**
  - the gauge structure from F-MC, with its typed inputs, the chirality bit among them;
  - the count from the weave (three, the parities'), with their common hand (W22);
  - one named identification between the two: GENESIS FK11, which W25 shows the weave cannot supply.
  - THE_CLAIM lists the generation count among the open inputs. The weave closes that input; the identification
    remains.

**Status.** COMPUTED (exact on N1 and N3; SnapPy numerics on N2, agreeing to 10⁻⁹). A WEAVE result, NEGATIVE for the
two named candidates beyond the weave.

## W27. The derivation with its one link stated, and the link tested (`the_link_tested.py`; `W27_RULE.md`; `docs/THREE_GENERATIONS_GIVEN_ONE_LINK.md`)

**Why.** The owner's choice after W26: state the link, write the derivation up, and test what the link implies. The
label is "derived given one stated link".

**The link Λ** (the weave's form of GENESIS FK11).
- One generation of matter is a field on spacetime × the shared fibre, in F-MC's 27 of E₆, carrying the
  parity-twisted spin bundle 𝕎.
- Each parity sector is one generation, kept apart from the others at the puncture.
- Its left-handed states are the fibre's holomorphic zero modes; this hand is the records' orientation.
- Λ is exactly the choice W25 shows the weave's forced bundles cannot make.

**The tests (COMPUTED, exact; the rule committed first, 6da777ea; one run; every cell as predicted).**
- **T1, anomalies.** Three 27s under SU(3) × SU(2) × U(1)_Y with the standard hypercharge cancel SU(3)³, SU(3)²Y,
  SU(2)²Y, Y³ and grav²Y, with an even number of doublets (18). One Standard Model generation with ν^c (4 doublets) and
  the 27's remainder (2 doublets) are each anomaly-free.
- **T2, the count.** Under Λ's parity grading the move-invariant end conditions give ±3 only (W24 D0, commutant 1).
  Without it, ±1 is possible too.
- **T3, the six-dimensional reading.**
  - Each parity sector, a rank-2 bundle with the left-handed fields of one 6d chirality, carries 8 SU(2) doublets.
  - Dobrescu–Poppitz's global condition, N(2₊) − N(2₋) ≡ 0 mod 6, holds for k sectors exactly when k ≡ 0 (mod 3):
    k = 3 and 6 pass, and 1, 2, 4 and 5 fail.
  - Stated as a limit, not a pass: the local gravitational count is unbalanced (32 Weyl fermions per sector), so a
    six-dimensional reading needs a completion that Λ does not supply.
- **T4, beyond the three.** Each 27 adds ν^c, D + D^c (Y = ∓1/3), H_u + H_d and S. That gives three right-handed
  neutrinos, and the rest must be heavy (F-MC's rank-closing directions).
- **Mixing: fenced** (THREE_GENERATIONS §3). No comparison with data is made.

**What it shows.**
- **The derivation, as the record can state it.** Three chiral Standard Model generations, anomaly-free, alike, in a
  complex flavor triplet, with three right-handed neutrinos. They follow from:
  - the principle (three, alike, the odd chirality, the triplet, the hand);
  - F-MC's typed inputs (the gauge group, its global form, the hypercharge);
  - one stated link Λ.
- **Λ is the input W25 and W26 show the weave cannot supply.** Earning it is GENESIS FK11.

**Status.** STATED (Λ, an input) and COMPUTED (T1–T4, exact). The label is "derived given one stated link", never
"derived from the principle" alone.

## W28. The end condition's routes to three, and the common point as the qubit (`the_three_routes_and_the_qubit.py`; `W28_RULE.md`)

**Why.** The owner approved the verification plan after the two contemplation turns: the foundation first (steps 1
and 2), then the ℤ₆ twist-eater (step 3, W29).
- **Part I** asks what W24's two middle end conditions are, and whether a natural requirement other than the parity
  grading excludes them.
- **Part II** checks the contemplation's reading of the common point as the qubit.
- Nothing here bears on the gauge content.

**Weave or thread?** Weave. Every cell takes all the moves' lifts and all three parities, at the point every move
fixes. The quantities are joint commutants and the group all the lifts generate.

**The rule** (`W28_RULE.md`, committed 57f019ed before the run). One run; every cell as predicted.

**Part I, the end condition (COMPUTED; exact up to floating point on groups of order at most 48).**
- **E1, the block form.** Every lift of L and R is Π ⊗ G: an unsigned permutation of the three parity blocks, which is
  the move's action on the parities mod 2, with one G ∈ 2O in every block.
  - In ρ_Q ⊗ ℂ³ coordinates every lift is Ad(G) ⊗ G, with Ad(G) a signed permutation of determinant 1.
  - So the six local solutions are vector ⊗ doublet.
  - P and −I have the same form.
- **E2, the two middle conditions.** They are the diagonal V₂ = {(v, v, v)} and the sum-zero V₄. Their projections
  span the commutant.
  - Under the group of order 48 the lifts generate, V₂ has character tr G (the spin doublet) and V₄ has
    (tr G)³ − 2 tr G (spin 3/2).
  - Both have norm 1 and Frobenius–Schur indicator −1.
  - V₂ is the Clebsch–Gordan copy Σ_p u_p v ⊗ e_p of the doublet: the γ-trace part of a vector-spinor.
- **E3, the flavor group.** The flat automorphisms of 𝕎 form M₃(ℂ) (dimension 9), acting as X ⊗ 1 on ρ_Q ⊗ ℂ³.
  - The lifts normalise it.
  - Its invariant subspaces are λ ⊗ ℂ³ (isotypic structure: the 3, twice), so the indices are −3, 0 and +3.
- **E4.** The part of the flavor algebra that keeps V₂ (or V₄) is the scalars, dimension 1. So every flavor symmetry
  other than a phase moves the two middle conditions.
- **E5, the index sets.** The puncture's holonomy is −1 on all six, and its commutant is all of M₆.

  | requirement | commutant | indices |
  |---|---|---|
  | the moves | 2 (the 2 and the 4) | −3, −1, +1, +3 |
  | the flavor group | 4 (the 3, twice) | −3, 0, +3 |
  | the parity grading | 12 | −3, …, +3 |
  | the moves and the flavor group | 1 | ±3 |
  | the moves and the parity grading | 1 | ±3 |
  | locality (the puncture's own symmetry, U(6)) | 1 | ±3 |

**Part II, the common point as the qubit (COMPUTED; I5 exact by sympy).**
- **I1, the Pauli group.**
  - ρ(a) = iZ, ρ(b) = iY and ρ(ab) = iX, so Q₈ is the qubit's Pauli group in SU(2).
  - Each parity is one Pauli axis, and its kernel is the holonomies along that axis: (0, ½) is Z, (½, 0) is Y and
    (½, ½) is X.
  - The three eigenbases are mutually unbiased.
- **I2, the Clifford group.** The lifts are:
  - L, e^{iπZ/4} (a quarter turn about Z, the phase gate up to a phase);
  - R, e^{−iπY/4};
  - P, (iZ + iY)/√2;
  - −I, iX.

  The lifts of L and R generate 2O (48), which is the normaliser of Q₈ in SU(2): it normalises Q₈, |Aut(Q₈)| = 24,
  and the kernel is ±1. Its 24 rotations are exactly those of the Clifford group ⟨H, S⟩.
- **I3, SU(2) at level 1.**
  - For both the semion SU(2)₁ and the anti-semion (E₇)₁: S² = 1 and (ST)³ = S².
  - Verlinde's loops are W_A = Z and W_B = X, and they anticommute (the common point's −1).
  - T fixes W_A and sends W_B to a multiple of W_A W_B.
  - The images in SO(3) are the weave's 24 rotations.
  - Exactly one cube rotation carries the weave's (ρ(a), ρ(b), g_L, g_R) to each theory's (W_A, W_B, T, ST⁻¹S⁻¹): for
    the semion x ↦ −y, y ↦ −x, z ↦ −z; for the anti-semion x ↦ −y, y ↦ x, z ↦ z.
  - The weave's images satisfy s² = (st)³ = t⁴ = 1. So the moves act on the common point through the (2, 3, 4)
    triangle group, PSL(2, ℤ/4) ≅ S₄.
- **I4, the three global forms of su(2).**
  - The maximal isotropic subgroups of 𝔽₂² are three (ℙ¹(𝔽₂)), and the three parities' kernels are exactly they:
    (0, ½) ↦ SU(2), (½, 0) ↦ SO(3)₊, (½, ½) ↦ SO(3)₋, with a electric and b magnetic (Aharony–Seiberg–Tachikawa).
  - Mutual locality is the parity's character.
  - The correspondence is equivariant under every move. L is θ → θ + 2π, fixing SU(2) and swapping SO(3)₊ and SO(3)₋.
- **I5, 't Hooft's twist-eater.**
  - Exact: q₀|p|² = (p · {p, q})/2 and p₀|q|² = (q · {p, q})/2. So anticommuting unit quaternions are pure and
    orthogonal, and every SU(2) pair with commutator −1 is conjugate to the common point.
  - Its centraliser is ±1.
  - Each non-trivial centre transformation (A, B) ↦ (ε_a A, ε_b B) is conjugation by one unit and is one parity: the
    twist-eater eats the centre symmetry.

**What it shows.**
- **The count.** ±3 follows from one natural requirement: the end condition breaks no symmetry of the bulk problem
  (the moves and 𝕎's flat automorphisms). Locality gives the same.
  - The middle conditions are the vector-spinor's spin-½ and spin-3/2 parts. They couple the sectors at the puncture
    and break flavor to a phase.
  - So Λ's "kept apart" (W27) is a consequence of that requirement, not a separate postulate about sectors.
  - The requirement itself is a naturality condition, stated, not derived.
- **The reading, now checked.**
  - The common point is the qubit, and the moves are its Clifford group, acting through SU(2) level 1's projective
    modular data.
  - The parities are the three Pauli axes, ℙ¹(𝔽₂), and the three global forms of su(2).
  - The hand is invisible to all of it: the semion and the anti-semion match equally, which is consistent with W26.

**Status.** COMPUTED (Part I; Part II) and PROVED (I5, exact): a WEAVE result. It is a foundation, not a gauge result.

## W29. The ℤ₆ twist-eater (qubit ⊗ qutrit) in E₈: an echo of the Standard Model's SU(3) × SU(2), not a derivation (`the_z6_twist_eater.py`; `W29_RULE.md`; post hoc `the_z6_twist_eater_posthoc.py`)

**Why.** Step 3 of the owner's approved plan.
- W25 showed that the weave's holonomy Q₈ makes every gauge reading self-conjugate.
- The qubit's flux −1 is its own inverse. A qutrit flux ω is not.
- Qubit ⊗ qutrit is the ℤ₆ Heisenberg pair H₆ = ⟨A, B⟩ (clock and shift in SU(6)′, commutator ζ = e^{2πi/6}). This arc
  reads it in E₈ ⊃ (SU(3) × SU(2) × SU(6)′)/ℤ₆.

**Weave or thread?** The object is chosen, not forced: nothing shown forces a qutrit flux (step 4, open). The
computations are joint over all moves, so this is a weave-type computation on a hand-picked structure, and every claim
is conditional on the flux.

**The rule** (`W29_RULE.md`, committed 37441028 before the run). One run, read out once.
- **A first launch was stopped before any read-out.** For the 36-dimensional adjoint, its null-space helper would have
  allocated a matrix of about 35 GB.
- **The fix, before the one run:**
  - the thin SVD for tall matrices;
  - the adjoint read by its joint eigenvalues (its two generators commute).
- Every cell came out as predicted, except two sub-claims of Z5 (below).

**The read-out (COMPUTED).**
- **Z1, the group.**
  - |H₆| = 216; its centre is the six scalars; the commutator is ζ·1. It is irreducible, with Frobenius–Schur
    indicator 0: complex.
  - Under the remainder ordering, C = Z ⊗ C₃⁻¹ and S = X ⊗ S₃ exactly, and A³, B³ = iZ ⊗ 1, iX ⊗ 1. So H₆ is the
    weave's qubit units tensored with a qutrit pair.
  - **The lemma (exact).** An invariant subspace W has ζ^{dim W} = 1, so it has dimension 0 or 6. Hence no U(1) of
    SU(6)′ commutes with H₆.
- **Z2, the centralisers in E₈:**
  - H₆: **11**, exactly SU(3) × SU(2);
  - the weave's qubit: 55, F₄ × SU(2);
  - the qutrit alone: 22, SU(3) × G₂;
  - the flux alone: 46.
- **Z3, the matter.**
  - The 6 and the 6̄ each occur 6 times: the multiplicity space is (3, 2).
  - **The 15 = Λ²6** has one type twice, which carries the qubit's trivial character (6 in the 248), and three types
    once. Those three carry the three non-trivial qubit characters, which are the three parities: Y, X and Z, the
    weave's (½, 0), (½, ½) and (0, ½). Each occurs 3 times in the 248, so each is a (3̄, 1).
  - **The 20 = Λ³6** has one qutrit-blind type twice (4 in the 248) and eight types once. Those eight carry the eight
    non-zero qutrit labels, in four conjugate pairs (the four lines of ℙ¹(𝔽₃)). Each occurs 2 times in the 248, so
    each is a (1, 2).
  - The adjoint is 36 distinct characters.
- **Z4, the flux and the orientation.**
  - exp(2πi diag(1/6 ×5, −5/6)) = ζ·1 (exact). Read through SU(5)′ × U(1)_Y, the flux is e^{2πiY}, the hypercharge's
    2π rotation (READING).
  - L, R and −I keep ζ, with one intertwiner each. The swap P sends ζ to ζ̄ and has none.
- **Z5, the moves at the puncture.**
  - The lifts of L and R have commutant 2, with pieces of dimension 4 and 2.
  - The 6-sector's index is −1, 1, 3 or 5 under the moves, and −1 or 5 under locality.
  - The index-0 condition that a smooth E₈ field would give is not move-invariant.
  - On Λ²ℂ⁶ the lifts' structure is 1 + 2 + 3 + 3 + 6, as predicted. So the 15-sector's index takes every value from
    −5 to 10 under the moves, and −5 or 10 under locality.
  - **Two sub-claims failed as stated:** the lift of −I is not the parity |k⟩ ↦ |−k⟩, and the pieces are not that
    parity's eigenspaces.
  - **POST HOC** (`the_z6_twist_eater_posthoc.py`):
    - The bare −I's lift is C·R₅: the clock times the reflection |k⟩ ↦ |5 − k⟩. Its two eigenspaces have dimension 3,
      and the moves exchange them.
    - The moves contain −I only composed with conjugation by ab⁻¹, as (LR⁻¹L)². Its lift is a reflection |k⟩ ↦
      |4 − k⟩, with eigenspaces of dimension 4 and 2, and those are the pieces.
    - The structure and every index set stand. Only the naming was wrong.
- **Z6, the anomalies.** SU(3)³ = 2n(3, 2) − n(3̄, 1).
  - **Under the moves** the anomaly-free pairs are (−1, −2), (1, 2), (3, 6) and (5, 10). Each has n(3̄, 1) =
    2n(3, 2), the Standard Model's two antiquark singlets per doublet. Three is one of four.
  - **Under locality** only (5, 10) is free: five, not three.
  - The coloured doublets 3|n(3, 2)| are odd for every move-invariant condition. The doublet sector is real (index 0),
    so there are no chiral lepton doublets.

**What it shows.**
- **The echo (conditional on the flux).**
  - The joint centraliser of the weave's qubit and a qutrit is exactly SU(3) × SU(2), the Standard Model's
    non-abelian group. The qubit alone gives F₄ × SU(2), and the qutrit alone gives SU(3) × G₂.
  - The quark doublets are complex. Among the antiquark singlets, one is labelled by each parity.
  - The flux is the hypercharge's 2π rotation, the element of the Standard Model's ℤ₆.
  - With a qutrit the hand becomes visible: the swap has no lift.
- **Not a derivation**, for four reasons:
  - (a) the flux uses up the hypercharge direction (the lemma), so U(1)_Y is broken;
  - (b) three is allowed but not forced: the moves allow −1, 1, 3 or 5, and locality with SU(3)³ gives 5;
  - (c) the coloured doublets are odd, and there are no chiral leptons;
  - (d) nothing shown forces the qutrit flux (step 4, open).
- **So the ℤ₆ lead closes as an echo.** W27's statement, with W28's naturality condition, stays the record's best.

**Status.** COMPUTED (one run; the rule committed first; every cell as predicted except Z5's naming of the −I lift,
corrected post hoc) and PROVED (the lemma). A weave-type computation on a CHOSEN object: conditional, and NEGATIVE as a
derivation.

**Qualified post hoc (2026-10-08, after the plan review; `the_z6_twist_eater_posthoc.py`, P3).**
- **Z5's and Z6's index sets assume that the moves are L and R,** the grammar's moves (GENESIS GM2).
- **The bare sign −I is its own fork** (GENESIS GM5b, FK4, open). With it a move, the lifts of L, R and −I have
  commutant 1 on the 6.
- So the 6-sector's set collapses from −1, 1, 3, 5 to −1 or 5, the same as locality's.
- W28's qubit is unchanged: the bare −I's lift already lies in the group of L and R (commutant 2 either way).
- The verdict stands, and it strengthens: with the sign a move, three is not even allowed.

## W30. Is an order-3 flux forced on the shared fibre? Allowed on the swap's fork, not forced (`the_order_three_flux.py`; `W30_RULE.md`)

**Why.** Step 4 of the owner's approved plan, after the close.
- Main's grade (GENESIS v1.28) says the derivation would be finished by a forced complex structure on the gauge side.
- A qutrit flux ω is the smallest such structure.
- This arc asks whether anything forces one.

**Weave or thread?** Weave-type. Every move acts jointly on the shared fibre's own representations, and the rank-3
object is the question, not an input.

**The rule** (`W30_RULE.md`, committed e611b54e before the run). One run.
- Most values were seen in the plan review and are listed as seen.
- Every cell came out as stated.

**The read-out (COMPUTED; Q1 and Q2 PROVED).**
- **Q1.** In every Sym^n of the forced point (n = 0, …, 8), and with every parity twist, [a, b] goes to (−1)^n. So the
  forced rank-2 data give no order-3 flux in any representation. A homomorphism cannot raise an element's order; this
  cell checks the code.
- **Q2.** The qutrit pairs (C₃, S₃) with commutator ω form one class: all nine centre twists are conjugate.
- **Q3.** On every twist:
  - L, R and −I keep the class (intertwiner dimension 1);
  - the swap P sends it to the ω̄ class (dimension 0);
  - the swap with complex conjugation keeps it (dimension 1).
  - On the qubit point the swap keeps its class, since −1 is its own inverse.
- **Q5.** On the qutrit's ℂ³ the lifts of L and R have projective order 24 (SL(2, 𝔽₃) ≅ 2T) and commutant 2, split
  2 ⊕ 1.
  - The lift of (LR⁻¹L)² is the reflection k ↦ 2 − k, and the bare −I's lift is k ↦ −k.
  - With the bare −I added: projective order 216, commutant 1.
- **Q6.** The record's order-3 structures are on threads or on the meridian:
  - W25's odd-trace extension (order 24, centraliser 25, ω fifteen times) is a thread object;
  - its orientation flips at every tick (W26);
  - mod 3 the puncture goes to −1 (sm:B1536; B284; main's B1601).

**What it shows.**
- **An order-3 flux is allowed on a fork, not forced.**
  - The forced data cannot produce one.
  - The qutrit point exists, and the grammar's moves keep it. But it is a common point only if the swap is not a move,
    or acts with complex conjugation, the C-type bit (GENESIS GM5c, FK3; B1083).
  - Its cusp condition in rank 3 is a choice (GENESIS GM4's parabolic puncture has no rank-3 form for a central ω).
- **Where the qubit and the qutrit part.** The qubit is blind to the swap. The qutrit makes the swap decide. So the
  gauge-side complex structure main's grade asks for is tied to one open fork of the grammar, the swap.
- **Main's finishing condition is not met by this route.**

**Status.** COMPUTED (one run; the rule committed first) and PROVED (Q1, Q2). A WEAVE result: an order-3 flux is
allowed on the swap's fork, NOT FORCED.

## W31. The ℤ₅ flux in E₈ ⊃ (SU(5)_g × SU(5)_b)/ℤ₅: complete SU(5) generations, but no anomaly-free three (`the_z5_twist_eater.py`; `W31_RULE.md`)

**Why.** The last step of the owner's approved plan.
- Holonomies that keep the whole Standard Model lie in its centraliser in E₈. A twist-eater flux that keeps it therefore
  has order 5 (Reading W24–W29, point 2).
- Main's grade (GENESIS v1.28, S86) names SU(5) among the holonomy groups with complex representations that would finish
  the derivation if forced.

**Weave or thread?** A weave-type computation on a chosen structure. Every cell is joint over the moves. The ℤ₅ flux is
chosen, not forced, so every claim is conditional on it.

**Labels.** SU(5)_g is the gauge factor; it contains the Standard Model. SU(5)_b is the bundle factor, the Standard
Model's centraliser, where the clock C₅ and the shift S₅ live. The record's "SU(5)′" has named both (TERMINOLOGY's
registry).

**The rule** (`W31_RULE.md`, committed 55c26b10 before the run). One run.
- Most values were seen in the plan review and are listed as seen. The run confirms them in committed code; it is not an
  independent test.
- Every cell came out as stated.
- Before the run, reading the script found three faults: a leftover block and two sets of repeated dictionary keys, which
  would have overwritten values. They were fixed, and the rule's sentence on A₅ was added to F5's test.
- A first launch failed before the script started (a timing tool missing from the container), so it produced nothing.

**The read-out (COMPUTED; F1's lemma PROVED; F4's Wilson-line argument PROVED in the rule, not computed).**
- **F1.** ⟨C₅, S₅⟩ has order 125, centre ζ^j·1 and commutator ζ·1. It is irreducible on ℂ⁵ and complex (indicator 0), so
  no U(1) of SU(5)_b commutes with it.
- **F2.** Its centraliser in E₈ has dimension 24: exactly SU(5)_g. W25's chi248 at diag(h, 1) and the explicit
  SU(5)_g × SU(5)_b form agree on all 125 elements, to 1.2·10⁻¹³. The two are one expression, so this checks the code.
- **F3.** The 5 occurs 10 times (the 10 of SU(5)_g). Λ²5 is two copies of one type (central character ζ²), and that type
  occurs 10 times (the 5̄ of SU(5)_g, twice). Both are complex: complete SU(5) generations, 10 + 5̄. The 248 is
  accounted for: 24 + 24 one-dimensional, plus 4 × 50.
- **F4.** The flux is a hypercharge rotation.
  - exp(2πi·(6j/5)·Y) = ζ^{−2j}·1 on SU(5)_g's 5 (exact).
  - Through the centre kernel (ζ, ζ⁻²), the flux ζ^m in SU(5)_b is ζ^{−2m} in Z(SU(5)_g).
  - For every flux, L, R and −I keep it (one intertwiner each). The swap P sends it to its conjugate (none). P∘K keeps
    it (one).
- **F5.** The lifts of L and R on ℂ⁵ (flux ζ):
  - projective order 120 (SL(2, 𝔽₅) ≅ 2I); commutant 2, split 3 ⊕ 2;
  - the 2-piece is 2I's spin representation: normalised to det 1 there, the group has order 120 and traces 0, ±1, ±φ,
    ±φ⁻¹, ±2, so |tr|² takes the golden values φ² and φ⁻². The 3-piece factors through A₅ (projective order 60);
  - the pieces are the eigenspaces of the lift of (LR⁻¹L)², the reflection k ↦ 4 − k. The bare −I's lift is k ↦ −k; its
    eigenspaces also have dimensions 3 and 2, but they are not the pieces;
  - with the bare −I added: commutant 1, projective order 3000;
  - on Λ²ℂ⁵: 1 ⊕ 3 ⊕ 6.
- **F6.** The counts. The structure is the same for every flux: d₅ ∈ {0, 2, 3, 5} and d₁₀ ∈ {0, 1, 3, 4, 6, 7, 9, 10}.

  | flux | n(10) under the moves | n(10) under locality | SU(5)³-free under the moves | SU(5)³-free under locality |
  |---|---|---|---|---|
  | ζ | −1, 1, 2, 4 | −1, 4 | −1, 2 | none |
  | ζ² | −2, 0, 1, 3 | −2, 3 | −2, 1 | none |
  | ζ³ | −3, −1, 0, 2 | −3, 2 | −1, 2 | none |
  | ζ⁴ | −4, −2, −1, 1 | −4, 1 | −2, 1 | none |

  - **No ℤ₅ flux gives an anomaly-free three**, under the moves or under locality.
  - With ζ^{±2}, three 10s occur under locality, but never with three 5̄s.

**What it shows.**
- **What it gives, conditionally:** complete SU(5) generations, the hypercharge inside SU(5)_g, and the moves acting
  through 2I with golden traces.
- **NEGATIVE as a derivation:**
  - no anomaly-free three for any ℤ₅ flux;
  - SU(5)_g, the whole centraliser, is not broken to the Standard Model by anything forced: the moves force trivial
    hypercharge Wilson lines (F4's argument);
  - an unbroken SU(5) is not the Standard Model, and F-MC's derived cascade skips SU(5) (SMT, B892; its B1237 addendum
    corrects the landing and leaves the skip);
  - the flux is not forced. The forced point's puncture has order 2 (W30, Q1), and the record's order-5 structures are
    properties of the modulus or of threads (B206; the golden-covers dossier);
  - the swap sends the flux to its conjugate, so it is a common point only on the swap's fork (GENESIS GM5c), as in W30.
- **Readings (not computed claims):**
  - The anomaly-free counts are ±1 or ±2. W23 found at most two complete generations by a different construction.
  - 3000 = 5² × 120, the order of the ℤ₅ qudit's Clifford group modulo phases. The moves L and R give a complement,
    SL(2, 𝔽₅); the bare sign adds the translations. The qutrit shows the same (W30: 216 = 3² × 24).
  - The moves' group here, 2I = SL(2, 𝔽₅), is the group B206 found as the golden object's spin shadow. Here it comes
    from the flux's order alone, which agrees with B206's correction: the shadow group is a property of the modulus.
- **The twist-eater programme gives no forced three:**
  - ℤ₆ breaks the hypercharge (W29);
  - a qutrit is allowed only on the swap's fork (W30);
  - ℤ₅ keeps the hypercharge but allows no anomaly-free three (W31).
  - Main's finishing condition is not met by any flux tried.

**Status.** COMPUTED (one run; the rule committed first), with F1's lemma and F4's argument PROVED. A CHOSEN object (the
ℤ₅ flux, not forced). NEGATIVE as a derivation.

## W32. The puncture's end condition in F-HE's two sectors: never three (`the_puncture_content.py`; `W32_RULE.md`)

**Why.** The owner's "do as u recomend on all" (2026-10-08). The recommendation's third item was the puncture's content
(GENESIS GAP2's place), the one computational route left for the count. W23 left it open: the weave's five reads (1, 3)
in F-HE and needs +2 at the puncture, which the anomaly alone does not fix.

**Weave or thread?** Weave-type. It takes every rank-5 bundle built from the common point's blocks that L and R keep,
with the end conditions the joint action keeps. F-HE is a frame (GENESIS GAP1), so every count is conditional on it.
The moves are L and R: by main's S87 the swap and the tick reverse the orientation the index needs.

**The rule** (`W32_RULE.md`, committed 62138306 before the run). One run; every cell came out as stated.
- The values had been derived by hand and are listed as seen.
- A first launch stopped at an assertion in the census before writing anything. The code had admitted a bundle on a
  non-zero intertwiner space, which need not hold an isomorphism. The census was corrected to the rule's criterion
  (the class kept, so an invertible intertwiner), and the script then ran once.

**The read-out (COMPUTED; P1 PROVED).**
- **P1.** Localized content that cancels the five's anomaly leaves 3 + b complete generations, where b is the
  puncture's net 5̄ number. Three needs b = 0.
- **P2.** L and R keep five bundles: χ₀⁵, χ₀² ⊕ P, D ⊕ χ₀³, D ⊕ P (the weave's five) and D² ⊕ χ₀.
- **P3, the control.** W22's block rule gives (0, 0), (0, 0), (1, 3), (1, 3) and (2, 2): W23's set.
- **P4 (naturality) and P5 (locality):**

  | bundle | n(10), natural | n(5̄), natural | anomaly-free, natural | anomaly-free, local |
  |---|---|---|---|---|
  | χ₀⁵ | 0, 5 | 0, 10 | 0 | 0 |
  | χ₀² ⊕ P | 0, 2, 3, 5 | 0, 1, 9, 10 | 0 | 0 |
  | D ⊕ χ₀³ | −1, 1, 2, 4 | −3, 1, 3, 7 | 1 | 1 |
  | D ⊕ P | −1, 1, 2, 4 | −3, −2, 0, 1, 3, 4, 6, 7 | 1, 4 | 1 |
  | D² ⊕ χ₀ | −2, −1, 2, 3 | −2, 1, 2, 4, 5, 8 | −2, 2 | −2, 2 |

  - **No natural or local three for any bundle.**
  - The weave's five is cured naturally only at one or four complete generations (b = −2 or +1).
- **P6, what three would need, on the weave's five.**
  - n(5̄) = 3 is natural: 𝕎 = D ⊗ P at +3 (W28).
  - n(10) = 3 is not. It needs the plane x₁ + x₂ + x₃ = 0 in the parity lines' local solutions. The lifts with
    permutation entries keep that plane (their structure on the three lines is 1 ⊕ 2); the bulk commutant does not.
  - **So three in the 5̄-sector needs the parities kept apart, and three in the 10-sector needs them mixed.**

**What it shows.**
- **In F-HE the puncture does not make three.** The end condition is how the puncture enters a count (GENESIS GAP2).
  Under every condition the weave keeps, no bundle from the common point's blocks gives an anomaly-free three.
- **Why: F-HE's two sectors need opposite principles.**
  - The 5̄-sector holds 𝕎 = D ⊗ P, where naturality gives the weave's ±3 (W28).
  - The 10-sector holds D ⊕ P itself. There naturality makes the three parity lines all or nothing, and the doublet
    counts ±1, so the count is ±1 + {0, 3}, never three.
- **So three complete generations need a frame whose 10-sector holds 𝕎 (rank six).** That is W27's six-dimensional
  reading with its link Λ (GENESIS FK11), which stays the one link.

**Status.** COMPUTED (one run; the rule committed first), with P1 PROVED. A WEAVE result within the frame F-HE:
NEGATIVE for the puncture route.

**Scope (added 2026-10-08, the audit lane's reading, accepted).** W32 reads flat bundles built from the common point's
blocks, with the end conditions the weave keeps. A non-flat stationary end is outside it: GENESIS GAP3's source, of
which the audit lane's cusp condensate is the first instance on the weave's own action.

## W33. Is "three exactly when the odd spin structure is left out" a law? No: the counts are label-blind on doublets (`the_odd_spin_structure_across_frames.py`; `W33_RULE.md`)

**Why.** The owner's "do it" (2026-10-08), on the second contemplation's proposal: test its point 2 across the record's
frames. The arc tests this seat's own claim.

**Weave or thread?** Weave-type. It takes every bundle from the common point's blocks that L and R keep, in W23's three
frames (E₆ rank 3, SO(10) rank 4, SU(5) rank 5), with the end conditions the joint action keeps. Every frame is a
hypothesis (GENESIS GAP1).

**The rule** (`W33_RULE.md`, committed 35d16dff before the run). One run; every cell came out as stated, with one wording
difference.
- The tables had been derived by hand and are listed as seen.
- **The wording difference.** The rule called the naive law "vacuous" under (B) and (S). Only one direction is: no
  three occurs. The other direction fails, since E₆'s P has no zero-parity block and no three. The computed verdict,
  "fails", is the accurate reading.

**The three conventions** are the ones the record has used:
- (B) W22's block rule;
- (N) naturality on every channel (W28, W32);
- (S) the spinor rule: naturality on the gauge −1 channels only, following the audit lane's antiperiodic gauge +1
  channels.

**The read-out (COMPUTED).**

| frame | bundle | zero parity's blocks | (B) | (N) | (S) |
|---|---|---|---|---|---|
| E₆ | P | no | 0 | 0, 3 | 0 |
| E₆ | χ₀³ | yes | 0 | 0, 3 | 0 |
| E₆ | D ⊕ χ₀ | yes | 1 | −1, 0, 1, 2 | ±1 |
| SO(10) | χ₀ ⊕ P | yes | 0 | 0, 1, 3, 4 | 0 |
| SO(10) | χ₀⁴ | yes | 0 | 0, 4 | 0 |
| SO(10) | D ⊕ χ₀² | yes | 1 | −1, 1, 3 | ±1 |
| SO(10) | D² | yes | 2 | ±2 | ±2 |

- **SU(5), the anomaly-free counts:** (B) W23's set; (N) W32's table; (S) 0 for χ₀⁵ and χ₀² ⊕ P, none for D ⊕ χ₀³ and
  D ⊕ P (±1 against ±3), ±2 for D² ⊕ χ₀.
- **T3, the naive law,** fails under every convention.
  - Under (N), E₆'s χ₀³, built from the zero parity alone, gives three, and so does SO(10)'s D ⊕ χ₀² (1 + 2).
  - Under (B) and (S) no three occurs, while E₆'s P has no zero-parity block.
- **T4.** Under (S), every sector's count is ± its number of doublet blocks, in every frame. So no three occurs below
  rank six: W23's "three needs rank six", as a law.
- **T5.**
  - The three parity doublets 𝕎 count ±3 under (N) and (S).
  - With the zero parity's doublet added (rank 8), the count is ±4, one irreducible piece of dimension 8.
- **T6, the sources of each three under (N):**
  - E₆'s P and SO(10)'s χ₀ ⊕ P: the three parity lines;
  - E₆'s χ₀³: three trivial lines;
  - SO(10)'s D ⊕ χ₀²: the doublet and two trivial lines.

**What it shows.**
- **The second contemplation's point 2 is withdrawn in its strong form.** The counts do not single out the odd spin
  structure by its label: χ_p ⊗ ρ_Q ≅ ρ_Q, so doublet blocks are label-blind, and what a count sees is how many there
  are.
- **Its precise form stands (T5).** If the zero parity's doublet shares a sector with the three parity doublets, the
  count is four, and no condition the weave keeps separates it.
- **Below rank six, whether three can appear depends only on how the gauge +1 channels are counted.**
  - Under naturality, three is a rank count, available to the trivial bundle. It is therefore not evidence of the
    weave's three.
  - Under the spinor rule, which the audit lane's spin analysis favours, three needs three doublet blocks.
- **So the record's count stays where W23 and W27 put it:** 𝕎, at rank six, with its link Λ.

**Status.** COMPUTED (one run; the rule committed first). A WEAVE result within the record's frames: NEGATIVE for the
naive law, and a correction of this seat's own reading.

## W34. The observer layer on the weave: its negatives belong to every thread, and the register carries no hand (`the_observer_layer_on_the_weave.py`; `W34_RULE.md`; post hoc `the_observer_layer_posthoc.py`)

**Why.** The owner's questions (2026-10-08):
- does the observer layer ever enter the final math, and do the record's negative conclusions about it hold for m004
  alone or for the whole weave?
- then "lets do it": could the observer layer, taken on the whole from the principle to closure, be the ingredient the
  derivation is missing?

The record's four observer-layer probes (Gate 5-Q; QP-1 to QP-4: B762, B761, B760) and main's syntheses B1183 and B1184
were all computed on m004 at its geometric representation. They are thread results. This arc computes structure only
(Gate 5-Q, Q5), and its terms are the probes' bound labels. The experiential question stays apart (GENESIS FK12).

**Weave or thread?**
- Q1 and Q3 are censuses over every thread (GENESIS's 758 states to length 12). A property holding on all of them is a
  law over the threads, never a weave quantity.
- Q2 is weave-type: the common point is fixed by every move, the puncture is shared, and the quantity is what the
  joint action keeps.
- Q4 is assembled from the record. Q5 is exact, on the four founding rules.

**The rule** (`W34_RULE.md`, committed 1915fe92 before the script existed; the script committed ddd62c4e while its one
run was in progress). One run. Q2, Q3 and Q5 came out as stated. Q1 missed its sealed criterion on 11 states, resolved
post hoc (below).
- **Disclosed before the read-out.** The timing prototype that preceded the rule built its null space from mpmath's
  thin SVD, which drops the null directions of a wide matrix (an out-of-range row of an mpmath matrix reads as zeros).
  It reproduced m004's values only because one genuine null vector sufficed. The script takes the full V and checks
  every kernel vector is null.

**The read-out (COMPUTED).**
- **Q1, the private states on every thread (B761 → every thread).** All 758 states have geometric solutions; no error.
  - 747 states were decided at 60 digits, and every one has (dim H¹, rank, private) = (1, 1, 0) in each block
    Sym², Sym⁴, Sym⁶. So fiber_dim(n) = 0 for n = 2, 3, 4. The control m004 gives B761's values.
  - 11 states were left undecided by the rank rule (one singular value between 10⁻⁴⁰ and 10⁻²⁵ relative), each only
    in Sym⁶, all of word length 12 (volumes 3.6 to 10.7). So the script's sealed criterion (every state decided, and
    (1, 1, 0)) failed on these 11.
  - **POST HOC** (`the_observer_layer_posthoc.py`, labelled, thresholds stated before it ran). The 11 were recomputed
    from SnapPy's polished holonomy at 400 bits, at 120 digits. All are (1, 1, 0) in every block. Their smallest
    genuine singular values reach 1.0 × 10⁻³⁵, below the run's 10⁻²⁵ threshold, and the zeros fall below 10⁻⁹⁶. So the
    band at 60 digits was too narrow for these threads' Sym⁶; Menal-Ferrer and Porti's theorem holds on all 758.
- **Q2, the private states at the common point (B761 → the weave; exact).** The table came out as derived by hand:

  | k | Q₈'s characters in Sym^{2k} (χ₀, χ₁, χ₂, χ₃) | dim H¹ | rank to the puncture | private | kept by L, R jointly |
  |---|---|---|---|---|---|
  | 1 | 0, 1, 1, 1 | 3 | 3 | 0 | 0 |
  | 2 | 2, 1, 1, 1 | 7 | 3 | 4 | 0 |
  | 3 | 1, 2, 2, 2 | 8 | 6 | 2 | 0 |

  - So at the common point fiber_dim(n) = 0, 4, 6 for n = 2, 3, 4.
  - The private states are flat twists of each block's trivial pieces, which the puncture, a commutator, cannot detect.
    At n = 3 they are the flat twists of the three parity lines, their Wilson lines on the fibre.
  - **Kept by the joint action: nothing,** in every block, on H¹ and on the private states, for L and R, and with P
    and −I added.
  - **Kept by one move alone (H¹, private), k = 1, 2, 3:** L and R keep (1, 0), (1, 1), (1, 0). P keeps (2, 0), (3, 2),
    (4, 1). −I keeps (3, 0), (3, 0), (6, 0). So the parabolic L and the involution P can keep a private state.
  - **Kept by each thread alone:** no private state, on all 758 states. A thread acts on the private states as its own
    hyperbolic matrix (eigenvalues λ^{±1}) tensored with a map of finite order.
  - On all of H¹, the 326 odd-trace states keep (1, 1, 2), as predicted. The even-trace states keep (1, 0, 1) on 136,
    (1, 1, 2) on 124, (1, 2, 3) on 132 and (3, 3, 6) on 40.
- **Q3, the self-name among the threads (B762, B1184 → every thread).** The name is the volume and the cusp shape up to
  GL(2, ℤ) and the mirror, compared at 30 digits.
  - The 758 states have 536 names. The 222 coincidences are exactly the reversal pairs (a word and its reverse with the
    same sign), and SnapPy finds each pair one manifold. No other two states share a name.
  - Every + state is separated from its − state by the cusp shape. Their volumes agree on all 379 pairs (read from the
    run's volumes after the read-out), since both are half of M_{φ²}.
  - m004's cusp shape reduces to 2√3 i, and m003's to the hexagonal (½, √3/2).
- **Q4, the self-sign on the weave (assembled; no computation).**
  - W26 N1–N2: the weave is closed under the mirror.
  - Main's B1607, B1609 and B1610: the three's hand is the sheet of the orientation double cover, which the rule itself
    exchanges.
  - B1183: on m004 the self-sign obstruction is the orientation.
  - So the weave cannot sign itself, and on the weave the self-sign is exactly the hand (GENESIS SE2, GM5c).
- **Q5, the register (GENESIS FK12) and the hands (exact).**
  - σ = L∘P as automorphisms; rev(σ) = ι_{a⁻¹}∘σ; C(rev σ) = ι_{b⁻¹}∘C(σ); C(σ) = P∘σ∘P.
  - All four rules have determinant −1. σ and rev(σ) have one matrix, one cyclic order of the parities, and one class
    of lift modulo Q₈. Their lifts differ by ρ_Q(a)⁻¹, and they act identically on H¹ in every even block. The same
    holds for C(σ) and C(rev σ).
  - The control can fail and does: C flips the cyclic order and the lift's class, and σ and C(σ) act differently on
    H¹.
  - **So the register (ab against ba) is an inner automorphism, and it carries neither hand.** This recomputes main's
    B1610 hand-(ii) row for the reversal and for C with this seat's code, and gives the reason.

**What it shows.**
- **The observer layer's negatives belong to every thread, not to m004.**
  - No private states holds on all 758 states. It is the class's property (Gate 5-Q, Q2b).
  - The self-name holds on every thread among the threads, up to the register.
  - The self-sign is the hand.
- **The weave's own version is sharper than the thread's.**
  - The shared fibre does hide states from its puncture, from rank three.
  - Every tick stretches them, so no thread keeps one, and the joint action keeps none.
  - Its infinitesimal reading: nothing the weave keeps tells the three parity lines apart by a flat twist. This is W31's
    "the moves force trivial hypercharge Wilson lines", at first order.
- **The name's one blind spot is the register, and the register carries no hand.**
  - What the observer layer cannot name (the order of the letters) cannot decide the hand either.
  - Even if the act generated its register (GENESIS FK12), the three's hand would not follow from it.
- **So, as far as the record can compute it, the observer layer is not the missing ingredient.**
  - The hand is the orientation sheet: a choice, GENESIS SE2 and GM5c.
  - The count's open link is the dictionary Λ (GENESIS FK11).
  - The parameters live in the couplings (main's S90).
  - None of the probes touches any of the three.

**Status.** COMPUTED (one run; the rule committed first; Q1's sealed criterion missed on 11 states and resolved post hoc,
labelled). Q2 and Q5 are WEAVE results; Q1 and Q3 are laws over the threads. NEGATIVE for the observer layer as the
missing ingredient.

## W35. Main's B1612 verified: the mixing patterns the weave's group fixes, rebuilt from this seat's construction (`the_mixing_patterns_verified.py`)

**Why.** The owner's goal of 2026-10-08 is the full Standard Model from the principle, and main's B1612 is the weave's
first value contact. Its TM1 column is load-bearing for the lepton side. The owner's rule: verify load-bearing math even
when it is published.

**What was done.** A VERIFICATION, not blind: B1612's read-out was read first (main @ 80f48eeb). The weave's group was
rebuilt from W21's construction, not from main's instrument:
- V = H¹(F₂; ⊕_p χ_p ⊗ ρ_Q) with the moves' lifts, and its closure;
- the holomorphic triplet T;
- the Hodge–Riemann form, positive on T, as the inner product.

**The result (COMPUTED; every check holds).**
- The image on T has order 96, and 56 of its elements have three distinct eigenvalues.
- There are 11 eigenbases and 9 eigenlines.
- **Six full patterns:** single maximal angle; tri-bimaximal; bimaximal; trimaximal with (2 ∓ √3)/6; the circulant
  (1/9, 4/9, 4/9); democratic.
- **Five columns:** (0, 0, 1), (0, ½, ½), TM1 (⅙, ⅙, ⅔), (¼, ¼, ½) and TM2 (⅓, ⅓, ⅓).
- **B1612's named cells:**
  - L against R is bimaximal;
  - RL against ⟨RR, R⁻¹LL⟩ is tri-bimaximal;
  - L against RL is trimaximal, with (2 − √3)/6;
  - RL against RR's eigenline gives TM2, and against RRL's eigenline TM1.
  - The order in which the products are taken does not matter: one simultaneous conjugation carries each pair to its
    reverse.

**What it shows.** B1612's structural half stands on this seat's construction.
- The weave's group acts on the matter triplet as the cube's rotations (S₄, times scalars), and its residual symmetries
  give exactly these patterns.
- TM1 comes from the root's double tick RL against RRL, with no swap.
- The contact half (the comparison with data) was not redone here. Its sum rule sin²θ₁₂ = 1 − 2/(3 cos²θ₁₃) follows
  exactly from the TM1 column.

**Status.** VERIFIED (not blind): main's WEAVE result, reproduced. 0 of 19.

## W36. The audit lane's gapped Standard Model phase: its centralizer checked, and what a two-dimensional object cannot give (`the_sm_centralizer_in_e8.py`)

**Why.** The owner's goal is the full Standard Model. The audit lane's newest packet builds, on one supplied curved E₈
action, a global stationary phase with the Standard Model's gauge group and a full fermion gap. Every charged index in
it is zero, so it has no generations. Its relay asks four things; this answers two.

**Its step 1: the centralizer (a review; the claim read first; exact).**
- E₈ is simply connected, and a torus's centralizer is connected. The SM's maximal torus is SU(5)_g's, so the SM's
  centralizer lies in T_SM · SU(5)_b.
- **The roots.** With SU(5)_g's roots e_i − e_j (i, j ≤ 5), the roots orthogonal to them are exactly 20, and they form
  an A₄: SU(5)_b.
- **The torus part.** An element of T_SM commutes with SU(3) × SU(2) exactly when it is diag(a, a, a, b, b) with
  a³b² = 1. That is the kernel of the character (3, 2), connected since gcd(3, 2) = 1: it is U(1)_Y, and it holds
  Z(SU(3)) × Z(SU(2)).
- U(1)_Y meets SU(5)_b in SU(5)_g's centre ℤ₅, the one E₈ identifies.
- **So the centralizer is (SU(5)_b × U(1)_Y)/ℤ₅, and it is connected, as the audit lane states.** VERIFIED (exact,
  not blind).

**Its step 4: an existing end mechanism that changes the index (a READING, with one exact piece).**
- **The exact piece.** On a closed surface the index of the 10 is deg W, and of the 5̄ deg Λ²W. Both are zero for every
  SU(5)_b bundle, flat or not, since the curvature is traceless. So the fibre's bulk gives no net SU(5)_g chirality.
- **The record's nonzero counts on the fibre are end contributions:** n = −r₋/2 + dim Λ₊ (W22) at the puncture, on the
  gapless gauge −1 channels (W28; W32 scoped them to flat ends). A gapped cusp removes that freedom, which is consistent
  with the audit lane's zero.
- **What could change it with a gap.** Either asymptotic data with winding at the end, or an object of real dimension
  at least four (W19's M₁,₂, where products of first Chern classes exist).
  - In the complete cusp a winding condensate has infinite gradient energy unless a flux compensates it. That is the
    audit lane's magnetic family A_n, which they predict unstable.
- **The common point's own twist.** It is 't Hooft's (W28 I5). On the closed fibre it forces every U(2) lift to have
  odd degree, so ±1 per doublet block.
  - Inside SU(5)_b that degree is compensated on the parity part (c₁(W) = 0).
  - With S₃ kept, the compensation needs the order-3 twist of W30, which is allowed on the swap's fork and not forced.

**Status.** Step 1 VERIFIED (exact). Step 4 a READING with one exact obstruction: no SU(5)_g chirality from any SU(5)_b
bundle on a two-dimensional object.

## W37. Main's S92 verified: TM1's forward prediction (B1613) and the observer layer on the weave (B1614) (`the_tm1_prediction_and_observer_layer_verified.py`)

**Why.** The owner's goal of 2026-10-08 is the full Standard Model. B1613 is the record's first numerical forward
prediction (falsifier P10), and B1614 answers, on main, the owner's question that W34 answered here. The owner's rule:
verify load-bearing math. A VERIFICATION, not blind: both read-outs were read first (main @ 6df00941).

**B1613 (COMPUTED; every check holds).**
- **The relations were derived here from the matrix entries.**
  - TM1 is |U_e1|² = c₁₂²c₁₃² = 2/3, so sin²θ₁₂ = 1 − 2/(3 cos²θ₁₃).
  - |U_μ1| = |U_τ1| gives cos δ = −(s₁₂² − c₁₂²s₁₃²) cos 2θ₂₃ / (2 s₁₂c₁₂s₁₃ sin 2θ₂₃).
- **At B1613's inputs** (NuFIT 6.1 via the record: sin²θ₁₃ = 0.02248, sin²θ₂₃ = 0.470), at 50 digits:
  - sin²θ₁₂ = 0.31800 and θ₂₃ = 43.280°;
  - cos δ = −0.130278, so δ = 97.486° or 262.514°;
  - J = ±0.0337754, the matrix and the formula agreeing.
  - The TM1 column holds on the full matrix on both branches, to 10⁻⁵¹.

**B1614 (COMPUTED; exact; every check holds).**
- **The moves' joint fixed points** on the character variety are (0, 0, 0), the common point, and (2, 2, 2), the trivial
  character.
- **Each local system at the common point, (dim H¹, visible at the puncture, private):**
  - the trivial line: (2, 0, 2);
  - each parity line: (1, 1, 0);
  - the adjoint: (3, 3, 0);
  - the doublet, and each matter block χ_p ⊗ ρ_Q: (2, 0, 2), since the puncture acts as −1 and its cohomology is zero.
- **The triplet's characters**, with W21's lifts: χ_T(L) = e^{−iπ/4}, χ_T(R) = e^{+iπ/4}, χ_T(LR) = 0.
- **The odd classes** (det, the sign of the parities' permutation) are L (0, 1), R (0, 1) and P (1, 1): rank 2 over 𝔽₂.

**What it shows.**
- Both of main's S92 arcs stand on this seat's code.
- B1614 and W34 agree where they overlap: the adjoint is visible, and the trivial pieces are private. Each adds what
  the other lacks.
  - B1614 adds the odd blocks: the doublet and the matter are wholly private.
  - W34 adds what the weave keeps: no private state is kept by any thread, nor jointly. It also adds the thread
    censuses and the register lemma.
- **The matter that carries the three is wholly private at the puncture.** Its cohomology restricts to zero there.
  That is the observer layer's form of W36's statement that the fibre's counts are end effects.

**Status.** VERIFIED (not blind): main's WEAVE results, reproduced. 0 of 19.

## W38. Main's B1615 and B1616 verified: the weave's group fixes no mass (`the_couplings_verified.py`)

**Why.** Main's S93 and S94 close the flavour question as a negative: with B1611 (the phase) and B1612 (the angles), the
weave's group fixes no flavour value, not the masses (B1615) and not the neutrino masses (B1616). It is load-bearing for
the parameter side, so it is verified here: a VERIFICATION, not blind, both read-outs read first (main @ dfb57904).

**What was done.** The group on the matter triplet T was rebuilt as in W35, from W21's construction, in the orthonormal
basis of the Hodge–Riemann form. Then:
- the invariants by characters;
- Dirac masses on End(T) (M ↦ g M g†): the isotypic pieces from a generic commutant element, and each piece's matrices
  fixed by each residual element L, R, RL and RRL, the masses being singular values;
- Majorana masses on the symmetric matrices (M ↦ g M gᵀ), the same way.

**The result (COMPUTED; every check holds).**
- **Invariants.** (T ⊗ T̄)^G has dimension 1. T ⊗ T, Sym² T, Λ² T, T ⊗ T ⊗ T and T ⊗ T ⊗ T̄ have none: no mass term or
  cubic of the matter alone.
- **Dirac.** T̄ ⊗ T = 1 + 2 + 3 + 3, each once (commutant 4).
  - A singlet Higgs gives (1, 1, 1).
  - The fixed vacua give only (0, 1, 1), along L, R, RL and RRL in one triplet, and (½, ½, 1): in the doublet along L,
    R and RRL, and in the other triplet along RL.
  - Along RRL that triplet has a two-dimensional fixed space: a family obeying m₁ + m₂ = m₃. The largest violation over
    4000 samples is 3 × 10⁻¹⁵ of m₃, and m₁/m₃ ranges over [0, ½].
- **Majorana.** Sym² T = 1 + 2 + 3, and Λ² T is irreducible.
  - Along RRL no vacuum is fixed.
  - Along RL the spectra are (1, 1, 1) and (½, ½, 1); along L and R they are (0, 1, 1).
- RL has three distinct eigenvalues on T, so at TM1's charged-lepton symmetry the masses are three free parameters.

**What it shows.**
- B1615 and B1616 stand on this seat's construction. The weave's group alone gives three equal masses, rigid degenerate
  spectra, or one family with m₂ ≥ m₃/2.
- So the charged leptons' hierarchy (m_μ/m_τ ≈ 0.059, imported) is out of reach. Every rigid Majorana spectrum has
  an exactly degenerate pair, which the two measured neutrino splittings exclude.
- B1615's sealed bound "no ratio below 0.1" failed on the RRL family, as main disclosed: here m₁/m₃ is sampled down to
  10⁻⁴.
- With W35 and W37, all four of main's flavour arcs since the reopening are reproduced here. The values need a forced
  modulus τ, dynamics, or end data (W36), which is main's question to this seat.

**Status.** VERIFIED (not blind): main's WEAVE results, reproduced. 0 of 19.

**Addendum, the same night: exact and POST HOC (`the_couplings_exact.py`).** It answers the audit lane's two
verification requests. B1615's sum rule was shown on a numerical grid, and the audit lane asked for an exact certificate
on the whole family. B1616's degeneracy was checked one irreducible at a time, and the audit lane asked whether it holds
on the whole residual-fixed space.
- **The normal form.**
  - The group's image in PGL(T) is S₄: order 24, with 9, 8 and 6 elements of orders 2, 3 and 4.
  - In the basis of the normal Klein group's three axes, each of the 96 elements is c(g) S(g). Here S(g) is a signed
    permutation matrix of determinant one and c is a character. So T is the cube's rotation group twisted by c: W21's
    T = μ ⊗ 3′, made explicit.
  - L and R are quarter-turns about two perpendicular axes, with c(L) = e^{−iπ/4} and c(R) = e^{iπ/4}. RL is a 3-cycle
    with c = 1, and RRL is an edge half-turn.
- **End(T) = 1 + 2 + 3 + 3′.** The four pieces are the identity, the traceless diagonal, the off-diagonal symmetric and
  the antisymmetric matrices, and they are pairwise inequivalent, so B1615's multiplicity-one premise holds. The
  antisymmetric piece gives (0, 1, 1) wherever it is fixed, because every antisymmetric 3 × 3 matrix has spectrum
  (0, s, s).
- **B1615's family, exactly.**
  - Along RRL the off-diagonal symmetric piece's fixed matrices are M = x A + z B, with A = E₂₃ + E₃₂ and
    B = E₁₂ + E₂₁ − E₁₃ − E₃₁.
  - On them (tr X)² − 2 tr X² vanishes identically, with X = M†M. That polynomial is Heron's product
    (m₁ + m₂ + m₃)(−m₁ + m₂ + m₃)(m₁ − m₂ + m₃)(m₁ + m₂ − m₃).
  - The masses are |x| and (s ∓ |x|)/2, with s = √(|x|² + 8|z|²). With r = |x|/s they are proportional to
    (r, (1 − r)/2, (1 + r)/2).
  - So m₁ + m₂ = m₃ on every member, and m₁/m₃ covers [0, ½] exactly, reaching ½ at r = 1/3.
- **Each residual's whole fixed space, all pieces at once.**
  - **Dirac.** Along each residual the pieces' fixed spaces add up to the commutant: dimension 3 for L, R and RL, and 5
    for RRL. The commutant holds every matrix diagonal in the residual's eigenbasis.
    - So the rigid spectra and the family hold for one Higgs irreducible at a time.
    - With Higgs fields in several irreducibles aligned with one residual, the three masses are free.
    - Either way, no value is fixed.
  - **Majorana.**
    - Along RL the whole fixed space is two-dimensional, and det(X − λ) = (λ − |t₀ − t₁|²)² (λ − |t₀ + 2t₁|²). Every
      member has a degenerate pair.
    - Along L and R it is one-dimensional, with masses (0, √2|t|, √2|t|).
    - Along RRL nothing is fixed.
    - So B1616's statement holds on the whole residual-fixed space, not only piece by piece.

**Status of the addendum.** EXACT (post hoc; a verification, not blind). 0 of 19.

**Scope, added after the independent review (2026-10-08).**
- Every statement above is for the residual ⟨g⟩ generated by the single element. That is the flavon scenario, where a
  vacuum breaks the parity grading.
- If the inner automorphisms or −I are added to the residual, as at ω (W40), the answers change (the reviewer's exact
  computation):
  - the Dirac fixed dimensions become 2, 2, 1, 2;
  - the spectra become (|a|, |b|, |b|) along L, R and RRL, and (1, 1, 1) along RL;
  - Sym² T is fixed nowhere, except (1, 1, 1) along RL under ⟨g, V₄⟩.
- So the free masses and the m₁ + m₂ = m₃ family exist only in the flavon scenario. The degeneracy of every Majorana
  spectrum holds in both.

## W39. Given Λ, the masses' tensor is T ⊗ T, not T̄ ⊗ T (a READING; nothing new is computed)

**Why.** B1615 treats a Dirac mass as T̄ ⊗ T: a left-handed field in T paired with a right-handed one in T. W27's link Λ
puts the fields differently. Every left-handed state of a generation is a holomorphic zero mode, so every left-handed
Weyl field of the 27 (Q, u^c, d^c, L, e^c, ν^c) is in T. The right-handed fields are their conjugates, in T̄. Weave or
thread: the invariants are the weave's (the group of every move); an alignment along one residual is a thread's choice.

**The reading (by hand, from W38 and its exact addendum).**
- **The tensor.** A mass term pairs two left-handed fields (Q u^c H, L e^c H, L ν^c H, ν^c ν^c). Given Λ its flavour
  tensor is T ⊗ T with the Higgs's representation, never T̄ ⊗ T.
- **With E₆'s cubic and one 27 Higgs, the Yukawa matrices are symmetric.** The d-symbol is symmetric, and so is the
  bilinear of two anticommuting Weyl spinors. So the masses lie in Sym² T, which is B1616's tensor, now for every
  sector, charged and neutral.
- **The consequences, on the record's group G** (lifts in SU(2), as W21 and B1611–B1616 use them):
  - A Higgs that carries no flavour gives no mass at all, since (Sym² T)^G = 0. (Under T̄ ⊗ T it gave (1, 1, 1).)
  - A Higgs from the three generations' own 27s gives none either, since (T ⊗ T ⊗ T)^G = 0.
  - Any mass therefore needs a Higgs carrying the character c̄²: T ⊗ T = c² ⊗ (1 + 2 + 3 + 3′), with
    c(L)² = −i.
  - Along any residual, all irreducibles at once, every spectrum has an exactly degenerate pair or vanishes (W38's
    addendum). So given Λ, the residual-vacuum reading fails for the charged fermions too, not only for the neutrinos.
  - With a Higgs in the antisymmetric part as well (an E₆ 351, outside the minimal Yukawa), the whole fixed spaces of
    T ⊗ T are, by hand:
    - along RL, the circulants, with three free masses;
    - along L and R, (0, |p|, |q|): one generation massless;
    - along RRL, nothing.
- **The premise both seats share: the character c.** [Withdrawn and replaced after the independent review of
  2026-10-08; the original text is in git history at db1095858.]
  - The selection rules do not depend on how the lifts are normalised. A U(1) acting on T by a phase gives T ⊗ T charge
    2, so a neutral Higgs still gives no mass. "Sym² T gains the singlet" only renames a Higgs that carries c̄², and is
    withdrawn.
  - The foundation review found that c itself belongs to the SU(2) normalisation of the lifts. Phases can remove it on
    T, but the ratio c² between T and T̄ and the S₄ image do not move.
  - In W24's frame, 𝕎 ≅ ρ_Q ⊗ ℂ³ sits in SU(6)′ and its holonomy commutes with I₂ ⊗ SU(3), which acts on T in the
    parity basis. So there the Klein signs and every S(g) are gauge (inside F₄ × SU(2)), and only c is flavour. That
    frame also has no E₆ cubic: its matter is vector-like, (26, 2) + 2(1, 2).
  - So which parts of G are gauge and which flavour is GENESIS FK11's datum. It has to be fixed in the same frame that
    supplies the cubic.
- **Wording fixed by the same review.**
  - The Yukawas are symmetric for any number of Higgs fields in 27s or 351′s, not only for one 27.
  - ν^c ν^c cannot come from a 27; it needs a 351′.
  - Higgs fields only in 27s share one Yukawa tensor across all sectors.

**Status.** READING given Λ (W27, the owner's ruling 2); the invariants are COMPUTED (W38). 0 of 19.

**Qualified the same night (after main's S95).** W39's consequences hold for couplings that are constants, invariant
under the whole group (weight 0). That is the reading B1615 to B1617's Z3 also take. Main's next cell (B1618) takes the
Yukawas as modular forms of weight k. There the automorphy factor can supply the phase c̄². So "a Higgs without flavour
gives no mass" holds at weight 0 only. The tensor point (T ⊗ T given Λ) is not affected.

**Corrected again, 2026-10-08 (in W43's rule, before W43 ran).** One sentence of the assurance round's replacement above
went too far: "'Sym² T gains the singlet' only renames a Higgs that carries c̄², and is withdrawn".
- The selection rules do depend only on each field's total transformation. But which Higgs counts as flavourless is
  frame-relative.
- In a frame where c is gauge (a U(1) on T commuting with the holonomy):
  - the flavour group is O;
  - gauge invariance gives any Higgs that couples to T T the compensating charge;
  - an O-singlet Higgs then gives Sym² T's invariant δ, three equal masses, as the first version said.
- W43 computes that frame. There TM1 returns under T ⊗ T. Under Sym² T no trimaximal family appears in either frame.
- So in the frames on record, "a Higgs without flavour gives no mass" holds in the record's frame and in W24's, and
  fails where c is gauge.

## W40. Main's B1617 verified: the weave at τ = ω (`the_weave_at_omega_verified.py`)

**Why.** Main's S95 reports B1617 (given the owner's tagged postulate τ = ω): NEGATIVE as sealed. This seat promised in
§38 to verify it with its own construction after the read-out. A VERIFICATION, not blind: the read-out was read first
(main @ 5658257a).

**What was done.** The residual symmetry at ω was built from W21's construction, with every lift in 2O, and restricted
to T (as in W35 and W38). Its generators:
- U: a ↦ b, b ↦ a⁻¹b (main's "L⁻¹ then R");
- the inner automorphisms (conjugation by a and by b);
- the sign −I.

**The result (COMPUTED; every check holds).**
- U's H₁ matrix [[0, −1], [1, 1]] has order 6 and fixes ω, under τ ↦ (aτ + b)/(cτ + d) and under the inverse matrix.
- The residual group has order 48 on T, and T is irreducible under it (commutant 1). So B1617's Z2 fails, as main
  found.
- In W38's normal form:
  - the inner automorphisms act as diagonal signs: the Klein group, the parity grading;
  - U acts as i times a signed 3-cycle of the parity axes;
  - −I acts as ±i times a parity sign.
  - All of them lie in the L, R group of order 96.
- U has order 12 on T, with eigen-turns ¼, 7/12 and 11/12 for one lift (shifted by ½ for the other).
- Invariants under the residual group:
  - T̄ ⊗ T has one, so three equal masses on B1615's tensor;
  - T ⊗ T and Sym² T have none, so no mass at ω at weight 0 on W39's tensor given Λ.
- Disclosed: the first run wrote three booleans as strings. The serialisation was fixed and the script rerun; the
  values are identical.

**What it shows.**
- B1617 stands on this seat's construction. The inner automorphisms fix every τ, so the parity grading is a symmetry at
  every τ, and at ω it joins U's 3-cycle into an A₄-type group that keeps T irreducible.
- This is the case §38 point 5 named: the Klein group together with a 3-cycle.

**Status.** VERIFIED (not blind): main's WEAVE result, reproduced, given τ = ω. 0 of 19.

**Added after the independent review (2026-10-08).**
- **The period rule.** On W21's period ratio a move acts by τ ↦ (δτ + β)/(γτ + α) (CONVENTIONS.md §3). Under it U fixes
  ω + 1, the same torus, and the move fixing ω is L U L⁻¹, with matrix [[1, −1], [1, 0]]. The script now computes the
  residual group with L U L⁻¹ as well, and gets the same order (48), irreducibility and eigen-turns, as conjugation
  requires.
- **The residual convention.** This section builds the residual from U together with the inner automorphisms and −I,
  which fix every τ. W38 and main's B1612 to B1616 build a thread's residual from the single element alone. The two are
  different scenarios, not one framework; see the assurance round below.

## W41. The weight of the weave's zero modes (`the_zero_modes_weight.py`; `W41_RULE.md`)

**Why.** Main's S95 asked for "the weights the weave's zero modes carry". The rule (`W41_RULE.md`, 4a1d580f) was
committed before the code. It also withdrew one line of relay §40 before any run: at ω, U's action on the holomorphic
modes is its topological action on H^{1,0} = T (W40's eigen-turns), with the automorphy factor already inside.
Weave-type: the quantity is the modes' transformation under all of SL(2, ℤ) at once.

**Disclosed.** A first launch used mpmath's nome-based theta functions. They take the principal q^{1/4}, which
misplaces a fourth root of unity once |Re τ| > 1 (or |Re 2τ| > 1 for the numerators). It was stopped before it wrote
any output. The thetas were rewritten as series in τ, with a control against mpmath at the base point (agreement
6.7 × 10⁻²²), and the run that counts was launched once.

**The result (COMPUTED; every check holds).**
- **K1, the weight by the norm (convention-free).** g(τ) = N(τ)/(Im τ)^{3/4}, where N is the mode's L² norm (W21's
  Hodge–Riemann form).
  - It is invariant under T, S, U, the record's L and R, and the matrix products RL and LRR, at τ₀ = 0.23 + 1.07i and
    τ₁ = −0.41 + 0.83i.
  - The largest relative change is 2.7 × 10⁻¹¹, at the most stretched image, LRR τ₀ with Im = 0.159. Every other change
    is at most 1.8 × 10⁻¹⁴.
  - The controls fail as predicted: exponent ¼ by 0.086 and exponent 1 by 0.046 (S at τ₀).
- **K2.** The numerator pair (θ₃, θ₂)(z | 2τ) has weight ½ and index ¼, with a constant unitary W(γ). W is fitted at
  two z and holds at three more and at τ₁ to 10⁻¹⁵:
  - W(T) = diag(1, i);
  - W(S) = e^{−iπ/4}/√2 · [[1, 1], [1, −1]];
  - W(U) = ½ [[1 − i, 1 + i], [1 − i, −1 − i]].
- **K3.** θ₁ carries the multiplier ε₁(T) = e^{iπ/4}, ε₁(S) = e^{−3iπ/4} and ε₁(U) = −i: eighth roots of unity, constant.
- **K4.** So f = θ₃(z | 2τ)/√θ₁(z | τ) has weight ¼ and index 0, and the exponentials cancel, as a flat section's
  must. The one-form F = f dz has weight −¾, and the normalised field's Kähler weight is ¾. For example,
  M_f(U) = (1/√2)[[1, i], [1, −i]].

**What it shows.** The weave's zero modes are a vector-valued modular form of weight −¾. The moves act by the
automorphy factor times ε ⊗ c ⊗ S (W38's normal form). At the fixed point ω the total action is W40's, with nothing
added. This is the input main asked for. B1618 sweeps every phase, so its verdict does not wait on it.

**Status.** COMPUTED (the rule first; one run after a disclosed stopped launch). 0 of 19.

**Added after the independent review (2026-10-08).**
- **Confirmed** with a different quadrature (a Gauss-reduced parallelogram, Duffy triangles, tanh-sinh): the fitted
  exponent is 0.7500000000000, with changes of at most 7 × 10⁻¹⁵ down to Im γτ = 0.0022.
  - So the "largest change" of 2.7 × 10⁻¹¹ reported above is the old quadrature's error, not a deviation of g.
  - W is the Weil representation, ε₁ is η³'s multiplier, and W(S)⁴ = −1, so W lives on Mp₂(ℤ). The double cover
    suffices.
  - In closed form, (cτ + d)^{−3/4} M_f = (η(γτ)/η(τ))^{−3/2} W.
- **A bug in W21's norm routine.** `l2_norm` integrated on the skewed (1, τ) parallelogram, so its error grows at small
  Im τ: 5 × 10⁻⁷ at 0.049, and 1.7 × 10⁻³ at 0.014.
  - W41's points stayed at Im τ ≥ 0.159, where the error is 2.7 × 10⁻¹¹, so no result changes.
  - The routine now integrates on a reduced basis of the same lattice, and restores the caller's mpmath precision.
- **Two qualifications.**
  - At ω the η-factor is exactly 1, so the total action is W(U), and W(U)³ = −i gives W40's {¼, 7/12, 11/12}. But
    continuing √θ₁ along the other arc gives −W(U), the set shifted by ½. So the phase at ω is a branch convention, the
    two lifts; W41 derives neither.
  - "Weight −¾" is the one-form's pullback factor, the same statement as "f has weight ¼". A field multiplying F carries
    (cτ + d)^{+3/4}, so any coupling built on F (B1618) must say which sign it means. The two components of F are one
    bundle section, not two modes.

## The assurance round of 2026-10-08 (the owner: "are we sure ... how can we make sure sure?")

**Why.** The owner asked whether the record's mathematics, questions, angle and scripts can be trusted, and how to make
sure. The owner approved a plan: a green baseline, a conventions registry, mutation tests, and independent adversarial
review.

**What was done.**
- **A conventions registry** (`CONVENTIONS.md`; `tests/test_weave_conventions.py`) pins every convention the
  dossier's scripts use. It found two things.
  - The dossier reads word strings two ways: `word` against `word_aut`, reversed. Nothing used so far changes.
  - Through the foundation review: the period rule. The registry's own first version of §3 was wrong, and is
    corrected.
- **Mutation tests.** Ten plausible bugs were injected into a separate worktree.
  - Rerunning and diffing the outputs caught all ten. The result tests caught five, because they read stored outputs.
  - So `tests/test_weave_regeneration.py` now reruns the fast scripts against their stored outputs, and probes W41.
- **Four independent adversarial reviews.** Each was a fresh agent with no shared context, given one claim and its
  code and told to break it. They are of the same kind as this seat, so independent in context, not in kind.
  - **The foundation** (W21's construction, rebuilt in exact Q(ζ₈) arithmetic before reading the code): all six claims
    confirmed.
    - G ≅ A₄ ⋊ ℤ/8, and its image in PGL(T) is S₄.
    - T ≇ T̄, with Q = +I on T and −I on T̄ exactly.
    - The character values, the c·S normal form, and the inner automorphisms as the parity signs all hold.
    - It found the period rule, and that c belongs to the SU(2) normalisation of the lifts.
  - **The masses at ω** (W38, W40, exact): all six claims confirmed. It found the residual convention, below, and seven
    script issues, now fixed with values identical.
  - **The weight** (W41, by an independent quadrature): four of five claims confirmed. The fifth, the phase at ω, is a
    branch convention. It found the norm routine's accuracy bug, now fixed.
  - **The readings** (relay §38–§41, W39, W41): no false theorem. Several conclusions ran past what was shown; they are
    corrected below and in relay §42.
- **The full suite.** Its failures all come from the environment, this branch's data, or the reviewers' temporary
  worktrees. None comes from this session's changes.
  - Data files main tracks and this branch does not: B1062, B1063, B1137, B646.
  - An unfetched remote branch: B1035.
  - The container's library versions: numpy 2.4.6 for B511; SnapPy 3.3.2's lift sign for B565; a census count for
    B616.
  - A mid-run untracked file: B1238.
  - Two gates that scan gitignored worktrees.
  - **The final tally** (the capped full run, then the unreached tests by file):
    - every test but four ran;
    - twelve distinct failures, none from this session's changes. The eleven above, plus B1282, which fails under
      four-way parallel load and passes alone in 37 s;
    - the four that never finished, each running past the 55-minute caps: B1350's order-six integrability test, B1278's
      y9 test, and two B1279 tests.
  - **Test hygiene for main.** Running the suite rewrites tracked outputs: a runtime field in B1301, longer digit
    strings in B1350, a table in B1374, and two new data files in B1374 and B1375. These were restored, not committed.
    The suite also needs a slow marker for its longest tests.

**The findings that change the record.**
1. **The residual convention (both seats).** The thread arcs (main's B1612 to B1616; W35, W38) take a residual to be
   ⟨g⟩. The ω arcs (B1617, B1618; W40) add the inner automorphisms and −I, because these fix every τ. These are two
   scenarios, not one framework.
   - **The flavon scenario:** a vacuum breaks the parity grading. TM1, and with it falsifier P10, live only here.
   - **The modular scenario:** nothing breaks the grading. Masses are degenerate at ω, and mixing is trivial while the
     grading holds.
   - Which holds depends on whether the vacuum breaks the grading. In the frames on record the grading is gauge, so
     that is GENESIS FK11's question.
2. **The period rule.** The move fixing ω is L U L⁻¹, not U. Group-level results are unchanged; τ-dependent evaluations
   at ω must use the period-rule stabiliser.
3. **The frame premise.** In W24's frame the Klein signs and every S(g) are gauge, only c is flavour, and there is no E₆
   cubic. Every flavour analysis since B1611 presupposes a frame the record has not fixed.
4. **This seat's readings, corrected** (relay §42):
   - §38 point 4: no thread-weighted measure charges a point of ℍ, though mass can escape to the cusp. Selecting τ needs
     a further functional, and the threads can supply one once a kernel is stated: V_s = Σ over trace-3 threads of
     cosh d(τ, γτ)^{−s} peaks at ω for s ≤ 8 and at i for s ≥ 9. Bowen's theorem as cited needs a compact surface.
   - §41: given Λ and couplings in τ alone, nontrivial mixing needs charged-lepton and neutrino vacua that share no
     Klein subgroup. A Majorana off-diagonal pair is pseudo-Dirac, a maximal angle rather than a permutation.
   - Three phrases are withdrawn:
     - "most likely a dynamics", which weighed no explicit breaking by end data;
     - "exactly symmetric at every τ" (a given τ keeps only V₄ × ⟨−I⟩);
     - "short threads pull τ toward i", which depends on the kernel and is a thread argument.
   - "The − threads and P add symmetry, so they give no values" is withdrawn. −I adds nothing; P fixes whole geodesics
     and forces δ ∈ {0, π}. Added symmetry can force discrete values.
   - W39's premise c is replaced (see W39).

**What it says.** The exact group-theoretic results survived three independent exact re-derivations. The errors were
in conventions, and in readings that ran past their computations. The checks that caught them were other agents: the
reviewers, and earlier the audit lane, not the author.

**Status.** ASSURANCE (post hoc; reviews and fixes recorded). 0 of 19.

## W42. Main's B1620 verified, and the threads' own zero modes (`the_breaking_verified.py`; `W42_RULE.md`)

**Why.**
- Main's B1620 (S98) counts the breaking the weave allows on all 68 subgroups of its group, under three mass tensors.
  Main's write-up for outside review counts all 19 numbers as free on its strength.
- Main asked this seat two things (relay THE_BREAKING_THE_WEAVE_ALLOWS, §3):
  1. verify the counts with the normal form;
  2. say whether the zero modes have a coupling that reads the word and not only τ.
- The rule (`W42_RULE.md`, 60f790748) was committed before the code, with every prediction derived by hand.
- **Part A is a VERIFICATION, not blind.** B1620's findings and its definition of a viable sector were read first. Its
  code was not run and its group was not used.

**Part A: what was done.**
- The group on T was built from W21's construction (W38), put in W38's normal form, and encoded exactly as pairs
  (k mod 24, S).
- Every subgroup was enumerated and sorted into conjugacy classes.
- Each subgroup's invariant matrices under each tensor were found exactly, as the orbits of the monomial action.
- A generic member was tested exactly in ℤ[ζ₂₄]: det M ≠ 0, and the discriminant of M M†'s characteristic polynomial
  ≠ 0, at random Gaussian-integer points.
  - One passing point proves a sector viable.
  - Three failing points bound the chance of a missed viable sector below 10⁻¹⁵.
- The second route was the criterion derived by hand. K came from W40's construction.

**Part A: the result (COMPUTED, exact; every cell as predicted).**
- **The group, in closed form.** G = {z S : S one of the cube's 24 rotations, z⁸ = 1, z⁴ = sgn S}. Here sgn is the
  sign of S's permutation of the three axes. The 96 elements built from W21 are exactly these.
- **The lattice: 68 subgroups in 26 classes.**
  - 57 are abelian, in 20 classes. Their orders 1, 2, 3, 4, 6, 8, 12 and 16 occur 1, 7, 4, 11, 4, 19, 4 and 7 times.
  - 11 are not, in 6 classes:
    - μ × A₄ for μ = 1, μ₂, μ₄;
    - four of order 24 over the S₃'s;
    - three of order 32 over the D₄'s;
    - G.
- **Viable under B1620's definition, and why.**
  - **T̄ ⊗ T: exactly the abelian subgroups, 57** (orders 1 to 16; 20 classes). The scalar c cancels.
  - **T ⊗ T: exactly the abelian subgroups on which T's character is real, 24** (orders 1, 2, 3, 4, 6 and 8;
    10 classes). These are the 16 subgroups of E below, and the 3-cycles' groups ⟨t⟩ and ⟨−t⟩.
  - **Sym² T: exactly the subgroups of E, 16** (orders 1, 2, 4 and 8; 8 classes). E = {±1} × V₄ is the group of the
    8 diagonal sign matrices in the parity basis.
  - The exact route and the criterion agree on all 204 sectors. Every viable sector passed at all three points, and
    every other sector at none.
- **No order-3 residual under Sym² T.** The 8 elements of order 3 are the 3-cycles, all with c = 1.
  - Each fixes a two-dimensional space of symmetric matrices: diag(a) ⊕ [[0, b], [b, 0]] in its eigenbasis, with
    spectrum (|a|, |b|, |b|).
  - No viable subgroup under Sym² T has order divisible by 3.
- **K.**
  - The inner automorphisms act as the parity signs. Their c = 1 lifts generate K = V₄, of order 4; all four lifts
    generate E, of order 8.
  - 10 subgroups contain K: orders 4, 8, 12, 16, 24, 32 (three), 48 and 96, as G/K ≅ ℤ₃ ⋊ ℤ₈ requires.
  - The viable ones have orders 4, 8 and 16 under T̄ ⊗ T, and 4 and 8 under the other two.
  - Every invariant matrix of each of them is diagonal in the parity basis, so every mixing pattern between two of them
    is a permutation.

**Part A: what it shows.**
- B1620's counts stand on this seat's construction, and all of them follow from one closed form.
- **Under Sym² T a three-mass residual is a group of parity signs.** Every rotation of the cube is broken.
- **Under T ⊗ T a residual keeps parity signs or a 3-cycle with c = ±1.** No edge half-turn or quarter-turn is viable,
  since each carries c with c² = ±i. W43 follows that up.

**Part B: the census (COMPUTED, exact; every cell as predicted).**
- **The census.**
  - It takes every thread to length 12: the 745 Lyndon words in L and R, each thread once, with no covers.
  - For each thread it takes both extensions ±g of the record's lifts.
  - By the Wang sequence (H⁰(F; 𝕎) = 0), the T part of a thread's own H¹ is the fixed space of its monodromy on T.
- **The monodromy.** On every thread it is c(w) S(w), with c(w) = e^{iπ(r − ℓ)/4} for r R's and ℓ L's. The exact
  product and the float route agree on every thread.
- **Zero modes exist exactly when r ≡ ℓ (mod 4).** That holds for 237 of the 745 threads.
  - That condition is c(w)² = i^{r − ℓ} = 1.
  - Its square is the length parity c⁴ = (−1)^{r + ℓ} = sgn S(w). So odd-length threads never have zero modes.
- **Their type.** The extension with εc = 1 gives the axis of S(w):
  - a parity line, when S is a face half-turn (72 threads);
  - a body diagonal, when S is a 3-cycle (144 threads);
  - all of T, when S = 1 (21 threads).

  The other extension gives the plane of two parity lines (for the 72), and nothing otherwise.
- **The census claim holds.**
  - Every zero-mode space of every thread is either spanned by parity lines or is a body diagonal (±1, ±1, ±1)/√3.
  - Its type is the same for every rotation of the word.
- **Under a general extension** (independent phases on the three parity summands along the circle), a zero-mode line
  has equal moduli on one cycle of S's axis permutation. That gives:
  - parity lines;
  - bimaximal lines (½, ½, 0) for quarter-turns and edge half-turns;
  - trimaximal lines for 3-cycles.
- **Main's B1621 tick.** For the thread RL (c = 1, a 3-cycle), (1 + g + g²)/3 is the projector onto its zero modes, the
  body diagonal (1, −1, 1)/√3. Every entry has modulus ⅓. That is B1621's T2 matrix.

**Part B: what it shows (the answer to main's ask 2).**
- **Yes: a thread's own H¹ is a coupling-free reading of its word.** It is the fixed space of the thread's monodromy.
  - It reads the word through c(w)² = i^{r − ℓ}, which decides whether the thread has zero modes. The length parity is
    that number's square.
  - It reads it through S(w) as well, which sets their direction.
- **Under the record's extension the threads break the parity grading only along a body diagonal.** That is the
  democratic direction, B1621's tick line, and it is the only grading-breaking shape the threads supply.
  - Bimaximal or phased trimaximal lines need extra phases on the circle, which the principle does not fix.
- **Each row is a thread object.** Which thread a sector reads is a choice, so a word-reading coupling is a thread
  result, not the weave's. Read jointly, the weave is invariant under the whole group, and so reads only τ and the
  grading (B1620's K cell).
- So the zero modes' language reproduces B1621's single grading-breaking shape for every thread at once, adds no other,
  and fixes no number.

**Status.** Part A VERIFIED (not blind): main's WEAVE counts reproduced exactly. Part B COMPUTED: a census of every
thread to length 12, each row a thread result. 0 of 19.

## W43. Which trimaximal family each tensor allows, in the record's frame and where c is gauge (`the_trimaximal_families.py`; `W43_RULE.md`)

**Why.**
- B1620's §3 and its relay title say TM1 (main's P10) is allowed under T̄ ⊗ T and T ⊗ T. W42 found that no odd
  rotation is viable under T ⊗ T, and TM1's fixed column needs one.
- B1620's own stored fits were read before the rule (copied verbatim to `received/`, sha256 as in its
  ARTIFACT_HASHES). They show its T ⊗ T families are TM2's.
- Main's relay also says: "In a frame with a U(1) on T, Sym² T gains invariants and the TM1 question reopens."
- The rule (`W43_RULE.md`, 250c362f0) was committed before the code. It states that the assurance round's withdrawal of
  W39's first premise went too far (see the note in W39).

**What was done.**
- **Two frames**, every subgroup of each taken as a residual, none chosen:
  - the record's frame, where every element c(g) S(g) acts as flavour (B1620's);
  - the frame where c is gauge, where the flavour group is O acting by S, with the ±1 that a charged Higgs leaves. That
    is B₃ = {±1} × O, the 48 signed permutation matrices.
- **For every ordered pair of viable residuals** (W42's exact viability), the fixed columns of the mixing |U|² were
  found at four sampled members, and the family dimension was taken by B1620's rank rule.
  - TM1's column is (⅔, ⅙, ⅙); TM2's is (⅓, ⅓, ⅓).
  - "Allowed" means a fixed column with family dimension 2.
- B1620's stored PMNS families below four dimensions were classified the same way, as a transcription.
- Every 3-cycle was tested with every twist in μ₂₄ under Sym² T.

**The result (COMPUTED; every cell as predicted).**
- **The record's frame.**

  | tensor | viable | TM1 | TM2 |
  |---|---|---|---|
  | T̄ ⊗ T | 57 | allowed: 36 pairs of dimension 2, orders (3, 8), (6, 8), (12, 8) | allowed: 179 pairs |
  | T ⊗ T | 24 | **no pair has a TM1 column at all (0 of 576)** | allowed: 72 pairs, orders (3, 2), (3, 4), (6, 2), (6, 4) |
  | Sym² T | 16 | none | none |

- **B1620's stored fits, transcribed.**
  - Under T ⊗ T its two PMNS families below four dimensions, both of orders (3, 2), carry TM2's column.
  - Under T̄ ⊗ T, two carry TM2's column and six carry TM1's (orders (3, 8) and (6, 8)).
- **The frame where c is gauge.**
  - B₃ has 98 subgroups, 66 of them abelian.
  - The viable residuals number 66 under T̄ ⊗ T, 66 under T ⊗ T (every element is real) and 49 under Sym² T (the
    subgroups whose every element squares to 1).
  - O's only invariant in Sym² T is the identity.
  - TM1 and TM2 are each allowed under T̄ ⊗ T and under T ⊗ T, by 72 pairs each, of orders (3, 2), (3, 4), (6, 2) and
    (6, 4). Neither is allowed under Sym² T.
- **No twist rescues a 3-cycle.** All 192 cases (8 rotations of order 3 × 24 twists) are non-viable under Sym² T, with
  fixed dimensions 0 or 2.
- **Post hoc** (`the_trimaximal_families_posthoc.py`; no cell depends on it).
  - The T̄ ⊗ T TM2 tally counted one pair at dimension 1 and one at 3. A fixed column allows at most 2.
  - Recomputed at 8 fresh points and three steps, they are 0 and 2.
  - The run's estimator takes the maximum over three points, so a point near a degeneracy can add a spurious rank.
    B1620's estimator is the same.

**What it shows.**
- **B1620's "TM1 allowed under T ⊗ T" does not hold in its own frame.** Under T ⊗ T the trimaximal family is TM2.
  - Every edge half-turn carries c with c² = ±i, so no residual containing one survives T ⊗ T.
  - TM1's column (⅔, ⅙, ⅙) is an edge half-turn's axis against a 3-cycle's eigenbasis.
  - B1620's own fits agree. Its TM1 statement holds for T̄ ⊗ T alone.
- **Given Λ, P10's TM1 needs both a frame and a Higgs.**
  - With E₆'s cubic and Higgs fields only in 27s (Sym² T), no residual pair gives TM1 or TM2 in either frame. Every
    trimaximal column needs a 3-cycle residual, and no 3-cycle survives Sym² T under any twist.
  - With an antisymmetric Yukawa (T ⊗ T, an E₆ 351), TM1 needs the frame where c is gauge. In the record's frame it is
    TM2.
  - Under B1615's T̄ ⊗ T, which is not Λ's tensor, TM1 holds in both frames.
  - So P10 tests Λ together with a frame (GENESIS FK11's datum) and a Higgs content.
- **Main's frame clause, graded.**
  - "Sym² T gains invariants" is right: where c is gauge, an O-singlet Higgs gives δ, three equal masses.
  - "The TM1 question reopens" holds under T ⊗ T, not under Sym² T.
- **What is not covered.**
  - Neither data fits nor CKM tallies were repeated in the frame where c is gauge.
  - Twisted residuals from Higgs fields in other representations of O are not covered, except the 3-cycles' twists.

**Status.** COMPUTED (the rule first; one run). It corrects a label in main's B1620 (TM1 under T ⊗ T) and grades main's
frame clause. 0 of 19.

## W44. The free-number count in every frame on record, with a strict fit predicate (`the_free_numbers_by_frame.py`; `W44_RULE.md`)

**Why.**
- "The weave's symmetry reduces none of the 13" is load-bearing in main's write-up for outside review. It was
  established in one frame, where all of G acts as flavour.
- W43 showed that the trimaximal family depends on the frame, and the frame is open (GENESIS FK11).
- The audit lane questioned B1620's fits: its PMNS score accepts an excursion of up to one half-width outside a range.
- The rule (`W44_RULE.md`, 72e481487) was committed before the code.
- The data are B1612's transcription, copied verbatim to `received/B1612_data.json` with the sha256 in B1612's
  ARTIFACT_HASHES. B1620's findings, scripts and stored fits were read first.

**What was done.**
- **Two frames:**
  - F_all, where every element c(g) S(g) is flavour (B1620's);
  - F_c, where c is gauge and the residuals are the subgroups of B₃ = {±1} × O.
- **The pairs.** Every ordered pair of viable residuals, one representative per orbit of simultaneous conjugation. That
  is 538, 120 and 80 orbits in F_all, and 632, 632 and 362 in F_c.
- **The block sums** tr(P_a P_b), exact from the residuals' isotypic projectors, and B1620's necessary block test.
- **The family dimension:** the most common rank over five points.
- **Fits** for every orbit below dimension 4 that passes a block test, with the strict predicate: every |U_ij| inside
  NuFIT's 3σ range to 10⁻⁶, or every |V_ij| within 3σ of PDG. Every witness is kept.
- **At dimension 4,** a witness in the standard parametrisation. The pair of trivial residuals realises it.

**The result (COMPUTED; D1 and D3 as predicted; D2 failed in one cell).**

| frame | tensor | viable | PMNS: smallest family with a witness | CKM: smallest family with a witness |
|---|---|---|---|---|
| F_all | T̄ ⊗ T | 57 | 2 (TM1 and TM2) | 4 |
| F_all | T ⊗ T | 24 | 2 (TM2) | 4 |
| F_all | Sym² T | 16 | 4 | 4 |
| F_c | T̄ ⊗ T | 66 | 2 (TM1 and TM2) | 4 |
| F_c | T ⊗ T | 66 | 2 (TM1 and TM2) | 4 |
| F_c | Sym² T | 49 | **3** (predicted 4) | 4 |

- **The CKM needs dimension 4 everywhere.** In both frames and under every tensor, every orbit below dimension 4 fails
  the necessary block test, so the lower bound is rigorous. A witness exists at dimension 4 (largest pull 0.006).
- **Below each PMNS minimum, every orbit fails the block test, with one exception.** Under Sym² T in F_c,
  two-dimensional families pass the test, but no witness was found.
- **D2 failed in that cell.** Under Sym² T in F_c, three-dimensional families reach the PMNS data.
  - Each fixes one entry: |U_μ3| or |U_τ3| = 1/√2, or one of |U_μ1|, |U_μ2|, |U_τ1| = ½.
  - These are the overlaps of an edge half-turn's axis with a parity line or with another edge axis.
  - Edge half-turns survive Sym² T only in this frame. In F_all they carry c with c² = ±i.
  - |U_μ3| = 1/√2 means sin²θ₂₃ = 1/(2 cos²θ₁₃) ≈ 0.511. Its mirror |U_τ3| = 1/√2 gives 0.489.
- **The two-dimensional families there fix a whole row at (½, ½, 1/√2).** Every start converges to |U_e1| = 0.7998
  and |U_e3| = 0.1556, which is 0.0012 outside NuFIT's 3σ ranges (0.801 and 0.155). They are not found, not proved
  unreachable.
- **D3, B1620's fits regraded strictly.**
  - The TM-type families, which B1620 scored 0, are reached.
  - B1620's four (8, 8) two-dimensional families (score 0.0707, counted as reached) are outside. Their row is the same
    (½, ½, 1/√2), 0.0012 beyond the ranges, as the audit lane suspected.
  - B1620's (2, 8) three-dimensional families (score 0.3627, also counted as reached) have strict witnesses.
  - The minimum of two stands.

**What it shows.**
- **The 13 are unreduced in every frame on record.**
  - The nine charged masses are free on every viable residual (W42).
  - The CKM needs a four-dimensional family in both frames; in W24's frame nothing is constrained at all.
  - So "the weave's symmetry reduces none of the 13" does not depend on the open frame.
- **The lepton sector, beyond the 19, depends on the frame and the tensor.**
  - Under T̄ ⊗ T and T ⊗ T, at most two relations: TM1 or TM2, as W43 found.
  - Under Sym² T, none in F_all and one in F_c (a fixed entry 1/√2 or ½). In W24's frame, none.
- **So the count reads:** 0 of 19 fixed by the weave's symmetry, in every frame. A residual chosen by a vacuum can add
  at most two lepton relations, and the frame and the Higgs content decide which.
- **Given Λ with Higgs fields only in 27s (Sym² T):**
  - in the record's frame there is no lepton relation;
  - where c is gauge there is one, such as a near-maximal θ₂₃.

**Status.** COMPUTED (the rule first; one run). One prediction failed and is recorded as failed. B1620's count is
confirmed and extended to both frames, and two of its fit grades are corrected. 0 of 19.

## Reading: why the flavour group is the cube's, and what a frame is (READING, by hand)

- **The parity summands are one local system.**
  - Each summand χ_p ⊗ ρ_Q of 𝕎 is isomorphic to ρ_Q as a local system on the fibre. The intertwiners are the
    quaternion units j, i and k, for χ = (−, +), (+, −) and (−, −) (checked exactly).
  - So 𝕎 ≅ ρ_Q ⊗ M, where M = ℂ³ is a multiplicity space whose basis is the three parities.
  - As a flat bundle, 𝕎's automorphism group is U(M) = U(3).
- **That gives the normal form.**
  - V = H¹(F₂; ρ_Q) ⊗ M and T = ℓ ⊗ M, where ℓ is the Hodge–Riemann-positive line of the two-dimensional
    H¹(F₂; ρ_Q).
  - A move acts on T as c(g) ⊗ S(g): c is its character on the single holomorphic mode ℓ, and S(g) is its action on M.
  - The move permutes the parity characters through SL(2, ℤ) → GL(2, 𝔽₂) ≅ S₃, and the intertwiners contribute signs.
  - The inner automorphisms contribute the parity signs V₄.
  - So S(G) = V₄ ⋊ S₃ = O, the cube's rotation group. **The flavour group is the cube's because the moves mod 2 act on
    the parities, and the parities carry signs.**
- **A frame is a subgroup of U(M).**
  - Which part of G is gauge is the question of which subgroup K ⊂ U(M) the gauge group realises, through its
    centraliser of 𝕎's holonomy.
  - The three frames on record:
    - K trivial (B1620's, all of G flavour);
    - K the centre U(1) (c gauge, W43's);
    - K ⊇ SU(3) (W24's E₈ embedding, where every S(g) is gauge).
  - The weave fixes S(G) ⊂ U(M), but not K. So GENESIS FK11's frame datum is exactly K. An object that forces the frame
    has to say which automorphisms of 𝕎 are gauge.

## W45. The triplet's index on the weave's own surface: zero for both hands, given Λ (`the_index_on_the_weaves_surface.py`; `W45_RULE.md`)

**Why.**
- GENESIS FK11's earning condition (main, B1604) asks for an even-dimensional object the weave forces, carrying a
  non-flat bundle whose index is the count.
- W19 named the object, the weave's own surface M₁,₂. W20 read it in the 27 and found three, but not chiral. Its
  erratum named the next step: a holomorphic index of the complex triplet T on the weave's orbifold.
- The rule (`W45_RULE.md`, 6a8ac3640) was committed before the code. It fixes the operator, the weight that operator
  forces, the formula and how its signs are fixed, the test that picks the convention, and a second route.
- Weave or thread: the quantity is defined on the weave's own surface, by every move at once, through T's
  representation of the whole modular group. No thread is chosen. Weave-type.

**The object (the rule's READING, by hand).**
- The four-dimensional Dirac operator on M₁,₂, twisted by 𝕎, with the fibre's odd spin structure, the only one every
  move keeps.
- Kodaira's formula gives K = π*λ³ up to the cusp, so the spinors carry weight 3/2.
- By Leray the index is a Riemann–Roch number of vector-valued modular forms, χ_k(ρ) = dim M_k(ρ) − dim S_{2−k}(ρ^∨),
  with ρ = ρ_T for one hand and ρ̄_T for the other. The sign is the hand, a convention. The magnitude is not.

**Fixes made in review, before the run (disclosed).** The run was the first and only launch.
- The search for the word u with S̃⁴ = conjugation by u tried only prefixes of the image of a, so it could miss a word
  v aᵐ with m ≠ 0, 1. It now writes the image of a as v a v⁻¹ and searches the power. The word found, a b⁻¹ a⁻¹ b,
  ends in b, so the old search would have found it too.
- E1's determinant check listed the determinants of the group's diagonal elements with c = 1. Those are rotations, so
  the check could not fail. It now builds the inner automorphisms' lifts by W40's construction, as W42's A4 does, and
  reads u through them for every choice of lift.
- Two checks could pass with nothing kept; they now require something kept. The points on the arc went from 70 to 120.

**The result (COMPUTED; E1 to E4 as predicted).**
- **E1, the structure (exact, in W42's normal form).**
  - S̃ = L ∘ R⁻¹ ∘ L has H₁ matrix [[0, 1], [−1, 0]]. S̃⁴ is conjugation by u = a b⁻¹ a⁻¹ b, a commutator.
  - On T the lifted S̃⁴ is −I for all four choices of lift signs, and S̃⁸ is 1.
  - The inner automorphisms' lifts are ±diag(1, −1, −1) for a and ±diag(−1, −1, 1) for b: signs times the parity
    signs, which have determinant 1.
  - Read through those lifts, u gives I for every choice (determinant 1), where S̃⁴ gives −I (determinant −1).
  - So the relation "S̃⁴ is conjugation by u" fails on T by the central sign, whatever lifts are chosen. The relation
    holds in Aut⁺(F₂), the orbifold fundamental group of M₁,₂. So T is a representation of the metaplectic double
    cover, not a local system on M₁,₂ itself, and only half-integral weights carry it.
- **E2, the formula's calibration (exact).** 1, 0 and 2 for the trivial representation at weights 0, 2 and 12; 1 for η
  at weight ½; 1 for W41's Weil representation at weight ½.
- **E3, the four identifications** (σ₁ = L, σ₂ = R⁻¹, S̃ = σ₁σ₂σ₁):

| S ↔, T ↔ | S² = (ST)³ | allowed weights | χ_k there | kept |
|---|---|---|---|---|
| S̃, L | no | 3/2, 7/2, 11/2, 15/2 | −¼, ¾, ¾, 7/4 | no |
| S̃, L⁻¹ (ρ_T) | yes | 3/2, 7/2, 11/2, 15/2 | 0, 1, 1, 2 | yes |
| S̃⁻¹, L (ρ̄_T) | yes | ½, 5/2, 9/2, 13/2 | 0, 0, 1, 1 | yes |
| S̃⁻¹, L⁻¹ | no | ½, 5/2, 9/2, 13/2 | ¼, ¼, 5/4, 5/4 | no |

- The two identifications the braid relation allows are exactly the two that are integral. ρ_T is the left action the
  record's right action gives, and ρ̄_T is its conjugate.
- tr ρ(ST) = 0 in all four, as predicted by hand, and tr ρ(S) = e^{±iπ/4}. The exponents of ρ(T) are ⅛, ⅜, ⅞ for ρ_T
  and ⅛, ⅝, ⅞ for ρ̄_T.
- **E4, the dimensions by the second route.** The q-expansions run to 24 terms in each component, and
  f(−1/τ) = τᵏ ρ(S) f(τ) is imposed at 120 points of the unit arc between ω and ω + 1. Null singular values are
  counted below 10⁻⁹ of the largest.

| space | dimension | smallest non-null singular value | largest null one |
|---|---|---|---|
| η: M_½ | 1 | 5.1 × 10⁻⁷ | 1.2 × 10⁻¹⁶ |
| Weil: M_½ | 1 | 2.2 × 10⁻⁷ | 1.8 × 10⁻¹⁶ |
| ρ_T: M_{3/2} | 0 | 1.5 × 10⁻⁷ | none |
| ρ_T's dual: S_½ | 0 | 1.9 × 10⁻⁷ | none |
| ρ_T: M_{7/2} | 1 | 1.5 × 10⁻⁷ | 3.8 × 10⁻¹⁶ |
| ρ̄_T: M_½ | 0 | 1.9 × 10⁻⁷ | none |
| ρ̄_T's dual: S_{3/2} | 0 | 1.5 × 10⁻⁷ | none |
| ρ̄_T: M_{5/2} | 0 | 1.5 × 10⁻⁷ | none |
| ρ̄_T: M_{9/2} | 1 | 1.6 × 10⁻⁷ | 2.5 × 10⁻¹⁶ |

- Every difference of dimensions equals χ, and every count has a gap of nine orders of magnitude.
- Post hoc, from the stored output: the two hands' systems agree where duality says they must. M_{3/2}(ρ_T) and S_{3/2}
  of ρ̄_T's dual have the same smallest singular value to nine digits, and so do S_½ of ρ_T's dual and M_½(ρ̄_T). So
  the kept ρ̄_T is ρ_T's dual.

**What it shows (given Λ).**
- **The index is zero for both hands at the weight the geometry forces.**
  - For ρ_T at weight 3/2, χ = 0 and both spaces are zero. There are no zero modes at all, neither chiral nor in
    vector-like pairs.
  - ρ̄_T's central character does not allow weight 3/2, so its spaces there vanish. At its nearest allowed weights, ½
    and 5/2, the index is 0 and every space is zero.
  - Below weight 7/2 neither hand has a non-zero index.
- **The weave's even-dimensional object gives no chiral three in its canonical reading:** the four-dimensional Dirac
  operator, the only spin structure the moves keep, and the canonical condition at the cusp.
- **With main's T-NO-INDEX-IN-THREE (B1604, on threads) and W20 (an Euler characteristic, not chiral), this closes the
  weave's own route to GENESIS FK11's index in that reading.** The chiral three needs end data (GENESIS FK10) or a frame
  beyond the weave's surface, as the rule's reading said.
- **One line of the rule's reading was loose.** It said three needs weight 15/2 or more. The table gives
  χ_{15/2}(ρ_T) = 2, and by the closed form below three first appears at 23/2 for ρ_T and at 25/2 for ρ̄_T. The bound
  held but was not sharp.
- **The fibre's count and the surface's index are different numbers (a READING).** On each fibre the three zero modes
  give the fibre's ±3 (W22, W28). Over the base they form the flat bundle with monodromy ρ_T, and at weight 3/2 its
  Riemann–Roch number is 0. The fibre's count does not survive to the surface's index.

**A reading (post hoc, by hand): where the index can move.**
- **The closed form.** On the allowed weights, with tr ρ(ST) = 0 and the exponents above:
  - χ_k(ρ_T) = ¼ + m/2 − (−1)^m/4 at k = 3/2 + 2m;
  - χ_k(ρ̄_T) = −¼ + m/2 + (−1)^m/4 at k = ½ + 2m.
- **Given Λ, the spin structure and the puncture's condition, the condition at the weave's one cusp is the only freedom
  left in the index.** Allowing the component with exponent λ_j a pole of order m_j there changes the index by Σ m_j.
- **One unit on every component is the cusp divisor, Δ⁻¹ at weight 12.** It adds exactly d = 3, since the formula
  gives χ_{k+12} = χ_k + d. So n units of end data on every component give 3n at the weight the geometry forces.
- **The canonical condition is n = 0.**
  - T's exponents all lie strictly between 0 and 1, so the lower and upper canonical extensions agree.
  - The other natural conditions agree with it (by hand). T's cusp monodromy has no eigenvalue 1, so the L² condition
    for the complete metric and compact support give the same spaces as the canonical extension.
  - A unit of end data is therefore none of these conditions. It is a pole at the cusp, a source placed there, and a
    choice unless the principle forces one.
  - The owner's ruling 3 keeps W28's naturality for flat counts only. This index, of the non-flat bundle λ^{3/2} ⊗ 𝒯,
    is not a flat count.
- **So on this object a chiral three is exactly one unit of end data at the cusp, and its three is the triplet's
  dimension.** Whether anything forces that unit is GENESIS FK10's question, not answered here.

**Status.** COMPUTED (the rule first; one run; fixes in review before it, disclosed). E1 to E4 held as predicted. One
line of the rule's reading was loose and is recorded with its sharp value; the end-data reading is post hoc. In its
canonical reading the weave's own surface does not earn GENESIS FK11, which stays open. 0 of 19.

## W46. Every end condition the weave keeps on its own surface: the four-dimensional index is n times the fibre's index (`the_end_conditions_on_the_weaves_surface.py`; `W46_RULE.md`)

**Why.**
- W45 read the weave's own surface with the canonical conditions at its two ends, given Λ, and found index 0 with no
  zero modes. Two ends remained to be read in full.
  - The puncture section: W22 and W28 give the six local solutions and four conditions the moves keep, with fibre
    index −3, −1, +1 and +3.
  - The cusp: W45's post-hoc reading gives units of end data there.
- The rule (`W46_RULE.md`, 253b14e96) was committed before the code. It reads all four puncture conditions and the
  cusp's uniform units, so it reads every end condition the weave keeps on its own surface.
- Weave-type: one surface, every move at once, and every condition the moves keep, none chosen.

**The object (the rule's READING, by hand).**
- A puncture condition is a subspace Λ₊ of the six local solutions L₆ that the moves keep: 0, V2, V4 or L₆ (W28 E2).
  𝕎 gets exponent −½ along the puncture section P on Λ₊, and +½ elsewhere.
- Along P the two extensions differ by Λ₊ ⊗ λ^{−1/2}. With K_Y^{1/2}|_P = λ^{3/2} that has weight 1. So the index for
  Λ₊ is W45's plus χ₁ of the moves' action on Λ₊.
- The six are a pushforward (W24's blocks_action) and T a pullback (W21's on_V), from the same lifts. So their
  monodromies are blocks_action and the inverse of on_V, with σ₁ = L, σ₂ = R⁻¹, S = S̃⁻¹ and T = L, as in W45.
- At the puncture: 0 → H⁰(all allowed) ⊗ λ⁻¹ → L₆ ⊗ λ^{−1/2} → H¹(canonical) → 0.
- n uniform units at the cusp add n times the fibre's index.

**The result (COMPUTED; H1 to H5 as predicted, under both overall lift signs).**
- **H1, the structure.**
  - The braid relation holds on T and on the six for exactly the same two of the four sign pairs: the record's lifts,
    and both negated.
  - ρ₆(S)² = −I, and S̃⁴ is I on the six, while on T it is −I.
  - V2 and V4 are invariant. tr ρ(S) = 0 on both, and tr ρ(ST) = 1 on V2 and −1 on V4.
  - The exponents with the record's lifts:

| | T | T̄ | the six | V2 | V4 |
|---|---|---|---|---|---|
| the record's lifts | ⅛, ⅜, ⅞ | ⅛, ⅝, ⅞ | ⅛, ⅛, ⅜, ⅝, ⅞, ⅞ | ⅛, ⅞ | ⅛, ⅜, ⅝, ⅞ |
| both negated | ⅜, ⅝, ⅞ | ⅛, ⅜, ⅝ | ⅛, ⅜, ⅜, ⅝, ⅝, ⅞ | ⅜, ⅝ | ⅛, ⅜, ⅝, ⅞ |

  - Under both signs the six's exponents are the union of T's and T̄'s.
  - The central scalars fit the exact sequence. ρ(S)² e^{iπw} is i for T at w = 0, for the six at w = −½ and for T̄ at
    w = −1. So the twisted weights are forced: 3/2, 1 and ½.
  - So W45's two representations are the two extreme puncture conditions, W28's ±3, whose sign is the orientation.
    ρ_T is the canonical condition's H¹, and ρ̄_T is the all-allowed condition's H⁰.
- **H2, the formula.** χ₁(V2) = χ₁(V4) = χ₁(six) = 0, and χ_{3/2}(ρ_T) = χ_{1/2}(ρ̄_T) = 0. The calibration η² at
  weight 1 gives 1.
- **H3, the other overall sign.** That sign is the base direction's other square root, v_η¹². The braid relation holds,
  and every χ is 0 again, W45's included.
- **H4, the second route** (q-expansions, W45's method). M₁ and the dual S₁ are zero for V2, V4 and the six under both
  signs. Under the other sign W45's four spaces are zero too. η² has dimension 1, with a gap of 5.1 × 10⁻⁷ against
  1.0 × 10⁻¹⁶. Every zero count's smallest singular value lies between 1.4 × 10⁻⁷ and 3.1 × 10⁻⁷.
- **H5, the table.** The four-dimensional index for each puncture condition and n uniform units at the cusp. It is the
  same under both signs, and the L₆ row equals its H⁰ form, χ_{1/2+12n}(ρ̄_T).

| puncture condition | fibre index | n = −1 | n = 0 | n = +1 |
|---|---|---|---|---|
| 0 (canonical) | −3 | +3 | 0 | −3 |
| V2 | −1 | +1 | 0 | −1 |
| V4 | +1 | −1 | 0 | +1 |
| L₆ (all allowed) | +3 | −3 | 0 | +3 |

- Post hoc, from the stored output: the dual pairs have equal smallest singular values to nine digits. For example,
  M_{3/2}(ρ_T) and S_{3/2} of ρ̄_T's dual agree under the other sign.

**What it shows (given Λ).**
- **The four-dimensional index is n times the fibre's index** for every end condition the moves keep at the puncture
  and every uniform condition at the cusp. With the natural cusp condition, n = 0, there is no zero mode at all, for
  every puncture condition and either base spin structure.
- **So no end condition the weave keeps gives a chiral count on its own surface.**
- **The record's ±3 is the fibre's count** (W22, W28; a flat count under the natural puncture condition, the owner's
  ruling 3). It becomes a four-dimensional ±3 exactly when one unit of end data sits at the cusp.
- **So GENESIS FK11's earning condition on the weave's surface is GENESIS FK10's question at the cusp:** is one unit of
  end data forced there? Nothing in the record supplies it. Every natural cusp condition gives n = 0 (W45).
- **Why, in one line (the rule's argument, by hand, now consistent with both routes).** Every piece's exponents are at
  least ⅛, η³'s. A zero mode divided by η³ is a holomorphic form of weight at most 0 with no invariant vector, so it
  vanishes.

**A reading (post hoc, by hand, from W42's stored census): the cusp and the threads that approach it.**
- The cusp's monodromy is the move L itself. L has order 8 on T and on the six: L⁴ = −I on both (c(L)⁴ = −1 with a
  quarter-turn; the 2O lift of a quarter-turn has order 8).
- So the threads that approach the cusp, those with long runs of L, see their own zero modes repeat with period 8 in
  the run's length. W42's census shows the step: LR has a body-diagonal zero mode for +g and none for −g, and L⁵R the
  reverse, since L⁴ = −I exchanges the two extensions.
- So nothing along the runs accumulates toward a unit at the cusp. The weave's own content supplies no unit there,
  consistent with W45's natural conditions, which all give n = 0. These are thread results, read as a family; the
  claim about the cusp is a reading.

**A reading (post hoc, by hand): the count as a product, given Λ.**
- At the cusp the move L fixes one parity line and swaps the other two.
  - In the record's normal form, L's eigenlines on T are that parity line (exponent ⅞) and two complex combinations of
    the swapped pair (⅛ and ⅝).
  - So end data at the cusp that L keeps and that respects Λ's parity grading has the form (m_fixed, m_pair, m_pair).
  - The four-dimensional index then moves by m_fixed + 2m_pair, times the puncture's sign.
- **If the source at the cusp is generation-blind,** coupling to the three parity sectors alike as gauge charges do,
  then m_fixed = m_pair = n.
- **The count is then a product of three factors:**
  - three parities (W1);
  - the puncture's ±1 per parity (W22, W28), whose sign is the hand;
  - the cusp's n units.
- **So every generation-blind chiral count on the weave's surface is a multiple of three, and three is the least
  non-zero one.** One unit is exactly three chiral generations.
- **Whether any unit is forced, and which n, is GENESIS FK10's question,** kept open by the owner's ruling of
  2026-10-09.

**Status.** COMPUTED (the rule first; one run; every cell as predicted). It closes the end conditions the weave keeps on
its own surface. GENESIS FK11 stays open, and its question on this surface is GENESIS FK10's at the cusp. 0 of 19.

## W47. Is one unit of end data at the weave's cusp forced? No: nothing on the weave's surface supplies it (`the_unit_at_the_weaves_cusp.py`; `W47_RULE.md`)

**Why.**
- Main named the arc for GENESIS FK10 (S104's relay): "If you see a forcing of one unit of end data at the weave's
  cusp (FK10), that is the arc."
- W45 and W46 left exactly one freedom on the weave's surface for a chiral count: the cusp's units n, with the count
  n times the fibre's index. The owner ruled the unit open, with no postulate.
- Two kinds of candidate remained: an end condition at the cusp other than the canonical one, and a twist of the
  triplet by a line bundle on the surface.
- The rule (`W47_RULE.md`, a76e27d6d) was committed before the code. Weave-type: every flat line bundle the surface
  admits and every natural condition, none chosen.

**A fix made in review, before the run (disclosed).** The run was the first and only launch. The check of K5's formula
I = n·f + t was first written over all 24 characters. For the 18 that do not keep the forced weights the twisted field
has no sections, so its index is 0 for every n, as the rule's facts section says. The check was scoped to the six
allowed twists, with a separate check that the other 18 give 0.

**The result (COMPUTED; K1 to K5 as predicted).**
- **K1, the flat line bundles (exact).**
  - The coinvariants of H₁(F₂) under L and R vanish: the Smith invariants of [L − 1 | R − 1] are 1 and 1. So the
    inner automorphisms die in the abelianization.
  - S̃⁸ maps to 24 under σ ↦ 1. So the flat line bundles on the weave's surface are the 24 characters ε_r = v_η^r of
    the metaplectic group.
  - Exactly the six with r ≡ 0 mod 4 keep the forced weights 3/2, 1 and ½, and each of them keeps all three or none.
- **K2, the cusp exponents.** Under every allowed twist, every exponent of T, T̄, the six, V2 and V4 is an odd
  multiple of 1/24. With the record's lifts they are {3, 9, 21}/24 on T and {3, 21}/24 on V2, and a twist adds 4m/24.
  No exponent is an integer, so the natural cusp conditions (canonical, L² at any power of the weight, compact support)
  coincide.
- **K3, the twisted index at n = 0.** It is 0 everywhere except −1 at r = 4 for the conditions 0 and V4, and −1 at
  r = 20 for V2 and L₆. The L₆ row equals its H⁰ form, χ_{1/2}(ρ̄_T ⊗ ε_r), at every r. No twist gives ±3.
- **K4, the second route.** q-expansion dimensions match the formula for every allowed twist and piece.
  - The non-zero values are actual forms. At r = 4, M_{3/2}(ρ_T ⊗ ε₄) and M₁(V2 ⊗ ε₄) each have dimension 1, with gaps
    of 1.8 × 10⁻⁷ and 2.2 × 10⁻⁷ against 4.9 × 10⁻¹⁶ and 1.0 × 10⁻¹⁶.
  - At r = 20 the dual cusp spaces S_{3/2} (of T̄ ⊗ ε₂₀'s dual) and S₁ (of V2 ⊗ ε₂₀'s dual) have dimension 1.
  - Every other space is zero.
- **K5, the full table** over the four puncture conditions, the 24 characters and n ∈ {−1, 0, 1}.
  - At every allowed twist, I = n·f + t, with f the fibre index and t the twist's term.
  - |I| = 3 occurs at exactly 20 places, all at the conditions 0 or L₆ with t = 0 and n = ±1.
  - A twist that does not keep the forced weights gives 0 throughout.

**What it shows (given Λ).**
- **Nothing on the weave's surface forces the unit.**
  - Every natural cusp condition is the canonical one, because no exponent is an integer. The reason is that the
    moves' c-twist is an odd power of η's multiplier.
  - Every flat line bundle the surface admits moves the index by at most one, never by three.
- **So main's named arc returns a negative: no forcing exists inside the weave.** The only route to a chiral three on
  the weave's own surface is one unit of end data at the cusp, at a natural puncture condition.
- **That unit is a non-flat source.** On the open surface it is the trivial bundle λ¹² ≅ O extended by Δ⁻¹, which
  vanishes nowhere there and has a simple pole at the cusp.
- **GENESIS FK10 at the cusp is not answerable inside the weave,** and the owner's ruling keeps it open.
- **Post hoc: chirality without three.** The order-6 twists ε₄ and ε₂₀ give a single chiral mode, an actual form, on
  some puncture conditions. A flat twist can make the surface chiral, but only by one mode, never by three alike.

**Status.** COMPUTED (the rule first; one run; a check's scope fixed in review before it, disclosed). Every cell held as
predicted. Main's named arc returns a negative: the weave does not force the unit, and GENESIS FK10 stays open by the
owner's ruling. 0 of 19.

## Reading: an outside source for the cusp's unit (READING, by hand; the owner chose to explore one, 2026-10-09)

Nothing here is computed beyond W45's closed form. A test follows only after a rule (W48).

1. **What a source is.** On the weave's surface a source at the cusp is a meromorphic modular form g of weight w with
   trivial multiplier. Dressing the zero modes by it allows f = g·F with F holomorphic. So the dressed space for a
   piece ρ at weight k is g·M_{k−w}(ρ), and the dressed index is χ_{k−w}(ρ).
2. **Only the weight counts.** A zero of g inside the surface takes back exactly what its pole at the cusp adds, so the
   index depends on w alone.
3. **The law for the triplet.** tr ρ_T(ST) = 0, so χ_{3/2+4j}(ρ_T) = j. The count rises by one for every −4 of weight.
   One unit at the cusp is w = −12, and three needs exactly that.
4. **The unit has one form.** A modular form of weight −12 with a simple pole at the cusp and no zeros on the open
   surface is 1/Δ = 1/η²⁴, up to a constant. In conformal field theory it is the vacuum character of 24 chiral
   oscillators (c = 24) with no zero-mode lattice. The left-movers of the bosonic string in light-cone gauge are such a
   sector.
5. **The natural candidates, read by the law** (canonical puncture condition):
   - 1/Δ, 24 oscillators alone: w = −12, three;
   - E₄/Δ, one E₈ lattice and 16 oscillators: w = −8, two;
   - E₄²/Δ, the heterotic string's left-movers: w = −4, one. This holds for E₈ × E₈ and for Spin(32)/ℤ₂ alike, since
     both lattices have the theta function E₄²;
   - J = j − 744, the Monster's vacuum: w = 0, none.
6. **What it shows.**
   - Under the simplest dressing, the heterotic string gives one chiral mode, not three. That string is the record's
     natural home for E₈.
   - Only a pure c = 24 oscillator vacuum gives three.
   - A lattice that carries the gauge charges carries weight, and that weight takes back part of the unit.
7. **What it costs.**
   - **A dictionary beyond Λ:** the records' torus read as a string worldsheet at one loop. The principle does not force
     that reading (GENESIS FK11).
   - **A count, not a spectrum.** The dressed index is a mathematical count. In the heterotic spectrum the q⁻¹ term is
     the left-moving tachyon, which level matching removes, so a unit in the index is not a state in the spectrum.
   - **The simplest dressing.** A sector with gauge charge is dressed by its coset theta function, a vector-valued
     form, not by the full lattice theta. The count above treats the lattice as a scalar factor, the simplest case.
   - **Numerology risk.** 24 appears often on the record: |O| = 24, |2T| = 24, and Mp₂(ℤ)^ab = ℤ/24. An exact match of
     c/24 = 1 is not a derivation by itself.
8. **The test it suggests (W48, rule first).** The dressed index and the q-expansion dimensions for the candidate
   sources, at all four puncture conditions, so that the law and the counts above are computed, not read.

## W48. The outside source tested: one mode per eight lattice-free chiral bosons, so the heterotic string gives one (`the_outside_source_at_the_cusp.py`; `W48_RULE.md`)

**Why.** The owner chose to explore an outside source for the cusp's unit (GENESIS FK10): a reading first, then a
rule-first test. The reading above gave a law and its candidates. This arc computes them. The rule (`W48_RULE.md`,
1add8f87c) was committed before the code. It fixes the candidates by a rule: the vacuum characters of c = 24 chiral
sectors, in a lattice family Θ_L/Δ (ℓ = 0, 8, 16, 24) and an oscillator family 1/η^c (c = 8, 12, 16, 24). The object
is weave-type; whether any source applies is a dictionary question beyond the principle.

**The result (COMPUTED; S1 to S4 as predicted).**
- **S1, the weight law.** With a source of weight w and trivial multiplier, the dressed four-dimensional index at the
  conditions (0, V2, V4, L₆) is:

| w | 0 | V2 | V4 | L₆ |
|---|---|---|---|---|
| +4 | +1 | 0 | 0 | −1 |
| 0 | 0 | 0 | 0 | 0 |
| −4 | −1 | 0 | 0 | +1 |
| −8 | −2 | −1 | +1 | +2 |
| −12 | −3 | −1 | +1 | +3 |
| −24 | −6 | −2 | +2 | +6 |

  - The L₆ row equals its H⁰ form at every w.
  - The lattice family's counts at the canonical condition are (24 − ℓ)/8: 3, 2, 1, 0 for 1/Δ, E₄/Δ, E₄²/Δ (the
    heterotic left-movers, either lattice) and a Niemeier vacuum (j plus a constant).
- **S2, the oscillator family.** The canonical counts are 1, 1, 2, 3 for 1/η⁸, 1/η¹², 1/η¹⁶ and 1/η²⁴. At c = 24 the
  four conditions give −3, −1, +1, +3, W46's n = 1 row. Not predicted, and recorded: 1/η¹² gives −1, 0, +1, +2, which
  is not of the form n times the fibre index.
- **S3, the second route.** q-expansion dimensions match χ for every candidate and piece, with every gap near
  1.6 × 10⁻⁷ against 5 × 10⁻¹⁶.
  - T's dressed spaces have dimension 3, 2, 1, 0 for ℓ = 0, 8, 16, 24, at weights 27/2, 19/2, 11/2 and 3/2.
  - Every dual cusp space is zero.
- **S4, the analytic facts.** |E₄(ω)| = 1.5 × 10⁻¹⁵. E₄² = 1 + 480q + 61920q² + …, and E₈ ⊕ E₈ and D₁₆⁺ have 480
  roots each. j − 744 has one zero on the arc from ω (j = 0) to i (j = 1728).

**What it shows.**
- **One chiral mode for every eight chiral bosons that carry no lattice.** That is the count of a c = 24 source on the
  weave's surface. So three needs 24 lattice-free chiral bosons: the bosonic string's light-cone left-movers, in 26
  dimensions.
- **The heterotic string gives one.** It is the record's natural home for E₈: eight transverse bosons free, sixteen on
  the lattice. A Niemeier or Monster vacuum gives none.
- **So the outside source explored, a string vacuum as the dressing, does not supply the unit in any form natural to
  the record.** GENESIS FK10 at the cusp stays open, as the owner ruled.
- **Scope.** This is the simplest dressing: holomorphic chiral sectors, with a lattice treated as a scalar factor. It
  rests on a dictionary beyond Λ, the records' torus read as a worldsheet. A sector's own coset theta function, or a
  non-holomorphic dressing, is outside it.

**Status.** COMPUTED (the rule first; one run; every cell as predicted). The owner's exploration of an outside source,
in its string-vacuum form, returns a negative for three. 0 of 19.

## W49. The generations are a multiplicity: one zero mode three times, so an end condition keeps three or splits it (`the_generations_are_a_multiplicity.py`; `W49_RULE.md`)

**Why.**
- The owner turned to the free numbers (2026-10-09): look for a state that breaks the weave's symmetry and is forced
  by the principle, and name the obstruction and attack it.
- **The obstruction as the record states it.**
  - Main's T-TAU-ONLY-PERMUTATION: couplings in τ alone give permutation mixing, because the inner automorphisms act
    on T as the parity signs at every τ.
  - Main's §3: all 19 are free, by Schur's lemma on an irreducible group.
- This arc checks the one link in a deeper form of that obstruction which was so far only a reading: W44's
  𝕎 ≅ ρ_Q ⊗ M, carried to the triplet. The rule (`W49_RULE.md`, cd174afa7) was committed before the code.
- **Weave or thread.** The objects are the weave's local system, its triplet T and the end conditions every move
  keeps, read by every move at once. Weave-type.
- **Notation.** D = H¹(F₂; ρ_Q) is the spin doublet (W21's code calls it M). Here M = ℂ³ is the multiplicity.

**Disclosed before the run.** The script was reviewed against the rule, then run once.
- **The rule's M4 inference was too weak for V4.**
  - The rule says V2's and V4's vectors have rank 2 generically, "so neither is X ⊗ Y".
  - That holds for the two-dimensional V2, since a two-dimensional product space has only rank-one vectors.
  - It does not hold for the four-dimensional V4: ℂ² ⊗ Y, with Y a plane in M, also has rank 2 generically.
  - The script adds a support test that decides both. A subspace W is a product exactly when
    dim W = dim X_W · dim Y_W, where X_W and Y_W are the spans of its matrices' columns and rows. The prediction is
    unchanged.
- **"Both match W42's normal form" was made concrete.** The group the lifts of L and R generate on T must be W42's
  set, and it must contain the inner automorphisms' lifts.
- **Four extra read-outs (E1 to E4)** were fixed in the script before the run, with no prior.

**The result (COMPUTED; M1 to M4 as predicted; every control holds).**
- **The controls.**
  - The units (j, i and k for the parities (½, 0), (0, ½) and (½, ½)) identify the weave's local system with ρ_Q ⊗ M
    on the fibre: Ψ⁻¹ W(x) Ψ = 1 ⊗ ρ_Q(x) for x = a, b.
  - Every lift of L and R on the six local solutions is S ⊗ g, with S a signed permutation of the parities.
- **M1, one line.**
  - T meets each parity block of V in a line.
  - The intertwiners Φ_p(z) = u_p⁻¹ z send the three lines to one line ℓ of D: the 2 × 3 matrix of the images has
    singular values 1.674 and 0.
  - ℓ and its Q-orthogonal complement are each invariant under every lift of L and R.
  - Q(ℓ̂, ℓ̂) = +2, and Q = −2 on the complement. So ℓ is D's holomorphic line, and T = ℓ ⊗ M.
  - On ℓ, L's two lifts act by e^{2πi·7/8} and e^{2πi·3/8}, and R's by e^{2πi·5/8} and e^{2πi/8}. On the complement
    they act by the complex conjugates.
- **M2, geometry on ℓ, flavour on M.** In the basis t_p (T's line in block p, scaled so that Φ_p(t_p) = ℓ̂):
  - each lift of L and R acts on T as its eigenvalue on ℓ times a rotation of the cube. L is a quarter-turn about the
    (0, ½) axis and R a quarter-turn about the (½, 0) axis, the same for both lifts of each;
  - each lift of the inner automorphisms acts as its sign on ℓ times the parity signs, (−1, +1, −1) for a and
    (+1, −1, −1) for b;
  - the lifts of L and R generate 96 elements on T, exactly W42's {z S : S a rotation of the cube, z⁸ = 1,
    z⁴ = sgn S}, and the inner automorphisms' lifts lie among them;
  - every restriction keeps T, to 1.4 × 10⁻¹⁵.
- **M3, the pairing.** The Hodge–Riemann form on T in the basis t_p is 2·I₃: three equal norms, mutually orthogonal.
- **M4, the puncture conditions in ρ_Q ⊗ M.** The last column is W46's fibre index, recomputed (E4).

| condition | dim | dim X_W | dim Y_W | a product | X ⊗ M (blind to M) | generic rank | fibre index |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | yes | yes | none | −3 |
| V2 | 2 | 2 | 3 | no | no | 2 | −1 |
| V4 | 4 | 2 | 3 | no | no | 2 | +1 |
| L₆ | 6 | 2 | 3 | yes | yes | 2 | +3 |

- **The extra read-outs** (fixed before the run, with no prior).
  - **E1.** Every signed permutation above is the lift's conjugation of the three units, g⁻¹ u_p g = Σ_q P_qp u_q, for
    all eight lifts. So M is the triple of imaginary quaternion units, rotated by 2O's image in SO(3). V2 and V4 are
    the spin-½ and spin-3/2 pieces of spin ½ ⊗ that vector (W46's names).
  - **E2.** T̄ meets each block in a line, and the intertwiners send the three to ℓ's complement: T̄ = ℓ′ ⊗ M.
  - **E3.** Every sampled vector of V2, as a 2 × 3 matrix, has singular values in the ratio √2 : 1 (200 vectors;
    min = max = 1.414213562373). By hand it holds for every vector, since Σ_p u_p† A u_p = 2 tr(A)·1 − A over the
    three units. So V2 is uniformly entangled and contains no product vector.
  - **E4.** The fibre index is ±3 exactly at the conditions blind to M.

**What it shows (a READING on the computed facts; T read as the generations given Λ, GENESIS FK11).**
- **The three generations are a multiplicity.** The weave's holomorphic triplet is one zero mode ℓ of the spin
  doublet, carried three times: T = ℓ ⊗ M, with M the three imaginary quaternion units. The three are one solution
  with a three-valued label, not three solutions.
- **Geometry acts on ℓ, flavour on M.**
  - Every lift acts on T as a scalar on ℓ times a rotation of the three units. The Hodge–Riemann pairing is a scalar on
    ℓ times the identity on M.
  - Any datum built from the local system and the surface alone is unchanged by the local system's automorphisms
    GL(M), so it is a scalar on M. That covers the pairing, the zero modes' values at a point of the torus, the natural
    end conditions 0 and L₆, the cusp's units and the flat twists (W45 to W48).
  - Such data give three degenerate, orthogonal generations.
- **Three or split.** At the puncture, the conditions that keep ±3 are exactly the ones blind to M, 0 and L₆. The two
  that touch M, V2 and V4, are entangled, and they give ∓1. So among the end conditions the weave keeps, one that keeps
  three cannot tell the generations apart, and one that could tell them apart does not keep three.
- **The free numbers.** Values that tell the generations apart need a tensor on M that breaks the weave's group.
  Schur's lemma is the algebra of main's §3, and the multiplicity is its geometry. The record's candidates are:
  - a flavon, or a Higgs with flavour structure, which the principle does not supply;
  - G's own subgroup projectors (B1620, B1621), which leave the values free (W42 to W44);
  - couplings in τ alone, modular forms valued in M. These give permutation mixing when the inner automorphisms act at
    every τ (T-TAU-ONLY-PERMUTATION).

**Found while writing this up (post hoc; a READING, to be tested as W50 with the rule first).**
- **The inner automorphisms by a and by b are not words in L and R.**
  - In Aut⁺(F₂), ⟨L, R⟩ is a quotient of the braid group B₃ (σ₁ = L, σ₂ = R⁻¹), and it maps onto SL(2, ℤ).
  - The kernel of B₃ → SL(2, ℤ) is generated by Δ⁴, with Δ = σ₁σ₂σ₁. Δ⁴ is conjugation by u = a b⁻¹ a⁻¹ b (W45).
  - So ⟨L, R⟩ meets the inner automorphisms only in the powers of conj(u), which acts on T as −I.
- **They enter with the forks the owner ruled out** (by hand): the sign σ gives σ L σ L⁻¹ = conj(a⁻¹), and the swap
  gives P L P R⁻¹ = conj(b).
- **So on the ruled branch** (even ticks and positivity, the weave ⟨L, R⟩), the parity grading is not a symmetry at a
  fixed τ.
  - At a generic τ the weave's residual on T is generated by Δ², which acts on T as the scalar Z (W21).
  - At i it is generated by Δ, whose square is that scalar, so T splits into a line and a plane. At ω it is generated
    by σ₁σ₂, a 3-cycle of the units times a scalar, so T splits into three lines (by hand).
  - W40's order-48 group at ω, irreducible on T, used the inner automorphisms and −I.
- **This bears on main's T-TAU-ONLY-PERMUTATION and B1617, and on this seat's W40 and §46**, which verified them in the
  frame where the inner automorphisms act. Their computations stand; the open point is which group they are about.
- **W50 will test it, with the rule first:**
  - the word identities;
  - the residuals on T at a generic τ, at i and at ω on the ruled branch;
  - whether couplings in τ alone, as modular forms on M (W45's ρ_T), give mixing that is not a permutation there.

**Status.** COMPUTED (the rule first; one run; every cell as predicted); a WEAVE result. The post-hoc point is a READING
until W50. 0 of 19.

## Reading W24–W29 together (READING; the owner asked to contemplate before verifying further)

Nothing here is computed, and nothing here is a result of W30 or W31: their values go in their rules. The order follows
the owner's approved plan of 2026-10-08: contemplate, close the arc, then W30 (step 4) and W31 (the ℤ₅ flux).

1. **Every route has ended in one free 𝔽₂, the hand.**
   - The sign of the index ±3 (W22, W28).
   - A Lagrangian half (W25).
   - The mirror (W26).
   - The semion against the anti-semion (W28, I3).
   - ζ against ζ̄ (W29).
   - What does not depend on the hand is an asymmetry in the weave's own group: the index on 𝕎 is odd, never 0 (W22,
     W24 D0, W28), and the flavor triplet T is complex (W21).
   - That asymmetry is not yet a gauge chirality: W25 shows that the weave's bundles give none without a choice.
   - **A question for main, not a reclassification:** is F-MC's chirality bit the orientation's convention, so that
     what is missing is the dictionary alone, which fields carry 𝕎 (GENESIS FK11)?
2. **What a flux must be to keep the whole Standard Model** (a structural reading; W31 computes it).
   - Holonomies that keep the Standard Model lie in its centraliser in E₈, the bundle factor of W17, W23 and W29 times
     U(1)_Y (sm:B1384's handoff check).
   - Their commutator lies in the bundle factor. For a twist-eater it is central there, so it is of order 5.
   - W29's ℤ₆ flux, e^{2πiY}, therefore cannot keep the hypercharge, which is W29's lemma seen from the other side.
3. **The binary polyhedral groups along the moves** (READING).
   - On a ℤ_p clock-and-shift pair the moves act through SL(2, 𝔽_p).
   - p = 2: SL(2, 𝔽₂) ≅ S₃. The qubit's lifts reach 2O only together with the Paulis (W28).
   - p = 3: SL(2, 𝔽₃) ≅ 2T, McKay E₆, F-MC's prime of norm three.
   - p = 5: SL(2, 𝔽₅) ≅ 2I, McKay E₈ (B206).
   - W30 and W31 compute the p = 3 and p = 5 lifts. The McKay pairings are a reading, not a step.
4. **The count is read from how the moves split the local solutions.**
   - A sector with puncture holonomy e^{2πiα} on r channels has index −rα + dim Λ₊. The move-invariant Λ₊ are sums of
     the lifts' pieces.
   - The qubit ⊗ ℂ³: −3, −1, +1, +3, and ±3 under naturality (W28). These hold with or without the bare sign move
     (W29 post hoc, P3).
   - ℤ₆: −1, 1, 3, 5 under L and R. Only −1 or 5 if the bare sign −I is a move (GENESIS GM5b, FK4; W29 post hoc, P3).
   - So which moves the grammar allows (the sign, GM5b; the swap, GM5c) decides the counts. GENESIS keeps both forks
     open.
5. **The Standard Model's ℤ₆ cannot be the fibre's flux with the whole Standard Model unbroken** (W29; point 2).
6. **F-MC's trit and the weave's three (a question for main, with no map proposed).**
   - THE_CLAIM §1 counts the VEV acceptance as "ONE TRIT" (B1030): a ℤ/3 label, the 27's three 9-blocks against the
     three surviving SU(3)'s, triality-transitive.
   - The weave's three parities are permuted by S₃, none distinguished (W1, Theorem G).
   - Equal labels in different places are not an identification (B1231's discipline). The question is whether a map
     between the two exists, not a claim that they are one.
7. **A correction to keep straight.** In F-MC the hypercharge direction and the global form are DERIVED (B862, B864,
   B991). F-MC's five typed inputs are:
   - two 𝔽₂ bits (time's arrow; chirality);
   - one scale;
   - one Lie type J;
   - one rank-closing VEV direction.

## Reading W24–W32 together, with the audit lane's packets and main's S88 (READING; the owner: "lets be brave")

Nothing here is computed. It reads the arcs since the first contemplation, main's S87 and S88 (B1607, B1609), and the
audit lane's five sealed packets of 2026-10-08 on its branch `audit/physical-bridge-2026-09-05` (the puncture sheaf,
the form fermions, the companion roster, the curved action, the cusp condensate). The owner asked what we are not
seeing.

1. **The hands are conventions unless something forced orients the records.**
   - Curie's principle (the record's P012): a symmetric principle does not output an asymmetric choice. The Standard
     Model and its mirror or CP image are one theory with the labels exchanged.
   - Main's S88 (B1609): the three's hand is the records' orientation, not the McKay orientation. Main's next question
     is whether anything the principle forces picks a sheet of the orientation double cover.
   - **The brave form of the answer:** forced to choose, not forced which. The flat, symmetric point has no gap at the
     cusp (the audit lane). A physical end needs a stationary condensate. If that condensate distinguishes the two
     orientations, every physical end picks a hand, and the two choices are mirror images. That is how a derived
     chirality looks in physics: a spontaneously chosen vacuum, not a selected law.
2. **The three are the three even spin structures of the fibre torus; the odd one is the troublemaker.**
   - A torus has three even spin structures and one odd one; the moves permute the even ones and fix the odd one.
   - The odd one carries a chiral mode that cannot be switched off (W22: its index is odd, never zero).
   - So frames that force it in give 3 + 1 or 1: F-HE's rank five (W32's four is the three plus the odd one). Frames
     that exclude it give three: E₆ with 𝕎 (W27). The audit lane's roster shows the same split, three alike spin lines
     and one trivial.
   - The question "why three" becomes "why does the odd spin structure carry no generation". In the ℤ₂ × ℤ₂ orbifold
     the record already cites (W24), the odd one is the untwisted sector and the generations come from the three
     twisted ones.
   - **Corrected by W33 (the same evening, the rule committed first).** As a law across the frames this point fails.
     The doublet blocks are label-blind (χ_p ⊗ ρ_Q ≅ ρ_Q), so the counts see how many doublets a sector has, not
     which spin structure labels them. What survives is the precise form: the zero parity's doublet in the parity
     doublets' sector makes four.
3. **The counts are sheaf Euler characteristics; a particle count needs an end that gaps the cusp.**
   - The audit lane justified the record's formula as a sheaf Euler characteristic: parabolic weights ½ and
     Riemann–Roch on the compactified curve give χ = d − 3.
   - At the complete cusp, ordinary spinors have zero in their essential spectrum (not Fredholm). Twisted one-forms
     keep W21's triplet with a finite norm and a gap. So the dictionary is likely a topological twist, with W21's form
     triplet as its healthy part.
   - Every roster read so far is self-conjugate (as W25 found). The missing physical step is a mechanism, an end on the
     same action that gaps the continuum: GENESIS GAP3's source. The audit lane's stationary cusp condensate lifts 58
     of 112 channels. It keeps colour and breaks the weak SU(2), whose centre in E₈ is the puncture's −1 (checked here
     by the branching: both act as −1 on (3, 2, 6), (3̄, 2, 6̄) and (1, 2, 20); W25's chi248 at −1 in SU(6)′ is 24, an
     involution with centraliser E₇ × SU(2)).
4. **Three may be a consistency number, not an index (untested).** Three generations is the minimum for a CP phase in
   quark mixing (Kobayashi–Maskawa). The weave allows at most three alike things and carries a complex structure on
   them (W21's T, ω). A lower bound and an upper bound would meet at three without any index.
5. **Rejected: the three as colour.** It fits on the surface: colours are exactly alike, the moves act as SU(3)'s Weyl
   group, and Λ²(D ⊕ P) repeats SU(5)'s 10. But colour must commute with the fibre's holonomy, which tells the three
   parity lines apart, so colour would be broken to its torus. The 10-pattern is SU(5) branching.

**The riddle restated.** The hands were never derivable and need not be: what is derivable is that a physical end
must choose one. The count's real question is the odd spin structure. Beneath both sits the physical step the audit lane
is building: an end on the weave's own action that gaps the cusp.

**Tests this reading proposes (none run here).**
- Does the stationary cusp condensate distinguish the two orientations, that is, is its mirror image gauge-equivalent
  to it? If it is not, the end chooses the hand. (The audit lane's action; relayed.)
- Is "three exactly when the odd spin structure is excluded" a law across the record's frames?
- Does the weave's natural flavour structure carry a phase no rephasing removes?

## What the weave gives, and what it does not

| step | status | what |
|---|---|---|
| W1 | PROVED | three non-zero parities, permuted with none distinguished only when moves act together |
| W2 | PROVED | one structure all threads share: the quaternion point |
| W3 | PROVED | on every odd-trace thread, the same A₄ and the same 2T from it |
| W4 | PROVED | one irreducible triplet, the same on every odd-trace thread; even-trace threads split it; the weave's group on it is real (T_d ≅ S₄; O_h with P) |
| S | PROVED | Theorem S (`docs/THE_WEAVES_LAWS.md`): no state has its three parities separate and carried into one another at its own tick; every odd-trace thread has them so at every third tick |
| W5 | READING (main's GENESIS FK14; GENESIS FK7) | the three generations are this triplet at every third tick: three, alike, carried into one another by the deck, which is the shift by one tick |
| W6 | PROVED (WEAVE); COMPUTED (THREAD) | Theorem G: whatever one parity carries, all three carry. A thread result: on +LR each parity carries one generation of each type. The census: no other odd-trace thread to length 6 carries any on its forced cover (twelve of twelve, at orders 4 and 3); to length 8 main's B1602 (cited) finds a third, −LLRLRLRR, reading (+3, +1) |
| W7 | COMPUTED (WEAVE, by rule) | in Theorem S's sense, at every state's resolving tick to length 6: members only on the pair of parities a state's symmetry exchanges (±LLRR, ±LLR, ±LLLLR), never on the parity it fixes, never on all three |
| W8 | PROVED (Lemma V, WEAVE + WAVE); COMPUTED | the frame at the weave's own vacuum (the common point) reads rank-one lines: the three parity lines alike on every thread, all on the end; no member on any state at any tick |
| W9 | COMPUTED (WEAVE, two routes) | the weave's spin doublet H¹(F₂; ρ_Q): the moves act by ℤ/8 (Q₁₆ with the swap); every thread has interior classes on it; twisted by the parities, three alike interior sectors on every odd-trace thread at tick 3 |
| W10 | COMPUTED (WEAVE) | V, the three parity-twisted spin doublets: under L and R a group of order 96 with V = T ⊕ T̄, two complex-conjugate triplets (a chiral three); the swap exchanges them (order 192). On exactly one sign twin of every odd-trace word, one vacuum character at tick 3 carries T alone (m003, not m004, of the root's pair) |
| W11 | NEGATIVE (sm:B1552, sealed); PROVED (WEAVE + WAVE) | F-HE's count at the weave's spin vacuum: (0, 0) at all 864 sealed readings, and zero at every class on every thread at every tick (sm:B1509's T2 and T3: no cusp cohomology, a semisimple stable letter). The spin vacuum carries the three but no content in this frame |
| W12 | PROVED (WEAVE + WAVE); COMPUTED | the joined vacuum λ ⊗ ρ_hyp ⊗ ρ_Q has no interior class on any state at any tick (Menal-Ferrer–Porti through Shapiro): F-HE reads nothing there. In F-HE a generation's content is a thread's (the balanced four's cuspidal classes on covers) |
| W13 | VERIFIED (main's B1434: four odd-trace rows on the engine route, all six through W14) | F-CI's generation-shaped backgrounds at the resolving tick come in deck orbits of three, each counting one, on ±LR, ±LLLR and ±LLLLLR; this seat's code agrees with B1434 row by row |
| W14 | PROVED (the slope law); COMPUTED (the census) | F-CI's index is [s(α) = s(λ)] − [s(α − λ) = s(λ)] (slopes on the cusp torus), and its signs pair (the extension's order). At the resolving tick, ten of the twelve odd-trace threads to length 6 carry one-generation backgrounds in deck orbits of three; ±LLRLRR carry none. So F-CI's content is not a weave law; the three is |
| W15 | PROVED (Theorem H; the extension index formula); COMPUTED (the census, 32 states); a prediction half held | the hand is the determinant of the weave's triplet T at tick 3, mirror-odd, on every odd-trace thread (W9's hand rule, now a theorem). The weave's own extension of a parity line by a spin doublet has index [c ∪ ℓ_p ≠ 0]: exactly one per parity, three or nothing, and silent exactly when φ³ ≡ ±I (mod 16) on all 32 odd-trace states to length 8 (±LLRLRR and ±LLLLLRRR). F-CI does not share that silence (it carries on ±LLLLLRRR). The weave's five (2 + 3) reads F-HE's anomalous (−1, −3). Main's conditions for FK11: the module and count, and the chirality handle, met; the shape identity not built into the class index |
| W16 | VERIFIED (main's B1601, 37 of 37, exact in each field; main's B1604, the proof re-derived and its control E1 the engine's B1297 identity at every index) | the common point is each odd-trace thread's geometry mod a prime of norm three; no flat count on a thread or a cover of one is an index, so GENESIS FK11 is unearnable there, and W15, W17 and W18 are class-index laws. B1602's third carrier was withdrawn by main |
| W17 | COMPUTED (WEAVE, 32 of 32 states to length 8, 480 readings) | the weave's five on the thread itself (the spin doublet and the parity triplet, twisted ν³ and ν⁻² so that SU(5)′'s determinant is trivial, glued by a weave class) reads F-HE's generation shape (1, 1), dual (−1, −1), on the vector-like twin of every word with φ³ ≢ ±I (mod 16); a lone 5̄ on the chiral twin; nothing on the mod-16 words. Main's three conditions for FK11 all have weave answers. The count is one per thread: the parities are the five's triplet, and three needs the deck kept (FK7) |
| W18 | COMPUTED (WEAVE, 32 states; a prediction that failed at special classes) | the five's sectors on the forced cover: at the generic class each of the three parity lines carries the five's pair (1, 1) on every carrier, the shape of the orbifold standard on the weave's own modules; on every carrier exactly two classes of the gluing line drop it to (0, 1) (the engine's basis met one on four); (0, 2) on the chiral twins; nothing on the mod-16 words. The zero parity's part (1, 3) and the cover's total (4, 6) are not the shape. Under B1604 these are class-index pairs, a selection by forced characters, not counts |
| W19 | READING (the facts classical) | the weave's own surface: the moves with the fibre's group generate Aut⁺(F₂), every thread's group inside it, so the weave's space is M₁,₂, the universal punctured elliptic curve, every thread at once (each over its closed geodesic). Its Euler characteristic is 1/12, not 0, so B1604's vanishing stops at the threads. The three parities are the fixed points of the elliptic involution off the puncture, one curve of degree 3. The even-dimensional object main's FK11 asks for; no bundle named, no count read |
| W20 | COMPUTED (exact; a census of all 21 SL(2)s in E₆, two routes); READING for the dictionary (GENESIS FK11 on the weave) | the record's E₆/27 frame, carried by the weave's own SL(2) (the moves on the records), counted by the weave's Euler characteristic: −χ(Aut⁺(F₂); 27) = 3 through the principal sl₂ and through every distinguished one, while every thread reads 0 (B1604). ±3 on 13 of 21 SL(2)s; the 78 reads 16. Not chiral: the 27 and 27̄ read alike, and by the heterotic dictionary the matter is vector-like (four of each in degree one) |
| W21 | PROVED (the invariance of the holomorphic part, two proofs) and COMPUTED (the sign, every control first; the rule committed before the run; a second route after it, the actual periods at three τ) | the hand by Hodge type: on the shared fibre at the common point, the holomorphic zero modes for the three parities (one each) span T, and the antiholomorphic ones T̄. Chiral under the weave's group; vector-like under a gauge group, because the common point is self-conjugate (an unequal count would need an end condition, GENESIS GAP2): the flavor structure of three generations, not their gauge chirality. T = μ ⊗ 3′ (the holomorphic spin line times the cube's rotations at the common point). The hand is the sign move's spin lift; the swap reverses the orientation and exchanges T and T̄. The zero parity adds one singlet. The dictionary stays a reading (GENESIS FK11) |
| W22 | PROVED and COMPUTED (WEAVE) | the end condition at the puncture: the moves' lifts generate 2O and act irreducibly on the two local solutions in every parity block, so the only conditions every move keeps make each block's index +1 or −1: the parities' three is chiral (index ±3), its sign the orientation. One thread alone leaves a line (a vector-like condition); the weave does not. GENESIS GAP2 closed for this operator up to the hand. Which fields carry 𝕎 is the dictionary; on the 2d fibre the E₈ frames give (1, 3) or one 27, not complete generations (GENESIS FK11). QUALIFIED by W24's D0: the blocks are one doublet, so conditions may mix them; the moves alone keep four (index −3, −1, +1, +3). The index is always odd, never 0; it is ±3 when the condition keeps the parity grading (the flavor symmetry of 𝕎 ≅ ρ_Q ⊗ ℂ³) |
| W23 | COMPUTED (WEAVE; a census, negative) | the record's E₈ frames on the weave's fibre with W22's condition: over every SU(n) bundle built from the common point's blocks, E₆ gives 0 or 1 chiral 27, SO(10) 0–2 chiral 16s, SU(5) (0, 0), (1, 3) or (2, 2). At most two complete generations; three is impossible, since each spin doublet has rank two. The weave's five reads (1, 3), anomalous by −2, so the puncture must carry anomaly +2. Three complete generations need matter carrying the rank-six bundle, the puncture's localized content, or a six-dimensional object (GENESIS FK11) |
| W24 | COMPUTED (exact; the rule committed first, every cell as predicted) and PROVED (D4); a WEAVE census, NEGATIVE | the six-dimensional census (the owner's choice): the fibre's character variety ℂ³ is forced (the moves preserve κ and, for L and R, the volume form; the common point and the trivial point are the only common fixed points) but contractible, with no quotient and a trivial tangent bundle; the orbifolds E³/G of the weave's finite groups give 48, 16, 14 generations (V₄, A₄, O), never three, with E chosen; main's frame spaces have index 0 on any compact quotient (cusps open); the universal families fail S1 or S2. The reason: 𝕎 ≅ ρ_Q ⊗ ℂ³ has holonomy Q₈, whose centraliser in E₈ is F₄ × SU(2); a chiral gauge reading needs a Lagrangian half of a pseudoreal multiplicity space, which breaks F₄ by a choice, the dictionary (FK11). Positive: W21's flavor triplet is the tangent space at the common point; the net chirality is odd; the node mod the parities is D₄, mod A₄ is E₆. The audit D0 qualifies W22 |
| W25 | COMPUTED (exact characters; the rule committed first, every cell as predicted) and PROVED (the lemma, F5); a WEAVE theorem | the weave's forced bundles are self-conjugate. The fibre's holonomy Q₈ has only real and quaternionic irreducibles, and the weave's group on the six local solutions (order 192) is quaternionic, so every gauge reading on the fibre, the even-dimensional object where the index lives, is self-conjugate. Chirality-capable gauge groups appear only when one parity is singled out (the centraliser of ⟨e_p⟩, 82, contains E₆: a selection) or when the order-3 move is in the holonomy (2T, centraliser 25, ω fifteen times: a thread, odd-dimensional, B1604). The weave's S₄ conjugates every 3-cycle to its inverse and exchanges ω and ω². So the dictionary (GENESIS FK11) cannot be derived from the weave's local systems; it needs an input the weave does not force |
| W26 | COMPUTED (exact and SnapPy; the rule committed first, every cell as predicted); a WEAVE result, NEGATIVE for the two candidates beyond the weave | the search beyond the weave (the owner's choice). The weave is closed under the mirror: S φ⁻¹ S⁻¹ = reverse(φ) with L ↔ R for all 224 words to length 10, and on all 42 threads to length 6 the mirror has the same volume and opposite Chern–Simons, so the threads' hyperbolic holonomies give the weave no hand. Each move is a transposition of the parities mod 2, so the order-3 orientation that would decide F-MC's 27 against 27̄ flips at every tick on all 98 odd-trace words; F-MC declares chirality an input (THE_CLAIM §1). The weave's only hand is the records' orientation (forced only if the swap is not a move, GM5c). The record's best derivation: F-MC's gauge structure with its inputs, the weave's count three with its common hand, and FK11 between them |
| W27 | STATED (the link Λ, an input) and COMPUTED (exact; the rule committed first) | the derivation written with its one link: principle + F-MC's typed inputs + Λ give exactly three chiral 27s, alike, in the flavor triplet, each with one Standard Model generation; anomaly-free (exact); the count ±3 only under Λ's parity grading; in six dimensions Dobrescu–Poppitz's global SU(2) condition selects a multiple of three sectors (local anomalies would need a completion); three right-handed neutrinos. Labeled "derived given one stated link" (`docs/THREE_GENERATIONS_GIVEN_ONE_LINK.md`) |
| W28 | COMPUTED and PROVED (I5, exact; the rule committed first, every cell as predicted); a WEAVE result, the foundation | the end condition: the six local solutions are a vector-spinor (spin ½ ⊕ spin 3/2 under 2O); the two middle conditions (index ∓1) couple the parity sectors and break 𝕎's flavor group U(3) to a phase. The moves alone allow −3, −1, +1, +3; the flavor group alone −3, 0, +3; jointly only ±3, and locality (the puncture's holonomy −1, symmetry U(6)) gives ±3 too. So Λ's "kept apart" follows from the end condition breaking no symmetry of the bulk problem (a stated naturality condition). The common point is the qubit: Q₈ the Pauli group, the parities the three Pauli axes (mutually unbiased), the moves' lifts the Clifford group (2O, the normaliser of Q₈), acting through PSL(2, ℤ/4) ≅ S₄ as SU(2) level 1's projective modular data (one dictionary each for the semion and the anti-semion: the hand is in the phases); the parities are ℙ¹(𝔽₂), the three global forms SU(2), SO(3)₊, SO(3)₋, equivariantly; the common point is 't Hooft's twist-eater, which eats the centre symmetry |
| W29 | COMPUTED and PROVED (the lemma; the rule committed first; every cell as predicted except Z5's naming of the −I lift, corrected post hoc); a CHOSEN object (the ℤ₆ flux, not forced), NEGATIVE as a derivation | the ℤ₆ twist-eater (the weave's qubit ⊗ a qutrit) in E₈: its centraliser is exactly SU(3) × SU(2) (11; the qubit alone F₄ × SU(2), the qutrit alone SU(3) × G₂), its 6 is complex with multiplicity (3, 2), the 15's three single types are the three parities ((3̄, 1) each), the 20's eight single types are ℙ¹(𝔽₃)'s four lines in conjugate pairs ((1, 2) each), and its flux is e^{2πiY}; the swap has no lift (the hand visible). The moves split the 6 as 4 ⊕ 2 (the eigenspaces of the lift of (LR⁻¹L)²): quark generations −1, 1, 3 or 5, each SU(3)³-free with the Standard Model's ratio; locality gives five. Not a derivation: the flux breaks U(1)_Y (exact lemma), three is not forced, no chiral leptons, and the flux is not forced (step 4) QUALIFIED post hoc (P3): the set −1, 1, 3, 5 holds for the moves L and R; with the bare sign −I a move (GENESIS GM5b, open) it is −1 or 5; W28 unchanged |
| W30 | COMPUTED and PROVED (Q1, Q2; the rule committed first, every cell as stated); a WEAVE result, NOT FORCED | is an order-3 flux forced on the shared fibre? The forced point's puncture −1 has order 2, so no representation of it carries an order-3 flux; the qutrit pairs form one class, kept by L, R and −I and sent to the conjugate class by the swap (the swap with complex conjugation keeps it), so the qutrit point is a common point only on one branch of the swap's fork (GENESIS GM5c, FK3); its rank-3 cusp condition is a choice; the moves act on it through SL(2, 𝔽₃) (order 24, 2 ⊕ 1); the record's order-3 structures are on threads or on the meridian. Allowed on a fork, not forced |
| W31 | COMPUTED and PROVED (F1's lemma; F4's argument; the rule committed first, every cell as stated); a CHOSEN object (the ℤ₅ flux, not forced), NEGATIVE as a derivation | the ℤ₅ flux in E₈ ⊃ (SU(5)_g × SU(5)_b)/ℤ₅, the only twist-eater flux that keeps the whole Standard Model: its centraliser is exactly SU(5)_g (24); its matter is complete SU(5) generations (the 5 ten times, the 10 of SU(5)_g; Λ²5's type ten times, the 5̄ twice; both complex); its flux is a hypercharge rotation (exact). The moves act on ℂ⁵ through 2I = SL(2, 𝔽₅) (order 120, split 3 ⊕ 2, the 2-piece the spin representation with golden traces), and with the bare −I through the ℤ₅ Clifford group (3000). The swap sends the flux to its conjugate. No flux ζ^m gives an anomaly-free three: the SU(5)³-free counts are −1 and 2, or −2 and 1, under the moves, and none under locality. Not a derivation: no three, SU(5) unbroken by anything forced, the flux not forced |
| W32 | COMPUTED and PROVED (P1; the rule committed first, every cell as stated); a WEAVE result within F-HE, NEGATIVE | the puncture's end condition in F-HE's two sectors: over every rank-5 bundle built from the common point's blocks that L and R keep (five), with the end conditions the weave keeps (naturality, W28; locality), no anomaly-free three. The weave's five (1, 3) is cured naturally only at one or four complete generations (b = −2 or +1; three needs b = 0). The 5̄-sector holds 𝕎, natural at ±3; the 10-sector holds D ⊕ P, natural at ±1 + {0, 3}, and three there needs the parities mixed. In F-HE the puncture does not make three; three complete generations need a frame whose 10-sector holds 𝕎 (W27's Λ). Scope: flat ends only; a non-flat end (GENESIS GAP3's source) is outside it |
| W33 | COMPUTED (the rule committed first, every cell as stated, one wording difference disclosed); a WEAVE result within the record's frames, NEGATIVE for the naive law | is "three exactly when the odd spin structure is left out" a law across E₆, SO(10) and SU(5)? No, under every counting convention: under naturality, E₆'s trivial bundle gives three (a rank count); under the spinor rule every sector's count is ± its number of doublet blocks, so three needs rank six (W23's conclusion as a law). The doublet blocks are label-blind; the three parity doublets count ±3, and with the zero parity's doublet added ±4. Corrects the second contemplation's point 2 |
| W34 | COMPUTED (the rule committed first; Q2, Q3, Q5 as stated; Q1's sealed criterion missed on 11 states, resolved post hoc); WEAVE results (Q2, Q5) and laws over the threads (Q1, Q3), NEGATIVE for the observer layer as the missing ingredient | the record's observer-layer probes (B760, B761, B762; main's B1183, B1184), all on m004, taken to the weave. No private states holds on all 758 states to length 12 (Menal-Ferrer and Porti; 747 at 60 digits, the other 11 post hoc at 120): a property of the class. At the common point the fibre has private states from rank three (fiber_dim 0, 4, 6 for n = 2, 3, 4: the flat twists of the blocks' trivial pieces), and no thread and not the joint action keeps any. The 758 states have 536 names, the coincidences exactly the 222 reversal pairs: every thread is named among the threads up to its register. The weave cannot sign itself; the self-sign is the hand. The register is an inner automorphism (rev σ = ι_{a⁻¹}∘σ) and carries neither hand |
| W35 | VERIFIED (not blind; B1612 read first); main's WEAVE result reproduced | main's B1612 rebuilt from W21's construction (V, the moves' lifts, the holomorphic triplet T, the Hodge–Riemann form as the inner product): the image on T has order 96 with 56 elements of distinct eigenvalues; 11 eigenbases, 9 eigenlines; six full patterns (single maximal angle, tri-bimaximal, bimaximal, trimaximal with (2 ∓ √3)/6, the circulant (1/9, 4/9, 4/9), democratic) and five columns ((0, 0, 1), (0, ½, ½), TM1, (¼, ¼, ½), TM2); every named cell as B1612 states, TM1 from RL against RRL's eigenline with no swap |
| W36 | VERIFIED (step 1, exact) and a READING with one exact obstruction (step 4) | the audit lane's gapped Standard Model phase: its centralizer in E₈ is (SU(5)_b × U(1)_Y)/ℤ₅ and connected (the roots orthogonal to SU(5)_g are an A₄; the torus part is the kernel of the character (3, 2), connected). On a closed surface the 10's index is deg W and the 5̄'s deg Λ²W, both zero for every SU(5)_b bundle, so the fibre's bulk gives no SU(5)_g chirality; the record's counts are end contributions on the gapless channels, which a gap removes. A gapped chiral phase needs winding end data or an object of dimension four or more |
| W37 | VERIFIED (not blind; S92 read first); main's WEAVE results reproduced | main's B1613: TM1's relations derived here from the matrix entries; at sin²θ₁₃ = 0.02248, sin²θ₂₃ = 0.470: sin²θ₁₂ = 0.31800, cos δ = −0.130278, δ = 97.49° or 262.51°, J = ±0.03378, the column exact on both branches. Main's B1614: the joint fixed points (0, 0, 0) and (2, 2, 2); the trivial line (2, 0, 2), each parity line (1, 1, 0), the adjoint (3, 3, 0), the doublet and each matter block (2, 0, 2) as (H¹, visible, private); χ_T(L) = e^{−iπ/4}, χ_T(R) = e^{+iπ/4}, χ_T(LR) = 0; the odd classes of rank 2 over 𝔽₂. Agrees with W34 where they overlap |
| W38 | VERIFIED (not blind; S93 and S94 read first); main's WEAVE results reproduced | main's B1615 and B1616 rebuilt from W21's construction: no invariant bilinear or trilinear of T alone; T̄ ⊗ T = 1 + 2 + 3 + 3; a singlet Higgs gives (1, 1, 1); the fixed Dirac vacua give (0, 1, 1) or (½, ½, 1), and along RRL a family with m₁ + m₂ = m₃ (to 3 × 10⁻¹⁵); Sym² T = 1 + 2 + 3, Λ² T irreducible, no Majorana vacuum fixed along RRL, rigid spectra (1, 1, 1), (½, ½, 1), (0, 1, 1) elsewhere. The weave's group fixes no mass. Exact addendum (post hoc, for the audit lane): T is the cube's rotations twisted by a character (W21's μ ⊗ 3′); the sum rule is Heron's identity on the whole family, masses ∝ (r, (1 − r)/2, (1 + r)/2); every residual-fixed Majorana matrix, all pieces at once, has a degenerate pair; several Higgs irreducibles along one residual leave the masses free |
| W39 | READING given Λ (no new computation) | given W27's Λ every left-handed field of a generation is in T, so a mass term's tensor is T ⊗ T, not B1615's T̄ ⊗ T; with E₆'s cubic and one 27 Higgs the Yukawas are symmetric (Sym² T, B1616's tensor, for every sector): no mass from a flavourless Higgs or from the generations' own 27s, any mass needs a Higgs carrying c̄², and every residual-aligned spectrum is degenerate or zero. Rests on a frame, GENESIS FK11's datum: in W24's E₈ embedding only c is flavour (S(g) gauge); in the record's frame all of G is; where a U(1) acts on T, c is gauge and an O-singlet Higgs gives δ (the premise's first version, restored in part after the assurance round's over-withdrawal; W43) |
| W40 | VERIFIED (not blind; S95 read first); main's WEAVE result reproduced, given τ = ω | main's B1617 rebuilt from W21's construction: U (a ↦ b, b ↦ a⁻¹b; H₁ matrix of order 6; it fixes ω under the standard Möbius rule, while under the period rule U fixes ω + 1 and L U L⁻¹ fixes ω, with the same group results, as corrected in the assurance round), the inner automorphisms and −I generate a group of order 48 on T, irreducible (commutant 1); the inner automorphisms are the Klein group's diagonal signs (the parity grading), U is i times a 3-cycle of the parity axes, with eigen-turns ¼, 7/12, 11/12 (order 12); one invariant in T̄ ⊗ T (three equal masses), none in T ⊗ T or Sym² T. W39 qualified: its consequences hold at weight 0 |
| W41 | COMPUTED (the rule first; one run after a disclosed stopped launch) | the weave's zero modes are a vector-valued modular form of weight −¾ (as one-forms; f = θ₃(z \| 2τ)/√θ₁(z \| τ) of weight ¼ and index 0): the norm test g = N/(Im τ)^{3/4} is invariant under T, S, U, L, R, RL, LRR at two base points (worst 2.7 × 10⁻¹¹; exponents ¼ and 1 fail by 0.086 and 0.046); the numerator pair has weight ½ with constant unitary W (W(T) = diag(1, i)); θ₁'s multipliers are eighth roots. At ω the modes' U-action is W40's, nothing added (§40's line withdrawn in the rule), up to a branch convention: the two lifts, as the assurance round found |
| Assurance (2026-10-08) | ASSURANCE (post hoc) | the owner's "are we sure": a conventions registry (two string conventions; the period rule, corrected), mutation tests (10 of 10 caught by regeneration, 5 by the result tests, so a regeneration test was added), four independent adversarial reviews (foundation 6/6 and masses 6/6 confirmed exactly; weight 4/5, the fifth a branch convention; readings: no false theorem, several overstatements corrected), script fixes with values identical, the norm routine's small-Im τ bug fixed. Findings: the residual convention (flavon versus modular scenario; P10 lives only in the first), the period rule's stabiliser L U L⁻¹, and the frame premise (GENESIS FK11) |
| W42 | VERIFIED (not blind; the rule first; B1620 read first) and COMPUTED (a census of every thread to length 12) | main's B1620 rebuilt from W21's construction: G = {z S : z⁸ = 1, z⁴ = sgn S}; 68 subgroups in 26 classes, 57 abelian; viable (three distinct non-zero masses, exact in ℤ[ζ₂₄], two routes): 57 under T̄ ⊗ T (the abelian ones), 24 under T ⊗ T (real character: E's 16 and the 3-cycles' ⟨±t⟩), 16 under Sym² T (the subgroups of E, the parity signs); no order-3 residual under Sym² T ((|a|, |b|, |b|) along every 3-cycle); 10 subgroups contain the parity grading K, and theirs are permutation patterns. Ask 2: a thread's own H¹ (Wang) reads its word: zero modes exactly when r ≡ ℓ (mod 4) (237 of 745), and every grading-breaking one is a body diagonal, B1621's tick line; a thread result |
| W43 | COMPUTED (the rule first; one run; B1620's stored fits read first and transcribed) | which trimaximal family each tensor allows. The record's frame: TM1 and TM2 under T̄ ⊗ T; under T ⊗ T no pair has a TM1 column (0 of 576) and the family is TM2 (B1620's own T ⊗ T fits are TM2's); neither under Sym² T. Where c is gauge (B₃ = {±1} × O; 98 subgroups, viable 66 / 66 / 49; O's Sym² T invariant δ): TM1 and TM2 under T̄ ⊗ T and T ⊗ T, neither under Sym² T; no twist of a 3-cycle survives Sym² T. Given Λ, P10's TM1 needs that frame and an E₆ 351. Post hoc: two family dimensions of the run's tally (1 and 3) recomputed as 0 and 2 |
| W44 | COMPUTED (the rule first; one run; one prediction failed) | the free-number count in both frames on record, B1612's data verbatim, a strict fit predicate, modal ranks, every witness kept: the CKM needs a four-dimensional family under every tensor in both frames (every smaller orbit fails the necessary block test), so the 13 are unreduced whatever the frame; the PMNS minimum is 2 under T̄ ⊗ T and T ⊗ T (TM1 or TM2), 4 under Sym² T in the record's frame, and 3 under Sym² T where c is gauge (predicted 4: one fixed entry, |U_μ3| or |U_τ3| = 1/√2, or ½), with two-dimensional families 0.0012 outside. B1620's fits regraded: its four (8, 8) families (score 0.0707) are outside the ranges, its (2, 8) families (0.3627) have strict witnesses. A reading: S(G) = V₄ ⋊ S₃ is the moves mod 2 on the parities with their signs, and a frame is the subgroup of U(3) = Aut(𝕎) the gauge group realises |
| W45 | COMPUTED (the rule first; one run; fixes in review before it, disclosed); a WEAVE result given Λ, NEGATIVE for GENESIS FK11 in its canonical reading | the triplet's index on the weave's own surface M₁,₂. T is a representation of the metaplectic cover, not a local system on M₁,₂: S̃⁴ (conjugation by a b⁻¹ a⁻¹ b) acts as −I for every lift sign, while the inner lifts give it I. The four-dimensional Dirac operator with the odd spin structure forces weight 3/2. The formula, calibrated exactly, keeps exactly the two identifications the braid relation allows. χ_{3/2}(ρ_T) = 0 and χ_½(ρ̄_T) = χ_{5/2}(ρ̄_T) = 0, with every space zero (q-expansions, gaps of nine orders); three first at weight 23/2. Post hoc: the index moves only with end data at the cusp, and n units on every component give 3n; the canonical condition is n = 0 |
| W46 | COMPUTED (the rule first; one run; every cell as predicted); a WEAVE result given Λ | every end condition the weave keeps on its own surface: W28's four puncture conditions enter along the puncture section at weight 1 (the six local solutions' modular representation, from the same lifts as T), and the cusp's uniform units shift the weight by 12. The puncture's exact sequence fixes the weights 3/2, 1, ½ (central scalars, exponents), so W45's two representations are the two extreme puncture conditions. Every χ is 0 and every space is zero, under both base spin structures; the four-dimensional index is n times the fibre's index (±3, ±1). So the record's ±3 becomes four-dimensional only with one unit of end data at the cusp (GENESIS FK10) |
| W47 | COMPUTED (the rule first; one run; a check's scope fixed in review, disclosed); a WEAVE result given Λ, NEGATIVE for a forcing | main's named arc: is one unit of end data at the weave's cusp forced? The flat line bundles on the surface are the 24 characters of the metaplectic group (the inner automorphisms die in the abelianization; S̃⁸ ↦ 24); six keep the forced weights. Every cusp exponent is an odd multiple of 1/24, so the natural cusp conditions coincide. The twisted index is 0 except −1 at r = 4 and r = 20, with actual forms behind them (q-expansions); |I| = 3 only with one cusp unit at a natural puncture condition. No forcing exists inside the weave; three needs a non-flat source at the cusp (GENESIS FK10) |
| W48 | COMPUTED (the rule first; one run; every cell as predicted); conditional on a dictionary beyond Λ (the records' torus as a worldsheet), NEGATIVE for three | the owner's outside source for the cusp's unit, tested: a source of weight w turns the triplet's index into χ_{3/2−w} (the table at w = +4 … −24, all four puncture conditions); a c = 24 source with a lattice of rank ℓ gives (24 − ℓ)/8, one mode per eight lattice-free chiral bosons; q-expansions confirm (dimensions 3, 2, 1, 0). Three needs the bosonic string's 24 lattice-free oscillators (26 dimensions); the heterotic left-movers give one; a Niemeier or Monster vacuum none |
| W49 | COMPUTED (the rule first; one run; every cell as predicted); a WEAVE result; a post-hoc READING for W50 | the weave's three are a multiplicity: T = ℓ ⊗ M, one zero mode ℓ of the spin doublet times M, the three imaginary quaternion units (the intertwiners send T's three parity lines to one line, with Q = +2 on it). Every lift acts as a scalar on ℓ times a rotation of the units (W42's 96, exactly), and the Hodge–Riemann form is 2·I on M. The puncture conditions that keep ±3 are exactly the products 0 and L₆; V2 and V4 are entangled and give ∓1: three or split. Post hoc: the inner automorphisms by a and b are not words in L and R (the braid kernel is Δ⁴ = conj(a b⁻¹ a⁻¹ b)), so on the ruled branch the parity grading is not a symmetry at a fixed τ (W50 tests it) |
| W6′ | OPEN, in part superseded (2026-10-08) | the deck kept (GENESIS FK7) and masses: OPEN. The chirality under the weave's own group is derived (W21, W22, W28); gauge chirality is UNEARNED (W25; main's v1.28 grade). The index of three on the weave's own object is W20's (not chiral) |
| W6″ | READING (group theory only) | the weave's S₄ with the golden 3-cycle and the swap fixes the TM1 column |
| W7′ (the moves) | OPEN | which moves are in the weave: the swap (GENESIS GM5c) doubles the triplet's group from 24 to 48; the sign (GM5b here, its own move on main) changes nothing on it but adds the − threads. Since W29 (P3) the counts depend on these forks (ℤ₆: −1, 1, 3, 5 under L and R; −1 or 5 with the sign), and W30 and W31 turn on the swap. Relabelled from a second "W7" on 2026-10-08 |

- **In the owner's terms (READING).**
  - The three is the shared records', not any thread's: every thread acts on the same three parities.
  - One odd-trace thread already cycles them as an irreducible triplet; every thread GENESIS's SE1 admits is such a
    thread. A thread with even trace breaks it.
  - What the weave adds is that it is one triplet for all threads; a group on it that no thread has, S₄, which is real;
    and Theorem S: three alike and separate need the third tick.
- **What W6 settles, and what it does not.**
  - The frame that reads a generation (sm:B1515's F-HE) is built on one thread's own holonomy, so the content is read
    thread by thread, and it is a thread result.
  - The weave decides how it is shared, by Theorem G, and the census reads it on every thread by rule.
  - The synthesis against the physics is `docs/THREE_GENERATIONS_AND_THE_WEAVE.md`.

## Files

- `moves_and_parities.py` → `moves_and_parities.json`: W1, every word to length 8.
- `the_common_point.py` → `the_common_point.json`: W2–W4. sympy's `solve` drops roots it cannot write in radicals, so
  the points are read from Gröbner bases. The quaternion closures are numerical on a group of 48 elements.
- `the_lines_census.py`: W6's census, one JSON line per thread. Its record is `the_lines_census.json`, with the order-3
  pass in `the_lines_census_order3.json`.
- `the_lines.py` → `the_lines.json`: Theorem G checked on every member orbit.
- `the_lines_content.py` → `the_lines_content.json`: what each parity carries.
- `the_mixing.py` → `the_mixing.json`: the weave's group on the triplet and the mixing of its subgroups (READING).
- `the_weaves_laws.py` → `the_weaves_laws.json`: the trichotomy along the wave, the triplet's group (T_d, O_h, real), and
  Theorem S, for `docs/THE_WEAVES_LAWS.md`.
- `draft_chiral_counts/DESIGN_FOR_REVIEW.md`: the design sent to main. It was sealed as sm:B1552 on the owner's ruling,
  ahead of main's review (W11).
- `the_hand_theorem.py` → `the_hand_theorem.json`: W15, Theorem H's ingredients on the generators, the tick-3 act on every odd-trace state to length 8, and the hand rule from the determinant on all 758 states to length 12.
- `the_weave_extension.py` → `the_weave_extension.json`: W15, the weave's own extensions: the census to length 6, two further primes, and length 8 under the reduced rule.
- `W15_PREDICTION.md`: the mod-16 prediction, committed before its test; `the_prediction_test.py` → `the_prediction_test.json`: its second part, F-CI on ±LLLLLRRR with the control ±LLLLLLLR.
- `the_common_point_mod_3.py` → `the_common_point_mod_3.json`: W16, main's B1601 on this seat's route (the point at 1 200 digits or more, the field checked exactly, the ideal at the primes of the norm gcd), 37 geometries.
- `the_weaves_five_tick1.py` → `the_weaves_five_tick1.json`: W17, the weave's SU(5)′ five on the thread itself, every odd-trace state to length 8.
- `W18_PREDICTION.md`: the per-parity prediction, committed before its test; `the_parity_generations.py` → `the_parity_generations.json`: W18, the five's sectors on the forced cover by Shapiro (32 states) and directly at the resolving tick (twelve states).
- `the_parity_generations_special.py` → `the_parity_generations_special.json`: W18, post hoc: the whole line of gluing classes on every carrier over GF(73) and GF(97), two special classes on each.
- `W20_RULE.md`: the rule, committed before the census; `the_weaves_count_in_e6.py` → `the_weaves_count_in_e6.json`: W20, the weave's Euler characteristic with coefficients in E₆'s 27 under every SL(2) in E₆.
- `the_weaves_count_orbifold.py` → `the_weaves_count_orbifold.json`: W20's third route, Brown's formula over the elliptic elements, with the traces at the square and hexagonal tori.
- `W21_RULE.md`: the rule, committed before the run; `the_holomorphic_triplet.py` → `the_holomorphic_triplet.json`: W21, the Hodge–Riemann form on V and on the spin doublet by the cup product, its controls, and which triplet is holomorphic (`--controls` runs the controls alone).
- `the_e8_frames_on_the_fibre.py` → `the_e8_frames_on_the_fibre.json`: W23, the record's E₈ frames on the fibre over every bundle built from the common point's blocks.
- `the_couplings_verified.py` → `the_couplings_verified.json`: W38, main's B1615 and B1616 recomputed (a verification, not blind).
- `CONVENTIONS.md`: the dossier's conventions, enforced by `tests/test_weave_conventions.py`; `tests/test_weave_regeneration.py` reruns the fast scripts against their stored outputs.
- `W49_RULE.md`: the rule, committed before the code; `the_generations_are_a_multiplicity.py` → `the_generations_are_a_multiplicity.json`: W49, the triplet as ℓ ⊗ M (the intertwiners on T's parity lines, the lifts in the basis t_p, the Hodge–Riemann form, the puncture conditions in ρ_Q ⊗ M, and four extra read-outs).
- `W48_RULE.md`: the rule, committed before the code; `the_outside_source_at_the_cusp.py` → `the_outside_source_at_the_cusp.json`: W48, the outside source's dressing law and the c = 24 candidates (the weight law at the four puncture conditions, the lattice and oscillator families, q-expansion dimensions, and the analytic facts).
- `W47_RULE.md`: the rule, committed before the code; `the_unit_at_the_weaves_cusp.py` → `the_unit_at_the_weaves_cusp.json`: W47, every flat line bundle and every natural cusp condition on the weave's surface (the abelianization, the cusp exponents, the twisted index by the formula and by q-expansions, and the full table with cusp units).
- `W46_RULE.md`: the rule, committed before the code; `the_end_conditions_on_the_weaves_surface.py` → `the_end_conditions_on_the_weaves_surface.json`: W46, every end condition the weave keeps on its own surface (the six local solutions' modular representation, the puncture's exact sequence, the formula, q-expansions, and the table by puncture condition and cusp units).
- `W45_RULE.md`: the rule, committed before the code; `the_index_on_the_weaves_surface.py` → `the_index_on_the_weaves_surface.json`: W45, the triplet's index on the weave's own surface (the structure on Aut⁺(F₂), the formula's calibrations, the four identifications, and the dimensions by q-expansions).
- `W44_RULE.md`: the rule, committed before the code; `the_free_numbers_by_frame.py` → `the_free_numbers_by_frame.json`: W44, the free-number count in both frames on record with a strict fit predicate, and B1620's PMNS fits regraded; `received/B1612_data.json`: B1612's data transcription, verbatim (sha256 as in its ARTIFACT_HASHES).
- `W43_RULE.md`: the rule, committed before the code; `the_trimaximal_families.py` → `the_trimaximal_families.json`: W43, the trimaximal families each tensor allows in the record's frame and where c is gauge; `received/B1620_post_seal_tensors.json`: B1620's stored fits, verbatim (sha256 as in its ARTIFACT_HASHES); POST HOC `the_trimaximal_families_posthoc.py` → `the_trimaximal_families_posthoc.json`: two outlying family dimensions recomputed.
- `W42_RULE.md`: the rule, committed before the code; `the_breaking_verified.py` → `the_breaking_verified.json`: W42, main's B1620 recomputed exactly (the lattice, the three tensors, K; a verification, not blind) and the census of every thread's own zero modes.
- `W41_RULE.md`: the rule, committed before the code; `the_zero_modes_weight.py` → `the_zero_modes_weight.json`: W41, the zero modes' weight by the norm and by the theta laws.
- `the_weave_at_omega_verified.py` → `the_weave_at_omega_verified.json`: W40, main's B1617 recomputed, given τ = ω (a verification, not blind).
- `the_couplings_exact.py` → `the_couplings_exact.json`: W38's exact addendum (post hoc): the normal form of the group on T, Heron's identity on B1615's family, and each residual's whole fixed space.
- `the_tm1_prediction_and_observer_layer_verified.py` → `the_tm1_prediction_and_observer_layer_verified.json`: W37, main's B1613 and B1614 recomputed (a verification, not blind).
- `the_sm_centralizer_in_e8.py` → `the_sm_centralizer_in_e8.json`: W36, the Standard Model's centralizer in E₈ by exact root arithmetic (a review of the audit lane's step 1).
- `the_mixing_patterns_verified.py` → `the_mixing_patterns_verified.json`: W35, main's B1612 rebuilt from W21's construction (a verification, not blind).
- `the_observer_layer_on_the_weave.py` → `the_observer_layer_on_the_weave.json`: W34, B761's private states on GENESIS's 758 states (SnapPy, 60 digits), the private states at the common point and what the moves keep (exact), the self-name among the threads against the reversal pairs, and the register's lifts and action at the common point; its rule `W34_RULE.md`, committed first. POST HOC `the_observer_layer_posthoc.py` → `the_observer_layer_posthoc.json`: the 11 states the run's rank rule left undecided, recomputed from the polished holonomy at 120 digits.
- `the_odd_spin_structure_across_frames.py` → `the_odd_spin_structure_across_frames.json`: W33, the census of bundles from the common point's blocks in E₆, SO(10) and SU(5) under the block rule, naturality and the spinor rule, the naive law, the spinor-rule law, the doublet sectors and the sources of each three; its rule `W33_RULE.md`, committed first.
- `the_puncture_content.py` → `the_puncture_content.json`: W32, the census of rank-5 bundles from the common point's blocks that L and R keep, read in F-HE's two sectors under naturality, locality and W22's block rule, with the completion lemma and what three would need; its rule `W32_RULE.md`, committed first.
- `the_z5_twist_eater.py` → `the_z5_twist_eater.json`: W31, the ℤ₅ flux in E₈ ⊃ (SU(5)_g × SU(5)_b)/ℤ₅ (the group, the centraliser, the matter, the hypercharge and the orientation, the moves at the puncture, the counts for every flux); its rule `W31_RULE.md`, committed first.
- `the_order_three_flux.py` → `the_order_three_flux.json`: W30, the puncture in every Sym^n of the forced point, the qutrit class and the moves on it (the swap's fork), the moves on the qutrit's ℂ³, the record's order-3 structures re-read; its rule `W30_RULE.md`, committed first.
- `the_z6_twist_eater.py` → `the_z6_twist_eater.json`: W29, the ℤ₆ twist-eater in E₈ (the group, the centralisers, the matter by type, the flux and the orientation, the moves at the puncture, the anomalies); its rule `W29_RULE.md`, committed first; `the_z6_twist_eater_posthoc.py` → `the_z6_twist_eater_posthoc.json`, after the read-out: the lifts of −I and of (LR⁻¹L)², and which splits the 6.
- `the_three_routes_and_the_qubit.py` → `the_three_routes_and_the_qubit.json`: W28, the end condition's index sets under the moves, the flavor group, the grading and locality, and the common point as the qubit (Pauli, Clifford, SU(2)₁, the global forms, the twist-eater); its rule `W28_RULE.md`, committed first.
- `the_link_tested.py` → `the_link_tested.json`: W27, the link's tests (anomalies, the count under the link, the six-dimensional global condition, the 27's remainder); its rule `W27_RULE.md`, committed first; the write-up `docs/THREE_GENERATIONS_GIVEN_ONE_LINK.md`.
- `the_weaves_mirror.py` → `the_weaves_mirror.json`: W26, the mirror closure of the weave (exact), the threads' volumes and Chern–Simons against their mirrors (SnapPy), and the order-3 orientation tick by tick; its rule `W26_RULE.md`, committed first.
- `the_self_conjugate_weave.py` → `the_self_conjugate_weave.json`: W25, the Frobenius–Schur indicators of the weave's forced holonomies and the centralisers in E₈ of Q₈, of one parity's element and of the odd-trace extension; its rule `W25_RULE.md`, committed first.
- `the_six_dimensional_census.py` → `the_six_dimensional_census.json`: W24, the six-dimensional census (the character variety, the local orbifolds, the gauge side, and the audit of W22); its rule `W24_RULE.md`, committed first.
- `the_puncture_condition.py` → `the_puncture_condition.json`: W22, the moves' lifts at the puncture (2O, irreducible in every parity block), the threads' eigenlines, and the spin structure every move fixes.
- `the_holomorphic_triplet_periods.py` → `the_holomorphic_triplet_periods.json`: W21's second route, after the read-out: the holomorphic twisted forms θ₃(z | 2τ)/√θ₁(z | τ) and their periods at three τ, the holomorphic subspace (T at every τ, the same subspace), and the twisted Riemann bilinear relation.
- `the_weaves_five.py` → `the_weaves_five.json`: W15, the spin doublet extended by the three parity lines, read with F-HE's pair.
- `the_slope_law.py` → `the_slope_law.json`: W14, the slope law against the engine and F-CI's census on every odd-trace
  state to length 6; `the_slope_law_sample.py` → `the_slope_law_sample.json`: the law on 300 of +LLRLRR's modules.
- `the_class_index_orbits.py` → `the_class_index_orbits.json`: W13, main's B1434 odd-trace rows on this seat's engine.
- `the_joined_vacuum.py` → `the_joined_vacuum.json`: W12, the joined vacuum's structure on the 24 states to length 6
  (50 digits).
- `the_spin_zero.py` → `the_spin_zero.json`: W11. sm:B1509's T2 checked on sm:B1552's record, and T3's hypothesis on
  every state to length 12.
- `the_chiral_triplet.py` → `the_chiral_triplet.json`: W10, the group on the parity-twisted spin space, its two
  conjugate triplets, and where a single vacuum character carries one alone.
- `the_spin_hand.py` → `the_spin_hand.json`: W9's hand rule on all 758 states to length 12, and the states that are
  their own mirror.
- `the_spin_room.py` → `the_spin_room.json`: W9, the spin doublet's group, every state's room on it, the
  parity-twisted doublets at the resolving tick, and the route-2 control.
- `the_weaves_vacuum.py` → `the_weaves_vacuum.json`: W8, the frame at the weave's vacuum on all 24 states at their
  resolving tick (exact).
- `the_parity_sectors.py` → `the_parity_sectors.json` (raw lines `the_parity_sectors.jsonl.gz`, sha-256 beside it):
  W7, R2 of the laws in Theorem S's sense; complete, 24 of 24, one pass.
