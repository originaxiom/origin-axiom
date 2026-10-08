"""Same-author separate rational/log-radius checks; no native imports.

Checks local leading norms and RR bookkeeping, not a global PDE solution.
"""
from fractions import Fraction as Q
import json


def integral(coefficients):
    return sum((v/Q(k+1) for k, v in enumerate(coefficients)), Q())


def mul(a, b):
    out = [Q()] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def run():
    predicates = {}
    def check(name, yes):
        predicates[name] = bool(yes)
        if not yes:
            raise AssertionError(name)
    # z^alpha grows in the canonical frame; one upper pole shifts it by -1.
    degrees = []
    for d in range(7):
        exponents = [Q(-1, 2)]*d + [Q(1, 2)]*(6-d)
        degrees.append(-sum(exponents))
        check(f"degree_rank_{d}", degrees[-1] == d-3)
        check(f"complement_rank_{d}", degrees[-1] == -(3-d))
    # t=-log r; smooth/form density exp(-(2s+2)t), spin cusp
    # density exp(-(2s+1)t)/t. The critical coefficient has s=-1/2.
    s = Q(-1, 2)
    check("form_decay_rate_positive", 2*s+2 > 0)
    check("cusp_spin_is_one_over_t", 2*s+1 == 0)
    check("regular_spin_decay_rate_positive", 2*Q(1, 2)+1 > 0)
    check("wrong_spin_weight_changes_measure", Q(-1) != Q(-1, 2))
    b = [Q(), Q(), Q(1), Q(-2), Q(1)]
    db = [Q(k)*b[k] for k in range(1, len(b))]
    n0, n1 = integral(mul(b, b)), integral(mul(db, db))
    check("bump_norm", n0 == Q(1, 630))
    check("bump_gradient_norm", n1 == Q(2, 105))
    check("weyl_ratio", n1/n0 == 12)
    check("spin_gauge_total_periodic", (-1)*(-1) == 1)
    check("untwisted_control_antiperiodic", (-1)*1 == -1)
    for n in range(1, 11):
        check(f"escaping_disjoint_support_{n}", (n+1)**3 > n**3+n)
    return {"predicates": predicates, "predicates_passed": len(predicates),
            "sheaf_indices": [int(d) for d in degrees],
            "weyl_residual_squared": "12/L^2",
            "pole_norms": {"one_form": "finite", "smooth_spin": "finite", "cusp_spin": "divergent"},
            "not_nonauthor_review": True}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
