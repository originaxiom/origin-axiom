"""Independent verification of cc3's m004 Maass eigenvalues (B792).

cc's OWN implementation -- written from the method, not from cc3's code. Different height,
different mode count, different pullback word set. Tests sigma_min(V(r)) at cc3's claimed
eigenvalues against DISPLACED controls, which is the discriminating test: a real eigenvalue
gives a sharp sigma_min dip, a displaced point does not.

Ingredients independently checked first:
  cusp shape tau = 2 sqrt(-3)  -- matches SnapPy to 1e-9
  relator  w a = b w, w = a b^-1 a^-1 b  -- exact (also B789's word)
"""
import numpy as np

W3 = np.sqrt(3.0)
OM = complex(-0.5, W3 / 2)                      # omega = e^{2 pi i/3}
TAU = complex(0.0, 2 * W3)                      # cusp lattice second generator

A = np.array([[1, 1], [0, 1]], dtype=complex)
B = np.array([[1, 0], [-OM, 1]], dtype=complex)
GENS = [A, np.linalg.inv(A), B, np.linalg.inv(B)]


# ---------------- action on upper half-space H^3 = {(z,t)} ----------------
def act(g, z, t):
    a, b, c, d = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    den = abs(c * z + d) ** 2 + abs(c) ** 2 * t ** 2
    zn = ((a * z + b) * np.conj(c * z + d) + a * np.conj(c) * t ** 2) / den
    return zn, t / den


def word_matrices(maxlen):
    """All products of generators up to maxlen, deduplicated."""
    out, seen = [], set()
    cur = [np.eye(2, dtype=complex)]
    for _ in range(maxlen):
        nxt = []
        for M in cur:
            for g in GENS:
                P = M @ g
                key = tuple(np.round(P.flatten(), 8))
                if key not in seen:
                    seen.add(key); out.append(P); nxt.append(P)
        cur = nxt
    return out


WORDS = word_matrices(4)


def pullback(z, t):
    """Steepest ascent to the maximal-height Gamma-translate."""
    for _ in range(60):
        best = (z, t); improved = False
        for M in WORDS:
            zn, tn = act(M, z, t)
            if tn > best[1] * (1 + 1e-13):
                best = (zn, tn); improved = True
        z, t = best
        if not improved:
            break
    return z, t


# ---------------- K_{ir}(x) by the exponentially-convergent trapezoid ----------------
def K_ir(r, x):
    """K_{ir}(x) = int_0^inf e^{-x cosh u} cos(r u) du, trapezoid (Poisson: exp. convergent)."""
    x = np.asarray(x, dtype=float)
    umax = np.minimum(np.arccosh(np.maximum(60.0 / np.maximum(x, 1e-12), 1.0000001)), 9.0)
    n = 900
    out = np.empty_like(x)
    for i, (xi, um) in enumerate(zip(x.ravel(), umax.ravel())):
        u = np.linspace(0.0, um, n)
        f = np.exp(-xi * np.cosh(u)) * np.cos(r * u)
        out.ravel()[i] = np.trapezoid(f, u) if hasattr(np, "trapezoid") else np.trapz(f, u)
    return out


# ---------------- dual lattice ----------------
def dual_modes(mmax):
    """Lam = Z + Z tau, tau = 2i sqrt3.  Lam* = {p + q i/(2 sqrt3)} with p,q integers."""
    out = []
    P = int(mmax) + 2
    Q = int(mmax * 2 * W3) + 2
    for p in range(-P, P + 1):
        for q in range(-Q, Q + 1):
            mu = complex(p, q / (2 * W3))
            if 0 < abs(mu) <= mmax:
                out.append(mu)
    return np.array(out)


def sigma_min(r, Y, mmax, npts, seed=5):
    mus = dual_modes(mmax)
    rng = np.random.default_rng(seed)
    # sample points in a fundamental domain for Lam
    zs = rng.random(npts) + 1j * (rng.random(npts) * 2 * W3)
    rows = []
    absmu = np.abs(mus)
    for z in zs:
        zp, tp = pullback(z, Y)
        k1 = Y * K_ir(r, 2 * np.pi * absmu * Y)
        k2 = tp * K_ir(r, 2 * np.pi * absmu * tp)
        e1 = np.exp(2j * np.pi * (mus.real * z.real + mus.imag * z.imag))
        e2 = np.exp(2j * np.pi * (mus.real * zp.real + mus.imag * zp.imag))
        rows.append(k1 * e1 - k2 * e2)
    V = np.array(rows)
    nrm = np.linalg.norm(V, axis=0)
    nrm[nrm == 0] = 1.0
    V = V / nrm                                   # column-normalise
    return np.linalg.svd(V, compute_uv=False)[-1]


if __name__ == "__main__":
    # cc3's claimed eigenvalues, and displaced negative controls
    CLAIMED = [3.938916864, 4.900085373, 5.670720035, 5.912917882,
               6.632802303, 7.072004187, 8.863405356]
    Y, MMAX = 0.62, 3.2
    NMODES = len(dual_modes(MMAX))
    NPTS = 3 * NMODES                  # MUST exceed modes: an underdetermined V has
                                       # sigma_min = 0 identically and tests nothing
    print(f"cc INDEPENDENT collocation:  Y={Y}  |mu|<={MMAX}  modes={NMODES}  points={NPTS}")
    print(f"  (overdetermined by {NPTS/NMODES:.1f}x -- required for sigma_min to mean anything)\n")
    print(f"{'r (cc3)':>14} {'sigma_min':>12} {'sigma@r+0.02':>14} {'sigma@r-0.02':>14} {'ratio':>9}")
    for r in CLAIMED:
        s0 = sigma_min(r, Y, MMAX, NPTS)
        sp_ = sigma_min(r + 0.02, Y, MMAX, NPTS)
        sm_ = sigma_min(r - 0.02, Y, MMAX, NPTS)
        ctrl = min(sp_, sm_)
        print(f"{r:>14.9f} {s0:>12.3e} {sp_:>14.3e} {sm_:>14.3e} {ctrl/s0:>9.1f}x")
