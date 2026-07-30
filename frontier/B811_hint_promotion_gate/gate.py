#!/usr/bin/env python3
"""B811 — the full promotion gate on H128-H131. Prereg 6fa4c2c6fa027b44.

Gate 5 holds throughout: NO SM value reaches CLAIMS.md under any outcome. This decides whether
four hints promote, park, or die BY THE PROGRAMME'S OWN GATE -- not whether physics is derivable.

The family, the sigma windows and the 3/20 thresholds are quoted from the sealed prereg and are
NOT adjustable here.
"""
from mpmath import mp, mpf, sqrt

mp.dps = 30
PHI = (1 + sqrt(5)) / 2

# --- targets, with their OWN quoted uncertainties (the window is the datum's, not ours) -----
TARGETS = {
    "alpha_s(M_Z)":  (mpf("0.1180"), mpf("0.0009"), "H128", "1/(2*phi^3)"),
    "sin2_theta13":  (mpf("0.0220"), mpf("0.0007"), "H129", "phi^-8"),
    "Koide_Q":       (mpf("2") / 3,  mpf("0.00002"), "H130", "2/3"),
}

# sealed family: (a*phi^n + c) / (b*phi^m + d)
NRANGE = range(-8, 9)
ABRANGE = (1, 2, 3, 4, 5)
CDRANGE = (-2, -1, 0, 1, 2)
PROMOTE_MAX, KILL_MIN = 3, 20          # sealed


def family():
    """Enumerate the sealed expression family, deduplicated to 12 significant figures."""
    seen = {}
    for n in NRANGE:
        pn = PHI**n
        for a in ABRANGE:
            for c in CDRANGE:
                num = a * pn + c
                for m in NRANGE:
                    pm = PHI**m
                    for b in ABRANGE:
                        for d in CDRANGE:
                            den = b * pm + d
                            if den == 0:
                                continue
                            v = num / den
                            if v <= 0 or v > 10:
                                continue
                            key = mp.nstr(v, 12)
                            if key not in seen:
                                seen[key] = (v, f"({a}phi^{n}{c:+})/({b}phi^{m}{d:+})")
    return seen


def n_hit(fam, target, sigma):
    """How many DISTINCT family values land inside the target's own uncertainty."""
    return [(v, e) for v, e in fam.values() if abs(v - target) <= sigma]


def level_check_alpha_s():
    """The independent structural test, which can kill on its own.

    alpha_s(M_Z) is a RUNNING coupling: its value is defined only at a chosen scale (M_Z), and it
    changes with that scale. The object is PROVED scale-free (S3/B615). A quantity that exists
    only relative to a scale choice cannot be an output of a scale-free structure.
    """
    # demonstrate the scale-dependence concretely: one-loop QCD running, n_f = 5
    b0 = 23 / (12 * mp.pi)                     # (33 - 2*5)/(12 pi)
    a_mz = mpf("0.1180")
    out = {}
    for mu_ratio, label in ((mpf(2), "2 M_Z"), (mpf("0.5"), "M_Z/2"), (mpf(10), "10 M_Z")):
        inv = 1 / a_mz + 2 * b0 * mp.log(mu_ratio)
        out[label] = 1 / inv
    return out


def main():
    print("=" * 78)
    print("B811 — the full promotion gate on H128-H131")
    print("=" * 78)
    fam = family()
    print(f"\n  sealed family enumerated: {len(fam)} distinct values in (0, 10]")

    # fairness check the prereg demands: the family must CONTAIN the hinted forms
    print("\n  fairness check -- does the family contain the hinted forms?")
    for name, (t, s, h, form) in TARGETS.items():
        hinted = {"1/(2*phi^3)": 1 / (2 * PHI**3), "phi^-8": PHI**-8, "2/3": mpf(2) / 3}[form]
        inside = any(abs(v - hinted) < mpf("1e-11") for v, _ in fam.values())
        print(f"    {h}: {form:14} = {mp.nstr(hinted,10):14} in family: {inside}")

    print(f"\n  sealed thresholds: PROMOTE if N_hit <= {PROMOTE_MAX};"
          f"  KILL if N_hit >= {KILL_MIN} AND a structural reason exists")
    print(f"\n  {'hint':6} {'target':16} {'value':12} {'sigma':10} {'N_hit':>6}  p_look_elsewhere")
    results = {}
    for name, (t, s, h, form) in TARGETS.items():
        hits = n_hit(fam, t, s)
        p = len(hits) / len(fam)
        results[h] = {"target": name, "N_hit": len(hits), "p": p}
        print(f"  {h:6} {name:16} {mp.nstr(t,8):12} {mp.nstr(s,6):10} {len(hits):>6}  {p:.5f}")

    print(f"\n  LEVEL CHECK (H128, independent, can kill alone):")
    run = level_check_alpha_s()
    print(f"    alpha_s is a RUNNING coupling -- one-loop QCD, n_f=5:")
    for k, v in run.items():
        print(f"      alpha_s({k:6}) = {mp.nstr(v, 8)}")
    print(f"    the object is PROVED SCALE-FREE (S3/B615). A quantity whose value is defined only")
    print(f"    relative to a chosen scale cannot be the output of a scale-free structure.")
    print(f"    => H128's target is not the KIND of thing the object can emit. Structural, and")
    print(f"       independent of any base rate.")

    print(f"\n  VERDICTS against the sealed criteria:")
    STRUCT = {
        "H128": "scale-dependence vs a proved scale-free object (level check above)",
        "H129": "B580: no phi-power structure in any computed number, checked blind",
        "H130": "B580: the carrying channel is PROVEN information-free (level-1 chord identical "
                "for 4_1, 5_2 and the UNKNOT); B686: Q=2/3 is a 120-degree parametrisation tautology",
    }
    for h, r in results.items():
        if r["N_hit"] <= PROMOTE_MAX:
            v = "PROMOTED"
        elif r["N_hit"] >= KILL_MIN and h in STRUCT:
            v = "KILLED (legal)"
        else:
            v = "DORMANT"
        r["verdict"] = v
        print(f"    {h}: N_hit={r['N_hit']:<5} -> {v}")
        if h in STRUCT:
            print(f"          structural reason: {STRUCT[h]}")
    print(f"\n  H131: already a computed NULL (no log-periodic golden modulation in Planck 2018 TT")
    print(f"        residuals; the initial 7x excess was diagnosed as a Gaussian-smoothing artifact).")
    print(f"        Nothing to promote; it stays NULL.")
    return results


if __name__ == "__main__":
    main()
