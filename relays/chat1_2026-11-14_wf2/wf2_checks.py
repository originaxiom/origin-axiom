#!/usr/bin/env python3
"""W-F2: mirrors or half-turns. Which realisation of three free distinctions lets a history run? Data-free, this seat's code.

    python3 -I -u wf2_checks.py

DEFINITIONS
  W3 = <a, b, c | a^2 = b^2 = c^2 = 1>; words are reduced strings with no letter twice in a row; a word's inverse is its
  reverse. Two cyclically reduced words (first letter != last letter, or length <= 1) are conjugate exactly when one is a
  rotation of the other (free products). The even part F2 = <x = ab, y = bc>.
  The same abstract group has two geometric realisations, and each fixes which elements are peripheral (the cusps):
    mirrors (the reflection group of an ideal triangle): the three pair products ab, bc, ca, each a cusp;
      the even part is the thrice-punctured sphere;
    half-turns (the once-punctured torus over the sphere with three cone points of order 2 and one puncture): the
      triple product abc, the one puncture; the even part is the once-punctured torus, whose cusp is [x, y] ~ (abc)^-2.
  A re-description (a substitution of a, b, c; W-F1's seven moves) is a history step of the realisation when it carries
  that realisation's peripheral classes to peripheral classes (each up to conjugacy and inverse).
  Its matrix is its action on H1 of the even part in the basis x, y (as in W-F1).

EXPECTATIONS, written before the run:
  M1  Every product of at most 4 of the seven moves (2,800 products) carries (abc)^2 to a conjugate of (abc)^2 or of
      (abc)^-2: every re-description is a history step of the half-turn realisation.
  M2  The products that carry the three pair classes {ab, bc, ca} to themselves (up to conjugacy and inverse) induce,
      up to sign, at most 6 distinct matrices on H1, every one of finite order: the mirror realisation's steps form a
      finite group, so no aperiodic history runs on it.
  M3  Some products induce a hyperbolic matrix (|trace| > 2); none of those carries the pair classes to themselves.
  Controls: the swap of a and b carries the pair classes to themselves (it must pass M2's test); "a through b" does not
  (it must fail it). Planted error: a peripheral test that compares words exactly, without conjugacy, must reject the
  swap of a and b on the half-turn cusp (abc -> bac is a conjugate of (abc)^-1, not equal to it).
"""
import itertools

import numpy as np


def say(*a):
    print(*a, flush=True)


def red(w):
    out = []
    for ch in w:
        if out and out[-1] == ch:
            out.pop()
        else:
            out.append(ch)
    return "".join(out)


def cyc_red(w):
    w = red(w)
    while len(w) >= 2 and w[0] == w[-1]:
        w = w[1:-1]
    return w


def conj(u, v):
    u, v = cyc_red(u), cyc_red(v)
    return len(u) == len(v) and (len(u) == 0 or u in v + v)


def conj_pm(u, v):
    return conj(u, v) or conj(u, v[::-1])


MOVES = {
    "swap a,b": {"a": "b", "b": "a", "c": "c"}, "swap b,c": {"a": "a", "b": "c", "c": "b"},
    "swap a,c": {"a": "c", "b": "b", "c": "a"}, "a through b": {"a": "bab", "b": "b", "c": "c"},
    "b through a": {"a": "a", "b": "aba", "c": "c"}, "c through b": {"a": "a", "b": "b", "c": "bcb"},
    "b through c": {"a": "a", "b": "cbc", "c": "c"},
}


def compose(f, g):  # f o g: apply g, then f
    return {ch: red("".join(f[d] for d in g[ch])) for ch in "abc"}


def img(f, w):
    return red("".join(f[ch] for ch in w))


PAIR = {"ab": (1, 0), "ba": (-1, 0), "bc": (0, 1), "cb": (0, -1), "ac": (1, 1), "ca": (-1, -1)}


def ab3(w):
    v = [0, 0]
    for i in range(0, len(w), 2):
        p = w[i:i + 2]
        v[0] += PAIR[p][0]
        v[1] += PAIR[p][1]
    return v


def matrix(f):
    return np.array([ab3(img(f, "ab")), ab3(img(f, "bc"))]).T


def finite_order(M):
    P, n = M.copy(), 1
    while n <= 12:
        if np.array_equal(P, np.eye(2, dtype=int)) or np.array_equal(P, -np.eye(2, dtype=int)):
            return True
        P = P @ M
        n += 1
    return False


PAIRS = ["ab", "bc", "ca"]


def keeps_pairs(f):
    imgs = [img(f, p) for p in PAIRS]
    return all(any(conj_pm(i, p) for p in PAIRS) for i in imgs) and \
        len({next(k for k, p in enumerate(PAIRS) if conj_pm(i, p)) for i in imgs}) == 3


def keeps_puncture(f):
    return conj_pm(img(f, "abcabc"), "abcabc")


prods = []
for r in range(1, 5):
    for combo in itertools.product(MOVES, repeat=r):
        f = {ch: ch for ch in "abc"}
        for k in combo:
            f = compose(f, MOVES[k])
        prods.append((combo, f))
say("products of at most 4 moves:", len(prods))

m1 = all(keeps_puncture(f) for _, f in prods)
say("M1 every product keeps the half-turn puncture (abc)^2 up to conjugacy and inverse:", m1)

mirror_steps = [(c, f) for c, f in prods if keeps_pairs(f)]
mats = set()
for _, f in mirror_steps:
    M = matrix(f)
    key = min(tuple(M.ravel()), tuple((-M).ravel()))
    mats.add(key)
fin = all(finite_order(np.array(k).reshape(2, 2)) for k in mats)
say("M2 products keeping the three pair cusps:", len(mirror_steps), "; distinct matrices up to sign:", len(mats),
    "; all of finite order:", fin, "; matrices:", sorted(mats))
say("M2 holds:", len(mats) <= 6 and fin)

hyper = [(c, f) for c, f in prods if abs(int(np.trace(matrix(f)))) > 2]
say("M3 products with a hyperbolic matrix:", len(hyper), "; of them keeping the pair cusps:",
    sum(keeps_pairs(f) for _, f in hyper), "; holds:", len(hyper) > 0 and not any(keeps_pairs(f) for _, f in hyper))
say("M3 example:", hyper[0][0] if hyper else None, matrix(hyper[0][1]).tolist() if hyper else None)

say("control: swap a,b keeps the pair cusps:", keeps_pairs(MOVES["swap a,b"]),
    "; a through b keeps them:", keeps_pairs(MOVES["a through b"]))
exact = lambda f: img(f, "abc") in ("abc", "cba")
say("planted error: an exact-word test accepts swap a,b on the half-turn cusp:", exact(MOVES["swap a,b"]),
    "; the conjugacy test accepts it:", conj_pm(img(MOVES["swap a,b"], "abc"), "abc"))
