#!/usr/bin/env python3
"""B1532 post-run check (written after the run; disclosed in FINDINGS): the members at the twists kappa^5 = 1, kappa != 1.

The sealed population is the lambda = 1 members.  A member nu = nu0 * eps, with nu0 a lambda = 1 member and eps trivial on the
fibre with eps(t_n) = kappa, kappa^5 = 1, kappa != 1, has the same V_eta (nu^5 = nu0^5).  Since eps^-4 = eps,
    W1(nu, c) = W1(nu0, c) (x) eps   and   Lambda^2 W1(nu, c) = Lambda^2 W1(nu0, c) (x) eps^2.
So on a finite abelian cover with deck characters B' its terms are W terms of nu0 at eps chi and Lambda^2 terms at eps^2 chi, and
by Lemma Z only the twists trivial on the cusp count.  With B0 = B' meet T_n^ (the characters of B' with chi(t_n) = 1):
  - if no chi in B' has chi(t_n) = kappa^-1 (equivalently, none has kappa^-2), the count is (0, 0);
  - otherwise, with x1 = eps chi1 in T_n^ for such a chi1, the count is
        S = ( sum over y in x1 + B0 of T_W(nu0, y, c),  sum over y in 2 x1 + B0 of T_L2(nu0, y, c) ),
    and the pairs (B0, x1 + B0) that occur are exactly those with 5 x1 in B0 (B' = <B0, eps^-1 x1>).
x1 in B0 gives nu0's own count over B0 (eps in B'), which the sealed census holds.  On M3 and M5 multiplication by 5 is invertible
on T_n, so nothing new occurs there; on M2, M4 and M6 the shifted cosets are new.  Every class is read as the census reads it
(c1; int, gen and each special class).  Both routes, on their own data, compared.

    python3 post_run_twists.py [--record]   ->  post_run_twists.json"""
import json
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import read_out as RO  # noqa: E402


def shifted_cosets(labels, B0):
    """the cosets x1 + B0 with 5 x1 in B0 and x1 not in B0, each with a representative"""
    seen, out = set(), []
    for x in sorted(labels):
        if x in B0 or RO.scale(x, 5) not in B0:
            continue
        C = frozenset(RO.shift(x, b) for b in B0)
        if C not in seen:
            seen.add(C)
            out.append((x, C))
    return out


def census(R, subs, trivial=False):
    """the shifted counts; with trivial=True the same code on the cosets x1 + B0 = B0 itself, which must reproduce the sealed
    census (read_out.Route.census) exactly"""
    hist, shaped, pairs = Counter(), [], Counter()
    for n in R.levels:
        labels = sorted(R.chars[n])
        cos = {B0: ([("0,0", B0)] if trivial else shifted_cosets(labels, B0)) for B0 in subs[n]}
        pairs[n] = sum(len(v) for v in cos.values())
        for nu in sorted(R.members[n]):
            if R.rows[(n, nu, "0,0")]["kind"] == "one":
                classes = {"c1": {chi: R.term_I(R.rows[(n, nu, chi)]["c"]) for chi in R.chars[n]}}
                specials = {}
            else:
                classes = {"int": {chi: R.term_I(R.rows[(n, nu, chi)]["int"]) for chi in R.chars[n]},
                           "gen": {chi: R.term_I(R.rows[(n, nu, chi)]["gen"][1]) for chi in R.chars[n]}}
                specials = R.special_classes(n, nu)
            for B0, cl in cos.items():
                for x1, C1 in cl:
                    C2 = frozenset(RO.shift(RO.scale(x1, 2), b) for b in B0)
                    for cname, tab in classes.items():
                        sw = sum(tab[y][0] for y in C1)
                        sl = sum(tab[y][1] for y in C2)
                        hist[(n, cname, sw, sl)] += 1
                        if sw == sl != 0:
                            shaped.append({"n": n, "nu": nu, "class": cname, "B0": sorted(B0), "x1": x1, "N": -sw})
                    gen = classes.get("gen")
                    for pt, spec in specials.items():
                        h1 = [y for y in spec if y in C1]
                        h2 = [y for y in spec if y in C2]
                        if not h1 and not h2:
                            continue
                        sw = sum(gen[y][0] for y in C1) + sum(spec[y][1][0] - gen[y][0] for y in h1)
                        sl = sum(gen[y][1] for y in C2) + sum(spec[y][1][1] - gen[y][1] for y in h2)
                        hist[(n, "special", sw, sl)] += 1
                        if sw == sl != 0:
                            shaped.append({"n": n, "nu": nu, "class": ["special", list(pt)], "B0": sorted(B0), "x1": x1,
                                           "N": -sw})
    return hist, shaped, pairs


def main():
    t0 = time.time()
    R = {route: RO.Route(route, RO.load(HERE / f"terms_{route}.jsonl")) for route in ("T", "L")}
    subs = {n: RO.subgroups(sorted(R["T"].chars[n])) for n in R["T"].levels}
    out = {"population": "members nu0 * eps at kappa^5 = 1, kappa != 1, on every finite abelian cover (B0, x1 + B0), 5 x1 in B0"}
    res = {}
    out["identity (the code at x1 = 0 reproduces the sealed census)"] = {}
    for route in ("T", "L"):
        sealed = R[route].census(subs)[0]
        mine = census(R[route], subs, trivial=True)[0]
        out["identity (the code at x1 = 0 reproduces the sealed census)"][route] = sealed == mine
        assert sealed == mine, ("the shifted-coset code does not reproduce the sealed census", route)
    for route in ("T", "L"):
        hist, shaped, pairs = census(R[route], subs)
        res[route] = (hist, shaped)
        out[route] = {"shifted (B0, coset) pairs by level": dict(pairs),
                      "counts read": sum(hist.values()),
                      "counts by level": dict(Counter(k[0] for k in hist.elements())),
                      "generation-shaped": shaped,
                      "N values": dict(Counter(s["N"] for s in shaped)),
                      "W values": dict(sorted(Counter(k[2] for k in hist.elements()).items())),
                      "Lambda^2 values": dict(sorted(Counter(k[3] for k in hist.elements()).items())),
                      "smallest W count": min(k[2] for k in hist), "smallest Lambda^2 count": min(k[3] for k in hist)}
    out["histogram (route T)"] = {str(k): v for k, v in sorted(res["T"][0].items())}
    out["routes agree"] = res["T"][0] == res["L"][0] and \
        sorted(json.dumps(s, sort_keys=True) for s in res["T"][1]) == sorted(json.dumps(s, sort_keys=True) for s in res["L"][1])
    out["seconds"] = round(time.time() - t0, 1)
    print(json.dumps({k: v for k, v in out.items() if k != "histogram (route T)"}, indent=1, default=str))
    if "--record" in sys.argv:
        (HERE / "post_run_twists.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    return out


if __name__ == "__main__":
    main()
