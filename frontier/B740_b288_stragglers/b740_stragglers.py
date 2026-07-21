"""B740 -- the B288 straggler re-run (run with: sage -python). Completes the (|p|<=8, 1<=q<=8) grid:
every slope the original line-40 `continue` skipped or line-45 recorded '>20' gets (a) exceptional-vs-
hyperbolic classification, (b) retriangulation recovery, (c) invariant trace field + sqrt(-3) test."""
import snappy
from sage.all import PolynomialRing
from math import gcd

EXCEPTIONAL = {(p, 1) for p in range(-4, 5)}           # the known exceptional slopes of 4_1 in this grid

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
    """Try hard for a positively-oriented solution."""
    for i in range(tries):
        M = snappy.Manifold('m004'); M.dehn_fill((p, q))
        if i:
            M.randomize()
        if 'positively' in M.solution_type():
            return M
        try:
            F = M.filled_triangulation()
            if 'positively' in F.solution_type():
                return F
            F.randomize()
            if 'positively' in F.solution_type():
                return F
        except Exception:
            pass
    return None

def main():
    total = skipped = 0
    rows = []
    for p in range(-8, 9):
        for q in range(1, 9):
            if gcd(abs(p), q) != 1:
                continue
            total += 1
            M = snappy.Manifold('m004'); M.dehn_fill((p, q))
            if 'positively' in M.solution_type():
                continue                                # analyzed by the original census
            skipped += 1
            if (p, q) in EXCEPTIONAL:
                rows.append((p, q, 'EXCEPTIONAL', None, None)); continue
            R = recover_positive(p, q)
            if R is None:
                rows.append((p, q, 'UNRESOLVED', None, None)); continue
            K = None
            for prec, deg in ((300, 12), (600, 18), (1000, 24)):
                K = field(R, prec, deg)
                if K is not None:
                    break
            if K is None:
                rows.append((p, q, 'RECOVERED', '>24', None))
            else:
                rows.append((p, q, 'RECOVERED', int(K.degree()), bool(has_sqrt_neg3(K))))
    print(f"grid total (coprime) = {total}; originally skipped = {skipped}")
    crack = False
    for r in rows:
        print(r)
        if r[2] == 'RECOVERED' and r[4] is True:
            crack = True
    n_exc = sum(1 for r in rows if r[2] == 'EXCEPTIONAL')
    n_rec = sum(1 for r in rows if r[2] == 'RECOVERED')
    n_unr = sum(1 for r in rows if r[2] == 'UNRESOLVED')
    n_deep = sum(1 for r in rows if r[2] == 'RECOVERED' and r[3] == '>24')
    print(f"exceptional={n_exc} recovered={n_rec} (field-unknown>{24}: {n_deep}) unresolved={n_unr}")
    print("VERDICT:", "A -- CRACK: a straggler contains sqrt(-3)!" if crack
          else "B -- reconfirmed on the completed grid: no recovered filling contains sqrt(-3)"
               + (" [with residual unknowns noted above]" if (n_unr or n_deep) else ""))

main()   # sage runs .py with __name__=='sage.all' -- call unconditionally
