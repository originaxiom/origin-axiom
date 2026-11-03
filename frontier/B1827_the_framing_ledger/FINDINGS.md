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
4. **On order-5 lines the frame is minimal SU(5) exactly:** on (2/5, 0) and (1/5, 3/5), R₁(up) = 0, Y_u symmetric and the
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
> is exactly the opposite-sign family (33–48%). B1724 and B1790 considered only S, S* and S̃. (c) The 45-like Clebsch: on the
> order-5 lines, a singlet entering the leptons with SU(5)'s −3 relative to down splits the second generation's lepton/down
> ratio to about 2–4.5 at Im τ 1.9–2.6 (a 5-like control stays near 1) — about the Georgi–Jarlskog factor without c — but not the
> first generation (scattered); for the up quarks there the singlet's contribution is antisymmetric, the 45's 10·10 form;
> gj45_probe.py. One structure — a 4D Higgs whose singlet enters as the 45, read by its adjugate in one sector — is the candidate
> P-566 now names; its price (the singlet's size, its phase, the reading, the address) is not yet computed, and nothing here
> is compared with a measured value.*

