"""Fit: GHRS's m004 formula I_T(x mu + y lam) = sum_k q^k J(2k,k,x) J(2k-x+2y,k,-2y)
   against snappy's own edge/cusp rows.  Which linear map (x,y) -> Z^{3N} does it use?"""
import snappy, itertools
M = snappy.Manifold("m004")
G = [list(map(int,r)) for r in M.gluing_equations(form='log')]
E0,E1,mer,lon = G
print("E0",E0,"\nE1",E1,"\nmer",mer,"\nlon",lon)
# snappy base triples with gauge k2=0, k1=k (symbolic: coefficient of k)
# tet1 slots: E0 -> (2,1,0);  tet2 slots: E0 -> (1,0,2)
def rot(t,r):  # rot^1 (a,b,c) = (b,c,a)
    return tuple(t[(i+r)%3] for i in range(3))
print("\ntet1 base (coef of k):", (2,1,0), " tet2 base:", (1,0,2))
# GHRS A=(2k,k,x), B=(2k-x+2y,k,-2y). find assignments
for (A_tet,B_tet) in [(1,2),(2,1)]:
    base = {1:(2,1,0), 2:(1,0,2)}
    # find r such that rot^r(base_Atet)=(2,1,0)
    rA=[r for r in range(3) if rot(base[A_tet],r)==(2,1,0)]
    rB=[r for r in range(3) if rot(base[B_tet],r)==(2,1,0)]
    print(f"\nA=tet{A_tet} rot {rA};  B=tet{B_tet} rot {rB}")
    rA,rB=rA[0],rB[0]
    # GHRS triples' boundary parts, in GHRS order:  A: (0,0,x)  B: (-x+2y,0,-2y)
    # transport back to snappy slot order:  snappy = rot^{-r}(GHRS)
    def back(t,r): return rot(t,(-r)%3)
    dA_x = back((0,0,1),rA);  dA_y = back((0,0,0),rA)       # per unit x ; per unit 2y
    dB_x = back((-1,0,0),rB); dB_y = back((2,0,-2),rB)      # coefficient of x ; of y(=2y/2)
    # careful: B boundary = (-x+2y, 0, -2y) = x*(-1,0,0) + (2y)*(1,0,-1)
    dB_w = back((1,0,-1),rB)                                 # per unit w=2y
    v_x=[0]*6; v_w=[0]*6
    for s in range(3):
        v_x[3*(A_tet-1)+s]=dA_x[s]; v_x[3*(B_tet-1)+s]=dB_x[s]
        v_w[3*(A_tet-1)+s]=0;       v_w[3*(B_tet-1)+s]=dB_w[s]
    print("  v(mu)      =",v_x)
    print("  v(lam/2)   =",v_w, "   => v(lam) =", [2*t for t in v_w])
    print("  -mer       =",[-t for t in mer], "   v(mu)==-mer?", v_x==[-t for t in mer], " ==mer?", v_x==mer)
    vl=[2*t for t in v_w]
    print("  -lon       =",[-t for t in lon], "   v(lam)==-lon?", vl==[-t for t in lon])
    # express v(mu)+mer and v(lam)+lon in the edge row span
    for nm,vv,row in [("mu",v_x,mer),("lam",vl,lon)]:
        d=[vv[i]+row[i] for i in range(6)]   # v + row  (i.e. v-(-row))
        sol=None
        for a in range(-4,5):
            for b in range(-4,5):
                if all(a*E0[i]+b*E1[i]==d[i] for i in range(6)): sol=(a,b)
        print(f"   v({nm}) - (-row) = {d}   = a*E0+b*E1 with (a,b)={sol}")
