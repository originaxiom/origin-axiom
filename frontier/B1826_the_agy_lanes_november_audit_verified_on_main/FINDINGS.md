# B1826 — THE AGY LANE'S NOVEMBER WORK, VERIFIED ON MAIN: THREE RESULTS KEPT (THE CHANNEL NORMS ARE SECTOR-BLIND; B1788's HYPOTHESIS (b) FAILS IDENTICALLY ON THE SLOPES 1/12, 1/4, 5/12; B1825's MISS IS A CKM CORNER INVERSION), EVERY "PARAMETER-FREE" CLAIM DECLINED

**Verdict: PROVED for the three results below (each recomputed by main's own code on main's evaluator); every claim of a
derived parameter, a zero-bit selection or a closure is DECLINED (post-hoc fits, by the lane's own concession and two
independent audits, main's provenance check confirming the decisive one). 0 of 19.**
- **The source.** The agy lane's branch `agy/audit-2026-11-02` (16 commits, 2026-11-02 22:39 to 2026-11-03 12:11, forked
  from main at 64a2a3d4e, B1825's output committed unread; nine relays, about 11 000 lines). Its first relay read B1825's
  output out and decomposed it; the later ones build a new frame (FR-COV) and escalate to a "Master ToE closure".
- **Two audits of it on record**, both seats, both read here in full at their conclusions: the physical-bridge lane's
  source review (`395b27210`, `audit/physical-bridge-2026-09-05`) and the independent audit lane
  (`audit/independent-2026-11-03`, `9d5129445` → `4b91b9be7`), which recomputed every late claim.
- cc (main), 2026-11-03, at the owner's word ("fetch all other seats and pay special attention and seriousness to agy's
  new work"). Credit: the agy lane for the results kept (cite agy:d80722af6); the SM seat for the closed form (sm:W177,
  harvest row 1496); the independent audit lane for the scope of the corner inversion and the pricing of the late claims.

## 1. Kept, verified on main (verification/main_checks.py, cusp_b_check.py; outputs beside them)

1. **The twisted channel norms are sector-blind.** For each channel s ∈ {1, i, j, k} the regularised norm c_s(τ, w) of
   B1656's frame is the same in the up (1, −4), down (1, 2) and lepton (−3, 6) sectors: the largest spread over three
   generic (line, τ) points and all channels where defined is **1.3 × 10⁻¹²** (main's `cA`). The lane's reason: the
   normalised kernel depends only on the Higgs twist ū = (q_L + q_R)w = ∓3w (Riemann's bilinear identity cancels the
   δ-dependence), and |K(−z; −ū)| = |K(z; ū)|. The closed form behind it (digamma and Hurwitz–Lerch) is the SM seat's
   W177, already harvested; new to main is the statement that the three sectors share c_s, so the evaluator computes it
   three times per point.
2. **B1788's hypothesis (b) fails identically on three slopes, not one.** c_j + c_k − c_1 − c_i ≡ 0 on the slopes
   α ∈ {1/12, 1/4, 5/12}: within 5 × 10⁻¹² on every line tested — (1/12, 0), (1/12, 1/12), (1/12, 5/12), (5/12, 0),
   (5/12, 1/3), (1/4, 0), (1/4, 1/2) — in all three sectors and at every τ tested (Im τ 1.8–4), not only in the cusp limit;
   it does not vanish on 2/5 (−9.0 to −10.0) or 1/7 (75–105). The lane derived the cusp limit (ψ(ν) + ψ(1 − ν) takes one
   value at ν and ν + ½ only for ν ∈ {¼, ¾}, i.e. {3α} ∈ {¼, ¾}); B1785 had seen α = 1/4. Main's finding beyond the lane's
   statement: the vanishing is exact at finite τ on these slopes. (The lane's replacement of hypothesis (a) by
   fermion-independent exponents is not verified here; the independent lane reports it holds in part — (a) fails in 18 of
   171 cases — and that its "explains B1788's anomalies" step mixes 2π and 4π conventions. Left open: P-559.)
3. **B1825's miss is a CKM corner inversion.** At B1825's least-χ²_ten address ((3/8, 3/8), DR, L₂, S̃S̃S, τ = 0.0934 +
   2.7426i) the frame's full |V| has **|V_ub|/(|V_us||V_cb|) = 1.063** and **|V_td|/(|V_us||V_cb|) = 0.094**, so
   **|V_ub|/|V_td| = 11.3**, and |J|/J_max ≈ 0.084: the Cabibbo rotation enters the (1,3) corner instead of the (3,1).
   This is the mechanism of B1825's dominant pulls (|V_ub| +12.6σ, |J| −7.2σ). The lane's account: a hierarchy pushes the
   Higgs vector towards the C³ null cone, locking both sectors' lightest left vector to ĥ*, with θ₁₂ of each sector
   inversely proportional to its m₂/m₃, so the steeper up hierarchy carries the larger 1–2 angle and it multiplies the 2–3
   rotation from the left. **Scope (the independent lane, not re-run here):** a strong tendency, not a no-go — in a scan
   of 15 532 rows, 52 of 250 hierarchical rows have |V_ub| < |V_td| and 17 of those have sin δ > 0.5. Read with B1713 and
   B1720 (masses and mixing do not meet) and B1825: where the six fit, the frame's mixing is inverted.

## 2. Declined (not derivations)

- **FR-COV's "pass" of B1825's gates** (Theorem 7: χ²_ten 7.2 at (2/5, 0), F₁₀, L₂, S̃S̃S̃ with sector scalars c_u = −i√2,
  c_d = −√(e^{iπ/4} − 1), c_e = −1): a post-hoc fit, never sealed; the targets are hard-coded in the lane's source.
  - **τ was fitted, then named.** Main's check of the lane's history: commit e7e348814 carries τ* = 0.44643117 +
    2.60792242i as an eight-digit literal (its "Golden" names only the line); τ_Golden = 1/√5 + iφ² first appears in the
    next commit, 06d9d7edb. The independent lane maps the passing region at 0.19% of the band's hyperbolic area (about 9
    bits) and finds 30 of 600 "natural" closed forms inside it, one fitting better.
  - **The characters were selected:** 3rd of 2 048 combinations (about 8 bits), the "derivation" written afterwards
    (independent lane); and a₀ is a free complex parameter (FR-COV has more freedom than FR-FIB, not less).
  - **The cell's "zero-bit selection"** rests on identities that fail (the line is not an eigenvector mod 5 of either
    matrix used — main: U(2, 0) ≡ (2, 4) and ((A³ − I)/4)(2, 0) ≡ (1, 4) mod 5; "U² ≡ I mod 5" fails, U² ≡ [[0, 3], [3,
  3]]) and on rules supplied, not derived.
- **The closure claims** — m_H = 126.28 GeV (a factor-2 error in the y_t² and λ beta functions; corrected, 118.9 GeV by
  the independent lane and 118.83 GeV by the lane's own repair), the γ vector of Phase 7 (a rounded best fit, impossible at one loop in the SM), the
  Planck mass, ρ_DE, Ω_DM/Ω_b, η_B (coincidences at the rate chance predicts), the neutrino masses (a mislabelled η⁶,
  factor 5.24, and inserted factors 3, 1/3) and PMNS (read from a basis-dependent overlap): each refuted by the independent
  lane's recomputation; main did not re-run them, since the lane conceded "0 of 19" itself (e7c474a4e) and keeps only a
  "Golden texture candidate", priced by the independent lane at about 17 bits of post-hoc selection beside the cell's
  choices, against the 3.6 bits the four can spare in B1825's budget (P-555).
- **The four "Step B defects"** change nothing in B1825: 4A follows the card (the six's code is two-part, the four's
  posterior mixes every choice, as written); 4B is a real gap in the card's word "physical" (the 48 order-12 lines have a
  massless electron, B1716, yet count as physical for the null's four), whose effect on p₂ the independent lane bounds by
  1.24×, far short of what X2 would need, and which cannot touch S (those rows never enter the support) — P-557; 4C is a
  uniform duplication; 4D's underflow claim is wrong (no IEEE underflow; the import-time cost is real, about 10 s).

## 3. What this changes

- **B1788** (a dated note): hypothesis (b) fails identically on α ∈ {1/12, 1/4, 5/12}.
- **B1825** (a dated note): the miss is the corner inversion; the frame's own V at the address is printed in full.
- **For the next design (P-555):** a frame that keeps both sectors' lightest vector on one sector-blind direction cannot
  carry the CKM's corners in the measured order; a second address, or any structure that separates the two sectors' light
  directions, is what the corner inversion asks for.

## Seen first

- `VERDICT topic-sweep /hypothesis \(b\)|c_j ?\+ ?c_k|5/12|1/12 .{0,20}(slope|line)|corner inversion|V_td/ (full text): 11
  of 1571 arcs on main match (NEGATIVE 4, PROVED 7); 2 register rows match (QUEUED 2)`: B1788 is the arc corrected; no arc
  states the vanishing on 1/12 and 5/12 or the corner inversion. The closed form is the SM seat's W177 (harvest row 1496).
- **Literature (pointers, not read on the bench; no search was run):** the Gatto–Sartori–Tonin relation of
  Fritzsch-type textures, sin θ_C ≈ √(m_d/m_s), where the Cabibbo angle comes from the down sector; here the frame's up
  sector carries it, which is the inversion.

> *2026-11-03 (S288): precedence for § 1.3. The locking of each sector's lightest state to conj(h) under S and to h
> under S̃ is B1739's (main, P-344: "each sector's lightest state overlaps conj(h) under S and h under S~", with r =
> |h·h|/|h|² falling like e^(−π Im τ)). The agy lane's addition is the 1–2 angle's dependence, θ₁₂ ∝ r/(m₂/m₃) per
> sector, and the corner inversion that follows from one shared r. The arc's credit line is read with this.*

> *Dated note 2026-11-03 (S298, the web seat's review of 2026-11-03, verified on main):*
> - *Item 2's "the vanishing is exact at finite τ on these slopes" holds where 12p₂ is an integer; hypothesis (b)'s σ_b vanishes identically at finite τ on these slopes only where 12p₂ is an integer (36 of the census's 40 lines on them); on the four order-8 lines (1/4, odd/8) it is nonzero off Re τ ∈ ℤ (∓0.10 at τ = 0.13 + 1.9i, 1.9 × 10⁻⁴ at Im τ 3.9) and vanishes only at Re τ ∈ ℤ and in the cusp limit, so (b) still fails there (the web seat's kernels note of 2026-11-03, reproduced on main with B1826's own functions, S298).*
> - *§ 1.3's "a strong tendency, not a no-go" holds with equal readings and up steeper than down; over main's whole sample with equal readings the corner order is near a coin flip, |V_ub| < |V_td| at 0.486 of 1 456 points (B1827's scans/mirror_rule_structure2_out.txt).*

> *Dated note 2026-11-03 (S298, the harvest of the physical-bridge lane's row 1538):*
> - *Item 1's sector-blindness holds as stated, for the three charged sectors (twist ∓3; their norms agree to 7 × 10⁻¹² on three more lines, main, S298). It does not extend to the LL pair (twist ∓6), whose norms differ from them by order 10 (main, S298); B1799 is unaffected (B1795's split uses each sector's own twist).*
> - *§ 2's "118.9 GeV by the independent lane and 118.83 GeV by the lane's own repair" are those lanes' values, not re-run here; the physical-bridge lane reads the agy repair's λ beta function as still off against Buttazzo et al. eq. 99 and the m_H formula as lacking pole matching, so neither value is certified. The refutation of 126.28 GeV stands.*

> *Dated note 2026-11-04 (Review 74, P-086's check of S298's 'verified on main'):* the two S298 checks had no committed instrument; they are now `verification/review74/sigma_b_order8.py` and `ll_pair_norms.py` with their outputs (main's runs, identical to the review reader's). σ_b on (1/4, odd/8) is ∓0.102 at 0.13 + 1.9i, ∓1.9 × 10⁻⁴ at 0.13 + 3.9i and ≤ 2 × 10⁻¹¹ at Re τ ∈ {0, 1}, in all three sectors, as S298 stated. **Corrected:** S298's "the LL pair at twist ∓6 differs by order 10" is not the shape. On three of the four lines checked, the LL pair's channel norms differ from the charged sectors' by 14 to 30. On (1/3, 1/6) at 0.2 + 2.3i they are the charged norms with the channels permuted (1 ↔ i, j ↔ k), within 0.03. The charged sectors agree to 1.3–4.5 × 10⁻¹² on all four. The title's, the claim line's and item 2's "the vanishing is exact at finite τ on these slopes" holds where 12p₂ is an integer (this page's S298 note).*
