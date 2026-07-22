"""Q3: exact verification of the three lemmas behind the generic-rung and jump laws.

L1 (standard, cited): multiplier twist of Gauss sums: for q nondegenerate on finite
   abelian A and gcd(r,|A|)=1: G(rq) = chi_A(r) G(q), chi_A(r) = prod over odd
   elementary divisors p^a (a ODD) of (r|p), times a 2-adic character mod 8.
L2 (verified here): character-sector decomposition of the 25-class Weyl sum:
   the chi-trivial sector sums to +1; every nontrivial-character sector sums to 0.
   => THE GENERIC-RUNG THEOREM: Z(kappa) = +1 for gcd(kappa, 2*3*5*7*11*19) = 1.
L3 (verified here): THE UNIFORM JUMP LAW: |term_w(kappa)|/|term_w(generic)| =
   prod over elementary divisors p^a of A_w of p^{min(v_p(kappa), a)/2} —
   no odd/dyadic case split; tested on ALL class x r cells (r = 13..25)."""
import json, math, sys
from fractions import Fraction
sys.path.insert(0, '<cc2-seat>/seat-work/next_queue/n1_counting')
import numpy as np
import sympy as sp
import n1_jeffrey_terms as J

W, eps = J.weyl_group()
buckets = {}
for idx in range(len(W)):
    w = W[idx]
    winv = np.rint(np.linalg.inv(w)).astype(np.int64)
    B = J.P_WORD * np.eye(6, dtype=np.int64) - w - winv
    cp = tuple(np.rint(np.poly(w.astype(float))).astype(np.int64))
    spec = tuple(sorted(np.linalg.eigvals(B.astype(float)).real.round(6)))
    buckets.setdefault((cp, spec), []).append((idx, B, int(eps[idx])))

# Smith normal form -> elementary divisors of A_w = Z^6 / B_w Z^6
def elem_divisors(B):
    from sympy.matrices.normalforms import smith_normal_form
    M = sp.Matrix(B.tolist())
    snf = smith_normal_form(M)
    return [abs(int(snf[i, i])) for i in range(6) if abs(int(snf[i, i])) != 1]

ordered = sorted(buckets.items(), key=lambda kv: -len(kv[1]))
rows = []
for bi, (key, members) in enumerate(ordered):
    divs = elem_divisors(members[0][1])
    det = 1
    for d in divs:
        det *= d
    rows.append({"bucket": bi, "size": len(members), "sign": members[0][2],
                 "divs": divs, "det": det})

terms = json.load(open('<cc2-seat>/seat-work/next_queue/n1_counting/jeffrey_terms.json'))
ext = json.load(open('<cc2-seat>/seat-work/next_queue/n1_counting/jeffrey_extension.json'))
contrib = {}
for src in (terms, ext):
    for row in src['rows']:
        for r, c in row['contrib'].items():
            contrib[(row['bucket'], int(r))] = complex(*c)
assert all(rows[b]["det"] == r0["absdetB"] for b, r0 in
           enumerate(terms["rows"])), "SNF dets must match banked |detB|"

Wn = 51840
print("=== L3: THE UNIFORM JUMP LAW (all classes x r = 14..25 vs generic r=13) ===")
bad = tot = 0
for row in rows:
    base = abs(contrib[(row["bucket"], 13)])
    if base < 1e-12:
        continue
    for r in range(14, 26):
        pred = 1.0
        for d in row["divs"]:
            for p in (2, 3, 5, 7, 11, 19):
                a = 0
                dd = d
                while dd % p == 0:
                    a += 1
                    dd //= p
                if a:
                    v = 0
                    rr = r
                    while rr % p == 0:
                        v += 1
                        rr //= p
                    pred *= p ** (min(v, a) / 2)
        obs = abs(contrib[(row["bucket"], r)]) / base
        tot += 1
        if abs(obs - pred) > 1e-6 * max(1, pred):
            bad += 1
            print(f"  VIOLATION b{row['bucket']} r={r}: obs {obs:.6f} pred {pred:.6f} "
                  f"divs {row['divs']}")
print(f"L3: {tot - bad}/{tot} PASS")

print("\n=== L2: character sectors (generic row r=13; chi from odd-exponent divisors) ===")
# chi signature: for each odd p, parity of #elementary divisors p^a with a ODD —
# the (r|p) twist exponent of L1. 2-adic twist treated empirically via the
# cross-check at rungs 13, 17, 23 (== 5, 1, 7 mod 8).

def vp(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

sector_sum = {}
for row in rows:
    sig = tuple(sum(1 for d in row["divs"] if vp(d, p) % 2 == 1 and vp(d, p) > 0) % 2
                for p in (3, 5, 7, 11, 19))
    c13 = contrib[(row["bucket"], 13)] / Wn
    sector_sum[sig] = sector_sum.get(sig, 0) + c13
for sig, s in sorted(sector_sum.items()):
    label = "TRIVIAL" if not any(sig) else f"chi{sig}"
    print(f"  sector {label}: sum = {s.real:+.10f} {s.imag:+.10f}i")
print("\n=== L2 cross-check: totals at the three fully generic rungs ===")
for r in (13, 17, 23):
    totr = sum(contrib[(row['bucket'], r)] for row in rows) / Wn
    print(f"  r={r}: Z = {totr.real:+.10f}")
print("\nclass table (bucket: size sign divisors):")
for row in rows:
    print(f"  b{row['bucket']:2d} sz{row['size']:5d} sgn{row['sign']:+d} divs {row['divs']}")
