#!/usr/bin/env python3
"""B1632 -- POST-SEAL DIAGNOSTIC (disclosed in FINDINGS).  The sealed C1 found no identification of (S, T) with the weave's
lifts that satisfies the Mp2(Z) relations exactly.  This diagnostic, on the sealed instrument's own constructions:
 D1  for each identification: is S^2 a scalar, does (S T)^3 equal S^2 up to a scalar, does S^8 equal I up to a scalar --
     i.e. is it a PROJECTIVE representation, and with which scalars;
 D2  every rescaling (S, T) -> (mu S, lam T) by roots of unity of order dividing 48 that makes it a genuine Mp2(Z)
     representation (S^2 central scalar, S^2 = (S T)^3, S^8 = I): the set of rescalings, and chi_k at every allowed
     half-integral weight -- in particular chi_{3/2} -- for each, and whether chi_{3/2} = 0 for all, some or none.
The physical multiplier (the zero modes' phases, the seat's W41) is not computed here; D2 says what holds for every choice.
Writes post_seal_projective.json."""
import json, pathlib, importlib.util, itertools, cmath, math
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("w45", HERE / "w45_on_main.py"); w45 = importlib.util.module_from_spec(spec); spec.loader.exec_module(w45)
om, cp, TB = w45.om, w45.cp, w45.TB


def scalar_of(A):
    s = A[0, 0]
    return (complex(s) if np.allclose(A, s * np.eye(A.shape[0]), atol=1e-9) else None)


def main():
    L = {"a": "a", "b": "ab"}; R = {"a": "ab", "b": "b"}; Linv = {"a": "a", "b": "Ab"}
    Sa = om.compose(om.compose(R, Linv), R)
    TS = cp.restrict(om.M_of(Sa), TB); TL = cp.restrict(om.M_of(L), TB); TR = cp.restrict(om.M_of(R), TB)
    Sopts = {"S~": TS, "S~^-1": np.linalg.inv(TS)}
    Topts = {"L": TL, "L^-1": np.linalg.inv(TL), "R": TR, "R^-1": np.linalg.inv(TR)}
    roots = [cmath.exp(2j * math.pi * m / 48) for m in range(48)]
    out = {"D1": [], "D2": {}}
    for (sn, S), (tn, T) in itertools.product(Sopts.items(), Topts.items()):
        s2 = scalar_of(S @ S); q = None
        if s2 is not None:
            q = scalar_of(np.linalg.matrix_power(S @ T, 3) @ np.linalg.inv(S @ S))
        s8 = scalar_of(np.linalg.matrix_power(S, 8))
        fmt = lambda z: None if z is None else round((cmath.phase(z) / (2 * math.pi)) % 1, 6)
        out["D1"].append({"S": sn, "T": tn, "S2_scalar_turn": fmt(s2), "ST3_over_S2_scalar_turn": fmt(q), "S8_scalar_turn": fmt(s8),
                          "projective": s2 is not None and q is not None and s8 is not None})
        if s2 is None or q is None: continue
        fixes = []
        for (mi, mu), (li, lam) in itertools.product(enumerate(roots), enumerate(roots)):
            S1, T1 = mu * S, lam * T
            S2 = S1 @ S1
            if not np.allclose(S2, S2[0, 0] * np.eye(3), atol=1e-9): continue
            if not np.allclose(S2, np.linalg.matrix_power(S1 @ T1, 3), atol=1e-9): continue
            if not np.allclose(np.linalg.matrix_power(S1, 8), np.eye(3), atol=1e-9): continue
            ch = {}
            for twok in range(-1, 28):
                k = twok / 2
                if w45.allowed(k, S1): ch[str(k)] = round(w45.chi(k, S1, T1), 6)
            fixes.append({"mu_48ths": mi, "lam_48ths": li, "chi": ch, "chi_3_2": ch.get("1.5")})
        vals = sorted({f["chi_3_2"] for f in fixes if f["chi_3_2"] is not None})
        out["D2"][f"{sn},{tn}"] = {"rescalings": len(fixes), "rescalings_allowing_3_2": sum(f["chi_3_2"] is not None for f in fixes),
                                   "chi_3_2_values": vals, "examples": fixes[:4]}
    json.dump(out, open(HERE / "post_seal_projective.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str)[:3000])


if __name__ == "__main__":
    main()
