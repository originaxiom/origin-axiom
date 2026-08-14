#!/usr/bin/env python3
"""B867 -- the Sakharov gate: are the three baryogenesis PRECONDITIONS structurally present?

NOT a computation of the baryon asymmetry (a value -- Gate 5 forbids it and nothing here
approaches it). A STRUCTURAL checklist: does the framework's banked cascade + transition supply
the stage on which baryogenesis could run? Each condition is tied to a banked arc and to a small
computation run here.

  S1 (B violation available): the SM-step coset is exactly (3,2)+(3bar,2) -- the X,Y boson
      content that mediates B-violating processes in SU(5)/SO(10); and the nu_R slot (B865's
      singlets) supplies the L-violating Majorana ingredient.
  S2 (C/CP violation possible): a chiral theory violates C structurally (the registerability
      gate IS the statement); CP needs a physical KM phase, which exists iff the generation
      count N satisfies (N-1)(N-2)/2 >= 1, i.e. N >= 3 -- and B866's S3 triple is the first
      structural THREE. Computed here: N = 3 is the MINIMAL N with a phase.
  S3 (departure from equilibrium): the transition is one-time -- V(phi) < V(0) with a barrier
      (B853/B6, exact Galois-conjugate values) and the mechanism consumes itself (B737-P2/B852:
      closing the cusp destroys the engine; no re-equilibration channel).

Mathematics + structural scope. Nothing reaches CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))


def s1_coset():
    """su(5) = SM + coset; the coset is (3,2)+(3bar,2), dim 12 -- the X,Y content."""
    dim_su5, dim_sm = 24, 12
    coset = dim_su5 - dim_sm
    xy = 6 + 6                              # (3,2) + (3bar,2)
    return dict(coset_dim=coset, xy_dim=xy, match=(coset == xy),
                nuR="B865: the chain's singlets land in (1,1)_0 -- the Majorana/L-violation slot")


def s2_km_counting():
    """Physical CP phases for N generations: (N-1)(N-2)/2. First N with a phase = 3."""
    counts = {N: (N - 1) * (N - 2) // 2 for N in range(1, 6)}
    first = min(N for N, c in counts.items() if c >= 1)
    return dict(phase_counts=counts, first_N_with_phase=first,
                s3_triple="B866: the S3 orbit of distinguished charges -- the structural three "
                          "(SIGNATURE, not yet a generation mechanism)")


def s3_barrier():
    """The one-time transition: exact potential values (B6/B853) + mechanism consumption."""
    k = sp.Symbol('kappa', positive=True)
    t = sp.Symbol('tau')
    V = k * (t**3 / 3 - t**2 / 2 - t)
    phi = (1 + sp.sqrt(5)) / 2
    Vphi = sp.simplify(V.subs(t, phi) / k)
    Vanti = sp.simplify(V.subs(t, -1 / phi) / k)
    return dict(V_phi_over_kappa=str(Vphi), V_anti_over_kappa=str(Vanti),
                broken_below_symmetric=bool(Vphi < 0), barrier=bool(Vanti > 0),
                galois_conjugates=bool(sp.simplify(
                    Vphi.subs(sp.sqrt(5), -sp.sqrt(5)) - Vanti) == 0),
                consumption="B737-P2/B852: Dehn filling destroys the cusp = the transition "
                            "consumes its own mechanism; no re-equilibration channel")


def main():
    res = dict(S1=s1_coset(), S2=s2_km_counting(), S3=s3_barrier())
    res["verdict"] = dict(
        S1_present=res["S1"]["match"],
        S2_present=(res["S2"]["first_N_with_phase"] == 3),
        S3_present=(res["S3"]["broken_below_symmetric"] and res["S3"]["barrier"]),
        all_preconditions_structural=True,
        what_this_is_NOT="a computation of the asymmetry (a value; Gate 5). The stage, not the "
                         "play. S2 additionally inherits B866's signature-not-mechanism caveat.")
    res["verdict"]["all_preconditions_structural"] = (
        res["verdict"]["S1_present"] and res["verdict"]["S2_present"]
        and res["verdict"]["S3_present"])
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)

    print("=" * 74)
    print("B867 -- the Sakharov gate (structural preconditions only)")
    print("=" * 74)
    print(f"\n  S1 B-violation available : coset {res['S1']['coset_dim']} = X,Y content "
          f"{res['S1']['xy_dim']} -> {res['verdict']['S1_present']}")
    print(f"  S2 CP possible           : phases(N) = {res['S2']['phase_counts']}; "
          f"first N with a phase = {res['S2']['first_N_with_phase']} = the S3 triple's 3 "
          f"-> {res['verdict']['S2_present']}")
    print(f"  S3 out-of-equilibrium    : V(phi)/k = {res['S3']['V_phi_over_kappa']} < 0, "
          f"barrier {res['S3']['V_anti_over_kappa']} > 0, Galois-conjugate "
          f"{res['S3']['galois_conjugates']} -> {res['verdict']['S3_present']}")
    print(f"\n  ALL THREE PRECONDITIONS STRUCTURALLY PRESENT: "
          f"{res['verdict']['all_preconditions_structural']}")
    print("  (the stage, not the play -- the asymmetry itself is a value and is NOT computed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
