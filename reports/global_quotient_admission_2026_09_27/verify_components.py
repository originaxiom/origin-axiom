"""Post-lattice component quotient; all finite scalar characters included."""
from functools import lru_cache
from itertools import product
from math import prod
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
import verify_monomial_lifts as m

CERTIFICATES = [
    [-5,-5,2,-5,-5,0,-7,0,0,0,5,-2,-2,-2,-2,1,1,-6,1,1,-2,5,-2,-2,-2,-7,0,0,0,0],
    [0,-5,-5,-3,-5,0,0,-7,0,0,-2,3,-2,0,-2,-6,1,1,1,1,-2,-2,3,0,-2,0,-7,0,0,0],
]


def compact_certificate(number):
    p, _ = m.action_and_cocycle(number)
    for domain in ("free", "mu", "both"):
        c, _, _ = m.rows(p, domain)
        certificate = sp.Matrix([CERTIFICATES[number]+[0]*(c.rows-30)])
        assert certificate*c == m.obstruction_row()
    return {"seed": number, "all_three_domains_liftable": True,
            "small_integer_certificate": CERTIFICATES[number]}


@lru_cache(None)
def components(number):
    p, exponent = m.action_and_cocycle(number)
    c, generators, words = m.rows(p, "both")
    d, u, v = [x.to_Matrix() for x in smith_normal_decomp(DomainMatrix.from_Matrix(c).convert_to(sp.ZZ))]
    assert d == u*c*v and abs(u.det()) == abs(v.det()) == 1
    r = c.rank()
    active = [i for i in range(r) if abs(d[i, i]) > 1]
    moduli = tuple(abs(int(d[i, i])) for i in active)
    vi = v.inv()
    def label(x):
        y = vi*x
        all_labels = [d[i,i]*y[i] for i in range(r)]
        assert all(a.q == 1 for a in all_labels)
        return tuple(int(all_labels[i]) % abs(int(d[i,i])) for i in active)
    universe = set(product(*(range(n) for n in moduli)))
    a = sp.Matrix(m.admission.topology_control()["relation_matrix"])[:, 1:]
    chars, _ = m.admission.finite_characters(a, 40)
    image = set()
    for character in chars:
        x = sp.Matrix([sp.Rational(a,40) for a in (0,*character) for _ in range(5)])
        assert all(t.q == 1 for t in c*x)
        image.add(label(x))
    def plus(x, y):
        return tuple((a+b) % n for a,b,n in zip(x,y,moduli))
    assert all(plus(x,y) in image for x in image for y in image)
    # The admissible diagonal-gauge torus and connected exponent family.
    _, mu, lam = m.cover(6)
    end_ps = [m.word(w, generators)[0] for w in (mu,lam)]
    end_constraints = sp.Matrix.vstack(*(sp.eye(5)-sp.eye(5)[list(m.inverse_perm(q)),:] for q in end_ps))
    neutral_diagonals = sp.Matrix.hstack(*end_constraints.nullspace())
    gauge = sp.Matrix.vstack(*(sp.eye(5)-sp.eye(5)[list(m.inverse_perm(q)),:] for q in p))*neutral_diagonals
    assert c*gauge == sp.zeros(c.rows,gauge.cols)
    joined = gauge.row_join(exponent)
    assert joined.rank() == c.cols-r and c*joined == sp.zeros(c.rows,joined.cols)
    answer = {"seed":number, "component_factors":moduli, "total_components":len(universe),
              "scalar_character_count":len(chars), "scalar_component_image":len(image),
              "residual_component_count":len(universe)//len(image),
              "slice_gauge_rank":gauge.rank(), "connected_family_plus_gauge_rank":joined.rank(),
              "identity_component_dimension":c.cols-r}
    witnesses=[]
    for i in active:
        if d[i,i] % 3:
            continue
        x = v[:,i]/3
        key = label(x)
        if key in image:
            continue
        cosets=[{plus(tuple(j*k % n for k,n in zip(key,moduli)), z) for z in image} for j in range(3)]
        if set.union(*cosets) != universe or sum(map(len,cosets)) != len(universe):
            continue
        phases=[list(x[5*j:5*j+5,0]) for j in range(7)]
        assert all(sum(q).q == 1 for q in phases)
        for w in words:
            _, value=m.literal_evaluate(w,p,phases)
            assert all(q.q == 1 for q in value)
        assert all((3*q).q == 1 for q in x)
        witnesses.append({"modulus":3, "generator_output_phases":[[int(3*q)%3 for q in row] for row in phases],
                          "component_label":key,"all_three_cosets_cover":True,
                          "determinant_one_all_generators":True})
        break
    answer["order_three_witnesses"]=witnesses
    if answer["residual_component_count"] == 3:
        assert len(witnesses)==1, "quotient order three found but explicit family witness not established"
    return answer


def run():
    for number in range(2):
        print("CERTIFICATE",json.dumps(compact_certificate(number)),flush=True)
        print("COMPONENTS",json.dumps(components(number)),flush=True)
    print("PASS: component quotient evaluated; no mode count inferred")


if __name__ == "__main__":
    run()
