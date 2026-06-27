"""B233 -- SYNTHESIS (H13 + H17), the exact backbone. Two cross-finding questions from the QUESTION pass:
  H17: WHY does 5 = m^2+4 (at m=1) govern golden across every face -- one reason, or a pile-up?
  H13: does the hyperbolicity-split motif (B217/B226/B229) have one unifying statement?
This script verifies the EXACT arithmetic facts behind the H17 verdict; H13 is a framing recorded in
FINDINGS.md (a candidate synthesis from 3 witnesses, not a computation). Nothing to CLAIMS.md.

H17 VERDICT (partial unification, not a pile-up):
  ROOT A := golden = m=1 = the smallest metallic mean, field Q(sqrt 5), discriminant 5.
  ROOT B := 5 is the largest prime p for which SL(2,F_p) is an exceptional (E_6/E_8) McKay group.
  Almost everything cascades from A through the SINGLE field Q(sqrt5)/prime 5:
    - golden = smallest metallic mean  (m=1)                              [A]
    - dynamically extremal: smallest regulator / systole 4 log phi        [A: m=1 smallest]
    - least-hierarchical: smallest bundle volume 2 v_tet                  [A: m=1 smallest]
    - anyon level k=3, n=k+2=5=m^2+4 (Fibonacci/SU(2)_3)                  [A]
    - SUSY coset denominator SU(2)_3 (=golden level)                      [A]
    - WRT period divisible by 5 (the squarefree disc part)               [A: disc Q(sqrt5)=5]
    - char-variety conductor 40 = 2^3 * 5                                 [A: the 5-part]
    - E_8 McKay: monodromy field Q(sqrt5) -> SL(2,F_5)=2I=E_8            [A *and* B meet here]
  The ONE genuine coincidence: the value that is min(m^2+4) (root A) is ALSO the largest McKay prime
  (root B). Both are "5". So H17 = NOT a pile-up: one cascade (from Q(sqrt5)) + one number coincidence
  (min-discriminant = max-McKay-prime = 5). Sharper than SYNTHESIS.md sec.9's "same point, reason 5".

Firewall: pure arithmetic / rep-theory; nothing to CLAIMS.md. Run: python verify_five.py (pyenv).
"""
from sympy import isprime, sqrt, Rational


def metallic_disc(m):
    return m * m + 4


def sl2_fp_order(p):
    return p * (p * p - 1)


# binary polyhedral (McKay E_6/E_7/E_8) group orders
MCKAY = {"E6 (2T)": 24, "E7 (2O)": 48, "E8 (2I)": 120}


def mckay_as_sl2fp():
    """which exceptional McKay groups arise as SL(2,F_p)? return {label: p or None}."""
    out = {}
    for label, order in MCKAY.items():
        p_found = None
        for p in (2, 3, 5, 7, 11, 13):
            if isprime(p) and sl2_fp_order(p) == order:
                p_found = p
                break
        out[label] = p_found
    return out


def check_root_A():
    """A: 5 is the smallest metallic discriminant m^2+4, = disc(Q(sqrt5))."""
    discs = [(m, metallic_disc(m)) for m in range(1, 8)]
    assert min(d for _, d in discs) == 5 and discs[0] == (1, 5)
    # discriminant of Q(sqrt 5) is 5 (5 = 1 mod 4 -> fundamental disc = 5)
    assert 5 % 4 == 1
    return discs


def check_root_B():
    """B: among SL(2,F_p), the exceptional McKay groups are p=3 (E_6) and p=5 (E_8); 5 is the largest;
    E_7 (2O) is NEVER an SL(2,F_p) (order 48 not of the form p(p^2-1)) -> structurally excluded."""
    m = mckay_as_sl2fp()
    assert m["E6 (2T)"] == 3                       # SL(2,3) = 2T = E_6
    assert m["E8 (2I)"] == 5                       # SL(2,5) = 2I = E_8
    assert m["E7 (2O)"] is None                    # 2O never a congruence quotient SL(2,F_p)
    mckay_primes = sorted(p for p in m.values() if p is not None)
    assert mckay_primes == [3, 5] and max(mckay_primes) == 5
    return m


def cascade_table():
    """each '5'-face and the root it flows from (A: m=1/Q(sqrt5)/disc5 ; B: max-McKay-prime)."""
    return [
        ("golden = smallest metallic mean (m=1)",            "A"),
        ("dynamically extremal (systole 4 log phi)",          "A"),
        ("least-hierarchical (smallest volume 2 v_tet)",      "A"),
        ("anyon level k=3, n=m^2+4=5 (Fibonacci/SU(2)_3)",    "A"),
        ("emergent-SUSY coset denominator SU(2)_3",           "A"),
        ("WRT period divisible by 5 (disc Q(sqrt5))",         "A"),
        ("char-variety conductor 40 = 2^3 * 5",               "A"),
        ("E_8 McKay (monodromy Q(sqrt5) -> SL(2,F_5)=2I)",    "A&B"),
    ]


if __name__ == "__main__":
    print("=" * 74)
    print("B233  H17: why does 5 govern golden across every face?")
    print("=" * 74)

    discs = check_root_A()
    print("\nROOT A -- 5 = the smallest metallic discriminant m^2+4 = disc(Q(sqrt5)):")
    print("  m^2+4 for m=1..7:", [d for _, d in discs], " -> min =", min(d for _, d in discs))

    m = check_root_B()
    print("\nROOT B -- exceptional McKay groups as SL(2,F_p)  [order p(p^2-1)]:")
    for label, order in MCKAY.items():
        p = m[label]
        print(f"  {label:10s} order {order:3d}  ->  SL(2,F_p) at p = {p if p else 'NONE (excluded)'}")
    print("  McKay primes = {3 (E_6), 5 (E_8)}; largest = 5; E_7 (2O) structurally excluded.")

    print("\nCASCADE -- which root each '5'-face flows from:")
    nA = nB = 0
    for face, root in cascade_table():
        print(f"  [{root:3s}]  {face}")
        nA += root.startswith("A")
        nB += "B" in root
    print(f"\n  {nA}/8 faces cascade from ROOT A (the field Q(sqrt5) / m=1);")
    print(f"  the E_8 McKay face is where A meets B; B contributes ONLY the fact that")
    print(f"  min(m^2+4)=5 is ALSO the largest McKay prime -- ONE genuine number coincidence.")
    print("\n  H17 VERDICT: NOT a pile-up. One cascade (Q(sqrt5)) + one coincidence")
    print("  (min-discriminant 5 = max-McKay-prime 5). A *partial* unification.")

    # locks
    assert nA == 8 and nB == 1
    assert metallic_disc(1) == 5 == min(metallic_disc(m_) for m_ in range(1, 50))
    assert sl2_fp_order(5) == 120 and sl2_fp_order(3) == 24 and 48 not in {sl2_fp_order(p) for p in range(2, 50) if isprime(p)}
    print("\nALL CHECKS PASS")
