"""B444 — the decisive SL(3) elimination-field control.

Run:  sage sl3_field_control.sage   (needs sl3_ptolemy.json from extract_ptolemy.py)

For each knot, build the 0-dimensional Ptolemy ideal over Q, eliminate to one
variable, factor over Q, and read off the number field of each factor. NO magma:
Sage's Groebner elimination_ideal solves each system in seconds. (SnapPy's own
.compute_solutions() would call magma — proprietary, license-only — but it is
NOT needed; the exact fields come straight out of the elimination.)

The question (Chat-2's control): reproduce fig-8's SL(3) field = Q(sqrt-7), then
compute 5_2's. Same field -> generic/laundering; different -> distinguished.
"""
import json

d = json.load(open("sl3_ptolemy.json"))


def field_label(f):
    """f irreducible over Q; return a short number-field label."""
    deg = f.degree()
    if deg == 1:
        return ("Q", 1, None)
    if deg == 2:
        disc = f.discriminant()
        sf = QQ(disc).squarefree_part()
        return ("Q(sqrt(%s))" % sf, 2, disc)
    return ("deg-%d field" % deg, deg, None)


for name in ["4_1", "5_2", "3_1"]:
    vars_ = d[name]["vars"]
    R = PolynomialRing(QQ, vars_, order="degrevlex")
    gens = {v: R.gen(i) for i, v in enumerate(vars_)}
    eqs = [R(sage_eval(s, locals=gens)) for s in d[name]["eqs"]]
    I = R.ideal(eqs)
    dim = I.dimension()
    print("=" * 64)
    print("KNOT %s   ideal dim = %s" % (name, dim), end="")
    if dim == 0:
        print("   #reps (deg) = %d" % I.vector_space_dimension())
    else:
        print("   POSITIVE-DIMENSIONAL (non-hyperbolic / torus knot: no discrete field)")
        print()
        continue
    fields_seen = set()
    for v in vars_:
        if v in ("c_0012_0", "c_0111_0"):   # normalisation coords, pinned to 1
            continue
        Je = I.elimination_ideal([gens[w] for w in vars_ if w != v])
        gg = [g for g in Je.gens() if g != 0]
        if not gg:
            continue
        S = PolynomialRing(QQ, "x")
        x = S.gen()
        gu = S(gg[0].subs({gens[v]: x}))
        if gu == 0:
            continue
        for (fp, e) in gu.factor():
            lbl, deg, disc = field_label(fp)
            if deg >= 2:
                fields_seen.add(lbl)
        # print one representative variable's factorisation
        if v == vars_[2]:
            print("   sample elimination (var %s):" % v)
            print("     ", gu.factor())
    print("   number fields appearing:", sorted(fields_seen))
    print()
