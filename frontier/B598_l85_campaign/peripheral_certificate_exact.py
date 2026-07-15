"""The EXACT peripheral certificate (step 1 upgraded from numerical to
algebraic; failure-enforcing).

Over Q(sqrt-3) symbolically (sympy): the geometric parabolic rep of
<a,b | abABaBAbaB> with rho(a) = [[1,1],[0,1]], rho(b) = [[1,0],[c,1]]:
solving the relator equation exactly forces c^2 - c + 1 = 0, i.e.
c = (1 +- sqrt(-3))/2 (the two geometric branches). At each branch, all
of the following hold EXACTLY (no floats anywhere):

  (1) the relator maps to the identity;
  (2) lambda = "abABaaBAbA" commutes with the meridian a;
  (3) lambda's exponent sum is 0 (null-homologous longitude);
  (4) lambda and a * (bABaaBAb) * a^{-1} agree (the group-equal words);
  (5) the image is -[[1, L],[0,1]] with L = -+ 2 sqrt(-3): the banked cusp
      shape, and trace(lambda) = -2 (the OTHER parabolic class);
  (6) c is a unit: c * cbar = 1 (cbar = the conjugate root) and the two
      branches multiply to 1 -- the rep is defined over the ring of
      integers of Q(sqrt-3).

Run: python3 peripheral_certificate_exact.py   (seconds)
"""
import sympy as sp

t = sp.symbols('c')
A = sp.Matrix([[1, 1], [0, 1]])
Bg = sp.Matrix([[1, 0], [t, 1]])
Ai = A.inv()
Bi = Bg.inv()


def word(w):
    D = {'a': A, 'b': Bg, 'A': Ai, 'B': Bi}
    M = sp.eye(2)
    for ch in w:
        M = M * D[ch]
    return sp.expand(M)


# (0) solve the relator exactly
R = word("abABaBAbaB") - sp.eye(2)
eqs = set()
for i in range(2):
    for j in range(2):
        p = sp.factor(R[i, j])
        if p != 0:
            eqs.add(p)
polys = [sp.Poly(e, t) for e in eqs]
# the common nontrivial factor of every relator entry:
common = sp.factor_list(polys[0].as_expr())[1]
target = sp.Poly(t**2 - t + 1, t)
found = any(sp.Poly(f, t) == target for f, _ in common)
assert found, f"relator does not force c^2 - c + 1: {common}"
# and every relator entry vanishes mod c^2 - c + 1:
for q in polys:
    assert sp.rem(q.as_expr(), target.as_expr(), t) == 0, "relator residue"
print("exact: the relator forces c^2 - c + 1 = 0 (both geometric branches)",
      flush=True)

LAM = "abABaaBAbA"
allok = True
for c0 in sp.solve(t**2 - t + 1, t):
    subs = lambda M: sp.simplify(M.subs(t, c0))
    L = subs(word(LAM))
    # (2) commutes with the meridian
    g2 = sp.simplify(subs(word("a")) * L - L * subs(word("a"))) == sp.zeros(2)
    # (3) exponent sum
    g3 = sum(1 if ch in "ab" else -1 for ch in LAM) == 0
    # (4) group-equal words
    Lc = subs(word("a") * word("bABaaBAb") * word("A"))
    g4 = sp.simplify(L - Lc) == sp.zeros(2)
    # (5) the cusp shape and the parabolic class
    g5 = (sp.simplify(L[0, 0] + 1) == 0 and sp.simplify(L[1, 1] + 1) == 0
          and sp.simplify(L[1, 0]) == 0
          and sp.simplify(L[0, 1]**2 + 12) == 0        # L = +-2 sqrt(-3)
          and sp.simplify(sp.trace(L) + 2) == 0)
    # (6) unit
    g6 = sp.simplify(c0 * sp.conjugate(c0) - 1) == 0
    print(f"branch c = {c0}: commute {g2}; exp-sum {g3}; group-equal {g4}; "
          f"cusp shape -[[1, +-2sqrt(-3)],[0,1]] {g5}; unit {g6}", flush=True)
    allok &= g2 and g3 and g4 and g5 and g6

assert allok, "EXACT PERIPHERAL CERTIFICATE FAILED"
print("STEP 1 UPGRADED: the peripheral certificate is exact over Q(sqrt-3). "
      "DONE", flush=True)
