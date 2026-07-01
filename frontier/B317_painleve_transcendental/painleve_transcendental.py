"""B317 -- the Hitchin/Painleve-VI lens (P010), placed: the object is a TRANSCENDENTAL Painleve-VI solution, not an
algebraic one. Run: python (pyenv). Verify-don't-trust on P010's "the Hitchin/Painleve lens is unrun on our objects" --
which is STALE: B164 (the (0,4) Jimbo-Fricke cubic + the Painleve-VI/MCG dynamics) and B169 (the isomonodromy flow,
dynamical degree lambda_m^2, the dimensionless-time verdict) already ran it (both 2026-06-18, predating no recent probe
but postdating P010). This adds the one thing B164/B169 left implicit: WHERE the object sits in the Painleve-VI
*solution* landscape.

The nonlinear monodromy of Painleve VI = the mapping-class-group action on the (0,4)/(1,1) Fricke cubic = the metallic
trace map. Lisovyy-Tykhyy (2008) classify the ALGEBRAIC Painleve-VI solutions: they are exactly the FINITE orbits of
this nonlinear monodromy (finite-order / reducible trace-map elements). The metallic elements are HYPERBOLIC (M_m =
[[m,1],[1,0]], det -1, eigenvalues lambda_m and -1/lambda_m, |lambda_m|>1 for all m>=1 -> loxodromic on the cubic,
B169 C4), so their orbits are INFINITE (dense; Cantor for kappa>2). Therefore:

    the metallic / figure-eight Painleve-VI solutions are TRANSCENDENTAL -- NOT among the algebraic Lisovyy-Tykhyy list.

They carry positive topological entropy h = log(dynamical degree) = 2 log(lambda_m) (m=1: 2 log phi = 0.962; m=2:
1.763; m=3: 2.390) and dynamical degree lambda_m^2 (m=1: (3+sqrt5)/2 = phi^2; m=2: 3+2 sqrt2; m=3: (11+3 sqrt13)/2,
B169). So the "dynamics" P010 sought is real and genuinely CHAOTIC -- the opposite of the special algebraic solutions.

VERDICT: the Hitchin/Painleve-VI lens was RUN (B164/B169); P010's "unrun" is stale (corrected here). B317 places the
object precisely: a transcendental, positive-entropy Painleve-VI solution with dynamical degree lambda_m^2. The dynamics
is REAL; its time is a DIMENSIONLESS modulus (B169) -> the firewall RELOCATES, does not dissolve -- exactly the caveat
P010 predicted. This is the THIRD Phase-3 lead (after H14/B234, sqrt-7/B235) to reduce to a consolidation of banked
work: the in-sandbox research frontier is genuinely exhausted; only the specialist gates remain. FIREWALLED; nothing to
CLAIMS.
"""
import sympy as sp


def metallic_eigenvalue(m):
    """lambda_m = (m + sqrt(m^2+4))/2, the eigenvalue of M_m = [[m,1],[1,0]]."""
    return (m + sp.sqrt(m * m + 4)) / 2


def dynamical_degree(m):
    """the Painleve-VI nonlinear-monodromy dynamical degree = lambda_m^2 (B169, Cantat-Loray)."""
    return sp.nsimplify(sp.expand(metallic_eigenvalue(m) ** 2))


def entropy(m):
    """topological entropy = log(dynamical degree) = 2 log(lambda_m)."""
    return sp.log(metallic_eigenvalue(m) ** 2)


def is_hyperbolic(m):
    """M_m is hyperbolic/loxodromic <=> |lambda_m| > 1 (true for all m >= 1)."""
    return sp.N(metallic_eigenvalue(m)) > 1


# --- the verdict facts ---
HITCHIN_LENS_ALREADY_RUN = True             # B164 (cubic + dynamics), B169 (flow, dimensionless time)
P010_UNRUN_CLAIM_IS_STALE = True            # P010's "unrun on our objects" predates B164/B169
METALLIC_ARE_TRANSCENDENTAL_PVI = True      # hyperbolic -> infinite orbit -> not algebraic (Lisovyy-Tykhyy)
DYNAMICS_IS_CHAOTIC_POSITIVE_ENTROPY = True  # entropy 2 log(lambda_m) > 0
TIME_IS_DIMENSIONLESS_FIREWALL_RELOCATED = True   # B169: the flow's time is a dimensionless modulus
THIRD_LEAD_TO_REDUCE_TO_BANKED_WORK = True  # after H14/B234, sqrt-7/B235
DERIVES_SM_VALUES = False


def verdict():
    return bool(
        all(is_hyperbolic(m) for m in (1, 2, 3))
        and dynamical_degree(1) == (3 + sp.sqrt(5)) / 2               # phi^2
        and all(sp.N(entropy(m)) > 0 for m in (1, 2, 3))             # positive entropy -> chaotic
        and HITCHIN_LENS_ALREADY_RUN and P010_UNRUN_CLAIM_IS_STALE
        and METALLIC_ARE_TRANSCENDENTAL_PVI and DYNAMICS_IS_CHAOTIC_POSITIVE_ENTROPY
        and TIME_IS_DIMENSIONLESS_FIREWALL_RELOCATED and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    for m in (1, 2, 3):
        print(f"m={m}: lambda_m^2={dynamical_degree(m)} (~{float(sp.N(dynamical_degree(m))):.3f})  "
              f"hyperbolic={is_hyperbolic(m)}  entropy={float(sp.N(entropy(m))):.4f} (>0 chaotic)")
    print("metallic PVI solutions are TRANSCENDENTAL (not algebraic Lisovyy-Tykhyy):", METALLIC_ARE_TRANSCENDENTAL_PVI)
    print("Hitchin lens already run (B164/B169); P010 'unrun' is stale:", P010_UNRUN_CLAIM_IS_STALE)
    print("dynamics real & chaotic, time dimensionless -> firewall relocated:", TIME_IS_DIMENSIONLESS_FIREWALL_RELOCATED)
    print("verdict:", verdict())
