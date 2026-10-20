"""B1682 -- main's own check of W110 (the word side of the record count), written without the seat's code.

Letters are signed integers: k is a_k, -k its inverse. A class of F_n is a cyclic word, keyed by the least rotation of
its cyclic reduction. Moves: R_ij a_i -> a_i a_j, L_ij a_i -> a_j a_i, and their inverses, as letter substitutions.

T1  the length counts, on random cyclic words (n = 2..6, length <= 40), by direct reduction:
      |R_ij^e(w)| = m + n_i - 2 #{a_i a_j^-e, a_j^e a_i^-1}      (the seat's lemma)
      |L_ij^e(w)| = m + n_i - 2 #{a_j^-e a_i, a_i^-1 a_j^e}      (main's own count for the left moves; no reversal)
T2  the census: every class to length 12 (n = 2), 8 (n = 3), 7 (n = 4), 6 (n = 5); the classes keeping their length
    under every R_ij^+-1, under every L_ij^+-1, kept by every transvection exactly and up to inversion; at n = 2 the
    classes kept by the record's R (a -> ab) and L (b -> ab).
T3  the sharper form, on the census at n = 3, 4: if one i has its length kept by R_ij^+-1 for every j != i, a_i is absent.
T4  the web seat's exploratory surface-word note at genus 2: the handle twists keep [a1, b1][a2, b2] as a word, and the
    eight transvections between the handles move its class.
"""
import json, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def reduce(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def cyc(w):
    w = reduce(w)
    i, j = 0, len(w) - 1
    while i < j and w[i] == -w[j]:
        i, j = i + 1, j - 1
    return w[i:j + 1]


def key(w):
    w = cyc(w)
    if not w:
        return ()
    return min(tuple(w[k:] + w[:k]) for k in range(len(w)))


def inv(w):
    return [-x for x in reversed(w)]


def apply(sub, w):
    out = []
    for x in w:
        img = sub.get(abs(x), [abs(x)])
        out.extend(img if x > 0 else inv(img))
    return reduce(out)


def R(i, j, e=1):
    return {i: [i, e * j]}


def Lm(i, j, e=1):
    return {i: [e * j, i]}


def pairs(w):
    m = len(w)
    return [(w[k], w[(k + 1) % m]) for k in range(m)]


def count_R(w, i, j, e):
    P = pairs(w)
    return sum(1 for p in P if p == (i, -e * j) or p == (e * j, -i))


def count_L(w, i, j, e):
    P = pairs(w)
    return sum(1 for p in P if p == (-e * j, i) or p == (-i, e * j))


def random_cyclic(n, m, rng):
    while True:
        w = []
        for _ in range(m):
            x = rng.choice([k for k in range(-n, n + 1) if k and (not w or k != -w[-1])])
            w.append(x)
        if m < 2 or w[0] != -w[-1]:
            return w


def t1(rng):
    fails, tried = 0, 0
    for _ in range(4000):
        n = rng.randint(2, 6)
        w = random_cyclic(n, rng.randint(1, 40), rng)
        m = len(w)
        for i in range(1, n + 1):
            ni = sum(1 for x in w if abs(x) == i)
            for j in range(1, n + 1):
                if j == i:
                    continue
                for e in (1, -1):
                    tried += 2
                    if len(cyc(apply(R(i, j, e), w))) != m + ni - 2 * count_R(w, i, j, e):
                        fails += 1
                    if len(cyc(apply(Lm(i, j, e), w))) != m + ni - 2 * count_L(w, i, j, e):
                        fails += 1
    return tried, fails


def classes(n, maxlen):
    letters = [k for k in range(-n, n + 1) if k]
    seen = set()
    for m in range(1, maxlen + 1):
        stack = [[x] for x in letters]
        while stack:
            w = stack.pop()
            if len(w) == m:
                if m == 1 or w[0] != -w[-1]:
                    k = key(w)
                    if k == tuple(w):
                        seen.add(k)
                continue
            for x in letters:
                if x != -w[-1]:
                    stack.append(w + [x])
    return sorted(seen, key=lambda t: (len(t), t))


def census(n, maxlen):
    C = classes(n, maxlen)
    Rs = [R(i, j, e) for i in range(1, n + 1) for j in range(1, n + 1) if i != j for e in (1, -1)]
    Ls = [Lm(i, j, e) for i in range(1, n + 1) for j in range(1, n + 1) if i != j for e in (1, -1)]
    tv = [R(i, j) for i in range(1, n + 1) for j in range(1, n + 1) if i != j] + \
         [Lm(i, j) for i in range(1, n + 1) for j in range(1, n + 1) if i != j]
    res = dict(n=n, maxlen=maxlen, classes=len(C), len_kept_R=[], len_kept_L=[], kept_tv=[], kept_tv_upto_inv=[],
               sharp_violations=0)
    for c in C:
        w, m = list(c), len(c)
        if all(len(cyc(apply(s, w))) == m for s in Rs):
            res["len_kept_R"].append(c)
        if all(len(cyc(apply(s, w))) == m for s in Ls):
            res["len_kept_L"].append(c)
        imgs = [key(apply(s, w)) for s in tv]
        if all(k == c for k in imgs):
            res["kept_tv"].append(c)
        ki = key(inv(w))
        if all(k in (c, ki) for k in imgs):
            res["kept_tv_upto_inv"].append(c)
        if n >= 3:
            for i in range(1, n + 1):
                if all(len(cyc(apply(R(i, j, e), w))) == m for j in range(1, n + 1) if j != i for e in (1, -1)):
                    if any(abs(x) == i for x in w):
                        res["sharp_violations"] += 1
    if n == 2:
        rec = [{1: [1, 2]}, {2: [1, 2]}]                      # the record's R: a -> ab and L: b -> ab
        res["kept_record"] = [c for c in C if all(key(apply(s, list(c))) == c for s in rec)]
    return res


def comm(x, y):
    return [x, y, -x, -y]


def t4():
    a1, b1, a2, b2 = 1, 2, 3, 4
    d = comm(a1, b1) + comm(a2, b2)
    twists = [{a1: [a1, b1]}, {b1: [b1, a1]}, {a2: [a2, b2]}, {b2: [b2, a2]}]
    kept_word = [apply(t, d) == d for t in twists]
    between = [{x: [x, y]} for x in (a1, b1) for y in (a2, b2)] + [{x: [x, y]} for x in (a2, b2) for y in (a1, b1)]
    moved = [key(apply(t, d)) not in (key(d), key(inv(d))) for t in between]
    return dict(twists_keep_the_word=kept_word, between_handle_transvections=len(between), moved=moved)


def main():
    rng = random.Random(1682)
    out = {}
    tried, fails = t1(rng)
    out["T1"] = dict(tried=tried, failures=fails)
    print(f"T1 length counts: {tried} move applications, failures {fails}")
    out["T2"] = {}
    for n, L in ((2, 12), (3, 8), (4, 7), (5, 6)):
        r = census(n, L)
        out["T2"][str(n)] = r
        line = (f"T2 n = {n} to length {L}: {r['classes']} classes; length kept by every R^+-1 {len(r['len_kept_R'])}, "
                f"by every L^+-1 {len(r['len_kept_L'])}; kept by every transvection {len(r['kept_tv'])}, "
                f"up to inversion {len(r['kept_tv_upto_inv'])}")
        if n == 2:
            line += f"; kept by the record's R and L {len(r['kept_record'])}: {r['kept_record']}"
        else:
            line += f"; T3 violations {r['sharp_violations']}"
        print(line, flush=True)
    out["T4"] = t4()
    print("T4 genus 2:", out["T4"])
    n2 = out["T2"]["2"]
    comm_powers = sorted(key(comm(1, 2) * k) for k in (1, 2, 3)) + sorted(key(inv(comm(1, 2) * k)) for k in (1, 2, 3))
    hold = dict(
        T1=fails == 0,
        T2_n_ge_3=all(not out["T2"][s][f] for s in ("3", "4", "5")
                      for f in ("len_kept_R", "len_kept_L", "kept_tv", "kept_tv_upto_inv")),
        T2_n2=sorted(n2["kept_record"]) == sorted(comm_powers) and sorted(n2["kept_tv"]) == sorted(comm_powers),
        T3=all(out["T2"][s]["sharp_violations"] == 0 for s in ("3", "4", "5")),
        T4=all(out["T4"]["twists_keep_the_word"]) and all(out["T4"]["moved"]),
    )
    out["hold"] = hold
    print("hold:", hold)
    (HERE / "main_kept_words.json").write_text(json.dumps(out, indent=1, default=list), encoding="utf-8")
    return 0 if all(hold.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
