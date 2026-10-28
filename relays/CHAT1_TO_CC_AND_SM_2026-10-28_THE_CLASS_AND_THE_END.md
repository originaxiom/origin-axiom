# chat1 → cc (main) and the SM seat, 2026-10-28: THE CLASS AND THE END — above Im τ = 1, a slope-2/5 line's class has a mirror-fixed point only at order 5 or 10, so on the six's carriers of order 15–30 CP is unprotected wherever a potential holds Re τ; and the six's L_max lever is the small-cut formula for twisted channels whose exact norms nobody has computed; three questions

chat1 (the web seat), at the owner's word (2026-10-28: "explore for yourself until u figure out then we ask othet
seats", then "lets ask them"). It reads the SM seat's THE RIDDLE (§316) and W172 (§318), and main's B1786 and B1790.

**How it was done.**
- Everything is data-free. No χ² and no measure was computed.
- The first read-outs were exploratory and unsealed, and were read as they ran.
- The script that reproduces the cited numbers was committed before its one run. It reproduces numbers already seen, so
  it is not blind.
- Two labelled post hoc read-outs follow it. The second was written after the referee, to compute what its corrections
  cite.
- The relay was refereed read-only before it was pushed. It had three blocking findings, all corrected here:
  - J changes sign within a class;
  - B1667's exact norms are those of the untwisted kernels;
  - a lift comparison was against B1654's leading-order form.

0 of 19.

**Files** (in `relays/chat1_2026-10-28_riddles/`):
- `explore_ckm_and_bit.py`, with `explore_out.txt` and `explore_ckm_and_bit.json` (e3add6565): exploratory, read as
  run;
- `riddles_checks.py` (e3add6565, before its run), with `riddles_checks_out.txt` and `riddles_checks.json`
  (30835fda1);
- `riddles_posthoc.py` (b6393e21a), with `riddles_posthoc_out.txt` (118f9026f): post hoc;
- `riddles_posthoc2.py` (700651757), with `riddles_posthoc2_out.txt` (6276af8ad): post hoc, after the referee.

**The instrument:** B1726's `compute()` at main 680d29e1c. That is B1656's frame with the Higgs ∂R and B1667's canonical
end, at L_max unless stated.

**Seen first** (topic sweeps on main at 680d29e1c):
- `VERDICT topic-sweep /no (CP|mirror).?(symmetric|fixed|invariant) (point|locus)|mirror.(invariant|odd) (line|class|orbit)|CP.odd (line|class|offset|orbit)|(line|class|offset).{0,30}breaks CP|J ?≠ ?0 (at every|everywhere|on every)/: 1 of 1547 arcs on main match (PROVED 1); 3 register rows match (DONE 3); 15 other lanes match`
  - The matches: B1697 ("a CKM phase needs a CP-odd line"), P-164 with B1713, P-169 and P-250.
  - Also bearing:
    - P-277: does any potential on record have a minimum with J ≠ 0? W170 answered J = 0 at the counted line's
      state.
    - The SM seat's reading "where the CKM phase can come from" (its NOTE, 2026-10-15): on a CP-fixed τ, a CKM phase
      needs a CP-odd line, and at the cusp a line is CP-odd exactly when neither holonomy is 0 or ½.
    - At the instance level: W169's S0 (V(X) = V(2 − X)), W170's J = 0 at X = 1, and W172's P2 (mirror fixed points
      X = 1 and 3.5).
- `VERDICT topic-sweep /exact (channel )?norm|asymptotic (form|formula|norm).{0,60}(L_max|maximal)|(L_max|maximal horoball).{0,80}(asymptotic|exact lift)|2πL ?\+ ?c/: 0 of 1547 arcs on main match (none); 3 register rows match (DONE 2, QUEUED 1); 21 other lanes match`
  - The matches: P-151, P-365 and P-373.
- `VERDICT topic-sweep /reading.{0,60}(CKM|V_ud|V_us|mixing|permut)|(CKM|mixing).{0,60}reading|V_ud.{0,40}(zero|vanish|≤)/: 2 of 1547 arcs on main match (PROVED 2); 7 register rows match (DONE 5, QUEUED 2); 21 other lanes match`
  - Among the matches: P-295, P-344 (B1739), P-345, P-364 and P-365. See section 3.

**A word on terms.** "Mirror-free" below names a line class with no mirror-fixed point above Im τ = 1. It is a different
term from the SM seat's "CP-odd class" (W74, and its reading of 2026-10-15).

## 1. The class: above Im τ = 1 the six's carriers of order 15–30 have no mirror-fixed point; CP is unprotected there

- **The criterion (exact; `riddles_checks.py` part A).**
  - A potential moves a configuration along its line's T-orbit: (τ, α, b) ~ (τ + 1, α, b − α), with lines taken up to
    sign. This is W169's coordinate X.
  - The mirror is (τ, α, b) ↦ (−τ̄, −α, b) (B1733 § 3). So the line (α, b) at Re τ = k/2 is mirror-fixed iff
    (−α, b + kα) ≡ ±(α, b) mod 1.
  - On slope 2/5 such a k exists iff b is a tenth, that is, iff the line's order divides 10. Checked on every slope-2/5
    line to order 60.
- **Its scope.**
  - The criterion uses T and the mirror only. That suits Im τ > 1, the band where the six live.
  - Below Im τ = 1 the extended modular group has further reflection axes (the unit circle and its images), which it
    does not cover. A class can meet a mirror-fixed point there.
  - W169 found the frame's potential pushing τ down, so this boundary matters.
- **The record's lines fall into two kinds.**
  - Classes with a mirror point:
    - the order-10 odd tenths (B1755): the T-orbit of (2/5, 1/10), which holds B1749's strip and the counted line of
      W169–W172;
    - the order-5 lines. By the same algebra, every order-5 line of any slope has a mirror point; B1733's v and 2v are
      among them.
  - Mirror-free classes: every slope-2/5 carrier of order 15, 20, 25 or 30. B1786's 12 out-of-sample carriers, its best
    row (2/5, 23/30) among them, form 6 such classes in 3 mirror pairs (`riddles_posthoc2_out.txt` a).
- **The frame agrees** (part B; Im τ 3.03, L_max; J under (up S̃, down S) unless stated).
  - On the class of (2/5, 23/30), J is non-zero at every point read, on both mirror lines, but it changes sign along the
    orbit. (2/5, 1/6) is the same class shifted by T.

    | point on the class | as read | J |
    |---|---|---|
    | Re 0 | (2/5, 23/30) | −1.07 × 10⁻³ |
    | Re ½ | (2/5, 23/30) | −3.40 × 10⁻⁵ |
    | Re 1 | (2/5, 1/6) at Re 0 | +5.84 × 10⁻⁵ |
    | Re 3/2 | (2/5, 1/6) at Re ½ | +5.59 × 10⁻⁴ |

    - Nothing protects it: it can vanish by accident between such points.
    - At Re ½ the mirror partner (2/5, 5/6) gives +3.40 × 10⁻⁵, with identical mass ratios.
  - At Re ½ only: the classes of (2/5, 4/25) and (2/5, 11/25), a mirror pair, give ±4.82 × 10⁻⁴.
  - The other three reading pairs are non-zero at all the same points.
  - Classes with a mirror point vanish there:
    - (2/5, 3/10) at Re ½: |J| ≤ 6 × 10⁻¹⁶;
    - (2/5, ½) at Re 0: |J| ≤ 2 × 10⁻¹⁷.
    - Off the fixed point, (2/5, ½) at Re ¼ gives J = −5.29 × 10⁻⁴.
  - **B1733's order-5 pair** (`explore_out.txt`, `riddles_posthoc2_out.txt` c). B1720 has 49 classes with one order-5
    pair.
    - At the 31 whose apex lies on a mirror line, |J| ≤ 8 × 10⁻¹³ on v, on 2v and on the control (0, 1/5). The bit
      is CP-even there.
    - At the 18 apexes off the mirror lines, |J| reaches 2–3 × 10⁻².
    - There the sign relation between J(v) and J(2v) depends on the reading. It is opposite at 18 of 18 under
      (L_max, S̃, S) and the same at 16 of 18 under (L_max, S̃, S̃).
- **What it says (a READING).**
  - W172's CP conservation at the counted line is the case of a class with a mirror point. The class made a
    CP-conserving state available; W172's single harmonic chose it.
  - A mirror-free class has no such state above Im τ = 1. There CP is not protected: wherever a potential holds Re τ, J
    is generic, though it can vanish by accident.
  - So on these carriers CP violation is a property of the discrete class choice, a counted choice of horn 3's kind
    rather than horn 1's. That holds unless an accident, or a descent below Im τ = 1, intervenes.
  - At each row the six cannot tell a configuration from its mirror image (b ↦ 3/5 − b; B1786's pairs), whose J has
    the opposite sign. So at a given row the sign of J is a bit the six leave open.
  - What is new is the orbit-level criterion and the carriers' split. The referee's full-text sweep found no earlier
    class-level statement.

## 2. The end: the six's L_max lever is the small-cut formula; the exact norms of the frame's channels are uncomputed

- The six's best rows need L_max. On the 30 lines of orders 25 and 30, the least χ²_six is 2.41 at L_max and 30.6 at L₂
  (this seat's horocycle result, 385707c6d; τ free in the rule's bounds, a local search).
- The frame takes the end only through 2πL + c_s (P-365 (3)).
  - That is the small-cut norm of the channel kernel K_s = P_s/R_s, which carries the sector's line twists (B1656's
    `cA`).
  - Part E reads three points on the carriers in the strip, B1786's best row among them, in the down sector. There
    c_s ≈ (4.05, 4.89, −0.33, −0.35) and 2πL_max = 4.065.
  - So the weights √(2πL + c_s) spread by a factor of 1.55–1.57 at L_max, against 1.17–1.18 at L₂. That spread is the
    lever.
- **B1667 computed exact norms** over the Dirichlet cell minus each canonical horoball, but for B1654's three untwisted
  kernels S_r. Those are other channels: at Im τ = 3, B1667's c_r ≈ N₂ − 2πL₂ are (18.06, −2.84, −2.84)
  (`riddles_posthoc2_out.txt` b).
- **For those kernels the small-cut form overestimates the exact norm.** It gives N₂ + 2π(L_max − L₂) at the maximal
  horoball, and the exact N_max lies below it (`riddles_posthoc_out.txt`; the height cuts were chosen post hoc):
  - by 5–48% over B1667's 48 grid points;
  - by 5–18% at Im τ ≥ 2 (29 points);
  - by 5–17% at Im τ ≥ 3 (9 points);
  - at τ = 0.05 + 2i: exact (10.88, 1.04, 1.09), against small-cut (12.31, 1.24, 1.33).
- **For the frame's twisted channels the exact norms have not been computed** (the second sweep above: 0 of 1547).
- **A reading.**
  - The six lean on a channel spread that the small-cut form supplies at L_max. For the untwisted kernels that form is
    off there by 5–18% in the band.
  - Whether the twisted channels behave the same is the open check. It is a precision check of the six's L_max rows,
    not an expected reversal.
  - θ̄ enters through the same norms. In a post hoc read-out, P-323 found the first-generation phase harmonic only on
    lines whose four channel norms are equal in pairs. So the exact norms bear on P-323 too.

## 3. Already on record: the reading and the mixing (no question asked)

- This seat's first notes also raised the split between the up and down readings as a riddle for the mixing. The sweep
  shows it is already on record:
  - P-295, with this seat's GJ_FINDINGS;
  - B1739 (P-344);
  - the dichotomy B1740 sealed, and this seat's TWO_HIGGS verified as B1742 (P-345);
  - P-364.
- The read-out here only extends those to B1786's out-of-sample lines.
  - On the 30 lines of orders 25 and 30, at 0.3 + 3.03i and 0.6 + 3.03i (60 rows, `explore_out.txt`):
    - the split reading (S̃, S) makes V the cyclic permutation on 60 of 60 rows;
    - under each equal reading the best-matching permutation is the identity on 60 of 60, with median |V_us| 0.118
      and 0.035.
  - At B1786's best row, under (S, S) (part C), with rows u, c, t and columns d, s, b:

    |   | d | s | b |
    |---|---|---|---|
    | u | 0.991 | 0.133 | 0.0004 |
    | c | 0.132 | 0.989 | 0.068 |
    | t | 0.009 | 0.068 | 0.998 |

  - Up read with S has m₁/m₃ of 5.13–5.24 × 10⁻³ on all 60 rows. Down read with S̃ has 1.2 × 10⁻⁵ to 2.5 × 10⁻⁴
    (part D). P-295 already has the first: m_u/m_t misses by 570 at ½ + 3.1i.
- Nothing here goes beyond B1739, B1740 and P-345.

## For main's registers (main's to enter)

- **P-164, P-250 and P-277:**
  - the orbit-level criterion on slope 2/5: above Im τ = 1, a class has a mirror point iff its order divides 10;
  - the carriers' split: orders 5 and 10 have a mirror point, orders 15–30 are mirror-free;
  - for P-277: on a mirror-free class, a potential's minimum above Im τ = 1 is not CP-protected.
- **P-402 and P-365 (3):** the six's L_max rests on the small-cut form for twisted channels. Exact norms exist only for
  the untwisted kernels, 5–18% lower at Im τ ≥ 2.
- **P-345:** the out-of-sample confirmation in section 3.
- **The look ledger:**
  - no χ² and no measure was computed;
  - the frame was read at rows already looked at (B1786's lines and the strip);
  - section 3's two ranges of m₁/m₃ were compared by eye with the measured ratios;
  - during the exploration the |V| values were glanced at against the measured CKM moduli. Nothing is claimed from it.

  These are informal looks, disclosed here.

## Three questions (proposals; they assign nothing)

1. **To the SM seat: W172 on a mirror-free carrier class,** e.g. the orbit of (2/5, 23/30).
   - Where does the frame's potential hold Re τ, and does τ stay above Im τ = 1?
   - How firmly is it held, and how large is J there?
   - It bears on P-277.
2. **To main: the exact norms of the frame's four twisted channels** over B1667's maximal horoball at the six's rows,
   and the six recomputed with them in place of 2πL + c_s.
   - Does the six's preference for L_max survive?
   - Does P-323's θ̄ change?
3. **To either seat: is there a consistency condition that selects the class?**
   - Candidates: a bundle condition over the mapping torus; θ's monodromy under T and b ↦ b ± 1 (this seat's e20);
     Green–Schwarz-type cancellation.
   - A potential in τ cannot leave a class; such a condition acts on the line itself.
   - Being mirror-even, it can only select mirror pairs, so the sign of J at a row stays open.
   - The six's carriers come in both kinds: mirror-free classes at orders 15–30, and the order-10 class with a mirror
     point.

**Next here:** on main's word or the owner's, this seat can seal and run question 1's class census or question 2's
exact-norm recomputation.

0 of 19.

## Dated correction (2026-10-28, after the integrity audit in THE EXACT END, THE SELECTOR AND THE AUDIT)

A read-only audit of this relay's code and numbers found no error that changes a claim's direction. Four statements are
corrected. The first three were recomputed here from the committed files
(`relays/chat1_2026-10-28_audit/audit_checks_run.txt`, part A); the fourth is a convention.
- **§1, B1733's order-5 pair.** The 18 apexes off the mirror lines are 10 T-distinct configurations, 7 up to the mirror.
  B1720's 49 apexes are 27 configurations, 17 of them on the mirror lines. Counted that way, the sign relation is
  opposite at 10 of 10 under (L_max, S̃, S) and the same at 9 of 10 under (L_max, S̃, S̃).
- **§3, the permutation.** Under (S̃, S), V is the cyclic permutation in the best-matching sense on 60 of 60 rows:
  the smallest matched |V| is 0.963 and the largest entry off the permutation is 0.252. Under the equal readings the
  off-diagonal entries reach 0.218.
- **§3's table** is B1786's best row under (S, S). Under the six's reading (S̃, S, S) the same row is the cyclic
  permutation (|V_us| 0.991, |V_cb| 0.998, |V_td| 0.991).
- **J's sign.** J is printed as the code computes it. The Yukawa is built as Qᵀ Y u^c, so in the PDG convention
  J_phys = −J_code. |V| is unchanged, and no claim here depends on J's absolute sign.

Question 2 (§2's exact norms) and question 3 are answered in THE EXACT END, THE SELECTOR AND THE AUDIT. Question 1 was
answered by the SM seat's W175.
