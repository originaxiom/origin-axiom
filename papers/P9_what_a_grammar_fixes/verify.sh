#!/bin/sh
# One-command verification of the paper: its own checks, then the locks of every arc of the record that the paper cites.
# Run from a clone of the repository (the locks read the arcs' committed outputs). Single-threaded BLAS.
set -e
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1
for c in checks/*.py; do echo "== $c"; python3 -B "$c"; done
ROOT=$(cd ../.. && pwd)
cd "$ROOT"
python3 -m pytest -q \
  tests/test_b1323_the_genesis_upgrades.py tests/test_b1454_genesis.py \
  tests/test_b1600_the_weave_verified.py tests/test_b1601_the_common_point_is_the_geometry_mod_3.py \
  tests/test_b1604_the_class_index_is_not_an_index.py tests/test_b1606_three_on_the_weave_graded.py \
  tests/test_b1609_the_even_subweave.py tests/test_b1620_the_breaking_the_weave_allows.py \
  tests/test_b1621_the_principles_clock_and_tick.py tests/test_b1633_the_weaves_word_coupling.py \
  tests/test_b1634_w50_on_main.py tests/test_b1640_the_frame_audit.py \
  tests/test_b1641_w46_on_main_and_the_two_objects.py tests/test_b1651_where_a_higgs_can_couple.py \
  tests/test_b1653_the_rank_of_a_point_coupling.py tests/test_b1654_the_norm_of_the_boundary_class.py \
  tests/test_b1656_the_electrons_zero.py tests/test_b1657_the_symmetric_point.py \
  tests/test_b1658_the_twisted_half_bound.py tests/test_b1659_the_joint_law.py \
  tests/test_b1660_the_one_higgs_census.py tests/test_b1662_the_pull_back_acts.py \
  tests/test_b1663_the_pull_backs_strength.py tests/test_b1666_the_layers_robust.py \
  tests/test_b1667_the_canonical_cusp.py tests/test_b1668_the_web_seats_low_thread_negatives_verified.py \
  tests/test_b1421_completeness_sweep.py tests/test_b1479_the_bit_is_the_sign.py \
  tests/test_b1481_the_hand_is_a_phase.py tests/test_b1603_the_count_at_every_member.py \
  tests/test_b1607_the_principles_tick_at_the_common_point.py tests/test_b1632_w45_on_main.py \
  tests/test_b1635_b1636_couplings_and_the_golden_spectrum.py tests/test_b1637_fits_on_the_ruled_branch.py \
  tests/test_b1644_a_higgs_in_the_multiplicity_space.py tests/test_b1645_the_half_bound.py \
  tests/test_b1646_the_direction_is_the_mass_matrix.py tests/test_b1649_the_kernel_at_the_puncture.py \
  tests/test_b1655_main_audits_its_negatives.py tests/test_b1664_the_layers.py tests/test_b1665_the_layers_resealed.py \
  frontier/B1624_the_gate_sees_the_dossier/verification/test_b1624_the_gate_sees_the_dossier.py \
  frontier/B1625_the_seats_corrections_to_b1620_taken/verification/test_b1625_the_seats_corrections_taken.py \
  frontier/B1648_the_scope_repairs/verification/test_b1648_the_scope_repairs.py \
  frontier/B1650_chat1s_field_and_scale_notes_verified/verification/test_b1650_chat1s_field_notes_verified.py
