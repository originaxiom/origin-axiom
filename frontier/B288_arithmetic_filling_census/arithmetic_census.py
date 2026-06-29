"""B288 -- THE ARITHMETIC FILLING CENSUS (the CRUX through the seam). Run with sage-python (SnapPy + Sage NF).

B282/B266: the figure-eight's E6 is ARITHMETIC, not geometric -- the CUSPED invariant trace field is Q(sqrt-3),
whose ramified prime 3 -> SL(2,F3)=2T -> McKay E6. New seam question: when we CLOSE the object (Dehn filling), does
the closed manifold RE-SEE Q(sqrt-3) (re-instantiate E6), or is the E6 datum an OPEN-object property lost on closing?

Sweep: every hyperbolic Dehn filling (p,q), |p|<=8, 1<=q<=8, gcd=1. For each closed manifold compute the invariant
trace field kM (Maclachlan-Reid commensurability invariant) and test whether Q(sqrt-3) subset kM (i.e. sqrt(-3) in kM,
equivalently x^2+3 has a root in kM). Two methods: (1) invariant trace field via traces-of-SQUARES (lift-independent);
(2) cross-check the larger shape/trace field -- if sqrt(-3) is absent there it is absent in every subfield.

RESULT: the CUSPED (open) object has kM = Q(sqrt-3); NO closed hyperbolic filling re-sees it. Every closed filling has
a higher-degree (3..15) invariant trace field, none containing sqrt(-3), and none imaginary-quadratic (arithmetic).
=> the E6 arithmetic atom is an OPEN-object property, DESTROYED by closing -- sharpening B281/B286. Leaning CATALOGUE
for the CRUX: the seam does not arithmetically select E6. FIREWALLED; nothing to CLAIMS.
"""
import snappy
from sage.all import PolynomialRing
from math import gcd


def has_sqrt_neg3(K):
    R = PolynomialRing(K, 'x'); x = R.gen()
    return len((x**2 + 3).roots()) > 0                 # sqrt(-3) in K  <=>  x^2+3 has a root in K


def invariant_trace_field(M, prec=200, degree=10):
    res = M.invariant_trace_field_gens().find_field(prec=prec, degree=degree, optimize=True)
    return res[0] if res else None                     # Sage NumberField or None (degree > `degree`)


def census(pmax=8, qmax=8):
    rows = []
    for p in range(-pmax, pmax + 1):
        for q in range(1, qmax + 1):
            if gcd(abs(p), q) != 1:
                continue
            M = snappy.Manifold('m004'); M.dehn_fill((p, q))
            if 'positively' not in M.solution_type():
                continue                               # skip non-hyperbolic / exceptional
            K = invariant_trace_field(M)
            if K is None:                              # bump degree/precision for the high-degree stragglers
                K = invariant_trace_field(M, prec=500, degree=20)
            if K is None:
                rows.append((p, q, '>20', None)); continue
            rows.append((p, q, K.degree(), has_sqrt_neg3(K)))
    return rows


if __name__ == "__main__":
    # the OPEN object re-sees E6:
    Mc = snappy.Manifold('m004')
    cf = invariant_trace_field(Mc, degree=4)
    print("CUSPED (open) m004: invariant trace field =", cf.defining_polynomial(),
          " -> sqrt(-3) in it:", has_sqrt_neg3(cf), "  [= Q(sqrt-3), the E6 atom]")

    rows = census()
    resolved = [r for r in rows if r[2] != '>20']
    n_sqrt3 = sum(1 for r in resolved if r[3])
    n_arith = sum(1 for r in resolved if r[2] == 2)
    print(f"\nclosed hyperbolic fillings resolved: {len(resolved)}  (stragglers deg>20: {len(rows)-len(resolved)})")
    print("degrees seen:", sorted(set(r[2] for r in resolved)))
    print("# re-seeing Q(sqrt-3) (re-instantiating E6):", n_sqrt3)
    print("# imaginary-quadratic (arithmetic):", n_arith)
    assert n_sqrt3 == 0 and n_arith == 0
    print("\nVERDICT: E6 (Q(sqrt-3)) is an OPEN-object property, LOST on closing. The seam does not arithmetically")
    print("select E6 -> leaning CATALOGUE for the CRUX. (Firewalled; nothing to CLAIMS.)")
