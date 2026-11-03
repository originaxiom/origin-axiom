# B1827 — THE FRAMING LEDGER: WHAT THE PROGRAMME EXCLUDES BY THE WAY IT IS FRAMED (the owner's exercise, 2026-11-03): EIGHTEEN COMMITMENTS INVENTORIED AND RANKED; THE CKM's CORNER INVERSION IS A CONSTRUCTION CHOICE, LIFTED BY A SECTOR-ODD SINGLET HIGGS; ON ORDER-5 LINES THE FRAME IS MINIMAL SU(5)

**Verdict: OPEN** — an audit of the programme's framing, with four data-free facts computed (§ 2) and a ranked list of
tests (docs/FRAMING_LEDGER.md § E). It claims no parameter. **0 of 19.**
- **The question** (the owner, 2026-11-03): "what are we excluding by the way we frame the program? … log everything so
  we clarify this once for all".
- **The ledger:** docs/FRAMING_LEDGER.md — eighteen commitments (FL-01–FL-18) in three layers (the foundations and their
  reading as physics; the frame's construction; the tests), each with its status, what it excludes, the evidence it costs
  the programme, and the readers' entries behind it.
- **The raw inventory, kept whole** (verification/readers/): A1 the foundations and the bar (60 entries), A2 the frame's
  construction with its code (39), A3 the tests' conventions (40), A4 the walls mapped to their causes and the hatches
  never tried (15 clusters, 14 groups), A5 a blind outside reading (12 commitments, a ranked eight, an assessment); the
  charter. Main checked a sample of every reader's citations (all held) and merged them.
- cc (main), 2026-11-03.

## 1. What the exercise found (the ledger, in brief)

- **One construction choice carries the CKM wall (FL-06).** The Higgs's internal orientation is built from the adjoint
  units i, j, k only — no singlet channel —, untwisted, shared by the sectors: it locks both quark sectors' light states
  (B1739) and inverts the CKM's corners (B1826). The choice is UNSTATED: it lives in the code (C-04, C-05).
- **About nine of the 19 have no frame at all (FL-05):** no action, normalisation, gauge kinetic function or scale exists
  on record; the gauge couplings, the Higgs sector and the scale are absent, not blocked.
- **The flat premise carries most value-walls (FL-02):** 107 of the record's 173 value-kills sit on flat premises (GENESIS
  l. 370); curvature, flux and one-leg hypercharge insertions were never tried.
- **The tests cap what can be recognised (FL-13–FL-15):** tree-level outputs at M_Z with no running (UNSTATED) and a flat
  10% allowance; the six can never compress; only the ten flavour numbers are graded; values are graded, relations never.

## 2. Computed (data-free, exploration tier; scripts and outputs in verification/scans/)

Two coarse facts of the measured world are used and disclosed: the hierarchy (m₂/m₃ < 0.1, m₁/m₃ < 0.01 in both quark
sectors) and that the up hierarchy is steeper than the down. No measured value is compared.
1. **The mirror rule cannot lift the corner inversion** (P-555): it keeps the six and r = ∣h·h∣/∣h∣² exactly; where up is
   steeper, nature's corner order with ∣V_ud∣ > 0.9 holds at 1.7% of the frame's points and 0 of 303 under the rule.
2. **A singlet Higgs component at natural magnitude, the same sign in up and down, does nothing** (0.7–4.0% at every one of
   ten phases; the frame alone 2.1%; median ∣V_ub∣/∣V_td∣ 20–29).
3. **The same singlet with opposite signs in up and down lifts the inversion generically: 33–47% at every phase, median
   ∣V_ub∣/∣V_td∣ 0.91–1.0.** **Robust (singlet_robustness.py, fresh seeds 1200–1439, four phases):** at ∣a₀∣² = 0.25, 1 and 4 × ∣h·h∣ the rate is 29–38%, 34–48% and 33–42% (the frame alone 2.2%, median 21), the median ∣V_ub∣/∣V_td∣ 1.03–1.11, 0.91–1.02 and 0.83–0.93: the effect holds over a factor 16 in the singlet's size, and a larger singlet moves the corner ratio further towards nature's side. The corner ratio becomes balanced, not the measured 0.43.
4. **On order-5 lines the frame is minimal SU(5) exactly** *(S291: verified on all 24 order-5 lines, with Y_e = λY_dᵀ, λ⁵ = 1, in general — see the note below)*: on (2/5, 0) and (1/5, 3/5), R₁(up) = 0, Y_u symmetric and the
   down and lepton spectra identical (on (2/5, 0) Y_e = Y_dᵀ to 2 × 10⁻¹⁵) — so the down–lepton degeneracy is SU(5)'s, and
   c = 3 is the Georgi–Jarlskog Clebsch put in by hand (the blind reader's claim, verified); the order-10 lines that won the
   six's fits break the relations slightly; an order-7 control has none.

**Correction disclosed (P-562):** main first expected opposite signs from a Higgs twisted like the matter; B1744 had shown
the frame's twisted residue quaternion is even (H_u = H_d). Fact 3 stands as a class result; what in the object makes the
singlet odd between the sectors is the first open test (P-566).

## Seen first

- The sweeps behind the exercise: P-555's (`VERDICT topic-sweep /two addresses|two loci|different addresses|masses and
  (the )?mixing|…/ (full text): 7 of 1571 arcs`, S286), P-562's correction found B1744 (THE HIGGS'S OWN TWIST) through
  reader A4's sweep of the kill graph's hatches; each reader swept its scope (A4 with topic_sweep.py --full per hatch).
- **Literature (pointers, not read on the bench; no search was run):** minimal SU(5) Yukawas (Y_u symmetric, Y_e = Y_dᵀ)
  and the Georgi–Jarlskog 45; Froggatt–Nielsen generation charges; modular flavour symmetry with several moduli; F-theory
  Yukawa points on matter curves — the comparisons the blind reader drew (verification/readers/A5_blind_pass.md).

## Disclosed

- Seen before the scans: B1825's run and B1826's corner inversion (both post-run read-outs); the two coarse facts above.

> *2026-11-03, later (S290; exploration tier, data-free; scans in verification/scans/): **which relation between the sectors
> lifts the corners.** (a) The Standard Model's reading (up reads S̃ = εS*εᵀ, down reads S) with a singlet at natural magnitude
> does not: it over-flips the corners (∣V_ub∣ < ∣V_td∣ at 70–76%, median ratio about 0.1) but scrambles the light generation
> (∣V_ud∣ > 0.9 at 14–20%; both at 0.2–3%), since S̃ conjugates the triplet too (B1739); sm_reading_singlet_scan.py. (b) The
> relation the scans reward — the singlet flipped, the triplet kept — is the ADJUGATE, adj(S) = εSᵀεᵀ = det(S)·S⁻¹, the
> quaternion conjugate a₀ − h·Q (verified exactly): a holomorphic reading with no complex conjugation. On the frame's 3D Higgs
> adj(S) = −S, so this reading was invisible by construction; it becomes distinct only once the Higgs has a singlet, and then it
> is exactly the opposite-sign family (33–48%). B1724 and B1790 considered only S, S* and S̃. (c) *[RETRACTED by S291, the note below: the probe's labels were wrong]* The 45-like Clebsch: on the
> order-5 lines, a singlet entering the leptons with SU(5)'s −3 relative to down splits the second generation's lepton/down
> ratio to about 2–4.5 at Im τ 1.9–2.6 (a 5-like control stays near 1) — about the Georgi–Jarlskog factor without c — but not the
> first generation (scattered); for the up quarks there the singlet's contribution is antisymmetric, the 45's 10·10 form;
> gj45_probe.py. One structure — a 4D Higgs whose singlet enters as the 45, read by its adjugate in one sector — is the candidate
> P-566 now names; its price (the singlet's size, its phase, the reading, the address) is not yet computed, and nothing here
> is compared with a measured value.*

> *2026-11-03, night (S291; the owner: "make sure sure sure all your claims and conclusions are right", then: "check whether
> we're missing valuable insight, whether we're making the proper existential question and could identify the answer if we
> ever get to it"). **THE RECHECK** (verification/recheck/, RECHECK.md; data-free).*
> - **Hold, exactly:** adj(S) = εSᵀεᵀ = det(S)·S⁻¹ = a₀ − h·Q, S̃ = a₀* + h*·Q, det S = a₀² + h·h; the frame's coupling is
>   linear in S and obeys Y(S, M) = −Y(adj S, Mᵀ)ᵀ, so the adjugate reading IS the opposite-sign family (500 random cases,
>   7 × 10⁻¹⁵); every scan number in § 2 and in S290's note matches its output file; c = 3 is the Georgi–Jarlskog factor in
>   the code (stepb_core.c_shift: × c on μ/τ, ÷ c on e/τ).
> - **Order 5, all 24 lines** (1 152 cases: three τ, both radii, four directions, both readings): R₁(up) = 0, M_u and Y_u
>   symmetric, the singlet's part of Y_u antisymmetric (the 45's 10·10 form), the down and lepton spectra equal — but
>   **Y_e = Y_dᵀ holds only on the 8 lines with a = 0 or b = 0; in general M_e = λM_dᵀ with λ a fifth root of unity, and
>   then, exactly (9 × 10⁻¹⁵), Y_e(S) = −λ Y_d(adj S)ᵀ: the leptons read the down sector through the adjugate.** The
>   reading that lifts the CKM's corners is, on these lines, the frame's own down–lepton relation (P-583).
> - **Disclosure owed:** two of the twelve phases (c = ±i) had no points: there a₀² = −h·h, the Higgs is null (det S = 0)
>   and every lightest state is massless (B1659's J4), so the hierarchy filter drops them — "every phase" means the ten
>   non-null ones. The SM reading's over-flip and scrambled ∣V_ud∣ are the reading's own (identical at c = 0: 73%, 14%,
>   1.2%), not the singlet's.
> - **RETRACTED — S290 (c), the 45-like split.** By the identity, the singlet's Clebsch relative to the triplet's SU(5)
>   relation is κ = −k (k the lepton's coefficient in the code): gj45_probe.py's "k = −3, the 45" was κ = +3, and its
>   "5-like control" k = +1 was κ = −1 (a true 5, k = −1, gives exactly 1 — verified). Rerun with the correct labels
>   (gj45_corrected.py; 24 lines, three τ, both radii, three directions, both readings, three phases): with the 45's κ = −3
>   the second generation's (μ/τ)/(s/b) has median 2.0 (quartiles 1.3–3.3) but the first's (e/τ)/(d/b) median 3.3
>   (1.5–6.0), where Georgi–Jarlskog needs about 3 and 1/3; the pattern at 1.1% (κ = +3: 0.5%). **The 45 half of P-566's
>   candidate is dead** on the coarse Georgi–Jarlskog fact (disclosed); the adjugate half stands as computed.
> - **Sharpened:** "about nine of the 19 have no frame" — nine lie outside the ten graded numbers; six have no frame
>   (g₁, g₂, g₃, m_H, v, y_t); three are frame outputs never examined (θ̄, P-569; y_b/y_t and y_τ/y_t, P-568).
>
> ***THE RECOGNITION AUDIT*** *(docs/FRAMING_LEDGER.md § G; verification/recognition/; verification/readers/A6_*).*
> - **R1 (main; a control of the test — no frame output enters):** the test's own measured inputs, run up with the
>   Standard Model's one-loop RGEs, move the ten from M_Z to 2 × 10¹⁶ GeV by −11.6% (c/t, u/t), +13.1% (s/b, d/b, ∣V_cb∣,
>   ∣V_ub∣), +28% (∣J∣) and 0 (the leptons, ∣V_us∣). The run reproduces the test's own source at 10¹² GeV (HZ2021's a and b,
>   P-363: 2.838 against 2.84, 0.268 against 0.269) and a two-loop table's shifts at 1–10 TeV to within 15% of the shift
>   (arXiv:1306.6879, Table 1, read through a fetch). **A theory exactly right at the unification scale scores
>   χ²_ten = 11.8 against nature at M_Z: it passes S (23.21) but pays 8.5 bits on K** (χ²/2 · log₂ e), more than the
>   3.6 bits of room B1825's address leaves (P-555); the four alone cost 5.9 bits. With σ-sized residuals as well, S would
>   reject it 39% of the time.
> - **A6, a blind reader** (it saw neither this arc nor the ledger), **verified by main citation by citation**
>   (A6_VERIFIED.md): the headline "0 of 19" counts Tier 4, which WHAT_WOULD_COUNT made "not a live criterion" (l. 381); the
>   owner's restated goal (2026-10-08: the structure and how many free numbers) has its answer on record, "all 19 are free";
>   the owner's total-inputs scoreboard (P-418, 2026-10-29: "'0 of 19' alone hid the drift") is unbuilt; every positive is
>   a READING while the dictionary is UNEARNED, and it is UNEARNABLE within F-HE and F-CI (GENESIS l. 424), so the board
>   cannot move under any outcome of any current test; B1825's PASS was unreachable before its seal (its own words) and its
>   K's power for a correct frame a σ away is 1 in 10 (its calibration); the allowance discards 29.7 bits of measured
>   information (main's recount); the frame's own length is not charged; one joint look ledger meets an exact hit's median
>   C_ten at m ≈ 108 (now 53); structural grades use two comparison classes (ℤ₆ DERIVED against the SM, sin²θ_W REPRODUCED
>   against the GUT class). Sharpened by main: B1786's m·r was already 0.0099–0.0112 at m = 41.
> - Main's reading of the question, the triggers that would reshape the foundations, and what is the owner's: the ledger's
>   § G. P-566 updated; P-572 sharpened; P-574–P-583. Nothing here is compared with a frame output. **0 of 19.**

> *2026-11-03, latest (S294; SEEN FIRST, owed and paid late).* Three statements of this arc were on record before it and
> were presented here without their sources: **(1)** "on order-5 lines the frame is minimal SU(5) — Y_u symmetric, Y_e =
> Y_dᵀ" is **B1728's** derived law (PROVED, 2026-10-23: a charge shift by the line's order is one phase, the left–right swap
> transposes, so d = e on order 5 with Y_e = Y_dᵀ) with B1698 and B1703's census (docs/LAW_MAP.md, "WHICH LINES SPLIT THE
> CHARGED SECTORS"); **(2)** "c = 3 is the Georgi–Jarlskog Clebsch by hand" is **B1742's** P-355 ("with c = 3 a fit there is
> Georgi–Jarlskog's by construction and D = 9"); **(3)** S291's M_e = λM_dᵀ, λ⁵ = 1, is B1728's phase law, which S292's
> law-map row wrongly called unproved (corrected). What is new here is narrower: the singlet's sign under the swap,
> Y(y, x; S) = −Y(x, y; adj S)ᵀ — B1728 stated the span(i, j, k) case and noted that its control S = 1 "breaks it"; the adjugate
> is the law that joins the two — and everything S289–S291 computed about the CKM's corners and the 45. The miss: the
> claims were checked against the code but the record was not swept for them first (`topic_sweep.py "Y_e = Y_d"` finds
> B1728 and B1742).*
