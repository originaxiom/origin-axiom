import mpmath as m
m.mp.dps=40

def w(z,tau,d=0):
    return m.matrix([sum((2*m.pi*1j*(n+a))**d*m.exp(2*m.pi*1j*tau*(n+a)**2+2*m.pi*1j*(n+a)*z) for n in range(-25,26)) for a in (m.mpf(0),m.mpf('.5'))])

def bloch(z,tau):
    u,v=w(z,tau); N=abs(u)**2+abs(v)**2
    return m.matrix([2*m.re(m.conj(u)*v)/N,2*m.im(m.conj(u)*v)/N,(abs(u)**2-abs(v)**2)/N])

tau=m.mpc('.23','1.1'); z=m.mpc('.31','.17')
H=m.matrix([[1,1],[1,-1]])/m.sqrt(2)
print('S w error', m.norm(w(z/tau,-1/tau)-m.sqrt(-1j*tau)*m.exp(m.pi*1j*z*z/(2*tau))*H*w(z,tau)))
print('period err',m.norm(w(z+tau,tau)-m.exp(-m.pi*1j*tau/2-m.pi*1j*z)*m.matrix([[0,1],[1,0]])*w(z,tau)))
n=bloch(z,tau)
nx=m.diff(lambda x:bloch(z+x,tau),m.mpf(0)); ny=m.diff(lambda x:bloch(z+1j*x,tau),m.mpf(0))
def cross(a,b): return m.matrix([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]])
print('BPS',m.norm(nx+cross(n,ny)))
nxx=m.diff(lambda x:bloch(z+x,tau),m.mpf(0),2); nyy=m.diff(lambda x:bloch(z+1j*x,tau),m.mpf(0),2)
print('EOM',m.norm(nxx+nyy+(m.norm(nx)**2+m.norm(ny)**2)*n))
u,v=w(z,tau);du,dv=w(z,tau,1); den=abs(u)**2+abs(v)**2
print('density',m.fdot(n,cross(nx,ny))/(4*m.pi),abs(u*dv-v*du)**2/(m.pi*den**2))
