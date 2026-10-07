#!/usr/bin/env python3
"""The parity lemma, checked exactly on every word state to length 12 (both signs): for phi in +-SL(2, Z) the four
conditions agree --
  (a) tr phi is odd;
  (b) phi mod 2 fixes no non-zero parity of F_2^2;
  (c) phi mod 2 has order 3 in GL(2, F_2), so it permutes the three non-zero parities as a 3-cycle;
  (d) the characteristic polynomial t^2 - (tr phi) t + 1 is Phi_3 = t^2 + t + 1 mod 2 (the parities form F_2[t]/Phi_3 = F_4).
And the GENESIS selection SE1 (|2 - tr phi| = 1 with phi hyperbolic) keeps one word up to rotation and swap, +LR, of trace 3.

The words: every cyclic word in L and R using both letters, primitive, up to rotation and the L <-> R swap, with either
sign; L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]] (sm:B1527's homology convention gives the same traces).

    python3 parity_lemma.py   ->  parity_lemma.json beside this file"""
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))


def mul(A, B, m=None):
    C = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return tuple(tuple(x % m for x in r) for r in C) if m else C


def canon(w):
    rots = [w[i:] + w[:i] for i in range(len(w))]
    sw = w.translate(str.maketrans("LR", "RL"))
    rots += [sw[i:] + sw[:i] for i in range(len(sw))]
    return min(rots)


def primitive(w):
    n = len(w)
    return not any(n % d == 0 and w == w[:d] * (n // d) for d in range(1, n))


def words(nmax):
    seen = set()
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" in w and "R" in w and primitive(w):
                c = canon(w)
                if c not in seen:
                    seen.add(c)
                    yield c


def main(nmax=12):
    rows, agree, se1 = 0, True, []
    I2 = ((1, 0), (0, 1))
    for w in words(nmax):
        M = I2
        for ch in w:
            M = mul(M, L if ch == "L" else R)
        for sign in (1, -1):
            P = tuple(tuple(sign * x for x in r) for r in M)
            tr = P[0][0] + P[1][1]
            a = tr % 2 == 1
            P2 = tuple(tuple(x % 2 for x in r) for r in P)
            b = all(tuple((P2[i][0] * v[0] + P2[i][1] * v[1]) % 2 for i in range(2)) != v
                    for v in ((1, 0), (0, 1), (1, 1)))
            X, k = P2, 1
            while X != I2:
                X, k = mul(X, P2, 2), k + 1
            c = k == 3
            d = (tr % 2, 1) == (1, 1)                     # t^2 - tr t + 1 = t^2 + t + 1 mod 2 iff tr odd
            agree = agree and a == b == c == d
            rows += 1
            if abs(2 - tr) == 1 and abs(tr) > 2:
                se1.append(("+" if sign == 1 else "-") + w)
    out = {"word states read (both signs)": rows, "max length": nmax, "the four conditions agree": agree,
           "SE1 (|2 - tr| = 1, hyperbolic)": se1}
    (HERE / "parity_lemma.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out))


if __name__ == "__main__":
    main()
