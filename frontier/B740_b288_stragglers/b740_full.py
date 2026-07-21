"""B740 FULL census (run: sage b740_full.py) -- the completed grid, actually computed.
The banked B288 resolved 54/78 hyperbolic fillings; the missing 24 are unidentifiable (no row list
banked), so recompute ALL 78: for every coprime (p,q), |p|<=8, 1<=q<=8, recover a positively-
oriented solution (retriangulate as needed), compute the invariant trace field (sage), test sqrt(-3).
"""
import snappy
from sage.all import PolynomialRing
from math import gcd

EXCEPTIONAL = {(p, 1) for p in range(-4, 5)}

def has_sqrt_neg3(K):
    R = PolynomialRing(K, 'x'); x = R.gen()
    return len((x**2 + 3).roots()) > 0

def field(M, prec, degree):
    try:
        res = M.invariant_trace_field_gens().find_field(prec=prec, degree=degree, optimize=True)
        return res[0] if res else None
    except Exception:
        return None

def recover_positive(p, q, tries=25):
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

rows = []; n_hyp = n_exc = n_unres = n_unknown = 0; crack = []
for p in range(-8, 9):
    for q in range(1, 9):
        if gcd(abs(p), q) != 1: continue
        if (p, q) in EXCEPTIONAL:
            n_exc += 1; continue
        R = recover_positive(p, q)
        if R is None:
            n_unres += 1; rows.append((p, q, 'UNRESOLVED', None)); print((p,q,'UNRESOLVED')); continue
        n_hyp += 1
        K = None
        for prec, deg in ((250, 12), (500, 18), (1000, 24)):
            K = field(R, prec, deg)
            if K is not None: break
        if K is None:
            n_unknown += 1; rows.append((p, q, '>24', None)); print((p, q, '>24', None))
        else:
            hit = bool(has_sqrt_neg3(K))
            rows.append((p, q, int(K.degree()), hit)); print((p, q, int(K.degree()), hit))
            if hit: crack.append((p, q))
print(f"\nSUMMARY: hyperbolic analyzed={n_hyp}  exceptional={n_exc}  unresolved={n_unres}  field>24={n_unknown}")
print("VERDICT:", ("A -- CRACK at " + str(crack)) if crack else
      "B -- the COMPLETED grid reconfirms: no closed hyperbolic filling's invariant trace field contains sqrt(-3)"
      + (" [with residual unknowns]" if (n_unres or n_unknown) else ""))
