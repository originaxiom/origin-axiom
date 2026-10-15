import sys; sys.path.insert(0,'.')
import numpy as np, mpmath as mp, pre
ns = pre.load()
thetas, th1p, S_A, R_A = ns['thetas'], ns['th1p'], ns['S_A'], ns['R_A']
mp.mp.dps = 40
rng = np.random.default_rng(99)
# (1) theta series vs mpmath jtheta at several (tau, z) incl. edge-of-P points
worst = 0
for tau in (0.13+1.07j, -0.4+0.95j, 0.5+0.9j, 2.9j, 4.9j):
    q = mp.exp(1j*mp.pi*mp.mpc(tau))
    for z in (0.3+0.1j, -0.5-0.4j*tau.imag/1.0*0.5, 0.5+0.5*tau, 0.01+0.002j):
        z = complex(z)
        t = thetas(np.array(z), tau)
        for r in (1,2,3,4):
            ref = complex(mp.jtheta(r, mp.pi*mp.mpc(z), q))
            worst = max(worst, abs(ref - t[r-1])/max(abs(ref),1e-300))
print("theta series vs jtheta, worst rel:", worst)
# (2) th1p = 2 pi eta^3 with eta = q^(1/12) prod (1-q^(2n)), q = e^{i pi tau}
for tau in (0.13+1.07j, 2j, 1j, ns['W']):
    q = mp.exp(1j*mp.pi*mp.mpc(tau))
    eta = mp.exp(1j*mp.pi*mp.mpc(tau)/12)*mp.qp(q**2)
    d = complex(2*mp.pi*eta**3)
    print("th1p vs 2 pi eta^3:", tau, abs(th1p(tau)-d))
    # also eta from standard: exp(2 pi i tau/24) prod(1-exp(2 pi i n tau))
    eta2 = mp.exp(2j*mp.pi*mp.mpc(tau)/24)*mp.qp(mp.exp(2j*mp.pi*mp.mpc(tau)))
    print("   eta formulas agree:", abs(eta-eta2))
    # theta2 theta3 theta4 = 2 eta^3
    t2,t3,t4 = (mp.jtheta(r,0,q) for r in (2,3,4))
    print("   th2 th3 th4 - 2 eta^3:", abs(t2*t3*t4-2*eta**3))
# (3) S_r ~ 1/z with residue 1, odd; s1 = -e_r/2
for tau in (0.13+1.07j, 1j):
    for r in (2,3,4):
        for z in (1e-4*(1+0.3j), 1e-4j):
            val = S_A(r, np.array(z), tau)
            print("tau",tau,"r",r,"z S(z) - 1 =", abs(val*z-1))
        # oddness
        z0 = 0.2+0.13j
        print("   odd:", abs(S_A(r,np.array(z0),tau)+S_A(r,np.array(-z0),tau)))
# (4) periodicity of |S_r|^2 and signs
tau = 0.13+1.07j
z0 = 0.17+0.21j
for r in (2,3,4):
    s0 = S_A(r,np.array(z0),tau)
    s1 = S_A(r,np.array(z0+1),tau)
    s2 = S_A(r,np.array(z0+tau),tau)
    print("r",r,"S(z+1)/S(z) =", np.round(s1/s0,10), " S(z+tau)/S(z) =", np.round(s2/s0,10))
# (5) R.R = 0 and magnitudes
for tau in (0.13+1.07j, 1j, ns['W'], 3j):
    R = R_A(tau)
    print("tau",tau,"R.R/|R|^2 =", abs(sum(R[r]**2 for r in (2,3,4)))/sum(abs(R[r])**2 for r in (2,3,4)), "R_i,R_j,R_k=", np.round([R[2],R[4],R[3]],6))
