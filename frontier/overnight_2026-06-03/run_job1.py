"""Overnight Job 1 -- Jacobian-level time-reversal (symbolic).

For the proven symbolic SL(3) Jacobian J(m) (B64.sl3_jacobian) and the SL(4) J(m)
(B65.symbolic_jacobian): charpoly(J) vs charpoly(J^-1), factored in the Dickson basis,
verifying charpoly(J^-1) = charpoly(J) under {even-k fixed, odd-k char(+M^k)<->char(-M^k)}.
Exploratory; writes time_reversal.json only. No commit.
"""

import importlib.util
import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "time_reversal.json"
m, t = sp.symbols("m t")


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def lucas(k):
    M = sp.Matrix([[m, 1], [1, 0]])
    Mk = M ** k if k >= 0 else M.inv() ** (-k)
    return sp.expand(sp.trace(Mk))


def catalog():
    ents = []
    for k in range(-6, 7):
        if k == 0:
            continue
        Lk = lucas(k)
        c = (-1) ** (k % 2)            # (-1)^k
        ents.append((f"char(M^{k})", sp.expand(t ** 2 - Lk * t + c)))
        ents.append((f"char(-M^{k})", sp.expand(t ** 2 + Lk * t + c)))
    ents.append(("(t-1)", sp.expand(t - 1)))
    ents.append(("(t+1)", sp.expand(t + 1)))
    return ents


def poly_key(f):
    return tuple(str(sp.expand(c)) for c in sp.Poly(sp.expand(f), t).all_coeffs())


def monic_t(f):
    P = sp.Poly(sp.expand(f), t)
    return sp.expand(f / P.LC())


def match_label(f, cat):
    fk = poly_key(f)
    for lab, g in cat:
        if poly_key(g) == fk:
            return lab
    return f"UNMATCHED[{sp.expand(f)}]"


def labeled_factors(cp, cat):
    cp = sp.expand(cp)
    _coeff, facs = sp.factor_list(cp)
    labels, keys = [], []
    for f, mult in facs:
        fm = monic_t(f)
        for _ in range(mult):
            labels.append(match_label(fm, cat))
            keys.append(poly_key(fm))
    return labels, sorted(keys)


def invert_factor(f):
    """monic-in-t inversion image t^deg f(1/t)/f(0) (eigenvalues -> reciprocals)."""
    n = sp.Poly(sp.expand(f), t).degree()
    g = sp.expand(t ** n * f.subs(t, 1 / t) / f.subs(t, 0))
    return monic_t(g)


def reversal_charpoly(cp, n):
    """charpoly(J^-1)(t) = t^n charpoly(J)(1/t) / charpoly(J)(0)."""
    return sp.expand(t ** n * cp.subs(t, 1 / t) / cp.subs(t, 0))


def analyze(name, J, cat, partial):
    n = J.shape[0]
    cp = sp.expand(J.charpoly(t).as_expr())
    cp_inv = reversal_charpoly(cp, n)
    lab, _keys = labeled_factors(cp, cat)
    lab_inv, keys_inv = labeled_factors(cp_inv, cat)
    # predicted inverse-factor multiset = invert each factor of charpoly(J)
    _coeff, facs = sp.factor_list(sp.expand(cp))
    pred_keys = []
    for f, mult in facs:
        fm = monic_t(f)
        for _ in range(mult):
            pred_keys.append(poly_key(invert_factor(fm)))
    passed = sorted(pred_keys) == keys_inv
    partial[name] = {
        "dim": n,
        "charpoly_J_factors": sorted(lab),
        "charpoly_Jinv_factors": sorted(lab_inv),
        "time_reversal_PASS": bool(passed),
        "rule": "even-k fixed, odd-k char(+M^k)<->char(-M^k)",
    }
    OUT.write_text(json.dumps(partial, indent=2))
    return passed


def main():
    b64 = load("b64_probe", "frontier/B64_parity_mechanism/probe.py")
    b65 = load("b65_probe", "frontier/B65_sl4_symbolic_jacobian/probe.py")
    cat = catalog()
    partial = {"job": "time_reversal", "started": time.strftime("%F %T"), "status": "running"}
    OUT.write_text(json.dumps(partial, indent=2))

    # SL(3) -- checkpoint before SL(4)
    J3 = b64.sl3_jacobian()
    analyze("SL3", J3, cat, partial)
    cp3 = sp.expand(J3.charpoly(t).as_expr())
    partial["SL3"]["reversal_equals_actual_inverse"] = bool(
        sp.expand(J3.inv().charpoly(t).as_expr() - reversal_charpoly(cp3, 8)) == 0)
    OUT.write_text(json.dumps(partial, indent=2))

    # SL(4)
    J4 = b65.symbolic_jacobian()
    analyze("SL4", J4, cat, partial)

    partial["status"] = "ok"
    partial["finished"] = time.strftime("%F %T")
    OUT.write_text(json.dumps(partial, indent=2))
    print("JOB1 done:", partial.get("SL3", {}).get("time_reversal_PASS"),
          partial.get("SL4", {}).get("time_reversal_PASS"))


if __name__ == "__main__":
    main()
