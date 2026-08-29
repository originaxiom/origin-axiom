#!/usr/bin/env python3
"""Hostile exact checks for the three new outside-tip claims in R023.

Dependency-free: Python 3 standard library only.  This certificate checks:

1. the norm-953 exhibit, while exposing the p=5 class-relation error;
2. the successor prime-witness repair, conditional on B1093's maximal order;
3. the Riley-sign/relator failure in grammar_disc48.py; and
4. the narrow projective golden-eigenline action of the exact reverser.

It deliberately does not accept the outside scripts' prose verdicts merely
because those scripts exit zero.
"""

from fractions import Fraction as F


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def cubic_norm(u, v, w):
    """Norm of u+v*t+w*t^2 for t^3-12*t+5=0."""
    multiplication = (
        (u, -5 * w, -5 * v),
        (v, u + 12 * w, 12 * v - 5 * w),
        (w, v, u + 12 * w),
    )
    return det3(multiplication)


# Exact exhibit and selected degree-one prime.
assert cubic_norm(-26, -1, 2) == 953
p = 953
# f=(x-372)(x^2+372x+187) mod 953.
assert (372 - 372) % p == 0  # x^2 coefficient: 372-372
assert (187 - 372 * 372) % p == (-12) % p
assert (-372 * 187) % p == 5
assert (-26 - 372 + 2 * 372 * 372) % p == 0
print("NORM-953: alpha=-26-theta+2theta^2 has exact norm 953;")
print("  f mod 953=(x-372)(x^2+372x+187), and alpha vanishes at x=372. PASS")

# The p=5 relation bug.  Modulo 5, f=x(x^2+3), with x^2+3 irreducible.
assert {a * a % 5 for a in range(5)} == {0, 1, 4}
assert cubic_norm(-2, 0, 1) == -175  # theta^2-2: v_5(N)=2 and v_7(N)=1
v_p, v_q = 0, 1  # nonzero at the degree-one root 0; one degree-two factor
outside_row = v_p + 2 * v_q
correct_class_coefficient = v_p - v_q  # [Q]=-[P] from (5)=P Q
assert outside_row == 2 and correct_class_coefficient == -1
print("P5-RELATION: theta^2-2 has (v_P,v_Q)=(0,1);")
print("  outside row uses v_P+2v_Q=2, but the class coefficient is v_P-v_Q=-1. DEFECT")


# The successor tip repairs the class-number proof by explicit witnesses,
# disjoint from the flawed relation matrix.
def roots_mod(prime):
    return [r for r in range(prime) if (r**3 - 12 * r + 5) % prime == 0]


def hensel_val(u, v, w, prime, root, cap=12):
    lifted, modulus = root, prime
    for _ in range(cap):
        f_value = (lifted**3 - 12 * lifted + 5) % (modulus * prime)
        derivative = (3 * lifted * lifted - 12) % (modulus * prime)
        inverse = pow(derivative, -1, modulus * prime)
        lifted = (lifted - f_value * inverse) % (modulus * prime)
        modulus *= prime
    value = (u + v * lifted + w * lifted * lifted) % modulus
    valuation = 0
    while valuation < cap - 1 and value % prime == 0:
        valuation += 1
        value //= prime
    return valuation


witnesses = {
    "p2": (-1, 2, 1, 2),
    "q2": (-1, 3, -1, 4),
    "p3": (-6, 2, 1, -3),
    "p5": (-5, 8, -2, -5),
    "p7a": (-1, 2, 0, 7),
    "p7b": (-3, 6, 2, -7),
    "p11a": (-4, -1, 0, -11),
    "p11b": (-2, 1, 0, 11),
}
for u, v, w, expected in witnesses.values():
    assert cubic_norm(u, v, w) == expected
# For a cubic, no root means irreducible; the root/derivative patterns below
# give exactly the eight prime ideals of norm at most 17 used by B1093.
assert roots_mod(2) == [1] and (3 * 1 * 1 - 12) % 2 != 0
assert roots_mod(3) == [1] and (3 * 1 * 1 - 12) % 3 == 0
assert roots_mod(5) == [0] and (3 * 0 * 0 - 12) % 5 != 0
assert roots_mod(7) == [4, 5]
assert [(3 * r * r - 12) % 7 for r in roots_mod(7)] == [1, 0]
assert roots_mod(11) == [2, 7]
assert [(3 * r * r - 12) % 11 for r in roots_mod(11)] == [0, 3]
assert roots_mod(13) == [] and roots_mod(17) == []
assert roots_mod(2) == [1]
assert hensel_val(*witnesses["q2"][:3], 2, 1) == 0
for prime, plain_root, first, second in (
    (7, 4, "p7a", "p7b"),
    (11, 7, "p11a", "p11b"),
):
    assert plain_root in roots_mod(prime)
    assert hensel_val(*witnesses[first][:3], prime, plain_root) == 1
    assert hensel_val(*witnesses[second][:3], prime, plain_root) == 0
assert 17**2 * 81 < 4 * 6237 < 18**2 * 81
print("PRINCIPAL-WITNESSES: all eight prime ideals below the Minkowski bound have")
print("  exact norm generators and discriminating valuations; with B1093's maximal-order gate, h(K)=1. PASS")


# Q(omega), omega^2=omega-1, and exact 2x2 word matrices.
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
W = (F(0), F(1))


def qadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def qneg(a):
    return (-a[0], -a[1])


def qmul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def mmul(a, b):
    return tuple(tuple(qadd(qmul(a[i][0], b[0][j]),
                            qmul(a[i][1], b[1][j]))
                       for j in range(2)) for i in range(2))


def minv(a):
    (p0, q0), (r0, s0) = a
    assert qadd(qmul(p0, s0), qneg(qmul(q0, r0))) == ONE
    return ((s0, qneg(q0)), (qneg(r0), p0))


IDENTITY = ((ONE, ZERO), (ZERO, ONE))
A = ((ONE, ONE), (ZERO, ONE))
B_WRONG = ((ONE, ZERO), (qneg(W), ONE))
B_BANKED = ((ONE, ZERO), (W, ONE))


def word_matrix(word, b_matrix):
    mats = {"a": A, "A": minv(A), "b": b_matrix, "B": minv(b_matrix)}
    out = IDENTITY
    for letter in word:
        out = mmul(out, mats[letter])
    return out


relator = "abABaBAbaB"
wrong_relator = word_matrix(relator, B_WRONG)
banked_relator = word_matrix(relator, B_BANKED)
expected_wrong = (((F(-1), F(0)), ZERO), ((F(-4), F(0)), (F(-1), F(0))))
assert wrong_relator == expected_wrong
assert banked_relator == IDENTITY

claimed_word = "baBAABab"
banked_word = "bABaaBAb"
claimed_in_banked = word_matrix(claimed_word, B_BANKED)
known_in_banked = word_matrix(banked_word, B_BANKED)
assert claimed_in_banked[1][0] != ZERO
assert known_in_banked[1][0] == ZERO
assert known_in_banked[0][0] == known_in_banked[1][1]
print("GRAMMAR-DISC48: wrong-sign b sends the m004 relator to [[-1,0],[-4,-1]];")
print("  corrected b satisfies it, but baBAABab is nonperipheral; bABaaBAb is peripheral. REFUTED")


# Exact arithmetic in Q(sqrt(5)) for the narrow reverser theorem.
def s5add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def s5mul(a, b):
    return (a[0] * b[0] + 5 * a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def s5scale(n, a):
    return (n * a[0], n * a[1])


def matvec(m, v):
    return tuple(
        s5add(s5add(s5scale(m[i][0], v[0]), s5scale(m[i][1], v[1])),
              s5scale(m[i][2], v[2])) for i in range(3)
    )


vu = ((F(3, 2), F(-1, 2)), (F(7, 2), F(-3, 2)), (F(1), F(0)))
vs = tuple((a, -b) for a, b in vu)
j2 = ((2, -1, 2), (0, 0, 1), (3, -2, 6))
dr = ((0, 1, 0), (1, 0, 0), (2, 2, -1))
phi4 = (F(7, 2), F(3, 2))
phi_minus4 = (F(7, 2), F(-3, 2))
lam = (F(9), F(-4))
lam_inverse = (F(9), F(4))
assert matvec(j2, vu) == tuple(s5mul(phi4, z) for z in vu)
assert matvec(j2, vs) == tuple(s5mul(phi_minus4, z) for z in vs)
assert matvec(dr, vu) == tuple(s5mul(lam, z) for z in vs)
assert matvec(dr, vs) == tuple(s5mul(lam_inverse, z) for z in vu)
assert s5mul(lam, lam_inverse) == (F(1), F(0))
print("GOLDEN-REVERSER: DR(v_u)=(9-4sqrt5)v_s and DR(v_s)=(9+4sqrt5)v_u. PASS")
print("R023 OUTSIDE-TIP HOSTILE AUDIT: PASS")
