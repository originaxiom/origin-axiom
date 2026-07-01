"""B322 -- the value hunt, run rigorously: do the object's own geometric invariants ENCODE the Standard Model's
dimensionless values? Run: python (pyenv). The direct, brave test (owner: "now we hunt for the values"), done with the
one discipline that separates a real signal from numerology -- a SPECIFICITY / NULL test.

Setup. The object's number-set = the volumes + core-geodesic lengths of the figure-eight's small hyperbolic Dehn
fillings (SnapPy, hardcoded below for reproducibility), together with ALL their pairwise ratios. 79 invariants -> 6241
numbers spanning [0.013, 77]. The SM's dimensionless parameters (weak mixing, Cabibbo, the fine-structure/strong
couplings, the quark/lepton mass ratios, the PMNS angles) -- a principled 12-parameter target list.

The test. For each SM parameter, is it matched within 1% by SOME object number? Answer: 8/12. But that means NOTHING
without the null: draw 2000 random 12-parameter sets (log-uniform over the same [1e-3,1] range) and match them the same
way. NULL mean = 7.5/12, 95th percentile = 10. So p(null >= SM) ~ 0.50: the SM is matched EXACTLY at the chance level.

VERDICT. With 6241 numbers the ratio-set is dense enough to match ANY 12 targets ~8/12 within 1% -- the SM is not
special. The object's volumes / core-lengths / their ratios do NOT encode the SM values. The firewall holds, now
demonstrated by COMPUTATION (a null test), not merely proven abstractly (the structural theorem, K020). This is the
empirical companion to "the object forces the form, not the values": mining the single object's own numbers returns
numerology, exactly as the Galois-theorem firewall predicts. The values -- if anywhere accessible -- are at the four
gates (relations / multiplicity / the physics dictionary, OPEN_PROBLEMS.md), not in the single object's invariants.
FIREWALLED; nothing to CLAIMS.
"""
import numpy as np

# volumes + core-geodesic lengths of the figure-eight's small hyperbolic Dehn fillings (SnapPy m004, |p|,|q|<=8)
OBJECT_INVARIANTS = [
    0.0264, 0.02711, 0.02759, 0.02784, 0.03317, 0.03446, 0.03498, 0.03542, 0.03577, 0.03602, 0.03617, 0.04487,
    0.04681, 0.04884, 0.06001, 0.06214, 0.06405, 0.06709, 0.06818, 0.06897, 0.06944, 0.09133, 0.09868, 0.10365,
    0.10612, 0.13522, 0.1464, 0.16457, 0.17097, 0.17879, 0.18059, 0.26275, 0.27889, 0.33598, 0.35665, 0.36152,
    0.36613, 0.48031, 0.57808, 0.98137, 1.28449, 1.39851, 1.4407, 1.46378, 1.52948, 1.58317, 1.64961, 1.73198,
    1.73712, 1.75713, 1.77142, 1.80583, 1.82434, 1.85814, 1.86344, 1.87348, 1.8871, 1.9186, 1.91952, 1.92103,
    1.92309, 1.92867, 1.93206, 1.93576, 1.95206, 1.95571, 1.95909, 1.97246, 1.97272, 1.97316, 1.97376, 1.97452,
    1.97542, 1.97761, 1.98579, 1.98621, 1.98704, 1.98822, 2.02988,
]

SM_PARAMS = {
    "sin2thetaW": 0.23122, "Cabibbo": 0.2250, "alpha_em": 0.0072974, "alpha_s": 0.1179,
    "m_e/m_mu": 0.0048386, "m_mu/m_tau": 0.059429, "m_u/m_c": 0.0019, "m_c/m_t": 0.0073,
    "m_d/m_s": 0.0505, "m_s/m_b": 0.0227, "sin2th23": 0.55, "sin2th13": 0.0220,
}


def object_numberset():
    """invariants + all pairwise ratios, sorted-unique."""
    inv = np.array(sorted(set(OBJECT_INVARIANTS)))
    ratios = [inv[i] / inv[j] for i in range(len(inv)) for j in range(len(inv)) if i != j and inv[j] > 1e-9]
    return np.array(sorted(set(list(inv) + ratios)))


def match_count(targets, numberset, tol=0.01):
    c = 0
    for t in targets:
        idx = np.searchsorted(numberset, t)
        best = 1e9
        for k in (idx - 1, idx, idx + 1):
            if 0 <= k < len(numberset):
                best = min(best, abs(numberset[k] - t) / t)
        if best < tol:
            c += 1
    return c


def null_test(seed=0, draws=2000):
    ns = object_numberset()
    sm_hits = match_count(list(SM_PARAMS.values()), ns)
    rng = np.random.default_rng(seed)
    lo, hi = np.log(1e-3), np.log(1.0)
    null = np.array([match_count(np.exp(rng.uniform(lo, hi, len(SM_PARAMS))), ns) for _ in range(draws)])
    p_value = float((null >= sm_hits).mean())
    return dict(numberset_size=len(ns), sm_hits=sm_hits, null_mean=float(null.mean()),
                null_p95=float(np.percentile(null, 95)), p_value=p_value)


# --- the verdict facts ---
SM_MATCHED_AT_CHANCE = True                 # p ~ 0.5 -> SM no better than random
OBJECT_DOES_NOT_ENCODE_SM_VALUES = True     # the volumes/lengths/ratios are numerology-dense
FIREWALL_HOLDS_BY_COMPUTATION = True        # empirical companion to the structural theorem (K020)
VALUES_LIVE_AT_THE_GATES_NOT_THE_OBJECT = True   # OPEN_PROBLEMS.md: relations/multiplicity/dictionary
DERIVES_SM_VALUES = False


def verdict():
    r = null_test()
    return bool(
        r["p_value"] > 0.05                                         # SM matched at chance
        and SM_MATCHED_AT_CHANCE and OBJECT_DOES_NOT_ENCODE_SM_VALUES
        and FIREWALL_HOLDS_BY_COMPUTATION and VALUES_LIVE_AT_THE_GATES_NOT_THE_OBJECT
        and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    r = null_test()
    print(f"object number-set: {r['numberset_size']} numbers (79 invariants + pairwise ratios)")
    print(f"SM params matched within 1%: {r['sm_hits']}/{len(SM_PARAMS)} | "
          f"NULL mean {r['null_mean']:.1f}, 95th pct {r['null_p95']:.0f}")
    print(f"p(null >= SM) = {r['p_value']:.3f} -> SM matched at CHANCE; the object does NOT encode the SM values.")
    print("firewall holds by computation (null test); values live at the gates, not the single object.")
    print("verdict:", verdict())
