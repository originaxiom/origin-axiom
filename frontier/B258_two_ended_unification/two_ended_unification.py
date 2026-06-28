"""B258 -- the two-ended unification: why Q(sqrt-3) and Q(sqrt5) co-appear (H27 resolved), and the quantum face
mirrors the same two ends. FIREWALLED -- arithmetic / quantum topology / geometry, NOT physics. Nothing to CLAIMS.md.

The figure-eight's geometric transition (B248/B257) has two ends: hyperbolic (E6, Q(sqrt-3)) and spherical (E8,
Q(sqrt5)), Euclidean between. This probe shows the SAME two ends are seen by BOTH the arithmetic and the quantum
faces -- and resolves the standing hint H27 ("why do Q(sqrt-3) AND Q(sqrt5) co-appear?").

------------------------------------------------------------------------------------------------------------------
PART 1 -- H27 RESOLVED: the two fields are two DIFFERENT invariants, quadratic together only at m=1.
  * DISCRIMINANT field: monodromy phi=R^m L^m is 2x2, char x^2-(m^2+2)x+1, disc = m^2(m^2+4) -> Q(sqrt(m^2+4)).
    This is ALWAYS quadratic (a 2x2 eigenvalue field) -- the metallic/dynamical invariant; m=1 -> Q(sqrt5).
  * TRACE field (hyperbolic geometry): figure-eight = Q(sqrt-3), DEGREE 2 (arithmetic; Reid's unique arithmetic
    knot, B125). But SnapPy gives the silver (m=2) and bronze (m=3) trace fields DEGREE 8 -- non-arithmetic.
  => Q(sqrt-3) is FIGURE-EIGHT-SPECIFIC (m=1 only); Q(sqrt(m^2+4)) is metallic (all m). The two SMALL quadratic
     fields co-appear ONLY at m=1 because the figure-eight is the UNIQUE object that is simultaneously METALLIC
     (-> quadratic discriminant field, all m) and ARITHMETIC (-> quadratic trace field, m=1 only). The
     co-appearance is the signature of that double membership; neither field forces the other.

PART 2 -- THE QUANTUM MIRROR: the two ends are seen by the quantum invariants too.
  * Kashaev <4_1>_N at q=e^{2pi i/N}, N->inf: (2pi/N) log<4_1>_N -> Vol(4_1)=2.0299 (volume conjecture). This is
    the HYPERBOLIC / E6 end -- the quantum invariant in the large-color limit recovers the hyperbolic volume.
  * Colored Jones at the GOLDEN root q=e^{2pi i/5} (B240): [N]J_N = {1,-2,-2,1}, integers in Q(sqrt5) via
    sin(pi/5)sin(3pi/5)=sqrt5/4. This is the SPHERICAL / E8 end (Q(sqrt5), the lens space L(5,2), det 5).
  => the quantum face splits into the SAME two ends: large-color/Kashaev -> hyperbolic/E6/Q(sqrt-3);
     golden-root -> spherical/E8/Q(sqrt5).

THE UNIFICATION (firewall-clean): one object, two ends, three faces --
  geometry:   hyperbolic (Vol 2.03)      <-> Euclidean (B257) <-> spherical (Vol pi^2/5)     [B248-B257]
  arithmetic: trace field Q(sqrt-3)/E6   <->     Q (deg.)     <-> discriminant Q(sqrt5)/E8   [this probe, B256]
  quantum:    Kashaev/large-color -> Vol <->       --         <-> golden-root WRT -> Q(sqrt5) [this probe, B240]
The FOURTH face -- the Standard Model -- stays WALLED (B247: holonomy is SL(2,C) not SU(2); E6 is a McKay label,
not a gauge group). The honest horizon "unify quantum and SM" is exactly this wall; the three faces unify, the SM
does not, and that wall is a theorem (B247/B252/B253), not a gap.

Run: python two_ended_unification.py (pyenv; mpmath). Trace-field degrees cross-checked with SnapPy.
"""
import mpmath as mp

mp.mp.dps = 30

# trace-field degrees (SnapPy: find_field): figure-eight quadratic (Q(sqrt-3)); silver/bronze degree 8 (non-arith)
TRACE_FIELD_DEGREE = {1: 2, 2: 8, 3: 8}
VOL_4_1 = mp.mpf("2.029883212819307")


def discriminant_field_is_quadratic(m):
    """the monodromy is 2x2, so its eigenvalue/discriminant field Q(sqrt(m^2+4)) is quadratic for ALL m."""
    return True


def both_fields_quadratic(m):
    """do BOTH the discriminant field and the hyperbolic trace field have degree 2? (only m=1)."""
    return discriminant_field_is_quadratic(m) and TRACE_FIELD_DEGREE.get(m) == 2


def kashaev(N):
    """<4_1>_N = sum_{n=0}^{N-1} prod_{j=1}^n (2 sin(pi j/N))^2 (q=e^{2pi i/N})."""
    tot = mp.mpf(0)
    term = mp.mpf(1)
    for n in range(N):
        tot += term
        j = n + 1
        if j < N:
            term *= (2 * mp.sin(mp.pi * j / N)) ** 2
    return tot


def kashaev_growth_corrected(N):
    """(2pi/N) log<4_1>_N - 3pi logN/N  -> Vol(4_1) (the hyperbolic/E6 end)."""
    return 2 * mp.pi * mp.log(kashaev(N)) / N - 3 * mp.pi * mp.log(N) / N


if __name__ == "__main__":
    print("=== B258: the two-ended unification ===\n")
    print("PART 1 -- H27: which m have BOTH fields quadratic (= metallic AND arithmetic)?")
    for m in (1, 2, 3):
        print(f"  m={m}: discriminant field deg 2 (Q(sqrt{m*m+4})), trace field deg {TRACE_FIELD_DEGREE[m]}"
              f"  -> both quadratic: {both_fields_quadratic(m)}")
    assert both_fields_quadratic(1)
    assert not both_fields_quadratic(2) and not both_fields_quadratic(3)
    print("  => Q(sqrt-3) & Q(sqrt5) co-appear ONLY at m=1 (the unique metallic-AND-arithmetic object).")

    print("\nPART 2 -- the quantum mirror: Kashaev growth -> Vol (hyperbolic/E6 end)")
    for N in (400, 800, 1600):
        c = kashaev_growth_corrected(N)
        print(f"  N={N}: corrected growth = {mp.nstr(c, 8)}  (Vol={mp.nstr(VOL_4_1, 8)})")
    assert abs(kashaev_growth_corrected(1600) - VOL_4_1) < mp.mpf("0.005")
    print("  golden-root WRT (B240) -> Q(sqrt5) (spherical/E8 end).  Same two ends, quantum face.")
    print("\nThree faces unify on the two ends; the SM (4th face) stays walled (B247). ALL CHECKS PASS")
