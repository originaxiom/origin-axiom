"""Figure: the chain and its prices -- what is forced, what is stated as an input (on the right), and what is open."""
from _style import *
from matplotlib.patches import FancyBboxPatch
chain = [("non-cancellation (the principle)", "stated"), ("the grammar: records, moves, pull-backs", "stated"),
         ("the seed $A=LR$ (unique under four inputs)", "forced"), ("the weave: every thread at once", "forced"),
         ("the triplet $T$; $2T$ at the common point", "forced"), ("its symmetry: $\\Gamma(4)$'s weight-one theta triplet", "forced"),
         ("couplings: isotropy; the joint law", "forced"), ("a chiral index $\\pm3$", "given"), ("the numbers of the Standard Model", "open")]
inputs = {1: "GM1--GM5 (GM5b adopted)", 2: "SE1, SE2", 6: "the frame; the hypercharge dictionary",
          7: "the triplet postulate; one cusp unit", 8: "the Higgs, $\\tau$, the line, $L$, the side, the read-out"}
col = {"forced": OI["green"], "stated": OI["orange"], "given": OI["sky"], "open": OI["grey"]}
fig, ax = plt.subplots(figsize=(6.0, 5.0)); ax.set_xlim(0, 10); ax.set_ylim(-1.0, len(chain) + 0.2); ax.axis("off")
for i, (lab, st) in enumerate(chain):
    y = len(chain) - 1 - i
    ax.add_patch(FancyBboxPatch((0.2, y - 0.32), 5.2, 0.64, boxstyle="round,pad=0.02", fc=col[st], ec="black", lw=0.6, alpha=0.8))
    ax.text(2.8, y, lab, ha="center", va="center", fontsize=7.5)
    if i < len(chain) - 1: ax.annotate("", (2.8, y - 0.36), (2.8, y - 0.64), arrowprops=dict(arrowstyle="<-", lw=0.7))
    if i in inputs:
        ax.annotate("", (5.45, y), (6.1, y), arrowprops=dict(arrowstyle="->", lw=0.6, color=OI["vermillion"]))
        ax.text(6.2, y, inputs[i], ha="left", va="center", fontsize=7, color=OI["vermillion"])
ax.text(0.2, -0.85, "forced (green) $\\cdot$ stated (orange) $\\cdot$ given two inputs (blue) $\\cdot$ open (grey); "
        "price: 4 axioms + 9 irreducible identifications = 13; 0 of 19", fontsize=6.6)
save(fig, "fig_chain", "the record's GENESIS v1.48 and identification ledger (drawn)")
