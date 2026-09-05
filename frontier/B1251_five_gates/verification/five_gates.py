#!/usr/bin/env python3
"""B1251 -- FIVE INDEPENDENT PLACES, ONE GATE: the value question funnels into one unpriced
identification, and two of its five shapes need no measured value at all.

Four verified results from the 2026-09-05 session that would otherwise live only in scratchpad.

(1) HIER IS S3, AND B307'S OBSTRUCTION IS ABOUT C3 -- NO CONFLICT.
    B923's hierarchy cubic HIER = 953^4 x^3 - 2^8 3^9 13 421493 x^2 + 2^21 3^8 17 1129 x - 2^32 3^11
    is irreducible over Q with discriminant whose squarefree part is 77 = 7*11 (B918's registered
    disc kernel), hence NOT a square, hence Gal(HIER) = S3.  B307 proved no hyperbolic knot has a
    CYCLIC CUBIC (C3) invariant trace field.  The two arcs had never been cross-read: the
    hierarchy's three-ness is S3 and is NOT the three-ness B307 excludes.
    NOT CLAIMED: that HIER's roots ARE three generations -- that is I-13 and is UNPRICED.

(2) THE E6 CUBIC IS UNIFORMLY D2-ODD, WHICH FORCES B916'S OBSERVED TRANSPORT UNIFORMITY.
    The cubic invariant's support on the 27 is the 45 triples with w_i + w_j + w_k = 0.  Under the
    B1250 decode (D2 = the SO(10) grading) that support is EXACTLY 5 triples of type 1.10.10 and 40
    of type 10.16.16 -- the textbook E6 cubic under SO(10), with no 1.1.1 and no 16.16.16 -- and the
    D2 sign product is -1 on ALL 45.  B916 recorded `cubic_transport: proportional, ratio 1 on 45`
    as an observation; it is now FORCED, because both support types carry the same D2 parity.
    This supplies the grading fact B923's gap 1 needs for |T|^2 invariance under H+ -> H+ D2.
    SCOPE: the absolute sign differs between B916's convention (+1) and the raw triple product (-1);
    that convention is NOT pinned down here.  What both agree on, and what gap 1 needs, is
    UNIFORMITY across the support.  The 45 is also an independent re-derivation of B916's count.

(3) L154's "SIX UNITS" IS FREE: c((E6)_1) = 6 IS rank(E6).
    For simply-laced g at level 1 the WZW central charge is c = dim/(1+h^) = rank(g): A1 -> 1,
    A2 -> 2, D4 -> 4, E6 -> 6, E7 -> 7, E8 -> 8, while non-simply-laced F4 and G2 give 26/5 and 14/5.
    So c((E6)_1) = 6 carries no more information than "E6 has rank 6", which the chain already
    supplies.  L154's leverage therefore does NOT live in the three six-unit routes; it rests
    entirely on the relation c = 6*sigma and on the identification "the two sigmas are one".
    REDIRECTS the genuinely-missing item (3): price the sigma identification, do not derive the 6.

(4) THE CONVERGENCE.  A7 (the order), C22 (the closing), the listener map u, sin^2(theta_W)'s
    Y-anchoring, and L154's sigma are FIVE INDEPENDENT PLACES that each funnel into one unpriced
    identification.  Two of I-13's five shapes need NO measured value: DIMENSIONFUL instances are
    type errors decidable from the physics word alone (an object invariant is dimensionless), and
    COUNT instances are integer -> integer, a finite faithfulness check.  Neither is owner-gated.

NOT CLAIMED anywhere here: any physical value, any crossing, any derivation of Standard Model
matter. Gate 5 clean.
"""
import sympy as sp

x = sp.symbols('x')
HIER = (953**4 * x**3 - 2**8 * 3**9 * 13 * 421493 * x**2
        + 2**21 * 3**8 * 17 * 1129 * x - 2**32 * 3**11)

SIMPLY_LACED = {"A1": (3, 2, 1), "A2": (8, 3, 2), "D4": (28, 6, 4),
                "E6": (78, 12, 6), "E7": (133, 18, 7), "E8": (248, 30, 8)}
NON_SIMPLY_LACED = {"F4": (52, 9), "G2": (14, 4)}


def squarefree(n):
    n = int(n)
    if n == 0:
        return 0
    s, out = (1 if n > 0 else -1), 1
    for p, e in sp.factorint(abs(n)).items():
        if e % 2:
            out *= p
    return s * out


def hier_galois():
    """Return (irreducible, squarefree_disc, group)."""
    p = sp.Poly(HIER, x)
    disc = int(sp.discriminant(HIER, x))
    sf = squarefree(disc)
    grp = "C3" if sp.sqrt(sp.Integer(disc)).is_Integer else "S3"
    return p.is_irreducible, sf, grp


def level1_central_charges():
    """c = dim/(1+h^) at level 1; equals rank exactly for simply-laced."""
    out = {}
    for nm, (d, h, rk) in SIMPLY_LACED.items():
        out[nm] = (sp.Rational(d, 1 + h), rk)
    for nm, (d, h) in NON_SIMPLY_LACED.items():
        out[nm] = (sp.Rational(d, 1 + h), None)
    return out


def cubic_support_grading():
    """The 45 cubic triples, their D2 sign product, and their SO(10) block composition."""
    import collections
    import importlib.util
    import itertools
    import json
    import pathlib
    root = pathlib.Path(__file__).resolve().parents[3]
    wts = json.loads((root / "frontier" / "B883_the_27" / "rep27.json").read_text())["weights"]
    D2 = json.loads((root / "frontier" / "B916_lambda_bridge" / "results.json").read_text()
                    )["H_prime_diag_vs_H_plus"]["D2"]
    src = root / "frontier" / "B1250_d2_decode" / "verification" / "d2_decode.py"
    spec = importlib.util.spec_from_file_location("dd", src)
    dd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dd)
    _, _, blocks = dd.stabiliser_blocks()
    name = {}
    for b, n in zip(blocks, ["1", "10", "16"]):
        for i in b:
            name[i] = n
    trip = [(i, j, k) for i, j, k in itertools.combinations(range(27), 3)
            if all(a + b + c == 0 for a, b, c in zip(wts[i], wts[j], wts[k]))]
    signs = collections.Counter(D2[i] * D2[j] * D2[k] for i, j, k in trip)
    comp = collections.Counter(tuple(sorted((name[i], name[j], name[k]))) for i, j, k in trip)
    return len(trip), dict(signs), {"·".join(k): v for k, v in sorted(comp.items())}


def selftest(verbose=True):
    fails = []
    irr, sf, grp = hier_galois()
    if not irr:
        fails.append("HIER not irreducible over Q")
    if sf != 77:
        fails.append(f"HIER squarefree disc {sf} != 77 (B918's disc kernel {{7,11}})")
    if grp != "S3":
        fails.append(f"Gal(HIER) = {grp}, expected S3 (B307 forbids C3, so S3 means NO conflict)")

    cc = level1_central_charges()
    for nm, (c, rk) in cc.items():
        if rk is not None and c != rk:
            fails.append(f"{nm}: level-1 c = {c} != rank {rk}")
        if rk is None and c.is_Integer:
            fails.append(f"{nm} is non-simply-laced but gave integer c = {c}")
    if cc["E6"][0] != 6:
        fails.append("c((E6)_1) != 6")

    n, signs, comp = cubic_support_grading()
    if n != 45:
        fails.append(f"cubic support {n} triples != 45 (B916's count)")
    if signs != {-1: 45}:
        fails.append(f"D2 sign products {signs} not uniform on the support")
    if comp != {"1·10·10": 5, "10·16·16": 40}:
        fails.append(f"support composition {comp} != the standard E6 cubic under SO(10)")

    if verbose:
        print(f"  [HIER] irreducible {irr}, squarefree disc {sf}, Gal = {grp}  -> B307 forbids C3: NO CONFLICT")
        print(f"  [c=rk] level-1 central charges: " +
              ", ".join(f"{k} {v[0]}" for k, v in cc.items()) + "  -> c((E6)_1) = 6 = rank(E6)")
        print(f"  [cube] {n} triples; D2 signs {signs}; composition {comp}")
    return fails


if __name__ == "__main__":
    print("B1251 -- five gates (selftest)")
    f = selftest()
    print()
    print("SELFTEST:", "PASS" if not f else "FAIL")
    for i in f:
        print("   !", i)
    raise SystemExit(1 if f else 0)
