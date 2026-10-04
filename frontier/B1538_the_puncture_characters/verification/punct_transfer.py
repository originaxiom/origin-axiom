#!/usr/bin/env python3
"""B1538 route T -- the transfer: the line's supply summed over a character's powers, from integer homology.  Library; nothing
sealed is computed on import.

For chi of order k on H = pi_1 N, let N' be the cyclic cover with pi_1 N' = ker chi, of degree k |D| over the state.
  - Shapiro: H^1(N'; C) = sum_j H^1(N; chi^j), and the same on the boundary.  So, with half lives, half dies on N',
        b1(N') - #cusps(N') = n_N'(1) = sum_{j mod k} n_N(chi^j).
  - Gamma acts on the cosets of ker chi, pairs (x, c) with x in D and c in Z/k, by (x, c)^g = (x^g, c + e(x, g)), where
    z_k^e(x,g) = chi(s_(x,g)) on route W's Reidemeister-Schreier generators (punct_covers.Cover.rs_values).
  - sm:B1536's cover_lib.check_cover confirms the action (Gamma's relators act trivially, and the action is transitive).  It
    therefore also confirms that chi is a character of H of order k.
  - H_1(N'; Z) is read from N''s own Reidemeister-Schreier presentation (abelianized; rank over Q by python-flint's fmpz_mat).
  - #cusps(N') comes from cover_lib.cusps.
No twisted coefficient and no character value enters the homology: only the permutation action does.  New code for B1538."""
import punct_covers as F


def cover_perms(C, ez, es, L):
    """the action of Gamma on Gamma / ker chi, and k = the order of chi"""
    vals = C.rs_values(ez, es, L)
    from math import gcd
    g = L
    for v in vals.values():
        g = gcd(g, v)
    k = L // g
    step = {key: (v // g) % k for key, v in vals.items()}
    d = C.d
    perms = {}
    for gen in "abt":
        perms[gen] = [C.perms[gen][x] * k + (c + step[(x, gen)]) % k for x in range(d) for c in range(k)]
    return perms, k


def homology_rank(G, perms):
    """b1 of the cover given by perms, from its Reidemeister-Schreier presentation abelianized"""
    import flint
    CL = F.cover_lib()
    P = CL.with_inverses(perms)
    d = len(perms[G.gens[0]])
    seen, order, i, tree = {0}, [0], 0, set()
    while i < len(order):
        x = order[i]
        i += 1
        for g in G.gens:
            y = P[g][x]                          # the edge (x, g): x^g = y
            if y not in seen:
                seen.add(y)
                order.append(y)
                tree.add((x, g))
            y = P["_inv"][g][x]                  # the edge (y, g): y^g = x
            if y not in seen:
                seen.add(y)
                order.append(y)
                tree.add((y, g))
    assert len(seen) == d and len(tree) == d - 1
    gidx = {}
    for x in range(d):
        for g in G.gens:
            if (x, g) not in tree:
                gidx[(x, g)] = len(gidx)
    rows = []
    for x in range(d):
        for r in G.rels:
            v = [0] * len(gidx)
            cur = x
            for c in r:
                g = c.lower()
                if c.islower():
                    if (cur, g) in gidx:
                        v[gidx[(cur, g)]] += 1
                    cur = P[g][cur]
                else:
                    prev = P["_inv"][g][cur]
                    if (prev, g) in gidx:
                        v[gidx[(prev, g)]] -= 1
                    cur = prev
            assert cur == x
            rows.append(v)
    ng = len(gidx)
    assert ng == d * (len(G.gens) - 1) + 1
    rk = flint.fmpz_mat(len(rows), ng, [e for r in rows for e in r]).rank()
    return ng - rk


def read(C, ez, es, L):
    """b1(N') - #cusps(N') for N' = ker chi, chi = (ez, es) mod L"""
    CL = F.cover_lib()
    perms, k = cover_perms(C, ez, es, L)
    assert CL.check_cover(C.st.G, perms), "chi is not a character of H"
    b1 = homology_rank(C.st.G, perms)
    nc = len(CL.cusps(C.st.G, perms))
    return {"k": k, "degree": C.d * k, "b1": b1, "cusps": nc, "n_N'": b1 - nc}
