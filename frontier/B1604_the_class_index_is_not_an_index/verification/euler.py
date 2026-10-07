#!/usr/bin/env python3
"""B1604 -- THE CLASS INDEX IS NOT AN INDEX.  The Euler characteristic of twisted cohomology on a cusped hyperbolic
3-manifold N (torus ends) vanishes for every flat module E: chi(N; E) = rank(E) chi(N) = 0.  With h^0, h^1 from the Fox
matrices and, by Poincare-Lefschetz duality, h^2(N; E) = dim H^1(N, dN; E*) = n(E*) + sum_i t0_i(E*) - h^0(E*) (the
long exact sequence of the pair: the kernel of H^1(E*) -> H^1(dN; E*) is the interior classes n(E*), the cokernel of
H^0(E*) -> H^0(dN; E*) contributes the rest) and h^3(N; E) = dim H^0(N, dN; E*) = 0, the constraint on the stacked
instrument's own numbers is  a0(E) - a1(E) + n(E*) + sum t0(E*) - a0(E*) = 0  at every module -- a consistency control the
instrument has not had.  Likewise the class index I(E) = n(E) - n(E*) is, by the same duality, the difference of the
interior ranks of E in degrees one and two: no Chern character governs it.

    python3 euler.py THREAD ...   -> euler_<thread>.json: the constraint at the four (every member), W1 and Lambda^2 W1
                                     (the first two members), on the thread's forced cover"""
import sys, json, pathlib
import snappy
HERE = pathlib.Path(__file__).resolve().parent
B1602 = HERE.parents[1] / "B1602_the_forced_cover_on_every_thread" / "verification"
sys.path.insert(0, str(B1602))
import forced_every as FE
MC, RM = FE.MC, FE.RM


def chi_data(S, E):
    c = S.counts(E); d = S.counts(MC.dual(E))
    h2 = d["n"] + d["t0_sum"] - d["a0"]
    return {"a0": c["a0"], "a1": c["a1"], "n": c["n"], "t0": c["t0"], "dual_a0": d["a0"], "dual_n": d["n"], "dual_t0": d["t0"],
            "h2": h2, "chi": c["a0"] - c["a1"] + h2, "I": c["n"] - d["n"]}


def run(name):
    M = snappy.Manifold(name); G, eps, label, group, good, ks = FE.forced(M)
    out = {"thread": name, "deck": label, "rows": []}
    for img in ks[:1]:
        perms = [[group.index(FE.mul(group[i], img[g])) for i in range(len(group))] for g in G.generators()]
        N = M.cover(perms); S = FE.site_of(N); done = 0
        for vals, nu in RM.sign_characters(S):
            V = S.four(nu); c = S.counts(V)
            row = {"nu": list(vals), "four": chi_data(S, V)}
            if c["n"] > 0 and done < 2:
                interior, other = S.classes(V); z = interior[0][0]
                W = S.extension(V, z); row["W1"] = chi_data(S, W)
                L2 = {g: MC.ext2(W[g]) for g in S.gens}; row["L2W1"] = chi_data(S, L2); done += 1
            out["rows"].append(row)
    out["chi_zero_everywhere"] = all(r[k]["chi"] == 0 for r in out["rows"] for k in r if k != "nu")
    out["modules_checked"] = sum(1 for r in out["rows"] for k in r if k != "nu")
    (HERE / f"euler_{name}.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    print(json.dumps({"thread": name, "modules": out["modules_checked"], "chi_zero": out["chi_zero_everywhere"],
                      "chis": sorted({r[k]["chi"] for r in out["rows"] for k in r if k != "nu"})}), flush=True)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        run(n)
