#!/usr/bin/env python3
"""POST HOC estimate, labelled: rough one-loop Standard Model running of the Georgi-Jarlskog ratios
    R2 = (y_mu/y_tau)/(y_s/y_b),  R1 = (y_d/y_b)/(y_e/y_tau),  D = R2*R1,  Z = R2/R1
from M_Z to 2e16 GeV.  Diagonal Yukawas; the top enters the down-type ratios through |V_tb| = 1 only; the light
entries' own Yukawas are neglected; gauge couplings at M_Z are approximate MS-bar values.  Starting masses: Huang-Zhou
2021 at M_Z, read from the record's pinned file at main's 3412bf09d.  An estimate of the size of the scale effect, not
a precision running.
    python3 -B rg_ratios.py      # writes rg_ratios_run.txt"""
import hashlib, json, math, subprocess, pathlib
from scipy.integrate import solve_ivp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
b = subprocess.run(["git", "show", "3412bf09d:frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"],
                   cwd=ROOT, capture_output=True, check=True).stdout
assert hashlib.sha256(b).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
m = json.loads(b)["masses_GeV"]["value"]
MZ = 91.1876
v = 246.0 / math.sqrt(2)
y0 = {k: m[k] / v for k in ("t", "b", "tau", "s", "d", "mu", "e")}
G0 = [math.sqrt(5 / 3) * 0.3578, 0.6517, 1.2177]          # g1 (GUT-normalised), g2, g3 at M_Z, approximate


def rhs(t, Y):
    g1, g2, g3, yt, yb, ytau, ls, ld, lmu, le = Y           # l* = ln(y_light / y_third of its sector)
    k = 1 / (16 * math.pi ** 2)
    T = 3 * yt ** 2 + 3 * yb ** 2 + ytau ** 2
    dyt = k * yt * (1.5 * (yt ** 2 - yb ** 2) + T - (17 / 20 * g1 ** 2 + 9 / 4 * g2 ** 2 + 8 * g3 ** 2))
    dyb = k * yb * (1.5 * (yb ** 2 - yt ** 2) + T - (1 / 4 * g1 ** 2 + 9 / 4 * g2 ** 2 + 8 * g3 ** 2))
    dytau = k * ytau * (1.5 * ytau ** 2 + T - (9 / 4 * g1 ** 2 + 9 / 4 * g2 ** 2))
    dlq = k * 1.5 * (yt ** 2 - yb ** 2)                      # the trace and gauge parts cancel in a ratio
    dll = k * 1.5 * (-ytau ** 2)
    return [k * 41 / 10 * g1 ** 3, k * (-19 / 6) * g2 ** 3, k * (-7) * g3 ** 3, dyt, dyb, dytau, dlq, dlq, dll, dll]


Y0 = G0 + [y0["t"], y0["b"], y0["tau"], math.log(y0["s"] / y0["b"]), math.log(y0["d"] / y0["b"]),
           math.log(y0["mu"] / y0["tau"]), math.log(y0["e"] / y0["tau"])]
LOG = []
for mu in (MZ, 1e3, 1e8, 1e12, 2e16):
    sol = solve_ivp(rhs, [0, math.log(mu / MZ)], Y0, rtol=1e-10, atol=1e-13) if mu > MZ else None
    Y = sol.y[:, -1] if sol is not None else Y0
    _g1, _g2, _g3, yt, yb, ytau, ls, ld, lmu, le = Y
    R2 = math.exp(lmu - ls); R1 = math.exp(ld - le)
    s = f"mu = {mu:.4g} GeV: y_t {yt:.3f}, y_b/y_tau {yb / ytau:.3f}, R2 {R2:.3f}, R1 {R1:.3f}, D {R2 * R1:.3f}, Z {R2 / R1:.3f}"
    LOG.append(s); print(s)
(HERE / "rg_ratios_run.txt").write_text("\n".join(LOG) + "\n")
