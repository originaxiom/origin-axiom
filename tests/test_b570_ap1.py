import itertools

CHI  = [1, 3, 6, 7]                       # banked left-fixed charge vector chi.M4 = chi mod 11 (B552)
CHI3 = [(c ** 3) % 11 for c in CHI]

def lin(m): return sum(m[i] * CHI[i] for i in range(4)) % 11
def cub(m): return sum(m[i] * CHI3[i] for i in range(4)) % 11
def AF(m):  return lin(m) == 0 and cub(m) == 0

HB = [
    (0, 1, 1, 5), (1, 5, 1, 0), (3, 2, 1, 1),                       # total 7  (the banked minimal casts)
    (0, 3, 3, 4), (2, 0, 3, 5), (3, 4, 3, 0), (5, 1, 3, 1),          # total 10
    (0, 0, 0, 11), (0, 0, 11, 0), (0, 11, 0, 0), (11, 0, 0, 0),      # total 11 (pure single-letter, order 11)
    (1, 4, 0, 6), (2, 8, 0, 1), (3, 1, 0, 7), (4, 5, 0, 2), (6, 2, 0, 3),  # total 11 (3-support)
    (1, 1, 8, 2),                                                   # total 12
    (0, 5, 5, 3), (2, 2, 5, 4), (5, 3, 5, 0), (7, 0, 5, 1),          # total 13
    (5, 0, 2, 7), (8, 1, 2, 3),                                      # total 14
    (1, 3, 10, 1), (3, 0, 10, 2),                                    # total 15
    (0, 7, 7, 2), (1, 0, 7, 8), (2, 4, 7, 3), (4, 1, 7, 4), (7, 2, 7, 0),  # total 16
    (10, 0, 4, 3),                                                  # total 17
    (8, 0, 1, 9),                                                   # total 18
    (0, 9, 9, 1), (6, 0, 9, 4), (9, 1, 9, 0),                        # total 19
]


def brute_solutions(T):
    out = []
    for n0 in range(T + 1):
        for n1 in range(T + 1 - n0):
            for n2 in range(T + 1 - n0 - n1):
                n3 = T - n0 - n1 - n2
                m = (n0, n1, n2, n3)
                if AF(m):
                    out.append(m)
    return set(out)


def reachable_by_total(hb, maxT):
    R = {0: {(0, 0, 0, 0)}}
    for T in range(1, maxT + 1):
        s = set()
        for g in hb:
            tg = sum(g)
            if tg <= T and (T - tg) in R:
                for r in R[T - tg]:
                    s.add(tuple(r[i] + g[i] for i in range(4)))
        R[T] = s
    return R


def test_charge_vector():
    assert CHI == [1, 3, 6, 7]
    assert CHI3 == [1, 5, 7, 2]


def test_three_minimal_casts_anomaly_free_and_exhaustive():
    for m in ((0, 1, 1, 5), (1, 5, 1, 0), (3, 2, 1, 1)):
        assert sum(m) == 7 and AF(m)
    for T in range(1, 7):
        assert brute_solutions(T) == set()
    assert brute_solutions(7) == {(0, 1, 1, 5), (1, 5, 1, 0), (3, 2, 1, 1)}


def test_monoid_closure():
    # concatenation (vector addition) of two anomaly-free casts is anomaly-free -- trivial
    # from linearity of lin/cub, verified on all pairs of the 35 generators.
    for g, h in itertools.product(HB, HB):
        s = tuple(g[i] + h[i] for i in range(4))
        assert AF(s)


def test_hilbert_basis_all_anomaly_free():
    assert len(HB) == 35
    assert len(set(HB)) == 35
    for m in HB:
        assert AF(m)


def test_hilbert_basis_minimal_no_generator_decomposes():
    # no HB element is p+q for two nonzero AF vectors with smaller total
    all_small = set()
    for T in range(1, 20):
        all_small |= brute_solutions(T)
    for m in HB:
        T = sum(m)
        decomposable = False
        for q in all_small:
            if sum(q) < T and all(q[i] <= m[i] for i in range(4)):
                decomposable = True
                break
        assert not decomposable, m


def test_hilbert_basis_generates_everything_up_to_40():
    R = reachable_by_total(HB, 40)
    for T in range(0, 41):
        assert R[T] == brute_solutions(T) if T > 0 else R[T] == {(0, 0, 0, 0)}


def test_achievable_totals_gap_structure():
    # cast totals realized: {0, 7} u [10, 40]; gaps exactly {1,2,3,4,5,6,8,9}
    achieved = {T for T in range(0, 41) if brute_solutions(T) or T == 0}
    gaps = {T for T in range(1, 41) if T not in achieved}
    assert gaps == {1, 2, 3, 4, 5, 6, 8, 9}


def test_base_cast_fails_ibanez_ross():
    base = (1, 1, 1, 1)  # one copy of each species (the raw M4-eigenvector base)
    assert lin(base) == 6 and cub(base) == 4 and not AF(base)


if __name__ == "__main__":
    import sys
    fails = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            try:
                fn()
                print("PASS", name)
            except AssertionError as e:
                fails += 1
                print("FAIL", name, e)
    sys.exit(1 if fails else 0)
