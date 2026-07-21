#!/usr/bin/env python3
"""
B739 Stage-B recompute — TOMB-L74 (tombstone bullet, speculations/TOMBSTONES.md:L74-76)

Banked kill (verbatim):
  "**`z0` / k=4 phase match** = a **k=4-specific arithmetic coincidence**: at `k=4`,
   `k+2=6=2*3` divides the argument so phases are multiples of `pi/3 = arg(z0)`; at all
   other `k` they are multiples of `pi/(k+2)!=pi/3`."

Citation topology (one hop, verified by inspection during this recompute):
  - z0 is the repo's declared figure-eight-complement regular ideal-triangulation shape,
    "the **6th cyclotomic** root `z0 = e^{i pi/3}`" (frontier/README.md:803; CLAIMS.md C10
    carries the seam identity 1 - z0 = conj(z0)).  Recomputed here from the census
    triangulation, not cited.
  - The arc's own phase-lattice convention is in-text, two bullets up (TOMBSTONES.md:L70-71):
    "the rep is defined over `q=exp(2 pi i/(k+2))`, so everything is roots of unity by
    construction"; the L74 bullet itself uses the half-lattice "multiples of `pi/(k+2)`".
  - The figure-eight monodromy convention is [[2,1],[1,1]] (frontier/README.md:353,398).
  - No computation for this bullet exists in the arc (Stage-A fact_basis: asserted;
    faces_consulted: none-arithmetic-only), so the lattice arithmetic below IS the kill.

THE DISCRIMINATING FACT (the fact that, if true, kills the claim "the z0/k=4 phase
match is structure"):
  membership of arg(z0) in the level-k phase lattice is decided by a divisibility
  condition on k+2 ALONE — it consumes no input from the figure-eight beyond
  arg(z0) = pi/3, i.e. beyond z0 being a primitive 6th root of unity.  At k=4 the
  condition holds because 3 | 6 (and indeed q(k=4) = exp(2 pi i/6) = z0 exactly).
  If true, the "match" is cyclotomic bookkeeping, not structure -> kill upheld.
  E19 both directions: the bullet's universally quantified clause "at all other k they
  are multiples of pi/(k+2) != pi/3" is ALSO recomputed (counterexample search), since
  Stage A flagged it as incomplete (k=1 gives k+2=3, also pi/3 multiples).

DECLARED CONVENTIONS (E1):
  C1 (repo): z0 = the geometric (Im > 0) tetrahedron shape of the SnapPea census
     figure-eight complement 4_1, recomputed at 212 bits via snappy 3.3.2, then
     identified exactly by its minimal polynomial z^2 - z + 1 = 0 (sympy).
  C2 (arc, in-text): level-k phases lie on a cyclotomic lattice tied to
     q = exp(2 pi i/(k+2)).  "Phases" is otherwise undeclared in the arc, so
     membership of arg(z0) is tested in the three faithful formulations:
       (i)   fundamental-phase identity:  2 pi/(k+2)  =  pi/3   (equivalently q = z0),
       (ii)  coarse q-lattice:            pi/3 in (2 pi/(k+2)) * Z,
       (iii) the bullet's written lattice: pi/3 in (pi/(k+2)) * Z.
     All membership tests are exact (sympy Rational; no floats).
  C3 (E1 choice, robustness layer ONLY — the arc never fixed the operator): the
     SU(2)_k Reshetikhin–Turaev SL(2,Z) representation,
       S_ab = sqrt(2/(k+2)) sin(pi (a+1)(b+1)/(k+2)),      a,b = 0..k,
       T    = diag(exp(2 pi i (h_a - c/24))),  h_a = a(a+2)/(4(k+2)),  c = 3k/(k+2)
     (the c/24-corrected T makes it a genuine linear rep: S^2 = I, (ST)^3 = I for
     SU(2)_k where charge conjugation C = I; both relations are verified numerically
     below before use).  Fig-8 monodromy word: [[2,1],[1,1]] = T (S T^-1 S^-1),
     verified on integer matrices.  Eigenphases at mpmath dps = 50, k = 1..12.
     The verdict rests on C1 + C2; C3 is reported as-is.

Deterministic: no wall-clock, no randomness, no network.
Environment: python 3.12.1, sympy 1.14.0, mpmath 1.3.0, snappy 3.3.2.
"""

from fractions import Fraction

import mpmath as mp
import sympy as sp

LINE = "-" * 78


# ----------------------------------------------------------------------------
# PART 1 — z0 recomputed from the census triangulation (compute, not cite)
# ----------------------------------------------------------------------------
def part1():
    print(LINE)
    print("PART 1 — z0 from the figure-eight census triangulation (snappy, 212 bits)")
    print(LINE)
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)  # plink/tkinter GUI warning only
        import snappy

    M = snappy.Manifold("4_1")
    shapes = M.tetrahedra_shapes("rect", bits_prec=212)
    sol_type = M.solution_type()
    print(f"manifold: 4_1   tetrahedra: {M.num_tetrahedra()}   solution type: {sol_type}")
    assert M.num_tetrahedra() == 2
    assert sol_type == "all tetrahedra positively oriented"  # geometric solution

    mp.mp.dps = 60
    zs = [mp.mpc(mp.mpf(str(s.real())), mp.mpf(str(s.imag()))) for s in shapes]
    for i, z in enumerate(zs):
        print(f"shape[{i}] = {mp.nstr(z, 40)}")
    # both tetrahedra share one shape
    assert abs(zs[0] - zs[1]) < mp.mpf("1e-40"), "tetrahedra shapes differ"
    z_num = zs[0]
    assert z_num.imag > 0  # geometric orientation (C1)

    # identify exactly: z^2 - z + 1 = 0
    residual = abs(z_num**2 - z_num + 1)
    print(f"|z^2 - z + 1| at the numerical shape = {mp.nstr(residual, 5)}")
    assert residual < mp.mpf("1e-40")

    z = sp.symbols("z")
    roots = sp.solve(z**2 - z + 1, z)
    z0 = next(r for r in roots if sp.im(r) > 0)
    z0 = sp.simplify(z0)
    arg_z0 = sp.simplify(sp.arg(z0))
    print(f"roots of z^2 - z + 1: {roots}")
    is_zeta6 = sp.simplify((z0 - sp.exp(sp.I * sp.pi / 3)).rewrite(sp.cos)) == 0
    print(f"z0 (Im > 0 root)    = {z0} = exp(i pi/3): {is_zeta6}")
    assert is_zeta6
    print(f"arg(z0)             = {arg_z0}   (exact)")
    assert sp.simplify(arg_z0 - sp.pi / 3) == 0
    # z0 is a primitive 6th root of unity
    assert sp.simplify(z0**6 - 1) == 0 and sp.simplify(z0**3 + 1) == 0
    print("z0^6 = 1, z0^3 = -1  -> z0 is a PRIMITIVE 6th root of unity (exact)")
    # seam identity (C10 cross-check, recomputed)
    assert sp.simplify(1 - z0 - sp.conjugate(z0)) == 0
    print("seam identity 1 - z0 = conj(z0): True (exact)")
    print("=> arg(z0) = pi/3, carried by z0 = zeta_6 and nothing else.")
    return sp.pi / 3


# ----------------------------------------------------------------------------
# PART 2 — exact lattice membership, three formulations, k = 1..1000
# ----------------------------------------------------------------------------
def part2():
    print()
    print(LINE)
    print("PART 2 — membership of arg(z0) = pi/3 in the level-k phase lattice (exact)")
    print(LINE)
    KMAX = 1000
    ks = range(1, KMAX + 1)

    # (i) fundamental-phase identity: 2 pi/(k+2) = pi/3  <=>  q(k) = z0
    match_i = [k for k in ks if sp.Rational(2, k + 2) == sp.Rational(1, 3)]
    # (ii) pi/3 in (2 pi/(k+2)) Z  <=>  (k+2)/6 in Z
    match_ii = [k for k in ks if sp.Rational(k + 2, 6).is_integer]
    # (iii) pi/3 in (pi/(k+2)) Z  <=>  (k+2)/3 in Z   [the bullet's written lattice]
    match_iii = [k for k in ks if sp.Rational(k + 2, 3).is_integer]

    # closed forms, verified by set equality over the whole range
    assert match_i == [4]
    assert match_ii == [k for k in ks if k % 6 == 4]
    assert match_iii == [k for k in ks if k % 3 == 1]

    print(f"(i)   2 pi/(k+2) = pi/3  (q = z0 exactly):   k in {match_i}   "
          f"(UNIQUE: k+2 = 6)")
    print(f"(ii)  pi/3 in (2 pi/(k+2))Z  <=>  6 | k+2  <=>  k ≡ 4 (mod 6): "
          f"first {match_ii[:6]}, count {len(match_ii)}/{KMAX}")
    print(f"(iii) pi/3 in (pi/(k+2))Z   <=>  3 | k+2  <=>  k ≡ 1 (mod 3): "
          f"first {match_iii[:6]}, count {len(match_iii)}/{KMAX}")
    print()
    print("k=4 instance (the bullet's own): k+2 = 6 = 2*3;  pi/3 = 1*(2 pi/6) = 2*(pi/6);")
    print("                                 q(4) = exp(2 pi i/6) = exp(i pi/3) = z0 exactly.")
    q4 = sp.exp(2 * sp.pi * sp.I / 6)
    assert sp.simplify(q4 - sp.exp(sp.I * sp.pi / 3)) == 0

    # E19 both directions: the universal clause "at all other k ... != pi/3"
    counterex = [k for k in match_iii if k != 4]
    print()
    print("Universal clause check ('at all other k they are multiples of pi/(k+2) != pi/3'):")
    print(f"  counterexamples on the bullet's own lattice (iii): {len(counterex)} of "
          f"{KMAX - 1} other k in 1..{KMAX};")
    for k in counterex[:3]:
        m = sp.Rational(k + 2, 3)
        print(f"    k = {k}:  pi/3 = {m} * (pi/{k + 2})   (exact)")
    print("  -> the clause is FALSE as written; the coincidence class is k ≡ 1 (mod 3),")
    print("     [resp. k ≡ 4 (mod 6) on the coarse q-lattice], not the singleton {4}.")
    print("     Uniqueness of k=4 survives only in formulation (i): q(k) = z0 itself.")

    # structural-content lemma: membership never consults the figure-eight
    print()
    print("Structure-content lemma (why the match is arithmetic, not structure):")
    print("  for ANY phase pi*p/q (gcd(p,q)=1), pi*p/q in (pi/(k+2))Z <=> q | k+2 —")
    print("  a divisibility condition on k+2 alone; the geometric object enters only")
    print("  through the reduced denominator q of its argument/pi.  Verified exactly:")
    for p, q in [(1, 3), (2, 3), (1, 4), (3, 5)]:
        pred = [k for k in range(1, 61) if (sp.Rational(p, q) * (k + 2)).is_integer]
        cong = [k for k in range(1, 61) if (k + 2) % q == 0]
        assert pred == cong
        print(f"    p/q = {p}/{q}: match set (k<=60) = {{k : {q} | k+2}} -> {pred[:5]}...  OK")
    print("  arg(z0)/pi = 1/3 -> q = 3 -> the z0 match set is k ≡ 1 (mod 3): the")
    print("  predicate uses ONLY that z0 is a primitive 6th root of unity (Part 1).")
    return match_i, match_ii, match_iii


# ----------------------------------------------------------------------------
# PART 3 — robustness layer (C3): SU(2)_k RT rep of the fig-8 monodromy
# ----------------------------------------------------------------------------
def part3():
    print()
    print(LINE)
    print("PART 3 — robustness (C3): SU(2)_k RT eigenphases of the fig-8 monodromy")
    print(LINE)
    mp.mp.dps = 50
    tol = mp.mpf("1e-40")

    # integer-matrix check of the SL(2,Z) word: [[2,1],[1,1]] = T * (S T^-1 S^-1)
    def mat2(a, b, c, d):
        return ((a, b), (c, d))

    def mul2(A, B):
        return ((A[0][0] * B[0][0] + A[0][1] * B[1][0],
                 A[0][0] * B[0][1] + A[0][1] * B[1][1]),
                (A[1][0] * B[0][0] + A[1][1] * B[1][0],
                 A[1][0] * B[0][1] + A[1][1] * B[1][1]))

    S2 = mat2(0, -1, 1, 0)
    T2 = mat2(1, 1, 0, 1)
    T2inv = mat2(1, -1, 0, 1)
    S2inv = mat2(0, 1, -1, 0)
    word = mul2(T2, mul2(S2, mul2(T2inv, S2inv)))
    print(f"SL(2,Z) word check: T*(S T^-1 S^-1) = {word}  == [[2,1],[1,1]]: "
          f"{word == mat2(2, 1, 1, 1)}")
    assert word == mat2(2, 1, 1, 1)

    print()
    print(" k  dim  S^2=I    (ST)^3=I   max||l|-1|   eigenphases/pi (exact rationals)"
          "     on pi/(k+2)Z?  +-pi/3 present?")
    match_set = []
    for k in range(1, 13):
        n = k + 1
        kk = k + 2
        S = mp.matrix(n, n)
        for a in range(n):
            for b in range(n):
                S[a, b] = mp.sqrt(mp.mpf(2) / kk) * mp.sin(mp.pi * (a + 1) * (b + 1) / kk)
        c = mp.mpf(3 * k) / kk
        T = mp.matrix(n, n)
        Tinv = mp.matrix(n, n)
        for a in range(n):
            h = mp.mpf(a * (a + 2)) / (4 * kk)
            th = 2 * mp.pi * (h - c / 24)
            T[a, a] = mp.exp(1j * th)
            Tinv[a, a] = mp.exp(-1j * th)
        I_n = mp.eye(n)
        rel_s2 = mp.mnorm(S * S - I_n, 1)
        ST = S * T
        rel_st3 = mp.mnorm(ST * ST * ST - I_n, 1)
        assert rel_s2 < tol and rel_st3 < tol, f"rep relations fail at k={k}"

        rho_M = T * S * Tinv * S  # S^-1 = S
        eigs = mp.eig(rho_M, left=False, right=False)
        unit_dev = max(abs(abs(l) - 1) for l in eigs)
        assert unit_dev < tol  # unitarity (the sibling L69 bullet's |lambda| = 1)

        rats = []
        for l in eigs:
            x = mp.arg(l) / mp.pi  # in (-1, 1]
            r = Fraction(float(x)).limit_denominator(10**4)
            assert abs(x - mp.mpf(r.numerator) / r.denominator) < tol, \
                f"eigenphase at k={k} not rational*pi with denom <= 1e4"
            rats.append(r)
        rats.sort()
        on_lattice = all((r * kk).denominator == 1 for r in rats)
        has_pi3 = any(abs(r) == Fraction(1, 3) for r in rats)
        if has_pi3:
            match_set.append(k)
        rstr = "[" + ", ".join(str(r) for r in rats) + "]"
        print(f" {k:2d}  {n:3d}  {mp.nstr(rel_s2, 2):>8}  {mp.nstr(rel_st3, 2):>8}   "
              f"{mp.nstr(unit_dev, 2):>9}   {rstr:<42}  {str(on_lattice):<12} {has_pi3}")

    print()
    print(f"k with an exact +-pi/3 eigenphase (C3 convention), k = 1..12: {match_set}")
    print(f"k ≡ 1 (mod 3) in 1..12 (the Part-2 lattice class):            "
          f"{[k for k in range(1, 13) if k % 3 == 1]}")
    print("(Reported as-is: C3 is one declared operator choice; the verdict rests on")
    print(" Part 1 + Part 2, which are convention-independent divisibility facts.)")
    return match_set


def main():
    print("B739 Stage-B recompute — TOMB-L74 ('z0 / k=4 phase match' tombstone)")
    print("Deterministic run: sympy exact arithmetic + mpmath dps 50/60 + snappy 212 bits")
    print()
    part1()
    part2()
    m3 = part3()
    print()
    print(LINE)
    print("VERDICT SUMMARY")
    print(LINE)
    print("RECONFIRMED. The discriminating fact recomputes TRUE: membership of")
    print("arg(z0) = pi/3 (recomputed: z0 = zeta_6 from the 4_1 gluing, |z^2-z+1| < 1e-40)")
    print("in the level-k phase lattice is pure divisibility on k+2 — 3 | k+2 on the")
    print("bullet's lattice pi/(k+2), 6 | k+2 on the q-lattice 2 pi/(k+2) — with no input")
    print("from the figure-eight beyond arg(z0)/pi = 1/3. At k=4: k+2 = 6, q(4) = z0")
    print("exactly (unique k). The match is cyclotomic bookkeeping; the kill of the")
    print("'structure' reading stands. CORRECTION carried with the reconfirmation: the")
    print("bullet's clause 'at all other k ... != pi/3' is FALSE as written — the")
    print("coincidence class is k ≡ 1 (mod 3) (334 of k <= 1000; k = 1, 7, 10, ...),")
    print("resp. k ≡ 4 (mod 6) on the q-lattice; k=4-uniqueness survives only as")
    print("q(k) = z0. A larger coincidence class makes the match LESS structural, not")
    print("more: nothing singles out k=4 = rank except formulation (i)'s tautology.")
    print("C3 side-observation (as-is): under the standard RT operator convention the")
    print(f"fig-8 monodromy at k=4 has NO +-pi/3 eigenphase (phases 0, +-pi/2, +-2pi/3;")
    print(f"+-pi/3 occurs at k = {m3}) — the literal eigenphase match is convention-")
    print("dependent and absent at k=4 itself, killing the 'structure' reading from a")
    print("second, independent direction.")


if __name__ == "__main__":
    main()
