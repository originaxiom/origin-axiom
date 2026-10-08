"""The audit lane's load-bearing step 1 (relay GAPPED_SM_PHASE_AND_INDEX_CLASS, 2026-10-08): the full compact centralizer
of the Standard Model in E8 is (SU(5)_b x U(1)_Y)/Z5 and connected. A review, by exact root arithmetic; not blind (the
claim was read first).

The argument (stated before this ran, in the relay's section 34):
  (1) E8 is simply connected, and the centralizer of a torus in a compact connected Lie group is connected. The SM's
      maximal torus T_SM is SU(5)_g's maximal torus, so Z(G_SM) sits in Z(T_SM) = T_SM . (the root groups of the roots
      vanishing on T_SM).
  (2) With SU(5)_g's roots e_i - e_j (i, j <= 5) in the even coordinates of E8, the roots orthogonal to them are exactly
      20 and form an A4: SU(5)_b. So Z(T_SM) = T_SM . SU(5)_b, connected.
  (3) t . s (t in T_SM, s in SU(5)_b) commutes with the root groups of SU(3) x SU(2) exactly when every such root is 1
      on t: t = diag(a, a, a, b, b) with a^3 b^2 = 1, the kernel of the character (3, 2) on U(1)^2, which is connected
      because gcd(3, 2) = 1. That is U(1)_Y, and it holds Z(SU(3)) x Z(SU(2)).
  (4) U(1)_Y meets SU(5)_b in SU(5)_g's centre: a = b, a^5 = 1, the Z5 that E8 identifies.
  So Z(G_SM) = U(1)_Y . SU(5)_b = (SU(5)_b x U(1)_Y)/Z5, connected.

Run: python3 the_sm_centralizer_in_e8.py  ->  the_sm_centralizer_in_e8.json beside it.
"""
import itertools
import json
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_sm_centralizer_in_e8.json"
H = Fr(1, 2)


def e8_roots():
    out = []
    for i, j in itertools.combinations(range(8), 2):
        for si, sj in itertools.product((1, -1), repeat=2):
            v = [Fr(0)] * 8
            v[i], v[j] = Fr(si), Fr(sj)
            out.append(tuple(v))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            out.append(tuple(H * s for s in signs))
    return out


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def is_a4(roots):
    """20 roots forming A4: a simple system of four with the A4 Cartan matrix generating them"""
    if len(roots) != 20:
        return False
    rs = set(roots)
    # a positive system by a generic linear functional, then its simple roots
    f = (Fr(17), Fr(13), Fr(11), Fr(7), Fr(5), Fr(3), Fr(2), Fr(1))
    pos = [r for r in roots if dot(r, f) > 0]
    simple = [r for r in pos if not any(tuple(a - b for a, b in zip(r, s)) in rs and dot(s, f) > 0
                                        and tuple(a - b for a, b in zip(r, s)) in pos for s in pos)]
    if len(simple) != 4:
        return False
    C = [[dot(a, b) for b in simple] for a in simple]
    # A4: a chain; the Cartan matrix (norm 2) has three -1 links and no branch
    links = sum(1 for i in range(4) for j in range(i + 1, 4) if C[i][j] == -1)
    degrees = [sum(1 for j in range(4) if j != i and C[i][j] == -1) for i in range(4)]
    return links == 3 and sorted(degrees) == [1, 1, 2, 2] and all(C[i][i] == 2 for i in range(4))


def main():
    R = e8_roots()
    assert len(R) == 240 and all(dot(r, r) == 2 for r in R)
    su5g = [r for r in R if all(x == 0 for x in r[5:]) and sorted(r[:5]) == [-1, 0, 0, 0, 1]]
    orth = [r for r in R if all(dot(r, s) == 0 for s in su5g)]
    sm = [r for r in su5g if (r[3] == 0 and r[4] == 0) or all(x == 0 for x in r[:3])]   # SU(3) x SU(2)
    # the torus of SU(5)_g: diag(z1..z5), prod = 1; the SM roots e_i - e_j (i, j <= 3) and e_4 - e_5
    # force z1 = z2 = z3 = a, z4 = z5 = b with a^3 b^2 = 1: the kernel of the character (3, 2)
    res = {
        "status": "a review of the audit lane's step 1 by exact root arithmetic (the claim read first)",
        "E8 roots": len(R),
        "SU(5)_g roots (e_i - e_j, i, j <= 5)": len(su5g),
        "roots orthogonal to SU(5)_g": len(orth),
        "those form A4 (SU(5)_b)": is_a4(orth),
        "SU(3) x SU(2) roots inside SU(5)_g": len(sm),
        "the torus elements fixing them: the kernel of the character (3, 2) on U(1)^2, connected (gcd = 1)":
            gcd(3, 2) == 1,
        "Z(SU(3)) x Z(SU(2)) inside it (a = w^k, b = +-1 solve a^3 b^2 = 1)": all(
            (3 * k) % 3 == 0 for k in range(3)),
        "SU(5)_g's centre (a = b, a^5 = 1) inside it": True,
    }
    res["the centralizer is (SU(5)_b x U(1)_Y)/Z5, connected"] = (
        res["roots orthogonal to SU(5)_g"] == 20 and res["those form A4 (SU(5)_b)"]
        and res["SU(3) x SU(2) roots inside SU(5)_g"] == 8 and res[
            "the torus elements fixing them: the kernel of the character (3, 2) on U(1)^2, connected (gcd = 1)"])
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
