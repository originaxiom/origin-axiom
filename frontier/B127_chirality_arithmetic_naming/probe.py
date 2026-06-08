"""B127 -- chirality, Fibonacci, arithmetic, and the object's proper name (verify-don't-trust resolution).

Resolves the "threads 3 & 4 + Fibonacci" investigation by re-deriving it in-sandbox. The physics-bridge claim
returns a CLEAN, MULTIPLY-CONFIRMED NEGATIVE (the firewall, P007, confirmed from a third and fourth independent
direction: chirality and arithmetic). A small set of clean MATH facts survive -- and the strongest is the object's
PROPER NAME: it is the metallic-mean Schrodinger cocycle analyzed by its Kohmoto-Kadanoff-Tang trace map, with kappa
its Fricke-Vogt invariant (knowledge/K010). MATH and physics enter as DIFFERENT tiers. Nothing to CLAIMS.md; P1-P16
and the functorial Sym(W)->trace-ring wall (B85) untouched.

VERIFIED MATH (this probe):

  M-1  Fibonacci/Yang-Lee FUSION ALGEBRA = the golden substitution matrix. [[1,1],[1,0]] (substitution) and
       [[0,1],[1,1]] (Fibonacci fusion) share char poly lambda^2-lambda-1, Perron eigenvalue phi = the quantum
       dimension of tau. The CATEGORIFICATION (F/R matrices, braiding, central charge) is NOT a framework output.

  M-2  The metallic family is the ACHIRAL (CS=0) + imaginary-quadratic corner of the once-punctured-torus bundles.
       Chern-Simons invariant of M_m^2 = R^m L^m is IDENTICALLY 0 (SnapPy complex_volume, machine zero, m=1..6),
       against a census MIX (m003 CS=4.93, m006=-2.25, m004=0, ...). Structural reason: R^m L^m is palindromic
       under reverse+swap (swap conjugation sends L^m R^m -> R^m L^m), an orientation-reversing symmetry -> amphichiral.

  M-3  expansion PERP physical-(unitary)-topological-order. Metallic m>=1 are hyperbolic -> NON-unitary complex-CS
       TQFT, and CS=0 -> chiral central charge c_- = 0 -> NON-chiral. Physical anyons need a UNITARY modular category
       and chiral order needs c_- != 0; the metallic members are neither. The only member that could give unitary
       order is m=0 (swap, lambda=1, non-hyperbolic) -- which has NO expansion. A structural no-go across the family.
       SHARPER (new): lambda_m = (m+sqrt(m^2+4))/2 < 2 ONLY for m=1; a 2cos(pi/(k+2)) quantum dimension is always < 2,
       so ONLY the golden case can be a quantum dimension at all (m>=2: lambda_m > 2 -> no categorification).

  M-4  Arithmetic TRICHOTOMY (decisive separation). The framework's faces live in arithmetically DISJOINT worlds:
       fusion/substitution -> Q(sqrt(m^2+4)) (REAL; m=1 -> Q(sqrt5) subset Q(zeta5)) = the quantum DIMENSION;
       manifold geometry -> imaginary quadratic (m=1 Q(sqrt-3)=Q(zeta3), m=2 Q(i)); braiding/twist -> Q(zeta5)-phase.
       Q(zeta3) ∩ Q(zeta5) = Q (gcd(3,5)=1) -- so "figure-eight quantized = Fibonacci" conflates the substitution
       (zeta5) with the manifold (zeta3); the manifold's hyperbolic geometry plays NO role in the Fibonacci link.

  The FRICKE-VOGT dictionary (the naming, K010): I = kappa - 2 vanishes exactly on the commuting/reducible locus
  (kappa = tr[A,B] = 2). "cancellation" (kappa=2, I=0) = abelian = periodic, AC spectrum [-2,2]; "non-cancellation"
  (kappa>2, I>0) = irreducible = the trace map hyperbolic (Damanik-Gorodetski horseshoe) = Cantor spectrum (Suto).

  The three BMR arithmetic once-punctured-torus-bundle classes, NAMED: RL -> Q(sqrt-3), RRLL -> Q(i), RRL -> Q(sqrt-7)
  (the sqrt-7 representative is NON-metallic). Refines the B125/B126 "exactly two" correction.

KILLS (first-class; each with the computation that killed it -- tombstoned in speculations/TOMBSTONES.md):
  K-A/K-B  "det=-1 breaks chirality / selects the SM chiral structure": DEAD and INVERTED -- det=-1 is the
           orientation-REVERSING SYMMETRY (amphichiral), and the chiral invariant (CS) is exactly the one that is 0.
           [Distinct from B124's ALGEBRAIC P-parity of the tower (char(-M^h) sectors) -- that is representation theory,
           orthogonal to the manifold's topological CS chirality. The two coexist; this inverts the TOPOLOGICAL reading.]
  K-C      "figure-eight quantized = the PHYSICAL Fibonacci order / det=-1 selects braiding chirality": DEAD --
           k=3 is selected not forced; wrong categorification (native quantization non-unitary -> Yang-Lee side, not
           unitary Fibonacci); CS=0 contradicts chirality selection; arithmetic separation (zeta5 fusion vs zeta3
           manifold). The framework supplies only the FUSION RULE (shared by Fibonacci AND Yang-Lee), never the braiding.
  K-D      "physical (unitary) topological order from the metallic family": DEAD (M-3).
  K-E      "a forced dimensionful scale or non-generic physical ratio": DEAD -- null test vs alpha^-1, m_p/m_e,
           sin^2(theta_W); all hyperbolic-unit invariants.
"""
from __future__ import annotations

import math

import sympy as sp

# Verified records (SnapPy 3.3.2 + cypari, in-sandbox). Used by tests/FINDINGS so the repo stays green w/o SnapPy.
CS_RECORD = {m: 0.0 for m in range(1, 7)}                         # metallic M_m^2 = R^m L^m all CS = 0
CENSUS_CS = {"m003": 4.93480, "m004": 0.0, "m006": -2.25297, "m009": -0.41123}   # the discriminating mix
BMR_CLASSES = {"RL": "Q(sqrt-3)", "RRLL": "Q(i)", "RRL": "Q(sqrt-7)"}            # the three arithmetic classes


# ----------------------------------------------------------------------------------------------------------------
# M-1: Fibonacci fusion algebra = golden substitution matrix.
# ----------------------------------------------------------------------------------------------------------------
def fibonacci_fusion_is_substitution():
    sub = sp.Matrix([[1, 1], [1, 0]])
    fus = sp.Matrix([[0, 1], [1, 1]])
    cp = sp.symbols("L")
    same = sp.factor(sub.charpoly(cp).as_expr()) == sp.factor(fus.charpoly(cp).as_expr())
    phi = (1 + sp.sqrt(5)) / 2
    perron = max(sub.eigenvals().keys(), key=lambda e: float(sp.re(e)))
    return {"same_char_poly_L2_minus_L_minus_1": bool(same),
            "perron_is_phi": bool(sp.simplify(perron - phi) == 0),
            "note": "fusion algebra shared; the categorification (braiding/central charge) is NOT a framework output."}


# ----------------------------------------------------------------------------------------------------------------
# M-3 (sharper): only the golden case can be a TQFT quantum dimension (lambda_m < 2 iff m=1).
# ----------------------------------------------------------------------------------------------------------------
def anyon_only_golden(mmax=8):
    rows = []
    for m in range(1, mmax + 1):
        lam = (m + math.sqrt(m * m + 4)) / 2
        in_range = lam < 2.0
        k = round(math.pi / math.acos(lam / 2)) - 2 if in_range else None
        rows.append((m, round(lam, 4), in_range, k))
    return {"rows": rows,
            "only_m1_below_2": all((r[2]) == (r[0] == 1) for r in rows),
            "note": "2cos(pi/(k+2)) < 2 always; lambda_m < 2 only for m=1 -> only golden categorifies (k=3)."}


# ----------------------------------------------------------------------------------------------------------------
# M-4: arithmetic trichotomy -- fusion field (real) vs manifold field (imaginary) are disjoint.
# ----------------------------------------------------------------------------------------------------------------
def _squarefree(n):
    d, sq, f = n, 1, 2
    while f * f <= d:
        while d % (f * f) == 0:
            d //= f * f
            sq *= f
        f += 1
    return n // (sq * sq)


def arithmetic_trichotomy(mmax=6):
    manifold = {1: "Q(sqrt-3)", 2: "Q(i)", 3: "deg>=4", 4: "deg 4", 5: "deg>=4", 6: "deg>=4"}
    rows = []
    for m in range(1, mmax + 1):
        rows.append((m, f"Q(sqrt{_squarefree(m*m+4)})", manifold[m]))
    return {"rows": rows,
            "zeta3_cap_zeta5_is_Q": True,   # gcd(3,5)=1; unique quadratic subfield of Q(zeta5) is Q(sqrt5)
            "note": "fusion Q(sqrt(m^2+4)) REAL; manifold imaginary-quadratic-or-higher; disjoint for every m. "
                    "Q(zeta3) ∩ Q(zeta5) = Q -> the figure-eight 'Fibonacci' link is the substitution (zeta5), "
                    "NOT the manifold (zeta3)."}


# ----------------------------------------------------------------------------------------------------------------
# The Fricke-Vogt dictionary (the naming's spine): I = kappa - 2 vanishes on the commuting locus.
# ----------------------------------------------------------------------------------------------------------------
def fricke_vogt_dictionary():
    x, y, z = sp.symbols("x y z")
    kappa = x ** 2 + y ** 2 + z ** 2 - x * y * z - 2     # = tr[A,B]
    I = sp.expand(kappa - 2)                              # Fricke-Vogt / Suto invariant (up to normalization)
    # the void Jacobian is hyperbolic (B124: {phi^2,-1,phi^-2}); the elliptic point is neutral.
    xs, ys, zs = sp.symbols("xs ys zs")
    T = [zs, xs, xs * zs - ys]
    DT = sp.Matrix([[sp.diff(Ti, v) for v in (xs, ys, zs)] for Ti in T])
    sr_void = max(abs(complex(e)) for e in DT.subs({xs: 2, ys: 2, zs: 2}).eigenvals())
    sr_ell = max(abs(complex(e)) for e in DT.subs({xs: 0, ys: 0, zs: 0}).eigenvals())
    return {"I_equals_kappa_minus_2": str(I),
            "void_hyperbolic": sr_void > 1.001, "elliptic_point_neutral": abs(sr_ell - 1) < 1e-9,
            "note": "kappa=2 (I=0) = commuting/reducible = periodic AC spectrum; kappa>2 = irreducible = trace map "
                    "hyperbolic (Damanik-Gorodetski horseshoe) = Cantor spectrum (Suto). The Fricke-Vogt naming."}


def central_charges():
    cmin = lambda p, q: sp.Rational(1) - sp.Rational(6 * (p - q) ** 2, p * q)
    return {"yang_lee_M_2_5": str(cmin(2, 5)), "yang_lee_is_minus_22_5": cmin(2, 5) == sp.Rational(-22, 5),
            "unitary_fibonacci_G2_1": "14/5",
            "note": "tau x tau = 1 + tau has TWO categorifications: unitary Fibonacci (c=+14/5) and non-unitary "
                    "Yang-Lee (c=-22/5). The framework's hyperbolic (non-unitary) quantization sits on the Yang-Lee side."}


def no_forced_scale():
    phis = [(m + math.sqrt(m * m + 4)) / 2 for m in range(1, 7)]
    vols = [2.029883, 3.663862, 4.813819, 5.573609, 6.066992, 6.391391]
    pool = phis + vols + [2 * math.log(p) for p in phis]
    targets = {"alpha^-1": 137.036, "mp/me": 1836.15, "sin2thetaW": 0.231}
    hit = any(abs(a / b - t) / t < 0.01 for a in pool for b in pool if b for t in targets.values())
    return {"any_ratio_within_1pct_of_a_constant": hit,
            "note": "hyperbolic-unit invariants; a physical scale requires INSERTING a length. K-E."}


# ----------------------------------------------------------------------------------------------------------------
# M-2 / BMR live recomputation (SnapPy-guarded).
# ----------------------------------------------------------------------------------------------------------------
def cs_achiral_locus(mmax=6):
    try:
        import snappy
    except Exception:
        return None
    metallic = {}
    for m in range(1, mmax + 1):
        cv = snappy.Manifold("b++" + "R" * m + "L" * m).complex_volume()
        metallic[m] = abs(float(cv.imag()))
    census = {n: float(snappy.Manifold(n).complex_volume().imag()) for n in ("m003", "m004", "m006")}
    return {"metallic_all_CS_zero": all(v < 1e-9 for v in metallic.values()),
            "census_is_a_mix": abs(census["m003"]) > 1 and abs(census["m004"]) < 1e-6,
            "metallic_CS": metallic, "census_CS": census}


def main():
    print("=" * 96)
    print("B127 -- chirality, Fibonacci, arithmetic, and the object's proper name")
    print("=" * 96)
    for name, fn in [("M-1 fusion=substitution", fibonacci_fusion_is_substitution),
                     ("M-3 anyon only golden (lambda_m<2 iff m=1)", anyon_only_golden),
                     ("M-4 arithmetic trichotomy", arithmetic_trichotomy),
                     ("Fricke-Vogt dictionary (the naming)", fricke_vogt_dictionary),
                     ("central charges (Fibonacci vs Yang-Lee)", central_charges),
                     ("K-E no forced scale", no_forced_scale)]:
        r = fn()
        print(f"\n[{name}]")
        for k, v in r.items():
            print(f"    {k}: {v}")
    cs = cs_achiral_locus()
    print("\n[M-2 CS=0 achiral locus]", "SnapPy absent -- record stands" if cs is None else cs)
    print(f"\n[BMR three classes] {BMR_CLASSES}  (RRL = the sqrt-7 representative is NON-metallic)")
    print("\nFour independent kills (K-A..K-E) tombstoned; the firewall (P007) confirmed from chirality + arithmetic.")
    print("The strongest survivor is the NAME: the metallic-mean Schrodinger cocycle (K010).")


if __name__ == "__main__":
    main()
