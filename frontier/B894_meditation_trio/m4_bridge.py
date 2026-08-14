"""B894 M4: the torsion-prime bridge — banked B581 block torsions vs disc(mu).

Support identity at p <= 13 (TRUE) + exponent comparison (no identity, honest).
Exact integer arithmetic; writes m4_bridge.json.
"""
import json
from sympy import factorint

# banked B581 torsions (frontier/B581_six_torsions/FINDINGS.md, repo-official)
TAU = {1: -3,
       4: 2**7*3*7*97,
       5: -(2**7*3**4*5**2*7**2*13),
       7: -(2**12*3**4*5*7**5*11*13*19*43),
       8: 2**14*3**3*5*7**3*11*13*31*607*49297,
       11: -(2**21*3**7*5*7**6*11**2*13**2*17*19*73*149*151*1471*160453)}
DISC_MU = 2**32*3**10*5**2*7**3*11*13**6  # B866


def smallblock(n, bound=13):
    return {p: e for p, e in factorint(abs(n)).items() if p <= bound}


def main():
    tau_ad = 1
    for v in TAU.values():
        tau_ad *= v
    res = {
        "tau_ad_smallblock": {str(k): v for k, v in smallblock(tau_ad).items()},
        "disc_mu": {str(k): v for k, v in factorint(DISC_MU).items()},
        "support_identity": set(smallblock(tau_ad)) == set(factorint(DISC_MU)),
        "measured_pair_smallblock": {str(k): v
                                     for k, v in smallblock(TAU[4]*TAU[8]).items()},
        "sign_law_alignment": {str(m): ("+" if TAU[m] > 0 else "-") for m in TAU},
        "large_primes_absent_from_disc": sorted(
            p for p in factorint(abs(tau_ad)) if p > 13),
        "entry_pattern": ("11 first divides tau_m at m=7; 13 at m=5; "
                          "7 saturates all m>=4 (B581, banked)"),
    }
    print("tau_ad small-prime block:", res["tau_ad_smallblock"])
    print("disc(mu):", res["disc_mu"])
    print("SUPPORT IDENTITY (primes <= 13):", res["support_identity"])
    print("torsion signs:", res["sign_law_alignment"],
          "=> positive exactly at the MEASURED slots {4,8}")
    json.dump(res, open(__file__.replace("m4_bridge.py", "m4_bridge.json"), "w"),
              indent=1, default=str)
    return res


if __name__ == "__main__":
    main()
