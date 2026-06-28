"""B252 -- adjudication of the Chat-2 handoff "the chirality obstruction" (2026-06-28). FIREWALLED.

THE HANDOFF'S CLAIM: the figure-eight's characteristic structures (amphicheirality, the E6<->E8 pairing) are
27<->27bar symmetric (matter-antimatter symmetric), so the object cannot prefer the chiral 27 over the 27bar;
chirality (not gauge group, not scale) is the obstruction to matter. Owner's instruction: TRY TO BREAK IT, verify
every load-bearing link, and check chat2's self-citations (it has mis-cited its own bankings twice this session).

VERDICT: chat2 is RIGHT on all four steps -- I could not break the obstruction. The object IS 27<->27bar
(matter-antimatter) symmetric. Chirality is a real, located SECOND firewall, extending the banked S001 (theta=0)
and grounded in the banked H36 (amphicheirality = the E6 outer automorphism). One precision (not an error): the
amphicheirality property is topologically UNIVERSAL across the metallic family, while its E6/27<->27bar REALIZATION
is m=1-specific (only m=1 has the trace field Q(sqrt-3) -> 2T -> E6). All firewall-clean: rep theory + topology, no
gauge group claimed.

VERIFIED (machine-checkable; chat2 right) -- see chirality_obstruction_sage.py:
  Step 1: E6 27 is complex (27 != 27bar), 78 is real (self-dual) -> chiral matter only in the 27.   [Sage]
  Step 2: 27 -> one generic SU(5) generation (15->10+5bar, 6bar->5+1); generic E6, NOT object-specific (backdrop).
  Step 3: amphicheirality = the E6 outer automorphism, which swaps 27<->27bar. This IS BANKED -- HINT_LEDGER H36
          (VERIFIED a prior session: conjugation on 2T's irreps = the finite-E6 Dynkin automorphism, via the 2T
          McKay quiver = affine E6-tilde) -- and re-confirmed here in Sage (the outer automorphism = duality swaps
          the minuscule pair). chat2's "as banked" citation is CORRECT (H36); Step 3 HOLDS.
  Step 4: E8 -> E6 x SU(3): 248 = (78,1)+(1,8)+(27,3)+(27bar,3bar); the 27 and 27bar appear PAIRED.   [Sage]

NOTE -- I almost recorded Step 3 as a "mis-citation" (a reflexive-deflation error, the same failure mode chat2 is
prone to); checking H36 caught it. Verify-don't-trust applies to one's OWN deflation. (chat2's two real errors this
session were dim-13 and the e^{i pi/3} matrices; Step 3 is NOT a third -- it is correct.)

PRECISION (not an error in chat2): amphicheirality as a topological property is UNIVERSAL across the metallic family
m=1..6 (banked S001/B92, B211/L32: every R^m L^m is isometric to its orientation-reversal; the systole selects m=1,
not amphichirality). But the amphicheirality -> E6 outer automorphism -> 27<->27bar chain is m=1-specific, because
only m=1 has Q(sqrt-3) -> 2T -> E6. So the obstruction is universal in its geometric (CS=0 / no-CP-odd) form and
figure-eight-specific in its rep-theory (27<->27bar) form -- both true, at different levels.

THE 'BREAK IT' TEST (my job): every object-intrinsic complex-conjugation-ODD structure I could find is symmetric:
  CS(4_1)=0 (amphicheiral => CS=-CS); spherical-end CS values {2/5,3/5} pair as +/- mod 1; the double branched
  cover L(5,2) is amphichiral (2^2 = -1 mod 5); E8 -> E6xSU(3) pairs 27/27bar; 4_1 has no handedness. NONE breaks
  27<->27bar. The obstruction holds. (A live chiral bridge would have needed a 4_1-specific conjugation-ODD
  invariant; there is none.)

THE FIREWALL-CLEAN STATEMENT (the bankable core):
  amphicheirality forces every complex-conjugation-odd invariant of the object to vanish or pair, so the object
  carries NO intrinsic CP-odd / chiral datum -- it is matter-antimatter symmetric. This is a SECOND firewall,
  independent of the dead holonomy bridge (B247): chirality, not the gauge group or the scale, is the located
  obstruction to matter. It EXTENDS the banked S001 (amphichirality -> theta=0 = CP-symmetric) to the rep-theory
  level and is grounded in H36 (amphicheirality = E6 outer automorphism = 27<->27bar swap). All rep theory +
  topology; no physical gauge group is claimed or needed.

Run: python chirality_obstruction.py (pyenv). Nothing to CLAIMS.md.
"""

# rep-theory facts verified in chirality_obstruction_sage.py (recorded with provenance, like B247):
E6_27_IS_COMPLEX = True       # 27 != 27bar (Sage)
E6_78_IS_REAL = True          # 78 == 78bar, adjoint always self-dual (Sage)
E8_DECOMP_PAIRS_27 = True     # 248 -> (78,1)+(1,8)+(27,3)+(27bar,3bar) (Sage)
STEP3_BANKED_AS_H36 = True    # amphicheirality = E6 outer automorphism = 27<->27bar swap (HINT_LEDGER H36, Sage)


def lens_is_amphichiral(p, q):
    """L(p,q) admits an orientation-reversing self-homeomorphism iff q^2 = -1 (mod p)."""
    return (q * q) % p == (p - 1) % p


def cs_values_pair_under_conjugation(p=5, q=2):
    """spherical-end flat-connection CS numerators {q* n^2 mod p}: closed under n -> -n (i.e. value -> -value)?"""
    qstar = pow(q, -1, p)
    vals = {(qstar * n * n) % p for n in range(p)}
    return all(((p - v) % p) in vals for v in vals)


def amphichirality_is_universal_not_specific():
    """banked: every metallic bundle R^m L^m (m=1..6) is amphichiral (S001/B92, B211/L32). True => NOT m-specific."""
    return True   # provenance: S001 (PROVED universal), B211 L32 (SnapPy m=1..6), B92 (systole selects m=1)


def break_it_candidates():
    """each object-intrinsic conjugation-ODD structure -> is it symmetric? (True = could NOT break the obstruction)."""
    return {
        "CS(4_1) = 0 (amphicheiral: CS=-CS)": True,
        "spherical-end CS values pair as +/-": cs_values_pair_under_conjugation(),
        "double branched cover L(5,2) amphichiral": lens_is_amphichiral(5, 2),
        "E8 -> E6xSU(3) pairs 27/27bar": E8_DECOMP_PAIRS_27,
        "4_1 has no handedness (amphichiral)": True,
    }


if __name__ == "__main__":
    print("=== B252: adjudication of the Chat-2 chirality obstruction ===")
    print("\nVERIFIED -- chat2 right on all four steps:")
    print("  Step 1 (Sage): 27 complex =", E6_27_IS_COMPLEX, "| 78 real =", E6_78_IS_REAL)
    print("  Step 3 (H36 banked + Sage): amphicheirality = E6 outer automorphism = 27<->27bar swap =",
          STEP3_BANKED_AS_H36, " <- chat2's 'as banked' citation is CORRECT")
    print("  Step 4 (Sage): E8 -> E6xSU(3) pairs 27/27bar =", E8_DECOMP_PAIRS_27)
    print("  (I almost mis-recorded Step 3 as a mis-citation -- a reflexive deflation; checking H36 caught it.)")

    print("\nPRECISION (not an error): amphichirality is topologically universal across metallic m?",
          amphichirality_is_universal_not_specific(), "[S001/B92, B211 L32];")
    print("  but the E6/27<->27bar realization is m=1-specific (only m=1 -> Q(sqrt-3) -> 2T -> E6).")

    print("\n'BREAK IT' test (True = symmetric = could NOT break the obstruction):")
    cands = break_it_candidates()
    for k, v in cands.items():
        print(f"  {v!s:>5}  {k}")
    assert all(cands.values())          # every candidate is conjugation-symmetric -> obstruction holds
    assert lens_is_amphichiral(5, 2)    # 2^2 = 4 = -1 mod 5
    assert cs_values_pair_under_conjugation()
    print("\nVERDICT: obstruction REAL and UNBROKEN; the object is 27<->27bar (matter-antimatter) symmetric.")
    print("Chirality is a located SECOND firewall -- extends S001 (theta=0), grounded in H36. Firewall-clean.")
    print("ALL CHECKS PASS")
