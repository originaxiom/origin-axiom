#!/usr/bin/env python3
"""W15, part 3: THE WEAVE'S FIVE. The spin doublet extended by the three parity lines along the weave's own classes, read
with F-HE's pair (I(W), I(Lambda^2 W)).

The weave's vacuum carries a doublet and a triplet: the spin doublet A = rho_Q (x) kappa (W9) and the three parity lines
B_p (W8), each made trivial on the cusp. Their sum has the shape of the Standard Model's 5 = 2 + 3. An extension class
c_p in H^1(A (x) B_p^*) for each parity glues them into the rank-five module

    W = [[A, (c_1 B_1, c_2 B_2, c_3 B_3)], [0, diag(B_1, B_2, B_3)]],

defined on every odd-trace thread at once. sm:B1509's frame (F-HE) reads a rank-five module by the pair
(I(W), I(Lambda^2 W)), with N(10') = -I(W) and N(5bar') = -I(Lambda^2 W); its generation shape is (-1, -1). The pair is
read here for W and for its dual (the other order of the extension), with no claim that the frame's dictionary applies:
GENESIS FK11 stays as it is.

The rule (named before the run): every odd-trace state of GENESIS to length 6 at tick 3; kappa every 24th root of unity
at which all three groups H^1(A (x) B_p^*) are non-zero; the classes c_p a basis class of each group (all combinations of
basis classes, at most 2 x 2 x 2) and one generic choice. The determinant of W is recorded (F-HE's frame is SU(5)').
sm:B1374's engine reads the indices over GF(p), p = 1 mod 24, with its identity checks.

    python3 the_weaves_five.py   ->  the_weaves_five.json beside it
"""
import itertools
import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_weave_extension as WE  # noqa: E402

IL, LV = WE.IL, WE.LV


def wedge2(F, M):
    d = len(M)
    pairs = [(i, j) for i in range(d) for j in range(i + 1, d)]
    return [[(M[k][i] * M[l][j] - M[l][i] * M[k][j]) % F.p for (i, j) in pairs] for (k, l) in pairs]


def five(S, A, Bvals, cvecs):
    F = S.F
    out = {}
    for gi, g in enumerate(S.gens):
        M = [[0] * 5 for _ in range(5)]
        for r in range(2):
            for c in range(2):
                M[r][c] = A[g][r][c]
        for p in range(3):
            b = Bvals[p][g]
            cv = cvecs[p][gi * 2:(gi + 1) * 2]
            M[0][2 + p] = cv[0] * b % F.p
            M[1][2 + p] = cv[1] * b % F.p
            M[2 + p][2 + p] = b
        out[g] = M
    return out


def read(S, mats):
    F = S.F
    W = IL.Rep(F, S.gens, mats)
    assert W.check_relators(S.rels)
    I1 = IL.index(W, S.rels, S.mu, S.lam)[0]
    L2 = IL.Rep(F, S.gens, {g: wedge2(F, mats[g]) for g in S.gens})
    assert L2.check_relators(S.rels)
    I2 = IL.index(L2, S.rels, S.mu, S.lam)[0]
    det_t = 1
    for r in range(5):
        det_t = det_t * mats["t"][r][r] % F.p                       # block upper-triangular: det = product of diagonal
    return I1, I2, det_t


def run(states=WE.STATES, seed=11):
    rng = random.Random(seed)
    p = LV.primes_for(24, k=1, start=20000)[0]
    F = IL.GF(p)
    z = F.root_of_unity(24)
    zpow = {pow(z, k, p): k for k in range(24)}
    res, summary = {"prime": p}, {}
    for sw in states:
        t0 = time.time()
        S = WE.Tick3(sw, F, z)
        Bvals = [S.B(par) for par in WE.PARITIES]
        rows = []
        for kexp in range(24):
            A = S.A_mats("0", kexp)
            bases = [S.h1_basis(IL.Rep(F, S.gens, S.tensor_scalar(A, Bv))) for Bv in Bvals]
            if not all(bases):
                continue
            choices = [("basis", idx) for idx in itertools.product(*[range(len(b)) for b in bases])]
            choices.append(("generic", None))
            for kind, idx in choices:
                if kind == "basis":
                    cvecs = [bases[q][i] for q, i in enumerate(idx)]
                else:
                    cvecs = []
                    for b in bases:
                        coef = [rng.randrange(1, p) for _ in b]
                        cvecs.append([sum(c * v[j] for c, v in zip(coef, b)) % p for j in range(len(b[0]))])
                mats = five(S, A, Bvals, cvecs)
                I1, I2, dt = read(S, mats)
                dual = {g: S.F.T(S.F.inverse(mats[g])) for g in S.gens}
                J1 = IL.index(IL.Rep(F, S.gens, dual), S.rels, S.mu, S.lam)[0]
                J2 = IL.index(IL.Rep(F, S.gens, {g: wedge2(F, dual[g]) for g in S.gens}), S.rels, S.mu, S.lam)[0]
                rows.append({"kappa (24ths)": kexp, "dims": [len(b) for b in bases],
                             "classes": kind if kind == "generic" else list(idx),
                             "W: (I(W), I(L2 W))": [I1, I2], "W*: (I, I(L2))": [J1, J2],
                             "det W on t (24ths)": zpow.get(dt)})
        pairs = sorted({tuple(r["W: (I(W), I(L2 W))"]) for r in rows})
        dpairs = sorted({tuple(r["W*: (I, I(L2))"]) for r in rows})
        summary[sw] = {"readings": len(rows), "pairs for W": [list(x) for x in pairs],
                       "pairs for W*": [list(x) for x in dpairs],
                       "kappas": sorted({r["kappa (24ths)"] for r in rows}),
                       "dets (24ths)": sorted({r["det W on t (24ths)"] for r in rows if r["det W on t (24ths)"] is not None}),
                       "seconds": round(time.time() - t0, 1)}
        res[sw] = rows
        print(sw, json.dumps(summary[sw]), flush=True)
    res["summary"] = summary
    return res


if __name__ == "__main__":
    states = sys.argv[1:] or WE.STATES
    out = run(states)
    if states == WE.STATES:                   # a partial run (states named on the command line) writes nothing
        with open(HERE / "the_weaves_five.json", "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
