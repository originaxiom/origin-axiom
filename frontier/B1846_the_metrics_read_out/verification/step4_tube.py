"""Step 4 helper (data-free): the shortest closed geodesic of a member as a group element from the word BFS, its complex
length checked against SnapPy's length spectrum, chi on it, and points of its axis pulled into the Ford domain.
Imported by the measure step; standalone it prints the geodesic's data."""
import sys, os, cmath
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def shortest_loxodromic(G, depth=6):
    best = None
    for X, cx in G._bfs(G.H, depth, 400.0):
        tr = X[0, 0] + X[1, 1]
        if abs(tr.imag) < 1e-9 and abs(tr.real) <= 2.0001:
            continue                                   # elliptic or parabolic; a complex trace is loxodromic
        L = 2 * cmath.acosh(tr / 2)
        if L.real < 0:
            L = -L
        if best is None or L.real < best[1].real - 1e-9:
            best = (X, L, cx)
    return best


def axis_points(X, n=64):
    """Points along the axis of loxodromic X (endpoints p, q on C), one translation length's worth."""
    a, b, c, d = X[0, 0], X[0, 1], X[1, 0], X[1, 1]
    disc = cmath.sqrt((a - d) ** 2 + 4 * b * c)
    p = ((a - d) + disc) / (2 * c); q = ((a - d) - disc) / (2 * c)
    # the axis: the semicircle over [p, q]; parametrise by hyperbolic arclength from the top
    ctr = (p + q) / 2; R = abs(p - q) / 2; u = (q - p) / abs(q - p)
    L = 2 * cmath.acosh((a + d) / 2)
    pts = []
    for k in range(n):
        s = (k / n - 0.5) * abs(L.real)            # arclength from the apex of the semicircle
        x = R * np.tanh(s); t = R / np.cosh(s)
        pts.append((ctr + x * u, t))
    return pts, (p, q)


if __name__ == "__main__":
    from oa_harm import Group
    import snappy
    name = sys.argv[1]
    G = Group(name, rmin=0.05, depth=6)
    X, L, cx = shortest_loxodromic(G)
    spec = snappy.Manifold(name).length_spectrum(1.0)
    print(f"{name}: shortest loxodromic from the BFS: complex length {L.real:.6f} {L.imag:+.6f}i, chi = {cx}")
    print("   SnapPy length spectrum:", [(round(float(g.length.real), 6), round(float(g.length.imag), 6)) for g in spec[:3]])
    pts, (p, q) = axis_points(X)
    zs = []
    for z, t in pts:
        z2, t2, ch = G.pullback(z, t)
        zs.append((t2, ch))
    print(f"   axis endpoints {p:.5f}, {q:.5f}; pulled-back heights min {min(z for z,_ in zs):.4f} max {max(z for z,_ in zs):.4f}")
