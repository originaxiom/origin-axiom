import numpy as np, math
EPS=np.array([[0,1],[-1,0]],complex);EI=np.linalg.inv(EPS)
QI=np.array([[1j,0],[0,-1j]]);QJ=EPS;QK=QI@QJ;BL=[QJ,QI,QK]
def Y(S,M): return np.array([[np.sum((a.T@EPS@S@b)*M) for b in BL] for a in BL])
worst=0;wj5=[1e9,1e9,1e9];wc=1e9;mins=[1e9,1e9]
for seed in range(300):
  rng=np.random.default_rng(seed)
  r=lambda:rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
  X=[r() for _ in range(40)]
  nul=[np.outer(rng.normal(size=2)+1j*rng.normal(size=2),rng.normal(size=2)+1j*rng.normal(size=2)) for _ in range(40)]
  for i in range(10):
    S0,M0=nul[i],nul[(i+7)%40];Xs,Zs=X[i],X[(i+3)%40];v=[]
    for e in(1e-3,1e-4):
      sv=np.linalg.svd(Y(S0+e*Xs,M0+e*Zs),compute_uv=False);v.append((sv[1]/sv[0],sv[2]/sv[0]))
    for a in(math.log10(v[0][0]/v[1][0]),math.log10(v[0][1]/v[1][1])): worst=max(worst,abs(a-1))
  def geo(S,N):
    sv=np.linalg.svd(Y(S,N@EI),compute_uv=False);return abs(sv[0]*sv[2]/sv[1]**2-1)
  wc=min(wc,np.median([geo(X[i],X[(i+11)%40]) for i in range(40)]))
  mins[0]=min(mins[0],min(abs(np.linalg.det(Z))/np.linalg.norm(Z)**2 for Z in X))
  sv=lambda S,M:(lambda s:s[2]/s[0])(np.linalg.svd(Y(S,M),compute_uv=False))
  mins[1]=min(mins[1],min(sv(X[i],X[(i+1)%40]) for i in range(40)))
  W=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));W=W+W.T
  b=[]
  for i in range(20):
    S,M=X[i],X[(i+5)%40];Yy=Y(S,M)+0.1*np.linalg.norm(Y(S,M))*W/np.linalg.norm(W)
    b.append(abs(np.linalg.det(Yy)-4*np.linalg.det(S)*np.linalg.det(M)*np.trace(EPS@S@M.T))/np.linalg.norm(Yy)**3)
  wj5[0]=min(wj5[0],min(b))
print("worst slope dev",worst,"min median geo dep",wc,"floors",mins,"J5a min",wj5[0])
