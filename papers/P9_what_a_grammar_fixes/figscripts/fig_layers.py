"""Figure: B1666 -- (a) the threads' layer averages of the defect reach the constant mode 0.315 by trace; (b) the
phase-1 amplitude's coherence by layer decays; (c) the cusp family L^(4m+1) R climbs toward 1, the root LR does not."""
from _style import *
import numpy as np
d = load_json("frontier/B1666_the_layers_robust/verification/the_layers_robust.json", "c5797e1e2bef7fda"); r = d["readouts"]
A = {int(k): v for k, v in r["A_by_t"].items()}; C = {int(k): v for k, v in r["C_by_t"].items()}
fig, axs = plt.subplots(1, 3, figsize=(6.6, 2.2))
t = np.array(sorted(A)); axs[0].plot(t, [A[x] for x in t], ".", ms=1.5, color=OI["blue"]); axs[0].axhline(0.31500491, color=OI["vermillion"], lw=0.9)
axs[0].set_xscale("log"); axs[0].set_xlabel("trace $t$"); axs[0].set_ylabel(r"layer mean $\langle f\rangle$"); axs[0].set_title("(a) the constant mode", fontsize=8)
tc = np.array(sorted(C)); axs[1].plot(tc, [C[x] for x in tc], ".", ms=1.5, color=OI["green"]); axs[1].set_xscale("log"); axs[1].set_xlabel("trace $t$"); axs[1].set_ylabel("coherence (phase-1)"); axs[1].set_title("(b) no constant wave", fontsize=8)
cf = sorted((len(w), v) for w, v in r["cusp_family_LnR"].items())
axs[2].plot([x for x, _ in cf], [y for _, y in cf], "o-", ms=2.5, lw=0.8, color=OI["purple"], label="$L^{4m+1}R$"); axs[2].axhline(r["LR"], color=OI["black"], ls="--", lw=0.8)
axs[2].text(12, r["LR"] - 0.08, "the root $LR$", fontsize=7); axs[2].set_xscale("log"); axs[2].set_xlabel("word length"); axs[2].set_ylabel("coherence"); axs[2].set_title("(c) the cusp, not the root", fontsize=8)
fig.tight_layout(); save(fig, "fig_layers", "B1666 the_layers_robust.json")
