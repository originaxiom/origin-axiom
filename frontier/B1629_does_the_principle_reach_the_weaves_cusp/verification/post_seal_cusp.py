#!/usr/bin/env python3
"""B1629 -- POST-SEAL REPAIR (disclosed in FINDINGS).  The sealed `cusp_reach.py` measured a geodesic's top only at the cusp's
representative at infinity (radius sqrt(tr^2 - 4) / (2|c|) over the word's rotations), so long runs of L -- which climb the
same cusp of the modular surface, seen from 0 -- read as low; it took no minimum over threads; and its measure cell read
the highest point reached, not the time spent near the cusp.  This repair:
 P1  the symmetric top: max over rotations of sqrt(tr^2 - 4) / (2 min(|b|, |c|)) (both cusp representatives, infinity
     and 0, related by S);
 P2  L^k R and L^k R^k for k <= 12 (a long run climbs), and the min and max symmetric top over every primitive thread
     of length <= 14 (is the tick LR the lowest?);
 P3  the clock's word read as moves: linear and cyclic longest runs, and the symmetric tops of its prefix words;
 P4  a time-near-the-cusp proxy for the weave's uniform measure: the fraction of LETTERS lying in a run of length >= k,
     over all primitive cyclic threads of length n = 10 ... 18, for k = 2 ... 8 (a letter deep in a long run is the
     geodesic deep in the cusp, by the continued-fraction coding).
Writes post_seal_cusp.json."""
import json, pathlib, itertools, math, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cr", HERE / "cusp_reach.py"); cr = importlib.util.module_from_spec(spec); spec.loader.exec_module(cr)


def sym_top(word):
    best = 0.0
    for k in range(len(word)):
        M = cr.mat(word[k:] + word[:k]); a, b, c, d = (int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1]))
        tr = a + d
        if tr * tr <= 4: continue
        m = min(abs(b), abs(c))
        if m == 0: continue
        best = max(best, math.sqrt(tr * tr - 4) / (2 * m))
    return best


def run_lengths(word):
    """cyclic runs: list of (letter, length)"""
    n = len(word); k = 0
    while k < n and word[k] == word[k - 1]: k += 1
    w = word[k:] + word[:k]; out = []; cur = 1
    for i in range(1, n + 1):
        if i < n and w[i] == w[i - 1]: cur += 1
        else: out.append(cur); cur = 1
    return out


def main():
    out = {}
    out["P2"] = {"L^k R": {k: round(sym_top("L" * k + "R"), 4) for k in range(1, 13)},
                 "L^k R^k": {k: round(sym_top("L" * k + "R" * k), 4) for k in range(1, 9)}}
    tops = {}
    for n in range(2, 15):
        for w in cr.primitive_cyclic_words(n): tops[w] = sym_top(w)
    lo = min(tops.values()); hi = max(tops.values())
    out["P2"].update({"threads_len_le_14": len(tops), "min_top": round(lo, 6), "argmin": sorted(w for w, t in tops.items() if abs(t - lo) < 1e-9)[:4],
                      "max_top": round(hi, 4), "LR_top": round(sym_top("LR"), 6), "LR_is_lowest": abs(sym_top("LR") - lo) < 1e-9,
                      "second_lowest": round(sorted(set(round(t, 9) for t in tops.values()))[1], 6)})
    F = [1, 2]
    while F[-1] < 6765: F.append(F[-1] + F[-2])
    rule = cr.fib_word(F[-1]).replace("a", "L").replace("b", "R")
    lin = {ch: max(len(m) for m in __import__("re").findall(ch + "+", rule)) for ch in "LR"}
    pre = [rule[:n] for n in range(2, 160) if "R" in rule[:n]]
    out["P3"] = {"linear_longest_runs": lin, "cyclic_longest_runs_over_prefixes": {ch: max(cr.runs(p)[ch] for p in pre) for ch in "LR"},
                 "prefix_words_symmetric_top_max": round(max(sym_top(p) for p in pre[:110]), 6)}
    p4 = {}
    for n in range(10, 19, 2):
        ws = cr.primitive_cyclic_words(n); tot = n * len(ws)
        row = {}
        for k in range(2, 9):
            inlong = sum(sum(r for r in run_lengths(w) if r >= k) for w in ws)
            row[k] = round(inlong / tot, 6)
        p4[n] = row
    out["P4_fraction_of_letters_in_runs_ge_k"] = p4
    json.dump(out, open(HERE / "post_seal_cusp.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
