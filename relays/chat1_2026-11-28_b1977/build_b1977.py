#!/usr/bin/env python3
"""Builds this folder's copy of main's frame for the B1977 card (this seat, 2026-11-28, as main's M88 asks): every file
main's B1940 frame_mp.py loads at main's commit 88a1e9474, copied verbatim into this one folder, and only the
loaders replaced, because the queue's rerun imports nothing but the modules beside the decisive script and refuses any
change to sys.path and any use of importlib. Run once, by hand, from a clone that holds be8c83d4f and the seat's
commits f77dae59f and 7dc9cdf67; it is not part of the card's run.

    python3 -I build_wlv1.py <clone>

Each replaced line is checked against main's text before it is replaced, and carries the marker "# [copy: ...]".
MANIFEST.md beside this file lists each file, its source, the SHA-256 of main's file, and every replaced line with
main's text. The test of the copy is the card's own: card_b1977.py reproduces the sealed output of 2026-11-24
(relays/chat1_2026-11-24_chk1/chk1b_out.txt) byte for byte.
"""
import hashlib
import pathlib
import subprocess
import sys

MAIN = "88a1e9474"
SEAT = "f77dae59f"
SEAT_RUN = "7dc9cdf67"
HERE = pathlib.Path(__file__).resolve().parent
NEW_ROOT = 'ROOT = pathlib.Path(__file__).resolve().parent / "main_tree"'
MARK = "  # [copy: loader replaced, see MANIFEST.md]"
A = "frontier/B1945_the_frames_cusp_exponents/verification/"
B40 = "frontier/B1940_the_area_options_corrected_in_extended_precision/verification/"
B32 = "frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/"
B28 = "frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/verification/"
B27 = ("frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_"
       "two_horocycle/verification/")
B24 = "frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/verification/"
B1724 = "frontier/B1724_the_readings_covariance/verification/"
B1716 = "frontier/B1716_the_zeros_derived/verification/"
B1691 = "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/"
B1667 = "frontier/B1667_the_canonical_cusp/verification/"
ROOT_LINE = 'ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())'
ROOT_HERE = 'ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())'

# (source path, its name here, {line: (main's text, the replacement)})
FILES = [
    (B40 + "frame_mp.py", "frame_mp.py", {
        15: (ROOT_LINE, NEW_ROOT),
        16: ('EB = next((ROOT / "frontier").glob("B1932_*")) / "verification"', "EB = pathlib.Path(__file__).resolve().parent"),
        17: ('sys.path.insert(0, str(EB)); _argv = sys.argv; sys.argv = ["x"]', '_argv = sys.argv; sys.argv = ["x"]')}),
    (B32 + "fiber_grid_t90.py", "fiber_grid_t90.py", {
        8: (ROOT_LINE, NEW_ROOT),
        9: ('V = next((ROOT / "frontier").glob("B1928_*")) / "verification"', "V = pathlib.Path(__file__).resolve().parent"),
        10: ("sys.path.insert(0, str(V))", "pass")}),
    (B28 + "fiber_grid.py", "fiber_grid.py", {
        13: (ROOT_HERE, NEW_ROOT),
        14: ('sys.path.insert(0, str(next((ROOT / "frontier").glob("B1927_*")) / "verification"))', "pass")}),
    (B27 + "canon_readout.py", "canon_readout.py", {
        18: (ROOT_HERE, NEW_ROOT),
        19: ('sys.path.insert(0, str(next((ROOT / "frontier").glob("B1924_*")) / "verification"))', "pass")}),
    (B24 + "thread_average.py", "thread_average.py", {
        15: (ROOT_HERE, NEW_ROOT),
        16: ('sys.path.insert(0, str(ROOT / "frontier" / "B1724_the_readings_covariance" / "verification"))', "pass")}),
    (B24 + "whole_average.py", "whole_average.py", {}),
    (B24 + "fast_norm.py", "fast_norm.py", {
        14: (ROOT_HERE, NEW_ROOT),
        15: ('sys.path.insert(0, str(ROOT / "frontier" / "B1716_the_zeros_derived" / "verification"))', "pass")}),
    (B1724 + "covariance.py", "covariance.py", {
        20: ("import sys, io, json, math, cmath, contextlib, importlib.util, pathlib",
             "import sys, io, json, math, cmath, contextlib, pathlib"),
        24: (ROOT_HERE, NEW_ROOT),
        36: ('        sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); '
             '_argv = sys.argv; sys.argv = ["x"]', '        _argv = sys.argv; sys.argv = ["x"]'),
        40: ("        sys.path.insert(0, str(P1691))", "        pass"),
        41: ('        spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); '
             'te = importlib.util.module_from_spec(spec)', "        pass"),
        42: ("        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)",
             "        with contextlib.redirect_stdout(io.StringIO()): import the_exponents as te"),
        130: ("    from multiprocessing import Pool",
              '    raise SystemExit("covariance.main() is not part of this copy: main\'s line 130 imports multiprocessing")')}),
    (B1716 + "b1656_funcs.py", "b1656_funcs.py", {}),     # B1723's b1656_funcs.py is the same file, byte for byte
    (B1691 + "the_exponents.py", "the_exponents.py", {}),
    (B1691 + "qseries.py", "qseries.py", {}),
]
B1977 = "frontier/B1977_order_30_rates_masses_and_mixing_on_one_grid/verification/"
DATA = [(B27 + "grid.json", "grid.json"), (B1667 + "the_canonical_cusp.json", "main_tree/" + B1667 + "the_canonical_cusp.json"),
        (B1977 + "rates30_run.json", "main_tree/" + B1977 + "rates30_run.json")]
TWIN = "frontier/B1723_the_golden_valley/verification/b1656_funcs.py"


def show(clone, rev, path):
    return subprocess.run(["git", "-C", clone, "show", "%s:%s" % (rev, path)], capture_output=True, check=True).stdout


def main(clone):
    man = ["# MANIFEST: main's frame, copied for the B1977 card", "",
           "Built by build_b1977.py from main at %s. Each file is main's, verbatim, but for the lines listed; each such "
           "line\nends with the marker \"# [copy: loader replaced, see MANIFEST.md]\". SHA-256 is of main's file." % MAIN, ""]
    for src, name, edits in FILES:
        raw = show(clone, MAIN, src)
        lines = raw.decode("utf-8").split("\n")
        for n, (old, new) in sorted(edits.items()):
            if lines[n - 1] != old:
                sys.exit("%s line %d is not as expected: %r" % (src, n, lines[n - 1]))
            lines[n - 1] = new + MARK
        (HERE / name).write_text("\n".join(lines), encoding="utf-8")
        man.append("- `%s` from `%s:%s`, %d lines, SHA-256 %s" % (name, MAIN, src, raw.count(b"\n"),
                                                                hashlib.sha256(raw).hexdigest()[:16]))
        for n, (old, new) in sorted(edits.items()):
            man.append("  - line %d, main's text: `%s`" % (n, old))
    twin = show(clone, MAIN, TWIN)
    assert twin == show(clone, MAIN, B1716 + "b1656_funcs.py")
    man.append("- `%s` (B1723's) is the same file as B1716's, byte for byte (SHA-256 %s): one copy serves both"
               % (TWIN, hashlib.sha256(twin).hexdigest()[:16]))
    for src, dest in DATA:
        raw = show(clone, MAIN, src)
        (HERE / dest).parent.mkdir(parents=True, exist_ok=True)
        (HERE / dest).write_bytes(raw)
        man.append("- data `%s` from `%s:%s`, SHA-256 %s" % (dest, MAIN, src, hashlib.sha256(raw).hexdigest()[:16]))
    # the seat's own CHK-1 files, with their loaders replaced the same way
    K = "relays/chat1_2026-11-24_chk1/"
    SEATFILES = [
        (SEAT, K + "chk1b_independent.py", {17: ("sys.path.insert(0, HERE)", "pass")}),
        (SEAT, K + "chk1_ref_frame.py", {
            10: ("MAIN = sys.argv[1] if len(sys.argv) > 1 else None", 'MAIN = __file__.rsplit("/", 1)[0] + "/main_tree"'),
            11: ('sys.path.insert(0, glob.glob(MAIN + "/frontier/B1940_*/verification")[0])', "pass")}),
        (SEAT_RUN, K + "chk1_run.py", {
            13: ("import multiprocessing as mpc", "pass"),
            22: ('sys.path.insert(0, os.path.join(HERE, "..", "chat1_2026-11-19_wd2"))', "pass"),
            23: ("import wd2_run as W  # noqa: E402  (reads sys.argv[1] as the checkout of main)",
                 "W = None  # the copy does not load W-D2's module: chk1b_independent.py uses only points(), SLOW, KEYS")}),
    ]
    for rev, path, edits in SEATFILES:
        raw = show(clone, rev, path)
        lines = raw.decode("utf-8").split("\n")
        for n, (old, new) in sorted(edits.items()):
            if lines[n - 1] != old:
                sys.exit("%s line %d is not as expected: %r" % (path, n, lines[n - 1]))
            lines[n - 1] = new + MARK
        name = path.rsplit("/", 1)[1]
        (HERE / name).write_text("\n".join(lines), encoding="utf-8")
        man.append("- `%s` from the seat's `%s:%s`, SHA-256 %s" % (name, rev, path, hashlib.sha256(raw).hexdigest()[:16]))
        for n, (old, new) in sorted(edits.items()):
            man.append("  - line %d, the seat's text: `%s`" % (n, old))
    (HERE / "MANIFEST.md").write_text("\n".join(man) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1])
