#!/usr/bin/env python3
"""A check, labelled post hoc (written after route_b_readings was read): main's reading S~ = eps S* eps^T is S of the
conjugated Higgs components, S~(v) = S(conj v), with S(v) = v_i Q_I + v_j Q_J + v_k Q_K and main's Q_I, Q_J, Q_K, eps
(B1656's funcs at 3412bf09d, imported through route_b_scan).  By the quaternion relations eps Q_I eps^T = -Q_I,
eps Q_J eps^T = Q_J, eps Q_K eps^T = -Q_K, and conj(Q_I) = -Q_I, conj(Q_J) = Q_J, conj(Q_K) = -Q_K.
    python3 -B readings_identity.py      # writes readings_identity_run.txt"""
import contextlib, importlib.util, io, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("rbs", HERE / "route_b_scan.py")
rbs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rbs)
B = rbs.B
rel = {"eps Q_I eps^T + Q_I": B.EPS @ B.QI @ B.EPS.T + B.QI, "eps Q_J eps^T - Q_J": B.EPS @ B.QJ @ B.EPS.T - B.QJ,
       "eps Q_K eps^T + Q_K": B.EPS @ B.QK @ B.EPS.T + B.QK, "conj Q_I + Q_I": np.conj(B.QI) + B.QI,
       "conj Q_J - Q_J": np.conj(B.QJ) - B.QJ, "conj Q_K + Q_K": np.conj(B.QK) + B.QK}
rng = np.random.default_rng(1724)
dev = max(float(np.abs(rbs.St(rbs.S_of(v)) - rbs.S_of(np.conj(v))).max())
          for v in (rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(1000)))
lines = [f"{k}: {float(np.abs(m).max()):.1e}" for k, m in rel.items()] + [f"max |S~(v) - S(conj v)| over 1000 random v: {dev:.1e}"]
print("\n".join(lines))
(HERE / "readings_identity_run.txt").write_text("\n".join(lines) + "\n")
