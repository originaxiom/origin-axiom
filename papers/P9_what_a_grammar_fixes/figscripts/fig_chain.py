"""Figure: the chain and its prices -- what follows from stated inputs, what is stated, what needs further tagged postulates, and what is open."""
from _style import *
from matplotlib.patches import FancyBboxPatch
chain = [("non-cancellation (the principle)", "stated"), ("the grammar: records, moves, pull-backs", "stated"),
         ("the weave: every thread at once", "forced"),
         ("the triplet $T$; $2T$ at the common point", "forced"), ("its symmetry: $\\Gamma(4)$'s weight-one theta triplet", "forced"),
         ("couplings: isotropy; the joint law", "given"), ("a chiral index $\\pm3$", "given"), ("the numbers of the Standard Model", "open")]
inputs = {1: "GM1--GM5 (GM5b adopted); positivity", 3: "the prime above 3: a census to length eight", 4: "the hand; the $\\eta$ twist",
          5: "the triplet postulate; the fibre frame;\nthe Higgs's locus", 6: "the triplet postulate; one cusp unit;\nthe extreme domain; $M_{1,2}$; the index formula",
          7: "the Higgs, $\\tau$, the line, the horocycle,\nthe side, the read-out, the dictionary"}
col = {"forced": OI["green"], "stated": OI["orange"], "given": OI["sky"], "open": OI["grey"]}
fig, ax = plt.subplots(figsize=(6.0, 5.4)); ax.set_xlim(0, 10); ax.set_ylim(-1.3, len(chain) + 0.2); ax.axis("off")
for i, (lab, st) in enumerate(chain):
    y = len(chain) - 1 - i
    ax.add_patch(FancyBboxPatch((0.2, y - 0.32), 5.2, 0.64, boxstyle="round,pad=0.02", fc=col[st], ec="black", lw=0.6, alpha=0.8))
    ax.text(2.8, y, lab, ha="center", va="center", fontsize=7.5)
    if i < len(chain) - 1: ax.annotate("", (2.8, y - 0.36), (2.8, y - 0.64), arrowprops=dict(arrowstyle="<-", lw=0.7))
    if i in inputs:
        ax.annotate("", (5.45, y), (6.1, y), arrowprops=dict(arrowstyle="->", lw=0.6, color=OI["vermillion"]))
        ax.text(6.2, y, inputs[i], ha="left", va="center", fontsize=6.6, color=OI["vermillion"])
# the seed is a side branch of the grammar, not a premise of what follows
yg = len(chain) - 2
ax.add_patch(FancyBboxPatch((6.2, yg - 1.0 - 0.32), 3.6, 0.64, boxstyle="round,pad=0.02", fc=OI["green"], ec="black", lw=0.6, alpha=0.8, ls="--"))
ax.text(8.0, yg - 1.0 + 0.08, "side branch: the seed $A=LR$", ha="center", va="center", fontsize=7)
ax.text(8.0, yg - 1.0 - 0.14, "(four inputs: GM3, GM4, SE1, SE2)", ha="center", va="center", fontsize=6.3)
ax.annotate("", (6.2, yg - 1.0), (5.45, yg - 0.15), arrowprops=dict(arrowstyle="<-", lw=0.6, ls="--"))
ax.text(0.2, -0.85, "green: follows from the stated inputs of its section $\\cdot$ orange: stated $\\cdot$ blue: also needs tagged postulates $\\cdot$ grey: open",
        fontsize=6.4)
ax.text(0.2, -1.2, "for comparison, the record prices its whole chain at four axioms and nine irreducible identifications; this paper derives 0 of 19", fontsize=6.4)
save(fig, "fig_chain", "the record's identification ledger (drawn)")
