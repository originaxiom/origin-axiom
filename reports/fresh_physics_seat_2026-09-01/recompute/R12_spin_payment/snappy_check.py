#!/usr/bin/env python3
"""R12 blind snappy cross-check for B1141 (written before opening the arc's scripts).

Checks:
 1. m004: volume, H1 = Z, 2-generator 1-relator presentation; my exact A,B satisfy
    snappy's relator and reproduce snappy's holonomy traces (up to conjugation
    and possibly complex conjugation / sign — PSL vs SL conventions).
 2. m000 (Gieseking): nonorientable, volume = Vol(m004)/2, orientation double
    cover isometric to m004.
 3. My beat automorphism is induced by an actual orientation-reversing symmetry:
    sigma = W0 . conj  normalizes rho(pi1(m004)), sigma^2 = rho(a), so
    <rho(pi1), sigma> is an index-2 extension whose quotient orbifold volume is
    Vol(m004)/2 = Vol(m000).
"""
import snappy
import numpy as np

M4 = snappy.Manifold('m004')
M0 = snappy.Manifold('m000')

print("m004:", M4.volume(), M4.homology(), "orientable:", M4.is_orientable())
print("m000:", M0.volume(), M0.homology(), "orientable:", M0.is_orientable())
print("vol(m000) == vol(m004)/2 :", abs(M0.volume() - M4.volume() / 2) < 1e-9)

G4 = M4.fundamental_group()
print("pi1(m004) generators:", G4.generators(), "relators:", G4.relators())

# --- my exact holonomy, numerically ---
w = np.exp(2j * np.pi / 3)
A = np.array([[1, 1], [0, 1]], dtype=complex)
B = np.array([[1, 0], [-w, 1]], dtype=complex)

def wtm(word, Ma, Mb):
    d = {'a': Ma, 'b': Mb, 'A': np.linalg.inv(Ma), 'B': np.linalg.inv(Mb)}
    M = np.eye(2, dtype=complex)
    for ch in word:
        M = M @ d[ch]
    return M

# snappy's census presentation uses different generators than the banked one.
# Identify my (A,B) inside snappy's holonomy by word search: find a pair of words
# (u,v) in snappy's generators whose SL2C images have the same trace triple
# (tr u, tr v, tr uv) as (A, B, AB) up to overall sign and complex conjugation
# — for irreducible SL2 reps the trace triple determines the pair up to conjugacy.
def sl2c(G, g):
    m = G.SL2C(g)
    return np.array([[complex(m[0, 0]), complex(m[0, 1])],
                     [complex(m[1, 0]), complex(m[1, 1])]])

sa, sb = sl2c(G4, 'a'), sl2c(G4, 'b')
tA, tB, tAB = np.trace(A), np.trace(B), np.trace(A @ B)
print(f"my trace triple: tr A={tA:.6f}, tr B={tB:.6f}, tr AB={tAB:.6f}")

from itertools import product
def words(maxlen):
    for L in range(1, maxlen + 1):
        for tup in product('abAB', repeat=L):
            yield ''.join(tup)

def close(x, y, eps=1e-8):
    return min(abs(x - y), abs(x + y), abs(np.conj(x) - y), abs(np.conj(x) + y)) < eps

found = None
cand_u = [wd for wd in words(4) if close(np.trace(wtm(wd, sa, sb)), tA)]
for u in cand_u:
    Mu = wtm(u, sa, sb)
    for v in words(4):
        Mv = wtm(v, sa, sb)
        if close(np.trace(Mv), tB) and close(np.trace(Mu @ Mv), tAB):
            # confirm the banked relator holds for (u,v) in PSL
            Rm = wtm('abABaBAbaB', Mu, Mv)
            if np.allclose(Rm, np.eye(2), atol=1e-6) or np.allclose(Rm, -np.eye(2), atol=1e-6):
                found = (u, v, np.trace(Mu), np.trace(Mv), np.trace(Mu @ Mv))
                break
    if found:
        break
if found:
    u, v, t1, t2, t3 = found
    print(f"MATCH inside snappy holonomy: u='{u}', v='{v}' with traces "
          f"({t1:.6f}, {t2:.6f}, {t3:.6f}) — banked relator holds on (u,v); "
          "my (A,B) is snappy's discrete faithful rep up to conjugacy/mirror")
else:
    print("NO word-pair match found up to length 4 — investigate")

# --- orientation double cover of m000 ---
try:
    C = M0.orientation_cover()
    print("orientation_cover(m000):", C, C.volume())
    print("cover isometric to m004:", C.is_isometric_to(M4))
except Exception as e:
    print("orientation_cover failed:", e)

# also: the covers of m000 of degree 2
print("degree-2 covers of m000:", [(c, c.is_orientable(), round(c.volume(), 6)) for c in M0.covers(2)])

# --- sigma = W0 . conj implements the beat and closes: numeric sanity ---
W0 = np.array([[1, 0.5 - np.sqrt(3) / 2 * 1j], [0, 1]], dtype=complex)
beat_b = wtm('BabAb', A, B)
print("sigma g sigma^-1 checks:")
print("  W0 conj(A) W0^-1 - A:", np.max(np.abs(W0 @ np.conj(A) @ np.linalg.inv(W0) - A)))
print("  W0 conj(B) W0^-1 - rho(beat(b)):", np.max(np.abs(W0 @ np.conj(B) @ np.linalg.inv(W0) - beat_b)))
print("  sigma^2 = W0 conj(W0) - A:", np.max(np.abs(W0 @ np.conj(W0) - A)))

# m000's own fundamental group, for the record (and orientation character via O31 dets)
G0 = M0.fundamental_group()
print("pi1(m000) generators:", G0.generators(), "relators:", G0.relators())
for g in G0.generators():
    Om = G0.O31(g)
    O = np.array([[float(Om[i, j]) for j in range(4)] for i in range(4)])
    print(f"  det O31({g}) = {np.linalg.det(O):+.6f}  (-1 = orientation-reversing)")
