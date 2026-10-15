import sys; sys.path.insert(0,'.')
from ref2 import *
mp.mp.dps = 25
tau = mp.mpc(0.23, 0.97); law = Rlaw(tau); J = C*tau+D
def V(q, a, b): return (mp.mpf(q*b)/5, mp.mpf(q*a)/5)
def k5(z):  # exponent k of zeta from z^2 (kills sign); return k mod 5 and sign
    k2 = mp.arg(z**2)/(2*mp.pi)*5   # = 2k mod 5
    k = int(mp.nint(k2))*3 % 5      # 2^{-1}=3 mod 5
    sgn = z / mp.exp(2j*mp.pi*k/5)
    return k, mp.nstr(sgn.real, 3)
print("per-leg reduction mod 1, down/lepton/up at (1,2): (k, sign) with ratio = sign*zeta^k")
for nm,(qu,qd) in {"up":(-3,5),"down":(3,-1),"lepton":(3,-9)}.items():
    for red in (False, True):
        _,o0,o = closure(tau, V(qu,1,2), V(qd,1,2), law, red=red)
        print(f"  {nm:6s} red={red}:", [k5(x) if x is not None else None for x in o], "id:", k5(o0) if o0 is not None else None)
print("general charges (qu,qd) at (1,2): observed k vs 2(qu^2+qd^2) mod 5")
bad = 0
for qu in range(-6,7):
    for qd in range(-6,7):
        _,o0,o = closure(tau, V(qu,1,2), V(qd,1,2), law)
        ks = set(k5(x)[0] for x in o if x is not None)
        pred = (2*(qu*qu+qd*qd)) % 5
        if ks != {pred}: bad += 1; print("  mismatch", qu, qd, ks, pred)
print("  mismatches:", bad, "of 169")
# single theta-constant leg with charge q: T_s[qv](g tau) J^{1/2}... compare with untwisted single-theta law
print("single theta-constant leg, charge q at (1,2): k such that phase = +-zeta^k  (H=+3 vs Hbar=-3)")
tg = g(tau)
for q in (-3, 3, 1, -1, 2, 5):
    row = []
    for n,t in ((2,4),(4,3),(3,2)):  # theta_i <- theta_j etc. (i,j,k)=(2,4,3): R law i<-j, j<-k, k<-i
        base = T(n,0,0,tg)/T(t,0,0,tau)
        v = V(q,1,2); r = T(n,v[0],v[1],tg)/T(t,v[0],v[1],tau)/base
        row.append(k5(r))
    print(f"  q={q:+d}:", row, " pred 2q^2/2=q^2 mod5:", (q*q)%5)
