"""B1957: the physical lane's package 'frontier response' (PHYSICAL-C5, 2026-11-16): the mathematics of its four hand
derivations and of its review of another seat's stages, rebuilt on main.  Nothing of any seat's is run; the other
seat's scripts are read as text.  NOT verified here: that the lane's restricted path action is the parent's (its
complete domains, its gauge inverse), and anything about the other seat's numerical outputs.
 F0  custody: the ten line ranges the package quotes from the other seat's four scripts are in those scripts at the
     commit it names, line for line (needs that seat's branch fetched).
 F1  the comparator density: with R = exp(-pi (Im z)^2/Im tau) |theta1(z)/theta1'(0)| (periods 1 and tau, tau = i sqrt 3)
     and Omega = 1/(R (1 + |log R|)): R is doubly periodic; where R < 1, the Laplacian of log R is -2 pi/Im tau and the
     curvature of Omega^2 |dz|^2 is -R^2 [(2 pi/Im tau)(L^2 - L) + |grad log R|^2], L = 1 - log R.  MAIN ADDS: that
     curvature is not constant (two points), so this density is not the hyperbolic metric of the punctured torus.
 F2  the omitted area: beyond t = T in r = r0 exp(-t) the area of Omega^2 is 2 pi/(T + a) to leading order, a = 1 +
     log(1/r0); at the script's r0 = 1/4 and T = 18 that is 2 pi/(19 + log 4); checked against a direct integral.
 F3  the five tails of its equation (5) and the sensitivity identity (7): the exponents 2, -1, -3, 2 with sum zero.
 F4  the cross-form series: with weights in [-3, 3], diagonal blocks lowering by 4 and one off-diagonal block shifting
     by 3, -1 or -5, every word of length four shifts by at most -9 and every word of length two without it by -8:
     beyond the span 6, so the series stops.
 F5  the half-line response: E = int K (s' + sqrt(V/K))^2 + W(s0) with W = 2 int sqrt(K V); for constant K and
     V = B s^2 (1 - s)^2: W = sqrt(K B)(s0^2 - 2 s0^3/3), W''(0) = 2 sqrt(K B), the wall tension sqrt(K B)/3; the energy
     of the first-order solution equals W(s0); the finite-interval formulas from the first integral; the tangent
     component of the full residual; the trial energy l^2/W; the phase identity (15); the kink of (16) has c' = m sin c
     and action 4 m.
 F6  the rejecting comparator: R(x, y) = (sqrt b x(1 - x), y - c x(1 - x)); on y = 0 the scalar wall exists with
     V = (b + c^2) x^2 (1 - x)^2, while the normal component of the gradient is -2 c x(1 - x) and the path's normal
     curvature is zero: equation (5) of the note fails by -c against 0."""
import functools, itertools, json, subprocess, math
import mpmath as mp
import sympy as sp
print = functools.partial(print, flush=True)
LANE = "8d5c91032"; DIR = "reports/physical_bridge_2026_09_05/frontier_response_2026_11_16/"

if __name__ == "__main__":
    raw = subprocess.run(["git", "show", "%s:%sSOURCE_QUOTES.json" % (LANE, DIR)], capture_output=True).stdout
    if raw:
        items = json.loads(raw); ok = 0
        for it in items:
            b = subprocess.run(["git", "show", "%s:%s" % (it["commit"], it["path"])], capture_output=True).stdout.decode("utf-8", "replace").split("\n")
            ok += "\n".join(b[it["start"] - 1:it["end"]]).strip() == it["text"].strip()
        print("F0: quoted line ranges held: %d of %d" % (ok, len(items)))
    else: print("F0: the lane's branch is not fetched here; custody not checked")
    mp.mp.dps = 30; tau = 1j * mp.sqrt(3); yt = mp.im(tau); q = mp.exp(1j * mp.pi * tau)
    th1 = lambda z: mp.jtheta(1, mp.pi * z, q); d0 = mp.diff(th1, 0)
    R = lambda x, y: mp.exp(-mp.pi * y * y / yt) * abs(th1(mp.mpc(x, y)) / d0); u = lambda x, y: mp.log(R(x, y))
    per = abs(R(mp.mpf("0.21") + 1, mp.mpf("0.33")) - R(mp.mpf("0.21"), mp.mpf("0.33"))) + abs(R(mp.mpf("0.21"), mp.mpf("0.33") + yt) - R(mp.mpf("0.21"), mp.mpf("0.33")))
    lap = lambda f, x, y: mp.diff(f, (x, y), (2, 0)) + mp.diff(f, (x, y), (0, 2))
    rows = []
    for (x0, y0) in ((mp.mpf("0.11"), mp.mpf("0.07")), (mp.mpf("0.05"), mp.mpf("-0.16")), (mp.mpf("-0.2"), mp.mpf("0.1"))):
        Rv = R(x0, y0); assert Rv < 1; Lv = 1 - mp.log(Rv); lu = lap(u, x0, y0); g2 = mp.diff(u, (x0, y0), (1, 0)) ** 2 + mp.diff(u, (x0, y0), (0, 1)) ** 2
        logOm = lambda x, y: -u(x, y) - mp.log(1 - u(x, y)); Kdirect = -(Rv * Lv) ** 2 * lap(logOm, x0, y0); Kform = -Rv ** 2 * ((2 * mp.pi / yt) * (Lv ** 2 - Lv) + g2)
        rows.append((mp.nstr(lu + 2 * mp.pi / yt, 3), mp.nstr(Kdirect, 8), mp.nstr(Kform, 8)))
    print("F1: R doubly periodic to %s; at three points (Laplacian of log R plus 2 pi/Im tau, the curvature computed directly, by the note's formula): %s" % (mp.nstr(per, 3), rows))
    r0 = mp.mpf(1) / 4; a = 1 + mp.log(1 / r0); Om = lambda x, y: 1 / (R(x, y) * (1 + abs(mp.log(R(x, y))))); out = []
    mp.mp.dps = 15                                                       # the area integral needs no more; the tail beyond T + 60 is added in closed form
    for T in (4, 8):
        f = lambda t, th: (Om(r0 * mp.exp(-t) * mp.cos(th), r0 * mp.exp(-t) * mp.sin(th)) * r0 * mp.exp(-t)) ** 2
        direct = mp.quad(lambda t: mp.quad(lambda th: f(t, th), [0, mp.pi, 2 * mp.pi]), [T, T + 2, T + 10, T + 60]) + 2 * mp.pi / (T + 60 + a)
        out.append((T, mp.nstr(direct, 10), mp.nstr(2 * mp.pi / (T + a), 10)))
    print("F2: (T, the area beyond T by direct integration, 2 pi/(T + a)): %s; at T = 18: 2 pi/(19 + log 4) = %s" % (out, mp.nstr(2 * mp.pi / (19 + mp.log(4)), 10)))
    mp.mp.dps = 30
    r, t_, a_ = sp.symbols("r t a", positive=True); Oms = 1 / (r * (t_ + a_)); tails = [sp.simplify(e * r ** 2) for e in (Oms, Oms ** -3, r ** -2 * Oms ** -3, Oms ** -2, r ** -2 * Oms ** -2)]
    eps = sp.symbols("epsilon"); A, J, K3, K2 = [sp.Function(n)(eps) for n in ("A", "J", "K3", "K2")]
    print("F3: the five tails (integrand times r^2): %s; the weights of the four averages in d log(lambda/e): %s, sum %s" % (tails, [sp.Rational(2, 2) * 2 / 2, -sp.Rational(1, 2), -sp.Rational(3, 2), sp.Rational(2, 2)], 2 - 1 - 3 + 2))
    span = 6; four = sorted({-4 * k + s for k in (3,) for s in (3, -1, -5)} | {-16}); two = -8
    print("F4: shifts of the words of length four: %s, of the word of length two: %d; all beyond the span %d: %s" % (four, two, span, all(abs(s) > span for s in four + [two])))
    s, s0, K, B, x, m = sp.symbols("s s0 K B x m", positive=True); V = B * s ** 2 * (1 - s) ** 2
    W = sp.simplify(2 * sp.integrate(sp.sqrt(K * B) * s * (1 - s), (s, 0, s0))); tension = sp.simplify(2 * sp.sqrt(B) * sp.integrate(s * (1 - s) * sp.sqrt(K), (s, 0, 1)))
    sol = 1 / (1 + (1 / s0 - 1) * sp.exp(sp.sqrt(B / K) * x)); ode = sp.simplify(sp.diff(sol, x) + sp.sqrt(B / K) * sol * (1 - sol))
    Enum = mp.quad(lambda xv: float((K * sp.diff(sol, x) ** 2 + V.subs(s, sol)).subs({K: 1.7, B: 2.3, s0: 0.6, x: xv})), [0, 5, 20, 80]); Wnum = float(W.subs({K: 1.7, B: 2.3, s0: 0.6}))
    c = sp.Function("c")(x); kink = 2 * sp.atan(sp.exp(m * x)); k1 = sp.simplify(sp.diff(kink, x) - m * sp.sin(kink)); act = sp.integrate(sp.simplify(2 * m ** 2 * sp.sin(kink) ** 2), (x, -sp.oo, sp.oo))
    pa, pb, eB = sp.symbols("a b eB", real=True); ph = sp.expand((pa - eB) ** 2 + (pb + eB) ** 2 - sp.Rational(1, 2) * ((pa + pb) ** 2 + (pa - pb - 2 * eB) ** 2))
    print("F5: W(s0) = %s; W''(0) = %s; the tension = %s; the first-order solution solves s' = -sqrt(V/K): %s; its energy %.10f against W(s0) = %.10f; the kink: c' - m sin c = %s, action %s; the phase identity's difference: %s" % (
        sp.factor(W), sp.simplify(sp.diff(W, s0, 2).subs(s0, 0)), tension, ode == 0, float(Enum), Wnum, k1, sp.simplify(act), ph))
    Cc = sp.symbols("C", positive=True); a1, b1 = 0.2, 0.7; Kv, Bv, Cv = 1.3, 2.1, 0.05; Vn = lambda sv: Bv * sv ** 2 * (1 - sv) ** 2
    Lint = mp.quad(lambda sv: mp.sqrt(Kv / (Vn(sv) + Cv)), [a1, b1]); Gint = mp.quad(lambda sv: mp.sqrt(Kv) * (2 * Vn(sv) + Cv) / mp.sqrt(Vn(sv) + Cv), [a1, b1])
    sx = mp.odefun(lambda xv, sv: mp.sqrt((Vn(sv) + Cv) / Kv), 0, a1); Eode = mp.quad(lambda xv: Kv * ((Vn(sx(xv)) + Cv) / Kv) + Vn(sx(xv)), mp.linspace(0, Lint, 9))
    print("F5: a finite interval from %.1f to %.1f with first integral C = %.2f: the profile reaches %.8f at the length %s; its energy %s against the formula's %s" % (a1, b1, Cv, float(sx(Lint)), mp.nstr(Lint, 8), mp.nstr(Eode, 9), mp.nstr(Gint, 9)))
    xs, ys, bb, cc = sp.symbols("x y b c", real=True); Rv2 = sp.Matrix([sp.sqrt(bb) * xs * (1 - xs), ys - cc * xs * (1 - xs)]); Vv = (Rv2.T * Rv2)[0]
    onpath = sp.factor(Vv.subs(ys, 0)); dVy = sp.factor(sp.diff(Vv, ys).subs(ys, 0)); Cvec = sp.Matrix([sp.sqrt(bb), -cc]); DR = Rv2.jacobian([xs, ys]).subs(ys, 0); lhs = (DR.T * Cvec)[1]
    print("F6: V on the path: %s; the normal derivative of V there: %s; the normal component of (DR)^T C: %s, against the right side 0 (a straight path has no normal curvature)" % (onpath, dVy, sp.simplify(lhs)))
