# Item 3: K=24 accuracy and overflow behaviour
import sys, math, warnings
import numpy as np, mpmath as mp, pre2
warnings.simplefilter("error")   # any overflow/underflow RuntimeWarning becomes an exception (except we catch below)
ns = pre2.load(); thetas=ns['thetas']; th1p=ns['th1p']; S_A=ns['S_A']; rmax_np=ns['rmax_np']; vertex_angles=ns['vertex_angles']
mp.mp.dps=40
W=ns['W']
def pts_in_P(tau, n=7):
    # sample points of P including the boundary/vertices
    out=[]
    for x in np.linspace(-.5,.5,n):
        for t in np.linspace(-.5,.5,n):
            out.append(x+t*tau)
    return out
cases=[W, -0.5+0.92j, 0.4+0.92j, 0.5+0.92j, 0.13+1.07j, 1j, 2.2j, 3.0j, 4.5j, 5.0j, 5.5j, 5.7j, 6.0j, 7j]
for tau in cases:
    tau=complex(tau)
    q=mp.exp(1j*mp.pi*mp.mpc(tau))
    worst_abs=0; worst_rel=0; worst_S=0
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            for z in pts_in_P(tau):
                z=complex(z)
                t=thetas(np.array(z),tau)
                for r in (1,2,3,4):
                    ref=complex(mp.jtheta(r,mp.pi*mp.mpc(z),q))
                    err=abs(t[r-1]-ref)
                    worst_abs=max(worst_abs,err)
                    if abs(ref)>1e-300: worst_rel=max(worst_rel,err/abs(ref))
                # S_r = th_r(z) th1p /(th_r(0) th_1(z)) relative error vs mp
                if abs(z)>1e-3:
                    tp=mp.jtheta(1,0,q,1)*mp.pi
                    for r in (2,3,4):
                        Sref=complex(mp.jtheta(r,mp.pi*mp.mpc(z),q)*tp/(mp.jtheta(r,0,q)*mp.jtheta(1,mp.pi*mp.mpc(z),q)))
                        worst_S=max(worst_S,abs(S_A(r,np.array(z),tau)-Sref)/abs(Sref))
        print(f"tau={tau}: max|Im z|={0.5*tau.imag:.3f}; theta abs err={worst_abs:.2e}, rel err={worst_rel:.2e}, S_r rel err={worst_S:.2e}")
    except Exception as e:
        print(f"tau={tau}: EXCEPTION {type(e).__name__}: {e}")
# explicit overflow stress: Im tau=5, |Im z| up to 2.55 (beyond P)
for tau,imz in ((5j,2.55),(5.5j,2.8),(9j,4.5)):
    z=0.31+1j*imz
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            t=thetas(np.array(z),tau)
        q=mp.exp(1j*mp.pi*mp.mpc(tau))
        ref=[complex(mp.jtheta(r,mp.pi*mp.mpc(z),q)) for r in (1,2,3,4)]
        print("stress",tau,z,"finite:",all(np.isfinite(t)),"rel errs",[f"{abs(t[i]-ref[i])/abs(ref[i]):.1e}" for i in range(4)])
    except Exception as e:
        print("stress",tau,z,"EXCEPTION",type(e).__name__,e)
