"""B1959's lock: K1, K2 and K3 (symbolic), K4 and K7 recomputed here (no stored number is read), with controls for K1, K3
and K4 and a growth check for K7's.  K5, K6 and K2's eigenvalue count are not in this lock (corrected 2026-11-19 at
Review 85, finding B8: this line said every computable step, each with the change that breaks it; owed, R85-3)."""
import math, pathlib, sys
import numpy as np
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cusp_inverse as CI


def test_the_channel_potential_is_a_perfect_square():
    t, x, w, m = sp.symbols("t x w m", real=True); e = sp.exp(sp.I * m * x)
    Dx = lambda g: sp.diff(g, x) + sp.I * (w / 2) * sp.exp(-t) * g
    assert sp.simplify(-sp.exp(2 * t) * Dx(Dx(e)) / e - (m * sp.exp(t) + w / 2) ** 2) == 0
    Dbad = lambda g: sp.diff(g, x) + sp.I * (w / 2) * g                                       # the control: a connection that does not shrink with the circle
    assert sp.simplify(-sp.exp(2 * t) * Dbad(Dbad(e)) / e - (m * sp.exp(t) + w / 2) ** 2) != 0


def test_the_two_conjugations_and_the_threshold():
    t, d, V = sp.symbols("t delta V", real=True); v = sp.Function("v"); W = sp.Function("W")
    u = sp.exp(t / 2) * v(t); assert sp.simplify((-sp.diff(u, t, 2) + sp.diff(u, t)) / sp.exp(t / 2) - (-sp.diff(v(t), t, 2) + v(t) / 4)) == 0
    u = sp.exp(-d * t) * W(t)
    assert sp.simplify((-sp.diff(u, t, 2) + sp.diff(u, t) + V * u) * sp.exp(d * t) - (-sp.diff(W(t), t, 2) + (1 + 2 * d) * sp.diff(W(t), t) + (V - d - d ** 2) * W(t))) == 0
    c, ell = sp.symbols("c ell", positive=True); b = (sp.sqrt(1 + 4 * ell ** 2 * c) - 1) / 2
    assert sp.simplify(b ** 2 + b - ell ** 2 * c) == 0                                         # so V = ell^2 c exceeds delta + delta^2 exactly when delta < beta
    assert sp.simplify((b / 2) ** 2 + b / 2 - ell ** 2 * c) != 0


def test_a_decaying_source_gives_a_decaying_solution_below_beta_and_not_above():
    L, c = 1.5, 0.4; V0 = L * L * c; beta = (math.sqrt(1 + 4 * V0) - 1) / 2; tt = np.linspace(0, 40, 8001); g = np.cos(1.3 * tt)
    def worst(delta, upto):
        u = CI.mode_solve(np.full(len(tt), V0), L * L * np.exp(-delta * tt) * g, tt, 1.0).real; return float(np.max(np.exp(delta * tt[tt < upto]) * np.abs(u[tt < upto])))
    d = 0.3; assert d < beta and worst(d, 30) <= max(1.0, L * L / (V0 - d - d * d)) + 1e-6      # the maximum principle's bound
    assert 0.8 > beta and worst(0.8, 30) > 50 * worst(0.8, 10)                                 # beyond beta the weighted solution grows


def test_the_constant_tail_is_fixed_by_the_source_and_is_needed():
    dl = 0.3; R0 = 3 * math.pi / 4; n = 20001; tt = np.linspace(-R0, 20.0, n); h = tt[1] - tt[0]; mid = (tt[:-1] + tt[1:]) / 2
    phi = np.where(tt < 0, math.sqrt(2) * np.sin(tt + R0), np.exp(-tt)); pm = np.where(mid < 0, math.sqrt(2) * np.sin(mid + R0), np.exp(-mid)); cell = np.full(n, h); cell[0] = cell[-1] = h / 2
    wgt = np.maximum(phi, 0) * cell; wgt[0] = pm[0] * h / 4; area = wgt.sum(); bump = np.where(tt < 0, np.sin(np.pi * np.clip(-tt / R0, 0, 1)) ** 2, 0.0); cusp = tt >= 0
    def solve(src):
        u = np.concatenate([[0.0], np.cumsum(-np.cumsum(src * wgt)[:-1] / pm * h)]); return u - np.sum(u * wgt) / area
    f = np.where(cusp, np.exp(-dl * np.maximum(tt, 0)), 1.0) * np.cos(1.3 * tt); f = f - bump * np.sum(f * wgt) / np.sum(bump * wgt)
    u = solve(f); a = u[-1]; fc = np.max(np.exp(dl * tt[cusp]) * np.abs(f[cusp]))
    assert abs(area - (math.sqrt(2) + 2)) < 1e-3 and abs(a) > 0.05                              # the constant is there, and is not zero
    assert np.max(np.exp(dl * tt[cusp]) * np.abs(u[cusp] - a)) <= fc / (dl * (1 + dl)) + 1e-6   # the rest decays, within the proved bound
    g = f + 0.2 * cusp; g = g - bump * np.sum(g * wgt) / np.sum(bump * wgt); u2 = solve(g)
    assert abs(u2[np.searchsorted(tt, 18.0)] - u2[np.searchsorted(tt, 8.0)]) > 1.5              # the control: a source that does not decay has no constant tail
