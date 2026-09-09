#!/usr/bin/env python3
"""B1324 PART C -- the discrete-symmetry dictionary (DESIGN section 5).
C1: m004's eight self-isometries as sign triples (orientation, s_m, s_l); the kernel {1, P}; the named maps read off twister bundles
    (a*B -> B*a the record swap's image; a*B -> b*A the inverse monodromy).
C2: the one-cusped H1 = Z census to 7 tetrahedra: distribution of triple-pattern sets, the fully symmetric ones named."""
import json, pathlib
from collections import Counter
import numpy as np, snappy
from snappy import twister
HERE = pathlib.Path(__file__).resolve().parent

def cusp_mat(m):
    try: return np.array([[int(m[0, 0]), int(m[0, 1])], [int(m[1, 0]), int(m[1, 1])]])
    except Exception: return np.array([[int(m[0][0]), int(m[0][1])], [int(m[1][0]), int(m[1][1])]])

def triple(A):
    det = int(round(np.linalg.det(A)))
    if A[0, 1] or A[1, 0]: return (det, None, None)
    return (det, int(np.sign(A[0, 0])), int(np.sign(A[1, 1])))

def triples_between(M, N):
    return Counter(triple(cusp_mat(iso.cusp_maps()[0])) for iso in M.is_isometric_to(N, return_isometries=True))

def geometric(M):
    for _ in range(30):
        if "positively" in M.solution_type(): return M
        M.randomize()
    return M

def c1():
    m004 = snappy.Manifold("m004")
    selfs = triples_between(m004, m004)
    S = twister.Surface("S_1_1")
    aB = geometric(S.bundle(monodromy="a*B")); Ba = geometric(S.bundle(monodromy="B*a")); bA = geometric(S.bundle(monodromy="b*A"))
    out = {
        "m004 self-isometry triples (orientation, s_m, s_l) -> count": {str(k): v for k, v in selfs.items()},
        "identity det = s_m*s_l on all": all(k[1] is not None and k[0] == k[1] * k[2] for k in selfs),
        "four patterns twice each": sorted(selfs.values()) == [2, 2, 2, 2] and len(selfs) == 4,
        "kernel of D4 -> (Z/2)^2 has order": selfs.get((1, 1, 1), 0),
        "a*B -> B*a (record swap's image, the reflection word) triples": {str(k): v for k, v in triples_between(aB, Ba).items()},
        "a*B -> b*A (inverse monodromy: rotation and flow reversal) triples": {str(k): v for k, v in triples_between(aB, bA).items()},
        "a*B -> a*B (self) triples": {str(k): v for k, v in triples_between(aB, aB).items()},
        "a*B is m004": bool(aB.is_isometric_to(m004)), "B*a is m004": bool(Ba.is_isometric_to(m004)), "b*A is m004": bool(bA.is_isometric_to(m004)),
    }
    # the prediction: the swap's image carries fibre reflection with flow kept: (-1, +1, -1) present among a*B -> B*a
    sw = triples_between(aB, Ba); inv = triples_between(aB, bA)
    out["PASS_C1"] = out["identity det = s_m*s_l on all"] and out["four patterns twice each"] and out["kernel of D4 -> (Z/2)^2 has order"] == 2 \
        and (-1, 1, -1) in sw and (1, -1, -1) in inv and (-1, -1, 1) in inv
    return out

def c2():
    cens = Counter(); names = {}; n = 0
    for k in range(2, 8):
        for N in snappy.OrientableCuspedCensus(cusps=1, tets=k):
            if str(N.homology()) != "Z": continue
            n += 1
            keys = frozenset(triple(cusp_mat(iso.cusp_maps()[0])) for iso in N.is_isometric_to(N, return_isometries=True))
            cens[keys] += 1; names.setdefault(keys, []).append(N.name())
    full = frozenset({(1, 1, 1), (-1, 1, -1), (-1, -1, 1), (1, -1, -1)})
    out = {"one-cusped H1=Z census manifolds to 7 tets": n,
           "pattern sets -> count": {str(sorted(k, key=str)): v for k, v in cens.most_common()},
           "fully symmetric (all four patterns)": names.get(full, []),
           "identity-only (chiral, non-invertible)": names.get(frozenset({(1, 1, 1)}), [])[:12],
           "identity holds on every census isometry": all(all(t[1] is not None and t[0] == t[1] * t[2] for t in k) for k in cens)}
    out["PASS_C2"] = out["identity holds on every census isometry"] and "m004" in out["fully symmetric (all four patterns)"]
    return out

if __name__ == "__main__":
    res = {"C1": c1(), "C2": c2()}
    res["PASS"] = res["C1"]["PASS_C1"] and res["C2"]["PASS_C2"]
    (HERE / "c_dictionary.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    for part in ("C1", "C2"):
        print(f"== {part}")
        for k, v in res[part].items(): print("   ", k, ":", v)
    print("C DICTIONARY:", "PASS" if res["PASS"] else "FAIL")
