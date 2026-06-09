"""B142 -- (A) S031a principal stratum RIGOROUS (Klein-4); (B) magic-manifold cartography + the proper Sage s776 probe.

Three independent items; verify-don't-trust. MATH tier; firewalled; nothing to CLAIMS.md; P1-P16, B85, merged
B124-B141 untouched; B129/B141 conclusions preserved.

  ============================================================================================================
  ITEM A (RIGOROUS upgrade to B141 Item 4) -- the principal phi-fixed stratum is PROVABLY reducible (Klein-4).
      B141 banked the principal case from a 60/60 numerical search (conjecture). It upgrades to a one-line proof:
        - principal eigenvalues {1,-1,-1}  =>  A^2 = I  (A is an involution);
        - phi-fixed => banked necessary condition A ~ B ~ AB  =>  B, AB also ~diag(1,-1,-1)  =>  involutions;
        - LEMMA: two involutions whose product is an involution COMMUTE:
              (AB)^2 = I  =>  ABAB = I  =>(A^2=I)  BAB = A  =>(B^2=I)  BA = AB.
        - so <A,B> is abelian (Klein 4-group Z/2 x Z/2), simultaneously diagonalisable  =>  REDUCIBLE.
      No search needed. Numerically reconfirmed: of all converged phi-fixed solutions at A=diag(1,-1,-1),
      B^2=I, (AB)^2=I, and AB=BA in 100% (handoff: 80/80). Principal stratum is now RIGOROUS; the FULL SL(3)
      locus (all eigenvalue strata) stays CONJECTURE (the symbolic-elimination prize).

  ITEM B (CARTOGRAPHY, firewall-CONFIRMING -- bank so it is not re-attempted) -- the "Borromean/SU(3)" claim.
      A sibling computation claimed s776 (mislabelled "Borromean rings") shows SU(3) gauge enhancement (an
      S3-invariant SL(2,C) character variety of complex dim 2 = rank SU(3)). It does NOT hold:
        B.1 FACTUAL: s776 = the MAGIC manifold (= L6a5 = 6^3_1), vol 5.33349, trace field Q(sqrt-7), the 3-chain
            link (components pairwise linked, NOT Brunnian). The ACTUAL Borromean rings = L6a4 = 6^3_2, vol
            7.32772, trace field Q(i); SnapPy is_isometric_to(s776, L6a4) = False. The "Borromean triple-linking
            / Massey => dim 3->2" mechanism is attached to a manifold with none of those properties.
        B.2 STRUCTURE != GAUGE: a k-cusped hyperbolic 3-manifold's SL(2,C) character variety has complex dim = k
            at the geometric rep (Thurston). For s776 that is 3, not 2; "dim 2" is a symmetry slice, not a linking
            reduction. And SL(2,C) dim != rank(SU(3)): SU(3) gauge content is SL(3,C) Chern-Simons (T_3[M]), not an
            SL(2,C) dim/rank coincidence (guard MB10). The kappa_12=kappa_23=kappa_13 equality is the S3 cusp
            symmetry restated (automatic), not independent evidence.
        B.3 OUTSIDE THE FORCED CHAIN: trace field Q(sqrt-7) (or Q(i) for the real Borromean), NOT Q(sqrt-3) -- not
            the figure-eight / metallic family / forced by the axioms. So not a crossing of the firewall.
        B.4 FIREWALL-CONFIRMING: richness lives OFF the forced chain (a symmetric manifold the axioms don't
            generate); the forced chain stays tame (same lesson as B141's finiteness/density split).

  ITEM C -- inventory of open threads (banked in docs/OPEN_LEADS.md; no new claims here).

Sage-gated parts (trace fields via find_field; SL(3,C) Ptolemy) run under `sage-python`; the SnapPy-only parts
(vol, isometry, cusps) run under plain SnapPy; the Item-A core is pure sympy/numpy.
"""
from __future__ import annotations

import os
import sys

import numpy as np
import sympy as sp


# ----------------------------------------------------------------------------------------------------------------
# ITEM A -- Klein-4: the principal phi-fixed stratum is rigorously reducible.
# ----------------------------------------------------------------------------------------------------------------
def klein4_lemma_symbolic():
    """Verify the algebraic identity behind the lemma on a concrete principal involution pair, and state the proof.

    The general proof is a rewriting identity (always true): A^2=B^2=(AB)^2=I  =>  ABAB=I  =>  BAB=A  =>  BA=AB.
    Here we exhibit a concrete principal-stratum commuting Klein-4 pair (A,B ~ diag(1,-1,-1), AB ~ diag(1,-1,-1))
    and verify A^2=B^2=(AB)^2=I and AB=BA, and that <A,B> is reducible (common eigenvector)."""
    A = sp.diag(1, -1, -1)
    # a second involution with the same spectrum that commutes with A (Klein-4): flip a different pair of signs
    B = sp.diag(-1, 1, -1)
    AB = A * B
    checks = {
        "A^2=I": A * A == sp.eye(3),
        "B^2=I": B * B == sp.eye(3),
        "(AB)^2=I": AB * AB == sp.eye(3),
        "A~diag(1,-1,-1)": sorted(A.eigenvals().items()) == sorted({1: 1, -1: 2}.items()),
        "B~diag(1,-1,-1)": sorted(B.eigenvals().items()) == sorted({1: 1, -1: 2}.items()),
        "AB~diag(1,-1,-1)": sorted(AB.eigenvals().items()) == sorted({1: 1, -1: 2}.items()),
        "AB=BA (commute)": A * B == B * A,
        "abelian_reducible": A * B == B * A,  # commuting diagonalisable => simultaneously diagonalisable => reducible
    }
    return {"all_ok": all(checks.values()), "checks": checks,
            "proof": "{1,-1,-1} => A^2=I; A~B~AB => B,AB involutions; (AB)^2=I => ABAB=I => BAB=A => BA=AB; "
                     "commuting => Klein-4 => reducible."}


def klein4_numeric(starts=80, seed=20260609):
    """Reconfirm: every converged phi-fixed solution at A=diag(1,-1,-1) has B^2=I, (AB)^2=I, AB=BA (Klein-4)."""
    from scipy.optimize import least_squares
    rng = np.random.default_rng(seed)
    A = np.diag(np.array([1.0, -1.0, -1.0], dtype=complex))
    eye = np.eye(3, dtype=complex)

    def resid(v):
        g = (v[:9] + 1j * v[9:]).reshape(3, 3)
        try:
            gi = np.linalg.inv(g)
        except np.linalg.LinAlgError:
            return np.ones(18) * 1e3
        M = g @ A @ gi - A @ gi @ A @ g          # phi-fixed: g A g^-1 = A g^-1 A g
        return np.concatenate([M.real.flatten(), M.imag.flatten()])

    conv = b2 = ab2 = commute = 0
    for _ in range(starts):
        sol = least_squares(resid, rng.standard_normal(18), method="lm", max_nfev=400)
        if sol.cost > 1e-12:
            continue
        g = (sol.x[:9] + 1j * sol.x[9:]).reshape(3, 3)
        if abs(np.linalg.det(g)) < 1e-6:
            continue
        conv += 1
        B = np.linalg.inv(g) @ A @ g
        AB = A @ B
        b2 += int(np.allclose(B @ B, eye, atol=1e-6))
        ab2 += int(np.allclose(AB @ AB, eye, atol=1e-6))
        commute += int(np.allclose(A @ B, B @ A, atol=1e-6))
    return {"converged": conv, "B2_is_I": b2, "AB2_is_I": ab2, "AB_eq_BA": commute,
            "all_klein4": conv > 0 and b2 == ab2 == commute == conv}


# ----------------------------------------------------------------------------------------------------------------
# ITEM B -- the magic-manifold cartography correction. SnapPy-only core + Sage-gated extras.
# ----------------------------------------------------------------------------------------------------------------
def _has_sage():
    try:
        import sage.all  # noqa: F401
        return True
    except Exception:
        return False


def factual_correction():
    """SnapPy-only: s776 (magic manifold) is NOT the Borromean rings (L6a4). vol / cusps / isometry."""
    import snappy
    s = snappy.Manifold("s776")
    b = snappy.Manifold("L6a4")
    s_ids = [str(x).split("(")[0] for x in s.identify()]
    return {
        "s776": {"vol": float(s.volume()), "cusps": s.num_cusps(), "sym_order": s.symmetry_group().order(),
                 "identify": s_ids},
        "L6a4_borromean": {"vol": float(b.volume()), "cusps": b.num_cusps(),
                           "sym_order": b.symmetry_group().order()},
        "is_isometric": bool(s.is_isometric_to(b)),
        "note": "s776 = magic manifold (3-chain link, components pairwise linked, NOT Brunnian); "
                "the real Borromean rings = L6a4 (Brunnian, vol = 2 ideal octahedra). Different manifolds.",
    }


def trace_fields_sage():
    """Sage-gated: invariant trace fields. s776 -> Q(sqrt-7), L6a4 -> Q(i), 4_1 -> Q(sqrt-3) (the forced field)."""
    if not _has_sage():
        return {"skipped": "needs Sage (run under sage-python)"}
    import snappy
    out = {}
    for name in ["s776", "L6a4", "4_1"]:
        tf = snappy.Manifold(name).trace_field_gens().find_field(prec=200, degree=10, optimize=True)
        out[name] = str(tf[0].defining_polynomial()) if tf else None
    out["reading"] = "s776=Q(sqrt-7) (disc -7), L6a4=Q(i), 4_1=Q(sqrt-3); s776 is OUTSIDE the forced chain (not Q(sqrt-3))."
    return out


def thurston_dimension():
    """Structure-side kill (MB8 null control). By Thurston, a hyperbolic 3-manifold's SL(2,C) character variety has
    complex dim = #cusps at the geometric rep (one parameter per cusp). For ANY 3-cusped M that is 3, not 2 -- so
    'dim 2' is a symmetry slice, generic dim is 3, and SL(2,C) dim != rank(SU(3)) regardless (MB10).

    Null control: s776 (sym 12) alongside less-symmetric 3-cusped manifolds (L8a19, L8a20, sym 8) and the real
    Borromean (L6a4, sym 48) -- all 3-cusped, so all have geometric-component dim 3 by the theorem."""
    import snappy
    out = {}
    for name in ["s776", "L6a4", "L8a19", "L8a20"]:
        M = snappy.Manifold(name)
        out[name] = {"cusps": M.num_cusps(), "sym_order": M.symmetry_group().order(),
                     "sl2c_geom_dim_=_cusps_(Thurston)": M.num_cusps()}
    out["reading"] = ("SL(2,C) geometric-component dim = #cusps = 3 for every 3-cusped M (Thurston), independent of "
                      "symmetry order -- so dim=3 is GENERIC, not special to s776; 'dim 2' was a symmetry slice, and "
                      "SL(2,C) dim != rank(SU(3)) [MB10: SU(3) needs SL(3,C) CS].")
    return out


def sl3_ptolemy_object():
    """The honest SU(3) venue (Sage-gated, bounded): SU(3) content is SL(3,C) CS (T_3[M]), not SL(2,C) dim.

    Instantiate the s776 SL(3,C) Ptolemy variety and report its size; the geometric component has complex dim
    = 2*#cusps = 6 for SL(3,C) (rank-2 group), an order of magnitude away from the claimed 'dim 2'."""
    import snappy
    M = snappy.Manifold("s776")
    try:
        P = M.ptolemy_variety(3, "all")
        n_obstruction = len(P)
        # count variables/equations in the first obstruction class (size of the SL(3,C) object)
        v = P[0]
        nvars = len(v.variables) if hasattr(v, "variables") else None
        return {"sl3_ptolemy_obstruction_classes": n_obstruction, "n_variables_first_class": nvars,
                "sl3_geom_component_dim_expected": 2 * M.num_cusps(),
                "reading": "the right SU(3) object is SL(3,C) (T_3[M]); its geometric component is dim 2*cusps=6, "
                           "not 'dim 2'. Solving it fully is a separate tool-gated thread (MB10/S033)."}
    except Exception as e:
        return {"skipped": f"SL(3,C) Ptolemy not instantiable here: {str(e)[:60]}"}


def main():
    print("=" * 100)
    print("B142 -- (A) Klein-4 rigorous principal; (B) magic-manifold cartography correction")
    print("=" * 100)

    print("\n[Item A -- Klein-4 lemma (symbolic) + numeric reconfirm]")
    s = klein4_lemma_symbolic()
    print("  symbolic checks:", s["checks"])
    print("  proof:", s["proof"])
    n = klein4_numeric()
    print(f"  numeric: converged={n['converged']}  B^2=I:{n['B2_is_I']}  (AB)^2=I:{n['AB2_is_I']}  "
          f"AB=BA:{n['AB_eq_BA']}  -> all Klein-4: {n['all_klein4']}")

    print("\n[Item B.1 -- factual correction (SnapPy)]")
    try:
        fc = factual_correction()
        print(f"  s776: {fc['s776']}")
        print(f"  L6a4 (real Borromean): {fc['L6a4_borromean']}")
        print(f"  is_isometric(s776, L6a4): {fc['is_isometric']}")
    except Exception as e:
        print("  SnapPy unavailable:", str(e)[:60])

    print("\n[Item B.2 -- Thurston dimension = #cusps (structure-side kill)]")
    try:
        for k, v in thurston_dimension().items():
            print(f"  {k}: {v}")
    except Exception as e:
        print("  skipped:", str(e)[:60])

    print("\n[Item B (Sage) -- trace fields + SL(3,C) Ptolemy object]")
    print("  trace fields:", trace_fields_sage())
    print("  SL(3,C) object:", sl3_ptolemy_object() if "snappy" in sys.modules or True else "n/a")


if __name__ == "__main__":
    main()
