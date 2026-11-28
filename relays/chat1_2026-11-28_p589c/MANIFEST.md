# MANIFEST: main's code, copied for the P-589 (c) card

Built by build_p589c.py from main at 88a1e9474. Each file is main's, verbatim, but for the lines listed; each such line
ends with a marker "# [copy: ...]". SHA-256 is of main's file.

- `exact_end_web_seat.py` from `88a1e9474:frontier/B1838_the_end/verification/exact_end_web_seat.py`, 148 lines, SHA-256 9bca3e3e389ea414
  - line 25, main's text: `import sys, json, math, pathlib, importlib.util, time`
  - line 29, main's text: `ROOT = pathlib.Path(sys.argv[1]).resolve(); HERE = pathlib.Path(__file__).resolve().parent`
  - line 30, main's text: `sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))`
  - line 32, main's text: `_spec = importlib.util.spec_from_file_location("b1667", ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.py")`
  - line 33, main's text: `C = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(C)`
- `census.py` from `88a1e9474:frontier/B1726_the_two_ingredients_replicated/verification/census.py`, 130 lines, SHA-256 185cf17d8b51c115
  - line 9, main's text: `import sys, io, json, math, contextlib, importlib.util, pathlib`
  - line 13, main's text: `ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())`
  - line 24, main's text: `        sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); _argv = sys.argv; sys.argv = ["x"]`
  - line 28, main's text: `        sys.path.insert(0, str(P1691))`
  - line 29, main's text: `        spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)`
  - line 30, main's text: `        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)`
  - line 113, main's text: `    from multiprocessing import Pool`
- `the_canonical_cusp.py` from `88a1e9474:frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.py`, 516 lines, SHA-256 dd5fe6893fd2d403
  - line 230, main's text: `import importlib.util, pathlib as _pl`
  - line 231, main's text: `_B1654 = sorted(_pl.Path(__file__).resolve().parents[3].glob("frontier/B1654_*/verification/the_norm_of_the_boundary_class.py"))[0]`
  - line 232, main's text: `_spec = importlib.util.spec_from_file_location("b1654", _B1654); b1654 = importlib.util.module_from_spec(_spec)`
  - line 233, main's text: `_src = _B1654.read_text()`
  - line 234, main's text: `_src = _src[:_src.index("# ---------------------------------------------------------------- route B")]   # route A and helpers only`
  - line 235, main's text: `_src = _src.replace("def thetas(z, tau):", "K = 40\ndef thetas(z, tau):", 1)`
  - line 236, main's text: `exec(compile(_src, str(_B1654), "exec"), b1654.__dict__)`
  - line 335, main's text: `from multiprocessing import Pool`
- `b1656_funcs.py` from `88a1e9474:frontier/B1723_the_golden_valley/verification/b1656_funcs.py`, 130 lines, SHA-256 31f09c433c14312d
- `the_exponents.py` from `88a1e9474:frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py`, 174 lines, SHA-256 a8d4ea9bae79dde8
- `qseries.py` from `88a1e9474:frontier/B1691_the_exponents_at_the_two_fixed_points/verification/qseries.py`, 88 lines, SHA-256 113b36d3da004a8a
- `b1654.py`: the text B1667's lines 231 to 236 executed, made from `88a1e9474:frontier/B1654_the_norm_of_the_boundary_class/verification/the_norm_of_the_boundary_class.py` (SHA-256 468fcf03672f0c50): its part before the line "# --- ... route B", with "def thetas(z, tau):" replaced once by "K = 40" and that line, as main's line 235 does
- data `main_tree/frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json` from `88a1e9474:frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json`, SHA-256 688152749777970f
- `p589c_exact_rows.py` from the seat's `e52f68352:relays/chat1_2026-11-25_p589c/p589c_exact_rows.py`, SHA-256 6645375691df3efb: its load() keeps only the import of exact_end_web_seat under the same stdout redirect, and returns main_tree as main's root
- `p589c_posthoc3.py` from the seat's `41e0fcbd2:relays/chat1_2026-11-25_p589c/p589c_posthoc3.py`, SHA-256 6bd69d2bbcc3f6f5: its import of p589c_exact_rows by importlib becomes a plain import, and its `import importlib.util` line becomes pass

ADDED 2026-11-28, before the card was filed (the card's stated commit holds the manifest above, unchanged otherwise):
- Two replaced lines are not loaders, and neither is on the run's path (census.py's still carries the "loader
  replaced" marker; the_canonical_cusp.py's carries its own): census.py line 113 (inside census.main()) and
  the_canonical_cusp.py line 335 (module level, used only by that module's own run) imported multiprocessing, which
  the rerun's guard refuses wherever it stands; the first becomes an exit and the second "Pool = None".
- b1654.py is not a file of main's but the text main's B1667 line 236 executed, made as its lines 233 to 235 make it.
