#!/usr/bin/env python3
"""B1520 -- the symmetry group of m004 as automorphisms of its group, with orientation (route S1), and its order (route S2).

S1. The group: Gamma = <m, n | R>, R = m n m^-1 n^-1 m n^-1 m^-1 n m n^-1 (main B1455's presentation; Ballas' matrices satisfy it).
    The faithful geometric representation in SL(2, C), exactly over Q(sqrt(-3)) with own arithmetic (class Kq below):
        m -> [[1, 1], [0, 1]],   n -> [[1, 0], [z, 1]],   z = (1 + sqrt(-3))/2,
    z being a root of the relator equations (the other root is its complex conjugate). A word map sigma (images of m and n as
    words) is an endomorphism of Gamma iff R(sigma(m), sigma(n)) is trivial in Gamma iff its image is the identity (the
    representation is faithful). Its character on (m, n, mn) is that of the representation (orientation kept) or of its
    complex conjugate (orientation reversed); in both cases the image has full covolume, so sigma is surjective, hence an
    automorphism (Gamma is Hopfian). The eight representatives: the Klein group V = {id, theta, s, s theta} (theta inverts
    both generators, s swaps them) and tau V, tau: m -> m, n -> n m n^-1 (orientation-reversing).
    Distinct in Out(Gamma): every non-identity element of V has order 2 and is not inner (an inner automorphism of order
    dividing 2 is conjugation by g with g^2 central, so g = 1 in this torsion-free, centreless group), and tau V is V's coset
    of opposite orientation. So the eight are pairwise distinct classes, and with |Out(Gamma)| = |Isom(m004)| = 8 (Mostow-
    Prasad; route S2) they are all of Out(Gamma).
    Also recorded: main B1455's eight simple maps (m, n) -> (m^a, n^b), (n^a, m^b), of which the mixed-sign four fail R.
S2. SnapPy: the symmetry group of m004 has order 8 and is amphichiral.
Usage: python3 symmetries.py   (writes symmetries.json beside it)"""
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = "mnMNmNMnmN"


class Kq:
    """a + b sqrt(-3), a and b rational"""
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, o):
        o = o if isinstance(o, Kq) else Kq(o)
        return Kq(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Kq(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, Kq) else Kq(o)))

    def __mul__(self, o):
        o = o if isinstance(o, Kq) else Kq(o)
        return Kq(self.a * o.a - 3 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __eq__(self, o):
        o = o if isinstance(o, Kq) else Kq(o)
        return self.a == o.a and self.b == o.b

    def conj(self):
        return Kq(self.a, -self.b)

    def __repr__(self):
        return f"{self.a} + {self.b} sqrt(-3)"


def mmul(X, Y):
    return ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]),
            (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))


def minv(X):  # determinant one
    return ((X[1][1], -X[0][1]), (-X[1][0], X[0][0]))


ONE = ((Kq(1), Kq(0)), (Kq(0), Kq(1)))
Z = Kq(F(1, 2), F(1, 2))
GEN = {"m": ((Kq(1), Kq(1)), (Kq(0), Kq(1))), "n": ((Kq(1), Kq(0)), (Z, Kq(1)))}
GEN["M"], GEN["N"] = minv(GEN["m"]), minv(GEN["n"])


def ev(word, gens):
    X = ONE
    for c in word:
        X = mmul(X, gens[c])
    return X


def is_identity(X):
    return X[0][0] == 1 and X[1][1] == 1 and X[0][1] == 0 and X[1][0] == 0


def tr(X):
    return X[0][0] + X[1][1]


def reduce(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def inverse_word(w):
    return "".join(c.swapcase() for c in reversed(w))


def compose(outer, inner):
    """the map x -> outer(inner(x)) on generators, as words"""
    def image(w, f):
        return reduce("".join(f[c] if c.islower() else inverse_word(f[c.lower()]) for c in w))
    return {"m": image(inner["m"], outer), "n": image(inner["n"], outer)}


def classify(sigma):
    img = {"m": ev(sigma["m"], GEN), "n": ev(sigma["n"], GEN)}
    img["M"], img["N"] = minv(img["m"]), minv(img["n"])
    endo = is_identity(ev(R, img))
    t = tr(mmul(img["m"], img["n"]))
    t0 = tr(mmul(GEN["m"], GEN["n"]))
    if t == t0 or t == -t0:
        orient = "kept"
    elif t == t0.conj() or t == -(t0.conj()):
        orient = "reversed"
    else:
        orient = "neither (not an automorphism)"
    # the meridian's exponent on H1(Gamma) = Z (both generators are meridians, image = sum of exponents of sigma(m))
    h1 = sum(1 if c.islower() else -1 for c in sigma["m"])
    return {"endomorphism (R -> 1)": endo, "orientation": orient, "on H1": h1,
            "tr(sigma(m) sigma(n))": repr(t), "automorphism": endo and orient != "neither (not an automorphism)"}


def main():
    ident = {"m": "m", "n": "n"}
    theta = {"m": "M", "n": "N"}
    swap = {"m": "n", "n": "m"}
    tau = {"m": "m", "n": "nmN"}
    V = {"id": ident, "theta": theta, "s": swap, "s.theta": compose(swap, theta)}
    reps = dict(V)
    for k, v in V.items():
        reps["tau." + k] = compose(tau, v)
    out = {"relator": R, "z": "(1 + sqrt(-3))/2", "representatives": {}}
    for k, v in reps.items():
        out["representatives"][k] = dict(v, **classify(v))
    # V is a group: closure and orders (as word maps, checked on the generators after free reduction)
    table = {}
    for a, va in V.items():
        for b, vb in V.items():
            c = compose(va, vb)
            table[f"{a}*{b}"] = next((k for k, v in V.items() if v == c), None)
    out["V closed under composition"] = all(x is not None for x in table.values())
    out["V multiplication"] = table
    # main B1455's eight simple maps
    simple = {}
    for sw in (False, True):
        for a in (1, -1):
            for b in (1, -1):
                x, y = ("n", "m") if sw else ("m", "n")
                sig = {"m": x if a == 1 else x.upper(), "n": y if b == 1 else y.upper()}
                simple[f"({'n' if sw else 'm'}^{a}, {'m' if sw else 'n'}^{b})"] = classify(sig)
    out["main B1455's eight simple maps"] = simple
    # S2: SnapPy
    try:
        import snappy
        G = snappy.Manifold("m004").symmetry_group()
        out["S2 SnapPy"] = {"group": str(G), "order": G.order(), "amphichiral": G.is_amphicheiral()}
    except Exception as exc:  # recorded, not hidden
        out["S2 SnapPy"] = {"error": repr(exc)}
    autos = [k for k, v in out["representatives"].items() if v["automorphism"]]
    kept = [k for k in autos if out["representatives"][k]["orientation"] == "kept"]
    rev = [k for k in autos if out["representatives"][k]["orientation"] == "reversed"]
    out["passed"] = (len(autos) == 8 and len(kept) == 4 and len(rev) == 4 and out["V closed under composition"]
                     and out["S2 SnapPy"].get("order") == 8 and out["S2 SnapPy"].get("amphichiral") is True)
    (HERE / "symmetries.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1, ensure_ascii=False))
    print("PASSED:", out["passed"])


if __name__ == "__main__":
    main()
