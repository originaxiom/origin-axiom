import numpy as np
from scipy.optimize import least_squares
I=1j
qi=np.array([[I,0],[0,-I]]);qj=np.array([[0,1],[-1,0]],dtype=complex);qk=qi@qj
C=[qj,qi,qk];E=qj;Ei=np.linalg.inv(E)
def Y(S,M): return np.array([[np.sum((a.T@E@S@b)*M) for b in C] for a in C])
Z=lambda S,N: Y(S,N@Ei)
def Y57(a,v): return np.outer(a,v)+np.outer(v,a)-(a@v)*np.eye(3)
rng=np.random.default_rng(3); rc=lambda *s: rng.normal(size=s)+1j*rng.normal(size=s)
def run(Wb,label):
    # Wb: list of 3 basis 2x2 matrices for hyperplane W (S and N both from W)
    ZB=np.zeros((3,3,3,3),dtype=complex)
    for i in range(3):
        for j in range(3): ZB[i,j]=Z(Wb[i],Wb[j])
    As=[rc(3) for _ in range(30)];Vs=[rc(3) for _ in range(30)]
    Yb=[Y57(a,v) for a,v in zip(As,Vs)]
    def res(x):
        z=x[:27]+1j*x[27:];L=z[:9].reshape(3,3);T1=z[9:18].reshape(3,3);T2=z[18:27].reshape(3,3)
        r=[]
        for a,v,y in zip(As,Vs,Yb):
            la,lv=L@a,L@v
            Zv=np.einsum('i,j,ijab->ab',la,lv,ZB)
            r.append((Zv-T1@y@T2).ravel())
        r=np.concatenate(r+[np.array([np.sum(abs(T1)**2)-3,np.sum(abs(T2)**2)-3])*5]);return np.concatenate([r.real,r.imag])
    best=9
    for t in range(6):
        z=len(Yb)
        s=least_squares(res,rng.normal(size=54),method='lm',max_nfev=2000)
        rel=np.linalg.norm(s.fun)/np.sqrt(sum(np.linalg.norm(y)**2 for y in Yb))
        z=s.x[:27]+1j*s.x[27:];L=z[:9].reshape(3,3);T1=z[9:18].reshape(3,3);T2=z[18:27].reshape(3,3)
        if rel<best:
            best=rel;keep=(L,T1,T2)
    L,T1,T2=keep
    print('cond L,T1,T2',np.linalg.cond(L),np.linalg.cond(T1),np.linalg.cond(T2))
    err=0
    for _ in range(20):
        a,v=rc(3),rc(3);la,lv=L@a,L@v
        Zv=np.einsum('i,j,ijab->ab',la,lv,ZB);err=max(err,np.linalg.norm(Zv-T1@Y57(a,v)@T2)/np.linalg.norm(Zv))
    print('fresh-data rel err',err)
    print(label,best,flush=True)
sl2=[np.array([[1,0],[0,-1]],dtype=complex),np.array([[0,1],[0,0]],dtype=complex),np.array([[0,0],[1,0]],dtype=complex)]
run(sl2,"traceless W")
run([qi,qj,qk],"span(i,j,k)")
run([np.eye(2,dtype=complex),qi,qj],"span(1,i,j)")
