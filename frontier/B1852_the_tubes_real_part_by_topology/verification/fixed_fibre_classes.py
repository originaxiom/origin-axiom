"""B1852 (data-free; exact integer matrices): the real part of tau at the two sigma-fixed fibres of a cyclic-palindrome
monodromy, by topology, with B1847's numerics identifying which fibre is which.

- **Why τ lies on a reflection locus.** A cyclic-palindrome monodromy phi has an isometry sigma that reverses fibre and
  circle (B1846). In the mapping torus it is sigma(x, t) = (J x, 1 - t) for a det -1 involution J with
  J phi J^-1 = phi^-1. It fixes two fibres:
  - t = 1/2, acting by J;
  - t = 0, acting by phi J.
  On each, sigma acts anticonformally, so that fibre's tau lies on the reflection locus of its involution.
- **The two classes.** The det -1 involutions of GL(2, Z) form two conjugacy classes:
  - J = I mod 2: the class of diag(1, -1), fixed geodesics reducing to Re tau = 0;
  - J != I mod 2: the class of [[0,1],[1,0]] and of tau -> 1 - conj(tau), reducing to Re tau = 1/2 or |tau| = 1.
  Above |tau| = 1 the reduced real part is therefore 0 or 1/2, decided by the class.
- **What is computed.** For each word, every reversing involution J (entries up to B), and the classes of J and phi J.
  - If all of them are != I mod 2, both fixed fibres sit at Re 1/2.
  - If J and phi J differ in class, the two fixed fibres sit one at Re 0 and one at Re 1/2.
- **Which fibre is which** is not decided by this algebra. For L^6RLR, B1847's independent numerics (the conformal
  modulus of the harmonic level surfaces) put the anti-apex (s = 1/2) at Re 1/2 to 7e-7, so the tube (s = 0, the other
  sigma-fixed level) is the class J = I mod 2: Re tau = 0. B1847's direct readings at s = 0 (-0.016, -0.048 on two
  grids) agree.
- **The control:** m004, both levels at Re 1/2 in B1847's table."""
import itertools
import numpy as np

L = np.array([[1, 1], [0, 1]], dtype=object); R = np.array([[1, 0], [1, 1]], dtype=object)
I2 = np.eye(2, dtype=object)


def mat(w):
    X = I2.copy()
    for ch in w:
        X = X.dot(L if ch == "L" else R)
    return X


def inv(X):
    a, b, c, d = X[0, 0], X[0, 1], X[1, 0], X[1, 1]; det = a * d - b * c
    return np.array([[d, -b], [-c, a]], dtype=object) * det


def eq(X, Y):
    return all(X[i, j] == Y[i, j] for i in range(2) for j in range(2))


def is_I_mod2(X):
    return all((X[i, j] - (1 if i == j else 0)) % 2 == 0 for i in range(2) for j in range(2))


def reversers(P, B=14):
    out = []
    for a, b, c, d in itertools.product(range(-B, B + 1), repeat=4):
        if a * d - b * c != -1 or a + d != 0:
            continue                                   # det -1 with trace 0 is exactly a det -1 involution
        J = np.array([[a, b], [c, d]], dtype=object)
        if eq(J.dot(P).dot(inv(J)), inv(P)):
            out.append(J)
    return out


def classes(w):
    phi = mat(w); Js = reversers(phi)
    assert Js, w
    pairs = set()
    for J in Js:
        K = phi.dot(J)
        assert eq(K.dot(K), I2) and eq(J.dot(J), I2)   # both fixed-fibre actions are involutions
        pairs.add((is_I_mod2(J), is_I_mod2(K)))
    return len(Js), pairs


rows = []
for name, w, b1847 in (
        ("m004 (LR), the control", "LR", "B1847: s = 0 at -0.5000, s = 1/2 at +0.5000 (both Re 1/2)"),
        ("L^6RLR, the read-out member", "LLLLLLRLR", "B1847: s = 1/2 (anti-apex) Re 1/2 to 7e-7; s = 0 (tube) -0.016, -0.048"),
        ("L^10RLR", "LLLLLLLLLLRLR", "no level-surface numerics"),
        ("L^5RLR (an odd run)", "LLLLLRLR", "no level-surface numerics")):
    n, pairs = classes(w)
    if pairs == {(False, False)}:
        verdict = "both fixed fibres != I mod 2: both at Re tau = 1/2"
    elif pairs <= {(True, False), (False, True)} and pairs:
        verdict = "the two fixed fibres in opposite classes: one at Re tau = 0, the other at Re tau = 1/2"
    else:
        verdict = "classes %s" % sorted(pairs)
    rows.append("%-30s %2d reversing involutions; %s  [%s]" % (name, n, verdict, b1847))
print("\n".join(rows))
print("=> L^6RLR: the anti-apex is the Re 1/2 fibre (B1847, 7e-7), so the tube's level surface has reduced Re tau = 0 exactly;"
      " with B1847's Im tau(Sigma_0) = 6.15 +- 0.15 the metric's own tau at the tube is 0 + 6.15(15) i")
