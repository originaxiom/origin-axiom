import numpy as np
exec(open('mine.py').read().split('mx=')[0])
p,q=c(),c();M=np.outer(p,q);S=c((2,2))
y=Y(S,M);A=np.array([[np.linalg.det(np.delete(np.delete(y,j,0),i,1))*(-1)**(i+j) for j in range(3)] for i in range(3)])/np.linalg.det(S)
pv=np.array([p@p,2j*p[0]*p[1],-1j*(p[0]**2-p[1]**2)]);qv=np.array([q@q,2j*q[0]*q[1],-1j*(q[0]**2-q[1]**2)])
for T in (np.outer(pv,qv),np.outer(qv,pv)):
    for k in (1,-1,1j,-1j,2,-2): 
        if np.allclose(A,k*T): print('match',k)
print(A/np.outer(pv,qv))
