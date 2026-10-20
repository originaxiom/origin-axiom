from lib import *
import random
random.seed(1)
names=list(GENS)
# intertwiners
print("intertwine err gens:",max(check_intertwine(GENS[n]) for n in names))
# inverse automorphism check
for a,b in [('L','Li'),('Lb','Lbi'),('R','Ri'),('Rb','Rbi')]:
    assert (GENS[a][0]@GENS[b][0]).key()==ID.key(), (a,b)
# random words: composite lift
worst_int=0;worst_coc=0;worst_ac=0
for t in range(300):
    n=random.randint(1,7)
    seq=[random.choice(names) for _ in range(n)]
    e=(ID,np.eye(2,dtype=complex)); Ds=np.eye(6,dtype=complex); As=np.eye(6,dtype=complex)
    Dprod=np.eye(6,dtype=complex)
    # right-action check: D_{e f}=D_f D_e ; build e=e1 e2 ... en
    Dlist=[];Alist=[]
    for nm in seq:
        f=GENS[nm]
        e=Emul(e,f)
        Dlist.append(Vrep(f));Alist.append(Wrep(f))
    worst_int=max(worst_int,check_intertwine(e))
    # D_e = D_en ... D_e1  (right action)
    Dp=np.eye(6,dtype=complex)
    for Dm in Dlist: Dp=Dm@Dp
    Ap=np.eye(6,dtype=complex)
    for Am in Alist: Ap=Ap@Am
    worst_coc=max(worst_coc,np.abs(Vrep(e)-Dp).max())
    worst_ac=max(worst_ac,np.abs(Wrep(e)-Ap).max())
print("composite intertwine err",worst_int)
print("cocycle D_{e1..en}=D_en..D_e1 err (V)",worst_coc)
print("A_{e f}=A_e A_f err (W)",worst_ac)
# dims
for p in P: print(p,"H1 dim",compl(p)[1] and 4-compl(p)[1])
# Delta, c, epsilon
Delta=L@Ri@L; gD=gL@np.linalg.inv(gR)@gL
D4=Delta@Delta@Delta@Delta
c=(1,-2,-1,2)
Ic=Aut(tuple(red(c+(1,)+inv(c))),tuple(red(c+(2,)+inv(c))))
print("Delta^4 == I_c:",D4.key()==Ic.key(),"  gD^2=",np.round(gD@gD,6).tolist(),"gD^4 trace",np.trace(np.linalg.matrix_power(gD,4)))
print("rho(c)=",np.round(rho(c),6).tolist())
e4=(D4,np.linalg.matrix_power(gD,4))
print("check intertwine (Delta,gD)^4:",check_intertwine(e4))
Jc=(Ic,rho(c)); print("J_c=(I_c,rho(c)): g=",np.round(Jc[1],6).tolist(),"; (Delta,gD)^4 g=",np.round(e4[1],6).tolist())
eps=(ID,-np.eye(2,dtype=complex))
print("D_eps = ",np.round(np.diag(Vrep(eps)),3),"  D_Jc diag/identity? ",np.abs(Vrep(Jc)-np.eye(6)).max(),"  D_(Delta,gD)^4 vs -I:",np.abs(Vrep(e4)+np.eye(6)).max())
# commutator of inner lifts
def J(h): return (Aut(red(h+(1,)+inv(h)),red(h+(2,)+inv(h))),rho(h))
Ja,Jb=J((1,)),J((2,))
Jbi=(Jb[0].__class__(*[red(inv((2,))+(x,)+(2,)) for x in (1,2)]),np.linalg.inv(Jb[1]))
# build J_b^-1 as J_{B}
JB=J((-2,));JA=J((-1,))
comm=Emul(Emul(Emul(Ja,JB),JA),Jb)
print("commutator Ja Jb^-1 Ja^-1 Jb: automorphism==I_c",comm[0].key()==Ic.key(),"lift g=",np.round(comm[1],6).tolist(), "-> equals J_c (g=-1)")
# nonsplitting: J inversion a->A,b->B, intertwiners
Jinv=Aut((-1,),(-2,))
print("J^2==id:",(Jinv@Jinv).key()==ID.key())
for g in (qk,-qk):
    print(" intertwiner err",max(np.abs(rho(Jinv((l,)))-g@rho((l,))@np.linalg.inv(g)).max() for l in (1,2)),"g^2=",np.round((g@g)[0,0],6))
# lift conjugation / twisted I_c^-1 vs I_c
Icinv=Aut(tuple(red(inv(c)+(1,)+c)),tuple(red(inv(c)+(2,)+c)))
print("I_c != I_c^-1 as automorphism:",Ic.key()!=Icinv.key())
# s=Delta^-1: s^4 = eps J_c^-1 : compute s as product of inverses
s=Rb@Rb  # placeholder not used
si=Lbi
S_aut=Li@R@Li ; # Delta^-1 = L^-1 R L^-1
gS=np.linalg.inv(gL)@gR@np.linalg.inv(gL)
S4=S_aut@S_aut@S_aut@S_aut
print("S=Delta^-1: S4==I_c^-1:",S4.key()==Icinv.key()," g(S^4)=",np.round(np.linalg.matrix_power(gS,4)[0,0],6),"(eps J_c^-1 has g = -(-1)=+1 ... )")
