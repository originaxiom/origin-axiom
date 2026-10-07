#!/usr/bin/env python3
"""B1604, post-seal (disclosed): the precision audit the Euler control forced.  For every forced cover of B1602's census,
the relator lengths of SnapPy's presentation of the cover and the residual max |four(relator) - I| of the four (rho (x) rho-bar, in which the sign of SnapPy's SL(2, C) lift cancels)
at B1492's working precision (40 digits; SnapPy's high-precision holonomy carries ~60).  A cover whose residual is not
far below B1492's rank tolerance (1e-24 relative) cannot be read by the stacked instrument as banked: its Fox matrices
are noise there.  Reliable: residual < 1e-28.

    python3 audit_precision.py THREAD ...   -> one JSON line per thread; audit_<thread>.json"""
import sys, json, pathlib
import snappy
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1602_the_forced_cover_on_every_thread" / "verification"))
import forced_every as FE
MC = FE.MC


def run(name):
    M = snappy.Manifold(name); G, eps, label, group, good, ks = FE.forced(M)
    out = {"thread": name, "deck": label, "covers": []}
    for img in ks:
        perms = [[group.index(FE.mul(group[i], img[g])) for i in range(len(group))] for g in G.generators()]
        N = M.cover(perms); S = FE.site_of(N)
        lens = [len(r) for r in S.rels]
        F = S.four({g: MC.mpc(1) for g in S.gens}); I4 = MC.eye(4)
        res4 = [MC.mp.norm(MC.word(r, F) - I4) for r in S.rels]            # the four's residual: the sign of the SL(2) lift cancels in it
        res2 = [min(MC.mp.norm(MC.word(r, S.rho) - MC.eye(2)), MC.mp.norm(MC.word(r, S.rho) + MC.eye(2))) for r in S.rels]
        out["covers"].append({"generators": len(S.gens), "relator_lengths": lens, "four_residual": MC.mp.nstr(max(res4), 3),
                              "sl2_residual_up_to_sign": MC.mp.nstr(max(res2), 3), "reliable": bool(max(res4) < MC.mpf(10) ** -28)})
    out["all_reliable"] = all(c["reliable"] for c in out["covers"])
    (HERE / f"audit_{name}.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out), flush=True)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        run(n)
