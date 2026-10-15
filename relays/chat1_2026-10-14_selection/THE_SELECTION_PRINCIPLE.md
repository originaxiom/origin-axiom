# The selection principle: what B990's law forbids, why every symmetric point is flat, and how far a principle that selects nothing inside a vacuum gets (chat1, 2026-10-14, evening)

> **2026-10-15, the audit of the negatives** (`../chat1_2026-10-15_audit/AUDIT_OF_THE_NEGATIVES.md`: auditor D, and chat1's post hoc on step 3a's completion).
> - **"At c = 6 it selects nothing" is wrong as worded.** The root is the action's most probable thread at every c:
>   27%, 50% or 66% at c = 6, by the word weight. It is near-certain only at c ≈ 105–138.
> - **"The root is not hierarchical enough" holds in W72's cell only.**
>   - In the (−½, 7/2) cell the root gives 1 : 0.0215 : 0 (H-ORTH) or 1 : 0.0184 : 0 (the ring completion E4·F), far
>     below its low-lying neighbours.
>   - So "the thread is the whole question for the hierarchy" is wrong: the cell matters as much.
> - **"The weave cannot choose a sign of CP" is withdrawn as a failure.** A word and its reverse are CP images, and
>   between CP-conjugate vacua the sign of the phase is a convention (spontaneous CP violation). The real CP obstacles
>   stand:
>   - one sector has no physical phase;
>   - one coupling for every sector gives J = 0;
>   - the reflection-symmetric threads carry 91.5–98.9% of the weight at c = 6.
> - **"Not found" stands as a report:** no principle fixes the nineteen. But its stated reason holds only in W72's
>   cell.

> **The owner (18:27).** "your task is to find/solve the selection principle. take your time, meditate, learn, swipe,
> research, do whatever you can, the reward is high." It quotes cc:
> - "What is missing: 1. A selection principle (the essential one)." Every "which?" on the record comes out free: which
>   τ, which Higgs direction (B1646), which Higgs location (B1651: the puncture is a choice), which vacuum.
> - "An invariant construction can only pick points that are fixed by its own symmetry (B990's law). Every point we
>   have tested that way gives no hierarchy: τ = ω, and the cusp; the democratic direction; the real locus."
>
> **Read:** cc's latest relays, the SM seat's W47–W80 (to `87cf7f551`), the audit lane's new commits, and two
> read-only sweeps (the record; the literature).
> - **Landed later and read:** B1650 and B1651's seal reached main at 19:28 and 19:35 (`dc5fd3dca`, `6d6f7f660`).
> - **cc's tribunal relay** ("THE FRAME TRIBUNAL, FOR YOUR ATTACK", not yet on main) reached me through the owner at
>   19:14. Its section to chat1 states what the record demands of a selection principle, in six items. §6b measures
>   this report against them; the tribunal answer is in the relay beside this file.
>
> **Tags:**
> - **[MATH]** proved or computed;
> - **[SEALED]** a sealed test, scored as sealed;
> - **[RECORD]** banked;
> - **[READING]** interpretation;
> - **[LIT]** literature, read at source by an agent.
>
> **Refereed** by two independent agents before commit: the first on the whole draft, the second on tonight's
> additions and the relay. Their blockers and majors are taken (§8). **0 of 19.** No arc number
> claimed. Nothing to CLAIMS.md, GENESIS or the ledgers.

## 0. The answer in brief

**I did not find a principle that fixes the nineteen.** What I found has four parts.

1. **What forbids a hierarchy on the record is not B990's law** (which forbids canonical *points*, not canonical
   *values*). It is three structural facts:
   - **(a)** Every renormalisable invariant potential for the Higgs in M is linear in the one orbit coordinate that
     measures the hierarchy, so its minima sit at the ends: the cone or the real locus. **[MATH, one line, §2a]**
   - **(b)** That coordinate is the very quantity the potential's isotropy term penalises (W67). **[RECORD]**
   - **(c)** At the stabilised points the residual symmetry kills the hierarchy-generating terms. The hierarchy is a
     power of the *displacement* from them. **[RECORD, LIT]**

   In the class-S dictionary the record already carries (B277), the hierarchy coordinate a·a is the adjoint mass² of
   N = 2*. Its smallness is a U(1)_r-spurion question. **[READING, §2d]**
2. **A principle that selects nothing inside a vacuum takes two of the four "which?" questions off the list.**
   **[SEALED, §4]**
   - In the vacuum thread, τ runs over the thread's closed geodesic, and the Higgs is the surface frame's unique mode h.
   - The thread then supplies the one thing the surface frame lacked: **a canonical normalisation of the matter modes**
     (W72's modes diverge at the cusp; W73 normalised them by hand).
   - With it every coupling is a finite, parameter-free cycle integral. The 2–3 hierarchy lives in that normalisation
     (labelled post hoc, §4).
   - The location (the puncture's residue coupling) and the vacuum (the thread) remain.
3. **The thread → hierarchy map is geometric.** **[SEALED for words ≤ 8; corrected beyond, §5]**
   - For short threads the hierarchy depth is set by how high the thread's geodesic climbs toward the modular cusp:
     ln(m₂/m₃) = 7.29 − 7.33·y_max. This held out of sample on 47 new threads (RMS 0.30), with y_max half the thread's
     Markov–Lagrange value (B1629's heights).
   - For long threads, golden blocks dilute it, so at least the height and the length matter (the referee's blocker).
   - **The golden root is the least hierarchical thread computed: 1 : 0.37 : 0.0096.**
4. **Two structural facts about the thread frame, from tonight.** **[MATH, exact, and labelled post hoc; §4, §4b]**
   - **The locus is not reduced by the thread.** A vacuum's residual act on the four candidate points is the thread's
     class mod 2, a subgroup of the surface frame's S₃. So it never restricts the locus more than the surface frame
     does: equally on odd-trace threads (the root among them), less on the rest. (A first draft claimed the opposite.
     The second referee's blocker withdrew it, §8.)
   - **The weave cannot choose a sign of CP.** In this frame a thread's reversed word carries exactly the conjugate
     couplings. A word and its reverse are one oriented manifold (B1456), with the same volume and Chern–Simons
     invariant. So the couplings keep the word's order, which the manifold forgets (GENESIS FK12, the register), and no
     action built from Vol and CS can prefer either order.

**So the selection problem is relocated, not solved.**
- "Which τ" and "which direction" become "which thread". "Which locus" stays at least as open as in the surface
  frame.
- The admitted threads cover m₂/m₃ from 0.37 down to 7·10⁻⁷, and below 10⁻¹⁰ on threads too high for double
  precision. So the thread is the whole question for the hierarchy.
- It is what the 3D gravity action weighs (c, L154). At large c it is the root, which is not hierarchical enough. At
  c = 6 it is a plurality.
- The three sectors still need structure that one thread does not give.
- **Against main's specification** (§6b).
  - **Met:** items 1, 5 and 6. Item 3 is met for τ and the direction, not for the locus or the frame.
  - **Fails, item 2.** At large c the dynamics lands on the root, the least hierarchical thread. At c = 6 it lands
    nowhere. Climbing threads are held back only by word weights the record does not fix.
  - **Fails for the weave, item 4, by a symmetry.**

## 1. What B990's law forbids, and what it does not  **[RECORD + MATH]**

- **B990 (X10):** "No invariant built from the G-action can distinguish one point of O from another … UNREACHABLE by any
  orbit invariant." Two routes:
  - **A**, shrink the group;
  - **B**, add structure the orbit cannot see.
- **That forbids canonical points with trivial stabiliser, not canonical orbits.** Physical observables are orbit
  invariants (singular-value ratios, mixing moduli, Jarlskog).
  - B1443's correction already says it: "a deck-invariant function can have minima that are not deck-symmetric …
    Nothing proved in the record forbids the object from fixing the pattern."
- **The record has counterexamples to the stronger wording.** W67's minima at τ₀ (j = 1280) and at j = 336 ∓ 192√7 are
  fixed by no elliptic element; they lie on reflection lines. They are, however, on the cone (§2b).
- **The accurate wording.** "Invariant constructions pick orbits; *simple* ones pick the orbits of maximal isotropy."
  That is Michel's theorem, with Kim's corollary for quartics [LIT].

## 2. Why every symmetric point is flat

**2a. Orbit-space linearity (a theorem).** **[MATH]**
- **The invariants.** SO(3) × U(1) acts on a ∈ ℂ³. Its polynomial invariants are generated by |a|² and |a·a|²; a·a has
  U(1) charge 2.
- **So every invariant of degree ≤ 4 is**
  V = α|a|² + β|a|⁴ + γ|a·a|².
- **On a sphere |a| = r it is linear in x = |a·a|²/|a|⁴ ∈ [0, 1].** Its minima lie:
  - at x = 0, the isotropic cone (γ > 0);
  - at x = 1, the real locus (γ < 0);
  - or everywhere (γ = 0).

  B1646's D4 minimised exactly this family and found "the cone or the real locus, never between". The theorem is why.
- **Interior minima, which are the hierarchy, need one of two things:**
  - a degree-8 term in x²;
  - or a U(1)-breaking term. With V ⊃ γ|a·a|² + Re(b·a·a), the minimum sits at |a·a|/|a|² = |b|/(2γ|a|²), for
    |b| < 2γ|a|² (factor checked by the referee).

  **The hierarchy is then the ratio of the phase-breaking coefficient to the isotropy coupling.**

**2b. The order parameter is the hierarchy.** **[RECORD]**
- Near the cone, m₂/m₃ ≈ C·|a·a|/|a|², with C ∈ [¼, 1] (chat1's field relay C8; B1646 D3). So γ|a·a|² penalises exactly
  (m₂/m₃)².
- **W67, the weave's own quartic:** "The minima of the potential and the rank-one points coincide, because both are set
  by the cone."

**2c. Residual symmetry.** **[RECORD + LIT]**
- **Near ω.** ω's Z₃ forces E₄(ω) = 0, and every section onto one isotropic line (W68). Masses go as δ² : δ : 1 with
  δ = |τ − ω|.
- **Near the cusp.** They go as powers of q (W53).
- **The literature.**
  - Feruglio (arXiv:2211.00659, 2302.11580) calls this universality near critical points.
  - Novichkov, Penedo and Petcov (2102.07488) give ε^l scaling with the residual-charge mismatch l.
- **So a hierarchy is a displacement from a symmetric point.** An invariant selection that lands *on* the point gives
  displacement zero.

**2d. The class-S reading.** **[READING; B150 and B277 are the record's: the trace map is N = 2*'s S-duality, and the
fibre lifts canonically to 4d N = 2* SU(2) with the puncture as the adjoint mass]**
- **The dictionary** (chat1's field relay, O1). Φ_a² = −[(a·a)℘(z) − Σ_r a_r²e_r]dz² is the general quadratic
  differential with a double pole at the puncture: N = 2*'s Seiberg–Witten form.
  - a·a is the adjoint mass² (up to normalisation), and Σ a_r²e_r the Coulomb modulus u.
  - The cone a·a = 0 is N = 4, and R, whose Φ_R is nilpotent everywhere (O6), sits at (m, u) = (0, 0).
- **The spurion argument.** If the flavon's phase is U(1)_r (Hitchin's circle action), a·a carries charge 2. Then a
  *small* nonzero |a·a|/|a|² needs U(1)_r breaking, which is §2a's second escape, or degree-8 terms.
- **Naturalness covers less than it seems.** 't Hooft naturalness covers N = 2*'s mass as a *parameter*, not a flavon's
  vev (the referee's correction).
- **A side reading.** The three units are the three degenerate curves −(℘ − e_r)dz², the singular points u = m²e_r. That
  is N = 1*'s three massive vacua, with W ∝ e_r (Dorey, hep-th/9906011). N = 1* also needs a third mass, outside the
  dictionary.

## 3. Every way out, and where the programme stands

| route | mechanism | natural size | on the record |
|---|---|---|---|
| explicit small breaking (B990's B) | Re(b·a·a), U(1)_r | \|b\|/2γ\|a\|² | no source named. Candidates: the cusp opening a·a = (ℓ/8π)² (H-RES); a weight-1 form vanishing at the cusp |
| destabilised symmetric point | ω a local maximum with a large quartic | NPP 2201.02020: \|u\| ≈ 0.0145/(m + 0.0625), from A_m ≈ 68.78m [LIT] | **absent.** The one-loop family a·log(y\|η\|⁴) + b·E(τ, 3) has curvatures −1/3 and +8.28 at ω with O(1–20) higher terms. A small ring needs a/b tuned near 24.85 (chat1 exploration, unsealed) |
| frustration | the sectors' isotropy points differ | set by the differences | waits on P-128's sector R's |
| radiative | rank one at tree level | (g²/16π²)·logs | W64 gives rank one. Weinberg (2001.06582) found equal ratios across sectors [LIT] |
| dimensional transmutation | N = 2* → pure SU(2): Λ = m·q^{1/4} | e^{−π Im τ/2} | W53's m₁/m₃ ≈ κq^{1/4} *is* this |
| **integrate, don't select** | **the thread frame (§4)** | **set by the vacuum thread's geometry** | **sealed and run today** |
| the surface frame | τ over the whole modular surface | needs a cusp normalisation | W72, W73 (H-end, post hoc): 1 : 0.019 : 0.0004 |

## 4. Integrate, don't select: the thread frame  **[SEALED: `PREREGISTRATION_THREAD_FRAME.md`, `FINDINGS_THREAD_FRAME.md`]**

- **H-thread (a hypothesis).**
  - The weave's threads are the closed geodesics of the modular surface: positive Lyndon words in L, R are the primitive
    hyperbolic classes.
  - In vacuum W, τ runs over W's geodesic. The couplings and norms are cycle integrals of the surface frame's invariant
    integrands: W72's forms, B1644's coupling with R, and the Higgs's unique surface mode h.
  - On a closed geodesic every norm is finite.
- **Sealed results.**
  - **TF1 holds:** rank 3.
  - **TF5 holds:** ρ = −0.986 between the hierarchy and the geodesic's height.
  - **TF2 fails:** the root is 1 : 0.369 : 0.0096, not hierarchical enough.
  - **TF3 fails:** F₊ is the *heaviest* state in every thread.
  - **Q0 and TF4 failed as worded on tolerance;** a post hoc check confirms the content. TF4 tested nothing at these
    lengths (corrections).
- **What the thread actually supplies is the normalisation** (the first referee's major, taken).
  - W72's surface Y, normalised by each thread's own K, gives ×0.90–1.02 of that thread's m₂/m₃ on all 12 threads
    (labelled post hoc, `post_hoc_hybrid.*`). So the 2–3 hierarchy lives in K: the modes' norms along the vacuum geodesic.
  - m₁/m₃ agrees only within a factor 7.4 (the root: 0.071 against 0.0096). The first generation's ratio depends on Y as
    well.
  - For the 2–3 ratio, that is the canonical replacement for W73's hand-chosen H-end.
- **CP is the modular surface's reflection.** **[labelled post hoc: `post_hoc_reversal.*`,
  `post_hoc_reversal_census.*`; the mechanism is W74's and B1456's]**
  - On the 12 sealed threads (length ≤ 5) K and Y are real, chiral ones included. Every word of length ≤ 5 is its own
    reverse.
  - Words that are not their own reverse have complex couplings in this basis. LLRLRR and the LLLRLRR family give
    Im Y/|Y| of 0.4–0.7%.
  - A thread's reversed word carries exactly the conjugate couplings (K to 4·10⁻¹⁵, Y to 3·10⁻¹¹), and so does its
    mirror (L ↔ R). Their composition W^T runs the same geodesic backwards and has the same couplings.
  - **The mechanism is on the record.**
    - W74 (the SM seat) showed that τ ↦ −τ̄, with C = diag(1, 1, −1), maps every section the surface frame uses to
      itself, so the surface frame's Yukawas are real.
    - The reflection carries W's geodesic onto rev(W)'s. So the same involution turns a thread's couplings into the
      conjugates of its reverse's.
    - B1456 (H1), main's check of the SM seat's GENESIS v1.2 (sm:B1519), proved M(reverse w) = D·M(w)⁻¹·D⁻¹ on 8,190
      words: a word and its reverse are one oriented manifold (GENESIS FK12).
    - Check C1 repeats this on T-ROOT's 31,040 threads: equal volume and CS. Check C2: W^T has W's volume and minus
      its CS.
- **What follows for CP.** **[READING]**
  - **The couplings keep the word's order; the manifold forgets it.** That is FK12's register question, met in the
    couplings.
  - Each sign of CS comes with both conjugates at equal weight:
    - W and rev(W), with CS = s, carry Y and Ȳ;
    - W^T and mirror(W), with CS = −s, carry Y and Ȳ.
  - So no weight built from Vol and CS, the level k included, can prefer a sign of CP. The weave is CP-symmetric. A CP
    sign could be chosen only spontaneously, or by something that reads the order: the register.
  - **The couplings' CP is blind to the CS sign.** W^T, the mirror manifold, has W's couplings. So B1224's β-odd bit and
    W76's census, which are CS statements, are not the couplings' CP in this frame.
  - **One sector carries no physical phase.**
    - A symmetric Y with Hermitian K can be brought to a real diagonal form (Takagi), so Im Y/|Y| depends on the
      basis.
    - A physical phase needs two sectors with different couplings. One coupling for all sectors gives CKM = 1 and
      J = 0 (W74).
  - Threads that are their own reverse carry 91–99% of the weave's weight at c = 6.

## 4b. The locus by thread: the residual act, and why it adds no selection  **[MATH, exact: `locus_by_thread.*`; corrected by the second referee]**

- **B1651's question** (sealed at `6d6f7f660`, not yet run): where can a Higgs couple the zero modes, and does anything
  force the puncture?
  - Under its premise P1 (an even Higgs at a single point, rather than at a pair {z₀, −z₀}), only the elliptic
    involution's four fixed points remain: the puncture and the three half-periods.
  - At one τ nothing forces the puncture. In the surface frame, under P1, the covariant loci are three: the puncture,
    the half-period orbit, and both.
- **In the thread frame the residual act is the thread's own.**
  - Going once around W, the fibre comes back through W's monodromy.
  - The monodromy fixes the puncture (B366: "the unique MCG-invariant point"). It permutes the half-periods through
    W mod 2 ∈ SL(2, F₂) ≅ S₃.
- **The classes are B1600's and B1602's.** The script checks them exactly on all 31,040 threads to length 18, in both
  letter conventions, with B1600's parity lemma. To length 8, up to mirror, it reproduces B1602's census, 16 / 13 / 8.

  | class (B1602) | threads | W mod 2 on the half-periods | the fibrewise involution's fixed set | covariant loci under B1651's P1 |
  |---|---|---|---|---|
  | A₄ | odd trace (all of even length): the root LR, LLLR, LLRRLR, … | a 3-cycle | one closed curve through all three half-periods | the puncture, the orbit, or both: **as in the surface frame** |
  | D₄ | every odd length: LLR, LLRLR, … | a transposition | two curves (one meets each fibre once, one twice) | more: the one fixed half-period alone is covariant too |
  | V₄ | W ≡ 1 mod 2 (Γ(2)): LLRR, LLRLRRLR, … | trivial | three curves | every subset |

  The involution acts freely on the cusp torus, so no curve of its fixed set lies at the puncture.
- **So the thread adds no selection.**
  - The residual act is a subgroup of the surface frame's S₃. It allows exactly the surface frame's loci on A₄
    threads and more on the others.
  - A first draft claimed the puncture forced in the root's vacuum. It read P1 as "one point per fibre" in the thread
    frame but not in the surface frame. Read uniformly:
    - **under B1651's P1,** an A₄ vacuum allows the surface frame's three loci;
    - **under a strict one-point-per-fibre reading,** the surface frame forces the puncture (B366), and an A₄ vacuum
      does the same, no more.
  - The withdrawn claim also assumed one lap. The SM seat's principle continues: "…and that is the cover the weave's
    congruence kernel cuts out". It reads the permuting deck as a flavour symmetry. On an A₄ thread a single
    half-period is single-valued on the three-lap cover.
- **What stands.**
  - **The exact per-class residual act, and the weights.**
    - A₄ threads carry 48%, 61% and 74% of the weave's weight at c = 6 under (A), (B) and (C). Under (A) that is a
      plurality: D₄ has 44%.
    - They carry 67–86% at c = 24.
    - The root alone carries 27%, 50% and 66% at c = 6.
  - **In the root's manifold the half-period orbit is one closed geodesic,** B1294's period-2 axis.
    - m004 has exactly one orientation-preserving involution that keeps the meridian and the longitude. It fixes "one
      closed geodesic (the period-2 axis)" (B1294).
    - The record identifies it as the fibre's elliptic involution: B1297's P, "the one non-trivial outer class that
      keeps the orientation and the base" (GENESIS FK9).
    - Its fixed points are the half-periods (fc R60, quoted in B1306's inputs).
  - **A single half-period alone** (one point per fibre, one lap) is covariant only on D₄ and V₄ threads. That is where
    two sectors at different single fixed points (P-131) could sit. On the root the half-period locus is the whole
    orbit.
  - **This answers single-valuedness only.** B1651's owed legality question (the pillowcase's twisted sectors, W60,
    P-108) is untouched.
- **A value at a regular point carries weight.** **[READING, by hand]**
  - Wherever τ moves (the surface frame, the thread frame), a move rescales dz by (cτ + d)⁻¹.
  - So a half-period's value carries one unit of weight more than the puncture's residue, which needs no frame (B1651's
    U1).
  - The Petersson factor (Im τ)^½ absorbs the modulus of (cτ + d). Only its phase is left as a debt when a puncture
    coupling and a half-period coupling are mixed (P-131).

## 5. The thread → hierarchy map  **[SEALED for words ≤ 8: `PREREGISTRATION_LAGRANGE_LAW.md`, `FINDINGS_LAGRANGE_LAW.md`; corrected beyond]**

- **The sealed law, out of sample.** ln(m₂/m₃) = 7.107 − 7.294·y_max was fitted on 12 threads and predicted the 47 new
  threads of length 6–8 with RMS 0.30 e-folds. Over all 59 admitted threads, ρ = −0.996.
- **Not one number beyond length 8** (the referee's blocker; chat1's own post hoc check below).
  - Golden blocks dilute the hierarchy: LLRR(LR)^k climbs 0.037 → 0.083 between lengths 10 and 28 (the first referee's
    re-run; chat1's filed post hoc confirms 0.037 and 0.059 at lengths 10 and 18), and LLR(LR)^k climbs
    0.0034 → 0.055.
  - Over all 501 admitted words of length 9–12, the sealed fit's RMS is 0.44 and grows with length.
  - **The mechanism.** The heavy mode's norm accumulates along the geodesic's length, while the light modes' norms are
    dominated by its highest point.
  - **So the map needs at least two numbers:** the height (half the Lagrange value, B1629/B482's Markov heights) and the
    length or golden content.
- **What stands.**
  - The golden root has the largest m₂/m₃ of all threads computed, approached from below by golden-dominated words.
  - The hierarchy is exponential in the height for short words.
- **What is withdrawn.**
  - "Fixed by one number".
  - "Markov makes the mild hierarchies discrete; the band 0.04–0.37 is forbidden": long Markov words fill it, giving
    0.0595 at length 18, which is the leptons' value.
  - "Hurwitz is B990 in Diophantine form".
- **The post hoc down-quark coincidence** (LLRLRLR: 0.0176 and 9.1·10⁻⁴ against 0.0187 and 9.4·10⁻⁴) is not
  significant. Its p ≈ 0.01–0.10 depends on the length cutoff, and it rides on the law's largest residual.

## 6. The selection principle, as it now stands

**[READING on the sealed results and the corrections]**
- **Inside a vacuum, τ and the Higgs's direction need not be selected.** They are integrated over the vacuum thread's
  closed geodesic, and the thread fixes the normalisation that the surface frame lacked.
- **B990 is kept by route A:** the thread shrinks the group.
- **The values then depend on the thread's geometry.** For short threads, they depend on how far its geodesic climbs
  toward the modular cusp.

**What this settles.**
- (i) The four "which?" questions are not independent. Two of them reduce to the vacuum thread. The locus does not
  (§4b).
- (ii) In this frame the hierarchy's size is a geometric property of the vacuum (its excursion toward the end), not a
  potential's minimum. That is why no invariant potential found it.
- (iii) The most symmetric vacuum, the golden root, gives the mildest hierarchy computed: 1 : 0.37 : 0.0096.

**What it does not settle.**
- (i) **Which thread.** This is now the whole question. The threads cover every order of magnitude.
- (ii) **The three sectors.** One thread gives every sector the same ratios.
- (iii) **The location.** The thread's residual act restricts it no more than the surface frame's does (§4b). P1 is a
  premise.
- (iv) **H-thread's derivation.**
- (v) **CP.** A vacuum's couplings are complex if it is not its own reverse. But one sector carries no physical phase,
  and the weave cannot pick a sign (§4).

**Where "which thread" lives.**
- In the record's dynamics it is the 3D gravity action: e^{−cVol/6π} with word weights.
- At large c it picks the root, whose 0.37 is not the observed pattern. At L154's c = 6 the weave is a plurality.
- So, given H-thread, the flavour hierarchy is another place where c is the hinge. That is a remark, not a result: the
  weights were computed only to length 5.

## 6b. Against main's specification  **[READING on §4–§6]**

cc's tribunal relay sets out what the record demands of a selection principle, "as a specification to start from, not a
constraint on your route". Item by item, for the thread frame weighed by the action:

| item (cc) | this report | status |
|---|---|---|
| 1. a dynamics, not a symmetry (B990) | Inside a vacuum nothing is selected: τ and the direction are integrated. Between vacua the 3D gravity action e^{−cVol/6π} weighs the threads | **met**, given H-thread |
| 2. land near a symmetric point, at a computable offset | At large c the action lands on the root, a symmetric point, at offset zero, and the root is the least hierarchical thread (1 : 0.37 : 0.0096). At c = 6 it lands on no vacuum: the root has 27–66%. The action barely penalises climbing (vol(LⁿR) < 3.664 while the height grows like n/2). The word weights, which the record does not fix, are what hold climbing threads back | **fails** |
| 3. select every "which" at once: τ, direction, locus, frame | One choice, the thread, carries τ's range, the normalisation K and the Higgs mode h. Not the locus: the thread's residual act restricts it no more than the surface frame's (§4b). Not the frame | **met for τ and the direction only** |
| 4. break mirror symmetry somewhere | Chiral threads break mirror symmetry (66% of the weight at c = 6 under (A), T4). But in this frame the couplings' CP is the reflection: a thread's reverse, with the same Vol and CS (B1456), carries the conjugate couplings. So the action cannot select a CP sign. One sector carries no physical phase, and one coupling for all sectors gives J = 0 | **fails for the weave; open with two sectors** |
| 5. link the action weighting to the Yukawas | H-thread is that link: the couplings are cycle integrals along the vacuum's thread | **met, as a hypothesis**: H-thread is not derived |
| 6. seal first | two sealed tests, refereed once; tonight's additions refereed separately; labelled post hoc checks | **met** |

**What item 2's failure says.**
- In this frame the dynamics and the hierarchy pull apart.
  - At large c the action selects the root, the least hierarchical thread. At c = 6 it selects nothing.
  - The hierarchy needs threads that climb toward the cusp. The action is nearly indifferent to climbing, and the word
    weights, which the record does not fix, are what suppress it.
- So a principle of cc's shape needs one of two things:
  - a different link, under which the root itself is hierarchical;
  - or a weight that prefers climbing threads, to the right height.

  Neither is on the record. That is the sharpest form I can give of what is still missing.

**What item 4 adds.** A dynamics that selects a sign of CP must read the word's order, which the oriented 3-manifold
forgets (B1456; FK12's register). The 3D gravity action, through Vol and CS, does not.

## 7. Next, ranked

0. **The tribunal first** (P-136, the owner's order). The thread frame is offered there as a column, in the relay beside
   this file. The numbers below wait on it.
1. **Sectors in the thread frame: other weights and representations.** This is the natural home of sector differences
   and of a second light-pair slope. Use the SM seat's constructions at weights −½, 3/2 and 7/2, and W54's weights 5
   and 7.
2. **The two-variable map.** Fit the height and the length (or golden content) jointly on all words to length 12, sealed.
   Then decide whether the hierarchy is a function of the thread's geodesic data alone.
3. **Which thread.** The weave's distribution of hierarchies at c = 6 against the three sectors, with weights computed to
   length 12 and more.
4. **H-thread's physics.** Is the base circle of the thread's mapping torus the direction along which the fibre's modulus
   runs? The Sol picture for closed torus bundles says yes. Check against W46's 4D index and the monodromy's twist on M.
5. **The other locus.** Under B1651's P1, an A₄ vacuum also allows the half-period orbit, one closed curve (§4b). Its
   Yukawa in the thread frame, sealed.
6. **CP.** With two sectors, J on threads that are not their own reverse (§4). Then: does anything on the record read
   the word's order (FK12)?
7. **The cusp opening as the U(1)_r source** (§2d): whether the gravity action fixes ℓ_∂, and with it a·a.

## 8. What the referees changed

**The first referee**, an agent of chat1's, read-only, upheld every sealed cell, the seal order and the hashes. Taken:
- **(1) Blocker:** the one-number law and the forbidden band fail beyond length 8.
- **(2)** The equidistribution sentence of the draft ("the surface frame is the thread frame averaged over all vacua")
  is false as stated. The integrands are not integrable on the modular surface, and Duke's theorem is for fixed
  discriminant and bounded test functions. It is removed.
- **(3)** The hierarchy lives in K.
- **(4)** "B990 in Diophantine form" conflated rank-one flatness with mild hierarchy. Withdrawn.
- **(5)** §2d's "no invariant potential generates a·a" contradicted §2a. Rewritten as a spurion argument.
- **Minor:** the factor 2 in §2a; "20 e-folds" corrected to 13.2; the excluded-word description; TF4 tested nothing; the
  CP read-out dropped without notice; credit to B1629, B482 and B1379.

**The second referee** (tonight, on the new sections and the relay), read-only, recomputed every new number. It upheld
the arithmetic and the reversal mathematics. Taken:
- **(6) Blocker: the locus claim is withdrawn.**
  - The draft said "under P1 the puncture is forced in the root's vacuum, unlike the surface frame".
  - It read P1 as "one point per fibre" in the thread frame but not in the surface frame, and it assumed one lap.
  - Read uniformly, the thread restricts the locus no more than the surface frame does. §4b is rewritten.
- **(7)** The relay's grade "D1 unbroken" used a laxer standard than main's for F1. It is regraded "broken to ⟨W⟩, the
  vacuum weighed by the action", and D5 likewise.
- **(8) Credit.**
  - B1456 (H1) and GENESIS FK12: a word and its reverse are one manifold.
  - W74: the reflection's action on sections.
  - "F5 shows why the surface frame is real" is withdrawn.
- **(9)** The per-thread hybrid had no filed script and holds for m₂/m₃ only. It is now filed as `post_hoc_hybrid.*`;
  m₁/m₃ agrees only within a factor 7.4.
- **Minor:**
  - the fixed-set column (the involution acts freely on the cusp torus);
  - "differ only in the fibre's orientation";
  - both CP conjugates named;
  - 4·10⁻¹⁵;
  - "below 10⁻¹⁰" (from excluded threads);
  - "dominant" (a plurality under (A));
  - item 2 at c = 6;
  - c is free in D6;
  - one sector has no rephasing-invariant phase;
  - the weight debt is a phase;
  - "or a deferral to P-108" removed;
  - U6 does not measure the orbit;
  - single-valuedness is not legality;
  - B1294's match upgraded.

## Sources

**Literature** (an agent's report):
- Novichkov, Penedo and Petcov, arXiv:2102.07488 and 2201.02020.
- Feruglio, arXiv:2211.00659 and 2302.11580.
- Feruglio, Gherardi, Romanino and Titov, arXiv:2101.08718.
- Leedom, Righi and Westphal, arXiv:2212.03876. Gonzalo, Ibáñez and Uranga, arXiv:1812.06520.
- Knapp-Pérez et al., arXiv:2304.14437. Kobayashi, Nasu, Sakuma and Yamada, arXiv:2310.15604.
- Ishiguro, Kobayashi and Otsuka, arXiv:2011.09154.
- Weinberg, arXiv:2001.06582.
- Duke, Imamoḡlu and Tóth, Ann. Math. 173 (2011) 947.
- Kim, Nucl. Phys. B196 (1982) 285; Abud–Sartori, Ann. Phys. 150 (1983) 307.
- Dorey, hep-th/9906011 (not re-read).

**The record.**
- B150, B277, B366, B482, B990, B1294, B1297, B1379, B1443, B1456, B1600, B1602, B1617, B1618, B1629, B1636, B1637,
  B1640, B1644–B1651 (B1651 sealed, not run); P-069, L254, P-128, P-129, P-131–P-136; GENESIS FK9 and FK12; fc R60 (in
  B1306's inputs).
- The SM seat's W49, W51, W53, W54, W59, W62, W64–W68, W72–W74, W76, and THE_WEAVES_LAWS (the single-valuedness
  principle).
- cc's relays: THE FIELD, BY FRAME (S124, on main) and THE FRAME TRIBUNAL (through the owner, not yet on main).
- chat1's field relay (O1, O6, C8) and T-ROOT (with the instrument fix of tonight, `t_root_fixed.*`).

**Today's files** (this folder):
- the thread frame: seal, script, run, JSON, post hoc convergence, findings;
- the Lagrange law: seal, script, run, JSON, findings;
- `post_hoc_long_words.*`, `post_hoc_reversal.*`, `post_hoc_reversal_census.*`, `post_hoc_hybrid.*` (labelled
  post hoc);
- `locus_by_thread.*` (an exact classification; no prediction).
