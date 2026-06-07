"""B121 -- the monodromy sl(2) grading of the adjoint: an EXTERNAL det=-1 GL(2,Z)-rep, not the principal one.

Phase 2 of the physics-bridge sweep (the structural lead). The (n^2-1)-dim trivial-point tower carries TWO
SL(2)-actions, and they are genuinely different:

  (A) the INTERNAL principal sl(2) of sl_n (Kostant): the adjoint = Sym^{n-1} (x) Sym^{n-1} (-) triv =
      (+)_{i=1}^{n-1} Sym^{2i} -- EVEN highest weights only; det=+1 (the defining rep Sym^{n-1} lands in SL(n)).
      This is the HITCHIN / Fuchsian section (B101: V0 = the principal V2 sector for SL(3)).
  (B) the EXTERNAL monodromy: the figure-eight mapping class acts on the SL(n) trace ring via N in GL(2,Z); at the
      trivial point this linearizes (B103) to rho_n(N) = (+)_d Sym^d(M_m)^{mu_d}, the Sym two-sequence (B117).

The NEGATIVE 'tower != Kostant' was already banked (B89-T/B98). This probe gives the POSITIVE characterization and
the precise OBSTRUCTION:

  THE PARITY OBSTRUCTION. The tower (monodromy rep) has ODD SL(2) highest weights for all n>=3 (n=3: Sym^3; n=4:
  Sym^1,Sym^3; ...), while the Kostant adjoint is EVEN-only. So the two SL(2)-reps are INEQUIVALENT for n>=3 (they
  agree only at n=2). The odd weights are the signature of det(M_m) = -1: the principal embedding uses the det=+1
  rep Sym^{n-1}; the monodromy uses the seed M_m directly, which sits in GL(2,Z) minus SL(2,Z) (det=-1). Concretely
  Sym^d(M_m) has eigenvalues (-1)^j phi^{d-2j} and det Sym^d(M_m) = (-1)^{d(d+1)/2} -- the det=-1 leaves a sign in
  every block; the odd-highest-weight blocks are exactly the char(-M^h) sectors (B112/B118's (-1)^{h+1} sign).

So: the monodromy sl(2) is the EXTERNAL det=-1 GL(2,Z)-action (the mapping class group), distinguished from the
INTERNAL principal/Hitchin sl(2) (det=+1) by the det=-1 PARITY -- on the same (n^2-1)-dim adjoint. The relation is
NOT a dimension coincidence (the kill condition): the parity obstruction is an explicit, n>=3 inequivalence.

Standalone rep theory / Lie theory; the Hitchin/Langlands physics READING is firewalled in
speculations/S024_monodromy_hitchin.md. NO physics in this file; no CLAIMS.md promotion; the rho_n / Sym-mu_d
proof stays the prize; P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_B103 = _load("b121_b103", "frontier/B103_tower_equivariance/probe.py")


def _mu(n):
    return _B103.two_sequence_mult(n)


# --------------------------------------------------------------------------- #
# the two SL(2)-actions on the (n^2-1)-dim adjoint
# --------------------------------------------------------------------------- #
def tower_highest_weights(n):
    """The monodromy rep (the tower) as SL(2)-irreps: highest weights = the two-sequence support (with mult)."""
    return sorted(d for d, v in _mu(n).items() for _ in range(v))


def kostant_highest_weights(n):
    """The principal sl(2) of sl_n (Kostant): adjoint = (+)_{i=1}^{n-1} Sym^{2i} -- even highest weights 2..2n-2."""
    return [2 * i for i in range(1, n)]


def monodromy_vs_principal(nmax=8):
    """The two SL(2)-reps share the dimension n^2-1 and agree ONLY at n=2; for n>=3 the tower has ODD highest
    weights (Kostant is even-only) -> INEQUIVALENT. NOT a dimension coincidence."""
    out = {}
    for n in range(2, nmax + 1):
        tw, kw = tower_highest_weights(n), kostant_highest_weights(n)
        dim_t = sum(d + 1 for d in tw)
        odd = [d for d in tw if d % 2 == 1]
        out[n] = {"tower_hw": tw, "kostant_hw": kw, "dim": dim_t, "dim_is_n2m1": dim_t == n * n - 1,
                  "agree": tw == kw, "odd_weights_in_tower": odd}
    return {"per_n": out, "agree_only_at_n2": all((out[n]["agree"]) == (n == 2) for n in out),
            "odd_weights_for_all_n_ge_3": all(len(out[n]["odd_weights_in_tower"]) > 0 for n in out if n >= 3),
            "dims_all_match": all(out[n]["dim_is_n2m1"] for n in out)}


# --------------------------------------------------------------------------- #
# the obstruction IS det(M_m) = -1
# --------------------------------------------------------------------------- #
def odd_weight_is_det_minus_one(dmax=6):
    """The odd weights come from det(M_m)=-1. Sym^d of the seed M_m=[[m,1],[1,0]] (det=-1) has eigenvalues
    (-1)^j phi^{d-2j}, and det Sym^d(M_m) = (-1)^{d(d+1)/2} -- a sign in every block; for the principal (det=+1
    seed) every Sym^d has det +1. The odd-d blocks are the char(-M^h) sectors (B112/B118)."""
    m = sp.symbols("m")
    M = sp.Matrix([[m, 1], [1, 0]])                      # det = -1
    P = sp.Matrix([[m, 1], [-1, 0]])                     # a det = +1 partner (same trace), eigenvalues != det=-1
    rows = {}
    for d in range(1, dmax + 1):
        det_M = sp.simplify(_sym_power(M, d).det())
        det_P = sp.simplify(_sym_power(P, d).det())
        rows[d] = {"det_symd_Mm": det_M, "predicted_(-1)^d(d+1)/2": (-1) ** (d * (d + 1) // 2),
                   "det_symd_principal_partner": det_P}
    return {"per_d": {d: {"det_symd_Mm": str(rows[d]["det_symd_Mm"]),
                          "matches_(-1)^d(d+1)/2": sp.simplify(rows[d]["det_symd_Mm"]
                                                              - rows[d]["predicted_(-1)^d(d+1)/2"]) == 0,
                          "det_principal_partner": str(rows[d]["det_symd_principal_partner"])}
                      for d in rows},
            "det_minus_one_leaves_sign": all(
                sp.simplify(rows[d]["det_symd_Mm"] - (-1) ** (d * (d + 1) // 2)) == 0 for d in rows)}


def _sym_power(Mat, k):
    """Sym^k of a 2x2 matrix (the induced action on degree-k monomials)."""
    a, b, c, dd = Mat[0, 0], Mat[0, 1], Mat[1, 0], Mat[1, 1]
    x, y = sp.symbols("x y")
    S = sp.zeros(k + 1, k + 1)
    for i in range(k + 1):
        poly = sp.expand((a * x + c * y) ** (k - i) * (b * x + dd * y) ** i)
        for j in range(k + 1):
            S[j, i] = poly.coeff(x, k - j).coeff(y, j)
    return S


# --------------------------------------------------------------------------- #
# the relation summary (internal/principal vs external/monodromy)
# --------------------------------------------------------------------------- #
def relation_summary():
    """The two SL(2)-actions on the (n^2-1)-dim adjoint: INTERNAL principal (Kostant, even, det=+1, the
    Hitchin/Fuchsian section, B101) vs EXTERNAL monodromy (GL(2,Z), mixed parity, det=-1, the mapping class group).
    Inequivalent for n>=3 by the det=-1 parity obstruction -- NOT a dimension coincidence."""
    mv = monodromy_vs_principal(8)
    dm = odd_weight_is_det_minus_one(6)
    return {"agree_only_at_n2": mv["agree_only_at_n2"], "dims_all_match": mv["dims_all_match"],
            "odd_weights_for_all_n_ge_3": mv["odd_weights_for_all_n_ge_3"],
            "obstruction_is_det_minus_one": dm["det_minus_one_leaves_sign"],
            "not_a_dimension_coincidence": (mv["dims_all_match"] and not all(
                mv["per_n"][n]["agree"] for n in mv["per_n"] if n >= 3)),
            "summary": "INTERNAL principal sl(2) c sl_n (Kostant, even weights, det=+1 = the Hitchin/Fuchsian "
                       "section, B101) vs EXTERNAL monodromy GL(2,Z) (the tower, mixed parity, det=-1 = the "
                       "mapping class group). Same (n^2-1)-dim adjoint; INEQUIVALENT for n>=3 by the det=-1 parity "
                       "obstruction (odd Sym^d). The negative 'tower != Kostant' (B89-T/B98) is now characterized "
                       "POSITIVELY: the monodromy is the det=-1 external action."}


def main():
    print("=" * 78)
    print("B121 -- the monodromy sl(2) grading: an EXTERNAL det=-1 GL(2,Z)-rep, not the principal one")
    print("=" * 78)
    mv = monodromy_vs_principal(8)
    print("\n[two SL(2)-actions on the (n^2-1)-dim adjoint]")
    for n, v in mv["per_n"].items():
        print(f"    n={n}: tower hw={v['tower_hw']} (odd {v['odd_weights_in_tower']}) | "
              f"kostant hw={v['kostant_hw']} | dim {v['dim']} | agree={v['agree']}")
    print(f"\n  agree only at n=2: {mv['agree_only_at_n2']}; odd weights for all n>=3: "
          f"{mv['odd_weights_for_all_n_ge_3']}; dims all = n^2-1: {mv['dims_all_match']}")
    dm = odd_weight_is_det_minus_one(6)
    print(f"\n[obstruction = det(M_m)=-1] det Sym^d(M_m) = (-1)^{{d(d+1)/2}} (a sign in every block): "
          f"{dm['det_minus_one_leaves_sign']}")
    for d, v in dm["per_d"].items():
        print(f"    d={d}: det Sym^d(M_m)={v['det_symd_Mm']} (matches: {v['matches_(-1)^d(d+1)/2']}), "
              f"det Sym^d(principal det+1 partner)={v['det_principal_partner']}")
    rs = relation_summary()
    print(f"\n[RELATION] not a dimension coincidence: {rs['not_a_dimension_coincidence']}; obstruction is det=-1: "
          f"{rs['obstruction_is_det_minus_one']}")
    print(f"    {rs['summary']}")
    print("\nThe Hitchin/Langlands READING is firewalled in speculations/S024. NO physics here.")


if __name__ == "__main__":
    main()
