"""B1296 / T1+T2 -- THE SWAP THEOREM and THE LEVEL-CURVE LEMMA, checked on B1295's harmonic generator.

T1 (swap): the strong inversions sigma_1: z -> -z and sigma_2: z -> -z + tau/2 reverse the meridian
(B1294: L = 2 = 1 - s_mu), so the harmonic generator omega is sigma-ODD and its radial component
g = omega(d/dt) satisfies g(sigma z) = -g(z): sigma swaps d+M = {g > 0} and d-M = {g < 0}. With 0 a
regular value (B1295: two annuli at every height), chi(d+) = chi(d-) and chi(d+) + chi(d-) = chi(T^2) = 0,
so chi(d+M) = 0 WITHOUT any coefficient: the smooth-frame net chirality of the object's own Higgs is 0
for every theta-odd equivariant direction. The full D4 acts with s_mu(m) = alpha(m) (the sign of the
meridian), so g(m z) = alpha(m) g(z) for all eight isometries -- checked below.
T2 (level curve): a sigma-odd 1-form annihilates T Fix(sigma): at the four arc endpoints (the fixed
points of sigma on the cusp torus) g = omega(d/dt) = 0 -- the arcs are LEVEL curves of the Higgs
potential -- while the normal component omega(d/dx) = 1 + d_x psi does NOT vanish, so Fix(sigma) is not
a zero locus of the object's field: it is not a Pantev-Wijnholt charge locus of THIS Higgs."""
import json, sys, os
import numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve()
for p in [ROOT] + list(ROOT.parents):
    if (p / "frontier").is_dir(): ROOT = p; break
else:
    ROOT = Path(os.environ.get("OA_ROOT", "."))
V = ROOT / "frontier" / "B1295_the_caveat_closed_by_computation" / "verification"
sys.path.insert(0, str(V))
from harmonic_generator import Lattice, radial, psi_eval

gen = json.load(open(V / "harmonic_generator.json")); cc = json.load(open(V / "cusp_coefficient.json"))
tau = complex(*gen["tau"]); chiT = gen["chiT"]; lat = Lattice(tau, chiT)
c = {tuple(int(x) for x in k.split(",")): complex(*v) for k, v in cc["coefficients_final"].items()}
assert not any((-a, -b) in c for (a, b) in c), "half-mode convention violated"
print(f"lattice tau = {tau:.6f}, chiT = {chiT}; {len(c)} half-modes; max|Re c| = {max(abs(v.real) for v in c.values()):.2e}, max|Im c| = {max(abs(v.imag) for v in c.values()):.4f}")

iso = cc["isometries"]                         # z -> alpha * (conj? zbar : z) + beta_x + beta_y_over_tau * tau
def act(m, z):
    w = np.conj(z) if m["conj"] else z
    return m["alpha"] * w + m["beta_x"] + m["beta_y_over_tau"] * tau
def g(z, t): return radial(lat, c, z, t)
rng = np.random.default_rng(1296)
pts = [(complex(rng.uniform(0, 1), rng.uniform(0, tau.imag)), t) for t in (0.6, 1.0, 1.6, 2.4) for _ in range(40)]
gmax = max(abs(g(z, t)) for z, t in pts)
out = {"tau": gen["tau"], "n_half_modes": len(c), "gmax_on_sample": gmax, "isometries": []}
print("\n[T1] g(m z, t) = alpha(m) g(z, t) for the eight cusp actions (alpha = the meridian sign s_mu):")
worst = 0.0
for m in iso:
    dev = max(abs(g(act(m, z), t) - m["alpha"] * g(z, t)) for z, t in pts) / gmax
    kind = {(1, False): "translation / identity", (1, True): "glide (conj)", (-1, False): "STRONG INVERSION", (-1, True): "rotatory reflection (order 4)"}[(m["alpha"], m["conj"])]
    print(f"     alpha {m['alpha']:+d} conj {str(m['conj']):5} beta = {m['beta_x']} + {m['beta_y_over_tau']} tau  [{kind:30}]  rel. deviation {dev:.2e}")
    out["isometries"].append({**m, "kind": kind, "rel_deviation": dev}); worst = max(worst, dev)
out["equivariance_worst_rel_deviation"] = worst
assert worst < 1e-8, worst
xs = np.linspace(0, 1, 60, endpoint=False); ys = np.linspace(0, tau.imag, 60, endpoint=False)
G = np.array([[g(complex(x, y), 1.0) for x in xs] for y in ys])
Gm = np.array([[g(-complex(x, y), 1.0) for x in xs] for y in ys])
nz = np.abs(G) > 1e-9 * gmax                     # away from the zero set (which contains the fixed points, where g == 0 exactly)
swap_ok = bool(np.all(np.sign(G[nz]) == -np.sign(Gm[nz])))
print(f"     grid 60x60 at t = 1: sign(g(-z)) == -sign(g(z)) at all {int(nz.sum())} points off the zero set: {swap_ok}  (sigma_1 maps d+M onto d-M)")
assert swap_ok
out["swap_on_grid"] = swap_ok

print("\n[T2] the arc endpoints = the fixed points of the strong inversions on the cusp:")
endpoints = []
for m in iso:
    if m["alpha"] == -1 and not m["conj"]:
        beta = m["beta_x"] + m["beta_y_over_tau"] * tau
        for a in (0, 0.5):
            for b in (0, 0.5):
                endpoints.append((m, beta / 2 + a + b * tau))         # -z + beta = z mod Lambda <=> z = beta/2 + (2-torsion)
h = 1e-6
rows = []
for m, z0 in endpoints:
    for t in (0.7, 1.0, 1.5):
        gt = g(z0, t)
        wx = 1.0 + (psi_eval(lat, c, z0 + h, t) - psi_eval(lat, c, z0 - h, t)) / (2 * h)       # omega(d/dx) = d_x phi_lin + d_x psi, d_x phi_lin = 1
        wy = chiT / tau.imag + (psi_eval(lat, c, z0 + 1j * h, t) - psi_eval(lat, c, z0 - 1j * h, t)) / (2 * h)
        rows.append({"sigma_beta_y_over_tau": m["beta_y_over_tau"], "z": [z0.real, z0.imag], "t": t, "g_tangential": gt, "omega_dx": wx, "omega_dy": wy})
maxg = max(abs(r["g_tangential"]) for r in rows); minwx = min(abs(r["omega_dx"]) for r in rows)
for r in rows[::3]:
    print(f"     sigma(beta={r['sigma_beta_y_over_tau']} tau) endpoint z = {r['z'][0]:.3f} + {r['z'][1]:.3f} i, t = {r['t']}: "
          f"g = omega(d_t) = {r['g_tangential']:+.2e}   omega(d_x) = {r['omega_dx']:+.6f}   omega(d_y) = {r['omega_dy']:+.5f}")
print(f"     over all 8 endpoints x 3 heights: max|g| = {maxg:.2e} (tangential component VANISHES); min|omega(d_x)| = {minwx:.6f} (the form does NOT vanish)")
out["endpoints"] = rows; out["endpoint_max_abs_g"] = maxg; out["endpoint_min_abs_omega_dx"] = minwx
assert maxg < 1e-8 * gmax and minwx > 0.5     # the normal component is O(1) on both endpoint orbits (1.28 / 0.72)
def close(a, b):
    d = a - b; n = lat.coords(d); return abs(n[0] - round(n[0])) < 1e-9 and abs(n[1] - round(n[1])) < 1e-9
stab = {}
for m0, z0 in endpoints:
    s = [i for i, m in enumerate(iso) if close(act(m, z0), z0)]
    stab.setdefault(len(s), 0); stab[len(s)] += 1
print(f"\n[T4] stabiliser sizes of the 8 endpoints under the 8 cusp actions: {stab}  (2 = {{identity, its own strong inversion}} only)")
out["endpoint_stabiliser_sizes"] = stab
assert stab == {2: 8}
# T4b: the ORBITS of the endpoints under the full cusp group, and fc's arc pairing (B1294 section B: 0<->tau/2, 1/2<->1/2+tau/2).
# If the two arcs of one strong inversion lay in one orbit, a symmetry would relate their signs; they do not.
orb = []
for m0, z0 in endpoints:
    images = [act(m, z0) for m in iso]
    o = frozenset(i for i, (_, z1) in enumerate(endpoints) if any(close(z1, w) for w in images))
    if o not in orb: orb.append(o)
sizes = sorted(len(o) for o in orb)
def idx(z): return next(i for i, (_, z1) in enumerate(endpoints) if close(z1, z))
arcs_sigma1 = [(idx(0), idx(tau / 2)), (idx(0.5), idx(0.5 + tau / 2))]           # fc's pairing for sigma_1 (beta = 0)
same_orbit = [any({a, b} <= o for o in orb) for a, b in arcs_sigma1]
cross = [any(a in o and c in o for o in orb) for (a, b) in arcs_sigma1[:1] for (c, d) in arcs_sigma1[1:]]
print(f"     [T4b] endpoint orbits under the 8 actions: sizes {sizes}; each arc of sigma_1 has both endpoints in one orbit: {same_orbit}; "
      f"the two arcs of sigma_1 lie in the SAME orbit: {cross[0]}  -> no symmetry relates the two arcs' signs (the sign pair is the closer's)")
out["endpoint_orbits"] = {"sizes": sizes, "arc_endpoints_same_orbit": same_orbit, "two_arcs_same_orbit": cross[0]}
assert sizes == [4, 4] and all(same_orbit) and not cross[0]
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "swap_and_level.json", "w"), indent=1)
print("\nVERDICT: T1 SWAP holds (D4-equivariant, sigma swaps d+ and d-); T2 LEVEL-CURVE holds (g = 0, omega(d_x) in {1.28, 0.72} != 0 at every arc endpoint); T4 no second stabiliser.")
print("SELFTEST: PASS")
