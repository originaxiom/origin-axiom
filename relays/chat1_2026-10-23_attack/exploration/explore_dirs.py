"""EXPLORATORY, data-free: the Higgs directions' components on rho(T)'s eigenlines at a few band points."""
import contextlib, importlib.util, io, sys, math, pathlib
import numpy as np
ZF = pathlib.Path(__file__).resolve().parents[2] / "chat1_2026-10-23_zero_free_frame"
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py")
zfc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(zfc)
e1 = np.array([1, 0, 0], dtype=complex); h0 = np.array([0, 1, 1j]) / math.sqrt(2); hb = np.conj(h0)
for tau in (0.5 + 2.6j, 0.35 + 3.05j, 0.1 + 2.0j, 0.1 + 1.5j):
    r = math.exp(-math.pi * tau.imag)
    print(f"tau {tau}, r = {r:.3e}, r^1/2 = {r**0.5:.3e}, r^1/4 = {r**0.25:.3e}")
    for d in ("dR", "F_6", "F_22", "F_-2", "F_2", "F_10", "F_-6"):
        v = zfc.direction(d, tau.real, tau.imag)
        c = [np.vdot(x, v) for x in (e1, h0, hb)]
        print(f"  {d:5s} |e1| {abs(c[0]):.3e}  |h0| {abs(c[1]):.3e}  |h0bar| {abs(c[2]):.3e}   |v.v| {abs(v @ v):.3e}")
