#!/usr/bin/env python3
"""SM-C6 E1, the owed step 4: the audit lane's criterion (B1457's harvest, AR1: "For surjective q, T descends iff
q(x)=q(x') implies q(Tx)=q(Tx'). An output O separately descends iff it is constant on q-fibres. Both conditions
preserve every finite future observation."; OPEN_LEADS: "the register survives exactly when both the updates and the
declared outputs descend"), re-derived with own code, then applied to E1's two drop points.
  A. Exhaustively, on every small system (states <= 4, one update, a binary output; states <= 3, two updates) and every
     quotient q (set partition):
       sep  = every update and the output descend along q;
       obs  = every finite future observation O(T_w x) is constant on q-fibres;
       bis  = q's fibres lie in the classes of observational equivalence (the largest bisimulation);
     checked: sep => obs always; obs <=> bis always; and whether obs => sep (the "exactly when").
  B. Word -> manifold (B1456's quotient: rotations and the reverse): the update "append a letter" descends, checked on
     every word to length 10; E1's outputs: the census descends, the labelled count does not (E1 levels 1 and 2).
  C. Module -> vacuum (forgetting which piece is the sub): the fibre of V(l, alpha) is {V(l, alpha), V(1/l, beta)};
     E2 found the second swaps (n, n*) on every level, so the based count descends exactly on its n = n* modules.
    python3 run_e1_criterion.py [out.json]"""
import sys, json, itertools, pathlib
HERE = pathlib.Path(__file__).resolve().parent


def partitions(n):
    """all set partitions of range(n) as label lists"""
    def rec(i, labels, k):
        if i == n: yield tuple(labels); return
        for c in range(k + 1):
            yield from rec(i + 1, labels + [c], max(k, c + 1))
    yield from rec(0, [], 0)


def bisim(n, Ts, O):
    """the largest bisimulation (observational equivalence) as a label list, by partition refinement"""
    lab = list(O)
    while True:
        sig = [(lab[x],) + tuple(lab[T[x]] for T in Ts) for x in range(n)]
        idx = {s: i for i, s in enumerate(sorted(set(sig)))}
        new = [idx[s] for s in sig]
        if len(set(new)) == len(set(lab)): return new
        lab = new


def obs_descends(n, Ts, O, q):
    """every finite future observation constant on q-fibres: brute force on words of length < n * n + 1"""
    L = n * n
    for x, y in itertools.combinations(range(n), 2):
        if q[x] != q[y]: continue
        frontier = {(x, y)}; seen = set()
        while frontier:
            a, b = frontier.pop()
            if (a, b) in seen: continue
            seen.add((a, b))
            if O[a] != O[b]: return False
            for T in Ts: frontier.add((T[a], T[b]))
    return True


def part_A():
    stats = {"systems": 0, "sep_implies_obs_fail": 0, "obs_iff_bis_fail": 0, "obs_without_sep": 0, "example": None}
    for n, nT in ((2, 1), (3, 1), (4, 1), (2, 2), (3, 2)):
        maps = list(itertools.product(range(n), repeat=n))
        for Ts in itertools.product(maps, repeat=nT):
            for O in itertools.product((0, 1), repeat=n):
                B = bisim(n, Ts, O)
                for q in partitions(n):
                    stats["systems"] += 1
                    sep = all(q[x] != q[y] or (q[T[x]] == q[T[y]]) for T in Ts for x in range(n) for y in range(n)) \
                        and all(q[x] != q[y] or O[x] == O[y] for x in range(n) for y in range(n))
                    obs = obs_descends(n, Ts, O, q)
                    bis = all(q[x] != q[y] or B[x] == B[y] for x in range(n) for y in range(n))
                    stats["sep_implies_obs_fail"] += sep and not obs
                    stats["obs_iff_bis_fail"] += obs != bis
                    if obs and not sep:
                        stats["obs_without_sep"] += 1
                        if stats["example"] is None:
                            stats["example"] = {"states": n, "updates": [list(T) for T in Ts], "output": list(O), "q": list(q)}
    return stats


def canon(w):
    rots = [w[i:] + w[:i] for i in range(len(w))]
    r = w[::-1]
    return min(rots + [r[i:] + r[:i] for i in range(len(r))])


def part_B():
    bad = tested = 0
    for n in range(2, 11):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w: continue
            for X in "LR":
                tested += 1
                bad += canon(w + X) != canon(w[::-1] + X)
    e1 = json.load(open(HERE / "e1_results.json")); e2l = json.load(open(HERE / "e1_level2_results.json"))
    seen, tests = set(), []
    for p in e1["pairs"] + [p for p in e2l["pairs"] if p["level"] == 2]:   # e1 lists each level-1 pair in both orders
        key = (frozenset((p["word"], p["reverse"])), p["sign"], p["level"])
        if key not in seen: seen.add(key); tests.append(p)
    return {"append_descends": {"tested": tested, "fails": bad},
            "census_descends_on": [sum(p["census_same"] for p in tests), len(tests)],
            "labelled_count_descends_on": [sum(p["labelled_same"] for p in tests), len(tests)]}


def part_C():
    e2 = json.load(open(HERE / "e2_results.json"))["summary"]
    e1 = json.load(open(HERE / "e1_results.json"))["census"]
    tot = sum(sum(c["census"].values()) for c in e1)
    eq = sum(c["census"].get("00", 0) + c["census"].get("11", 0) for c in e1)
    return {"O_swaps_n_and_nstar_on_every_level (E2)": e2["O_swaps_everywhere"],
            "modules_on_census_levels": tot, "based_count_descends_on (n = n*)": eq,
            "based_count_does_not_descend_on (n != n*)": tot - eq}


def main():
    out_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "e1_criterion_results.json"
    A = part_A(); Bp = part_B(); C = part_C()
    res = {"A_lemma": A, "B_word_to_manifold": Bp, "C_module_to_vacuum": C,
           "summary": {"sufficient (sep => obs) on every system": A["sep_implies_obs_fail"] == 0,
                       "exact condition (obs <=> fibres inside observational equivalence) on every system": A["obs_iff_bis_fail"] == 0,
                       "'exactly when' holds as stated": A["obs_without_sep"] == 0,
                       "append descends to the manifold": Bp["append_descends"]["fails"] == 0}}
    json.dump(res, open(out_path, "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
