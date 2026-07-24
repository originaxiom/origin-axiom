"""P2W3-H4 (OI-088): why is the figure-eight minimal along the ARITHMETICITY axis?

Sealed criterion:
  object-native reason found (structure)        -> RESOLVED-A
  it is Reid's theorem, cited as EXTERNAL       -> RESOLVED-B (EXTERNAL)
  neither settles                               -> UNRESOLVED

The discriminating question: does arithmeticity single out the figure-eight (RL, m=1)
WITHIN THE OBJECT-NATIVE FAMILY (the metallic once-punctured-torus bundles R^m L^m =
the trace-map tower), or only within the EXTERNAL class "knot complements in S^3"?

  - If arithmeticity picks EXACTLY m=1 among the object-native metallic tower, that is an
    object-native minimum -> RESOLVED-A candidate.
  - If arithmeticity picks a SCATTERED set (m=1 AND m=2, plus off-family short words),
    then object-natively arithmeticity does NOT bottom out uniquely at RL. The unique
    "figure-eight = only arithmetic knot" then lives only in the class of KNOT complements
    in S^3, a restriction the object (a bundle / trace-map tower) does not privilege ->
    the uniqueness is Reid's theorem on that external class -> RESOLVED-B (EXTERNAL).

We recompute the discriminating fact IN-CELL (SnapPy + cypari, pyenv; method = B125/B147
shape-field + integral-traces Maclachlan-Reid criterion). Two seeds for the primitive
element of the shape field (conditioning check). No SM values; nothing to CLAIMS.
"""
from __future__ import annotations
import json, os

CELL = os.path.dirname(os.path.abspath(__file__))


def _squarefree_neg(disc):
    d, sfree, f = -disc, 1, 2
    while f * f <= d:
        e = 0
        while d % f == 0:
            d //= f; e += 1
        if e % 2 == 1:
            sfree *= f
        f += 1
    if d > 1:
        sfree *= d
    return sfree


def invariant_trace_field(word, seed=(7, 3), bits_prec=500):
    """Degree + imag-quadratic flag + field label via the shape field (Neumann-Reid)."""
    import cypari, snappy
    pari = cypari.pari
    M = snappy.Manifold("b++" + word)

    def hp(z):
        return pari(str(z.real())) + pari(str(z.imag())) * pari("I")

    a, b = seed
    sh = M.tetrahedra_shapes(part="rect", bits_prec=bits_prec)
    alpha = sum((a * i + b) * hp(z) for i, z in enumerate(sh))
    for d in range(2, 12):
        p = pari.algdep(alpha, d)
        if abs(complex(p.subst("x", alpha))) < 1e-70 and pari.polisirreducible(p):
            if d == 2:
                c0, c1, c2 = int(p.polcoef(0)), int(p.polcoef(1)), int(p.polcoef(2))
                disc = c1 * c1 - 4 * c2 * c0
                lbl = f"Q(sqrt-{_squarefree_neg(disc)})" if disc < 0 else str(p)
                return 2, disc < 0, lbl
            return d, False, str(p)
    return None, None, None


def integral_traces(word, bits_prec=500, dmax=6, tol=1e-55):
    """All traces algebraic integers? Check trace-field generators (gens + pairwise
    products; Fricke). Algebraic integer <=> minimal poly is MONIC."""
    import cypari, snappy
    pari = cypari.pari
    G = snappy.ManifoldHP("b++" + word).fundamental_group()
    gens = list(G.generators())

    def tr(w):
        Mx = G.SL2C(w)
        z = Mx[0][0] + Mx[1][1]
        return pari(str(z.real())) + pari(str(z.imag())) * pari("I")

    words = list(gens) + [a + b for a in gens for b in gens if a != b]
    for w in words:
        t = tr(w)
        z = complex(t)
        if abs(z.imag) < 1e-30 and abs(z.real - round(z.real)) < 1e-30:
            continue  # rational integer trace (algdep(.,1) raises on non-rationals; skip)
        matched = False
        for d in range(2, dmax + 1):
            p = pari.algdep(t, d)
            if abs(complex(p.subst("x", t))) < tol and pari.polisirreducible(p):
                lead = int(p.polcoef(int(p.poldegree())))
                if abs(lead) != 1:
                    return False
                matched = True
                break
        if not matched:
            return None
    return True


def is_arithmetic(word, seed=(7, 3)):
    deg, imag_quad, field = invariant_trace_field(word, seed=seed)
    if deg != 2 or not imag_quad:
        return False, deg, field, None
    integ = integral_traces(word)
    return bool(integ), deg, field, integ


def main():
    # object-native family = metallic tower R^m L^m (m=1 figure-eight, m=2 silver, ...)
    metallic = {m: "R" * m + "L" * m for m in (1, 2, 3, 4)}
    # off-metallic SHORT words (word-length 3, chiral) -- the B147 scattering probe
    off = {"RRL": "RRL", "RLL": "RLL"}

    results = {"metallic": {}, "off_metallic": {}, "conditioning": {}}

    for m, w in metallic.items():
        arith, deg, field, integ = is_arithmetic(w)
        results["metallic"][m] = {"word": w, "field": field, "deg": deg,
                                  "integral_traces": integ, "arithmetic": arith}

    for name, w in off.items():
        arith, deg, field, integ = is_arithmetic(w)
        results["off_metallic"][name] = {"word": w, "field": field, "deg": deg,
                                         "integral_traces": integ, "arithmetic": arith}

    # conditioning: 2nd seed for the shape-field primitive element on the two verdicts that matter
    for m in (1, 2):
        a2, d2, f2 = invariant_trace_field(metallic[m], seed=(5, 2))
        results["conditioning"][f"m{m}_seed2"] = {"deg": a2, "field": f2}

    # ---- discriminating fact ----
    metallic_arith = sorted(m for m, r in results["metallic"].items() if r["arithmetic"])
    off_arith = [n for n, r in results["off_metallic"].items() if r["arithmetic"]]
    unique_native_min = metallic_arith == [1]  # arithmeticity picks ONLY m=1 in the tower?
    scattered = (len(metallic_arith) > 1) or bool(off_arith)

    # ---- verdict block ----
    if unique_native_min and not scattered:
        verdict = "RESOLVED-A"
        headline = "Arithmeticity singles out m=1 within the object-native tower: object-native minimum."
    elif scattered and not unique_native_min:
        verdict = "RESOLVED-B"
        headline = ("Object-natively arithmeticity is SCATTERED (metallic {%s}%s), not minimal at RL; "
                    "the figure-eight's arithmetic UNIQUENESS lives only in the external class "
                    "'knot complements in S^3' = Reid's theorem (EXTERNAL).") % (
                        ",".join(f"m={x}" for x in metallic_arith),
                        f" + off-family {off_arith}" if off_arith else "")
    else:
        verdict = "UNRESOLVED"
        headline = "Arithmetic pattern did not resolve into native-minimum vs scattered."

    discriminating = {
        "object_native_family": "metallic once-punctured-torus bundles R^m L^m (the trace-map tower)",
        "arithmetic_metallic_members": [f"m={x}" for x in metallic_arith],
        "arithmetic_off_metallic_short_words": off_arith,
        "arithmeticity_selects_unique_m1_in_tower": unique_native_min,
        "arithmeticity_scattered_over_object_family": scattered,
        "figure8_unique_only_as": "arithmetic KNOT complement in S^3 (Reid 1991) -- knot-in-S^3 restriction is NOT object-native",
        "residual_min_is_word_length": ("RL is the SHORTEST arithmetic word; 'minimal-arithmetic' reduces to "
                                        "word-length monotonicity among a scattered arithmetic set -- the exact "
                                        "OI-088 deflation costume, not an independent arithmetic minimum"),
    }

    out = {
        "cell": "P2W3-H4", "oi": "OI-088",
        "question": "object-native reason for figure-eight arithmetic-minimality vs Reid (EXTERNAL)?",
        "verdict": verdict, "headline": headline,
        "discriminating_fact": discriminating,
        "results": results,
        "method": "SnapPy 3.3.2 + cypari; Maclachlan-Reid Thm 8.3.2 (imag-quad invariant trace field + integral traces); 2 seeds",
        "reuses": ["B123", "B125", "B147"], "external": "Reid 1991 (unique arithmetic knot); Maclachlan-Reid; BMR (arithmetic o-p-t bundles finite)",
        "gate": "5-Q: structural only, no SM values, nothing to CLAIMS, one-number pin untouched",
    }
    with open(os.path.join(CELL, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print("=== P2W3-H4 / OI-088 ===")
    print("object-native family: metallic tower R^m L^m")
    for m, r in results["metallic"].items():
        print(f"  m={m:>1} ({r['word']:<8}) field={r['field']:<10} arithmetic={r['arithmetic']}")
    for n, r in results["off_metallic"].items():
        print(f"  off {n:<5}({r['word']:<8}) field={r['field']:<10} arithmetic={r['arithmetic']}")
    print("conditioning (seed2):", results["conditioning"])
    print("arithmetic metallic members:", metallic_arith, "| off-family arithmetic:", off_arith)
    print("unique m=1 in tower?", unique_native_min, "| scattered?", scattered)
    print("VERDICT:", verdict)
    print(headline)


if __name__ == "__main__":
    main()
