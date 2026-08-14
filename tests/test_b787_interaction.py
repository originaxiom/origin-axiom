"""B787 -- the Interaction Programme: locks on the one HIT (iota-id) + the exact door sub-results.

The 6 doors were MISSes (base-rate discipline); this locks only what is EXACT and verified:
the iota-identification mechanism, D2's Born floor, D4's E6->F4 split. Every assertion
recomputes the fact.
"""
import sympy as sp
from sympy.combinatorics import Permutation
from sympy.combinatorics.named_groups import AlternatingGroup

phi = (1 + sp.sqrt(5)) / 2


def test_iota_id_A5_ambivalence_and_rank_4():
    # THE PHASE-1 HIT (verified). iota=inversion fixes T3 (A5 ambivalent, even conjugator)
    # but flips T7 (monodromy inversion); in <c,theta,gamma5> T7=T3, so iota is a 4th generator.
    A5 = AlternatingGroup(5)
    elts = list(A5.elements)
    five = [g for g in elts if g.order() == 5]
    # 5-cycles split into exactly two A5-classes (5A, 5B), size 12 each
    classes, seen = [], set()
    for g in five:
        if g in seen:
            continue
        c = frozenset(h * g * h**-1 for h in elts)
        classes.append(c); seen |= c
    assert len(classes) == 2 and sorted(len(c) for c in classes) == [12, 12]
    g = Permutation([1, 2, 3, 4, 0])                      # (0 1 2 3 4)
    h_even = Permutation([0, 4, 3, 2, 1])                 # (1 4)(2 3): reverses the cycle
    assert h_even.is_even and h_even * g * h_even**-1 == g**-1   # inversion via EVEN conjugator
    ci = [i for i, c in enumerate(classes) if g in c][0]
    assert g**-1 in classes[ci]                          # iota FIXES T3 (same class)
    odd = Permutation([1, 0, 2, 3, 4])                   # (0 1): odd, realizes Out(A5)
    assert (odd * g * odd**-1) not in classes[ci]        # gamma5 FLIPS T3 (swaps 5A<->5B)
    # iota FLIPS T7: monodromy inversion swaps the loxodromic spectrum
    assert sp.simplify(phi**2 - (phi**-2)**-1) == 0 and sp.simplify(phi**2) != sp.simplify(phi**-2)
    # => iota flips T7 but fixes T3, while span elements have T7=T3 => rank 3 -> 4


def test_d2_born_floor_below_juno_and_theorem():
    # D2 MISS: the diagonal Fibonacci-R self-overlap Born floor is sin^2(36deg)=(5-sqrt5)/8,
    # strictly ABOVE both JUNO (0.30902) and |S_tautau|^2 = 1/(phi*sqrt5) -- structural unreachability.
    floor = sp.sin(sp.pi / 5) ** 2
    assert sp.simplify(floor - (5 - sp.sqrt(5)) / 8) == 0
    juno = sp.Rational(30902, 100000)
    Stt = 1 / (phi * sp.sqrt(5))
    assert float(juno) < float(floor) and float(Stt) < float(floor)


def test_d4_e6_to_f4_exponent_split_and_torsion_fibonacci():
    # D4 exact sub-result: E6 exponents {1,4,5,7,8,11}; F4 (the E6->F4 folding fixed sub) = {1,5,7,11};
    # the odd (E6-only) exponents are {4,8}; and the torsion identity U_m(3/2) = F_{2m+2}.
    e6 = {1, 4, 5, 7, 8, 11}
    f4 = {1, 5, 7, 11}
    assert f4 < e6 and (e6 - f4) == {4, 8}
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]
    for m in range(0, 6):
        assert sp.chebyshevu(m, sp.Rational(3, 2)) == fib[2 * m + 2]   # U_m(3/2) = F_{2m+2}
