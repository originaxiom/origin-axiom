"""R56 -- THE ENDPOINT THEOREM, object side.
Pantev-Wijnholt (arXiv:0905.1968) eqs (3.39)-(3.40), (3.63): for an abelian Higgs field on Q with
singular charge loci Delta+ (positive) and Delta- (negative), M = Q \ (Delta+ u Delta-),
   N_chi(R) = h^1(M, d+M),  N_chibar(R) = h^2(M, d+M),  net(R) = chi(M, d+M) = chi(M) - chi(d+M)
and for Q = S^3 with charge graphs:  net = n- - l- - n+ + l+  = chi(Delta-) - chi(Delta+).
Braun-Cizel-Huebner-Schaefer-Nameki (arXiv:1812.06072) (2.50),(7.13)-(7.14): on a closed odd-dimensional
Q the chiral index is the Euler characteristic and vanishes; chi(M3) = chi(Sigma+) = chi(Sigma-) = 0.
"""
import itertools
from fractions import Fraction as Fr

def chi_graph(n_components, n_loops): return n_components - n_loops

print("[1] The object as Pantev-Wijnholt's charge locus: Q = S^3, Delta = the figure-eight knot")
for name, (n, l) in {"figure-eight knot 4_1": (1, 1), "any knot": (1, 1), "any c-component link": (3, 3),
                     "the Hopf link": (2, 2), "an unknotted arc (one endpoint pair)": (1, 0),
                     "three disjoint arcs": (3, 0), "a point charge": (1, 0)}.items():
    print(f"    chi({name:36s}) = n - l = {n} - {l} = {chi_graph(n, l):+d}")
print("    net chiral = chi(Delta-) - chi(Delta+): with the knot as the only charge locus, either sign: 0 - 0 = 0")
# PW (3.61): the individual counts with the knot negative and nothing positive (n+ = l+ = 0, r = 0)
n_m, l_m, n_p, l_p, r = 1, 1, 0, 0, 0
b2 = n_m - 1 + l_p - r; b1 = n_p - 1 + l_m - r
print(f"    PW (3.61) knot negative, nothing positive: h1(M,d+M) = {b1}, h2(M,d+M) = {b2}  -> no localized matter at all")
n_m, l_m, n_p, l_p = 0, 0, 1, 1
b2 = n_m - 1 + l_p - r; b1 = n_p - 1 + l_m - r
print(f"    PW (3.61) knot positive, nothing negative: h1(M,d+M) = {b1}, h2(M,d+M) = {b2}")

print("\n[2] chi of the object itself and of its cusp (the relative formula net = chi(M) - chi(d+M))")
# S^3 \ 4_1: b0=1, b1=1 (H1 = Z), b2=0, b3=0 (one torus end)
betti = [1, 1, 0, 0]
chiM = sum((-1)**i * b for i, b in enumerate(betti))
print(f"    Betti(m004) = {betti} -> chi(m004) = {chiM}")
print("    net = -chi(d+M) with d+M a subsurface of the cusp torus T^2:")
for k in range(0, 4):
    print(f"      d+ = {k} disk(s): net = {-k:+d};   d+ = T^2 minus {k} disk(s): net = {+k:+d};   d+ = annuli: 0")
print("    => three generations <=> exactly three disks of one sign on the cusp torus (three POINTS on the object's cusp)")

print("\n[3] The object's own graphs (its ideal triangulation), as candidate charge loci")
# m004: 2 ideal tetrahedra, 2 edges, 4 faces, 1 cusp.  Edge graph: 2 arcs from the cusp to itself = knot u 2 arcs
V, E, F, T = 0, 2, 4, 2   # ideal vertices don't count; the knot is the vertex link
print(f"    ideal triangulation: {T} tetrahedra, {E} edges, {F} faces; chi(m004) = -V + E - F + T = {-V + E - F + T}")
print(f"    edge graph  (knot + 2 arcs attached at the cusp): n = 1, l = 1 + 2 = 3  -> chi = {chi_graph(1, 3):+d}")
print(f"    dual spine  (2 vertices = tetrahedra, 4 edges = faces): chi = V - E = {2 - 4:+d}")
print("    => the object's intrinsic graphs give |net| in {0, 2}; NO intrinsic graph with chi = 3 is present")

print("\n[4] The whole metallic family: every member is a once-punctured-torus bundle / knot-or-link complement")
print("    closed 1-manifold charge loci have chi = 0 for every member; closed Q have chi = 0 (odd dimension):")
print("    net chiral = 0 across the family in the Higgs-bundle frame -- the family is chirality-blind by Euler characteristic")

print("\n[5] Which sl2 (I-25): B1112's projectivity filter on B1256's four three-chiral labellings")
def idx(dims): return Fr(sum(n*(n*n-1) for n in dims), 6) / 6
rows = {"principal (2,2,2,2,2,2)": [17,9,1], "subregular (2,2,2,0,2,2)": [13,9,5],
        "(1,0,1,1,1,1)": [8,7,5,4,3], "(1,1,1,0,1,1)": [7,6,5,4,3,2], "(1,0,1,0,1,1)": [6,5,4,4,3,3,2]}
surv = []
for k, d in rows.items():
    proj = all(n % 2 == 1 for n in d)
    print(f"    {k:26s} 27 = {'+'.join(map(str, d)):18s} index = {str(idx(d)):>3}  projective = {proj}")
    if proj: surv.append(k)
print(f"    survivors of the object's own PSL(2) geometry: {surv}")
print("    I-19 (EARNED, B1242): E6 CS contains 3d gravity at index 156 = PRINCIPAL.  B1257's selector: SUBREGULAR (84).")
print("    => the record carries both; they are different sl2's; I-19's earning fixes I-25 = principal unless I-19 is redone at 84")
print("\nALL STATEMENTS ABOVE ARE ARITHMETIC ON CITED FORMULAS; nothing here is a new physical claim.")
