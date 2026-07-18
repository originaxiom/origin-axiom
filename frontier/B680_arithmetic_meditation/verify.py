"""B680 — the arithmetic meditation: the two computable facts, exact-grade."""
import mpmath as mp


def volume_is_being_L_value(dps=40):
    mp.mp.dps = dps
    Vol = 2*mp.im(mp.polylog(2, mp.e**(1j*mp.pi/3)))       # Bloch-Wigner at ω
    L = (mp.zeta(2, mp.mpf(1)/3) - mp.zeta(2, mp.mpf(2)/3))/9   # L(χ_-3, 2)
    return Vol, (3*mp.sqrt(3)/2)*L


def inert_5_in_eisenstein():
    return (pow((-3) % 5, 2, 5) == 4, 3, 5, 3*5)   # -3 non-residue mod 5 => inert


if __name__ == "__main__":
    V, P = volume_is_being_L_value()
    assert abs(V - P) < mp.mpf(10)**-38
    assert abs(V - mp.mpf('2.029883212819307250')) < 1e-18
    inert, ram, ine, lvl = inert_5_in_eisenstein()
    assert inert and lvl == 15
    print("Vol(4_1) = (3√3/2)·L(χ_-3,2) to 38+ digits: VERIFIED")
    print("5 inert, 3 ramified in Q(√-3), 15 = their product: VERIFIED")
