# Periodic curves of the trace map: Fix_sigma(T^k) = { p : T^k(p) = sigma(p) },  sigma a sign twist (PSL(2) level reps)
import sys, json, itertools
R.<X,Y,Z> = PolynomialRing(QQ, order='degrevlex')
kappa = X^2 + Y^2 + Z^2 - X*Y*Z - 2
def Lm(p):  return (p[0], p[2], p[0]*p[2] - p[1])            # x -> x,  y -> yx
def Rm(p):  return (p[2], p[1], p[2]*p[1] - p[0])            # x -> xy, y -> y
def Li(p):  return (p[0], p[0]*p[1] - p[2], p[1])
def Ri(p):  return (p[0]*p[1] - p[2], p[1], p[0])
SIG = {"+++": (1,1,1), "+--": (1,-1,-1), "-+-": (-1,1,-1), "--+": (-1,-1,1)}
def apply(word, p, inverse=False):
    # trace map of the automorphism word (applied as substitution: later letters act first on traces)
    if not inverse:
        for c in word: p = Lm(p) if c == "L" else Rm(p)
    else:
        for c in reversed(word): p = Li(p) if c == "L" else Ri(p)
    return p
def fix_ideal(word, k, sig):
    w = word * k; h = len(w) // 2; p0 = (X, Y, Z)
    A = apply(w[:h], p0)                                       # T_first(p)
    q = tuple(s * c for s, c in zip(SIG[sig], p0))
    B = apply(w[h:], q, inverse=True)                          # T_second^{-1}(sigma p)
    return R.ideal([a - b for a, b in zip(A, B)])
def describe(word, k, sig):
    I = fix_ideal(word, k, sig)
    out = []
    for P in I.minimal_associated_primes():
        d = P.dimension()
        rec = dict(dim=int(d), gens=[str(g) for g in P.gens()][:6])
        if d == 1:
            try: rec["degree"] = int(P.homogenize().hilbert_polynomial().leading_coefficient())
            except Exception as e: rec["degree"] = str(e)[:60]
            try: rec["genus"] = int(Curve(list(P.gens()), AffineSpace(R)).geometric_genus())
            except Exception as e: rec["genus"] = str(e)[:60]
            # intersections with kappa = 2 and kappa = -2
            for val, nm in ((2, "at_kappa_2"), (-2, "at_kappa_m2")):
                J = (P + R.ideal(kappa - val)).radical()
                rec[nm] = dict(dim=int(J.dimension()), points=int(J.vector_space_dimension()) if J.dimension() == 0 else None,
                               gens=[str(g) for g in J.groebner_basis()][:8])
        out.append(rec)
    return out
if __name__ == "__main__":
    word = sys.argv[1]; k = int(sys.argv[2])
    res = {}
    for sig in SIG:
        res[sig] = describe(word, k, sig)
        print(word, k, sig); 
        for r in res[sig]: print("   ", json.dumps(r))
        sys.stdout.flush()
    json.dump(res, open("periodic_curves_%s_%d.json" % (word, k), "w"), indent=1)
