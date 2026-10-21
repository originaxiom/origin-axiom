"""B1699 (P-247): this frame's own coupling strength against tau.  No data.  B1645's covariant coupling
Y(a) = a R^T + R a^T - (a.R) 1 (R the theta triplet, weight -1/2); the Higgs a = DR (weight 3/2, so Y has weight 1) or
the unit-free a0 = D2R - E4 R/48 (weight 7/2, Y weight 3; B1697).  The invariant strength: y^k s1^2 (the top Yukawa's
Petersson-normalised strength) and y^k |Y|_F^2, k = Y's weight.  Computed: the invariance under tau -> -1/tau, tau + 1
and -conj(tau); the strength on Re tau = 0 and 1/2 (y up to 5); dS/dy on a grid of the fundamental domain; the strength
on the arc |tau| = 1 between i and omega, its critical points there and their kind; the selected tau (P-247's rule:
the critical points of y s1^2 for DR other than i and omega), refined by bisection.
    python3 -B the_strength.py [--workers 8]      # writes the_strength.json beside itself"""
import sys, io, json, math, contextlib, importlib.util, pathlib
import numpy as np, mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
P = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(P))
spec = importlib.util.spec_from_file_location("te", P / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
mp.mp.dps = 30
def E4(t):
    q = mp.exp(2j * mp.pi * t); return 1 + 240 * mp.fsum(n**3 * q**n / (1 - q**n) for n in range(1, 60))
def vecs(t):
    R = np.array([complex(te.ev(c, t)) for c in te.B[0]]); D1 = np.array([complex(te.ev(c, t)) for c in te.B[1]])
    D2 = np.array([complex(te.ev(c, t)) for c in te.B[2]]); return R, D1, D2 - complex(E4(t)) * R / 48
def Y(a, R): return np.outer(a, R) + np.outer(R, a) - (a @ R) * np.eye(3)
def strengths(t):
    t = mp.mpc(t); y = float(mp.im(t)); R, d1, a0 = vecs(t); out = {}
    for name, a, k in (("DR", d1, 1.0), ("a0", a0, 3.0)):
        sv = np.linalg.svd(Y(a, R), compute_uv=False)
        out[name] = {"top": y**k * sv[0]**2, "frob": y**k * float(np.sum(sv**2))}
    return out
def top_DR(t): return strengths(t)["DR"]["top"]
def on_arc(th): return complex(math.cos(th), math.sin(th))
def dS_dtheta(th, h=1e-5): return (top_DR(on_arc(th + h)) - top_DR(on_arc(th - h))) / (2 * h)
def grid_task(p):
    x, y = p; h = 1e-4
    up, dn = strengths(complex(x, y + h)), strengths(complex(x, y - h))
    here, refl = strengths(complex(x, y)), strengths(complex(-x, y))
    return {"x": x, "y": y, "dy": {k: (up[k]["top"] - dn[k]["top"]) / (2 * h) for k in up},
            "refl": max(abs(here[k][m] / refl[k][m] - 1) for k in here for m in ("top", "frob"))}
if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    out = {}
    rng = np.random.default_rng(1699); inv = 0.0
    for _ in range(5):
        t = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 2.0)); a = strengths(t)
        for b in (strengths(-1 / t), strengths(t + 1)):
            inv = max(inv, max(abs(a[h][m] / b[h][m] - 1) for h in a for m in ("top", "frob")))
    out["invariance_max_rel_dev"] = inv
    lines = {}
    for re_t in (0.0, 0.5):
        ys = np.round(np.arange(1.0 if re_t == 0 else 0.87, 5.0001, 0.01), 4); rows = [strengths(complex(re_t, y)) for y in ys]
        for h in ("DR", "a0"):
            for m in ("top", "frob"):
                v = np.array([r[h][m] for r in rows]); dv = np.diff(v)
                lines["%s|%s|%s" % (re_t, h, m)] = {"critical_y": [float(ys[i + 1]) for i in range(len(dv) - 1) if dv[i] * dv[i + 1] < 0],
                                                    "monotone_increasing": bool(np.all(dv > 0)), "at_y_min": float(v[0]), "at_y_5": float(v[-1])}
    out["symmetry_lines"] = lines
    pts = [(round(x, 3), round(y, 3)) for x in np.arange(-0.5, 0.5001, 0.05) for y in np.arange(0.88, 5.0001, 0.04) if x * x + y * y >= 1.0 + 1e-3]
    with Pool(nw) as Pl: g = Pl.map(grid_task, pts, chunksize=8)
    out["grid"] = {"points": len(g), "reflection_max_rel_dev": max(r["refl"] for r in g)}
    for k in ("DR", "a0"):
        nonpos = [(r["x"], r["y"]) for r in g if r["dy"][k] <= 0]
        out["grid"][k] = {"dS_dy_nonpositive_at": nonpos, "min_dS_dy": min(r["dy"][k] for r in g),
                          "nonpositive_within_0.05_of_the_arc": all(abs(math.hypot(x, y) - 1) < 0.05 for x, y in nonpos)}
    th = np.linspace(math.pi / 2, 2 * math.pi / 3, 241); rows = [strengths(on_arc(t)) for t in th]; arc = {}
    for h in ("DR", "a0"):
        for m in ("top", "frob"):
            v = np.array([r[h][m] for r in rows]); dv = np.diff(v)
            arc["%s|%s" % (h, m)] = {"at_i": float(v[0]), "at_omega": float(v[-1]),
                                     "critical_theta_over_pi": [round(float(th[i + 1]) / math.pi, 4) for i in range(len(dv) - 1) if dv[i] * dv[i + 1] < 0]}
    out["arc"] = arc
    lo, hi = 0.58 * math.pi, 0.60 * math.pi
    assert dS_dtheta(lo) * dS_dtheta(hi) < 0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if dS_dtheta(lo) * dS_dtheta(mid) <= 0: hi = mid
        else: lo = mid
    ths = 0.5 * (lo + hi); ts = on_arc(ths); h = 1e-3
    tau_sel = complex(-ts.real, ts.imag)                      # the mirror image, Re tau > 0 (the strength is reflection-invariant)
    out["selected"] = {"theta_over_pi": ths / math.pi, "tau": [tau_sel.real, tau_sel.imag], "strength": top_DR(ts),
                       "second_difference_along_arc": top_DR(on_arc(ths + h)) + top_DR(on_arc(ths - h)) - 2 * top_DR(ts),
                       "second_difference_normal": top_DR(ts * (1 + h)) + top_DR(ts * (1 - h)) - 2 * top_DR(ts)}
    out["selected"]["kind"] = "saddle" if out["selected"]["second_difference_along_arc"] < 0 < out["selected"]["second_difference_normal"] else "other"
    json.dump(out, open(HERE / "the_strength.json", "w"), indent=1)
    print("selected tau %.6f%+.6fi (%s); strength %.6g" % (tau_sel.real, tau_sel.imag, out["selected"]["kind"], out["selected"]["strength"]))
