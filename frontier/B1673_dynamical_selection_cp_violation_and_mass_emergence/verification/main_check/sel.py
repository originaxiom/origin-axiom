import numpy as np, itertools
exec(open("yuk.py").read().split("gs=[(2,3)")[0])
S0=np.array([[1.0,0.2j],[-0.2j,0.8]])
Lm=np.array([[1,1],[0,1]]);Rm=np.array([[1,0],[1,1]])
def words_arc(maxlen=5):
    out=[]
    for n in range(1,maxlen+1):
        for t in itertools.product("LR",repeat=n):
            w="".join(t)
            if "L" in w and "R" in w: out.append(w)
    return out
def act(g,p): return ((g[0,0]*p[0]+g[0,1]*p[1])%1,(g[1,0]*p[0]+g[1,1]*p[1])%1)
def sv(Y): return np.sort(np.linalg.svd(Y,compute_uv=False))[::-1]
def run(s,words,p0=(2/9,3/9),S=S0,phase=True,cache={}):
    Yu=np.zeros((3,3),complex);Yd=Yu.copy();Ye=Yu.copy()
    for w in words:
        g=np.eye(2,dtype=int)
        for c in w: g=g@(Lm if c=="L" else Rm)
        tr=abs(g[0,0]+g[1,1]);ell=2*np.arccosh(tr/2)
        psi=w.count("R")-w.count("L");ph=(1j)**(psi%4) if phase else 1
        pt=act(g,p0)
        key=(round(pt[0]*9)%9,round(pt[1]*9)%9,id(S))
        if key not in cache:
            ww=line_w(pt[0],pt[1],om)
            r=[]
            for q in (("Q","u"),("Q","d"),("L","e")):
                x,y=sector_twists(ww,om,SIXY[q[0]],SIXY[q[1]]);r.append(coupling(S,weighted_M(residues(x,y,om))))
            cache[key]=r
        r=cache[key];wt=np.exp(-s*ell)*ph
        Yu+=wt*r[0];Yd+=wt*r[1];Ye+=wt*r[2]
    return Yu,Yd,Ye
def J(Yu,Yd):
    Uu=np.linalg.svd(Yu)[0];Ud=np.linalg.svd(Yd)[0];V=Uu.conj().T@Ud
    return float(np.imag(V[0,1]*V[1,2]*np.conj(V[0,2])*np.conj(V[1,1]))),np.abs(V)
W=words_arc(5)
print("n words",len(W))
Yu,Yd,Ye=run(1.925,W)
a=sv(Yu);print("arc s=1.925 up",a,"m2/m3",a[1]/a[0],"m1/m2",a[2]/a[1],"J",J(Yu,Yd)[0])
print("down",sv(Yd),"lep",sv(Ye))
print("s scan: s, up m2/m1', m1/m2, J, down ratios, lep ratios")
for s in [0.5,1,1.5,1.925,2.5,3,3.5,4]:
    Yu,Yd,Ye=run(s,W);a=sv(Yu);b=sv(Yd);c=sv(Ye)
    print(f"s={s:5.3f} up {a[1]/a[0]:.3f} {a[2]/a[1]:.3f} | dn {b[1]/b[0]:.3f} {b[2]/b[1]:.3f} | lep {c[1]/c[0]:.3f} {c[2]/c[1]:.3f} | J {J(Yu,Yd)[0]:.4f}")
print("maxlen dependence at s=1.925")
for ml in (3,4,5,6,7):
    Yu,Yd,Ye=run(1.925,words_arc(ml));a=sv(Yu);print(ml,len(words_arc(ml)),a[1]/a[0],a[2]/a[1],J(Yu,Yd)[0])
print("no phase i^Psi, s=1.925");Yu,Yd,Ye=run(1.925,W,phase=False);a=sv(Yu);print(a[1]/a[0],a[2]/a[1],J(Yu,Yd)[0])
print("different base point");
for p0 in [(1/9,1/9),(2/9,5/9),(1/9,4/9),(4/9,2/9)]:
    Yu,Yd,Ye=run(1.925,W,p0=p0);a=sv(Yu);c=sv(Ye);print(p0,a[1]/a[0],a[2]/a[1],"lep",c[2]/c[0],J(Yu,Yd)[0])
print("Y of the CKM abs:");print(np.round(J(*run(1.925,W)[:2])[1],3))
