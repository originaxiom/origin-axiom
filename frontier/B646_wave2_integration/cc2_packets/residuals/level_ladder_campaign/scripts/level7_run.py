"""Level-5 (kappa=17) run — sealed per PREREG_L7.md. Blind bank, then certify.

Order: (0) banked-rung gates k=1..4 (Z values + odd dims + orders via float);
(1) k=5 full gate battery; (2) BLIND BANK readouts; (3) certificates: exact-Z
(mod Phi_204), orders at dps50, magnitude minpolys w/ disc parity, even control.
"""
import json
import sys
sys.path.insert(0, 'scripts')

import mpmath as mp
import numpy as np
import sympy as sp

from engine import (Level, weyl_group, mp_odd_blocks, mp_certify_order, theta)
from p2_certify import exact_Z, mp_even_block, minpolys, eig_order, fib_order
from p3_verdict import exact_trace_theta_rho, block_magnitudes

mp.mp.dps = 50


def main():
    W, eps = weyl_group()
    print("=== (0) banked-rung gates k=1..4 ===", flush=True)
    banked = {1: (3, 1, 1.0, 1), 2: (9, 3, 1.0, 4), 3: (20, 8, 1.0, 60),
              4: (42, 17, 0.0, 12), 5: (78, 34, 1.0, 36), 6: (139, 61, 1.0, 18)}
    for k, (Nk, dk, Zk, ok) in banked.items():
        L = Level(k, W, eps)
        rep, okg, S, T, rho = L.run_gates()
        assert okg, f"gate failure k={k}"
        out, S_odd, B_odd = L.readouts(S, rho)
        assert out['N'] == Nk and out['dim_odd'] == dk
        assert abs(out['Z'][0] - Zk) < 1e-8 and abs(out['Z'][1]) < 1e-8
        assert out['order_float'] == ok
        print(f"  k={k}: reproduced (N={Nk}, dim_odd={dk}, Z={Zk}, ord={ok})", flush=True)

    print("\n=== (1) k=5 build + gates ===", flush=True)
    L5 = Level(7, W, eps)
    rep, okg, S, T, rho = L5.run_gates()
    for kk, v in rep.items():
        print(f"  gate {kk}: {v:.3e}" if isinstance(v, float) else f"  gate {kk}: {v}", flush=True)
    assert okg, "GATE FAILURE at level 5 — HARD STOP"

    print("\n=== (2) BLIND BANK ===", flush=True)
    out, S_odd_f, B_odd_f = L5.readouts(S, rho)
    np.savez('outputs/level7_blocks.npz', S_odd=S_odd_f, B_odd=B_odd_f,
             counts=L5.counts, T_expo=L5.T_expo)
    with open('outputs/level7_readouts.json', 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != 'ws_2K'}, indent=1), flush=True)
    print("BANKED outputs/level7_readouts.json (+npz) before comparison.", flush=True)

    print("\n=== (3) certificates ===", flush=True)
    red, num = exact_Z(L5)
    print(f"exact Z5 (unnormalized, mod Phi_204): zero-poly = {red.is_zero}; "
          f"numeric ~ {mp.nstr(num, 12)}", flush=True)
    zt, _, ztnum = exact_trace_theta_rho(L5)
    print(f"exact Tr(Theta rho): zero-poly = {zt}; numeric ~ {mp.nstr(ztnum, 12)}", flush=True)

    S_odd, B_odd, _ = mp_odd_blocks(L5, dps=50)
    o_odd, dev_o, props_o = eig_order(B_odd, dps=50)
    print(f"ord(B_odd) = {o_odd} (dev {dev_o if dev_o is None else f'{dev_o:.1e}'}; "
          f"proper divisors { {d: f'{v:.1e}' for d, v in (props_o or {}).items()} })", flush=True)
    print(f"clock check: divides 36 = ord(A1 mod 228): "
          f"{o_odd is not None and 36 % o_odd == 0}; equality: {o_odd == 36}", flush=True)

    ws = block_magnitudes(S_odd, L5.K)
    print(f"\nodd block: {len(ws)} distinct magnitudes w = 34|S_odd|^2-scale 2K={2*L5.K}", flush=True)
    mps_ = minpolys(ws)
    sqrt17 = False
    for w, coeffs, disc, primes in mps_:
        if coeffs is None:
            print(f"  w = {mp.nstr(mp.mpf(w), 25)}: UNIDENTIFIED <= deg16/1e14 "
                  f"(Bantay bound deg | 32; priced out)", flush=True)
            continue
        fac = sp.factorint(abs(int(disc))) if disc else {}
        odd17 = fac.get(17, 0) % 2 == 1
        if len(coeffs) == 3 and odd17:
            sqrt17 = True
        tag = "  <-- Q(sqrt17) QUADRATIC" if (len(coeffs) == 3 and odd17) else \
              ("  [17-odd-exp disc]" if odd17 else "")
        print(f"  minpoly {coeffs}  disc {dict(fac)}{tag}", flush=True)
    print(f"\nsqrt-p import scan (p>=5 would REFUTE the null-prediction): sqrt17-style flag = {sqrt17}", flush=True)

    S_even, B_even = mp_even_block(L5, dps=50)
    o_even, dev_e, _ = eig_order(B_even, dps=50)
    tr_o = mp.fsum(B_odd[i, i] for i in range(B_odd.rows))
    tr_e = mp.fsum(B_even[i, i] for i in range(B_even.rows))
    print(f"\neven control: ord(B_even) = {o_even}; tr_odd = {mp.nstr(tr_o, 15)}; "
          f"tr_even = {mp.nstr(tr_e, 15)}", flush=True)


if __name__ == '__main__':
    main()
