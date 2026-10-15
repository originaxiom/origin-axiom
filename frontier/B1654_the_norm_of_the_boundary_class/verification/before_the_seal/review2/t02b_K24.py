import sys, math, warnings
import numpy as np, mpmath as mp, pre2
ns = pre2.load(); thetas=ns['thetas']; S_A=ns['S_A']
mp.mp.dps=40
W=ns['W']
rng=np.random.default_rng(7)
cases=[W, -0.5+0.92j, 0.4+0.92j, 0.5+0.92j, 0.13+1.07j, 1j, 2.2j, 3.0j, 4.5j, 5.0j, 5.5j, 5.7j, 6.0j, 7j]
for tau in cases:
    tau=complex(tau)
    q=mp.exp(1j*mp.pi*mp.mpc(tau))
    tp=mp.jtheta(1,0,q,1)*mp.pi
    worst_th=0; worst_S=0
    for _ in range(60):
        x=rng.uniform(-.5,.5); t=rng.uniform(-.5,.5); z=complex(x+t*tau)
        th=thetas(np.array(z),tau)
        for r in (1,2,3,4):
            ref=complex(mp.jtheta(r,mp.pi*mp.mpc(z),q))
            if abs(ref)>1e-8*math.exp(math.pi*abs(z.imag)): worst_th=max(worst_th,abs(th[r-1]-ref)/abs(ref))
        for r in (2,3,4):
            Sref=complex(mp.jtheta(r,mp.pi*mp.mpc(z),q)*tp/(mp.jtheta(r,0,q)*mp.jtheta(1,mp.pi*mp.mpc(z),q)))
            if abs(Sref)>1e-6:
                worst_S=max(worst_S,abs(S_A(r,np.array(z),tau)-Sref)/abs(Sref))
    # th1p
    d=ns['th1p'](tau); dref=complex(tp)
    print(f"tau={tau:.4f}: theta rel err (random z in P, |ref|>1e-8 scale) = {worst_th:.2e}; S_r rel err = {worst_S:.2e}; th1p rel err = {abs(d-dref)/abs(dref):.2e}")
# truncation: size of the first dropped term (n=24 in th1/th2; m=24 in th3/th4) at the worst z in P
for tau in (W, -0.5+0.92j, 1j, 5j, 5.5j):
    tau=complex(tau); qa=abs(np.exp(1j*np.pi*tau))
    imz=0.5*tau.imag
    n=24
    d1=qa**((n+.5)**2)*math.exp((2*n+1)*math.pi*imz)
    d3=qa**(n**2)*math.exp(2*n*math.pi*imz)
    print(f"tau={tau:.3f}: first dropped terms at the edge of P: theta1/2: {d1:.2e}  theta3/4: {d3:.2e}")
