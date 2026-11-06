"""B1845 -- the object's own level-5 line (RL fixes exactly (1/5, 2/5), (2/5, 4/5)), the excursion's apexes (Re 1/2 exact,
Im -> 2 + sqrt5/2), and the period average's committed output (the hierarchy washed out away from the apex). Data-free."""
import json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent


def _mat(s):
    L = np.array([[1, 0], [1, 1]], dtype=object); R = np.array([[1, 1], [0, 1]], dtype=object); M = np.eye(2, dtype=object)
    for ch in s:
        M = M.dot(L if ch == "L" else R)
    return M


def _fixed5(A):
    out = set()
    I = np.eye(2, dtype=object)
    for B in (A - I, A + I):
        for x in range(5):
            for y in range(5):
                if (x, y) == (0, 0):
                    continue
                w = np.array([x, y], dtype=object).dot(B)
                if all(int(e) % 5 == 0 for e in w):
                    out.add(min((x, y), ((-x) % 5, (-y) % 5)))
    return out


def test_level_five_is_the_objects_own():
    LR = _mat("LR"); P = np.eye(2, dtype=object)
    orders = []
    for k in range(1, 11):
        P = P.dot(LR) % 5
        if (P == np.eye(2, dtype=object)).all() or (P == 4 * np.eye(2, dtype=object)).all():
            orders.append(k)
    assert orders == [5, 10]


def test_the_objects_own_order_five_lines():
    assert _fixed5(_mat("RL")) == {(1, 2), (2, 4)}
    assert _fixed5(_mat("LR")) == {(1, 3), (2, 1)}


def test_the_excursion_apexes_and_the_period_average_output():
    t = (HERE / "approximants_run.txt").read_text(encoding="utf-8")
    assert "k=12" in t and "Re 0.500000" in t and "3.118033988769" in t
    d = json.loads((HERE / "period_N41.json").read_text(encoding="utf-8"))
    rows = d["rows"]; assert len(rows) == 41 and abs(d["ell"] - 13.6) < 0.01
    apex = min(rows, key=lambda r: abs(r["t"]))
    for key in ("up_St", "down_S"):
        A = np.array([r["lnratios"][key] for r in rows])
        assert apex["lnratios"][key][1] < A.mean(0)[1] - 3.0, key      # the apex is far more hierarchical than the loop
    assert np.mean([r["reduced"][1] > 2 for r in rows]) < 0.25
