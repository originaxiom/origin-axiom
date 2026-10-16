"""EXPLORATION (P-179, the owner's 'are we sure'): how does the matter's defect D (W87's closed form, as in
p177/motion_defect.py) transform under the moves? D(g t) / D(t) / (c t + d)^k for k = -1, and the phase left over
(the multiplier). If D carries a non-trivial multiplier, a coherent (amplitude) average along a thread g obeys
I = chi(g) I and vanishes unless chi(g) = 1."""
import mpmath as mp
mp.mp.dps = 30
def D(t):
    t = mp.mpc(t); q = mp.exp(1j*mp.pi*t)
    t2, t3 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q)
    eta = mp.exp(1j*mp.pi*t/12)*mp.qp(mp.exp(2j*mp.pi*t))
    lam = t2**4/t3**4; h = lam*mp.log(abs(lam)) + (1 - lam)*mp.log(abs(1 - lam))
    return -t3**4*h/(4*mp.pi*eta**6)
def eta6(t):
    t = mp.mpc(t); return (mp.exp(1j*mp.pi*t/12)*mp.qp(mp.exp(2j*mp.pi*t)))**6
G = {"L": (1, 1, 0, 1), "R": (1, 0, 1, 1), "S=LR^-1L": (0, 1, -1, 0), "L^-1R": (0, -1, 1, 1)}
pts = [mp.mpc(0.13, 1.1), mp.mpc(-0.31, 0.92), mp.mpc(0.4, 1.7)]
for name, (a, b, c, d) in G.items():
    for k in (-1,):
        rD = [D((a*t + b)/(c*t + d))/D(t)/(c*t + d)**k for t in pts]
        rE = [eta6((a*t + b)/(c*t + d))/eta6(t)/(c*t + d)**3 for t in pts]
        print(f"{name:9s} D: ratio/(ct+d)^{k} = {mp.nstr(rD[0], 8)}  spread {mp.nstr(max(abs(x - rD[0]) for x in rD), 3)}"
              f"   | eta^6 multiplier {mp.nstr(rE[0], 8)}  spread {mp.nstr(max(abs(x - rE[0]) for x in rE), 3)}")
