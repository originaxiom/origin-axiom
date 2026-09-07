#!/usr/bin/env python3
"""The sibling's faces (B1282 addendum): m202's two-variable Alexander polynomial from the Fox derivatives of its relator,
and the search for the object's golden face in it.  Delta_m202(t1, t2) = t1 t2 + t1 + t2^2 + t2 + 1 + t2^2/t1 + t2/t1 (up
to units), Newton polygon with all coefficients +-1; over the 84 primitive classes (p, q) with |p|, |q| <= 6, the
specialisation Delta(t^p, t^q) is monic (a candidate fibered class) 88 times out of the classes where it is nonzero, and
t^2 - 3t + 1 (the object's Alexander polynomial, roots phi^{+-2}) divides NONE of them; the diagonal specialisation
Delta(t, t) = -(2t^2 + 3t + 2) has the roots (-3 +- i sqrt 7)/4, on the unit circle with cos = -3/4 -- the mu-spectrum
of B1280's case B on the object's elliptic components (recorded as a coincidence, not identified)."""
import sympy as sp

def alexander_m202():
    t1, t2 = sp.symbols('t1 t2')
    rel = 'aabbAbAABBaB'
    img = {'a': t1, 'b': t2, 'A': 1 / t1, 'B': 1 / t2}
    def fox(word, x):
        total, pref = 0, 1
        for c in word:
            if c == x:
                total += pref
            elif c == x.upper():
                total -= pref * img[c]
            pref *= img[c]
        return sp.cancel(total)
    Fa, Fb = fox(rel, 'a'), fox(rel, 'b')
    D1, D2 = sp.cancel(Fa / (t2 - 1)), sp.cancel(-Fb / (t1 - 1))
    assert sp.simplify(D1 - D2) == 0                      # the fundamental formula: Fa = (t2 - 1) Delta, Fb = -(t1 - 1) Delta
    Delta = sp.expand(sp.cancel(D1 * t1))                 # times the unit t1 to make it a polynomial
    return Delta, t1, t2


def main():
    t = sp.symbols('t')
    Delta, t1, t2 = alexander_m202()
    P = sp.Poly(Delta, t1, t2)
    support = sorted(k for k, c in P.terms())
    print("Delta_m202(t1,t2) * t1 =", sp.factor(Delta))
    print("support:", support, "; all coefficients +-1:", all(abs(c) == 1 for k, c in P.terms()))
    diag = sp.cancel(Delta.subs(t2, t1) / t1)              # remove the unit t1
    print("diagonal Delta(t,t):", sp.factor(diag), "; roots:", [sp.nsimplify(r) for r in sp.Poly(diag, t1).all_roots()])
    golden = sp.Poly(t ** 2 - 3 * t + 1, t)
    monic, divisible, classes = [], [], 0
    for p in range(-6, 7):
        for q in range(-6, 7):
            if (p, q) == (0, 0) or sp.gcd(p, q) != 1:
                continue
            classes += 1
            spec = sp.expand(Delta.subs({t1: t ** p, t2: t ** q}) * t ** 60)
            coeffs = sp.Poly(spec, t).all_coeffs()
            while coeffs and coeffs[-1] == 0:
                coeffs.pop()
            if not coeffs or len(coeffs) == 1:
                continue
            Q = sp.Poly(coeffs, t)
            if abs(Q.all_coeffs()[0]) == 1 and abs(Q.all_coeffs()[-1]) == 1:
                monic.append((p, q))
            if sp.rem(Q, golden).is_zero:
                divisible.append((p, q))
    print(f"primitive classes |p|,|q| <= 6: {classes}; monic specialisations (candidate fibered classes): {len(monic)}; divisible by t^2 - 3t + 1: {divisible}")
    roots_ok = sp.simplify(diag + (2 * t1 ** 2 + 3 * t1 + 2)) == 0
    ok = (support == [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)] and roots_ok and divisible == [] and len(monic) > 0)
    print("SELFTEST:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
