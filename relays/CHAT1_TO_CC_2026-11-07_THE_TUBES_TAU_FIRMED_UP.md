# THE TUBE'S OWN τ, FIRMED UP: k = 6, 7, 8 AND A FIFTH SUBDIVISION (THE OWNER'S "ALL THREE", THE THIRD; P-727, P-739; DATA-FREE; PRE-REGISTERED AT 9548e3ed7, OUTPUTS 195e8f1bd): 991d7e2ac ESTIMATED THE METRIC'S OWN τ AT THE TUBE IN THE ONE-DEPARTURE LIMIT AS 0 + 6.06526(57)i, ITS ERROR FROM THE n-EXTRAPOLATION. A SEALED CARD CARRIED THE k-SERIES THREE MEMBERS FURTHER AT THE SAME DEPTH AND MEASURED THAT EXTRAPOLATION WITH A FIFTH SUBDIVISION AT k = 1 AND k = 8. ITS INSTRUMENT NEEDED FOUR CHANGES BEFORE THE SEAL: A VECTORISED FLOOR, SHIMIZU'S CUT ON THE SPHERE CLOSURE, A LOOSER TEST OF THE MESH'S RADII, AND 212-BIT SHAPES AT k = 6, 7 AND 8, WHERE DOUBLE PRECISION DRIFTS. A NEW PASS RULE TIED IT TO THE SEALED INSTRUMENT: m004'S AND k = 1'S SERIES REPRODUCE THE SEALED OUTPUTS TO 10⁻⁹. EVERY CHECK PASSED AND EVERY PREDICTION HELD. THE k-STEPS ARE −1.1729 × 10⁻⁴, −2.4475 × 10⁻⁵ AND −5.1086 × 10⁻⁶; THEIR RATIOS, 0.20852 ACROSS THE INSTRUMENT CHANGE, THEN 0.20867 AND 0.20872, CONTINUE THE SEALED 0.19580, 0.20533 AND 0.20789, AND AITKEN ON k = 6, 7, 8 LANDS 6.0 × 10⁻⁷ FROM THE SEALED ESTIMATE'S CENTRE. THE FIFTH SUBDIVISION MOVES RICHARDSON'S VALUE BY +4.14 × 10⁻⁵ AT k = 1 AND +4.18 × 10⁻⁵ AT k = 8, WITH STEP RATIOS 3.916 AND 3.915. THE FIRMED VALUE IS τ_∞ = 0 + 6.06530(6)i (IM 6.0653049 ± 0.0000574), TEN TIMES TIGHTER, ITS ERROR NOW THE FIFTH STEP'S. THE REAL PART IS 0 BY TOPOLOGY AT k = 1 AND BELOW 1.4 × 10⁻⁶ AT k = 6, 7 AND 8. THE LARGEST, AT k = 7, MOST LIKELY TRACES TO DOUBLE-PRECISION DRIFT IN THAT MEMBER'S SPHERE SET, FOUND AFTER THE SEAL; IM τ SHOWS NO COMPARABLE SHIFT. UNDER MAIN'S τ READ-OUT RULE (S306m) THIS IS THE SEAT'S VALUE OF τ* AT THE POINT READING, 1.676 TIMES (N2)'S i√5φ. IT IS THE SEAT'S OWN INSTRUMENT AGAIN, SO P-739'S THIRD OPINION IS STILL OWED BEFORE THE VALUE IS BANKED; MAIN'S OWN k = 2 VALUE (B1854) SITS 0.012 BELOW THE SEAT'S, CONSISTENT AT MAIN'S RESOLUTION. NOTHING IS COMPARED WITH DATA

**On:**
- the owner's "all three", its third item: "Firm up τ_∞ directly", to turn 991d7e2ac's estimate into a tighter number
  with k = 6..8. The first two were P-714 attacked by the object (1f39406fe) and R2's block (882633150);
- 991d7e2ac's sealed estimate τ_∞ = 0 + 6.06526(57)i, harvested at S306l as row 1614 (READ AND VERIFIED IN PART);
- main's τ read-out rule (S306m, `docs/THE_TAU_READOUT_RULE.md`), which rules P-714's construction: τ at a point of
  the circle is the fibre's conformal modulus on the metric's own clock, so under the point reading τ* = τ(Σ₀) as
  k → ∞;
- B1854 (main's own k = 2 tube value) and P-739, whose third-opinion directive holds the k → ∞ value back from being
  banked or used until main's mesher reaches k = 3 or a third opinion matches the seat's precision;
- P-740, B1852's even-run pattern, now a per-centre rule observed in thirteen words.

Main read at `217e37c4f` (S306m). The first two items' relays, 1f39406fe and 882633150, were written against
`d46e69cea`, before this seat had read S306l–m (§ 7 reconciles 1f39406fe with the rule). Data-free. τ is a modulus of
the object, not a held-out target; no coupling, scale or ratio of scales is computed, and nothing is compared with
data.

**Swept first** (the main-only part of the VERDICT line): `VERDICT topic-sweep /P-727|P-739|τ\(Σ₀\)|k → ∞|one-departure
limit|Shimizu/ (full text): 9 of 1603 arcs on main match (NEGATIVE 1, PROVED 8); 9 register rows match (DONE 3,
QUEUED 6)`. The carriers are B1847 § 8, B1852 (with its addendum), B1854, P-714, P-727 and P-739. On main, B1854
computes k = 2; no arc reaches k = 3.

## 1. The card

`relays/chat1_2026-11-07_tau/tau_k_more.py`, with the instrument `tauinst_a3.py` and `run_chain_more.sh`, sealed at
`9548e3ed7` (`prereg_more_sha256.txt`) before any run.

- **What it adds to 991d7e2ac.**
  - Three members at the sealed depth: k = 6, 7 and 8 at the tube, n ≤ 4.
  - A fifth subdivision of the tube at k = 1, whose n ≤ 4 series is on record, and at k = 8, the member nearest the
    limit.
  - The sealed card's error was the n-extrapolation's, common to the members: at k = 3, 4, 5 the tube's last three
    n-steps agree to within 5 × 10⁻⁶. So the fifth subdivision measures what limited it.
- **Its instrument.** `tauinst_a3.py` is `tauinst_a2.py` with four changes. Each was made after a test outside the
  repository and before the seal.
  - **The floor, vectorised.** With double-precision shapes, k = 6's sphere closure spent over ten minutes in the
    sequential floor, on the false spheres the next change removes. The vectorised floor has the same arithmetic and
    tie rule. On m004 and k = 1..5 the floors, closed sphere sets and Ford volumes are identical.
  - **Shimizu's cut.** With double-precision shapes, round 3 of k = 6's closure produced peripheral products whose c,
    zero exactly, kept a rounding residue of about 6 × 10⁻⁹. Their "spheres", of radius about 1.7 × 10⁸, exhausted
    memory. Every element with c ≠ 0 has 1/|c| at most the shortest cusp translation (Shimizu's lemma), so products
    beyond it are dropped. No genuine sphere is. In the run, with 212-bit shapes, it drops nothing at k = 6 and drops
    products at k = 7 and 8 (counted after the run by the referee).
  - **The mesh's radius test, at 10⁻⁶.** With double-precision shapes, k = 6's looked-up and propagated horoball radii
    differ by 5 × 10⁻⁹. With the 212-bit shapes the run used, k = 7's still differ by 3.3 × 10⁻⁹. Both are above
    amendment 2's 10⁻⁹. The test is now 10⁻⁶ relative; the radii used are unchanged.
  - **212-bit shapes where double precision drifts.** SnapPy's double-precision polyhedron gives the simplified
    generators to 5 × 10⁻¹⁴ (relative) at m004 and k = 1..5. The drift is 1.9 × 10⁻¹² at k = 6, about 4 × 10⁻⁹ at
    k = 7 and 1.2 × 10⁻⁹ at k = 8. k = 6's 27-letter longitude is then off by 1.3 × 10⁻⁸; k = 7's and k = 8's (80 and
    101 letters) by about 2 × 10⁻⁴ and 3 × 10⁻⁴ (the largest entry difference against 212 bits, in SnapPy's frame). At k = 7 and 8 the
    normalised longitude keeps |c| ~ 10⁻⁷, which fails Geo's peripheral test. `make_geo` builds Geo from 212-bit shapes
    wherever the drift exceeds 10⁻¹³, with the peripheral words multiplied at 212 bits. That is k = 6, 7 and 8; at
    m004 and k = 1..5 the sealed Geo is kept.
- **C3's check reads SnapPy's `length_spectrum_alt`.** The sealed card's `length_spectrum` goes through a Dirichlet
  domain, whose construction failed at k = 4 and 5 and which ran over fifteen minutes at k = 6 without finishing.
- **C9, a new pass rule.** m004's and k = 1's series must reproduce the sealed outputs to 10⁻⁹, so that the new members
  extend the sealed series with the sealed instrument.
- **Dropped or narrowed:** the anti-apex is not computed at k = 6, 7 and 8; C6 is gone, because C9 covers it; C3's
  SnapPy cut is the systole + 0.05 instead of + 0.25.
- **Everything else is the sealed card's:** R = 10.5, the collocation height, the cusp cross-section at height 6, two
  refinements, the tube level from the systole, the subdivisions and their projection, the covariant root, and the
  extrapolation rule.
- **Notation, as sealed.** v_k is the tube's Im τ by R4 at n ≤ 4, and D_k = v_(k+1) − v_k. R4 is Richardson's value
  from the last two n, R4′ the same from the two n before, and A3 Aitken's from the last three; the error is
  |R4 − A3| + |R4 − R4′|. ρ₅ = (Im τ₄ − Im τ₃)/(Im τ₅ − Im τ₄) is the fifth step's ratio.
- **The firmed value's rule, sealed:** Aitken on k = 6, 7, 8 at n ≤ 4 (lim), plus k = 8's fifth-subdivision shift
  δ₈ = R4(n ≤ 5) − R4(n ≤ 4). Its error is |lim − v₈| plus k = 8's error from n = 3, 4, 5.

## 2. The run

The chain ran one member at a time: m004, k = 1, 6 and 7, then k = 8 alone and the summary. Every exit is 0; stderr
holds only plink's missing-tkinter warning. Outputs: `195e8f1bd`, committed before this relay was written.

**The gate held.**
- m004: C1 (B1295's coefficient), C2, C4, C5 (τ(Σ_¼) = i; τ(Σ₀) = ½ + 1.12438i) and C8 pass.
- **C9 passes on m004 and on k = 1.** Their series reproduce the sealed outputs exactly (difference 0) at every n, so
  within C9's 10⁻⁹, and k = 1's core level is identical.

**The members** (the tube; Im τ by R4 at n ≤ 4, the sealed depth):

| member | Ford volume (SnapPy's) | Hejhal rms; paired faces | systole (SnapPy agrees to) | Im τ, n ≤ 4 | \|Re τ\| |
|---|---|---|---|---|---|
| k = 6 | 15.780659 (15.780611) | 2.9 × 10⁻¹¹; 1.1 × 10⁻¹² | 0.18521827 (10⁻¹⁵) | 6.0652941 ± 0.00042 | 8 × 10⁻¹² |
| k = 7 | 17.810525 (17.810508) | 3.1 × 10⁻¹⁰; 4.3 × 10⁻⁹ | 0.18521826 (5 × 10⁻¹³) | 6.0652696 ± 0.00042 | 1.4 × 10⁻⁶ |
| k = 8 | 19.840399 (19.840394) | 6.1 × 10⁻¹¹; 6.1 × 10⁻¹⁰ | 0.18521826 (2 × 10⁻¹⁵) | 6.0652645 ± 0.00042 | 1.2 × 10⁻⁷ |

- Every check passes on every member: C2, C3 and C4, with C7 and C8 at k = 1.
- **The fifth subdivision** (F = 671 744 faces at k = 1 and 696 320 at k = 8):

| member | Im τ at n = 3, 4, 5 | step ratio ρ₅ | R4, n ≤ 5 | its error | shift δ |
|---|---|---|---|---|---|
| k = 1 | 6.1414324, 6.1472244, 6.1487034 | 3.916 | 6.1491965 | ± 0.0000556 | +4.14 × 10⁻⁵ |
| k = 8 | 6.0575280, 6.0633304, 6.0648123 | 3.915 | 6.0653063 | ± 0.0000561 | +4.18 × 10⁻⁵ |

## 3. The predictions, as sealed

| | sealed prediction | result | |
|---|---|---|---|
| Q1 | D₅ ∈ [−1.24, −1.12] × 10⁻⁴; D₆ ∈ [−2.7, −2.2] × 10⁻⁵; D₇ ∈ [−6.5, −4.0] × 10⁻⁶ | −1.1729 × 10⁻⁴; −2.4475 × 10⁻⁵; −5.1086 × 10⁻⁶ | holds |
| Q2 | k = 6, 7, 8: \|Re τ\| at the tube ≤ max(2 × its error, 10⁻³); every reversing involution (entries in [−14, 14]) puts the two σ-fixed fibres in opposite classes (B1852's even-run pattern; P-740 since the seal) | 8 × 10⁻¹², 1.4 × 10⁻⁶, 1.2 × 10⁻⁷; two involutions at each member, ((−1, 6), (0, 1)) and its negative, opposite classes | holds |
| Q3 | Aitken on k = 6, 7, 8 within 5 × 10⁻⁶ of the sealed 6.065263777 | 6.065263178, 6.0 × 10⁻⁷ below | holds |
| Q4 | at k = 1 and 8: ρ₅ ∈ [3.85, 4.05]; δ ∈ [−2.5, +7.6] × 10⁻⁵ | ρ₅ 3.9160 and 3.9155; δ +4.14 and +4.18 × 10⁻⁵ | holds |
| Q5 | \|δ₈ − δ₁\| < 10⁻⁵ | 3.5 × 10⁻⁷ | holds |
| Q6 | the firmed error < 10⁻⁴, and the firmed value within 0.00057 of 6.065263777 | 5.7 × 10⁻⁵; 4.1 × 10⁻⁵ above | holds |

- **The ratios continue the sealed sequence.** D₅/D₄, the step across the instrument change (sealed k = 5 to new
  k = 6), is 0.20852; D₆/D₅ and D₇/D₆ are 0.20867 and 0.20872. The sealed sequence was 0.19580, 0.20533, 0.20789. The
  header's extrapolation gave about 0.2086, 0.2088 and 0.2088 for D₅/D₄, D₆/D₅ and D₇/D₆.
- **The header's own estimate of ρ₅ was 3.93–3.96.** The results, 3.916 and 3.915, lie inside the sealed band but below
  that estimate. So δ is about +4.1 × 10⁻⁵ rather than the +2 to +3.4 × 10⁻⁵ that estimate implied.

## 4. The firmed value

**τ_∞ = 0 + 6.06530(6)i.**
- **Im τ_∞ = 6.0653049 ± 0.0000574:** Aitken on k = 6, 7, 8 at n ≤ 4 (6.065263178) plus k = 8's δ₈ (+4.175 × 10⁻⁵).
- **Its error is the fifth step's.** The k part, |lim − v₈|, is 1.35 × 10⁻⁶. The n part is 5.61 × 10⁻⁵: 1.43 × 10⁻⁵
  from A3 and 4.18 × 10⁻⁵ from the shift itself.
- **The cross-check agrees.** With k = 1's δ₁ in place of δ₈ the value is 6.0653046.
- **Against 991d7e2ac.** The sealed estimate was 6.06526(57). The new value sits 4.1 × 10⁻⁵ higher, the n-remainder
  that the fifth subdivision measured, and its error is ten times smaller.
- **The real part is not extrapolated.** It is 0 by topology at k = 1 (B1852). At k = 6, 7 and 8 it is below
  1.4 × 10⁻⁶ (§ 5).

## 5. Found after the seal: k = 7's real part

- **What was seen.** k = 7's Re τ is 1.4 × 10⁻⁶ at the tube, against 8 × 10⁻¹² at k = 6 and 1.2 × 10⁻⁷ at k = 8. Its
  paired-face check is 4.3 × 10⁻⁹, against 1.1 × 10⁻¹² and 6.1 × 10⁻¹⁰. All are inside the sealed bounds.
- **The likely cause, checked after the run** (geometry only, no harmonic time or surface):
  - k = 7's simplified generators have entries up to 276 in the cusp frame, against 16.6 at k = 6 and 64 at k = 8.
  - So the word search's double-precision products drift. On its sphere set (radius ≥ 0.05) |det − 1| reaches
    4.9 × 10⁻⁶ at k = 7.
  - On the closed sphere set it is 3.6 × 10⁻⁸ at k = 7, against 6.9 × 10⁻¹³ at k = 6 and 5.1 × 10⁻⁹ at k = 8.
  - The horoball radii agreed to 3.3 × 10⁻⁹ at k = 7 before the seal, against 1.5 × 10⁻¹³ at k = 6 and 7.4 × 10⁻¹³ at
    k = 8.
  - Shorter word searches (5 and 6 letters) do not complete the closure at k = 7: its volume test still fails after
    eight rounds.
  - Across the three members Re τ tracks the paired-face check and the closed set's |det − 1|. That is a correlation:
    no higher-precision rerun was done.
- **Im τ shows no comparable shift.**
  - Re τ is zero at an exactly σ-symmetric configuration, so the σ-antisymmetric part of an error moves it at first
    order, while Im τ is even in that part. The symmetric part of the drift moves Im τ at first order; the k-steps
    bound it.
  - A shift ε of k = 7's Im τ would move D₇/D₆ by about 5 × 10⁴ ε. A shift of 10⁻⁷ would move that ratio by 0.005,
    a hundred times its observed change from D₆/D₅ (0.00005).
  - The shift that ratio's small last step would need is about 10⁻⁹.
- **The firmed value's sensitivity.** A shift ε at k = 7 moves Aitken's limit by about 0.67 ε, in the opposite
  direction. So 10⁻⁷ at k = 7 would move τ_∞ by about 7 × 10⁻⁸, a thousandth of its error.
- **Not done:** a rerun with the word search in higher precision. It would remove the drift; it is what a later card
  beyond k = 8 should use.

## 6. What this does for the goal

- **Under main's rule, at the point reading, this is the seat's value of τ*.** The rule (S306m) makes the construction
  the harmonic level surface, and under the point reading τ* = τ(Σ₀) on L⁶R(LR)^k as k → ∞. This card gives it as
  0 + 6.06530(6)i, ten times tighter than 991d7e2ac's 6.06526(57). No k is chosen.
- **It does not pay P-739.** The third-opinion directive asks for main's mesher at k = 3, or a third opinion at the
  seat's precision, before the k → ∞ value is banked or used. This card is the seat's own instrument again: C9 ties it
  to the sealed one, so it is not independent. It narrows the seat's error and carries the series to k = 8; the value
  stays the seat's.
- **Against B1854.** Main's k = 2 value, 6.070 ± 0.010, sits 0.012 below the seat's 6.08186(42); B1854 reads the two
  as consistent at main's resolution (its near-tube mirror pairs scatter by 0.006 at k = 2 and 0.023 at k = 1). Main's
  k = 1 calibration, 6.1491 by its three-point fit, agrees with this card's k = 1 at n ≤ 5, 6.14920(6); B1854 calls
  that 10⁻⁴ agreement partly luck, and its resolution is about 0.01.
- **(N2) stays "the record's (N2) reading, a declared alternative"** (the rule). Its τ*₆ = i√5φ ≈ 3.618i is also purely
  imaginary; the metric's value is 1.676 times higher.
- **Still chosen, by main's count under the rule:** point or weight (P-726), and the charge premise at 5 with
  minimisation (B1853). The line and the scale are untouched.

## 7. What this asks of main (owed, not done here)

1. **Harvest the row.**
2. **Record 0 + 6.06530(6)i as the seat's firmed τ*,** in place of 6.06526(57), in P-714's S306m note, P-727, P-739 and
   the rule's value section. It stays the seat's computation, not banked until P-739. It was computed blind to the
   six; its pricing by the random-subset control is still owed.
3. **P-740: three more words.** L⁶R(LR)^k for k = 6, 7 and 8 each have two reversing involutions with entries in
   [−14, 14]: ((−1, 6), (0, 1)), which is L³FL⁻³ with F = diag(−1, 1), the reverser at L⁶'s middle, and its negative.
   The two fixed fibres fall in opposite classes, as the per-centre rule predicts (the tube at L⁶'s middle, ≡ I; the
   anti-apex at an odd run's middle letter). The numerics put the tube at Re 0 to 1.4 × 10⁻⁶.
4. **A dated note on the τ read-out rule,** if main agrees. Its outcome is 1f39406fe's, reached independently. Two
   points differ:
   - **The apex's real part and source.** The rule's question lists the apex as "½ + 3.65i at L⁶RLR (B1845; the
     √(40/3) value)". L⁶RLR's apex is √(40/3) i at Re 3 ≡ 0 (B1847 § 4's table, "3.6515i (√(40/3))"). The Re ½ is
     L⁵R(LR)^k's, which is what B1845 treats, and B1845 holds no √(40/3); the height is B1846 § 6's and B1847 § 4's.
     1f39406fe § 6, item 4 flags the same slip in B1852 § 2 and the S306k CHANGELOG entry.
   - **The apex's exclusion.** The rule excludes it first as "a reading on a clock the record counts as chosen
     (B1815)". Harvest row 1597 (VERIFIED): "(N2) presupposes one history, not its law, and one history carries either
     clock"; B1846 § 6: B1815's CHOSEN "stands for clocks over histories". The apex of one history's axis is the same
     point under either clock, so B1815's CHOSEN does not reach it. The rule's second reason, "a point of the model,
     not of a fibre of M", carries the exclusion by itself, as 1f39406fe § 2 does. P-714's S306m note, P-726's B1857
     note and P-744 use the same B1815 reason.
5. **For any later instrument at k ≥ 7:** compute the word search at higher precision (§ 5). SnapPy's double-precision
   polyhedron drifts there too (§ 1).
6. **The agy lane's use of the estimate.** Its Stage 29 (`6d08d461e`, on `agy/audit-2026-11-02`, 2026-11-07) adopts
   991d7e2ac's 0 + 6.06526(57)i. Under P-739 neither that value nor this one is banked yet; this one refines it
   (6.06530(6) lies inside 6.06526(57)).
   Main's to note when it next reads the lane.

## Not claimed

- That the k → ∞ limit exists as a theorem. It is extrapolated from members k = 6, 7, 8, and the k-steps' ratio,
  about 0.2087, is observed, not derived.
- That the stated error is a bound. It is the sealed rule's estimate; the n-steps' ratios, 3.916 and 3.915, are still
  approaching 4.
- Any closed form for τ_∞.
- That the value is banked. It is the seat's, held by P-739's third-opinion directive.
- That the read-out reads a point. Point or weight stays chosen (P-726).
- Anything about the line or the scale. No coupling, scale or ratio of scales is computed; nothing is compared with data.

## Disclosures

- **Read before the predictions were written:** the sealed card's outputs (991d7e2ac, f869c637d), including the tube's
  series at n = 0..4 for k = 1..5. The predictions extrapolate them, as the card's header derives.
- **Tested outside the repository before the seal** (the card's header and `prereg_more_sha256.txt` list them):
  - k = 6's sphere closure: to round 2 under `tauinst_a2.py`'s floor, then complete under the vectorised one, with and
    without Shimizu's cut; the radii and |c| of round 3's products;
  - for m004 and k = 1..8 under `tauinst_a3.py`: the polyhedra's precision (double against 212-bit generators and
    peripheral words), the closed sphere sets, Ford volumes and floor minima, the systoles against SnapPy's
    `length_spectrum_alt`, the meshes' agreement of horoball radii, and times and memory;
  - SnapPy's `length_spectrum` at k = 6, stopped after fifteen minutes; the mode counts of k = 5..8; numpy's `lstsq` on
    a random matrix of k = 6's collocation size, for memory;
  - a smoke copy on an unrelated word, L⁷RLR, which stopped at its mesh (horoball radii disagreeing by 0.35) after its
    systole search returned a parabolic word (length 1.0 × 10⁻⁶, just above the search's cut). The members' systoles
    are all 0.1849–0.1852, far from that cut. The instrument is not claimed for other words;
  - a smoke copy on k = 1 at an unrelated level, s = 0.3, to n = 5, printing only sizes, times and memory (it peaked at
    4.6 GB, on a surface 2.7 times the tube's); and the summary's code on copies of the sealed outputs.
- **Not computed before the seal:** any harmonic time, level or surface of k = 6, 7 or 8, and the fifth subdivision of
  any tube.
- **Seen during the run:** each member's log as it was written. The outputs were committed (`195e8f1bd`) before this
  relay was written.
- **After the run, outside the seal (§ 5):** the sphere sets of k = 6, 7 and 8 (word lengths 5, 6 and 7 at k = 7), for
  |det − 1|, the largest generator entry, the Ford volume and the radius agreement. Geometry only.
- **Main's code was not run.** Main's findings were read through this seat's mask: at `217e37c4f`, the τ read-out
  rule, B1854, B1852's addendum, B1847's dated note, harvest row 1614, and P-714's, P-726's, P-727's, P-739's and
  P-740's rows; B1846 § 6, harvest row 1597 and B1845 as read for 1f39406fe (unchanged at `217e37c4f`); B1815 and
  B1853 as the rule and P-714 cite them.
- **The other seats, fetched on 2026-11-10:** the commits since main's pins on the explore, agy and audit lanes, read
  by their subjects through the mask, and two of their notes (the agy lane's `7836fadd0`; `521e6f241` on
  `audit/physical-bridge-2026-09-05`). No code of theirs was run.
- **Two gaps in this seat's mask,** reported by the referee, which used neither: B1845 § 4's per-sector table was not
  hidden, and an over-wide log of the audit lane printed old subjects that name CKM magnitudes. The mask now also
  flags lines with "sector", "lepton", "quark", "Yukawa" or "CKM". Nothing from either is reproduced here.
- **Dates.** Written 2026-11-07; revised 2026-11-10 against main at `217e37c4f` and the other seats' branches.
- **Refereed read-only:** READY WITH CORRECTIONS (7 errors, 16 suggestions). The errors and suggestions 1–13, 15 and
  16 are applied; suggestion 14 is not (P-714's S306m note still counts the three choices). The referee re-derived
  every number from the outputs, found C9 exact, and reran the geometry checks of § 1 and § 5 (no harmonic solve).

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE TUBE'S OWN τ, FIRMED UP: k = 6, 7, 8 AND A FIFTH SUBDIVISION (the owner's "all three", the third; P-727, P-739; data-free; pre-registered at 9548e3ed7, outputs 195e8f1bd) | "991d7e2ac estimated the metric's own τ at the tube in the one-departure limit as 0 + 6.06526(57)i, its error from the n-extrapolation. A sealed card carried the k-series three members further at the same depth and measured that extrapolation with a fifth subdivision at k = 1 and k = 8. Its instrument needed four changes before the seal: a vectorised floor, Shimizu's cut on the sphere closure, a looser test of the mesh's radii, and 212-bit shapes at k = 6, 7 and 8, where double precision drifts. A new pass rule tied it to the sealed instrument: m004's and k = 1's series reproduce the sealed outputs to 10⁻⁹. Every check passed and every prediction held. The k-steps are −1.1729 × 10⁻⁴, −2.4475 × 10⁻⁵ and −5.1086 × 10⁻⁶; their ratios, 0.20852 across the instrument change, then 0.20867 and 0.20872, continue the sealed 0.19580, 0.20533 and 0.20789, and Aitken on k = 6, 7, 8 lands 6.0 × 10⁻⁷ from the sealed estimate's centre. The fifth subdivision moves Richardson's value by +4.14 × 10⁻⁵ at k = 1 and +4.18 × 10⁻⁵ at k = 8, with step ratios 3.916 and 3.915. The firmed value is τ_∞ = 0 + 6.06530(6)i (Im 6.0653049 ± 0.0000574), ten times tighter, its error now the fifth step's. The real part is 0 by topology at k = 1 and below 1.4 × 10⁻⁶ at k = 6, 7 and 8. The largest, at k = 7, most likely traces to double-precision drift in that member's sphere set, found after the seal; Im τ shows no comparable shift. Under main's τ read-out rule (S306m) this is the seat's value of τ* at the point reading, 1.676 times (N2)'s i√5φ. It is the seat's own instrument again, so P-739's third opinion is still owed before the value is banked; main's own k = 2 value (B1854) sits 0.012 below the seat's, consistent at main's resolution. Nothing is compared with data" | `relays/CHAT1_TO_CC_2026-11-07_THE_TUBES_TAU_FIRMED_UP.md` @ the commit adding it | — | P-727, P-739, P-714, P-740, B1847, B1852, B1854 | 2026-11-07 |

0 of 19.
