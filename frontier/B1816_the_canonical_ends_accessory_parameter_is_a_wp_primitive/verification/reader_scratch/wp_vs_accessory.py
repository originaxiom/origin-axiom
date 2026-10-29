"""EXPLORATORY, UNSEALED (literature-report sanity check; not a banked result).
Does the B1667 accessory parameter c(tau) (y'' + (P/4 + c) y = 0) satisfy  dc/dtaubar = (i/4) * J,
J = d(l,t)/d(x,y) the Fenchel-Nielsen Jacobian (dl^dt = J dx^dy)?  [ <=> d(sigma_F - sigma_ref) = -i omega_WP,
omega_WP = (1/2) dl^dt (Wolpert's normalisation), C = 2c the Schwarzian accessory parameter.]
Also compares the hyperbolic alternative c_hyp = (pi^2/12) E2*(tau), and the cusp law l ~ pi/(y + 4 log2/pi)."""
import os, sys, time, importlib.util, json, pathlib
ROOT = next(r for r in pathlib.Path(__file__).resolve().parents if (r / "frontier").is_dir() and (r / "GENESIS.md").is_file())
sys.dont_write_bytecode = True
P = ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.py"
spec = importlib.util.spec_from_file_location("cc", P); cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
import numpy as np
from multiprocessing import Pool

RUN = json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())
GRID = {(round(p["tau"][0], 6), round(p["tau"][1], 6)): complex(*p["c"]) for p in RUN["points"]}

def fn(tau, c):
    _, _, Aa, Ab = cc.monodromy(tau, c)
    x, y, z = (abs(v) for v in cc.traces(Aa, Ab))
    l = 2 * np.arccosh(x / 2)
    t = 2 * np.arcsinh((2 * z - x * y) / (2 * x))        # FN twist of the a-curve (derived; = 0 at i, = l/2 at omega)
    return l, t, (x, y, z)

def E2star(tau):
    q = np.exp(2j * np.pi * tau); n = np.arange(1, 400)
    return 1 - 24 * np.sum(n * q ** n / (1 - q ** n)) - 3 / (np.pi * tau.imag)

def nearest_start(tau):
    k = min(GRID, key=lambda k: abs(complex(*k) - tau)); return complex(*k), GRID[k]

def job(tau, h=1e-3):
    tau = complex(tau); t0 = time.time()
    tau_s, c_s = nearest_start(tau)
    c0, res0 = cc.newton_walk(tau_s, c_s, tau, step=0.1) if abs(tau - tau_s) > 1e-12 else cc.solve_accessory(tau, c_s)
    out = {"tau": [tau.real, tau.imag], "c": [c0.real, c0.imag]}
    vals = {}
    for key, d in (("xp", h), ("xm", -h), ("yp", 1j * h), ("ym", -1j * h)):
        c, r = cc.solve_accessory(tau + d, c0)
        assert np.max(np.abs(r)) < 1e-11, (tau, key, r)
        vals[key] = (c,) + fn(tau + d, c)[:2]
    l0, t0_, tr = fn(tau, c0)
    cx = (vals["xp"][0] - vals["xm"][0]) / (2 * h); cy = (vals["yp"][0] - vals["ym"][0]) / (2 * h)
    dcb = 0.5 * (cx + 1j * cy)
    lx = (vals["xp"][1] - vals["xm"][1]) / (2 * h); ly = (vals["yp"][1] - vals["ym"][1]) / (2 * h)
    tx = (vals["xp"][2] - vals["xm"][2]) / (2 * h); ty = (vals["yp"][2] - vals["ym"][2]) / (2 * h)
    J = lx * ty - ly * tx
    out.update(l=l0, t=t0_, traces=tr, dcbar=[dcb.real, dcb.imag], J=J,
               ratio_ImDcb_over_Jq=dcb.imag / (J / 4), re_over_abs=abs(dcb.real) / abs(dcb),
               hyp_pred=np.pi / (8 * tau.imag ** 2), wp_cusp_pred=np.pi ** 2 / (4 * tau.imag ** 3),
               c_hyp=complex((np.pi ** 2 / 12) * E2star(tau)).real,
               C_minus_cusp_law=(2 * c0 - (np.pi ** 2 / 6 - l0 ** 2 / 2)),
               delta_eff=np.pi / l0 - tau.imag, secs=time.time() - t0)
    return out

def fmt(r):
    tau = complex(*r["tau"]); c = complex(*r["c"])
    return (f"{tau.real:6.2f}{tau.imag:+6.2f}i Imdcb={r['dcbar'][1]:.6e} J/4={r['J']/4:.6e} ratio={r['ratio_ImDcb_over_Jq']:.6f} "
            f"|Re|/|dcb|={r['re_over_abs']:.1e} hyp={r['hyp_pred']:.4e} wpcusp={r['wp_cusp_pred']:.4e} |C-(pi2/6-l2/2)|={abs(r['C_minus_cusp_law']):.3e} "
            f"c={c.real:.8f}{c.imag:+.8f}j c_hyp={r['c_hyp']:.6f} l={r['l']:.8f} t={r['t']:.8f} d_eff={r['delta_eff']:.5f} ({r['secs']:.0f}s)")

if __name__ == "__main__":
    taus = [0.25 + 3.0j, 0.25 + 4.0j, 0.15 + 1.25j, 0.25 + 1.0j, 1j, 0.35 + 1.5j, 0.05 + 2.0j, 0.45 + 0.95j,
            0.1 + 1.1j, 0.25 + 5.0j, 0.25 + 6.0j, 0.25 + 8.0j]
    out = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "wp_vs_accessory.jsonl"), "w")
    with Pool(2) as pool:
        for r in pool.imap_unordered(job, taus):
            out.write(json.dumps(r, default=str) + "\n"); out.flush()
            print(fmt(r), flush=True)
