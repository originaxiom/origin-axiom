"""The arena check: the facts the fresh look (docs/A_FRESH_LOOK_FROM_THE_PRINCIPLE_2026-10-15.md) rests on.

A post hoc check of classical mathematics on the record's threads, written for a READING. It has no rule, makes no
prediction and reads no data. It was first run in scratch, then copied here and run once to write the JSON.

  A1  Rademacher's function, from Dedekind sums, equals #R - #L on every thread to length 12 (Ghys: the linking
      number of a thread's modular knot with the trefoil)
  A2  a thread's closed geodesic passes through an image of i exactly when the thread is reciprocal (its cyclic word
      equals its reverse with the letters swapped), on every thread to length 10 (Sarnak)
  A3  the threads to length 10 whose closed geodesic passes through an image of omega
  A4  the root LR passes through i and comes within ln sqrt(5/3) of omega (disk radius 4 - sqrt 15); LLR and LRR pass
      through omega
  A5  the threads grouped by trace (discriminant t^2 - 4): the first classes
  A6  the order-3 move of B1657 and W94 is the trefoil's monodromy: trace 1, order 6, fixes omega; the traces with
      torsion-free H_1 (|2 - t| = 1) are 1 and 3
  A7  Lorenz-braid linking numbers between every two threads to length 8: positive integers, mirror-invariant

Run: python3 the_arena_check.py  ->  the_arena_check.json beside it.
"""
import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_arena_check.json"
L = ((1, 0), (1, 1))
R = ((1, 1), (0, 1))
OMEGA = complex(-0.5, math.sqrt(3) / 2)


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def word_mat(w):
    M = ((1, 0), (0, 1))
    for ch in w:
        M = mul(M, L if ch == "L" else R)
    return M


def canon(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def primitive(w):
    n = len(w)
    return all(not (n % d == 0 and w == w[:d] * (n // d)) for d in range(1, n))


def threads(nmax):
    """primitive cyclic words in L and R with both letters, one per rotation class, by length"""
    out = []
    for n in range(2, nmax + 1):
        seen = set()
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" in w and "R" in w and primitive(w):
                c = canon(w)
                if c not in seen:
                    seen.add(c)
                    out.append(c)
    return out


def swaprev(w):
    return "".join("R" if ch == "L" else "L" for ch in reversed(w))


def dedekind_s(h, k):
    def saw(x):
        return Fr(0) if x.denominator == 1 else x - math.floor(x) - Fr(1, 2)
    return sum(saw(Fr(j, k)) * saw(Fr(h * j, k)) for j in range(1, k))


def rademacher_psi(A):
    """Psi(A) = Phi(A) - 3 sign(c (a + d)), Phi(A) = (a + d)/c - 12 s(d, c) for c > 0 (Rademacher)"""
    (a, b), (c, d) = A
    sg = (c * (a + d) > 0) - (c * (a + d) < 0)
    if c < 0:
        a, b, c, d = -a, -b, -c, -d
    phi = Fr(b, d) if c == 0 else Fr(a + d, c) - 12 * dedekind_s(d, c)
    return phi - 3 * sg


def hdist(z, w):
    return math.acosh(1 + abs(z - w) ** 2 / (2 * z.imag * w.imag))


def reduce_F(z):
    for _ in range(1000):
        z = complex(z.real - round(z.real), z.imag)
        if abs(z) < 1 - 1e-15:
            z = -1 / z
        else:
            break
    return z


def geodesic(A):
    """the axis of A in the upper half-plane, by arclength s, and the length of one period"""
    (a, b), (c, d) = A
    t = a + d
    disc = t * t - 4
    x1, x2 = ((a - d) + math.sqrt(disc)) / (2 * c), ((a - d) - math.sqrt(disc)) / (2 * c)
    ctr, rad = (x1 + x2) / 2, abs(x1 - x2) / 2
    ell = 2 * math.log((t + math.sqrt(disc)) / 2)
    return (lambda s: complex(ctr + rad * math.tanh(s), rad / math.cosh(s))), ell


def min_dist(A, pts, nsamp=6000):
    """the distance on the modular surface from the thread's closed geodesic to the orbit of the given points"""
    z, ell = geodesic(A)
    f = lambda s: min(hdist(reduce_F(z(s)), p) for p in pts)
    ss = [-ell / 2 + ell * k / nsamp for k in range(nsamp + 1)]
    vals = [f(s) for s in ss]
    best, h = min(vals), ell / nsamp
    for k in sorted(range(len(ss)), key=lambda k: vals[k])[:12]:
        lo, hi = ss[k] - 2 * h, ss[k] + 2 * h
        for _ in range(200):
            m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
            if f(m1) < f(m2):
                hi = m2
            else:
                lo = m1
        best = min(best, f((lo + hi) / 2))
    return best


def lorenz_linking(words):
    """linking numbers of the Lorenz knots coded by the words (Birman-Williams braid; all crossings positive)"""
    strands = []
    for c, w in enumerate(words):
        for k in range(len(w)):
            s = w[k:] + w[:k]
            strands.append(((s * (64 // len(s) + 2))[:64], c, k, len(w)))
    strands.sort(key=lambda t: t[0])
    pos = {(t[1], t[2]): p for p, t in enumerate(strands)}
    perm = [pos[(t[1], (t[2] + 1) % t[3])] for t in strands]
    left = [t[0][0] == "L" for t in strands]
    m = len(words)
    cross = [[0] * m for _ in range(m)]
    for i in range(len(strands)):
        if left[i]:
            for j in range(len(strands)):
                if not left[j] and perm[i] > perm[j]:
                    a, b = strands[i][1], strands[j][1]
                    if a != b:
                        cross[a][b] += 1
                        cross[b][a] += 1
    return [[Fr(cross[a][b], 2) for b in range(m)] for a in range(m)]


def main():
    out = {"status": "post hoc check for a READING; no rule, no prediction, no data", "page":
           "docs/A_FRESH_LOOK_FROM_THE_PRINCIPLE_2026-10-15.md"}
    t12 = threads(12)
    bad = [w for w in t12 if rademacher_psi(word_mat(w)) != w.count("R") - w.count("L")]
    out["A1"] = {"threads to length 12": len(t12), "Psi == #R - #L on all": not bad, "exceptions": bad[:5]}
    t10 = [w for w in t12 if len(w) <= 10]
    recip, thru_i, thru_w, mism = [], [], [], []
    for w in t10:
        A = word_mat(w)
        di, dw = min_dist(A, [1j]), min_dist(A, [OMEGA, OMEGA + 1])
        rec = canon(swaprev(w)) == w
        if rec:
            recip.append(w)
        if di < 1e-7:
            thru_i.append(w)
        if dw < 1e-7:
            thru_w.append(w)
        if rec != (di < 1e-7):
            mism.append(w)
    out["A2"] = {"threads to length 10": len(t10), "reciprocal": len(recip), "through an image of i": len(thru_i),
                 "reciprocal exactly when through i": not mism, "mismatches": mism}
    mirror_pairs = all(canon(swaprev(w)) in thru_w for w in thru_w)
    out["A3"] = {"through an image of omega": thru_w, "count": len(thru_w),
                 "closed under the mirror (reverse with letters swapped)": mirror_pairs,
                 "none reciprocal": not any(w in recip for w in thru_w)}
    root = word_mat("LR")
    d_root_w = min_dist(root, [OMEGA, OMEGA + 1], 40000)
    out["A4"] = {"LR": {"matrix": root, "d to i": min_dist(root, [1j], 40000), "d to omega": d_root_w,
                        "ln sqrt(5/3)": math.log(math.sqrt(5 / 3)), "tanh(d/2)": math.tanh(d_root_w / 2),
                        "4 - sqrt 15": 4 - math.sqrt(15), "|i + 1/2|^2 (the axis radius^2 is 5/4)": 1.25},
                 "LLR": {"d to omega": min_dist(word_mat("LLR"), [OMEGA, OMEGA + 1], 40000)},
                 "LRR": {"d to omega": min_dist(word_mat("LRR"), [OMEGA, OMEGA + 1], 40000)}}
    out["A4"]["holds"] = bool(out["A4"]["LR"]["d to i"] < 1e-9 and abs(d_root_w - math.log(math.sqrt(5 / 3))) < 1e-9
                              and abs(math.tanh(d_root_w / 2) - (4 - math.sqrt(15))) < 1e-9
                              and out["A4"]["LLR"]["d to omega"] < 1e-9 and out["A4"]["LRR"]["d to omega"] < 1e-9)
    by_t = defaultdict(list)
    for w in t12:
        A = word_mat(w)
        by_t[A[0][0] + A[1][1]].append(w)
    out["A5"] = {str(t): {"discriminant t^2 - 4": t * t - 4, "threads to length 12": by_t[t]} for t in sorted(by_t)[:6]}
    g = ((0, -1), (1, 1))
    g3 = mul(mul(g, g), g)
    w0 = OMEGA
    fixed = abs((g[0][0] * w0 + g[0][1]) / (g[1][0] * w0 + g[1][1]) - w0)
    out["A6"] = {"gamma (B1657, W94)": g, "gamma^3": g3, "trace": g[0][0] + g[1][1],
                 "gamma^-1 (the trefoil's monodromy)": ((1, 1), (-1, 0)), "|gamma(omega) - omega|": fixed,
                 "torsion-free traces |2 - t| = 1 among t in -10..10": [t for t in range(-10, 11) if abs(2 - t) == 1],
                 "holds": bool(g3 == ((-1, 0), (0, -1)) and fixed < 1e-15)}
    t8 = [w for w in t12 if len(w) <= 8]
    lk = lorenz_linking(t8)
    vals = [lk[a][b] for a in range(len(t8)) for b in range(a + 1, len(t8))]
    sw = lambda w: canon("".join("R" if ch == "L" else "L" for ch in w))
    idx = {w: k for k, w in enumerate(t8)}
    mir = all(lk[a][b] == lk[idx[sw(t8[a])]][idx[sw(t8[b])]] for a in range(len(t8)) for b in range(len(t8)) if a != b)
    short = ["LR", "LLR", "LRR", "LLLR", "LRRR", "LLRR"]
    out["A7"] = {"threads to length 8": len(t8), "pairs": len(vals), "min": int(min(vals)), "max": int(max(vals)),
                 "all integers": all(v.denominator == 1 for v in vals), "mirror-invariant": mir,
                 "the six shortest": {"words": short, "linking": [[int(lk[idx[a]][idx[b]]) if a != b else None
                                                                  for b in short] for a in short]}}
    out["A7"]["holds"] = bool(min(vals) >= 1 and out["A7"]["all integers"] and mir)
    out["all hold"] = bool(not bad and not mism and mirror_pairs and out["A4"]["holds"] and out["A6"]["holds"]
                           and out["A7"]["holds"])
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print({k: (v.get("holds") if isinstance(v, dict) and "holds" in v else None) for k, v in out.items()
           if k.startswith("A")}, "all hold:", out["all hold"])


if __name__ == "__main__":
    main()
