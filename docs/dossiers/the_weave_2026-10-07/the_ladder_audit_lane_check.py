# Post hoc check (2026-10-24) of the audit lane's two countercontrols in its ladder opinion (its relay at a9053eab7),
# on this seat's own code. Not a sealed run.
# (1) PSL(2, F_7) is a finite quotient of the moves' group with T of order 7, so "every finite quotient" must read
#     "every finite quotient by T^N" (the triangle groups Delta(2, 3, N)).
# (2) For an even lattice L that is not unimodular, Z_L = (Im tau)^(r/2) sum_mu |Theta_mu|^2 is still invariant under
#     T and S, so "invariance under every move" selects a unimodular lattice only for a single scalar theta series.
import itertools
import mpmath as mp

p = 7
def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % p for j in range(2)) for i in range(2))
I = ((1, 0), (0, 1)); M = ((p - 1, 0), (0, p - 1))
S = ((0, p - 1), (1, 0)); U = ((0, p - 1), (1, 1))
def power(A, n):
    R = I
    for _ in range(n):
        R = mul(R, A)
    return R
T = mul(S, U)
proj_order = next(n for n in range(1, 50) if power(T, n) in (I, M))
G = {I}; frontier = [I]
while frontier:
    nxt = []
    for g in frontier:
        for h in (S, U):
            x = mul(g, h)
            if x not in G:
                G.add(x); nxt.append(x)
    frontier = nxt
print("(1) S^2 = -I:", power(S, 2) == M, "| U^3 = -I:", power(U, 3) == M, "| T = SU projective order:", proj_order,
      "| |<S, U>| in SL(2, F7):", len(G), "| projective:", len(G) // 2)

mp.mp.dps = 30
def theta(mu, tau, N=40):     # the A1 lattice sqrt(2) Z: x = sqrt(2)(n + mu/2), q^(x^2/2), mu = 0, 1 in L*/L
    return mp.fsum(mp.exp(2j * mp.pi * tau * (n + mu / mp.mpf(2)) ** 2) for n in range(-N, N + 1))
def Z(tau):
    return mp.sqrt(mp.im(tau)) * (abs(theta(0, tau)) ** 2 + abs(theta(1, tau)) ** 2)
tau = mp.mpc("0.137", "1.291")
zt, zT, zS = Z(tau), Z(tau + 1), Z(-1 / tau)
print("(2) A1 (det 2): Z(tau) =", mp.nstr(zt, 15), "| |Z(tau+1)/Z - 1| =", mp.nstr(abs(zT / zt - 1), 3),
      "| |Z(-1/tau)/Z - 1| =", mp.nstr(abs(zS / zt - 1), 3))
th = lambda t: theta(0, t)
k = mp.mpf(1) / 2
print("    the scalar theta of A1 alone is not modular of its weight: |Theta_0(-1/tau)/((-i tau)^(1/2) Theta_0(tau)) - 1| =",
      mp.nstr(abs(th(-1 / tau) / ((-1j * tau) ** k * th(tau)) - 1), 3))
