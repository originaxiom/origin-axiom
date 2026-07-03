"""B381 (D2) — the twist isolation, executed as pre-registered.

Q1: exhaustive intertwiner search (mod p) over the candidate family
    U = X^m Z^n · diag(zeta15^{q·j(j-1)/2 + r·j}) · (Galois relabel sigma_c on indices)
against U D_theta U^-1 = phase * T^k and U WR_theta U^-1 = phase * S-word — at level 15,
where D_theta, WR_theta (the theta lift) and T, S (the canonical lift, S = F/g) are the two
banked models. Q2: the twist cocycle + the commutant mechanism (Par in the canonical
commutant; Par vs J in the theta model = the Weyl step, P57).
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B372_level45_sweeper"))
from fp_engine import primes_1_mod, primitive_root

N = 15
p = primes_1_mod(720, 1)[0]
g = primitive_root(p)
def zeta(n): return pow(g, (p-1)//n, p)
z15, z60 = zeta(15), zeta(60)

def mm(A,B):
    Bt=list(zip(*B))
    return [[sum(x*y for x,y in zip(r,c))%p for c in Bt] for r in A]
def diag(f): return [[f(j)%p if i==j else 0 for j in range(N)] for i in range(N)]

# the theta lift
Dth = diag(lambda j: pow(z15,(j*(j-1)//2)%15,p))
Dthi= diag(lambda j: pow(z15,(-(j*(j-1)//2))%15,p))
F   = [[pow(z15,(i*j)%15,p) for j in range(N)] for i in range(N)]
iN  = pow(N,p-2,p)
Fi  = [[pow(z15,(-i*j)%15,p)*iN%p for j in range(N)] for i in range(N)]
WRth= mm(mm(F,Dthi),Fi)

# the canonical lift: T = diag zeta^{j^2}; S = F / g(15); g(15) = sum zeta^{x^2} = i*sqrt15
Tc  = diag(lambda j: pow(z15,(j*j)%15,p))
g15 = sum(pow(z15,(x*x)%15,p) for x in range(15)) % p
g15i= pow(g15,p-2,p)
Sc  = [[F[i][j]*g15i%p for j in range(N)] for i in range(N)]

X = [[1 if i==(j+1)%N else 0 for j in range(N)] for i in range(N)]
Z = diag(lambda j: pow(z15,j,p))
Par = [[1 if i==(-j)%N else 0 for j in range(N)] for i in range(N)]

def eq_up_to_phase(A,B):
    nz = next(((i,j) for i in range(N) for j in range(N) if B[i][j]%p), None)
    if nz is None: return False
    i0,j0 = nz
    if A[i0][j0]%p==0: return False
    lam = A[i0][j0]*pow(B[i0][j0],p-2,p)%p
    return all(A[i][j]==lam*B[i][j]%p for i in range(N) for j in range(N))

# Q1: search U = X^m Z^n diag(zeta^{q j(j-1)/2 + r j}) P_sigma_c
from math import gcd
def perm_c(c):
    return [[1 if i==(c*j)%N else 0 for j in range(N)] for i in range(N)]
found = []
targets_D = [Tc]  # conjugation should carry D_theta to a power of T (search k too)
Tpow = {k: diag(lambda j,k=k: pow(z15,(k*j*j)%15,p)) for k in range(1,15) if gcd(k,15)==1}
count = 0
for c in [c for c in range(1,15) if gcd(c,15)==1]:
    Pc = perm_c(c)
    Pci = perm_c(pow(c,-1,15))
    for q in range(15):
        for r in range(15):
            Dg = diag(lambda j,q=q,r=r: pow(z15,(q*(j*(j-1)//2)+r*j)%15,p))
            # U0 = Dg * Pc  (Heisenberg X^m Z^n only shifts labels/phases of the SAME shape:
            # X^m Z^n conjugation on diagonals = diagonal shift; fold into (q,r,c) search + m below)
            for m in range(15):
                Xm = [[1 if i==(j+m)%N else 0 for j in range(N)] for i in range(N)]
                U = mm(Xm, mm(Dg, Pc))
                Ui = None
                # U^{-1} = Pc^{-1} Dg^{-1} X^{-m}
                Dgi = diag(lambda j,q=q,r=r: pow(z15,(-(q*(j*(j-1)//2)+r*j))%15,p))
                Xmi = [[1 if i==(j-m)%N else 0 for j in range(N)] for i in range(N)]
                Ui = mm(Pci, mm(Dgi, Xmi))
                A = mm(mm(U,Dth),Ui)
                hitD = None
                for k,Tk in Tpow.items():
                    if eq_up_to_phase(A,Tk): hitD=k; break
                if hitD is None: continue
                B = mm(mm(U,WRth),Ui)
                # S-side target: S^{±1} up to phase (the canonical S-word family)
                Sci = mm(mm(Fi_:=[[pow(z15,(-i*j)%15,p)*1%p for j in range(N)] for i in range(N)],[[0]*N]*N),[[0]*N]*N) if False else None
                okS = eq_up_to_phase(B, Sc) or eq_up_to_phase(B, mm(mm(Sc,Sc),Sc))
                count += 1
                if okS:
                    found.append(dict(c=c,q=q,r=r,m=m,k=hitD))
print(f"Q1: intertwiner candidates found: {found if found else 'NONE (family exhausted)'}")

# Q2: the commutant fact + the twist cocycle
comm_can = all(eq_up_to_phase(mm(Par,G), mm(G,Par)) for G in (Tc,Sc))
comm_th  = all(eq_up_to_phase(mm(Par,G), mm(G,Par)) for G in (Dth,WRth))
print(f"Q2: Par commutes with the CANONICAL image: {comm_can}; with the THETA image: {comm_th}")
# the defect delta(j) = theta/canonical diagonal phase = zeta^{-j(j+1)/2}
delta_ok = all(Dth[j][j]*pow(Tc[j][j],p-2,p)%p == pow(z15,(-(j*(j+1)//2))%15,p) for j in range(N))
print(f"Q2: twist cocycle delta(j) = zeta15^(-j(j+1)/2) exactly: {delta_ok}")
json.dump(dict(intertwiners=found, par_commutes_canonical=comm_can,
               par_commutes_theta=comm_th, delta_halfchar=delta_ok),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"twist_isolation.json"),"w"), indent=1)
print("DONE")
