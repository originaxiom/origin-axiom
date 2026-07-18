"""B690 — the 3-adic twin deviates with bounded defect (E-2a intake)."""


def _s3(n):
    s = 0
    while n:
        s += n % 3; n //= 3
    return s


def test_being_3adic_defect_bounded_only_n4_exact():
    pred = lambda n: n + (n - _s3(n))//2       # n + v3(n!)
    actual = {2: 3, 3: 3, 4: 5, 5: 5, 100: 146}
    defects = {n: actual[n] - pred(n) for n in actual}
    assert max(abs(d) for d in defects.values()) == 2   # bounded defect
    assert [n for n in actual if defects[n] == 0] == [4]  # only n=4 exact
