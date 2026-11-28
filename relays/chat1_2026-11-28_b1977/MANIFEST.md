# MANIFEST: main's frame, copied for the B1977 card

Built by build_b1977.py from main at 88a1e9474. Each file is main's, verbatim, but for the lines listed; each such line
ends with the marker "# [copy: loader replaced, see MANIFEST.md]". SHA-256 is of main's file.

- `frame_mp.py` from `88a1e9474:frontier/B1940_the_area_options_corrected_in_extended_precision/verification/frame_mp.py`, 130 lines, SHA-256 718e208a6eedf352
  - line 15, main's text: `ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())`
  - line 16, main's text: `EB = next((ROOT / "frontier").glob("B1932_*")) / "verification"`
  - line 17, main's text: `sys.path.insert(0, str(EB)); _argv = sys.argv; sys.argv = ["x"]`
- `fiber_grid_t90.py` from `88a1e9474:frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/fiber_grid_t90.py`, 59 lines, SHA-256 172ecaa943bf866a
  - line 8, main's text: `ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())`
  - line 9, main's text: `V = next((ROOT / "frontier").glob("B1928_*")) / "verification"`
  - line 10, main's text: `sys.path.insert(0, str(V))`
- `fiber_grid.py` from `88a1e9474:frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/verification/fiber_grid.py`, 51 lines, SHA-256 8107fd2fc80a5e9c
  - line 13, main's text: `ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())`
  - line 14, main's text: `sys.path.insert(0, str(next((ROOT / "frontier").glob("B1927_*")) / "verification"))`
- `canon_readout.py` from `88a1e9474:frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_two_horocycle/verification/canon_readout.py`, 114 lines, SHA-256 34432d7bb9075720
  - line 18, main's text: `ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())`
  - line 19, main's text: `sys.path.insert(0, str(next((ROOT / "frontier").glob("B1924_*")) / "verification"))`
- `thread_average.py` from `88a1e9474:frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/verification/thread_average.py`, 111 lines, SHA-256 9fdba403ec89136b
  - line 15, main's text: `ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())`
  - line 16, main's text: `sys.path.insert(0, str(ROOT / "frontier" / "B1724_the_readings_covariance" / "verification"))`
- `whole_average.py` from `88a1e9474:frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/verification/whole_average.py`, 63 lines, SHA-256 cd012803089b85d2
- `fast_norm.py` from `88a1e9474:frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/verification/fast_norm.py`, 73 lines, SHA-256 272de87d5b1b8a7a
  - line 14, main's text: `ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())`
  - line 15, main's text: `sys.path.insert(0, str(ROOT / "frontier" / "B1716_the_zeros_derived" / "verification"))`
- `covariance.py` from `88a1e9474:frontier/B1724_the_readings_covariance/verification/covariance.py`, 152 lines, SHA-256 75bc75017f487481
  - line 20, main's text: `import sys, io, json, math, cmath, contextlib, importlib.util, pathlib`
  - line 24, main's text: `ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())`
  - line 36, main's text: `        sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); _argv = sys.argv; sys.argv = ["x"]`
  - line 40, main's text: `        sys.path.insert(0, str(P1691))`
  - line 41, main's text: `        spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)`
  - line 42, main's text: `        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)`
  - line 130, main's text: `    from multiprocessing import Pool`
- `b1656_funcs.py` from `88a1e9474:frontier/B1716_the_zeros_derived/verification/b1656_funcs.py`, 130 lines, SHA-256 31f09c433c14312d
- `the_exponents.py` from `88a1e9474:frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py`, 174 lines, SHA-256 a8d4ea9bae79dde8
- `qseries.py` from `88a1e9474:frontier/B1691_the_exponents_at_the_two_fixed_points/verification/qseries.py`, 88 lines, SHA-256 113b36d3da004a8a
- `frontier/B1723_the_golden_valley/verification/b1656_funcs.py` (B1723's) is the same file as B1716's, byte for byte (SHA-256 31f09c433c14312d): one copy serves both
- data `grid.json` from `88a1e9474:frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_two_horocycle/verification/grid.json`, SHA-256 11d822f4357d1cb5
- data `main_tree/frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json` from `88a1e9474:frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json`, SHA-256 688152749777970f
- data `main_tree/frontier/B1977_order_30_rates_masses_and_mixing_on_one_grid/verification/rates30_run.json` from `88a1e9474:frontier/B1977_order_30_rates_masses_and_mixing_on_one_grid/verification/rates30_run.json`, SHA-256 337e21e4ec932b45
- `chk1b_independent.py` from the seat's `f77dae59f:relays/chat1_2026-11-24_chk1/chk1b_independent.py`, SHA-256 9d6b83741d9c6715
  - line 17, the seat's text: `sys.path.insert(0, HERE)`
- `chk1_ref_frame.py` from the seat's `f77dae59f:relays/chat1_2026-11-24_chk1/chk1_ref_frame.py`, SHA-256 ee378cae28ecd631
  - line 10, the seat's text: `MAIN = sys.argv[1] if len(sys.argv) > 1 else None`
  - line 11, the seat's text: `sys.path.insert(0, glob.glob(MAIN + "/frontier/B1940_*/verification")[0])`
- `chk1_run.py` from the seat's `7dc9cdf67:relays/chat1_2026-11-24_chk1/chk1_run.py`, SHA-256 5d2fcd65b076c434
  - line 13, the seat's text: `import multiprocessing as mpc`
  - line 22, the seat's text: `sys.path.insert(0, os.path.join(HERE, "..", "chat1_2026-11-19_wd2"))`
  - line 23, the seat's text: `import wd2_run as W  # noqa: E402  (reads sys.argv[1] as the checkout of main)`

ADDED 2026-11-28, after the referee read (the card's stated commit holds the manifest above, unchanged otherwise):
- Three replaced lines are not loaders, and none is on the run's path: covariance.py line 130 and chk1_run.py line 13
  imported multiprocessing, which the rerun's guard refuses wherever it stands; chk1_run.py line 23 imported W-D2's
  module, which chk1b_independent.py does not use (it takes only points(), SLOW and KEYS from chk1_run.py).
- build_b1977.py was derived from build_wlv1.py: its docstring's "be8c83d4f" should read 88a1e9474, its usage line
  names build_wlv1.py, and its constant A is unused. None of this is on the run's path.
