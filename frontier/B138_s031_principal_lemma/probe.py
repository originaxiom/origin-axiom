"""B138 -- S031 push: the principal-image direction PROVED (all n); the SL(4) bulk obstruction; an object-clarification.

A "push further" on the S031 sealing capstone (the metallic SL(n) trace map fixes only the Sym^{n-1} image of its SL(2)
fixed point; the SL(n) fixed-point traces lie in the SL(2) trace field K_m). Two pieces and one honest obstruction:

  ============================================================================================================
  (1) THE PRINCIPAL-IMAGE DIRECTION -- PROVED (all n). The "easy half" of S031: the principal Sym^{n-1} image of
      an SL(2) rep defined over a field K is itself a trace-map fixed point with ALL traces in K.
      PROOF: the symmetric-power functor Sym^{d} is defined over Z -- the matrix entries of Sym^d(g) are integer
      polynomials in the entries of g (the action on degree-d monomials). Hence g in SL(2,K) => Sym^{n-1}(g) in
      SL(n,K), and every word-trace tr(W(Sym^{n-1}(A), Sym^{n-1}(B))) = tr(Sym^{n-1}(W(A,B))) lies in K. The metallic
      SL(2) fixed point lives over K_m (m=1: Q(sqrt-3); m=2: Q(i)), so its principal image is a K_m-sealed SL(n)
      fixed point, for every n. Verified n=2..5 for m=1 (Q(sqrt-3)) and m=2 (Q(i)) below.
      This proves the SYM-IMAGE COMPONENT always seals; the open hard half is that NOTHING ELSE escapes K_m.

  (2) THE SL(4) BULK OBSTRUCTION (honest negative). The B137-style off-sublocus root-find -- find SL(4) trace-map
      fixed points tcoords(A,B)=tcoords(A^m B, A) and test escape from K_m -- is INTRACTABLE in-session: a faithful
      separating residual (word-traces over {A,B,A^-1,B^-1} up to length 4 = 340 words) makes least_squares too slow
      to converge across enough starts (timed out > 20 min); a lighter residual UNDER-PINS the SL(4) character
      (matching too few traces converges to spurious points), so the irreducibility/escape classification is
      unreliable. SL(4) sealing evidence was NOT obtained. (Needs a proper complete SL(4) trace-coordinate set
      a la Lawton-for-SL(3), or a symbolic component analysis -- future work / NEEDS-EXPERTISE.)

  (3) OBJECT-CLARIFICATION (corrects an in-session mis-conflation; banked so it is not repeated). The S031
      "fixes only the Sym^{n-1} image" is about the DISCRETE fixed points of the trace-map automorphism
      phi_m(A,B)=(A^m B, A) (B129/B137: saddles, isolated; among them the only genuine irreducible one is the
      Sym^{n-1} image). This is NOT contradicted by B71's V0/W1/W2 (the SL(3) figure-eight GEOMETRIC character
      variety has 3 positive-dimensional components) -- those are components of the BUNDLE character variety, a
      DIFFERENT object. A generic point on a positive-dim geometric component (e.g. df.realize_bundle_rep) has
      continuously-varying traces (no single number field), so it is NOT a B137-style discrete fixed point and must
      not be used to test K_m-sealing. (This is why the known-SL(4)-rep trace-field check returned 'OTHER'.)

S031 status after B138: principal-image direction proved (all n); SL(3) full sealing computationally verified
m=1 (B129), m=2 (B137); SL(n>=4) bulk + the all-n converse remain OPEN. MATH tier; nothing to CLAIMS.md; P1-P16,
B85, the merged B124-B137 untouched.
"""
from __future__ import annotations

import itertools

import sympy as sp


def sym_power(g, d):
    """Sym^d of a 2x2 matrix g (action on degree-d monomials x^{d-i} y^i). Defined over Z in the entries of g."""
    x, y = sp.symbols("x y")
    a, b, c, dd = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    X, Y = a * x + b * y, c * x + dd * y
    basis = [x ** (d - i) * y ** i for i in range(d + 1)]
    M = sp.zeros(d + 1, d + 1)
    for j, mon in enumerate(basis):
        poly = sp.Poly(sp.expand(mon.subs({x: X, y: Y}, simultaneous=True)), x, y)
        for i, b2 in enumerate(basis):
            M[i, j] = poly.coeff_monomial(b2)
    return M


def _in_field(z, field):
    z = sp.expand(sp.simplify(z))
    re, im = sp.re(z), sp.im(z)
    if field == "Q(sqrt-3)":
        return bool(sp.simplify(re).is_rational and sp.simplify(im / sp.sqrt(3)).is_rational)
    if field == "Q(i)":
        return bool(sp.simplify(re).is_rational and sp.simplify(im).is_rational)
    raise ValueError(field)


def _metallic_sl2(m):
    """The metallic SL(2) fixed rep over K_m: m=1 figure-eight / Q(sqrt-3), m=2 silver / Q(i)."""
    w = sp.Rational(1, 2) + sp.sqrt(-3) / 2
    A = sp.Matrix([[1, 1], [0, 1]])
    if m == 1:
        return A, sp.Matrix([[1, 0], [-w, 1]]), "Q(sqrt-3)"
    if m == 2:
        return A, sp.Matrix([[1, 0], [-sp.I, 1]]), "Q(i)"
    raise ValueError("only m=1,2 (the arithmetic members) have a quadratic K_m")


def principal_image_seals(m, nmax=5, maxlen=3):
    """The principal Sym^{n-1} image of the metallic SL(2) rep has all word-traces in K_m, for n=2..nmax."""
    A2, B2, field = _metallic_sl2(m)
    rows = {}
    for d in range(1, nmax):                                       # SL(n), n = d+1
        A, B = sym_power(A2, d), sym_power(B2, d)
        wm = {"A": A, "B": B, "a": A.inv(), "b": B.inv()}
        ok = True
        for L in range(1, maxlen + 1):
            for t in itertools.product("ABab", repeat=L):
                M = sp.eye(d + 1)
                for ch in t:
                    M = M * wm[ch]
                if not _in_field(sp.simplify(M.trace()), field):
                    ok = False
        rows[d + 1] = {"det_A_is_1": bool(sp.simplify(A.det()) == 1), "all_traces_in_K": ok}
    return {"m": m, "field": field, "rows": rows, "sealed_all_n": all(r["all_traces_in_K"] for r in rows.values())}


def main():
    print("=" * 96)
    print("B138 -- S031: the principal-image direction PROVED (all n) + the SL(4) bulk obstruction")
    print("=" * 96)
    print("\n[principal-image lemma -- Sym^{n-1} of the metallic SL(2) rep seals in K_m]")
    for m in (1, 2):
        r = principal_image_seals(m)
        print(f"  {r['field']}: ", {n: rr["all_traces_in_K"] for n, rr in r["rows"].items()},
              " all-n sealed:", r["sealed_all_n"])
    print("\nPROVED: the Sym^{n-1} image always seals in K_m (Sym is Z-defined). The converse (nothing ELSE escapes)")
    print("is open; SL(3) verified m=1 (B129), m=2 (B137); the SL(4) bulk root-find is intractable in-session.")
    print("OBJECT NOTE: S031 is about DISCRETE trace-map fixed points (B129/B137), not B71's positive-dim geometric")
    print("components -- generic points on the latter have continuous traces and do NOT test K_m-sealing.")


if __name__ == "__main__":
    main()
