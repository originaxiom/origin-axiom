"""B1423: the McKay door, verified end to end — the step the chain had as prose and not as a link.

Q(sqrt-3) --(unique ramified prime)--> 3 --(residue field)--> F_3 --(surjection)--> SL(2,3) = 2T
       --(McKay graph of the faithful 2-dim rep)--> the affine E6 diagram.

Four checks, each able to fail:
  (1) the discriminant of Q(sqrt-3) is -3 and (sqrt-3)^2 = (3), so 3 is the unique ramified prime,
      with residue field of order 3;
  (2) pi_1(m004) surjects onto SL(2,3), and the number of such surjections up to Aut is 2;
  (3) the McKay graph of SL(2,3) with respect to a faithful 2-dimensional representation is the
      affine E6 diagram: 7 nodes, 6 edges, valencies {1,1,1,2,2,2,3}, marks (the irreducible
      degrees) {1,1,1,2,2,2,3};
  (4) CONTROLS, so the criterion can fail: the same construction on the binary dihedral group of
      order 8 gives affine D4 (5 nodes), and pi_1(m004) has NO surjection onto SL(2,5) = 2I.
Run: sage -python mckay_door.py
"""
from sage.all import QuadraticField, libgap
import snappy


def arithmetic_step():
    K = QuadraticField(-3, 's')
    disc = int(K.discriminant())
    fac = K.ideal(3).factor()
    ram = [(P, e) for P, e in fac]
    I = K.ideal(K.gen())
    return {"disc": disc, "ramified_exponent": int(ram[0][1]), "n_primes_over_3": len(ram),
            "residue_field_order": int(I.norm())}


def quotient_step():
    M = snappy.Manifold("m004")
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    libgap.eval("F := FreeGroup(%s)" % ",".join('"%s"' % g for g in gens))
    libgap.eval("g := GeneratorsOfGroup(F)")

    def word(w):
        return "*".join("g[%d]%s" % (gens.index(c.lower()) + 1, "" if c.islower() else "^-1") for c in w)

    libgap.eval("G := F/[%s]" % ",".join(word(r) for r in rels))
    return {"onto_SL23": int(libgap.eval("Length(GQuotients(G, SL(2,3)))")),
            "onto_SL25": int(libgap.eval("Length(GQuotients(G, SL(2,5)))"))}


def mckay_graph(group_gap):
    libgap.eval("H := %s" % group_gap)
    libgap.eval("t := CharacterTable(H)")
    libgap.eval("irr := Irr(t)")
    n = int(libgap.eval("Length(irr)"))
    degs = [int(libgap.eval("irr[%d][1]" % (i + 1))) for i in range(n)]
    # a faithful representation of the smallest degree > 1 (the McKay rep)
    libgap.eval("two := First(irr, x -> x[1] > 1 and Length(ClassPositionsOfKernel(x)) = 1)")
    A = [[int(libgap.eval("ScalarProduct(t, irr[%d]*two, irr[%d])" % (i + 1, j + 1))) for j in range(n)]
         for i in range(n)]
    edges = sum(1 for i in range(n) for j in range(i + 1, n) if A[i][j])
    valency = sorted(sum(row) for row in A)
    return {"nodes": n, "edges": edges, "valencies": valency, "marks": sorted(degs)}


if __name__ == "__main__":
    a = arithmetic_step()
    print("(1) Q(sqrt-3): disc %d; 3 = (sqrt-3)^%d with %d prime above it; residue field order %d"
          % (a["disc"], a["ramified_exponent"], a["n_primes_over_3"], a["residue_field_order"]))
    q = quotient_step()
    print("(2) pi_1(m004) ->> SL(2,3) up to Aut: %d   | ->> SL(2,5): %d" % (q["onto_SL23"], q["onto_SL25"]))
    m = mckay_graph("SL(2,3)")
    print("(3) McKay(2T): nodes %d, edges %d, valencies %s, marks %s"
          % (m["nodes"], m["edges"], m["valencies"], m["marks"]))
    affine_e6 = (m["nodes"] == 7 and m["edges"] == 6
                 and m["valencies"] == [1, 1, 1, 2, 2, 2, 3] and m["marks"] == [1, 1, 1, 2, 2, 2, 3])
    print("    is the affine E6 diagram:", affine_e6)
    c = mckay_graph("SmallGroup(8,4)")          # the quaternion group Q8 = binary dihedral -> affine D4
    print("(4) CONTROL McKay(Q8): nodes %d, edges %d, valencies %s -> affine D4 (5 nodes):"
          % (c["nodes"], c["edges"], c["valencies"]), c["nodes"] == 5)
    print("    CONTROL no 2I quotient:", q["onto_SL25"] == 0)
    print("DOOR VERIFIED:", a["residue_field_order"] == 3 and q["onto_SL23"] == 2 and affine_e6
          and c["nodes"] == 5 and q["onto_SL25"] == 0)
