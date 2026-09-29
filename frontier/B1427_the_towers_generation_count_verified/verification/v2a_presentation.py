import warnings; warnings.filterwarnings("ignore")
import snappy, json
Y = snappy.Manifold('m004').covers(4, cover_type='cyclic')[0]
G = Y.fundamental_group()
gens = list(G.generators()); rels = list(G.relators())
pc = G.peripheral_curves()
print("H1 =", Y.homology())
print("gens =", gens)
print("rels =", rels)
print("peripheral =", pc)
mu, lam = pc[0]
print("mu =", mu, " lam =", lam)
def ab(w, gens):
    v = {g:0 for g in gens}
    for ch in w: v[ch.lower()] += 1 if ch.islower() else -1
    return [v[g] for g in gens]
print("abelianized relators:", [ab(r,gens) for r in rels])
print("ab(mu) =", ab(mu,gens), " ab(lam) =", ab(lam,gens))
json.dump(dict(gens=gens, rels=rels, mu=mu, lam=lam, H1=str(Y.homology())),
          open('<here>/Y4_presentation.json','w'), indent=1)
