# THE PLAN AFTER THE READING TEST (chat1, 2026-10-24): what we may be missing, and what to do about it

chat1 (the web seat), at the owner's word ("agrees. should we put all these into a plan"), after a pause to ask what we
have learned, what we could be getting wrong and which angle we are missing. **A plan, not a result**: §0 cites sealed and
computed results; everything else is a proposal. 0 of 19.

## 0. Where we stand

- **THE READING TEST (sealed; `READING_TEST_RESULT.md`):** with the Higgs direction free and main's Standard Model
  reading (up S̃ = S(h̄), down and leptons S(h), c = 3), the declared search found no row below χ²_nine 1 045 on 4 256 fresh
  rows over all 266 lines (power control 34 of 36, at its threshold). Exact statements: Lemma A (Y h = Yᵀh = (h·h) u),
  Lemma A′ (‖u‖ ≤ √3 m₃), Lemma B (|V_tb| ≤ cos(α_u3 − α_d3)).
- **New today, data-free (`exploration/e9_quaternion_higgs.py`, committed before its run):** restoring the Higgs's scalar
  part h₀ (zero in every census since B1700) does not lift the obstruction. With B1736's general coupling,
  **det Y = N(S) N(M) ⟨S, M⟩** (N the quaternion norm h₀² + h·h of the Higgs, w² + u·u of the channel; symbolic). At a null
  Higgs quaternion, N(S) = 0, every sector's light left state is the conjugate of the null eigenvector x of [h]_× with
  eigenvalue h₀ — the same for every channel (Yᵀx = 0 to 10⁻¹⁵; in general Yᵀx = (λ − h₀)(u × x − w x)) — and the
  Standard Model's reading maps it to its conjugate, so |V_ud| = 0 for every h₀ (largest 7 × 10⁻¹³ on 384 stored rows of
  the reading test's grid). The obstruction belongs to the quaternionic coupling itself; Lemma A's null case is h₀ = 0.
- **Running:** THE HOLOMORPHIC READING TEST (A1: one direction read S in every sector), sealed at 110af4a13; the store is
  being built; then C2, the scan (about 3.5 hours, one resume) and the calibration (lepton-tied random targets included).

## 1. Seven places we may be wrong

1. **Family SU(2) or electroweak SU(2)?** Main identifies the frame's conjugation S̃ = εS̄εᵀ with H̃ = iσ₂H*. In B1736 the
   quaternion units of S carry the family group (the Higgs transforms as ρ′, the cube's rotations, ≅ S₄ at level 4; corrected 2026-10-24 from "inside 2I", see
   `LITERATURE_DIVE.md`), so εS̄εᵀ is a
   conjugation in the family SU(2). If the electroweak doublet index is not what S̃ acts on, "the up quarks see h̄" is not
   what one Higgs doublet does: one doublet with one family direction gives the same h in every sector — A1. Then the
   reading test's two-doublet pointer is wrong, and an A1 pass would mean the Standard Model's single doublet works. A
   hypothesis (P-295 records another alternative); it decides how A1's result is worded.
2. **A known class of models, unread.** Yukawas built from Jacobi theta functions with characteristics, shifted by
   background data, are what magnetized-torus compactifications give (Cremades, Ibáñez, Marchesano 2004; Kobayashi et al.
   on metaplectic flavour symmetries); hierarchies from τ near a residual-symmetry point, suppressed by powers of a small ε,
   are the modular-flavour mechanism (Novichkov, Penedo, Petcov 2021), and the frame's r = e^{−π Im τ} near the cusp is
   that mechanism. That literature finds viable hierarchies only for restricted representation choices, typically with
   different weights per field and several couplings, and the quark sector is its hard case. We may be rediscovering its
   obstructions and missing its escape routes.
3. **The comparison scale.** The frame carries unification-scale fingerprints: on the 16 lines of order 1, 2 and 5 the
   leptons copy the down quarks (m_τ = m_b at the frame's scale, b–τ unification); c = 3 is the Georgi–Jarlskog factor;
   equal holomorphic readings are what supersymmetry's holomorphy asks. We compare at M_Z with a 10% floor. V_cb, V_ub and
   m_c/m_t run noticeably between M_Z and the unification scale while V_us barely does (values to be taken from the
   literature before use). Far-off negatives (1 045) are safe; anything within about 30% of the data is not.
4. **Observables left out.** The nine are 9 of the 19. The CP phase (J) is one of them, and the frame has a known CP
   tension (J vanishes at self-conjugate configurations; TWO_HIGGS's H8; THE_FRAMING_CHECK §3). The inter-sector ratios
   m_b/m_τ and m_b/m_t are predictions the frame makes and we never test.
5. **τ without dynamics.** τ is placed by fit or by a geometric rule (B1720's apexes). In the model class of 2, τ is a field
   whose potential decides where it sits; B1704 found the frame's one-loop potential runs τ to the cusp unless tuned. The
   principle that fixes τ may be a stabilisation mechanism, not a geometric choice.
6. **The frame's hand-made parts.** The horocycle moves V_cb by a factor 2.7 (L_max over L₂), and V_cb is the entry we fail
   most; the L table, the constants c_s and the base section were chosen upstream and every test takes them as given. (The
   scalar part h₀ = 0 was checked today: harmless for the obstruction.)
7. **The bar for fitted structures.** PRECISION_BAR's 21.67 is the 99% line for nine numbers with nothing fitted; a
   structure that fits four numbers per row has five left, whose 99% line is 15.09. The calibration against random targets
   is the honest arbiter; any reading of a fitted structure must say so.

## 2. The plan

**Track A — now, while A1 runs (cheap):**
- **A-1. The identification question** (blind spot 1): a short data-free note on what εS̄εᵀ does in B1736's family
  representation, and the alternative reading "A1 = one doublet with one family direction"; to main and the SM seat
  before A1's cells are read. (chat1 drafts; main decides; about an hour.)
- **A-2. Bank e9** — done (`exploration/e9_quaternion_higgs.py`, output committed).
- **A-3. The literature dive** (blind spots 2 and 5): map the frame onto magnetized-torus and modular-flavour
  constructions (characteristics ↔ the lines (α, b), background shifts ↔ ?, Higgs zero modes ↔ h ∈ CP²); collect known
  results on quark mixing, on what fixes the Higgs combination, and on modulus stabilisation; a note with citations and a
  list of testable imports. (A research side task, 2–3 hours.)
- **A-4. Targets at the unification scale** (blind spot 3): pin published running values (Antusch and Maurer 2013, or a
  later update) for the Standard Model and the MSSM at tan β 10, 30, 50 in a data file with hashes, beside the
  scale-stable combinations (D). (1–2 hours.)

**Track B — when A1's cells are read:**
- **B-1.** Word A1's result under A-1's answer (one doublet or two).
- **B-2. Read the Higgs off the fits** (post hoc, labelled): A1's rows store the fitted h at ten τ on every line; test
  whether h(τ) is smooth along each line and transforms under B1724's laws like a modular form, and fit its weight and
  level against the record's forms, the covariant pencil and level-4 forms; a candidate rule for h.
- **B-3. Read-outs on A1's rows:** J at each optimum; m_b/m_τ and m_b/m_t where defined.

**Track C — the next sealed tests** (each with its own rule, a fresh grid, a calibration with lepton-tied targets,
THE_BAR's look correction, and a read-only referee before the seal):
- **C-1. If A1 passes:** THE HIGGS RULE — h from B-2's rule, nothing continuous fitted but τ; J and m_b/m_τ as cells.
- **C-2. If A1 fails or lands near the bar:** A1 against A-4's unification-scale targets, the same design; and A1 with τ at
  B1720's apexes (τ by rule).
- **C-3. In every future rule:** J and m_b/m_τ as cells; the fitted-structure line (15.09 for four fitted numbers) beside
  21.67.

**Track D — theory, longer:**
- **D-1. τ's dynamics:** a modular-invariant potential for τ (from A-3 and B1704): does a natural one have its minimum in
  Im τ 2–3.4?
- **D-2. The hand-made parts:** each with its origin arc and whether any test has checked it; a horocycle rule as a
  candidate selection principle (V_cb belongs to the channels at Im τ ≳ 3, and the horocycle scales it by 2.7).

## 3. Asks

- **To main (cc):** the identification question (A-1) — is the SU(2) in which S̃ = εS̄εᵀ is a conjugation the family
  group's or SU(2)_L? Verify e9 (a dated note on B1739 or B1736). The origins of the horocycle table and the constants c_s
  (D-2).
- **To the SM seat:** the identification question from the E₆ side; a third opinion on Lemmas A, A′, B and e9.

## 4. What would count (unchanged)

A sealed row below both bars on fresh rows, specific against random targets including lepton-tied ones, under THE_BAR's
look correction, is a value-level match for the structure tested — with whatever it fits named. A number of the 19 needs h
and τ from rules, nothing continuous fitted.

0 of 19.
