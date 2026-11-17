"""B1957: the physical lane's P-C3e, the linear statement (its equation (3)): the gauge operator on the complete cusp is
a bijection between a space of fields 'constant times Q in the tail, plus decaying' and decaying sources orthogonal to
Q.  Main's independent check of the steps that can be checked exactly: the reduction on the cusp, the indicial roots,
which solutions the physical measure admits, the decay of the solution for a decaying source with explicit constants,
and the solutions at nonzero angular frequency.  Symbolic and exact; nothing of the lane's is run (it has no code for
this step).  What this does NOT check is listed at the end."""
import sympy as sp, mpmath as mp

if __name__ == "__main__":
    t, y, x, s = sp.symbols("t y x s", real=True); ell, c, d, n = sp.symbols("ell c delta n", positive=True)
    # 1: the cusp's Laplacian on functions of the height alone, in t = ln y, and its measure
    f = sp.Function("f"); lap = -y ** 2 * sp.diff(f(sp.log(y)), y, 2); red = sp.simplify(lap.subs(y, sp.exp(t)).doit())
    g = sp.Function("g"); expr = sp.simplify((-y ** 2 * sp.diff(g(y), y, 2)).subs(g(y), sp.exp(sp.Symbol("r") * sp.log(y))).doit() / y ** sp.Symbol("r"))
    print("1: on y^r the operator -y^2 d^2/dy^2 gives %s times y^r, that is -(r^2 - r): in t = ln y it is -(d^2/dt^2 - d/dt), the lane's (1); the area form dx dy / y^2 is exp(-t) dt dx" % sp.factor(expr))
    # 2: indicial roots of ell^-2 (-f'' + f') + c f = 0
    r = sp.Symbol("r"); roots = sp.solve(sp.Eq(-(r ** 2 - r) / ell ** 2 + c, 0), r); beta = (sp.sqrt(1 + 4 * ell ** 2 * c) - 1) / 2
    ok = sp.simplify(roots[0] + beta) == 0 and sp.simplify(roots[1] - 1 - beta) == 0 or sp.simplify(roots[1] + beta) == 0 and sp.simplify(roots[0] - 1 - beta) == 0
    print("2: the exponents are -beta and 1 + beta with beta = (sqrt(1 + 4 ell^2 c) - 1)/2: %s; exp(2 r t) exp(-t) is integrable at infinity iff r < 1/2: the first is admitted, the second is not; at c = 0 they are 0 (a constant, admitted: the area is finite) and 1 (not admitted)" % ok)
    # 3: a source bounded by exp(-delta t): the solution's bound, with its constant
    b = sp.Symbol("beta", positive=True); pW = sp.simplify(sp.exp(-t) * (sp.diff(sp.exp((1 + b) * t), t) * sp.exp(-b * t) - sp.exp((1 + b) * t) * sp.diff(sp.exp(-b * t), t)))
    I1 = sp.exp(-b * t) * sp.exp((b - d) * t) / (b - d); I2 = sp.exp((1 + b) * t) * sp.exp(-(1 + b + d) * t) / (1 + b + d)
    bound = sp.simplify((I1 + I2) / pW * sp.exp(d * t)); want = 1 / ((b - d) * (1 + b + d))
    print("3: in Sturm-Liouville form the Wronskian constant is %s; for a source bounded by M exp(-delta t) with delta < beta the two Green's integrals give |f| <= M exp(-delta t) / ((beta - delta)(1 + beta + delta)): %s; and (beta - delta)(1 + beta + delta) = ell^2 c - delta - delta^2: %s" % (
        pW, sp.simplify(bound - want) == 0, sp.simplify(sp.expand((beta - d) * (1 + beta + d)) - (ell ** 2 * c - d - d ** 2)) == 0))
    print("   so the solution decays at the source's rate, with a constant that blows up as delta reaches beta: the lane's condition delta < min beta_c is exactly what is needed")
    h = sp.exp(t) * sp.integrate(sp.exp(-s) * sp.exp(-d * s), (s, t, sp.oo)); fp = -sp.integrate(h.subs(t, s), (s, t, sp.oo))
    print("   at c = 0 (the Q direction): f' = %s and f - a = %s for the source exp(-delta t): a constant plus a decaying term, for every delta > 0" % (sp.simplify(h), sp.simplify(fp)))
    # 4: nonzero angular frequency: -f'' + f' + (k^2 exp(2t) + ell^2 c) f = 0 is solved by exp(t/2) K_nu(k exp(t)), nu = beta + 1/2
    mp.mp.dps = 30; worst = 0
    for kk, lc in ((2 * mp.pi, mp.mpf(0)), (2 * mp.pi, mp.mpf("0.7")), (6 * mp.pi, mp.mpf("2.3"))):
        nu = mp.sqrt(mp.mpf(1) / 4 + lc); F = lambda tt: mp.exp(tt / 2) * mp.besselk(nu, kk * mp.exp(tt))
        for tt in (mp.mpf("-0.5"), mp.mpf("0.3"), mp.mpf("1.1")):
            res = -mp.diff(F, tt, 2) + mp.diff(F, tt) + (kk ** 2 * mp.exp(2 * tt) + lc) * F(tt); worst = max(worst, abs(res / F(tt)))
    print("4: at angular frequency k the decaying solution is exp(t/2) K_nu(k exp(t)) with nu = sqrt(1/4 + ell^2 c) = beta + 1/2: relative residual %s; it falls like exp(-k exp(t)), faster than any exponential, so these modes meet every weight" % mp.nstr(worst, 3))
    print("NOT checked here: that the background is exactly parallel on the whole cusp end (so that the operator separates into these channels); that the global kernel is exactly Q; the uniformity in the angular frequency in the presence of the lane's first-order angular drift; the Schauder and core-matching steps; and everything after (3) (the two implicit-function arguments), which rests on the lane's earlier proof files")
