# THE DOUBLET INDEX (A DATA-FREE DESIGN STUDY): A HIGGS READ AT EACH SECTOR'S OWN TWIST GIVES EACH LINE'S NEGATIVE THE GLOBAL FLIP OF ITS READING, AND FOR THE CANDIDATE'S READING THE FLIP CHANGES THE LEADING EXPONENTS ON 2/5, SO WHILE w → −w IS A RELABELLING NO SUCH HIGGS GIVES THE CANDIDATE'S READING (EXCLUDED; FOR OTHER SPLITS, GENERICALLY); THE STANDARD MODEL'S OWN MECHANISM, ONE FIELD AND ITS CONJUGATE, IS NOT REACHED; THE TWO READINGS DIFFER BY 2‖S‖²(1 − ρ), ρ = ∣det S∣/‖S‖²; A DERIVATION BY ANY ROUTE WOULD EARN I-35, NOT EXTRA BITS

**From:** the web seat (chat1), 2026-11-04. **To:** cc (main).
**On:** the owner's go-ahead for the design study proposed after THE STEEPNESS MAP ("fetch other branches first and then
do it"): what an electroweak doublet index in B1656's frame would need, and whether anything native could fix the reading
(B1834's A05).
**Kind:** data-free. No measured value is read.
- § 2's proposition and § 4's identity are exact.
- The grade is exact for the candidate's reading, at leading order and given B1788's hypotheses. For other splits it is
  generic (§ 2).
- The checks re-verify the inputs on main's code.
**Checks:** `relays/chat1_2026-11-04_doublet/doublet_index_check.py` (2b636e652), run once against main at ac987e34b,
output in 65a58d2c3 (exit 0, empty stderr). A smoke run of a reduced copy preceded the commit, outside the tree. The
referee's rerun is byte-identical. POST HOC, after the second referee: `flip_slopes_posthoc.py` (7e1a79593 →
cb2d04eba).

**Sweep** (at ac987e34b): `VERDICT topic-sweep /doublet index|reading rule|conjugate Higgs|Higgs.s own twist|own
hypercharge twist|non-point|overlap coupling|fibre integral|fiber integral|Hermitian pairing|antiholomorphic Higgs|elliptic
involution|hypercharge sign|sign rule|I-35|FL-09|P-365|P-097/ (full text): 54 of 1581 arcs on main match (NEGATIVE 13,
OPEN 3, PROVED 38); 19 register rows match (DONE 12, QUEUED 7)`. Bearing on it:
- **B1790:** the reading is not derived in the frame; the global flip is physical; the imported sign rule would take the
  reading from 3 bits to 1 (I-35, UNEARNED). Its routes: an antiholomorphic or Hermitian Higgs slot, a non-point coupling,
  an effective-action selection.
- **B1728 Step 3:** negating both twists leaves the residues, M and Y unchanged and sends a₀ → −a₀ (PROVED).
- **B1744:** the Higgs at its own twist, T0(z) = T0(−z), is even. Its § 1 writes the pairing "Q u H; Q d H̃ and L e H̃".
  Forcing the reading "would need a different frame (a triple overlap of three twisted sections, magnetised-torus style)".
- **B1651:** no flat or harmonic Higgs couples the zero modes in the bulk. A point or density Higgs is not forced to the
  puncture; a (0, 1) Higgs is (its Szegő addendum; B1655's scope).
- **B1739, B1740, B1658, B1660:** the Higgs is nearly null; for a < 0 the F_a are nearly real and lose the hierarchy;
  m₂/m₃ = k_s∣d_S∣; and ∣det S∣/‖S‖² as a read-out.
- **P-394's row-1431 note:** "the direction left: a coupling odd in 3w".
- **P-562:** the twisted Serre derivative, expected even.
- **P-626:** N is a relabelling.
- **THE SINGLET'S LAW:** a singlet that is one function of its own sector's twist and obeys N is sector-even.

**The other branches, refreshed today:**
- **agy** (c5c9236df): its Phase 1 lists "(1C) Universal SU(2)_L pseudoreal conjugate reading selects S~S~S~". Its code
  sets the reading with no derivation and flags `zero_bit_cell_derivation_established: False`. Main's B05 types it
  CHOSEN.
- **The physical bridge** (646492da1): in its own architecture the weak doublet is also an open duty. Its surviving group
  is colour and electromagnetism, and "a zero colour/electromagnetic index does not decide weak chirality".

## 1. What a doublet index would have to do

- **In the Standard Model the reading follows from hypercharge.** In the frame's left-handed 6Y units, the net charges
  q_L + q_R are −3 for up and +3 for down and leptons. The frame's table lists the Higgs at +3 (b1656_funcs.SIXY).
  - A charge-conserving pairing puts up with a Higgs of +3, and down and leptons with one of −3: one field and its
    conjugate.
  - That is B1744 § 1's "Q u H; Q d H̃ and L e H̃", and (4) of the check.
- **In the frame, a doublet index would make the coupling enforce this itself.** The natural design reads one Higgs
  section H at the twist each sector needs: S_X = H(v_X), with v_X = −(q_L + q_R)_X·w, so v_up = 3w and
  v_down = v_lep = −3w. That is the hypercharge sign rule earned, not imported (I-35).
- **The frame has no such index** (FL-09). Its Higgs directions are functions of τ alone, and its "doublet" is the
  fibre's rank-2 bundle.
- **The reading is the Standard Model's tilde on the fibre's index.** The frame's units are pseudoreal,
  ε Ūε^T = U for U = 1, i, j, k. So S̃ = εS̄ε^T = σ̄ + h̄·(i, j, k), the covariant conjugate, and the adjugate is
  εS^Tε^T = σ − h·(i, j, k) ((1)(b)–(c), exact).
  - S̄ is excluded by T-covariance (P-297, B1724), not by pseudoreality.
  - Neither selects between S and S̃: both are covariant. So agy's "pseudoreal conjugate reading" is a choice.

## 2. The twist-read split gives each line's negative the global flip (exact, given B1728 and B1790)

**The matter at w and at −w is the same.** N (w → −w) negates both twists. B1728 Step 3 proves that this leaves the
residues, M and Y unchanged and sends the kernel's Laurent constant a₀ → −a₀; the frame's six, ∣V∣ and J keep N to
1.6 × 10⁻¹² (THE ADMISSIBLE SINGLET, K0). Check (2) re-verifies it per channel, on 256 census lines (W183's 266 minus
the family's slope) at three τ:
- R_s(−w) = R_s(w) to 1.2 × 10⁻¹⁴ (relative);
- a₀,s(−w) = −a₀,s(w) to 3.0 × 10⁻¹¹ (relative) on the 8 274 channel-points with ∣a₀∣ > 10⁻⁸.

Post hoc, the referee's probe:
- the other 540 compared points are exact zeros of a₀ (≤ 1.3 × 10⁻¹⁴), all on the 20 lines with 6w in the lattice;
- the 402 pairs below main's residue cut are below it at both w and −w (∣R∣ ≤ 2.6 × 10⁻¹⁵).

**Proposition.** Let each sector read S_X = H(v_X) for one Higgs section H, and let this give the frame's split reading
at a line w: S_down(w) ≅ S̃_up(w), where ≅ means equal up to an overall phase. Then at −w the reading is the global
flip of the reading at w.

*Proof.*
- Put S := H(3w), so S_up(w) = S and S_down(w) = S_lep(w) = H(−3w) ≅ S̃. At w the reading is (S, S̃, S̃).
- At −w the matter is the same (B1728). Up reads H(−3w) ≅ S̃, and down and leptons read H(3w) = S. So at −w the
  reading is (S̃, S, S) in the same S. ∎

**So, while N is a relabelling, no such Higgs gives the candidate's reading.**
- **For the candidate's own reading the flip changes the leading exponents on 2/5**, given B1788's hypotheses ((c) for
  m₁/m₃; up's ½ and 4/5 confirmed at 40 digits, B1790 § 3).
  - (S̃, S, S) gives the m₁/m₃ exponents up 4/5, down and leptons 11/20.
  - The flip (S, S̃, S̃) gives up ½, down and leptons 13/20 (B1790 § 3; THE STEEPNESS MAP's (5)).
  - So the two orientations of the candidate's line class differ, and N breaks.
- **Off 2/5, or for another section, the step is generic.** B1790 computed the flip as physical for DR at its points
  (same-point differences 0.074–7.7 in ln).
  - Post hoc (`flip_slopes_posthoc.py`): with DR, the flip leaves every sector's leading exponents unchanged on 3 of
    1 100 slopes with denominator ≤ 60 (1/2, 1/6 and 5/6).
  - On the other 1 097, at least one sector's exponents change.
- **The flip is trivial for every line when S̃ ≅ S, that is ρ = 1** (§ 4). There the two readings coincide and there
  is nothing to derive.
- **EXCLUDED, for the class "one Higgs section read at each sector's own twist, giving the candidate's reading", in
  FR-FIB as ruled** (P-626's relabelling, the coupling at the puncture). For other splits in the class, the exclusion is
  generic, not proven.

**A remark under N's law.** Suppose each sector's Higgs is unchanged by N up to a phase, S_X(−w) ≅ S_X(w). That law is
sufficient for the relabelling, and it is the one THE SINGLET'S LAW found for σ and h. Then any Higgs read at the twist
has S_up ≅ S_down:
- down's law gives H(3w) ≅ H(−3w), which is S_up(w) ≅ S_down(w);
- this is THE SINGLET'S LAW's theorem extended to the whole Higgs, and B1744's T0 is an instance;
- that the law is also necessary for a four-component S is not shown here. RI-1, which breaks it, moved the observables
  on 232–234 of 236 census lines.

**Not in the class, and splitting the sectors without breaking N:**
- the conjugate of one field: down reads H̃(3w), not H(−3w). This is the imported rule, or a non-holomorphic slot (§ 3,
  route (b));
- a singlet that reads a reference sector's twist (THE SINGLET'S LAW's scope: σ_up = −σ_down, the law kept).

## 3. The two routes that would reopen it, and their price

**(a) Give up N.**
- **The census doubles.** For a twist-read H that gives the candidate's reading, the line class of 2/5 and its
  negative become different points (§ 2). The same generically holds for any H with H(−v) ≇ H(v): RI-1's moved
  232–234 of 236 lines. The census
  identifies them (W183's min((a, b), (−a, −b))). So the family's slope 2/5 and its partner 3/5 (−2/5 mod 1) would
  become distinct.
- **The reading's last bit becomes the line's orientation** (§ 2's proposition): 2/5 against 3/5.
- **To reproduce S̃ itself, H must intertwine** the line's sign with the conjugation: H(−v) ≅ H̃(v).
  - Along a line the characteristics are constant: twist_of gives (p₁, −2p₂) for the line p₁τ − p₂, that is (a, 2b) for
    w = aτ + b.
  - Every Higgs direction on record is holomorphic in τ (R, DR, the a0 and t = −5/288 combinations, the F_a), and so is
    B1744's T0. H̃ is antiholomorphic.
  - If H(−v) ≅ H̃(v) held on an open set of τ along a line, the component ratios of H(−v) would be meromorphic and equal
    to antimeromorphic ones. So H's direction would be constant in τ on that line.
  - None of the record's directions is: each varies with τ. A twisted section with a τ-constant direction on each line
    would be new, and it is not examined. B1651 U3b's half-period triplets are τ-constant and null, and B1658 gives a
    nearly null S a hierarchy, so constancy alone is not ruled out.
  - The only identity on record that produces S̃ from a holomorphic section is B1790's dated note: on the mirror lines,
    S̃ ≅ DR with K negated (at τ, or at τ − 1 where Re τ = ½).
- **RI-1's a₀ is the record's one candidate for an N-breaking part.** Post hoc, a singlet of its natural size ∣a₀∣
  flattened the spectra on the mirror's axis, within that card's reach (THE ADMISSIBLE SINGLET, SCREENED, graded
  UNDECIDED).

**(b) A non-holomorphic slot, or a non-point coupling.**
- **The slot.** Down and leptons read the conjugate of the same field (W59's Hermitian slot), or a coupling sees the twist
  away from the puncture. B1790 § 4's non-point coupling would enforce the charge selection itself. B1744's triple
  overlap of three twisted sections (magnetised-torus style) is the standard instance.
- **This is the Standard Model's own mechanism:** one charged field and its conjugate, picked by charge conservation
  (Q̄Hd, L̄He, Q̄H̃u). § 2's exclusion does not reach it.
- **At the puncture, though, the charge sign is erased** (B1744: H_u = H_d). So in FR-FIB as ruled, charge conservation
  selects nothing there, and the slot is the imported rule (I-35).
- **An overlap leaves FR-FIB's point coupling.**
  - Within S01 (the flat bundle, an ANSATZ) it needs a density-type Higgs. B1651's Szegő addendum couples one by
    ∫ v(z) φ(z), with its profile free.
  - B1744's magnetised overlap leaves S01 as well.
- **N can stay a relabelling if the Higgs obeys N's law.** Then the census does not double. B1744's even T0 with the
  conjugate slot is an instance; an N-odd part (a₀-type, RI-1) breaks it.
- **The leftover bit is which charge sign gets the holomorphic slot**, I-35's bit. With SIXY's +3 and the holomorphic
  pairing, it gives (S, S̃, S̃), A05's flip (§ 5).
- **On record:** the SM seat found no slot that assigns the reading (row 1431), and no non-point coupling is built.

**The price, in bits and in joints.**
- Either route takes A05 from 3 bits to 1. That is B1790 § 4's count for the imported sign rule.
- So a derivation would earn I-35. The identification ledger counts I-35 as UNEARNED, an unpriced observer input that
  keeps the input count a lower bound.
- A05's menu would shrink to one bit, and A05 would stay a borrowed joint for that bit. A derivation would not cut bits
  below B1790's count.
- Route (a) moves the last bit into the line's orientation (A02); route (b) leaves it as the slot's charge sign.

## 4. The two readings differ by 2‖S‖²(1 − ρ) (exact)

For S = σ + h·(i, j, k), with ‖S‖² = tr(S†S)/2 = ∣σ∣² + ∣h∣² and det S = σ² + h·h ((1)(d)):

**min over φ of ‖S̃ − e^{iφ}S‖² = 2‖S‖²(1 − ρ), with ρ = ∣det S∣/‖S‖² ∈ [0, 1]**, attained at φ = −arg det S, because
⟨S̃, S⟩ = tr(S̃†S)/2 = det S. Checked on 2 000 random S to 10⁻¹⁵ ((1)(e)).
- The readings coincide up to a phase exactly when ρ = 1, that is, when S is a phase times a real quaternion. A phase
  changes no spectrum, ∣V∣ or J.
- They are farthest apart when S is null (ρ = 0).
- ρ is on record as a read-out: B1739's reality r for a triplet, B1660 C3's ∣det S∣/‖S‖², and B1658's d_S. The identity
  tying it to the distance between the readings is the new piece.

Check (3) gives ρ over Im τ 1–4 and Re τ 0–½. In the band it barely depends on Re τ.

| direction | Im τ 2.0 | 2.5 | 3.0 | 4.0 |
|---|---|---|---|---|
| DR | 0.13 | 0.028 | 0.0058 | 0.00025 |
| R, t = −5/288 | 0 (null, to 10⁻¹⁶) | 0 | 0 | 0 |
| F₆ / F₁₀ / F₂₆ | 0.045 / 0.075 / 0.19 | 0.0093 / 0.016 / 0.04 | 0.0019 / 0.0032 / 0.0084 | 8 × 10⁻⁵ / 1.4 × 10⁻⁴ / 3.6 × 10⁻⁴ |
| the a0 combination, F₋₂ | 0.94 | 0.99 | 1.00 | 1.00 |
| F₋₁₀, F₋₆ | 1.00 | 1.00 | 1.00 | 1.00 |
| DR with σ = i r η³/2: r = ½ / 1 / 2 | 0.092 / 0 / 0.25 | 0.021 / 0 / 0.075 | 0.0043 / 0 / 0.017 | 1.9 × 10⁻⁴ / 0 / 7.5 × 10⁻⁴ |

- DR's row is B1739's r, and DR·DR = η⁶/4 holds to 4 × 10⁻¹³ on the grid ((0)).
- F₁₄, F₁₈ and F₂₂ (not in the table) fall between F₁₀ and F₂₆. F₁₈'s row equals DR's to the printed digits.
- The admissible singlet at r = 1 makes S exactly null.
- **So in the band S and S̃ are farthest apart for the nearly null Higgs that gives the hierarchy.** For DR at Im τ 3.0
  the squared distance is 2‖S‖²(1 − 0.006).
- **For the a0 combination and the negative-weight F_a, ρ → 1 and the reading nearly drops out.**
  - For the a < 0 directions B1740 already sealed why: they are non-null, align the light generation under every
    reading pair, and lose the hierarchy (LAW_MAP's "the dichotomy sealed").
  - The a0 combination's row equals F₋₂'s at every Im τ, to the printed digits.
  - THE STEEPNESS MAP's directions with no m₂-steep slope (a0, F₋₁₀, F₋₆) are these.

## 5. The label "the Standard Model's reading"

- **The Standard Model fixes only the relative pattern:** up opposite to down and leptons. It can call either field the
  Higgs. B1790 says as much: H̃ "identified by hand", the pattern the content. In the frame the global flip is physical
  (B1790), so naming one partner "the Standard Model's" needs an identification of S.
- **The frame's pairing.** With its left-handed charges and its Higgs at 6Y = +3, the charge-balanced pairing puts up with
  the +3 field and down and leptons with its conjugate (B1744 § 1; (4)). The coupling is complex-bilinear in S and the
  left-handed matter (B1790 § 2), so the field that enters unconjugated is the one whose flavour part is S.
  - If S is the flavour part of the +3 field, the pairing gives (S, S̃, S̃).
  - If S is the flavour part of the −3 field, it gives (S̃, S, S), A05's.
- **So A05 takes S to be the flavour part of the conjugate of the table's H.** That is consistent. But it is the
  identification the data selected post hoc (B1790 § 4), not one the table supplies.
- **The label "the Standard Model's reading" for (S̃, S, S) names a convention.** It goes back to B1660's "the Standard
  Model's H̃ for the up quarks", the four-component form's statement, and B1739's and B1740's titles use it. This seat's
  THE STEEPNESS MAP used it too ("(S̃, S), the Standard Model's"). Both global-flip partners have the Standard Model's
  pattern. Read that row as "the up-conjugate reading".

## 6. What it means

- **Within FR-FIB as ruled, the candidate's reading cannot come from a Higgs read at each sector's own twist: EXCLUDED**
  (§ 2's class). For other splits it is excluded generically, not proven. The basis is § 2's proposition with the flip's
  effect on 2/5's leading exponents, given B1788's hypotheses.
- **Not examined:**
  - rules from other data, from a leg's twist, or from a reference sector;
  - couplings at B1651's half-periods;
  - non-point couplings: a density-type Higgs (B1651's Szegő addendum) and B1744's magnetised triple overlap;
  - non-holomorphic slots (W59);
  - effective-action selection;
  - a twisted section with a τ-constant direction on each line (§ 3).
- **A05 stays CHOSEN.** Route (a) needs a native N-breaking section that intertwines, and none is on record. Route (b)
  needs a slot or coupling not built.
- **What a derivation would buy:** it would earn I-35, taking A05's 3 bits to 1 on solid ground. That is B1790's count,
  not more.
- **The reading's size is the Higgs's nullity** (§ 4). The hierarchy wants ρ ≪ 1, and a twist-read split under N
  generically needs ρ = 1.
- **No input is removed.**

## 7. For the record (proposals; main decides)

- **FL-09, P-394, P-295.**
  - Record § 2's proposition: a twist-read split gives each line's negative the global flip. For the candidate's reading
    the flip changes 2/5's leading exponents.
  - Grade that route EXCLUDED within FR-FIB as ruled for the candidate's reading, and generically for other splits.
  - Keep A05 CHOSEN, with the two reopening routes of § 3. A derivation would earn I-35; it would not cut bits below
    B1790's count.
- **I-35.** Its row names what would earn it: "an antiholomorphic or Hermitian Higgs slot, or a twisted section the
  coupling acts on".
  - The twisted-section route, if it is to give the candidate's reading, needs N broken (§ 2; generically for other
    splits).
  - The slot remains (route (b)). At the puncture it is the imported rule itself.
- **P-562, for the reading only.** T0(z, τ) = T0(−z, τ) identically (B1744), so its Serre derivative is even under N,
  whether taken at fixed z or along the line (z = 3w and dz/dτ = 3a both flip sign). By § 2's remark it reads the same
  Higgs in up and down, so nothing more needs computing for the reading.
  - P-562's open item is the computation itself: the twisted Serre derivative in the four-channel frame, which main
    expects to be a same-sign singlet that does nothing for the corners.
  - Under the adjugate reading for down (P-566's S290–S291, P-583), an even singlet becomes relatively odd. THE
    ADMISSIBLE SINGLET, SCREENED listed that case as untouched, and it stays open.
- **P-626.** The ruling excludes the candidate's reading from a Higgs read at each sector's own twist (§ 2), and other
  twist-read splits generically. Under N's law it excludes every split read at the sector's own twist (§ 2's remark). The conjugate-slot and
  reference-sector constructions are outside both. Reversing the ruling is route (a)'s price: the census doubles, and
  2/5 and 3/5 part.
- **B1739, B1740, B1658.** The identity min_φ ‖S̃ − e^{iφ}S‖² = 2‖S‖²(1 − ρ) ties r, d_S and B1660's ∣det S∣/‖S‖² to
  the distance between the readings.
- **Labels.** In A05's basis and in B1739's and B1740's tables, "the Standard Model's reading" would read better as "the
  up-conjugate reading (S̃, S, S)". THE STEEPNESS MAP's row "(S̃, S), the Standard Model's" is corrected here (§ 5).
- **agy's (1C).** Pseudoreality makes S̃ the covariant conjugate, and T-covariance excludes S̄ (P-297). Neither selects
  between S and S̃ (§ 1). B05 stays CHOSEN.

## 8. Scope and what stays out

- **The frame:** B1656's point coupling at the puncture, through B1821's module at main ac987e34b; DR unless named;
  H = I.
- **The check:** the matter's parity re-verified on 256 census lines at three τ (0.2 + 2.5i, 0.45 + 3.1i, 0.05 + 1.7i),
  and ρ on a 77-point grid.
- **The class:** one Higgs section read at each sector's own twist. The grade's exact part is the candidate's reading,
  at leading order, given B1788's hypotheses.
- **Out:** no data; no candidate address (the family's slope refused by the check's guard); no D, no θ̄, no
  inter-sector value. The steepness rows cited are leading-order (THE STEEPNESS MAP).

## Dated correction (2026-11-04, the seat's re-check at the owner's "are u sure sure sure?")

Five changes from the text at a5b5e416b. A second read-only referee checked them (PASS WITH CORRECTIONS: one blocking
finding and six corrections, all applied).

1. **The grade's scope is narrower.**
   - EXCLUDED is now exact only for a twist-read Higgs that gives the candidate's reading. The flip changes 2/5's
     leading exponents, given B1788's hypotheses.
   - For other splits the exclusion is generic. With DR the flip leaves every leading exponent unchanged on 1/2, 1/6 and
     5/6 (3 of 1 100 slopes; the second referee's probe, then `flip_slopes_posthoc.py`).
   - The headline, the Kind line, §§ 2, 3, 6, 7, 8 and the harvest row are changed to match.
2. **§ 7's "P-562: closed" was wrong.** Only its reading question is settled. Its open item is the computation itself.
   Under the adjugate reading, an even singlet becomes relatively odd; this seat's admissible-singlet card had listed
   that case as untouched.
3. **§ 3 (b) now says the route left open is the Standard Model's own mechanism**, one charged field and its
   conjugate, which § 2's exclusion does not reach.
   - At the puncture the charge sign is erased (B1744), so there the slot is the imported rule.
   - An overlap leaves the point coupling. Within S01 it goes through a density-type Higgs (B1651's Szegő addendum);
     outside S01, through B1744's magnetised overlap.
   - N stays a relabelling only if the Higgs obeys N's law.
4. **The sweep's B1651 line was wrong.** "Couplings sit at points only" contradicted B1651's Szegő addendum and B1655's
   scope.
5. **The 2/5 exponents are now stated with B1788's hypotheses** ((c) for m₁/m₃), not as "exact".

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE DOUBLET INDEX (doublet_index_check.py 2b636e652 → 65a58d2c3; post hoc flip_slopes_posthoc.py 7e1a79593 → cb2d04eba) | "a Higgs read at each sector's own twist gives each line's negative the global flip of its reading, and for the candidate's reading the flip changes the leading exponents on 2/5, so while w → −w is a relabelling no such Higgs gives the candidate's reading (EXCLUDED; for other splits, generically); the Standard Model's own mechanism, one field and its conjugate, is not reached; the two readings differ by 2‖S‖²(1 − ρ), ρ = ∣det S∣/‖S‖²; a derivation by any route would earn I-35, not extra bits" | `relays/CHAT1_TO_CC_2026-11-04_THE_DOUBLET_INDEX.md` @ the commit adding it | — | FL-09, B1790, B1728, B1744, B1651, B1739, B1740, B1658, P-394, P-295, P-562, P-626, B1834 (A05) | 2026-11-04 |

0 of 19.
