"""B108 -- does the opposition involution theta=-w0 PREDICT the Dehn-filling scalars c?

The top-priority computation (CC-web "Final Computation Arc", Task 1 / speculation S012): the per-eigenvector
degree=rank scalar c (L_i = c * M_i^k on the Dehn-filling reps, B106 D4) takes the values
    c = 1 (SL(3) W1), 1 (SL(3) W2), -1 (SL(4) principal), i (SL(4) secondary).
If the opposition involution theta=-w0 -- the engine of the tower's Dickson-parity decomposition (B62/B64) --
predicted these c, it would tie the Dehn-filling sector to the tower structure and feed the rho_n catalog proof.

This probe runs the explicit-matrix / contragredient route (the naive weight-space route is closed, S012 notes)
and applies the HINGE TEST: theta must predict ALL FOUR c, not just some.

RESULT (a clean structural NEGATIVE with a precise obstruction):
  1a/1b  theta is a genuine TOWER symmetry: the exchange/contragredient involution P (P^2 = I) COMMUTES with the
         trivial-point Jacobian J(m) (symbolic, SL(3)); it organizes the Dickson parity sectors (B62 height-2
         split (1,0),(1,1),(2,1) at n=3,4,5). So on the tower side, theta is exactly the right structure.
  1c     At the Dehn-filling reps, theta acts as the CONTRAGREDIENT (A,B) -> (A^-T, B^-T), under which the
         relation L = c*M^k maps to L^-1 = c'*M^-k, i.e. c -> c^{-1} (verified numerically, all 4 components).
  1d     HINGE: theta FIXES c iff c^2 = 1. It fixes c=1 (W1,W2) and c=-1 (principal) -- but it sends the
         secondary i -> -i. theta=-w0 is an INVOLUTION (order 2); its eigenvalues are +-1 (orders 1,2); the
         secondary's c=i has multiplicative ORDER 4. An order-2 symmetry cannot single out an order-4 scalar --
         it sees the Z/4 {1,i,-1,-i} only as the Z/2 flip i<->-i. So the hinge FAILS on the secondary.

VERDICT: theta=-w0 does NOT predict c (the hinge is not met). It accounts for the order-<=2 components and
matches c=(-1)^{n-1} for the principal (B83), but the order-4 secondary c=i lies beyond an involution's reach.
The order-4 scalar must come from a Z/4 source -- the natural candidate is the forced cusp spectrum {1,i,-i}
(B95, n=3, the order-4 element a=i), NOT the opposition involution. degree=rank's c therefore stays OPEN; this
result tells the rho_n proof exactly what is missing (an order-4 ingredient theta does not carry).

Standalone trace-map / Lie theory; NO physics; no CLAIMS.md promotion; proven core P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import numpy as np
import sympy as sp
from numpy.linalg import inv

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod          # @dataclass in some probes needs the module registered
    spec.loader.exec_module(mod)
    return mod


_B54 = _load("b108_b54", "frontier/B54_general_c_exchange_structure/probe.py")
_B62 = _load("b108_b62", "frontier/B62_opposition_involution/probe.py")
_B103 = _load("b108_b103", "frontier/B103_tower_equivariance/probe.py")
_B106 = _load("b108_b106", "frontier/B106_dehn_filling_anatomy/probe.py")
_DF = _load("b108_df", "frontier/B73_sl4_apoly/dehn_filling.py")
_PER = _load("b108_per", "frontier/B71_sl3_apoly/peripheral.py")


# --------------------------------------------------------------------------- #
# 1a / 1b -- theta=-w0 is the contragredient involution and a TOWER symmetry
# --------------------------------------------------------------------------- #
def theta_is_tower_symmetry():
    """SL(3): the exchange/contragredient involution P satisfies P^2=I and [P, J(m)]=0 (symbolic) -- so theta is a
    symmetry of the trivial-point Jacobian (the tower). Reports the B62 height-2 split it induces."""
    P = _B54.exchange_involution()
    involution = (P * P == sp.eye(8))
    J = _B103._Jm_n3_exact()
    commutes = sp.simplify(P * J - J * P) == sp.zeros(8)
    splits = {n: _B62.height2_sectors(n) for n in (3, 4, 5)}   # (#char(M^2), #char(-M^2)) at height 2
    return {"P_is_involution": bool(involution), "commutes_with_Jm": bool(commutes),
            "height2_split_n345": splits}


# --------------------------------------------------------------------------- #
# 1c -- theta at the Dehn-filling reps: the contragredient sends c -> c^{-1}
# --------------------------------------------------------------------------- #
def _c_from(mu, comm, k):
    mu, comm = np.array(mu, complex), np.array(comm, complex)
    w, V = np.linalg.eig(mu)
    L = np.diag(inv(V) @ comm @ V)
    return complex(np.mean(L / (w ** k)))


def _realize(component, seed):
    """Return (A, B, mu, k) for a Dehn-filling component."""
    if component in ("W1", "W2"):
        gen = {"W1": _PER.W1, "W2": _PER.W2}[component]
        k = 3 if component == "W1" else -3
        # vary the (p,q) point a touch by seed for robustness
        p, q = 2.3 + 0.13 * seed, 3.1 + 0.17 * seed
        A, B = _PER.realize(gen(p, q))
        mu, _ = _PER.meridian(A, B)
        return A, B, mu, k
    k = _B106.SL4_EXPONENT[component]
    A, B, t = _DF.realize_bundle_rep(np.array(_B106.SL4_SPECTRA[component]), seed=seed)
    return A, B, inv(A) @ t, k


def contragredient_c(component, seed=0):
    """c on the rep vs c on the contragredient (dual) rep (A,B)->(A^-T,B^-T). theta sends c -> c^{-1}."""
    A, B, mu, k = _realize(component, seed)
    comm = A @ B @ inv(A) @ inv(B)
    c = _c_from(mu, comm, k)
    # the contragredient / dual representation
    Ad, Bd = inv(A).T, inv(B).T
    if component in ("W1", "W2"):
        mud, _ = _PER.meridian(Ad, Bd)
    else:
        # dual monodromy t* = t^-T solves the dual figure-eight relation; mu* = (A*)^-1 t*
        _, _, t = _DF.realize_bundle_rep(np.array(_B106.SL4_SPECTRA[component]), seed=seed)
        mud = inv(Ad) @ inv(t).T
    commd = Ad @ Bd @ inv(Ad) @ inv(Bd)
    cd = _c_from(mud, commd, k)
    return {"c": c, "c_dual": cd, "c_times_cdual": complex(c * cd)}


# --------------------------------------------------------------------------- #
# 1d -- the HINGE TEST: theta fixes c iff c^2 = 1; order-4 c=i is unreachable
# --------------------------------------------------------------------------- #
def _order(c, qmax=12, tol=1e-6):
    for q in range(1, qmax + 1):
        if abs(c ** q - 1) < tol:
            return q
    return None


def hinge_test():
    """For all four Dehn-filling components at the B106-CANONICAL realization (seed=0): c, its multiplicative
    ORDER, and whether theta fixes it (theta-fixed iff c_dual == c iff c^2=1). theta (an involution, order 2)
    predicts c iff order(c) <= 2. The order-4 secondary (c=i) fails the hinge.

    Robustness note (honest): |c|=1 and c->c^{-1} under the contragredient hold for EVERY realization (checked
    by contragredient_c across seeds in the test); the canonical c-VALUES are the B106/D4 seed=0 reference --
    W1 c=1, W2 c=1, principal c=-1, secondary c=i. (The secondary realization is branch-sensitive: some seeds
    land on a degenerate c=-1 rep; the genuine secondary, B106 seed=0, carries the order-4 c=i, and that is the
    component that fails the hinge.)"""
    rows = {}
    for comp in ("W1", "W2", "principal", "secondary"):
        r = contragredient_c(comp, 0)
        c = r["c"]
        rows[comp] = {
            "c_seed0": complex(c),
            "is_root_of_unity": abs(abs(c) - 1) < 1e-3,
            "order": _order(c),
            "c2_is_1": abs(c ** 2 - 1) < 1e-3,
            "theta_fixes": abs(r["c_dual"] - c) < 1e-3,        # theta-fixed iff c_dual == c
        }
    theta_order = 2
    predicted = {k: (v["order"] is not None and v["order"] <= theta_order) for k, v in rows.items()}
    all_four = all(predicted.values())
    return {"rows": rows, "theta_order": theta_order, "predicted_by_theta": predicted,
            "hinge_all_four_passed": all_four,
            "obstruction": None if all_four else
            "theta=-w0 is order 2; the secondary c=i is order 4; an involution cannot single out an order-4 "
            "scalar (it sends i -> -i). The order-4 ingredient must come from a Z/4 source (candidate: the "
            "forced cusp spectrum {1,i,-i}, B95), not the opposition involution."}


def main():
    print("=" * 78)
    print("B108 -- does theta=-w0 PREDICT the Dehn-filling c?  (Task 1; the hinge: ALL FOUR or it fails)")
    print("=" * 78)
    sym = theta_is_tower_symmetry()
    print("\n[1a/1b] theta as a tower symmetry (SL(3)):")
    print(f"    P^2 = I (involution)      : {sym['P_is_involution']}")
    print(f"    [P, J(m)] = 0 (symbolic)  : {sym['commutes_with_Jm']}   <- theta organizes the tower")
    print(f"    B62 height-2 split n=3,4,5: {sym['height2_split_n345']}")
    print("\n[1c] theta at the Dehn-filling reps = contragredient, c -> c^{-1}:")
    for comp in ("W1", "W2", "principal", "secondary"):
        r = contragredient_c(comp, 0)
        print(f"    {comp:>10}: c={r['c']:+.3f}  c_dual={r['c_dual']:+.3f}  c*c_dual={r['c_times_cdual']:+.3f}")
    print("\n[1d] THE HINGE TEST:")
    h = hinge_test()
    for comp, v in h["rows"].items():
        tag = "predicted" if h["predicted_by_theta"][comp] else "NOT predicted"
        print(f"    {comp:>10}: c={v['c_seed0']:+.3f}  order={v['order']}  theta-fixed={v['theta_fixes']}"
              f"  -> {tag}")
    print(f"\n    theta order = {h['theta_order']};  HINGE (all four) passed: {h['hinge_all_four_passed']}")
    if not h["hinge_all_four_passed"]:
        print(f"    OBSTRUCTION: {h['obstruction']}")
    print("\nVERDICT: NEGATIVE on the hinge -- theta organizes the tower and the order-<=2 c, but the order-4")
    print("secondary c=i is beyond an involution. degree=rank's c stays OPEN; the missing piece is order-4.")


if __name__ == "__main__":
    main()
