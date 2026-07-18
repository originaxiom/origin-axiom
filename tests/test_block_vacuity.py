"""Block-vacuity gate lock — the six blocks are distinct (B581 spectrum)."""


def test_six_block_torsions_distinct_and_sign_law():
    tau = {1: -3, 4: 260736, 5: -165110400, 7: -3257341296168960,
           8: 100636318520821923840,
           11: -(2**21 * 3**7 * 5 * 7**6 * 11**2 * 13**2 * 17 * 19 * 73
                 * 149 * 151 * 1471 * 160453)}
    assert len(set(tau.values())) == 6                      # independent
    for m, t in tau.items():
        assert (1 if t > 0 else -1) == (-1)**m              # sign law
    cas = {m: m*(m+1) for m in tau}
    assert len(set(cas.values())) == 6                      # distinct Casimirs
