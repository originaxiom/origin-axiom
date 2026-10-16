"""Figure: the joint law (B1659) -- the three masses of Y(S, M) against the Higgs's defect and the matter's defect:
the lightest goes as the product of the two defects, the middle as their sum, the heaviest stays."""
from _style import *
import numpy as np
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ; BLOCKS = [QJ, QI, QK]
def Y(S, M): return np.array([[np.sum((Ca.T @ EPS @ S @ Cb)*M) for Cb in BLOCKS] for Ca in BLOCKS])
rng = np.random.default_rng(3)
u, v = rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)
p, q = rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)
X, Z = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)), rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
S0, M0 = np.outer(u, v), np.outer(p, q)          # null Higgs, null matter
ts = np.logspace(-5, -0.5, 40)
fig, axs = plt.subplots(1, 2, figsize=(6.3, 2.4), sharey=True)
for ax, mode in zip(axs, ("higgs", "matter")):
    ms = []
    for t in ts:
        S = S0 + (t*X if mode == "higgs" else 1e-2*X); M = M0 + (t*Z if mode == "matter" else 1e-2*Z)
        ms.append(np.linalg.svd(Y(S, M), compute_uv=False))
    ms = np.array(ms)
    for k, (col, lab) in enumerate(((OI["blue"], "$m_3$"), (OI["green"], "$m_2$"), (OI["vermillion"], "$m_1$"))):
        ax.loglog(ts, ms[:, k], color=col, lw=1.2, label=lab)
    ax.set_xlabel(("Higgs defect $t$" if mode == "higgs" else "matter defect $t$") + " (the other at $10^{-2}$)")
axs[0].set_ylabel("masses (singular values of $Y$)"); axs[0].legend(frameon=False, fontsize=7)
fig.tight_layout(); save(fig, "fig_joint", "B1659's coupling (its lock's construction), a random null S and M")
