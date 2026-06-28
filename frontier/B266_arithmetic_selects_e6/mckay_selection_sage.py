"""B266 reproducibility -- the McKay graphs of the binary polyhedral groups (run with sage-python, uses libgap).
Builds, from GAP character tables, the McKay graph of each binary polyhedral group G (adjacency
A[i][j] = mult of chi_j in chi_i (x) V, V = a faithful 2-dim irrep) and reports node count / valences / marks.

Confirms:  SL(2,3)=2T -> affine E6 ;  SL(2,5)=2I -> affine E8 ;  SmallGroup(48,28)=2O -> affine E7.
And: 2O is NEVER isomorphic to any SL(2,q)  (|2O|=48 is not an SL(2,q) order q(q^2-1)).
Results hard-coded into arithmetic_selects_e6.py (MCKAY)."""
from sage.all import libgap


def mckay_graph(G):
    ct = G.CharacterTable(); irr = ct.Irr(); n = len(irr)
    dims = [int(c[0]) for c in irr]
    faith = [i for i in range(n) if dims[i] == 2 and int(libgap.KernelOfCharacter(irr[i]).Size()) == 1]
    V = irr[faith[0]]
    A = [[int(libgap.ScalarProduct(ct, irr[i] * V, irr[j])) for j in range(n)] for i in range(n)]
    deg = sorted(sum(r) for r in A)
    return {"nodes": n, "edges": sum(sum(r) for r in A) // 2, "valences": deg, "marks": sorted(dims)}


if __name__ == "__main__":
    GROUPS = [("SL(2,3)=2T", libgap.SL(2, 3), "affine E6"),
              ("SL(2,5)=2I", libgap.SL(2, 5), "affine E8"),
              ("SmallGroup(48,28)=2O", libgap.SmallGroup(48, 28), "affine E7")]
    for lab, G, exp in GROUPS:
        g = mckay_graph(G)
        print(f"{lab:24} |G|={int(G.Size()):>3}  McKay: {g['nodes']} nodes, {g['edges']} edges, "
              f"valences={g['valences']}, marks={g['marks']}   (expect {exp})")
    twoO = libgap.SmallGroup(48, 28)
    print("\n2O ~ SL(2,q) for some q?",
          any(bool(libgap.IsomorphismGroups(libgap.SL(2, q), twoO) != libgap.fail) for q in [2, 3, 4, 5, 7, 8, 9]),
          "  (|2O|=48 not an SL(2,q) order -> E7 has no prime-reduction home)")
