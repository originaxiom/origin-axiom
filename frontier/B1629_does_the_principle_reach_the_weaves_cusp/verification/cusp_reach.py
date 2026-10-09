#!/usr/bin/env python3
"""B1629 -- DOES THE PRINCIPLE REACH THE WEAVE'S CUSP?  The SM seat's W45 and W46 put the weave's chiral count at the cusp
of its own surface (one unit of end data there gives n times the fibre's index; the natural condition gives n = 0), and
the owner's ruling keeps FK10 open.  This arc asks whether any datum the principle forces visits that cusp.  On the
modular surface a thread (a positive primitive word w in L = [[1,0],[1,1]], R = [[1,1],[0,1]] with both letters) is a
closed geodesic, and the height it reaches up the cusp is governed by its longest run of one letter.  Exact up to
floating point; no data.
 C1  the rule's own words: the prefixes of the fixed-point word of a -> ab, b -> a (a -> L, b -> R), read cyclically, up
     to length F_20; the longest run of each letter over all of them.
 C2  the closed geodesics' heights: for a hyperbolic M in SL(2, Z), its axis has endpoints the fixed points x+ and x- of
     the Moebius map; the top of the geodesic over the cyclic rotations of w is max (|x+ - x-| / 2) taken over the
     conjugates by the rotations.  (i) the heights of the rule's prefix words, against (ii) every primitive positive
     word with both letters of length <= 14, and (iii) the family L^k R for k <= 12 (one long run), to show what a run
     does.
 C3  the weave's uniform measure: over all primitive cyclic positive words with both letters of length n (n = 10 ... 18),
     the fraction whose top lies above height Y for Y = 2, 4, 8 -- whether it tends to zero with Y (no atom at the cusp).
 C4  the cusp's own monodromy: the single move L has trace 2 (parabolic); every thread has trace >= 3; the tick
     sigma^2 = LR has trace 3.
Writes cusp_reach.json."""
import json, pathlib, itertools, math
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
L = np.array([[1, 0], [1, 1]], dtype=object); R = np.array([[1, 1], [0, 1]], dtype=object)


def mat(word):
    M = np.array([[1, 0], [0, 1]], dtype=object)
    for ch in word: M = M.dot(L if ch == "L" else R)
    return M


def top_height(word):
    best = 0.0
    for k in range(len(word)):
        w = word[k:] + word[:k]
        M = mat(w); a, b, c, d = (int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1]))
        tr = a + d
        if c == 0 or tr * tr <= 4: continue
        disc = math.sqrt(tr * tr - 4)
        xp, xm = ((a - d) + disc) / (2 * c), ((a - d) - disc) / (2 * c)
        best = max(best, abs(xp - xm) / 2)
    return best


def runs(word):
    """longest cyclic run of each letter"""
    w = word + word; out = {}
    for ch in "LR":
        m = cur = 0
        for x in w:
            cur = cur + 1 if x == ch else 0; m = max(m, cur)
        out[ch] = min(m, len(word))
    return out


def fib_word(n):
    w = "a"
    while len(w) < n: w = "".join("ab" if c == "a" else "a" for c in w)
    return w[:n]


def primitive_cyclic_words(n):
    seen = set(); out = []
    for t in itertools.product("LR", repeat=n):
        w = "".join(t)
        if "L" not in w or "R" not in w: continue
        rots = [w[k:] + w[:k] for k in range(n)]
        c = min(rots)
        if c in seen: continue
        seen.add(c)
        if any(n % p == 0 and c == c[:p] * (n // p) for p in range(1, n)): continue
        out.append(c)
    return out


def main():
    out = {}
    F = [1, 2]
    while F[-1] < 6765: F.append(F[-1] + F[-2])
    rule = fib_word(F[-1]).replace("a", "L").replace("b", "R")
    prefixes = [rule[:n] for n in range(2, 200) if "R" in rule[:n]]
    r = {"L": 0, "R": 0}
    for p in [rule[:n] for n in range(2, len(rule) + 1, 97)] + prefixes:
        for ch, v in runs(p).items(): r[ch] = max(r[ch], v)
    out["C1"] = {"word_length": len(rule), "longest_run_L": r["L"], "longest_run_R": r["R"]}
    heights_rule = [top_height(p) for p in prefixes[:120]]
    all14 = [top_height(w) for n in range(2, 15) for w in primitive_cyclic_words(n)]
    lk = {k: round(top_height("L" * k + "R"), 6) for k in range(1, 13)}
    out["C2"] = {"rule_prefix_words_max_top": round(max(heights_rule), 6), "rule_prefix_words_n": len(heights_rule),
                 "all_threads_len_le_14_max_top": round(max(all14), 6), "all_threads_len_le_14_n": len(all14),
                 "L^k R_tops": lk, "LR_top": round(top_height("LR"), 6)}
    c3 = {}
    for n in range(10, 19, 2):
        ws = primitive_cyclic_words(n); tops = [top_height(w) for w in ws]
        c3[n] = {"threads": len(ws), **{f"frac_above_{Y}": round(sum(t > Y for t in tops) / len(tops), 6) for Y in (2, 4, 8)}}
    out["C3"] = c3
    tr = lambda w: int(mat(w)[0, 0] + mat(w)[1, 1])
    out["C4"] = {"trace_L": tr("L"), "trace_LR": tr("LR"),
                 "min_thread_trace_len_le_12": min(tr(w) for n in range(2, 13) for w in primitive_cyclic_words(n))}
    json.dump(out, open(HERE / "cusp_reach.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
