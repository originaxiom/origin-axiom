"""Data-free: the 2-3 sector in the canonical frame (null Higgs h0): kappa_s = (row f2 . conj row f3)/|row f3|^2 of the
block B_s = [[a2 - i w, -a1], [2 a3, a2 + i w]]; V_cb against |kappa_u - kappa_d| and up m2/m3 against |w/(2 a3)|^2."""
import contextlib, importlib.util, io, sys, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("cs", HERE.parent / "channel_store.py"); cs = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(cs)
f1 = np.array([0, 1, -1j]) / math.sqrt(2); f2 = np.array([1, 0, 0], dtype=complex); f3 = np.array([0, 1, 1j]) / math.sqrt(2)
for (re_t, im_t, a, b) in ((0.5625, 2.6, 0.4, 0.1), (0.0625, 2.6, 0.4, 0.1), (0.35, 3.05, 0.4, 0.1), (0.1875, 2.8, 0.4, 0.9)):
    U = cs.weights(re_t, im_t, a, b)
    for ih, hor in enumerate(cs.HORS):
        k = {}; info = {}
        for i_s, sec in enumerate(("up", "down")):
            w, u = U[i_s, ih, 0], U[i_s, ih, 1:]
            a1, a2, a3 = np.vdot(f1, u), np.vdot(f2, u), np.vdot(f3, u)
            r2 = np.array([a2 - 1j * w, -a1]); r3 = np.array([2 * a3, a2 + 1j * w])
            k[sec] = np.vdot(r3, r2) / np.vdot(r3, r3)
            nu = np.linalg.norm(u); info[sec] = (abs(w / (2 * a3)) if abs(a3) > 0 else float("nan"), abs(a2 - 1j * w) / nu, abs(a2 + 1j * w) / nu)
        Yu = cs.closed(U[0, ih], f3); Yd = cs.closed(U[1, ih], f3)
        Uu, su, _ = np.linalg.svd(Yu); Ud, sd, _ = np.linalg.svd(Yd)
        V = np.conj(Uu[:, ::-1].T) @ Ud[:, ::-1]
        print(f"tau {re_t}+{im_t}i ({a},{b}) {hor:5s}: V_cb {abs(V[1,2]):.4f} vs |k_u - k_d| {abs(k['up'] - k['down']):.4f} (|k_u| {abs(k['up']):.4f}, |k_d| {abs(k['down']):.4f}); "
              f"up m2/m3 {su[1]/su[0]:.3e} vs |w/2a3|^2 {info['up'][0]**2:.3e}; down |a2-iw|/|u| {info['down'][1]:.3f}, |a2+iw|/|u| {info['down'][2]:.3f}")
