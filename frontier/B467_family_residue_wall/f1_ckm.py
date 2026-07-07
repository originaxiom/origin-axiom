#!/usr/bin/env python3
"""B467 F1 — the family-ratio value scan vs CKM, per prereg (null-calibrated).

Killed-trap flags binding: B428 (3 = generations), HELD(value-matching) per B322/B398.
The deliverable is a QUANTIFIED look-elsewhere verdict. Nothing fires from this script.

Also the H112 fold-in: the exact family table tr(A_m A_n) with the candidate identity
tr = (mn+1)^2 + m^2 + n^2 + 1, read against the (1,2) coincidence tr = 15 = seam level.
"""
import math
import random
import sys

SQRT = math.sqrt


def alpha(m):
    return (m + SQRT(m * m + 4)) / 2


# fixed by prereg
TARGETS = {
    'sin_th12 (Cabibbo)': 0.2250,
    'sin_th23': 0.0418,
    'sin_th13': 0.0037,
    'delta_CP (rad)': 1.144,
}
TOL = 1e-3

BASE_FUNCS = [
    ('x', lambda x: x), ('x^2', lambda x: x * x), ('x^3', lambda x: x ** 3),
    ('sqrt(x)', lambda x: SQRT(x) if x > 0 else float('nan')),
    ('1/x', lambda x: 1 / x if x else float('nan')),
    ('x/(1+x)', lambda x: x / (1 + x)),
    ('(1-x)/(1+x)', lambda x: (1 - x) / (1 + x)),
    ('1-x', lambda x: 1 - x),
    ('log(x)', lambda x: math.log(x) if x > 0 else float('nan')),
    ('arctan(x)', math.atan),
    ('x/pi', lambda x: x / math.pi),
    ('x*pi/4', lambda x: x * math.pi / 4),
]


def inputs_from(r12, r23, r13):
    return {
        'r12': r12, 'r23': r23, 'r13': r13,
        'r12/r23': r12 / r23, 'r12*r23': r12 * r23, 'r12-r23': r12 - r23,
    }


def scan(vals):
    """all (input, f) and one composition level (f2 o f1); returns {expr: value}."""
    out = {}
    for iname, x in vals.items():
        for fn, f in BASE_FUNCS:
            v = f(x)
            if v == v and abs(v) < 1e6:
                out[f"{fn}[{iname}]"] = v
                for gn, g in BASE_FUNCS:
                    w = g(v)
                    if w == w and abs(w) < 1e6:
                        out[f"{gn}[{fn}[{iname}]]"] = w
    return out


def hits(pool, target):
    return [(e, v) for e, v in pool.items()
            if v != 0 and abs(v - target) / abs(target) < TOL]


def main():
    a1, a2, a3 = alpha(1), alpha(2), alpha(3)
    r12, r23, r13 = a1 / a2, a2 / a3, a1 / a3
    print(f"exact ratios: r12 = {r12:.6f}, r23 = {r23:.6f}, r13 = {r13:.6f}")
    print("(Chat-1's decimals 0.6686 / 0.7346 were wrong — corrected)")
    pool = scan(inputs_from(r12, r23, r13))
    print(f"function-class size (fixed by prereg): {len(pool)} expressions\n")

    rng = random.Random(467)
    NNULL = 10_000
    print(f"{'target':<22} {'hits':>5} {'null mean':>10} {'null p':>8}   verdict")
    fired = False
    for tname, t in TARGETS.items():
        h = hits(pool, t)
        null_counts = []
        for _ in range(NNULL):
            u = [rng.uniform(0.55, 0.80), rng.uniform(0.65, 0.85), rng.uniform(0.40, 0.60)]
            null_counts.append(len(hits(scan(inputs_from(*u)), t)))
        mean = sum(null_counts) / NNULL
        pge = sum(1 for c in null_counts if c >= len(h)) / NNULL
        verdict = "LAUNDERS (look-elsewhere)" if pge >= 0.01 or not h else "ESCALATE per B398"
        if h and pge < 0.01:
            fired = True
        print(f"{tname:<22} {len(h):>5} {mean:>10.2f} {pge:>8.4f}   {verdict}")
        for e, v in h[:3]:
            print(f"    e.g. {e} = {v:.6f}")

    print("\n== H112 fold-in: the family table tr(A_m A_n) ==")
    def Amat(m):
        return [[m * m + 1, m], [m, 1]]
    def tr_prod(m, n):
        A, B = Amat(m), Amat(n)
        return A[0][0] * B[0][0] + A[0][1] * B[1][0] + A[1][0] * B[0][1] + A[1][1] * B[1][1]
    ident_ok = True
    for m in range(1, 7):
        row = []
        for n in range(m, 7):
            t = tr_prod(m, n)
            cand = (m * n + 1) ** 2 + m * m + n * n + 1
            ident_ok &= (t == cand)
            row.append(f"({m},{n})={t}")
        print("  " + "  ".join(row))
    print(f"identity tr(A_mA_n) = (mn+1)^2 + m^2 + n^2 + 1: {'HOLDS' if ident_ok else 'FAILS'}")
    print("(1,2) = 15 = the pair-seam level; (1,3) = 27, (2,3) = 63, (1,4) = 43 ... — "
          "the naive 'tr = conductor of the pair compositum' law is refuted by (1,3): "
          "cond(Q(sqrt5)*Q(sqrt13)) = 65 != 27. H112 updated with the table.")
    print("\nF1 VERDICT: " + ("ESCALATION REQUIRED" if fired else
          "no target survives the null — the scan LAUNDERS (look-elsewhere quantified)"))
    sys.exit(0)


if __name__ == '__main__':
    main()
