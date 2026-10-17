"""Figure: the seed is forced, 144 -> 1 -- for the words L^a R^b (a, b = 1..12) the trace is 2 + ab and the torsion of
H_1 has order |2 - tr| = ab (T-ROOT); only (1, 1), LR, is torsion-free."""
from _style import *
import numpy as np
from matplotlib.colors import LogNorm
a = np.arange(1, 13); A, B = np.meshgrid(a, a); tors = A*B
fig, ax = plt.subplots(figsize=(3.0, 2.7))
im = ax.imshow(tors, origin="lower", extent=(0.5, 12.5, 0.5, 12.5), cmap="cividis", norm=LogNorm(1, 144))
cs = ax.contour(A, B, 2 + A*B, levels=[3, 6, 12, 24, 48, 96], colors="white", linewidths=0.5); ax.clabel(cs, fontsize=5, fmt="tr %d")
ax.plot(1, 1, "o", mfc="none", mec=OI["vermillion"], ms=9, mew=1.5); ax.text(1.6, 1.25, "$LR$", color=OI["vermillion"], fontsize=8)
ax.set_xlabel("$a$"); ax.set_ylabel("$b$"); cb = fig.colorbar(im, ax=ax, fraction=0.046); cb.set_label(r"torsion of $H_1$, $|2-\mathrm{tr}|=ab$", fontsize=7)
save(fig, "fig_seed", "exact (T-ROOT; GENESIS SE1)")
