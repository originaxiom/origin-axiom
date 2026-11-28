#!/usr/bin/env python3
"""Builds this folder's copy of main's code for the P-589 (c) card (this seat, 2026-11-28, as main's M88 asks): B1838's
exact-norm instrument and every file it loads at main's commit 88a1e9474, copied verbatim into this one folder, with
only the loaders replaced, because the queue's rerun imports nothing but the modules beside the decisive script and
refuses any change to sys.path, any use of importlib, exec and compile, and any import of multiprocessing. Run once, by
hand, from a clone that holds 88a1e9474 and the seat's commits e52f68352 and 41e0fcbd2; not part of the card's run.

    python3 -I build_p589c.py <clone>

Each replaced line is checked against main's text before it is replaced, and carries the marker "# [copy: ...]".
B1667's module executed a slice of B1654's file with one text substitution (exec of compile); b1654.py here is that
slice with that substitution, exactly the text main's line executed. MANIFEST.md lists every file, its source, the
SHA-256 of main's file, and every replaced line with main's text. The copy's test is the card's own: card_p589c.py
reproduces the sealed outputs of 2026-11-25 (p589c_exact_rows_out.txt and p589c_posthoc3_out.txt) byte for byte.
"""
import hashlib
import pathlib
import subprocess
import sys

MAIN = "88a1e9474"
SEAT_ROWS, SEAT_POST = "e52f68352", "41e0fcbd2"
HERE = pathlib.Path(__file__).resolve().parent
MARK = "  # [copy: loader replaced, see MANIFEST.md]"
NEW_ROOT = 'ROOT = pathlib.Path(__file__).resolve().parent / "main_tree"'
B1838 = "frontier/B1838_the_end/verification/"
B1726 = "frontier/B1726_the_two_ingredients_replicated/verification/"
B1667 = "frontier/B1667_the_canonical_cusp/verification/"
B1654 = "frontier/B1654_the_norm_of_the_boundary_class/verification/"
B1723 = "frontier/B1723_the_golden_valley/verification/"
B1691 = "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/"
ROOT_HERE = 'ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())'

FILES = [
    (B1838 + "exact_end_web_seat.py", "exact_end_web_seat.py", {
        25: ("import sys, json, math, pathlib, importlib.util, time", "import sys, json, math, pathlib, time"),
        29: ("ROOT = pathlib.Path(sys.argv[1]).resolve(); HERE = pathlib.Path(__file__).resolve().parent",
             NEW_ROOT + "; HERE = pathlib.Path(__file__).resolve().parent"),
        30: ('sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))', "pass"),
        32: ('_spec = importlib.util.spec_from_file_location("b1667", ROOT / "frontier" / "B1667_the_canonical_cusp" / '
             '"verification" / "the_canonical_cusp.py")', "pass"),
        33: ("C = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(C)", "import the_canonical_cusp as C")}),
    (B1726 + "census.py", "census.py", {
        9: ("import sys, io, json, math, contextlib, importlib.util, pathlib", "import sys, io, json, math, contextlib, pathlib"),
        13: (ROOT_HERE, NEW_ROOT),
        24: ('        sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); '
             '_argv = sys.argv; sys.argv = ["x"]', '        _argv = sys.argv; sys.argv = ["x"]'),
        28: ("        sys.path.insert(0, str(P1691))", "        pass"),
        29: ('        spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); '
             'te = importlib.util.module_from_spec(spec)', "        pass"),
        30: ("        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)",
             "        with contextlib.redirect_stdout(io.StringIO()): import the_exponents as te"),
        113: ("    from multiprocessing import Pool",
              '    raise SystemExit("census.main() is not part of this copy: main\'s line 113 imports multiprocessing")')}),
    (B1667 + "the_canonical_cusp.py", "the_canonical_cusp.py", {
        230: ("import importlib.util, pathlib as _pl", "import pathlib as _pl"),
        231: ('_B1654 = sorted(_pl.Path(__file__).resolve().parents[3].glob("frontier/B1654_*/verification/'
              'the_norm_of_the_boundary_class.py"))[0]', "pass"),
        232: ('_spec = importlib.util.spec_from_file_location("b1654", _B1654); b1654 = importlib.util.module_from_spec(_spec)',
              "pass"),
        233: ("_src = _B1654.read_text()", "pass"),
        234: ('_src = _src[:_src.index("# ---------------------------------------------------------------- route B")]   '
              '# route A and helpers only', "pass"),
        235: ('_src = _src.replace("def thetas(z, tau):", "K = 40\\ndef thetas(z, tau):", 1)', "pass"),
        236: ('exec(compile(_src, str(_B1654), "exec"), b1654.__dict__)', "import b1654"),
        335: ("from multiprocessing import Pool",
              "Pool = None  # [copy: main's line imports multiprocessing, used only by this module's own run]")}),
    (B1723 + "b1656_funcs.py", "b1656_funcs.py", {}),
    (B1691 + "the_exponents.py", "the_exponents.py", {}),
    (B1691 + "qseries.py", "qseries.py", {}),
]
DATA = [(B1667 + "the_canonical_cusp.json", "main_tree/" + B1667 + "the_canonical_cusp.json")]


def show(clone, rev, path):
    return subprocess.run(["git", "-C", clone, "show", "%s:%s" % (rev, path)], capture_output=True, check=True).stdout


def edit(raw, edits, src):
    lines = raw.decode("utf-8").split("\n")
    for n, (old, new) in sorted(edits.items()):
        if lines[n - 1] != old:
            sys.exit("%s line %d is not as expected: %r" % (src, n, lines[n - 1]))
        lines[n - 1] = new if new.endswith("]") and "# [copy:" in new else new + MARK
    return "\n".join(lines)


def main(clone):
    man = ["# MANIFEST: main's code, copied for the P-589 (c) card", "",
           "Built by build_p589c.py from main at %s. Each file is main's, verbatim, but for the lines listed; each such "
           "line\nends with a marker \"# [copy: ...]\". SHA-256 is of main's file." % MAIN, ""]
    for src, name, edits in FILES:
        raw = show(clone, MAIN, src)
        (HERE / name).write_text(edit(raw, edits, src), encoding="utf-8")
        man.append("- `%s` from `%s:%s`, %d lines, SHA-256 %s" % (name, MAIN, src, raw.count(b"\n"),
                                                                hashlib.sha256(raw).hexdigest()[:16]))
        for n, (old, new) in sorted(edits.items()):
            man.append("  - line %d, main's text: `%s`" % (n, old))
    raw = show(clone, MAIN, B1654 + "the_norm_of_the_boundary_class.py")
    s = raw.decode("utf-8")
    s = s[:s.index("# ---------------------------------------------------------------- route B")]
    s = s.replace("def thetas(z, tau):", "K = 40\ndef thetas(z, tau):", 1)
    (HERE / "b1654.py").write_text(s, encoding="utf-8")
    man.append("- `b1654.py`: the text B1667's lines 231 to 236 executed, made from `%s:%sthe_norm_of_the_boundary_class.py` "
               "(SHA-256 %s): its part before the line \"# --- ... route B\", with \"def thetas(z, tau):\" replaced once by "
               "\"K = 40\" and that line, as main's line 235 does" % (MAIN, B1654, hashlib.sha256(raw).hexdigest()[:16]))
    for src, dest in DATA:
        raw = show(clone, MAIN, src)
        (HERE / dest).parent.mkdir(parents=True, exist_ok=True)
        (HERE / dest).write_bytes(raw)
        man.append("- data `%s` from `%s:%s`, SHA-256 %s" % (dest, MAIN, src, hashlib.sha256(raw).hexdigest()[:16]))
    K = "relays/chat1_2026-11-25_p589c/"
    rows = show(clone, SEAT_ROWS, K + "p589c_exact_rows.py").decode("utf-8")
    old = ('    head = subprocess.run(["git", "-C", main_dir, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()\n'
           '    if not head.startswith(REV):\n'
           '        sys.exit("the checkout is at %s, not %s" % (head[:9], REV))\n'
           '    import importlib.util\n'
           '    root = pathlib.Path(main_dir).resolve()\n'
           '    argv = sys.argv\n'
           '    sys.argv = [argv[0], str(root)]\n'
           '    sp = importlib.util.spec_from_file_location("ee", root / "frontier" / "B1838_the_end" / "verification" /\n'
           '                                                "exact_end_web_seat.py")\n'
           '    ee = importlib.util.module_from_spec(sp)\n'
           '    with contextlib.redirect_stdout(io.StringIO()):\n'
           '        sp.loader.exec_module(ee)\n'
           '    sys.argv = argv\n'
           '    return ee, root\n')
    new = ('    root = pathlib.Path(__file__).resolve().parent / "main_tree"' + MARK + '\n'
           '    with contextlib.redirect_stdout(io.StringIO()):\n'
           '        import exact_end_web_seat as ee' + MARK + '\n'
           '    return ee, root\n')
    assert rows.count(old) == 1, "p589c_exact_rows.py's load() is not as expected"
    (HERE / "p589c_exact_rows.py").write_text(rows.replace(old, new), encoding="utf-8")
    man.append("- `p589c_exact_rows.py` from the seat's `%s:%sp589c_exact_rows.py`, SHA-256 %s: its load() keeps only "
               "the import of exact_end_web_seat under the same stdout redirect, and returns main_tree as main's root"
               % (SEAT_ROWS, K, hashlib.sha256(rows.encode()).hexdigest()[:16]))
    post = show(clone, SEAT_POST, K + "p589c_posthoc3.py").decode("utf-8")
    old = ('spec = importlib.util.spec_from_file_location("rows", HERE / "p589c_exact_rows.py")\n'
           'RW = importlib.util.module_from_spec(spec)\n'
           'spec.loader.exec_module(RW)\n')
    new = 'import p589c_exact_rows as RW' + MARK + '\n'
    assert post.count(old) == 1 and post.count("import importlib.util\n") == 1
    post2 = post.replace(old, new).replace("import importlib.util\n", "pass" + MARK + "\n", 1)
    (HERE / "p589c_posthoc3.py").write_text(post2, encoding="utf-8")
    man.append("- `p589c_posthoc3.py` from the seat's `%s:%sp589c_posthoc3.py`, SHA-256 %s: its import of "
               "p589c_exact_rows by importlib becomes a plain import, and its `import importlib.util` line becomes pass"
               % (SEAT_POST, K, hashlib.sha256(post.encode()).hexdigest()[:16]))
    (HERE / "MANIFEST.md").write_text("\n".join(man) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1])
