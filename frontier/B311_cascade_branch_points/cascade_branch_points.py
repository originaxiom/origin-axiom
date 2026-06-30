"""B311 -- the cascade's object-specific core = the TRINIFICATION branch point (only); the full chain is NOT realized
on the figure-eight's curve. Run: python (pyenv). Verifies (and corrects) Chat-2's proposed extension to B306/B310:
"u = 2pi i/3 (M = e^{i pi/3}) and u = pi i (M = i) are special points on the figure-eight's A-polynomial; compute the
E6 centralizer there and the deformation realization closes."

Verify-don't-trust on the cross-chat handoff. The figure-eight geometric A-polynomial component is
    A(M,L) = M^4 L^2 - (M^8 - M^6 - 2M^4 - M^2 + 1) L + M^4
(sign fixed by the complete-structure check: at M=1, A = (L+1)^2, so the geometric longitude is L=-1, not the abelian
L=1). Its discriminant in L, in x = M^2, factors EXACTLY:
    Disc(x) = (x-1)^2 (x+1)^2 (x^2 - 3x + 1) (x^2 + x + 1)
                               [GOLDEN]      [EISENSTEIN]
    x^2 + x + 1  -> x = omega, omega^2      = the Q(sqrt-3) (Eisenstein) end
    x^2 - 3x + 1 -> x = phi^2, phi^-2       = the Q(sqrt5)  (golden) end
So the program's TWO arithmetic ends sit in ONE figure-eight discriminant -- an object-specific fact (banked-theme).

Now the cascade grading points (principal lift: E6 meridian holonomy acts on a root of height h with eigenvalue
M^{2h}; centralizer = {height == 0 mod N} when M^{2h}=1):
  * N=2 (SU(6)xSU(2)): M = i      (x=-1) -- IS a branch point, BUT L_double = +1 => REDUCIBLE (abelian line).
  * N=3 (trinification): M = e^{i pi/3} (x=omega) -- IS a branch point, L_double = -1 => IRREDUCIBLE (geometric).
  * N>=4 (M=e^{i pi/N}): x = M^2 NOT in the branch set (e.g. N=4 -> x=i, not a root) -- NOT branch points at all.

THE CATCH Chat-2's optimism missed: the FIRST cascade step (N=2, SU(6)xSU(2)) lands on the REDUCIBLE (abelian) locus
L=1, NOT a genuine irreducible E6 flat connection; and N>=4 are not on the curve at all. So the grading points are
ISOLATED branch points, the first one reducible -- NOT a connected deformation realizing the chain. The ONLY cascade
step sitting at a genuine irreducible object-specific branch point is the TRINIFICATION (N=3, M=e^{i pi/3}, Eisenstein,
same L=-1 as the complete structure).

VERDICT: Chat-2's branch-point claim is TRUE (verified) but does NOT close the deformation realization. It REFINES
B310: there IS object-specific content (the trinification is character-variety-special -- an irreducible A-poly branch
point, upgrading B305 from arithmetic-eigenvalue to character-variety relevance; and the two arithmetic ends live in
one discriminant), but it is ONE step (trinification), not the cascade. The full physical realization of the chain
remains the T[4_1;E6] CRUX (specialist). FIREWALLED; nothing to CLAIMS.
"""
import sympy as sp

M, L, x = sp.symbols("M L x")
_c = M**8 - M**6 - 2 * M**4 - M**2 + 1            # the figure-eight geometric A-poly coefficient
_A = M**4 * L**2 - _c * L + M**4


def a_poly_sign_ok():
    """Complete structure M=1 must give the geometric L=-1 (double), not the abelian L=1 -- fixes the c sign."""
    return sp.factor(_A.subs(M, 1)) == (L + 1) ** 2


def discriminant_factored():
    """Disc_L(A) in x=M^2, factored."""
    disc = (_c**2 - 4 * M**8).subs({M**8: x**4, M**6: x**3, M**4: x**2, M**2: x})
    return sp.factor(disc)


def branch_points_x():
    """roots x=M^2 of the discriminant (with multiplicity)."""
    disc = (_c**2 - 4 * M**8).subs({M**8: x**4, M**6: x**3, M**4: x**2, M**2: x})
    return sp.roots(sp.Poly(disc, x))


def L_double(Mval):
    """the colliding (double) longitude root at a branch point: L = c/(2 M^4)."""
    return sp.nsimplify(sp.simplify(_c.subs(M, Mval) / (2 * Mval**4)))


def is_branch(Mval):
    return sp.simplify((_c**2 - 4 * M**8).subs(M, Mval)) == 0


def is_reducible(Mval):
    """branch point on the abelian line L=1 (longitude trivial) => reducible."""
    return sp.simplify(L_double(Mval) - 1) == 0


# --- the verdict facts ---
TWO_ENDS_IN_ONE_DISCRIMINANT = True            # x^2+x+1 (Eisenstein) AND x^2-3x+1 (golden) both divide Disc
N2_IS_BRANCH_BUT_REDUCIBLE = True              # M=i: branch point, L=1, abelian -- NOT a genuine E6 breaking
N3_TRINIF_IS_IRREDUCIBLE_BRANCH = True         # M=e^{i pi/3}: branch point, L=-1, irreducible (the one object step)
NGE4_NOT_BRANCH = True                          # N>=4 grading points are not on the discriminant locus
CHAT2_BRANCHPOINT_CLAIM_VERIFIED = True        # the two points ARE branch points (Chat-2 right)
CASCADE_REALIZATION_CLOSED = False             # but reducibility + isolation => NOT a connected breaking
OBJECT_CORE_IS_TRINIFICATION_ONLY = True       # the only irreducible object-specific cascade step is N=3 (B305)
REALIZATION_IS_THE_CRUX = True                 # the full physical chain is still the T[4_1;E6] CRUX
DERIVES_SM_VALUES = False


def verdict():
    return bool(
        a_poly_sign_ok()
        and discriminant_factored() == (x - 1) ** 2 * (x + 1) ** 2 * (x**2 - 3 * x + 1) * (x**2 + x + 1)
        and is_branch(sp.I) and is_reducible(sp.I)                       # N=2 branch + reducible
        and is_branch(sp.exp(sp.I * sp.pi / 3)) and not is_reducible(sp.exp(sp.I * sp.pi / 3))  # N=3 branch + irred
        and not is_branch(sp.exp(sp.I * sp.pi / 4))                      # N=4 not a branch point
        and CHAT2_BRANCHPOINT_CLAIM_VERIFIED and not CASCADE_REALIZATION_CLOSED
        and OBJECT_CORE_IS_TRINIFICATION_ONLY and REALIZATION_IS_THE_CRUX and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    print("A-poly sign check (complete structure L=-1):", a_poly_sign_ok())
    print("Disc factored (x=M^2):", discriminant_factored())
    print("branch points x=M^2:", {sp.nsimplify(r): m for r, m in branch_points_x().items()})
    for lbl, Mv in [("N=2 SU(6)xSU(2)  M=i", sp.I), ("N=3 trinif  M=e^{ipi/3}", sp.exp(sp.I * sp.pi / 3)),
                    ("N=4         M=e^{ipi/4}", sp.exp(sp.I * sp.pi / 4))]:
        print(f"  {lbl}: branch={is_branch(Mv)}  L_double={L_double(Mv) if is_branch(Mv) else '-'}  "
              f"reducible={is_reducible(Mv) if is_branch(Mv) else '-'}")
    print("object-specific core = trinification only (B305):", OBJECT_CORE_IS_TRINIFICATION_ONLY,
          "| realization = CRUX:", REALIZATION_IS_THE_CRUX)
    print("verdict:", verdict())
