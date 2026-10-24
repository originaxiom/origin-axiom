#!/usr/bin/env python3
"""e17 (data-free; P-139, input to main's P-327): the one-loop cusp coefficient of the record's contents on every one of
B1713's 266 lines, in main's own conventions (B1686's closed-form cells, `frontier/B1686_w60_w62_on_main/verification/
main_w62.py`, read from main with git show; B1704's criterion: a content can hold tau off the cusp only if its total cusp
coefficient is negative).  Labelled exploration: no data enters; committed before its run, output committed before read.

The conventions copied from B1686 (units of zeta(6) per unit weight; bosons positive, a Weyl fermion -2):
  S_c(tau, p) = sum' cos 2pi(m p1 + n p2) y^3 / |m + n tau|^6, whose cusp coefficient (y -> infinity, n = 0) is
  kappa(p1) = 2 sum_{m>=1} cos(2 pi m p1) / m^6 / zeta(6) = 84 B_6({p1})  (B_6 the Bernoulli polynomial);
  the Higgs: three complex copies at the parity characteristics p + 3w, p in {(1/2,0), (0,1/2), (1/2,1/2)} (B1686's
  copies(w)), weight 2 each;
  the matter: 45 Weyl fermions in rho_Q, each -2 x the comb, comb = sum_{a,b<2} (-1/2) S_c((a/2,b/2)) + sum_{a,b<4} (1/4)
  S_c((a/4,b/4)), cusp coefficient k_rho = -31/512 (B1686); gauge 2 x 12 x 2; graviton (9/2) x 2.
The one addition (B1728's law): on the line w = alpha tau + b a field of charge q = 6Y is twisted by q w, so every
characteristic of its local system shifts by q w and its cusp coefficient by q alpha in the first component.  Charges
and counts per generation: Q 1 (6 Weyl), u^c -4 (3), d^c 2 (3), L -3 (2), e^c 6 (1); the Higgs 3.
Checks: (K1) kappa's closed form against the direct sum and against B1686's S_c at y = 8; (K2) the comb's cusp
coefficient equals kappa(1/4 + s) + kappa(3/4 + s) at s = 0, 0.1, 0.37 (S_c at y = 8); (K3) B1686's recorded totals on its
three half-period lines (9.574, 9.574, 1.699 for matter + Higgs; 5.449 matter alone; +48 gauge; +9 graviton).
    python3 -B e17_cusp_coefficients_on_lines.py      # writes e17_cusp_coefficients_on_lines_out.txt and .json"""
import json, math, pathlib, subprocess
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
out, res = [], {}
ZETA6 = math.pi ** 6 / 945


def B6(x):
    return x ** 6 - 3 * x ** 5 + 2.5 * x ** 4 - 0.5 * x ** 2 + 1 / 42


def kappa(x):                       # units of zeta(6) per unit weight
    return 84 * B6(float(x) % 1.0)


def S_c(tau, p, M=60):              # B1686's S_c, verbatim in substance
    m, n = np.meshgrid(np.arange(-M, M + 1), np.arange(-M, M + 1), indexing="ij"); m = m.ravel(); n = n.ravel()
    nz = (m != 0) | (n != 0); m, n = m[nz], n[nz]
    return float(np.sum(np.cos(2 * np.pi * (m * p[0] + n * p[1])) * tau.imag ** 3 / np.abs(m + n * tau) ** 6))


# K1
mm = np.arange(1, 200001)
k1 = []
for x in (0.0, 0.5, 0.2, 0.05, 0.65, 0.3):
    direct = 2 * float(np.sum(np.cos(2 * np.pi * mm * x) / mm.astype(float) ** 6)) / ZETA6
    lat = S_c(complex(0, 8.0), (x, 0.17)) / 8.0 ** 3 / ZETA6
    k1.append((x, kappa(x), direct, lat))
out.append("K1 kappa(x): closed form, direct sum, B1686's S_c at y = 8 (second component 0.17): " +
           "; ".join(f"x={x}: {a:.6f}, {b:.6f}, {c:.6f}" for x, a, b, c in k1))


# K2
def comb_lattice(tau, s):
    return (sum(-0.5 * S_c(tau, (a / 2 + s, b / 2)) for a in range(2) for b in range(2)) +
            sum(0.25 * S_c(tau, (a / 4 + s, b / 4)) for a in range(4) for b in range(4)))


k2 = [(s, comb_lattice(complex(0, 8.0), (s)) / 8.0 ** 3 / ZETA6, kappa(0.25 + s) + kappa(0.75 + s)) for s in (0.0, 0.1, 0.37)]
out.append("K2 the comb's cusp coefficient, lattice at y = 8 against kappa(1/4+s) + kappa(3/4+s): " +
           "; ".join(f"s={s}: {a:.6f}, {b:.6f}" for s, a, b in k2) + f"; k_rho = -31/512 = {-31/512:.6f}")

FIELDS = [("Q", 1, 6), ("u^c", -4, 3), ("d^c", 2, 3), ("L", -3, 2), ("e^c", 6, 1)]
PAR = [(Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 2)), (Fr(1, 2), Fr(1, 2))]
GAUGE, GRAV = 2 * 12 * 2.0, 4.5 * 2.0


def matter(alpha):
    return sum(-2 * 3 * n * (kappa(0.25 + q * alpha) + kappa(0.75 + q * alpha)) for _, q, n in FIELDS)


def higgs(alpha):
    return sum(2 * kappa(p[0] + 3 * alpha) for p in PAR)


def totals(alpha):
    a = float(alpha); mt, h = matter(a), higgs(a)
    return {"(d) matter alone": mt, "(a) matter + Higgs": mt + h, "(b) + gauge": mt + h + GAUGE, "(c) + graviton": mt + h + GAUGE + GRAV}


# K3
k3 = {str(l): totals(l[0]) for l in ((Fr(1, 2), Fr(1, 2)), (Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 2)))}
out.append("K3 B1686's half-period lines (recorded: matter + Higgs 9.574, 9.574, 1.699; matter alone 5.449; +48; +9): " +
           "; ".join(f"{l}: " + ", ".join(f"{k} {v:.3f}" for k, v in t.items()) for l, t in k3.items()))


# the 266 lines
def _lines(lo, hi):
    seen, r = set(), []
    for N in range(lo, hi + 1):
        for j in range(N):
            for k in range(N):
                if math.gcd(math.gcd(j, k), N) != 1:
                    continue
                a, b = Fr(j, N), Fr(k, N); na, nb = (-a) % 1, (-b) % 1
                key = min((a, b), (na, nb))
                if key in seen:
                    continue
                seen.add(key); r.append((N, key[0], key[1]))
    return r


LINES = _lines(1, 7) + _lines(8, 12)
rows = []
for idx, (N, a, b) in enumerate(LINES):
    t = totals(a); rows.append({"index": idx, "order": N, "line": [str(a), str(b)], **t})
res["lines"] = rows
for key in ("(d) matter alone", "(a) matter + Higgs", "(b) + gauge", "(c) + graviton"):
    neg = [r for r in rows if r[key] < 0]
    out.append(f"lines with {key} negative: {len(neg)} of {len(rows)}; by order " +
               str(sorted({(r['order'], sum(1 for q in neg if q['order'] == r['order'])) for r in neg})))
a25 = Fr(2, 5)
out.append("the alpha = 2/5 lines (orders 5 and 10; the value depends on alpha only): " +
           ", ".join(f"{k} {v:.4f}" for k, v in totals(a25).items()))
out.append("  per field at alpha = 2/5 (each Weyl fermion's -2 x comb, times its count over three generations): " +
           ", ".join(f"{nm} (q alpha = {Fr(q) * a25 % 1}): {-2 * 3 * n * (kappa(0.25 + q * 0.4) + kappa(0.75 + q * 0.4)):.4f}" for nm, q, n in FIELDS) +
           f"; the Higgs's copies at first components {[str((p[0] + 3 * a25) % 1) for p in PAR]}: {higgs(0.4):.4f}")
alphas = sorted({r["line"][0] for r in rows}, key=lambda s: Fr(s))
out.append("by alpha (matter alone, matter + Higgs): " + "; ".join(
    f"{al}: {totals(Fr(al))['(d) matter alone']:.3f}, {totals(Fr(al))['(a) matter + Higgs']:.3f}" for al in alphas))
mins = {k: min(totals(Fr(al))[k] for al in alphas) for k in ("(b) + gauge", "(c) + graviton")}
out.append(f"the smallest totals over every alpha with the gauge fields: {mins}")
res["checks"] = {"K1": k1, "K2": k2, "K3": k3}
(HERE / "e17_cusp_coefficients_on_lines_out.txt").write_text("\n".join(out) + "\n")
(HERE / "e17_cusp_coefficients_on_lines.json").write_text(json.dumps(res, indent=1))
print("written")
