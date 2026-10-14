"""POST HOC (labelled), after the referee of the meditation: B517's self-coupling carried from the golden half-tick F
to the threads. No prediction is scored.

B517: the two-way coupling [[F, C], [D, F]] with C, D in Z[F] (the commutant), both nontrivial (not 0, not I),
nonnegative entries; among entries {0,1,2,3}^4 the unique irreducible Pisot quartic is (C, D) = (F, F^2) (or exchanged).
Carried to a thread W (det +1), Z[W] = span{I, W}. Read-outs, for F (control) and every Lyndon word of length 2..8:
  S1  the shape (C, D) = (W, W^2): irreducible Pisot?
  S2  the shape (C, D) = (W, W + I): irreducible Pisot? (At F the two shapes coincide, since F^2 = F + I.)
  S3  B517's scan: C = c0 I + c1 W, D = d0 I + d1 W with c0, c1, d0, d1 in {0,1,2,3}, C and D not 0 and not I:
      how many (C, D) give an irreducible Pisot characteristic polynomial.
'Pisot' here: exactly one root of modulus > 1, it is real and > 1, all others of modulus < 1; 'irreducible' over Q.

Run once:  python3 -B post_hoc_self_coupling.py > post_hoc_self_coupling_run.txt 2>&1
"""
import json, pathlib
import numpy as np
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
x = sp.symbols("x")


def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()


def mat(word):
    M = sp.eye(2)
    for ch in word:
        M = M * (sp.Matrix([[1, 0], [1, 1]]) if ch == "L" else sp.Matrix([[1, 1], [0, 1]]))
    return M


def pisot_irreducible(W, C, D):
    T = sp.Matrix(sp.BlockMatrix([[W, C], [D, W]]))
    p = sp.Poly(T.charpoly(x).as_expr(), x)
    r = np.roots([float(c) for c in p.all_coeffs()])
    big = [z for z in r if abs(z) > 1 + 1e-12]
    small_ok = all(abs(z) < 1 - 1e-12 for z in r if abs(z) <= 1 + 1e-12)
    pis = len(big) == 1 and abs(big[0].imag) < 1e-12 and big[0].real > 1 and small_ok
    irr = len(sp.factor_list(p.as_expr())[1]) == 1 and sp.factor_list(p.as_expr())[1][0][1] == 1
    return bool(pis and irr), [round(float(abs(z)), 4) for z in sorted(r, key=abs, reverse=True)], str(p.as_expr())


I2 = sp.eye(2)
words = {"F (control)": sp.Matrix([[1, 1], [1, 0]])}
for w in lyndon(8):
    if len(w) >= 2:
        words[w] = mat(w)
out = {"status": "post hoc (labelled), after the meditation's referee; no prediction"}
rows = {}
for name, W in words.items():
    s1 = pisot_irreducible(W, W, W * W)
    s2 = pisot_irreducible(W, W, W + I2)
    hits = []
    for c0 in range(4):
        for c1 in range(4):
            for d0 in range(4):
                for d1 in range(4):
                    C = c0 * I2 + c1 * W; D = d0 * I2 + d1 * W
                    if C == sp.zeros(2) or D == sp.zeros(2) or C == I2 or D == I2:
                        continue
                    ok, _, _ = pisot_irreducible(W, C, D)
                    if ok:
                        hits.append([c0, c1, d0, d1])
    rows[name] = {"trace": int(W.trace()), "det": int(W.det()), "S1 (W, W^2)": [s1[0], s1[1]],
                  "S2 (W, W+I)": [s2[0], s2[1], s2[2]], "S3 scan hits": len(hits), "S3 first hits": hits[:6]}
    print(f"{name:<12} tr {int(W.trace()):>3} det {int(W.det()):>2}  S1 {s1[0]!s:<5}  S2 {s2[0]!s:<5}  S3 hits {len(hits)}",
          flush=True)
out["rows"] = rows
out["summary"] = {
    "S1 passes": [n for n, r in rows.items() if r["S1 (W, W^2)"][0]],
    "S2 passes": [n for n, r in rows.items() if r["S2 (W, W+I)"][0]],
    "S2 fails": [n for n, r in rows.items() if not r["S2 (W, W+I)"][0]],
    "S3 admitted": [n for n, r in rows.items() if r["S3 scan hits"] > 0],
    "S3 not admitted": [n for n, r in rows.items() if r["S3 scan hits"] == 0]}
print(json.dumps(out["summary"], indent=1))
(HERE / "post_hoc_self_coupling.json").write_text(json.dumps(out, indent=1) + "\n")
