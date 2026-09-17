import snappy, warnings, math, cmath; warnings.filterwarnings("ignore")
from snappy import Manifold
import mpmath as mp
from collections import Counter
mp.mp.dps=60

print("="*70); print("Vol(m004) = 9*sqrt(3)*zeta_K(2)/pi^2 for K=Q(sqrt-3)"); print("="*70)
# zeta_K(s) = zeta(s) * L(s, chi_{-3})


# use Dirichlet L with character mod 3: chi(1)=1, chi(2)=-1
L2 = mp.nsum(lambda n: (mp.mpf(1)/mp.mpf(n)**2 if int(n)%3==1 else (-mp.mpf(1)/mp.mpf(n)**2 if int(n)%3==2 else mp.mpf(0))), [1, mp.inf])
zk2 = mp.zeta(2)*L2
pred = 9*mp.sqrt(3)*zk2/mp.pi**2
print("  zeta_K(2)      =", mp.nstr(zk2,35))
print("  9*sqrt3*zK(2)/pi^2 =", mp.nstr(pred,35))
M=Manifold('m004'); M.set_peripheral_curves('fillings') if False else None
Mh=M.high_precision()
print("  Vol(m004) [SnapPy 1000-bit] =", mp.nstr(mp.mpf(str(Mh.volume())),35))
print("  agree to 30 dp:", mp.nstr(abs(pred-mp.mpf(str(Mh.volume()))),5))

print(); print("="*70); print("Covolume / index 12 in PSL(2,O_K)"); print("="*70)
# covolume of PSL(2,O_{-3}) = |d|^{3/2} zeta_K(2) / (4 pi^2)
cov = mp.mpf(3)**mp.mpf(1.5)*zk2/(4*mp.pi**2)
print("  covol PSL(2,O_-3) =", mp.nstr(cov,20), " (paper quotes 0.16916)")
print("  ratio Vol(m004)/covol =", mp.nstr(pred/cov,20), " (paper: index 12)")

print(); print("="*70); print("HEXAGONAL CUSPS among the 87 covers"); print("="*70)
def reduce_tau(t):
    t=complex(t)
    if t.imag<0: t=t.conjugate()
    for _ in range(200):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t)<1-1e-12: t = -1/t
        else: break
    return t
hexc=0; hexm=0; tot=0
rep=cmath.exp(1j*math.pi/3)
M=Manifold('m004'); allc=[]
for d in range(2,11):
    for c in M.covers(d): allc.append(Manifold(c))
for c in allc:
    shapes=[reduce_tau(s) for s in c.cusp_info('shape')]
    tot+=len(shapes)
    n=sum(1 for s in shapes if abs(s-rep)<1e-6 or abs(s-rep.conjugate())<1e-6 or abs(s-(rep-1))<1e-6)
    hexc+=n
    if n>0: hexm+=1
print("  covers with >=1 hexagonal cusp:",hexm," hexagonal cusps:",hexc," total cusps:",tot)
print("  paper: fourteen covers, 16 of the 201 cusps")

print(); print("="*70); print("one-cusped census manifolds with H1 = Z, <= 7 tetrahedra"); print("="*70)
cnt=0; names=[]
for M in snappy.OrientableCuspedCensus(cusps=1):
    if M.num_tetrahedra()>7: break
    if str(M.homology())=='Z': cnt+=1; names.append(M.name())
print("  count:",cnt," (paper: 2804)")

print(); print("="*70); print("KOIDE angle vs 2/9"); print("="*70)
# PDG charged lepton masses (MeV)
me,mmu,mtau = mp.mpf('0.51099895000'), mp.mpf('105.6583755'), mp.mpf('1776.86')
dme,dmmu,dmtau = mp.mpf('0.00000000015'), mp.mpf('0.0000023'), mp.mpf('0.12')
def theta(me,mmu,mtau):
    v=[mp.sqrt(me),mp.sqrt(mmu),mp.sqrt(mtau)]
    s=sum(v); n=mp.sqrt(sum(x*x for x in v))
    # Koide parametrisation: cos(theta) direction vs (1,1,1)/sqrt3 ... use the standard "Koide angle"
    return s/(mp.sqrt(3)*n)   # = cos(phi); Koide's relation <=> this = sqrt(3/2)/sqrt(3)... 
c=theta(me,mmu,mtau)
print("  (sum sqrt m)/(sqrt3 * |v|) =", mp.nstr(c,12), "  Koide Q =", mp.nstr((me+mmu+mtau)/(mp.sqrt(me)+mp.sqrt(mmu)+mp.sqrt(mtau))**2,12), " (Koide: 2/3)")
print("  2/9 =", mp.nstr(mp.mpf(2)/9,12))
