"""B681 — the blackboard v5 pre-test for the W3 survivor (design-stage).
Decomposes the divided-power law into (Habiro divided-power) x (level-5)."""
import math
from fractions import Fraction


def s5(n):
    s = 0
    while n:
        s += n % 5
        n //= 5
    return s


def v5_factorial(n):          # Legendre, p=5
    return (n - s5(n)) // 4


def v5_int(x):
    v = 0
    while x and x % 5 == 0:
        x //= 5
        v += 1
    return v


def divided_power_v5(n):      # the banked law: v5(den c_n) = v5(5^n n!)
    return n + v5_factorial(n)


if __name__ == "__main__":
    banked = {1: 1, 10: 12, 40: 49, 80: 99, 119: 146}
    for n, tgt in banked.items():
        assert v5_factorial(n) == v5_int(math.factorial(n))
        assert divided_power_v5(n) == tgt          # n + v5(n!) = target
    # the decomposition is exact at every witness:
    #   v5(n!)  = the divided-power (Gamma^n vs Sym^n) denominator (Habiro)
    #   5^n     = one factor of 5 per grade = 2 S-applications/grade
    print("PRE-TEST PASS: divided-power law = n + v5(n!), all witnesses exact")
