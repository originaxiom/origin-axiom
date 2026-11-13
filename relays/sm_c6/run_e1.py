#!/usr/bin/env python3
"""SM-C6 E1: the based count (n(V), n(V*)) of every sector module, on the word -> manifold and module -> vacuum steps.
Card: relays/cards/SM_C6_E1_the-based-count.md (pushed before this run).  Uses B1438's own exact_slopes from a checkout of
main, whose root is the first argument.  Data-free.
    python3 run_e1.py MAIN_CHECKOUT [out.json]"""
import sys, io, json, time, itertools, contextlib, pathlib
from collections import Counter
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(MAIN / "frontier" / "B1438_the_slope_law" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import slope_law as SL

CENSUS_LEVELS = [(1, "LR", k) for k in range(1, 6)] + [(-1, "LR", k) for k in range(1, 6)] + \
                [(1, "LLR", k) for k in range(1, 5)] + [(-1, "LLR", k) for k in range(1, 5)] + \
                [(1, "LLLR", k) for k in range(1, 4)] + [(-1, "LLLR", k) for k in range(1, 4)]


def rot_class(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def broken_words(lengths=(6, 7)):
    out = []
    for n in lengths:
        seen = set()
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w: continue
            c = rot_class(w)
            if c in seen: continue
            seen.add(c)
            r = rot_class(w[::-1])
            if r != c and (r, c) not in [(b, a) for a, b in out]:
                out.append((c, r))
    return out


def based(S, N, swap_plant=False):
    """{(l, alpha): (n, n*)} over all sector modules of a level (l, alpha, beta = alpha - l non-trivial)"""
    chars = [k for k in S if k != (0, 0, 0)]
    out = {}
    for l in chars:
        for a in chars:
            if a == l: continue
            b = tuple((x - y) % N for x, y in zip(a, l))
            bi = tuple((-x) % N for x in b)
            sa = S[b] if swap_plant else S[a]
            out[(l, a)] = (int(sa == S[l]), int(S[bi] == S[l]))
    return out


def census(B):
    c = Counter(B.values())
    return {"%d%d" % k: v for k, v in sorted(c.items())}


NMAX = 60          # deviation from the card, disclosed on the page: exact arithmetic beyond N = 60 is out of reach here


def torsion(eps, w, k):
    out = SL.ac.level(eps, w, k)
    return max(1, SL.ac.torsion_exponent(out[5]))


def level(eps, w, k):
    t = time.time()
    N, F, S = SL.exact_slopes(eps, w, k)
    return N, S, time.time() - t


def main():
    out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "e1_results.json"
    res = {"census": [], "pairs": [], "plants": {}}
    # step 2: the census on B1438's census levels
    p1_changed = 0
    for eps, w, k in CENSUS_LEVELS:
        N, S, dt = level(eps, w, k)
        B = based(S, N); Bp = based(S, N, swap_plant=True)
        c, cp = census(B), census(Bp)
        p1_changed += (c != cp)
        res["census"].append({"state": ("+" if eps > 0 else "-") + w, "level": k, "N": N, "characters": len(S) - 1,
                              "modules": len(B), "census": c, "share_11": (c.get("11", 0) / len(B)) if B else None,
                              "plant_P1_census": cp})
        print("census", eps, w, k, "N", N, "modules", len(B), c, round(dt, 1), "s", flush=True)
    res["plants"]["P1 census changed on levels"] = [p1_changed, len(CENSUS_LEVELS)]
    # step 1: words against their reverses
    pairs = broken_words()
    multisets = []
    for (w, r) in pairs:
        for eps in (1, -1):
            for k in (1, 2):
                if max(torsion(eps, w, k), torsion(eps, r, k)) > NMAX:
                    res.setdefault("skipped", []).append({"word": w, "sign": eps, "level": k,
                                                          "N": [torsion(eps, w, k), torsion(eps, r, k)]})
                    continue
                Nw, Sw, _ = level(eps, w, k); Nr, Sr, _ = level(eps, r, k)
                Bw, Br = based(Sw, Nw), based(Sr, Nr)
                same_chars = set(Sw) == set(Sr)
                labelled_same = same_chars and Bw == Br
                cw, cr = census(Bw), census(Br)
                multisets.append(((eps, w, k), cw))
                res["pairs"].append({"word": w, "reverse": r, "sign": eps, "level": k, "N": [Nw, Nr],
                                     "same_coordinate_characters": same_chars, "labelled_same": labelled_same,
                                     "census_w": cw, "census_r": cr, "census_same": cw == cr,
                                     "slopes_as_sets_same": sorted(map(str, (v.c for kk, v in Sw.items() if kk != (0, 0, 0)))) ==
                                                            sorted(map(str, (v.c for kk, v in Sr.items() if kk != (0, 0, 0))))})
                print("pair", w, r, eps, k, "labelled_same", labelled_same, "census_same", cw == cr, flush=True)
    # plant P2: each word against the next word of the same length that is neither it nor its reverse
    p2_diff, p2_n = 0, 0
    for idx, ((eps, w, k), cw) in enumerate(multisets):
        others = [(e2, w2, k2, c2) for (e2, w2, k2), c2 in multisets if e2 == eps and k2 == k and len(w2) == len(w)
                  and w2 != w and rot_class(w2[::-1]) != w]
        if not others: continue
        p2_n += 1; p2_diff += (others[0][3] != cw)
    res["plants"]["P2 census differs for an unrelated word"] = [p2_diff, p2_n]
    P = res["pairs"]
    res["summary"] = {
        "census_levels": len(res["census"]),
        "levels_with_11": sum(1 for c in res["census"] if c["census"].get("11", 0) > 0),
        "pairs_tested": len(P), "skipped_levels_N_over_60": len(res.get("skipped", [])),
        "labelled_differs": sum(not p["labelled_same"] for p in P),
        "census_same": sum(p["census_same"] for p in P),
        "outcome": ("1" if all(p["census_same"] for p in P) and any(not p["labelled_same"] for p in P)
                    else "2" if not all(p["census_same"] for p in P) else "3")}
    json.dump(res, open(out_path, "w"), indent=1)
    print(json.dumps(res["summary"], indent=1)); print(json.dumps(res["plants"]))


if __name__ == "__main__":
    main()
