"""B1104 — the 4d suspension selection test (L177). See PREREGISTRATION.md.

Works on the ABSTRACT symmetry group (SnapPy's multiplication table; the cusp
action alone is NOT faithful — kernel of order 2, itself a finding recorded in
the results), attaches each element's cusp matrix and orientation character,
classifies every suspension M x_psi S^1, and runs the sealed filters. The
element->matrix correspondence is SELF-CERTIFIED as a homomorphism against the
multiplication table before any downstream use. Writes b1104_results.json.
"""
import json
import os

import snappy


def mat_of(iso):
    m = iso.cusp_maps()[0]
    return ((int(m[0][0]), int(m[0][1])), (int(m[1][0]), int(m[1][1])))


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2))
                 for i in range(2))


def main():
    M = snappy.Manifold("m004")
    G = M.symmetry_group()
    n = G.order()
    isos = G.isometries()
    assert n == 8 and len(isos) == 8

    table = [[G.multiply_elements(i, j) for j in range(n)] for i in range(n)]
    mats = [mat_of(isos[i]) for i in range(n)]

    # identity element: the row index i with table[i][j] = j for all j
    ident = [i for i in range(n) if all(table[i][j] == j for j in range(n))]
    assert len(ident) == 1
    e = ident[0]

    # self-certify element->matrix as a (anti)homomorphism
    hom = all(mats[table[i][j]] == mul(mats[i], mats[j])
              for i in range(n) for j in range(n))
    antihom = all(mats[table[i][j]] == mul(mats[j], mats[i])
                  for i in range(n) for j in range(n))
    assert hom or antihom, "cusp map is neither hom nor antihom vs the table"

    kernel = [i for i in range(n) if mats[i] == mats[e]]

    def elt_order(i):
        p, k = i, 1
        while p != e:
            p = table[p][i]
            k += 1
            assert k <= 2 * n
        return k

    orders = [elt_order(i) for i in range(n)]
    inv = [next(j for j in range(n) if table[i][j] == e) for i in range(n)]
    center = [i for i in range(n)
              if all(table[i][j] == table[j][i] for j in range(n))]

    def conj_class(i):
        return frozenset(table[table[g][i]][inv[g]] for g in range(n))

    classes = sorted({conj_class(i) for i in range(n)}, key=lambda c: sorted(c))

    rows = []
    for i in range(n):
        A = mats[i]
        d = det(A)
        a = A[0][0]  # image of the meridian's mu-coefficient (SnapPy column conv.)
        h1_tor = abs(a - 1)  # H1(M_psi) = Z + Z/|a-1| (0 -> Z summand)
        rows.append({
            "elt": i, "order": orders[i], "in_center": i in center,
            "in_cusp_kernel": i in kernel,
            "cusp_matrix": [list(A[0]), list(A[1])], "det": d,
            "suspension_orientable": d == 1,
            "h1_mu_coeff": a,
            "H1_suspension": ("Z^2" if a == 1 else f"Z + Z/{h1_tor}"),
        })

    nontrivial = [r for r in rows if r["order"] != 1]
    f_center = [r for r in rows if r["in_center"] and r["order"] != 1]
    f_tick = [r for r in rows if r["det"] == -1 and r["order"] == 2]
    joint = [r for r in rows if r["in_center"] and r["det"] == -1
             and r["order"] == 2]

    c1_pass = False  # |MCG| = 8 finite: no infinite-order element exists
    if len(joint) == 1:
        c2 = "UNIQUE-NONTRIVIAL"
    elif not f_center and not f_tick:
        c2 = "ONLY-TRIVIAL"
    else:
        c2 = "NO-SECTION"
    c3_pass = bool(f_tick)

    out = {
        "group": "D4 (SnapPy), order 8",
        "hom_certified": bool(hom), "antihom_certified": bool(antihom),
        "cusp_kernel_size": len(kernel),
        "element_orders": sorted(orders),
        "conjugacy_class_sizes": sorted(len(c) for c in classes),
        "center_elements": len(center),
        "rows": rows,
        "filters": {
            "nontrivial": len(nontrivial),
            "theta_center_nontrivial": len(f_center),
            "tick_or_reversing_involutions": len(f_tick),
            "joint_survivors": len(joint),
        },
        "C1_escalator_repeat": c1_pass,
        "C2_selection": c2,
        "C3_gieseking_analog": c3_pass,
    }
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "b1104_results.json"), "w") as f:
        json.dump(out, f, indent=2)

    print(f"group order 8; hom={hom} antihom={antihom}; cusp kernel {len(kernel)}")
    print(f"element orders: {sorted(orders)}; classes {sorted(len(c) for c in classes)}; "
          f"center {len(center)}")
    for r in rows:
        print(f"  e{r['elt']}: order {r['order']} center {r['in_center']} "
              f"kernel {r['in_cusp_kernel']} det {r['det']:+d} "
              f"or-susp {r['suspension_orientable']} H1(susp) {r['H1_suspension']}")
    print(f"filters: theta-center {len(f_center)} | tick {len(f_tick)} | joint {len(joint)}")
    print(f"C1 {c1_pass} | C2 {c2} | C3 {c3_pass}")


if __name__ == "__main__":
    main()
