# chat1 → cc (main) and the SM seat, 2026-10-29: THE INTEGERS — four ways an integer of the object enters a magnitude on record, and what each still leaves chosen; the cyclic fibre isogenies the object carries (exact: degrees 5, 11, 19, 29, 31, 41, 55, 59 up to 60, none of 2, 3, 6 or 9); the shortest route to an integer-fixed τ is B1804's holomorphic frame with P-425's question (a design study, data-free)

chat1 (the web seat), at the owner's word (2026-10-29, "i aprove your recomendation, go for it, while cc does its own
job"). The recommendation was to look for a frame in which the hierarchy comes from an integer of the object rather than
from τ's height, with a side step on why B1811's parameter-free points miss. A design study: one exact count; no
measured number read except where labelled. 0 of 19.

**How it was done.**
- Swept first (below). Read the source: B1785, B1788, B1800, B1804, B1808, B1809, B1811, B1812, and B286, B326, B350,
  B489, B743.
- **One exact count,** `relays/chat1_2026-10-29_integers/isogeny_lemma.py`, committed (5cef18323) before its one run.
  Its output `isogeny_lemma_out.txt` was committed unread (d4c521ade), then read.
  - **A convention, disclosed:** the script's L and R are GENESIS's R and L. Its printed "LR = ((1,1),(1,2))" is
    therefore GENESIS's RL, and its listed fixed points are RL's.
  - The counts are conjugation-invariant and unchanged. The script also checks RL directly.
  - Cosmetic: an empty format field prints "( mod 5 = 2)".
- **Refereed read-only before the push.** Three blocking findings, all applied:
  - a first draft said an integer can enter a magnitude in "only two ways". That was an unearned negative: the record
    has four (§ 1);
  - it dropped "cyclic" from the isogeny statements, which made some false (§ 3);
  - it over-explained B1811's overshoot (§ 2).

  The referee recounted every index-k sublattice independently (Hermite normal form, k ≤ 130) and reproduced the counts.
  Its non-blocking points are applied too.

**Seen first** (topic sweeps on main at 965938922; each VERDICT line cut before its list of other lanes):
- `VERDICT topic-sweep /isogen|Hecke (image|operator|correspondence)|T_[23N] ?\(|τ ?→ ?[0-9]τ|tau ?-> ?[0-9] ?tau/ (full text): 10 of 1559 arcs on main match (NEGATIVE 1, PROVED 9); 1 register rows match (QUEUED 1)`
  - The matches are the isogeny classes of the character variety's curves (40a: B211, B509, B510, B1237, B1238; 15a:
    B512, B683, B692, B698) and B1483's cusp curve.
  - The register row is P-425 (B1804's holomorphic frame).
  - None asks which fibre isogenies extend over the object.
- `VERDICT topic-sweep /Lucas (ladder|number)|L_\{?2n|cover degree|k-fold cover.{0,60}(mass|ratio|hierarch|scale)/ (full text): 11 of 1559 arcs on main match (NEGATIVE 4, PROVED 7); 0 register rows match (none)`
  - B350: "the cyclic-cover abelian torsion class carries no forced choice: orders are the Lucas ladder".
  - B489: the cover tower's "arithmetic echoes are numerology".
- `VERDICT topic-sweep /flux (integer|quantum|number).{0,80}(hierarch|ratio|mass)|(hierarch|mass ratio).{0,80}flux (integer|quantum)/ (full text): 1 of 1559 arcs on main match (PROVED 1); 1 register rows match (QUEUED 1)`
  - B1809 (the census) and P-405 (the membrane-instanton route).
- `VERDICT topic-sweep /hierarch.{0,60}(filling|tower|cover|torsion|integer|discrete datum)|(filling|tower|cover degree|torsion).{0,60}hierarch/ (full text): 6 of 1559 arcs on main match (NEGATIVE 2, PROVED 4); 0 register rows match (none)`
  - B286 (the filling's "2π/n scale"), B326 (the generation ℤ/3 is "texture, not magnitudes"), B350, B923 and others.
- **The numerical route.** B743: "the object's whole real algebraic tower and canonical analytic values contain no SM
  ratio at testable precision". Low-digit targets are UNTESTABLE there, not closed. This note asks for a physical
  mechanism, not for matches.
- **Main's latest** (S253, B1812): LR lies in the E₁₀ 7-brane class, and the object fixes the total class, not where
  any tower sits. That bears on the towers, not on magnitudes.

## Frame card (the 2026-10-29 rule, item 1)

This note builds no frame. It reads the cards of B1809 § 4: FR-FIB, B1656's fibre frame; FR-FLUX, the flux frames of
B1800 and B1804. Those cards hold the continuous configurations, the discrete choices and the typed conditions. No
positive is claimed, so there is no null. § 4 says what the null of a later test must range over.

## 1. Four ways an integer of the object enters a magnitude on record (a reading)

1. **As a flux that fixes τ.** In B1804's holomorphic frame, LR-invariant (1,1) fluxes force isolated CM points:
   - (1, 0, 1) → i; (2, −1, 2) → ω; (1, 0, 3) → √−3; (1, 0, 12) → 2√3 i.
   - B1804: "LR does not choose the point. The flux integers do."
   - P-425 asks whether requiring CM by the compositum ℚ(√5, √−3) cuts that freedom.
2. **As exponents.**
   - **In the flux-overlap frame,** the characteristics set the leading exponents: each entry's lies in [0, ¼] ∪ {9/16}
     (B1800). In Cremades–Ibáñez–Marchesano generally, ϑ[c/N](0, Nτ) leads with e^{iπτc²/N}, so the flux integers and
     the characteristics enter the exponents.
   - **In FR-FIB,** B1788 bounds the second generation, e(m₂/m₃) = ½ − (‖2q_L α‖ + ‖2q_R α‖)/2 ≤ ½. The m₁/m₃ exponents
     reach 4/5 (B1788's table).
3. **As a multiplier of τ.**
   - The N in ϑ(0, Nτ): N = 2 in B1800, for flux-one matter and a flux-two Higgs. B1800 lists the flux-3 route as not
     covered.
   - A fibre isogeny (§ 3).
4. **As discrete end data in the prefactor.** B1809 § 3: the horocycle choice moves R's m₂/m₃(i) by a factor of 11.

## 2. The side step: FR-FIB's second generation at the symmetric points

- **The estimate.** By B1788's bound, the leading term of m₂/m₃ is at least |q|^{1/2} = e^{−π Im τ} times its
  prefactor. That is 0.043 at τ = i and 0.066 at ω. B1785 fitted the exponents at Im τ 4–6, so at Im τ ≤ 1 this is an
  estimate of the leading term.
- **Labelled post hoc** (one data number, already compared by B1811): the up quarks' m_c/m_t ≈ e^{−5.63} (HZ2021, as
  B1785 § 3 quotes it). At i this needs a second-generation prefactor of at most about 0.083, and at ω about 0.055. That
  is a suppression of 12–18 below order one.
- **Against B1811.** At B1811's χ²-best row, F₆ at (i, 0), L₂, c/t is 40× too large. That is consistent with this
  estimate.
  - B1811's other overshoots are not explained by it.
  - u/t is 1 739× too large, but that is m₁/m₃, which ½ does not bound.
  - s/b (7.9×) and μ/τ (7.5×) need no suppression by this arithmetic: s/b allows a prefactor up to about 0.44 at i.
- **For the n ≥ 2 members B1811 did not run:** to reach c/t, each would need its second-generation up prefactor
  suppressed 12–18-fold. Whether any is, only a sealed run would tell. This reading was written after B1811 and Table T
  were read (§ 4).

## 3. The cyclic fibre isogenies the object carries (exact; `isogeny_lemma_out.txt`; the referee's recount to k = 130)

- **The setting.** A cyclic degree-k isogeny of the fibre torus is an index-k sublattice with cyclic quotient, a point
  of P¹(ℤ/k). It extends over the mapping torus of the monodromy exactly when the monodromy fixes that point.
  - LR and RL are conjugate, and M^{−T} is conjugate to M, so the counts on lines and on dual lines agree.
  - Non-cyclic sublattices are n times a cyclic one and give the same τ′, so "cyclic" is the right restriction for the
    action on τ.
- **The count.** For k = 2 to 60 the monodromy fixes points of P¹(ℤ/k) only for k ∈ {5, 11, 19, 29, 31, 41, 55, 59}.
  There is one fixed point at k = 5 and two at each of the others.
  - The referee's recount gives the cyclic degree set as 5^a · ∏ p^b with a ≤ 1 and p split. For example, 121 has two
    and 25 has none.
- **The primes.** x² − 3x + 1, the characteristic polynomial, has discriminant 5.
  - p = 5 is ramified and has one fixed point.
  - The split primes (p ≡ ±1 mod 5) have two each.
  - The inert primes (p ≡ ±2 mod 5: 2, 3, 7, 13, 17, …) have none.
- **Consequences.**
  - No cyclic isogeny of degree 2, 3, 4, 6, 9, 10, 12, 15, 25 or 30 extends over m004. In particular the three
    generations give no cyclic 3-isogeny of the fibre that extends.
  - Over cyclic covers in the base (monodromy M^m), more extend: M² ≡ −I mod 3, so every 3-isogeny extends over the
    double cover. Those covers are CHOSEN (B350, B489).
- **Label.** The set is FORCED for this object, since it depends on the trace 3. The mechanism, eigenlines of the
  monodromy mod p, is generic in E20's sense.
- **Not yet a multiplier of the frame's τ.** In FR-FIB, LR does not act holomorphically on E_τ (B1804: τ ↦ (2τ+1)/(τ+1),
  no fixed point in ℍ). Using these isogenies to move the frame's τ would be an identification that needs a map.
- **Not computed: where they send i and ω.** That depends on the convention tying τ to the monodromy's basis. It would
  also be a look once read against the band, so it belongs inside a sealed test's data-free first half (§ 4).

## 4. Disclosure, and how a test of an integer route would have to be built

- **This seat knows the band.** The six's strip sits at Im τ ≈ 3.03 (P-373). Any integer that would carry i or ω into
  it, chosen after that knowledge, is post hoc, so this note names no target integer.
  - § 2's reading of the n ≥ 2 members was written after B1811 and B1809's Table T were read.
- **A sealed test of any route in § 1 would need:**
  1. **The integer fixed by a rule stated before any value is computed.** For example: P-425's CM condition, if it cuts
     the fluxes to finitely many points; or every cyclic isogeny of degree ≤ K applied to i and ω, once the map of § 3
     is given.
  2. **The Higgs direction** fixed in the same way, or ranged over in the null.
  3. **A null** that ranges over every integer the rule could have picked and every direction it allows.
  4. **The look count,** by docs/LOOK_LEDGER.md and the SM seat's § 315 convention, with § 2's post hoc reading
     entered.

## 5. What it says (a reading)

- **Integers enter the record's magnitudes in four ways.** Three of them leave a choice on record:
  - the flux integers choose B1804's CM point;
  - the fluxes and characteristics choose the exponents;
  - the horocycle is CHOSEN.

  The fourth, the cyclic isogenies, is FORCED as a set, but it is not yet a frame: it needs a map to the frame's τ.
- **The shortest route to an integer-fixed τ** is B1804's holomorphic frame with P-425's question.
  - If requiring CM by ℚ(√5, √−3) cuts the flux integers to finitely many points, τ there is set by the object's
    arithmetic, not by a fit.
  - The Higgs direction would then be the remaining choice, as in every frame of B1809.
- **The side step:** in FR-FIB at the symmetric points, the up quarks' second generation needs a prefactor suppressed
  12–18-fold. That is consistent with c/t at B1811's best row. It does not explain B1811's other misses.

## 6. Proposals (they assign nothing)

1. **To main, for P-425:** if CM by ℚ(√5, √−3) cuts the flux freedom to finitely many points, this seat offers to write
   the sealed comparison with those points fixed in advance and the Higgs direction ranged over in the null, before any
   value is computed.
2. **To main, for P-418 and the census:** the cyclic isogeny set of § 3 as FORCED for this object, with its scope:
   degrees 5^a · ∏ p^b (p split in ℚ(√5)); none of degree 2 or 3; not yet tied to the frame's τ.
3. **To main, for P-432's n ≥ 2 members:** § 2's reading, if they are run, disclosed as written after B1811.

0 of 19.
