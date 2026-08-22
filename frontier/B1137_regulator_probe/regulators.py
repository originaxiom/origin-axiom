"""R48-3 THE REGULATOR PROBE -- object-side regulator computation (STEP 1).

Hurwitz-zeta route, per the sealed prereg/delegation instructions:
    L(s,chi,q) = q^{-s} * sum_a chi(a) * zeta(s, a/q)          (s != 1)
    L(1,chi)   = -q^{-1} * sum_a chi(a) * psi(a/q)             (digamma limit)

chi_-3 mod 3: chi(1)=1, chi(2)=-1               (odd character; K=Q(sqrt(-3)))
chi_5  mod 5: Legendre symbol; chi(1)=chi(4)=1, chi(2)=chi(3)=-1   (even character; K=Q(sqrt(5)))

All object-side computation only -- Gate 5: no SM quantity appears in this module.
"""
from mpmath import mp, mpf, zeta, digamma, sqrt, log, pi

CHI_M3 = {1: 1, 2: -1}                     # mod 3
CHI_5  = {1: 1, 2: -1, 3: -1, 4: 1}         # mod 5, Legendre symbol

def L_chi(s, q, chi, dps):
    """Dirichlet L(s, chi) for a primitive character mod q, via Hurwitz zeta / digamma."""
    old = mp.dps
    mp.dps = dps + 15   # internal guard digits
    try:
        s = mpf(s) if not isinstance(s, int) else s
        if s == 1:
            total = mp.mpf(0)
            for a, ca in chi.items():
                total += ca * digamma(mpf(a) / q)
            val = -total / q
        else:
            total = mp.mpf(0)
            for a, ca in chi.items():
                total += ca * zeta(s, mpf(a) / q)
            val = total * mp.mpf(q) ** (-mpf(s))
        mp.dps = dps + 15
        return +val   # round to current precision context but keep guard digits in the mpf
    finally:
        mp.dps = old

def compute_all(dps=80):
    """Return a dict of all Tier-A object regulators + the two controls, at `dps` working digits."""
    mp.dps = dps + 20
    out = {}

    # --- E6 end: K = Q(sqrt(-3)), chi_-3 mod 3 (odd character) ---
    L_m3 = {}
    for n in range(1, 7):
        L_m3[n] = L_chi(n, 3, CHI_M3, dps)
    zeta_n = {n: zeta(n) for n in range(2, 7)}
    zetaK = {n: zeta_n[n] * L_m3[n] for n in range(2, 7)}

    # --- E8 end: K = Q(sqrt(5)), chi_5 mod 5 (even character) ---
    L_5 = {}
    for n in range(1, 5):
        L_5[n] = L_chi(n, 5, CHI_5, dps)
    zetaF = {n: zeta_n[n] * L_5[n] for n in range(2, 5)}

    # --- controls ---
    Vol = 9 * sqrt(3) * zetaK[2] / pi**2
    entropy_lhs = 2 * sqrt(5) * L_5[1]
    entropy_rhs = 4 * log((1 + sqrt(5)) / 2)

    out['L_chi_m3'] = L_m3          # n=1..6
    out['L_chi_5'] = L_5            # n=1..4
    out['zetaK'] = zetaK            # n=2..6
    out['zetaF'] = zetaF            # n=2..4
    out['zeta_plain'] = zeta_n      # n=2..6 (Riemann zeta, kept for reference/normalization only)
    out['Vol'] = Vol
    out['entropy_lhs'] = entropy_lhs
    out['entropy_rhs'] = entropy_rhs
    out['dps'] = dps
    return out

if __name__ == '__main__':
    mp.dps = 100
    R = compute_all(dps=80)
    mp.dps = 80
    print("dps =", R['dps'])
    print("Vol(m004) target : 2.0298832128193072500...")
    print("9*sqrt3*zetaK(2)/pi^2 =", R['Vol'])
    print("entropy control: 2*sqrt5*L(1,chi5) =", R['entropy_lhs'])
    print("               : 4*log(phi)        =", R['entropy_rhs'])
    print("diff Vol      :", R['Vol'] - mpf('2.0298832128193072500'))
    print("diff entropy  :", R['entropy_lhs'] - R['entropy_rhs'])
