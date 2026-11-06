"""Data-free: the Teichmuller reading at the symmetric points of a member's closed geodesic in the modular surface -- the
monodromy's axis in H, followed over one period and reduced to the standard fundamental domain; the local maxima of
Im tau are the apex and the anti-apex. Control: m004 (LR) gives the golden apex 1/2 + (sqrt5/2) i and passes through i."""
import math
import numpy as np
L_ = np.array([[1, 0], [1, 1]], dtype=float); R_ = np.array([[1, 1], [0, 1]], dtype=float)


def mat(w):
    M = np.eye(2)
    for ch in w:
        M = M @ (L_ if ch == "L" else R_)
    return M


def reduce(t):
    for _ in range(500):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-14:
            t = -1 / t
        else:
            break
    return t


def readings(w, n=200001):
    a, b, c, d = mat(w).ravel()
    disc = math.sqrt((a + d) ** 2 - 4)
    p = ((a - d) + disc) / (2 * c); q = ((a - d) - disc) / (2 * c)
    ctr = (p + q) / 2; Rr = abs(p - q) / 2; ell = 2 * math.acosh((a + d) / 2)
    pts = [reduce(complex(ctr + Rr * math.tanh(s0 - ell / 2), Rr / math.cosh(s0 - ell / 2))) for s0 in np.linspace(0, ell, n)]
    im = np.array([z.imag for z in pts])
    loc = [i for i in range(1, len(im) - 1) if im[i] >= im[i - 1] and im[i] >= im[i + 1]]
    vals = sorted(set((round(pts[i].real, 5), round(im[i], 6)) for i in loc), key=lambda v: -v[1])
    return ell, im.max(), im.min(), vals


if __name__ == "__main__":
    for w in ("LR", "LLLLLLRLR"):
        ell, mx, mn, vals = readings(w)
        print(f"{w}: translation length {ell:.6f}; reduced path max Im {mx:.6f}, min Im {mn:.6f}; local maxima (Re, Im) {vals}")
    print(f"sqrt5/2 = {math.sqrt(5)/2:.6f}; sqrt(40/3) = {math.sqrt(40/3):.6f}; sqrt(15/8) = {math.sqrt(15/8):.6f}")
