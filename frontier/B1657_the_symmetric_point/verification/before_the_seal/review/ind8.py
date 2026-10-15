import mpmath as mp, json
mp.mp.dps=40
def thetas(tau):
    q=mp.exp(1j*mp.pi*tau); return [mp.jtheta(j,0,q) for j in (2,3,4)], mp.jtheta(1,0,q,1)*mp.pi
def cR(tau):
    (t2,t3,t4),tp=thetas(tau)
    c=[-2*mp.pi*mp.log(mp.pi/2*abs(t)**2) for t in (t2,t3,t4)]
    R=[-t2**2/tp, 1j*t3**2/tp, -t4**2/tp]
    return c,R
def Dclosed(tau):
    c,R=cR(tau); return sum(ci*Ri**2 for ci,Ri in zip(c,R)), sum(abs(x)**2 for x in R)
B=json.load(open('./frontier/B1654_the_norm_of_the_boundary_class/verification/the_norm_of_the_boundary_class.json'))
TAUS={"omega":mp.exp(2j*mp.pi/3),"i":mp.mpc(0,1),"t1":mp.mpc(.13,1.07),"t2":mp.mpc(.3,1.6),"t3":mp.mpc(0,2.2)}
for k,t in TAUS.items():
    c,R=cR(t); stored=[B['N2']['pairs']["%s,%d"%(k,r)]['A'] for r in (2,3,4)]
    D,R2=Dclosed(t); Ds=complex(*B['N5']['D_over_R2'][k])
    print(k,"c vs stored:",max(abs(float(ci)-s) for ci,s in zip(c,stored)),"  D/|R|^2 closed vs stored:",abs(complex(D/R2)-Ds))
# kappa
w=mp.exp(2j*mp.pi/3)
for phi in (0.3,1.1,2.0):
    for d in (mp.mpf('1e-6'),):
        t=w+d*mp.exp(1j*phi); D,R2=Dclosed(t); k=D/R2/d
        print("phi",phi,"|D|/(|R|^2 d) =",mp.nstr(abs(k),12)," arg(D e^{i phi})/pi =",mp.nstr(mp.arg(D/R2*mp.exp(1j*phi))/mp.pi,12))
(t2,t3,t4),tp=thetas(w)
W87=mp.pi**2*mp.sqrt(3)/6*abs(t3)**4
print("W87 slope",W87)
# exact kappa from closed form: D = -th3^4 h/(4 pi eta^6); compute via derivative numerically (complex step not valid -> use directional)
def Dfun(t): D,R2=Dclosed(t); return D/R2
d=mp.mpf('1e-12'); k=Dfun(w+d)/d; k2=Dfun(w+d*1j)/(d*1j)
print("D/|R|^2 / conj(delta) approx:", mp.nstr(Dfun(w+d*mp.exp(0.7j))/(d*mp.exp(-0.7j)),15), "abs",mp.nstr(abs(Dfun(w+d*mp.exp(0.7j))/(d*mp.exp(-0.7j))),15))
print("arg kappa/pi:", mp.nstr(mp.arg(Dfun(w+d*mp.exp(0.7j))/(d*mp.exp(-0.7j)))/mp.pi,15))
