import mpmath as mp
mp.mp.dps=30
def th(k,z,tau):
    q=mp.exp(1j*mp.pi*tau)  # nome
    return mp.jtheta(k,mp.pi*z,q)
for tau in [1j*0.9, 0.3+1.1j, -0.5+mp.sqrt(3)/2*1j, 0.17+0.6j]:
    # numerator vector N(z)=(i th2(z|2tau), th3(z|2tau))
    N=lambda z:mp.matrix([1j*th(2,z,2*tau),th(3,z,2*tau)])
    v=N(0); d=mp.diff(lambda z:th(1,z,tau),0)
    b=v/mp.sqrt(d)
    # (1) F = z^-1/2 b + O(z^3/2): check F z^{1/2} - b ~ z^2
    errs=[]
    for z in [mp.mpf('0.02'),mp.mpf('0.01')]:
        F=N(z)/mp.sqrt(th(1,z,tau))
        errs.append(mp.norm(F*mp.sqrt(z)-b))
    ratio=errs[0]/errs[1]  # expect 4 for O(z^2)
    # (2) F(z+tau) constant-matrix relation: N(z+tau) = c(z)*T*N(z), T=[[0,i],[-i,0]]
    T=mp.matrix([[0,1j],[-1j,0]])
    z0=mp.mpc('0.23','0.11')
    A=N(z0+tau); B=T*N(z0)
    c1=A[0]/B[0]; c2=A[1]/B[1]
    z1=mp.mpc('-0.31','0.07'); A=N(z1+tau); B=T*N(z1)
    print("tau",mp.nstr(tau,5),"|b|",mp.nstr(mp.norm(b),6),"O(z^2) ratio",mp.nstr(ratio,6),
          " c1/c2 at z0",mp.nstr(c1/c2,8)," at z1",mp.nstr(A[0]/B[0]/(A[1]/B[1]),8))
    # N(z+1)
    A=N(z0+1);print("   N(z+1) = diag(-1,1)N? err",mp.nstr(mp.norm(A-mp.matrix([[-1,0],[0,1]])*N(z0)),5))
