"""Corrects chat1's Step B. A FLAT boundary connection carries conjugation-ODD spectral asymmetry.
S^1 Dirac operator, flat U(1) holonomy e^{2 pi i a}: eta(a) = zeta_H(0,a) - zeta_H(0,1-a) = 1 - 2a."""
import mpmath as mp
eta=lambda a: mp.zeta(0,a)-mp.zeta(0,1-a)
for a in [0.1,0.25,0.5,0.75]:
    print(f"a={a}: eta={mp.nstr(eta(mp.mpf(a)),8)}  1-2a={1-2*a:.4f}  eta(1-a)={mp.nstr(eta(1-mp.mpf(a)),8)}")
print("eta odd under conjugation, non-zero for a != 1/2 => flat data can carry chirality via APS")
