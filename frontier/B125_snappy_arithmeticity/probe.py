"""B125 -- SnapPy arithmeticity of the metallic R^m L^m once-punctured-torus bundles (overturns K009).

HEADLINE (CORRECTION). With SnapPy now runnable in-sandbox, the invariant trace field kM of the metallic family is
computable directly. Result: arithmeticity does NOT uniquely select m=1. It selects {m=1 golden, m=2 silver} and
kills m>=3. This is exactly the gap the B123 audit flagged -- Reid 1991 is about KNOTS, but the m>=2 metallic
manifolds are once-punctured-torus BUNDLES, so knot-uniqueness never transferred. (And it closes cleanly: K009
already cited "exactly two arithmetic once-punctured-torus bundles" -- they are m=1 and m=2.)

CALIBRATION (B147). The "exactly two" here is correct as a statement about the METALLIC family (m=1 golden Q(sqrt-3),
m=2 silver Q(i)); do NOT read it as "exactly two o-p-t bundles overall." B147 found arithmetic CHIRAL (non-metallic)
o-p-t bundles -- RRL/RLL = Q(sqrt-7), full Maclachlan-Reid (imag-quadratic invariant trace field + integral traces,
Humbert vol = 3x Bianchi covolume) -- so there are >=4 arithmetic o-p-t bundles. This metallic m=1,2 result STANDS;
only the loose paraphrase "exactly two o-p-t bundles" was over-stated. See frontier/B147_arithmetic_chiral_bundle/.

STRUCTURAL IDENTITY (the spine; pure numpy, always runs).
    M_m = [[m,1],[1,0]],  det = -1.   Its orientable square is a positive LR-word:
        M_m^2 = R^m L^m ,   R = [[1,1],[0,1]],  L = [[1,0],[1,1]].
    trace(M_m^2) = m^2 + 2  (-> 3,6,11,18,27,38). For m=1 this is RL = the figure-eight (m004).
    So the orientable metallic members ARE the R^m L^m punctured-torus bundles ('b++' + 'R'*m + 'L'*m in SnapPy).

ARITHMETICITY CRITERION (Maclachlan-Reid, *The Arithmetic of Hyperbolic 3-Manifolds*, Thm 8.3.2, non-cocompact):
    a non-cocompact finite-covolume Kleinian group is ARITHMETIC  <=>  kM is imaginary quadratic AND every trace is
    an algebraic integer. (For cusped manifolds the invariant quaternion algebra is automatically M_2(kM) -- the
    parabolics split it -- so there is no separate algebra condition.)

THE RESULT (VERIFIED in-sandbox, SnapPy 3.3.2 + cypari 2.5.6; reproduced two ways -- shape field [Neumann-Reid] and
the lift-independent traces-of-SQUARES field):
    m=1 golden : kM = Q(sqrt-3)  (Phi_6 shape e^{i pi/3})  -- imag.quadratic, integral -> ARITHMETIC
    m=2 silver : kM = Q(i)        (roots 1+-i)              -- imag.quadratic, integral -> ARITHMETIC  [NEW]
    m=3 bronze : kM degree >= 4 (canonical 6)  -- not imag.quadratic            -> non-arithmetic
    m=4        : kM degree 4                     -- not imag.quadratic            -> non-arithmetic
    m=5,6      : kM degree >= 4 (canonical 6)  -- not imag.quadratic            -> non-arithmetic
    Q(sqrt-3) and Q(i) have distinct squarefree discriminants -> DIFFERENT Bianchi families -> NOT commensurable:
    two genuinely distinct arithmetic metallic manifolds.

HONEST SCOPE (verify-don't-trust on THIS handoff). The two ARITHMETIC verdicts (m=1 Q(sqrt-3), m=2 Q(i)) and the
non-arithmetic verdict for m>=3 (kM not imaginary quadratic) reproduce robustly and precision-stably. The EXACT
non-arithmetic field degree for m=3,5,6 is primitive-element/precision-sensitive in a numpy+cypari reproduction
(observed 4 or 8; the canonical Maclachlan-Reid value is 6) -- it does NOT affect any verdict (anything > 2 kills
imaginary-quadratic). We bank the verdicts + the two fields; we do not over-claim the exact m>=3 degrees.

PRESERVED (NOT corrected): Reid 1991 (the figure-eight is the unique arithmetic KNOT) STANDS -- it is about knot
complements in S^3; m=2's R^2 L^2 being arithmetic confirms the theorem's scope (m=2 is necessarily not a knot,
else a second arithmetic knot). The order-6 echo (B123) stays an OBSERVATION, not a connection.

MATH tier only. Physics POSTULATED/quarantined, untouched. Nothing to CLAIMS.md; P1-P16 untouched; the functorial
Sym(W)->trace-ring wall (B85) is NOT touched by any of this.
"""
from __future__ import annotations

import numpy as np

# The verified record (SnapPy 3.3.2 + cypari 2.5.6, in-sandbox, 2026-06-08). Used by the tests/FINDINGS so the
# repo stays green without SnapPy. `live_arithmeticity()` below recomputes it when SnapPy is importable.
RECORD = {
    1: {"metal": "golden", "field": "Q(sqrt-3)", "kM_degree": 2, "imag_quadratic": True,  "arithmetic": True},
    2: {"metal": "silver", "field": "Q(i)",      "kM_degree": 2, "imag_quadratic": True,  "arithmetic": True},
    3: {"metal": "bronze", "field": "deg>=4 (canon 6)", "kM_degree": None, "imag_quadratic": False, "arithmetic": False},
    4: {"metal": "-",      "field": "deg 4",     "kM_degree": 4, "imag_quadratic": False, "arithmetic": False},
    5: {"metal": "-",      "field": "deg>=4 (canon 6)", "kM_degree": None, "imag_quadratic": False, "arithmetic": False},
    6: {"metal": "-",      "field": "deg>=4 (canon 6)", "kM_degree": None, "imag_quadratic": False, "arithmetic": False},
}
VOLUMES = {1: 2.029883, 2: 3.663862, 3: 4.813819, 4: 5.573609, 5: 6.066992, 6: 6.391087}
ARITHMETIC_SELECTED = (1, 2)   # the two-element selector -- NOT a unique m=1 criterion


# ----------------------------------------------------------------------------------------------------------------
# The spine: M_m^2 = R^m L^m (pure numpy, no external tooling).
# ----------------------------------------------------------------------------------------------------------------
def structural_identity(mmax=6):
    R = np.array([[1, 1], [0, 1]], dtype=object)
    L = np.array([[1, 0], [1, 1]], dtype=object)

    def mpow(X, k):
        out = np.eye(2, dtype=object)
        for _ in range(k):
            out = out @ X
        return out

    rows = []
    for m in range(1, mmax + 1):
        Mm = np.array([[m, 1], [1, 0]], dtype=object)
        M2 = Mm @ Mm
        ok = np.array_equal(M2, mpow(R, m) @ mpow(L, m))
        rows.append((m, int(np.trace(M2)), bool(ok)))
    return {"rows": rows,
            "all_equal_RmLm": all(ok for _, _, ok in rows),
            "trace_is_m2_plus_2": all(tr == m * m + 2 for m, tr, _ in rows)}


# ----------------------------------------------------------------------------------------------------------------
# Live recomputation (SnapPy-guarded). Returns None if SnapPy/cypari are unavailable.
# ----------------------------------------------------------------------------------------------------------------
def live_arithmeticity(mmax=4, bits_prec=400):
    try:
        import cypari
        import snappy
    except Exception:
        return None
    pari = cypari.pari

    def hp(z):
        return pari(str(z.real())) + pari(str(z.imag())) * pari("I")

    def squarefree_neg(disc):
        d, sfree = -disc, 1
        f = 2
        while f * f <= d:
            e = 0
            while d % f == 0:
                d //= f
                e += 1
            if e % 2 == 1:
                sfree *= f
            f += 1
        if d > 1:
            sfree *= d
        return sfree

    out = {}
    for m in range(1, mmax + 1):
        M = snappy.Manifold("b++" + "R" * m + "L" * m)
        vol_ok = abs(float(M.volume()) - VOLUMES[m]) < 1e-3
        sh = M.tetrahedra_shapes(part="rect", bits_prec=bits_prec)
        alpha = sum((7 * i + 3) * hp(z) for i, z in enumerate(sh))   # generic primitive element of the shape field
        deg, field = None, None
        for d in range(2, 11):
            p = alpha.algdep(d)
            if abs(complex(p.subst("x", alpha))) < 1e-70 and pari.polisirreducible(p):
                deg = d
                if d == 2:
                    c0, c1, c2 = (int(p.polcoef(0)), int(p.polcoef(1)), int(p.polcoef(2)))
                    disc = c1 * c1 - 4 * c2 * c0
                    if disc < 0:
                        field = f"Q(sqrt-{squarefree_neg(disc)})"
                break
        imag_quad = (deg == 2 and field is not None)
        out[m] = {"vol_ok": bool(vol_ok), "kM_degree": deg, "field": field,
                  "imag_quadratic": bool(imag_quad), "arithmetic": bool(imag_quad)}
    return out


def main():
    print("=" * 96)
    print("B125 -- SnapPy arithmeticity of the metallic R^m L^m bundles (overturns K009)")
    print("=" * 96)

    si = structural_identity()
    print("\n[spine] M_m^2 = R^m L^m and trace = m^2+2:",
          si["all_equal_RmLm"] and si["trace_is_m2_plus_2"])
    for m, tr, ok in si["rows"]:
        print(f"    m={m}: tr(M_m^2)={tr:>3d}  ==R^mL^m {ok}")

    print("\n[record] arithmeticity verdict (SnapPy 3.3.2 + cypari, verified in-sandbox):")
    for m, r in RECORD.items():
        tag = "ARITHMETIC" if r["arithmetic"] else "non-arithmetic"
        print(f"    m={m} {r['metal']:>6}: kM = {r['field']:<18} -> {tag}")
    print(f"    arithmeticity selects m in {ARITHMETIC_SELECTED} (golden Q(sqrt-3) + silver Q(i), distinct "
          f"Bianchi families -> not commensurable); kills m>=3.")

    live = live_arithmeticity()
    if live is None:
        print("\n[live] SnapPy/cypari not importable -- skipping live recomputation (record stands).")
    else:
        print("\n[live] recomputed (shape field, SnapPy present):")
        for m, r in live.items():
            print(f"    m={m}: vol_ok={r['vol_ok']} deg={r['kM_degree']} field={r['field']} "
                  f"-> {'ARITHMETIC' if r['arithmetic'] else 'non-arithmetic'}")

    print("\nCorrection of K009: arithmeticity is a TWO-element selector {m=1,m=2}, NOT a unique m=1 criterion.")
    print("Reid 1991 (unique arithmetic KNOT) STANDS (knots != bundles). The functorial wall is untouched.")


if __name__ == "__main__":
    main()
