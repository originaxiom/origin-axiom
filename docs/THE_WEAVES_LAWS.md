# THE WEAVE'S LAWS — what holds across every thread and every tick, and what it could mean

cc (the SM-derivation seat), 2026-10-07. The owner, verbatim:
- "should we give a read to our law and theorem ledger/register ... will it help?";
- "most of them could be about m004, therefore keepnin mind not to repeat the mistake we do. we should recheck what applies
  to the whole weave and "wave"";
- "we should also see what law / theorem is valid across the threads so we can read what couldnit mean".

**The method.** Three read-only reviews of the record's registers ran the same day:
- the theorem registry (this branch and main's), the theorem ledger, the claims, the law map, the kind table, and the
  derivation and identification records;
- THE_SPINE and the verdict ledger (this branch and main's);
- the SM verdict, the hint ledger, the lead register, the open leads and GENESIS (this branch's v1.10 and main's v1.23).

**The tags.** Every entry bearing on the generations was tagged with one of three:
- **WEAVE:** proved or checked for every thread (state) of a stated kind, or for every move;
- **WAVE:** proved or checked at every tick (level, monodromy φⁿ);
- **THREAD:** one manifold (usually m004, "the object") or a hand-picked list.

Only WEAVE and WAVE entries are listed as laws (§1). The thread results that look universal are in §2. The reading in §3
is kept apart from the laws and marked READING. Two laws are new here (Theorem S and the trichotomy), checked by
`docs/dossiers/the_weave_2026-10-07/the_weaves_laws.py`. Nothing is promoted, and 0 of 19 stands.

**A unit, named (GENESIS's rule that a count over states names its unit).**
- **States.** A GENESIS state is a primitive signed cyclic word in L and R, up to rotation and the L↔R swap. There are
  758 to length 12.
- **Words.** The weave dossier's W1–W3 counts (2,554 to length 8) are words in L, R and P up to rotation only. They are
  words, not threads: LPLP and LR are one matrix (m004), and LRLR is m004's second level.
- **Why the words are safe.** W1–W3 are statements about each word's matrix mod 2, so they hold for every word. Where a
  number of threads is meant, it is a number of states.

## 1. The laws

### 1a. The three and its symmetry

| law | statement | population | how | tag |
|---|---|---|---|---|
| W1, the parities | The records have three non-zero parities. Each of L, R and P fixes a different one; any two of them generate all six permutations (GL(2, F₂) = S₃); a thread cycles all three exactly when its trace is odd | every word; 2,554 words to length 8 | proof, with enumeration | WEAVE |
| **the trichotomy (new)** | φ acts on the parities through φ mod 2 ∈ S₃, and its class is fixed by the trace: a 3-cycle (one orbit) at odd trace; an involution (a line and a pair) at even trace with φ ≢ I mod 2; the identity (three lines) at φ ≡ I mod 2. At tick n the class is that of (φ mod 2)ⁿ. So an odd-trace thread has one orbit at ticks 1, 2, 4 and 5, and three lines at ticks 3 and 6 | 758 states to length 12: 326, 268 and 164 in the three classes; every integer matrix of determinant ±1 with entries of size ≤ 6 | proof; checked | WEAVE + WAVE |
| **Theorem S (new)** | At its own tick, no state has its three parities both separate and carried into one another by a symmetry. They are separate only when φ ≡ I mod 2, and then the state's isometries act on them through a group of order at most 2. At every third tick of every odd-trace state they are both: separate, and cycled by the deck | the 164 states with φ ≡ I mod 2 to length 12: 54 split 1 + 2, 110 split 1 + 1 + 1, none 3 | proof (below); checked | WEAVE + WAVE |
| W2, the common point | With the puncture parabolic, the quaternion point a ↦ i, b ↦ j is the one point of the fibre's characters that every move fixes. Every thread shares it. Its uniqueness already holds for one shear | every move | proof (Gröbner bases) | WEAVE |
| W3, the image | The common point extends over every thread. The image is 2T, Q₁₆ or Q₈ by the trichotomy's class, and A₄, D₄ or V₄ modulo ±1 | 2,554 words; a mod-2 proof | proof | WEAVE + WAVE |
| W4, the triplet's group (corrected here) | The parity-twisted cohomology is one triplet. L, R and the fibre's translations act on it as T_d, which is S₄ of order 24: L and R are reflections and −1 is not in it. The sign −I acts as the translation by ab and adds nothing. The swap P doubles the group to O_h (48). Every element is conjugate to its inverse, so all characters are real. One odd-trace thread with the fibre gives A₄ (12), which has a complex pair of characters | the moves | proof; computed | WEAVE |
| the direction is a marking | Conjugating by L (the change of marking LR → RL, one manifold) carries a thread's 3-cycle into the class of its inverse | every odd-trace thread | proof; computed on ±LR | WEAVE |
| Theorem G | On the forced A₄ cover of every odd-trace thread, a member orbit sits a third on each parity, and on the third level it gives one sector per parity, cycled by the deck, each with the member's count | every odd-trace thread | proof (Shapiro) | WEAVE, at tick 3 |
| **Lemma V (new)** | On a hyperbolic once-punctured-torus bundle no rank-one line is interior: h¹(ν) ≤ 1, and when it is 1, ν is trivial on the cusp and the class restricts to it injectively (finite order needed only when ν is trivial on the fibre). So the frame at the weave's own vacuum, the common point, whose module four(ρ_Q) = 1 ⊕ 3 is a sum of such lines by Shapiro, has no member on any state at any tick | every state at every tick; 72 parity lines and 768 characters of order dividing 4 on the 24 states to length 6 at their resolving tick | proof (Wang sequence; the puncture loop); checked exactly | WEAVE + WAVE |
| **the spin doublet (new)** | The fibre's cohomology with coefficients in the common point, H¹(F₂; ρ_Q), is two-dimensional and every thread's class in it is interior (ρ_Q([a, b]) = −1). L and R act on it as commuting rotations (cyclic of order 8; Q₁₆ with the swap), so every thread acts with finite order and has interior classes; twisted by the parities, the three are alike for every lift at the resolving tick of every odd-trace and every involution state | 24 states to length 6; route 2 (Fox calculus) on five | computed | WEAVE |
| **the hand rule (new)** | The spin doublet's two conjugate lines sit at different κ exactly when n_L − n_R + 2·[sign −] ≢ 0 (mod 4); on every state that is its own mirror, the + state keeps them together and the − state apart, which is main's B1479 read off another object | 758 states to length 12 (34 own-mirror words, 68 states) | computed, against the formula | WEAVE |
| **the chiral triplet (new)** | On the three parity-twisted spin doublets V (six-dimensional, every class interior) L and R act through a group of order 96 with V = T ⊕ T̄, two irreducible complex-conjugate triplets; the swap exchanges them (order 192, V irreducible). At tick 3 of every odd-trace state T's three classes sit at one κ and T̄'s at κ̄; κ ≠ κ̄ on exactly one sign twin of each odd-trace word (n_L − n_R + 2·[sign −] ≡ 2 mod 4), where one vacuum character carries T alone | the moves; 24 states to length 6 | computed | WEAVE |
| the gcd law (lifted) | An orbit of the forced cover is one module at the ticks 3 does not divide and three sectors at every third tick. That is B1507's gcd(n, 3), lifted from m004 to every odd-trace thread by the trichotomy | every odd-trace thread, every tick | proof | WEAVE + WAVE |

**Theorem S, the proof.**
- **Separate needs the identity mod 2.** On a state M with monodromy φ, a parity is a sector of its own exactly when the
  base loop fixes it, that is, when φ mod 2 fixes it. All three are separate exactly when φ ≡ I mod 2.
- **Symmetries.** M's isometries keep its one fibration (b₁ = 1). So they are the g in GL(2, ℤ) with gφg⁻¹ = φ^±1, acting
  on the parities as g mod 2.
- **Those that keep the base's direction** form the centralizer of φ, a unit group ±η^k of a real quadratic order.
  - **φ = ±ηᵐ** with m = 1, or m = 2 when η has determinant −1. A larger m would make φ's cyclic word a proper power,
    and the cyclic word of a hyperbolic class is unique (Salepci, as GENESIS §3 uses it).
  - **So η² ≡ I mod 2,** and η mod 2 has order at most 2.
- **Those that reverse the base's direction.** Each such g has g² in the centralizer, so g mod 2 has order at most 2.
  - **The product of two distinct transpositions of S₃ is a 3-cycle.** Its square is again a 3-cycle.
  - **So all these images are one transposition at most,** and the image group has order 1 or 2. □
- **At the third tick of an odd-trace state,** the monodromy is φ³ ≡ I mod 2. The deck φ, with φ mod 2 a 3-cycle, is in
  the centralizer of φ³. This is the case the proof excludes for states: φ³ is not primitive.
- **The check.**
  - `the_weaves_laws.py` finds the normalizer's images on all 164 states with φ ≡ I mod 2 to length 12.
  - The commuting elements come from a Pell equation; the reversing ones are the trace-zero solutions.
  - The tally (54 and 110) is the same with the search bound at 60 and at 200.

### 1b. What a count can be: the record's laws proved for every state or tick

| law | statement (quoted or condensed) | where | tag |
|---|---|---|---|
| GENESIS T-ROOT | "the torsion of H₁ has order abs(2 − tr) for orientation-preserving monodromy and abs(tr) for orientation-reversing" | GENESIS §4 | WEAVE |
| GENESIS levels | the n-th level's torsion has order abs(2 − tr φⁿ), "also the number of fibre characters its monodromy fixes" | GENESIS §3 | WEAVE + WAVE |
| B1385 T1 | "No word state has a free cusp (one cusp, b₁ = 1, closed under concatenation and fibre-cyclic covers)" | `docs/OPEN_LEADS.md` | WEAVE + WAVE |
| B1369, H-FREE-CUSP | "a chiral generation from bulk matter with the Standard Model unbroken needs a free cusp" | `docs/HINT_LEDGER.md` (22) | WEAVE + WAVE |
| B1351 | "χ(Q; L) = 0 for every local system on a closed 3-manifold" | `docs/THE_VERDICT_OF_THE_OBJECT_2026-09-16.md` | WEAVE + WAVE |
| B1291 | no fixed-locus count of 3 on any one-cusped manifold | `docs/OPEN_LEADS.md` | WEAVE + WAVE |
| B307 | "no hyperbolic knot has a C₃ trace field ... 3 must be relational" | `docs/HINT_LEDGER.md` | WEAVE |
| E65 | a holonomy through SL(2) → E₆ has "net chirality identically zero — for every embedding" | `docs/THE_SM_VERDICT.md` | WEAVE |
| B356 | chiral candidates at character level exist only for A₄ and 2T; "S₄/2O/A₅/2I closed by the reality theorem" | `docs/HINT_LEDGER.md` | WEAVE |
| main's B1440 | no flat bundle of rank n counts more than ⌊n/2⌋ on a once-punctured-torus bundle, so rank five never counts three; every level is such a bundle | main, S29 | WEAVE + WAVE |
| main's GENESIS GAP2 | "no state of X_gen carries three generations in either frame, by counting ends, not by search" (one module, the state's own level) | main's GENESIS v1.23 | WEAVE |
| Theorem C (sm:B1535) | N(5̄′) ≤ n(ν³ ⊗ ρ) and N(10′) ≤ b0 + n(ν⁴) at a finite-order member on any finite cover | GENESIS F-HE (main v1.16) | WEAVE + WAVE |
| Lemma W, Corollary C1 (sm:B1535) | n(ν⁴) = 0 on every finite abelian cover of a word state at characters trivial on the puncture loops, so at most one generation there | `docs/OPEN_LEADS.md` | WEAVE + WAVE |
| Lemma F′ (sm:B1545) | I(W₁) ≥ k − m_A − b0 at every finite-order member | `docs/OPEN_LEADS.md` | WEAVE + WAVE |
| main's mirror laws | the class index is mirror-even for every module; ind(V) ≠ ind(V̄) only for n ≡ 2 (mod 4) | main's GENESIS v1.23 | WEAVE |
| main's sign (B1482) | the − states need exactly the central −I, which "words in L, R and P never give"; positivity (GENESIS GM5d, CHOSEN) is what excludes it | main's GENESIS v1.14 | WEAVE |
| main's Proposition 1 | every word state has a canonical cover with abs(2 − tr φ) ends; three ends exactly on L³R | main's GENESIS v1.23 | WEAVE |
| main's room laws | T-COMPANION-NO-ROOM; T-ROOM-NEEDS-GENUS: room is zero at fibre genus one, so it needs a non-abelian cover of degree ≥ 3 | main's GENESIS v1.23 | WEAVE + WAVE |

### 1c. Bounded censuses: laws by rule, not by proof

- **The grammar's census.** 758 states and 536 manifolds to length 12 (GENESIS §3).
- **F-CI.** 95 of 758 states carry a generation-shaped background at their own level (GENESIS).
- **No index near the hyperbolic point.** None on any word state to length 12, nor at levels M₂–M₆ (sm:B1527, sm:B1529).
- **The amphichiral − states.** To length 12, the − state is the one on which no spin structure survives the mirror
  (main's GENESIS v1.13).
- **The founding field.** ℚ(√−3) occurs only on ±(LR)ᵏ, among 154 states to length 8 (B1385 T3).
- **Orbits of three.** Ten of the twelve three-fold levels to length 6 carry orbits of three (main's B1434).
- **The three-ended covers.** Ten states (sm:B1549).
- **The forced A₄ cover.** The twelve odd-trace states to length 6 (W6). Members are only on ±LR, and generations only on
  +LR. The census is complete at orders 4 and 3.

## 2. What looks universal and is one thread's

| claim | where | its population | what the weave says now |
|---|---|---|---|
| each parity of +LR carries one generation of each of six types | sm:B1550; W6 | THREAD: +LR's forced cover | Theorem G makes it shared by the three parities on any thread. The content is +LR's. On the forced cover no other odd-trace thread to length 6 has a member, but other covers of other threads carry content (sm:B1549: +LLLR's L8a15 and −LLLLLR's three-ended covers carry three; sm:B1530: the silver pair ±LLRR carry one at their own level) |
| one generation at the hyperbolic point on the silver pair | sm:B1530 | THREAD: ±LLRR at their own tick | read by parity after the fact, from the banked record. On m135 at κ = 1 the two members that read (−1, −1) are characters whose fibre restrictions are (0, ½) and (½, 0); the one at (½, ½) is simple and reads (0, 0). On m136 at κ = −1 the members are at the same two, and there is none at (½, ½). In the word's marking the silver threads' isometries act on the parities by exactly the swap of the first two (`the_weaves_laws.py`). So the generation is on the pair the thread carries into one another, and the third parity reads none: Theorem S's 1 + 2, with the content on the 2 |
| "the level question has become one bit: is the root's deck gauged (one, on m004) or kept (three, on s961)?" | B1506, B1507 | THREAD: m004's levels | WEAVE + WAVE now (trichotomy, Theorem S, the gcd law). It is the one bit for every odd-trace thread, not m004's |
| "the image is A₄ (irreducible) iff 3 ∤ n and V₄ iff 3 ∣ n" | B1274 | THREAD: m004's closed tower, n ≤ 6 | the trichotomy proves it on every odd-trace thread at every tick |
| the deck's ℤ/3 is irreducible on the Klein group, so exact tri-bimaximal mixing, with the breaking external | B343 | THREAD: m004's deck | holds on every odd-trace thread (W1). The weave offers residual symmetries inside it (a READING; `docs/THREE_GENERATIONS_AND_THE_WEAVE.md` §3) |
| m004 maps onto 2T in exactly two ways, as do a third of the census manifolds | B993 | m004 and a census of census manifolds | W3: the common point extends over every odd-trace thread with the two choices ±g |
| "4₁ is a one-generation object" | B298; H54 | THREAD: m004 | at its own tick every state is: main's GAP2 for one module, Theorem S for the parities |
| character-distinguished generations are zero-diagonal; a hollow texture is refuted | B1273, B1361 | THREAD: m004's tower; the algebra is general | parity sectors are character-distinguished on every thread. A kept, unbroken deck gives the refuted texture on every thread: the deck must break at order one, or the Higgs must be parity-neutral |
| the triplet's Yukawa is ε_ijk, so zero | B1271 | THREAD: m004's E₈ family tensor | not lifted. On the weave's T_d the invariant cubic is xyz, not ε_ijk, and with P neither is invariant. Recheck R15 |
| the object "withholds a chiral generation" for every hyperbolic knot complement | the verdict of the object | THREAD: checked on m004 | among the states only +LR is a knot complement. Recheck R12 |
| three generations force Pin⁺ | B1383 | THREAD: m004 and m000 | recheck R8 |
| L³R is the only state with three ends | main's GENESIS v1.22 | WEAVE (a proof) | a competing "why three": ends, not parities. Main reads both mechanisms as needing FK14 (main's GENESIS v1.23) |

## 3. What the laws could mean together (READING)

1. **The three is the records', not a thread's.** The two records have 2² − 1 = 3 non-zero parities, and every thread acts
   on the same three (W1). No thread is chosen. Every thread of odd trace cycles them (the trichotomy), and every thread
   GENESIS's SE1 admits is such a thread.
2. **Alike and distinct need the wave.**
   - At its own tick no state has the three both separate and carried into one another (Theorem S).
   - At every third tick of every odd-trace thread they are both, and what carries them is the deck: the shift by one tick.
   - If the generations are the parities, they are the three phases of the breath, the wave programme's act.
   - Whether the phases are three things or one thing seen three times is one bit for the whole weave: the deck kept or
     gauged, GENESIS FK7.
   - B1506 found this bit on m004. The trichotomy and Theorem S show it is the same bit on every odd-trace thread, and
     that no state avoids it at its own tick.
   - Its fence stays (B1506, B1384): the three sectors are three vacua, and reading them as three generations needs the
     whole orbit in one configuration, which GENESIS does not derive ("All legal states are physically realised
     together | NOT DERIVED").
   - **The third tick is not chosen by hand: it is the weave's cover, seen on each thread.**
     - The joint action of the moves on the parities is S₃ = SL(2, F₂). Its kernel is the congruence subgroup Γ(2),
       which is defined by all the moves together, not by any thread.
     - Restricted to a thread, the kernel cuts out the cover whose deck is ⟨φ mod 2⟩. That is the thread's tick 3 on an
       odd-trace thread, its tick 2 on an involution thread, and the thread itself when φ ≡ I mod 2.
     - So the one rule gives every thread at once the tick at which its parities separate (the trichotomy).
     - The parities are alike there only when the thread's own share of S₃ is transitive, which happens on the odd-trace
       threads.
     - A thread's own loops act on the parities through a cyclic part of S₃.
       - When φ ≡ I mod 2 the parities are separate, and its isometries add at most a transposition (Theorem S).
       - When φ is a 3-cycle they are alike, but they are one orbit of its loops, so not separate.
     - Three alike and separate at once belongs to the joint action, and to the cover it cuts out on each thread.
     - That is the owner's rule as a theorem about the parities: the property that makes three generations three alike
       things belongs to the interaction, not to an object.
     - What it leaves open is the same bit: whether the weave's cover is kept (GENESIS FK7).
   - **READING: the weave's answer to that bit.**
     - The moves themselves tell the three parities apart: L, R and the swap each fix a different one (W1). So the
       parities are labels the grammar can read, not a redundancy of the description.
     - A label the grammar reads is single-valued on a state only where the act fixes it, and that is the cover the
       weave's congruence kernel cuts out, the resolving tick.
     - So the weave reads the deck that permutes the labels as kept: a flavour symmetry, not a gauge redundancy.
     - The step from "the grammar can read it" to "it must be single-valued" is a principle, not a theorem. It is offered
       for GENESIS FK7, not claimed.
3. **Three is a sum, never one module.**
   - Rank five counts at most two on any once-punctured-torus bundle at any tick (B1440).
   - One module at a state's own level never counts three (main's GAP2).
   - Pulled-back members carry at most one generation (Corollary C1).
   - So three is a sum of sectors (main's orbifold standard) or a module of rank ≥ 6.
   - The weave's three is a sum of sectors. Its cover is forced by the parities, not chosen by a character. Main still
     counts any three found on a cover's own characters as a selection until its FK14 is ruled.
4. **The three carries no hand.**
   - The weave's group on the triplet is real: S₄ = T_d without P, O_h with it.
   - One thread's A₄ has a complex pair of characters, the only place B356 allows a hand. Which member of the pair is
     which, though, is a marking: LR against RL, one manifold.
   - So chirality is not in the three. It must come from elsewhere:
     - main's sign (B1479–B1483: the − state is where a hand can be registered);
     - the register's order (GENESIS FK12);
     - a source (GENESIS GAP3).
   - By T1 and H-FREE-CUSP it cannot come from bulk matter with the Standard Model unbroken, on any state at any tick.
   - The three and the hand are separate ingredients.
5. **The weave's own vacuum: its abelian part is empty, its spin part is not, and with the parities it carries a chiral
   three (W9, W10).**
   - **The abelian part (Lemma V).** At the common point, the one vacuum every move fixes, F-HE's module four(ρ_Q) = 1 ⊕ 3
     reads the three parity lines. On every thread they are alike, but all three are on the end. No line of that part is
     interior on any state at any tick.
   - **The spin part (W9).** The common point itself, the spin doublet, carries interior classes on every thread, because
     the moves act on it with finite order.
   - **With the parities, three alike interior sectors.** These appear on every odd-trace thread at its third tick. They
     are one module of the thread, 2 ⊕ 2′ ⊕ 2″, whose summands are told apart by a cube root of unity on the base.
   - **That is weave-level content, not +LR's alone.** Whether it is a generation needs a frame for the spin module; F-HE
     on the forced spin cover is the candidate, for main's review.
   - **READING, the hand.** Without the swap the doublet's group is abelian, and its two complex-conjugate lines are kept
     apart by every L,R-thread. That is a candidate for a hand that is not a marking. The swap exchanges them, as GENESIS
     FK3's C-type bit (B1083) would.
     - **Where the lines are apart is a rule over all 758 states:** n_L − n_R + 2·[sign −] ≢ 0 (mod 4).
     - **On every state that is its own mirror,** the − state has them apart and the + state together. That is main's
       "the hand is in the sign" (B1479–B1483), found from a different object.
   - **The chiral three (W10).**
     - With the parities, L and R act on the six-dimensional parity-twisted spin space as a group of order 96. It splits
       into two complex-conjugate triplets T and T̄, and the swap exchanges them.
     - At tick 3, on exactly one sign twin of every odd-trace word, one vacuum character carries T alone: three alike,
       separate, interior and chiral. On the root's pair that twin is m003; m004 carries T ⊕ T̄ together.
     - This is the most the weave gives toward three generations: the number, the alikeness, the separation, interior
       content and a hand, all from the joint action with no thread chosen.
     - Whether each of the three is a generation needs a frame with the Standard Model's dictionary on the spin module.
       Whether the third tick counts is GENESIS FK7.
6. **Masses.**
   - A kept, unbroken deck gives a texture the data refute (B1273, B1361; sL-5), so the deck must break at order one, or
     the Higgs must be parity-neutral.
   - At a state's own tick the three parities split 1 + 2 or 1 + 1 + 1 under its isometries, never 3 (Theorem S).
   - The 1 + 2 is the pattern B1507's lead (i) asks about on s961, as S₃'s "2 + 1". It is not compared with data here.
7. **In the hyperbolic frame, content is a thread's** (in the weave's spin vacuum it is not: item 5). What the parities
   carry in the hyperbolic frame depends on the thread and the cover:
   - on the forced A₄ cover, members only on ±LR and generations only on +LR (to length 6, complete);
   - elsewhere, other threads carry content (§2).
   - THE_BAR grades "only +LR" at p ≈ 0.29 on twelve threads: no selection is claimed.
   - Two of the record's generation findings on word states sit on parities, each at the tick where its thread
     separates them, though in two senses of "sits":
     - **+LR's, at tick 3, on all three alike (sm:B1550).** In Theorem G's sense, members of the forced cover labelled
       by the edge or translation they sit on.
     - **The silver pair's, at tick 1, on the two parities the thread carries into one another; the third reads none**
       (sm:B1530, read by parity after the fact). In Theorem S's sense, characters of the state whose fibre restriction
       is the parity.
     - That is an observation on two threads, not a law.
   - **R2 in Theorem S's sense found the same shape on all 24 states to length 6: content on pairs, never on three.**
     - Members are on ±LLRR (tick 1), ±LLR and ±LLLLR (tick 2), on the pair each state's symmetry exchanges.
     - None is on the parity it fixes, and none is on any odd-trace state at tick 3.
     - So in that sense the parities carry two alike, not three.
     - The three alike with content is +LR's alone, and only in Theorem G's sense.
8. **So the weave derives the three, and leaves five things open.**
   - **Derived:**
     - that there are three;
     - that they are alike under the weave;
     - that they are separate at every third tick;
     - that their symmetry is real;
     - that its own vacuum carries them on the end in its abelian part (Lemma V), and as three alike interior sectors
       in its spin part on every odd-trace thread at tick 3 (W9).
     - that, with the parities, L and R carry them as a chiral triplet T ⊕ T̄, alone at one vacuum character on exactly
       one sign twin of every odd-trace word (W10).
   - **Open:**
     - whether those interior sectors are generations: a frame for the spin module (F-HE on the forced spin cover);
     - the deck kept (GENESIS FK7);
     - the hand (GENESIS FK4 and FK12; main's sign);
     - the masses;
     - why +LR's content and not another thread's (GENESIS FK9).

## 4. The rechecks

Each line gives the cheapest test across the weave (other threads) and along the wave (other ticks).

- **R1. W6's content.**
  - Weave: run the census rule on the even-trace ±LLR and ±LLRR (their forced covers are Q₁₆ and Q₈) and on LP.
  - Wave: run +LR's ticks 2, 4 and 6. The gcd law predicts three sectors only at 3 and 6.
  - Running: the twelfth thread at order 4, and +LRLR and +LLLRLLLR at tick 2.
- **R2. "Only +LR", and where the content sits.**
  - Label L8a15's three members and −LLLLLR's three-ended cover by parity.
  - Census every state to length 6 at the tick where the weave's cover separates its parities (tick 3, 2 or 1), in
    Theorem S's sense: the characters of that tick whose fibre restriction is a non-zero parity, sector by sector.
    **Done (W7 in the dossier; 24 of 24, one pass).** Members sit only on pairs:
    - on ±LLR and ±LLLLR at tick 2, on the two parities the deck exchanges;
    - on ±LLRR at tick 1, on the two parities the isometries exchange;
    - never on the parity the state's symmetry fixes, never at the zero parity, and on no odd-trace state at tick 3.
    The counts on ±LLR and ±LLLLR need a sealed arc.
  - Read ±LLLR at tick 2.
- **R3. B1506's three vacua.** Do the three sectors of +LR at tick 3 differ by characters of order 4? Check also on −LR's
  sectors at ticks 1–6.
- **R4. Hollow textures.** Compute the Yukawa selection rule from the parity and member characters on the sectors of ±LR
  at tick 3 (character arithmetic only).
- **R5. The mixing.**
  - Find the O_h class of every odd-trace thread's image (the ± threads and LP), and check that TM1 and TM2 are stable
    across classes.
  - Repeat at tick 2.
- **R6. The founding field.** Certify the trace fields to length 12 and correlate them with the census.
- **R7. "The count is a bit".** On one +LR orbit and on −LR, seal both orders and a fused deformation (GENESIS FK12).
- **R8. Pin⁺** (B1383). Only LᵐRᵐ have orientation-reversing roots. Repeat on the bronze L³R³ and L³P.
- **R9. Room.** Compute the act's invariant H₁ on the genus-3 fibre of the Q₈ and 2T covers, for all twelve odd-trace
  threads and at ticks 2 and 4.
- **R10. B993's "exactly 2".** Count the 2T surjections on all 24 states to length 6. W3 predicts the two from the common
  point on each odd-trace state.
- **R11. Done here.** The "one-generation object" (B298) is now Theorem S, with main's GAP2.
- **R12. The knot complement's chirality.** Read the longitude trace on −LR and ±LLLR.
- **R13. Fixed points.** Apply main's fixed-points rule and the parity rule to every thread: +LR has 1 fixed point,
  +LLLR 3 and −LLLLLR 9.
- **R14. Outside these files.** "Swap = Breath" is a reading, and the data are fenced.
- **R16. The weave's vacuum on the forced spin cover.** Read Lemma V's lines where it does not apply, on the 2T cover of
  every odd-trace thread (fibre genus 3), as rank-one characters with their interior classes. Check also whether
  Theorem C's bound holds at the weave's vacuum.
  - **Its structure is done by Shapiro (W9).** The spin cover's interior lines are the spin doublet's classes. They
    exist on every thread, and with the parities there are three alike on every odd-trace thread at tick 3.
  - **Open:** the frame's counts there, which need main's review and a seal.
- **R15. The family tensor on the parity triplet.** On the weave's T_d the invariant cubic is xyz, so B1271's zero does
  not transfer as stated.

## Sources

- **The reviews.** Three reviews, read-only, 2026-10-07. Their findings are folded in above, and line references are in
  the session record.
- **The new laws.** `docs/dossiers/the_weave_2026-10-07/the_weaves_laws.py` → `the_weaves_laws.json`.
- **The dossier.** `docs/dossiers/the_weave_2026-10-07/NOTE.md`.
- **The synthesis.** `docs/THREE_GENERATIONS_AND_THE_WEAVE.md`.
- **The rule.** `docs/THE_WEAVE.md`.
