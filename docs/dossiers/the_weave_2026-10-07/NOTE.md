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
- Two checks follow the close: W30 (is an order-3 flux forced?) and W31 (the ℤ₅ flux).

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
| W6′ | OPEN, in part superseded (2026-10-08) | the deck kept (GENESIS FK7) and masses: OPEN. The chirality under the weave's own group is derived (W21, W22, W28); gauge chirality is UNEARNED (W25; main's v1.28 grade). The index of three on the weave's own object is W20's (not chiral) |
| W6″ | READING (group theory only) | the weave's S₄ with the golden 3-cycle and the swap fixes the TM1 column |
| W7′ (the moves) | OPEN | which moves are in the weave: the swap (GENESIS GM5c) doubles the triplet's group from 24 to 48; the sign (GM5b here, its own move on main) changes nothing on it but adds the − threads. Since W29 (P3) the counts depend on these forks (ℤ₆: −1, 1, 3, 5 under L and R; −1 or 5 with the sign), and W30 turns on the swap. Relabelled from a second "W7" on 2026-10-08 |

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
