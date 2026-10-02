"""B1518 -- the covariates of main's 988 census levels (B1439), computed before any outcome is read.

Main's B1439 computed, for every signed word state (eps, w) to length 12 and every level k <= 12 whose fibre torsion is at
most 2 000, its generation-shaped backgrounds (the five charged sectors with equal non-zero index; B1434 PREREG :34).
This file reads only the non-outcome fields of main's records (state, k, torsion, N) and adds, with own code:
  - the fibre torsion group G of the level's monodromy (eps A(w))^k, as invariant factors (d1 | d2);
  - the level's manifold key: the level is the bundle of eps^k A(w)^k, so (+w)^k and (-w)^k coincide for even k, and a
    word and its reverse give one manifold (B1517); key = (eps^k, canonical word of w under rotation, swap and reversal, k).
Controls: |G| equals main's torsion and d2 equals main's exponent N on every record.

    python3 level_covariates.py --write    # writes level_covariates.json (no outcome field)
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from covariates import word, mul, smith_2x2, canon_manifold  # noqa: E402

I2 = ((1, 0), (0, 1))


def power(A, k):
    M = I2
    for _ in range(k):
        M = mul(M, A)
    return M


def level_row(state, k):
    eps = 1 if state[0] == "+" else -1
    w = state[1:]
    A = word(w)
    if eps == -1:
        A = ((-A[0][0], -A[0][1]), (-A[1][0], -A[1][1]))
    B = power(A, k)
    M = ((B[0][0] - 1, B[0][1]), (B[1][0], B[1][1] - 1))
    d1, d2 = smith_2x2(M)
    sign_k = "+" if (eps ** k) == 1 else "-"
    return {"state": state, "k": k, "d1": d1, "d2": d2, "torsion_own": d1 * d2,
            "manifold_key": f"{sign_k}{canon_manifold(w)}^{k}"}


def load_main():
    return json.loads((HERE / "main_B1439_levels.json").read_text(encoding="utf-8"))


def table():
    main = load_main()
    rows, bad_t, bad_n = [], [], []
    for r in main["records"]:
        x = level_row(r["state"], r["k"])
        x["torsion_main"] = r["torsion"]
        x["N_main"] = r["N"]
        if x["torsion_own"] != r["torsion"]:
            bad_t.append((r["state"], r["k"]))
        if x["d2"] != r["N"]:
            bad_n.append((r["state"], r["k"]))
        rows.append(x)
    c = {"levels": len(rows), "distinct_manifold_keys": len({x["manifold_key"] for x in rows}),
         "torsion_agrees_on_every_record": not bad_t, "exponent_agrees_on_every_record": not bad_n,
         "disagreements": bad_t[:5] + bad_n[:5]}
    c["passed"] = c["levels"] == 988 and not bad_t and not bad_n
    return rows, c


if __name__ == "__main__":
    rows, c = table()
    print(json.dumps(c, indent=1))
    if "--write" in sys.argv:
        (HERE / "level_covariates.json").write_text(json.dumps({"controls": c, "rows": rows}, indent=0) + "\n",
                                                   encoding="utf-8")
    sys.exit(0 if c["passed"] else 1)
