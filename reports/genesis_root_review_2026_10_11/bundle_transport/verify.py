"""Exact common-point, cohomology and local-boundary transport checks."""
import importlib.util
import json
from functools import lru_cache
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("sealed_word_lifts", HERE.parent / "word_lifts" / "verify.py")
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)
I2, I6 = s.eye(2), s.eye(6)
qi = s.diag(s.I, -s.I)
qj = s.Matrix([[0, 1], [-1, 0]])
qk = qi * qj
PAR = ((1, 0), (0, 1), (1, 1))
UP = dict(zip(PAR, (qj, qi, qk)))
GL, GR = (I2 + qi) / s.sqrt(2), (I2 - qj) / s.sqrt(2)


def clean(m):
    return m.applyfunc(s.simplify)


def equal(a, b):
    return clean(a - b) == s.zeros(*a.shape)


def chi(p, word):
    return (-1) ** sum(p[0 if x.lower() == "a" else 1] for x in word)


@lru_cache(None)
def rep(p, word):
    out = I2
    for x in word:
        a = qi if x.lower() == "a" else qj
        if x.isupper():
            a = -a  # Each quaternion generator has square -I.
        out = out * chi(p, x) * a
    return s.ImmutableMatrix(clean(out))


def after(p, f):
    return tuple(0 if chi(p, f[x]) == 1 else 1 for x in "ab")


def cocycle(p, word, za, zb):
    value, prefix = s.zeros(2, 1), I2
    for x in word:
        z = za if x.lower() == "a" else zb
        if x.isupper():
            z = -rep(p, x) * z
        value += prefix * z
        prefix = prefix * rep(p, x)
    return clean(value)


def project(p, za, zb, chart="a"):
    a, b = rep(p, "a") - I2, rep(p, "b") - I2
    return clean(zb - b * a.inv() * za) if chart == "a" else clean(za - a * b.inv() * zb)


def cohom(f, g, chart="a"):
    out = s.zeros(6)
    gi = g.inv()
    for ip, p in enumerate(PAR):
        q = after(p, f)
        iq = PAR.index(q)
        for k in range(2):
            zero, e = s.zeros(2, 1), I2[:, k]
            za, zb = (zero, e) if chart == "a" else (e, zero)
            aa = gi * cocycle(p, f["a"], za, zb)
            bb = gi * cocycle(p, f["b"], za, zb)
            out[2 * iq:2 * iq + 2, 2 * ip + k] = project(q, aa, bb, chart)
    return clean(out)


def local(f, g):
    out = s.zeros(6)
    for ip, p in enumerate(PAR):
        iq = PAR.index(after(p, f))
        out[2 * iq:2 * iq + 2, 2 * ip:2 * ip + 2] = UP[PAR[iq]].inv() * g * UP[p]
    return clean(out)


def commutant_dimension(gens):
    # Nonzero scalar rescaling leaves a commutator kernel unchanged.
    blocks = [s.kronecker_product(I6, g) - s.kronecker_product(g.T, I6) for g in gens]
    return 36 - s.Matrix.vstack(*blocks).rank()


def verify():
    facts = {}
    def check(name, value):
        facts[name] = bool(value)
        if not value:
            raise AssertionError(name)

    pjs = [s.diag(*[1 if i // 2 == j else 0 for i in range(6)]) for j in range(3)]
    za, zb = s.Matrix([1, 2 + s.I]), s.Matrix([3 - s.I, 5])
    probes = ("", "a", "b", "A", "B", "ab", "aB", "aBAb")
    for ip, p in enumerate(PAR):
        for x in "ab":
            check(f"twist_{ip}_{x}", equal(rep(p, x), UP[p] * rep((0, 0), x) * UP[p].inv()))
        check(f"peripheral_{ip}", equal(rep(p, w.C), -I2))
        check(f"chart_a_invertible_{ip}", (rep(p, "a") - I2).det() != 0)
        check(f"chart_b_invertible_{ip}", (rep(p, "b") - I2).det() != 0)
        ca, cb = (rep(p, "a") - I2) * za, (rep(p, "b") - I2) * za
        check(f"coboundary_chart_a_{ip}", equal(project(p, ca, cb), s.zeros(2, 1)))
        check(f"coboundary_chart_b_{ip}", equal(project(p, ca, cb, "b"), s.zeros(2, 1)))
        for ix, x in enumerate(probes):
            for iy, y in enumerate(probes):
                check(f"cocycle_{ip}_{ix}_{iy}", equal(cocycle(p, x+y, za, zb), cocycle(p, x, za, zb) + rep(p, x) * cocycle(p, y, za, zb)))
            check(f"cocycle_inverse_{ip}_{ix}", equal(cocycle(p, w.inv(x), za, zb), -rep(p, w.inv(x)) * cocycle(p, x, za, zb)))

    base = [(w.L0, GL), (w.R0, GR)]
    cm = [cohom(f, g) for f, g in base]
    lm = [local(f, g) for f, g in base]
    chart_change = s.diag(*[-(rep(p, "a") - I2) * (rep(p, "b") - I2).inv() for p in PAR])
    for i, (f, g) in enumerate(base):
        for x in "ab":
            check(f"lift_{i}_{x}", equal(rep((0, 0), f[x]), g * rep((0, 0), x) * g.inv()))
        check(f"two_charts_{i}", equal(cohom(f, g, "b"), chart_change * cm[i] * chart_change.inv()))
        check(f"local_unitary_{i}", equal(lm[i].H * lm[i], I6))
    check("pullback_order", equal(cohom(w.compose(w.L0, w.R0), GL * GR), cm[1] * cm[0]))
    check("wrong_order_control", not equal(cm[0] * cm[1], cm[1] * cm[0]))

    delta = w.compose(w.L0, w.compose(w.INVERSES[2], w.L0))
    gd = clean(GL * GR.inv() * GL)
    cd = cohom(delta, gd)
    z = clean(cd ** 2)
    check("central_square", equal(z ** 2, -I6))
    projectors = [clean((I6 - s.I * z) / 2), clean((I6 + s.I * z) / 2)]
    for i, pj in enumerate(projectors):
        check(f"triplet_projector_{i}", equal(pj ** 2, pj) and pj.rank() == 3)
        check(f"triplet_invariant_{i}", all(equal(pj * m, m * pj) for m in cm))

    # Remove sqrt(2) from the generators before exact rank computation.
    local_comm = commutant_dimension([clean(s.sqrt(2) * m) for m in lm])
    graded_comm = commutant_dimension([clean(s.sqrt(2) * m) for m in lm] + pjs)
    check("local_commutant_two", local_comm == 2)
    check("graded_local_commutant_one", graded_comm == 1)

    rows = []
    for iq, (l, r, q) in enumerate(w.PAIR_TABLE):
        u = rep((0, 0), q)
        d = s.diag(*[chi(p, q) for p in PAR for _ in range(2)])
        e = s.diag(*[UP[p].inv() * u * UP[p] for p in PAR])
        check(f"inner_cohom_{iq}", equal(cohom(w.inner(q), u), d))
        check(f"unitary_cohom_{iq}", equal(d.H * d, I6))
        check(f"unitary_local_{iq}", equal(e.H * e, I6))
        for j, pj in enumerate(pjs):
            check(f"grading_cohom_{iq}_{j}", equal(d * pj, pj * d))
            check(f"grading_local_{iq}_{j}", equal(e * pj, pj * e))
        new_cm = []
        for j, (fnew, (_, g)) in enumerate(zip((l, r), base)):
            gg = clean(u * g * u.inv())
            cnew, lnew = cohom(fnew, gg), local(fnew, gg)
            new_cm.append(cnew)
            check(f"cohom_transport_{iq}_{j}", equal(cnew, d.inv() * cm[j] * d))
            check(f"local_transport_{iq}_{j}", equal(lnew, e * lm[j] * e.inv()))
            check(f"central_sign_cohom_{iq}_{j}", equal(cohom(fnew, -gg), -cnew))
            check(f"central_sign_local_{iq}_{j}", equal(local(fnew, -gg), -lnew))
            check(f"transported_lift_{iq}_{j}", all(equal(rep((0, 0), fnew[x]), gg * rep((0, 0), x) * gg.inv()) for x in "ab"))
        new_delta = clean(new_cm[0] * new_cm[1].inv() * new_cm[0])
        new_z = clean(new_delta ** 2)
        check(f"central_transport_{iq}", equal(new_z, d.inv() * z * d))
        for j, pj in enumerate(projectors):
            moved = clean(d.inv() * pj * d)
            check(f"triplet_transport_{iq}_{j}", moved.rank() == 3 and all(equal(moved * m, m * moved) for m in new_cm))
        lead = s.Matrix([1, 2, 3, 4, 5, 6])
        t = s.Symbol("t", nonzero=True)
        for n in (-2, -1, 0, 1, 2):
            check(f"uniform_order_{iq}_{n}", equal(d * (t ** n * lead), t ** n * (d * lead)) and d * lead != s.zeros(6, 1))
        rows.append({"q": q, "cohomology_signs": list(map(int, d.diagonal())), "cohomology_transport": True, "local_transport": True})

    for q in ("a", "b", "ab", "aB", w.C):
        d = s.diag(*[chi(p, q) for p in PAR for _ in range(2)])
        check("extra_inner_" + q, equal(cohom(w.inner(q), rep((0, 0), q)), d))
    check("central_natural_lift", equal(cohom(w.inner(w.C), -I2), I6))
    check("central_opposite_lift", equal(cohom(w.inner(w.C), I2), -I6))
    check("delta_four_lift", equal(gd ** 4, I2) and equal(cd ** 4, -I6))
    check("two_sixes_not_identified", not equal(local(w.inner(w.C), -I2), cohom(w.inner(w.C), -I2)))
    return {"status": "PASS", "exact_checks": len(facts), "pairs": rows,
            "local_commutant": local_comm, "graded_local_commutant": graded_comm,
            "triplet_ranks": [int(p.rank()) for p in projectors],
            "preserves_uniform_end_order": True, "selects_end_order": False,
            "physical_dictionary_derived": False, "full_analytic_domain_verified": False}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
