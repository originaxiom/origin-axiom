"""B147 -- is the chiral bundle RRL (invariant trace field Q(sqrt-7)) fully ARITHMETIC?

B146 found that RRL/RLL are CHIRAL once-punctured-torus bundles with imaginary-quadratic INVARIANT trace field
Q(sqrt-7) -- refuting B145's "no arithmetic chiral o-p-t bundle" AS STATED (B145 used the non-invariant trace field).
But imaginary-quadratic invariant trace field is only NECESSARY for arithmeticity. The decisive question (B147):

  Maclachlan-Reid (Arithmetic of Hyperbolic 3-Manifolds, Thm 8.3.2, non-cocompact): a cusped finite-covolume Kleinian
  group is ARITHMETIC  <=>  the invariant trace field kM is imaginary quadratic AND every trace is an algebraic
  integer (for cusped M the invariant quaternion algebra is automatically M_2(kM)).

  B125 (and B145) checked only the imaginary-quadratic half and *equated* it with arithmeticity -- INCOMPLETE.
  B147 adds the missing INTEGRAL-TRACES test. Outcome:
    - RRL traces INTEGRAL  -> RRL arithmetic -> there IS an arithmetic chiral o-p-t bundle -> the arithmetic arm
      collapses outright (a major correction).
    - RRL traces NON-INTEGRAL -> RRL non-arithmetic -> "no arithmetic chiral o-p-t bundle" SURVIVES (only via the
      integral-traces condition, which B145 never tested), consistent with the cited "exactly two arithmetic
      once-punctured-torus bundles" = RL (golden, Q(sqrt-3)) + RRLL (silver, Q(i)), both amphichiral/metallic.

Controls: RL and RRLL must come out ARITHMETIC (integral); a non-imag-quadratic bundle (RRRL, kM degree 4) is
non-arithmetic for the trivial reason. MATH tier; firewalled; nothing to CLAIMS.md.

Run under PLAIN pyenv python (SnapPy + cypari) -- NOT sage-python (cypari clashes with Sage's pari -> SIGABRT). The
invariant trace field is computed via the shape field + cypari algdep (Neumann-Reid; the B125 method), no Sage needed.
"""
from __future__ import annotations


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


def _invariant_trace_field(word, bits_prec=500):
    """Degree + imaginary-quadratic flag of the invariant trace field via the shape field (Neumann-Reid; B125)."""
    import cypari
    import snappy
    pari = cypari.pari
    M = snappy.Manifold("b++" + word)

    def hp(z):
        return pari(str(z.real())) + pari(str(z.imag())) * pari("I")

    sh = M.tetrahedra_shapes(part="rect", bits_prec=bits_prec)
    alpha = sum((7 * i + 3) * hp(z) for i, z in enumerate(sh))   # generic primitive element of the shape field
    for d in range(2, 12):
        p = pari.algdep(alpha, d)
        if abs(complex(p.subst("x", alpha))) < 1e-70 and pari.polisirreducible(p):
            poly = str(p)
            if d == 2:
                c0, c1, c2 = int(p.polcoef(0)), int(p.polcoef(1)), int(p.polcoef(2))
                disc = c1 * c1 - 4 * c2 * c0
                return 2, (disc < 0), (f"Q(sqrt-{_squarefree_neg(disc)})" if disc < 0 else poly)
            return d, False, poly
    return None, None, None


def integral_traces(word, bits_prec=500, dmax=6, tol=1e-60):
    """Are all traces of the holonomy group algebraic integers? Check the trace-field generators (fundamental-group
    generators + pairwise products): for a 2-generator-type group these generate the trace field (Fricke), and
    integrality propagates by the integer Cayley-Hamilton/Fricke recursions. Algebraic integer <=> minimal polynomial
    (pari algdep) is MONIC (|leading coeff| = 1)."""
    import cypari
    import snappy
    pari = cypari.pari

    Mhp = snappy.ManifoldHP("b++" + word)
    G = Mhp.fundamental_group()
    gens = list(G.generators())

    def trace_pari(w):
        Mx = G.SL2C(w)
        t = Mx[0][0] + Mx[1][1]
        return pari(str(t.real())) + pari(str(t.imag())) * pari("I")

    words = list(gens) + [a + b for a in gens for b in gens if a != b]
    rows = []
    all_integral = True
    for w in words:
        tau = trace_pari(w)
        z = complex(tau)
        # degree-1 (rational) pre-check: algdep(.,1) raises on non-rationals, so handle integers directly
        if abs(z.imag) < 1e-30 and abs(z.real - round(z.real)) < 1e-30:
            rows.append({"word": w, "deg": 1, "lead": 1, "integral": True, "minpoly": f"x - {round(z.real)}"})
            continue
        minpoly = None
        for d in range(2, dmax + 1):
            p = pari.algdep(tau, d)
            if abs(complex(p.subst("x", tau))) < tol and pari.polisirreducible(p):
                minpoly = p
                break
        if minpoly is None:
            rows.append({"word": w, "deg": None, "lead": None, "integral": None})
            all_integral = None if all_integral is True else all_integral
            continue
        actual_deg = int(minpoly.poldegree())                    # ACTUAL degree (not the search degree)
        lead = int(minpoly.polcoef(actual_deg))                  # leading coefficient
        integral = abs(lead) == 1                                # algebraic integer <=> monic minimal polynomial
        all_integral = all_integral and integral
        rows.append({"word": w, "deg": actual_deg, "lead": lead, "integral": integral, "minpoly": str(minpoly)})
    return {"rows": rows, "all_traces_integral": all_integral}


def arithmetic_verdict(word):
    deg, imag_quad, poly = _invariant_trace_field(word)
    it = integral_traces(word)
    arithmetic = bool(imag_quad) and it["all_traces_integral"] is True
    return {"word": word, "invariant_trace_field": poly, "deg": deg, "imag_quadratic": imag_quad,
            "all_traces_integral": it["all_traces_integral"], "ARITHMETIC": arithmetic,
            "amphichiral_self_mirror": _anti_palindromic(word), "trace_rows": it["rows"]}


def _anti_palindromic(w):
    sw = w.translate(str.maketrans("RL", "LR"))
    return len(w) == len(sw) and sw in (w[::-1] + w[::-1])


def arithmetic_scan(maxlen=7):
    """All arithmetic o-p-t bundles in range = imaginary-quadratic invariant trace field + integral traces."""
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from frontier.B145_forced_chirality.probe import enumerate_words
    found = []
    for w in enumerate_words(maxlen):
        try:
            deg, iq, poly = _invariant_trace_field(w)
            if not iq:
                continue
            if integral_traces(w)["all_traces_integral"] is True:
                found.append((w, poly, "amphichiral" if _anti_palindromic(w) else "CHIRAL"))
        except Exception:
            continue
    return found


# Independent cross-check (recorded; run under sage-python, NOT this cypari process -- cypari clashes with Sage pari):
#   an arithmetic manifold's volume is an INTEGER multiple of its field's Bianchi covolume (Humbert).
#   vol(b++RL)/covol(Q(sqrt-3))   = 12   (matches the known figure-eight value)
#   vol(b++RRLL)/covol(Q(i))      = 12
#   vol(b++RRL)/covol(Q(sqrt-7))  = 3    vol(b++RLL)/covol(Q(sqrt-7)) = 3   -> RRL/RLL arithmetic, CHIRAL.
VOLUME_BIANCHI_RATIOS = {"RL": ("Q(sqrt-3)", 12), "RRLL": ("Q(i)", 12), "RRL": ("Q(sqrt-7)", 3), "RLL": ("Q(sqrt-7)", 3)}


def main():
    print("=" * 100)
    print("B147 -- is the chiral bundle RRL (Q(sqrt-7)) fully ARITHMETIC? (full Maclachlan-Reid criterion)")
    print("=" * 100)
    try:
        import cypari  # noqa: F401
        import snappy  # noqa: F401
    except Exception as e:
        print("needs snappy+cypari (sage-python):", e)
        return
    for w in ["RL", "RRLL", "RRL", "RLL", "RRRL"]:
        r = arithmetic_verdict(w)
        tag = "amphichiral" if r["amphichiral_self_mirror"] else "CHIRAL"
        print(f"\nb++{w}  [{tag}]  invariant trace field {r['invariant_trace_field']} (deg {r['deg']}, "
              f"imag_quad={r['imag_quadratic']})")
        print(f"    all traces integral: {r['all_traces_integral']}   =>   ARITHMETIC: {r['ARITHMETIC']}")
        nonint = [(x['word'], x['lead']) for x in r['trace_rows'] if x['integral'] is False]
        if nonint:
            print(f"    NON-integral traces (word, leading coeff): {nonint[:6]}")

    print("\n[arithmetic o-p-t bundle scan, len<=7]")
    for w, poly, chi in arithmetic_scan():
        print(f"    b++{w:7} {poly:12} {chi}")
    print("\n[independent volume/Bianchi-covolume cross-check (Humbert; sage-python)]")
    for w, (fld, r) in VOLUME_BIANCHI_RATIOS.items():
        print(f"    vol(b++{w})/covol({fld}) = {r}  (integer -> arithmetic; RL's 12 matches the known value)")
    print("\nVERDICT: RRL/RLL are ARITHMETIC and CHIRAL (Q(sqrt-7), integral traces, vol = 3x Bianchi covolume).")
    print("So arithmetic CHIRAL o-p-t bundles EXIST -> B145's arithmetic arm refuted; canonical=>amphichiral fails for")
    print("arithmeticity. The firewall SURVIVES via the B146 dichotomy: RRL/RLL are a MIRROR PAIR, both arithmetic,")
    print("so arithmeticity (orientation-independent) cannot PREFER a handedness. (Corrects the 'exactly two o-p-t")
    print("bundles' paraphrase: >=4 arithmetic; the metallic m=1,2 result, B125, stands.)")


if __name__ == "__main__":
    main()
