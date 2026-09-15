import snappy, mpmath as mp, itertools, math
mp.mp.dps = 60
def shape_field(M):
    z = M.tetrahedra_shapes('rect')[0]
    z = mp.mpc(str(z.real()), str(z.imag()))
    # minimal polynomial over Q via integer relation on 1, z, z^2, ... (real and imaginary parts jointly)
    for deg in (2,3,4):
        vec_re=[mp.re(z**k) for k in range(deg+1)]; vec_im=[mp.im(z**k) for k in range(deg+1)]
        rel = mp.pslq([mp.re(z**k) for k in range(deg+1)], maxcoeff=500, maxsteps=10**5)
        if rel and abs(sum(c*z**k for k,c in enumerate(rel)))<mp.mpf(10)**-40: return rel
    return None
def cusp_info(M):
    G = M.symmetry_group()
    out = []
    try:
        isos = G.isometries()
    except Exception as e:
        return G, str(e)
    for iso in isos:
        maps = iso.cusp_maps()
        traces = [int(round(m[0,0]+m[1,1])) for m in maps]
        dets = [int(round(m[0,0]*m[1,1]-m[0,1]*m[1,0])) for m in maps]
        out.append((traces, dets, iso.cusp_images()))
    return G, out
for name in ["m004","m202","s958","s959","m009","s961"]:
    M = snappy.Manifold(name)
    G, info = cusp_info(M)
    vol = float(M.volume())
    print(f"== {name}: vol={vol:.6f} ratio={vol/2.0298832128:.4f} cusps={M.num_cusps()} H1={M.homology()} Sym order={G.order()} amphi={G.is_amphicheiral()} shapepoly={shape_field(M)}")
    if isinstance(info, str): print("  isometries:", info); continue
    order3 = [(tr,de,img) for tr,de,img in info if all(t==-1 for t in tr)]
    print(f"  isometries={len(info)}; with cusp trace -1 on every cusp (order-3 rotation, det(A-I)=3 fixed pts/cusp): {len(order3)}; sample traces: {[i[0] for i in info][:8]}")
# Jorgensen number of m004 from its own holonomy
M = snappy.Manifold("m004"); G = M.fundamental_group()
print("m004 gens", G.generators(), "rels", G.relators())
A = G.SL2C('a'); B = G.SL2C('b')
tr = lambda X: X[0,0]+X[1,1]
comm = A*B*A.inverse()*B.inverse()
J = abs(tr(A)**2-4) + abs(tr(comm)-2)
print(f"tr a={tr(A)}, tr b={tr(B)}, tr[a,b]={tr(comm)}, J(a,b)={J}")
# one-loop SM running: alpha1 (GUT-normalised) meets alpha2 where?
a_em_inv, s2 = 127.951, 0.23122
a2i = s2*a_em_inv; a1i = 0.6*(1-s2)*a_em_inv
b1, b2 = 41/10, -19/6
L = (a1i - a2i)/((b1 - b2)/(2*math.pi))
mu = 91.1876*math.exp(L)
print(f"alpha1^-1(MZ)={a1i:.2f} alpha2^-1(MZ)={a2i:.2f}; one-loop meeting at mu={mu:.3e} GeV (sin^2 there = 3/8 by construction); alpha_s^-1 there = {8.5 - (-7)/(2*math.pi)*L:.2f} vs {a1i - b1/(2*math.pi)*L:.2f}")
