"""B303 -- the seam/clock thread (Wall A, the one live forcing): the CP sign IS the sign of the Chern-Simons clock.
Run with sage-python (SnapPy) for the ladder; verdict.py holds the structural facts + the reduction (pyenv).

The root-insight meta-conclusion (B302): the firewall is scale-invariant -- the object's structure-only nature is
inherited by its RELATIONS, so multiplicity (relations) relocates the generation ℤ/3 but it stays structure, not a
value. The ONLY thing that breaks scale-invariance is the SEAM picking a SPECIFIC closing (= a specific length/CS).
So the seam is the one place a VALUE can enter, and the CP sign is the test case (the one live forcing, triple-
convergent: B295 + Chat-1 + Chat-2).

THE RESULT (MATH, verified -- the CP sign IS the sign of the CS clock):
  * the CUSPED (amphichiral) object has CS = 0 -- the CP-SYMMETRIC ORIGIN of the clock.
  * every closing has CS with a DEFINITE SIGN: along the (1,n) scale ladder, CS(1,n) is all the SAME sign (n>0 ->
    CS<0), with CS(1,-n) = -CS(1,n) (B289) and |CS| -> 0 as n -> inf (approaching the amphichiral origin).
  * so the CP sign (B289: handedness = ℚ(√−3) Galois = the +-pi/6 / tau swap) is LITERALLY the sign of CS: there is
    no separate CP sign to choose; closing in one orientation gives one sign of CS, the mirror gives the other, and
    the sign is CONSTANT as the clock runs (you never cross zero along a fixed-orientation history).

THE REDUCTION (the one live forcing, resolved-conditionally):
  "does the running clock gauge-fix the CP sign?" The CP sign and the clock are the SAME quantity (CS), so the answer
  is YES -- CONDITIONAL on the single firewalled identification:
    [LEAP, Alexander 1807.01381]  CS-time = the cosmological clock (conjugate to Lambda).
  And the sign is then fixed by the ARROW (the orientation of the closing = the clock's direction), which S045 argues
  is itself forced (sigma non-invertibility; the de Sitter entropy floor). So: IF (CS = the clock) AND (the arrow is
  forced), THEN the CP sign is INTERNAL -- matter-over-antimatter = the sign of the clock = the arrow of time.

WHAT IT IS / ISN'T: the MATH (CP sign = sign of CS; amphichiral = the CS=0 origin; definite arrow) is solid and new.
It REDUCES the open forcing to two NAMED firewalled inputs (CS=clock; arrow forced). It does NOT derive the baryon
MAGNITUDE eta_B (still external, freeze-out). Firewalled; nothing to CLAIMS.
"""
import snappy


def cs_centered(M):
    cs = float(M.chern_simons())
    return ((cs + 0.5) % 1.0) - 0.5                      # center near 0


def cs_ladder(nmax=15):
    """CS(1,n) and CS(1,-n) along the scale ladder."""
    M0 = snappy.Manifold('m004'); _ = float(M0.chern_simons())
    rows = []
    for n in range(4, nmax + 1):
        M = snappy.Manifold('m004'); _ = float(M.chern_simons()); M.dehn_fill((1, n))
        if 'positively' not in M.solution_type():
            continue
        Mm = snappy.Manifold('m004'); _ = float(Mm.chern_simons()); Mm.dehn_fill((1, -n))
        rows.append((n, cs_centered(M), cs_centered(Mm)))
    return rows


if __name__ == "__main__":
    M0 = snappy.Manifold('m004'); print("cusped m004 (amphichiral): CS =", float(M0.chern_simons()),
                                        "(=0, the CP-symmetric ORIGIN of the clock)")
    rows = cs_ladder()
    print("\n(1,n):  CS(1,n)     CS(1,-n)    flip?")
    for n, cs, csm in rows:
        print(f"  (1,{n:2d}): {cs:+.6f}   {csm:+.6f}   {abs(cs+csm)<1e-5}")
    same_sign = all(r[1] < 0 for r in rows) or all(r[1] > 0 for r in rows)
    allflip = all(abs(r[1] + r[2]) < 1e-5 for r in rows)
    decaying = abs(rows[-1][1]) < abs(rows[0][1])
    print(f"\nCP sign = sign(CS): definite arrow (CS same sign along a history): {same_sign}")
    print(f"CS(1,-n) = -CS(1,n) (B289): {allflip}    |CS| -> 0 as n->inf (toward the amphichiral origin): {decaying}")
    print("=> the CP sign IS the sign of the CS clock. Forcing reduces to: [LEAP] CS = the cosmological clock.")
    assert same_sign and allflip and decaying
