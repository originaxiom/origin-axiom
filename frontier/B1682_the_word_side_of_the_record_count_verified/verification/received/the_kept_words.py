"""W110: the checks of the word side of the record count (main's ask C4, relay of 2026-10-20). The proof,
W110_PROOF.md, was committed before this script (6ed2c3373). One run. The proof does not rest on these checks.

C1  Whitehead's count, by direct reduction, for every R_ij^{+-1} and L_ij^{+-1} (the latter through the reversal) on
    every class of the census; and L_ij = rev R_ij rev on every class.
C2  n = 3 to length 8 and n = 4 to length 7: the classes kept by every transvection and by the full moves, exactly and
    up to inversion; the classes keeping their length under every R_ij^{+-1}.
C3  n = 2 to length 12: the classes kept by <L, R>, by the four transvections and by the full moves.
C4  the singular points of the level surface kappa = x^2 + y^2 + z^2 - xyz - 2 = -2.

Run: python3 the_kept_words.py -> the_kept_words.json and the_kept_words_run.txt beside it.
"""
import itertools
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_kept_words.json"
RUN = HERE / "the_kept_words_run.txt"
LINES = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LINES.append(s)


# ---------------------------------------------------------------- words, classes and moves

def inv(w):
    return tuple(-x for x in reversed(w))


def rev(w):
    return tuple(reversed(w))


def free(w):
    st = []
    for x in w:
        if st and st[-1] == -x:
            st.pop()
        else:
            st.append(x)
    return tuple(st)


def cyc(w):
    w = free(w)
    while len(w) >= 2 and w[0] == -w[-1]:
        w = w[1:-1]
    return w


def canon(w):
    if not w:
        return ()
    return min(w[r:] + w[:r] for r in range(len(w)))


def canon_pm(w):
    return min(canon(w), canon(inv(w)))


def apply(phi, w):
    out = []
    for x in w:
        out.extend(phi.get(x, (x,)) if x > 0 else inv(phi.get(-x, (-x,))))
    return free(out)


def R(i, j):
    return {i: (i, j)}


def Rinv(i, j):
    return {i: (i, -j)}


def L(i, j):
    return {i: (j, i)}


def Linv(i, j):
    return {i: (-j, i)}


def inversion(i):
    return {i: (-i,)}


def swap(i, j):
    return {i: (j,), j: (i,)}


def classes(n, lmax):
    """one representative per conjugacy class up to inversion: the cyclically reduced words of length 1..lmax equal to
    their own canon_pm"""
    letters = [x for k in range(1, n + 1) for x in (k, -k)]
    reps = []

    def rec(w):
        if w and w[0] != -w[-1] and canon_pm(w) == w:
            reps.append(w)
        if len(w) == lmax:
            return
        for x in letters:
            if w and w[-1] == -x:
                continue
            rec(w + (x,))
    rec(())
    return reps


def kept(w, moves, up_to_inv):
    cw, ciw = canon(w), canon(inv(w))
    for phi in moves:
        cv = canon(cyc(apply(phi, w)))
        if cv == cw or (up_to_inv and cv == ciw):
            continue
        return False
    return True


def counts(w, i, j):
    m = len(w)
    pairs = [(w[p], w[(p + 1) % m]) for p in range(m)]
    c = sum(1 for p in pairs if p in ((i, -j), (j, -i)))
    cp = sum(1 for p in pairs if p in ((i, j), (-j, -i)))
    ni = sum(1 for x in w if abs(x) == i)
    return m, ni, c, cp


def move_sets(n):
    pairs = list(itertools.permutations(range(1, n + 1), 2))
    trans = [R(i, j) for i, j in pairs] + [L(i, j) for i, j in pairs]
    full = trans + [inversion(i) for i in range(1, n + 1)] + [swap(i, j) for i, j in itertools.combinations(
        range(1, n + 1), 2)]
    sets = {"transvections": trans, "full": full}
    if n == 2:
        sets = {"<L, R>": [R(1, 2), L(2, 1)], **sets}
    return pairs, sets


# ---------------------------------------------------------------- the census

def census(n, lmax):
    reps = classes(n, lmax)
    pairs, sets = move_sets(n)
    lemma_bad, rev_bad = [], 0
    length_kept = []
    for w in reps:
        all_len = True
        for i, j in pairs:
            m, ni, c, cp = counts(w, i, j)
            lr, lri = len(cyc(apply(R(i, j), w))), len(cyc(apply(Rinv(i, j), w)))
            if lr != m + ni - 2 * c or lri != m + ni - 2 * cp:
                lemma_bad.append([list(w), i, j, "R"])
            m2, ni2, c2, cp2 = counts(rev(w), i, j)
            ll, lli = len(cyc(apply(L(i, j), w))), len(cyc(apply(Linv(i, j), w)))
            if ll != m2 + ni2 - 2 * c2 or lli != m2 + ni2 - 2 * cp2:
                lemma_bad.append([list(w), i, j, "L"])
            if apply(L(i, j), w) != rev(apply(R(i, j), rev(w))):
                rev_bad += 1
            if lr != m or lri != m:
                all_len = False
        if all_len:
            length_kept.append(w)
    res = {"n": n, "max length": lmax, "classes up to inversion": len(reps),
           "lemma failures": len(lemma_bad), "lemma failures (first five)": lemma_bad[:5],
           "L = rev R rev failures": rev_bad,
           "classes keeping their length under every R_ij^{+-1}": len(length_kept),
           "those classes (first ten)": [list(w) for w in length_kept[:10]], "kept": {}}
    for name, moves in sets.items():
        for crit, up in (("exactly", False), ("up to inversion", True)):
            k = [w for w in reps if kept(w, moves, up)]
            res["kept"][f"{name}, {crit}"] = {"count": len(k), "classes (first ten)": [list(w) for w in k[:10]]}
    say(f"census n = {n} to length {lmax}: {len(reps)} classes; lemma failures {len(lemma_bad)}; rev failures "
        f"{rev_bad}; length kept by every R_ij^±1: {len(length_kept)}")
    for key, v in res["kept"].items():
        say(f"  kept, {key}: {v['count']}", v["classes (first ten)"] if v["count"] else "")
    return res


def main():
    out = {"status": "one run", "proof": "W110_PROOF.md (6ed2c3373)", "cells": {}}
    c3, c2a, c2b = census(2, 12), census(3, 8), census(4, 7)
    out["census"] = {"n = 2": c3, "n = 3": c2a, "n = 4": c2b}
    out["cells"]["C1"] = all(r["lemma failures"] == 0 and r["L = rev R rev failures"] == 0 for r in (c3, c2a, c2b))
    out["cells"]["C2"] = all(r["classes keeping their length under every R_ij^{+-1}"] == 0
                             and all(v["count"] == 0 for v in r["kept"].values()) for r in (c2a, c2b))
    comm = sorted(canon_pm((1, 2, -1, -2) * k) for k in (1, 2, 3))
    ok3 = True
    for key, v in c3["kept"].items():
        want = [] if key == "full, exactly" else comm
        got = sorted(tuple(w) for w in v["classes (first ten)"])
        ok3 = ok3 and got == want and v["count"] == len(want)
    out["cells"]["C3"] = ok3
    out["C3 expected classes"] = [list(w) for w in comm]
    x, y, z = sp.symbols("x y z")
    kappa = x ** 2 + y ** 2 + z ** 2 - x * y * z - 2
    sing = sp.solve([sp.diff(kappa, v) for v in (x, y, z)] + [kappa + 2], [x, y, z], dict=True)
    pts = sorted(tuple(str(s.get(v, v)) for v in (x, y, z)) for s in sing)
    out["C4"] = {"singular points of kappa = -2": pts}
    out["cells"]["C4"] = pts == [("0", "0", "0")]
    say("C4 singular points of kappa = -2:", pts)
    say("cells:", out["cells"])
    OUT.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    RUN.write_text("\n".join(LINES) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
