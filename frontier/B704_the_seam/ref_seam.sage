from sage.all import NumberField, PolynomialRing, QQ, GF, VectorSpace, matrix
R.<x> = PolynomialRing(QQ)
# the object's stage fields: p* = signed shadow prime (quadratic subfield of Q(zeta_p))
# being p=3 -> -3 ; hearing p=5 -> 5 ; E6 p=7 -> -7 ; then p=11->-11, 13->13
stars = {3:-3, 5:5, 7:-7, 11:-11, 13:13}
print("=== THE SEAM: the observer's measurement-freedom vector space ===")
print("stage p -> p* (fiber-functor field Q(sqrt p*), B700):", stars)
# build the multiquadratic field Q(sqrt-3, sqrt5, sqrt-7) and its Galois group
gens=[-3,5,-7]
K = NumberField([x^2-d for d in gens], names=[f's{i}' for i in range(len(gens))])
print(f"\nQ(sqrt-3,sqrt5,sqrt-7): degree {K.absolute_degree()} = 2^{len(gens)} (multiquadratic)")
Kabs=K.absolute_field('a'); G=Kabs.galois_group()
print(f"Gal = {G.structure_description()}  (= (Z/2)^{len(gens)}, an F_2-vector space)")
print(f"  => the observer's freedom over 3 stages is an F_2-vector space of dim {len(gens)}.")
print()
# the 'meetings' = the F_2-sums = disc products (genus theory). 7 nonzero vectors:
print("The 7 nonzero vectors (subsets of {-3,5,-7}) = the MEETINGS (disc products):")
import itertools
def sqfree(n):
    from sage.all import squarefree_part
    return squarefree_part(n)
for r in range(1,4):
    for combo in itertools.combinations(gens,r):
        prod=1
        for d in combo: prod*=d
        D=sqfree(prod)
        label={-3:'being(3)',5:'hearing(5)',-7:'E6(7)'}
        names=' + '.join(label[d] for d in combo)
        print(f"  {names:38} -> sqrt({D})   [disc {D}]")
print()
print("So: STAGES = basis vectors ; MEETINGS = sums ; the group law = discriminant")
print("multiplication (genus theory). being(3)+hearing(5)=meeting(-15) is cell-2's V4,")
print("now one plane inside the full seam vector space.")
print()
print("=== THE BOUNDARY (B701) formalized ===")
print("The object canonically fixes the VECTOR SPACE V (the multiquadratic structure /")
print("the fields / the torsors). It does NOT fix a VECTOR (a basepoint / a value) --")
print("there is no canonical ORIGIN (B701 non-canonicity). A MEASUREMENT = a choice of")
print("origin/coordinates. The SM values are the coordinates; unreachable because V has")
print("no canonical origin. 'Where you end and I begin' = the object gives V, the observer")
print("picks the point in V.")
