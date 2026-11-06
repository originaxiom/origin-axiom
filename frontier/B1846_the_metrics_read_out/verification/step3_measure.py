"""Step 3 (data-free): the harmonic generator phi by collocation on a member, its integrity checks, and the two
metric-native measures on the fibration circle s = phi mod 1:
  E(s) -- the energy density pushed forward (THEOREM: uniform up to exp-small terms, by coarea + d*dphi = 0);
  rho(s) -- the volume density pushed forward (the one that can localise).
Checks: |c_(0,2)| = 4.260982635 on m004 (B1295, the known answer); the generator relations phi(g P) - phi(P) = chi(g);
a second collocation height; the domain's Monte Carlo volume against SnapPy's; E(s) flat.
usage: step3_measure.py NAME RCUT Y NPTS [DEPTH]"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from oa_harm import Group, solve, apply_m

name = sys.argv[1]; Rcut = float(sys.argv[2]); Y = float(sys.argv[3]); npts = int(sys.argv[4])
depth = int(sys.argv[5]) if len(sys.argv) > 5 else 7
t0 = time.time()
G = Group(name, rmin=0.8 * min(Y * 0.9, float(os.environ.get('OA_TLO', '1'))), depth=depth)
lat = G.lat
# keep only sphere translates that can meet the prism over the central cell (speed; the cell's circumradius + radius)
corners = [(x * lat.w1 + y * lat.w2) for x in (-.5, .5) for y in (-.5, .5)]
Rcell = max(abs(c) for c in corners)
a, b, c, d = G.MA.T
ctr = -d / c; rad = 1 / np.abs(c)
keep = np.abs(ctr) <= Rcell + rad + 1e-9
G.MA = G.MA[keep]; G.MC = G.MC[keep]
print(f"{name}: lattice w1 {lat.w1:.6f} w2 {lat.w2:.6f} chi ({lat.c1},{lat.c2}); sphere translates kept {keep.sum()} of {len(keep)}; {time.time()-t0:.1f}s", flush=True)

# the floor, deterministically
fl = []
for i in range(30):
    for j in range(30):
        _, ts, _ = G.pullback(((i + .5) / 30 - .5) * lat.w1 + ((j + .5) / 30 - .5) * lat.w2, 0.005)
        fl.append(ts)
floor = min(fl)
print(f"   domain floor (min pulled-back height of a 30x30 grid at t = 0.005): {floor:.5f}", flush=True)

H1, info1 = solve(G, Y, Rcut, npts, seed=1)
print("   solve at Y:", json.dumps(info1), f"{time.time()-t0:.1f}s", flush=True)
H2, info2 = solve(G, Y * 0.9, Rcut, npts, seed=2)
print("   solve at 0.9 Y:", json.dumps(info2), flush=True)

# the known answer on m004
control = None
if name == "m004":
    for (m1, m2, mu), cm in zip(H1.modes, H1.coef):
        if (m1, m2) == (0, 2):
            print(f"   CONTROL m004 |c_(0,2)| = {abs(cm):.9f}  (B1295: 4.260982635)"); control = abs(cm)

# equivariance phi(M P) - phi(P) = chi(M) on the face-pairing elements, at points ON M's isometric sphere (M is a
# Euclidean isometry there, so P and M P have the same height, which is kept above Y where the series is valid);
# plus the generators themselves wherever a random P and its image both sit above Y (no infinite rejection loop)
rng = np.random.default_rng(11)
dev = {}
a_, b_, c_, d_ = G.MA.T
big = np.where(1 / np.abs(c_) > Y * 1.05)[0]
worst = 0.0; nchk = 0
for jj in big[:: max(1, len(big) // 60)]:
    Mx = np.array([[a_[jj], b_[jj]], [c_[jj], d_[jj]]]); r = 1 / abs(c_[jj]); ctr = -d_[jj] / c_[jj]
    for _ in range(3):
        tq = rng.uniform(Y * 1.02, r * 0.98); ang = rng.uniform(0, 2 * np.pi)
        zq = ctr + np.sqrt(r * r - tq * tq) * np.exp(1j * ang)
        zb, tb = apply_m(Mx, zq, tq)
        worst = max(worst, abs(H1.phi([zb], [tb])[0] - H1.phi([zq], [tq])[0] - G.MC[jj])); nchk += 1
dev["face pairings"] = worst
for g in G.gens:
    Mx = G.H[g]; w = 0.0; n = 0; tries = 0
    while n < 100 and tries < 200000:
        tries += 1
        x, y = rng.uniform(-.5, .5, 2); zq = x * lat.w1 + y * lat.w2; tq = rng.uniform(Y, 1.5)
        zb, tb = apply_m(Mx, zq, tq)
        if tb < Y:
            continue
        n += 1
        w = max(w, abs(H1.phi([zb], [tb])[0] - H1.phi([zq], [tq])[0] - G.chi[g]))
    dev[g] = (w if n else None, n)
print(f"   equivariance max |phi(M P) - phi(P) - chi(M)|: face pairings {dev['face pairings']:.2e} ({nchk} points); generators "
      + ", ".join(f"{g}: {v[0]:.2e} ({v[1]} pts)" if v[0] is not None else f"{g}: none above Y" for g, v in dev.items() if g != "face pairings"), flush=True)

# sample the Ford domain with hyperbolic volume weight; the cusp above 1 sampled to T_cut, its tail is uniform in s
a, b, c, d = G.MA.T
def inside(z, t):
    out = np.ones(len(z), bool); ch = max(1, int(2e6 // len(c)))
    for k in range(0, len(z), ch):
        D = np.abs(c[None, :] * z[k:k+ch, None] + d[None, :]) ** 2 + np.abs(c[None, :]) ** 2 * t[k:k+ch, None] ** 2
        out[k:k+ch] = np.all(D >= 1 - 1e-12, axis=1)
    return out
tlo = float(os.environ.get('OA_TLO', 0.85 * floor)); Tcut = 5.0; N = int(os.environ.get("OA_NMC", "400000"))
x = rng.uniform(-.5, .5, N); y = rng.uniform(-.5, .5, N); z = x * lat.w1 + y * lat.w2
u = rng.uniform(0, 1, N); t = (tlo ** -2 - u * (tlo ** -2 - Tcut ** -2)) ** -0.5
ins = inside(z, t)
W = lat.covol * (tlo ** -2 - Tcut ** -2) / 2
vol_cut = W * ins.mean(); vol_tail = lat.covol / (2 * Tcut ** 2)
print(f"   domain volume {vol_cut + vol_tail:.4f} +- {W*np.sqrt(ins.mean()*(1-ins.mean())/N):.4f}  (SnapPy {G.vol:.6f})", flush=True)
zi, ti = z[ins], t[ins]
print(f"   lowest accepted sample height {ti.min():.5f} (sampling from tlo = {tlo:.5f}; must sit clearly above tlo)", flush=True)
phis = np.concatenate([H1.phi(zi[k:k+4000], ti[k:k+4000]) for k in range(0, len(zi), 4000)])
phis2 = np.concatenate([H2.phi(zi[k:k+4000], ti[k:k+4000]) for k in range(0, len(zi), 4000)])
gr = [H1.grad(zi[k:k+4000], ti[k:k+4000]) for k in range(0, len(zi), 4000)]
gx = np.concatenate([g[0] for g in gr]); gy = np.concatenate([g[1] for g in gr]); gt = np.concatenate([g[2] for g in gr])
e = ti ** 2 * (gx ** 2 + gy ** 2 + gt ** 2)                  # hyperbolic |d phi|^2
s = np.mod(phis, 1.0); s2 = np.mod(phis2, 1.0)
nb = 40
rho, _ = np.histogram(s, bins=nb, range=(0, 1)); rho2, _ = np.histogram(s2, bins=nb, range=(0, 1))
E, _ = np.histogram(s, bins=nb, range=(0, 1), weights=e)
E2, _ = np.histogram(s, bins=nb, range=(0, 1), weights=e * e)
cnt = rho.copy()
# per-bin standard errors (the sample is i.i.d. over the prism; a bin's total is a sum of i.i.d. weighted indicators)
Nall = len(z)
Ebar = E / Nall; Evar = (E2 / Nall - Ebar ** 2) / Nall
E_se_rel = np.sqrt(np.maximum(Evar, 0)) / np.maximum(Ebar, 1e-300)
chi2_E = float(np.sum(((E / E.mean() - 1) / np.maximum(E_se_rel * E / E.mean(), 1e-300)) ** 2))
rho_se_rel = 1 / np.sqrt(np.maximum(cnt, 1))
# the cusp tail above Tcut is uniform in s (phi = phi_lin + exp-small there): add it so rho is the full pushforward
rho = rho / len(s) * vol_cut + vol_tail / nb; rho2 = rho2 / len(s2) * vol_cut + vol_tail / nb
rho = rho / rho.mean(); rho2 = rho2 / rho2.mean(); E = E / E.mean()
print(f"   |phi_Y - phi_0.9Y| over the sample: max {np.abs(phis-phis2).max():.2e}, rms {np.sqrt(np.mean((phis-phis2)**2)):.2e}")
print(f"   E(s)/mean over {nb} bins: min {E.min():.3f} max {E.max():.3f}  (theorem: flat; MC noise ~ {1/np.sqrt(len(s)/nb):.3f} x spread)")
print(f"   rho(s)/mean over {nb} bins: min {rho.min():.3f} max {rho.max():.3f} at s = {(np.argmax(rho)+.5)/nb:.3f};  second height: max {rho2.max():.3f} at {(np.argmax(rho2)+.5)/nb:.3f}")
print(f"   E flatness: chi2 = {chi2_E:.1f} on {nb - 1} dof (per-bin relative s.e. median {np.median(E_se_rel):.3f}); "
      f"rho per-bin relative s.e. (sampled part) median {np.median(rho_se_rel):.3f}")
print("   rho profile:", " ".join(f"{v:.2f}" for v in rho))
print("   E profile:  ", " ".join(f"{v:.2f}" for v in E))
out = dict(name=name, control_c02=control, Rcut=Rcut, Y=Y, npts=npts, depth=depth, floor=floor, info1=info1, info2=info2, gen_dev=dev,
           volume=vol_cut + vol_tail, snappy_volume=G.vol, rho=rho.tolist(), rho2=rho2.tolist(), E=E.tolist(), E_se_rel=E_se_rel.tolist(), chi2_E=chi2_E, rho_se_rel=rho_se_rel.tolist(),
           n_sample=int(len(s)))
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"step3_{name}_R{Rcut:g}.json"), "w"), indent=1)
print(f"   done {time.time()-t0:.1f}s")
