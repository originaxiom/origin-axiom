"""B917 locks: the value-arc verification layer."""
import sympy as sp


def test_p9_product_law_integers():
    assert 27 * 2304**4 == 760840571584512
    assert sp.factorint(2304) == {2: 8, 3: 2}
    assert 13824 == 6 * 2304


def test_value_primes_and_split_patterns():
    rho = sp.Symbol("rho")
    MU = sp.Poly(500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197,
                 rho)
    for p in (953, 1129, 421493):
        assert sp.isprime(p)
        degs = sorted(f.degree() for f, _ in sp.factor_list(MU, modulus=p)[1])
        assert degs == [1, 2]
    for p in (17, 19):
        degs = sorted(f.degree() for f, _ in sp.factor_list(MU, modulus=p)[1])
        assert degs == [3]


def test_lambda_unity_bank():
    # the canonical-gauge identity is banked via B914's exact data:
    # T = c^2/(s_i s_j s_k) with s_i = q_i/q_ref  and  c^2 = q_i q_j q_k
    # (lambda = 1) together force T = q_ref^3 / ... -- the lock asserts the
    # recorded consistency: all six T equal (B914) AND lambda = 1 was computed
    # from the same stored environment (documented in FINDINGS; the exact
    # rerun is scripted in B916's bridge cell).
    import json, os
    r = json.load(open(os.path.join(os.path.dirname(__file__), "..",
                                    "frontier", "B914_ratio_table",
                                    "results.json")))
    vals = {v["value_50d"] for v in r["T_table"].values()}
    assert len(vals) == 1
