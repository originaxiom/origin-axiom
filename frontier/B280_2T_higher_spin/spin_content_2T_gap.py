"""B280 -- the 2T (binary tetrahedral = SL(2,3)) higher-spin content. Run with sage-python (needs GAP).

Decomposes the SU(2) spin-j irreps restricted to 2T = SL(2,3) (spin-1/2 = the faithful quaternionic 2-dim irrep,
FS indicator -1; spin-j = Sym^{2j} of it). Headline NEGATIVE: spin-3/2 splits as 2+2 (two distinct 2-dim irreps),
NOT 3+1 -- so there is no triplet+singlet, killing 'three generations + a Higgs from the A_4/2T spin-3/2'.
"""
from sage.all import gap


def decompositions():
    gap.eval("G := SL(2,3);; t := CharacterTable(G);; irr := Irr(t);;")
    dims = [int(d) for d in gap.eval("List(irr, x->x[1]);").replace("[", "").replace("]", "").split(",")]
    # spin-1/2 = faithful 2-dim irrep with FS indicator -1 (quaternionic; 2T subset SU(2)=Sp(1))
    gap.eval("two := Filtered(irr, x->x[1]=2);;")
    gap.eval("chi := First(two, x->Indicator(t,[x],2)[1] = -1);;")   # the quaternionic one
    gap.eval("n := NrConjugacyClasses(t);; p2 := PowerMap(t,2);; p3 := PowerMap(t,3);;")
    gap.eval("sym2 := List([1..n], i -> (chi[i]^2 + chi[p2[i]])/2);;")               # spin-1  = Sym^2
    gap.eval("sym3 := List([1..n], i -> (chi[i]^3 + 3*chi[i]*chi[p2[i]] + 2*chi[p3[i]])/6);;")  # spin-3/2 = Sym^3
    gap.eval("c2 := Character(t, sym2);; c3 := Character(t, sym3);;")
    spin1 = [int(x) for x in gap.eval("MatScalarProducts(t, irr, [c2])[1];").strip("[]").split(",")]
    spin32 = [int(x) for x in gap.eval("MatScalarProducts(t, irr, [c3])[1];").strip("[]").split(",")]
    return dims, spin1, spin32


if __name__ == "__main__":
    dims, spin1, spin32 = decompositions()
    print("2T irrep dims:", dims)                       # [1,1,1,2,2,2,3]
    print("spin-1   |2T  multiplicities:", spin1)        # -> the 3 (rho_3)
    print("spin-3/2 |2T  multiplicities:", spin32)       # -> 2+2 (two distinct 2-dim irreps), NOT 3+1
    # spin-1 = the single 3-dim irrep:
    assert sum(m * d for m, d in zip(spin1, dims)) == 3 and spin1[dims.index(3)] == 1
    # spin-3/2 = exactly two distinct 2-dim irreps, each once; NO 3 and NO 1:
    two_idx = [i for i, d in enumerate(dims) if d == 2]
    assert sum(spin32[i] for i in two_idx) == 2 and all(spin32[i] in (0, 1) for i in two_idx)
    assert spin32[dims.index(3)] == 0 and all(spin32[i] == 0 for i, d in enumerate(dims) if d == 1)
    print("OK: spin-1=rho_3 ; spin-3/2 = 2+2 (NOT 3+1) -> no triplet+singlet.")
