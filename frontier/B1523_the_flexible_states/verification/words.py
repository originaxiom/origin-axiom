#!/usr/bin/env python3
"""B1523 -- the word states and what their words alone say about their isometries.

A word state (sm:B1516 C4, sm:B1517, main's B1434/B1439 convention) is a signed primitive cyclic word w in L and R with both
letters, taken up to rotation and the L<->R swap; it names the once-punctured-torus bundle with monodromy +-w, built in SnapPy as
'b++w' (sign +) or 'b+-w' (sign -), as sm:B1517 does. There are 758 to length 12; up to reversal as well they are 536 manifolds
(a word and its reverse are two states and one manifold, sm:B1517 C2/C3).

The isometries of a hyperbolic once-punctured-torus bundle preserve the fibration (b1 = 1), so they are the h in GL2(Z) with
h w h^-1 = w^(+-1), modulo the monodromy. Writing P = [[0,1],[1,0]] (det -1, P L P = R) and using sm:B1517 C6's identity
reverse(w) = (PJ) w^-1 (PJ)^-1 with det(PJ) = -1, the four kinds of self-map of the bundle are:

  id, iota  (h = +-1, e = +1): orientation kept, the base kept; the fibre boundary l and the section x kept
  "rev"     (w ~ reverse(w) up to rotation):      orientation kept, the base reversed; l -> l^-1, x -> x^-1
  "swap"    (w ~ swap(w) up to rotation):         orientation reversed, the base kept;  l -> l^-1, x -> x
  "swaprev" (w ~ swap(reverse(w)) up to rotation): orientation reversed, the base reversed; l -> l,    x -> x^-1 (mod l)

so the predicted order is |Isom| = 2 (1 + rev + swap + swaprev), each kind coming with its iota-partner. A map inverts the
longitude l exactly when (orientation sign) x (sign on H1(M) = Z) = -1, i.e. for the kinds "rev" and "swap".

This module only enumerates and classifies; it reads no cohomology.
Usage: python3 words.py   (prints the counts by length; writes nothing)"""
import itertools

SW = str.maketrans("LR", "RL")


def rots(w):
    return [w[i:] + w[:i] for i in range(len(w))]


def canon(w):
    return min(rots(w))


def primitive(w):
    n = len(w)
    return not any(n % d == 0 and w == w[:d] * (n // d) for d in range(1, n))


def kinds(w):
    """which of the three non-trivial kinds of self-map the cyclic word w carries"""
    c = canon(w)
    return {"rev": canon(w[::-1]) == c, "swap": canon(w.translate(SW)) == c, "swaprev": canon(w[::-1].translate(SW)) == c}


def predicted(w):
    k = kinds(w)
    order = 2 * (1 + k["rev"] + k["swap"] + k["swaprev"])
    inverting = k["rev"] or k["swap"]          # a map that inverts the fibre boundary exists
    return {"kinds": k, "isometry order": order, "a longitude-inverting isometry": inverting}


def states(maxlen=12, minlen=2):
    """the word states: (sign, canonical word) up to rotation and swap, with their manifold class (rotation, swap, reversal)"""
    out = {}
    for n in range(minlen, maxlen + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w or not primitive(w):
                continue
            c = canon(w)
            st = min(c, canon(c.translate(SW)))
            man = min(st, canon(c[::-1]), canon(c[::-1].translate(SW)))
            for sign in "+-":
                key = (sign, st)
                if key not in out:
                    out[key] = {"sign": sign, "word": st, "length": n, "manifold": (sign, man),
                                "snappy": ("b++" if sign == "+" else "b+-") + st}
    return out


def manifolds(maxlen=12):
    """one representative state per manifold (the class's minimal state), with the states it carries"""
    st = states(maxlen)
    out = {}
    for key, s in sorted(st.items(), key=lambda kv: (kv[1]["length"], kv[0])):
        m = s["manifold"]
        if m not in out:
            out[m] = {"representative": key, "states": [], **{k: s[k] for k in ("sign", "length")}}
        out[m]["states"].append(key)
    for m, rec in out.items():
        sign, w = rec["representative"]
        rec["word"] = w
        rec["snappy"] = ("b++" if sign == "+" else "b+-") + w
        rec.update(predicted(w))
    return out


if __name__ == "__main__":
    st = states(12)
    man = manifolds(12)
    print("states", len(st), "manifolds", len(man))
    for n in range(2, 13):
        ms = [m for m in man.values() if m["length"] == n]
        print(n, "states", sum(1 for s in st.values() if s["length"] == n), "manifolds", len(ms),
              "without a longitude-inverting isometry", sum(1 for m in ms if not m["a longitude-inverting isometry"]))
    print("total without", sum(1 for m in man.values() if not m["a longitude-inverting isometry"]))
