"""B740 deep pass (sage b740_deep.py): the 18 degree->24 unknowns -- invariant trace field at
degree 32 / prec 2000, plus the SHAPE-field cross-check (B288's own method 2: if sqrt(-3) is absent
in the shape field it is absent in every subfield, including the invariant trace field)."""
import snappy
from sage.all import PolynomialRing
from math import gcd
exec(open('/tmp/unknown18.py').read())

def has_sqrt_neg3(K):
    R = PolynomialRing(K, 'x'); x = R.gen()
    return len((x**2 + 3).roots()) > 0

def recover(p, q, tries=25):
    for i in range(tries):
        M = snappy.Manifold('m004'); M.dehn_fill((p, q))
        if i: M.randomize()
        if 'positively' in M.solution_type(): return M
        try:
            F = M.filled_triangulation()
            if 'positively' in F.solution_type(): return F
            F.randomize()
            if 'positively' in F.solution_type(): return F
        except Exception: pass
    return None

resolved = 0; crack = []
for (p, q) in SLOPES:
    R = recover(p, q)
    tag = None
    if R is not None:
        # route 1: invariant trace field, deeper
        try:
            res = R.invariant_trace_field_gens().find_field(prec=2000, degree=32, optimize=True)
            K = res[0] if res else None
        except Exception:
            K = None
        if K is not None:
            tag = ('ITF', int(K.degree()), bool(has_sqrt_neg3(K)))
        else:
            # route 2: shape field (superfield) -- absence there is decisive
            try:
                res = R.tetrahedra_field_gens().find_field(prec=2000, degree=32, optimize=True)
                S = res[0] if res else None
            except Exception:
                S = None
            if S is not None:
                tag = ('SHAPE', int(S.degree()), bool(has_sqrt_neg3(S)))
    if tag is None:
        print((p, q, 'STILL-UNKNOWN'))
    else:
        resolved += 1
        print((p, q) + tag)
        if tag[2]: crack.append((p, q, tag[0]))
print(f"\nDEEP SUMMARY: resolved {resolved}/{len(SLOPES)}")
print("VERDICT:", ("A -- CRACK: " + str(crack)) if crack else
      "B -- no sqrt(-3) in any resolved deep field" + ("" if resolved==len(SLOPES) else " [some STILL-UNKNOWN]"))
