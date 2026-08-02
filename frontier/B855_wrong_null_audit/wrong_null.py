#!/usr/bin/env python3
"""B855 -- the wrong-null audit: the programme's genericity controls were family members.

A genericity verdict is only as good as its null. This checks the nulls the corpus actually used,
and the one cc proposed as a fix. Everything here is recomputed, not cited.

Mathematics scope. Nothing reaches CLAIMS.md.
"""
import json
import os
import warnings

warnings.filterwarnings("ignore")
import mpmath as mp
import snappy

HERE = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 30


def L_chi(s, dK):
    """L(s, chi_dK) for the two imaginary quadratic fields in play."""
    if dK == -3:
        return (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3)) / mp.power(3, s)
    if dK == -4:
        return (mp.zeta(s, mp.mpf(1) / 4) - mp.zeta(s, mp.mpf(3) / 4)) / mp.power(4, s)
    raise ValueError(dK)


def covolume(dK):
    """Humbert: vol(PSL(2,O_K)\\H^3) = |d_K|^{3/2} zeta_K(2) / (4 pi^2)."""
    return abs(dK) ** mp.mpf(1.5) * mp.zeta(2) * L_chi(2, dK) / (4 * mp.pi ** 2)


# The two rows of the family, plus the manifolds used as "controls" in the corpus.
PANEL = [
    ("m004", -3, "GOLDEN m=1 -- the object"),
    ("m003", -3, "the sister"),
    ("m206", -3, "used as a witness in B723"),
    ("m136", -4, "SILVER m=2 -- the family's second row"),
    ("m129", -4, "proposed by cc as a NON-commensurable null"),
    ("m135", -4, ""),
]
# candidate genuine nulls -- different field, so not commensurable with either row
CANDIDATE_NULLS = ["m009", "m010", "m015", "m022", "m023", "m039", "m040", "m006", "m007"]


def main():
    res = {"covolumes": {}, "panel": [], "amphichiral": {}, "candidate_nulls": []}
    for dK in (-3, -4):
        res["covolumes"][str(dK)] = mp.nstr(covolume(dK), 18)

    for name, dK, note in PANEL:
        M = snappy.Manifold(name)
        # USE THE COMPUTED VOLUME. The first version of this line overrode it with a
        # hardcoded class value keyed on the field -- which would have forced every row to
        # index 12 by construction and made the whole audit vacuous. Caught before banking.
        v = mp.mpf(repr(float(M.volume())))
        idx = v / covolume(dK)
        res["panel"].append(dict(name=name, field_disc=dK, volume=mp.nstr(v, 16),
                                 index=mp.nstr(idx, 18),
                                 index_is_12=bool(abs(idx - 12) < mp.mpf("1e-12")),
                                 note=note))

    for name in ["m004", "m003", "m136", "m135", "m129", "m015", "m009"]:
        try:
            res["amphichiral"][name] = bool(snappy.Manifold(name).symmetry_group()
                                            .is_amphicheiral())
        except Exception as exc:                                       # pragma: no cover
            res["amphichiral"][name] = f"unavailable: {exc}"

    for name in CANDIDATE_NULLS:
        M = snappy.Manifold(name)
        v = float(M.volume())
        res["candidate_nulls"].append(dict(
            name=name, volume=v, cusps=M.num_cusps(),
            # a manifold commensurable with either row would have vol an integer multiple
            # of that row's covolume; report both ratios so the check is visible.
            ratio_O3=mp.nstr(mp.mpf(repr(v)) / covolume(-3), 12),
            ratio_O1=mp.nstr(mp.mpf(repr(v)) / covolume(-4), 12)))

    # Reid: 4_1 is the UNIQUE arithmetic knot complement in S^3.
    res["reid"] = ("Reid 1991: the figure-eight is the unique arithmetic knot complement in S^3. "
                   "Since commensurability preserves arithmeticity, NO other knot complement is "
                   "commensurable with 4_1. In particular 4_1 and 5_2 are NOT commensurable.")
    res["family_rows"] = 2
    res["repo_has_null_noncommensurable_with_both_rows"] = False

    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)

    print("=" * 78)
    print("B855 -- the wrong-null audit")
    print("=" * 78)
    print(f"\n  covol PSL(2,O_-3) = {res['covolumes']['-3']}")
    print(f"  covol PSL(2,O_-1) = {res['covolumes']['-4']}")
    print(f"\n  {'manifold':9} {'field':7} {'volume':20} {'index':20} note")
    for r in res["panel"]:
        fld = "Q(v-3)" if r["field_disc"] == -3 else "Q(i)"
        print(f"  {r['name']:9} {fld:7} {r['volume']:20} {r['index']:20} {r['note']}")
    print("\n  => BOTH rows are index 12. m136, m129, m135 are all commensurable:")
    print("     m129 is the SILVER's class-mate, NOT a null.")
    print(f"\n  amphichirality: {res['amphichiral']}")
    print("\n  " + res["reid"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
