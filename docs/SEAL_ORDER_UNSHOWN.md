# The sealed tests whose order git cannot show (a list that may only shrink)

<!-- doc-currency: frozen -->

*Frozen 2026-11-06 at Review 76's R76-2 (P-601; Review 74's R74-9). Made from `scripts/gates/gates.py`'s
`seal_order_class()` at `4be2b821b`. Rows may only be removed. The gate `seal-order-unshown` recomputes the class from git on
every run and fails on any test not listed here, on any row beyond the ceiling `SEAL_ORDER_UNSHOWN_CEILING`, and on any
listed test whose order now shows.*

## The class

- **The class.** A sealed test is an arc folder holding `PREREGISTRATION.md`. Its order is unshown when its rule
  (`PREREGISTRATION.md`) and its record (`FINDINGS.md`) were first committed in the same commit, the early practice.
  - A rename keeps a file's first commit.
  - Ancestry certifies an order; a timestamp certifies nothing.
- **What it does not say.** It does not say that any of these tests was written after its results, nor that it was
  written before them. Git cannot show either.
  - The text is what was sealed. Its hashes, where it has them, are checked by `seal-digests`.
  - Its verdict stands as recorded, with this disclosure.
- **The count.** The Lab panel's Tests view counts 90 tests with an order it cannot show (P-535).
  - **80 have their rule and record in one commit.** This list is those 80, less B1670.
  - **9 more committed an output with their rule or script:** B1409, B1455, B1471, B1474, B1476, B1496 and
    B1609–B1611.
  - **The panel also counts B496's retitling** of its sealed rule after its record, adjudicated at Review 74 (P-535).
- **B1670 is in the class on main.** Its order is shown on the kept referee branch, where the seal `ad3dd5d44` is a
  strict ancestor of the record `fecdd63bd` (Review 74). The gate checks that ancestry in every clone.
- **The 9 are not on this list.** They stay with P-601. B496 is on it for its rule and record; its retitling is a
  separate matter, already adjudicated.

## The list (79)

| test | folder | the one commit | date |
|---|---|---|---|
| P3 | `frontier/P3_depth_exposure` | `b43902f73` | 2026-07-23 |
| B425 | `frontier/B425_geometric_torsion` | `ddc3ba1d5` | 2026-07-04 |
| B435 | `frontier/B435_child_founding` | `d7d149094` | 2026-07-05 |
| B480 | `frontier/B480_qca_dirac_lens` | `fb3a75a53` | 2026-07-08 |
| B496 | `frontier/B496_tm_endomorphism` | `baa49e6bd` | 2026-07-10 |
| B497 | `frontier/B497_endomorphism_monoid` | `398aa48a4` | 2026-07-10 |
| B498 | `frontier/B498_mixed_monoid_dynamics` | `2302f7c9d` | 2026-07-10 |
| B507 | `frontier/B507_beta_function` | `262b93381` | 2026-07-10 |
| B508 | `frontier/B508_geometry_machine` | `f4395d709` | 2026-07-10 |
| B531 | `frontier/B531_trace_map_gate` | `d6fb17814` | 2026-07-12 |
| B533 | `frontier/B533_coupling_invariance` | `70ba3b618` | 2026-07-12 |
| B535 | `frontier/B535_coupling_space` | `2accadc52` | 2026-07-12 |
| B539 | `frontier/B539_relations_campaign` | `1214a1e9b` | 2026-07-12 |
| B540 | `frontier/B540_observer_flow` | `474da0746` | 2026-07-12 |
| B548 | `frontier/B548_unhideable_census` | `844a6d9ae` | 2026-07-12 |
| B549 | `frontier/B549_forced_bin_predictions` | `844a6d9ae` | 2026-07-12 |
| B575 | `frontier/B575_bridge_obstruction` | `b29eedd12` | 2026-07-14 |
| B584 | `frontier/B584_theta_listener` | `00c176790` | 2026-07-14 |
| B585 | `frontier/B585_listener_law` | `c4c973acf` | 2026-07-14 |
| B586 | `frontier/B586_round3_handoff` | `3c0fa84d8` | 2026-07-14 |
| B587 | `frontier/B587_weil_mechanism` | `306f6dddb` | 2026-07-14 |
| B588 | `frontier/B588_sector_exchange` | `7c1c3908e` | 2026-07-14 |
| B592 | `frontier/B592_mirror_listener` | `35e586673` | 2026-07-14 |
| B593 | `frontier/B593_round4_hearing` | `63241bf0c` | 2026-07-14 |
| B594 | `frontier/B594_e6_hearing` | `8c0ff89f3` | 2026-07-14 |
| B595 | `frontier/B595_dictionary` | `1a369ba84` | 2026-07-14 |
| B596 | `frontier/B596_cat_map` | `07c5a152f` | 2026-07-14 |
| B632 | `frontier/B632_cubic_route` | `eb5a70787` | 2026-07-15 |
| B640 | `frontier/B640_hearing_group` | `b453fe24c` | 2026-07-16 |
| B641 | `frontier/B641_twistframe_law` | `53dab53bf` | 2026-07-16 |
| B642 | `frontier/B642_galois_ear` | `53dab53bf` | 2026-07-16 |
| B643 | `frontier/B643_flip_symmetry` | `2797776b6` | 2026-07-16 |
| B644 | `frontier/B644_mckay_comparison` | `6326874ce` | 2026-07-16 |
| B649 | `frontier/B649_silver_holonomy` | `a75150682` | 2026-07-16 |
| B654 | `frontier/B654_listening_synthesis` | `f196c8e53` | 2026-07-17 |
| B655 | `frontier/B655_beta_adjudication` | `48a9df89f` | 2026-07-17 |
| B658 | `frontier/B658_order4_flips` | `55a97bdcf` | 2026-07-17 |
| B709 | `frontier/B709_turok_marriage_adjudication` | `bb55a7c05` | 2026-07-19 |
| B742 | `frontier/B742_negatives_hunt_p1` | `4860553a8` | 2026-07-21 |
| B746 | `frontier/B746_golden_ledger` | `eeef58ae4` | 2026-07-21 |
| B747 | `frontier/B747_mirror_sweep` | `635b6574f` | 2026-07-21 |
| B748 | `frontier/B748_v4_completion` | `635b6574f` | 2026-07-21 |
| B749 | `frontier/B749_genesis_forks` | `08e16340f` | 2026-07-22 |
| B750 | `frontier/B750_lack_ledger` | `418fb45f1` | 2026-07-21 |
| B751 | `frontier/B751_iterated_hearing_adjudication` | `98c256e66` | 2026-07-22 |
| B752 | `frontier/B752_qualia_handoff_receipt` | `41697bd97` | 2026-07-22 |
| B753 | `frontier/B753_mixing_structure` | `870d8cc3f` | 2026-07-22 |
| B754 | `frontier/B754_p2_spectral` | `d251e3dfe` | 2026-07-22 |
| B755 | `frontier/B755_carried_recomputes` | `1cc2e3bc5` | 2026-07-22 |
| B757 | `frontier/B757_two_z3_identity` | `e6cf925f8` | 2026-07-22 |
| B758 | `frontier/B758_theorem_ledger` | `19452e225` | 2026-07-22 |
| B759 | `frontier/B759_qp3_integration` | `abc391955` | 2026-07-22 |
| B760 | `frontier/B760_qp4_closure` | `abc391955` | 2026-07-22 |
| B761 | `frontier/B761_qp2_private` | `abc391955` | 2026-07-22 |
| B762 | `frontier/B762_qp1_self_naming` | `abc391955` | 2026-07-22 |
| B764 | `frontier/B764_c19_comparator` | `ed22d8ab7` | 2026-07-22 |
| B765 | `frontier/B765_p3_depth` | `b00ac1f2d` | 2026-07-23 |
| B766 | `frontier/B766_measurement_torsor` | `ac3dd82f7` | 2026-07-23 |
| B767 | `frontier/B767_stabilizations` | `4d6f892bd` | 2026-07-23 |
| B768 | `frontier/B768_correspondence_crosstest` | `08a561c87` | 2026-07-23 |
| B769 | `frontier/B769_t1_structure` | `e789ef5f4` | 2026-07-23 |
| B771 | `frontier/B771_phase1_wave1` | `856957ad5` | 2026-07-23 |
| B780 | `frontier/B780_galois_reversal_gate` | `cb7ca083c` | 2026-07-24 |
| B781 | `frontier/B781_m003_sister` | `e22864e73` | 2026-07-24 |
| B782 | `frontier/B782_choice_incomputability` | `04dde4a61` | 2026-07-24 |
| B790 | `frontier/B790_maass_adjudication` | `99b627b93` | 2026-07-28 |
| B821 | `frontier/B821_lexicon_refresh` | `a7df05cd3` | 2026-07-30 |
| B822 | `frontier/B822_lexicon_gate_fix` | `a7df05cd3` | 2026-07-30 |
| B824 | `frontier/B824_charvar_motif` | `f5b4c934e` | 2026-07-30 |
| B825 | `frontier/B825_markov_motif` | `f5b4c934e` | 2026-07-30 |
| B830 | `frontier/B830_b720_recompute` | `9841601c4` | 2026-07-31 |
| B839 | `frontier/B839_b685_residue` | `13fcc83ca` | 2026-07-31 |
| B849 | `frontier/B849_order_parameter` | `9ffdd971f` | 2026-08-02 |
| B850 | `frontier/B850_length_spectrum_type` | `7ca82db06` | 2026-08-02 |
| B936 | `frontier/B936_cohomology_reading` | `4b92b097c` | 2026-08-06 |
| B1065 | `frontier/B1065_amendment_controls` | `69436c06e` | 2026-08-13 |
| B1066 | `frontier/B1066_lane3_nomination` | `74d87f311` | 2026-08-13 |
| B1102 | `frontier/B1102_exact_hypercharge_solve` | `6b206a14c` | 2026-08-21 |
| B1104 | `frontier/B1104_fourd_suspension` | `6683c0a28` | 2026-08-21 |
