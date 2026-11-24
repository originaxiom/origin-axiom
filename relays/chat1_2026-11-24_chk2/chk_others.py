#!/usr/bin/env python3
"""CHK-2c: spot checks of the physical lane's note of 2026-11-20 (NORMALIZABLE_INTERIOR_DOUBLET_AND_COLORED_COVER_MODES)
and of agy-exp's Gieseking / D5 claim card (2026-11-24). Data-free.

    python3 -I -u chk_others.py

Expectations, written before the run:
  P1  From trace -2, trace of square -2, determinant -1 and e_(5-j) = D conj(e_j), the characteristic polynomial is
      z^5 + 2z^4 + 3z^3 + 3z^2 + 2z + 1 = (z+1)(z^2+1)(z^2+z+1).                                         95 %
  P2  From trace -s, trace of square 8s + s^2, determinant s^2 (s = omega^2), it is z^4 + s z^3 - 4s z^2 + s z + s^2,
      and no root has modulus 1.                                                                           90 %
  P3  The cubic z^3 - 2 s^2 z^2 - 2 z + s^2 (s = omega^2 and s = omega) has no root of modulus 1.             80 %
  G1  The orientation double cover of the Gieseking manifold (m000) is the figure-eight complement (m004).    99 %
  G2  pi_1(m004) has surjections onto D_5; the regular 10-fold cover and the irregular 5-fold cover are listed with
      their cusps and H_1 (read-outs, no prediction of the values).
"""
import itertools

import mpmath as mp
import sympy as sp

mp.mp.dps = 40
z = sp.symbols("z")
w = sp.exp(2 * sp.pi * sp.I / 3)


def charpoly(m, e1, p2, det, D):
    """Characteristic polynomial of degree m from the trace e1, the trace of the square p2, the determinant, and
    the Hermitian-form symmetry e_(m-j) = D conj(e_j)."""
    e = {0: 1, 1: e1, 2: sp.expand((e1 ** 2 - p2) / 2), m: det}
    for j in range(1, m):
        if (m - j) not in e:
            e[m - j] = sp.expand(D * sp.conjugate(e[j]))
    for j in range(m + 1):
        if j not in e:
            raise ValueError("underdetermined at %d" % j)
    return sp.expand(sum((-1) ** j * e[j] * z ** (m - j) for j in range(m + 1))), e


P1, _ = charpoly(5, -2, -2, -1, -1)
print("P1 =", P1, "| equals (z+1)(z^2+1)(z^2+z+1):", sp.expand(P1 - (z + 1) * (z ** 2 + 1) * (z ** 2 + z + 1)) == 0)

s = w ** 2
P2, e2 = charpoly(4, -s, 8 * s + s ** 2, s ** 2, s ** 2)
target = z ** 4 + s * z ** 3 - 4 * s * z ** 2 + s * z + s ** 2
print("P2 matches the note:", sp.simplify(sp.expand(P2 - target)) == 0,
      "| e2 self-consistent:", sp.simplify(e2[2] - sp.expand(s ** 2 * sp.conjugate(e2[2]))) == 0)
c2 = [complex(sp.N(sp.expand(target).coeff(z, k), 30)) for k in range(4, -1, -1)]
r2 = mp.polyroots(c2, maxsteps=200, extraprec=60)
print("    |roots of P2| =", [mp.nstr(abs(r), 12) for r in r2])

for name, sv in (("omega^2", w ** 2), ("omega", w)):
    cub = z ** 3 - 2 * sv ** 2 * z ** 2 - 2 * z + sv ** 2
    cc = [complex(sp.N(sp.expand(cub).coeff(z, k), 30)) for k in range(3, -1, -1)]
    rr = mp.polyroots(cc, maxsteps=200, extraprec=60)
    print("P3  s = %s: |roots| = %s" % (name, [mp.nstr(abs(r), 12) for r in rr]))

try:
    import snappy
    G0 = snappy.Manifold("m000")
    oc = G0.orientation_cover()
    print("G1  m000 orientable: %s, volume %s; its orientation cover is m004: %s"
          % (G0.is_orientable(), G0.volume(), oc.is_isometric_to(snappy.Manifold("m004"))))
    M = snappy.Manifold("m004")
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    print("    pi_1(m004): generators %s, relators %s" % (gens, rels))
    # D_5 as permutations of the five vertices (irregular cover) and of its own ten elements (regular cover).
    rot = (1, 2, 3, 4, 0)
    ref = (0, 4, 3, 2, 1)

    def comp(p, q):                       # p after q
        return tuple(p[q[i]] for i in range(5))

    def inv(p):
        out = [0] * 5
        for i, v in enumerate(p):
            out[v] = i
        return tuple(out)

    elems = {tuple(range(5))}
    frontier = [tuple(range(5))]
    while frontier:
        nxt = []
        for e in frontier:
            for g in (rot, ref):
                c = comp(g, e)
                if c not in elems:
                    elems.add(c)
                    nxt.append(c)
        frontier = nxt
    elems = sorted(elems)
    assert len(elems) == 10

    def word(rel, imgs):
        p = tuple(range(5))
        for ch in rel:
            g = imgs[ch.lower()]
            p = comp(p, g if ch.islower() else inv(g))
        return p

    def generated(imgs):
        S = {tuple(range(5))}
        fr = [tuple(range(5))]
        while fr:
            nx = []
            for e in fr:
                for g in imgs.values():
                    c = comp(g, e)
                    if c not in S:
                        S.add(c)
                        nx.append(c)
            fr = nx
        return len(S)

    homs = []
    for ims in itertools.product(elems, repeat=len(gens)):
        imgs = dict(zip(gens, ims))
        if all(word(r, imgs) == tuple(range(5)) for r in rels) and generated(imgs) == 10:
            homs.append(imgs)
    print("G2  surjections pi_1(m004) -> D_5 (as maps on generators): %d" % len(homs))
    if homs:
        imgs = homs[0]
        perm5 = [list(imgs[g]) for g in gens]
        C5 = M.cover(perm5)
        idx = {e: i for i, e in enumerate(elems)}
        perm10 = [[idx[comp(imgs[g], e)] for e in elems] for g in gens]
        C10 = M.cover(perm10)
        for name, C in (("irregular 5-fold", C5), ("regular 10-fold", C10)):
            print("    %s cover: cusps %d, H_1 = %s, volume %s" % (name, C.num_cusps(), C.homology(), C.volume()))
except Exception as exc:  # noqa: BLE001
    print("SnapPy part not run:", exc)
print("done")
