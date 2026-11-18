#!/usr/bin/env python3
"""W-P1, step 3's follow-up (W-P1c-F), after its referee read. Data-free; no frame is read.

    python3 -I wp1c_followup.py

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, "Step 3, after its referee read" (committed before this
script). The functions and the words are wp1c_heights.py's: its text is run up to its controls, so nothing of its
output is computed here twice except what this follow-up needs.

  F0  the closed form against the sampling: for y >= 1, a run of a letters starting at rotation k contributes
      2 arccosh(rho / y) when rho > y, rho the radius of M_k's axis (for a run of R, of the letter-swapped word's);
      pooled shares within 2e-4 of the sampled ones, and each word's time above each height within 5e-3;
  F1  the share above height 3: (a) at n = 20, 40, 80; (b) at X = 100, 200, 400; beside B1813's 0.0346 and 0.315 and
      the area's 1/pi;
  F2  (a)'s standard errors at heights 1.118, 2, 3, 4, 6: 1,000 resamples of the 2,000 words, seed 7;
  F3  the time above 1.118, 2, 4, 6 by the length of the run under each excursion (closed form): (a) n = 40, (b) X = 400.
"""
import math
import pathlib

import mpmath as mp
import numpy as np

src = (pathlib.Path(__file__).resolve().parent / "wp1c_heights.py").read_text()
exec(compile(src[:src.index("# H0: controls")], "wp1c_heights.py", "exec"))

YS = (math.sqrt(5) / 2 + 1e-9, 2.0, 3.0, 4.0, 6.0)
YN = ("1.118", "2", "3", "4", "6")
SWAP = str.maketrans("LR", "RL")


def runs(word):
    """the maximal cyclic runs: (start index, letter, length)"""
    n = len(word)
    k0 = next(i for i in range(n) if word[i] != word[i - 1])
    out, i = [], 0
    while i < n:
        k = (k0 + i) % n
        a = 1
        while a < n and word[(k + a) % n] == word[k]:
            a += 1
        out.append((k, word[k], a))
        i += a
    return out


def closed(word):
    """per run: (length a, rho); the time above y is the sum of 2 arccosh(rho / y) over runs with rho > y"""
    out = []
    for k, c, a in runs(word):
        w = word if c == "L" else word.translate(SWAP)
        y, x = ends(mat(w[k:] + w[:k]))
        out.append((a, float((x - y) / 2)))
    return out


def above_closed(rs, Y):
    return sum(2 * math.acosh(r / Y) for a, r in rs if r > Y)


def words_a(n, seed):
    rng = np.random.default_rng(seed)
    words = []
    while len(words) < N_WORDS:
        w = "".join(rng.choice(["L", "R"], size=n))
        if len(set(w)) == 2:
            words.append(w)
    return words


def per_word(words):
    """sampled time above each height and the length, per word; and the closed form's time above each height"""
    A = np.zeros((len(words), len(YS))); C = np.zeros_like(A); Ln = np.zeros(len(words))
    rs_all = []
    for i, w in enumerate(words):
        h, wt, total, ell = thread(w)
        Ln[i] = wt.sum()
        rs = closed(w)
        rs_all.append(rs)
        for j, Y in enumerate(YS):
            A[i, j] = wt[h > Y].sum()
            C[i, j] = above_closed(rs, Y)
    return A, C, Ln, rs_all


def carry(rs_all, Y, tot):
    by = {b: 0.0 for b in BINS}
    for rs in rs_all:
        for a, r in rs:
            if r > Y:
                by[bin_of(a)] += 2 * math.acosh(r / Y)
    return ", ".join("%s: %.3f" % (b, by[b] / tot) for b in BINS)


store = {}
worst_pool, worst_word = 0.0, 0.0
for n, seed in ((20, 1), (40, 2), (80, 3)):
    A, C, Ln, rs_all = per_word(words_a(n, seed))
    store[("a", n)] = (A, C, Ln, rs_all)
for X in (100, 200, 400):
    A, C, Ln, rs_all = per_word(lyndon_words(X))
    store[("b", X)] = (A, C, Ln, rs_all)
for key, (A, C, Ln, rs_all) in store.items():
    sp, sc = A.sum(0) / Ln.sum(), C.sum(0) / Ln.sum()
    worst_pool = max(worst_pool, float(np.abs(sp - sc).max()))
    worst_word = max(worst_word, float(np.abs(A - C).max()))
    print("F0 %s %d: sampled %s; closed form %s" % (key[0], key[1], ["%.5f" % v for v in sp], ["%.5f" % v for v in sc]))
print("F0: heights %s; worst pooled difference %.1e (bound 2e-4): %s; worst per-word difference %.1e (bound 5e-3): %s" % (
    "/".join(YN), worst_pool, worst_pool < 2e-4, worst_word, worst_word < 5e-3))

for key, (A, C, Ln, rs_all) in store.items():
    print("F1 %s %d: share above 3, sampled %.5f, closed form %.5f" % (key[0], key[1], A[:, 2].sum() / Ln.sum(),
                                                                      C[:, 2].sum() / Ln.sum()))
print("F1: B1813: 0.0346 move by move; 0.315 at trace <= 400 by length; the area 1/pi = %.5f" % (1 / math.pi))

rng = np.random.default_rng(7)
for n in (20, 40, 80):
    A, C, Ln, rs_all = store[("a", n)]
    N = len(Ln)
    sh = np.empty((1000, len(YS)))
    for b in range(1000):
        idx = rng.integers(0, N, size=N)
        sh[b] = A[idx].sum(0) / Ln[idx].sum()
    print("F2 (a) n = %d: shares above %s: %s; standard errors %s" % (
        n, "/".join(YN), ["%.5f" % v for v in A.sum(0) / Ln.sum()], ["%.5f" % v for v in sh.std(0, ddof=1)]))

for lab, key in (("(a) n = 40", ("a", 40)), ("(b) X = 400", ("b", 400))):
    A, C, Ln, rs_all = store[key]
    for j in (0, 1, 3, 4):
        tot = C[:, j].sum()
        print("F3 %s, above %s, by the run under each excursion: %s" % (lab, YN[j], carry(rs_all, YS[j], tot)))
