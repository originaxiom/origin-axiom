# W0d reading log (seat cc3, 2026-07-17)

All paths under `[machine-path]` (read-only) unless
noted. Sealed prereg read first as instructed.

## Prereg / campaign scaffolding
- `[machine-path]` (sealed prereg, read first)

## B662 successor campaign (the source of the Massey wall + the γ5′ identification)
- `frontier/B662_successor_campaign/CAMPAIGN_PREREGISTRATION.md`
- `frontier/B662_successor_campaign/CAMPAIGN_SYNTHESIS.md`
- `frontier/B662_successor_campaign/WAVE3_FINDINGS.md`
- `frontier/B662_successor_campaign/cellH/FINDINGS_CELL.md` (the Massey wall; H¹(D;27)=5, cup classes fill H², scalar Massey undefined/full-indeterminacy)
- `frontier/B662_successor_campaign/cellI/FINDINGS_CELL.md` (the ear = Γ5′-doublet 2̂′, exact character equality on all 9 classes of SL(2,5); weight-5 forced; H129, L108)

## Terminology / architecture
- `TERMINOLOGY.md` ("the stage" = SU(3)₂ κ=5; "the weld/the double"; "hearing/deaf"; the (i₁,i₂) reduction, the portal law, the invariant line)
- `docs/LAW_MAP.md` (the walls list: cubic dichotomy/Massey wall as 4th wall; the total mirror wall; the equivariance wall (row 9); the dimensionful no-go (row 10))
- `docs/OPEN_LEADS.md` (grepped for L106, L107, L108 — the cup-class-values lead, the cross-landscape lead, the γ5′ functor's last leg)

## The stage: SU(3)_2 modular data
- `frontier/B238_su32_levelrank/su32_wrt.py` (read in full — Kac–Peterson S,T construction, modular_gate, wrt_trace; R=T, L=S⁻¹T⁻¹S convention)
- `tests/test_b238_su32_levelrank.py` (the test lock: modular gates, figure-eight coincidence at -1/phi, level-rank non-equality in general, kappa=5 shared conductor)

## The hearing group / weld operator / equivariance wall
- `frontier/B640_hearing_group/FINDINGS.md` (2I×ℤ/3, the golden character, tr rho(RL) = -1/phi, ord(W(RL))=20 on the full 6-dim stage, the McKay placement)
- `frontier/B644_mckay_comparison/FINDINGS.md` (the congruence-shadow theorem: rho_hear factors through mod-5 reduction; the M3 adjudication)
- `frontier/B650_typed_functor/FINDINGS.md` (THE EQUIVARIANCE WALL, W2-G1: no nonzero linear monodromy-equivariant map classical -> stage; the group-functorial resolution W2-G2)
- `frontier/B666_leads_campaign/cellS/PROOF_NOTE.md` (the scale-torsor no-go theorem; Hom(G,R+)=0 for finite/profinite G, verified exactly on 2I, 2I x Z/3, SL(2,Z/15), W(E6) etc. — read for adjacent "rigidity-flavored" reasoning, NOT Ocneanu rigidity itself, noted as a distinct theorem in SCOUT.md)
- `frontier/B492_verlinde_boundary_lens/FINDINGS.md` (Verlinde/Affleck-Ludwig lens on the Fibonacci category, not SU(3)_2 — read to check for tube-algebra/Verlinde precedent; found none directly reusable)
- `frontier/B663_bifocal_anatomy/BIFOCAL_STRUCTURE_HANDOFF.md` (the bifocal split: being-end Q(sqrt-3)/2T/E6 vs hearing-end Q(sqrt5)/2I/E8 — background)
- `frontier/B664_metallic_landscape/METALLIC_LANDSCAPE_HANDOFF.md` (grepped/read around "the weld operator W(n) = R^{n-2}L on the SU(3)_2 space" — confirms the R,L,W convention used in quantum_probe.py)
- `frontier/B660_structure_campaign/origin_docs/DARK_SECTOR_CAMPAIGN.md` (grepped/read around "the weld operator W = T.S acts on the 27-dimensional space" — a DIFFERENT stage context (E6-level-2/27, not SU(3)_2); noted in SCOUT.md §0 to avoid conflating the two "weld operator" usages in the repo)
- `frontier/B667_computation_campaign_adjudication/ADJUDICATION.md` (the disclosed prior category error: "the weld operator restricted to the V2 block crosses the equivariance wall if read module-linearly" — directly informed the §1 equivariance-wall discussion and the ranking's design caution)

## Ocneanu / rigidity citation trail (repo-wide search)
- grep across the repo for "ocneanu", "davydov", "rigidity" — the only genuine hit on Ocneanu's actual mathematical work: `frontier/B312_face_iv_houses_the_form/FINDINGS.md` line 63 ("Ocneanu (quantum subgroups / module categories over SU(2)k)"); `frontier/B429_bosonic_rigidity/` uses "rigidity" in an unrelated sense (not read in full, confirmed unrelated by filename/grep context only)
- grep for "quantum cochain", "categorified fox", "tube algebra", "hochschild", "module categor(y/ies)" across the whole repo: no prior discussion found except the one Ocneanu citation above and one incidental "module" hit in `frontier/B670_anatomy_full/packet/VERDICT_LEDGER.md` (checked context, unrelated) — confirms this scout cell is genuinely new territory in the repo, consistent with its purpose.

## Exploratory computation (this cell's own output, not repo-modifying)
- `quantum_probe.py` (written and run in this cell's directory) — imports (read-only) `frontier/B238_su32_levelrank/su32_wrt.py`; computes SU(3)_2 fusion rules via Verlinde formula, the invertible-object Z/3 subgroup, and the weld operator's eigenvalues/ker/coker on the 6-dim stage.
- `quantum_probe_output.txt` — its verbatim output, cross-checked against banked trace(RL)=-1/phi (B238/B640) and ord(W(RL))=20 (B640) — both matched exactly, confirming the probe uses the correct banked conventions.

## Not read in full (time-bounded; referenced only via grep context, believed non-decisive)
- `frontier/B650_typed_functor/TYPES.md`, `PREREG_WAVE2.md` (the type-system detail behind the equivariance wall; FINDINGS.md's summary was judged sufficient for this scout's purposes)
- `frontier/B663_bifocal_anatomy/BIFOCAL_CLARIFICATION_CC2.md`, `anatomy_packet/ATLAS.md` (background only, not decisive to this cell's question)
- `docs/CAMPAIGN_STATUS.md`, `PROGRESS_LOG.md` (grepped for context terms, e.g. "the weld word R^2L = m136", not read end-to-end — this is a 440K-line changelog-style file)
