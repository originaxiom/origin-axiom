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
  tests/test_b1667_the_canonical_cusp.py
