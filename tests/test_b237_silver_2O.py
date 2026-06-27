"""B237 locks -- the ARITHMETIC behind L48 (the GQuotients result itself is GAP/SnapPy, documented in
FINDINGS + silver_2O.py, run via sage-python). Here we lock the supporting facts that make the verdict
inevitable: 2O (order 48) is never SL(2,F_p), while 2T(24)=SL(2,3) and 2I(120)=SL(2,5) are. Firewall:
rep-theory arithmetic; nothing to CLAIMS.md."""
from sympy import isprime


def sl2_fp_order(p):
    return p * (p * p - 1)


def test_2O_is_never_SL2Fp_but_2T_2I_are():
    """|2O|=48 is not p(p^2-1) for any prime; |2T|=24=SL(2,3); |2I|=120=SL(2,5)."""
    orders = {sl2_fp_order(p): p for p in range(2, 200) if isprime(p)}
    assert 48 not in orders                       # 2O (binary octahedral) -- never a congruence quotient
    assert orders.get(24) == 3                    # 2T = SL(2,3) = E6
    assert orders.get(120) == 5                   # 2I = SL(2,5) = E8


def test_2O_is_double_cover_of_S4_order():
    """silver realizes the octahedral ROTATION group S4 (order 24), not the binary cover 2O (order 48)."""
    assert 48 == 2 * 24                            # 2O = 2.S4 (binary octahedral double-covers S4)
