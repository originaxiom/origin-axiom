"""Fold test (data-free): is the level surface {phi = s} a single-valued graph v(u, t) over the strip? At fixed (u, t),
scan v across a wide window and count the sign changes of phi - s (each is a sheet of the level set crossing the line)."""
import sys, os, math, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "B1846_the_metrics_read_out", "verification"))
from fastpull import pullback_batch
name, s = sys.argv[1], float(sys.argv[2])
G, H, info = pickle.load(open(os.path.join(HERE, "cache", sys.argv[3]), "rb"))
lat = G.lat
wf = lat.w1 if lat.c1 == 0 else lat.w2
L = abs(wf); e = wf / L; nu = 1j * e
g = lat.phi_lin(nu) - lat.phi_lin(0)
W = abs(1 / g)                       # one period of phi_lin across the strip's normal
vs = s / g + np.linspace(-W / 2, W / 2, 1601)        # one period centred on this level's own sheet
def phi(u, t):
    Z = u * e + vs * nu; T = np.full(len(Z), t)
    Zs, Ts, C = pullback_batch(G, Z, T)
    out = np.empty(len(Z))
    for k in range(0, len(Z), 4000):
        out[k:k + 4000] = H.phi(Zs[k:k + 4000], Ts[k:k + 4000])
    return out - C
print(f"{name}: one period of the transverse coordinate {W:.4f}; counting crossings of phi = s + n (any integer n) on lines of fixed (u, t)")
for t in (2.0, 1.0, 0.7, 0.5, 0.45, 0.42, 0.40, 0.38):
    counts = []
    for u in np.linspace(-L / 2, L / 2, 25)[:-1]:
        f = phi(u, t) - s
        frac = f - np.round(f)                       # crossings of any level s + n
        sc = np.sum((np.sign(frac[:-1]) != np.sign(frac[1:])) & (np.abs(frac[:-1] - frac[1:]) < 0.5))
        counts.append(int(sc))
    print(f"   t = {t:.2f}: crossings per period over 24 lines of u: min {min(counts)} max {max(counts)}  {counts}", flush=True)
