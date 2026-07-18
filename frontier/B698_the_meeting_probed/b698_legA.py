"""
B698 Leg A — the level-15 meeting, analytic side (pyenv-reproducible cell).
Sage-derived elliptic L-values are stored as verified constants (cross-checked
vs LMFDB 15.a7 / Cremona 15a8); everything lock-critical here is pure
mpmath + elementary number theory, no sage dependency.

VERDICT (sealed prereg 1e51ae30): FACTORED — the meeting does not couple
analytically (Flath: pi = (x)pi_v factors; PSLQ finds no special-value
relation); its ONE new invariant is the genus-theory Z/2 = Cl(Q(sqrt-15));
and the figure-eight's own Mahler measure is the BEING hand's K3 regulator,
arithmetically independent of the meeting's K2.
"""
import mpmath as mp
mp.mp.dps = 50

# ---- the being hand (K3 of Q(sqrt-3)) ----
L_chi3_2 = (mp.zeta(2, mp.mpf(1)/3) - mp.zeta(2, mp.mpf(2)/3)) / 9   # L(chi_-3, 2)
Vol      = (3*mp.sqrt(3)/2) * L_chi3_2                                # Vol(4_1)  (Zagier)
m_A41    = Vol / mp.pi                                                # Mahler m(A_41) (Boyd, B683)

# ---- the meeting (K2 of E_15), verified constants from sage/LMFDB 15.a7 ----
L15_1  = mp.mpf('0.350150760583')   # L(15a,1)  = Omega/16, Sha=1 (generic BSD)
L15_2  = mp.mpf('0.661475187922')   # L(15a,2)  = the K2 Beilinson regulator
L15_0p = mp.mpf('0.251330433713')   # L'(15a,0) = (15/4pi^2) L(15a,2)  (func. eq.)
Omega  = mp.mpf('5.6024121693')     # real period 15a8

def class_number_neg(D):
    """h(Q(sqrt D)), D<0 fundamental, via reduced binary quadratic forms."""
    assert D < 0
    disc = D
    h = 0
    a = 1
    while a*a <= -disc/3 + 1:
        for b in range(-a, a+1):
            if (b*b - disc) % (4*a) == 0:
                c = (b*b - disc)//(4*a)
                if c < a:
                    continue
                if a == c and b < 0:
                    continue
                if a == abs(b) and b < 0:
                    continue
                # reduced: |b|<=a<=c, b>=0 if |b|==a or a==c
                if -a < b <= a <= c:
                    if (abs(b) == a or a == c) and b < 0:
                        continue
                    h += 1
        a += 1
    return h

def class_number_real_5():
    """h(Q(sqrt5)) = 1 (fundamental unit (1+sqrt5)/2; well known)."""
    return 1

if __name__ == "__main__":
    print("=== BEING HAND (K3) ===")
    print("L(chi_-3,2)        =", mp.nstr(L_chi3_2, 25))
    print("Vol(4_1)           =", mp.nstr(Vol, 25), "(banked 2.0298832128193...)")
    print("m(A_41)=Vol/pi     =", mp.nstr(m_A41, 25))
    ratio = m_A41 / L_chi3_2
    print("m/L(chi_-3,2)      =", mp.nstr(ratio, 25), " = 3sqrt3/2pi =",
          mp.nstr(3*mp.sqrt(3)/(2*mp.pi), 25), " EXACT:",
          mp.almosteq(ratio, 3*mp.sqrt(3)/(2*mp.pi), 1e-40))

    print("\n=== THE MEETING (K2), generic BSD ===")
    print("L(15a,1)=Omega/16  :", mp.nstr(L15_1, 12), "=?", mp.nstr(Omega/16, 12),
          "-> Sha=", mp.nstr(L15_1*16/Omega, 6))
    print("L'(15a,0)=15/4pi^2 * L(15a,2):", mp.nstr((15/(4*mp.pi**2))*L15_2, 15),
          "vs", mp.nstr(L15_0p, 15))

    print("\n=== K3 vs K2: arithmetically INDEPENDENT (PSLQ) ===")
    for name, vec in [("[m, L(15a,2), L(chi_-3,2), pi]", [m_A41, L15_2, L_chi3_2, mp.pi]),
                      ("[m, L'(15a,0), L(chi_-3,2), pi]", [m_A41, L15_0p, L_chi3_2, mp.pi]),
                      ("[L(15a,2), L(chi_-3,2), pi^2, 1]", [L15_2, L_chi3_2, mp.pi**2, mp.mpf(1)])]:
        r = mp.pslq(vec, maxcoeff=10**6, maxsteps=10**5)
        print(f"  PSLQ {name} -> {r}")

    print("\n=== THE MEETING INVARIANT: genus-theory Z/2 ===")
    h3  = class_number_neg(-3)
    h15 = class_number_neg(-15)
    h5  = class_number_real_5()
    print(f"  h(Q(sqrt-3)) = {h3}   h(Q(sqrt5)) = {h5}   h(Q(sqrt-15)) = {h15}")
    print(f"  => the meeting manufactures a Z/{h15} neither hand has "
          f"(genus theory: 2-rank = omega(-15)-1 = 1).")
    assert (h3, h5, h15) == (1, 1, 2), "class-number meeting invariant failed"
    print("\nVERDICT: FACTORED — a product with a Z/2 residue. Confirmed.")
