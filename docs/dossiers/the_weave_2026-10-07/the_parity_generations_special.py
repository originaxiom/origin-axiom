#!/usr/bin/env python3
"""W18, post hoc (after its read-out): WHERE EACH PARITY LINE'S PAIR DROPS. The whole line of gluing classes, per carrier.

W18's census read the gluing group H^1(M; Hom(P nu^-2, D nu^3)) at its two basis classes and one generic combination.
On four carriers the second basis class dropped each parity line's pair (I(W (x) P), I(L2 W (x) P)) from (1, 1) to
(0, 1). The basis comes from row reduction, so it is not random. This instrument asks where the pair drops on the
whole projective line of classes.

The rule (stated before this ran; it is not a prediction): every carrier of W18 (the 14 vector-like twins of the words
with phi^3 != +-I mod 16), lift 0, the first nu at which the gluing group is two-dimensional, and every class
c = b0 + s b1 (s in GF(p)) and c = b1, over GF(p) for the two smallest primes p = 1 mod 24, 73 and 97 (the cube and
fourth roots of unity are then in the field, so the whole line is read). At each class the first index I(W_c (x) P) is
read; where it differs from 1, the second, I(L2 W_c (x) P), is read too.

    python3 the_parity_generations_special.py   ->  the_parity_generations_special.json beside it
"""
import json
import sys
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_parity_generations as PG  # noqa: E402
import the_weave_extension as WE  # noqa: E402
import the_weaves_five as FV  # noqa: E402
import the_weaves_five_tick1 as T1  # noqa: E402

IL = WE.IL
CARRIERS = ["+LR", "-LLLR", "+LLLLLR", "-LLLRLR", "+LLLRRR", "-LLLLLLLR", "+LLLLLRLR", "-LLLLRLRR", "-LLLLRRLR",
            "-LLLRLLRR", "+LLLRLRRR", "-LLLRRLLR", "-LLRLLRLR", "+LLRLRLRR"]
PRIMES = (73, 97)


def scan(job):
    sw, p = job
    F = IL.GF(p)
    z = F.root_of_unity(24)
    S = T1.Tick1(sw, F, z)
    g = S.lifts[0]
    basis = None
    for nexp in range(24):
        Dm, Pm, basis = PG.gluing_basis(F, S, g, nexp)
        if len(basis) == 2:
            break
    assert basis is not None and len(basis) == 2, sw
    P0 = S.P(g, 0)
    tally, special = {}, []
    for s in list(range(p)) + ["inf"]:
        c = basis[1] if s == "inf" else [(a + s * b) % p for a, b in zip(basis[0], basis[1])]
        Wm = T1.five(F, S.gens, Dm, Pm, c)
        X = {h: PG.kron(F, Wm[h], P0[h]) for h in S.gens}
        I1 = IL.index(IL.Rep(F, S.gens, X), S.rels, S.mu, S.lam)[0]
        tally[str(I1)] = tally.get(str(I1), 0) + 1
        if I1 != 1:
            L2 = {h: PG.kron(F, FV.wedge2(F, Wm[h]), P0[h]) for h in S.gens}
            I2 = IL.index(IL.Rep(F, S.gens, L2), S.rels, S.mu, S.lam)[0]
            special.append({"s": s, "pair": [I1, I2]})
    return {"state": sw, "p": p, "nu (24ths)": nexp, "classes read": p + 1, "I(W (x) P) tally": tally,
            "the special classes": special}


if __name__ == "__main__":
    jobs = [(sw, p) for p in PRIMES for sw in CARRIERS]
    with Pool(2) as pool:
        rows = list(pool.imap(scan, jobs, chunksize=1))
    for r in rows:
        print(r["state"], r["p"], r["I(W (x) P) tally"], [x["s"] for x in r["the special classes"]], flush=True)
    out = {"rule": __doc__.split("The rule")[1].split("python3")[0].strip(), "rows": rows,
           "two special classes on every carrier at both primes":
               all(len(r["the special classes"]) == 2 for r in rows),
           "every special class reads (0, 1)":
               all(x["pair"] == [0, 1] for r in rows for x in r["the special classes"]),
           "the basis met a special class (s = inf) on":
               sorted({r["state"] for r in rows if any(x["s"] == "inf" for x in r["the special classes"])})}
    with open(HERE / "the_parity_generations_special.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in out.items() if k not in ("rows", "rule")}))
