"""W75: chat1's scale check on this seat's instruments, and the field's size at the puncture. The rule (W75_RULE.md)
was committed before this script.

  U1  the mirror pairs on every thread (745 Lyndon words, b++ bundles): isometry of b++swap(W) with b++W, the
      reversed copy's CS against -CS(W) and CS(swap W), and chat1's K1 count reproduced on the same instrument
  U2  the local model by the ODE in L: Hitchin's equation for h = diag(e^u, e^-u), theta = E21 dz/z is
      u'' + e^(-2u) = 0; its three branches; the shift L0 is a rescaling of z; the model h = diag(L, 1/L) directly
  U3  the uniformizing bundle in the log frame; it solves at c = 1 and not at c = 2; the flat connection on |z| = r
      is i N with N nilpotent, so the monodromy has trace 2, and -2 with the log frame's -1
  U4  the size: the pointwise norm of theta is 1/(2R) on unit vectors of a curvature -1/R^2 cusp metric; in the
      canonical coordinate L = 4 pi Im w and the residue's norm is the horocycle's length over 4 pi
  plus the read-outs: swap-symmetric threads, threads with CS = pi^2/2, U1's wall-clock, U3's N at three L

Fibre-level cells (U2 to U4) are facts of the shared fibre's end, the same on every thread; U1 is a census of every
thread under chat1's stated rule.

Run: python3 the_puncture_scale.py  ->  the_puncture_scale.json beside it.
"""
import itertools
import json
import math
import time
import warnings
from pathlib import Path

import snappy
import sympy as sp

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
OUT = HERE / "the_puncture_scale.json"
PI2 = math.pi ** 2


def red(v):                                     # reduce mod pi^2 to (-pi^2/2, pi^2/2]
    w = math.fmod(v, PI2)
    if w > PI2 / 2:
        w -= PI2
    if w <= -PI2 / 2:
        w += PI2
    return w


def least_rotation(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def is_lyndon(w):
    return all(w < w[i:] + w[:i] for i in range(1, len(w)))


def swap(w):
    return w.translate(str.maketrans("LR", "RL"))


def cs_of(M):
    return red(complex(M.complex_volume()).imag)


def u1():
    t0 = time.time()
    threads = [w for n in range(2, 13) for w in ("".join(p) for p in itertools.product("LR", repeat=n))
               if is_lyndon(w)]
    cs, iso_fail, rev_bad, swap_bad, errors = {}, [], [], [], []
    for w in threads:
        cs[w] = cs_of(snappy.Manifold("b++" + w))
    for w in threads:
        m = least_rotation(swap(w))
        try:
            A = snappy.Manifold("b++" + w)
            B = snappy.Manifold("b++" + m)
            if not A.is_isometric_to(B):
                iso_fail.append([w, m, "not isometric"])
        except Exception as e:                  # recorded as a failure, as the rule says
            iso_fail.append([w, m, repr(e)[:120]])
        try:
            R = snappy.Manifold("b++" + w)
            R.reverse_orientation()
            cr = cs_of(R)
            if abs(red(cr + cs[w])) > 1e-8:
                rev_bad.append([w, cs[w], cr])
            if m not in cs or abs(red(cr - cs[m])) > 1e-6:
                swap_bad.append([w, m, cr, cs.get(m)])
        except Exception as e:
            errors.append([w, repr(e)[:120]])
    nonzero = sum(1 for v in cs.values() if abs(v) > 1e-6)
    symm = [w for w in threads if least_rotation(swap(w)) in (w, least_rotation(w[::-1]))]
    half = [w for w in threads if abs(abs(cs[w]) - PI2 / 2) < 1e-6]
    out = {"threads": len(threads), "isometry failures": iso_fail, "reversal: CS(rev) != -CS(W)": rev_bad,
           "reversal: CS(rev) != CS(swap W)": swap_bad, "errors": errors,
           "K1 reproduced: threads with |CS| > 1e-6": nonzero,
           "holds": bool(len(threads) == 745 and not iso_fail and not rev_bad and not swap_bad and not errors
                         and nonzero == 690)}
    reads = {"swap-symmetric threads": len(symm), "threads with CS = pi^2/2": half,
             "U1 wall-clock (s)": round(time.time() - t0, 1)}
    return out, reads


x, y = sp.symbols("x y", real=True)
R2 = x ** 2 + y ** 2
Lf = -sp.log(R2)                                # L = -log|z|^2 on the punctured unit disc
Z = x + sp.I * y
E12 = sp.Matrix([[0, 1], [0, 0]])
E21 = sp.Matrix([[0, 0], [1, 0]])


def quarter_laplacian(f):                       # d_z d_zbar f
    return (sp.diff(f, x, 2) + sp.diff(f, y, 2)) / 4


def hitchin(hd, Theta):
    """F_h + [theta, theta*_h], coefficient of dz ^ dzbar, for diagonal h = diag(hd) and theta = Theta dz.
    F_h = dbar(h^-1 d h) = -d_z d_zbar log h_i dz ^ dzbar; theta*_h = h^-1 conj(Theta)^T h dzbar."""
    H = sp.diag(*hd)
    Ts = H.inv() * Theta.conjugate().T * H
    F = sp.diag(*[-quarter_laplacian(sp.log(h)) for h in hd])
    return (F + Theta * Ts - Ts * Theta).applyfunc(sp.simplify)


def zero(e):
    return sp.simplify(e) == 0 or sp.simplify(sp.expand(e.rewrite(sp.exp))) == 0


def u2():
    s, a, L0, mu = sp.symbols("s a L0 mu", positive=True)
    grad2 = sp.simplify(sp.diff(Lf, x) ** 2 + sp.diff(Lf, y) ** 2)
    ingredients = {"Laplacian of L = 0": zero(sp.diff(Lf, x, 2) + sp.diff(Lf, y, 2)),
                   "|grad L|^2 = 4/|z|^2": zero(grad2 - 4 / R2)}
    chain = {}
    for name, f in {"L^3": lambda t: t ** 3, "exp(L/3)": lambda t: sp.exp(t / 3), "sin L": sp.sin}.items():
        f2 = sp.diff(f(s), s, 2).subs(s, Lf)
        chain[name] = zero(quarter_laplacian(f(Lf)) - f2 / R2)
    h1, h2 = sp.symbols("h1 h2", positive=True)
    H = sp.diag(h1, h2)
    Th = E21 / Z
    Ts = H.inv() * Th.conjugate().T * H
    br = (Th * Ts - Ts * Th).applyfunc(sp.simplify)
    bracket_ok = all(zero(br[i, j] - t) for (i, j), t in
                     {(0, 0): -h2 / (h1 * R2), (1, 1): h2 / (h1 * R2), (0, 1): 0, (1, 0): 0}.items())
    branches = {"e^u = L - L0": sp.log(s - L0), "e^u = sinh(a (L - L0)) / a": sp.log(sp.sinh(a * (s - L0)) / a),
                "e^u = sin(a (L - L0)) / a": sp.log(sp.sin(a * (s - L0)) / a)}
    ode = {k: zero(sp.diff(u, s, 2) + sp.exp(-2 * u)) for k, u in branches.items()}
    lam_z = -sp.log(mu ** 2 * R2)               # L at lambda z, |lambda| = mu
    rescale = zero(sp.expand_log(lam_z - (Lf - sp.log(mu ** 2)), force=True))
    model = hitchin([Lf, 1 / Lf], E21 / Z)
    direct = all(zero(model[i, j]) for i in range(2) for j in range(2))
    shifted = hitchin([Lf - sp.Rational(1, 5), 1 / (Lf - sp.Rational(1, 5))], E21 / Z)
    direct_shift = all(zero(shifted[i, j]) for i in range(2) for j in range(2))
    ok = (all(ingredients.values()) and all(chain.values()) and bracket_ok and all(ode.values()) and rescale
          and direct and direct_shift)
    return {"chain-rule ingredients": ingredients, "chain rule on test functions": chain,
            "the bracket for diag(h1, h2)": bracket_ok, "the three branches solve u'' + e^(-2u) = 0": ode,
            "L(lambda z) = L - log|lambda|^2": rescale, "h = diag(L, 1/L) solves, directly": direct,
            "h = diag(L - 1/5, 1/(L - 1/5)) solves, directly": direct_shift, "holds": bool(ok)}


def u3():
    c, Lp, rr = sp.symbols("c Lp rr", positive=True)                # rr = |z|^2, Lp = L > 0 on the unit disc
    g = c ** 2 / (rr * Lp ** 2)
    hf = [g ** sp.Rational(-1, 2), g ** sp.Rational(1, 2)]          # frame f = ((dz)^1/2, (dz)^-1/2)
    he = [hf[0] / sp.sqrt(rr), hf[1] * sp.sqrt(rr)]                  # e1 = z^-1/2 f1, e2 = z^1/2 f2
    frame_ok = zero(he[0] - Lp / c) and zero(he[1] - c / Lp)
    zh = sp.Symbol("zh")                                              # a square root of z
    P = sp.diag(1 / zh, zh)
    phi_e = (P.inv() * E21 * P).applyfunc(sp.simplify)                # Phi_f = E21 dz; Phi_e = P^-1 Phi_f P
    phi_ok = zero(phi_e[1, 0] - 1 / zh ** 2) and phi_e[0, 0] == 0 and phi_e[0, 1] == 0 and phi_e[1, 1] == 0
    solves = {}
    for cv in (1, 2):
        Hm = hitchin([Lf / cv, cv / Lf], E21 / Z)
        solves[f"c = {cv}"] = all(zero(Hm[i, j]) for i in range(2) for j in range(2))
    H = sp.diag(Lf, 1 / Lf)
    dzh = ((sp.diff(H, x) - sp.I * sp.diff(H, y)) / 2)
    Nmat = (Z * H.inv() * dzh + E21 - H.inv() * E12 * H).applyfunc(sp.simplify)   # A_phi = i N on |z| = r
    target = sp.Matrix([[-1 / Lf, -1 / Lf ** 2], [1, 1 / Lf]])
    n_ok = all(zero(Nmat[i, j] - target[i, j]) for i in range(2) for j in range(2))
    Ns = sp.Matrix([[-1 / Lp, -1 / Lp ** 2], [1, 1 / Lp]])
    nil = (Ns * Ns).applyfunc(sp.simplify) == sp.zeros(2, 2) and Ns != sp.zeros(2, 2)
    mono = (sp.eye(2) - 2 * sp.pi * sp.I * Ns)                        # exp(-2 pi i N) for N^2 = 0
    tr = sp.simplify(mono.trace())
    ok = frame_ok and phi_ok and solves["c = 1"] and not solves["c = 2"] and n_ok and nil and tr == 2
    reads = {f"N at L = {v}": [[str(e) for e in row] for row in Ns.subs(Lp, v).tolist()] for v in (1, 2, 10)}
    return {"frame change: h_e = diag(L/c, c/L)": frame_ok, "Phi in the log frame is E21 dz/z": phi_ok,
            "solves Hitchin's equation": solves, "A_phi = i N with N as predicted": n_ok,
            "N^2 = 0 and N != 0": bool(nil), "trace of exp(-2 pi i N)": str(tr),
            "trace with the log frame's -1": str(-tr), "holds": bool(ok)}, reads


def u4():
    Lp, Rr, X, Y = sp.symbols("Lp R X Y", positive=True)
    Hs = sp.diag(sp.sqrt(Lp), 1 / sp.sqrt(Lp))
    B = (Hs * E21 * Hs.inv()).applyfunc(sp.simplify)
    ev = list((B.T * B).applyfunc(sp.simplify).eigenvals().keys())
    res_norm = sp.simplify(sp.sqrt(sp.Max(*ev)))                      # operator norm of the residue in h
    dz_over_z_on_unit = Lp / (2 * Rr)                                # metric R^2 4|dz|^2/(|z|^2 L^2)
    pointwise = sp.simplify(res_norm * dz_over_z_on_unit)
    curv_metric = 4 * Rr ** 2 / (R2 * Lf ** 2)
    curvature = sp.simplify(-(sp.diff(sp.log(curv_metric), x, 2) + sp.diff(sp.log(curv_metric), y, 2))
                            / (2 * curv_metric))                     # K = -Laplacian(log rho) / (2 rho)
    z_of_w = sp.exp(2 * sp.pi * sp.I * (X + sp.I * Y))
    L_w = sp.simplify(-sp.log(sp.simplify(sp.Abs(z_of_w) ** 2)))
    metric_match = zero(4 * (2 * sp.pi) ** 2 / (4 * sp.pi * Y) ** 2 - 1 / Y ** 2)   # 4|dz|^2/(|z|^2 L^2) = |dw|^2/Y^2
    length = sp.integrate(1 / Y, (X, 0, 1))
    d = sp.Symbol("d", positive=True)
    ok = (zero(res_norm - 1 / Lp) and zero(pointwise - 1 / (2 * Rr)) and zero(curvature + 1 / Rr ** 2)
          and zero(L_w - 4 * sp.pi * Y) and metric_match and zero(length - 1 / Y)
          and zero((1 / (4 * sp.pi * Y)) - length / (4 * sp.pi))
          and zero(sp.integrate(1 / Y, (Y, 1, sp.exp(d))) - d))
    return {"residue's norm in h": str(res_norm), "pointwise norm on unit vectors": str(pointwise),
            "at R = 1": str(pointwise.subs(Rr, 1)), "at R = 1/2": str(pointwise.subs(Rr, sp.Rational(1, 2))),
            "curvature of R^2 4|dz|^2/(|z|^2 L^2)": str(curvature), "L in the canonical coordinate": str(L_w),
            "the cusp metric is |dw|^2/Y^2": metric_match, "horocycle length": str(length),
            "holds": bool(ok)}


def main():
    out = {"status": "W75: chat1's scale check on this seat's instruments (the rule W75_RULE.md first; one run)",
           "snappy": snappy.__version__, "sympy": sp.__version__}
    out["U2"] = u2()
    out["U3"], r3 = u3()
    out["U4"] = u4()
    out["U1"], r1 = u1()
    out["read-outs"] = {**r1, **r3}
    out["cells"] = {k: out[k]["holds"] for k in ("U1", "U2", "U3", "U4")}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
