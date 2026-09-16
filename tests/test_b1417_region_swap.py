"""B1417 lock: the region-swap lemma's grid check -- chi(g>0) = chi(g<0) = 0 for random theta-odd (z -> -z) fields with transverse zeros,
and the non-transverse product mode's +4 resolves to 0 under a generic odd perturbation."""
import numpy as np

def chi_super(G):
    P = G > 0
    V = P.sum(); E = (P & np.roll(P, -1, 0)).sum() + (P & np.roll(P, -1, 1)).sum()
    F = (P & np.roll(P, -1, 0) & np.roll(P, -1, 1) & np.roll(np.roll(P, -1, 0), -1, 1)).sum()
    return int(V - E + F)

def test_region_swap():
    rng = np.random.default_rng(3); N = 360; x = np.arange(N) / N; X, Y = np.meshgrid(x, x, indexing="ij")
    for _ in range(12):
        g = np.zeros_like(X)
        for k in range(-5, 6):
            for l in range(-3, 4):
                if (k, l) > (0, 0): g += rng.normal() * np.sin(2 * np.pi * (k * X + l * Y))
        assert chi_super(g) == 0 and chi_super(-g) == 0
    g = np.sin(4 * np.pi * X) * np.cos(2 * np.pi * Y)
    assert chi_super(g) == 4 and chi_super(-g) == 4          # open rectangles: not a surface invariant
    g2 = g + 0.05 * np.sin(2 * np.pi * (X + Y))
    assert chi_super(g2) == 0 and chi_super(-g2) == 0
