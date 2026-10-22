#!/usr/bin/env python3
"""W121 — the record's triplet on the closed 4d solutions (the script; `W121_RULE.md` was committed and pushed
before it).

- P1: the record's flat bundle at a pinched record: rho_Q of every primitive class's Christoffel word.
- P2, P3: the record's own rho_T and its conjugate (W45's kept identifications, imported from
  `the_index_on_the_weaves_surface.py`): the lifted product of 2k positive twists, and each factor's exponents.
- P4: the count on K3 (24 strings), by the sum over the factors and by the stack degree.
- P5: the general law over chi(O_S) and the base genus.

    python3 -B the_triplet_on_k3.py      # writes the_triplet_on_k3.json and the_triplet_on_k3_run.txt beside itself
"""
import contextlib
import io
import json
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_index_on_the_weaves_surface as W45  # noqa: E402

out, log = {"arc": "W121", "rule": "W121_RULE.md"}, []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    log.append(s)


# ---------------- P1: the vanishing cycles under rho_Q ----------------
QI = np.array([[1j, 0], [0, -1j]])
QJ = np.array([[0, 1], [-1, 0]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def christoffel(p, q):
    """the lower Christoffel word with |p| a's and |q| b's (letters inverted for negative p or q)"""
    P, Q = abs(p), abs(q)
    n = P + Q
    w = []
    for i in range(1, n + 1):
        w.append("a" if (i * Q) // n == ((i - 1) * Q) // n else "b")
    return [(c, (1 if (p >= 0 if c == "a" else q >= 0) else -1)) for c in w]


def rhoQ(word):
    M = I2.copy()
    for c, e in word:
        g = QI if c == "a" else QJ
        M = M @ (g if e == 1 else np.linalg.inv(g))
    return M


classes, bad = 0, []
for p in range(-30, 31):
    for q in range(-30, 31):
        if (p, q) == (0, 0) or math.gcd(p, q) != 1:
            continue
        classes += 1
        M = rhoQ(christoffel(p, q))
        order4 = np.allclose(M @ M, -I2, atol=1e-12) and not np.allclose(M, I2) and not np.allclose(M, -I2)
        if not order4:
            bad.append([p, q])
P1 = {"primitive classes": classes, "not of order 4": bad, "holds": not bad and classes > 0}
say("P1 primitive classes", classes, "| not of order 4:", bad, "->", P1["holds"])
out["P1"] = P1

# ---------------- P2, P3: the record's rho_T and its conjugate ----------------
with contextlib.redirect_stdout(io.StringIO()):
    _, kept = W45.E3()
hands = {"rho_T": kept["S <-> S~, T <-> L^-1"], "rho_T bar": kept["S <-> S~^-1, T <-> L"]}


def exponents(M):
    lam = sorted((float(np.angle(z) / (2 * np.pi)) % 1.0) for z in np.linalg.eigvals(M))
    return [Fr(x).limit_denominator(24) for x in lam], max(abs(x - float(Fr(x).limit_denominator(24))) for x in lam)


P2, P3 = {}, {}
for name, (rS, rT) in hands.items():
    rS, rT = np.array(rS, dtype=complex), np.array(rT, dtype=complex)
    tw2 = rS @ rT @ np.linalg.inv(rS)                       # rho(S T S^-1), the second positive twist
    Q = rT @ tw2
    scal, P = {}, np.eye(3, dtype=complex)
    for k in range(1, 13):
        P = P @ Q
        c = P[0, 0]
        if np.allclose(P, c * np.eye(3), atol=1e-12):
            scal[k] = [round(c.real, 12), round(c.imag, 12)]
    P2[name] = {"scalar at k": sorted(scal), "values": {str(k): v for k, v in scal.items()},
                "holds": sorted(scal) == [3, 6, 9, 12] and scal.get(6) == [-1.0, 0.0] and scal.get(12) == [1.0, 0.0]}
    say("P2", name, ": (rho(T) rho(STS^-1))^k scalar at k =", sorted(scal), "values", scal, "->", P2[name]["holds"])
    eT, dT = exponents(rT)
    e2, d2 = exponents(tw2)
    want = [Fr(1, 8), Fr(3, 8), Fr(7, 8)] if name == "rho_T" else [Fr(1, 8), Fr(5, 8), Fr(7, 8)]
    P3[name] = {"exponents of rho(T)": [str(x) for x in eT], "exponents of rho(STS^-1)": [str(x) for x in e2],
                "rounding": max(dT, d2), "sum": str(sum(eT)), "no exponent is 0": all(x != 0 for x in eT + e2),
                "holds": eT == want and e2 == want and max(dT, d2) < 1e-9 and all(x != 0 for x in eT + e2)}
    say("P3", name, ": exponents", [str(x) for x in eT], "and", [str(x) for x in e2], "| rounding %.2g" % max(dT, d2),
        "->", P3[name]["holds"])
out["P2"], out["P3"] = P2, P3

# ---------------- P4: the count on K3 ----------------
P4 = {}
for name in hands:
    mu = sum(Fr(x) for x in P3[name]["exponents of rho(T)"])
    factors = 24
    deg_sum = -factors * mu                                   # the canonical extension, factor by factor
    deg_stack = Fr(48) * (-Fr(1, 2) * mu)                    # D = 24 chi(O_S) = 48 times the stack degree
    spinor = Fr(0)                                           # K_C (x) L = O on K3
    index = 3 * spinor + deg_sum + 3 * (1 - 0)
    P4[name] = {"degree by the factors": str(deg_sum), "degree by the stack": str(deg_stack),
                "index": str(index), "holds": deg_sum == deg_stack and index == (-30 if name == "rho_T" else -36)}
    say("P4", name, ": degree", deg_sum, "=", deg_stack, "| index on K3", index, "->", P4[name]["holds"])
out["P4"] = P4

# ---------------- P5: the general law ----------------
P5 = {}
for name in hands:
    mu = sum(Fr(x) for x in P3[name]["exponents of rho(T)"])
    law = -15 if name == "rho_T" else -18
    table, ok = {}, True
    for chi in (2, 4, 6):
        for g in (0, 1, 2):
            N = 12 * chi
            idx = Fr(3, 2) * (2 * g - 2 + chi) - N * mu + 3 * (1 - g)
            table[f"chi {chi}, g {g}"] = str(idx)
            ok &= idx == law * chi
    never3 = all(abs(law * chi) != 3 for chi in range(2, 101, 2))
    k3 = law * 2
    added = sorted(n for n in range(0, 40) if abs(k3 + 3 * n) == 3)
    parity = all(((2 * g - 2 + chi) % 2 == 0) == (chi % 2 == 0) == ((12 * chi) % 24 == 0)
                 for chi in range(1, 13) for g in range(0, 4))
    want_added = [9, 11] if name == "rho_T" else [11, 13]
    P5[name] = {"index by chi and genus": table, "law": f"{law} chi(O_S)", "never +-3 for even chi to 100": never3,
                "added units to reach +-3 on K3": added, "spinor and lift both need chi even": parity,
                "holds": ok and never3 and added == want_added and parity}
    say("P5", name, ": law", law, "chi | genus cancels:", ok, "| never +-3:", never3, "| units to add on K3:", added,
        "| parity:", parity, "->", P5[name]["holds"])
out["P5"] = P5

out["verdict"] = {"P1": P1["holds"], "P2": all(v["holds"] for v in P2.values()),
                  "P3": all(v["holds"] for v in P3.values()), "P4": all(v["holds"] for v in P4.values()),
                  "P5": all(v["holds"] for v in P5.values())}
say("verdict", out["verdict"])
(HERE / "the_triplet_on_k3.json").write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
(HERE / "the_triplet_on_k3_run.txt").write_text("\n".join(log) + "\n", encoding="utf-8")
