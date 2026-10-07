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
| +LLLRRR | 11 | 1024, none | running |
| −LLLRRR | −11 | 256, none | running |
| +LLRLRR | 15 | running | running |
| −LLRLRR | −15 | 256, none | running |

**Status at this commit: eleven of twelve threads read at order 4, and eight at order 3. The rest are running, and this
table is completed when they finish.**

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

## What the weave gives, and what it does not

| step | status | what |
|---|---|---|
| W1 | PROVED | three non-zero parities, permuted with none distinguished only when moves act together |
| W2 | PROVED | one structure all threads share: the quaternion point |
| W3 | PROVED | on every odd-trace thread, the same A₄ and the same 2T from it |
| W4 | PROVED | one irreducible triplet, the same on every odd-trace thread; even-trace threads split it; the weave's group on it is real (T_d ≅ S₄; O_h with P) |
| S | PROVED | Theorem S (`docs/THE_WEAVES_LAWS.md`): no state has its three parities separate and carried into one another at its own tick; every odd-trace thread has them so at every third tick |
| W5 | READING (main's GENESIS FK14; GENESIS FK7) | the three generations are this triplet at every third tick: three, alike, carried into one another by the deck, which is the shift by one tick |
| W6 | PROVED (WEAVE); COMPUTED (THREAD) | Theorem G: whatever one parity carries, all three carry. A thread result: on +LR each parity carries one generation of each type. The census: no other odd-trace thread to length 6 read so far carries any on its forced cover (eleven of twelve at order 4) |
| W7 | COMPUTED (WEAVE, by rule) | in Theorem S's sense, at every state's resolving tick to length 6: members only on the pair of parities a state's symmetry exchanges (±LLRR, ±LLR, ±LLLLR), never on the parity it fixes, never on all three |
| W8 | PROVED (Lemma V, WEAVE + WAVE); COMPUTED | the frame at the weave's own vacuum (the common point) reads rank-one lines: the three parity lines alike on every thread, all on the end; no member on any state at any tick |
| W9 | COMPUTED (WEAVE, two routes) | the weave's spin doublet H¹(F₂; ρ_Q): the moves act by ℤ/8 (Q₁₆ with the swap); every thread has interior classes on it; twisted by the parities, three alike interior sectors on every odd-trace thread at tick 3 |
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
- `the_spin_room.py` → `the_spin_room.json`: W9, the spin doublet's group, every state's room on it, the
  parity-twisted doublets at the resolving tick, and the route-2 control.
- `the_weaves_vacuum.py` → `the_weaves_vacuum.json`: W8, the frame at the weave's vacuum on all 24 states at their
  resolving tick (exact).
- `the_parity_sectors.py` → `the_parity_sectors.json` (raw lines `the_parity_sectors.jsonl.gz`, sha-256 beside it):
  W7, R2 of the laws in Theorem S's sense; complete, 24 of 24, one pass.
