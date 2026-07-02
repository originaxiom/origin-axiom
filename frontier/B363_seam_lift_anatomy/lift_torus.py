"""B363 (L57 opener) -- the seam function on the lift torus.

Any lift of the pair observable differs from the canonical one by Heisenberg twists:
    W1~ = X^a Z^b W1_can,   W2~ = X^c Z^d W2_can,   (a,b,c,d) in (Z/15)^4.
The seam coefficient s becomes a FUNCTION on this lift torus. This scan maps its vanishing
locus -- the shape of the seam-bearing sector -- numerically (double precision suffices to
separate s = 0 from |s| >= 1/2880), via the 4-embedding Galois transport (numeric pipelines at
zeta -> zeta^g for g in Gal(Q(zeta60)/H) = {1,19,31,49}; eigenvalue labels transported k -> gk).

Aggregate observable per twist: S := sum over all projector pairs |s(a,b)|  (the total seam
content of the table). S = 0 <=> the whole table is seam-free at that twist.

Design notes:
- X = diag(zeta15^j), Z: e_j -> e_{j+1}; the canonical W's are B355's (T = e(x^2), S-kernel -2).
- For each Galois embedding g: rebuild T, S, X, Z with zeta -> zeta^g, twist, take eigenprojectors
  (numpy), form D(a,b) = table of tr(Par P Q); the H-average is (1/4) sum_g D_g with the PROJECTOR
  LABELS matched by transported eigenvalues (lambda -> lambda^g).
- s-extraction: for t_H in H: s = (t_H - tau5(t_H) - tau3(t_H) + tau15(t_H))/(4 sqrt(-15)) where
  tau5 flips sqrt5, tau3 flips sqrt(-3). Numerically: the four embeddings give exactly
  {t_H} once averaged -- instead we extract s directly: over the four Galois images of the RAW t,
  s = (1/4) * sum_g chi(g) t^(g) / sqrt(-15) with chi(g) = the character of Gal on sqrt(-15):
  sigma_g(sqrt(-15)) = chi(g) sqrt(-15). For g in {1,19,31,49} (fixing H) that's chi = 1 -- those
  give t_H. To READ s we need embeddings MOVING sqrt5 and sqrt(-3): use the full 8-element group
  Gal(Q(zeta60)/Q(sqrt-15))? Simpler: compute t_H (4-embedding average) as a COMPLEX NUMBER and
  solve the 4-dim real system t_H = p + q sqrt5 + r i sqrt3 + s i sqrt15 -- (Re, Im) give 2 eqs for
  4 unknowns... underdetermined numerically from ONE embedding of t_H. Fix: compute t_H under TWO
  different embeddings of H into C: the identity and one with sqrt5 -> -sqrt5 (g with chi5(g) = -1,
  e.g. g = 7: check 7 mod 5 QNR -> flips sqrt5; 7 mod 12? sqrt(-3) flip depends on g mod 3;
  chi_{-3}(7) = (7|3) = 1 -> fixes sqrt(-3)). Then:
      t_H^(1)  = p + q sqrt5 + r i sqrt3 + s i sqrt15
      t_H^(7)  = p - q sqrt5 + r i sqrt3 - s i sqrt15
  => s = Im(t_H^(1) - t_H^(7)) / (2 sqrt15),  q = Re(t_H^(1) - t_H^(7))/(2 sqrt5), etc.
  t_H^(7) is computed by running the whole averaged pipeline with zeta -> zeta^7 composed with the
  H-average set {7, 7*19, 7*31, 7*49} mod 60 = {7, 13, 37, 43}.
"""
import cmath
import json
import sys

import numpy as np

N = 15


def build(g):
    """Numeric pipeline at the embedding zeta60 -> zeta60^g. Returns W1, W2 (canonical), X, Z, and
    the eigen-transport base zeta20^g, zeta12^g."""
    z15 = cmath.exp(2j * cmath.pi * ((4 * g) % 60) / 60)      # zeta15 at this embedding
    T = np.zeros((N, N), complex)
    F = np.zeros((N, N), complex)
    for x in range(N):
        T[x, x] = z15 ** (x * x % 15)
        for y in range(N):
            F[x, y] = z15 ** ((-2 * x * y) % 15)
    gsum = sum(z15 ** (x * x % 15) for x in range(N))
    S = F / gsum
    W1 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    T2 = T @ T
    W2 = T2 @ S @ np.linalg.inv(T2) @ np.linalg.inv(S)
    X = np.diag([z15 ** j for j in range(N)])
    Z = np.zeros((N, N), complex)
    for j in range(N):
        Z[(j + 1) % N, j] = 1
    return W1, W2, X, Z, z15


def projs(W, tol=1e-8):
    ev, V = np.linalg.eig(W)
    cl = []
    for e in ev:
        if not any(abs(c - e) < 1e-7 for c in cl):
            cl.append(e)
    out = []
    for lam in cl:
        P = np.eye(N, dtype=complex)
        for mu in cl:
            if abs(mu - lam) > 1e-7:
                P = P @ (W - mu * np.eye(N)) / (lam - mu)
        out.append((lam, P))
    return out


PARP = np.zeros((N, N))
for x in range(N):
    PARP[(-x) % N, x] = 1


def table_seam_total(a, b, c, d, embeddings_cache):
    """Total |s| over the table for twists W1~ = X^a Z^b W1, W2~ = X^c Z^d W2."""
    # for each of the 8 embeddings (two H-cosets x 4), compute the raw table values keyed by
    # transported eigenvalue labels; average per coset; then s per entry; sum |s|.
    tabs = {}
    for g, (W1, W2, X, Z, z15) in embeddings_cache.items():
        W1t = np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Z, b) @ W1
        W2t = np.linalg.matrix_power(X, c) @ np.linalg.matrix_power(Z, d) @ W2
        P1 = projs(W1t)
        P2 = projs(W2t)
        tab = {}
        for l1, P in P1:
            for l2, Q in P2:
                # label by eigenvalue at the REFERENCE embedding: transport back k -> k * g^{-1}
                t = np.trace(PARP @ P @ Q)
                tab[(complex(round(l1.real, 6), round(l1.imag, 6)),
                     complex(round(l2.real, 6), round(l2.imag, 6)))] = t
        tabs[g] = tab
    # match labels across embeddings by transported eigenvalues:
    # sigma_g(lambda) = lambda^g when lambda is a root of unity at reference embedding 1.
    ref = tabs[1]
    # build transported-key lookup per g: for reference eigenpair (u, v), the g-embedding key is (u^g, v^g)
    total = 0.0
    inv_s15 = 1 / (15 ** 0.5)
    for (u, v) in ref:
        vals_id = []      # embeddings fixing H: {1,19,31,49}
        vals_fl = []      # sqrt5-flipping coset: {7,13,37,43}
        okay = True
        for g in (1, 19, 31, 49, 7, 13, 37, 43):
            key = (complex(round((u ** g).real, 6), round((u ** g).imag, 6)),
                   complex(round((v ** g).real, 6), round((v ** g).imag, 6)))
            tg = tabs[g].get(key)
            if tg is None:
                okay = False
                break
            (vals_id if g in (1, 19, 31, 49) else vals_fl).append(tg)
        if not okay:
            continue
        tH1 = sum(vals_id) / 4
        tH7 = sum(vals_fl) / 4
        s = (tH1 - tH7).imag / (2 * 15 ** 0.5)
        total += abs(s)
    return total


def main():
    cache = {g: build(g) for g in (1, 19, 31, 49, 7, 13, 37, 43)}
    print("embeddings built", flush=True)
    # gate: canonical (0,0,0,0) must be seam-free; the known theta-ish twists should light up
    S00 = table_seam_total(0, 0, 0, 0, cache)
    print(f"gate canonical twist (0,0,0,0): total|s| = {S00:.3e} (expect ~0)", flush=True)
    # scan the W1-twist plane with W2 canonical, then the diagonal twists
    grid = {}
    for a in range(N):
        for b in range(N):
            grid[(a, b)] = table_seam_total(a, b, 0, 0, cache)
        print(f"row a={a} done", flush=True)
    json.dump({f"{a},{b}": grid[(a, b)] for (a, b) in grid}, open("lift_torus_scan.json", "w"))
    bright = {k: v for k, v in grid.items() if v > 1e-6}
    print(f"W1-twist plane: bright twists {len(bright)}/225", flush=True)
    # crude structure print
    for b in range(N):
        row = "".join("#" if grid[(a, b)] > 1e-6 else "." for a in range(N))
        print(f"  b={b:2d}: {row}", flush=True)


if __name__ == "__main__":
    main()
