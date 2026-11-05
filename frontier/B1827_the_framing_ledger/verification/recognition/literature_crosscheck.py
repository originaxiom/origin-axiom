"""R1's cross-check against a published two-loop SM table (Antusch & Maurer, arXiv:1306.6879v2, Table 1, MS-bar, read on the
bench through a fetch on 2026-11-03; its SM columns stop at 10 TeV): the relative shifts M_Z -> 1 TeV and -> 10 TeV of
c/t, s/b, mu/tau, theta23 (~|V_cb|), theta13 (= |V_ub|), against running_control.py's one-loop shifts at the same scales."""
import math, sys, pathlib
sys.argv = ["x"]
import importlib.util
spec = importlib.util.spec_from_file_location("rc", pathlib.Path(__file__).with_name("running_control.py"))
AM = {  # printed values: M_Z, 1 TeV, 10 TeV
    "c/t": [3.60e-3 / 0.9861, 3.104e-3 / 0.8685, 2.776e-3 / 0.7894],
    "s/b": [3.12e-4 / 1.639e-2, 2.70e-4 / 1.388e-2, 2.42e-4 / 1.224e-2],
    "mu/tau": [5.899863e-4 / 1.002950e-2, 6.0127e-4 / 1.02213e-2, 6.0761e-4 / 1.0329e-2],
    "|V_cb|": [4.208e-2, 4.296e-2, 4.364e-2], "|V_ub|": [3.64e-3, 3.72e-3, 3.77e-3]}
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    rc = importlib.util.module_from_spec(spec); spec.loader.exec_module(rc)
f0, _ = rc.ten(rc.run(rc.MZ)); idx = {"c/t": 0, "s/b": 2, "mu/tau": 4, "|V_cb|": 7, "|V_ub|": 8}
for k, (a0, a1, a2) in AM.items():
    ours = [100 * (math.exp(rc.ten(rc.run(mu))[0][idx[k]] - f0[idx[k]]) - 1) for mu in (1e3, 1e4)]
    print("%-7s two-loop table: 1 TeV %+.2f%%  10 TeV %+.2f%%   | ours (one loop): 1 TeV %+.2f%%  10 TeV %+.2f%%" % (
        k, 100 * (a1 / a0 - 1), 100 * (a2 / a0 - 1), ours[0], ours[1]))
