import numpy as np
rng=np.random.default_rng(5)
# independent Y: Y_ab = sum_{cd} (SB_a^T eps S SB_b)_{cd} M_cd with quaternion basis (pauli-like)
sq=[np.array([[1j,0],[0,-1j]]),np.array([[0,1],[-1,0]])];sq.append(sq[0]@sq[1])
B=[sq[1],sq[0],sq[2]];eps=sq[1]
Y=lambda S,M:np.array([[np.sum((B[a].T@eps@S@B[b])*M) for b in range(3)] for a in range(3)])
E=[np.eye(4)[i].reshape(2,2).astype(complex) for i in range(4)]
def gram(M):
    L=np.array([Y(e,M).ravel() for e in E]).T; return np.linalg.eigvalsh(L.conj().T@L)
rr=lambda *s:rng.normal(size=s)+1j*rng.normal(size=s)
for _ in range(3):
    p,q=rr(2),rr(2);M=np.outer(p,q);M/=np.linalg.norm(M);print(np.round(gram(M),10))
# complex S Rayleigh, and exact census identity
mx=0;mn=9;worst=0
for _ in range(2000):
    p,q=rr(2),rr(2);M=np.outer(p,q);S=rr(2,2)
    y=Y(S,M);r=np.linalg.norm(y)**2/np.linalg.norm(S)**2/np.linalg.norm(M)**2;mx=max(mx,r);mn=min(mn,r)
    sv=np.linalg.svd(y,compute_uv=False);t=sv[1]/sv[0]
    worst=max(worst,abs(t+1/t-np.linalg.norm(y)**2/(2*abs(np.linalg.det(S))*np.linalg.norm(M)**2))/(t+1/t))
print(mn,mx,worst)
# cross-sector ratio one S, random null Ms
rm=0
for _ in range(5000):
    S=rr(2,2);v=[]
    for k in 2*[0]:
        p,q=rr(2),rr(2);M=np.outer(p,q);y=Y(S,M);sv=np.linalg.svd(y,compute_uv=False);t=sv[1]/sv[0];v.append(t+1/t)
    rm=max(rm,v[0]/v[1],v[1]/v[0])
print('max pair ratio',rm)
# non-null M range
nn=[np.linalg.norm(Y(rr(2,2),M:=rr(2,2)))**2 for _ in range(1)]
mm=[];
for _ in range(3000):
    M=rr(2,2);S=rr(2,2);mm.append(np.linalg.norm(Y(S,M))**2/np.linalg.norm(S)**2/np.linalg.norm(M)**2)
print('nonnull range',min(mm),max(mm), 'gram nonnull',np.round(gram(rr(2,2)/3),3))
# error propagation check
t,e=0.003685,0.000102;print((t+1/t),(1-1/t**2)*e)
