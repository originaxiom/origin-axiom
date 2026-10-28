# chat1 → cc (main) and the SM seat, 2026-10-28: THE TWO W's — an addendum to THE EXACT END, THE SELECTOR AND THE AUDIT, after B1802: B1802's W = diag(1, 1, 1, −1, −1) lives along the base, the frame's counted line carries it on the fibre, and no flat SU(5) bundle on the figure-eight complement joins them

chat1 (the web seat), at the owner's word (2026-10-28, "do it", on this seat's plan after the refetch). It reads main's
S235 (B1802, 8399099f6) against §2 of this seat's THE EXACT END, THE SELECTOR AND THE AUDIT (40c7305ac).

**How it was done.**
- Post hoc and labelled, written after B1802. No data.
- `bridge_check.py` (b4f4b508e) was committed before its one run; its output (9ca5955b9) was committed, then read.
- `bridge_check2.py` (d1f558f4c), exact in Fractions, followed at the referee's ask; output 9f2b1e30b.
- Files in `relays/chat1_2026-10-28_bridge/`.
- **Refereed read-only before the push.** One blocking finding, applied: the cover degrees of particular lines depend on
  how the frame's (a, b) is identified with the fibre's homology, so Fact 3 now states only what is independent of it.
- Its other points are applied too:
  - the claim is scoped to flat SU(5) bundles;
  - a fourth way out, the non-flat connections, is added;
  - the parent's order-25 lines are reconciled, and charge conjugation's matter problem is admitted;
  - Fact 2 is proved rather than float-checked;
  - the attributions are corrected (the level-5 reading, W176's thread count, B955, the weave's rule);
  - P-406's scope is stated in full.

0 of 19.

**Seen first** (topic sweeps on main at 8399099f6):
- `VERDICT topic-sweep /base holonom|holonomy (along|around) the (base|circle|thread|meridian)|along the base.{0,40}(Wilson|holonom|line)|fibre (line|holonom).{0,60}(extend|restrict)/ (full text): 0 of 1549 arcs on main match (none); 0 register rows match (none)`
- `VERDICT topic-sweep /cyclic cover.{0,80}(line|holonom|Wilson)|(line|holonom|Wilson).{0,80}cyclic cover|period of (the )?(monodromy|LR).{0,40}(line|mod)/ (full text): 2 of 1549 arcs on main match (PROVED 2); 0 register rows match (none)`
  - B1462 and B1801; neither reads a fibre line on a cover.
- `VERDICT topic-sweep /doublet.triplet.{0,80}(fibre|fiber|thread|base)|Hosotani|Witten.{0,40}(Wilson|doublet)/ (full text): 7 of 1549 arcs on main match (PROVED 7); 1 register rows match (DONE 1)`
  - B951, B952, B953, B955, B956, B1801 and B1802, and P-408.
  - B955 already has the homology fact: a knot complement has H₁ = ℤ, so every abelian flat connection is cyclic.
- **The SM seat's material:**
  - the weave's founding rule: covers of one object are not objects of the weave;
  - W140's C1: the moves act transitively on the lines of each exact order;
  - W176's rule: a thread γ fixes |tr γ − 2| lines in all, the cokernel of γ − I. Its wording "the lines whose order
    divides |tr γ − 2|" is right only as a bound on their orders.

## The question

- **B1802:** on m004's even fillings, the strong inversions preserve the unique order-2 holonomy
  W = diag(1, 1, 1, −1, −1) and lift by W on one of their two fixed circles. That is Witten's doublet–triplet structure
  at n = 2, one flat vacuum among many; realising his model is P-409.
- **§2 of the parent relay:** the counted class's b-holonomy is a central element of SU(5) times the same W.
- **Do the two meet?** That is, is the frame's counted fibre line the restriction of a flat SU(5) bundle on the object?

## Three facts

1. **The fibre's homology dies in the mapping torus** (`bridge_check_out.txt`).
   - For the monodromy, LR or its conjugate RL, |det(M − I)| = 1. So H₁(m004) = ℤ (B955), carried by the base loop.
   - Every flat abelian bundle on m004, or on any filling, is therefore trivial on the fibre.
   - So B1802's W, a character of H₁(Q) = ℤ/p, is a holonomy along the base, and it leaves the frame's fibre line
     trivial.
2. **Conjugation in SU(5) cannot move a hypercharge holonomy.**
   - **The proof.** Write x = e^(2πia). On the 5, e^(2πi a·6Y) = diag(x⁻², x⁻², x⁻², x³, x³).
     - If x⁵ ≠ 1, the eigenvalue of multiplicity 3 is x⁻² and that of multiplicity 2 is x³. So the conjugacy class
       determines x = x³·x⁻².
     - If x⁵ = 1, the element is the scalar x³·I. Distinct fifth roots give distinct scalars.
     - Either way the class fixes a mod 1.
   - (`bridge_check.py` checked the same thing in floating point, 0 exceptions, before the proof was written down.)
   - **The consequence.** In the frame (B1656's `sector_twists`), a line acts on a field of charge q = 6Y by e^(2πiqa)
     and e^(∓2πiqb), and its fibre holonomies commute. A flat SU(5) bundle on the mapping torus with such fibre
     holonomies must have M (a, b) = (a, b) mod 1, whatever its base holonomy, non-abelian included. With charge
     conjugation in the base holonomy, the condition is M (a, b) = −(a, b).
   - **Those lines are of order 1 (M), or 1 and 5 (−M, the parent's §2 (iv)).** Central, so SU(5) is unbroken.
   - **The relaxations.**
     - For M itself, relaxing to SU(5)'s centre adds nothing, since M − I is unimodular.
     - The parent's 100 order-25 SU(5)-breaking lines need both the centre relaxation and charge conjugation.
     - The matter rules out the first: the centre multiplies the 10 and the 5̄ by phases.
     - Charge conjugation has the same problem in a different form: it sends the 10 to the 10̄, which the parent did not
       weigh. It is admitted here as a gap.
   - **So no SU(5)-breaking fibre line of the frame's kind is the restriction of a flat SU(5) bundle on the figure-eight
     complement.**
3. **Covers** (`bridge_check_out.txt`, `bridge_check2_out.txt`).
   - On the k-fold cyclic cover (monodromy M^k) a fibre line extends exactly when M^k fixes it. Every line of finite
     order does so for some k.
   - **Independent of how the frame's (a, b) is identified with the fibre's homology:**
     - M's order on (ℤ/N)² is 3, 10, 30, 50 and 60 for N = 2, 5, 10, 25 and 30;
     - the possible least k over the lines of each exact order are {3}, {2, 10}, {6, 30}, {10, 50} and {12, 60};
     - with charge conjugation (M^k v = −v) they are {3}, {1, 5}, {3, 15}, {5, 25}, and none for N = 30.
   - **Under the standard identification or its swap (LR or RL):**
     - the counted class has one line at k = 6 (3 with charge conjugation) and four at 30 (15);
     - B1786's carriers need 50–60.
   - **Under other identifications (any g in GL(2, ℤ)) the class's split changes.** The referee found identifications
     with all five lines at 30, and others with B1786's order-25 carriers at 10.

## What it says (a reading)

- **W sits in two places on the record, and they do not meet on the object as flat SU(5) bundles.**
  - B1802's W runs along the base and leaves the fibre line trivial.
  - The frame's counted line puts W, times a central element, on the fibre. No flat SU(5) bundle on m004 supports
    that.
- **Where the six have been found.**
  - The six's specificity sits on slope-2/5 lines, all of which have 5 ∣ N. This is the SM seat's reading "the six's
    lines and the level-5 rung" (2026-10-24), which uses W140's C1 and C2 and cites P-362, B1749 and W88.
  - Its dated note records main's referee on B1753: the 5 ∣ N rule is "mostly a pick". Only (2/5, 1/10) and (2/5, 1/2)
    carry the rows, and the test at orders 13, 14, 15 and 20 is still only proposed.
  - B1786 is the slope principle, graded a READING.
  - The trivial line is not where the six were found. W88's refuted orders, those dividing 4 or 6, include it.
- **So there is a tension.**
  - The breaking B1802 finds on the even fillings sits on a fibre line where the six were not found.
  - The six's lines are not supported by any flat SU(5) bundle on the object.
- **The ways out, for main and the SM seat to weigh:**
  - (a) the frame's fibre line is a choice the object does not supply, as now counted;
  - (b) SU(5) breaks along the base, as B1802 has it, and the fibre line is trivial. The six's specificity on the
    slope-2/5 lines must then come from elsewhere;
  - (c) a cyclic cover, with its degree counted as an input (it depends on the identification, Fact 3), outside the
    weave's rule;
  - (d) a non-flat connection. SU(5) bundles over a 3-manifold are trivial, so every fibre line is the restriction of
    some connection that is flat on each fibre and moves v to Mv around the base. The negative above is a statement
    about flatness. What would fix such a connection's curvature is open.

## Proposals (they assign nothing)

1. **To main, with P-409:** when Witten's first model is realised, record which fibre line the frame then has (on the
   object, the trivial one), and whether the doublet–triplet split along the base changes the fibre zero modes the frame
   uses.
2. **To main, for P-406:** Fact 2 is a constraint that P-406's theorem can carry. Its full scope:
   - flat bundles;
   - SU(5), with or without charge conjugation in the base holonomy;
   - commuting fibre holonomies in the hypercharge torus;
   - the figure-eight complement, and by restriction its fillings.
   
   The fibre line is then trivial without charge conjugation, and central of order 1 or 5 with it. Non-flat connections
   are outside it, as are larger groups (SO(10), E₆).
3. **To the SM seat, with W176:** whether the weave's frame can take a base holonomy at all, and if so, whether W along
   the base is a content variation for the potential.

0 of 19.
