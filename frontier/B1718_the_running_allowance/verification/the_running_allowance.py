"""B1718 (P-265): how far the within-sector mass ratios (m2/m3, m1/m3 per charged sector, the ratios every sealed test
since B1693 compares) run between M_Z and a high scale, in the SM at one loop.  Three generations of diagonal Yukawas
(mixing neglected in the running), y = sqrt(2) m / v at M_Z from the pinned Huang-Zhou 2021 masses (B1637's file);
gauge couplings at M_Z standard values, quoted (g1 GUT-normalised); a sensitivity check moves each gauge coupling by 3%.
QCD and every flavour-universal term cancel in a within-sector ratio; the Yukawa matrix term is what is left.
    python3 -B the_running_allowance.py      # writes the_running_allowance.json beside itself"""
import hashlib, json, math, pathlib
import numpy as np
from scipy.integrate import solve_ivp
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
assert hashlib.sha256(DATA.read_bytes()).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
m = json.loads(DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]
MZ, V = 91.1876, 246.22
Y0 = {"u": [math.sqrt(2) * m[q] / V for q in ("u", "c", "t")], "d": [math.sqrt(2) * m[q] / V for q in ("d", "s", "b")],
      "e": [math.sqrt(2) * m[q] / V for q in ("e", "mu", "tau")]}
G0 = [math.sqrt(5 / 3) * 0.3575, 0.6517, 1.2104]; B = [41 / 10, -19 / 6, -7]
def rhs(t, v):
    g1, g2, g3 = v[0:3]; u, d, e = v[3:6], v[6:9], v[9:12]; k = 1 / (16 * math.pi ** 2)
    T = 3 * sum(x * x for x in u) + 3 * sum(x * x for x in d) + sum(x * x for x in e)
    gu = 17 / 20 * g1 ** 2 + 9 / 4 * g2 ** 2 + 8 * g3 ** 2; gd = 1 / 4 * g1 ** 2 + 9 / 4 * g2 ** 2 + 8 * g3 ** 2; ge = 9 / 4 * g1 ** 2 + 9 / 4 * g2 ** 2
    return ([k * B[i] * v[i] ** 3 for i in range(3)] + [k * u[i] * (1.5 * (u[i] ** 2 - d[i] ** 2) + T - gu) for i in range(3)]
            + [k * d[i] * (1.5 * (d[i] ** 2 - u[i] ** 2) + T - gd) for i in range(3)] + [k * e[i] * (1.5 * e[i] ** 2 + T - ge) for i in range(3)])
NAMES = {"u": ("c/t", "u/t"), "d": ("s/b", "d/b"), "e": ("mu/tau", "e/tau")}
def factors(L, g0):
    v0 = list(g0) + Y0["u"] + Y0["d"] + Y0["e"]
    s = solve_ivp(rhs, [0, math.log(L / MZ)], v0, rtol=1e-10, atol=1e-14); v = s.y[:, -1]
    out = {}
    for off, sec in ((3, "u"), (6, "d"), (9, "e")):
        y1, y0 = v[off:off + 3], v0[off:off + 3]
        out[NAMES[sec][0]] = (y1[1] / y1[2]) / (y0[1] / y0[2]); out[NAMES[sec][1]] = (y1[0] / y1[2]) / (y0[0] / y0[2])
    return out, float(v[5])
OUT = {"inputs": {"y_MZ": Y0, "g_MZ": G0, "v": V}, "scales": {}}
for L in (1e4, 1e8, 1e12, 1e16, 1e18):
    f, yt = factors(L, G0)
    sens = 0.0
    for i in range(3):
        for s in (0.97, 1.03):
            g = list(G0); g[i] *= s; f2, _ = factors(L, g); sens = max(sens, max(abs(math.log(f2[k] / f[k])) for k in f))
    OUT["scales"]["%.0e" % L] = {"y_t": yt, "factors": f, "largest_abs_log": max(abs(math.log(x)) for x in f.values()), "sensitivity_3pc_gauge": sens}
OUT["largest_abs_log_to_1e16"] = OUT["scales"]["1e+16"]["largest_abs_log"]; OUT["largest_abs_log_to_1e18"] = OUT["scales"]["1e+18"]["largest_abs_log"]
OUT["allowance_0.10_covers_up_to"] = max((L for L in OUT["scales"] if OUT["scales"][L]["largest_abs_log"] <= math.log(1.10) + 1e-12), key=float, default=None)
if __name__ == "__main__":
    json.dump(OUT, open(HERE / "the_running_allowance.json", "w"), indent=1)
    for L, r in OUT["scales"].items():
        print(L, "y_t %.3f" % r["y_t"], " ".join("%s %.3f" % kv for kv in r["factors"].items()), "| max|log| %.3f | sensitivity %.4f" % (r["largest_abs_log"], r["sensitivity_3pc_gauge"]))
    print("a 10% allowance covers the running up to", OUT["allowance_0.10_covers_up_to"], "GeV")
