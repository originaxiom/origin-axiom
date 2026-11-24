#!/usr/bin/env python3
"""Checks that fd_rank.py's embedded frame computes what main's own modules compute. Data-free.

    python3 -I validate_fd_rank.py <a checkout of main>

It compares rows_at from fd_rank.py with main's cm_zero_line.rows_at (B1821), loaded from the checkout as this seat's
relations_check.py loaded it, at the 16 (line, tau) points of the rank and at the four shifts of one of them.

Expectations, written before the run:
  V1  every row's six mass ratios, three |V| and J agree to 1e-12 relative (or 1e-14 absolute for J).   90 %
  V2  fd_rank.py's printed part (1) equals relations_check_out.txt's part (1) line for line (checked by diff after
      fd_rank.py's run).                                                                               90 %
"""
import contextlib
import importlib.util
import io
import os
import pathlib
import sys
from fractions import Fraction as Fr

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("fd_rank", HERE / "fd_rank.py")
FD = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FD)
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
cwd = os.getcwd()
os.chdir(ROOT)
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    Z.mods()
os.chdir(cwd)

LINES1 = [(Fr(1, 7), Fr(2, 7)), (Fr(3, 8), Fr(3, 8)), (Fr(4, 9), Fr(1, 3)), (Fr(2, 5), Fr(1, 10)), (Fr(3, 11), Fr(5, 11)),
          (Fr(1, 12), Fr(0)), (Fr(5, 12), Fr(1, 4)), (Fr(1, 4), Fr(1, 8))]
pts = [(line, tau) for line in LINES1 for tau in (complex(0.13, 2.2), complex(0.31, 3.1))]
h = 1e-5
pts += [(LINES1[0], complex(0.13, 2.2) + d) for d in (h, -h, 1j * h, -1j * h)]
worst_rel, worst_J, nrows, keymis = 0.0, 0.0, 0, 0
for line, tau in pts:
    with contextlib.redirect_stdout(io.StringIO()):
        a = Z.rows_at(tau, line)
        b = FD.rows_at(tau, line)
    if len(a) != len(b):
        keymis += 1
        continue
    for ra, rb in zip(a, b):
        if (ra["direction"], ra["radius"], ra["reading"], ra["V defined"]) != (
                rb["direction"], rb["radius"], rb["reading"], rb["V defined"]):
            keymis += 1
            continue
        nrows += 1
        va = ra["up"] + ra["down"] + ra["lepton"] + ra["V"]
        vb = rb["up"] + rb["down"] + rb["lepton"] + rb["V"]
        for x, y in zip(va, vb):
            if max(abs(x), abs(y)) > 1e-300:
                worst_rel = max(worst_rel, abs(x - y) / max(abs(x), abs(y)))
        worst_J = max(worst_J, abs(ra["J"] - rb["J"]))
v1 = keymis == 0 and worst_rel <= 1e-12 and worst_J <= 1e-14
print("V1 holds: %s | points %d, rows %d, mismatched keys %d, worst relative difference %.2e, worst J difference %.2e"
      % (v1, len(pts), nrows, keymis, worst_rel, worst_J))
