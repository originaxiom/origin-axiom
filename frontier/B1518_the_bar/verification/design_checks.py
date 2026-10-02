"""B1518 -- design-time facts about the covariates (no outcome is read): disclosed in PREREGISTRATION section 2.

  F1  odd word length forces even fibre torsion (both signs); the literature sweep's check, proved here and counted
  F2  (|G|, sign) fixes the trace of A: tr A = |G| + 2 for sign +, |G| - 2 for sign -
  F3  the strata: how many units sit in S1, S2 and S3 strata with at least two members (the tests' power)
  F4  reversal symmetry against symmetry order and amphichirality, by manifold (T3 and T4's confounding)
  F5  exponent-two levels: how many own levels and census levels have N <= 2 (where main's B1442 lemma decides)
  F6  the conditional tests' power: strata holding both values of the tested feature

    python3 design_checks.py --write    # writes design_checks.json
"""
import json
import pathlib
import sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from covariates import word  # noqa: E402

STRATA = {"S1": ["d1", "d2"], "S2": ["d1", "d2", "sign"], "S3": ["d1", "d2", "sign", "symmetry_order"]}


def manifold_units(rows):
    g = defaultdict(list)
    for r in rows:
        g[r["manifold"]].append(r)
    return [rs[0] for _, rs in sorted(g.items())]


def facts():
    rows = json.loads((HERE / "covariates.json").read_text(encoding="utf-8"))["rows"]
    lev = json.loads((HERE / "level_covariates.json").read_text(encoding="utf-8"))["rows"]
    U = manifold_units(rows)
    f = {}
    # F1: mod 2, L and R are the two transpositions of SL(2, F2) = S3; an odd word is a transposition, trace 0 mod 2
    odd = [r for r in rows if r["length"] % 2]
    f["F1 odd length: states, of which torsion even"] = [len(odd), sum(1 for r in odd if r["torsion"] % 2 == 0)]
    even = [r for r in rows if r["length"] % 2 == 0]
    ev_even = [r for r in even if r["torsion"] % 2 == 0]
    mod2_identity = [r for r in even if all(x % 2 == (i == j) for i, row_ in enumerate(word(r["word"]))
                                            for j, x in enumerate(row_))]
    f["F1 even length: states, torsion even, A = I mod 2"] = [len(even), len(ev_even), len(mod2_identity)]
    f["F1 even length: torsion even exactly when A = I mod 2"] = {r["state"] for r in ev_even} == {
        r["state"] for r in mod2_identity}
    # F2
    ok = all((sum(word(r["word"])[i][i] for i in range(2)) == (r["torsion"] + 2 if r["sign"] == "+"
                                                               else r["torsion"] - 2)) for r in rows)
    f["F2 (|G|, sign) fixes tr A on every state"] = ok
    # F3
    for name, keys in STRATA.items():
        s = Counter(tuple(u[k] for k in keys) for u in U)
        f[f"F3 {name} strata (manifolds): strata, units in strata of size >= 2"] = [
            len(s), sum(n for n in s.values() if n >= 2)]
    # F4
    ct = Counter((u["reversal_closed"], u["symmetry_order"]) for u in U)
    f["F4 manifolds by (reversal-closed, symmetry order)"] = {f"{a}, {b}": n for (a, b), n in sorted(ct.items())}
    ca = Counter((u["reversal_closed"], u["amphichiral"]) for u in U)
    f["F4 manifolds by (reversal-closed, amphichiral)"] = {f"{a}, {b}": n for (a, b), n in sorted(ca.items())}
    f["F4 manifolds: units, reversal-closed, amphichiral"] = [len(U), sum(u["reversal_closed"] for u in U),
                                                           sum(u["amphichiral"] for u in U)]
    # F6: the conditional tests can only learn from strata holding both values of their feature
    for feat, keys in (("reversal_closed", ["d1", "d2", "sign"]), ("amphichiral", ["d1", "d2", "sign", "reversal_closed"])):
        s = defaultdict(list)
        for u in U:
            s[tuple(u[k] for k in keys)].append(u[feat])
        both = [v for v in s.values() if any(v) and not all(v)]
        f[f"F6 {feat} given {keys}: informative strata, their units, of which with the feature"] = [
            len(both), sum(len(v) for v in both), sum(sum(v) for v in both)]
    # F5
    f["F5 own levels with exponent <= 2 (manifolds)"] = sum(1 for u in U if u["d2"] <= 2)
    keys = {}
    for r in lev:
        keys.setdefault(r["manifold_key"], r)
    f["F5 census level-manifolds with exponent <= 2"] = sum(1 for r in keys.values() if r["d2"] <= 2)
    f["F5 census level-manifolds by k"] = dict(sorted(Counter(r["k"] for r in keys.values()).items()))
    return f


if __name__ == "__main__":
    out = facts()
    text = json.dumps(out, indent=1, default=list)
    print(text)
    if "--write" in sys.argv:
        (HERE / "design_checks.json").write_text(text + "\n", encoding="utf-8")
