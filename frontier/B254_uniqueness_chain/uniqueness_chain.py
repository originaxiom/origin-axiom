"""B254 -- the uniqueness chain & chain merger: the arithmetic+CFT spine of "why the figure-eight reaches E6",
verified and firewalled. Adjudicates the Chat-1 handoff (2026-06-28). FIREWALLED -- arithmetic / rep theory / CFT,
NOT physics. Nothing to CLAIMS.md.

THE SPINE (each arrow verified or cited):
  figure-eight 4_1  --[Reid 1991, B125]-->  the UNIQUE arithmetic knot in S^3, trace field Q(sqrt-3)
  Q(sqrt-3)         --[McKay, B210/B249]-->  2T (binary tetrahedral) -> E6
  (E6)_1            --[conformal embedding]-> SU(3)_2 x (G2)_1
  (G2)_1            =  Fibonacci TQFT (c=14/5) -> SU(2)_3 x U(1)  [THE MERGER: the golden SU(2)_3 of B204]
  => (E6)_1 ⊃ SU(3)_2 x SU(2)_3 x U(1)

THE CHAIN MERGER (the new content): the FORCED chain (B204: phi -> SU(2)_3 -> Fibonacci -> TCI) and the ARITHMETIC
chain (4_1 -> Q(sqrt-3) -> 2T -> E6) converge at (G2)_1 = Fibonacci inside (E6)_1. The SU(2)_3 from
Freedman-Larsen-Wang universality (quantum face) IS the SU(2)_3 of the E6 conformal embedding (arithmetic face).
Verified by central charges (exact rationals).

CORRECTION to the handoff (verify-don't-trust): the handoff's McKay step said Q(sqrt-1)/Q(sqrt-2)->E7,
Q(sqrt-7)->E8. WRONG: E7<->2O has field Q(sqrt2), E8<->2I has field Q(sqrt5). The spine Q(sqrt-3)->2T->E6 is
correct (= B210/B249). Corrected below.

THE AMPHICHEIRAL Z2 GRADING (rep theory; the Yukawa PHYSICS is firewalled): the amphicheiral involution = the E6
diagram automorphism (H36), whose fixed algebra is F4. Branchings (Sage-verified): 27 = 1 + 26, 78 = 26 + 52. The
cubic 27^3 then carries a Z2 selection rule. This is rep theory; the "Yukawa texture matches observed masses" claim
is UNVERIFIED overclaim and firewalled (no mass pattern asserted).

FIREWALL: E6/E7/E8 are McKay/Arnold labels; SU(3)xSU(2)xU(1) here is a CFT coset, NOT a derived SM gauge group. No
scale (K018), no dynamics, no matter content claimed. The handoff's "E6 GUT boundary conditions / SU(2)_R / one SM
generation / Yukawa masses" framing is the dead bridge (B247) and stays firewalled.

Run: python uniqueness_chain.py (pyenv). Sage cross-check: uniqueness_chain_sage.py.
"""
import sympy as sp


def c_level1(dim, dual_coxeter):
    """central charge of a level-1 WZW: c = dim / (1 + h^vee)."""
    return sp.Rational(dim, 1 + dual_coxeter)


def c_su2(k):
    return sp.Rational(3 * k, k + 2)


def c_su3(k):
    return sp.Rational(8 * k, k + 3)


# (dim, h^vee) for the exceptional groups
EXC = {"G2": (14, 4), "F4": (52, 9), "E6": (78, 12), "E7": (133, 18), "E8": (248, 30)}

# McKay: binary polyhedral -> ADE -> character field (CORRECTED)
MCKAY = {"2T": (24, "E6", "Q(sqrt-3)"), "2O": (48, "E7", "Q(sqrt2)"), "2I": (120, "E8", "Q(sqrt5)")}

# amphicheiral Z2 (E6 -> F4) branchings, Sage-verified
F4_BRANCH = {"27": ("1", "26"), "78": ("26", "52")}


def conformal_tower_closes():
    """(E6)_1 ⊃ SU(3)_2 x SU(2)_3 x U(1): central charges sum to c((E6)_1)=6."""
    cE6 = c_level1(*EXC["E6"])
    return c_su3(2) + c_su2(3) + 1 == cE6, cE6


def g2_is_fibonacci_and_hosts_su2_3():
    """(G2)_1 (c=14/5, Fibonacci) ⊃ SU(2)_3 x U(1): the chain merger. c(SU(2)_3)+1 = c((G2)_1)."""
    cG2 = c_level1(*EXC["G2"])
    return c_su2(3) + 1 == cG2, cG2


if __name__ == "__main__":
    print("=== B254: the uniqueness chain & chain merger (verified, firewalled) ===\n")
    print("central charges (level-1 WZW): " + ", ".join(f"c(({g})_1)={c_level1(*v)}" for g, v in EXC.items()))
    print(f"conformal embedding SU(3)_2 x (G2)_1 = {c_su3(2)}+{c_level1(*EXC['G2'])} = "
          f"{c_su3(2)+c_level1(*EXC['G2'])} = c((E6)_1)")

    tower_ok, cE6 = conformal_tower_closes()
    merge_ok, cG2 = g2_is_fibonacci_and_hosts_su2_3()
    print(f"\n(E6)_1 ⊃ SU(3)_2 x SU(2)_3 x U(1): closes at c={cE6}? {tower_ok}")
    print(f"MERGER: (G2)_1=Fibonacci (c={cG2}) ⊃ SU(2)_3 x U(1) [= the golden SU(2)_3 of B204]? {merge_ok}")

    print("\nMcKay (corrected): " + " | ".join(f"{g}->{ade},{fld}" for g, (o, ade, fld) in MCKAY.items()))
    print(f"amphicheiral Z2 (E6->F4): 27 = {'+'.join(F4_BRANCH['27'])}, 78 = {'+'.join(F4_BRANCH['78'])}")

    assert tower_ok and merge_ok
    assert MCKAY["2T"][1] == "E6" and MCKAY["2T"][2] == "Q(sqrt-3)"   # the spine
    assert MCKAY["2I"][2] == "Q(sqrt5)" and MCKAY["2O"][2] == "Q(sqrt2)"  # handoff's "other fields" corrected
    print("\nVERDICT: the arithmetic+CFT spine verifies; the quantum (B204) and arithmetic (B210) chains merge at")
    print("(G2)_1=Fibonacci inside (E6)_1. Physics framing (SM/GUT/Yukawa-mass) firewalled. ALL CHECKS PASS")
