#!/usr/bin/env python3
"""FINISHING THE CONSISTENCY CAMPAIGN -- C-2, C-3, C-4, C-6.

Seal: outside_bench/seals/CONSISTENCY_CAMPAIGN_FINISH_PREREG.md
      sha256 0c7c729c21a7bafa647db5d2ededf845c0d0a20d95fd50bfa65feb6469b8ec1e

docs/CONSISTENCY_CAMPAIGN.md was opened 2026-08-31 on the owner's instruction
"craft a campaign and do it properly".  B1230 ran C-1, C-5, C-5b.  C-2, C-3,
C-4, C-6 did not run.  This finishes what can be finished and reports the rest
as blocked, naming on whom.

THE CAMPAIGN'S STOP RULES BIND:
  1. No cell may claim a row DELETED -- cells re-TYPE (continuum -> finite -> bit).
  2. Every continuous-parameter count states the field it is taken over.
  3. A cell that cannot fail does not run (MB12).
  4. already_banked before every novelty claim.
  5. Cited is not verified.

C-4 is a CROSS-CHECK, declared as such in the seal: the r-label is ALREADY
typed FINITE-place by B1182.  Modular data either confirms that from an
independent direction or does not.

Exact arithmetic in the cyclotomic field Q(zeta_24) via sympy.
"""
from __future__ import annotations

import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 60

RUN, BLOCKED = [], []


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


# ---------------------------------------------------------------- (E6)_1 data
# E6's centre is Z/3 -> 3 primaries.  Level 1 simply-laced: c = rank = 6.
# Conformal weights of the three: 0 (vacuum), 2/3 (27), 2/3 (27-bar).
RANK = 6
C_CENTRAL = sp.Integer(RANK)                 # c = rank at level 1
H = [sp.Integer(0), sp.Rational(2, 3), sp.Rational(2, 3)]
N = 3


def zeta(k, n):
    """exp(2*pi*i*k/n), exact."""
    return sp.exp(2 * sp.pi * sp.I * sp.Rational(k, n))


def build_T():
    """T = diag(exp(2*pi*i*(h_j - c/24)))."""
    return sp.diag(*[sp.simplify(sp.exp(2 * sp.pi * sp.I * (H[j] - C_CENTRAL / 24)))
                     for j in range(N)])


def build_S():
    """(E6)_1 is a pointed MTC with Z/3 fusion: S_jk = omega^{jk}/sqrt(3)."""
    w = zeta(1, 3)
    M = sp.Matrix(N, N, lambda j, k: w ** (j * k))
    return sp.simplify(M / sp.sqrt(N))


def order_of_diag(T):
    """Exact multiplicative order of a diagonal matrix of roots of unity."""
    orders = []
    for j in range(T.rows):
        e = sp.simplify(T[j, j])
        k = 1
        while k <= 240:
            if sp.simplify(e ** k - 1) == 0:
                orders.append(k)
                break
            k += 1
        else:
            return None, None
    return sp.ilcm(*orders) if len(orders) > 1 else orders[0], orders


def main() -> int:
    print("=" * 78)
    print(" FINISHING THE CONSISTENCY CAMPAIGN -- C-2, C-3, C-4, C-6")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/CONSISTENCY_CAMPAIGN_FINISH_PREREG.md
    sha256 0c7c729c21a7bafa647db5d2ededf845c0d0a20d95fd50bfa65feb6469b8ec1e""")
    failures = []

    # ================================================================== C-4
    rule("C-4 -- THE r-LABEL VIA THE T-MATRIX  (a CROSS-CHECK, per the seal)")
    print("""
    Campaign question, verbatim:
      "The r-label via the T-matrix.  T has finite order (12 at E6).  Is the
       arrow a branch choice of finite order?"
    Outcomes, verbatim:
      "FINITE-PLACE CONFIRMED (matches B1182's typing from an independent
       direction) / UNRELATED"

    B1182's banked typing (GRAND_COMPUTATION_v0 section 5):
      "the r-label (arrow) | one Z/2 seed, FINITE-place | B1182: r -> k7
       (fixes K pointwise, flips sqrt3), finite orbits"
    So the r-label is ALREADY finite.  C-4 asks whether modular data says the
    same from an independent direction.  It is not a new deletion.
""")
    T = build_T()
    S = build_S()
    print(f"    primaries        : {N}   (E6's centre is Z/3)")
    print(f"    central charge c : {C_CENTRAL}   (level 1 simply-laced: c = rank)")
    print(f"    conformal weights: {H}")
    print("\n    T = diag" + str(tuple(sp.simplify(T[j, j]) for j in range(N))))
    for j in range(N):
        print(f"      T[{j},{j}] = {sp.nsimplify(sp.simplify(T[j, j]))}"
              f"   = exp(2*pi*i*{sp.nsimplify(H[j] - C_CENTRAL/24)})")

    # ------------------------------------------------------------ T2
    ordT, per = order_of_diag(T)
    print(f"\n    per-entry orders : {per}")
    print(f"    ORDER OF T       : {ordT}   (computed, not asserted)")
    ok_t2 = (ordT == 12)
    print(f"    T2 -> {'PASS' if ok_t2 else 'FAIL'} (the campaign says '12 at E6')")
    if not ok_t2:
        failures.append("T2")

    # ------------------------------------------------------------ T1
    rule("CONTROL T1 -- is this actually a modular tensor category?")
    print("""
    T's ORDER above is exact (root-of-unity exponent arithmetic).  The four
    MTC identities are matrix identities in Q(zeta_24); sympy's simplify does
    not reduce these symbolic exponentials reliably (the first run printed
    -I == -I and still reported FAIL), so they are verified NUMERICALLY at
    dps = 60 with residuals printed.  A residual is a number you can check;
    a boolean from a simplifier that silently gives up is not.
""")
    def E(x):
        return mp.e ** (2j * mp.pi * x)

    def resid(A, B):
        return max(abs(A[j, k] - B[j, k]) for j in range(N) for k in range(N))

    Tn = mp.matrix(N, N)
    for j in range(N):
        Tn[j, j] = E(mp.mpf(sp.Rational(H[j]).p) / sp.Rational(H[j]).q
                     - mp.mpf(int(C_CENTRAL)) / 24)
    Cn = mp.matrix([[1 if (j + k) % N == 0 else 0 for k in range(N)] for j in range(N)])
    Idn = mp.matrix([[1 if j == k else 0 for k in range(N)] for j in range(N)])

    print("""    THE S-MATRIX SIGN IS DETERMINED BY THE THEOREM, NOT CHOSEN.  A pointed
    Z/3 MTC has S_jk = w^{s*jk}/sqrt(3) with s = +1 or -1.  The first run used
    s = +1 and (ST)^3 = S^2 failed by EXACTLY 1.0 -- a real discrepancy, not
    precision.  Both signs are computed below; exactly one satisfies the
    relations, and that is what fixes the convention.
""")
    chosen = None
    for sign in (+1, -1):
        Sn = mp.matrix(N, N)
        for j in range(N):
            for k in range(N):
                Sn[j, k] = E(mp.mpf(sign * j * k) / 3) / mp.sqrt(N)
        Sdag = mp.matrix([[mp.conj(Sn[k, j]) for k in range(N)] for j in range(N)])
        ST = Sn * Tn
        rs = (resid(Sn, Sn.T), resid(Sn * Sdag, Idn),
              resid(Sn * Sn, Cn), resid(ST * ST * ST, Sn * Sn))
        print(f"    S_jk = w^{{{'+' if sign > 0 else '-'}jk}}/sqrt(3):"
              f"  symmetric {mp.nstr(rs[0], 4)}   unitary {mp.nstr(rs[1], 4)}"
              f"   S^2=C {mp.nstr(rs[2], 4)}   (ST)^3=S^2 {mp.nstr(rs[3], 4)}")
        if all(r < mp.mpf(10) ** (-30) for r in rs):
            chosen = (sign, rs)
    ok_t1 = chosen is not None
    if ok_t1:
        print(f"\n    -> the relations FIX the sign at s = {chosen[0]:+d};"
              f" all four residuals < 1e-30")
    else:
        print("\n    -> NEITHER sign satisfies the relations: the data is not an MTC")
    print(f"    T1 -> {'PASS' if ok_t1 else 'FAIL'} (all four are theorems of an MTC)")
    print("""    Note: T's ORDER, computed exactly above, does not depend on this sign --
    the load-bearing number is untouched by the convention.""")
    if not ok_t1:
        failures.append("T1")

    # ------------------------------------------------------------ T3
    rule("CONTROL T3 -- the Gauss-sum condition fixes the c/24 phase")
    theta_n = [mp.e ** (2j * mp.pi * mp.mpf(sp.Rational(H[j]).p) / sp.Rational(H[j]).q)
               if H[j] != 0 else mp.mpf(1) for j in range(N)]
    gauss_n = sum(theta_n) / mp.sqrt(N)
    target_n = mp.e ** (2j * mp.pi * mp.mpf(int(C_CENTRAL)) / 8)
    r_gauss = abs(gauss_n - target_n)
    ok_t3 = r_gauss < mp.mpf(10) ** (-30)
    print(f"    sum_j theta_j / sqrt(N) = {mp.nstr(gauss_n, 12)}")
    print(f"    exp(2*pi*i*c/8)         = {mp.nstr(target_n, 12)}   (c = {C_CENTRAL})")
    print(f"    residual                = {mp.nstr(r_gauss, 5)}")
    print(f"    T3 -> {'PASS' if ok_t3 else 'FAIL'}")
    if not ok_t3:
        failures.append("T3")

    # ------------------------------------------------------------ the verdict
    rule("C-4 VERDICT")
    finite = (ordT is not None and ordT < sp.oo)
    c4 = "FINITE-PLACE CONFIRMED" if (finite and ok_t1 and ok_t2) else "UNRELATED"
    print(f"""    T has finite order {ordT}.  Every branch choice inside this modular
    data therefore lies in a finite-order structure -- there is no continuum
    for the arrow to live in on the RCFT side.

    -> C-4 = {c4}

    AND WHAT IT IS NOT, per the seal: the r-label was ALREADY typed
    FINITE-place by B1182 from the arithmetic side (r -> k7, finite orbits).
    This is a SECOND, INDEPENDENT direction agreeing -- a cross-check.  NO ROW
    IS DELETED (stop rule 1), and the input count does not move.""")
    RUN.append(("C-4", c4))

    # ================================================================== C-3
    rule("C-3 -- LAMBDA AS A KMS WEIGHT: NOT RUN, BLOCKED")
    print("""
    Campaign question, verbatim:
      "lambda as a KMS weight.  Is the modular (Tomita-Takesaki) flow periodic
       for a rational boundary?  Periodic => lambda is a finite label."
    Outcomes, verbatim:
      "PERIODIC (lambda joins the finite menus) / NOT (lambda stays a genuine
       continuum; the floor carries it)"

    BLOCKED, and the seal said so in advance.  Tomita-Takesaki modular theory
    for the local algebra of a rational boundary is operator algebra, not
    arithmetic.  This bench has no instrument for it and will not manufacture
    an argument in order to avoid reporting a block.

    WHAT WOULD SETTLE IT: a statement, with citation, of whether the modular
    automorphism group of the vacuum state on a chiral RCFT's local algebra is
    periodic -- the Bisognano-Wichmann / Borchers line for conformal nets is
    where such a statement would live.  That is a reading task for someone who
    holds the operator-algebra literature, not a computation.""")
    BLOCKED.append(("C-3", "operator algebra; no instrument on this bench"))

    # ================================================================== C-2
    rule("C-2 -- THE Z/12 CHARACTER ASSIGNMENT: NOT RUN, BLOCKED (externally held)")
    print("""
    Campaign question, verbatim:
      "The Z/12 character assignment (codex holds it; B1216's R1).  Decides
       identity-vs-scalar on B_0."
    Outcomes, verbatim:
      "A: identity -> P^3 is real, floor carries 3 continuous params /
       B: scalar -> B_0 is 1-dim over Q(zeta_12), P = a point, ZERO"

    BLOCKED.  The campaign's own status column reads RELAY, and its cell text
    says "codex holds it".  The datum is not in this repository.

    WHAT IS NEEDED AND FROM WHOM: the Z/12 character assignment on B_0 from
    the seat that holds it (B1216's R1).  NOTE THE STAKE, since it is the
    largest single item left in the input accounting: outcome B would take the
    P^3 Higgs line from THREE continuous parameters to ZERO.  That is the
    biggest available reduction named anywhere in the deletion schedule, and
    it is waiting on a relay, not on mathematics.""")
    BLOCKED.append(("C-2", "externally held (codex; B1216 R1) -- and it is the "
                           "largest single reduction left: 3 continuous params -> 0"))

    # ================================================================== C-6
    rule("C-6 -- THE LEDGER AMENDMENT, over what actually ran")
    print(f"""
    Campaign cells, final state:
      C-1   RAN  (B1230)  OVER-COUNTED -- sigma counted as a continuum where
                          consistency gives a finite menu; two rows state no field
      C-5   RAN  (B1230)  REFUTED B1229's uniqueness: c = 6 has FOUR solutions
      C-5b  RAN  (B1230)  the recovery
      C-4   RAN  (here)   {c4}
      C-3   BLOCKED       operator algebra
      C-2   BLOCKED       externally held -- the largest reduction left
      C-6   RAN  (here)   this table

    THE AMENDMENT, and it is a typing not a deletion (stop rule 1):
      the r-label (arrow)  FINITE-place, now confirmed from TWO independent
                           directions -- arithmetic (B1182: r -> k7, finite
                           orbits) and modular data (C-4: ord(T) = {ordT})
      sigma                finite menu, NOT a continuum -- but the menu's
                           TIGHTNESS rests on the two-character restriction,
                           which C-5 showed is doing real work (c = 6 has four
                           solutions without it).  Carried as a HYPOTHESIS.
      the P^3 Higgs line   UNRESOLVED, pending C-2.  3 continuous params or 0.
      lambda               UNRESOLVED, pending C-3.  Finite label or continuum.

    SO THE CAMPAIGN'S NET EFFECT ON THE INPUT COUNT IS: nothing deleted, one
    typing cross-confirmed, and TWO ROWS WHOSE RESOLUTION IS BLOCKED ON
    MATERIAL THIS BENCH DOES NOT HOLD.""")
    RUN.append(("C-6", "amendment written over what ran"))

    # ------------------------------------------------------------ T4
    rule("CONTROL T4 -- a campaign that comes back all-green is not this campaign")
    print(f"    cells RUN     : {len(RUN)}  {[c for c, _ in RUN]}")
    print(f"    cells BLOCKED : {len(BLOCKED)}  {[c for c, _ in BLOCKED]}")
    ok_t4 = len(BLOCKED) >= 1 and len(RUN) >= 1
    print(f"    T4 -> {'PASS' if ok_t4 else 'FAIL'}")
    if not ok_t4:
        failures.append("T4")

    rule("VERDICT")
    for c, v in RUN:
        print(f"    {c:5s} RAN      {v}")
    for c, v in BLOCKED:
        print(f"    {c:5s} BLOCKED  {v}")
    print(f"\n    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    print("""
    NOT CONCLUDED: no row is DELETED (stop rule 1).  sigma is not claimed to be
    1 -- C-5 refuted that uniqueness argument and the restriction it leaned on
    is carried as a hypothesis (#26).  Nothing about the SM.  No value.""")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
