"""Step 5 (data-free), the second method: the volume measure on the circle sampled through SnapPy's own ideal
tetrahedra (developed by SnapPy's fundamental-polyhedron engine), not through the Ford domain. Each tetrahedron is
sampled exactly (one vertex sent to infinity; the prism over the other three above their hemisphere; Dirichlet(1/2)
barycentrics against the 1/h^2 corner singularity), its points pulled back and theta = phi mod 1 read.
Checks: each tetrahedron's Monte Carlo volume against Bloch-Wigner D(z) of SnapPy's shape; the frame match of SnapPy's
engine and the collocation frame on every original generator.
usage: step5_tets.py NAME RCUT Y NPTS DEPTH NSAMP  (reuses step3's solver settings)"""
import sys, os, json, cmath, math, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from oa_harm import Group, solve, apply_m
import snappy
from snappy.snap import fundamental_polyhedron as fp

name = sys.argv[1]; Rcut = float(sys.argv[2]); Y = float(sys.argv[3]); npts = int(sys.argv[4]); depth = int(sys.argv[5])
NS = int(sys.argv[6])
t0 = time.time()
G = Group(name, rmin=0.8 * Y * 0.9, depth=depth); lat = G.lat
H1, info = solve(G, Y, Rcut, npts, seed=1)
print(f"{name}: solve resid_rms {info['resid_rms']:.2e} rank {info['rank']}/{info['n_unknown']}  {time.time()-t0:.0f}s", flush=True)

# the tube: theta on the shortest geodesic's axis (chi = 0 there, so theta is single-valued along it)
from step4_tube import shortest_loxodromic, axis_points
X, L, cx = shortest_loxodromic(G, depth=6)
pts, _ = axis_points(X, n=96)
tax = []
for zq, tq in pts:
    zs, ts, _ = G.pullback(zq, tq)
    tax.append(H1.phi([zs], [ts])[0] % 1.0)
tax = np.array(tax); tube_theta = float(np.angle(np.mean(np.exp(2j * math.pi * tax))) / (2 * math.pi) % 1)
spread = np.max(np.abs(((tax - tube_theta + 0.5) % 1) - 0.5))
print(f"   shortest geodesic: length {L.real:.6f}{L.imag:+.6f}i chi {cx};  theta on its axis: circular mean {tube_theta:.4f}, "
      f"max deviation {spread:.2e} over 96 points", flush=True)

M = snappy.Manifold(name)
shapes = M.tetrahedra_shapes('rect')
E = fp.FundamentalPolyhedronEngine.from_manifold_and_shapes(M, shapes, normalize_matrices=True)
U = M.fundamental_group(simplify_presentation=False)
Gs = M.fundamental_group()
# frame check: the engine's matrices for the original generators vs the simplified group's SL2C of their words
emats = E.matrices_for_presentation(U)
worst = 0.0
for k, w in enumerate(Gs.original_generators()):
    A = np.array([[complex(emats[k][0, 0]), complex(emats[k][0, 1])], [complex(emats[k][1, 0]), complex(emats[k][1, 1])]])
    m = Gs.SL2C(w); B = np.array([[complex(m[0, 0]), complex(m[0, 1])], [complex(m[1, 0]), complex(m[1, 1])]])
    worst = max(worst, min(np.abs(A - B).max(), np.abs(A + B).max()))
print(f"   frame check (engine vs SL2C on {len(emats)} original generators): max deviation {worst:.2e}", flush=True)


def mob(Mx, v):
    a, b, c, d = Mx[0, 0], Mx[0, 1], Mx[1, 0], Mx[1, 1]
    if v is None:
        return None if abs(c) < 1e-14 else a / c
    den = c * v + d
    return None if abs(den) < 1e-14 else (a * v + b) / den


def bloch_wigner(z):
    import mpmath
    z = mpmath.mpc(z.real, z.imag)
    return float(mpmath.im(mpmath.polylog(2, z)) + mpmath.arg(1 - z) * mpmath.log(abs(z)))


rng = np.random.default_rng(23)
nb = 40
rho_t = np.zeros(nb); rows = []
for T in E.mcomplex.Tetrahedra:
    raw = []
    for key in (1, 2, 4, 8):
        v = T.SnapPeaIdealVertices[key]
        raw.append(None if str(v) == "Infinity" else complex(v))
    V = [mob(G.Fr, v) for v in raw]                       # into the collocation frame
    v0 = V[0]
    A = np.eye(2, dtype=complex) if v0 is None else np.array([[0, 1], [-1, v0]], dtype=complex)
    tri = [mob(A, v) for v in V[1:]]
    assert all(q is not None for q in tri)
    a_, b_, c_ = tri
    # circumcircle
    d = 2 * (a_.real * (b_.imag - c_.imag) + b_.real * (c_.imag - a_.imag) + c_.real * (a_.imag - b_.imag))
    ux = ((abs(a_)**2) * (b_.imag - c_.imag) + (abs(b_)**2) * (c_.imag - a_.imag) + (abs(c_)**2) * (a_.imag - b_.imag)) / d
    uy = ((abs(a_)**2) * (c_.real - b_.real) + (abs(b_)**2) * (a_.real - c_.real) + (abs(c_)**2) * (b_.real - a_.real)) / d
    ctr = complex(ux, uy); R = abs(a_ - ctr)
    area = abs(((b_ - a_).conjugate() * (c_ - a_)).imag) / 2
    lam = rng.dirichlet([0.5, 0.5, 0.5], NS)
    z = lam[:, 0] * a_ + lam[:, 1] * b_ + lam[:, 2] * c_
    h2 = np.maximum(R * R - np.abs(z - ctr) ** 2, 1e-300)
    pz = np.prod(lam, axis=1) ** -0.5 / (2 * math.pi * 2 * area)
    w = (1 / (2 * h2)) / pz
    u = rng.uniform(0, 1, NS); t = np.sqrt(h2) / np.sqrt(1 - u)
    Ai = np.linalg.inv(A)
    th = np.empty(NS)
    for k in range(NS):
        zz, tt = apply_m(Ai, z[k], t[k])
        zs, ts, _ = G.pullback(zz, tt)
        th[k] = H1.phi([zs], [ts])[0] % 1.0
    vol_mc = w.mean(); vol_err = w.std() / math.sqrt(NS)
    sh = complex(shapes[T.Index]); vol_bw = bloch_wigner(sh)
    hist, _ = np.histogram(th, bins=nb, range=(0, 1), weights=w / NS)
    rho_t += hist
    ang = np.angle(np.sum(w * np.exp(2j * math.pi * th)))
    conc = abs(np.sum(w * np.exp(2j * math.pi * th))) / np.sum(w)
    rows.append(dict(tet=T.Index, vol_mc=vol_mc, vol_err=vol_err, vol_bw=vol_bw, theta_circmean=(ang / (2 * math.pi)) % 1,
                     concentration=conc, hist=hist.tolist()))
    print(f"   tet {T.Index}: volume MC {vol_mc:.4f} +- {vol_err:.4f}  (Bloch-Wigner {vol_bw:.4f});  theta circular mean "
          f"{(ang/(2*math.pi))%1:.4f}, concentration |<e^(2 pi i theta)>| {conc:.3f}   {time.time()-t0:.0f}s", flush=True)
rho = rho_t / rho_t.mean()
print("   rho via tetrahedra:", " ".join(f"{v:.2f}" for v in rho))
json.dump(dict(name=name, tube_theta=tube_theta, tube_length=[L.real, L.imag], tube_chi=int(cx), tube_spread=float(spread), rows=rows, rho=rho.tolist(), frame_dev=worst, info=info),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"step5_{name}.json"), "w"), indent=1)
