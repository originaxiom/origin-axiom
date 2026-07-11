import sympy as sp
phi=(1+sp.sqrt(5))/2

print("=== the golden section hidden in the split (exact) ===")
# scattering a,A = 0.618, transparent b,B = 0.382 -- are these 1/phi and 1/phi^2 exactly?
print("  1/phi   =", sp.nsimplify(1/phi), "=", float(1/phi))
print("  1/phi^2 =", sp.nsimplify(1/phi**2), "=", float(1/phi**2))
print("  => active letters {a,A} : passive letters {b,B} = 1/phi : 1/phi^2  (the golden section)")

print("\n=== the grammar as a graph, and its ONE broken symmetry ===")
allowed={('a','b'),('a','A'),('b','A'),('A','a'),('A','A'),('A','B'),('B','a')}
swap={'a':'A','A':'a','b':'B','B':'b'}
print("  allowed transitions (7 of 16):", sorted(allowed))
img={(swap[x],swap[y]) for (x,y) in allowed}
print("  under the swap a<->A, b<->B, the allowed set maps to itself EXCEPT:")
print("    allowed but image forbidden:", sorted(allowed-img))
print("    image of allowed that's forbidden:", sorted(img-allowed))
print("  => the grammar is swap-symmetric except for the single self-loop A->A")
print("     (a->a, its mirror, is forbidden). The dominant letter A is the symmetry-breaker.")

print("\n=== the passive letters are pure couriers ===")
print("  b -> A   (always, deterministic)")
print("  B -> a   (always, deterministic)")
print("  => b and B never branch: each carries flow into exactly one active letter,")
print("     b into A, B into a -- swapped images of each other. The passives are the")
print("     wiring; the actives {a,A} are where the object decides.")

print("\n=== who a and A become under the object folding on itself (phi) ===")
sub={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}
for L in 'aA':
    im=sub[L]
    print(f"  {L} -> {im}   (starts with a, ends with {im[-1]}; contains a:{im.count('a')} b:{im.count('b')} A:{im.count('A')} B:{im.count('B')})")
print("  every image starts with 'a' -> the object always re-begins from a; a is the seed it returns to.")
