"""w47 verifier.  Claims (SM relay section 51, W47) and expectations:
 C1 Mp2(Z)=<S,T|S^2=(ST)^3,S^8=1> has abelianization Z/24 => 24 characters chi_r(T)=e(r/24), chi(S)=e(-r/8)  [expect HOLDS]
 C2 exactly six characters keep a given weight's central consistency (r = const mod 4); 18 leave no sections [expect HOLDS]
 C3 cusp exponents of rho_theta (x) chi^j (allowed j) are all odd multiples of 1/24 => no exponent 0, so canonical/L2/cuspidal agree [expect HOLDS]
 C4 flat twists: chi_{3/2} = 0 except at j=4 (main B1634 P5: +1); relay says -1 at r=4 and r=20 [expect: sign/dual convention, maybe r=20 differs]
 rho_theta built independently from classical theta/eta laws: v=(th2^2,th3^2,th4^2)*eta^21, weight 23/2."""
import numpy as np, sympy as sp, itertools
from sympy import Matrix
e=lambda x: np.exp(2j*np.pi*x)
# C1: abelianization via Smith normal form. relations in additive notation: S^2 (ST)^3 ^-1 -> 2s-3s-3t = -s-3t ; 8s
M=Matrix([[-1,-3],[8,0]])
from sympy.matrices.normalforms import smith_normal_form
print("C1 SNF of relation matrix:",smith_normal_form(M,domain=sp.ZZ).tolist(), "=> |ab| =",abs(M.det()))
# S=T^-3 so S^8 = T^-24
# rho_theta
P=np.array([[0,0,1],[0,1,0],[1,0,0]],dtype=complex)
Tth=np.diag([1j,0,0]).astype(complex); Tth[1,2]=Tth[2,1]=1  # th3^2,th4^2 swap
RT=e(21/24)*Tth
RS=e(1/8)*P   # (-i tau)^{23/2} = e(1/8) tau^{23/2}; theta^2 laws -i tau, swap 2<->4
print("T eigenphases/ (1/24):",sorted(np.round(np.angle(np.linalg.eigvals(RT))/(2*np.pi)%1*24,6)))
# check relations up to scalar
def prop(A,B):
    k=np.argmax(abs(B)); c=A.flat[k]/B.flat[k]; return np.allclose(A,c*B),c
print("S^2 vs (ST)^3:",prop(RS@RS,np.linalg.matrix_power(RS@RT,3)))
print("S^8:",np.round(np.linalg.matrix_power(RS,8)[0,0],6))
# numeric check of the laws at a point (independent mpmath)
import mpmath as mp
def vec(t):
    q=mp.exp(1j*mp.pi*t); th=[mp.jtheta(n,0,q)**2 for n in (2,3,4)]
    eta=mp.exp(2j*mp.pi*t/24)*mp.nprod(lambda n:1-mp.exp(2j*mp.pi*t*n),[1,mp.inf])
    return np.array([complex(x*eta**21) for x in th])
t=mp.mpc(-0.31,0.93)
for name,(A,tt,k) in {"S":(RS,-1/t,0),"T":(RT,t+1,0)}.items():
    lhs=vec(tt); f=vec(t)
    fac=complex(mp.sqrt(t))**23 if name=="S" else 1
    # principal sqrt for tau^{23/2}
    print(name,"law rel err",np.linalg.norm(lhs-fac*(A@f))/np.linalg.norm(lhs))
# dimension formula calibration
def alpha(A):
    ev=np.linalg.eigvals(A); out=0
    for x in ev:
        b=(np.angle(x)/(2*np.pi))%1
        if abs(b-1)<1e-9: b=0
        out+=b
    return out
def chi_gen(S,T,k,m,n,inv=False):
    # fixed-point factors: i^k=e(k/4) at tau=i, e(k/6) at tau=e(1/3). Borcherds/Skoruppa: d + dk/12 - alpha(e(k/4)S) - alpha((e(k/3) ST)^-1) - alpha(T); S,ST rescaled by phases e(m/8), e(n/6)
    d=3
    a=alpha(e(k/4)*e(m/8)*S); b=alpha(np.linalg.inv(e(k/6)*e(n/6)*(S@T)))
    return d+d*k/12-a-b-alpha(T)
target={7/2:1,11/2:1,15/2:2,19/2:2,23/2:3,27/2:3}
good=[]
CONJ=False
for cj in (False,True):
 for m in range(8):
  for n in range(6):
    A,B=(np.conj(RS),np.conj(RT)) if cj else (RS,RT)
    vals={k:chi_gen(A,B,k,m,n) for k in target}
    if all(abs(vals[k]-target[k])<1e-6 for k in target): good.append((cj,m,n))
print("phase choices (S*e(m/8), ST*e(n/6)) reproducing dims 1,1,2,2,3,3 at k=7/2..27/2:",good)
CONJ,m,n=good[0]
print('calibration:',good)

print("\nj  Z-phase  exponents(x24)  chi_{3/2}")
rows=[]
for j in range(24):
    Sj=RS*e(-j/8); Tj=RT*e(j/24)
    if CONJ: Sj,Tj=np.conj(Sj),np.conj(Tj)
    Zj=np.linalg.matrix_power(Sj,2)[0,0]
    exps=sorted(np.round(((np.angle(np.linalg.eigvals(Tj))/(2*np.pi))%1)*24,6))
    # n phase for twisted: ST rescales consistently; phase fixed by (ST)^3=S^2 -> keep same (m,n) relative: use chi of twisted with same m,n
    c=chi_gen(Sj,Tj,1.5,m,n).real
    # dual twist: rho^vee = conj; weight same
    cd=chi_gen(np.conj(Sj),np.conj(Tj),1.5,m,n).real
    rows.append((j,Zj,exps,c,cd)); print(j,np.round(Zj,3),exps,round(c,4),round(cd,4))
allowed=[j for j in range(24) if abs(rows[j][1]-rows[0][1])<1e-9]
print("allowed j (Z-phase = j=0 phase):",allowed,"count",len(allowed))
print("all exponents at allowed j odd multiples of 1/24:",all(all(abs(x-round(x))<1e-6 and int(round(x))%2==1 for x in rows[j][2]) for j in allowed))
print("exponents odd for ALL j in 0..23 too?",all(all(int(round(x))%2==1 for x in rows[j][2]) for j in range(24)))
print("chi_{3/2} at allowed j:",{j:round(rows[j][3],3) for j in allowed}," dual-conj:",{j:round(rows[j][4],3) for j in allowed})
