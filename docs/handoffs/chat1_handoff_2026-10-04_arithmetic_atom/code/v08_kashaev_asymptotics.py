"""Kashaev invariant of the figure-eight: <4_1>_N = sum_k prod_j |1-q^j|^2, q = e^{2 pi i/N}.
Fits C and a1 in  K_N ~ C N^{3/2} exp(N vol/2pi)(1 + a1/N + ...)  FROM DATA (not assumed)."""
import mpmath as mp
mp.mp.dps=80
L2=(mp.zeta(2,mp.mpf(1)/3)-mp.zeta(2,mp.mpf(2)/3))/9; vol=12*mp.sqrt(3)*L2/8
def K(N):
    q=mp.expjpi(mp.mpf(2)/N); t=mp.mpf(0); p=mp.mpf(1)
    for k in range(N):
        if k: p*=abs(1-q**k)**2
        t+=p
    return t
Ns=[400,600,800,1000,1200,1600]
R={N:mp.log(K(N))-N*vol/(2*mp.pi)-mp.mpf(3)/2*mp.log(N) for N in Ns}
A=mp.matrix([[1,mp.mpf(1)/N,mp.mpf(1)/N**2,mp.mpf(1)/N**3] for N in Ns]); b=mp.matrix([R[N] for N in Ns])
s=mp.lu_solve(A.T*A,A.T*b)
print(f"C  fitted {mp.nstr(mp.exp(s[0]),15)}   3^(-1/4) {mp.nstr(mp.mpf(3)**(-mp.mpf(1)/4),15)}")
print(f"a1 fitted {mp.nstr(s[1],12)}   11pi/(36sqrt3) {mp.nstr(11*mp.pi/(36*mp.sqrt(3)),12)}")
