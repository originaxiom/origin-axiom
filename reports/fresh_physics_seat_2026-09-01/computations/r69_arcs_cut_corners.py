"""R69 -- Euler characteristics for Fix(theta) as a charge locus (Pantev-Wijnholt: net = chi(M \\ Delta) - chi(d+)), and the filling closure."""
chi_M = 0                              # m004: Betti 1,1,0,0
def chi_remove_arcs(chi, k): return chi - k        # chi(M) = chi(M\N(A)) + chi(N(A)) - chi(annulus) = chi(M\N(A)) + 1
chi_Mprime = chi_remove_arcs(chi_M, 2)
chi_tube = 0                            # boundary of a tubular neighbourhood of an arc: an annulus
print(f"chi(m004) = {chi_M};  chi(m004 minus the two theta-arcs) = {chi_Mprime};  chi(tube around an arc) = {chi_tube}")
for signs in [("+","+"),("-","-"),("+","-")]:
    plus = [s for s in signs if s == "+"]; minus = [s for s in signs if s == "-"]
    chi_dplus = len(plus)*chi_tube        # d+ = boundary of the neighbourhood of the positive locus (PW's convention); cusp part chosen empty
    net_general = len(minus) - len(plus)   # chi(Delta-) - chi(Delta+), each arc chi = 1
    print(f"  arcs signed {signs}: chi(Delta-) - chi(Delta+) = {net_general}   [knot: 1 - 1 loops -> chi 0]")
# control: the knot as locus (n=1, l=1): chi = 0
print("  knot 4_1 as locus: chi = 1 - 1 = 0 -> net 0 (R56)")
# the filling: the solid-torus strong inversion fixes two arcs joining the four boundary points in pairs; Fix(theta) in M(p/q) is a union of closed loops
def filled_pairing(p, q):
    # 2-torsion points labelled 0=(0,0), 1=(1/2,0), 2=(0,1/2), 3=(1/2,1/2) in (u,v) with z = u + v*tau; the meridian curve of slope (p,q)
    # through 0 passes through the 2-torsion point (p mod 2, q mod 2); the solid torus joins 0 with it and the other two with each other
    a = (p % 2, q % 2); idx = {(0,0):0,(1,0):1,(0,1):2,(1,1):3}
    partner = idx[a] if a != (0,0) else None
    return partner
M_pairs = {(0, 2), (1, 3)}      # R61: the theta-arcs join 0<->tau/2 and 1/2<->1/2+tau/2
for (p, q) in [(1,0),(0,1),(1,1),(5,1),(2,1),(3,2)]:
    j = filled_pairing(p, q); others = [k for k in (1,2,3) if k != j]
    st_pairs = {tuple(sorted((0, j))), tuple(sorted(others))}
    comps = 1 if st_pairs != M_pairs else 2
    print(f"  filling slope {p}/{q}: solid-torus arcs join {sorted(st_pairs)}; with M's arcs {sorted(M_pairs)} -> Fix(theta) = {comps} closed loop(s), chi = 0")
