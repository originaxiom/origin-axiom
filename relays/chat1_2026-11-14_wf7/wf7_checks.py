#!/usr/bin/env python3
"""W-F7: the mixed faces of three distinctions. Data-free; this seat's own code.

The helpers (reduction, conjugacy in W_3, the seven moves, composition, the matrix on H_1 of the even part, finite
order) are taken by text from W-F2's sealed script (definitions only, up to its census), which is not re-run.

    python3 -I -u wf7_checks.py

DEFINITIONS
  W_3 = <a, b, c | a^2, b^2, c^2>. A face is a choice, for each letter, of mirror (M) or half-turn (H), and its corners:
    MMM (mirrors a, b, c): corners <a, b>, <b, c>, <c, a>; rotation elements ab, bc, ca (W-F2's mirror face).
    HHH (half-turns a, b, c): the one puncture abc; tested, as in W-F2, through (abc)^2.
    MMH (mirrors p, q, half-turn r): a disc with one cone point and two ideal corners <p, q> and <q, rpr>; rotation
      elements pq and q r p r. Three labellings (r = a, b, c).
    MHH (mirror p, half-turns q, r): a disc with two cone points and one ideal corner <p, (qr) p (qr)^-1>; rotation
      element p q r p r q. Three labellings (p = a, b, c).
  A history step of a face is a product f of W-F2's seven moves (at most four; 2,800 products) that sends each mirror
  to a conjugate of a mirror and each half-turn to a conjugate of a half-turn (bijectively on the classes), and the
  face's rotation elements to its rotation elements up to conjugacy and inverse (bijectively). Its matrix is its action
  on H_1 of the even part <x = ab, y = bc>. Hyperbolic: |trace| > 2. Parabolic: |trace| = 2 and the matrix is not +-I.

EXPECTATIONS, written before the run (derived by hand: the mapping class groups of the four faces are S_3-like and
finite for MMM and MMH, contain the half-twist of the two cone points for MHH, which acts by R = [[1, 0], [1, 1]] up to
conjugacy and sign, and contain every hyperbolic element for HHH):
  W1  MMM (control): 538 steps, every step's matrix of finite order, 6 distinct matrices up to sign (W-F2, M2).
  W2  HHH (control): every one of the 2,800 products is a step, and 380 of them have a hyperbolic matrix (W-F2, M1, M3).
  W3  MMH, each labelling: every step's matrix has finite order; no step is parabolic or hyperbolic.
  W4  MHH, each labelling: no step is hyperbolic; some step is parabolic (the half-twist of the two half-turns, a product
      of two moves, e.g. "swap b,c" after "c through b" when a is the mirror).
"""
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wf2", "wf2_checks.py")).read()
ns = {}
exec(SRC.split("prods = []")[0], ns)
red, conj, conj_pm, MOVES, compose, img = ns["red"], ns["conj"], ns["conj_pm"], ns["MOVES"], ns["compose"], ns["img"]
matrix, finite_order, say, itertools = ns["matrix"], ns["finite_order"], ns["say"], ns["itertools"]

prods = []
for r in range(1, 5):
    for combo in itertools.product(MOVES, repeat=r):
        f = {ch: ch for ch in "abc"}
        for k in combo:
            f = compose(f, MOVES[k])
        prods.append((combo, f))
say("products of at most 4 moves:", len(prods))


def keeps_classes(f, mirrors):
    halves = [ch for ch in "abc" if ch not in mirrors]
    for group in (mirrors, halves):
        targets = []
        for ch in group:
            t = [g for g in group if conj(img(f, ch), g)]
            if not t:
                return False
            targets.append(t[0])
        if len(set(targets)) != len(group):
            return False
    return True


def keeps_rot(f, rots):
    imgs = [img(f, w) for w in rots]
    idx = []
    for i in imgs:
        t = [k for k, w in enumerate(rots) if conj_pm(i, w)]
        if not t:
            return False
        idx.append(t[0])
    return len(set(idx)) == len(rots)


def face(kind, lab):
    if kind == "MMM":
        return "abc", ["ab", "bc", "ca"]
    if kind == "HHH":
        return "", ["abcabc"]
    if kind == "MMH":
        r = lab
        p, q = [ch for ch in "abc" if ch != r]
        return p + q, [p + q, q + r + p + r]
    p = lab
    q, r = [ch for ch in "abc" if ch != p]
    return p, [p + q + r + p + r + q]


def census(kind, lab):
    mirrors, rots = face(kind, lab)
    steps = [(c, f) for c, f in prods if keeps_classes(f, mirrors) and keeps_rot(f, rots)]
    mats, hyp, par, fin = set(), 0, 0, 0
    for _, f in steps:
        Mx = matrix(f)
        tr = abs(int(Mx[0, 0] + Mx[1, 1]))
        mats.add(min(tuple(Mx.ravel()), tuple((-Mx).ravel())))
        hyp += tr > 2
        is_pm_id = np.array_equal(Mx, np.eye(2, dtype=int)) or np.array_equal(Mx, -np.eye(2, dtype=int))
        par += tr == 2 and not is_pm_id
        fin += finite_order(Mx)
    return dict(steps=len(steps), matrices=len(mats), hyperbolic=hyp, parabolic=par, finite_order=fin)


res = {}
for kind, labs in (("MMM", [""]), ("HHH", [""]), ("MMH", list("abc")), ("MHH", list("abc"))):
    for lab in labs:
        res[(kind, lab)] = census(kind, lab)
        say(kind, "labelling", lab or "-", res[(kind, lab)])

w1 = res[("MMM", "")]["finite_order"] == res[("MMM", "")]["steps"] == 538 and res[("MMM", "")]["matrices"] == 6
w2 = res[("HHH", "")]["steps"] == 2800 and res[("HHH", "")]["hyperbolic"] == 380
w3 = all(res[("MMH", l)]["finite_order"] == res[("MMH", l)]["steps"] and res[("MMH", l)]["hyperbolic"] == 0
         and res[("MMH", l)]["parabolic"] == 0 for l in "abc")
w4 = all(res[("MHH", l)]["hyperbolic"] == 0 and res[("MHH", l)]["parabolic"] > 0 for l in "abc")
half_twist = compose(MOVES["swap b,c"], MOVES["c through b"])
say("the half-twist (a mirror; b, c half-turns):", half_twist, "; matrix", matrix(half_twist).tolist(),
    "; a step of MHH(a):", keeps_classes(half_twist, "a") and keeps_rot(half_twist, face("MHH", "a")[1]))
say("W1 holds:", w1)
say("W2 holds:", w2)
say("W3 holds:", w3)
say("W4 holds:", w4)
