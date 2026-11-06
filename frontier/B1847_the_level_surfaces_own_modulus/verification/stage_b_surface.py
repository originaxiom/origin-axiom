"""P-727 stage B scaffolding (data-free): on a member, (1) the fibre group's generators x, y (chi = 0) whose commutator is
the fibre's cusp translation, (2) the level surface {phi = s} through the cusp as a graph v(u, t) over the strip (u along
the fibre direction, t the height), by continuation down from the cusp, with phi evaluated anywhere by exact pullback.
Checks: the commutator equals the translation; phi(P(u,t)) = s on the surface; the fold test (d phi / d v != 0)."""
import sys, os, math, cmath, time, itertools, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "B1846_the_metrics_read_out", "verification"))
from oa_harm import Group, solve, apply_m, chi_word


def setup(name, Rcut, Y, npts, depth):
    import pickle
    cf = os.path.join(HERE, "cache", f"setup_{name}_{Rcut}_{Y}_{npts}_{depth}.pkl")
    if os.path.exists(cf):
        G, H, info = pickle.load(open(cf, "rb"))
    else:
        G = Group(name, rmin=0.8 * Y * 0.9, depth=depth)
        H, info = solve(G, Y, Rcut, npts, seed=1)
        os.makedirs(os.path.dirname(cf), exist_ok=True)
        pickle.dump((G, H, info), open(cf, "wb"))
    lat = G.lat
    if lat.c1 == 0:
        wf, cf = lat.w1, lat.c2
    elif lat.c2 == 0:
        wf, cf = lat.w2, lat.c1
    else:
        raise ValueError("no chi = 0 cusp direction")
    return G, H, info, wf


def phi_any(G, H, z, t):
    zs, ts, chi = G.pullback(z, t)
    return float(H.phi([zs], [ts])[0]) - chi


def fibre_generators(G, wf, maxlen=5):
    """Short chi = 0 words x, y with [x, y] = +- the translation by +- wf (exactly, as matrices up to sign)."""
    letters = []
    for g in G.gens:
        letters += [g, g.upper()]
    cands = []
    for L in range(1, maxlen + 1):
        for tup in itertools.product(letters, repeat=L):
            w = "".join(tup)
            if any(a == b.swapcase() for a, b in zip(w, w[1:])):
                continue
            if chi_word(G.chi, w) != 0:
                continue
            cands.append(w)
        if len(cands) > 400:
            break
    mats = {w: G.wmat(w) for w in cands}
    for wx, wy in itertools.combinations(cands[:200], 2):
        X, Yy = mats[wx], mats[wy]
        K = X @ Yy @ np.linalg.inv(X) @ np.linalg.inv(Yy)
        if abs(K[1, 0]) < 1e-8 and abs(abs(K[0, 0]) - 1) < 1e-8:
            tr = K[0, 1] / K[1, 1]
            if abs(abs(tr) - abs(wf)) < 1e-7 and abs((tr / wf).imag) < 1e-7:
                return wx, wy, complex(tr)
    return None


def surface_graph(G, H, wf, s, us, ts, v0=None):
    """v(u, t) on the level phi = s, by continuation downward in t at each u; returns V (len(us) x len(ts)), fold flags."""
    e = wf / abs(wf); nu = 1j * e
    lat = G.lat
    # phi_lin's slope along nu
    g = lat.phi_lin(nu) - lat.phi_lin(0)
    vs = s / g
    V = np.full((len(us), len(ts)), np.nan); dphi = np.full((len(us), len(ts)), np.nan)
    for i, u in enumerate(us):
        v = vs if v0 is None else v0
        for j, t in enumerate(ts):          # ts descending
            for _ in range(30):
                f0 = phi_any(G, H, u * e + v * nu, t) - s
                h = 1e-6
                f1 = phi_any(G, H, u * e + (v + h) * nu, t) - s
                d = (f1 - f0) / h
                if abs(d) < 1e-12:
                    break
                step = -f0 / d
                step = max(-0.2, min(0.2, step))
                v += step
                if abs(step) < 1e-11:
                    break
            V[i, j] = v; dphi[i, j] = d
    return V, dphi


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "m004"
    t0 = time.time()
    if name == "m004":
        G, H, info, wf = setup("m004", 6, 0.55, 900, 6)
    else:
        G, H, info, wf = setup(name, 10, 0.33, 6724, 7)
    print(f"{name}: solve resid {info['resid_rms']:.1e}; fibre direction wf = {wf:.6f} (|wf| {abs(wf):.6f}); {time.time()-t0:.0f}s", flush=True)
    fg = fibre_generators(G, wf)
    print(f"   fibre generators (x, y) with [x, y] = translation: {fg}", flush=True)
    us = np.linspace(-abs(wf) / 2, abs(wf) / 2, 9)
    ts = np.exp(np.linspace(math.log(4.0), math.log(0.3), 40))
    V, D = surface_graph(G, H, wf, 0.0, us, ts)
    print(f"   level s = 0: v(u, t) range {np.nanmin(V):+.4f}..{np.nanmax(V):+.4f}; min |d phi/d v| {np.nanmin(np.abs(D)):.3e}; "
          f"{time.time()-t0:.0f}s", flush=True)
    for i in (0, 4, 8):
        print("   u = %+.3f: v at t = 4, 1, 0.5, 0.3:" % us[i], [round(V[i, j], 4) for j in (0, 17, 30, 39)])
