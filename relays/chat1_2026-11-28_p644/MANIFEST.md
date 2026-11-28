# MANIFEST: main's frame, copied for the P-644 card

Built by build_p644.py from main at 88a1e9474. Each file is main's, verbatim, but for the lines listed; each such line
ends with the marker "# [copy: loader replaced, see MANIFEST.md]". SHA-256 is of main's file.

- `thread_average.py` from `88a1e9474:frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/verification/thread_average.py`, 111 lines, SHA-256 9fdba403ec89136b
  - line 15, main's text: `ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())`
  - line 16, main's text: `sys.path.insert(0, str(ROOT / "frontier" / "B1724_the_readings_covariance" / "verification"))`
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
- data `main_tree/frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json` from `88a1e9474:frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json`, SHA-256 688152749777970f
- `p644_rival.py` from the seat's `348e7874f:relays/chat1_2026-11-25_p644/p644_rival.py`, SHA-256 5528fa7f8298a07c: its load() keeps the plain imports of thread_average, fast_norm and covariance and the patch of cA (main's commit check, root and sys.path insert removed)
- `p644_rival_posthoc.py` from the seat's `5b3ca3e7b:relays/chat1_2026-11-25_p644/p644_rival_posthoc.py`, SHA-256 ea4c70a44bd1621f: its import of p644_rival by importlib becomes a plain import, and its `import importlib.util` line becomes pass
