"""Direct cone check for the separately authored exceptional-neighborhood bound."""
import json
from functools import lru_cache

from verify_exceptional import companion, cohom, inputs, modules, scaled, specialization
from verify_global_seed import eye, hs, null_columns, pullback, vs, zero
from verify_topology import cover


def relative_h1(rep, n, degree):
    rels, mu, lam = cover(n)
    d, ng = rep.d, len(rep.mats)
    d0 = vs(*(g-eye(d) for g in rep.mats))
    d1 = vs(*(hs(*(rep.fox(r, g) for g in range(1, ng+1))) for r in rels))
    restriction = vs(*(hs(*(rep.fox(w, g) for g in range(1, ng+1))) for w in (mu, lam)))
    boundary0 = vs(rep.word(mu)-eye(d), rep.word(lam)-eye(d))
    cone0 = vs(d0, eye(d))
    cone1 = vs(hs(d1, zero(d1.nrows(), d)), hs(restriction, -boundary0))
    assert cone1*cone0 == zero(cone1.nrows(), d)
    assert cone0.rank() == d
    value = scaled((cone1.ncols()-cone1.rank()-cone0.rank(),), degree)[0]
    ordinary, _ = cohom(rep, n, degree)
    a0, a1, t0, _, r1 = ordinary
    assert value == a1-r1+t0-a0
    return {"relative_H1": value, "ordinary": ordinary, "interior": a1-r1,
            "cone1_shape_over_Q": [cone1.nrows(), cone1.ncols()],
            "cone1_rank_over_Q": cone1.rank()}


@lru_cache(None)
def check_points():
    rows = []
    for i, seed in enumerate(inputs()["seeds"]):
        mods = modules(seed)
        for polynomial in (["1", "-1"], ["1", "1", "1", "1", "1"]):
            value = companion(polynomial)
            degree = value.nrows()
            rep = pullback(specialization(mods["E"], value))
            assert rep.word(cover(6)[1]) == eye(rep.d)
            row = {"seed": i, "polynomial": polynomial,
                   "E": relative_h1(rep, 6, degree),
                   "dual": relative_h1(rep.dual(), 6, degree)}
            for side in ("E", "dual"):
                assert row[side]["relative_H1"] == 3
                assert row[side]["ordinary"][2] == 3
            assert row["E"]["ordinary"][2] == row["dual"]["ordinary"][2]
            rows.append(row)
    return rows


def main():
    for row in check_points():
        print("POINT", json.dumps(row), flush=True)
    print("BOUND", json.dumps({str(b): min(b, 3-b) for b in range(4)}))
    print("PASS: direct relative cone inputs; scoped nearby fixed-meridian bound at most one")


if __name__ == "__main__":
    main()
