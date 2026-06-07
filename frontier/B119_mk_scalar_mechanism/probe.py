"""B119 -- the M^k-scalar (centrality) mechanism across components, n=3..6: a sharp negative on "prove k=n".

Chat-2 PATH 3 (the hard path; be brave). B111 ADDITION 1 (the one surviving exponent lead): the cusp eigenvalue
arithmetic CONTROLS the degree=rank exponent -- on the SL(4) SECONDARY, M^4=zeta^4=-1 is SCALAR, so [A,B]=c*(-1)Id
is a CENTRAL (trivial) commutator => k=4 is algebraically impossible and k=3=n-1 is forced. B111 left open whether
the same arithmetic can PROVE k=n on the PRINCIPAL. This probe extends the M^k-centrality arithmetic to all n and
the three component types, attempts the brave k=n proof on the principal -- and reports a SHARP NEGATIVE with the
obstruction stated precisely (the B95 wall), plus an emergent correction to the cusp-order reading (B111 ADD2).

REFRAME (B117). The BULK char(M^n) is no longer a "promotion" to be explained -- it is Sym^n presence (mu_n=1,
B117). So this is the PERIPHERAL k=n on the Dehn-filling component: the one open shot at a POSITIVE power-half
mechanism. It does not close.

THE ARITHMETIC (pure eigenvalue, no walled tower).
  Principal degree=rank component (B95): the forced cusp spectrum is eigenvalue 1 at mult n-2 plus {a, 1/a} with
  a + 1/a = 3 - n. The order of a (2cos = 3-n) is:
        n=3 -> 4,   n=4 -> 3,   n=5 -> 2,   n>=6 -> INFINITE (|2cos|>2, hyperbolic, not a root of unity).
  M^k is CENTRAL on the principal iff order(a) | k. So M^k is NON-central for k not a multiple of order(a).

THE BRAVE k=n ATTEMPT -- and why it does NOT close.
  Where the principal exists (n=3,4): the longitude L=[A,B] of an irreducible rep is NON-central, so M^k must be
  non-central => k is NOT a multiple of order(a). That EXCLUDES k in {order(a), 2 order(a), ...} (e.g. n=4 excludes
  k=3,6) but does NOT single out k=n -- many k qualify (n=4: k=1,2,4,5 all non-central). So centrality arithmetic
  is NECESSARY but NOT SUFFICIENT; k=n is pinned by the PROVED A-polynomial L=(-1)^{n-1}M^n (B83), not by
  scalar-ness. The "scalar-ness + bundle relations" route is SUBSUMED by B83, not an independent proof.
  For n>=5 there is NOTHING to prove: the principal Dehn-filling rep does NOT exist irreducibly (B95 -- n=5
  degenerates to A^2=I/dihedral/reducible; n>=6 has no finite-order spectrum of the forced shape). So
  "exponent = rank on the principal" is an n in {3,4} phenomenon (B95); the brave k=n proof CANNOT be completed.

THE SECONDARY (extends B111 to the type arithmetic, where it exists). On the SL(4) secondary (odd 8th roots,
  order 2n=8): M^k central iff n | k, so M^n = -I is central => k=n gives a central commutator => the OBSERVED
  non-central longitude is M^{n-1} => exponent n-1. (Generalizes B111's secondary result as the 2n-type arithmetic.)

EMERGENT (chased inline) -- a correction to B111 ADD2. The cusp order on the degree=rank PRINCIPAL is order(a)
  with a+1/a=3-n, i.e. the sequence {4, 3, 2, infinite} for n=3,4,5,>=6 -- NOT a clean "{n-1, n+1, 2n}" law. The
  B111 ADD2 reading conflated DIFFERENT components: the n=3 W1 (order 4 = n+1), the n=4 principal (order 3 = n-1),
  the n=4 secondary (order 8 = 2n). There is no single all-n cusp-order law; the orders are the multiplicative
  orders of each component's primitive cusp eigenvalue, and M^k centrality is governed by exactly those orders.

Standalone trace-map / Lie theory; NO physics; no CLAIMS.md promotion; the rho_n proof stays the prize; P1-P16
untouched.
"""
from __future__ import annotations

import importlib.util
import math
import pathlib
import sys

import numpy as np

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_B95 = _load("b119_b95", "frontier/B95_degree_rank_mechanism/probe.py")
_B111 = _load("b119_b111", "frontier/B111_sign_structure/probe.py")


def _is_central(vals, tol=1e-9):
    a = np.array(vals, complex)
    return bool(np.max(np.abs(a - a[0])) < tol)


def _order(z, qmax=48, tol=1e-9):
    for q in range(1, qmax + 1):
        if abs(z ** q - 1) < tol:
            return q
    return None


# --------------------------------------------------------------------------- #
# the principal a-root order: {4, 3, 2, infinite}
# --------------------------------------------------------------------------- #
def principal_cusp_order(nmax=8):
    """The forced principal cusp order = order(a), a+1/a = 3-n (B95): {n=3:4, n=4:3, n=5:2, n>=6: infinite}."""
    out = {}
    for n in range(3, nmax + 1):
        _, is_rou, apa = _B95.forced_principal_spectrum(n)
        val = (3 - n) / 2.0
        if abs(val) <= 1:
            theta = math.acos(val)
            order = int(round(2 * math.pi / theta)) if theta > 1e-9 else 1
        else:
            order = None                                   # hyperbolic -> not a root of unity
        out[n] = {"a_plus_ainv": apa, "is_root_of_unity": bool(is_rou), "order_a": order}
    return out


# --------------------------------------------------------------------------- #
# M^k centrality on the principal; the brave k=n attempt
# --------------------------------------------------------------------------- #
def mpower_central_principal(nmax=5):
    """On the principal, M^k central iff order(a) | k. k=n is non-central where the principal exists (n=3,4) but
    NOT the unique non-central k -> centrality does NOT force k=n."""
    out = {}
    for n in range(3, nmax + 1):
        spec, is_rou, _ = _B95.forced_principal_spectrum(n)
        if spec is None or not is_rou:
            out[n] = {"exists_finite_order": False}
            continue
        s = np.array(spec, complex)
        oa = _order(s[np.argmax(np.abs(s - 1))])           # order of the non-trivial eigenvalue a
        central = {k: _is_central(s ** k) for k in range(1, 2 * n + 1)}
        noncentral_ks = [k for k, c in central.items() if not c]
        out[n] = {"exists_finite_order": True, "order_a": oa,
                  "kn_noncentral": (not central.get(n, True)),
                  "noncentral_ks_upto_2n": noncentral_ks,
                  "kn_is_unique_noncentral": noncentral_ks == [n]}
    return out


def brave_kn_verdict():
    """The brave attempt: can scalar-ness PROVE k=n on the principal? NO. Where it exists (n=3,4) centrality only
    excludes multiples of order(a), not pinning k=n (B83's A-poly pins it). For n>=5 the principal does not exist
    irreducibly (B95). So exponent=rank is an n in {3,4} phenomenon; the proof cannot be completed."""
    mc = mpower_central_principal(5)
    n5 = _B95.n5_principal_is_reducible()
    forced_by_scalarness = all(mc[n].get("kn_is_unique_noncentral", False) for n in (3, 4))
    return {"kn_noncentral_where_exists": all(mc[n]["kn_noncentral"] for n in (3, 4)),
            "kn_forced_by_scalarness": forced_by_scalarness,          # expected FALSE -- not unique
            "n5_principal_A2_is_I": bool(n5[0]),                       # B95: n=5 degenerates (reducible)
            "n6plus_principal_finite_order": principal_cusp_order(6)[6]["is_root_of_unity"],  # False
            "verdict": "k=n on the principal is NOT forced by M^k centrality (only multiples of order(a) excluded; "
                       "k=n pinned by the proved A-poly B83, not scalar-ness). For n>=5 the principal does not "
                       "exist irreducibly (B95: n=5 A^2=I dihedral; n>=6 no finite-order spectrum). exponent=rank "
                       "is an n in {3,4} phenomenon; the brave proof CANNOT be completed -- a sharp negative."}


# --------------------------------------------------------------------------- #
# the secondary (2n) type arithmetic -- extends B111's secondary result
# --------------------------------------------------------------------------- #
def secondary_exponent_arithmetic():
    """On the SL(4) secondary (odd 8th roots, order 2n=8): M^k central iff n | k, so M^n=-I is central => k=n
    gives a central commutator => the non-central longitude is M^{n-1} => exponent n-1 (= B111's secondary)."""
    spec = _B111._CUSP_SPECTRA["SL4_secondary"]
    s = np.array(spec, complex)
    n = len(s)
    central = {k: _is_central(s ** k) for k in range(1, 2 * n + 1)}
    central_ks = [k for k, c in central.items() if c]
    return {"n": n, "cusp_order_2n": _order(s[0]), "Mn_central": central.get(n, False),
            "central_ks_upto_2n": central_ks, "central_iff_n_divides_k": central_ks == [n, 2 * n],
            "exponent_forced": n - 1,
            "note": "M^n=-I central => k=n central commutator => non-central longitude = M^{n-1} => exponent n-1 "
                    "(B111). The 2n-type arithmetic; valid where the secondary exists (n=4 computed; n=3 = W2)."}


# --------------------------------------------------------------------------- #
# emergent: the cusp-order correction to B111 ADD2
# --------------------------------------------------------------------------- #
def cusp_order_correction():
    """The cusp order on the degree=rank principal = order(a) = {4,3,2,inf}, NOT a clean {n-1,n+1,2n} law. B111
    ADD2 read three DIFFERENT components as one law. M^k centrality is governed by each component's eigenvalue
    order. Scalar-ness <-> order: M^k central iff order(a) | k (principal)."""
    pc = principal_cusp_order(6)
    seq = [pc[n]["order_a"] for n in (3, 4, 5)] + ["inf"]      # 4,3,2,inf
    b111_components = {"n=3 W1": ("order 4", "n+1"), "n=4 principal": ("order 3", "n-1"),
                       "n=4 secondary": ("order 8", "2n")}
    return {"principal_order_sequence_n3to6": seq,
            "clean_nm1_np1_2n_law": False,                         # the principal sequence is 4,3,2,inf, not a single law
            "b111_add2_conflated_components": b111_components,
            "scalarness_governed_by_order": "M^k central iff order(a)|k (principal); the orders ARE the cusp "
                                            "eigenvalue orders, not a closed (n-1,n+1,2n) formula."}


def main():
    print("=" * 78)
    print("B119 -- the M^k-scalar (centrality) mechanism across components: a sharp negative on 'prove k=n'")
    print("=" * 78)
    pc = principal_cusp_order(8)
    print("\n[principal cusp order = order(a), a+1/a=3-n]:")
    for n, v in pc.items():
        print(f"    n={n}: a+1/a={v['a_plus_ainv']}, root-of-unity={v['is_root_of_unity']}, order(a)={v['order_a']}")
    mc = mpower_central_principal(5)
    print("\n[M^k centrality on the principal: central iff order(a)|k]:")
    for n, v in mc.items():
        if v["exists_finite_order"]:
            print(f"    n={n}: order(a)={v['order_a']}, k=n non-central={v['kn_noncentral']}, "
                  f"non-central k<=2n={v['noncentral_ks_upto_2n']}, k=n UNIQUE={v['kn_is_unique_noncentral']}")
        else:
            print(f"    n={n}: principal does NOT exist as a finite-order irreducible (B95)")
    bv = brave_kn_verdict()
    print(f"\n[BRAVE k=n attempt] forced by scalar-ness: {bv['kn_forced_by_scalarness']} "
          f"(non-central where exists: {bv['kn_noncentral_where_exists']}); n=5 A^2=I: {bv['n5_principal_A2_is_I']}; "
          f"n>=6 finite-order: {bv['n6plus_principal_finite_order']}")
    print(f"    VERDICT: {bv['verdict']}")
    se = secondary_exponent_arithmetic()
    print(f"\n[secondary 2n-type] M^n central: {se['Mn_central']}, central iff n|k: {se['central_iff_n_divides_k']} "
          f"=> exponent forced = n-1 = {se['exponent_forced']} (B111)")
    cc = cusp_order_correction()
    print(f"\n[EMERGENT -- B111 ADD2 correction] principal order sequence n=3..6: {cc['principal_order_sequence_n3to6']}"
          f" (clean (n-1,n+1,2n) law: {cc['clean_nm1_np1_2n_law']})")
    print("    => no single all-n cusp-order law; B111 ADD2 conflated W1(n+1), principal(n-1), secondary(2n).")
    print("\nSCOPE: a sharp NEGATIVE on the positive power-half mechanism (the peripheral k=n). The bulk char(M^n)")
    print("is Sym^n presence (B117); the all-n prize stays the Sym two-sequence mu_d (B103). NO physics.")


if __name__ == "__main__":
    main()
