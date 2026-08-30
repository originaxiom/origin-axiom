#!/usr/bin/env python3
"""GC-1 (1): INDEPENDENT recompute of the volume ladder -- own code, does not
import or exec og3_volume_spectrum.py. Covers ALL 35 non-regular members
(members_B minus members_A) plus a spread sample of regular members, >=30 total
(here: all 112, since each high-precision volume takes well under a second).

Method: snappy .high_precision().volume() (212-bit internal), cast through
mpmath at 50 dps, ratio to Vol(m004), test half-integrality at 1e-30.
"""
import json
import snappy
import mpmath as mp
mp.mp.dps = 50

FAM = str(__import__("pathlib").Path(__file__).resolve().parents[3] / "frontier/B1186_family_is_112/verification/family_census.json")

def hp_vol(name):
    M = snappy.Manifold(name).high_precision()
    return mp.mpf(str(M.volume()).replace(" ", ""))

def main():
    fam = json.load(open(FAM))
    members_B = fam["members_B"]
    members_A = set(fam["members_A"])
    non_regular = sorted(set(members_B) - members_A)
    assert len(non_regular) == 35, f"expected 35 non-regular, got {len(non_regular)}"

    V0 = hp_vol("m004")
    print("V0 = Vol(m004) [own recompute] =", V0)

    rows = []
    fails = []
    for name in members_B:
        V = hp_vol(name)
        r = V / V0
        half = r * 2
        n = mp.nint(half)
        resid = abs(half - n)
        is_half_int = resid < mp.mpf(10) ** -30
        rows.append({"name": name, "regular": name in members_A,
                     "ratio": float(r), "half_int_val": float(n) / 2,
                     "residual": mp.nstr(resid, 5)})
        if not is_half_int:
            fails.append((name, float(r), mp.nstr(resid, 10)))

    print(f"recomputed {len(rows)} members (all of members_B); non-regular among them: "
          f"{sum(1 for r in rows if not r['regular'])}")
    print("FAILURES (should be empty):", fails)

    # explicit report on every one of the 35 non-regular members
    print("\n--- all 35 non-regular members (independent recompute) ---")
    for row in rows:
        if not row["regular"]:
            print(f"  {row['name']:>14s}  ratio={row['ratio']:.15f}  "
                  f"half-int-val={row['half_int_val']}  residual~{row['residual']}")

    out = {"V0_m004_recompute": str(V0), "n_members_checked": len(rows),
           "n_non_regular_checked": sum(1 for r in rows if not r["regular"]),
           "failures": fails, "rows": rows}
    json.dump(out, open("ladder_recompute_output.json", "w"), indent=1)
    print("\nDONE. failures:", len(fails))

if __name__ == "__main__":
    main()
