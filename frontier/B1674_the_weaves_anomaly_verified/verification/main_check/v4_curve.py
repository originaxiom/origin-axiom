import mpmath as mp
mp.mp.dps=20
def eta(t): return mp.exp(2j*mp.pi*t/24)*mp.qp(mp.exp(2j*mp.pi*t))
def E6(t):
    q=mp.exp(2j*mp.pi*t); return 1-504*mp.nsum(lambda n: n**5*q**n/(1-q**n),[1,mp.inf])
P=lambda x,y: 12*mp.arg(eta(mp.mpc(x,y)))+2*mp.arg(E6(mp.mpc(x,y)))
for y in [1.0,1.2,1.22,1.24,1.26,1.28,1.3]:
    xs=[mp.mpf(k)/1000 for k in range(1,60)]
    z=[]
    for a,b in zip(xs,xs[1:]):
        if mp.sin(P(a,y))*mp.sin(P(b,y))<0: z.append(mp.findroot(lambda x: mp.sin(P(x,y)),(a,b),solver='anderson'))
    print(y,[mp.nstr(r,6) for r in z], " sin at x=0.001:",mp.nstr(mp.sin(P(0.001,y)),4))
