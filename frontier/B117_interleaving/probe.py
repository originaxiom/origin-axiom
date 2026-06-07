"""B117 -- the interleaving insight: the tower is the Sym two-sequence; the "promotion" is a Sym^1 absence.

The Opus interleaving handoff (verify-don't-trust). The (n^2-1)-dim trivial-point tower admits TWO decompositions
that cut across each other: the HEIGHT decomposition (theta=-w0 on the A_{n-1} root system, B112) and the SYM
decomposition (the plethysm (+)_d Sym^d(M)^{mu_d}, B103/B58). Each Sym^d contributes eigenvalues
(-1)^j phi^{d-2j} at MULTIPLE heights |d-2j|. The tower factorization is their INTERSECTION; the SYM side is the
ACTUAL tower (B116).

THE INSIGHT (a clean derivation of the two-sequence's SHAPE + a reframing of the "promotion"):

  DIMENSION IDENTITY. The full set {Sym^0..Sym^n} has dim sum (n+1)(n+2)/2; the tower has dim n^2-1.
        (n+1)(n+2)/2 - (n^2-1) = -(n-4)(n+1)/2,   zero iff n=4.
  So n=4 is the UNIQUE perfect fit; n<4 is a SURPLUS (must OMIT modules), n>4 a DEFICIT (must DOUBLE modules).
  This DERIVES the shape of B103's two-sequence mu_d = [2<=d<=n] + [0<=d<=n-3]:
     n=3: surplus 2 -> omit Sym^1; the unique subset of {0,1,2,3} summing to 8 is {0,2,3}.
     n=4: surplus 0 -> all of Sym^0..Sym^4, multiplicity 1 (= the B80 tower, verified).
     n>=5: deficit -> DOUBLE the overlap Sym^2..Sym^{n-3} (n=5: Sym^2; n=6: Sym^2,Sym^3).

  THE "PROMOTION" IS A SYM^1 ABSENCE (the B111/B113 framing is SUPERSEDED). There is no promotion. At n=3 the
  tower is Sym^0 (+) Sym^2 (+) Sym^3; Sym^1 is simply ABSENT (forced by the surplus). The char(-M) at height 1
  comes from Sym^3's height-1 contribution, NOT a "promoted Sym^1". At n=4 all Sym modules are present; nothing is
  promoted. So the height-1 behaviour is a SELECTION (which Sym^d appear), not a promotion.

  DEGREE=RANK = Sym^n PRESENCE. mu_n = 1 for ALL n>=2 (the [2<=d<=n] sequence always includes d=n), so char(M^n)
  is ALWAYS a tower factor -- which is degree=rank (M^n = L) at the characteristic-polynomial level. Status
  precision (honor the DO-NOT): Sym^n's presence is DIM-FORCED only at n=3 (the unique subset {0,2,3}); at n=2,4
  it is rep-theory (B33/V18; B103), NOT a dimension necessity (at n=4 removing Sym^4 leaves {0..3} summing to 10,
  fillable by multiplicities in principle); at n>=5 it is the two-sequence form (B103).

THE REFRAME: the tower is ONE object -- the Sym two-sequence -- NOT two separable halves (sign + power). The
prize is to prove the two-sequence mu_d for all n (B103's standing open problem, the realization/trace-ring wall).

Standalone trace-map / Lie theory; NO physics; no CLAIMS.md promotion; the rho_n proof stays the prize; P1-P16
untouched.
"""
from __future__ import annotations

import importlib.util
import itertools
import math
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


_B103 = _load("b117_b103", "frontier/B103_tower_equivariance/probe.py")
_SYM = _load("b117_sym", "frontier/B58_phaseA/sym_decomposition.py")

_t, _m = sp.symbols("t m")
_PHI = (1 + sp.sqrt(5)) / 2


# --------------------------------------------------------------------------- #
# 3a -- the dimension identity
# --------------------------------------------------------------------------- #
def dimension_identity():
    """(n+1)(n+2)/2 - (n^2-1) = -(n-4)(n+1)/2; zero iff n=4. The surplus/deficit per n."""
    n = sp.symbols("n")
    diff = sp.factor((n + 1) * (n + 2) / 2 - (n ** 2 - 1))
    roots = [int(r) for r in sp.solve(diff, n)]
    surplus = {k: int(-((k - 4) * (k + 1)) / 2) for k in range(2, 9)}
    return {"diff_factored": str(diff), "roots": roots, "unique_perfect_fit": 4 in roots,
            "surplus_per_n": surplus}


# --------------------------------------------------------------------------- #
# 3b / 3e -- the Sym-selection = B103 two-sequence; n=3 uniqueness; the doubling
# --------------------------------------------------------------------------- #
def sym_selection_equals_two_sequence(nmax=8):
    """The dimension-derived Sym-selection = B103's two_sequence_mult mu_d for all n; mu_n=1; total dim n^2-1."""
    out = {}
    for n in range(2, nmax + 1):
        mu = _B103.two_sequence_mult(n)
        out[n] = {"mu": dict(sorted(mu.items())), "sym_n_mult": mu.get(n, 0),
                  "total_dim": sum((d + 1) * v for d, v in mu.items()), "target_dim": n ** 2 - 1,
                  "doubled": sorted(d for d, v in mu.items() if v >= 2)}
    return {"per_n": out, "all_total_dims_match": all(v["total_dim"] == v["target_dim"] for v in out.values()),
            "sym_n_always_present": all(v["sym_n_mult"] == 1 for v in out.values())}


def n3_uniqueness():
    """The unique subset of {0,1,2,3} with sum(d+1)=8 is {0,2,3} (Sym^1 absent) -- enumerate all 16 subsets."""
    target = 3 ** 2 - 1
    sols = [S for r in range(5) for S in itertools.combinations(range(4), r)
            if sum(d + 1 for d in S) == target]
    return {"target_dim": target, "solutions": [list(S) for S in sols],
            "unique": len(sols) == 1, "sym1_absent": 1 not in (sols[0] if sols else [])}


# --------------------------------------------------------------------------- #
# 3c -- the Sym product = the B80 proved n=4 tower
# --------------------------------------------------------------------------- #
def _char_sym(d):
    """char poly of Sym^d(M_1): roots (-1)^j phi^{d-2j}, j=0..d."""
    return sp.expand(sp.prod([_t - ((-1) ** j) * _PHI ** (d - 2 * j) for j in range(d + 1)]))


def sym_product_equals_b80_tower():
    """Sym^0..Sym^4 char-poly product = the B80 proved n=4 tower char poly (degree 15, roots match)."""
    prod = sp.expand(sp.prod([_char_sym(d) for d in range(5)]))
    sym_roots = sorted(np.roots([float(c) for c in sp.Poly(prod, _t).all_coeffs()]).real)
    tower_roots = sorted(np.linalg.eigvals(np.array(_B103._Jm_n4_exact().subs(_m, 1)).astype(np.float64)).real)
    return {"sym_degree": sp.Poly(prod, _t).degree(), "dim_sl4": 15,
            "roots_match_b80_tower": bool(np.allclose(sym_roots, tower_roots, atol=1e-6))}


# --------------------------------------------------------------------------- #
# 6 -- Sym^n always present: the precise dim-vs-rep-theory status
# --------------------------------------------------------------------------- #
def sym_n_presence_status():
    """mu_n=1 for all n>=2 (=> char(M^n) always a factor = degree=rank). Status: dim-forced only at n=3
    (unique subset); rep-theory at n=2,4 (NOT dim-necessity); two-sequence form at n>=5."""
    status = {}
    for n in range(2, 7):
        full_minus_top = (n + 1) * (n + 2) // 2 - (n + 1)     # dim of {0..n-1} at mult 1
        dim_forced = full_minus_top < n ** 2 - 1              # can {0..n-1} even reach n^2-1?
        status[n] = {"sym_n_mult": _B103.two_sequence_mult(n).get(n, 0),
                     "dim_forced": dim_forced,
                     "basis": ("dimension (unique subset)" if (n == 3) else
                               "rep-theory (B33/V18, B103) -- NOT dim-necessity" if n in (2, 4) else
                               "two-sequence form (B103)")}
    return {"per_n": status, "char_Mn_always_a_factor": all(v["sym_n_mult"] == 1 for v in status.values()),
            "caveat": "Sym^n presence is dim-FORCED only at n=3; rep-theory at n=2,4; two-sequence form at n>=5"}


# --------------------------------------------------------------------------- #
# PATH 4 -- the n=6 prediction vs the (gauge-corrupted) B66 data (consistency)
# --------------------------------------------------------------------------- #
def n6_path4_crosscheck():
    """The two-sequence predicts the n=6 bulk (Sym^2, Sym^3 doubled). B66 (26/35, gauge-corrupted) measured the
    |k|=3 total as 2 -- the known under-count (B58 Phase A); the two-sequence gives |k|=3 total = a_3+b_3 = 2+1 = 3
    (= max(n-d,1), the V17-annotated correction). A consistency check (n=6 is gauge-corrupted; not decisive)."""
    a, b = _SYM.sym_counts(6)
    k3_total = a.get(3, 0) + b.get(3, 0)
    return {"n6_char_M": dict(sorted(a.items())), "n6_char_negM": dict(sorted(b.items())),
            "k3_total_prediction": k3_total, "b66_measured_k3": 2,
            "note": "B66's measured 2 is the gauge under-count (B58 Phase A); the two-sequence's 3 = max(n-d,1) "
                    "(the V17-annotated correction). The doubled modules are Sym^2,Sym^3 (the overlap [2<=d<=n-3])."}


def main():
    print("=" * 78)
    print("B117 -- the tower is the Sym two-sequence; the 'promotion' is a Sym^1 absence")
    print("=" * 78)
    di = dimension_identity()
    print(f"\n[3a] dimension identity: (n+1)(n+2)/2-(n^2-1) = {di['diff_factored']} -> roots {di['roots']}; "
          f"surplus {di['surplus_per_n']}")
    ss = sym_selection_equals_two_sequence()
    print(f"\n[Sym-selection = two-sequence] total dims match: {ss['all_total_dims_match']}; "
          f"Sym^n always present (mu_n=1): {ss['sym_n_always_present']}")
    for n, v in ss["per_n"].items():
        print(f"    n={n}: mu={v['mu']}  doubled={v['doubled']}")
    u = n3_uniqueness()
    print(f"\n[3b] n=3 unique selection {u['solutions']} (Sym^1 absent: {u['sym1_absent']})")
    sp4 = sym_product_equals_b80_tower()
    print(f"\n[3c] Sym^0..4 product (deg {sp4['sym_degree']}) = B80 n=4 tower: {sp4['roots_match_b80_tower']}")
    sn = sym_n_presence_status()
    print(f"\n[6] char(M^n) always a factor (= degree=rank): {sn['char_Mn_always_a_factor']}")
    for n, v in sn["per_n"].items():
        print(f"    n={n}: present, basis = {v['basis']}")
    print(f"    CAVEAT: {sn['caveat']}")
    c = n6_path4_crosscheck()
    print(f"\n[Path 4] n=6 prediction char(M^h) {c['n6_char_M']}, char(-M^h) {c['n6_char_negM']}; "
          f"|k|=3 total predicted {c['k3_total_prediction']} vs B66 measured {c['b66_measured_k3']} (under-count)")
    print("\nREFRAME: the tower = the Sym two-sequence (ONE object); 'promotion' SUPERSEDED (Sym^1 absence);")
    print("degree=rank's char(M^n) = Sym^n presence. The prize = prove the two-sequence mu_d for all n (B103).")


if __name__ == "__main__":
    main()
