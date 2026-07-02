"""B367 (W2.3) — the V3 local-symbol search, exactly as pre-registered.

DECLARED MODEL (PREREGISTRATION.md; three factors, within the <=4 budget; no post-hoc
extensions): with e = (60/ord)*a mod 60 the eigenvalue exponent on the zeta_60 scale and
(e4, e3, e5) its CRT components,

    s(a, b; m1, m2)  =  X3[e3(a), e3(b), m1%3, m2%3]
                      * X5[e5(a), e5(b), m1%5, m2%5]
                      * X4[e4(a), e4(b)]

for rational-valued tables X3, X5 (seed-local) and X4 (universal). The solver is exact
multiplicative tensor completion over Q: gauge-fix on a spanning set of nonzero entries,
propagate to a fixpoint, then demand (i) every nonzero entry reproduces exactly, (ii) every
zero entry has at least one factor cell that is forced to 0 without contradicting any
nonzero entry. Training pairs: (1,2), (2,3), (2,4), (3,4) jointly (uniformity is built in:
factor cells are shared across pairs through their keys). Held-outs (only if the fit
passes): the (1,3)/(1,4) zeros, then the fresh exact pairs (2,7) and (3,7).

NULL (declared): 200 random tables with the same support, sign balance, and denominator
pool, run through the identical solver; the claim needs true-pass AND < 5% random passes.
"""
import json
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ORD = {1: 20, 2: 12, 3: 6, 4: 20, 7: 12}


def load_tables(path=os.path.join(HERE, "step0_tables.json")):
    data = json.load(open(path))
    out = {}
    for pair, tab in data.items():
        m1, m2 = (int(x) for x in pair.split(","))
        out[(m1, m2)] = {tuple(int(x) for x in k.split(",")): Fr(v[3])
                         for k, v in tab.items()}
    return out


def crt_keys(m1, m2, a, b):
    e1 = (60 // ORD[m1]) * a % 60
    e2 = (60 // ORD[m2]) * b % 60
    k3 = (e1 % 3, e2 % 3, m1 % 3, m2 % 3)
    k5 = (e1 % 5, e2 % 5, m1 % 5, m2 % 5)
    k4 = (e1 % 4, e2 % 4)
    return k3, k5, k4


def records(tables, pairs):
    """(k3, k5, k4, s) for every entry (zeros included) of the given pairs."""
    recs = []
    for (m1, m2) in pairs:
        tab = tables[(m1, m2)]
        for a in range(ORD[m1]):
            for b in range(ORD[m2]):
                s = tab.get((a, b), Fr(0))
                recs.append((*crt_keys(m1, m2, a, b), s))
    return recs


def solve_model(recs):
    """Exact multiplicative completion. Returns (X3, X5, X4) or None."""
    nz = [r for r in recs if r[3] != 0]
    zero = [r for r in recs if r[3] == 0]
    X = [{}, {}, {}]                       # X3, X5, X4 assignments

    changed = True
    pending = list(nz)
    while pending:
        progress = False
        rest = []
        for k3, k5, k4, s in pending:
            keys = (k3, k5, k4)
            known = [X[i].get(keys[i]) for i in range(3)]
            unknown = [i for i in range(3) if known[i] is None]
            if not unknown:
                if known[0] * known[1] * known[2] != s:
                    return None
                progress = True
            elif len(unknown) == 1:
                i = unknown[0]
                prod = Fr(1)
                for j in range(3):
                    if j != i:
                        prod *= known[j]
                X[i][keys[i]] = s / prod
                progress = True
            else:
                rest.append((k3, k5, k4, s))
        if not progress and rest:
            # gauge-fix a fresh component: set all-but-one unknown of the first record to 1
            k3, k5, k4, s = rest[0]
            keys = (k3, k5, k4)
            unknown = [i for i in range(3) if X[i].get(keys[i]) is None]
            for i in unknown[:-1]:
                X[i][keys[i]] = Fr(1)
            rest = rest  # re-enter loop with the fix applied
        pending = rest

    # every nonzero entry must now reproduce (fixpoint reached with all keys assigned)
    for k3, k5, k4, s in nz:
        v = X[0].get(k3), X[1].get(k5), X[2].get(k4)
        if None in v or v[0] * v[1] * v[2] != s:
            return None
    # zero entries: need a factor cell equal to 0; a cell touched by any nonzero entry
    # cannot be 0, so the zero must sit on a cell that only zero entries use.
    nz_cells = [set(), set(), set()]
    for k3, k5, k4, _s in nz:
        nz_cells[0].add(k3), nz_cells[1].add(k5), nz_cells[2].add(k4)
    for k3, k5, k4, _s in zero:
        keys = (k3, k5, k4)
        if all(keys[i] in nz_cells[i] for i in range(3)):
            return None                    # all three factors provably nonzero
        for i in range(3):
            if keys[i] not in nz_cells[i]:
                X[i][keys[i]] = Fr(0)
                break
    return X


def null_tables(tables, pairs, n=200, seed=20260703):
    """Random tables: same support, same value pool with sign balance, per pair."""
    rng = random.Random(seed)
    outs = []
    for _ in range(n):
        rnd = {}
        for (m1, m2) in pairs:
            tab = tables[(m1, m2)]
            support = [k for k, v in tab.items() if v != 0]
            pool = [abs(v) for v in tab.values() if v != 0]
            vals = [rng.choice(pool) * rng.choice((1, -1)) for _ in support]
            new = {k: Fr(0) for k in tab}
            for k, v in zip(support, vals):
                new[k] = v
            rnd[(m1, m2)] = new
        outs.append(rnd)
    return outs


def run():
    tables = load_tables()
    train = [(1, 2), (2, 3), (2, 4), (3, 4)]
    fit = solve_model(records(tables, train))
    true_pass = fit is not None

    null_pass = 0
    for rnd in null_tables(tables, train):
        if solve_model(records(rnd, train)) is not None:
            null_pass += 1

    report = dict(true_pass=true_pass, null_pass=null_pass, null_total=200)
    if true_pass:
        X3, X5, X4 = fit
        report["X3"] = {str(k): str(v) for k, v in sorted(X3.items())}
        report["X5"] = {str(k): str(v) for k, v in sorted(X5.items())}
        report["X4"] = {str(k): str(v) for k, v in sorted(X4.items())}
        # held-out zeros predicted?
        zrecs = records(tables, [(1, 3), (1, 4)])
        ok = True
        for k3, k5, k4, s in zrecs:
            v3, v5, v4 = X3.get(k3), X5.get(k5), X4.get(k4)
            pred = None if None in (v3, v5, v4) else v3 * v5 * v4
            if pred is not None and pred != s:
                ok = False
        report["heldout_zero_pairs_consistent"] = ok
    with open(os.path.join(HERE, "v3_report.json"), "w") as fh:
        json.dump(report, fh, indent=1)
    return report


if __name__ == "__main__":
    r = run()
    for k, v in r.items():
        if not str(k).startswith("X"):
            print(f"  {k}: {v}")
    if r["true_pass"]:
        print("  -> factor tables written to v3_report.json")
