"""P3 — the verdict pass.

1. PRED-2 exactness: full factorint (with exponents) of every level-4 minpoly
   discriminant, odd AND even blocks; the falsifier fires only on an ODD
   exponent of a prime >= 5 (field ramification), not on index primes
   (even exponents) — the envelope Q(zeta_192) ramifies only at {2,3}.
2. Exact sector traces at level 4: tr_odd = (Z - Tr(Theta rho))/2 with
   Tr(Theta rho) certified by integer reduction mod Phi_192.
3. The cross-level parity comparison: B_even orders at k=1..4 and the even
   block's magnitude arithmetic at k=3 (is the golden import sector-blind?).
4. The k=1..4 law table assembled.
"""
import sys
sys.path.insert(0, 'scripts')

import mpmath as mp
import numpy as np
import sympy as sp

from engine import Level, weyl_group, mp_odd_blocks, theta, HVEE
from p2_certify import mp_even_block, minpolys, eig_order, fib_order

mp.mp.dps = 50


def exact_trace_theta_rho(L):
    """Tr(Theta rho) = sum_a T_{theta a}^2 S_{theta a, a} T_a — integer
    coefficient vector over zeta_{12K}, reduced mod Phi_{12K}. Returns
    (is_zero, reduced_poly, numeric)."""
    M12 = 12 * L.K
    idx_theta = [L.PRIM.index(theta(p)) for p in L.PRIM]
    coef = [0] * M12
    for a in range(L.N):
        ta = idx_theta[a]
        sh = (2 * int(L.T_expo[ta]) + int(L.T_expo[a])) % M12
        row = L.counts[ta, a]
        for j in range(L.M6):
            c = int(row[j])
            if c:
                coef[(2 * j + sh) % M12] += c
    x = sp.Symbol('x')
    poly = sp.Poly(list(reversed(coef)), x, domain='ZZ')
    phi = sp.Poly(sp.cyclotomic_poly(M12, x), x, domain='ZZ')
    red = poly.rem(phi)
    zval = mp.e ** (2j * mp.pi / M12)
    num = mp.fsum(int(c) * zval ** e for e, c in enumerate(coef) if c)
    return red.is_zero, red, num


def disc_parity_report(mps_, label):
    """For each minpoly: factorint(disc) with exponents; flag any prime >= 5
    with ODD exponent (genuine field ramification -> PRED-2 falsifier)."""
    print(f"\n--- disc exponent parity: {label} ---")
    fired = False
    seen = set()
    for w, coeffs, disc, primes in mps_:
        if coeffs is None:
            print(f"  w = {w}: NO MINPOLY FOUND (raise degree?)")
            fired = True
            continue
        key = tuple(coeffs)
        if key in seen:
            continue
        seen.add(key)
        if disc == 0:
            continue
        fac = sp.factorint(abs(int(disc)))
        bad = {p: e for p, e in fac.items() if p >= 5 and e % 2 == 1}
        tag = f"  minpoly {coeffs}: disc = {sp.factorint(abs(int(disc)))}"
        if bad:
            tag += f"   *** ODD-EXPONENT PRIME >= 5: {bad} — F2 FIRES ***"
            fired = True
        print(tag)
    return fired


def block_magnitudes(S_block, K, dps=50):
    vals = []
    for i in range(S_block.rows):
        for j in range(S_block.cols):
            m = mp.sqrt((S_block[i, j] * mp.conj(S_block[i, j])).real)
            if m > mp.mpf('1e-30') and not any(abs(m - v) < mp.mpf('1e-30') for v in vals):
                vals.append(m)
    return sorted(2 * K * v ** 2 for v in vals)


def main():
    W, eps = weyl_group()

    # ---- 2. exact sector traces at level 4 ----
    print("=== exact sector-trace certificates, level 4 ===")
    L4 = Level(4, W, eps)
    zt_zero, _, zt_num = exact_trace_theta_rho(L4)
    print(f"Tr(Theta rho) zero-poly = {zt_zero}; numeric ~ {mp.nstr(zt_num, 12)}")
    print("with Z4 = 0 exactly (P2): tr_odd = (Z - Tr(Theta rho))/2 = 0 EXACTLY, "
          "tr_even = 0 EXACTLY" if zt_zero else "SECTOR TRACES NOT BOTH ZERO — recheck")

    # sanity: same certificate at levels 1-3 (expect NONZERO: +1 lives somewhere)
    for k in (1, 2, 3):
        Lk = Level(k, W, eps)
        z0, _, num = exact_trace_theta_rho(Lk)
        print(f"  level {k}: Tr(Theta rho) zero-poly = {z0}; numeric ~ {mp.nstr(num, 10)}")

    # ---- 1. PRED-2 exactness at level 4 ----
    S_odd, B_odd, _ = mp_odd_blocks(L4, dps=50)
    ws_odd = block_magnitudes(S_odd, L4.K)
    mps_odd = minpolys(ws_odd)
    f_odd = disc_parity_report(mps_odd, "level-4 ODD block (18 values)")

    S_even4, B_even4 = mp_even_block(L4, dps=50)
    ws_even4 = block_magnitudes(S_even4, L4.K)
    mps_even4 = minpolys(ws_even4)
    f_even4 = disc_parity_report(mps_even4, "level-4 EVEN block (24 values)")

    print(f"\nPRED-2 verdict (field-ramification form): odd-block F2 fired = {f_odd}; "
          f"even-block (control) fired = {f_even4}")

    # ---- 3. cross-level parity comparison ----
    print("\n=== B_even orders across the ladder ===")
    ladder = {}
    for k in (1, 2, 3, 4):
        Lk = Level(k, W, eps)
        S_e, B_e = mp_even_block(Lk, dps=50)
        oe, dev, props = eig_order(B_e, dps=50)
        ladder[k] = oe
        print(f"level {k}: ord(B_even) = {oe} (dev {dev if dev is None else f'{dev:.1e}'})")

    print("\n=== level-3 EVEN block magnitude arithmetic (the golden-import parity control) ===")
    L3 = Level(3, W, eps)
    S_e3, B_e3 = mp_even_block(L3, dps=50)
    ws_e3 = block_magnitudes(S_e3, L3.K)
    print(f"{len(ws_e3)} distinct even-block magnitudes at level 3")
    mps_e3 = minpolys(ws_e3)
    disc_parity_report(mps_e3, "level-3 EVEN block")
    sqrt5 = any(coeffs and len(coeffs) == 3 and
                sp.Integer(coeffs[1] ** 2 - 4 * coeffs[0] * coeffs[2]).is_positive and
                sp.factorint(coeffs[1] ** 2 - 4 * coeffs[0] * coeffs[2]).get(5, 0) % 2 == 1
                for _, coeffs, _, _ in mps_e3)
    deg_ge2 = [c for _, c, _, _ in mps_e3 if c and len(c) > 2]
    print(f"level-3 even block: any quadratic with sqrt5 disc = {sqrt5}; "
          f"n irrational values = {len(deg_ge2)}")

    # ---- 4. the law table ----
    print("\n=== THE LADDER TABLE (k = 1..4) ===")
    rows = {
        1: dict(kappa=13, Z='+1', clock_odd=1, clock_even=None, content='degenerate (dim 1)'),
        2: dict(kappa=14, Z='+1', clock_odd=4, clock_even=ladder[2], content='Z/7 sine kernel (7 | 14 split)'),
        3: dict(kappa=15, Z='+1', clock_odd=60, clock_even=ladder[3], content='golden octic, Q(sqrt5) (5 | 15 inert)'),
        4: dict(kappa=16, Z='0 (exact)', clock_odd=12, clock_even=ladder[4],
                content='Q(sqrt2) import + thirds (2 inert; dyadic)'),
    }
    for k, r in rows.items():
        print(f"  k={k}  kappa={r['kappa']}  Z={r['Z']}  clock(odd)={r['clock_odd']}  "
              f"clock(even)={r['clock_even']}  content: {r['content']}")
    print("\nPisano anchors: level2 ord4 <-> N=3 (unique <=200); level3 ord60 <-> N in {30,...};"
          f"\n  level4 ord12 <-> N in {[N for N in range(2,201) if fib_order(N)==12]} (includes kappa=16)")


if __name__ == '__main__':
    main()
