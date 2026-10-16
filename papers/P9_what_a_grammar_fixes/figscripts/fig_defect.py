"""Figure: the matter's defect relative to its norm, f = |D|/||R||^2, on the modular surface's fundamental domain (it is
modular-invariant); it vanishes at omega and toward the cusp; the root LR's closed geodesic drawn reduced."""
from _style import *
import importlib.util, math, numpy as np
spec = importlib.util.spec_from_file_location("b1663", ROOT / "frontier/B1663_the_pull_backs_strength/verification/the_pull_backs_strength.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
xs = np.linspace(-0.5, 0.5, 161); ys = np.linspace(math.sqrt(3)/2, 2.6, 161); F = np.full((len(ys), len(xs)), np.nan)
for i, y in enumerate(ys):
    for j, x in enumerate(xs):
        if x*x + y*y >= 1: F[i, j] = m.f_raw(complex(x, y))
fig, ax = plt.subplots(figsize=(3.2, 3.6))
im = ax.pcolormesh(xs, ys, F, cmap="viridis", shading="auto")
th = np.linspace(np.pi/3, 2*np.pi/3, 100); ax.plot(np.cos(th), np.sin(th), color="white", lw=0.8)
# the root's closed geodesic, one period, reduced to the domain
a, b, c, d = 2, 1, 1, 1; tr = 3; ell = 2*math.acosh(1.5); disc = math.sqrt(5); xa, xr = ((a - d) + disc)/(2*c), ((a - d) - disc)/(2*c)
pts = [m.reduce((xa*1j*math.exp(s) + xr)/(1j*math.exp(s) + 1)) for s in np.linspace(-ell/2, ell/2, 2000)]
ax.plot([p.real for p in pts], [p.imag for p in pts], ".", ms=0.6, color=OI["vermillion"])
ax.plot([-0.5, 0.5], [math.sqrt(3)/2]*2, "o", ms=4, mfc="white", mec="black"); ax.text(-0.47, 0.78, r"$\omega$", fontsize=8)
ax.plot([0], [1], "s", ms=3.5, mfc="white", mec="black"); ax.text(0.03, 0.96, "$i$", fontsize=8)
ax.set_xlim(-0.5, 0.5); ax.set_ylim(0.75, 2.6); ax.set_xlabel(r"$\mathrm{Re}\,\tau$"); ax.set_ylabel(r"$\mathrm{Im}\,\tau$")
cb = fig.colorbar(im, ax=ax, fraction=0.05); cb.set_label(r"$f=|D|/\|R\|^2$", fontsize=8)
save(fig, "fig_defect", "B1663's sealed f (W87's closed form)")
