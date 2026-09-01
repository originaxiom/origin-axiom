#!/usr/bin/env python3
"""R12: derive the Gieseking beat from m000's OWN holonomy (independent of the
banked beat formula) and verify it induces the same extension as W0 . conj.

Method:
  pi1(m000) = <a0, b0 | a0 a0 b0 b0 A0 B0>, both generators orientation-reversing
  (det O31 = -1). Even (orientation-preserving) subgroup Gamma+ contains
  X = a0^2, Z = a0 b0.  snappy's SL2C('w') for an odd word w returns the matrix
  part M_w of the antiholomorphic Moebius action z -> M_w . conj(z) — verified
  below via SL2C(aa) == SL2C(a) conj(SL2C(a)).

  1. find words (u, v) in {X, Z} matching the trace triple of my (A, B, AB)
     and satisfying the banked relator -> an isomorphism onto m004's group;
  2. solve for the conjugacy P with P U P^-1 = +-A, P V P^-1 = +-B;
  3. transport sigma0 = M_a0 . conj into my coordinates: W' = P M_a0 conj(P)^-1;
  4. check W' . conj normalizes rho(pi1(m004)) and that
     Q = conj(W0^-1 W') is (up to sign) an element of rho(pi1(m004))
     -> <rho(Gamma), W0 . conj> IS the m000 holonomy group, i.e. the banked
        beat is the actual Gieseking beat (up to inner choice).
"""
import snappy
import numpy as np
from itertools import product

w = np.exp(2j * np.pi / 3)
A = np.array([[1, 1], [0, 1]], dtype=complex)
B = np.array([[1, 0], [-w, 1]], dtype=complex)
W0 = np.array([[1, 0.5 - np.sqrt(3) / 2 * 1j], [0, 1]], dtype=complex)

def wtm(word, d):
    M = np.eye(2, dtype=complex)
    inv = {k.upper(): np.linalg.inv(v) for k, v in d.items()}
    dd = {**d, **inv}
    for ch in word:
        M = M @ dd[ch]
    return M

G0 = snappy.Manifold('m000').fundamental_group()
def sl2c(g):
    m = G0.SL2C(g)
    return np.array([[complex(m[0, 0]), complex(m[0, 1])],
                     [complex(m[1, 0]), complex(m[1, 1])]])

Ma = sl2c('a')
# convention check: for odd words snappy returns the matrix part of M . conj
lhs = sl2c('aa')
rhs = Ma @ np.conj(Ma)
conv = min(np.max(np.abs(lhs - rhs)), np.max(np.abs(lhs + rhs)))
print("SL2C(aa) == +-SL2C(a) conj(SL2C(a)):", conv < 1e-9, f"(dev {conv:.2e})")
assert conv < 1e-9

X, Z = sl2c('aa'), sl2c('ab')
tA, tB, tAB = 2.0, 2.0, np.trace(A @ B)
print(f"target traces: (2, 2, {tAB:.6f})")

def close(x, y, eps=1e-6):
    return abs(x - y) < eps or abs(x + y) < eps

def close_cc(x, y, eps=1e-6):
    return close(x, y, eps) or close(np.conj(x), y, eps)

d0 = {'x': X, 'z': Z}
found = None
for Lu in range(1, 5):
    for tup_u in product('xzXZ', repeat=Lu):
        u = ''.join(tup_u); Mu = wtm(u, d0)
        if not close_cc(np.trace(Mu), tA):
            continue
        for Lv in range(1, 5):
            for tup_v in product('xzXZ', repeat=Lv):
                v = ''.join(tup_v); Mv = wtm(v, d0)
                if not close_cc(np.trace(Mv), tB) or not close_cc(np.trace(Mu @ Mv), tAB):
                    continue
                Rm = wtm('abABaBAbaB', {'a': Mu, 'b': Mv})
                if np.allclose(Rm, np.eye(2), atol=1e-6) or np.allclose(Rm, -np.eye(2), atol=1e-6):
                    found = (u, v, Mu, Mv)
                    break
            if found: break
        if found: break
    if found: break

assert found, "no generator pair found in Gamma+"
u, v, U, V = found
print(f"generator pair in Gamma+ = <x=a0^2, z=a0 b0>: u='{u}', v='{v}'")
print(f"  traces: {np.trace(U):.6f}, {np.trace(V):.6f}, {np.trace(U@V):.6f}")

# is the m000 rep the same complex structure as mine or the mirror?
mirror = not close(np.trace(U @ V), tAB)
if mirror:
    print("  (m000 rep is the complex-conjugate/mirror copy -> conjugate everything)")
    U, V, X, Z, Ma = (np.conj(U), np.conj(V), np.conj(X), np.conj(Z), np.conj(Ma))

# solve P U P^-1 = eps_a A, P V P^-1 = eps_b B  (linear in P for fixed signs)
P = None
for ea in (1, -1):
    for eb in (1, -1):
        # kron equations: (I x P) vec stuff — build linear system for P entries
        rows = []
        for (Msrc, Mdst) in ((U, ea * A), (V, eb * B)):
            # P Msrc - Mdst P = 0 -> (Msrc^T kron I - I kron Mdst) vec(P) = 0
            rows.append(np.kron(Msrc.T, np.eye(2)) - np.kron(np.eye(2), Mdst))
        Msys = np.vstack(rows)
        _, s, Vh = np.linalg.svd(Msys)
        if s[-1] < 1e-8:
            vec = Vh[-1].conj()
            Pc = vec.reshape(2, 2, order='F')  # column-stacking to match kron formula
            det = np.linalg.det(Pc)
            if abs(det) > 1e-12:
                Pc = Pc / np.sqrt(det)
                res = max(np.max(np.abs(Pc @ U @ np.linalg.inv(Pc) - ea * A)),
                          np.max(np.abs(Pc @ V @ np.linalg.inv(Pc) - eb * B)))
                if res < 1e-6:
                    P = Pc
                    print(f"  conjugacy P found with signs ({ea:+d},{eb:+d}); "
                          f"smallest singular value {s[-1]:.2e}")
                    break
    if P is not None: break
assert P is not None, "no conjugacy found"
err = max(np.max(np.abs(P @ U @ np.linalg.inv(P) - ea * A)),
          np.max(np.abs(P @ V @ np.linalg.inv(P) - eb * B)))
print(f"  conjugacy residual: {err:.2e}")

# transport sigma0 = Ma . conj into my coordinates
Wp = P @ Ma @ np.linalg.inv(np.conj(P))
print("transported odd element W' =", np.round(Wp, 6).tolist())

# does W'.conj normalize rho(Gamma)? check images of A, B are +-words in A,B
dAB = {'a': A, 'b': B}
def find_word(Mtarget, maxlen=8, eps=1e-6):
    for L in range(0, maxlen + 1):
        for tup in product('abAB', repeat=L):
            wd = ''.join(tup)
            Mw = wtm(wd, dAB)
            if np.allclose(Mw, Mtarget, atol=eps):
                return '+' + (wd or 'e')
            if np.allclose(Mw, -Mtarget, atol=eps):
                return '-' + (wd or 'e')
    return None

imgA = Wp @ np.conj(A) @ np.linalg.inv(Wp)
imgB = Wp @ np.conj(B) @ np.linalg.inv(Wp)
wa = find_word(imgA, 6)
wb = find_word(imgB, 6)
print(f"  W' conj(A) W'^-1 = {wa} ;  W' conj(B) W'^-1 = {wb}")
assert wa and wb, "W'.conj does not normalize rho(Gamma) visibly"

# the coset test: Q = conj(W0^-1 W') should be +- an element of rho(Gamma)
Q = np.conj(np.linalg.inv(W0) @ Wp)
wq = find_word(Q, 8)
print(f"  Q = conj(W0^-1 W') = {np.round(Q,6).tolist()}")
print(f"  Q as +-word in A,B: {wq}")
if wq:
    print("  -> sigma0 and W0.conj lie in the SAME index-2 extension: the banked")
    print("     beat IS the Gieseking beat (they differ by the inner element above).")
else:
    print("  -> Q not found as a short word; extensions may differ by a symmetry — inspect.")

# independent beat: the automorphism induced by sigma0, expressed on (a, b):
# beat_derived(g) = word of W' conj(rho(g)) W'^-1  (computed above: wa, wb)
print("\nDERIVED beat from m000 holonomy: a ->", wa, ", b ->", wb)
print("BANKED beat:                      a -> +a , b -> +BabAb  (up to inner/sign)")
