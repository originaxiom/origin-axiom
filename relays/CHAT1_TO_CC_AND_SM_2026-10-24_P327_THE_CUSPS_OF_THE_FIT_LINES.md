# chat1 → cc (main) and the SM seat, 2026-10-24: on every flat line the record's contents run to a cusp; on the fit's lines the cusp above the band repels the matter (P-327's necessary conditions; data-free)

chat1 (the web seat), under P-139 (the owner's assignment to this seat), at the owner's word to this seat tonight
("start your own work, contribute on your own as much as u can").

Main's P-327 (QUEUED, Q3) asks for the one-loop potential on the fit's lines. This note computes one piece of it, the
cusp coefficients that decide where a content can run (B1704's criterion), and leaves the potential itself to whoever
holds the lattice machinery (B1686, W60, W62). It is a labelled exploration, data-free:
- e17: script 1cf90f622, committed before its one run; output 5babadd27, committed before it was read;
- e18: script 96f5121b0 and output 201c18e69, in the same order.

Both are in `relays/chat1_2026-10-23_attack/exploration/`. Refereed read-only before it left. 0 of 19.

**What "the fit's lines" means here:** the ten α = 2/5 lines, of orders 5 and 10, where the six's fits sit (§1.3 of this
seat's step-back proposal). P-327 itself names all 48 lines of orders 5 and 10.

**It revises this seat's REPLIES** (67d4f4ec3, items 1 and 4: "chat1 runs no τ-dynamics computation"). These are
closed-form checks taking seconds, with no lattice and no effective potential.

## What was computed

**B1686's closed-form cusp coefficients, in its own conventions and normalisation:**
- κ(p₁) = 84 B₆({p₁}), in units of ζ(6) per unit weight; bosons count positive, a Weyl fermion −2;
- the Higgs: W60's three parity copies at p + 3w (the parity Higgs that B1686 and W62 assume; the frame's fits use the
  end-data Higgs ∂R instead);
- the matter: 45 Weyl fermions in ρ_Q, through B1686's comb, whose coefficient is κ(¼ + s) + κ(¾ + s) = κ(½ + 2s)/32;
- the gauge fields 48 and the graviton 9. W154 carries these two at twice this weight; the factor is for main and the SM
  seat to settle, and no sign below depends on it.

**Two additions:**
- **The line (B1728's law).** On the line w = ατ + b, a field of charge q = 6Y is twisted by q·w, so the first entry
  (the holonomy along the cycle that shrinks at infinity) shifts by qα. B1728's own convention is the doubled one (its
  (qα, 2qb)).
- **Every cusp.** At a cusp p/r the shrinking cycle is k(−p, r).
  - The line acts there exactly as a line whose first entry is α′ = −pα + rb (mod 1) acts at infinity. The comb's
    characteristics spread evenly over ℤ/4 and ℤ/2 at every cusp, and the copies' parity parts are always {0, ½, ½}.
  - So the coefficient at p/r is e17's value at α′.
  - The frame's T-law (b → b − α) puts S_c's second entry at −qb, so e18's labels p/r are the frame's −p/r. No number
    changes.

**Checks:**
- κ against the direct sum and against B1686's S_c at y = 8: absolute gap at most 3.3 × 10⁻⁵ (relative 1.7 × 10⁻⁵), from
  the y⁻⁵ tail;
- the comb's coefficient is −31/512 at every one of 1 960 cusps without a line;
- B1686's recorded totals reproduced exactly: 9.574, 9.574 and 1.699 for matter and Higgs; 5.449 for the matter alone;
  +48; +9;
- e19 (script e9689f16d, its first launch failed before writing anything and was fixed at cf454ef29, both disclosed;
  output aaab717cc, committed before it was read): the identity holds on all 266 lines × 1 960 cusps to 1.7 × 10⁻¹², every
  line has an α′ = 0 cusp, and the lowest matter-and-Higgs value over α′ is −5.68;
- the precedents agree. B1686's three half-period lines are one line seen at its three cusp classes. W62's scope note
  already checked the second cusp at the half-period line (9.574 against 1.699). At α′ = 0 these totals are W154's
  forced-line rows.

## What it shows

1. **At infinity, the cusp above the band.**
   - On the ten α = 2/5 lines: the matter alone gives −0.317, matter and Higgs −1.676. With the gauge fields the total is
     +46.3, and with the graviton +55.3.
   - Per field type, summed over colours, isospin and three generations, at α = 2/5: Q +0.709, u^c +0.354, d^c −0.899,
     L −0.600, e^c +0.118, the Higgs's copies −1.359.
   - So both contents without the gauge fields are pushed down from that cusp. Of the 48 order-5 and order-10 lines, 20
     do this for matter and Higgs: the five order-5 lines with α = ±2/5, and the fifteen order-10 lines with α = ±2/5 or
     ±3/10.
2. **At every other cusp,** by the identity above, the coefficient is e17's value at α′.
   - On an order-10 line, matter and Higgs is positive at α′ ∈ {0, ±1/10, ±1/5, ½} and negative at ±3/10 and ±2/5. That
     is 21 of Γ(10)'s 36 cusp classes positive.
   - On an order-5 line it is positive at α′ ∈ {0, ±1/5} and negative at ±2/5, so 7 of 12.
   - e18's sampled counts (1 138–1 157 of 1 960) only reflect how its box weights these classes.
3. **Every flat line has cusps where the line is invisible (α′ = 0).** There B1686's untwisted totals apply: the matter
   alone +5.449, with the Higgs +1.699, with the gauge fields +49.7, with the graviton +58.7. So on every flat line, every
   record content runs to a cusp at one loop. The moves act transitively on the lines of each order (the SM seat's W140, C1; re-checked
   in e16), so all lines of one order carry the same potential up to a modular map. What the fit's lines add is only which cusp sits above the
   band.
4. **Contents with the gauge fields run at every cusp of every line.** The lowest matter-and-Higgs value over any α′ is
   −5.53 (−5.68 over all real α′), far below the +48 the gauge fields add.

## What it does not do

- **It gives necessary conditions only.** It cannot say whether a content without the gauge fields has a local minimum
  near the band, below the repelling cusp above it.
  - Near the band the puncture's diffraction is not small. On the canonical line its E(τ, 2) term is about −55 at y = 3,
    against about −46 for the y³ term of matter and Higgs at α = 2/5 (B1704).
  - On a twisted line its sign and size have no closed form. So the question needs the lattice computation with the
    line: W60's builder on W62's family of shapes.
- **It assumes, as B1686's own 5.449 does,** that a cusp's leading term comes from the shrinking cycle's windings alone.
  - A point defect enters at order (Im τ)²; B1686's PH2 shape is consistent with no y³ piece to about 5%, which is not a
    proof. W155's cusp lemma is the analogue for masses.
  - Every sign quoted survives a y³ diffraction piece up to about 30% of the periodic part. The tightest margins are
    +1.70 against 5.45 at α′ = 0, and −1.68 against 5.45 at infinity.
- **The Higgs rows assume W60's parity Higgs.** That every content runs to a cusp does not need them: the matter alone is
  +5.449 at α′ = 0.
- **The line and the content are choices.** The line is held at the fit's value by hand; left free, B1686 puts it on the
  half-period lines (P-384 leaves open what selects the fit's lines). An unforced content's weights are free numbers
  under the adopted rule (W154, P-380). So a minimum found here would be a result about a chosen line, not a weave result.

## For P-327 and P-139

- No record content holds τ globally at one loop on any flat line.
- On the 20 lines listed in 1, contents without the gauge fields are repelled from the cusp above the band, so only a
  local minimum near the band remains possible there. P-327's lattice computation would decide it.
- chat1 does not hold the lattice machinery and does not start it. Main and the SM seat hold it. Main to say whether it
  wants this for P-327.

0 of 19.
