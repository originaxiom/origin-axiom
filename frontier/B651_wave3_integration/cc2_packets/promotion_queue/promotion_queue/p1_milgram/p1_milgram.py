"""P1 — exact algebraic certification of the sector sums (the generic-rung law's
promotion step). Per class: G_w(r) computed as an exact integer cyclotomic vector,
identified as sqrt|A| * zeta_8^j (Milgram), at r = 13 ((13|5) = -1) and r = 29
((29|5) = +1). Then the totals and sector sums are exact Q(zeta_8) arithmetic.
Technique: the banked exact-Z certificate style (integer vectors mod Phi_N)."""
import json, sys
from fractions import Fraction
from math import gcd
sys.path.insert(0, '<seat-workdir>/seat-work/next_queue/n1_counting')
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
ordered = sorted(buckets.items(), key=lambda kv: -len(kv[1]))

x = sp.symbols('x')

def cyc_reduce(vec_dict, N):
    """integer dict {exponent mod N: count} -> canonical coeff tuple mod Phi_N"""
    coeffs = [0] * N
    for e, c in vec_dict.items():
        coeffs[e % N] += c
    p = sp.Poly(list(reversed(coeffs)), x, domain='QQ')
    rem = p.rem(sp.Poly(sp.cyclotomic_poly(N, x), x))
    return rem

def gauss_exact(B, r):
    """G_w(r) as (Poly mod Phi_N, N): sum of zeta_{2b}^{-a} over cosets."""
    Bs = sp.Matrix(B.tolist())
    ad = abs(int(Bs.det()))
    M = sp.Matrix(J.C6.tolist()) * Bs.inv()
    H = J.hnf_column(B)
    diag = [int(H[i, i]) for i in range(6)]
    Mf = [[Fraction(M[i, j]) for j in range(6)] for i in range(6)]
    import itertools
    terms = {}
    dens = set()
    raw = []
    for xx in itertools.product(*[range(d) for d in diag]):
        q = Fraction(0)
        for i in range(6):
            if xx[i]:
                for jj in range(6):
                    if xx[jj]:
                        q += xx[i] * Mf[i][jj] * xx[jj]
        e = (r * q) % 2
        raw.append(e)
        dens.add(e.denominator)
    N = 2 * np.lcm.reduce([int(d) for d in dens]) if dens else 2
    N = int(N)
    for e in raw:
        expo = int(-(e * N // 2)) % N          # e^{-i pi e} = zeta_N^{-e*N/2}
        terms[expo] = terms.get(expo, 0) + 1
    return cyc_reduce(terms, N), N, ad

def embed(polyrem, N, Np):
    """coeff poly over zeta_N -> dict over zeta_Np (N | Np)"""
    k = Np // N
    out = {}
    cs = list(reversed(polyrem.all_coeffs()))
    for e, c in enumerate(cs):
        if c:
            out[(e * k) % Np] = out.get((e * k) % Np, 0) + c
    return out

def poly_of(dic, Np):
    coeffs = [0] * Np
    for e, c in dic.items():
        coeffs[e % Np] += c
    p = sp.Poly(list(reversed(coeffs)), x, domain='QQ')
    return p.rem(sp.Poly(sp.cyclotomic_poly(Np, x), x))

def sqrt5_dict(Np):
    """sqrt5 = sum_t (t|5) zeta_5^t over Q(zeta_5) c Q(zeta_Np) (5 | Np)"""
    k = Np // 5
    d = {}
    for t in (1, 2, 3, 4):
        leg = 1 if t in (1, 4) else -1
        d[(t * k) % Np] = leg
    return d

def mul_dicts(d1, d2, Np):
    out = {}
    for e1, c1 in d1.items():
        for e2, c2 in d2.items():
            out[(e1 + e2) % Np] = out.get((e1 + e2) % Np, 0) + c1 * c2
    return out

def vp(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

results = []
for bi, (key, members) in enumerate(ordered):
    idx0, B0, sgn = members[0]
    row = {"bucket": bi, "size": len(members), "sign": sgn}
    for r in (13, 29):
        Gp, N, ad = gauss_exact(B0, r)
        # sqrt|A| = m * 5^(v5/2): m integer part
        m = 1
        rest = ad
        for p in (2, 3, 5, 7, 11, 19):
            v = vp(ad, p)
            m *= p ** (v // 2)
            if v % 2 and p != 5:
                raise RuntimeError(f"odd exponent at p={p} bucket {bi}")
        has5 = vp(ad, 5) % 2 == 1
        Np = int(np.lcm(np.lcm(N, 8), 40 if has5 else 8))
        Gd = embed(Gp, N, Np)
        Gcan = poly_of(Gd, Np)
        ident = None
        for j in range(8):
            base = {(j * (Np // 8)) % Np: m}
            cand = mul_dicts(base, sqrt5_dict(Np), Np) if has5 else base
            if poly_of(cand, Np) == Gcan:
                ident = j
                break
        assert ident is not None, f"bucket {bi} r={r}: no candidate matched (ad={ad}, N={N})"
        row[f"j_{r}"] = ident
        row[f"has5"] = has5
        row[f"absdet"] = ad
    results.append(row)
    print(f"b{bi:2d} sz{row['size']:5d} sgn{sgn:+d} det{row['absdet']:5d} "
          f"sqrt5={'Y' if row['has5'] else 'n'}  zeta8-exponents: "
          f"r13 -> {row['j_13']}, r29 -> {row['j_29']}", flush=True)

# exact Q(zeta_8) totals: term = sign*size/|W| * zeta_8^j  (gamma = G/sqrt|A| = zeta_8^j)
Wn = 51840
def total(rkey):
    acc = [Fraction(0)] * 8
    for row in results:
        acc[row[rkey]] += Fraction(row["sign"] * row["size"], Wn)
    return acc

def z8_value(acc):
    # zeta_8^j coordinates -> reduce: zeta_8^4 = -1 etc.; return as (a + b*z + c*z^2 + d*z^3)
    red = [acc[k] - acc[k + 4] for k in range(4)]
    return red

t13, t29 = z8_value(total("j_13")), z8_value(total("j_29"))
print(f"\nEXACT total at r=13 (Q(zeta8) coords 1,z,z2,z3): {[str(c) for c in t13]}  "
      f"(theorem needs [1,0,0,0])", flush=True)
print(f"EXACT total at r=29: {[str(c) for c in t29]}  (theorem needs [0,0,0,0])", flush=True)

# sector sums at r=13
triv = [Fraction(0)] * 8
chi5 = [Fraction(0)] * 8
for row in results:
    (chi5 if row["has5"] else triv)[row["j_13"]] += Fraction(row["sign"] * row["size"], Wn)
print(f"trivial sector (r=13): {[str(c) for c in z8_value(triv)]}  (needs [1/2,0,0,0])",
      flush=True)
print(f"chi5 sector    (r=13): {[str(c) for c in z8_value(chi5)]}  (needs [1/2,0,0,0])",
      flush=True)

# per-class twist ratio certificate
flips = all((row["j_29"] - row["j_13"]) % 8 == (4 if row["has5"] else 0) for row in results)
print(f"\nTWIST CERTIFICATE: gamma(29)/gamma(13) = -1 exactly on chi5 classes and +1 "
      f"on trivial classes (as zeta8-exponent shift 4/0): {flips}", flush=True)
with open('<seat-workdir>/seat-work/promotion_queue/p1_milgram/p1_certificates.json',
          'w') as f:
    json.dump(results, f, indent=1)
print("DONE — p1_certificates.json", flush=True)
