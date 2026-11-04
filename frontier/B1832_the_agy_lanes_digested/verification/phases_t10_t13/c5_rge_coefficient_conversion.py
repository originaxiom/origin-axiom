"""agy digest, Phase 3 / audit finding 6 / Theorem 12 -- the RGE TOOL only (every m_H, M_t number built on it is a VALUE
claim and is not re-run here).  Two checks, sympy:
  R1  the rate: with t = ln(mu/M_Z)/(2 pi), d/dt = 4 pi d/d ln mu^2, so a beta written for d/d ln mu^2 as
      b1/(4 pi)^2 + b2/(4 pi)^4 needs f1 = 1/(4 pi), f2 = 1/(64 pi^3); the legacy 1/(8 pi), 1/(128 pi^3) on y_t^2 and lambda
      run them at half rate while the legacy gauge lines (41/5, -19/3, -14 at 1/(8 pi)) run at full rate.
  R2  the two-loop lambda polynomial at 18c607040 (all three copies: phase3's corrected integrator, the audit function,
      Theorem 12) against the standard two-loop SM lambda beta in (g, g') normalisation for d/d ln mu, V = lambda (H^+H)^2,
      AS RECALLED here (Ford-Jack-Jones / Luo-Wang-Xiao form) -- converted to d/d ln mu^2 and g1^2 = (5/3) g'^2.
      Recalled, not read from the paper on this bench: main confirms against arXiv:1307.3536's appendix before relying on it.
"""
import json, pathlib
import sympy as sp
OUT = {}
def rec(k, v): OUT[k] = v; print(k, ":", v)
pi = sp.pi
mu = sp.symbols("mu", positive=True)
t = sp.log(mu) / (2 * pi)                        # up to the constant ln M_Z
rec("R1 d ln(mu^2)/dt", sp.simplify(sp.diff(2 * sp.log(mu), mu) / sp.diff(t, mu)))
rec("R1 f1 = 4 pi/(4 pi)^2, f2 = 4 pi/(4 pi)^4", [str(sp.simplify(4 * pi / (4 * pi) ** 2)), str(sp.simplify(4 * pi / (4 * pi) ** 4))])
rec("R1 legacy gauge 41/5 * 1/(8 pi) == 41/10 * 1/(4 pi)", sp.simplify(sp.Rational(41, 5) / (8 * pi) - sp.Rational(41, 10) / (4 * pi)) == 0)

lam, yt, g, gp, gs = sp.symbols("lam yt g gp gs", positive=True)   # yt, g, gp, gs are the SQUARED couplings here
std = (-312 * lam ** 3 - 144 * lam ** 2 * yt - 3 * lam * yt ** 2 + 30 * yt ** 3 + 80 * lam * gs * yt - 32 * gs * yt ** 2
       + 36 * lam ** 2 * (3 * g + gp) + lam * yt * (sp.Rational(45, 2) * g + sp.Rational(85, 6) * gp) - sp.Rational(8, 3) * gp * yt ** 2
       - sp.Rational(73, 8) * lam * g ** 2 + sp.Rational(39, 4) * lam * g * gp + sp.Rational(629, 24) * lam * gp ** 2
       + sp.Rational(305, 16) * g ** 3 - sp.Rational(289, 48) * g ** 2 * gp - sp.Rational(559, 48) * g * gp ** 2 - sp.Rational(379, 48) * gp ** 3
       - sp.Rational(9, 4) * g ** 2 * yt + sp.Rational(21, 2) * g * gp * yt - sp.Rational(19, 4) * gp ** 2 * yt)
g1, g2, g3 = sp.symbols("g1 g2 g3", positive=True)                    # squared, GUT-normalised g1
conv = sp.expand((std / 2).subs({gp: sp.Rational(3, 5) * g1, g: g2, gs: g3}))
R = sp.Rational
lane = (-156 * lam ** 3 - 72 * lam ** 2 * yt - R(3, 2) * lam * yt ** 2 + 15 * yt ** 3 + 40 * g3 * lam * yt - 16 * g3 * yt ** 2
        + lam ** 2 * (54 * g2 + R(54, 5) * g1) + lam * yt * (R(45, 4) * g2 + R(17, 4) * g1) - R(4, 5) * g1 * yt ** 2
        - R(9, 8) * g2 ** 2 * yt - R(171, 200) * g1 ** 2 * yt + R(63, 20) * g1 * g2 * yt
        - R(73, 16) * lam * g2 ** 2 + R(117, 40) * lam * g1 * g2 + R(1887, 400) * lam * g1 ** 2
        + R(305, 32) * g2 ** 3 - R(289, 160) * g1 * g2 ** 2 - R(1677, 800) * g1 ** 2 * g2 - R(3411, 4000) * g1 ** 3)
rec("R2 converted standard - lane (18c607040) two-loop lambda polynomial", str(sp.simplify(conv - lane)))
rec("R2 the 'factor-of-3' terms of the earlier version: 1887/400 = 3 x 629/400, 1677/800 = 3 x 559/800, 3411/4000 = 9 x 379/4000",
    [R(1887, 400) / R(629, 400), R(1677, 800) / R(559, 800), R(3411, 4000) / R(379, 4000)])
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(OUT, indent=1, default=str))
