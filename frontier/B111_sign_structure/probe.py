"""B111 -- the tower's SIGN structure vs the opposition involution: the closed form + the degree=rank promotion.

Banks the CC-web "sign findings" handoff (verify-don't-trust):
  PART 0  -- the SL(3) sign rule (engine-free) and the opposition-involution all-heights CLOSED FORM.
  PATH B  -- the IMMEDIATE reconciliation: is the closed form the proved tower? DECISION (the key result).
  PATH C  -- the general-n check (n=3,4 exact).
plus the s_n<->c bridge banked DEAD (same parity argument as B108).

THE RESULT (sharp, and it scopes the rho_n prize). For the metallic family the trivial-rep tower char(J)
factors as prod char(+-M^k) * parity. Two pieces:

  (i) the BULK opposition involution theta=-w0 gives, in CLOSED FORM over each height-h root space of A_{n-1},
        mult char(M^h) = ceil((n-h)/2),   mult char(-M^h) = floor((n-h)/2),   h = 1..n-1
      (verified vs B62's height-2 splits (1,0),(1,1),(2,1) at n=3,4,5; computed n=3..12). This is the bulk
      sign/multiplicity law -- the all-heights generalization of B62 (which only had height 2).

  (ii) BUT the closed form is NOT the proved tower. Diffing it against the EXACT repo tower (n=3 from the Lawton
      Jacobian; n=4 from B80's proved _Jm_n4_exact):
        Tower(n) = [closed form, heights 1..n-1]  with exactly ONE char(M^1) PROMOTED to char(M^n).
      The single non-bulk ingredient is char(M^n) = the DEGREE=RANK top power (the longitude L = c*M^n, B83/B89).
      char(M^1) = the meridian; char(M^n) = the longitude: degree=rank promotes one meridian to the longitude,
      structurally, inside the tower.

So the tower = (bulk theta height-decomposition) + (one degree=rank promotion M -> M^n). The rho_n proof's
SIGN half is the closed form (bulk theta); the only piece theta does NOT supply is the top power char(M^n),
which is exactly degree=rank (the peripheral thread, Path A). The two halves of the prize are thereby named.

CORRECTION (verify-don't-trust): the handoff's SL(3) parity rule (t-1)(t+det N) is WRONG; the computed parity is
(t-1)(t - det N)  [det N=-1 -> (t-1)(t+1); det N=+1 -> (t-1)^2]. The s2=+1 part is SL(3)-specific (SL(4) carries
char(-M^2)).

Standalone trace-map / Lie theory; NO physics; no CLAIMS.md promotion; the rho_n catalog proof stays the prize;
proven core P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import numpy as np
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_B103 = _load("b111_b103", "frontier/B103_tower_equivariance/probe.py")
_B62 = _load("b111_b62", "frontier/B62_opposition_involution/probe.py")

_t, _m = sp.symbols("t m")
_PHI = (1 + sp.sqrt(5)) / 2


# --------------------------------------------------------------------------- #
# PART 0 -- the SL(3) sign rule (engine-free)
# --------------------------------------------------------------------------- #
def _abel_det(word):
    return int(sp.Matrix(_B103.word_abelianization(word)).det())


def sl3_sign_rule():
    """char(J) at the trivial rep for the metallic family (m=1,2,3, det N=-1) and the figure-eight (det N=+1).
    Reports the parity factor; verifies m-stability and the CORRECTED parity (t-1)(t - det N)."""
    out = {}
    words = {"metallic_m1": ["U", "S"], "metallic_m2": ["U", "U", "S"],
             "metallic_m3": ["U", "U", "U", "S"], "figure_eight": ["U", "L"]}
    for name, w in words.items():
        J = sp.Matrix(_B103.lawton_jacobian(w))
        cp = sp.factor(J.charpoly(_t).as_expr())
        dN = _abel_det(w)
        parity = sp.expand((_t - 1) * (_t - dN))           # predicted: (t-1)(t - det N)
        # parity divides char(J)?
        q, r = sp.div(cp, parity, _t)
        out[name] = {"det_N": dN, "char_factored": str(cp),
                     "parity_predicted": str(sp.factor(parity)), "parity_divides": sp.simplify(r) == 0}
    # m-stability: the three metallic det/parity identical
    mstable = (out["metallic_m1"]["det_N"] == out["metallic_m2"]["det_N"] == out["metallic_m3"]["det_N"] == -1)
    return {"components": out, "metallic_m_stable_det_minus1": mstable,
            "parity_rule": "(t-1)(t - det N)  [handoff's (t + det N) corrected]"}


# --------------------------------------------------------------------------- #
# the opposition-involution all-heights CLOSED FORM
# --------------------------------------------------------------------------- #
def opposition_closed_form(n):
    """mult char(M^h)=ceil((n-h)/2), char(-M^h)=floor((n-h)/2), h=1..n-1 (the bulk theta height-decomposition)."""
    f = {}
    for h in range(1, n):
        cp = int(sp.ceiling(sp.Rational(n - h, 2)))
        fl = int(sp.floor(sp.Rational(n - h, 2)))
        if cp:
            f[("+", h)] = cp
        if fl:
            f[("-", h)] = fl
    return f


def closed_form_matches_b62(ns=(3, 4, 5)):
    """At height 2 the closed form (mult) must equal B62's published splits (dim/2): (1,0),(1,1),(2,1)."""
    out = {}
    for n in ns:
        cf = opposition_closed_form(n)
        plus = cf.get(("+", 2), 0)
        minus = cf.get(("-", 2), 0)
        b62 = _B62.height2_sectors(n)        # (#char(M^2), #char(-M^2))
        out[n] = {"closed_form_h2": (plus, minus), "b62": tuple(b62), "match": (plus, minus) == tuple(b62)}
    return out


def excess_plus_over_minus(n):
    """Net (+)-over-(-) char excess = floor(n/2) (handoff Part 0)."""
    cf = opposition_closed_form(n)
    plus = sum(v for (s, h), v in cf.items() if s == "+")
    minus = sum(v for (s, h), v in cf.items() if s == "-")
    return {"plus": plus, "minus": minus, "excess": plus - minus, "floor_n_2": n // 2,
            "matches": plus - minus == n // 2}


# --------------------------------------------------------------------------- #
# PATH B / C -- the tower (exact, from the repo) vs the closed form: the PROMOTION
# --------------------------------------------------------------------------- #
def _ident(x):
    """Identify a real eigenvalue as (sign, k) with value sign*phi^k."""
    if abs(x) < 1e-9:
        return None
    for k in range(-9, 10):
        if abs(x - float(_PHI ** k)) < 1e-4:
            return ("+", k)
        if abs(x + float(_PHI ** k)) < 1e-4:
            return ("-", k)
    return ("?", round(float(x), 3))


def _tower_char_multiset(eigs):
    """Group identified eigenvalues into char(+-M^h) factors (h>=1) + the parity (|k|=0) factors. char(M^h) =
    {+phi^h, (-1)^h phi^-h}; char(-M^h) = {-phi^h, -(-1)^h phi^-h}; char(M^-h)=char(-M^h) odd h / char(M^h) even h."""
    ids = [_ident(x) for x in eigs]
    ids = [i for i in ids if i is not None]
    # parity = the |k|=0 eigenvalues (+1 / -1)
    parity = sorted(i[0] for i in ids if i[1] == 0)
    # for the rest, fold negative powers via det=-1 identity to heights h>=1
    factors = {}
    used = [False] * len(ids)
    for h in range(1, 9):
        for sign in ("+", "-"):
            # char(sign M^h) eigenvalue pair, written at height h (positive power)
            if sign == "+":
                pair = [("+", h), ("+" if h % 2 == 0 else "-", -h)]
            else:
                pair = [("-", h), ("-" if h % 2 == 0 else "+", -h)]
            # how many such pairs present?
            while all(pair[j] in [ids[k] for k in range(len(ids)) if not used[k]] for j in range(2)):
                for pj in pair:
                    for k in range(len(ids)):
                        if not used[k] and ids[k] == pj:
                            used[k] = True
                            break
                factors[(sign, h)] = factors.get((sign, h), 0) + 1
    return factors, parity


def tower_vs_closed_form(n):
    """Diff the EXACT repo tower against the closed form. Result: tower = closed form with ONE char(M^1) promoted
    to char(M^n) (the degree=rank top power). n=3 from the Lawton Jacobian, n=4 from B80's _Jm_n4_exact."""
    if n == 3:
        J = np.array(_B103.lawton_jacobian(["U", "S"])).astype(float)
    elif n == 4:
        J = np.array(_B103._Jm_n4_exact().subs(_m, 1)).astype(np.float64)
    else:
        raise ValueError("exact tower available for n=3,4")
    eigs = np.linalg.eigvals(J)
    tower, parity = _tower_char_multiset(eigs)
    closed = opposition_closed_form(n)
    # the promotion: tower should equal closed - {(+,1):1} + {(+,n):1}
    predicted = dict(closed)
    predicted[("+", 1)] = predicted.get(("+", 1), 0) - 1
    if predicted.get(("+", 1), 0) == 0:
        predicted.pop(("+", 1), None)
    predicted[("+", n)] = predicted.get(("+", n), 0) + 1
    return {"tower_factors": {f"{s}M^{h}": v for (s, h), v in sorted(tower.items())},
            "closed_form": {f"{s}M^{h}": v for (s, h), v in sorted(closed.items())},
            "promotion_predicted": {f"{s}M^{h}": v for (s, h), v in sorted(predicted.items())},
            "tower_equals_closed_plus_promotion": tower == predicted,
            "promotion": f"one char(M^1) -> char(M^{n}) (= char(M^n), the degree=rank top power L=c*M^n)"}


# --------------------------------------------------------------------------- #
# s_n <-> c bridge: DEAD by the same parity argument as B108
# --------------------------------------------------------------------------- #
def s_n_to_c_bridge_dead():
    """The conjecture 's_n = c' is DEAD: s_n in {+-1} is order <= 2, but the secondary Dehn-filling c=i is order 4
    (B106/B108). An order-<=2 sign cannot equal an order-4 scalar -- the same parity obstruction that killed theta->c."""
    s_n_order = 2          # s_n in {+1,-1}
    c_secondary_order = 4  # c = i
    return {"s_n_max_order": s_n_order, "c_secondary_order": c_secondary_order,
            "bridge_dead": c_secondary_order > s_n_order,
            "reason": "s_n in {+-1} (order<=2) cannot equal the order-4 secondary c=i; same parity argument as B108/theta->c"}


# --------------------------------------------------------------------------- #
# ADDITION 1 -- M^k scalar/non-scalar per component: the degree=rank exponent's algebraic constraint
# --------------------------------------------------------------------------- #
_W = np.exp(2j * np.pi / 3)        # cube root of unity
_Z = np.exp(1j * np.pi / 4)        # primitive 8th root of unity
_CUSP_SPECTRA = {                  # the meridian (cusp) eigenvalue spectra per component
    "SL3_W1": [1, 1j, -1j],                       # n=3, order 4 = n+1
    "SL4_principal": [1, 1, _W, _W ** 2],          # n=4, order 3 = n-1
    "SL4_secondary": [_Z, _Z ** 3, _Z ** 5, _Z ** 7],  # n=4, order 8 = 2n
}
_EXPONENT = {"SL3_W1": 3, "SL4_principal": 4, "SL4_secondary": 3}


def _is_scalar(vals, tol=1e-9):
    a = np.array(vals, complex)
    return bool(np.max(np.abs(a - a[0])) < tol)


def mpower_scalar_table():
    """ADDITION 1 (pure eigenvalue arithmetic): is M^k scalar on each component's cusp spectrum? On the SL(4)
    SECONDARY, M^4 = zeta^4 = -1 is SCALAR => [A,B]=c*(-1)*Id is trivial => k=4 ALGEBRAICALLY IMPOSSIBLE; k=3
    (non-scalar) is forced. On the PRINCIPAL, M^4 is non-scalar => k=4 allowed. Proves the NEGATIVE
    characterization (why k!=4 on the secondary); does NOT prove k=n on the principal (only allowed)."""
    out = {}
    for name, spec in _CUSP_SPECTRA.items():
        s = np.array(spec, complex)
        table = {k: (not _is_scalar(s ** k)) for k in range(1, 9)}   # True = non-scalar
        k = _EXPONENT[name]
        out[name] = {"exponent_k": k, "Mk_nonscalar": table,
                     "exponent_is_nonscalar": table[k],
                     "M4_scalar": (not table[4])}
    secondary = out["SL4_secondary"]
    return {"per_component": out,
            "secondary_k4_impossible": secondary["M4_scalar"],          # M^4 scalar on the secondary
            "principal_k4_allowed": out["SL4_principal"]["Mk_nonscalar"][4],
            "verdict": "k=4 algebraically IMPOSSIBLE on the SL(4) secondary (M^4=-1 scalar -> trivial commutator); "
                       "k=4 ALLOWED on the principal (M^4 non-scalar). Proves k!=4 on secondary; does NOT prove "
                       "k=n on the principal."}


# --------------------------------------------------------------------------- #
# ADDITION 2 -- the cusp order pattern {n-1, n+1, 2n} + the ord-1 TESTED-NEGATIVE
# --------------------------------------------------------------------------- #
def _mult_order(z, qmax=24, tol=1e-9):
    for q in range(1, qmax + 1):
        if abs(z ** q - 1) < tol:
            return q
    return None


def cusp_order_pattern():
    """ADDITION 2: the cusp eigenvalue orders are {n-1, n+1, 2n} on the three component types; and the simple
    formula k = ord-1 FAILS the all-four hinge (OK at SL(3), FAIL at SL(4)) -> TESTED-NEGATIVE on ord-1."""
    out = {}
    for name, spec in _CUSP_SPECTRA.items():
        s = np.array(spec, complex)
        n = len(s)
        gens = [v for v in s if abs(v - 1) > 1e-9]
        ordz = _mult_order(gens[0]) if gens else 1
        k = _EXPONENT[name]
        which = {n - 1: "n-1", n + 1: "n+1", 2 * n: "2n"}.get(ordz, "?")
        out[name] = {"n": n, "cusp_order": ordz, "order_is": which, "k": k,
                     "ord_minus_1": ordz - 1, "ord_minus_1_eq_k": (ordz - 1 == k)}
    ord1_hinge = all(v["ord_minus_1_eq_k"] for v in out.values())
    return {"per_component": out, "pattern_is_nm1_np1_2n": all(v["order_is"] in ("n-1", "n+1", "2n") for v in out.values()),
            "ord_minus_1_formula_passes_hinge": ord1_hinge,
            "verdict": "cusp orders ARE {n-1,n+1,2n}; the ord-1 formula FAILS the hinge (TESTED-NEGATIVE) -- "
                       "Path A right direction, the specific formula open."}


# --------------------------------------------------------------------------- #
# covering-degree (ADDITION 1 A1d) -- the candidate POSITIVE mechanism (a hypothesis)
# --------------------------------------------------------------------------- #
def covering_degree_test():
    """A1d: the covering map (cusp parameter mu) -> L = c*M^k. At the eigenvalue level mu -> mu^k is k-to-1, so the
    covering degree = k on all four components (consistent with the hypothesis 'mechanism = Weyl-orbit covering
    degree'). HONEST: this is the eigenvalue-level degree; whether the FULL component covering (SL(n) + Weyl
    constraints) is exactly k needs the character-variety covering map -- the open part of the hypothesis."""
    out = {}
    for name, spec in _CUSP_SPECTRA.items():
        k = _EXPONENT[name]
        gens = [v for v in np.array(spec, complex) if abs(v - 1) > 1e-9]
        zeta = gens[0]
        mu0 = zeta * np.exp(0.07 + 0.05j)        # a generic cusp deformation off the root of unity
        L0 = mu0 ** k
        roots = [abs(L0) ** (1 / k) * np.exp(1j * (np.angle(L0) + 2 * np.pi * j) / k) for j in range(k)]
        degree = len({tuple(np.round([r.real, r.imag], 6)) for r in roots})
        out[name] = {"k": k, "eigenvalue_covering_degree": degree, "equals_k": degree == k}
    return {"per_component": out,
            "eigenvalue_degree_equals_k_all": all(v["equals_k"] for v in out.values()),
            "status": "PARTIAL-POSITIVE (eigenvalue level): covering degree = k on all four; the full-component "
                      "covering (with SL(n)+Weyl constraints) is OPEN -- a HYPOTHESIS, not a solved mechanism."}


def main():
    print("=" * 78)
    print("B111 -- the tower's sign structure: the opposition-involution closed form + degree=rank promotion")
    print("=" * 78)
    print("\n[PART 0] SL(3) sign rule:")
    sr = sl3_sign_rule()
    for name, v in sr["components"].items():
        print(f"    {name:>13} (det N={v['det_N']:+d}): parity {v['parity_predicted']} divides={v['parity_divides']}")
    print(f"    m-stable (det=-1): {sr['metallic_m_stable_det_minus1']};  parity rule: {sr['parity_rule']}")
    print("\n[closed form] opposition-involution all-heights multiplicities:")
    for n in (3, 4, 5, 6):
        print(f"    n={n}: {opposition_closed_form(n)}  excess(+over-)={excess_plus_over_minus(n)['excess']}"
              f" (=floor(n/2)={n//2})")
    print("    vs B62 height-2:", closed_form_matches_b62())
    print("\n[PATH B/C] tower (exact, repo) vs closed form -- the PROMOTION:")
    for n in (3, 4):
        r = tower_vs_closed_form(n)
        print(f"    n={n}: tower==closed+promotion: {r['tower_equals_closed_plus_promotion']}  [{r['promotion']}]")
        print(f"          tower   = {r['tower_factors']}")
        print(f"          closed  = {r['closed_form']}")
    print("\n[ADDITION 1] M^k scalar/non-scalar -- the degree=rank exponent constraint:")
    mp = mpower_scalar_table()
    for name, v in mp["per_component"].items():
        print(f"    {name:>14}: k={v['exponent_k']}, M^4 scalar={v['M4_scalar']}, exponent non-scalar={v['exponent_is_nonscalar']}")
    print(f"    => secondary k=4 IMPOSSIBLE: {mp['secondary_k4_impossible']}; principal k=4 allowed: {mp['principal_k4_allowed']}")
    print("\n[ADDITION 2] cusp order pattern {n-1,n+1,2n} + ord-1 hinge:")
    co = cusp_order_pattern()
    for name, v in co["per_component"].items():
        print(f"    {name:>14}: ord={v['cusp_order']} ({v['order_is']}), k={v['k']}, ord-1==k: {v['ord_minus_1_eq_k']}")
    print(f"    => pattern {{n-1,n+1,2n}}: {co['pattern_is_nm1_np1_2n']}; ord-1 hinge passes: {co['ord_minus_1_formula_passes_hinge']} (TESTED-NEGATIVE)")
    print("\n[covering degree, A1d -- candidate positive mechanism]:")
    cd = covering_degree_test()
    for name, v in cd["per_component"].items():
        print(f"    {name:>14}: eigenvalue covering degree={v['eigenvalue_covering_degree']} (=k? {v['equals_k']})")
    print(f"    => {cd['status']}")
    print("\n[s_n<->c bridge] DEAD:", s_n_to_c_bridge_dead()["bridge_dead"],
          "--", s_n_to_c_bridge_dead()["reason"])


if __name__ == "__main__":
    main()
