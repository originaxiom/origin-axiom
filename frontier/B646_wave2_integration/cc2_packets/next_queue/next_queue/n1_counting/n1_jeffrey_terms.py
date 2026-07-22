"""N1-D2: the Jeffrey Prop-4.5 pipeline instrumented PER WEYL CLASS, r = 13..19.
Adapted verbatim from level_ladder_campaign/scripts/jeffrey_run.py (banked pipeline);
changes: absolute import path, RS extended through 19, per-bucket contributions
dumped to jeffrey_terms.json. Gates: totals at r=13..17 must reproduce the banked
pattern (equal units at 13,14,15,17 magnitude; zero at 16); r=18,19 are NEW —
sealed expectation (prereg aa47092d): |Z_J(18)| = unit, |Z_J(19)| = 2 x unit."""
import itertools, json, sys
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp

sys.path.insert(0, '<cc2-seat>/seat-work/level_ladder_campaign/scripts')
from engine import weyl_group, C6

P_WORD = 3
RS = (13, 14, 15, 16, 17, 18, 19)
OUTDIR = '<cc2-seat>/seat-work/next_queue/n1_counting'


def hnf_column(B):
    from sympy.matrices.normalforms import hermite_normal_form
    M = sp.Matrix(B.tolist())
    H = hermite_normal_form(M)
    return np.array(H.tolist(), dtype=np.int64)


def gauss_sum(B, r):
    Bs = sp.Matrix(B.tolist())
    det = int(Bs.det())
    ad = abs(det)
    Binv = Bs.inv()
    M = sp.Matrix(C6.tolist()) * Binv
    H = hnf_column(B)
    diag = [int(H[i, i]) for i in range(6)]
    assert np.prod(diag) == ad, (diag, ad)
    Mf = np.array([[Fraction(M[i, j]) for j in range(6)] for i in range(6)])
    total = 0j
    for x in itertools.product(*[range(d) for d in diag]):
        mu = np.array(x, dtype=object)
        q = Fraction(0)
        for i in range(6):
            if mu[i]:
                for j in range(6):
                    if mu[j]:
                        q += mu[i] * Mf[i, j] * mu[j]
        e = (r * q) % 2
        total += complex(mp.e ** (-1j * mp.pi * mp.mpf(e.numerator) / e.denominator))
    return total, ad


def main():
    mp.mp.dps = 30
    W, eps = weyl_group()
    print(f"|W| = {len(W)}", flush=True)
    buckets = {}
    for idx in range(len(W)):
        w = W[idx]
        winv = np.rint(np.linalg.inv(w)).astype(np.int64)
        assert (w @ winv == np.eye(6, dtype=np.int64)).all()
        B = P_WORD * np.eye(6, dtype=np.int64) - w - winv
        cp = tuple(np.rint(np.poly(w.astype(float))).astype(np.int64))
        spec = tuple(sorted(np.linalg.eigvals(B.astype(float)).real.round(6)))
        key = (cp, spec)
        buckets.setdefault(key, []).append((idx, B, int(eps[idx])))
    print(f"buckets: {len(buckets)}", flush=True)

    results = {r: 0j for r in RS}
    rows = []
    for bi, (key, members) in enumerate(sorted(buckets.items(), key=lambda kv: -len(kv[1]))):
        idx0, B0, s0 = members[0]
        assert all(s == s0 for _, _, s in members)
        reps = members[:2] if len(members) > 1 else members[:1]
        row = {"bucket": bi, "charpoly": [int(c) for c in key[0]],
               "size": len(members), "sign": s0, "absdetB": None, "contrib": {}}
        for r in RS:
            vals = []
            for idx, B, s in reps:
                g, ad = gauss_sum(B, r)
                vals.append(g)
            assert all(abs(v - vals[0]) < 1e-7 * max(1, abs(vals[0])) or
                       abs(v - vals[0]) < 1e-6 for v in vals), f"not class fn r={r}: {key}"
            row["absdetB"] = ad
            c = len(members) * s0 * vals[0] / np.sqrt(ad)
            results[r] += c
            row["contrib"][str(r)] = [c.real, c.imag]
        rows.append(row)
        if bi % 5 == 0:
            print(f"  bucket {bi + 1}/{len(buckets)} size {len(members)} "
                  f"|detB| {row['absdetB']} done", flush=True)

    print("\n==== totals Z_J(r) ====", flush=True)
    zs = {}
    for r in RS:
        z = results[r] / len(W)
        zs[r] = z
        print(f"  r = {r}: {z.real:+.10f} {z.imag:+.10f}i  |Z_J| = {abs(z):.10f}", flush=True)
    unit = abs(zs[13])
    print("\nGATES: zero@16:", abs(zs[16]) < 1e-7,
          " units@13,14,15,17:", [round(abs(zs[r]) / unit, 8) for r in (14, 15, 17)], flush=True)
    print("NEW r=18 ratio:", round(abs(zs[18]) / unit, 8),
          " r=19 ratio (sealed expectation 2):", round(abs(zs[19]) / unit, 8), flush=True)
    with open(f"{OUTDIR}/jeffrey_terms.json", "w") as f:
        json.dump({"totals": {str(r): [zs[r].real, zs[r].imag] for r in RS},
                   "unit": unit, "rows": rows}, f, indent=1)
    print("DONE — jeffrey_terms.json written", flush=True)


if __name__ == '__main__':
    main()
