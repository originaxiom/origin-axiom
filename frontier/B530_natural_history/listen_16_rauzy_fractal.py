"""
Movement XIV — the explicit 3-d Rauzy fractal: the object's geometric self.

The object is a unimodular Pisot substitution (movement XIII), so it has a Rauzy
fractal: project the abelianized prefixes of the fixed point onto the 3-d
CONTRACTING eigenspace (R^1 (+) C = the real mode -0.440 and the breath plane
|gamma|=1/sqrt(phi), movement XII), and take the closure.  What we find:

  * a BOUNDED compact tile in R^3 (a genuine fractal, not escaping).
  * FOUR subtiles R_a, R_b, R_A, R_B (colour = the letter), whose VOLUMES equal
    the golden-tensor letter frequencies (phi,1)(x)(sqrt phi,1) EXACTLY
    (movement III) -- the geometry's measure IS the golden tensor.
  * DISJOINT interiors: 3-d mixed-bin fraction 5.8% -> 0.3% -> 0.0% as the bins
    shrink -> overlaps live on the measure-zero boundary, exactly as the strong
    coincidence condition (movement XIII) guarantees.

Run as __main__ to also render frontier/B530_natural_history/rauzy_fractal.png.
No physics -- the object's own tile.
"""
import numpy as np
from collections import defaultdict

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPH = 'abAB'
M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)


def fixed_point(n):
    u = 'a'
    while len(u) < n:
        u = ''.join(SUB[c] for c in u)
    return u[:n]


def rauzy_points(n=400000):
    """Project abelianized prefixes of the fixed point onto the contracting 3-space."""
    u = fixed_point(n)
    idx = {c: i for i, c in enumerate(ALPH)}
    steps = np.zeros((len(u), 4))
    for k, c in enumerate(u):
        steps[k, idx[c]] = 1
    P = np.cumsum(steps, axis=0)
    vals, V = np.linalg.eig(M)
    W = np.linalg.inv(V)
    i_perr = int(np.argmax(vals.real))
    i_real = [i for i in range(4) if abs(vals[i].imag) < 1e-9 and i != i_perr][0]
    i_cplx = [i for i in range(4) if vals[i].imag > 1e-9][0]
    cr = (W[i_real] @ P.T).real
    cc = (W[i_cplx] @ P.T)
    z = np.vstack([cr, cc.real, cc.imag]).T                 # R^3 = R (+) C
    lab = np.array([idx[c] for c in u])
    return z, lab


def checks(z, lab):
    phi = (1 + np.sqrt(5)) / 2
    sq = np.sqrt(phi)
    w = np.array([phi, 1, phi * sq, sq])
    w = w / w.sum()                                          # golden-tensor freqs
    freq = np.array([(lab == i).mean() for i in range(4)])
    measure_ok = np.allclose(freq, w, atol=2e-3)             # subtile volumes = golden tensor
    bounded = np.abs(z).max() < 5                            # compact fractal
    # 3-d interiors disjoint: mixed-bin fraction falls toward 0 as bins shrink
    fracs = []
    for h in (0.02, 0.01, 0.005):
        g = np.round(z / h).astype(int)
        bl = defaultdict(set)
        for k in range(len(z)):
            bl[tuple(g[k])].add(lab[k])
        fracs.append(sum(1 for s in bl.values() if len(s) > 1) / len(bl))
    disjoint = fracs[0] > fracs[1] > fracs[2] and fracs[2] < 0.01
    return dict(measure_ok=bool(measure_ok), bounded=bool(bounded),
                disjoint=bool(disjoint), freq=freq.round(4).tolist(),
                golden_tensor=w.round(4).tolist(), mixed_bin_fracs=[round(f, 4) for f in fracs])


def render(z, lab, path):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    cols = ['#e63946', '#457b9d', '#f4a261', '#2a9d8f']
    names = ['R_a', 'R_b', 'R_A', 'R_B']
    fig, ax = plt.subplots(1, 2, figsize=(15, 7.4), facecolor='white')
    sl = np.abs(z[:, 0]) < 0.04
    for i in range(4):
        m = sl & (lab == i)
        ax[0].scatter(z[m, 1], z[m, 2], s=0.5, c=cols[i], marker='.', linewidths=0, label=names[i])
    ax[0].set_title('breath-plane slice  |real mode|<0.04  (crisp fractal boundary)', fontsize=12)
    ax[0].set_aspect('equal'); ax[0].set_xticks([]); ax[0].set_yticks([])
    ax[0].legend(markerscale=25, loc='upper right', framealpha=0.95)
    for i in range(4):
        m = lab == i
        ax[1].scatter(z[m, 0], z[m, 2], s=0.12, c=cols[i], marker='.', linewidths=0)
    ax[1].set_title('(real mode -0.440) x (breath Im): the self-similar striping', fontsize=12)
    ax[1].set_aspect('equal'); ax[1].set_xticks([]); ax[1].set_yticks([])
    fig.suptitle('The 4-letter object as a 3-d quasicrystal - its Rauzy fractal\n'
                 '4 subtiles = 4 letters, subtile volumes = golden-tensor frequencies, interiors disjoint',
                 fontsize=12.5)
    plt.tight_layout(rect=[0, 0, 1, 0.92])
    plt.savefig(path, dpi=145, bbox_inches='tight')


if __name__ == "__main__":
    import os
    z, lab = rauzy_points()
    print("Rauzy fractal:", z.shape, "points in R^3")
    print(checks(z, lab))
    out = os.path.join(os.path.dirname(__file__), 'rauzy_fractal.png')
    render(z, lab, out)
    print("rendered", out)
