#!/usr/bin/env python3
"""B1492 D5 -- frame F-CI on L8a15 under the seal (B1418's definitions, the loop of B1490's instrument): the isometry
group, chirality, the order of each isometry and the cusps it fixes, and the cusp counts |det(X - I)| over the
cusp-fixing orientation-preserving isometries (the 'three' is a value 3).  Writes fci_L8a15.json."""
import json, pathlib, collections, itertools
import snappy
HERE = pathlib.Path(__file__).resolve().parent


def perm_order(p):
    n = len(p); seen = [False] * n; lcm = 1
    from math import gcd
    for i in range(n):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]: seen[j] = True; j = p[j]; L += 1
            lcm = lcm * L // gcd(lcm, L)
    return lcm


def main(name="L8a15"):
    M = snappy.Manifold(name); isos = M.is_isometric_to(M, return_isometries=True)
    out = dict(name=name, cusps=M.num_cusps(), H1=str(M.homology()), volume=float(M.volume()), cusp_shapes=[str(s) for s in M.cusp_info("shape")], isometries=[])
    reversing = 0; dets = collections.Counter(); end_perms = set()
    for iso in isos:
        maps = iso.cusp_maps(); imgs = list(iso.cusp_images())
        d0 = int(maps[0][0][0] * maps[0][1][1] - maps[0][0][1] * maps[0][1][0])
        row = dict(cusp_images=imgs, orientation="reversing" if d0 == -1 else "preserving", end_permutation_order=perm_order(imgs), fixed_cusps=[], det_values=[])
        if d0 == -1: reversing += 1
        else:
            for i in range(M.num_cusps()):
                if imgs[i] == i:
                    X = maps[i]; a, b, c, d = int(X[0][0]), int(X[0][1]), int(X[1][0]), int(X[1][1]); v = abs((a - 1) * (d - 1) - b * c)
                    row["fixed_cusps"].append(i); row["det_values"].append(v); dets[v] += 1
        end_perms.add(tuple(imgs)); out["isometries"].append(row)
    order3 = [r for r in out["isometries"] if r["end_permutation_order"] == 3]
    out["summary"] = dict(total=len(isos), orientation_reversing=reversing, chiral=(reversing == 0), distinct_end_permutations=len(end_perms),
                          acts_on_ends_as_S3=(len(end_perms) == 6), order3_on_ends=len(order3), order3_fix_no_cusp=all(not r["fixed_cusps"] for r in order3),
                          cusp_fixing_det_values=dict(dets), three=(3 in dets))
    print(json.dumps(out["summary"])); json.dump(out, open(HERE / f"fci_{name}.json", "w"), indent=1, default=str)


if __name__ == "__main__":
    main()
