"""B1854 (P-739; data-free): the tube's tau on b++L^6R(LR)^k with B1847's own full-group mesher (stage_e_gamma.main),
one Hejhal setup per member shared by every run (the setup is the cost: ~13 GB, tens of minutes; one heavy job at a time).
The core level s0 = phi(core) mod 1 is found first (core_gradient.py's method); the mesher then runs at s0 + d for each
d below, each run's printout written to runs/k<k>_s<s>_N<N>.txt exactly as B1847's gamma_runs/ files.
Usage: tube_driver.py k [N1 N2 [d1,d2,...]]  (the control: k = 1 at d = 0.001 must reproduce B1847's gamma_lim2_s0.001.txt)"""
import sys, os, io, contextlib, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")   # verification -> the arc -> frontier -> the root
B1847 = os.path.join(ROOT, "frontier", "B1847_the_level_surfaces_own_modulus", "verification")
sys.path.insert(0, os.path.join(ROOT, "frontier", "B1854_the_tubes_tau_beyond_k1_on_main", "verification")); sys.path.insert(0, B1847); sys.path.insert(0, os.path.join(ROOT, "frontier", "B1846_the_metrics_read_out", "verification")); sys.path.insert(0, HERE)
import stage_e_gamma_k3 as SE   # the copy with the basis taken from the words (P-739)
from stage_b_modulus import reduce_tau
from step4_tube import shortest_loxodromic, axis_points
from fastpull import pullback_batch
k = int(sys.argv[1]); N1 = int(sys.argv[2]) if len(sys.argv) > 2 else 120; N2 = int(sys.argv[3]) if len(sys.argv) > 3 else 90
word = "b++LLLLLLR" + "LR" * k
t0 = time.time()
cache = SE.setup(word, 12, 0.33, 9604, 7)
SE.setup = lambda *a, **kw: cache                      # every run below reuses this one setup
G, H, info, wf = cache
X, Lc, cx = shortest_loxodromic(G, depth=6)
pts, ends = axis_points(X, n=200)
Z = np.array([p[0] for p in pts]); T = np.array([p[1] for p in pts])
Zs, Ts, Cs = pullback_batch(G, Z, T)
phi = H.phi(Zs, Ts) - Cs
s0 = float(np.mod(np.median(phi), 1.0))
gx, gy, gt = H.grad(Zs, Ts); g = Ts * np.sqrt(gx ** 2 + gy ** 2 + gt ** 2)
os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
with open(os.path.join(HERE, "runs", "k%d_core.txt" % k), "w") as f:
    f.write("%s: setup %.0fs; core length %.8f; s0 = %.6f (spread %.1e); |d theta| on the core %.6f..%.6f\n"
            % (word, time.time() - t0, Lc.real, s0, np.ptp(np.mod(phi - s0 + 0.5, 1.0)), g.min(), g.max()))
print(open(os.path.join(HERE, "runs", "k%d_core.txt" % k)).read(), flush=True)
DS = [float(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else [0.002, 0.001, 0.0005, -0.001, -0.002, 0.005]
for d in DS:
    s = round(s0 + d, 6)
    buf = io.StringIO()
    t1 = time.time()
    try:
        with contextlib.redirect_stdout(buf):
            Dm = SE.main(word, s, N1, N2, N2)
            tau, info = SE.finish(Dm)                    # B1847's command line: main, then finish, then reduce
            tr = reduce_tau(tau)
            print(f"   tau {tau.real:+.6f}{tau.imag:+.6f}i  reduced {tr.real:+.6f}{tr.imag:+.6f}i  detE-1 {info['detE']-1:+.2e}  {info}", flush=True)
            # the covariant root (row 1614; B1847's dated note): tau_cov = Re tau + i Im tau sqrt(det E), then reduced
            tc = reduce_tau(complex(tau.real, tau.imag * np.sqrt(info["detE"])))
            print(f"   covariant root: reduced {tc.real:+.6f}{tc.imag:+.6f}i", flush=True)
    except Exception as e:
        import traceback
        buf.write("FAILED: %r\n" % (e,)); buf.write(traceback.format_exc())
    out = buf.getvalue() + "   [run %.0fs]\n" % (time.time() - t1)
    with open(os.path.join(HERE, "runs", "k%d_s%.6f_N%d.txt" % (k, s, N1)), "w") as f:
        f.write(out)
    print("k=%d s=%.6f (d=%+.4f): %s" % (k, s, d, [l.strip()[:90] for l in out.splitlines() if "reduced" in l][-2:] or out.splitlines()[-2:]), flush=True)
