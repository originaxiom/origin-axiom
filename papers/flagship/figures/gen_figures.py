#!/usr/bin/env python
"""
Figure generation harness for the flagship paper.

One function per figure (fig01 .. fig12). Each is standalone and deterministic,
saves a PDF and a PNG into figures/out/, and fails loud if a required data file
is missing. Reuses committed probe data (frontier/B80, frontier/B149) where it
exists; re-derives small symbolic/numeric objects in-script otherwise.

Run all:      python gen_figures.py
Run one:      python gen_figures.py fig09
Environment:  the canonical pyenv (matplotlib, numpy, sympy, scipy).

No physics is claimed here. Figures that touch a GATED or POSTULATED result
carry that word in the plot itself, mirroring the paper's proof-status badges.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "out")
plt.style.use(os.path.join(HERE, "style.mplstyle"))

PHI = (1.0 + np.sqrt(5.0)) / 2.0

# proof-status palette (matches the LaTeX \status badges)
STATUS_COLORS = {
    "PROVED": "#2e7d54",
    "SYMBOLIC-EXACT": "#2e7d54",
    "NUMERICAL": "#1b3a5b",
    "STRUCTURAL": "#7a4f9e",
    "KNOWN": "#8c8c8c",
    "GATED": "#b6411a",
    "POSTULATED": "#c79a1e",
}


def _load_json(relpath: str):
    p = os.path.join(ROOT, relpath)
    if not os.path.exists(p):
        raise FileNotFoundError(f"required data file missing: {relpath}")
    with open(p) as fh:
        return json.load(fh)


def _badge(ax, status: str, loc=(0.015, 0.93)):
    """Stamp a proof-status badge on an axes, mirroring the paper."""
    ax.text(
        loc[0], loc[1], status, transform=ax.transAxes, fontsize=8.5,
        fontweight="bold", color="white", va="center", ha="left",
        bbox=dict(boxstyle="round,pad=0.3", fc=STATUS_COLORS.get(status, "#333"),
                  ec="none"),
        zorder=20,
    )


def _save(fig, name: str):
    os.makedirs(OUT, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"))
    plt.close(fig)
    print(f"  wrote out/{name}.pdf, out/{name}.png")


# ----------------------------------------------------------------------------
# Fig 1 -- metallic means and the monodromy dilatation
# ----------------------------------------------------------------------------
def fig01():
    """Metallic means lambda_m and the dilatation lambda_m^2 vs m; golden/silver."""
    m = np.arange(1, 9)
    lam = (m + np.sqrt(m * m + 4.0)) / 2.0  # metallic mean: x = m + 1/x
    dil = lam ** 2                           # monodromy dilatation (R^m L^m)

    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.9))

    ax = axes[0]
    ax.plot(m, lam, "o-", color="#1b3a5b", label=r"metallic mean $\lambda_m$")
    ax.plot(m, dil, "s--", color="#b6411a",
            label=r"dilatation $\lambda_m^{2}$")
    for mi, li, di, name in [(1, lam[0], dil[0], "golden\n(figure-eight)"),
                             (2, lam[1], dil[1], "silver")]:
        ax.annotate(name, (mi, di), textcoords="offset points",
                    xytext=(6, -2), fontsize=8.5, color="#444")
        ax.scatter([mi], [di], s=70, facecolor="none", edgecolor="#b6411a",
                   linewidth=1.6, zorder=5)
    ax.set_xlabel(r"block parameter $m$  ($R^m L^m$)")
    ax.set_ylabel("value")
    ax.set_title(r"metallic means $\lambda_m=\frac{m+\sqrt{m^2+4}}{2}$")
    ax.legend(loc="upper left")

    # right: continued-fraction convergence to the golden mean
    ax = axes[1]
    x = 1.0
    iters = list(range(1, 13))
    vals = []
    for _ in iters:
        x = 1.0 + 1.0 / x
        vals.append(x)
    ax.plot(iters, vals, "o-", color="#2e7d54")
    ax.axhline(PHI, color="#8c8c8c", ls=":", lw=1.4,
               label=fr"$\varphi={PHI:.6f}$")
    ax.set_xlabel("continued-fraction depth")
    ax.set_ylabel(r"$[1;1,1,\dots]$ convergents")
    ax.set_title("self-reference: $x = m + 1/x$")
    ax.legend(loc="upper right")
    _badge(ax, "PROVED")

    fig.suptitle("The metallic family: the seed and its dilatation", y=1.02,
                 fontsize=12.5)
    _save(fig, "fig01_metallic_means")


# ----------------------------------------------------------------------------
# Fig 2 -- the Fricke cubic surface
# ----------------------------------------------------------------------------
def fig02():
    """The Fricke cubic foliation: the kappa=2 Cayley leaf (point-cloud isosurface)."""
    fig = plt.figure(figsize=(7.8, 5.8))
    ax = fig.add_subplot(111, projection="3d")

    # robust isosurface render of the leaf kappa = 2  (x^2+y^2+z^2-xyz = 4),
    # the classical Cayley nodal cubic -- a bounded, four-noded surface.
    g = np.linspace(-2.6, 2.6, 170)
    X, Y, Z = np.meshgrid(g, g, g)
    K = X * X + Y * Y + Z * Z - X * Y * Z - 2.0
    sel = np.abs(K - 2.0) < 0.05
    xs, ys, zs = X[sel], Y[sel], Z[sel]
    ax.scatter(xs, ys, zs, c=zs, cmap="viridis", s=2.2, alpha=0.5, linewidths=0)
    # the four nodes of the Cayley cubic
    nodes = [(2, 2, 2), (2, -2, -2), (-2, 2, -2), (-2, -2, 2)]
    nx = [p[0] for p in nodes]; ny = [p[1] for p in nodes]; nz = [p[2] for p in nodes]
    ax.scatter(nx, ny, nz, color="#b6411a", s=34, depthshade=False, zorder=6)

    ax.set_title(r"Fricke cubic foliation: the $\kappa=2$ leaf (Cayley nodal cubic)")
    ax.set_xlabel("$x=\\mathrm{tr}\\,A$")
    ax.set_ylabel("$y=\\mathrm{tr}\\,B$")
    ax.set_zlabel("$z=\\mathrm{tr}\\,AB$")
    ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.6, 2.6); ax.set_zlim(-2.6, 2.6)
    ax.view_init(elev=20, azim=-52)
    ax.text2D(0.015, 0.95, "PROVED", transform=ax.transAxes, fontsize=8.5,
              fontweight="bold", color="white",
              bbox=dict(boxstyle="round,pad=0.3", fc=STATUS_COLORS["PROVED"],
                        ec="none"))
    ax.text2D(0.0, -0.02,
              r"the trace map preserves each $\kappa$-leaf $\kappa=x^2+y^2+z^2-xyz-2$;"
              "\n"
              r"the Markov leaf $\kappa=-2$ (four noncompact horns) is the degenerate fibre.",
              transform=ax.transAxes, fontsize=8.2, color="#555")
    _save(fig, "fig02_fricke_cubic")


# ----------------------------------------------------------------------------
# Fig 3 -- trace-map linearization at the void (saddle + Lyapunov spectrum)
# ----------------------------------------------------------------------------
def fig03():
    """The void fixed point: hyperbolic saddle + a marginal direction. Exponents from B109."""
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.9),
                             gridspec_kw={"width_ratios": [1.25, 1]})

    # (a) streamplot of a linear saddle with rates +/- 4 log phi
    r = 4.0 * np.log(PHI)
    ax = axes[0]
    g = np.linspace(-1.0, 1.0, 26)
    U, V = np.meshgrid(g, g)
    dU = r * U      # unstable
    dV = -r * V     # stable
    ax.streamplot(g, g, dU, dV, color=np.hypot(dU, dV), cmap="cividis",
                  density=1.1, linewidth=0.8, arrowsize=0.9)
    ax.set_xlabel("unstable direction")
    ax.set_ylabel("stable direction")
    ax.set_title("linearized trace map at the void")
    ax.set_aspect("equal")

    # (b) Lyapunov spectrum bar
    ax = axes[1]
    exps = [-r, 0.0, r]
    labels = [r"$-4\log\varphi$", r"$0$", r"$+4\log\varphi$"]
    colors = ["#1b3a5b", "#8c8c8c", "#b6411a"]
    ax.bar(range(3), exps, color=colors, width=0.6)
    ax.axhline(0, color="#333", lw=0.8)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labels)
    ax.set_ylabel("Lyapunov exponent")
    ax.set_title(r"spectrum $\{0,\pm 4\log\varphi\}$")
    for i, e in enumerate(exps):
        ax.annotate(f"{e:+.3f}", (i, e), textcoords="offset points",
                    xytext=(0, 6 if e >= 0 else -12), ha="center", fontsize=8)
    _badge(ax, "NUMERICAL", loc=(0.03, 0.07))

    fig.suptitle("The void as a hyperbolic saddle (one marginal direction)",
                 y=1.02, fontsize=12.5)
    _save(fig, "fig03_trace_map_dynamics")


# ----------------------------------------------------------------------------
# Fig 4 -- the Dickson tower factorization (n=2,3,4)
# ----------------------------------------------------------------------------
def fig04():
    """Factors char(+/- M^k) of the (n^2-1)-dim Jacobian, graded by parity. Data: B80."""
    data = _load_json("frontier/B80_sl4_adproof/jacobian_m_crt.json")
    assert data.get("matches_tower") is True

    # factor catalog per n (the proved towers); (k, sign): char(sign * M^k)
    towers = {
        2: [(1, +1)],
        3: [(1, -1), (2, +1), (3, +1)],
        4: [(1, -1), (1, +1), (2, +1), (3, +1), (4, +1), (2, -1)],
    }
    fig, ax = plt.subplots(figsize=(8.4, 4.0))
    for row, n in enumerate((2, 3, 4)):
        ax.axhline(row, color="#eee", lw=8, zorder=0)
        for (k, sign) in towers[n]:
            xpos = k if sign > 0 else -k
            parity = "even" if k % 2 == 0 else "odd"
            color = "#2e7d54" if parity == "even" else "#7a4f9e"
            marker = "o" if sign > 0 else "D"
            ax.scatter([xpos], [row], s=190, marker=marker, color=color,
                       edgecolor="#222", linewidth=1.0, zorder=4)
            lbl = ("-" if sign < 0 else "") + f"M^{k}" if k > 1 else \
                  ("-M" if sign < 0 else "M")
            ax.annotate(fr"$\chi({lbl})$", (xpos, row),
                        textcoords="offset points", xytext=(0, 12),
                        ha="center", fontsize=8.5)
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["SL(2)\n(dim 3)", "SL(3)\n(dim 8)", "SL(4)\n(dim 15)"])
    ax.set_xlabel(r"signed power $k$ of the monodromy $M$  (sign $=$ marker: $\circ\ +,\ \diamond\ -$)")
    ax.set_xlim(-3.5, 4.8)
    ax.set_ylim(-0.6, 2.7)
    ax.set_title(r"Dickson tower: $\det(tI-J(m))=\prod_k \chi(\pm M^{k})$")
    # parity legend
    from matplotlib.lines import Line2D
    leg = [Line2D([0], [0], marker="o", color="w", markerfacecolor="#2e7d54",
                  markeredgecolor="#222", markersize=10, label="even $|k|$ (P-symmetric)"),
           Line2D([0], [0], marker="o", color="w", markerfacecolor="#7a4f9e",
                  markeredgecolor="#222", markersize=10, label="odd $|k|$ (P-antisymmetric)")]
    ax.legend(handles=leg, loc="lower right")
    _badge(ax, "PROVED")
    _save(fig, "fig04_dickson_tower")


# ----------------------------------------------------------------------------
# Fig 5 -- opposition involution on the A_2 weight lattice
# ----------------------------------------------------------------------------
def fig05():
    """theta = -w0 acting on the A_2 (SL(3)) weight lattice; the parity grading."""
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    # A_2 simple roots
    a1 = np.array([1.0, 0.0])
    a2 = np.array([-0.5, np.sqrt(3) / 2])
    pts = {}
    for i in range(-3, 4):
        for j in range(-3, 4):
            p = i * a1 + j * a2
            if np.linalg.norm(p) <= 2.7:
                pts[(i, j)] = p
    P = np.array(list(pts.values()))
    ax.scatter(P[:, 0], P[:, 1], s=22, color="#cfcfcf", zorder=1)

    # roots (the hexagon)
    roots = [a1, a2, a1 + a2, -a1, -a2, -(a1 + a2)]
    for r in roots:
        ax.annotate("", xy=r, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color="#1b3a5b", lw=1.6))
    # -w0 for A_2 is the reflection through the vertical axis (swap a1<->a2)
    ax.axvline(0, color="#b6411a", ls="--", lw=1.4)
    ax.annotate(r"$\theta=-w_0$ (mirror)", (0.06, 2.45), color="#b6411a",
                fontsize=10)
    # a sample weight and its image
    w = 2 * a1 + a2
    wI = np.array([-w[0], w[1]])
    for q, c, lab in [(w, "#2e7d54", r"$\mu$"), (wI, "#7a4f9e", r"$-w_0\mu$")]:
        ax.scatter([q[0]], [q[1]], s=90, color=c, edgecolor="#222", zorder=5)
        ax.annotate(lab, q, textcoords="offset points", xytext=(8, 6),
                    fontsize=11, color=c)
    ax.annotate("", xy=wI, xytext=w,
                arrowprops=dict(arrowstyle="-|>", color="#888", lw=1.2,
                                connectionstyle="arc3,rad=0.25"))
    ax.set_aspect("equal")
    ax.set_xlim(-2.9, 2.9)
    ax.set_ylim(-2.9, 2.9)
    ax.set_title(r"Opposition involution $\theta=-w_0$ on the $A_2$ weight lattice")
    ax.set_xlabel("even $|k|$ fixed (symmetric) $\\cdot$ odd $|k|$ flipped (antisymmetric)")
    _badge(ax, "PROVED")
    _save(fig, "fig05_opposition_involution")


# ----------------------------------------------------------------------------
# Fig 6 -- the figure-eight A-polynomial curve (SL(2), Cooper-Long)
# ----------------------------------------------------------------------------
def fig06():
    """A(M,L)=M^4 L^2 + (-M^8+M^6+2M^4+M^2-1)L + M^4: real branches in (M,L)."""
    M = np.linspace(0.2, 2.2, 1400)
    A = M ** 4
    B = -M ** 8 + M ** 6 + 2 * M ** 4 + M ** 2 - 1
    C = M ** 4
    disc = B * B - 4 * A * C
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    real = disc >= 0
    sq = np.sqrt(np.where(real, disc, np.nan))
    for sign, c in ((+1, "#1b3a5b"), (-1, "#b6411a")):
        L = (-B + sign * sq) / (2 * A)
        ax.plot(M, L, color=c, lw=1.8,
                label=fr"$L_{{{'+'if sign>0 else '-'}}}(M)$")
    # complex region: plot |L| (both roots share modulus there)
    comp = ~real
    modL = np.sqrt(np.where(comp, C / A, np.nan))  # |L| = sqrt(C/A) = 1
    ax.plot(M, modL, color="#8c8c8c", ls=":", lw=1.4, label=r"$|L|$ (complex $L$)")
    ax.axhline(1, color="#ddd", lw=0.6)
    ax.set_yscale("log")
    ax.set_xlabel(r"meridian eigenvalue $M$")
    ax.set_ylabel(r"longitude eigenvalue $L$")
    ax.set_title(r"Figure-eight $A$-polynomial (Cooper--Long, 1996) from $\mathrm{Fix}(T_1^2)$")
    ax.legend(loc="upper center", ncol=3)
    _badge(ax, "KNOWN")
    _save(fig, "fig06_apolynomial_sl2")


# ----------------------------------------------------------------------------
# Fig 7 -- the SL(3) character variety: three components
# ----------------------------------------------------------------------------
def fig07():
    """Schematic of the SL(3) figure-eight character variety (Falbel / HMP)."""
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.set_axis_off()

    # V0 geometric blob (Sym^2 of the SL(2) component)
    from matplotlib.patches import Ellipse
    v0 = Ellipse((0.30, 0.55), 0.42, 0.42, facecolor="#2e7d54", alpha=0.22,
                 edgecolor="#2e7d54", lw=1.8)
    ax.add_patch(v0)
    ax.text(0.30, 0.55, r"$V_0$" + "\ngeometric\n($\\mathrm{Sym}^2$, dim 2)",
            ha="center", va="center", fontsize=10, color="#1c5c3c")

    # W1, W2 Dehn-filling components
    for (cx, cy, name, eqn, col) in [
        (0.74, 0.74, r"$W_1$", r"$M^3=L$", "#1b3a5b"),
        (0.74, 0.34, r"$W_2$", r"$M^3 L=1$", "#7a4f9e"),
    ]:
        e = Ellipse((cx, cy), 0.34, 0.26, facecolor=col, alpha=0.18,
                    edgecolor=col, lw=1.8)
        ax.add_patch(e)
        ax.text(cx, cy + 0.03, name, ha="center", fontsize=11, color=col)
        ax.text(cx, cy - 0.05, eqn + "\n(Dehn filling, dim 2)", ha="center",
                fontsize=9, color=col)

    ax.text(0.5, 0.04,
            "Three components reproduced exactly by the trace map (matches Falbel/HMP); "
            "the boundary $A$-variety is $M^3=L$ and $M^3L=1$.",
            ha="center", fontsize=8.5, color="#555")
    ax.set_xlim(0, 1.05)
    ax.set_ylim(0, 1)
    ax.set_title(r"SL(3) figure-eight character variety: the degree$=$rank base case")
    ax.text(0.015, 0.93, "KNOWN", transform=ax.transAxes, fontsize=8.5,
            fontweight="bold", color="white",
            bbox=dict(boxstyle="round,pad=0.3", fc=STATUS_COLORS["KNOWN"], ec="none"))
    _save(fig, "fig07_sl3_character_variety")


# ----------------------------------------------------------------------------
# Fig 8 -- the A_n family: slope = rank
# ----------------------------------------------------------------------------
def fig08():
    """L = (-1)^{n-1} M^n on the principal component: |L| vs |M| in log-log."""
    M = np.linspace(1.02, 2.2, 400)
    fig, ax = plt.subplots(figsize=(7.4, 4.8))
    specs = [
        (2, "#8c8c8c", "-", "SL(2) Cooper--Long  (slope 2)", "KNOWN"),
        (3, "#1b3a5b", "-", r"SL(3) Falbel  $L=+M^3$  (slope 3)", "KNOWN"),
        (4, "#b6411a", "--", r"SL(4)  $L=-M^4$  (slope 4)", "GATED"),
        (5, "#7a4f9e", ":", r"SL(5)  $L=+M^5$  (predicted)", "GATED"),
    ]
    for n, c, ls, lab, _ in specs:
        ax.plot(np.log(M), n * np.log(M), ls, color=c, lw=2.0, label=lab)
    ax.set_xlabel(r"$\log |M|$  (meridian)")
    ax.set_ylabel(r"$\log |L|$  (longitude)")
    ax.set_title(r"The $A_n$ family $L=(-1)^{n-1}M^{n}$ : exponent $=$ rank")
    ax.legend(loc="upper left")
    ax.text(0.97, 0.06,
            "GATED:  n=3 known (Falbel);  n=4 APPEARS-NOVEL,\n"
            "NEEDS-SPECIALIST;  n$\\geq$5 conjectural",
            transform=ax.transAxes, fontsize=8.5, color="#b6411a", ha="right",
            bbox=dict(boxstyle="round,pad=0.35", fc="#fff3ee", ec="#b6411a", lw=1.2))
    _save(fig, "fig08_an_family_slope_rank")


# ----------------------------------------------------------------------------
# Fig 9 -- the SL(4) ideal stratification (completeness)
# ----------------------------------------------------------------------------
def fig09():
    """Gauge-rank strata: only rankQ2 (B89) carries irreducible reps; all satisfy M^4=L. Data: B149."""
    d = _load_json("frontier/B149_sl4_ideal_completeness/irreducibility_fp.json")
    strata = d["per_stratum"]
    names, irr, redL, redN = [], [], [], []
    order = ["rankQ2 (Q=I2,B89)", "rankQ1 [[1,1],[0,0]]", "rankQ0 (Q=0)",
             "rankQ1 [[1,0],[0,0]]", "rankQ1 [[0,1],[0,0]]"]
    pretty = {
        "rankQ2 (Q=I2,B89)": "rank $Q$=2\n(B89 family)",
        "rankQ1 [[1,1],[0,0]]": "rank $Q$=1\n$[[1,1],[0,0]]$",
        "rankQ0 (Q=0)": "rank $Q$=0\n($\\det t=0$)",
        "rankQ1 [[1,0],[0,0]]": "rank $Q$=1\n$[[1,0],[0,0]]$",
        "rankQ1 [[0,1],[0,0]]": "rank $Q$=1\n$[[0,1],[0,0]]$",
    }
    for k in order:
        s = strata[k]
        names.append(pretty[k])
        irr.append(s["irr&M4=L"] + s["irr&M4!=L"])
        redL.append(s["red&M4=L"])
        redN.append(s["red&M4!=L"])
    y = np.arange(len(names))
    fig, ax = plt.subplots(figsize=(8.2, 4.4))
    ax.barh(y, irr, color="#2e7d54", label="irreducible ($M^4{=}L$)")
    ax.barh(y, redL, left=irr, color="#9ec6b0", label="reducible ($M^4{=}L$)")
    ax.barh(y, redN, left=np.array(irr) + np.array(redL), color="#d9d9d9",
            label="reducible / vacuous ($M^4{\\neq}L$)")
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=8.5)
    ax.invert_yaxis()
    ax.set_xlabel("number of sampled $\\mathbb{F}_p$ representations (Burnside test)")
    ax.set_title(r"SL(4) completeness: the irreducible locus $=$ the B89 family")
    ax.legend(loc="lower right")
    ax.annotate("only stratum with\nirreducible reps", (12, 0),
                textcoords="offset points", xytext=(14, 0), va="center",
                fontsize=8.5, color="#2e7d54",
                arrowprops=dict(arrowstyle="->", color="#2e7d54"))
    _badge(ax, "PROVED", loc=(0.015, 0.07))
    _save(fig, "fig09_sl4_stratification")


# ----------------------------------------------------------------------------
# Fig 10 -- the chirality census (palindrome criterion)
# ----------------------------------------------------------------------------
def fig10():
    """Block-length sequences (m1,...,mk): cyclic palindrome <=> amphichiral."""
    def is_cyclic_palindrome(seq):
        rev = seq[::-1]
        return any(rev == seq[i:] + seq[:i] for i in range(len(seq)))

    # enumerate compositions with entries in {1,2,3} of length 1..3
    rows = []
    for L in (1, 2, 3):
        from itertools import product
        for seq in product((1, 2, 3), repeat=L):
            rows.append(tuple(seq))
    # dedup cyclic rotations (keep lexicographically minimal rotation)
    def canon(s):
        return min(s[i:] + s[:i] for i in range(len(s)))
    seen, uniq = set(), []
    for s in rows:
        c = canon(s)
        if c not in seen:
            seen.add(c)
            uniq.append(c)
    uniq.sort(key=lambda s: (len(s), s))

    grid = np.zeros((len(uniq), 1))
    labels = []
    arith = {(1,): r"$\mathbb{Q}(\sqrt{-3})$", (2,): r"$\mathbb{Q}(i)$"}
    for i, s in enumerate(uniq):
        amph = is_cyclic_palindrome(list(s))
        grid[i, 0] = 1.0 if amph else 0.0
        tag = "".join(f"$R^{{{m}}}L^{{{m}}}$" if m > 1 else "$RL$" for m in s)
        labels.append(tag)

    fig, ax = plt.subplots(figsize=(5.6, 6.4))
    ax.imshow(grid, aspect="auto", cmap=matplotlib.colors.ListedColormap(
        ["#f3d9cf", "#cfe6da"]), vmin=0, vmax=1)
    ax.set_xticks([])
    ax.set_yticks(range(len(uniq)))
    ax.set_yticklabels(labels, fontsize=8.5)
    for i, s in enumerate(uniq):
        amph = is_cyclic_palindrome(list(s))
        ax.text(0, i, "amphichiral" if amph else "chiral", ha="center",
                va="center", fontsize=8,
                color="#1c5c3c" if amph else "#8a3415")
        # arithmetic annotation for the canonical singles + the chiral pair
        note = arith.get(s)
        if note:
            ax.text(0.62, i, note, ha="left", va="center", fontsize=7.5,
                    color="#555", transform=ax.get_yaxis_transform())
    # the RRL/RLL chiral arithmetic pair (length-3 mixed) -- annotate one
    ax.set_title("Chirality census:\ncyclic palindrome $\\Leftrightarrow$ amphichiral",
                 fontsize=11)
    ax.text(0.5, -0.04,
            r"chiral arithmetic pair $RRL/RLL\in\mathbb{Q}(\sqrt{-7})$ refutes "
            r"`arithmetic $\Rightarrow$ amphichiral'",
            transform=ax.transAxes, ha="center", fontsize=7.6, color="#8a3415")
    ax.text(0.015, 0.985, "PROVED", transform=ax.transAxes, fontsize=8.5,
            fontweight="bold", color="white", va="top",
            bbox=dict(boxstyle="round,pad=0.3", fc=STATUS_COLORS["PROVED"], ec="none"))
    _save(fig, "fig10_chirality_census")


# ----------------------------------------------------------------------------
# Fig 11 -- the metallic Schrodinger cocycle: Cantor spectrum
# ----------------------------------------------------------------------------
def fig11():
    """Fibonacci Hamiltonian spectrum vs coupling V (the object's proper name, K010)."""
    def fib(n):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def potential(N, alpha=1.0 / PHI):
        # characteristic Fibonacci potential v_n = chi_{[1-alpha,1)}(n*alpha mod 1)
        n = np.arange(1, N + 1)
        frac = (n * alpha) % 1.0
        return np.where(frac >= (1.0 - alpha), 1.0, 0.0)

    def spectrum_at(V, period, energies):
        v = potential(period)
        allowed = np.zeros_like(energies, dtype=bool)
        for j, E in enumerate(energies):
            T = np.eye(2)
            for n in range(period):
                t = np.array([[E - V * v[n], -1.0], [1.0, 0.0]])
                T = t @ T
            allowed[j] = abs(np.trace(T)) <= 2.0
        return allowed

    period = fib(10)  # 89
    energies = np.linspace(-4.0, 4.0, 2600)
    couplings = np.linspace(0.0, 3.0, 130)

    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    xs, ys = [], []
    for V in couplings:
        allowed = spectrum_at(V, period, energies)
        e = energies[allowed]
        xs.append(np.full_like(e, V))
        ys.append(e)
    X = np.concatenate(xs)
    Y = np.concatenate(ys)
    ax.scatter(X, Y, s=0.25, color="#1b3a5b", marker=".", linewidths=0)
    ax.set_xlabel("coupling $V$")
    ax.set_ylabel("energy $E$ (spectrum)")
    ax.set_title("Metallic Schrödinger cocycle: the Fibonacci Cantor spectrum")
    ax.annotate("Cantor set\n(gaps open as $V$ grows)", (2.2, 3.0), fontsize=8.5,
                color="#444")
    _badge(ax, "NUMERICAL")
    _save(fig, "fig11_cantor_spectrum")


# ----------------------------------------------------------------------------
# Fig 12 -- the bridge and the wall
# ----------------------------------------------------------------------------
def fig12():
    """Schematic: the FORCED symmetry bridge and the CONFIRMED dimensional wall."""
    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    def box(x, y, w, h, text, fc, ec, fs=9):
        p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012",
                           fc=fc, ec=ec, lw=1.6)
        ax.add_patch(p)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=fs, color="#222")

    def arrow(x0, y0, x1, y1, c="#2e7d54"):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1),
                     arrowstyle="-|>", mutation_scale=16, lw=1.8, color=c))

    # the bridge (left)
    ax.text(0.24, 0.96, "THE BRIDGE  (FORCED)", ha="center", fontsize=11,
            color="#2e7d54", fontweight="bold")
    box(0.04, 0.70, 0.40, 0.13,
        r"metallic trace map" + "\n" + r"$\mathrm{SL}(2,\mathbb{Z})$ on $\kappa=x^2+y^2+z^2-xyz-2$",
        "#eaf4ee", "#2e7d54")
    box(0.04, 0.46, 0.40, 0.13,
        "mapping class group\nof the once-punctured torus", "#eaf4ee", "#2e7d54")
    box(0.04, 0.22, 0.40, 0.13,
        r"$\mathcal{N}=2^{*}$ class-$S$ S-duality" + "\n(Allegretti--Shan)",
        "#eaf4ee", "#2e7d54")
    arrow(0.24, 0.70, 0.24, 0.595)
    arrow(0.24, 0.46, 0.24, 0.355)
    ax.text(0.24, 0.12, "same group, same action,\nsame character variety",
            ha="center", fontsize=8.5, color="#1c5c3c", style="italic")

    # the wall (right)
    ax.text(0.76, 0.96, "THE WALL  (CONFIRMED)", ha="center", fontsize=11,
            color="#b6411a", fontweight="bold")
    ax.add_patch(Rectangle((0.545, 0.08), 0.012, 0.82, fc="#b6411a",
                           ec="none", alpha=0.6))
    box(0.60, 0.58, 0.37, 0.16,
        r"complex volume $\widehat{c}(\rho)=i(\mathrm{Vol}+iCS)$" + "\n" +
        r"$\in \mathbb{C}/4\pi^2\mathbb{Z}$  (dimensionless)",
        "#fbede6", "#b6411a")
    box(0.60, 0.34, 0.37, 0.14,
        "the scale lives in $\\hbar\\leftrightarrow k$\nand the squashing radius",
        "#fbeae0", "#b6411a")
    box(0.60, 0.12, 0.37, 0.13,
        r"figure-eight: $\mathrm{Vol}=2.0299,\ CS=0$" + "\nthe scale-carrier vanishes",
        "#fbeae0", "#b6411a")
    ax.text(0.5, 0.015,
            "A symmetry identity is not a scale.  Structure crosses; magnitude does not.",
            ha="center", fontsize=9, color="#444")
    _save(fig, "fig12_bridge_and_wall")


ALL = [fig01, fig02, fig03, fig04, fig05, fig06, fig07, fig08, fig09, fig10,
       fig11, fig12]


def main(argv):
    targets = argv[1:]
    funcs = {f.__name__: f for f in ALL}
    if targets:
        chosen = [funcs[t] for t in targets]
    else:
        chosen = ALL
    for f in chosen:
        print(f"[{f.__name__}] {f.__doc__.splitlines()[0] if f.__doc__ else ''}")
        f()
    print(f"done: {len(chosen)} figure(s) -> {OUT}")


if __name__ == "__main__":
    main(sys.argv)
