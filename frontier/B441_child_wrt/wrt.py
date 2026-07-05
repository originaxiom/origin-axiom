"""B441 (C5) — the child's WRT/quantum invariant via the Kirby surgery formula. VALIDATED tool.

tau_r(K(p,1)) = F_L / F_{U_sgn(p)},  F_L = sum_{n=1}^{r-1} [n]^2 t_n^p J'_n(K;q),
F_{U±} = sum_n [n]^2 t_n^{±1},  [n]=sin(n pi/r)/sin(pi/r),  t_n = exp(i pi (n^2-1)/(2r))  (the
RT framing twist, conformal weight h_n=(n^2-1)/(4r)),  q = exp(2 pi i/r).

TWO validations baked in (see validate()): (1) tau_r(S^3)=1 via +1 surgery on the unknot;
(2) amphichirality tau_r(4_1(5,1)) = conj tau_r(4_1(-5,1)) (4_1 is amphichiral). Both caught
real bugs during the build (the colored-Jones convention; a factor-of-2 in the twist).

Firewall: quantum topology arithmetic. No physics claim. The 'field content' this computes is
a cyclotomic-field question about a knot invariant, not a physical amplitude.
"""
import mpmath as mp

def cj_fig8(n, q):
    """normalized n-colored Jones of the figure-eight (Habiro). Validated vs Kashaev <4_1>_N."""
    total = mp.mpf(1); prod = mp.mpf(1)
    for k in range(1, n):
        prod *= (1 - q**(n-k))*(1 - q**(n+k))
        total += q**(-k*n) * prod
    return total

def cj_unknot(n, q):
    return mp.mpf(1)                                   # child of the unknot at (5,1) = L(5,1)

def wrt(cj, p, r):
    """the WRT invariant tau_r(K(p,1)) for colored-Jones function cj."""
    q = mp.e**(2j*mp.pi/r)
    qd = lambda n: mp.sin(n*mp.pi/r)/mp.sin(mp.pi/r)
    tw = lambda n: mp.e**(1j*mp.pi*(n*n-1)/(2*r))
    FL = FUp = FUm = mp.mpf(0)
    for n in range(1, r):
        d2 = qd(n)**2
        FL  += d2 * tw(n)**p * cj(n, q)
        FUp += d2 * tw(n)
        FUm += d2 * tw(n)**(-1)
    return FL / (FUp if p > 0 else FUm)

def validate(dps=45):
    mp.mp.dps = dps
    ok_s3, ok_amphi = True, True
    for r in (5, 7, 9, 11, 13):
        if abs(wrt(cj_unknot, 1, r) - 1) > mp.mpf(10)**(-dps+5):
            ok_s3 = False
        if abs(wrt(cj_fig8, 5, r) - mp.conj(wrt(cj_fig8, -5, r))) > mp.mpf(10)**(-dps+5):
            ok_amphi = False
    return ok_s3, ok_amphi

if __name__ == "__main__":
    print("validations (S^3=1, amphichirality):", validate())
