#!/usr/bin/env python
"""Figures for the narrow SL(4) Dehn-filling note (3 figures, no padding).

  fig_tower  -- the Dickson factorisation n=2,3,4 (corrected n=2 row = chi(M^2)(t+1))
  fig_slope  -- the Dehn-filling slope L=+M^3 (n=3) and L=-M^4 (n=4); no n=2/n=5
  fig_strat  -- the gauge-rank stratification (B149 finite-field classification)

Deterministic; pyenv (numpy, matplotlib). Reuses frontier/B149 data for fig_strat.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "out")
PHI = (1 + np.sqrt(5)) / 2

plt.rcParams.update({
    "figure.dpi": 140, "savefig.dpi": 300, "savefig.bbox": "tight",
    "font.family": "serif", "font.serif": ["DejaVu Serif"], "mathtext.fontset": "cm",
    "font.size": 11, "axes.grid": True, "grid.alpha": 0.5, "grid.linewidth": 0.5,
    "axes.axisbelow": True,
})


def save(fig, name):
    os.makedirs(OUT, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"))
    plt.close(fig)
    print("wrote", name)


def fig_tower():
    # (k, sign): chi(sign*M^k). n=2 row corrected to chi(M^2).
    towers = {
        2: [(2, +1)],
        3: [(1, -1), (2, +1), (3, +1)],
        4: [(1, +1), (1, -1), (2, +1), (2, -1), (3, +1), (4, +1)],
    }
    fig, ax = plt.subplots(figsize=(8.2, 3.6))
    for row, n in enumerate((2, 3, 4)):
        ax.axhline(row, color="#eee", lw=8, zorder=0)
        for (k, sign) in towers[n]:
            xpos = k if sign > 0 else -k
            color = "#2e7d54" if k % 2 == 0 else "#7a4f9e"
            marker = "o" if sign > 0 else "D"
            ax.scatter([xpos], [row], s=180, marker=marker, color=color,
                       edgecolor="#222", linewidth=1.0, zorder=4)
            lbl = ("-" if sign < 0 else "") + (f"M^{k}" if k > 1 else "M")
            ax.annotate(fr"$\chi({lbl})$", (xpos, row), textcoords="offset points",
                        xytext=(0, 12), ha="center", fontsize=8.5)
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["SL(2)\n(dim 3)", "SL(3)\n(dim 8)", "SL(4)\n(dim 15)"])
    ax.set_xlabel(r"signed power $k$  ($\circ$ sign $+$, $\diamond$ sign $-$;  colour $=$ parity of $|k|$)")
    ax.set_xlim(-3.4, 4.7); ax.set_ylim(-0.6, 2.7)
    ax.set_title(r"Dickson tower: $\det(tI-J(m))=\prod_k\chi(\pm M^{k})$  (with $(t\mp1)$ factors)")
    leg = [Line2D([0],[0],marker="o",color="w",markerfacecolor="#2e7d54",markeredgecolor="#222",markersize=10,label="even $|k|$"),
           Line2D([0],[0],marker="o",color="w",markerfacecolor="#7a4f9e",markeredgecolor="#222",markersize=10,label="odd $|k|$")]
    ax.legend(handles=leg, loc="lower right", fontsize=8)
    ax.text(-3.2, 0.0, r"$\chi(M^2)$ base case", fontsize=7.5, color="#555", va="center")
    save(fig, "fig_tower")


def fig_slope():
    M = np.linspace(1.02, 2.2, 300)
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.plot(np.log(M), 3*np.log(M), "-", color="#1b3a5b", lw=2.0,
            label=r"$n=3$:  $L=+M^3$  (Falbel, KNOWN)")
    ax.plot(np.log(M), 4*np.log(M), "--", color="#b6411a", lw=2.0,
            label=r"$n=4$:  $L=-M^4$  (this paper)")
    ax.set_xlabel(r"$\log|M|$  (meridian)")
    ax.set_ylabel(r"$\log|L|$  (longitude)")
    ax.set_title(r"The figure-eight Dehn-filling slope, by rank")
    ax.legend(loc="upper left")
    ax.text(0.40, 0.06, "no $n=2$ monomial instance;\n$n\\geq5$ open",
            transform=ax.transAxes, fontsize=8.5, color="#555",
            bbox=dict(boxstyle="round,pad=0.3", fc="#f6f6f6", ec="#ccc"))
    save(fig, "fig_slope")


def fig_strat():
    p = os.path.join(ROOT, "frontier", "B149_sl4_ideal_completeness", "irreducibility_fp.json")
    d = json.load(open(p))["per_stratum"]
    order = ["rankQ2 (Q=I2,B89)", "rankQ1 [[1,1],[0,0]]", "rankQ0 (Q=0)",
             "rankQ1 [[1,0],[0,0]]", "rankQ1 [[0,1],[0,0]]"]
    pretty = {"rankQ2 (Q=I2,B89)": "rank $Q$=2\n(the family)",
              "rankQ1 [[1,1],[0,0]]": "rank $Q$=1\n$[[1,1],[0,0]]$",
              "rankQ0 (Q=0)": "rank $Q$=0\n($\\det t=0$)",
              "rankQ1 [[1,0],[0,0]]": "rank $Q$=1\n$[[1,0],[0,0]]$",
              "rankQ1 [[0,1],[0,0]]": "rank $Q$=1\n$[[0,1],[0,0]]$"}
    names, irr, redL, redN = [], [], [], []
    for k in order:
        s = d[k]; names.append(pretty[k])
        irr.append(s["irr&M4=L"] + s["irr&M4!=L"]); redL.append(s["red&M4=L"]); redN.append(s["red&M4!=L"])
    y = np.arange(len(names))
    fig, ax = plt.subplots(figsize=(7.8, 3.8))
    ax.barh(y, irr, color="#2e7d54", label=r"irreducible ($M^4{=}L$)")
    ax.barh(y, redL, left=irr, color="#9ec6b0", label=r"reducible ($M^4{=}L$)")
    ax.barh(y, redN, left=np.array(irr)+np.array(redL), color="#d9d9d9", label=r"reducible / vacuous")
    ax.set_yticks(y); ax.set_yticklabels(names, fontsize=8.5); ax.invert_yaxis()
    ax.set_xlabel(r"sampled $\mathbb{F}_p$ representations (Burnside test)")
    ax.set_title(r"SL(4) completeness: the irreducible locus $=$ the family")
    ax.legend(loc="lower right", fontsize=8)
    save(fig, "fig_strat")


if __name__ == "__main__":
    fig_tower(); fig_slope(); fig_strat()
    print("done ->", OUT)
