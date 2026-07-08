# per-class F_p dimension probe, invoked as: sage rung2_perclass.sage <name> <class_index>
import json, sys
d = json.load(open('ptolemy_systems.json'))
nm, ci = sys.argv[1], int(sys.argv[2])
sys_ = d[nm]['3'][ci]
R = PolynomialRing(GF(31991), sys_['vars'], order='degrevlex')
gens = {v: R.gen(i) for i, v in enumerate(sys_['vars'])}
I = R.ideal([R(sage_eval(e, locals=gens)) for e in sys_['eqs']])
print(f"{nm} class {ci}: dim = {I.dimension()}", flush=True)
