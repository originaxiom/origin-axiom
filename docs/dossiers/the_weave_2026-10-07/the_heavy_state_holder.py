#!/usr/bin/env python3
"""W150 — the frame's heavy states as tau's holder: Higaki, Kawamura and Kobayashi's one-loop mechanism on every
singlet form of the joint family group (the rule: W150_RULE.md, committed and pushed before this script).

  V = (m0^2 / 16 pi^2) f(m_Q^2), f(u) = u (log(u / mu^2) - 1), m_Q^2 = M^2 (2 Im tau)^k |Y(tau)|^2, M = |c0| M_Q;
  every form below has leading coefficient 1, so mu = M means the crossing m_Q = mu is (2 Im tau)^k |Y|^2 = 1.

  H1  sympy: d f(u(x, y)) / dx = log(u / mu^2) du/dx; g(t) = t log t - t + 1 has g(1) = g'(1) = 0 and g'' = 1/t,
      so f >= -mu^2 with equality exactly at u = mu^2
  H2  the leading term x^k e^{-px} = 1 beyond x = k/p, p = 2 pi / 3, k = 6, 8, 10, 12: the root to two significant
      figures against the paper's 3.9, 7.9, 12, 16, and against -(k/p) W_{-1}(-p/k) to 1e-10
  H3  the slope of ln|Y(iy)| over y = 3, 3.5, ..., 6 for every form: -pi for the 1' forms, 0 for the level-1 forms
      other than Delta, -2 pi for Delta, each to 1e-3
  H4  along tau = iy, y in (1, 8] (step 1e-4 on (1, 1.3], 1e-3 beyond): every sign change of ln m_Q^2 / M^2,
      refined to 1e-15; a crossing is "cusp side" when m_Q^2 decreases there; each is checked to be a local minimum
      of V; the predicted cusp-side Im tau0 (2.66, 3.95, 5.23, 6.55 for the 1' forms of weight 10, 12, 14, 16, each to
      +-0.02; none at weight 6, none for a level-1 form) and the predicted near-i crossings (in (1, 1.3) exactly for
      the forms with a factor E6)
  H5  the weight-10 level curve m_Q = mu through tau0, at Re tau = -0.5, -0.45, ..., 0.5: its Im tau within 3e-5 of
      tau0's, and V / (-(m0^2/16 pi^2) mu^2) - 1 below 1e-20 there
  H6  the leading-term bounds (k / (pi e))^{k/2} against 2.20 and 7.70 (1%); the window ends sqrt(x^k e^{-pi x}) at
      x = 7.2 and 4.0 against [0.237, 1.91] and [1.71, 7.65] (1%); the exact forms' window ends against the leading
      ones (1%); and the phrase "about a factor 8 in mu/M at either weight", read as a factor in [6, 10] at each
  R   read-outs: the weight-10 curve's Im tau0 beside S215's 2.6-2.7 (no test); d^2 V / d(Im tau)^2 across the curve
      at tau0, in units of m0^2 M^2 / 16 pi^2 (equal to (d ln u / dy)^2 there, since f'(1) = 0 and f''(1) = 1)

  FLAGGED BEFORE THE RUN (the rule is pushed and is not changed): H6's phrase "about a factor 8 in mu/M at either
  weight" does not follow from the rule's own window at weight 12, where 7.65 / 1.71 = 4.5. The cell is scored as
  worded, with "about a factor 8" read as [6, 10], so H6 is expected to fail on that phrase.

  The thetas are not used; eta is W146's direct product; E4 and E6 are direct divisor sums (CONVENTIONS section 4).

    python3 -B the_heavy_state_holder.py      # writes the_heavy_state_holder.json beside itself
"""
import contextlib
import io
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_higgs_invariant_dichotomy as W146  # noqa: E402  (eta_pow: eta by its product, any tau)

OUT = HERE / "the_heavy_state_holder.json"
mp.mp.dps = 30
J = mp.mpc(0, 1)
PI = mp.pi


def s(x, n=6):
    return mp.nstr(x, n)


# ---------------------------------------------------------------- the forms

def sigma(n, k):
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def eis(tau, k, c):
    q = mp.exp(2 * PI * J * tau)
    eps = mp.mpf(10) ** (-(mp.mp.dps + 10))
    tot, n, qn = mp.mpc(1), 1, q
    while True:
        t = c * sigma(n, k - 1) * qn
        tot += t
        if n > 3 and abs(t) < eps:
            return tot
        n += 1
        qn *= q


def E4(tau):
    return eis(tau, 4, 240)


def E6(tau):
    return eis(tau, 6, -504)


def eta(tau, p):
    return W146.eta_pow(tau, p)


FORMS = {
    # name: (weight, class, factor E6, function)
    "eta^12": (6, "1'", False, lambda t: eta(t, 12)),
    "eta^12 E4": (10, "1'", False, lambda t: eta(t, 12) * E4(t)),
    "eta^12 E6": (12, "1'", True, lambda t: eta(t, 12) * E6(t)),
    "eta^12 E4^2": (14, "1'", False, lambda t: eta(t, 12) * E4(t) ** 2),
    "eta^12 E4 E6": (16, "1'", True, lambda t: eta(t, 12) * E4(t) * E6(t)),
    "E4": (4, "1", False, E4),
    "E6": (6, "1", True, E6),
    "E4^2": (8, "1", False, lambda t: E4(t) ** 2),
    "E4 E6": (10, "1", True, lambda t: E4(t) * E6(t)),
    "E4^3": (12, "1", False, lambda t: E4(t) ** 3),
    "E6^2": (12, "1", True, lambda t: E6(t) ** 2),
    "Delta": (12, "1", False, lambda t: eta(t, 24)),
}


def lnu(name, tau):
    k, _, _, Y = FORMS[name]
    return k * mp.log(2 * mp.im(tau)) + 2 * mp.log(abs(Y(tau)))


# ---------------------------------------------------------------- H1

def H1():
    x, y, mu, t = sp.symbols("x y mu t", positive=True)
    u = sp.Function("u")(x, y)
    V = u * (sp.log(u / mu ** 2) - 1)
    chain = all(sp.simplify(sp.diff(V, v) - sp.log(u / mu ** 2) * sp.diff(u, v)) == 0 for v in (x, y))
    g = t * sp.log(t) - t + 1
    gibbs = (sp.simplify(g.subs(t, 1)) == 0 and sp.simplify(sp.diff(g, t).subs(t, 1)) == 0
             and sp.simplify(sp.diff(g, t, 2) - 1 / t) == 0)
    fmin = sp.simplify((u * (sp.log(u / mu ** 2) - 1)).subs(u, mu ** 2) + mu ** 2) == 0
    res = {"dV = log(u/mu^2) du (both directions)": bool(chain), "g(1) = g'(1) = 0, g'' = 1/t": bool(gibbs),
           "f(mu^2) = -mu^2": bool(fmin)}
    return res, bool(chain and gibbs and fmin)


# ---------------------------------------------------------------- H2

def sig2(x):
    return float(mp.nstr(x, 2))


def leading_root(k, p, mu_over_M=1):
    """the root of x^k e^{-px} = (mu/M)^2 beyond x = k/p, or None"""
    target = 2 * mp.log(mu_over_M)
    g = lambda xx: k * mp.log(xx) - p * xx - target
    x0 = mp.mpf(k) / p
    if g(x0) < 0:
        return None
    hi = x0 * 2
    while g(hi) > 0:
        hi *= 2
    return mp.findroot(g, (x0, hi), solver="bisect", tol=mp.mpf(10) ** -25)


def H2():
    p = 2 * PI / 3
    want = {6: 3.9, 8: 7.9, 10: 12.0, 12: 16.0}
    rows, ok = {}, True
    for k, w in want.items():
        r = leading_root(k, p)
        lw = -(mp.mpf(k) / p) * mp.lambertw(-p / k, -1).real
        rows[str(k)] = {"root": s(r, 8), "two figures": sig2(r), "paper": w, "|root - Lambert|": s(abs(r - lw), 3)}
        ok &= sig2(r) == w and abs(r - lw) < mp.mpf("1e-10")
    return rows, bool(ok)


# ---------------------------------------------------------------- H3

def H3():
    ys = [mp.mpf(3) + mp.mpf(i) / 2 for i in range(7)]
    rows, ok = {}, True
    for name, (k, cls, _, Y) in FORMS.items():
        vals = [mp.log(abs(Y(J * y))) for y in ys]
        n = len(ys)
        my, mv = sum(ys) / n, sum(vals) / n
        slope = sum((a - my) * (b - mv) for a, b in zip(ys, vals)) / sum((a - my) ** 2 for a in ys)
        want = -PI if cls == "1'" else (-2 * PI if name == "Delta" else 0)
        rows[name] = {"slope": s(slope, 8), "predicted": s(want, 8)}
        ok &= abs(slope - want) < mp.mpf("1e-3")
    return rows, bool(ok)


# ---------------------------------------------------------------- H4

def crossings(name):
    ys = [1 + mp.mpf(i) / 10 ** 4 for i in range(1, 3001)] + [mp.mpf("1.3") + mp.mpf(i) / 10 ** 3 for i in
                                                                  range(1, 6701)]
    vals = [lnu(name, J * y) for y in ys]
    out = []
    for a, b, va, vb in zip(ys, ys[1:], vals, vals[1:]):
        if va == 0 or (va < 0) != (vb < 0):
            y0 = mp.findroot(lambda yy: lnu(name, J * yy), (a, b), solver="bisect", tol=mp.mpf(10) ** -15)
            h = mp.mpf("1e-6")
            decreasing = lnu(name, J * (y0 + h)) < lnu(name, J * (y0 - h))
            V = lambda yy: (lambda u: u * (mp.log(u) - 1))(mp.e ** lnu(name, J * yy))
            is_min = V(y0 + mp.mpf("1e-3")) > V(y0) and V(y0 - mp.mpf("1e-3")) > V(y0)
            out.append((y0, bool(decreasing), bool(is_min)))
    return out


def H4():
    want_cusp = {"eta^12 E4": 2.66, "eta^12 E6": 3.95, "eta^12 E4^2": 5.23, "eta^12 E4 E6": 6.55}
    rows, ok = {}, True
    for name, (k, cls, has_e6, _) in FORMS.items():
        cr = crossings(name)
        cusp = [y for y, dec, _ in cr if dec]
        near = [y for y, _, _ in cr if y < mp.mpf("1.3")]
        rows[name] = {"weight": k, "class": cls, "crossings (Im tau, cusp side, local minimum of V)":
                      [[s(y, 8), d, m] for y, d, m in cr]}
        ok &= all(m for _, _, m in cr)
        if name in want_cusp:
            ok &= len(cusp) == 1 and abs(cusp[0] - want_cusp[name]) <= mp.mpf("0.02")
        else:
            ok &= len(cusp) == 0
        ok &= (len(near) == 1) if has_e6 else (len(near) == 0)
    return rows, bool(ok)


# ---------------------------------------------------------------- H5

def H5(rows4):
    name = "eta^12 E4"
    y0 = [mp.mpf(c[0]) for c in rows4[name]["crossings (Im tau, cusp side, local minimum of V)"] if c[1]][0]
    y0 = mp.findroot(lambda yy: lnu(name, J * yy), y0, tol=mp.mpf(10) ** -25)
    worst_dy, worst_v, pts = mp.mpf(0), mp.mpf(0), []
    for i in range(21):
        x = mp.mpf(-1) / 2 + mp.mpf(i) / 20
        yx = mp.findroot(lambda yy: lnu(name, x + J * yy), y0, tol=mp.mpf(10) ** -25)
        u = mp.e ** lnu(name, x + J * yx)
        V = u * (mp.log(u) - 1)
        worst_dy = max(worst_dy, abs(yx - y0))
        worst_v = max(worst_v, abs(V / (-1) - 1))
        pts.append([s(x, 3), s(yx, 10)])
    res = {"Im tau0 on Re tau = 0": s(y0, 12), "the curve (Re tau, Im tau)": pts,
           "max |Im tau(x) - Im tau0|": s(worst_dy, 3), "max |V / V_min - 1|": s(worst_v, 3)}
    return res, bool(worst_dy < mp.mpf("3e-5") and worst_v < mp.mpf("1e-20")), y0


# ---------------------------------------------------------------- H6

def H6():
    bound = {k: (mp.mpf(k) / (PI * mp.e)) ** (mp.mpf(k) / 2) for k in (10, 12)}
    lead = {k: (mp.sqrt(mp.mpf(7.2) ** k * mp.e ** (-PI * 7.2)), mp.sqrt(mp.mpf(4) ** k * mp.e ** (-PI * 4)))
            for k in (10, 12)}
    exact_name = {10: "eta^12 E4", 12: "eta^12 E6"}
    exact = {k: (mp.sqrt(mp.e ** lnu(exact_name[k], J * mp.mpf("3.6"))), mp.sqrt(mp.e ** lnu(exact_name[k], J * 2)))
             for k in (10, 12)}
    want_b = {10: 2.20, 12: 7.70}
    want_w = {10: (0.237, 1.91), 12: (1.71, 7.65)}
    rel = lambda a, b: abs(a - b) / abs(b)
    ok_b = all(rel(bound[k], want_b[k]) < 0.01 for k in (10, 12))
    ok_w = all(rel(lead[k][0], want_w[k][0]) < 0.01 and rel(lead[k][1], want_w[k][1]) < 0.01 for k in (10, 12))
    ok_e = all(rel(exact[k][0], lead[k][0]) < 0.01 and rel(exact[k][1], lead[k][1]) < 0.01 for k in (10, 12))
    factor = {k: lead[k][1] / lead[k][0] for k in (10, 12)}
    ok_f = all(6 <= factor[k] <= 10 for k in (10, 12))
    res = {"existence bounds (k/(pi e))^{k/2}": {str(k): s(v, 5) for k, v in bound.items()},
           "window ends, leading term (Im tau 3.6, 2.0)": {str(k): [s(a, 5), s(b, 5)] for k, (a, b) in lead.items()},
           "window ends, exact forms (Im tau 3.6, 2.0)": {str(k): [s(a, 5), s(b, 5)] for k, (a, b) in exact.items()},
           "factor across the band": {str(k): s(v, 4) for k, v in factor.items()},
           "parts": {"bounds within 1%": bool(ok_b), "windows within 1%": bool(ok_w),
                     "exact within 1% of leading": bool(ok_e), "factor in [6, 10] at each weight": bool(ok_f)}}
    return res, bool(ok_b and ok_w and ok_e and ok_f)


def main():
    out = {"arc": "W150", "rule": "W150_RULE.md", "status": "one run", "python": sys.version.split()[0]}
    out["H1"], ok1 = H1()
    out["H2"], ok2 = H2()
    out["H3"], ok3 = H3()
    out["H4"], ok4 = H4()
    out["H5"], ok5, y0 = H5(out["H4"])
    out["H6"], ok6 = H6()
    h = mp.mpf("1e-8")
    d = (lnu("eta^12 E4", J * (y0 + h)) - lnu("eta^12 E4", J * (y0 - h))) / (2 * h)
    out["R"] = {"weight-10 Im tau0": s(y0, 8), "S215's band (seen before the rule; no test)": "2.6-2.7",
                "d^2V/dy^2 at tau0 in units of m0^2 M^2/16 pi^2 = (d ln u/dy)^2": s(d ** 2, 8)}
    out["cells"] = {"H1": ok1, "H2": ok2, "H3": ok3, "H4": ok4, "H5": ok5, "H6": ok6}
    out["every predicted cell holds"] = bool(all(out["cells"].values()))
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])


if __name__ == "__main__":
    main()
