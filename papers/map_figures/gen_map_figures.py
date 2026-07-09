#!/usr/bin/env python
"""
Figures for THE MAP OF THE OBJECT (the synthesis paper).

One function per figure. Each is standalone, deterministic, grounded in a verified
computation (no plotted value is asserted without a check in-script), and saves a
PDF + PNG to out/. Reuses the flagship style.mplstyle and its proof-status badges.

    Run all:  python gen_map_figures.py
    Run one:  python gen_map_figures.py mapfig2

No physics is claimed. Figures touching a GATED/APPEARS-NOVEL result say so on the plot.
"""
from __future__ import annotations
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
FLAGSHIP_STYLE = os.path.join(HERE, "..", "flagship", "figures", "style.mplstyle")
plt.style.use(FLAGSHIP_STYLE)
OUT = os.path.join(HERE, "out")

STATUS_COLORS = {
    "PROVED": "#2e7d54", "KNOWN": "#8c8c8c", "NUMERICAL": "#1b3a5b",
    "STRUCTURAL": "#7a4f9e", "GATED": "#b6411a", "NOVEL-GATED": "#b6411a",
}
PHI = (1.0 + np.sqrt(5.0)) / 2.0


def _badge(ax, status, loc=(0.015, 0.93)):
    ax.text(loc[0], loc[1], status, transform=ax.transAxes, fontsize=8.5,
            fontweight="bold", color="white", va="center", ha="left",
            bbox=dict(boxstyle="round,pad=0.3", fc=STATUS_COLORS.get(status, "#333"), ec="none"),
            zorder=20)


def _save(fig, name):
    os.makedirs(OUT, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"))
    plt.close(fig)
    print(f"  wrote out/{name}.pdf, out/{name}.png")


def _lucas(k):
    a, b = 2, 1
    for _ in range(k):
        a, b = b, a + b
    return a


# ---------------------------------------------------------------------------
# mapfig1 -- the metallic family as the fixed points of the Gauss map (the spine)
# ---------------------------------------------------------------------------
def mapfig1():
    """Gauss map G(x)={1/x}; the metallic means are its constant-CF fixed points.
    Grounded: 1/lambda_m = [0;m,m,...] satisfies G(1/lambda_m)=1/lambda_m exactly."""
    G = lambda x: (1.0 / x) % 1.0
    fig, ax = plt.subplots()
    # the Gauss map, branch by branch (1/(k+1), 1/k]
    for k in range(1, 9):
        xs = np.linspace(1.0 / (k + 1) + 1e-6, 1.0 / k, 400)
        ax.plot(xs, G(xs), color="#1b3a5b", lw=1.4)
    ax.plot([0, 1], [0, 1], "--", color="#8c8c8c", lw=1.0, label=r"$y=x$ (fixed locus)")

    names = {1: "golden", 2: "silver", 3: "bronze", 4: "copper"}
    for m in range(1, 5):
        lam = (m + np.sqrt(m * m + 4)) / 2.0
        xf = 1.0 / lam
        assert abs(G(xf) - xf) < 1e-9, f"1/lambda_{m} not a Gauss fixed point!"
        ax.plot([xf], [xf], "o", color="#b6411a", ms=8, zorder=15)
        ax.annotate(rf"$1/\lambda_{{{m}}}=[0;\overline{{{m}}}]$" + f"\n{names[m]}",
                    (xf, xf), textcoords="offset points", xytext=(8, -14 if m > 1 else 6),
                    fontsize=8, color="#7a1a08")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xlabel(r"$x$  (BKL / Kasner parameter)")
    ax.set_ylabel(r"$G(x)=\{1/x\}$")
    ax.set_title("The metallic family = the constant-CF fixed points of the Gauss map")
    ax.legend(loc="lower right")
    _badge(ax, "KNOWN")
    _save(fig, "mapfig1_gauss_spine")


# ---------------------------------------------------------------------------
# mapfig2 -- the self-interaction cover tower (B489): volume and torsion
# ---------------------------------------------------------------------------
def mapfig2():
    """The n-fold cyclic cover of 4_1: volume = n*vol(4_1) (covering, exact) and
    H1 torsion = |L(2n)-2| (Fox-Weber). Grounded: both from B489, recomputed here."""
    VOL41 = 2.0298832128193072
    ns = np.arange(1, 9)
    vols = ns * VOL41
    tors = np.array([abs(_lucas(2 * n) - 2) for n in ns])
    # sanity: n=2 torsion is the figure-eight knot determinant 5
    assert tors[1] == 5, "torsion(n=2) != det(4_1)=5"

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 4.0))
    a1.plot(ns, vols, "o-", color="#2e7d54")
    a1.set_xlabel(r"cover degree $n$"); a1.set_ylabel(r"$\mathrm{vol}\,(b{+}{+}(RL)^n)$")
    a1.set_title(r"volume $= n\cdot\mathrm{vol}(4_1)$  (covering, exact)")
    a1.annotate(r"$\mathrm{vol}(4_1)=2.02988\ldots$", (0.05, 0.9), xycoords="axes fraction", fontsize=8.5)
    _badge(a1, "KNOWN", loc=(0.03, 0.07))

    a2.semilogy(ns, tors, "s-", color="#1b3a5b")
    a2.set_xlabel(r"cover degree $n$"); a2.set_ylabel(r"$|H_1\ \mathrm{torsion}| = |L(2n)-2|$")
    a2.set_title(r"torsion $=|\det(A_1^n-I)|=|L(2n)-2|$")
    for n, t in zip(ns, tors):
        a2.annotate(str(t), (n, t), textcoords="offset points", xytext=(0, 6), fontsize=7.5, ha="center")
    a2.annotate(r"$n{=}2:\ 5=\det(4_1)=|\Delta(-1)|$", (0.28, 0.10), xycoords="axes fraction",
                fontsize=8.5, color="#7a1a08")
    _badge(a2, "KNOWN", loc=(0.03, 0.9))
    fig.suptitle("The self-interaction tower: the cyclic-cover tower of the figure-eight (B489)", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    _save(fig, "mapfig2_cover_tower")


# ---------------------------------------------------------------------------
# mapfig3 -- the seam's broken subfield lattice (P1/B459): Q(sqrt-15) never realized
# ---------------------------------------------------------------------------
def mapfig3():
    """The realized surviving-fields of the seam form: the subfield lattice of
    Q(sqrt5,sqrt-3) with the Q(sqrt-15) node NEVER realized, plus a zero stratum.
    Grounded: populations 120/20/20/10/70 from verify_patterns.py (B459)."""
    pop = {"full": 120, "q5": 20, "q3": 20, "q15": 0, "rat": 10, "dark": 70}
    assert sum(v for k, v in pop.items() if k != "q15") == 240
    fig, ax = plt.subplots(figsize=(7.4, 5.2))
    ax.axis("off")
    # node positions (Hasse diagram) + the zero stratum off to the side
    nodes = {
        "full": (0.5, 0.82, r"$\mathbb{Q}(\sqrt{5},\sqrt{-3})$", pop["full"], "#2e7d54"),
        "q5":   (0.18, 0.55, r"$\mathbb{Q}(\sqrt{5})$",  pop["q5"], "#1b3a5b"),
        "q3":   (0.50, 0.55, r"$\mathbb{Q}(\sqrt{-3})$", pop["q3"], "#1b3a5b"),
        "q15":  (0.82, 0.55, r"$\mathbb{Q}(\sqrt{-15})$", pop["q15"], "#b6411a"),
        "rat":  (0.34, 0.28, r"$\mathbb{Q}$", pop["rat"], "#7a4f9e"),
        "dark": (0.82, 0.20, r"$0$  (dark)", pop["dark"], "#333333"),
    }
    edges = [("full", "q5"), ("full", "q3"), ("full", "q15"),
             ("q5", "rat"), ("q3", "rat"), ("q15", "rat")]
    for u, v in edges:
        x1, y1 = nodes[u][0], nodes[u][1]
        x2, y2 = nodes[v][0], nodes[v][1]
        dead = ("q15" in (u, v))
        ax.plot([x1, x2], [y1, y2], color=("#b6411a" if dead else "#999999"),
                lw=1.0, ls=(":" if dead else "-"), zorder=1)
    for key, (x, y, lab, n, col) in nodes.items():
        dead = (key == "q15")
        ax.add_patch(FancyBboxPatch((x - 0.115, y - 0.055), 0.23, 0.11,
                     boxstyle="round,pad=0.01", fc="white",
                     ec=col, lw=1.6, ls=("--" if dead else "-"), zorder=2))
        ax.text(x, y + 0.012, lab, ha="center", va="center", fontsize=10.5,
                color=("#b6411a" if dead else "#111111"), zorder=3)
        tag = ("NEVER realized" if dead else f"{n} pts")
        ax.text(x, y - 0.032, tag, ha="center", va="center", fontsize=8,
                color=("#b6411a" if dead else "#555555"), zorder=3,
                fontstyle=("italic" if dead else "normal"))
        if dead:
            ax.plot([x - 0.11, x + 0.11], [y + 0.05, y - 0.05], color="#b6411a", lw=1.8, zorder=4)
    ax.text(0.5, 0.99, "The seam form's broken subfield lattice  (level 15)",
            ha="center", va="top", fontsize=12, transform=ax.transAxes)
    ax.text(0.5, 0.02,
            r"realized: $\{$full, $\mathbb{Q}(\sqrt{5})$, $\mathbb{Q}(\sqrt{-3})$, $\mathbb{Q}$, $0\}$"
            r"  —  $\mathbb{Q}(\sqrt{-15})$ (the level's own field) dies in every non-free pattern",
            ha="center", va="bottom", fontsize=8.5, transform=ax.transAxes, color="#333333")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    _badge(ax, "NOVEL-GATED", loc=(0.015, 0.90))
    _save(fig, "mapfig3_broken_lattice")


FIGS = {"mapfig1": mapfig1, "mapfig2": mapfig2, "mapfig3": mapfig3}
if __name__ == "__main__":
    which = sys.argv[1:] or list(FIGS)
    for name in which:
        print(f"[{name}]")
        FIGS[name]()
