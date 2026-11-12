"""B1884 -- the web seat's sealed card "what level a ground names", verified on main with main's own code.

Integers only.  Rows as vectors, as the seat writes them: L has rows (1,0),(1,1); R has rows (1,1),(0,1); the exchange P swaps
the coordinates; the tick F = L P has rows (0,1),(1,1).  N runs from 2 to 200, as on the card.  None of the seat's code is run.

EXPECTATIONS, WRITTEN BEFORE THE RUN (each says how it could fail)
 G0  F^2 = L R, F'^2 = R L for F' = P F P, P L P = R, F' = R F R^-1, det F = det F' = -1; v0 = (1,3) has v0 L R = -v0 and
     v0 F = 3 v0 modulo 5.
 G1  By hand: det(F - I) = -1 and det(F + I) = 1, so F keeps no vector up to sign at any N; det(LR - I) = -1 and
     det(LR + I) = 5.  By brute force to N = 200: F and F' keep no primitive vector up to sign; L R and R L keep four at
     N = 5 and none elsewhere.  Fails if a vector turns up at some N.
 G2  The lines kept as sets by each of the four are as many as the roots of x^2 - x - 1 modulo N (for the tick) or of
     x^2 - 3x + 1 (for its square), and both counts are rho(N): 1 at 5, 0 at 25 and at 2, 2 at a prime that is +-1 mod 5,
     multiplicative.  So exactly one line is kept at N = 5 and at no other N to 200.  Fails if another N has exactly one.
 G3  At N = 5 the tick moves the four non-zero vectors of its line in one orbit of length 4; its square in two of length 2.
 G4  Of the non-negative integer matrices of determinant -1 with entries to 8 (the seat counts 87), those with no line of
     their own at any level are exactly F and F'.  By hand: for determinant -1 and trace s, det(g - I) = -s and
     det(g + I) = s, so no own line exactly when s = 1.
 G5  Main's own question: in B1872's convention (columns, the ground [[2,1],[1,1]], the mark (1,2)) the same counts hold.
"""
import itertools
import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT, RES = [], {}


def P_(*a):
    s = " ".join(str(x) for x in a); OUT.append(s); print(s)


def check(name, ok, detail=""):
    RES[name] = bool(ok)
    P_("   [%s] %s%s" % ("ok" if ok else "FAILS", name, (" -- " + str(detail)) if detail else ""))


def mul(A, B):
    return (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])


def det(A):
    return A[0] * A[3] - A[1] * A[2]


def inv(A):
    d = det(A); assert d in (1, -1)
    return (A[3] * d, -A[1] * d, -A[2] * d, A[0] * d)


def row(v, A, n):
    return ((v[0] * A[0] + v[1] * A[2]) % n, (v[0] * A[1] + v[1] * A[3]) % n)


I2, L, R, SW = (1, 0, 0, 1), (1, 0, 1, 1), (1, 1, 0, 1), (0, 1, 1, 0)
F = mul(L, SW)
F2 = mul(mul(SW, F), SW)
LR, RL = mul(L, R), mul(R, L)


def primitive(n):
    return [(a, b) for a in range(n) for b in range(n) if math.gcd(math.gcd(a, b), n) == 1]


def kept_up_to_sign(g, n):
    return [v for v in primitive(n) if row(v, g, n) in (v, ((-v[0]) % n, (-v[1]) % n))]


def lines_kept(g, n):
    """the cyclic subgroups of order n of (Z/n)^2 that g carries to themselves, as sets"""
    seen, out = set(), 0
    units = [u for u in range(1, n) if math.gcd(u, n) == 1] or [1]
    for v in primitive(n):
        ln = frozenset(((u * v[0]) % n, (u * v[1]) % n) for u in units)
        if ln in seen:
            continue
        seen.add(ln)
        if row(v, g, n) in ln:
            out += 1
    return out


def roots(poly, n):
    return sum(1 for x in range(n) if poly(x) % n == 0)


def main():
    P_("THE WEB SEAT'S CARD ON WHAT LEVEL A GROUND NAMES, ON MAIN")
    check("G0 F = L P is [[0,1],[1,1]]; F^2 = L R; F'^2 = R L; P L P = R; F' = R F R^-1; det F = det F' = -1",
          F == (0, 1, 1, 1) and mul(F, F) == LR and mul(F2, F2) == RL and mul(mul(SW, L), SW) == R and mul(mul(R, F), inv(R)) == F2 and det(F) == det(F2) == -1)
    check("G0 v0 = (1,3): v0 L R = -v0 and v0 F = 3 v0 modulo 5", row((1, 3), LR, 5) == (4, 2) and row((1, 3), F, 5) == (3, 4))
    dm = lambda g, s: det((g[0] + s, g[1], g[2], g[3] + s))
    check("G1 det(F - I) = -1, det(F + I) = 1; det(LR - I) = -1, det(LR + I) = 5", (dm(F, -1), dm(F, 1), dm(LR, -1), dm(LR, 1)) == (-1, 1, -1, 5))
    kept = {name: {n: len(kept_up_to_sign(g, n)) for n in range(2, 201)} for name, g in (("F", F), ("F'", F2), ("LR", LR), ("RL", RL))}
    check("G1 to N = 200: the tick and its other side keep no primitive vector up to sign at any N", all(v == 0 for nm in ("F", "F'") for v in kept[nm].values()))
    check("G1 to N = 200: the tick's square, entered at either place, keeps four at N = 5 and none elsewhere",
          all({n: c for n, c in kept[nm].items() if c} == {5: 4} for nm in ("LR", "RL")))
    rho = lambda n: roots(lambda x: x * x - x - 1, n)
    rho3 = lambda n: roots(lambda x: x * x - 3 * x + 1, n)
    lines = {name: {n: lines_kept(g, n) for n in range(2, 201)} for name, g in (("F", F), ("F'", F2), ("LR", LR), ("RL", RL))}
    check("G2 the lines kept as sets by each of the four equal the roots of x^2 - x - 1 modulo N, for every N to 200",
          all(lines[nm][n] == rho(n) for nm in lines for n in range(2, 201)))
    check("G2 and the roots of x^2 - 3x + 1 are as many (the tick's square)", all(rho(n) == rho3(n) for n in range(2, 201)))
    where = sorted(n for n in range(2, 201) if rho(n))
    P_("   N to 200 at which a line is kept: %s" % where)
    check("G2 exactly one line is kept at N = 5 and at no other N to 200; elsewhere there are two or none",
          [n for n in where if rho(n) == 1] == [5] and all(rho(n) == 2 for n in where if n != 5))
    check("G2 rho is as the card says: 1 at 5, 0 at 25, 0 at 2, 2 at a prime that is +-1 modulo 5, 0 at one that is +-2",
          rho(5) == 1 and rho(25) == 0 and rho(2) == 0 and all(rho(p) == (2 if p % 5 in (1, 4) else 0) for p in (3, 7, 11, 13, 17, 19, 29, 31, 41, 59, 61, 71, 79, 89, 101, 109, 131)))
    check("G2 rho is multiplicative on the N to 200 that are products of two coprime parts", all(rho(a * b) == rho(a) * rho(b) for a in range(2, 101) for b in range(a + 1, 101) if math.gcd(a, b) == 1 and a * b <= 200)
          and len({a * b for a in range(2, 101) for b in range(a + 1, 101) if math.gcd(a, b) == 1 and a * b <= 200}) == 139,
          "every coprime factorisation of the 139 levels to 200 that have one (corrected 2026-11-12, Review 79: the parts ran to 14 only, 47 levels)")

    def orbits(g):
        vs = [(k * 1 % 5, k * 3 % 5) for k in (1, 2, 3, 4)] if row((1, 3), g, 5) in [(k % 5, 3 * k % 5) for k in range(1, 5)] else [(k % 5, 2 * k % 5) for k in (1, 2, 3, 4)]
        seen, out = set(), []
        for v in vs:
            if v in seen: continue
            n, w = 0, v
            while w not in seen:
                seen.add(w); w = row(w, g, 5); n += 1
            out.append(n)
        return sorted(out)
    check("G3 at N = 5 the tick and its other side move their line's four vectors in one orbit of length 4; the square in two of length 2",
          orbits(F) == [4] and orbits(F2) == [4] and orbits(LR) == [2, 2] and orbits(RL) == [2, 2], (orbits(F), orbits(F2), orbits(LR), orbits(RL)))
    mats = [m for m in itertools.product(range(9), repeat=4) if det(m) == -1]
    both = [m for m in itertools.product(range(9), repeat=4) if det(m) in (1, -1)]
    check("G4 non-negative matrices with entries to 8: 174 of determinant +-1, 87 of determinant -1", (len(both), len(mats)) == (174, 87), (len(both), len(mats)))
    none = [m for m in mats if abs(dm(m, -1)) == 1 and abs(dm(m, 1)) == 1]
    check("G4 those with det(g - I) and det(g + I) both units (no line of their own at any level) are exactly the tick and its other side", sorted(none) == sorted([F, F2]), none)
    check("G4 by hand, on all 87: det(g - I) = -trace and det(g + I) = trace", all(dm(m, -1) == -(m[0] + m[3]) and dm(m, 1) == m[0] + m[3] for m in mats))
    brute = [m for m in mats if all(not kept_up_to_sign(m, n) for n in range(2, 41))]
    check("G4 and by brute force to N = 40: the same two keep no vector up to sign", sorted(brute) == sorted([F, F2]), len(brute))
    # main's convention: columns, the ground [[2,1],[1,1]], the mark (1,2)
    Lm, Rm = (1, 1, 0, 1), (1, 0, 1, 1)
    Fm = mul(Lm, SW); LRm = mul(Lm, Rm)
    col = lambda g, v, n: ((g[0] * v[0] + g[1] * v[1]) % n, (g[2] * v[0] + g[3] * v[1]) % n)
    keptc = lambda g, n: [v for v in primitive(n) if col(g, v, n) in (v, ((-v[0]) % n, (-v[1]) % n))]
    check("G5 in B1872's convention: the ground [[2,1],[1,1]] keeps (1,2) up to sign at N = 5, four vectors there and none at another N to 60; its tick keeps none",
          mul(Fm, Fm) == LRm and col(LRm, (1, 2), 5) == (4, 3) and {n: len(keptc(LRm, n)) for n in range(2, 61) if keptc(LRm, n)} == {5: 4} and not any(keptc(Fm, n) for n in range(2, 61)),
          (Fm, LRm))
    # the seat's table of the other root histories (reported there, not predicted): one line as a set, and vectors up to sign
    table = {}
    for name, word in (("L2R", "LLR"), ("LR2", "LRR"), ("L3R", "LLLR"), ("LR3", "LRRR"), ("L4R", "LLLLR"), ("LR4", "LRRRR"), ("L2R2", "LLRR")):
        g = I2
        for ch in word:
            g = mul(g, L if ch == "L" else R)
        table[name] = {"trace": g[0] + g[3], "discriminant": (g[0] + g[3]) ** 2 - 4,
                       "exactly_one_line_at": [n for n in range(2, 61) if lines_kept(g, n) == 1], "a_vector_up_to_sign_at": [n for n in range(2, 61) if kept_up_to_sign(g, n)]}
        P_("   %-5s trace %d, discriminant %d: exactly one line kept at N = %s; a vector kept up to sign at N = %s" % (
            name, table[name]["trace"], table[name]["discriminant"], table[name]["exactly_one_line_at"] or "none", table[name]["a_vector_up_to_sign_at"]))
    want = {"L2R": ([2, 3, 6], [2, 3, 6]), "LR2": ([2, 3, 6], [2, 3, 6]), "L3R": ([3, 7, 21], [3, 7]), "LR3": ([3, 7, 21], [3, 7]),
            "L4R": ([2], [2, 4, 8]), "LR4": ([2], [2, 4, 8]), "L2R2": ([], [2, 4])}
    check("the seat's table of the seven other root histories (reported there, not predicted) is reproduced to N = 60",
          all((table[k]["exactly_one_line_at"], table[k]["a_vector_up_to_sign_at"]) == want[k] for k in want), {k: (table[k]["exactly_one_line_at"], table[k]["a_vector_up_to_sign_at"]) for k in table})
    n = sum(1 for v in RES.values() if isinstance(v, bool)); bad = [k for k, v in RES.items() if v is False]
    P_(""); P_("CHECKS: %d, FAILING: %d%s" % (n, len(bad), (" -- " + "; ".join(bad)) if bad else ""))
    RES["numbers"] = {"levels_with_a_line_kept": where, "table": table, "matrices_det_minus_one": len(mats)}
    (HERE / "ground_level_on_main.json").write_text(json.dumps(RES, indent=1) + "\n", encoding="utf-8")
    (HERE / "ground_level_on_main_run.txt").write_text("\n".join(OUT) + "\n", encoding="utf-8")
    return not bad


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
