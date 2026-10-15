# EXPLORATION: in the least-volume family L R^n, the smallest n for which an order-N line closes all three sectors
# (N^2 | Q_gamma(w)), both signs; the bundle's volume (SnapPy) and the geodesic's height.
import math, warnings, snappy
warnings.filterwarnings("ignore")
exec(open("closing_by_volume_syllables.py").read().split("words =")[0])   # mat, closing
def height(w):
    best = None
    for i in range(len(w)):
        A, B, C, D = mat(w[i:] + w[:i]); m = min(abs(B), abs(C))
        if best is None or m < best[0]: best = (m, A + D)
    return math.sqrt(best[1]**2 - 4) / (2*best[0])
for N in (5, 7, 9, 11, 13):
    for eps in (1, -1):
        for n in range(1, 400):
            w = "L" + "R"*n
            k = closing(w, N, eps)
            if k:
                M = snappy.Manifold(f"b+{'+' if eps > 0 else '-'}{w}")
                print(f"N={N} eps={eps:+d}: smallest n = {n}  (L R^{n}: Vol {float(M.volume()):.6f}, height {height(w):.2f}, closing lines {k}, H1 {M.homology()})", flush=True)
                break
print("for scale: Vol(L R^n) -> 3.66386 (the Whitehead link) as n grows; Vol(L R) = 2.02988 (the root)")
