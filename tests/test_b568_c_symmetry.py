"""B568 seed observation — the defect-carrier spectrum is exactly C-symmetric.

The banked first-core-length map (B560-1B, locked in test_b560_cells.py context)
satisfies len(q) = len(11-q) for every nonzero charge class: the object's matter
comes in particle/antiparticle pairs of identical minimal size, in four
size-species {3,9,14,16}."""


def test_carrier_spectrum_charge_conjugation_symmetric():
    first = {1: 3, 2: 9, 3: 3, 4: 16, 5: 14, 6: 14, 7: 16, 8: 3, 9: 9, 10: 3}
    assert all(first[q] == first[11 - q] for q in range(1, 11))     # C-symmetry, exact
    assert sorted(set(first.values())) == [3, 9, 14, 16]            # four size-species
    from collections import Counter
    assert Counter(first.values()) == {3: 4, 9: 2, 14: 2, 16: 2}    # multiplicities
