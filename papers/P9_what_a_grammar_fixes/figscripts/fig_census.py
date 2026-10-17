"""Figure: B1660's one-Higgs census (a scoreboard) -- chi2_min on each of W59's 18 lines in the three readings of the
up sector, against the conservative bound 11.07."""
from _style import *
import numpy as np, hashlib
d = load_json("frontier/B1660_the_one_higgs_census/verification/the_one_higgs_census.json", "1f01bdaa6a26795c")
fig, ax = plt.subplots(figsize=(6.3, 2.6))
mk = {"same": ("o", OI["blue"], "the same $S$"), "tilde": ("s", OI["vermillion"], r"$\tilde S=\epsilon\bar S\epsilon^T$"), "bar": ("^", OI["green"], r"$\bar S$")}
for k, (m, c, lab) in mk.items():
    cells = d["C2"]["census"][k]; y = [c_["chi2_min"] for c_ in cells]
    ax.plot(range(18), y, m, color=c, ms=4.5, label=lab, mfc="none" if k == "tilde" else c)
ax.axhline(11.07, color=OI["black"], lw=0.8, ls="--"); ax.text(17.4, 13, "11.07", ha="right", va="bottom", fontsize=7)
ax.set_yscale("log"); ax.set_xlabel(r"flat line (the 18 fixed at $\omega$, in the record's order)"); ax.set_ylabel(r"$\chi^2_{\min}$ (160 starts)")
ax.set_xticks(range(18)); ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.18))
save(fig, "fig_census", "B1660 the_one_higgs_census.json")
