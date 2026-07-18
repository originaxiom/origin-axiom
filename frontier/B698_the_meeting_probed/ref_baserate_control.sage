from sage.all import EllipticCurve
import mpmath as mp
mp.mp.dps=30
Lbeing = float((mp.zeta(2,mp.mpf(1)/3)-mp.zeta(2,mp.mpf(2)/3))/9)  # L(chi_-3,2)=0.7813024
print("being value L(chi_-3,2) =", Lbeing)
print()
# rank-0 squarefree-conductor N=p*q curves (control), plus 15a8
labels=['15a8','21a1','26a1','33a1','35a1','38a1','39a1','55a1','57a1','65a1','77a1','85a1','91a1','95a1']
print(f"{'curve':7} {'N':4} {'L(E,2)':12} {'L(E,2)/being':14} {'L(E,1)/Om':10}")
for lbl in labels:
    try:
        E=EllipticCurve(lbl)
        if E.rank()!=0: continue
        L=E.lseries()
        L2=float(L(2).n(30)); L1=float(L(1).n(30)); Om=float(E.period_lattice().omega().n(30))
        N=int(E.conductor())
        print(f"{lbl:7} {N:4} {L2:.8f}  {L2/Lbeing:.8f}     {L1/Om:.6f}")
    except Exception as e:
        print(lbl,"err",e)
print()
print("QUESTION: is 15a8's L(E,2)/being any 'nicer' (rational/algebraic) than the controls?")
# check 15a8 specifically for simple rational L(2)/being or L(2)/pi^2 etc.
E=EllipticCurve('15a8'); L=E.lseries()
L2=float(L(2).n(30))
import math
print(f"15a8: L(2)={L2:.10f}  L(2)/being={L2/Lbeing:.10f}  L(2)/pi^2={L2/math.pi**2:.10f}  L(2)*15/pi^2={L2*15/math.pi**2:.8f}")
print(f"      m(A_41)=Vol/pi=0.6461318944 ; L(2)=0.6614751900 ; ratio L(2)/m={L2/0.6461318944:.8f}")
