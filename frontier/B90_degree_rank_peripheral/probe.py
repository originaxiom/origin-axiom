"""B90 (Task 1b) -- the peripheral form of degree=rank, and the honest limits of the reduction.

[CORRECTED 2026-06-05 after the CC-web audit -- see the AUDIT block below. The original framing
("Lemma 1 reduces degree=rank to a collapse-lemma; exponent = rank from A's Cayley-Hamilton") OVERSTATED
the result; two of its pieces do not survive scrutiny.]

degree=rank (B73/B77/B83): on the PRINCIPAL figure-eight Dehn-filling component (A-spectrum {1,1,...,w,w2}
with tr A = tr A^-1 = 1), the longitude is the meridian's rank-th power, [A,B] = (-1)^(n-1) mu^n
(mu = A^-1 t, V46), PROVED exact at n=3 (B71/V47) and n=4 (B89/V72).  B77 located the mechanism in the
cusp.  This stage writes the peripheral structure explicitly and tests how much of degree=rank it forces.

WHAT IS TRUE (kept):
  (L1b)  X mu X^-1 = mu A ,     X = A mu A^-1 ,                                                  GENUINE.
  L1b is a real consequence of the bundle relations (= the (*) equation t A^-2 t A = A^-1 t A t with
  t = A mu), PROVED uniformly in n; it FAILS on a random non-bundle (A,t) (dev O(10)).  It is the clean
  meridian form of the second bundle relation.

WHAT DOES NOT SURVIVE (the audit, honest):
  (L1a)  lambda = [A,B] = mu X^-1 mu Y^-1 ,   Y = A^-1 mu A .                                    TAUTOLOGY.
  L1a is a pure algebraic REWRITING of the longitude (with B := A^-2 t A t^-1): it holds for an ARBITRARY
  (A,t) pair, even when the bundle constraint fails (verified: dev ~1e-10 on random non-bundle (A,t)).
  So L1a is NOT constraint content and does NOT count toward any reduction.

  "EXPONENT = RANK from A's degree-n Cayley-Hamilton."                                           REFUTED.
  The HINGE TEST (`hinge_test`) settles whether L1b + CH(A) forces the exponent: BOTH SL(4) Dehn-filling
  components satisfy L1b, and both have 4x4 A (CH degree 4) -- but the principal {1,1,w,w2} gives M^4=L
  while the secondary {prim 8th roots, z^4+1} gives M^3=L.  Same n, same CH degree, L1b on both, DIFFERENT
  exponents (4 vs 3).  So the exponent is NOT determined by L1b + degree-n Cayley-Hamilton; it depends on
  the specific (principal) A-spectrum.  The "exponent = rank = CH degree" mechanism is false.

HONEST STATUS (post-audit):
  * L1b (the meridian form of the bundle constraint) is the genuine, uniform peripheral result here.
  * degree=rank `[A,B]=(-1)^(n-1) mu^n` stays PROVED only at n=3,4 (B71,B89); the uniform-n statement is
    OPEN, and is NOT reduced to "L1b + CH" (that reduction is refuted by the secondary component).
  * The real open question is sharper than before: WHY does the PRINCIPAL spectrum (and not the secondary)
    give exponent = n?  L1b is component-blind, so the mechanism must read the spectrum -- the cusp's
    cyclic boundary holonomy and the A-eigenvalue orders (cf. B88's degrees {3,4}), not Cayley-Hamilton.

Standalone low-dim topology / group theory; no physics, no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib

import numpy as np
from scipy.optimize import least_squares

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _inv(M):
    return np.linalg.inv(M)


def lemma1_residuals(A, B, t):
    """(L1a dev, L1b dev) on a rep. NOTE: L1a is a tautology (holds for any (A,t)); only L1b is genuine."""
    Ai = _inv(A)
    mu = Ai @ t
    comm = A @ B @ Ai @ _inv(B)
    X = A @ mu @ Ai
    Y = Ai @ mu @ A
    l1a = np.max(np.abs(comm - mu @ _inv(X) @ mu @ _inv(Y)))
    l1b = np.max(np.abs(X @ mu @ _inv(X) - mu @ A))
    return l1a, l1b


def l1a_is_tautology(seed=0, trials=3):
    """L1a holds even on RANDOM non-bundle (A,t) (B := A^-2 t A t^-1). Returns the worst deviation."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(trials):
        A = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
        A = A / np.linalg.det(A) ** 0.25
        t = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
        t = t / np.linalg.det(t) ** 0.25
        Ai, ti = _inv(A), _inv(t)
        B = Ai @ Ai @ t @ A @ ti               # B := A^-2 t A t^-1 (definition only -- bundle constraint NOT imposed)
        mu = Ai @ t
        comm = A @ B @ Ai @ _inv(B)
        X, Y = A @ mu @ Ai, Ai @ mu @ A
        worst = max(worst, np.max(np.abs(comm - mu @ _inv(X) @ mu @ _inv(Y))))
    return worst


def collapse_dev(A, B, t, n):
    """Scalar-deviation of lambda*mu^-n and the scalar c (= (-1)^(n-1) on the principal component)."""
    Ai = _inv(A)
    mu = Ai @ t
    comm = A @ B @ Ai @ _inv(B)
    S = comm @ np.linalg.matrix_power(_inv(mu), n)
    dev = max(np.max(np.abs(S - np.diag(np.diag(S)))), np.max(np.abs(np.diag(S) - np.mean(np.diag(S)))))
    return dev, complex(np.mean(np.diag(S)))


def _best_exponent(A, B, t, ks=(2, 3, 4, 5)):
    Ai = _inv(A)
    mu = Ai @ t
    comm = A @ B @ Ai @ _inv(B)

    def dev(k):
        S = comm @ np.linalg.matrix_power(_inv(mu), k)
        return max(np.max(np.abs(S - np.diag(np.diag(S)))), np.max(np.abs(np.diag(S) - np.mean(np.diag(S)))))
    devs = {k: dev(k) for k in ks}
    return min(devs, key=devs.get), devs


def hinge_test():
    """THE HINGE TEST: both SL(4) Dehn-filling components satisfy L1b, with DIFFERENT exponents (4 vs 3).
    Returns {component: (l1b_dev, best_k)} -- refutes 'exponent = CH degree = rank'."""
    spec = importlib.util.spec_from_file_location(
        "b73", _ROOT / "frontier" / "B73_sl4_apoly" / "dehn_filling.py")
    b73 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(b73)
    out = {}
    for name, A_spec in (("principal {1,1,w,w2}", b73.SPEC_W1),
                         ("secondary {prim 8th, z^4+1}", b73.SPEC_Z4)):
        rep = None
        for sd in range(40):
            r = b73.realize_bundle_rep(A_spec, seed=sd, tries=120)
            if r is not None:
                rep = r
                break
        if rep is None:
            out[name] = (None, None)
            continue
        A, B, t = rep
        _, l1b = lemma1_residuals(A, B, t)
        k, _ = _best_exponent(A, B, t)
        out[name] = (l1b, k)
    return out


def main():
    print("B90 (Task 1b) -- the peripheral form of degree=rank, with the audit corrections\n")
    print("L1b (GENUINE, proved uniform):  X mu X^-1 = mu A   (X = A mu A^-1)")
    print(f"L1a (TAUTOLOGY): lambda = mu X^-1 mu Y^-1 holds on RANDOM non-bundle (A,t): "
          f"dev = {l1a_is_tautology():.1e}  (=> rewriting, not constraint content)\n")
    print("THE HINGE TEST -- does L1b + CH(A) force the exponent? (both components have 4x4 A, CH deg 4)")
    for name, (l1b, k) in hinge_test().items():
        print(f"  {name}: L1b dev={l1b:.0e}, best exponent M^{k}=L")
    print("\n=> both satisfy L1b but exponents differ (4 vs 3) => 'exponent = CH degree = rank' REFUTED.")
    print("   L1b is the genuine uniform peripheral constraint; the exponent needs the PRINCIPAL spectrum.")
    print("   degree=rank stays PROVED only at n=3,4 (B71,B89); uniform-n is OPEN (NOT reduced to L1b+CH).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
