#!/usr/bin/env python3
"""
F4 track-S verify: INDEPENDENT re-derivation of B649 stage 2b's headline
(S2b-G1: "both silver relators evaluate to I27 EXACTLY in GL27(L)") using
the persisted, hash-verified letters27_L.json, via sympy's algebraic
number field (own arithmetic backend, not cc's Fraction-vector quotient
ring in b649_stage2b.py). Also independently re-verifies S2b-G3
(tr27(mu) = tr27(lam) = 27 exactly).
"""
import json
import os
import time

import sympy
from sympy import QQ, I as sI, sqrt as sy_sqrt

SRC = "<seat-workdir>/origin-axiom/frontier/B649_silver_holonomy"
RESULTS = {}

s0 = sy_sqrt(4 + 4 * sy_sqrt(2))
K = QQ.algebraic_field(s0, sI)
ZERO = K.from_sympy(sympy.Integer(0))
ONE = K.from_sympy(sympy.Integer(1))
TWENTYSEVEN = K.from_sympy(sympy.Integer(27))

d27 = json.load(open(os.path.join(SRC, "letters27_L.json")))


def elt_from_coeffs(vec8):
    re_c, im_c = vec8[:4], vec8[4:]
    expr = sum(sympy.Rational(c) * s0 ** k for k, c in enumerate(re_c)) + \
        sI * sum(sympy.Rational(c) * s0 ** k for k, c in enumerate(im_c))
    return K.from_sympy(sympy.expand(expr))


def load_mat27(nm):
    return [[elt_from_coeffs(d27[nm][i][j]) for j in range(27)] for i in range(27)]


print("loading 6 lifted 27x27 letters into sympy algebraic field...", flush=True)
t0 = time.time()
LETS = {nm: load_mat27(nm) for nm in "abcABC"}
print(f"  loaded in {time.time()-t0:.1f}s", flush=True)


def mm27(A, B):
    n = 27
    Bt = list(zip(*B))
    out = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        nz = [(k, Ai[k]) for k in range(n) if Ai[k] != ZERO]
        for j in range(n):
            col = Bt[j]
            acc = ZERO
            for k, a in nz:
                b = col[k]
                if b != ZERO:
                    acc = acc + a * b
            out[i][j] = acc
    return out


def word27(w):
    m = None
    for ch in w:
        m = LETS[ch] if m is None else mm27(m, LETS[ch])
    return m


print("\n== independent S2b-G1 check (sympy algebraic field) ==", flush=True)
for rel in ("aBAbcc", "aaCbcB"):
    t0 = time.time()
    R = word27(rel)
    ok = all((R[i][j] == (ONE if i == j else ZERO)) for i in range(27) for j in range(27))
    dt = time.time() - t0
    print(f"  {rel}: = I27 exactly (sympy field): {ok}   ({dt:.1f}s)", flush=True)
    RESULTS[f"S2bG1_{rel}"] = bool(ok)

print("\n== independent S2b-G3 check (sympy algebraic field) ==", flush=True)
for w, nm in (("CCB", "mu"), ("caCA", "lam")):
    W = word27(w)
    t = ZERO
    for i in range(27):
        t = t + W[i][i]
    ok = (t == TWENTYSEVEN)
    print(f"  tr27({nm}={w}) = 27 exactly (sympy field): {ok}", flush=True)
    RESULTS[f"S2bG3_tr27_{nm}"] = bool(ok)

with open("<seat-workdir>/seat-work/finisher_queue/f4_receipt/stage2b_results.json", "w") as f:
    json.dump(RESULTS, f, indent=2)
print("\nWrote stage2b_results.json")
