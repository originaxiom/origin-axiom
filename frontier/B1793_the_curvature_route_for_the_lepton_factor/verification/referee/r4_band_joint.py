"""Band-wide: on slope-2/5 lines (2/5, k/30) and (2/5, k/25), Re tau in {0.05, 0.3, 0.55, 0.85}, Im tau in {2.5, 3.0, 3.45}:
FREE common channel weights lam2_s (a superset of any metric on the pair kernel, any horocycle): max R2, max R1, and the joint
reach max_lam min(R2, R1) (random 3000 + Nelder-Mead from the 5 best).  c = 3 needs R2 ~ 3 AND R1 ~ 3."""
import sys, os, math, json, numpy as np
from fractions import Fraction as Fr
from multiprocessing import Pool
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

def cell(task):
    import ref_lib as RL
    from scipy.optimize import minimize
    a, b, re_t, im = task; B = RL.B; KEYS = list(B.UNITS); rng = np.random.default_rng(hash((str(b), re_t, im)) % 2**32)
    t = complex(re_t, im); S = RL.higgs_S(t); L = RL.L_of(im); sd = RL.sector_data(a, b, t); Rd, Rl = sd["down"][2], sd["lep"][2]
    x, y, _ = sd["down"]; c0, _ = RL.c_weighted(x, y, t, Rd, n=64)
    lam0 = {s: (2*math.pi*L + c0[s] if c0[s] is not None else 0.0) for s in KEYS}
    R20, R10, _ = RL.ratios_from_lam2(lam0, Rd, Rl, S)
    def f(ll):
        R2, R1, _ = RL.ratios_from_lam2(dict(zip(KEYS, np.exp(ll))), Rd, Rl, S); return R2, R1
    LL = rng.uniform(-7, 7, (3000, 4)); vals = np.array([f(l) for l in LL]); jm = np.minimum(vals[:, 0], vals[:, 1])
    best = []
    for i in np.argsort(-jm)[:5]:
        r = minimize(lambda l: -min(f(np.clip(l, -12, 12))), LL[i], method="Nelder-Mead", options=dict(maxiter=600, xatol=1e-4, fatol=1e-6))
        best.append((-r.fun, list(np.clip(r.x, -12, 12))))
    jbest = max(best)
    return dict(line=[str(a), str(b)], re=re_t, im=im, frame=[R20, R10], maxR2=float(vals[:, 0].max()), maxR1=float(vals[:, 1].max()),
                joint_rand=float(jm.max()), joint_opt=float(jbest[0]), joint_lam=[float(v) for v in np.exp(np.array(jbest[1]) - max(jbest[1]))],
                frac_both_ge2p5=float(((vals[:, 0] >= 2.5) & (vals[:, 1] >= 2.5)).mean()))

if __name__ == "__main__":
    bs = sorted({Fr(k, 30) for k in range(30)} | {Fr(k, 25) for k in range(25)})
    tasks = [(Fr(2, 5), b, r, i) for b in bs for r in (0.05, 0.3, 0.55, 0.85) for i in (2.5, 3.0, 3.45)]
    print("cells", len(tasks), flush=True)
    with Pool(4) as p: out = p.map(cell, tasks, chunksize=4)
    json.dump(out, open(__import__("pathlib").Path(__file__).resolve().parent / "r4_band_joint.json", "w"), indent=1)
    jo = np.array([o["joint_opt"] for o in out]); m2 = np.array([o["maxR2"] for o in out]); m1 = np.array([o["maxR1"] for o in out])
    print("joint reach max_lam min(R2,R1): quantiles 0/50/90/99/100%%: %s" % np.round(np.quantile(jo, [0, .5, .9, .99, 1]), 3))
    print("cells with joint reach >= 2.5: %d of %d; >= 2.0: %d" % ((jo >= 2.5).sum(), len(out), (jo >= 2.0).sum()))
    print("max R2 over free lam: quantiles %s ; max R1: %s" % (np.round(np.quantile(m2, [0, .5, .9, 1]), 3), np.round(np.quantile(m1, [0, .5, .9, 1]), 3)))
    for o in sorted(out, key=lambda o: -o["joint_opt"])[:8]:
        print("  top: line %s Re %.2f Im %.2f frame (%.3f, %.3f) joint %.3f lam/max %s frac_both>=2.5 %.4f" % (o["line"], o["re"], o["im"], *o["frame"], o["joint_opt"], np.round(o["joint_lam"], 4), o["frac_both_ge2p5"]))
