#!/usr/bin/env python3
"""B1522 -- X5, post-run (written and run after the census, disclosed as such): Lemma F beyond the sealed range.

The census stops at M_12; Lemma F is stated for every odd n with p = L_n prime. Here M_13 (L_13 = 521) is checked by code that
shares nothing with route F's closure or route R:
  - Phi^13 = I mod 521, so T_13 = F_521^2 and its characters are all of F_521^2;
  - the group is built as {+-M^j S^e} mod 521 (M^2 = Phi^-1, M^26 = I), checked closed under the four lifts' matrices, of order
    8n = 104, with sigma = (-1)^e and d = (j + e) mod 2 (eps and alpha dualise, iota and tau do not);
  - the 271 441 characters are counted: unfixed by every reflection (d = 1, sigma = -1), and in addition by every rotation
    (d = 1, sigma = +1).
And every odd-n Lucas number is +-1 mod 5, so an odd-n Lucas prime is split in Q(sqrt 5) (checked for n < 200).
Usage: python3 lemma_f_beyond.py   (writes lemma_f_beyond.json; about 4 s)"""
import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run(n=13, p=521):
    t0 = time.time()

    def mul(A, B):
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % p for j in range(2)) for i in range(2))
    I = ((1, 0), (0, 1))
    PHI = ((0, p - 1), (1, 3))
    M = ((2, 1), (p - 1, p - 1))
    S = ((0, 1), (1, 0))
    NEG = ((p - 1, 0), (0, p - 1))
    P = I
    for _ in range(n):
        P = mul(P, PHI)
    assert P == I, "Phi^n = I mod p, so T_n = F_p^2"
    assert mul(mul(M, M), PHI) == I, "M^2 = Phi^-1"
    els, Mj = {}, I
    for j in range(2 * n):
        for e in (0, 1):
            B = mul(Mj, S) if e else Mj
            els[B] = (j, e)
            els[mul(NEG, B)] = (j, e)
        Mj = mul(Mj, M)
    assert Mj == I, "M^(2n) = I on T_n"
    assert len(els) == 8 * n
    for B in list(els):
        for G in (NEG, S, M, PHI):
            assert mul(B, G) in els, "closed under the four lifts"
    refl = [B for B, (j, e) in els.items() if e == 1 and (j + e) % 2 == 1]
    rot = [B for B, (j, e) in els.items() if e == 0 and (j + e) % 2 == 1]
    assert len(refl) == len(rot) == 2 * n

    def fixed(a, b, Bs):
        return any(((a * B[0][0] + b * B[1][0]) % p, (a * B[0][1] + b * B[1][1]) % p) == (a, b) for B in Bs)
    generic = unitary = 0
    for a in range(p):
        for b in range(p):
            if not fixed(a, b, refl):
                generic += 1
                if not fixed(a, b, rot):
                    unitary += 1
    L = [2, 1]
    for _ in range(2, 200):
        L.append(L[-1] + L[-2])
    return {"n": n, "p = L_n": p, "characters": p * p, "group order": len(els), "reflections": len(refl), "rotations": len(rot),
            "unfixed off the circle": generic, "Lemma F": (p - 1) * (p + 1 - 2 * n),
            "unfixed on the circle": unitary, "Lemma F (unitary)": (p - 1) * (p - 1 - 2 * n),
            "odd-n Lucas numbers mod 5 (n < 200)": sorted({L[k] % 5 for k in range(1, 200, 2)}),
            "passed": generic == (p - 1) * (p + 1 - 2 * n) and unitary == (p - 1) * (p - 1 - 2 * n),
            "seconds": round(time.time() - t0, 1)}


if __name__ == "__main__":
    out = run()
    (HERE / "lemma_f_beyond.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(out, ensure_ascii=False))
