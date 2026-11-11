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
    from sympy.combinatorics.named_groups import SymmetricGroup
    s4_order = int(SymmetricGroup(4).order())
    # 2T = SL(2,3) has index 2 in 2O, while S4 = PGL(2,3) has order 24
    two_O_order = 2 * sl2_fp_order(3)
    assert s4_order == 24 and two_O_order == 48 == 2 * s4_order
