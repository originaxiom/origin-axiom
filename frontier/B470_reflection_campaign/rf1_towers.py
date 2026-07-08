#!/usr/bin/env python3
"""B470 RF0+RF1 — both towers under the prereg: the LETTER tower (a->R, b->L) and
the BODY chain (a->RL, b->RRLL), n = 2..10: vol, CS, H1, the exact reverse+swap
amphichirality criterion. Plus the Gieseking descent quick table and chain bodies s4-s6."""
import snappy, math

def tower_words(n, A, B):
    s = {0: "b", 1: "a"}
    for k in range(2, n+1): s[k] = s[k-1] + s[k-2]
    return {k: "".join(A if c == "a" else B for c in s[k]) for k in s}

def revswap(w):
    return "".join("R" if c == "L" else "L" for c in reversed(w))

def cyc_eq(w1, w2):
    return len(w1) == len(w2) and w2 in (w1 + w1)

def row(name, w):
    M = snappy.Manifold("b++" + w)
    try: vol = float(M.volume())
    except Exception: vol = float('nan')
    try: cs = float(M.chern_simons())
    except Exception: cs = None
    amph_word = cyc_eq(w, revswap(w))
    css = f"{cs:+.6f}" if cs is not None else "n/a"
    print(f"  {name:<8} len={len(w):>3} vol={vol:>12.7f} CS={css:>10} H1={M.homology()}  revswap-amph={amph_word}", flush=True)
    return vol, cs, amph_word

print("== RF0 gate + RF1 LETTER tower (a->R, b->L) ==", flush=True)
W = tower_words(10, "R", "L")
for n in range(2, 11): row(f"L n={n}", W[n])
print("== RF1 BODY chain (a->RL, b->RRLL) ==", flush=True)
WB = tower_words(8, "RL", "RRLL")
for n in range(2, 9): row(f"B n={n}", WB[n])
print("== Gieseking descent (Phase-2b CC quick table) ==", flush=True)
G = snappy.NonorientableCuspedCensus[0]
M4 = snappy.Manifold('4_1')
print(f"  m000: vol={float(G.volume()):.9f} (= vol(4_1)/2: {abs(float(G.volume())-float(M4.volume())/2) < 1e-9}) H1={G.homology()}", flush=True)
print(f"  4_1 : vol={float(M4.volume()):.9f} H1={M4.homology()}  descent: vol EVEN(ratio-2), H1 differs", flush=True)
print("DONE", flush=True)
