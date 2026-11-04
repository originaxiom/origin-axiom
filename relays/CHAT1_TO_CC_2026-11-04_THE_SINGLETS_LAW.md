# THE HIGGS SINGLET'S LAW: ITS OWN TWIST CANNOT SIGN IT, AND ITS SIZE IS NOT FOUND FORCED

**From:** the web seat (chat1), 2026-11-04. **To:** cc (main); § 6 is also for the SM seat (W183).
**On:** RI-1 (P-591), P-566 Q1, FL-06; W183's open part ("the normalisation from first principles, and the rule that the
singlet reads the constant term").
**Kind:** data-free. No measured value is read. Nothing is computed on the candidate family's slope (a = 2/5, 3/5); no
D, no corner order, no θ̄. It assigns nothing.
**Check:** `relays/chat1_2026-11-04_singlet/singlet_law_check.py` (fdaecb4f7), run once against main at eb130f01f;
output in 317e233f7 (exit 0, empty stderr). The frame is FR-FIB as B1821's module builds it (B1656's residues, channel
norms and coupling; L_max; H = I) with the record's triplet DR. Numbers not in that output are marked post hoc; they
come from this seat or its two read-only referees.

**In one paragraph.** Main's frame fixes how a Higgs singlet must transform if the six, |V| and J are to be functions
of the physical point. Under the same line at τ + 1 the singlet must gain e^{iπ/4}, the triplet's own multiplier. Under
w → −w, w → w + 1 and w → w + τ it must not change. The mirror is a further, CHOSEN condition: the singlet must go to
minus its conjugate, or it carries a CP phase of its own.

The kernel's Laurent constant a₀ obeys A, P and the mirror. It fails T, which η³ repairs canonically, and it fails
w → −w, which is fatal to RI-1 as typed. Up's summed twist is minus down's, so a₀'s oddness between sectors and its
oddness under w → −w are one fact. Main's censuses list lines up to sign, and B1724 requires predictions not to depend
on the SL(2, ℤ) representative, −1 included. So on a census line RI-1's singlet is defined only up to a common sign. In
main's frame at τ = i the two signs give different six, |V| or J on 234 of 236 lines.

No singlet that is one function of its own sector's summed twist can differ between up and down and obey the law. A
sector-odd singlet must take its sign from outside its own twist. The routes on record are CHOSEN rules that compare
sectors: the hypercharge sign, through the adjugate reading (S291) or another sector's twist as reference. The Standard
Model's reading gives only a formal sign, and a different family. With a constant coefficient, the law and the mirror admit σ = i r η³/2 with r real. Its natural size
r = 1 is the null Higgs. The size is NOT FOUND forced: one real number r with its sign, or a chosen invariant function.

## 1. What was asked

- **RI-1** (P-591; the SM seat's retrieval sweep) identifies the Higgs's sector-odd singlet with the identity kernel's
  Laurent constant a₀(X) at the sector's summed twist u_X = (q_L + q_R)w: a₀(up) = −a₀(down) = −a₀(lepton). The
  identity is agy's Theorem 15 and this seat's kernels note, § 5.
- **W183** tested it at τ = i on its census, with a bare size (σ = a₀) and a natural one (|σ| = |DR·DR|^{1/2}). Its
  rule already warned that "a₀ has modular weight 1 and DR weight 3/2, so σ_X/DR is not invariant under the moves of
  τ". It left open "the normalisation from first principles, and the rule that the singlet reads the constant term".
- **The owner's item 1** (2026-11-03): is the singlet's size forced, data-free, before any card?
- **What the record holds:**
  - the frame's maps of (τ, w): B1790 lists the mirror, τ → −τ̄, w → −w, w → w̄, the T step, w → w + 1 and w → w + τ;
  - B1724's rule that predictions must not depend on the SL(2, ℤ) representative;
  - the triplet's T law (B1724's e^{iπ/4}) and its real structure (B1790's identity);
  - the singlet's mirror law, as an uncomputed candidate: agy's Theorem 11, (τ, c) → (−τ̄, −c̄), which is P-566's
    "amphichiral involution" on the singlet coefficient (B1827's DESIGN_NOTE, P566_NOTE § 2);
  - not the singlet's A, P, N or T laws.

## 2. The law (computed; (1) of the check)

A point is x = (a, b, τ), w = aτ + b. The relabellings are the strong-angle note's:
- A: (a, b + 1, τ);
- P: (a + 1, b, τ);
- N: (−a, −b, τ), the elliptic involution w → −w;
- T: (a, b − a, τ + 1), the same line at τ + 1;
- M: (a, −b, −τ̄), B1821's mirror.

With no singlet, the six, |V| and J are unchanged by A, P, N and T to 10⁻¹². M keeps the six and |V| and sends J to −J,
to 2 × 10⁻¹³.

**The test.** At 42 points (14 lines, slopes 2/5 and 3/5 excluded, at τ = i, 0.13 + 2.2i, −0.27 + 2.6i), each sector got a
random complex singlet c_X at x. At the relabelled point the singlet was c_X times one candidate multiplier, shared by
the three sectors. Of the candidates tried, exactly one per relabelling keeps everything. That holds in both readings:
every sector reading S, and the Standard Model's reading with up on S̃.

| relabelling | the singlet must become | departure | the other candidates tried |
|---|---|---|---|
| A, P, N | σ | ≤ 9.5 × 10⁻¹⁴ | −σ: ≥ 1.5 × 10⁻² |
| T | e^{iπ/4} σ | ≤ 1.1 × 10⁻¹² | the other seven eighth roots: ≥ 1.1 × 10⁻², up to 0.84 |
| M | −σ̄ (J → −J) | ≤ 2.8 × 10⁻¹⁴ | +σ̄, ±iσ̄: ≥ 1.5 × 10⁻² |

**The whole Higgs obeys the same law.** A random triplet h and a random singlet were carried by it:
- under T, σ → e^{iπ/4}σ and h → e^{iπ/4}(h₁, h₃, −h₂);
- under M, σ → −σ̄ and h → (h̄₁, h̄₂, −h̄₃).

Everything was kept, to 7 × 10⁻¹³. So the law belongs to the frame's matter, not to DR. On DR it reproduces B1724's T law
(to 2 × 10⁻¹⁶) and B1790's real structure (exactly).

**The N row also follows from the strong-angle note.** Its Theorem 1 (a proof sketch, with each law checked
numerically) gives bil(−x, −y; −u) = −bil(x, y; u). So Y_X(Nx; S) = Y_X(x; S) for every S. The T row follows from the
same mechanism: the kernels gain one common phase and B1724's rotation, the rotation fixes the singlet, and the singlet
must then gain the triplet's own phase.

**Per sector** (post hoc; the second referee, three random singlets on the 236 lines of § 3 at τ = i):
- down's six see the sign of down's singlet on every line;
- up's miss it on the 7 order-5 lines;
- the leptons' miss it on the 36 order-9 lines, B1703's protected first generations.

Under σ = a₀ itself the blind counts are 34 (up), 29 (down) and 74 (leptons). The theorem of § 3 uses only down's law.

**Which rules are required.**
- **T relabels one physical point:** the same line w on the same torus.
- **N identifies w with −w.** It is −I in SL(2, ℤ), the rotation z → −z of the torus, which carries the flat bundle of
  holonomy w to that of −w. B1724 requires predictions not to depend on the SL(2, ℤ) representative, and the
  covariance group it finds for S*, Γ⁰(2) = ⟨R, T², −1⟩, contains −1.
- **Main's censuses list lines up to sign.** B1712, B1713, B1716, B1723, B1725, B1726, B1729 and B1732 each key a line
  by min((a, b), (−a, −b) mod 1). So does the SM seat's own_lines, which is W178's and W183's census.
  - B1713 gives the reason: "w and -w give the same spectra in every sector" (B1703's law).
  - That is the matter's own N-invariance. The keying alone does not bind a new ingredient; B1724's rule does.
- A singlet that breaks T or N makes the prediction depend on how the point is written.
- **M maps a point to its CP image.** Keeping it is a CHOSEN condition: the singlet adds no CP phase of its own. It is
  not a relabelling.

## 3. RI-1's singlet breaks the law at N; a sector's own twist cannot sign its singlet

**a₀'s own laws** ((2) of the check, exact to 4 × 10⁻¹⁴). They were tested on the 11 of the 14 lines where a₀ ≠ 0; it
vanishes identically on the half-period lines (1/3, 1/6), (1/2, 1/3) and (1/6, 1/2).
- a₀(Ax) = a₀(Px) = a₀(Tx) = a₀(x);
- a₀(Nx) = −a₀(x);
- a₀(Mx) = −ā₀(x).

(1)'s M row derives, for the singlet, the law that agy's Theorem 11 and P-566 proposed. The Laurent constant obeys it
too.

The check uses the closed form 2πi Im(u)/Im(τ) + θ₁′(u)/θ₁(u) for a₀ throughout, as W183's route 1 does. Main's a0_of
agrees with it to 5 × 10⁻¹⁴, relative to 1 + |a₀|. That is on the 666 of 756 sector-points where main's identity residue
clears its 10⁻¹² cut.

**T: repairable, and invisible at τ = i.**
- a₀ lacks the triplet's e^{iπ/4}, as W183's rule foresaw.
- η³ carries it, and η³/2 is the canonical holomorphic root of the triplet's own invariant: DR·DR = η⁶/4 (row 1318's
  audit; here to 4 × 10⁻¹⁵).
- So a₀ e^{i arg η³} obeys T: 0 of 236 census lines move at τ = i.
- At Re τ = 0, η³ is real and positive, so this repaired rule equals W183's there.

**N: not repairable within RI-1.**

*Theorem.* Let a singlet be one function of its own sector's summed twist, σ_X = g(u_X, τ). If it obeys the law under
N, it is the same in up, down and leptons.

*Proof.* u_up = −3w and u_down = u_lep = 3w. So σ_up(w) = g(−3w, τ) = σ_down(−w), and N's law in down gives
σ_down(−w) = σ_down(w). ∎ Only down's law is used.

a₀'s oddness between sectors and its oddness under w → −w are therefore one fact. The sign flip is PROVED, since E₁* is
odd. On a census line (w ~ −w), RI-1's singlet is defined only up to a common sign, and the two signs give different
physics. That is COMPUTED, in main's frame, on W183's census at τ = i and in W183's reading ((3) of the check):

| variant (W183's) | lines whose six, \|V\| or J move (> 10⁻⁶) | by more than 0.01 | median | largest |
|---|---|---|---|---|
| B, σ = a₀ | 234 of 236 | 215 | 0.24 | 0.92 |
| N, natural size | 232 of 236 | 225 | 0.42 | 0.97 |
| even (down's phase in every sector) | 232 of 236 | 222 | 0.31 | 0.67 |
| the twelve fixed phases | 0 of 236 | 0 | — | 7 × 10⁻¹⁴ |

The census has 266 lines, and 30 are left out. The split, post hoc: the 10 on the family's slope, the 5 with 3w in the
lattice and the 15 half-period lines (W183's rule names the 5 and the 15).

**B1744 is an instance.** B1744's twisted residue quaternion obeys T0(3w) = T0(−3w). That is N's law for a Higgs read
from the twist, and by the theorem it is why H_u = H_d there.

**Scope.**
- The theorem covers singlets that are one function of their own sector's summed twist: RI-1, and P-566's "θ₁ alone".
- **A singlet that also reads another sector's twist can be odd and obey the law.** Post hoc, the second referee built
  σ_X = i a₀(X)·(a₀(down)/|a₀(down)|)·e^{i arg η³}.
  - It keeps every rule to 8 × 10⁻¹³ in both readings at 22 points, and gives σ_up = −σ_down = −σ_lep.
  - Its sign, a₀(X)/a₀(down), is the hypercharge sign. So it is § 4's "sgn" family under the hypercharge sign rule,
    which B1790 and FL-09 call imported, with the reference sector one more bit.
- **The sign can also come from the reading.**
  - The adjugate reading (down on adj S = σ − h·(i, j, k); S291, P-583) is exactly "sgn" (§ 4).
  - The Standard Model's reading (up on S̃) gives a formal sign and a different family (§ 4).
  - Both are reading choices. B1744 lists "which slot carries the twist" among the unforced choices.
- A singlet built from a leg's twist (up and down share the doublet's leg q_L w), or from other data, is a new
  construction with a chosen form, not RI-1. It is not classified here.

## 4. What the law admits

Write σ = (η³/2)·f. Then f must be unchanged under A, P, N and T; with the mirror, also f(Mx) = −conj f(x).

**With a constant coefficient** and the mirror kept, f = i r with r real. The families checked ((4) of the check, both
readings):
- σ = i r η³/2 in every sector ("uni"), r = ½, 1, 2;
- ε_X i r η³/2 with ε_up = +1 and ε_down = ε_lep = −1 ("sgn");
- ε_X i |a₀(X)| e^{i arg η³}, which has no free number.

All three keep every rule, to 1.2 × 10⁻¹². The real-axis controls r η³/2 and ε_X r η³/2 (r = 1, the only real-axis size
checked) keep A, P, N and T and break M by 0.50–0.52.

- **The adjugate reading.** "sgn", in the reading where every sector reads S, is exactly one singlet with up on S and
  down and leptons on adj S. The reason is algebraic: adj(σ + h·(i, j, k)) = σ − h·(i, j, k), and Y is linear in S
  (S291). So that reading keeps every rule on the imaginary axis and breaks M on the real axis (by 0.50 at r = 1).
- **det S_X = (1 − r²) η⁶/4**, to 4 × 10⁻¹⁵. The natural size r = 1 is the null Higgs, det S = 0. These are W183's null
  phases ±i (S291: c = ±i make det S = 0, B1659 J4).
- **In the Standard Model's reading, the uniform singlet i r η³/2 carries a formal sign.** Up's singlet over its
  triplet's root (η̄³/2), divided by down's over η³/2, is −1 to 12 digits; the real-axis control gives +1. P566_NOTE § 2
  noted this first ("an imaginary singlet flips sign between the sectors automatically"), and S290 scanned that reading.
  - The reading is CHOSEN: it is imported by hand and not derived (FL-09; B1790, NEGATIVE).
  - It is not the adjugate's odd family. Post hoc, both referees found the two differ, by up to 0.27 in the six and up
    to 0.98 in |V|.
- **Admissible singlets keep J = 0 on the mirror's fixed set.** On b = 0 or ½ at Re τ = 0, τ = i and 1.7i (12
  points), |J| ≤ 2 × 10⁻¹⁶ with them. With the real-axis controls |J| reaches 0.07, a CP phase of their own.

**W183's twelve phases at τ = i.** Only ±i obey M. On 226 of the 236 lines the other ten move under M (with J → −J).
The 10 lines that stay are the six of order 4 and four of order 12, where J vanishes identically. That was found after
the run and is not in the committed output.

## 5. The answer: the size is NOT FOUND forced

- The law fixes the singlet's multiplier. With the mirror, a CHOSEN condition, it also fixes the axis of a
  constant-coefficient singlet.
- The relabellings and the mirror leave the size free. For a constant coefficient that is one real number r, with its
  sign: no rule relates r to −r. Post hoc, the referees found the six move by up to 0.27 and |V| by up to 0.64 between
  the two.
- Otherwise the size is a CHOSEN invariant function, such as i|a₀|e^{i arg η³}, which has no free number but is a choice.
- On the admissible axis the natural size is the null Higgs. RI-1 as typed cannot carry the sector's sign. On record,
  a sector-odd admissible singlet takes it from a CHOSEN rule that compares sectors (§ 3, scope).
- **So no input is reduced.** A constant-coefficient singlet adds one real input and keeps the sign rule's choice.
- **The price is NOT FOUND.** It depends on the resolution in r that a card needs. Illustrative grids (CHOSEN) of |r|
  from 1/8 to 8, with both signs:

  | step | values | price |
  |---|---|---|
  | √2 | 26 | 4.70 bits (4.58 without the null r = ±1) |
  | 2 | 14 | 3.81 bits |
  | 4 | 8 | 3.00 bits |

  P-555's budget is 3.63 bits, before the sign rule's bit and the four CKM numbers' prior looks (S298).
- This note proposes no card.

## 6. For the record (proposals; main decides)

- **RI-1 (P-591).** The sign identity is the object's (Theorem 15; W183's O1). As the Higgs's singlet it is not a
  function of the census's lines: the sign flip is PROVED and the different physics COMPUTED in main's frame (§ 3).
  Proposed: while lines are identified up to sign (B1724's −1; the censuses named), RI-1's signed constant cannot be a
  candidate for an identification row. Its magnitude on the i axis is an admissible, CHOSEN size.
- **W183 (for the SM seat).** The counts here are main's frame, not W178's.
  - Its results under B, N and even are those of the census's representative, min((a, b), (−a, −b)). The other
    representative moves the six, |V| or J on 234, 232 and 232 of 236 lines (median 0.24, 0.42, 0.31).
  - **O8's four lines.** The six move by up to 0.099 on (4/9, 1/3) and (4/9, 2/3), and by up to 0.335 on (4/9, 4/9) and
    (4/9, 5/9). No D is computed here.
  - Post hoc (the second referee): down moves by 0.099 and 0.335, up by 0.049 and 0.229, and the leptons by at most
    2 × 10⁻¹⁵. So D, which compares down with the leptons, depends on the representative, and the sealed targets are
    those of one representative.
  - At τ = i the T repair changes nothing.
  - Its read-outs at Re τ 1/8 and 3/8 used rules without η³'s phase. There the singlet sits off the repaired one by
    arg η³ ≈ π Re τ/4, derived from η's product, not taken from the output.
  - Its twelve phases obey N. Only ±i obey M, and those are null.
  - The SM seat can verify the N law on its own code in minutes: the six at (a, b) and (−a, −b) under σ = a₀.
- **P-566 Q1.** Its three candidates in turn:
  - the hypercharge sign works only as a CHOSEN rule (the adjugate reading, or another sector's twist as reference);
  - the amphichiral involution is the M law, which tells no sector apart;
  - θ₁ alone is excluded by the theorem.

  The Standard Model's reading gives a formal sign of a different family. On the admissible axis the natural magnitude
  is the null Higgs, so a lift needs r ≠ ±1 or a chosen function.
- **P-558.** The agy lane's ½η³ "with no phase chosen" is the real-axis singlet, and it breaks the mirror. The
  admissible ½iη³ is null.
- **P-562 / B1744.** T0(3w) = T0(−3w) is N's law. The charge sign is erased by it, not by accident.
- **FL-06.** The sector difference cannot come from a sector's own twist. A CHOSEN rule supplies it: the adjugate
  reading, or the hypercharge sign with a reference sector. The Standard Model's reading gives its own family. Each
  comes at the cost of r and of that choice.

## 7. What stays out

- No measured value; no D; no corner order; no θ̄; nothing on the family's slope.
- The law is computed in main's frame, with B1821's module and main's norms, not W178's. It follows from how the matter
  transforms (§ 2), so W178's numerics should give it too. That is not checked here.
- Singlets built from more than their own sector's summed twist (§ 3, scope) are not classified.
- S (τ → −1/τ) is not used. B1724's S covariance passes the end as L + log|τ|, and the radius rule here is a function of
  Im τ alone (B1821's interpolant of B1667's column), so S does not relabel these points.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE HIGGS SINGLET'S LAW (RI-1's open part; singlet_law_check.py fdaecb4f7 → 317e233f7) | "No singlet that is one function of its own sector's summed twist can differ between up and down and obey the law" | `relays/CHAT1_TO_CC_2026-11-04_THE_SINGLETS_LAW.md` @ the commit adding it | — | P-591, P-566, P-562, P-558, P-583, FL-06, FL-09, B1744, B1790, B1724, B1713, B1821, B1827; W183 | 2026-11-04 |

0 of 19.
