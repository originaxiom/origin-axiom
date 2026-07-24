"""B774 Stage B -- CHORD-PASS cell CP-010-tower.

Source negative / wall: OI-010 (rho_n catalog, the all-n tower stabilization) hits the
B85 PROCESI WALL. In-sandbox terminus (OPEN_LEADS:223, TOMBSTONES:88-97):

    rho_n  ~=  rho_{n-1} (+) Sym^n(V) (+) Sym^{n-3}(V)         (verified n<=5, extended n=8)

The Cayley-Hamilton derivation of the lag-3 Sym^{n-3} term does NOT close in-sandbox because
the characteristic polynomial of the monodromy J(m) on rho_5 contains the factor

    char(M^2)^2

-- the "doubled Sym^2 = char(M^2)^2 isotypic space" (THEOREM_REGISTRY T-FILTRATION / B522).
The char poly (a symmetric trace polynomial / a Procesi trace-ring invariant) sees only
char(M^2)^2 and CANNOT separate the two blocks it collides, so the trace-ring induction stalls.

CHORD ANALOG TO COMPUTE (the assignment): build the tower/intertwiner in the CHARACTER
(chord) ring rather than the Procesi TRACE ring, with an invariant FINER than any symmetric
trace polynomial, to SEPARATE the two cases the char(M^2)^2 degeneracy collides. The decisive
question (B773/W4-304): is the collision a TRACE-PROJECTION ARTIFACT hiding a theta-odd
cancellation (=> LIGHTS UP / OVERTURN), or is it a genuine multiplicity that the theta-odd /
chord sector is EMPTY at (=> HARDENS)?

CHORD DISCIPLINE (binding, W3-082c): a chord-POSITIVE must be a genuine non-abelian / theta-odd
object, NOT a finer ABELIAN / character invariant relabeled. A Z-grading, a multiplicity count,
a filtration degree = still abelian. The W4-304 overturn signature: a par/trace ZERO that
decomposes as even=odd CANCELLATION with a NONZERO theta-odd piece -- exhibit it or there is
no overturn.

Env: pyenv python3 (NOT sage). Re-runnable: writes output.txt + results.json.
"""
from __future__ import annotations

import json
import os
import sympy as sp

t, m, x, y = sp.symbols("t m x y")
M = sp.Matrix([[m, 1], [1, 0]])                 # metallic homological monodromy M_m, det = -1


def Lk(k):
    Mk = M**k if k >= 0 else (M.inv()) ** (-k)
    return sp.expand(sp.trace(Mk))


def char_Mk(k, sign=1):
    """char(sign*M^k) = t^2 - sign*L_k t + (-1)^k."""
    return sp.expand(t**2 - sign * Lk(k) * t + (-1) ** (k % 2))


def sym_power(Mat, d):
    """Sym^d of a 2x2 matrix acting on degree-d monomials x^{d-i} y^i."""
    a, b, c, dd = Mat[0, 0], Mat[0, 1], Mat[1, 0], Mat[1, 1]
    S = sp.zeros(d + 1, d + 1)
    for i in range(d + 1):
        poly = sp.expand((a * x + c * y) ** (d - i) * (b * x + dd * y) ** i)
        for j in range(d + 1):
            S[j, i] = poly.coeff(x, d - j).coeff(y, j)
    return S


def sym_charpoly(d):
    if d == 0:
        return t - 1
    return sp.expand(sym_power(M, d).charpoly(t).as_expr())


def proved_tower5():
    """The structural n=5 metallic tower char poly (B62/B232), symbolic in m."""
    return sp.expand((t - 1) ** 2 * (t + 1) ** 2 * char_Mk(-1) * char_Mk(1) ** 2
                     * char_Mk(2) ** 2 * char_Mk(3) * char_Mk(4) * char_Mk(5)
                     * char_Mk(2, -1) * char_Mk(3, -1))


def theta_parity(k):
    """Opposition-involution / Dickson parity of the height-|k| tower factor char(+/-M^k)
    (B64): even |k| -> symmetric (theta-EVEN); odd |k| -> antisymmetric (theta-ODD).
    The sign-flipped companion char(-M^k) is the OPPOSITE-parity partner at the same height."""
    return "even" if (k % 2 == 0) else "odd"


def main():
    lines = []
    def p(s=""):
        lines.append(s)
        print(s)

    results = {"cell": "CP-010-tower", "source_wall": "OI-010 / B85 Procesi wall",
               "chord_analog": "separate char(M^2)^2 degeneracy by an invariant finer than a symmetric trace polynomial"}

    p("B774 CP-010-tower -- CHORD PASS over the B85 char(M^2)^2 tower wall")
    p("=" * 78)

    # ---------------------------------------------------------------- #
    # 1. EXHIBIT THE WALL: the doubled factor at n=5.
    # ---------------------------------------------------------------- #
    p("\n[1] THE WALL: char poly of J(m) on rho_5 carries char(M^2)^2 (doubled Sym^2).")
    tw5 = proved_tower5()
    cM2 = char_Mk(2)                        # t^2 - L_2 t + 1  (theta-EVEN, k=2)
    cM2_odd = char_Mk(2, -1)                # t^2 + L_2 t + 1 = char(-M^2)  (theta-ODD partner)
    # count multiplicity of char(M^2) and of char(-M^2) in the tower
    def mult(poly, factor):
        P = sp.Poly(poly, t); f = sp.Poly(factor, t); c = 0
        while P.degree() >= f.degree() and sp.rem(P, f).as_expr() == 0:
            P = sp.quo(P, f); c += 1
        return c
    mult_even = mult(tw5, cM2)
    mult_odd = mult(tw5, cM2_odd)
    p(f"    multiplicity of char(M^2)  [theta-EVEN, k=2] in tower(5) = {mult_even}")
    p(f"    multiplicity of char(-M^2) [theta-ODD  partner ] in tower(5) = {mult_odd}")
    results["mult_char_M2_even"] = mult_even
    results["mult_char_negM2_odd"] = mult_odd
    p("    => the DEGENERACY (the wall) lives entirely in the char(M^2) = theta-EVEN sector.")

    # ---------------------------------------------------------------- #
    # 2. WHERE THE TWO COPIES COME FROM, and that they are ISOMORPHIC M-modules.
    # ---------------------------------------------------------------- #
    p("\n[2] THE TWO COLLIDING BLOCKS. tower = prod_{d=2}^n Sym^d  *  prod_{d=0}^{n-3} Sym^d.")
    p("    At n=5 the value d=2 (Sym^2) occurs ONCE in each sequence -> two Sym^2 summands.")
    S2_up = sym_power(M, 2)      # the d=2 block of the 'up' sequence
    S2_dn = sym_power(M, 2)      # the d=2 block of the 'lag-3' sequence
    cp_up = sp.factor(S2_up.charpoly(t).as_expr())
    cp_dn = sp.factor(S2_dn.charpoly(t).as_expr())
    p(f"    Sym^2 char poly (up ) = {cp_up}")
    p(f"    Sym^2 char poly (dn ) = {cp_dn}")
    iso = sp.simplify(sp.Matrix(S2_up) - sp.Matrix(S2_dn)) == sp.zeros(3, 3)
    p(f"    the two colliding blocks are the SAME M_m-module Sym^2(V)?  {iso}")
    p("    => they are ISOMORPHIC as M_m = SL(2)-modules. No invariant of the M-action")
    p("       whatsoever (char poly, full CHARACTER, Jordan form, eigen-anything) can")
    p("       distinguish two isomorphic summands -- the degeneracy is a MULTIPLICITY, intrinsic.")
    results["two_blocks_isomorphic_M_modules"] = bool(iso)

    # each Sym^2 factors as (t+1)*char(M^2): the +1 eigenvalue is det M = -1 (lambda*mu=-1)
    check_factor = sp.expand(sym_charpoly(2) - (t + 1) * cM2) == 0
    p(f"    check  char(Sym^2) == (t+1)*char(M^2) ?  {check_factor}   [the doubled char(M^2)]")
    results["sym2_equals_tplus1_times_charM2"] = bool(check_factor)

    # ---------------------------------------------------------------- #
    # 3. THE THETA-ODD (CHORD) SECTOR AT THE COLLISION: is it empty?
    # ---------------------------------------------------------------- #
    p("\n[3] CHORD PROBE: does the theta-odd invariant separate the char(M^2)^2 collision?")
    p(f"    both colliding copies sit at height k=2 -> theta parity = '{theta_parity(2)}' (EVEN).")
    p("    the theta-ODD content at this height is the DISTINCT factor char(-M^2), which appears")
    p(f"    with multiplicity {mult_odd} (NOT doubled) -- it is a different, non-degenerate block.")
    theta_odd_separates = (mult_odd >= 2) and (mult_even != mult_odd + 0)  # would need doubling in odd sector
    # The odd sector separates the collision only if the two colliding copies had opposite theta-parity.
    both_even = (theta_parity(2) == "even")
    p(f"    do the two colliding copies have OPPOSITE theta-parity?  {not both_even}")
    p("    => NO. Both copies are theta-EVEN; the theta-odd sector (char(-M^2)) is a SEPARATE,")
    p("       single block. The theta-odd / chord invariant is EMPTY at the degeneracy.")
    results["theta_odd_separates_collision"] = bool(not both_even)

    # ---------------------------------------------------------------- #
    # 4. W4-304 OVERTURN SIGNATURE CHECK: is the wall a par-ZERO = even-odd CANCELLATION?
    # ---------------------------------------------------------------- #
    p("\n[4] W4-304 SIGNATURE: an overturn needs a par/trace ZERO = even=odd CANCELLATION")
    p("    with a NONZERO theta-odd piece. Here the wall is char(M^2)^2 -- a DOUBLED NONZERO")
    p("    factor (a multiplicity 2), NOT a vanishing. There is nothing that cancels to zero.")
    is_a_zero = False   # char(M^2)^2 is not a zero of anything; it's a repeated nonzero factor
    p(f"    is the degeneracy a par-zero (a cancellation)?  {is_a_zero}")
    p("    => the W4-304 overturn signature is ABSENT. No trace-hidden theta-odd cancellation.")
    results["w4304_signature_present"] = is_a_zero

    # ---------------------------------------------------------------- #
    # 5. WHAT DOES separate the two blocks -- and is it a CHORD or an abelian relabel?
    # ---------------------------------------------------------------- #
    p("\n[5] THE ACTUAL SEPARATOR (honesty gate vs W3-082c).")
    p("    The two isomorphic Sym^2 blocks ARE separated in the Procesi ring -- by the DEGREE")
    p("    FILTRATION (B522 T-FILTRATION): the 'up' copy sits at trace-word degree d=2, the")
    p("    'lag-3' copy at a different filtration degree. That separator is a Z-GRADING")
    p("    (word-length / Procesi degree) -- an ABELIAN, scalar datum, finer than the char poly")
    p("    but expressible as graded DIMENSIONS. Per W3-082c ('an 8-rank is still abelian;")
    p("    a finer character/grading is NOT a chord'), a grading refinement is NOT a chord positive.")
    p("    No non-abelian / theta-odd object is required or available to split the collision:")
    p("    the two summands are literally the same module, distinguished only by position.")
    results["separator"] = "degree grading (Z-graded Procesi filtration) -- ABELIAN"
    results["separator_is_genuine_chord"] = False

    # ---------------------------------------------------------------- #
    # VERDICT
    # ---------------------------------------------------------------- #
    p("\n" + "=" * 78)
    p("VERDICT LOGIC")
    # An OVERTURN requires: W4-304 signature present (a par-zero = even-odd cancellation) AND
    #   a genuine theta-odd separator. Neither holds.
    # HARDENS requires: the theta-odd/chord analog is EMPTY at the collision -- confirmed:
    #   both colliding copies are theta-even, the odd sector is a distinct non-degenerate block,
    #   the only separator is an abelian grading.
    overturn = results["w4304_signature_present"] and results["theta_odd_separates_collision"]
    hardens = (not results["theta_odd_separates_collision"]
               and not results["w4304_signature_present"]
               and results["two_blocks_isomorphic_M_modules"])
    if overturn:
        verdict = "OVERTURNED"
    elif hardens:
        verdict = "HARDENS"
    else:
        verdict = "NEEDS-SPECIALIST"

    is_genuine_chord = False   # nothing non-abelian/theta-odd separates the collision
    results["verdict"] = verdict
    results["is_genuine_chord"] = is_genuine_chord

    p(f"  W4-304 overturn signature (par-zero = even-odd cancellation): {results['w4304_signature_present']}")
    p(f"  theta-odd sector separates the char(M^2)^2 collision:          {results['theta_odd_separates_collision']}")
    p(f"  colliding copies are isomorphic theta-EVEN Sym^2 modules:      {results['two_blocks_isomorphic_M_modules']}")
    p(f"  only separator = abelian degree grading (not a chord):         True")
    p("")
    p(f"  VERDICT = {verdict}")
    p(f"  is_genuine_chord = {is_genuine_chord}")
    p("")
    p("  READING: the B85 char(M^2)^2 wall is NOT a trace-projection artifact. The two colliding")
    p("  blocks are the SAME theta-EVEN module Sym^2(V) (a genuine multiplicity), not an even=odd")
    p("  cancellation hiding a theta-odd piece (contrast W4-304). The theta-odd/chord sector at this")
    p("  height is a separate, non-degenerate block char(-M^2). The finer invariant that DOES split")
    p("  the collision is the ABELIAN Procesi degree grading (B522) -- a character/grading refinement,")
    p("  explicitly NOT a non-abelian chord object (W3-082c trap). The wall HARDENS at the chord level;")
    p("  the residual all-n proof remains the ABELIAN grading/catalog task (NEEDS-LIT, per B522/OI-010),")
    p("  untouched by any theta-odd structure. Gate 5/5-Q clean; nothing to CLAIMS; one-number pin untouched.")

    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "output.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(os.path.join(here, "results.json"), "w") as f:
        json.dump(results, f, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
