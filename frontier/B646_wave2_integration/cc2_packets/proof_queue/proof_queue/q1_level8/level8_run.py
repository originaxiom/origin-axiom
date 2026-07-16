"""Q1 — E6 level-8 (kappa=20) run, sealed per PREREG_Q1.md. Blind bank, then certify.
Order: (0) banked-rung gates k=1..7; (1) k=8 gate battery; (2) BLIND BANK;
(3) certificates (exact-Z mod Phi_240, Tr(Theta rho), ord at dps 50, minpolys, even).
Diagonal-aware mp block build (T is diagonal — no full N^3 mp products)."""
import json
import sys
sys.path.insert(0, '/Users/dri/oa-seat-cc2/seat-work/level_ladder_campaign/scripts')

import mpmath as mp
import numpy as np
import sympy as sp

from engine import Level, weyl_group
from p2_certify import exact_Z, mp_even_block, minpolys, eig_order
from p3_verdict import exact_trace_theta_rho, block_magnitudes

mp.mp.dps = 50
OUT = '/Users/dri/oa-seat-cc2/seat-work/proof_queue/q1_level8/outputs'


def mp_blocks_diagaware(L, dps=50):
    """S_odd, B_odd at dps, exploiting diagonal T: rho_ab = t_a^2 * S_ab * t_b."""
    mp.mp.dps = dps
    S = L.S_mp(dps)
    t = [mp.e ** (2j * mp.pi * int(e) / (12 * L.K)) for e in L.T_expo]
    n = len(L.pairs)
    s2 = 1 / mp.sqrt(2)
    S_odd = mp.matrix(n, n)
    B_odd = mp.matrix(n, n)
    for i, (a, b) in enumerate(L.pairs):
        for j, (c, d) in enumerate(L.pairs):
            so = (S[a, c] - S[a, d] - S[b, c] + S[b, d]) / 2
            bo = (t[a] * t[a] * S[a, c] * t[c] - t[a] * t[a] * S[a, d] * t[d]
                  - t[b] * t[b] * S[b, c] * t[c] + t[b] * t[b] * S[b, d] * t[d]) / 2
            S_odd[i, j] = so
            B_odd[i, j] = bo
    return S_odd, B_odd


def main():
    W, eps = weyl_group()
    print("=== (0) banked-rung gates k=1..7 ===", flush=True)
    banked = {1: (3, 1, 1.0, 1), 2: (9, 3, 1.0, 4), 3: (20, 8, 1.0, 60),
              4: (42, 17, 0.0, 12), 5: (78, 34, 1.0, 36), 6: (139, 61, 1.0, 18),
              7: (231, 105, 2.0, 36)}
    for k, (Nk, dk, Zk, ok) in banked.items():
        L = Level(k, W, eps)
        rep, okg, S, T, rho = L.run_gates()
        assert okg, f"gate failure k={k}"
        out, S_odd, B_odd = L.readouts(S, rho)
        assert out['N'] == Nk and out['dim_odd'] == dk
        assert abs(out['Z'][0] - Zk) < 1e-8 and abs(out['Z'][1]) < 1e-8
        assert out['order_float'] == ok
        print(f"  k={k}: reproduced (N={Nk}, dim_odd={dk}, Z={Zk}, ord={ok})", flush=True)

    print("\n=== (1) LEVEL 8 build + gates ===", flush=True)
    L8 = Level(8, W, eps)
    assert L8.k == 8 and L8.K == 20, "runner level check (the L6 lesson)"
    rep, okg, S, T, rho = L8.run_gates()
    for kk, v in rep.items():
        print(f"  gate {kk}: {v:.3e}" if isinstance(v, float) else f"  gate {kk}: {v}",
              flush=True)
    assert okg, "GATE FAILURE at level 8 — HARD STOP"

    print("\n=== (2) BLIND BANK ===", flush=True)
    out, S_odd_f, B_odd_f = L8.readouts(S, rho)
    np.savez(f'{OUT}/level8_blocks.npz', S_odd=S_odd_f, B_odd=B_odd_f,
             counts=L8.counts, T_expo=L8.T_expo)
    with open(f'{OUT}/level8_readouts.json', 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != 'ws_2K'}, indent=1),
          flush=True)
    print("BANKED level8_readouts.json (+npz) before comparison.", flush=True)

    print("\n=== (3) certificates ===", flush=True)
    red, num = exact_Z(L8)
    print(f"exact Z8 (unnormalized, mod Phi_240): zero-poly = {red.is_zero}; "
          f"numeric ~ {mp.nstr(num, 12)}", flush=True)
    zt, _, ztnum = exact_trace_theta_rho(L8)
    print(f"exact Tr(Theta rho): zero-poly = {zt}; numeric ~ {mp.nstr(ztnum, 12)}",
          flush=True)

    S_odd, B_odd = mp_blocks_diagaware(L8, dps=50)
    o_odd, dev_o, props_o = eig_order(B_odd, dps=50)
    print(f"ord(B_odd) = {o_odd} (dev {dev_o if dev_o is None else f'{dev_o:.1e}'}; "
          f"proper divisors { {d: f'{v:.1e}' for d, v in (props_o or {}).items()} })",
          flush=True)
    print(f"P-Q1-b check: divides 60 = ord(A1 mod 60): "
          f"{o_odd is not None and 60 % o_odd == 0}; equality: {o_odd == 60}", flush=True)

    ws = block_magnitudes(S_odd, L8.K)
    print(f"\nodd block: {len(ws)} distinct magnitudes, scale 2K={2 * L8.K}", flush=True)
    mps_ = minpolys(ws)
    sqrt5 = False
    other_import = []
    for w, coeffs, disc, primes in mps_:
        if coeffs is None:
            print(f"  w = {mp.nstr(mp.mpf(w), 25)}: UNIDENTIFIED <= deg16/1e14", flush=True)
            continue
        fac = sp.factorint(abs(int(disc))) if disc else {}
        if len(coeffs) == 3:
            for p, e in fac.items():
                if p >= 5 and e % 2 == 1:
                    (sqrt5 := True) if p == 5 else other_import.append(p)
        print(f"  minpoly {coeffs}  disc {dict(fac)}", flush=True)
    print(f"\nP-Q1-c: sqrt5 import flag = {sqrt5}; other sqrt-p (p>=7, would REFUTE "
          f"typing): {sorted(set(other_import)) or 'none'}", flush=True)

    S_even, B_even = mp_even_block(L8, dps=50)
    o_even, dev_e, _ = eig_order(B_even, dps=50)
    tr_o = mp.fsum(B_odd[i, i] for i in range(B_odd.rows))
    tr_e = mp.fsum(B_even[i, i] for i in range(B_even.rows))
    print(f"\neven control: ord(B_even) = {o_even}; tr_odd = {mp.nstr(tr_o, 15)}; "
          f"tr_even = {mp.nstr(tr_e, 15)}", flush=True)
    print("\nP-Q1-a check: Z8 = tr_odd + tr_even vs sealed +1 "
          f"= {mp.nstr(tr_o + tr_e, 15)}", flush=True)


if __name__ == '__main__':
    main()
