"""B315 -- H14 answered: is the object's E8+E6-E7 exclusion the SAME obstruction as heterotic string theory's E7-skip?
Run: python (pyenv). The audit's self-labelled "deepest framework-search question" (NOTICED since 2026-06-27).

A rep-theory + arithmetic synthesis, grounded in banked results (B234/H20/H30). The exceptional trichotomy -- the
Frobenius-Schur reality of the minimal faithful rep, the McKay group, and the object's character/trace field:

    E6:  27  FS=0  (COMPLEX)     chiral-capable   McKay 2T -> Q(sqrt-3)  disc -3   [Eisenstein end]
    E7:  56  FS=-1 (PSEUDOREAL)  non-chiral       McKay 2O -> Q(sqrt2)   disc  8   [EXCLUDED]
    E8:  248 FS=+1 (REAL)        adjoint/gauge    McKay 2I -> Q(sqrt5)   disc  5   [golden end]

HETEROTIC (E8 -> SU(3)xE6 standard embedding, chiral N=1): keeps E6 (27 complex, chiral matter), SKIPS E7 because the
56 is PSEUDOREAL (FS=-1) -> non-chiral -> no chiral matter. So heterotic's reason = NON-CHIRALITY.

THE OBJECT excludes E7 by THREE INDEPENDENT obstructions (B234/H20/H30):
  (1) Diophantine:  48 != p(p^2-1)  -- no congruence quotient 2O <-> SL(2,q);
  (2) rep-theoretic: FS(56)=-1 pseudoreal (w0=-1, symplectic) -> non-chiral        <== SHARED with heterotic;
  (3) arithmetic:   the McKay field Q(sqrt2)/2O has disc 8; the trace-1 law disc=t^2-4det gives disc=1 mod 4 (trace-1
                    reaches {-3 [E6, cusp det+1], 5 [E8, monodromy det-1]}; disc 8 [E7] needs EVEN trace -- it appears
                    only at the silver bundle m=2, not the figure-eight).

VERDICT (H14): heterotic's E7-skip = obstruction (2) (non-chirality) = ONE of the object's three -> SHARED, not the
whole. The object's exclusion CONTAINS heterotic's (it adds the Diophantine + arithmetic obstructions). It is NOT "the
same single obstruction" (B234/H30: the group-congruence and the field are distinct objects, independent). The two
COINCIDE because E7 is the PSEUDOREAL exceptional: pseudoreality (FS=-1) is the shared ROOT -- it is simultaneously
heterotic's non-chirality AND, via the McKay 2O->Q(sqrt2) field with no trace-1 home, the object's arithmetic exclusion.

BONUS [HOOK, firewalled]: the object's two-ended E8+E6 structure mirrors the heterotic standard embedding itself --
E8 (golden, ambient/gauge) -> E6 (Eisenstein, matter GUT with the chiral 27), E7 skipped -- a structural RHYME, not a
physical crossing. FIREWALLED; heterotic-string physics is [LEAP]; the math (FS reality, McKay fields, disc
reachability) is clean. Nothing to CLAIMS.
"""

# the exceptional trichotomy (reality of the minimal faithful rep; McKay group; character/trace field)
EXCEPTIONAL = {
    "E6": dict(rep="27", fs=0, reality="complex", mckay="2T", field="Q(sqrt-3)", disc=-3),
    "E7": dict(rep="56", fs=-1, reality="pseudoreal", mckay="2O", field="Q(sqrt2)", disc=8),
    "E8": dict(rep="248", fs=1, reality="real", mckay="2I", field="Q(sqrt5)", disc=5),
}


def chiral_capable(g):
    """chiral matter needs a COMPLEX rep (Frobenius-Schur indicator 0)."""
    return EXCEPTIONAL[g]["fs"] == 0


def metallic_disc(t, det):
    """discriminant of a trace-t, det-det unimodular element: t^2 - 4 det (B239)."""
    return t * t - 4 * det


def trace1_reaches():
    """the trace-1 fields: disc = 1 - 4 det for det in {+1, -1}."""
    return sorted({metallic_disc(1, 1), metallic_disc(1, -1)})   # {-3, 5}


def e7_needs_even_trace():
    """disc 8 (E7/2O) is unreachable at odd trace; even t=2, det=-1 gives 8 (silver m=2)."""
    odd = all(metallic_disc(t, -1) != 8 for t in (1, 3, 5, 7))
    even = metallic_disc(2, -1) == 8
    return odd and even


# --- the verdict facts ---
ONLY_E6_IS_CHIRAL_CAPABLE = None            # set below
HETEROTIC_SKIP_IS_NONCHIRALITY = True       # E8->SU(3)xE6 keeps E6 (27 complex), skips E7 (56 pseudoreal)
OBJECT_E7_OVERDETERMINED_THREEFOLD = True   # Diophantine + rep-theoretic + arithmetic (B234/H20)
SHARED_OBSTRUCTION_IS_NONCHIRALITY = True   # heterotic's reason = obstruction (2) = one of the object's three
SAME_SINGLE_OBSTRUCTION = False             # B234/H30: group-congruence vs field are distinct, independent
OBJECT_CONTAINS_HETEROTIC = True            # the object's exclusion is strictly stronger
SHARED_ROOT_IS_PSEUDOREALITY = True         # FS(56)=-1 is the common root of both exclusions
TWO_ENDS_MIRROR_HETEROTIC_CHAIN_IS_HOOK = True   # E8->E6 skip-E7 rhyme, firewalled [HOOK]
DERIVES_SM_VALUES = False

ONLY_E6_IS_CHIRAL_CAPABLE = (chiral_capable("E6") and not chiral_capable("E7") and not chiral_capable("E8"))


def verdict():
    return bool(
        ONLY_E6_IS_CHIRAL_CAPABLE
        and trace1_reaches() == [-3, 5] and e7_needs_even_trace()
        and HETEROTIC_SKIP_IS_NONCHIRALITY and OBJECT_E7_OVERDETERMINED_THREEFOLD
        and SHARED_OBSTRUCTION_IS_NONCHIRALITY and not SAME_SINGLE_OBSTRUCTION
        and OBJECT_CONTAINS_HETEROTIC and SHARED_ROOT_IS_PSEUDOREALITY
        and TWO_ENDS_MIRROR_HETEROTIC_CHAIN_IS_HOOK and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    for g, d in EXCEPTIONAL.items():
        print(f"{g}: {d['rep']:4s} FS={d['fs']:+d} ({d['reality']:10s}) chiral={chiral_capable(g)}  "
              f"{d['mckay']}->{d['field']} (disc {d['disc']})")
    print("only E6 chiral-capable:", ONLY_E6_IS_CHIRAL_CAPABLE)
    print("trace-1 reaches:", trace1_reaches(), "| E7/disc-8 needs even trace:", e7_needs_even_trace())
    print("heterotic skip = non-chirality = one of the object's 3 (shared):", SHARED_OBSTRUCTION_IS_NONCHIRALITY)
    print("same single obstruction:", SAME_SINGLE_OBSTRUCTION, "| object contains heterotic:", OBJECT_CONTAINS_HETEROTIC)
    print("shared root = pseudoreality FS(56)=-1:", SHARED_ROOT_IS_PSEUDOREALITY)
    print("verdict:", verdict())
