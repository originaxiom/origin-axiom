#!/usr/bin/env python3
"""W140 — the hypercharge line inside E6: which flat lines the weave allows, and which line orders keep m_e = m_d in
the joint frame's extended matrices, against main's frame (the rule: W140_RULE.md, committed and pushed before this
script existed).

  C1  the weave's line: the points of (Z/N)^2 fixed by L and R (and -I), N <= 12; the orbits of <L, R> against the
      sets of points of each exact order
  C2  the threads' lines: the lines of order <= 12 up to sign (B1713's 266); each fixed by the thread L^N R^N
  C3  the control: the light-fields model, each Yukawa entry a generic coupling F of the three fields' labels
      (family, 6Y mod N); which sector pairs coincide for N = 1 ... 12, with and without the sign symmetry
  C4  the joint frame: W139's extended 6 x 6 matrices, each entry weighted by F of its three components' labels; the
      three light masses at hierarchical vevs
  C5  the read-out: the census in lines up to sign; the six singular values at non-hierarchical vevs; D per order

    python3 -B the_hypercharge_line.py      # writes the_hypercharge_line.json beside itself
"""
import contextlib
import io
import itertools
import json
import platform
import random
import sys
import time
import traceback
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_e6_breaking as EB  # noqa: E402  (W139: monomials, components, NEUTRAL, QROWS, QCOLS, LROWS, LCOLS)

OUT = HERE / "the_hypercharge_line.json"
mp.mp.dps = 30
NMAX = 12
LM = ((1, 1), (0, 1))
RM = ((1, 0), (1, 1))
COINCIDE, SPLIT = 1e-20, 1e-6
DRAWS = 5


# ------------------------------------------------------------------ C1, C2: the lines
def act(M, v, N):
    return ((M[0][0] * v[0] + M[0][1] * v[1]) % N, (M[1][0] * v[0] + M[1][1] * v[1]) % N)


def order(v, N):
    return N // gcd(gcd(v[0], v[1]), N)


def C1():
    rows, ok = {}, True
    for N in range(1, NMAX + 1):
        pts = list(itertools.product(range(N), repeat=2))
        fixed = [v for v in pts if act(LM, v, N) == v and act(RM, v, N) == v]
        fixed_mi = [v for v in fixed if ((-v[0]) % N, (-v[1]) % N) == v]
        seen, orbits = set(), []
        for v in pts:
            if v in seen:
                continue
            orb, todo = {v}, [v]
            while todo:
                w = todo.pop()
                for M in (LM, RM):
                    x = act(M, w, N)
                    if x not in orb:
                        orb.add(x)
                        todo.append(x)
            seen |= orb
            orbits.append(frozenset(orb))
        by_order = {}
        for v in pts:
            by_order.setdefault(order(v, N), set()).add(v)
        same = set(orbits) == {frozenset(s) for s in by_order.values()}
        rows[N] = {"fixed by L and R": [list(v) for v in fixed], "fixed by L, R and -I": [list(v) for v in fixed_mi],
                   "orbits": len(orbits), "orbit sizes": sorted(len(o) for o in orbits),
                   "orbits are the exact-order sets": same}
        ok &= fixed == [(0, 0)] and fixed_mi == [(0, 0)] and same
    return {"per N": rows}, bool(ok)


def matpow(M, n):
    out = ((1, 0), (0, 1))
    for _ in range(n):
        out = tuple(tuple(sum(out[i][k] * M[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return out


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def lines_up_to_sign():
    pts = set()
    for N in range(1, NMAX + 1):
        for a, b in itertools.product(range(N), repeat=2):
            pts.add((Fr(a, N), Fr(b, N)))
    canon = set()
    for v in pts:
        w = ((-v[0]) % 1, (-v[1]) % 1)
        canon.add(min(v, w))
    return sorted(canon)


def line_order(v):
    d = 1
    for x in v:
        d = d * x.denominator // gcd(d, x.denominator)
    return d


def C2():
    lines = lines_up_to_sign()
    fixed_ok, traces = True, {}
    for v in lines:
        N = line_order(v)
        W = matmul(matpow(LM, N), matpow(RM, N))
        traces[N] = W[0][0] + W[1][1]
        img = ((W[0][0] * v[0] + W[0][1] * v[1]) % 1, (W[1][0] * v[0] + W[1][1] * v[1]) % 1)
        fixed_ok &= img == v
    hyperbolic = all(t == N * N + 2 and t > 2 for N, t in traces.items())
    per_order = {}
    for v in lines:
        per_order[line_order(v)] = per_order.get(line_order(v), 0) + 1
    r = {"lines of order <= 12 up to sign": len(lines), "per order": dict(sorted(per_order.items())),
         "each fixed by L^N R^N": bool(fixed_ok), "traces of L^N R^N": dict(sorted(traces.items())),
         "all hyperbolic with trace N^2 + 2": bool(hyperbolic)}
    return r, len(lines) == 266 and fixed_ok and hyperbolic, lines


# ------------------------------------------------------------------ the generic coupling
def crand(rng, scale=1):
    return mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)) * scale


class Coupling:
    """F(l1, l2, l3), totally symmetric in its labels l = (family, q mod N); with sign=True also invariant under
    negating every twist. Values drawn lazily, so the table holds only the labels used."""

    def __init__(self, N, rng, sign):
        self.N, self.rng, self.sign, self.tab = N, rng, sign, {}

    def G(self, labels):
        key = tuple(sorted(labels))
        if key not in self.tab:
            self.tab[key] = crand(self.rng)
        return self.tab[key]

    def __call__(self, *labels):
        labels = tuple((f, q % self.N) for f, q in labels)
        if not self.sign:
            return self.G(labels)
        return self.G(labels) + self.G(tuple((f, (-q) % self.N) for f, q in labels))


def svals(M):
    S = mp.svd_c(M, compute_uv=False)
    return sorted(S[i] for i in range(S.rows))


def maxlog(x, y):
    return max(abs(mp.log(a / b)) for a, b in zip(x, y))


def classify(vals):
    if max(vals) < COINCIDE:
        return "coincide"
    if min(vals) > SPLIT:
        return "split"
    return "neither"


# ------------------------------------------------------------------ C3: the light-fields model
Q6 = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "Hu": 3, "Hd": -3}
SECTORS = {"u": ("Q", "u", "Hu"), "d": ("Q", "d", "Hd"), "e": ("L", "e", "Hd")}
PAIRS = (("d", "e"), ("u", "d"), ("u", "e"))
PRED3 = {True: {"d=e": {1, 2, 4, 5}, "u=d": {1, 2, 3, 6}, "u=e": {1, 2, 7}},
         False: {"d=e": {1, 2, 4, 5}, "u=d": {1, 2, 3, 6}, "u=e": {1, 2}}}


def light_masses(F, h):
    out = {}
    for X, (l, r, hf) in SECTORS.items():
        M = mp.matrix(3, 3)
        for a, b in itertools.product(range(3), repeat=2):
            M[a, b] = sum((F((a, Q6[l]), (b, Q6[r]), (j, Q6[hf])) * h[j] for j in range(3)), mp.mpc(0))
        out[X] = svals(M)
    return out


def C3():
    rows, ok = {}, True
    for sign in (True, False):
        rng = random.Random(1400 + sign)
        per = {}
        for N in range(1, NMAX + 1):
            vals = {"%s=%s" % p: [] for p in PAIRS}
            for _ in range(DRAWS):
                F = Coupling(N, rng, sign)
                h = [crand(rng) for _ in range(3)]
                m = light_masses(F, h)
                for x, y in PAIRS:
                    vals["%s=%s" % (x, y)].append(float(maxlog(m[x], m[y])))
            per[N] = {k: {"class": classify(v), "max |ln ratio|": max(v), "min |ln ratio|": min(v)}
                      for k, v in vals.items()}
        found = {k: sorted(N for N in per if per[N][k]["class"] == "coincide") for k in PRED3[sign]}
        clean = all(per[N][k]["class"] != "neither" for N in per for k in per[N])
        match = all(set(found[k]) == PRED3[sign][k] for k in found)
        rows["with the sign symmetry" if sign else "without the sign symmetry"] = {
            "per N": per, "coinciding orders": found, "predicted": {k: sorted(v) for k, v in PRED3[sign].items()},
            "every order clean": bool(clean), "as predicted": bool(match)}
        ok &= clean and match
    return rows, bool(ok)


# ------------------------------------------------------------------ C4: E6's extended matrices
def q6_of_components():
    return {i: int(6 * y) for i, _, _, _, y, _ in EB.components()}


def extended(F, vevs, q6):
    tab = EB.hessian_table(1)
    Mq, Ml = mp.matrix(6, 6), mp.matrix(6, 6)
    for (M, rows, cols) in ((Mq, EB.QROWS, EB.QCOLS), (Ml, EB.LROWS, EB.LCOLS)):
        for a, b in itertools.product(range(3), repeat=2):
            for s, t in itertools.product(range(2), repeat=2):
                p, q = rows[s], cols[t]
                M[2 * a + s, 2 * b + t] = sum((c * F((a, q6[p]), (b, q6[q]), (j, q6[r])) * vevs[j].get(r, 0)
                                               for j in range(3) for c, r in tab.get((p, q), [])), mp.mpc(0))
    return Mq, Ml


def random_vevs(rng, singlet_scale):
    vevs = []
    for _ in range(3):
        vevs.append({idx: crand(rng, singlet_scale if n >= 3 else 1) for n, idx in enumerate(EB.NEUTRAL)})
    return vevs


def C4():
    q6 = q6_of_components()
    assert all(sum(q6[i] for i in m) == 0 for _, m in EB.monomials(1))  # every monomial is neutral
    rows, ok = {}, True
    six = {}
    for sign in (True, False):
        rng = random.Random(1410 + sign)
        per = {}
        for N in range(1, NMAX + 1):
            light, Ds, allsix = [], [], []
            for _ in range(DRAWS):
                F = Coupling(N, rng, sign)
                vh = random_vevs(rng, 10**4)
                Mq, Ml = extended(F, vh, q6)
                sq, sl = svals(Mq), svals(Ml)
                light.append(float(maxlog(sq[:3], sl[:3])))
                Ds.append(float(abs(mp.log((sl[1] * sq[0]) / (sq[1] * sl[0])))))
                vn = random_vevs(rng, 1)
                Mq, Ml = extended(F, vn, q6)
                allsix.append(float(maxlog(svals(Mq), svals(Ml))))
            per[N] = {"class": classify(light), "max |ln ratio| (light three)": max(light),
                      "min |ln ratio| (light three)": min(light), "median |ln D|": sorted(Ds)[DRAWS // 2],
                      "six singular values, non-hierarchical": classify(allsix)}
        found = sorted(N for N in per if per[N]["class"] == "coincide")
        clean = all(per[N]["class"] != "neither" for N in per)
        key = "with the sign symmetry" if sign else "without the sign symmetry"
        rows[key] = {"per N": per, "coinciding orders": found, "predicted": [1, 5], "every order clean": bool(clean),
                     "as predicted": bool(found == [1, 5])}
        six[key] = sorted(N for N in per if per[N]["six singular values, non-hierarchical"] == "coincide")
        ok &= clean and found == [1, 5]
    rows["twists 6Y of the 27's components"] = {str(i): q6[i] for i in sorted(q6)}
    return rows, bool(ok), six


def C5(lines, c3, c4, six):
    def count(orders):
        return sum(1 for v in lines if line_order(v) in set(orders))
    main_set = c3["with the sign symmetry"]["coinciding orders"]["d=e"] if c3 else None
    joint_set = c4["with the sign symmetry"]["coinciding orders"] if c4 else None
    return {"lines up to sign": len(lines),
            "keep d = e in main's frame (C3, with the sign symmetry)": count(main_set) if main_set else None,
            "keep d = e in the joint frame (C4, with the sign symmetry)": count(joint_set) if joint_set else None,
            "orders where all six extended singular values coincide (non-hierarchical)": six}


def guarded(fn, *args):
    try:
        return fn(*args), None
    except Exception:  # a failed part is a failed launch of that part (the rule's discipline)
        return None, traceback.format_exc()


def main():
    t0 = time.time()
    out, cells, errors = {"arc": "W140", "rule": "W140_RULE.md", "status": "one run"}, {}, {}
    r, err = guarded(C1)
    if err:
        errors["C1"], cells["C1"] = err, False
    else:
        out["C1"], cells["C1"] = r
    r, err = guarded(C2)
    lines = []
    if err:
        errors["C2"], cells["C2"] = err, False
    else:
        out["C2"], cells["C2"], lines = r
    r, err = guarded(C3)
    if err:
        errors["C3"], cells["C3"] = err, False
    else:
        out["C3"], cells["C3"] = r
    r, err = guarded(C4)
    six = None
    if err:
        errors["C4"], cells["C4"] = err, False
    else:
        out["C4"], cells["C4"], six = r
    r, err = guarded(C5, lines, out.get("C3"), out.get("C4"), six)
    if err:
        errors["C5"] = err
    else:
        out["C5 (read-out)"] = r
    out["cells"] = {k: bool(cells[k]) for k in ("C1", "C2", "C3", "C4")}
    out["every cell holds"] = bool(all(out["cells"].values()))
    out["errors"] = errors
    out["environment"] = {"python": platform.python_version(), "mpmath": mp.__version__}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])
    if errors:
        print("errors:", ", ".join(errors), file=sys.stderr)


if __name__ == "__main__":
    main()
