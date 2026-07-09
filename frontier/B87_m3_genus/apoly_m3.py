"""B87 continuation -- the m=3 metallic A-polynomial A_3(M,L) and its spectral-curve genus.

Completes the spectral genus sequence 3, 1, ? (m=1 fig-8 genus 3; m=2 silver genus 1; m=3 open,
blocked by B69's 'elimination too slow'). Trace-map framing (B67/B69) made numerical to sidestep the
slow symbolic (M,L) elimination: build the rep on Fix(T_3^2), solve for the bundle monodromy t, read
(tr t, kappa)=(M+1/M, L+1/L), fit the meridian<->longitude relation, then A_3(M,L) + genus.

Verified ingredient: metallic monodromy word map  phi_m(a)=a*(a^m b)^m,  phi_m(b)=a^m b
(m=1 -> a^2 b, ab = B67; m=2 abelianizes to trace m^2+2=6). Here phi_3(a)=a(a^3 b)^3, phi_3(b)=a^3 b.
"""
import numpy as np
import sympy as sp

# ---- trace map T_3^2 and its fixed-locus equations (to sample the character curve) ----
def pseq(m, X, Y, Z):
    p = [Y, Z]
    for _ in range(2, m + 2): p.append(sp.expand(X*p[-1] - p[-2]))
    return p
def Tm(m, v):
    X, Y, Z = v; p = pseq(m, X, Y, Z); return (p[m], X, p[m+1])
xs, ys, zs = sp.symbols("x y z")
T3 = Tm(3, Tm(3, (xs, ys, zs)))
e0 = sp.lambdify((xs, ys, zs), sp.expand(T3[0]-xs), "numpy")   # =0 on Fix
e2 = sp.lambdify((xs, ys, zs), sp.expand(T3[2]-zs), "numpy")   # =0 on Fix  (T3[1]==x identically)

def build_AB(x, y, z):
    A = np.array([[x, -1], [1, 0]], complex)
    disc = (y-x)**2 - 4*(2-z)
    u = ((y-x) + np.sqrt(disc+0j))/2
    w = x*u + 1 - z
    B = np.array([[u, 1], [w, y-u]], complex)
    return A, B
def phi3(A, B):
    A3B = np.linalg.matrix_power(A,3) @ B
    return A @ np.linalg.matrix_power(A3B,3), A3B
def solve_t(A, B, Ap, Bp):
    I2 = np.eye(2, dtype=complex)
    rows = []
    for X, Y in ((A, Ap), (B, Bp)):
        rows.append(np.kron(X.T, I2) - np.kron(I2, Y))
    E = np.vstack(rows)                                        # 8x4
    t = np.linalg.svd(E)[2][-1].conj().reshape(2, 2, order="F")
    return t/np.sqrt(np.linalg.det(t))

def samples_at(x):
    out = []
    seeds = [(x, x), (x/(x-1), x/(x-1)), (1.3, 0.7), (-x, x), (2.0, -1.0), (0.5, 1.7)]
    for sy, sz in seeds:
        yz = np.array([sy, sz], complex)
        # Newton on (e0,e2)=0 in (y,z)
        for _ in range(60):
            f = np.array([e0(x, yz[0], yz[1]), e2(x, yz[0], yz[1])], complex)
            if np.max(np.abs(f)) < 1e-13: break
            h = 1e-7
            J = np.empty((2,2), complex)
            for k in range(2):
                d = yz.copy(); d[k]+=h
                J[:,k] = (np.array([e0(x,d[0],d[1]), e2(x,d[0],d[1])],complex)-f)/h
            try: yz = yz - np.linalg.solve(J, f)
            except np.linalg.LinAlgError: break
        if np.max(np.abs([e0(x,yz[0],yz[1]), e2(x,yz[0],yz[1])])) > 1e-9: continue
        y, z = yz
        A, B = build_AB(x, y, z)
        Ap, Bp = phi3(A, B)
        t = solve_t(A, B, Ap, Bp)
        res = np.max(np.abs(t@A@np.linalg.inv(t)-Ap)) + np.max(np.abs(t@B@np.linalg.inv(t)-Bp))
        if res < 1e-8:
            comm = B@A@np.linalg.inv(B)@np.linalg.inv(A)
            out.append((np.trace(t), np.trace(comm), res))
    return out

if __name__ == "__main__":
    import json, os
    pts=[]; x=2.11
    while len(pts) < 90 and x < 30:
        x += 0.173
        for P,S,res in samples_at(x):
            if abs(P.imag)<1 or True: pts.append((P,S))
    # dedup near-duplicates
    uniq=[]
    for P,S in pts:
        if all(abs(P-Q)+abs(S-T)>1e-4 for Q,T in uniq): uniq.append((P,S))
    print(f"collected {len(uniq)} distinct (tr t, kappa) samples on the m=3 curve")
    Ps=np.array([p for p,s in uniq]); Ss=np.array([s for p,s in uniq])
    P,L,M = sp.symbols("P L M")
    found=None
    for deg in (2,4,6,8,10,12):
        if len(uniq) < deg+3: continue
        V=np.vander(Ps, deg+1, increasing=True)
        c,_,_,_=np.linalg.lstsq(V,Ss,rcond=None)
        err=np.max(np.abs(V@c-Ss))
        if err<1e-5:
            cr=[round(v.real) for v in c]
            introundok = max(abs(c[k].real-cr[k]) for k in range(len(cr)))<1e-3 and max(abs(v.imag) for v in c)<1e-3
            print(f"kappa=poly(tr t) deg {deg}: err {err:.1e}, integer={introundok}, coeffs(const->hi)={cr}")
            if introundok: found=(deg,cr); break
    if found:
        deg,cr=found
        Spoly=sum(cr[k]*P**k for k in range(len(cr)))
        print(f"\nMERIDIAN<->LONGITUDE IDENTITY (m=3):  kappa = {sp.expand(Spoly)}")
        # A_3(M,L): substitute P=(M^2+1)/M, S=kappa=(L^2+1)/L into  S - poly(P) = 0
        expr = (L**2+1)/L - Spoly.subs(P,(M**2+1)/M)
        num=sp.expand(sp.numer(sp.together(expr)))
        A3=sp.prod([f for f,e in sp.factor_list(num)[1]])
        A3=sp.expand(A3)
        print(f"A_3(M,L) (squarefree) =\n{A3}")
        degL=sp.degree(sp.Poly(A3,L),L)
        print(f"degree in L = {degL}")
        # spectral genus (B87 reader): if degree 2 in L, disc_L -> hyperelliptic genus
        if degL==2:
            a,b,cc=sp.Poly(A3,L).all_coeffs()
            disc=sp.expand(b**2-4*a*cc)
            sq=sp.prod([f for f,e in sp.factor_list(disc)[1] if e%2==1])
            dM=sp.degree(sp.Poly(sq,M),M)
            g=(dM-1)//2
            print(f"\nspectral curve w^2 = disc_L(M): branch = {sp.factor(sq)}")
            print(f"=> m=3 SPECTRAL GENUS = {g}   (sequence: m=1->3, m=2->1, m=3->{g})")
            json.dump({"m":3,"kappa_of_P":[int(v) for v in cr],"A3_degL":int(degL),
                       "spectral_genus":int(g),"branch":str(sp.factor(sq)),"n_samples":len(uniq)},
                      open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"apoly_m3.json"),"w"),indent=1)
        else:
            print(f"A_3 is degree {degL} in L (not 2) -> the spectral curve is not the simple hyperelliptic cover; report structure.")
    else:
        print("no clean integer kappa=poly(P); relation is multivalued/higher -- needs the degree-2-in-kappa handling.")
