"""Figure: B1663 -- the pull-back's strength p sets the side and the speed of the walk, not the motion's averaged defect."""
from _style import *
d = load_json("frontier/B1663_the_pull_backs_strength/verification/the_pull_backs_strength.json", "ba75deef32086103")
ps = d["PS"]; T2, T3, T4 = d["T2"]["by_p"], d["T3"]["by_p"], d["T4"]["by_p"]
g = lambda T, k: ([T[str(p)][k] for p in ps], [T[str(p)].get("se", 0) for p in ps])
fig, axs = plt.subplots(1, 3, figsize=(6.6, 2.1))
for ax, (T, key, lab, col) in zip(axs, ((T2, "P_pos", r"$P(\xi>0)$, the side", OI["blue"]), (T3, "rate", "escape per step, the speed", OI["vermillion"]), (T4, "mean", r"$E_p\langle f\rangle$, the defect", OI["green"]))):
    y, e = g(T, key); ax.errorbar(ps, y, yerr=e, fmt="o-", color=col, ms=3.5, lw=1, capsize=2); ax.set_xlabel("pull-back strength $p$"); ax.set_title(lab, fontsize=8)
axs[2].axhline(0.31500491, color=OI["grey"], ls="--", lw=0.8); axs[2].text(0.0, 0.33, "typical motion 0.315", fontsize=6.5, color=OI["grey"])
axs[2].set_ylim(0.28, 0.56); fig.tight_layout(); save(fig, "fig_pullback", "B1663 the_pull_backs_strength.json")
