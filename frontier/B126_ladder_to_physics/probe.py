"""B126 -- the ladder to physics: how far does the metallic object's rigidity propagate?

A foundational-question probe, run with a 5-agent literature fleet + direct computation. The guiding question
(synthesizing two exploration threads): the metallic object is maximally rigid at the CLASSICAL character-variety
level (Level 1) -- does that rigidity PROPAGATE up the ladder to physics (quantize -> 3d N=2 theory T[M] -> 4d ->
particle content), or does the determination DILUTE? Answer (literature-grounded + computed): it propagates EXACTLY
TWO FLOORS, provably, then hits a nameable wall. MATH/number-theory tier; the physics readings are firewalled
(speculations/S029, philosophy/P007, PHYSICS_BRIDGE_MAP). Nothing to CLAIMS.md; P1-P16 untouched; the functorial
Sym(W)->trace-ring wall (B85) is not touched.

WHAT IS COMPUTED IN-HOUSE (verify-don't-trust):

  (A) The homology torsion = the metallic parameter (the headline structural fact).
      H_1(M_m) = Z (+) (Z/m)^2  for the orientable metallic bundle M_m^2 = R^m L^m. PROVED by the Smith normal form
      of M_m^2 - I = m * M_m = [[m^2,m],[m,0]] (invariant factors (m,m)); confirmed by SnapPy for m=1..7. So the
      metallic m IS the order of the homology torsion -- structural, no free choices.

  (B) The arithmetic <=> A-polynomial-simplicity correlation (reproducing the A-poly thread).
      On the GEOMETRIC component of the bundle character variety (Fix of the monodromy trace map), the degree of the
      commutator coordinate kappa = tr[a,b] over Q(z) is [1,1,3,3,...] for m=1,2,3,4: kappa is RATIONAL in the
      parameter z exactly for the two ARITHMETIC members (m=1,2; B125), with a sharp jump at the arithmetic boundary
      m=2/3. This is a FAMILY-SPECIFIC observation, NOT a general law -- the literature has NO "arithmetic <=> simple
      A-polynomial" theorem (arithmetic manifolds routinely have complicated A-polynomials); the only literature link
      is Mahler-measure <-> Dedekind zeta (analytic size, not degree).

THE LADDER MAP (literature-grounded; see FINDINGS for citations). Rigidity propagates exactly two floors:
  - FLOOR 1 (arithmetic -> quantization): the invariant trace field determines the FIELD of the perturbative quantum
    series -- a THEOREM (Dimofte-Garoufalidis arXiv:1202.6268/1511.05628), PROVEN for our exact family (once-
    punctured-torus bundles, Yoon arXiv:2110.11003: 1-loop = adjoint torsion). [In-house confirmation of the adjoint
    torsion is Sage-gated in SnapPy; cited instead.]
  - FLOOR 2 (rigidity -> rigidity of T[M]): Mostow rigidity => T[M] has NO marginal couplings (no conformal
    manifold); and M selects the SUSY PHASE -- 4_1 has irreducible flat connections => unbroken SUSY, gapped vacua
    (Cho-Gang-Kim arXiv:2007.01532). The H_1 torsion (A) -> the one-form/center symmetry / line-operator spectrum of
    T[M] (DGG; Aharony-Seiberg-Tachikawa; arXiv:2511.13696). [The SU(m)/Standard-Model reading is FENCED: S029.]
  - THE WALL: 3d -> 4d (the 4d theory is data of the 2d BOUNDARY surface, not the 3-manifold M) + the SUSY-breaking
    SCALE (orthogonal input -- no manifold mechanism). Honest ceiling: N=4 SYM / N=2* (geometric Langlands,
    Kapustin-Witten). It does NOT reach chiral matter, generations, or the Standard Model.

So we lack no CONCEPT; we lack the one thing no 3-manifold can supply -- the 2d-boundary / decompactification data
that fixes the 4d theory, and the orthogonal SUSY-breaking input that fixes the scales.
"""
from __future__ import annotations

import sympy as sp

# ----------------------------------------------------------------------------------------------------------------
# (A) homology torsion = the metallic parameter (always runs; SNF). SnapPy cross-check is guarded.
# ----------------------------------------------------------------------------------------------------------------
def homology_torsion(mmax=7):
    """H_1(M_m) = Z (+) (Z/m)^2: coker(M_m^2 - I) = Z/m (+) Z/m by the Smith normal form of M_m^2 - I = m*M_m."""
    from sympy.matrices.normalforms import smith_normal_form
    rows = []
    for m in range(1, mmax + 1):
        Mm = sp.Matrix([[m, 1], [1, 0]])
        A = Mm * Mm - sp.eye(2)
        S = smith_normal_form(A, domain=sp.ZZ)
        inv = sorted(abs(S[i, i]) for i in range(2))
        rows.append((m, inv, A.tolist()))
    return {"rows": rows,
            "torsion_is_Zm_squared": all(inv == [m, m] for m, inv, _ in rows),
            "note": "H_1(M_m) = Z (+) Z/m (+) Z/m; the metallic m = the order of the homology torsion."}


def homology_torsion_snappy(mmax=7):
    """Live SnapPy cross-check of (A). Returns None if SnapPy is unavailable."""
    try:
        import snappy
    except Exception:
        return None
    out = {}
    for m in range(1, mmax + 1):
        M = snappy.Manifold("b++" + "R" * m + "L" * m)
        out[m] = str(M.homology())
    return out


# ----------------------------------------------------------------------------------------------------------------
# (B) arithmetic <=> A-poly simplicity: kappa-degree over Q(z) on the geometric component of Fix(monodromy).
#     Dehn-twist trace maps on Fricke coords (x,y,z)=(tr a, tr b, tr ab); both preserve kappa.
# ----------------------------------------------------------------------------------------------------------------
_x, _y, _z, _k = sp.symbols("x y z k")
_kap = _x ** 2 + _y ** 2 + _z ** 2 - _x * _y * _z - 2


def _Ta(p):
    X, Y, Z = p
    return (X, Z, X * Z - Y)


def _Tb(p):
    X, Y, Z = p
    return (Z, Y, Y * Z - X)


def _phi(m):
    def power(T, k):
        f = lambda p: p
        for _ in range(k):
            g = f
            f = (lambda gg: (lambda p: T(gg(p))))(g)
        return f
    fa, fb = power(_Ta, m), power(_Tb, m)
    return lambda p: fa(fb(p))


def kappa_degree(m):
    """Degree(s) in k of the z-k relation on Fix(phi_m*) after eliminating x,y -- i.e. deg of kappa over Q(z) on
    each component. The geometric component is the highest-degree factor; m=1,2 give {1} (kappa rational in z), m>=3
    acquire a degree-3 (geometric) component. Can be slow for m>=5."""
    Xp, Yp, Zp = _phi(m)((_x, _y, _z))
    eqs = [sp.expand(Xp - _x), sp.expand(Yp - _y), sp.expand(Zp - _z), sp.expand(_k - _kap)]
    G = sp.groebner(eqs, _x, _y, _z, _k, order="lex")
    elim = [g for g in G.exprs if (_x not in g.free_symbols) and (_y not in g.free_symbols)]
    degs = set()
    for e in elim:
        for f, _mult in sp.factor_list(e)[1]:
            if _k in f.free_symbols:
                degs.add(sp.Poly(f, _k).degree())
    return sorted(degs)


# the verified record (m=1..4 computed here; m=5,6 from the longer run, recorded). geometric-component degree =
# the max of each entry's degrees.
KAPPA_DEGREE_RECORD = {1: [1], 2: [1], 3: [1, 3], 4: [1, 3], 5: [1, 3, 7], 6: [1, 3, 6]}
ARITHMETIC = (1, 2)   # B125: the arithmetic members of the family -- exactly the kappa-rational ones


def main():
    print("=" * 96)
    print("B126 -- the ladder to physics: how far does the metallic rigidity propagate?")
    print("=" * 96)

    h = homology_torsion()
    print("\n[A] H_1(M_m) = Z (+) (Z/m)^2  (metallic m = order of homology torsion):",
          h["torsion_is_Zm_squared"])
    for m, inv, A in h["rows"]:
        print(f"    m={m}: M_m^2-I = {A}  SNF invariant factors {inv} -> Z (+) Z/{m} (+) Z/{m}")
    snap = homology_torsion_snappy()
    if snap:
        print("    SnapPy cross-check:", {m: snap[m] for m in (1, 2, 3)}, "...")

    print("\n[B] kappa-degree over Q(z) on Fix(monodromy) -- arithmetic (m=1,2) <=> kappa rational (degree 1):")
    for m in range(1, 5):
        d = kappa_degree(m)
        tag = "ARITHMETIC (kappa rational)" if max(d) == 1 else "non-arithmetic (geometric deg %d)" % max(d)
        print(f"    m={m}: kappa k-degrees {d}  -> {tag}")
    print(f"    (m=5,6 recorded: {KAPPA_DEGREE_RECORD[5]}, {KAPPA_DEGREE_RECORD[6]}; family-specific, NOT a general law)")

    print("\n[LADDER] rigidity propagates EXACTLY TWO FLOORS, then hits the wall:")
    print("    Floor 1 (arithmetic -> quantization field): THEOREM, proven for our family (Yoon 2110.11003).")
    print("    Floor 2 (Mostow -> no marginal couplings; M selects SUSY phase): 4_1 -> unbroken SUSY (CGK 2007.01532).")
    print("    WALL: 3d->4d = data of the 2d BOUNDARY, not M; SUSY-breaking scale = orthogonal. Ceiling: N=4 SYM/N=2*.")
    print("\n    => we lack no concept; we lack what no 3-manifold supplies (the 2d-boundary + the SUSY scale).")
    print("    Physics readings firewalled: S029 (H_1 torsion -> center symmetry), P007 (the reframe).")


if __name__ == "__main__":
    main()
