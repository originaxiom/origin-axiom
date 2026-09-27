"""Exhaustive finite ansatz; diagnostics explicitly capped before execution."""
import hashlib
import json
from itertools import permutations
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "global_sl5_seed_2026_09_27"))
from verify_global_seed import (
    DEGREE, Rep, circle_restrictions, eye, indexed, kron, null_columns,
    pullback, wedge_over_field, zero,
)
from verify_topology import cover
from flint import fmpq_mat


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    out = [0]*len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def even(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2 == 0


def word_value(word, generators):
    value = tuple(range(6))
    invs = [inverse(p) for p in generators]
    for x in word:
        value = compose(value, generators[x-1] if x > 0 else invs[-x-1])
    return value


def generated_group(generators):
    identity = tuple(range(6))
    found, queue = {identity}, [identity]
    for p in queue:
        for g in generators:
            q = compose(p, g)
            if q not in found:
                found.add(q)
                queue.append(q)
    return found


def doubly_transitive(group):
    return len({(g[0], g[1]) for g in group}) == 30


def augmentation(p):
    return fmpq_mat([[int(i == p[j])-int(i == p[5]) for j in range(5)] for i in range(5)])


def scan_fixed_meridian(t):
    all_perms = list(permutations(range(6)))
    elements = [p for p in all_perms if even(p)]
    ids = {p: i for i, p in enumerate(elements)}
    mul = [[ids[compose(p, q)] for q in elements] for p in elements]
    invs = [ids[inverse(p)] for p in elements]
    identity, tid = ids[tuple(range(6))], ids[t]
    rels, _, _ = cover(2)
    centralizer = [p for p in all_perms if compose(p, t) == compose(t, p)]
    conjugations = [[ids[compose(compose(c, p), inverse(c))] for p in elements] for c in centralizer]
    valid, transitive, irreducible = 0, 0, 0
    representatives = {}
    for b in range(360):
        for c in range(360):
            gens = (tid, b, c)
            ok = True
            for rel in rels:
                v = identity
                for x in rel:
                    g = gens[abs(x)-1]
                    v = mul[v][g if x > 0 else invs[g]]
                if v != identity:
                    ok = False
                    break
            if not ok:
                continue
            valid += 1
            group = generated_group([t, elements[b], elements[c]])
            transitive += len({g[0] for g in group}) == 6
            if not doubly_transitive(group):
                continue
            irreducible += 1
            key = min((action[b], action[c]) for action in conjugations)
            representatives[key] = len(group)
    ordered = sorted(representatives)
    digest = hashlib.sha256(json.dumps(ordered, separators=(",", ":")).encode()).hexdigest()
    cap = inputs()["diagnostic_cap_per_meridian"]
    selected = [{"B": elements[b], "C": elements[c], "pair_ids": [b, c],
                 "image_order": representatives[(b, c)]} for b, c in ordered[:cap]]
    return {"pairs_examined": 360**2, "relator_solutions": valid,
            "transitive_solutions": transitive, "irreducible_solutions": irreducible,
            "centralizer_order_in_S6": len(centralizer),
            "permutation_conjugacy_representatives": len(ordered),
            "representative_list_sha256": digest, "selected": selected,
            "unanalysed_representatives": max(0, len(ordered)-cap)}


def symmetric_tracefree_action(generators):
    n = 5
    gram = eye(n)+fmpq_mat([[1]*n for _ in range(n)])
    units = []
    for i in range(n):
        for j in range(n):
            x = zero(n, n)
            x[i, j] = 1
            units.append(x)
    cols = []
    for x in units:
        constraint = x.transpose()*gram-gram*x
        cols.append([constraint[i, j] for i in range(n) for j in range(n)]
                    +[sum(x[i, i] for i in range(n))])
    constraints = fmpq_mat(list(map(list, zip(*cols))))
    basis = null_columns(constraints)
    assert basis.ncols() == 14
    echelon, rank = basis.transpose().rref()
    selected = [next(j for j in range(25) if echelon[i, j]) for i in range(rank)]
    square = fmpq_mat([[basis[i, j] for j in range(14)] for i in selected])
    invsquare = square.inv()
    actions = []
    for g in generators:
        assert g.transpose()*gram*g == gram
        gi = g.inv()
        columns = []
        for j in range(14):
            x = fmpq_mat([[basis[5*i+k, j] for k in range(5)] for i in range(5)])
            transformed = g*x*gi
            columns.append([transformed[i, k] for i in range(5) for k in range(5)])
        target = fmpq_mat(list(map(list, zip(*columns))))
        rows = fmpq_mat([[target[i, j] for j in range(14)] for i in selected])
        action = invsquare*rows
        assert basis*action == target
        actions.append(action)
    return actions


def diagnostics(t, row):
    permutations_ = [t, tuple(row["B"]), tuple(row["C"])]
    rels, mu, lam = cover(2)
    identity = tuple(range(6))
    assert all(word_value(r, permutations_) == identity for r in rels)
    group = generated_group(permutations_)
    assert doubly_transitive(group) and len(group) == row["image_order"]
    matrices = [augmentation(p) for p in permutations_]
    gram = eye(5)+fmpq_mat([[1]*5 for _ in range(5)])
    assert all(g.det() == 1 and g.transpose()*gram*g == gram for g in matrices)
    e = Rep([kron(g, eye(DEGREE)) for g in matrices])
    wedge = Rep([wedge_over_field(g) for g in e.mats])
    deformations = Rep([kron(g, eye(DEGREE)) for g in symmetric_tracefree_action(matrices)])
    assert e.word(mu)**3 == eye(e.d)
    result = {"permutations": permutations_, "image_order": len(group),
              "longitude_permutation": word_value(lam, permutations_), "coefficients": {}}
    for name, rep in (("E", e), ("wedge2E", wedge)):
        down, up = indexed(rep, 2), indexed(pullback(rep), 6)
        assert down["I"] == up["I"] == 0
        result["coefficients"][name] = {"down": down, "up": up,
                                        "up_interior_dimension": up["V"][1]-up["V"][4]}
    result["E_up_capacity_at_least_three"] = result["coefficients"]["E"]["up"]["V"][2] >= 3
    result["nonorthogonal_deformation_data"] = indexed(deformations, 2)
    result["nonorthogonal_restriction_profile"] = circle_restrictions(deformations, 2)
    return result


def main():
    out = {}
    for name, meridian in inputs()["meridians"].items():
        t = tuple(meridian)
        scan = scan_fixed_meridian(t)
        print("SCAN", name, json.dumps(scan), flush=True)
        rows = []
        for i, row in enumerate(scan["selected"]):
            result = diagnostics(t, row)
            rows.append(result)
            print("SEED", name, i, json.dumps(result), flush=True)
        out[name] = {"scan": scan, "diagnostics": rows}
    print("SUMMARY", json.dumps({name: {"irreducible_representatives": v["scan"]["permutation_conjugacy_representatives"],
                                       "analysed": len(v["diagnostics"]),
                                       "unanalysed": v["scan"]["unanalysed_representatives"],
                                       "capacity_and_meridian_tangent": [
                                           [d["E_up_capacity_at_least_three"], d["nonorthogonal_restriction_profile"]["meridian_kernel"]]
                                           for d in v["diagnostics"]]}
                               for name, v in out.items()}))
    print("PASS: exact finite-domain search; no chiral or nonlinear-integrability claim")


if __name__ == "__main__":
    main()
