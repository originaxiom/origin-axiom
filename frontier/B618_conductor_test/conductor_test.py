"""B618 — the conductor-unification third-object test (registered
prediction, sealed in B617's FINDINGS before this run).

THE PREDICTION: the trace-5 bundle (word R^3 L, monodromy [[4,3],[1,1]],
torsion base tr^2 - 4 = 21 = disc Q(sqrt 21)) shows its eigenvalue-field
content in the odd hearing trace at 21-related levels — kappa = 0 mod d
for some d | 21, d > 1 — mirroring the fig-8's mod-5 law and m136's
mod-12 content. FALSIFIABLE: content could appear at unrelated kappa or
never (then the conductor unification dies at n = 3).
OPERATIONAL TEST (declared): compute tr B_odd(kappa) for kappa = 4..45;
classify each value's field: rational/cyclotomic-only (the "generic"
family: values in Q(zeta_24)-type small cyclotomics with rational-only
magnitudes) vs sqrt(21)-BEARING (detected by: the value's conjugate-pair
{v, v'} under sqrt21 -> -sqrt21 reconstruction — practically, test
whether Re/Im are rational combinations a + b*sqrt(21) with small
rational a, b via PSLQ-style lattice fit at 30 digits; report the
kappa-set carrying sqrt(21) content).
"""
import importlib.util
import math
import os
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)


def odd_trace(level, word):
    w, S, T, cc = b238.su3_data(level)
    n = len(w)
    Cm = np.zeros((n, n))
    for i, wt in enumerate(w):
        Cm[w.index((wt[1], wt[0])), i] = 1.0
    R = T
    L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
    W = np.eye(n, dtype=complex)
    for ch in word:
        W = W @ (R if ch == "R" else L)
    prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    U = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        U[w.index((a, b)), j] = 1 / np.sqrt(2)
        U[w.index((b, a)), j] = -1 / np.sqrt(2)
    return np.trace(-(U.T @ W @ U))


def fit_sqrt(x, root, den_max=24, tol=1e-9):
    """x ~ a + b*sqrt(root), a,b rational with denominator <= den_max?"""
    s = math.sqrt(root)
    for db in range(1, den_max + 1):
        for nb in range(-4 * db, 4 * db + 1):
            b = nb / db
            a = x - b * s
            fa = Fraction(a).limit_denominator(den_max)
            if abs(float(fa) - a) < tol:
                if nb != 0:
                    return (fa, Fraction(nb, db))
                # rational-only
                return (fa, Fraction(0))
    return None


print("B618 — the tr-5 (R^3 L) conductor scan:", flush=True)
bearing = []
for kap in range(4, 46):
    tr = odd_trace(kap - 3, "RRRL")
    hits = []
    for part, val in (("Re", tr.real), ("Im", tr.imag)):
        if abs(val) < 1e-9:
            continue
        f = fit_sqrt(val, 21)
        if f and f[1] != 0:
            hits.append(f"{part} = {f[0]} + {f[1]}*sqrt21")
    tag = ("  <-- sqrt(21)-BEARING: " + "; ".join(hits)) if hits else ""
    if hits:
        bearing.append(kap)
    print(f"  kappa={kap:>2}: tr = {tr.real:+.9f}{tr.imag:+.9f}j{tag}",
          flush=True)

print(f"\nsqrt(21)-bearing levels: {bearing}", flush=True)
d21 = [k for k in bearing if k % 21 == 0]
d7 = [k for k in bearing if k % 7 == 0]
d3 = [k for k in bearing if k % 3 == 0]
pred = bool(bearing) and all(k % 21 == 0 or k % 7 == 0 or k % 3 == 0
                             for k in bearing)
print(f"of these: mod-21 {d21}, mod-7 {d7}, mod-3 {d3}", flush=True)
print(f"PREDICTION VERDICT (content at d|21 levels only, d>1): "
      f"{'PASS' if pred else ('FAIL' if bearing else 'NO CONTENT FOUND — FAIL (no window)')}",
      flush=True)
print("B618 DONE", flush=True)
