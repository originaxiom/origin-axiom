import mpmath as m
m.mp.dps=45

def th(k,z,t):
    # z has period 1; safe exploratory points have small real tau
    return m.jtheta(k,m.pi*z,m.exp(m.pi*1j*t))
def eta(t):
    q=m.exp(2*m.pi*1j*t)
    return m.exp(m.pi*1j*t/12)*m.fprod(1-q**n for n in range(1,140))
def ch(a,b,z,t):
    return sum(m.exp(m.pi*1j*t*(n+a)**2+2*m.pi*1j*(n+a)*(z+b)) for n in range(-24,25))
def E(z,t):
    return th(1,z,t)/(2*m.pi*eta(t)**3)
def s(k,z,t):
    return th(k,z,2*t)/m.sqrt(th(1,z,t))
def correl(z,t):
    return ch(m.mpf(1)/4,0,z-t/2,2*t)/eta(2*t) * E(z,2*t)**(-m.mpf(1)/2)*E(z-t,2*t)**(-m.mpf(1)/2)*E(-t,2*t)**(m.mpf(1)/4)
for t in [1j, .13+1.2j,.21+.73j]:
 for z in [.2+.08j,.29+.13j]:
    W=s(3,z,t)*m.diff(lambda x:s(2,x,t),z)-s(2,z,t)*m.diff(lambda x:s(3,x,t),z)
    p=lambda x: th(1,x,t)
    wp=-(m.diff(p,z,2)/p(z)-(m.diff(p,z)/p(z))**2)+m.diff(p,0,3)/(3*m.diff(p,0))
    res=m.diff(lambda x:s(3,x,t),z,2)-m.mpf(3)/4*wp*s(3,z,t)
    rat=correl(z,t)/s(3,z,t)
    print('tau,z=',t,z)
    print('W/(-pi eta3)',m.nstr(W/(-m.pi*eta(t)**3),20),'lame',m.nstr(res,5))
    print('C/eta',m.nstr(rat/eta(t),24),'C4/eta4',m.nstr((rat/eta(t))**4,24))
