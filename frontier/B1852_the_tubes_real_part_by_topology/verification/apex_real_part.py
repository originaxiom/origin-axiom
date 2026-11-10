"""B1852, the correction of 2026-11-10 (data-free; exact, sympy): the Teichmuller apex of a word's axis, with its real part.

- **What is computed.** For a hyperbolic M = [[a, b], [c, d]] in SL(2, Z) the axis of tau -> (a tau + b)/(c tau + d) is
  the semicircle centred at (a - d)/(2c) with radius sqrt(tr^2 - 4)/(2|c|). Its apex is centre + i radius.
- **The highest apex** is taken over the word's cyclic conjugates and their S-conjugates (B1845's first control omitted
  the S-conjugates and was caught). The real part is reduced by tau -> tau + n and tau -> -conj(tau) to [0, 1/2].
- **Why this file exists.** B1852's FINDINGS wrote L^6RLR's apex as 1/2 + 3.65i, carrying B1845's Re 1/2 (proved there
  for L^5R(LR)^k) over to the even run. The web seat caught it. Exact: L^6RLR's apex is 2 sqrt(30)/3 i at Re 0.
- **The family:** L^6R(LR)^k at Re 0 for every k computed, heights falling to 2 + golden ratio; L^5R(LR)^k at Re 1/2."""
import sympy as sp

L = sp.Matrix([[1, 1], [0, 1]]); R = sp.Matrix([[1, 0], [1, 1]]); S = sp.Matrix([[0, -1], [1, 0]])


def mat(w):
    X = sp.eye(2)
    for ch in w:
        X = X * (L if ch == "L" else R)
    return X


def apex(w):
    best = None
    for i in range(len(w)):
        M0 = mat(w[i:] + w[:i])
        for M in (M0, S * M0 * S.inv()):
            a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
            if c == 0:
                continue
            D = (a + d) ** 2 - 4
            h2 = sp.Rational(D, 4 * c * c)                       # the apex height squared, exact
            re = sp.Rational(a - d, 2 * c)
            re = re - sp.floor(re)                               # tau -> tau + n
            re = min(re, 1 - re)                                 # tau -> -conj(tau)
            if best is None or h2 > best[0]:
                best = (h2, {re})
            elif h2 == best[0]:
                best[1].add(re)
    return best


rows = []
for name, w in ([("L^6RLR", "LLLLLLRLR"), ("L^5RLR", "LLLLLRLR")]
                + [("L^6R(LR)^%d" % k, "LLLLLLR" + "LR" * k) for k in (2, 3, 8)]
                + [("L^5R(LR)^%d" % k, "LLLLLR" + "LR" * k) for k in (2, 3)]):
    h2, res = apex(w)
    rows.append("%-12s apex height^2 = %-28s height = %.6f   reduced Re in %s" % (name, h2, float(sp.sqrt(h2)), sorted(res)))
print("\n".join(rows))
h2, res = apex("LLLLLLRLR")
assert h2 == sp.Rational(40, 3) and res == {0}
assert sp.simplify(sp.sqrt(h2) - 2 * sp.sqrt(30) / 3) == 0
h2, res = apex("LLLLLRLR")
assert h2 == sp.Rational(357, 36) and res == {sp.Rational(1, 2)}
print("=> L^6RLR: apex 2 sqrt(30)/3 i = sqrt(40/3) i at Re 0 exactly; L^5RLR: apex 1/2 + sqrt(357)/6 i at Re 1/2 exactly")
print("=> the limit of the L^6 heights is 2 + golden ratio = %.6f" % float(2 + (1 + sp.sqrt(5)) / 2))
