#!/usr/bin/env python3
"""B480 Q1 reproducer: split-step QW dispersion; D'Ariano reproduce-gate; the object
doublet (order-4 coin); mass = alignment (not object-forced); object spectrum not a
dispersion (chaotic/arithmetic). See FINDINGS.md."""
import numpy as np
np.seterr(all="ignore"); mp=np.linalg.matrix_power
sy=np.array([[0,-1j],[1j,0]])
def massgap(C):
    g=1e9
    for k in np.linspace(-np.pi,np.pi,4001):
        U=np.diag([np.exp(-1j*k),np.exp(1j*k)])@C
        w=np.sort(np.angle(np.linalg.eigvals(U))); g=min(g,abs(w[1]-w[0])/2)
    return g
# reproduce-gate: mass = coin angle
for th in (0.0,0.3,0.8):
    C=np.cos(th)*np.eye(2)-1j*np.sin(th)*sy
    print(f"coin {th}: mass {massgap(C):.4f}")
# mass = alignment for the object order-4 coin
for a in (0.0,0.3,np.pi/4,np.pi/2):
    R=np.cos(a)*np.eye(2)-1j*np.sin(a)*sy
    print(f"alpha {a:.3f}: mass {massgap(R@np.diag([1j,-1j])@R.conj().T):.4f}")

