#!/usr/bin/env python3
"""B739 Stage-B recompute — TOMB-L57 (the CS-crossover k~4 <-> n=4 Value-kill).

BANKED KILL (speculations/TOMBSTONES.md L57-61, verbatim core):
    "The hoped coincidence 'the Chern-Simons level crosses over near k~4, matching the
    rank n=4' is m-dependent -- k~2 at m=2, k~1 at m=3 -- so it is a figure-eight-volume
    coincidence, not structure. TESTED-NEGATIVE / DEAD."
The kill cites "Chat-1 seven-hints A4" (external chat; no script/artifact in-repo =>
fact_basis cited-unverified).  E19 discipline: the discriminating fact -- THE CROSSOVER
LEVEL IS m-DEPENDENT (k_c(2) != 4, k_c(3) != 4) -- must be RE-DERIVED as an actual
computation from the repo's own declared conventions.

DECLARED CONVENTIONS (E1 -- each sourced or, where the kill left it implicit, declared):
 C1. The metallic-family manifold at seed m is the once-punctured-torus bundle with
     monodromy R^m L^m, built as SnapPy 'b++' + 'R'*m + 'L'*m  (in-repo: B125 SS1,
     "the orientable metallic members ARE exactly the R^m L^m bundles"; m=1 == m004,
     the figure-eight complement, verified below).
 C2. At CS level k the quantum phases live on the lattice (2*pi/(k+2))*Z -- the repo's
     own adjacent kill line: "the rep is defined over q = exp(2*pi*i/(k+2)), so
     everything is roots of unity by construction" (TOMBSTONES.md, same block).
 C3. The geometric angle of seed m is theta_m = max over ideal-tetrahedron shapes of
     arg(z) for the geometric solution (for m=1 this is the banked z0 = e^{i*pi/3},
     B123/B125: "shape e^{i*pi/3}").  The kill never declared WHICH angle; 'max arg'
     is the declared choice -- it is the unique natural one that reproduces the kill's
     own m=1 anchor (k=4, via k+2 = 2*pi/(pi/3) = 6, the tombstone's explicit
     "k+2 = 6 = 2*3" phase-match) and is applied uniformly across m.
 C4. The crossover level is where the phase quantum equals the geometric angle:
     2*pi/(k_c+2) = theta_m  <=>  k_c(m) = 2*pi/theta_m - 2   (continuous), with the
     integer-lattice variant (smallest integer k>=1 with theta_m in (2*pi/(k+2))*Z)
     computed alongside.
 CROSS-CHECK. vol(M) = sum over tetrahedra of Lob(alpha)+Lob(beta)+Lob(gamma) (dihedral
     args of each shape; Lob = Lobachevsky = Cl_2(2x)/2) must match SnapPy's volume --
     this ties the ANGLE datum to the VOLUME datum, i.e. verifies the tombstone's
     "figure-eight-VOLUME coincidence" wording: theta_1 = pi/3 and vol(4_1) = 6*Lob(pi/3)
     are the same geometric fact.

Deterministic: fixed inputs, no wall-clock, no randomness, no network.
Environment: python 3.12.1, snappy 3.3.2 (ManifoldHP, quad-double), sympy 1.14, mpmath.
Gate 5: pure mathematics (levels, shapes, volumes); no SM quantities.
"""

import cmath
import math

import mpmath
import snappy
import sympy as sp

mpmath.mp.dps = 40

RANK_N = 4          # the claim side: the rank n=4 the k~4 match was read against
BANKED = {1: "k~4", 2: "k~2", 3: "k~1"}   # the banked (cited-unverified) values
TOL = 1e-12         # exactness tolerance at float64 level (HP shapes are far tighter)


def lob(theta):
    """Lobachevsky function Lob(theta) = Cl_2(2*theta)/2 (mpmath Clausen, exact series)."""
    return mpmath.re(mpmath.clsin(2, 2 * theta)) / 2


def exact_id(z, tol=TOL):
    """Identify a float shape with its exact value where the banked arcs claim one."""
    candidates = [
        (sp.Rational(1, 2) + sp.sqrt(3) / 2 * sp.I, "z0=(1+i*sqrt(3))/2=e^{i*pi/3}", "z^2-z+1 (Phi_6)"),
        (1 + sp.I, "1+i", "z^2-2z+2"),
        (sp.Rational(1, 2) + sp.I / 2, "(1+i)/2", "2z^2-2z+1"),
        (sp.I, "i", "z^2+1"),
    ]
    for val, name, poly in candidates:
        if abs(z - complex(sp.N(val, 20))) < tol:
            return name, poly
    return None, None


def main():
    print("=" * 78)
    print("TOMB-L57 recompute: is the CS-crossover level m-dependent?")
    print("k_c(m) = 2*pi/theta_m - 2,  theta_m = max ideal-tetrahedron shape arg (C1-C4)")
    print("=" * 78)

    # --- sanity: the m=1 bundle IS the figure-eight complement (B125's anchor) -------
    assert snappy.ManifoldHP("b++RL").is_isometric_to(snappy.ManifoldHP("m004")), \
        "b++RL is not m004 -- convention C1 broken"
    print("[sanity] b++RL isometric to m004 (figure-eight complement): OK")

    results = {}
    for m in (1, 2, 3):
        word = "b++" + "R" * m + "L" * m
        M = snappy.ManifoldHP(word)
        vol_snappy = float(M.volume())
        shapes = [complex(z) for z in M.tetrahedra_shapes("rect")]
        args = [cmath.phase(z) for z in shapes]
        assert all(a > 0 for a in args), "non-geometric solution (Im z <= 0)"

        # Lobachevsky volume cross-check (ties the angle datum to the volume datum)
        vol_lob = mpmath.mpf(0)
        for z in shapes:
            a = cmath.phase(z)
            b = cmath.phase(1 / (1 - z))
            c = math.pi - a - b
            vol_lob += lob(a) + lob(b) + lob(c)
        vol_lob = float(vol_lob)
        assert abs(vol_lob - vol_snappy) < 1e-9, "Lobachevsky volume mismatch"

        theta = max(args)
        k_c = 2 * math.pi / theta - 2

        # exact identifications where banked (B123: m=1 shape; B125: m=2 field Q(i))
        print(f"\n--- m={m}  ({word}) ---")
        print(f"  volume(SnapPy HP) = {vol_snappy:.15f}")
        print(f"  volume(Lobachevsky sum) = {vol_lob:.15f}   [match < 1e-9: OK]")
        for z in shapes:
            name, poly = exact_id(z)
            tag = f"  = {name}  [{poly}]" if name else "  (non-quadratic field, numeric)"
            print(f"  shape {z.real:+.12f}{z.imag:+.12f}i  arg={cmath.phase(z):.12f}{tag}")

        # exact theta / k_c statements for the arithmetic members
        if m == 1:
            assert abs(theta - math.pi / 3) < TOL
            theta_exact, kc_exact = "pi/3", sp.Integer(4)
        elif m == 2:
            assert abs(theta - math.pi / 2) < TOL
            theta_exact, kc_exact = "pi/2", sp.Integer(2)
        else:
            theta_exact, kc_exact = None, None

        # integer-lattice variant: smallest k >= 1 with theta_m in (2*pi/(k+2))*Z
        k_lattice = None
        for k in range(1, 1001):
            j = theta * (k + 2) / (2 * math.pi)
            if abs(j - round(j)) < 1e-9 and round(j) >= 1:
                k_lattice = k
                break

        print(f"  theta_m (max arg) = {theta:.12f}" + (f"  = {theta_exact} EXACTLY" if theta_exact else ""))
        print(f"  k_c(m) = 2*pi/theta - 2 = {k_c:.12f}" + (f"  = {kc_exact} EXACTLY" if kc_exact is not None else ""))
        print(f"  lattice variant: smallest integer k with theta in (2*pi/(k+2))*Z: "
              + (str(k_lattice) if k_lattice else "none for k <= 1000 (theta/2*pi irrational)"))
        print(f"  banked value: {BANKED[m]}")
        results[m] = (theta, k_c, k_lattice, vol_snappy)

    # ------------------------------ the discriminating fact ------------------------------
    print("\n" + "=" * 78)
    print("DISCRIMINATING FACT (recomputed, not cited):")
    print("=" * 78)
    kcs = {m: results[m][1] for m in results}
    print(f"  k_c(1) = {kcs[1]:.6f}   (banked k~4;  = rank n={RANK_N} -- the claimed match)")
    print(f"  k_c(2) = {kcs[2]:.6f}   (banked k~2;  reproduced EXACTLY)")
    print(f"  k_c(3) = {kcs[3]:.6f}   (banked k~1;  recomputes to 1.7645 -- floor 1;")
    print( "                            value drift noted, still != 4)")
    m_dependent = not (abs(kcs[2] - kcs[1]) < 0.5 and abs(kcs[3] - kcs[1]) < 0.5)
    match_only_at_m1 = (abs(kcs[1] - RANK_N) < 0.5
                        and abs(kcs[2] - RANK_N) > 0.5
                        and abs(kcs[3] - RANK_N) > 0.5)
    print(f"\n  m-dependent (k_c not constant across m)?          {m_dependent}")
    print(f"  k_c = n = 4 holds at m=1 ONLY?                     {match_only_at_m1}")
    print( "  the m=1 anchor is the 6th-root-of-unity shape z0 (k_c+2 = 2*pi/(pi/3) = 6),")
    print(f"  the SAME datum as vol(4_1) = 6*Lob(pi/3) = {6 * float(lob(math.pi / 3)):.9f}")
    print( "  -- i.e. a figure-eight-GEOMETRY (volume) accident, exactly as banked.")

    verdict = "RECONFIRMED" if (m_dependent and match_only_at_m1) else "REVIVED"
    print(f"\nVERDICT: {verdict} -- the banked kill "
          + ("stands: the crossover level is m-dependent; k~4 <-> n=4 is not structure."
             if verdict == "RECONFIRMED" else "fails under recompute."))


if __name__ == "__main__":
    main()
