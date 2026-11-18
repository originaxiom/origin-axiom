#!/usr/bin/env python3
"""W-P1, step 2's sweep follow-up (W-P1b-F). Data-free; no frame is read.

    python3 -I wp1b_followup.py

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, "Step 2, the sweep's follow-up" (committed before this
script). The construction is wp1b_class_test.py's: its text is run up to its group, then the group is built here.

  G1  the orders of the elements whose traces differ between the classes; whether order 10 agrees everywhere;
  G2  rho_a(LR)'s eigenvalue angles (turns) and traces on the even and odd sectors;
  G3  rho_a(T)'s exponents on the even sector (multiples of 1/5);
  G4  the Frobenius-Schur indicators of the even 3 and the odd 2, and the orders of their images (projective for the 3);
  G5  B1953's two facts with D(a, b) = psi(3ab) X^a Z^b: residuals of rho_a(T) D(a, b) rho_a(T)^-1 against D(a, b - a)
      and of rho_a(S) D(a, b) rho_a(S)^-1 against D(-b, a), over the 24 labels.
"""
import pathlib

import numpy as np

src = (pathlib.Path(__file__).resolve().parent / "wp1b_class_test.py").read_text()
exec(compile(src[:src.index("Gs = {a: group(a)")], "wp1b_class_test.py", "exec"))

Gs = {a: group(a)[0] for a in (1, 2)}


def order(g):
    I = np.eye(2, dtype=int)
    A, n = g % 5, 1
    while not np.array_equal(A % 5, I):
        A, n = (A @ g) % 5, n + 1
    return n


# G1
diff_orders, ten_agree = {}, True
for k, (g, M1) in Gs[1].items():
    M2 = Gs[2][k][1]
    same = np.isclose(np.trace(M1), np.trace(M2))
    o = order(g)
    if not same:
        diff_orders[o] = diff_orders.get(o, 0) + 1
    if o == 10 and not same:
        ten_agree = False
counts = {}
for k, (g, M) in Gs[1].items():
    counts[order(g)] = counts.get(order(g), 0) + 1
print("G1: elements by order: %s; the elements whose traces differ, by order: %s; traces agree on every element of "
      "order 10: %s" % (dict(sorted(counts.items())), dict(sorted(diff_orders.items())), ten_agree))

# G2, G3
gam = np.array([[2, 1], [1, 1]])
for a in (1, 2):
    M = Gs[a][key(gam)][1]
    out = []
    for name, B in (("even", EVEN), ("odd", ODD)):
        blk = B.T @ M @ B
        ang = sorted(round((np.angle(w) / (2 * np.pi)) % 1, 6) % 1 for w in np.linalg.eigvals(blk))
        out.append("%s sector angles %s, trace %.6f%+.0ei" % (name, ang, np.trace(blk).real, np.trace(blk).imag))
    print("G2 a=%d: rho(LR): %s (phi = %.6f, 1 - phi = %.6f)" % (a, "; ".join(out), (1 + 5 ** 0.5) / 2,
                                                                 1 - (1 + 5 ** 0.5) / 2))
for a in (1, 2):
    S, T = weil(a)
    ex = sorted(int(round(((np.angle(w) / (2 * np.pi)) % 1) * 5)) % 5 for w in np.linalg.eigvals(EVEN.T @ T @ EVEN))
    print("G3 a=%d: rho(T)'s exponents on the even sector: %s" % (a, ex))

# G4
for a in (1, 2):
    G = Gs[a]
    res = []
    for name, B in (("3 (even)", EVEN), ("2 (odd)", ODD)):
        fs = sum(np.trace(B.T @ (M @ M) @ B) for g, M in G.values()) / len(G)
        imgs = set()
        for g, M in G.values():
            blk = B.T @ M @ B
            imgs.add(tuple(np.round(blk, 6).ravel()))
        res.append("%s: indicator %.6f, image of order %d" % (name, fs.real, len(imgs)))
    print("G4 a=%d: %s" % (a, "; ".join(res)))

# G5
psi = lambda x: z ** (x % 5)
D3 = lambda p, q: psi(3 * p * q) * np.linalg.matrix_power(Xs, p % 5) @ np.linalg.matrix_power(Zs, q % 5)
V = [(p, q) for p in range(5) for q in range(5) if (p, q) != (0, 0)]
for a in (1, 2):
    S, T = weil(a)
    rT = max(np.abs(T @ D3(p, q) @ np.linalg.inv(T) - D3(p, q - p)).max() for p, q in V)
    rS = max(np.abs(S @ D3(p, q) @ np.linalg.inv(S) - D3(-q, p)).max() for p, q in V)
    print("G5 a=%d: B1953's facts: T against D(a, b - a): residual %.1e; S against D(-b, a): residual %.1e" % (a, rT, rS))
