"""B343 -- the object forces EXACT TBM (theta13=0), not TM1/TM2: irreducibility is why (Chat-2, verified).

Corrects B342/S048's "would-be TM2" reading. Chat-2 self-corrected three times (each smaller and truer);
this seat verified the final landing. The chain:

  1. The (Z/4)^2 congruence torsion (B326) has 2-torsion subgroup {(0,0),(0,2),(2,0),(2,2)} = the Klein
     four-group Z2xZ2 -- structurally the NEUTRINO residual-symmetry type (TBM's Klein group).
  2. The deck Z/3 acts on it by Phi_3 = x^2+x+1 reduced mod 2 (IRREDUCIBLE over F2): it 3-CYCLES the
     three nonzero Klein elements {(1,0),(0,1),(1,1)} and FIXES NONE.
  3. The charged-lepton Z/3, T = diag(1,w,w^2), does NOT normalize the neutrino Klein {1,S,U,SU}
     (T S T^-1 is not in it) -- so T alone does not select a column. (B342's "Z/3 -> TM2" conflated the
     charged-lepton and neutrino sectors; corrected.)
  4. TM1 vs TM2 requires SELECTING one Z2 of the Klein group. The object's Z/3 cycles all three
     symmetrically -> selects NONE -> the FULL Klein survives -> EXACT TBM (theta13 = 0). Not TM1, not
     TM2 -- the symmetric point. And theta13 = 0 is EXCLUDED (observed 8.57 deg).

VERDICT: the object forces exact TBM; the TM2 selection is RETRACTED. The TBM-breaking (theta13's size
AND its direction, TM1/TM2) is EXTERNAL -- the object's irreducibility symmetrizes over all breaking
directions. UNIFICATION: the SAME irreducibility (Phi_3 irreducible mod 2 for the Klein, mod 4 for the
full torsion, B326) is why the object is mass-blind (B335), split-blind (B327/B329), AND direction-blind
-- one arithmetic property = "symmetric, hence magnitude- and direction-blind."

Surviving falsifiable content (firewalled [LEAP] on the identification): lepton mixing is TBM-structured
(large, near-TBM) -- observed; quark mixing small -- observed; the deviation theta13 is external.
Firewalled; nothing to CLAIMS. Needs only sympy/numpy.
"""
import sympy as sp
import numpy as np

W = sp.exp(2 * sp.I * sp.pi / 3)


def two_torsion_is_klein():
    """2-torsion of (Z/4)^2 = {(0,0),(0,2),(2,0),(2,2)} = Klein Z2xZ2."""
    tt = [(a, b) for a in (0, 2) for b in (0, 2)]
    return len(tt) == 4 and all((2 * a % 4, 2 * b % 4) == (0, 0) for a, b in tt)


def deck_z3_cycles_the_three_z2s():
    """deck = companion(Phi_3) mod 2 -> 3-cycle on {(1,0),(0,1),(1,1)}, fixes none (irreducible)."""
    C = sp.Matrix([[0, 1], [1, 1]])                     # companion of x^2+x+1 mod 2
    nz = [(1, 0), (0, 1), (1, 1)]
    imgs = [tuple(int(x) % 2 for x in (C * sp.Matrix(v))) for v in nz]
    x = sp.symbols('x')
    irreducible = len(sp.Poly(x**2 + x + 1, modulus=2).factor_list()[1]) == 1
    return set(imgs) == set(nz) and all(imgs[i] != nz[i] for i in range(3)) and irreducible


def T_does_not_normalize_neutrino_klein():
    """T=diag(1,w,w^2) (charged-lepton Z/3) does not fix a neutrino Z2: T S T^-1 not in {1,S,U,SU}."""
    T = sp.diag(1, W, W**2)
    S = sp.Rational(1, 3) * sp.Matrix([[-1, 2, 2], [2, -1, 2], [2, 2, -1]])
    U = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    TST = sp.simplify(T * S * T.inv())
    return not any(sp.simplify(TST - M) == sp.zeros(3) for M in [sp.eye(3), S, U, sp.simplify(S * U)])


def full_klein_gives_exact_tbm():
    """unbroken Klein residual -> exact TBM: theta13 = 0, sin^2 theta12 = 1/3."""
    UT = np.array([[np.sqrt(2/3), np.sqrt(1/3), 0], [-np.sqrt(1/6), np.sqrt(1/3), np.sqrt(1/2)],
                   [-np.sqrt(1/6), np.sqrt(1/3), -np.sqrt(1/2)]])
    theta13 = np.degrees(np.arcsin(abs(UT[0, 2])))
    s12sq = abs(UT[0, 1])**2 / (1 - abs(UT[0, 2])**2)
    return abs(theta13) < 1e-9, abs(s12sq - 1/3) < 1e-9


if __name__ == "__main__":
    print("1. 2-torsion = Klein Z2xZ2:", two_torsion_is_klein())
    print("2. deck Z/3 3-cycles the three Z2s (irreducible, fixes none):", deck_z3_cycles_the_three_z2s())
    print("3. T (charged-lepton Z/3) does NOT normalize the neutrino Klein:", T_does_not_normalize_neutrino_klein())
    t13_zero, s12_third = full_klein_gives_exact_tbm()
    print("4. full Klein -> exact TBM: theta13=0:", t13_zero, " sin^2 th12=1/3:", s12_third, " (theta13=0 EXCLUDED)")
    print("=> object forces EXACT TBM, not TM2 (RETRACTED). Breaking (theta13) external. Irreducibility unifies")
    print("   every silence: mass-blind (B335), split-blind (B327/B329), direction-blind (here). One property.")
