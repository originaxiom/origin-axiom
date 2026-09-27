"""Exact character/weight audit. Standard library only, no upstream imports."""
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path
import json

ZERO4 = (0, 0, 0, 0)


def unit(i, n=8):
    return tuple(int(j == i) for j in range(n))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def ip(a, b):
    return sum(x*y for x, y in zip(a, b))


def roots_twice():
    roots = []
    for i, j in combinations(range(8), 2):
        for a, b in product((-2, 2), repeat=2):
            r = [0]*8
            r[i], r[j] = a, b
            roots.append(tuple(r))
    roots.extend(s for s in product((-1, 1), repeat=8) if s.count(-1) % 2 == 0)
    return roots


def bases_twice():
    gauge = [tuple(2*x for x in sub(unit(i), unit(i+1))) for i in range(4)]
    struct = [tuple(2*x for x in sub(unit(6), unit(7))),
              tuple(2*x for x in sub(unit(5), unit(6))),
              tuple(2*x for x in add(unit(6), unit(7))), (-1,)*8]
    return gauge, struct


def dynkin(r, basis):
    dots = [ip(r, b) for b in basis]
    assert all(x % 4 == 0 for x in dots)
    return tuple(x//4 for x in dots)


def a4_labels(v):
    return tuple(v[i]-v[i+1] for i in range(4))


def exterior(k):
    return Counter(a4_labels(tuple(int(i in chosen) for i in range(5)))
                   for chosen in combinations(range(5), k))


def adjoint():
    out = Counter({ZERO4: 4})
    for i in range(5):
        for j in range(5):
            if i != j:
                out[a4_labels(sub(unit(i, 5), unit(j, 5)))] += 1
    return out


def dual(weights):
    return Counter({tuple(-x for x in w): m for w, m in weights.items()})


def tensor(a, b):
    return Counter({(u, v): x*y for u, x in a.items() for v, y in b.items()})


def expected_branching(wrong_conjugation=False):
    one = Counter({ZERO4: 1})
    five, ten, ad = exterior(1), exterior(2), adjoint()
    out = tensor(ad, one) + tensor(one, ad)
    out += tensor(ten, five) + tensor(dual(ten), dual(five))
    out += tensor(five, ten if wrong_conjugation else dual(ten))
    out += tensor(dual(five), ten)
    return out


def actual_branching(include_cartan=True):
    g, s = bases_twice()
    out = Counter((dynkin(r, g), dynkin(r, s)) for r in roots_twice())
    if include_cartan:
        out[(ZERO4, ZERO4)] += 8
    return out


def sm_label(g):
    return (g[0], g[1], g[3], -2*g[0]-4*g[1]-6*g[2]-3*g[3])


def fibre(weights, label):
    out = Counter()
    for (g, s), mult in weights.items():
        if sm_label(g) == label:
            out[s] += mult
    return out


SECTOR_LABELS = {"Q": (1, 0, 1, 1), "u": (0, 1, 0, -4),
                 "e": (0, 0, 0, 6), "d": (0, 1, 0, 2),
                 "L": (0, 0, 1, -3)}


def character_profiles():
    data = json.loads(Path(__file__).with_name("INPUTS.json").read_text())
    n = data["modulus"]
    assert all(data[k][0] == 0 for k in ("chi", "gamma", "hypercharge_character"))
    def rotate(c, k):
        xs = c[1:]
        return [c[0]] + xs[k:] + xs[:k]
    profiles = {}
    for name, y, gam in data["sectors"]:
        rows = []
        for shift in data["deck_shifts"]:
            c = rotate(data["chi"], shift)
            g = rotate(data["gamma"], shift)
            h = rotate(data["hypercharge_character"], shift)
            for sign in (1, -1):
                rows.append(tuple((sign*a+gam*b+y*d) % n for a,b,d in zip(c,g,h)))
        profiles[name] = rows
    return profiles, n


def oriented_grid_count(rows, n):
    assert len(rows) == 6 and len({len(r) for r in rows}) == 1
    good = trials = 0
    for top in combinations(range(6), 3):
        bottom = tuple(i for i in range(6) if i not in top)
        for matched in permutations(bottom):
            trials += 1
            ds = [tuple((x-y) % n for x,y in zip(rows[i], rows[j]))
                  for i,j in zip(top, matched)]
            good += ds[0] == ds[1] == ds[2]
    assert trials == 120
    return good


def synthetic_grid():
    a = [(0,)*7, (7, 11, 0, 0, 0, 0, 0)]
    b = [(0, 0, 13, 0, 0, 0, 0), (0, 0, 0, 17, 0, 0, 0),
         (0, 0, 0, 0, 19, 0, 0)]
    return [add(x,y) for x in a for y in b]


def run():
    roots = roots_twice()
    assert len(roots) == len(set(roots)) == 240 and all(ip(r,r) == 8 for r in roots)
    gauge, struct = bases_twice()
    expected_cartan = [[2 if i == j else -int(abs(i-j) == 1) for j in range(4)] for i in range(4)]
    for basis in (gauge, struct):
        assert [[ip(a,b)//4 for b in basis] for a in basis] == expected_cartan
        assert all(b in roots for b in basis)
    assert all(ip(g,s) == 0 for g in gauge for s in struct)
    actual = actual_branching()
    assert actual == expected_branching() and sum(actual.values()) == 248
    assert actual != expected_branching(wrong_conjugation=True)
    assert actual_branching(False) != actual
    ranks = {}
    for name, label in SECTOR_LABELS.items():
        predicted = exterior(1 if name in ("Q", "u", "e") else 2)
        assert fibre(actual,label) == predicted
        assert fibre(actual,tuple(-x for x in label)) == dual(predicted)
        ranks[name] = sum(predicted.values())
    neutral = fibre(actual, (0,0,0,0))
    assert sum(neutral.values()) == 28
    neutral[ZERO4] -= 3
    assert neutral == adjoint() + Counter({ZERO4:1})
    mixed = [a4_labels(sub(unit(i,5),unit(j,5))) for i in range(2) for j in range(2,5)]
    assert len(set(mixed)) == 6
    assert all(actual[(ZERO4,w)] == 1 and actual[(ZERO4,tuple(-x for x in w))] == 1 for w in mixed)
    profiles, n = character_profiles()
    counts = {name:oriented_grid_count(rows,n) for name,rows in profiles.items()}
    assert set(counts.values()) == {0}
    synthetic = oriented_grid_count(synthetic_grid(),n)
    assert synthetic > 0
    return {"scope":"specified E8 adjoint parent and literal M6 character seed; not physical modes",
            "full_weight_multiset_dimension":sum(actual.values()), "charged_coefficient_ranks":ranks,
            "SM_singlet_algebra_dimension":sum(neutral.values()), "naive_zero_weight_count":28,
            "each_mixed_six_is_SM_neutral":True, "oriented_pairings_per_sector":120,
            "M6_successful_oriented_pairings":counts, "synthetic_successful_pairings":synthetic,
            "wrong_conjugation_and_missing_Cartans_rejected":True}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
