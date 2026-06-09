"""B140 -- compute-session reconciliation (verify-don't-trust the load-bearing items).

A Chat-2 compute session reconciled against the repo. Net effect: SUBTRACTIVE -- close one open lead, retract one
(never-banked) over-claim, tighten two framings, record two facts. NO new frontier claim. This probe re-derives the
load-bearing pieces in-sandbox before banking.

  ============================================================================================================
  ITEM 1 -- CLOSE B139-G: the chirality firewall is GENUS-GENERAL. The mirror M -> M-bar of any oriented
      hyperbolic 3-manifold has SAME volume, OPPOSITE Chern-Simons, CONJUGATE-isomorphic trace field (the general
      orientation-reversal theorem -- orientation reversal conjugates the complex volume). GENUS-INDEPENDENT.
      The genus-1 M -> M^T relabeling is a genus-1 MECHANISM; the CONCLUSION is general. Confirmed: genus-1
      bundles + chiral knots (vol same / CS opposite); a chiral GENUS-2 surface bundle exists. (The genus-2 CS
      NUMERIC is the one soft spot -- SnapPy complex_volume returns None on the twister triangulations; the
      genus-2 piece rests on the general theorem + the existence of the chiral genus-2 example.)

  ITEMS 2-3 -- REFRAME S031 + SHARPEN B138 (the crux: phi vs phi^2).
      The metallic incidence N=[[m,1],[1,0]] has det = -1 (orientation-reversing), and N^2 = R^m L^m (the bundle).
      So the SINGLE map phi_m (det -1) has ISOLATED/discrete fixed points (S031's object), while phi_m^2 (det +1,
      = the R^m L^m bundle monodromy) has a POSITIVE-DIMENSIONAL fixed locus (B71's geometric character variety).
      The genuine IRREDUCIBLE phi-fixed point is the RATIONAL Sym^{n-1} image of the SL(2) point (0,0,0):
          SL(2): phi-fixed = {(0,0,0) irreducible kappa=-2, (2,2,2) reducible}  (m=1);
                            {(0,0,0), (2,2,2), (-2,-2,2)} (m=2); unique irreducible (0,0,0), RATIONAL.
          SL(3): the unique irreducible phi-fixed point = Sym^2(0,0,0), trace coords (-1,-1,-1), commutator 3,
                 RATIONAL (even though the SL(2) rep realizing (0,0,0) is over Q(i)).
      So "sealed in K_m (=Q(sqrt-3) at m=1)" is LOOSE: K_m is the phi^2-GEOMETRIC-BUNDLE trace field; the actual
      phi-fixed content is Q (a tighter seal). B129's 0-escape conclusion STANDS (Q subset Q(sqrt-3)); only the
      framing tightens. S031's real content is RIGIDITY/UNIQUENESS of the principal fixed point, not field-sealing.
      RETRACTED (never banked): "~35 non-principal phi-fixed points carry Q(sqrt-3)" and "the converse routes to
      Heusener-Munoz-Porti" -- there are NO non-principal irreducible phi-fixed points (verified); the converse is
      a rigidity problem, not an HMP classification.

  ITEM 4 -- RECORD: [[m,1],[1,0]]^2 = R^m L^m (verified), so the geometric (phi^2) bundles ARE the R^m L^m
      once-punctured-torus bundles; the block sequence (m,m) is a cyclic palindrome => by B134/K011 every metallic
      bundle is amphichiral (figure-eight CS=0).

  ITEM 5 -- RECORD (do NOT conflate with S031): the phi^2-GEOMETRIC bundles' trace fields are m=1 -> Q(sqrt-3),
      m=2 -> Q(i) (imaginary quadratic -- the two arithmetic members), m>=3 -> higher-degree (structural, not a
      compute limit). This is the phi^2-bundle object, DISTINCT from S031's phi-fixed points.

MATH tier; firewalled; nothing to CLAIMS.md; P1-P16, B85, the merged B124-B139 untouched.
"""
from __future__ import annotations

import os
import sys

import sympy as sp

# reuse the Z-defined symmetric-power functor from B138 (add repo root to path for standalone runs)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from frontier.B138_s031_principal_lemma.probe import sym_power  # noqa: E402

I = sp.I
R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])


# ----------------------------------------------------------------------------------------------------------------
# ITEMS 3-4: the metallic-incidence facts (det = -1; N^2 = R^m L^m; tr N^2 = m^2+2).
# ----------------------------------------------------------------------------------------------------------------
def incidence(m):
    return sp.Matrix([[m, 1], [1, 0]])


def incidence_facts(mmax=4):
    rows = {}
    for m in range(1, mmax + 1):
        N = incidence(m)
        RmLm = (R ** m) * (L ** m)
        rows[m] = {
            "det_is_minus_1": bool(N.det() == -1),
            "N2_eq_RmLm": bool((N * N) == RmLm),
            "tr_N2_eq_m2_plus_2": bool(sp.trace(N * N) == m * m + 2),
        }
    return {"rows": rows,
            "all_det_minus1": all(r["det_is_minus_1"] for r in rows.values()),
            "all_N2_eq_RmLm": all(r["N2_eq_RmLm"] for r in rows.values()),
            "all_trN2": all(r["tr_N2_eq_m2_plus_2"] for r in rows.values())}


# ----------------------------------------------------------------------------------------------------------------
# ITEMS 2-3: the phi vs phi^2 fixed loci on the SL(2) trace surface (x,y,z) = (trA, trB, trAB).
# phi_m(A,B) = (A^m B, A). On trace coords (using tr(A^k B) recursions):
#   m=1: (x,y,z) -> (z, x, x*z - y)            [tr(AB)=z, trA=x, tr(A^2 B)=x z - y]
#   m=2: (x,y,z) -> (x*z - y, x, x*(x*z-y) - z)[tr(A^2 B)=x z - y, trA=x, tr(A^3 B)=x*tr(A^2B) - tr(AB)]
# ----------------------------------------------------------------------------------------------------------------
def kappa(x, y, z):
    """Fricke commutator trace tr[A,B] = x^2+y^2+z^2 - xyz - 2 (kappa=2 <=> reducible)."""
    return x * x + y * y + z * z - x * y * z - 2


def phi_map(m, x, y, z):
    if m == 1:
        return (z, x, x * z - y)
    if m == 2:
        t2 = x * z - y                     # tr(A^2 B)
        return (t2, x, x * t2 - z)         # (tr(A^2B), trA, tr(A^3B))
    raise ValueError("m in {1,2}")


def phi_fixed_sl2(m):
    x, y, z = sp.symbols("x y z", complex=True)
    fx, fy, fz = phi_map(m, x, y, z)
    sols = sp.solve([sp.Eq(fx, x), sp.Eq(fy, y), sp.Eq(fz, z)], [x, y, z], dict=True)
    pts = []
    for s in sols:
        p = (sp.nsimplify(s[x]), sp.nsimplify(s[y]), sp.nsimplify(s[z]))
        k = sp.simplify(kappa(*p))
        irred = bool(k != 2)
        rational = all(v.is_rational for v in p)
        pts.append({"pt": p, "kappa": k, "irreducible": irred, "rational": rational})
    irr = [p for p in pts if p["irreducible"]]
    return {"m": m, "points": pts,
            "unique_irreducible_is_000_rational":
                len(irr) == 1 and irr[0]["pt"] == (sp.Integer(0),) * 3 and irr[0]["rational"]}


def phi2_fixed_is_positive_dim(m=1):
    """phi_m^2 fixed locus on (x,y,z) is a CURVE (positive-dim) -- the geometric bundle character variety."""
    x, y, z = sp.symbols("x y z", complex=True)
    fx, fy, fz = phi_map(m, x, y, z)
    gx, gy, gz = phi_map(m, fx, fy, fz)                       # phi^2
    sols = sp.solve([sp.Eq(gx, x), sp.Eq(gy, y), sp.Eq(gz, z)], [x, y, z], dict=True)
    # a positive-dim component => at least one solution branch retains a free parameter
    free = any(any(len(sp.Matrix([s[v]]).free_symbols) > 0 for v in (x, y, z)) for s in sols) if sols else False
    return {"m": m, "n_branches": len(sols), "has_free_parameter_curve": free, "branches": sols}


# ----------------------------------------------------------------------------------------------------------------
# ITEM 2 (SL3): Sym^2 of the SL(2) point (0,0,0) has RATIONAL Lawton trace coordinates (-1,-1,-1), commutator 3.
# ----------------------------------------------------------------------------------------------------------------
def sym2_of_000_is_rational():
    A2 = sp.Matrix([[0, 1], [-1, 0]])          # trA = 0, det 1
    B2 = sp.Matrix([[0, I], [I, 0]])           # trB = 0, det 1, trAB = 0
    assert sp.trace(A2) == 0 and sp.trace(B2) == 0 and sp.trace(A2 * B2) == 0 and A2.det() == 1 and B2.det() == 1
    A, B = sym_power(A2, 2), sym_power(B2, 2)   # SL(3)
    tA, tB, tAB = sp.simplify(sp.trace(A)), sp.simplify(sp.trace(B)), sp.simplify(sp.trace(A * B))
    comm = sp.simplify(sp.trace(A * B * A.inv() * B.inv()))
    coords = (tA, tB, tAB)
    return {"trace_coords": coords, "commutator": comm,
            "coords_are_-1": tuple(coords) == (sp.Integer(-1),) * 3,
            "commutator_is_3": comm == 3,
            "all_rational": all(sp.nsimplify(c).is_rational for c in (tA, tB, tAB, comm))}


# ----------------------------------------------------------------------------------------------------------------
# ITEM 1 (SnapPy-gated): the genus-general mirror (vol same / CS opposite), + a chiral genus-2 bundle exists.
# ----------------------------------------------------------------------------------------------------------------
def mirror_word(word):
    return "".join("L" if c == "R" else "R" for c in word)[::-1]


def genus_general_live():
    try:
        import snappy
    except Exception:
        return None
    out = {"genus1_bundles": [], "knots": [], "genus2": None}
    ok = True
    for w in ["RRL", "RRRL", "RRLRL", "RRRLL"]:
        M = snappy.Manifold("b++" + w)
        Mm = snappy.Manifold("b++" + mirror_word(w))
        cv, cvm = M.complex_volume(), Mm.complex_volume()
        vol_eq = abs(float(cv.real()) - float(cvm.real())) < 1e-9
        cs_flip = abs(float(cv.imag()) + float(cvm.imag())) < 1e-9
        ok = ok and vol_eq and cs_flip
        out["genus1_bundles"].append({"word": w, "vol_eq": vol_eq, "cs_flip": cs_flip})
    for k in ["5_2", "6_1"]:
        M = snappy.Manifold(k)
        Mm = M.copy(); Mm.reverse_orientation()
        cv, cvm = M.complex_volume(), Mm.complex_volume()
        vol_eq = abs(float(cv.real()) - float(cvm.real())) < 1e-9
        cs_flip = abs(float(cv.imag()) + float(cvm.imag())) < 1e-9
        ok = ok and vol_eq and cs_flip
        out["knots"].append({"knot": k, "vol_eq": vol_eq, "cs_flip": cs_flip})
    # chiral genus-2 surface bundle via twister (existence + amphicheiral=False; CS numeric is the soft spot)
    try:
        import twister  # noqa: F401
        g2 = snappy.twister.Surface("S_2").bundle("a*B*c*d*E")
        sg = g2.symmetry_group()
        amph = sg.is_amphicheiral() if sg.is_full_group() else None
        try:
            cv = g2.complex_volume()
            cs_rendered = True
        except Exception:
            cs_rendered = False
        out["genus2"] = {"built": True, "is_amphicheiral": amph, "chiral": (amph is False),
                         "cs_numeric_rendered": cs_rendered}
    except Exception as e:
        out["genus2"] = {"built": False, "reason": str(e)[:80]}
    out["genus1_and_knots_vol_same_cs_opposite"] = ok
    return out


# ----------------------------------------------------------------------------------------------------------------
# ITEM 5 (SnapPy-gated): the phi^2-geometric bundles' trace fields (degree-2 test): m=1 Q(sqrt-3), m=2 Q(i), m>=3 not.
# ----------------------------------------------------------------------------------------------------------------
# The phi^2-geometric bundle trace fields are already banked: m=1 Q(sqrt-3) (B125/B129), m=2 Q(i) (B125), and
# S031 already records "m>=3 has non-quadratic K_m". The in-sandbox trace_field_gens needs Sage; recorded for ref.
BUNDLE_TRACE_FIELDS = {1: "Q(sqrt-3)  [B125/B129]", 2: "Q(i)  [B125]", 3: "non-quadratic (higher-degree)  [S031]"}


def bundle_trace_fields_live():
    try:
        import snappy
    except Exception:
        return None
    out = {}
    for m in (1, 2, 3):
        M = snappy.Manifold("b++" + "R" * m + "L" * m)
        try:
            tf = M.trace_field_gens().find_field(prec=200, degree=4, optimize=True)
            poly = None if tf is None else str(tf[0])
            deg = None if tf is None else tf[0].degree()
        except Exception as e:
            msg = str(e)
            poly = "needs Sage" if "Sage" in msg else f"err:{msg[:40]}"
            deg = None
        out[m] = {"min_poly": poly, "degree": deg, "banked": BUNDLE_TRACE_FIELDS[m]}
    return out


def main():
    print("=" * 100)
    print("B140 -- compute-session reconciliation (verify-don't-trust)")
    print("=" * 100)

    print("\n[Items 3-4: metallic incidence facts]")
    f = incidence_facts()
    for m, r in f["rows"].items():
        print(f"    m={m}: det=-1 {r['det_is_minus_1']}, N^2=R^mL^m {r['N2_eq_RmLm']}, tr N^2=m^2+2 {r['tr_N2_eq_m2_plus_2']}")
    print(f"    ALL: det-1 {f['all_det_minus1']}, N^2=R^mL^m {f['all_N2_eq_RmLm']}, trN^2 {f['all_trN2']}")

    print("\n[Items 2-3: phi-fixed SL(2) trace-coord loci -- unique irreducible (0,0,0), RATIONAL]")
    for m in (1, 2):
        r = phi_fixed_sl2(m)
        pts = [(tuple(p["pt"]), f"kappa={p['kappa']}", "irred" if p["irreducible"] else "red") for p in r["points"]]
        print(f"    m={m}: {pts}")
        print(f"           unique irreducible (0,0,0) & rational: {r['unique_irreducible_is_000_rational']}")
    p2 = phi2_fixed_is_positive_dim(1)
    print(f"    phi^2-fixed (m=1): {p2['n_branches']} branch(es), positive-dim curve: {p2['has_free_parameter_curve']}")

    print("\n[Item 2: SL(3) Sym^2(0,0,0) is RATIONAL]")
    s = sym2_of_000_is_rational()
    print(f"    trace coords {tuple(s['trace_coords'])}, commutator {s['commutator']}; "
          f"coords=(-1,-1,-1) {s['coords_are_-1']}, comm=3 {s['commutator_is_3']}, all rational {s['all_rational']}")

    print("\n[Item 1: genus-general mirror -- the orientation-reversal theorem is the load-bearing content]")
    print("    THEOREM (genus-independent, standard): for an oriented hyperbolic 3-manifold M, the mirror M-bar has")
    print("    SAME volume, OPPOSITE CS, conjugate-isomorphic trace field (orientation reversal conjugates cplx vol).")
    g = genus_general_live()
    if g is None:
        print("    SnapPy absent -- the theorem carries Item 1.")
    else:
        print(f"    confirmed genus-1 bundles + knots vol-same/CS-opposite: {g['genus1_and_knots_vol_same_cs_opposite']}")
        print(f"    genus-2 illustration: {g['genus2']}  (twister gating; illustration, NOT load-bearing -- theorem closes it)")

    print("\n[Item 5: phi^2-geometric bundle trace fields -- already banked (B125/B129); trace_field needs Sage]")
    b = bundle_trace_fields_live()
    if b is None:
        print(f"    SnapPy absent. Banked: {BUNDLE_TRACE_FIELDS}")
    else:
        for m, r in b.items():
            print(f"    m={m}: in-sandbox={r['min_poly']}  banked={r['banked']}")


if __name__ == "__main__":
    main()
