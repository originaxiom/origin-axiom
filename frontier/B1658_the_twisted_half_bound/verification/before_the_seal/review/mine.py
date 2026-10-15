import numpy as np
rng=np.random.default_rng(7)
QI=np.array([[1j,0],[0,-1j]]);QJ=np.array([[0,1],[-1,0]],complex);QK=QI@QJ;E=QJ;B=[QJ,QI,QK]
def Y(S,M): return np.array([[np.sum((a.T@E@S@b)*M) for b in B] for a in B])
c=lambda n=2:rng.normal(size=n)+1j*rng.normal(size=n)
def adj(Y): return np.linalg.inv(Y).T*np.linalg.det(Y)
mx=[0,0,0,0]
for _ in range(2000):
    p,q,u,v=c(),c(),c(),c();M=np.outer(p,q);S=c((2,2));y=Y(S,M)
    sv=np.linalg.svd(y,compute_uv=False)
    A=np.array([[np.linalg.det(np.delete(np.delete(y,j,0),i,1))*(-1)**(i+j) for j in range(3)] for i in range(3)])
    mx[0]=max(mx[0],abs(np.linalg.norm(A)/(abs(np.linalg.det(S))*np.linalg.norm(M)**2)-2))
    S1=np.outer(u,v);y1=Y(S1,M);n2=np.linalg.norm(y1)**2
    f=(abs(u@u.conj())*abs(p@p.conj())+abs(np.vdot(u,p))**2)*(2*abs(v@v.conj())*abs(q@q.conj())-abs(v@q)**2)
    mx[1]=max(mx[1],abs(n2/f-1))
    mx[2]=max(mx[2],abs(sv[0]*sv[1]/(2*abs(np.linalg.det(S))*np.linalg.norm(M)**2)-1),sv[2]/sv[0])
    # general S: ratio ||Y||^2/(||S||^2||M||^2) range
    r=np.linalg.norm(y)**2/(np.linalg.norm(S)**2*np.linalg.norm(M)**2)
    mx[3]=max(mx[3],r)
print(mx)
# general (non-null) S range of ||Y||^2/(|S|^2|M|^2) and exact t+1/t cross-sector bound
rs=[];ex=[]
for _ in range(20000):
    S=c((2,2));p,q,p2,q2=c(),c(),c(),c();M=np.outer(p,q);M2=np.outer(p2,q2)
    f=lambda M:np.linalg.norm(Y(S,M))**2/(2*abs(np.linalg.det(S))*np.linalg.norm(M)**2)
    ex.append(f(M)/f(M2)); rs.append(np.linalg.norm(Y(S,M))**2/(np.linalg.norm(S)**2*np.linalg.norm(M)**2))
print(min(rs),max(rs),min(ex),max(ex))
# real quaternion S: det=|S|^2 -> d_S=1/ ... 
Sr=sum(x*U for x,U in zip(rng.normal(size=4),[np.eye(2),QI,QJ,QK]));print(abs(np.linalg.det(Sr))/np.linalg.norm(Sr)**2)
