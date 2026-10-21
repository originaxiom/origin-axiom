"""Exploratory checks for main's P-211 argument (chat1, 2026-10-21; not banked, no data).
Main's relay of 2026-10-21 (§3) argues that under a surface's moves the odd-p Heisenberg character is fixed at every
genus, while the 2-group one is fixed only at genus 1. This checks both on explicit matrices, and adds the moves of
determinant -1 (the swap a <-> b, an inversion), which reverse orientation: they send the commutator [a, b] to a
conjugate of its inverse, so the central character z -> z^-1. That is invisible at p = 2 and not at odd p.
Representations: the quaternion point a -> iZ, b -> iY (p = 2); H(3) by clock and shift (p = 3); at genus 2 their
tensor squares (one copy per handle). The test maps at genus 2 are automorphisms of F_4 with the stated action on
homology (the in-handle twists are mapping classes, the handle swap up to an inner automorphism; the mixing map and
the inversion are chosen for their symplectic and anti-symplectic homology actions). The character depends only on the
homology action mod p (odd p) or on q composed with it (p = 2), so each stands for the mapping classes with that action.
The genus-2 2-group representation is the quaternion point's tensor square, 2^(1+4)_+ of Arf 0.
Characters of F_{2g} through Heisenberg representations, before and after automorphisms of F_{2g}:
fixed (as a character) iff tr rho(phi(w)) = tr rho(w) for every word w; tested on 300 seeded random words, 300 commutators of random words, and the handles' commutators."""
import numpy as np, random
# usage: python3 -B heisenberg_moves.py > heisenberg_moves_run.txt
w3 = np.exp(2j*np.pi/3)
X3 = np.roll(np.eye(3), 1, axis=0); Z3 = np.diag([1, w3, w3**2])
I2 = np.eye(2); Z = np.diag([1, -1]); Y = np.array([[0, -1j], [1j, 0]])
qZ, qY = 1j*Z, 1j*Y                              # the quaternion point: a -> iZ, b -> iY
def kron(*m):
    r = np.eye(1)
    for x in m: r = np.kron(r, x)
    return r
def inv(w): return [-x for x in reversed(w)]
def apply(phi, w):
    out = []
    for x in w: out += phi[x] if x > 0 else inv(phi[-x])
    return out
def ev(G, w):
    M = np.eye(G[1].shape[0], dtype=complex)
    for x in w: M = M @ (G[x] if x > 0 else np.linalg.inv(G[-x]))
    return M
def fixed(G, phi, n, seed=1):
    rng = random.Random(seed); worst = 0
    rw = lambda: [rng.choice([1, -1]) * rng.randint(1, n) for _ in range(rng.randint(1, 6))]
    comm = lambda u, v: u + v + inv(u) + inv(v)
    words = [rw() for _ in range(300)] + [comm(rw(), rw()) for _ in range(300)]
    words += [comm([2*i+1], [2*i+2]) for i in range(n // 2)] + [comm([1], [2]) * 2]
    if n == 4: words += [comm([1], [2]) + comm([3], [4]), comm([1], [2]) + inv(comm([3], [4]))]
    for w in words:
        worst = max(worst, abs(np.trace(ev(G, apply(phi, w))) - np.trace(ev(G, w))))
    return worst < 1e-9, worst
def ident(n): return {k: [k] for k in range(1, n + 1)}
def mv(n, **kw):
    p = ident(n)
    for k, v in kw.items(): p[int(k[1:])] = v
    return p
# genus 1 (two records): generators 1 = a, 2 = b
g1 = {"R: a->ab": mv(2, k1=[1, 2]), "L: b->ab": mv(2, k2=[1, 2]),
      "swap a<->b (det -1)": {1: [2], 2: [1]}, "inversion b->b^-1 (det -1)": mv(2, k2=[-2])}
reps1 = {"Q8 (p=2), 2-dim": {1: qZ, 2: qY}, "H(3) (p=3), 3-dim": {1: X3, 2: Z3}}
print("genus 1 (two records):")
for rn, G in reps1.items():
    for mn, phi in g1.items():
        ok, d = fixed(G, phi, 2); print(f"  {rn:22s} {mn:28s} fixed: {ok}  (max |dtr| {d:.2e})")
# genus 2 (four records a1, b1, a2, b2 = 1, 2, 3, 4)
g2 = {"twist in handle 1: b1->b1 a1": mv(4, k2=[2, 1]), "twist in handle 1: a1->a1 b1": mv(4, k1=[1, 2]),
      "twist in handle 2: a2->a2 b2": mv(4, k3=[3, 4]), "handle swap": {1: [3], 2: [4], 3: [1], 4: [2]},
      "symplectic mixing: a1->a1 b2, a2->a2 b1": {1: [1, 4], 2: [2], 3: [3, 2], 4: [4]},
      "anti-symplectic: b1->b1^-1, b2->b2^-1": mv(4, k2=[-2], k4=[-4])}
reps2 = {"H(3)^{(x)2} (p=3), 9-dim": {1: kron(X3, np.eye(3)), 2: kron(Z3, np.eye(3)), 3: kron(np.eye(3), X3), 4: kron(np.eye(3), Z3)},
         "Q8 (x) Q8 (p=2), 4-dim": {1: kron(qZ, I2), 2: kron(qY, I2), 3: kron(I2, qZ), 4: kron(I2, qY)}}
print("genus 2 (four records, the surface route):")
for rn, G in reps2.items():
    for mn, phi in g2.items():
        ok, d = fixed(G, phi, 4); print(f"  {rn:26s} {mn:42s} fixed: {ok}  (max |dtr| {d:.2e})")
