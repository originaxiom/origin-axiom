import json
d = json.load(open('ptolemy_systems.json'))
def build(R, sys_):
    gens = {v: R.gen(i) for i, v in enumerate(sys_['vars'])}
    return [R(sage_eval(e, locals=gens)) for e in sys_['eqs']]
print("== SL(2) exact eliminations (all classes, all three manifolds) ==", flush=True)
for nm in ['L6a4', 's776', 'm129']:
    fields = set(); zero_dim = 0
    for ci, sys_ in enumerate(d[nm]['2']):
        R = PolynomialRing(QQ, sys_['vars'], order='degrevlex')
        I = R.ideal(build(R, sys_))
        dim = I.dimension()
        if dim != 0:
            print(f"  {nm} class {ci}: dim {dim}", flush=True)
            continue
        zero_dim += 1
        last = R.gens()[-1]
        Je = I.elimination_ideal([g for g in R.gens()[:-1]])
        for g in Je.gens():
            if g == 0: continue
            S = PolynomialRing(QQ, 'x'); x = S.gen()
            gu = S(g.subs({last: x}))
            for f, m in gu.factor():
                if f.degree() == 2:
                    disc = f.discriminant()
                    fields.add(("disc %s" % QQ(disc).squarefree_part(), 2))
                elif f.degree() > 2:
                    fields.add(("deg %d" % f.degree(), f.degree()))
    print(f"  {nm}: {zero_dim} zero-dim SL(2) classes; fields: {sorted(fields)}", flush=True)
print("SL2 DONE", flush=True)
