import numpy as np, itertools, random
s2=np.sqrt(2)
I2=np.eye(2,dtype=complex)
qi=np.array([[1j,0],[0,-1j]]);qj=np.array([[0,1],[-1,0]],dtype=complex);qk=qi@qj
# free group words: tuples of nonzero ints, 1=a,2=b, negative=inverse
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return tuple(out)
def inv(w): return tuple(-x for x in reversed(w))
class Aut:
    def __init__(s,ia,ib): s.im={1:red(ia),2:red(ib)}
    def __call__(s,w):
        out=[]
        for x in w:
            out+= list(s.im[x]) if x>0 else list(inv(s.im[-x]))
        return red(out)
    def __matmul__(s,o): # s after o
        return Aut(s(o.im[1]),s(o.im[2]))
    def key(s): return (s.im[1],s.im[2])
    def inverse(s):
        # search inverse among generated words: use Nielsen via brute not needed; provided externally
        raise NotImplementedError
ID=Aut((1,),(2,))
L=Aut((1,),(1,2)); Lb=Aut((1,),(2,1)); R=Aut((1,2),(2,)); Rb=Aut((2,1),(2,))
Li=Aut((1,),(-1,2)); Lbi=Aut((1,),(2,-1)); Ri=Aut((1,-2),(2,)); Rbi=Aut((-2,1),(2,))
def sq(a,b):return (a+b*1j)/s2
gL=(np.eye(2)+qi)/s2; gLb=(np.eye(2)-qi)/s2; gR=(np.eye(2)-qj)/s2; gRb=(np.eye(2)+qj)/s2
def rho(w):
    M=np.eye(2,dtype=complex)
    for x in w:
        g={1:qi,2:qj}[abs(x)]
        M=M@(g if x>0 else np.linalg.inv(g))
    return M
GENS={'L':(L,gL),'Lb':(Lb,gLb),'R':(R,gR),'Rb':(Rb,gRb),
 'Li':(Li,np.linalg.inv(gL)),'Lbi':(Lbi,np.linalg.inv(gLb)),'Ri':(Ri,np.linalg.inv(gR)),'Rbi':(Rbi,np.linalg.inv(gRb))}
def Emul(e,f): return (e[0]@f[0], e[1]@f[1])
def Einv_gen(name):
    return GENS[name]
def check_intertwine(e):
    phi,g=e
    return max(np.abs(rho(phi(w))-g@rho(w)@np.linalg.inv(g)).max() for w in [(1,),(2,)])
# parity
def ab(w):
    return np.array([sum(1 for x in w if abs(x)==1 and True)%2*0,0])
def expsum(w,l): return sum((1 if x>0 else -1) for x in w if abs(x)==l)
def chi(p,w): return (-1)**((p[0]*expsum(w,1)+p[1]*expsum(w,2))%2)
def Mrep(p,x):
    return chi(p,(x,))*rho((x,))
def Mw(p,w):
    M=np.eye(2,dtype=complex)
    for x in w: M=M@(Mrep(p,abs(x)) if x>0 else np.linalg.inv(Mrep(p,abs(x))))
    return M
def zw(p,za,zb,w):
    # cocycle value z(w) with z(xy)=z(x)+M(x)z(y)
    v=np.zeros(2,dtype=complex); M=np.eye(2,dtype=complex)
    for x in w:
        if x>0:
            zx=za if x==1 else zb; Mx=Mrep(p,x)
            v=v+M@zx; M=M@Mx
        else:
            Mx=Mrep(p,-x); zx=-np.linalg.inv(Mx)@(za if x==-1 else zb)
            v=v+M@zx; M=M@np.linalg.inv(Mx)
    return v
P=[(1,0),(0,1),(1,1)]
def coboundary(p):
    # columns: v in C^2 -> ((M(a)-1)v,(M(b)-1)v)
    return np.vstack([Mrep(p,1)-np.eye(2),Mrep(p,2)-np.eye(2)])
def compl(p):
    B=coboundary(p); u,s,vh=np.linalg.svd(B); r=(s>1e-9).sum()
    return u[:,r:],r  # orthonormal basis of orthocomplement of range
def Dmat_cochain(p,e):
    """matrix of z -> D_e z on C^4 (z(a),z(b)); lands in M_{p phi}"""
    phi,g=e; gi=np.linalg.inv(g)
    cols=[]
    for k in range(4):
        z=np.zeros(4,dtype=complex);z[k]=1
        za,zb=z[:2],z[2:]
        out=np.concatenate([gi@zw(p,za,zb,phi((1,))),gi@zw(p,za,zb,phi((2,)))])
        cols.append(out)
    return np.array(cols).T
def pphi(p,phi):
    # chi_{p phi}(x)=chi_p(phi(x)): p' = (chi_p(phi(a))->bit, chi_p(phi(b)))
    return tuple(int(chi(p,phi((l,)))==-1) for l in (1,2))
def Vrep(e):
    """6x6 matrix of D_e on V=sum_p H^1(M_p) in orthocomplement bases."""
    Q={p:compl(p)[0] for p in P}
    D=np.zeros((6,6),dtype=complex)
    for ip,p in enumerate(P):
        q=pphi(p,e[0]); iq=P.index(q)
        Dm=Dmat_cochain(p,e)
        # check preserves coboundaries
        D[2*iq:2*iq+2,2*ip:2*ip+2]=Q[q].conj().T@Dm@Q[p]
    return D
def Wrep(e):
    """A_e: e_p (x) v -> e_{p phi^{-1}} (x) g v ; need phi^-1 parity: p' with p'phi=p"""
    phi,g=e
    A=np.zeros((6,6),dtype=complex)
    for ip,p in enumerate(P):
        for iq,q in enumerate(P):
            if pphi(q,phi)==p:  # q phi = p  => q = p phi^-1
                A[2*iq:2*iq+2,2*ip:2*ip+2]=g
    return A
