# The weave: what the joint action of every allowed move forces on every thread at once

cc (the SM-derivation seat), 2026-10-07. **Structure and proofs only. No count is read.** Written for the owner's rule,
stated daily for a year and given a fixed name today, **the weave** (`docs/THE_WEAVE.md`). The rule: reality comes from
the interaction of all the objects the principle allows, together, and not from single objects or from covers of one.
- A **thread** is one allowed object, a closed path of moves through the shared fibre.
- **The weave** is the joint action of all the moves on that fibre, and what it forces.

Nothing below is read off one thread. Each step is PROVED here and checked by the scripts beside this note, unless it is
marked READING or OPEN. Nothing is promoted, and 0 of 19 stands.

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
| W6′ | OPEN | the deck kept (GENESIS FK7); the chirality (the extension's order decides generation against anti-generation); one module of index three (the smooth standard) |
| W6″ | READING (group theory only) | the weave's S₄ with the golden 3-cycle and the swap fixes the TM1 column |
| W7 | OPEN | which moves are in the weave: the swap (GENESIS GM5c) doubles the triplet's group from 24 to 48; the sign (GM5b here, its own move on main) changes nothing on it but adds the − threads |

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
