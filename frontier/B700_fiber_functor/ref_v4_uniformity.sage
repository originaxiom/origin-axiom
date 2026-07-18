from sage.all import NumberField, PolynomialRing, QQ
R.<x> = PolynomialRing(QQ)
# Q(sqrt-3, sqrt5): primitive elt sqrt-3+sqrt5, minpoly x^4 - 4x^2 + 64
K.<a> = NumberField(x^4 - 4*x^2 + 64)
print("K degree:", K.degree(), " Galois:", K.is_galois())
G = K.galois_group()
print("Gal(K/Q):", G.structure_description(), " order", G.order())
subs = K.subfields(2)
discs = []
print("quadratic subfields (disc):")
for (F,emb,_) in subs:
    d = int(F.discriminant()); discs.append(d)
    name = {5:"Q(sqrt5)=hearing",-3:"Q(sqrt-3)=being",-15:"Q(sqrt-15)=meeting"}.get(d,f"disc {d}")
    print(f"   disc={d:>4}  {name}")
ok = sorted(discs)==[-15,-3,5]
print("three subfields = {being -3, hearing 5, meeting -15}:", ok)
# the group law: the involution fixing Q(sqrt-3) TIMES the one fixing Q(sqrt5)
# = the one fixing Q(sqrt-15).  In V4 each nonidentity elt fixes exactly one
# quadratic subfield; product of any two distinct = the third.
gens=[g for g in G if g.order()==2]
print("involutions in Gal:", len(gens), "(V4 has 3)")
# verify product law: for the three involutions s_being,s_hearing,s_meeting,
# s_being * s_hearing = s_meeting (the nonidentity closing V4)
import itertools
prod_ok=True
nonid=[g for g in G if g!=G.identity()]
for u,v in itertools.combinations(nonid,2):
    w=u*v
    if w==G.identity() or w==u or w==v: prod_ok=False
print("V4 product law (being*hearing=meeting, any two distinct give the third):", prod_ok and len(nonid)==3)
print()
print("VERDICT: the three measurement-ambiguity Z/2's = the three involutions of")
print("V4 = Gal(Q(sqrt-3,sqrt5)/Q); being(sqrt-3) * hearing(sqrt5) = meeting(sqrt-15).")
