import verify as v


def test_truncated_ring():
    assert v.mul({0: 1, 3: 2}, {0: 1, 3: -2}, 6) == {0: 1, 6: -4}
    assert v.mul({0: 1, 3: 2}, {0: 1, 3: -2}, 5) == {0: 1}


def test_actual_theta_coefficients():
    a, b, c = v.theta_series(16)
    assert a == {1: 2, 9: 2}
    assert b == {0: 1, 4: 2, 16: 2}
    assert c == {0: 1, 4: -2, 16: 2}


def test_euler_product_not_theta_alias():
    assert v.euler(3, 16) == {0: 1, 8: -3}
    assert v.euler(24, 16) == {0: 1, 8: -24, 16: 252}


def test_sign_and_normalization_controls():
    a, b, c = v.theta_series(32)
    p = v.mul(v.mul(a, b, 32), c, 32)
    wrong = v.mul(v.mul(a, b, 32), b, 32)
    assert p != wrong
    assert min(v.power(p, 8, 32)) == 8
    assert v.power(p, 8, 32)[8] == 256


def test_scoped_complete_record():
    result = v.run()
    assert len(result['checks']) == 23
    assert result['all_passed']
    assert len(result['delta_q_coefficients_1_to_32']) == 32
