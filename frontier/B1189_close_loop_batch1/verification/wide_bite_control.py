#!/usr/bin/env python3
"""GC-1 (2): WIDE bite control -- >=20 census manifolds NOT in members_B, spanning
small (few tetrahedra, low volume) and large (more tetrahedra, higher volume),
must land OFF the half-integer lattice of Vol(m004). Two-sided: also re-affirms
a couple of KNOWN members as a positive sanity check inside the same run.
"""
import json
import random
import snappy
import mpmath as mp
mp.mp.dps = 50

FAM = str(__import__("pathlib").Path(__file__).resolve().parents[3] / "frontier/B1186_family_is_112/verification/family_census.json")

def hp_vol(name):
    M = snappy.Manifold(name).high_precision()
    return mp.mpf(str(M.volume()).replace(" ", ""))

def main():
    fam = json.load(open(FAM))
    members_B = set(fam["members_B"])

    census = snappy.OrientableCuspedCensus
    n = len(census)
    print("census size:", n)

    rng = random.Random(20260828)  # fixed seed, declared

    # small: first 3000 manifolds (low tet count, low volume) minus members
    small_pool = [census[i].name() for i in rng.sample(range(0, 3000), 40)]
    # mid: middle of the census
    mid_pool = [census[i].name() for i in rng.sample(range(60000, 120000), 40)]
    # large: near the end of the census (many tetrahedra, higher volume, incl o10_*)
    large_pool = [census[i].name() for i in rng.sample(range(n - 20000, n), 40)]

    def take_non_family(pool, k):
        out, seen = [], set()
        for c in pool:
            if c not in members_B and c not in seen:
                out.append(c); seen.add(c)
            if len(out) == k:
                break
        return out

    controls = (take_non_family(small_pool, 8) + take_non_family(mid_pool, 8)
                + take_non_family(large_pool, 8))
    print(f"selected {len(controls)} non-family control manifolds (target >=20; "
          f"8 small + 8 mid + 8 large by census position)")
    assert len(controls) >= 20

    V0 = hp_vol("m004")
    on_lattice = []
    off_lattice = []
    for name in controls:
        M = snappy.Manifold(name)
        tets = M.num_tetrahedra()
        V = hp_vol(name)
        r = V / V0
        half = r * 2
        resid = abs(half - mp.nint(half))
        rec = {"name": name, "tets": tets, "ratio": float(r), "residual": mp.nstr(resid, 6)}
        if resid < mp.mpf(10) ** -9:   # generous tolerance for the NEGATIVE side
            on_lattice.append(rec)
        else:
            off_lattice.append(rec)

    print(f"\nON-lattice (should be EMPTY for a clean bite): {len(on_lattice)}")
    for r in on_lattice:
        print("  ", r)
    print(f"\nOFF-lattice (expected: all {len(controls)}):")
    for r in off_lattice:
        print(f"  {r['name']:>14s} tets={r['tets']:<3d} ratio={r['ratio']:.10f} resid~{r['residual']}")

    # positive-side re-affirmation inside the same script/run (two-sided control)
    pos_checks = ["m004", "m003", "t06829"]
    print("\npositive re-affirmation (must be ON-lattice):")
    pos_ok = True
    for name in pos_checks:
        V = hp_vol(name)
        r = V / V0
        half = r * 2
        resid = abs(half - mp.nint(half))
        ok = resid < mp.mpf(10) ** -30
        pos_ok &= ok
        print(f"  {name}: ratio={float(r):.6f} residual~{mp.nstr(resid,5)} on-lattice={ok}")

    out = {"n_controls": len(controls), "on_lattice": on_lattice, "off_lattice": off_lattice,
           "positive_reaffirmation_all_pass": pos_ok}
    json.dump(out, open("wide_bite_control_output.json", "w"), indent=1)
    print("\nVERDICT: bite control", "PASSES" if not on_lattice and pos_ok else "FAILS")

if __name__ == "__main__":
    main()
