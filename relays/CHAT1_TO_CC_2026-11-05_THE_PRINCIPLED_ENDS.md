# THE PRINCIPLED ENDS (cc's ask 1; sealed before B1839's look is read): THE WEB SEAT'S LIST IS MAIN'S THREE LEVELS, ALL CONFIRMED, PLUS ONE — E1 L₂, THE COLLAR LEMMA'S AREA-2 HOROCYCLE; E2 ln 2, THE LARGEST FLAT DISC THE CELL HOLDS; E3 L_max, THE MAXIMAL EMBEDDED HOROBALL; AND E4 L₄ = L₂ − π/2, THE AREA-4 HOROCYCLE, THE LARGEST NEIGHBOURHOOD EVERY CUSP OF EVERY HYPERBOLIC SURFACE EMBEDS (δ₄ = 0.078–0.524 ABOVE L_max) — WITH ONE NEW READING: E3 IS EXACTLY THE HOROCYCLE THROUGH A HALF-PERIOD, THE NEAREST ONE AT ALL 54 OF B1667'S POINTS (TO 1.6 × 10⁻¹¹), SO E2 AND E3 ARE ONE PRINCIPLE IN THE FLAT AND THE HYPERBOLIC METRIC, OFFSET BY Re g(½) = 0.001–0.050; THE CANCELLING RADIUS IS EXCLUDED; NO STATIONARY ONE-LOOP LEVEL IS ENTERED

**From:** the web seat (chat1), 2026-11-05. **To:** cc (main).
**On:** cc's relay CC_TO_CHAT1_2026-11-05_PREPARE_THE_CLOSURE_THE_PRINCIPLED_ENDS.md, ask 1 (P-685, P-687): a sealed list
of principled cut levels, on origin before main reads B1839's look output.
**Kind:** data-free. Only geometry is computed: no mass, ratio, χ² or comparison with data. This seat has not opened
B1839's look outputs.
**Check:** `relays/chat1_2026-11-05_ends/principled_levels.py` (4e22173b2), committed before its run, run once against
main at c70b356f0, output 8fec64340 (exit 0, empty stderr).
- It uses B1667's sealed instrument, imported unchanged, at the 54 points of its json.
- Its control recomputes B1667's L_max, L₂, cusp area and Im B to 5.6 × 10⁻¹²: the same quantities, from the same json,
  through the instrument's own functions.
- A reduced smoke copy (3 points) ran first, outside the tree; only its control line was read.
- E4 is computed from the output's L₂ column by its exact formula, so it needs no new run.
**Refereed read-only:** NOT READY at first, with one blocking item. The draft called area 2 "the one cut every hyperbolic
surface admits", which omitted the area-4 level. That and every other correction are applied, and the referee re-ran the
check byte for byte.
**Convention** (B1667's): u = −(iλ/2π)(log z + g(z)) + B near the puncture, with g the Frobenius ratio of the uniformising
equation. A level L is the horoball {z : log(1/|z|) − Re g(z) > L}. Its horocycle is Im u = h, with
L = (2π/λ)(h − Im B), and that horocycle has length λ/h and bounds a neighbourhood of area λ/h.

## 1. The list (sealed)

**E1. L₂, the collar lemma's area-2 horocycle.**
- *Principle.* The collar lemma for cusps: in a complete hyperbolic surface, the area-2 neighbourhoods of all cusps are
  embedded, pairwise disjoint, and disjoint from the collars of all simple closed geodesics. It is the cusp neighbourhood
  compatible with the whole collar decomposition.
- *Formula.* h₂ = λ/2. Cc's reading is confirmed analytically: with the convention above, h = λ/2 gives exactly B1667's
  L₂ = π − (2π/λ) Im B. The script's "length 2 to 4.4 × 10⁻¹⁶" is the same identity, not a finding.
- *Range.* L₂ = 2.292–2.786 at the 54 points.

**E2. ln 2, the largest round flat disc the cell holds.**
- *Principle.* In the flat metric of C/(Z + τZ), the largest disc about the puncture inside the Dirichlet cell has
  radius equal to the inradius, half the shortest lattice vector. It is the flat cut through the nearest half-period ½.
- *Formula.* e^(−L) = ½, so L = ln 2, independent of τ for reduced τ. The script finds the shortest vector exactly 1
  at all 54 points.
- *Caveat.* The principle is flat. As a horoball level it is ln 2 in B1667's convention, which differs from the flat disc
  by the Frobenius term (E3 below).

**E3. L_max, the maximal embedded horoball, which is the horocycle through a half-period.**
- *Principle.* The largest horoball about the cusp that does not overlap its own images (B1667, through min|c|).
- *New reading: its boundary passes exactly through a half-period.* In the z-plane every lift of the cusp is a lattice
  point.
  - The maximal horoball first touches the horoball at some lattice point v, and v is primitive: if v = 2v′, the
    horoball at v′ would be met first.
  - Two tangent horoballs meet in exactly one point.
  - The rotation by π about v/2 is an isometry, the elliptic involution composed with the translation by v. It swaps the
    two horoballs, so it fixes their contact point, which is therefore v/2, a half-period.
  - Hence L_max = max over half-periods p of [log(1/|p|) − Re g(p)]. The script takes p over the half-periods with
    |p| < 0.9, inside the series' disc of convergence.
- *Verified.* The script computes the right side independently of min|c|. It agrees with B1667's L_max to
  ≤ 1.6 × 10⁻¹¹ at all 54 points, median 1.0 × 10⁻¹¹.
  - ½ is a contact point at all 54 points, and the only one at 52. At τ = i, ½ and τ/2 tie; at τ = ω all three
    half-periods tie.
  - That the contact is at ½, rather than at another half-period, is checked at these points, not derived.
  - The referee also continued the developing map by ODE from the cell's centre to ½, with no series. That gives
    L(½) = L_max within 10⁻¹¹ at seven τ (uncommitted).
- *Formula where ½ is the contact.* L_max = ln 2 − Re g(½). Range 0.6431–0.6921.
- **So E2 and E3 are one principle, the cut through the nearest half-period,** taken in the flat metric and in the
  hyperbolic one.
  - They differ by the Frobenius correction: ln 2 − L_max equals Re g(½) within 1.6 × 10⁻¹¹ at every point, and ranges
    0.0011–0.0501.
  - This also accounts for B1838's "e^(−L_max) above the inradius": e^(−L_max) = ½·e^(Re g(½)).

**E4 (added by the web seat). L₄ = L₂ − π/2, the area-4 horocycle: the largest neighbourhood every cusp of every
hyperbolic surface embeds.**
- *Principle.* Take a torsion-free Fuchsian group containing T: u → u + λ, and any element γ with lower-left entry c ≠ 0.
  - The traces of T^n γ are a + d + nλc, an arithmetic progression with step λ|c|. They must avoid the open interval
    (−2, 2), since an element with |trace| < 2 would be elliptic.
  - That forces λ|c| ≥ 4. So h_max = 1/min|c| ≤ λ/4, and the horoball at h = λ/4, of area 4, is always embedded.
  - It is the best single-cusp bound: the thrice-punctured sphere attains it. Area 2 is the bound that holds for all cusps
    at once and stays clear of the collars, which is what makes it the collar lemma's.
  - For the once-punctured torus, with one cusp and no other cusp to clear, E4 is the universal level, and E1 the
    collar-compatible one.
- *Formula.* h₄ = λ/4, so L₄ = π/2 − (2π/λ) Im B = L₂ − π/2.
- *Range.* L₄ = 0.7215–1.2157 at the 54 points, all above L_max, as the theorem requires. B1667's cusp areas are
  4.210–6.000.

## 2. Excluded, with reasons

- **X. The cancelling radius (the density note's dated note).** Cc's reading is confirmed, with numbers.
  - As a level it is L_c = ½ log|G₂(τ)|. That is 0.572–0.644 at the 54 points: ½ log π at τ = i, and ½ log(2π/√3) at ω.
  - G₂ is complex away from Re τ = 0 and ½, by at most 4.5% here, so taking |G₂| is a convention. It moves L_c by at most
    5 × 10⁻⁴, while L_max − L_c is at least 0.047.
  - L_c lies below L_max at every one of the 54 points. So e^(−L_c) = 0.525–0.564 is beyond the maximal embedded horoball,
    and no embedded horoball has it.
  - The 0.551 quoted in cc's relay is the large-Im τ limit √3/π. At B1667's points the radius is 0.525–0.564, and the
    reading holds at each one.
  - It is also the wrong kind of object. It is the radius at which a finite disc cancels the constant of the density
    design's cross-kernel principal value. The ε² term behind it is exact only for a disc inside the cell, and 0.525–0.564
    lies past the cell's sides. It is not a property of the channel norms.
- **The zeta-regularised end.** Not entered. B1838 § 2b shows its scale is degenerate with L. This seat agrees.
- **The per-channel equality levels** (B1838's single-horocycle test: about 0.81 for j and k, 0.91 for 1 and 0.94–0.95 for
  i). Not entered. They are three depths, not one level. They are defined by matching the small-cut ansatz itself, so
  they cannot ground it.
- **(iii) a stationary level of a one-loop functional.** None entered.
  - No functional on record has a stationary level in L with its scale fixed by the geometry.
  - The channel norms grow monotonically with L at fixed τ, so positive sums of their logarithms have no stationary
    point. A signed, supertrace-like sum is not excluded by this; none is on record.
  - The zeta scale is degenerate (above).
  - This seat proposes none rather than choose one.
- **(v) THE EXACT END and THE HOROCYCLE AND THE HEIGHT.** These make nothing canonical beyond E1 and E3. Both used
  B1667's two horocycles, and the horocycle test's preference for L_max was the data's (P-402), not a principle.

## 3. For B1839 and B1840

- **E1, E2 and E4 sit at τ-dependent offsets from L_max:**
  - δ₁ = L₂ − L_max = π(1 − 2/A_cusp), 1.649–2.094 at the 54 points;
  - δ₂ = ln 2 − L_max, which equals Re g(½) where ½ is the contact, 0.0011–0.0501;
  - δ₄ = L₄ − L_max = π(½ − 2/A_cusp), 0.0784–0.5236. It is smallest, 0.078, at τ = 0.25 + 4i.
  - None is one value of B1839's δ grid. Evaluating them needs each row's own τ, as main's frozen-row instrument plans
    (P-688).
- **E3 is δ = 0.**
- **At any τ,** c(τ) comes from B1667's accessory solve, as B1839's census does it. L_max, L₂ and L₄ then follow by
  B1667's formulas, and E2 is ln 2.
  - E3's identity, ln 2 − Re g(½), holds where ½ is the first contact. At B1839's apexes, compute both routes, or state
    that as an assumption.

## 4. Scope

- The 54 points are B1667's.
- The contact at a half-period is proved for every τ (§ 1, E3). That it is ½ is checked at those points.
- E4's bound is a theorem for every torsion-free Fuchsian group.
- This seat did not open `look_run.txt` or `look.json`. No held-out quantity is computed, read or implied.
- The other two asks follow separately: the Higgs-twist law (ask 3), and the census's third opinion (ask 2, once
  `norms.npz` lands).

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE PRINCIPLED ENDS (principled_levels.py 4e22173b2 → 8fec64340) | "the web seat's list is main's three levels, all confirmed, plus one — E1 L₂, the collar lemma's area-2 horocycle; E2 ln 2, the largest flat disc the cell holds; E3 L_max, the maximal embedded horoball; and E4 L₄ = L₂ − π/2, the area-4 horocycle, the largest neighbourhood every cusp of every hyperbolic surface embeds (δ₄ = 0.078–0.524 above L_max) — with one new reading: E3 is exactly the horocycle through a half-period, the nearest one at all 54 of B1667's points (to 1.6 × 10⁻¹¹), so E2 and E3 are one principle in the flat and the hyperbolic metric, offset by Re g(½) = 0.001–0.050; the cancelling radius is excluded; no stationary one-loop level is entered" | `relays/CHAT1_TO_CC_2026-11-05_THE_PRINCIPLED_ENDS.md` @ the commit adding it | — | B1840, B1839, B1838, B1667, P-685, P-687 | 2026-11-05 |

0 of 19.
