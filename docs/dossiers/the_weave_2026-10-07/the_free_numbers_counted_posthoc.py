"""W52, POST HOC (written after W52's one run, which recorded C2 and C3 as failed). Two degeneracies, derived by hand
after the read-out, are checked here against every rank W52 computed. Nothing in W52's JSON is changed.

  P1  the zero-diagonal identity. For a symmetric matrix with zero diagonal, [[0, x, y], [x, 0, z], [y, z, 0]], the
      invariants of Y^H Y satisfy t2 = t1^2 / 4 (t1 = 2(|x|^2 + |y|^2 + |z|^2), t2 = (|x|^2 + |y|^2 + |z|^2)^2), so
      (m1^2 + m2^2 + m3^2)^2 = 4 (m1^2 m2^2 + m1^2 m3^2 + m2^2 m3^2), that is m3 = m1 + m2 exactly. Checked on the O+ forms
      at k = 1 and k = 3 at random tau.
  P2  the dependency pattern. The CKM and the up and down ratios depend only on tau and the up and down sectors' own
      coefficients; each sector's ratios only on tau and its own. With P1 (a sector whose coupling is O+ alone has one
      ratio, not two), the generic rank is 3 plus the largest matching between those observables and the parameters
      they depend on. Compared with all 128 computed ranks.
  P3  the quark sector at the geometry's weight: the number of quark observables (four ratios and the CKM's four) and
      of the parameters they depend on.

Run: python3 the_free_numbers_counted_posthoc.py  ->  the_free_numbers_counted_posthoc.json beside it.
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_free_numbers_counted as FC  # noqa: E402  (W52: the forms by frame and weight)

OUT = HERE / "the_free_numbers_counted_posthoc.json"


def P1(forms):
    rng = np.random.default_rng(5201)
    worst_t, worst_m = 0.0, 0.0
    for k in (1, 3):
        f = forms["Sym^2 T"][k][0]                       # the one symmetric coupling there: O+ alone
        for _ in range(5):
            t = complex(rng.uniform(-0.45, 0.45), rng.uniform(0.95, 2.0))
            Y = f(t)
            G = Y.conj().T @ Y
            t1 = float(np.real(np.trace(G)))
            t2 = float(np.real((np.trace(G) ** 2 - np.trace(G @ G)) / 2))
            worst_t = max(worst_t, abs(t2 - t1 ** 2 / 4) / t1 ** 2)
            m = np.sort(np.linalg.svd(Y, compute_uv=False))
            worst_m = max(worst_m, abs(m[2] - m[0] - m[1]) / m[2])
            worst_t = max(worst_t, float(np.max(np.abs(np.diag(Y)))) / float(np.max(np.abs(Y))))
    return {"max relative |t2 - t1^2/4| (and the diagonal's size)": worst_t,
            "max relative |m3 - m1 - m2|": worst_m}


def max_matching(rows, ncols):
    """rows: a list of sets of column indices; the size of a largest matching (augmenting paths)"""
    match_col = [-1] * ncols

    def try_row(r, seen):
        for c in rows[r]:
            if c in seen:
                continue
            seen.add(c)
            if match_col[c] == -1 or try_row(match_col[c], seen):
                match_col[c] = r
                return True
        return False

    return sum(1 for r in range(len(rows)) if try_row(r, set()))


def model_rank(ks, ds):
    """3 scales + the largest matching between (ratios, CKM) and (tau, each sector's own coefficients)"""
    cols, start = {"tau": [0, 1]}, 2
    for s, d in zip(FC.SECTORS, ds):
        n = 2 * (d - 1)
        cols[s] = list(range(start, start + n))
        start += n
    groups = []
    for i, (k, d) in enumerate(zip(ks, ds)):
        for g in groups:
            if ks[g[0]] == k and ds[g[0]] == 1 and d == 1:
                g.append(i)
                break
        else:
            groups.append([i])
    rows = []
    for g in groups:
        dep = set(cols["tau"]) | {c for i in g for c in cols[FC.SECTORS[i]]}
        n_ratio = 1 if ds[g[0]] == 1 else 2               # P1: O+ alone has one ratio
        rows += [dep] * n_ratio
    if not any(0 in g and 1 in g for g in groups):
        rows += [set(cols["tau"]) | set(cols["u"]) | set(cols["d"])] * 4
    return 3 + max_matching(rows, start)


def main():
    forms, _ = FC.basis_functions()
    p1 = P1(forms)
    w52 = json.loads((HERE / "the_free_numbers_counted.json").read_text(encoding="utf-8"))
    rows = w52["C2: the scan"]
    agree, table = 0, {}
    for key, v in rows.items():
        frame, ks = key.split(": ")
        ks = tuple(int(x) for x in ks.strip("()").split(", "))
        r2 = model_rank(ks, v["d"])
        got = v["ranks at three points"][0]
        table[key] = {"computed": got, "the model": r2}
        agree += int(r2 == got and len(set(v["ranks at three points"])) == 1)
    quark = {"observables (four ratios and the CKM's four)": 8,
             "parameters they depend on at k = 3, 3 (tau and two complex ratios)": 2 + 2 + 2,
             "relations among them": 8 - 6}
    checks = {
        "P1: O+ alone has t2 = t1^2/4 and m3 = m1 + m2 to 1e-10": bool(
            p1["max relative |t2 - t1^2/4| (and the diagonal's size)"] < 1e-10
            and p1["max relative |m3 - m1 - m2|"] < 1e-10),
        "P2: the matching model reproduces every computed rank (128 of 128)": agree == len(rows) == 128,
    }
    out = {"status": "W52 post hoc: the two degeneracies behind C2's and C3's failures (labelled post hoc)",
           "P1": p1, "P2: the model against the computed ranks": table, "P2: agreements": agree, "P3": quark,
           "checks": {k: bool(v) for k, v in checks.items()}, "every check holds": bool(all(checks.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["checks"], indent=1))
    print("agreements:", agree, "of", len(rows))


if __name__ == "__main__":
    main()
