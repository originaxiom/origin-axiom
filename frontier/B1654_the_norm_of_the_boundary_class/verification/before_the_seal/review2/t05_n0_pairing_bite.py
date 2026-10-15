# Item 7: does the N0 channel-assignment check bite? Re-implement it with deliberate mis-assignments.
import math, itertools
import numpy as np, mpmath as mp, pre2
ns = pre2.load(); thetas=ns['thetas']; th1p=ns['th1p']; S_A=ns['S_A']; R_A=ns['R_A']; W=ns['W']
mp.mp.dps=40
qq=lambda tau: mp.exp(1j*mp.pi*mp.mpc(tau))
CPRIME={2:-1,4:-1,3:1j}
def v_B1651(r,z,tau):
    q=qq(tau); return complex(CPRIME[r]*mp.jtheta(r,0,q)*mp.jtheta(r,mp.pi*mp.mpc(z),q)/mp.jtheta(1,mp.pi*mp.mpc(z),q))
def check(Rfun, Sfun, taus=(W,1j,0.13+1.07j), zs=(0.1+0.07j,-0.23+0.31j)):
    return max(abs(Rfun(tau)[r]*complex(Sfun(r,np.array(z),tau))-v_B1651(r,z,tau))/abs(v_B1651(r,z,tau)) for tau in taus for z in zs for r in (2,3,4))
print("as coded:", check(R_A,S_A))
# (1) swap R keys 2<->4
def R_swap24(tau): R=R_A(tau); return {2:R[4],4:R[2],3:R[3]}
print("R keys 2<->4 swapped:", check(R_swap24,S_A), "  (per tau:", [check(R_swap24,S_A,taus=(t,)) for t in (W,1j,0.13+1.07j)], ")")
# (2) swap R keys 2<->3
def R_swap23(tau): R=R_A(tau); return {2:R[3],3:R[2],4:R[4]}
print("R keys 2<->3 swapped:", check(R_swap23,S_A), "  (per tau:", [check(R_swap23,S_A,taus=(t,)) for t in (W,1j,0.13+1.07j)], ")")
# (3) swap R keys 3<->4
def R_swap34(tau): R=R_A(tau); return {2:R[2],3:R[4],4:R[3]}
print("R keys 3<->4 swapped:", check(R_swap34,S_A), "  (per tau:", [check(R_swap34,S_A,taus=(t,)) for t in (W,1j,0.13+1.07j)], ")")
# (4) S channel mis-indexed (S_A(r) uses theta_{r'})
def S_swap(perm):
    def f(r,z,tau):
        t=thetas(np.asarray(z),tau); t0=thetas(np.array(0.0),tau); rr=perm[r]
        return t[rr-1]*th1p(tau)/(t0[rr-1]*t[0])
    return f
for perm in ({2:4,4:2,3:3},{2:3,3:2,4:4},{2:2,3:4,4:3},{2:3,3:4,4:2},{2:4,3:2,4:3}):
    print("S perm",perm,":", check(R_A,S_swap(perm)))
# (5) wrong phase on R_k: -i instead of i; or +1 on R_i
def R_phase(tau): R=R_A(tau); return {2:R[2],4:R[4],3:-R[3]}
print("R_k sign flip:", check(R_phase,S_A))
def R_phase2(tau): R=R_A(tau); return {2:R[2],4:R[4],3:1j*R[3]}
print("R_k extra i (c3 = -1 instead of i):", check(R_phase2,S_A))
# (6) is the check blind to swapping at tau = i only? (theta2 = theta4 there)
print("R keys 2<->4 swapped, tau=i only:", check(R_swap24,S_A,taus=(1j,)))
