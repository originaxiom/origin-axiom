"""Data-free: |d theta| along the tube's core (the shortest geodesic aaBa of L^6RLR), by exact pullback into the Ford
domain. Nonzero everywhere on the core, so the tube level s = 0 is a REGULAR level: its modulus is the limit of tau(s)."""
import sys, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "B1846_the_metrics_read_out", "verification"))
from stage_b_surface import setup
from step4_tube import shortest_loxodromic, axis_points
from fastpull import pullback_batch
if __name__ == "__main__":
    G, H, info, wf = setup("b++LLLLLLRLR", 12, 0.33, 9604, 7)
    X, L, cx = shortest_loxodromic(G, depth=6)
    pts, ends = axis_points(X, n=400)
    Z = np.array([p[0] for p in pts]); T = np.array([p[1] for p in pts])
    Zs, Ts, Cs = pullback_batch(G, Z, T)
    gx, gy, gt = H.grad(Zs, Ts)
    g = Ts * np.sqrt(gx ** 2 + gy ** 2 + gt ** 2)
    phi = H.phi(Zs, Ts) - Cs
    print(f"core length {L.real:.6f}{L.imag:+.6f}i; theta on the core: max |phi - nearest integer| {np.abs(phi - np.round(phi)).max():.2e}")
    print(f"|d theta| on the core (hyperbolic): min {g.min():.6e} max {g.max():.6e} over 400 points")
