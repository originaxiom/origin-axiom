# The rule that picks no thread, in the thread frame: a reading and a design (chat1; nothing computed against data)

chat1 (the web seat), 2026-10-16. A reading, at the owner's "go for it, maybe selection principle is hiding behind the
rule that picks no threads" and "maybe the very ab ≠ ba principle irritates, excites the wave that pushes back, on a
very fundamental level".
- **The rule is the SM seat's.** It is stated in §139.4: sum over every thread of one discriminant, choose none. It is
  held as W95 (N2) for the record's invariants, pending the owner's ruling (§140.4).
- **This note carries the rule into chat1's cycle integrals**, fixes its indexing, and adds three facts §139 did not
  state:
  - the trace layers;
  - the commutator subgroup;
  - the Higgs's character.
- Classical results are cited. Everything else is checked by `arena_checks.py`, pure algebra; its run is beside it.
- No value is derived, and nothing here touches data. 0 of 19.

## 1. The rule, indexed

**A layer is a trace.** All threads of trace t have the same length, 2 arccosh(t/2), so a layer is "every primitive
closed geodesic of one length".
- **The layers, from the run:**
  - t = 3: LR, alone;
  - t = 4: LLR and LRR, which pass through ω (§139.4);
  - t = 5: LLLR and LRRR;
  - t = 6: L⁴R, LLRR and LR⁴;
  - then 2, 4, 2, 6, 3 and 4 threads up to t = 12, and 10 at t = 20.
- **Nothing is chosen inside a layer.** Only the layer t and, in a twisted sector, the line order N are left. The root
  is the first layer and its only thread.

**The classical sums are indexed by discriminant** (Zagier for D < 0; Duke–Imamoḡlu–Tóth, Annals 2011, and
Katok–Sarnak, Israel J. Math. 1993, for D > 0). They run over every form of discriminant D, primitive or not, each with
its own weight. They and the trace layers are related exactly:
- **The bridge.** A matrix [[a, b], [c, d]] of trace t gives the form [c, d − a, −b] of discriminant t² − 4, and back.
  So the classical sum at D = t² − 4 is the trace-t layer plus the powers of shallower threads:
  - (LR)² at t = 7;
  - (LLR)² and (LRR)² at t = 14;
  - (LR)³ at t = 18.

  The round trip is exact on every thread to t = 12.
- **The same thread can also appear at a smaller discriminant.** A thread whose form has content f appears there too,
  at D′ = (t² − 4)/f²:
  - LLRR at D′ = 8;
  - L⁴R² and L²R⁴ at D′ = 24;
  - LLLRRR at D′ = 13.

  So a rule "by discriminant" (§139) and a rule "by trace" (here) group the same threads differently. The balanced
  threads LLRR and LLLRRR are among the ones that move.
- **What follows.** Modularity statements are about the classical indexing: the generating function in D is a (mock)
  modular form of weight ½ for D > 0, and of weight 3/2 for Zagier's D < 0. Any generating-function reading must be
  posed there and the layers recovered from it, not the other way round.

**In the thread frame:** K_t = Σ_γ K_γ and Y_t = Σ_γ Y_γ over the layer, and in a twisted sector also over every
closing line of order N on each thread. This is the SM seat's W73-per-sector weave reading, carried into the thread
frame.

## 2. Where a selection could hide in it (questions, not claims)

1. **Equidistribution.**
   - Duke (Invent. Math. 1988): as the fundamental discriminant D → ∞, the geodesics of discriminant D equidistribute
     on the modular surface. If that carries to the layers, the traced thread frame tends to the surface frame, W72's
     Petersson pairing. The record's two frames would then be one object read at two scales.
   - **The carry is not shown.**
     - Many layer discriminants are not fundamental (32, 45, 96, 117).
     - The primitive forms of discriminant D′ sit in exactly one layer, the trace of their generating automorph
       (checked to t = 20). So the smallest discriminant in layer t tends to ∞ with t, though not monotonically:
       8 at t = 6, 13 at t = 11, 20 at t = 18.
     - The carry still needs the theorem for non-fundamental discriminants. chat1 has not traced that in the
       literature.
   - **The catch is the cusp.** Each layer's deepest threads are L^(t−2)R and its mirror, at height √(t² − 4)/2 (the
     run). The integrands grow there, so the limit needs a cusp regularisation set by the layer. One reading is
     B1654's cutoff L as a function of the layer. It is not shown.
2. **Selberg's trace formula.**
   - Its hyperbolic side is a sum over closed geodesics grouped by length, which is exactly the trace layers with their
     powers. Sarnak (J. Number Theory 1982) counts the layers this way.
   - For a weight that depends only on length, the formula equates that sum with a spectral side: the Laplacian's
     eigenvalues, plus the identity, elliptic, parabolic and continuous-spectrum terms.
   - Cycle integrals are not such a weight. Their route is a relative trace formula: the automorphic kernel
     integrated along the geodesics. Its spectral side carries the Maass forms' periods along the geodesics, not the
     eigenvalues alone; those periods are what Katok–Sarnak relate to weight-½ coefficients.
     - *Dated correction, 2026-10-16:* the first version credited this route itself to Katok–Sarnak, whose method is
       the theta (Shintani) lift.
   - Whether the layer sums of chat1's cells have a spectral side of that kind, and whether a selection shows there,
     is a question.
3. **The record's selection rules, read as layers.**
   - SE1 picks the first layer.
   - The least-volume threads on which an order-N line closes are L·Rⁿ (13:43 addendum), with n = kN² for the sign +
     and n = kN² − 4 for the sign −. That is T-tower, which takes either sign, to n ≤ 3N². Every L·Rⁿ is one of the
     deepest pair in its layer.
   - On T-tower the 19:41 addendum bounds the six-ratio comparison's failure at more than 40 orders of magnitude at
     N = 9 and 11, if the measured offsets hold. The bound comes from a law that does not depend on N, measured at
     excluded orders, in C1 and the E4 cells but not ORTH. No N = 9 or 11 quantity was computed.
   - The traced rule weighs every member of a layer at once, the deep ones included.

## 3. AB ≠ BA (the owner's second thought), as structure

These are classical facts the record has used without connecting them; each "checked" is in the run.
- **LR and RL generate the commutator subgroup.**
  - Both are balanced (Ψ = #R − #L = 0). The subgroup they generate has index 6 in PSL(2, ℤ) and index 12 in SL(2, ℤ),
    by coset enumeration (checked).
  - Those are the two commutator subgroups' indices, and both abelianisations are cyclic, generated by T. So ⟨LR, RL⟩
    is SL(2, ℤ)′, mapping onto PSL(2, ℤ)′ = Γ′.
  - It lies in the kernel of every character and is their common kernel. On positive words it is exactly the words with
    Ψ ≡ 0 mod 12: the moves the count #R − #L cannot see.
  - Its quotient of the upper half-plane is the modular torus. That is the once-punctured torus with Markov traces
    (3, 3, 6), and tr LR = tr RL = 3, tr(LR·RL) = 6 (checked).
- **Their commutator is the puncture.**
  - [LR, RL] = [[5, −6], [6, −7]] has trace −2, so it is parabolic (checked). For a once-punctured torus, the
    commutator of the free generators is the loop around the puncture (classical).
  - So the failure of AB = BA, taken once around, is the cusp. The hierarchies chat1's arc has measured are set
    at the cusp:
    - W84's deep-cusp exponents;
    - the per-field cusp law (19:41);
    - B1654's boundary-class lift;
    - FK10's cusp unit.
  - That is the shape of "excites the wave that pushes back": non-commutativity makes the boundary, and the boundary
    sets the exponents. It is a reading. Its claims are the facts above.

  > **Dated corrections, 2026-10-16 (chat1; refereed before they left).**
  > - **The quotations.** The note's opening quotes were cleaned up. The owner's words are "go for it, maybe selwction
  >   principle is hiding behind the rule that picks no threads" and "maybe very a ab ba principle irritates, exitates
  >   the wave that pushes back, on very foundamental level".
  >   - "ab ≠ ba", and this section's "AB ≠ BA", are chat1's rendering of "a ab ba".
  >   - The owner uses "a ab ba" for the principle itself (P-177, passage 5: "the principle of a ab ba existence"), so
  >     the order-swap reading here is chat1's, not the owner's.
  >   - The first version also had "weave" for the owner's "wave". That is corrected in the two places it occurred.
  > - **The reading above needs a limit, from W-trace (`W_TRACE_UNTWISTED.md`).**
  >   - The cusp that weighs the integrals is reached by long runs of one letter. The dominant threads are L^(t−2)R
  >     and its mirror, the least balanced in each layer (Ψ = ±(t − 3)).
  >   - L and R are themselves parabolic. [LR, RL] encircles the cusp once only in the six-fold cover, the modular
  >     torus.
  >   - **So in the integrals, depth comes from repeating one move, not from the order-swap.** The order-swap's
  >     commutator makes the cusp a puncture of the torus; it does not set how deep a thread goes.
  >   - "Non-commutativity makes the boundary, and the boundary sets the exponents" stands only in that weaker sense.
  >   - The balanced threads (LLRR, LLLRRR) are the shallowest in their layers, to t = 12 (the range computed).
- **The Higgs sees only the abelian shadow.**
  - W72's Higgs modes transform as ρ′ = ρ_R ⊗ χ_i, with χ_i(S) = χ_i(T) = i (the record's ρ′; stage 1 of the low-thread
    instrument used it).
  - χ_i is η⁶'s multiplier, of weight 3.
  - A character factors through the abelianisation, so on a word χ_i = i^(#R − #L) = i^Ψ, with Ψ Rademacher's function.
    Checked numerically on all 254 positive words to length 7, against η⁶'s transformation, to 10⁻²⁸.
  - Ghys showed Ψ is the thread's linking number with the trefoil, the "links the cusp" of §139.3, up to orientation.
  - So, relative to the matter, the Higgs is blind to ⟨LR, RL⟩ and feels each thread only through that linking number,
    mod 4. χ_i's kernel is an index-4 subgroup of SL(2, ℤ) not containing −I; on positive words it is Ψ ≡ 0 mod 4.
  - On a thread of sign −, the lift picks up χ_i(−I) = −1. That sign matters in twisted sectors.
  - Balanced threads (the root, LLRR, LLLRRR, …) are invisible to that phase.

## 4. The design (chat1's next arc, after the current seal's run; for the owner to rule)

- **W-trace, untwisted first.**
  - K_t and Y_t at layers t = 3 to about 12, in every cell, with `tlow2.py` (the instrument in the current seal).
  - It checks the trend toward Duke's limit and where the cusp takes over, with both indexings, trace and the classical
    discriminant.
  - No data contact.
- **W-trace, twisted.**
  - In the per-field reading: the orbit sum over every closing line of order N on every thread of the layer.
  - Sealed before it is run, with the current seal's null and predicate.
  - Compared by layer: no thread is chosen and no line is chosen.
- **The generating function and the spectral side, readings after the numbers.**
  - Whether the classical-indexed values fit a (mock) modular form in D (Zagier, Duke–Imamoḡlu–Tóth).
  - Whether a relative trace formula, the automorphic kernel integrated along the layer's geodesics, turns the layer
    sum into a spectral statement in the geodesic periods.
- **Coordination with §139.**
  - Its N2 (W95) is this rule on the record's invariants; W-trace is the cycle-integral half.
  - Its N3, the field on the arena, is the frame in which W-trace's limit is the surface frame.
  - chat1 asks the owner to assign W95 to the SM seat and W-trace to chat1, and to say which indexing W95 uses, so the
    two can be compared.

## 5. What it does not do

- It derives no value, selects no layer, and does not claim a selection exists.
- The equidistribution transfer, the cutoff's link to the layer, the generating function and the spectral dual are
  questions.
- Checked in the run:
  - the coset indices;
  - the traces;
  - the character, as η⁶'s multiplier and as i^Ψ on words;
  - the matrix–form bridge, the contents and the powers;
  - the one layer per primitive discriminant;
  - the unique deepest pair. Duke, Selberg, Sarnak, Ghys and the punctured-torus fact are cited, not re-proved.

chat1, 2026-10-16. 0 of 19.
