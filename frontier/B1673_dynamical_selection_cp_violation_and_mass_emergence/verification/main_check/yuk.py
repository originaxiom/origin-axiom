import numpy as np, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[4]
src=(ROOT/"frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py").read_text()
NS={"__file__":"h","__name__":"h"}
exec(compile(src.split("T0 = time.time()")[0],"h","exec"),NS)
line_w,sector_twists,residues,weighted_M,coupling,SIXY,om=NS["line_w"],NS["sector_twists"],NS["residues"],NS["weighted_M"],NS["coupling"],NS["SIXY"],NS["OM"]
# NOTE B1656 OM = exp(2 pi i/3) = -1/2 + i sqrt3/2  same as arc omega
gs=[(2,3),(2,4),(3,2),(3,4),(4,2),(4,3),(5,6),(5,7),(6,5),(6,7),(7,5),(7,6)]
L18=[(b+i,b+j) for b in (1,2) for i in (0,3,6) for j in (0,3,6)]
def Y(pt,S,sec):
    w=line_w(pt[0]/9,pt[1]/9,om)
    q={"u":("Q","u"),"d":("Q","d"),"e":("L","e")}[sec]
    x,y=sector_twists(w,om,SIXY[q[0]],SIXY[q[1]])
    return coupling(S,weighted_M(residues(x,y,om)))
def J(Yu,Yd):
    Uu=np.linalg.svd(Yu)[0];Ud=np.linalg.svd(Yd)[0];V=Uu.conj().T@Ud
    return float(np.imag(V[0,1]*V[1,2]*np.conj(V[0,2])*np.conj(V[1,1]))),V
def sv(Y): return np.sort(np.linalg.svd(Y,compute_uv=False))[::-1]
S0=np.array([[1.0,0.2j],[-0.2j,0.8]])
Sre=np.array([[1.0,0.2],[0.2,0.8]])
rng=np.random.default_rng(1)
def avg(pts,S,sec): return sum(Y(p,S,sec) for p in pts)/len(pts)
for name,S in [("S_arc(complex)",S0),("S real",Sre),("S real diag",np.diag([1.,.8]).astype(complex))]:
    Yu=avg(gs,S,"u");Yd=avg(gs,S,"d");Ye=avg(gs,S,"e")
    j,V=J(Yu,Yd)
    print(name,"GS-avg J=",j,"sv u",sv(Yu),"d",sv(Yd),"e",sv(Ye))
    Yu=avg(L18,S,"u");Yd=avg(L18,S,"d");Ye=avg(L18,S,"e")
    print(name,"W59-18 avg J=",J(Yu,Yd)[0],"sv u",sv(Yu),"e",sv(Ye))
# single points
for p in gs[:3]+L18[:3]:
    print("single",p,"J(S_arc)=",J(Y(p,S0,"u"),Y(p,S0,"d"))[0],"sv_u",sv(Y(p,S0,"u")),"sv_e",sv(Y(p,S0,"e")))
# S dependence of GS-avg J & ratios
for k in range(5):
    A=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));S=A+A.conj().T
    Yu=avg(gs,S,"u");Yd=avg(gs,S,"d");Ye=avg(gs,S,"e");j,_=J(Yu,Yd)
    print("rand S",k,"J",j,"u ratios",sv(Yu)[1:]/sv(Yu)[:2] if False else (sv(Yu)[2]/sv(Yu)[0]),(sv(Yu)[1]/sv(Yu)[0]),"e m1/m3",sv(Ye)[2]/sv(Ye)[0])
# Is orbit-avg of one mu6 orbit (6 pts) already rank 3? and avg over any two arbitrary lines
Yu=avg(gs[:2],S0,"u");print("2 pts GS sv u",sv(Yu))
Yu=avg(L18,S0,"e");print("W59 avg lep sv",sv(Yu))
Yu=avg([(1,1),(2,5)],S0,"e");print("2 W59 pts lep",sv(Yu))
