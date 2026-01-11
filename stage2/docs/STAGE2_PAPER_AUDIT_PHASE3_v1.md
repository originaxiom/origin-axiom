# Stage 2 paper audit — Phase 3 (mechanism module)

Status (2026-01-11): This note records a Stage 2–era audit of the Phase 3 paper `artifacts/origin-axiom-phase3.pdf` against the Phase 3 contracts and the current Stage 2 mechanism and joint verdicts. It is descriptive only and does not propose edits to the LaTeX sources.

## 1. Inputs and sections inspected

Paper:

- `artifacts/origin-axiom-phase3.pdf`

Phase 3 docs and alignment:

- `phase3/MECHANISM_CONTRACT.md`
- `phase3/SCOPE.md`, `phase3/ROLE_IN_PROGRAM.md`, `phase3/REPRODUCIBILITY.md`
- `phase3/PHASE3_ALIGNMENT_v1.md`
- global docs: `docs/PHASES.md`, `docs/CLAIMS_INDEX.md`, `docs/FUTURE_WORK_AND_ROADMAP.md`
- archived flavor experiment docs under `experiments/phase3_flavor_v1/`

Stage 2 context:

- `stage2/mech_measure_analysis/docs/STAGE2_MECH_VERDICT_v1.md`
- `stage2/mech_measure_analysis/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md`
- `stage2/joint_mech_frw_analysis/docs/STAGE2_JOINT_VERDICT_v1.md`
- `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`
- `stage2/theta_star_analysis/docs/STAGE2_THETA_STAR_ALIGNMENT_v1.md`

Paper sections explicitly inspected:

- Title page + abstract
- Sec. 1 Introduction
- Mechanism definition and construction (ensemble, amplitude, floor)
- Claim and non-claim section at the mechanism level
- Diagnostics and instability penalty section
- Discussion and limitations
- Conclusion

The aim is to check narrative alignment, claims alignment, and scope/status language against the current Phase 3 contracts and Stage 2 verdicts.

## 2. Summary of the Phase 3 paper’s own story

The Phase 3 paper presents Phase 3 as a mechanism-only rung whose job is to implement and test a concrete toy mechanism for a non-cancelling floor on a global amplitude observable. The construction is:

- A finite ensemble of complex modes \(z_k(\theta) = \exp(i(\alpha_k + \sigma_k \theta))\) with fixed offsets and a small set of integer windings.
- A baseline global amplitude \(A_0(\theta)\) defined as an average over the modes.
- A floor-enforced amplitude \(A(\theta) = \max(A_0(\theta), \varepsilon)\) for a positive floor scale \(\varepsilon\).
- A set of diagnostics that compare the unconstrained and floor-enforced amplitudes as functions of \(\theta\).

Within this setup the paper emphasises three goals:

1. Define a clean and reproducible toy vacuum mechanism that exposes both the unconstrained diagnostic \(A_0(\theta)\) and the floor-enforced diagnostic \(A(\theta)\).
2. Demonstrate a genuine binding regime where the floor is active on a non-zero fraction of the \(\theta\)-grid while leaving regions where the unconstrained behaviour is still visible.
3. Quantify the global impact of the floor via simple diagnostics such as mean shifts, distances between \(A_0\) and \(A\), and binding fractions.

The text explicitly states that this mechanism-focused Phase 3 replaces the earlier flavor calibration experiment as the canonical definition of Phase 3, with the flavor work preserved in `experiments/phase3_flavor_v1/` as an archived negative result.

At the mechanism level the paper claims that:

- There exists a deterministic toy vacuum ensemble and global amplitude \(A_0(\theta)\) for which a strictly positive floor \(\varepsilon\) can be enforced in a numerically stable way.
- For the baseline configuration one can choose \(\varepsilon\) such that the system enters a binding regime with a demonstrable global shift in the amplitude distribution between the unconstrained and floor-enforced cases.

The paper explicitly states that Phase 3 does not claim that the toy vacuum is physical, that \(\theta\) is a physical phase, that any particular value of \(\theta\) (including \(\theta_\star\)) has been selected by Nature, or that the mechanism explains observed vacuum energy. No corridor narrowing or parameter reduction is attempted; the goal is to build and stress-test a transparent mechanism rung.

## 3. Alignment with Phase 3 contracts and global program docs

Comparing the paper with `phase3/MECHANISM_CONTRACT.md`, `phase3/SCOPE.md`, `phase3/ROLE_IN_PROGRAM.md`, `phase3/PHASE3_ALIGNMENT_v1.md`, and global docs:

- Role and identity:
  - The paper consistently describes Phase 3 as a mechanism module whose job is to implement and probe a non-cancellation floor on a global diagnostic, not as a flavor-calibration rung and not as a measure or data phase.
  - This matches the Phase 3 alignment memo and `docs/PHASES.md`, which define Phase 3 as a mechanism module sitting between Phase 2 and the FRW-facing work of later phases.

- Claims structure:
  - The paper’s mechanism-level claims (existence of a stable floor-enforced ensemble and existence of a binding regime with global impact on the amplitude distribution) agree with the Phase 3 mechanism contract and the way Phase 3 is indexed in `docs/CLAIMS_INDEX.md`.
  - There is no claim in the paper that a canonical measure over \(\theta\) has been derived, nor that \(\theta_\star\) is selected; these are explicitly listed as non-claims.

- Flavor archive status:
  - The paper’s brief discussion of the retired flavor experiment matches the repository structure and archive banner in `experiments/phase3_flavor_v1/`, and it correctly treats that work as a preserved negative result, not part of canonical Phase 3.

- Reproducibility:
  - The description of scripts, configuration, and outputs in the paper is consistent with `phase3/REPRODUCIBILITY.md` and the Phase 3 alignment memo: the ensemble, diagnostics, and instability penalty are built from clearly specified code paths and tables under `phase3/outputs/tables/`.

Net: the Phase 3 paper is well aligned with the Phase 3 contracts and global docs as locked in the current Stage 2 snapshot.

## 4. Alignment with Stage 2 mechanism and joint verdicts

Stage 2 mechanism and joint verdicts emphasise that:

- Phase 3 produces a family of smooth, bounded diagnostics over \(\theta\) that can be treated as measure-like or flag-like internal diagnostics.
- No single column is promoted to a canonical measure over \(\theta\).
- On the joint grid with Phase 4 FRW scalars the mechanism diagnostics are highly redundant with FRW vacuum-sector quantities and mostly act as reparameterisations.
- θ★ lies inside the FRW-viable band but is not singled out by any of the current diagnostics.

The Phase 3 paper is consistent with these conclusions:

- It presents the diagnostics as internal, toy-model quantities used to quantify the impact of the floor on the ensemble; it does not elevate any of them to a fundamental measure.
- It does not attempt to interpret the diagnostics as independent axes of structure beyond their role in the mechanism testbed.
- It does not claim that the mechanism by itself selects θ★ or yields a distinguished \(\theta\) in any operational sense.

The instability penalty scalar introduced in the paper is explicitly described as a toy measure of how much probability mass lies near small amplitudes in the ensemble, without any corridor or selection role; Stage 2 later uses related information in a diagnostic way and likewise does not treat it as a canonical measure. There is no tension between the paper’s description and the Stage 2 mechanism and joint verdicts.

## 5. Scope and limitation language audit

The discussion and limitations sections in the paper clearly state that:

- The vacuum ensemble is highly idealised, with no spatial structure, local dynamics, or link to a Hamiltonian or Lagrangian.
- The global amplitude is an aggregate diagnostic, not a physical observable, and none of the reported numerical values are to be interpreted as physical scales.
- The mechanism is not claimed to be realistic vacuum physics, and any physical reading would require substantial upgrades (local formulation, richer field content, better connection to FRW and data).

This matches the Stage 2 master verdict’s stance that Phase 3 is a disciplined mechanism rung, not a final physical model, and that later phases and belts are responsible for any data-level or measure-level interpretation.

References to θ and θ★ in the paper are framed as internal control parameters for the ensemble, not as physically selected values. The paper does not suggest that the current mechanism or diagnostics pick out a special \(\theta\); this is aligned with the Stage 2 θ★ verdict.

## 6. Potential future tightening (for a later editing rung)

This audit does not propose changes to the LaTeX sources, but for a future editing rung it may be helpful to:

- Add a brief cross-reference from the Phase 3 conclusion to the Stage 2 mechanism and joint belts, noting that later analyses have quantified how the Phase 3 diagnostics correlate with FRW scalars and remain redundant at the present toy level.
- Optionally add a single sentence clarifying that any attempt to promote a Phase 3 diagnostic to a canonical θ-measure is explicitly deferred and would require new rungs and gates.

These would be minor clarifications; the current text is already cautious and does not misrepresent the Stage 2 picture.

## 7. Verdict

For the Stage 2 snapshot:

- The Phase 3 paper accurately presents Phase 3 as a mechanism-only phase implementing a non-cancellation floor in a controlled toy ensemble, with clearly stated internal goals and limitations.
- The mechanism-level claims in the paper agree with the Phase 3 mechanism contract and global program docs, and they do not assert a canonical θ-measure, θ★ selection, or real-data match.
- The way diagnostics and the instability penalty are framed is fully compatible with the Stage 2 mechanism and joint verdicts, which treat these quantities as internal diagnostics that are redundant with FRW scalars and not yet physically privileged.
- No contradictions were found between the Phase 3 paper and the current Stage 2 verdicts; any future edits can be limited to minor clarifications and cross-links rather than substantive claim changes.
