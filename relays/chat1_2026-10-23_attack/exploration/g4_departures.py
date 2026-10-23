"""Data-free: the record Higgs forms' departures from their leading null eigenline at the cusp, delta (along e1) and
epsilon (along the other null line), against r = exp(-pi Im tau): delta / r^(1/2) and epsilon / r tend to constants."""
import contextlib, importlib.util, io, sys, math, pathlib
import numpy as np
ZF = pathlib.Path(__file__).resolve().parents[2] / "chat1_2026-10-23_zero_free_frame"
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py"); zfc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(zfc)
rbs = zfc.rbs
f1 = np.array([0, 1, -1j]) / math.sqrt(2); f2 = np.array([1, 0, 0], dtype=complex); f3 = np.array([0, 1, 1j]) / math.sqrt(2)
def dep(v):
    c = np.array([np.vdot(f2, v), np.vdot(f3, v), np.vdot(f1, v)])
    lead = 1 if abs(c[1]) >= abs(c[2]) else 2
    return abs(c[0] / c[lead]), abs(c[3 - lead] / c[lead]), ["h0", "conj h0"][lead - 1]
for d in ("F_2", "dR", "F_6", "F_10", "F_14", "F_22", "h2", "h3"):
    row = []
    for y in (2.5, 3.0, 3.5, 4.0):
        r = math.exp(-math.pi * y)
        if d in ("h2", "h3"):
            v = rbs.at(rbs.H2 if d == "h2" else rbs.H3, 0.3, y); v = v / np.linalg.norm(v)
        else:
            v = zfc.direction(d, 0.3, y)
        de, ep, lead = dep(v)
        row.append(f"Im {y}: delta/r^.5 {de / r ** 0.5:9.4f}  eps/r {ep / r:9.4f} ({lead})")
    print(f"{d:5s} " + " | ".join(row))
