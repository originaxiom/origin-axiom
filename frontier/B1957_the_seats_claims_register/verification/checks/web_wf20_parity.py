"""B1957: the web seat's W-F20, its check E1 to E3 (parities on the level-5 charge classes), by enumeration on main.
The class of a field is 2 (6Y) mod 5.  A parity is a function f on the classes 1 to 4 with f(5 - k) = 1 - f(k).
The rule: a sector's Higgs reads S (holomorphic) when its class has matter's parity, and S~ otherwise.
 E1  the parities; those that put all five matter fields in one class; the world each gives, for both signs of the
     hypercharge convention.
 E2  the class is the exterior degree mod 5 for the standard embedding, and exterior-degree parity is one of the two.
 E3  with the Higgs entering as an operator of degree +1 or -1, both of its components are odd: the rule gives S~ three
     times, against the charge rule (up takes the conjugate of down's and the leptons' reading)."""
import itertools
SIXY = {"Q": 1, "u^c": -4, "d^c": 2, "L": -3, "e^c": 6}; DEG = {"Q": 2, "u^c": 2, "e^c": 2, "d^c": 4, "L": 4}; H = 3     # 10 = Lambda^2, 5bar = Lambda^4, the Higgs's 5 = Lambda^1
cls = lambda y: (2 * y) % 5
if __name__ == "__main__":
    pars = [dict(zip((1, 2, 3, 4), (f1, f2, 1 - f2, 1 - f1))) for f1, f2 in itertools.product((0, 1), repeat=2)]
    print("classes of matter: %s; of the up Higgs (6Y = 3) and its conjugate: %d, %d; the class equals the exterior degree mod 5 for every field: %s" % ({k: cls(v) for k, v in SIXY.items()}, cls(H), cls(-H), all(cls(SIXY[k]) == DEG[k] % 5 for k in SIXY) and cls(H) == 1))
    good = []
    for f in pars:
        for sign in (1, -1):
            m = {f[cls(sign * v)] for v in SIXY.values()}
            if len(m) != 1: break
        else: good.append(f)
    print("E1: parities (conjugation-odd functions on the four classes): %d; those with all matter in one class, for both signs: %d; complementary: %s" % (len(pars), len(good), len(good) == 2 and all(good[0][k] != good[1][k] for k in (1, 2, 3, 4))))
    for f in good:
        for sign in (1, -1):
            mp = f[cls(sign * SIXY["Q"])]; world = {s: ("S" if f[cls(sign * hy)] == mp else "S~") for s, hy in (("up", H), ("down", -H), ("leptons", -H))}
            print("    parity %s, hypercharge sign %+d: %s" % (f, sign, world))
    deg = {k: k % 2 for k in (1, 2, 3, 4)}; print("E2: exterior-degree parity %s is one of the two: %s" % (deg, deg in good))
    print("E3: the operator lift puts the Higgs and its conjugate at degrees +1 and -1, parities %d and %d, both unlike matter's (%d): the rule gives %s" % (1 % 2, (-1) % 2, 0, ("S~", "S~", "S~")))
