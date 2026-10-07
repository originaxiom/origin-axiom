#!/usr/bin/env python3
"""The fixed-point companions of the four states on record: structure only, no count at any class.

A word state M = T1 x_phi S^1 has H_1(M) = Z<t> + coker(phi_* - I), and its peripheral group maps onto Z<t> (the fibre's
boundary is a commutator). So the maximal abelian cover to which the cusp lifts is the cover along coker(phi_* - I) with
t -> 0. It is the mapping torus of phi on the torus with every fixed point of phi punctured (NOTE.md, Proposition 1), so it
has |det(phi - I)| = |2 - tr phi| cusps. This script reads, in SnapPy, for m003 = -LR, m136 = +LLRR and m135 = -LLRR:
  1. every cover of degree d = |2 - tr phi|, and that exactly one has d cusps (so it is the companion);
  2. its homology, and whether it is free of rank d (then n(1) = b1 - d = 0);
  3. for every set A of 2, 3 or 4 cusps, the group H_1 / <the peripheral subgroups of A>, whose characters are exactly the
     characters trivial on every cusp of A;
  4. its census name where SnapPy has one, its symmetry group, and the permutations of the cusps that its isometries
     realise, with and without orientation.
For m003's companion it also reads the link L10n113's linking matrix and checks item 3 against it.

    python3 companions.py   ->  companions.json beside this file (a few minutes)"""
import itertools
import json
from collections import Counter
from pathlib import Path

import snappy
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE = Path(__file__).resolve().parent
STATES = (("m003", "-LR", -3), ("m136", "+LLRR", 6), ("m135", "-LLRR", -6))


def word_vec(w, gens):
    v = [0] * len(gens)
    for ch in w:
        if ch.islower():
            v[gens.index(ch)] += 1
        else:
            v[gens.index(ch.lower())] -= 1
    return v


def coker(rows, ncols):
    if not rows:
        return (ncols, ())
    S = smith_normal_form(Matrix(rows), domain=ZZ)
    d = [abs(S[k, k]) for k in range(min(S.shape))]
    return (ncols - sum(1 for x in d if x != 0), tuple(int(x) for x in d if x not in (0, 1)))


def peripheral_quotients(C, sizes):
    G = C.fundamental_group()
    gens = list(G.generators())
    rel = [word_vec(r, gens) for r in G.relators()]
    per = [(word_vec(m, gens), word_vec(lo, gens)) for (m, lo) in G.peripheral_curves()]
    out = {"H1 (free rank, torsion)": coker(rel, len(gens))}
    for s in sizes:
        q = {A: coker(rel + [v for i in A for v in per[i]], len(gens)) for A in itertools.combinations(range(len(per)), s)}
        out[s] = q
    return out


def cusp_action(C):
    iso = C.is_isometric_to(C, return_isometries=True)
    every, keep = set(), set()
    for f in iso:
        p = tuple(f.cusp_images())
        every.add(p)
        if all(m[0][0] * m[1][1] - m[0][1] * m[1][0] > 0 for m in f.cusp_maps()):
            keep.add(p)
    return len(iso), len(every), len(keep)


def main():
    rec = {}
    for name, word, tr in STATES:
        M = snappy.Manifold(name)
        d = abs(2 - tr)
        covers = M.covers(d)
        hits = [C for C in covers if C.num_cusps() == d]
        assert len(hits) == 1, (name, len(hits))
        C = hits[0]
        pq = peripheral_quotients(C, (2, 3, 4))
        n_iso, n_perm, n_perm_or = cusp_action(C)
        ident = [str(x).split("(")[0] for x in C.identify()]
        row = {
            "monodromy": word, "trace": tr, "|2 - tr|": d, "H1(M)": str(M.homology()),
            "covers of degree d": len(covers), "of them with d cusps": len(hits),
            "companion H1 (free rank, torsion)": list(pq["H1 (free rank, torsion)"]),
            "n(1) = b1 - cusps": pq["H1 (free rank, torsion)"][0] - d if not pq["H1 (free rank, torsion)"][1] else None,
            "volume": float(C.volume()), "volume / vol(M)": float(C.volume() / M.volume()),
            "census names": ident, "symmetry group": str(C.symmetry_group()),
            "isometries": n_iso, "cusp permutations realised": n_perm,
            "cusp permutations realised, orientation kept": n_perm_or,
        }
        for s in (2, 3, 4):
            row[f"quotients over {s} cusps (free rank, torsion): count"] = {str(k): v for k, v in Counter(pq[s].values()).items()}
            row[f"some non-trivial character is trivial on {s} cusps"] = any(q != (0, ()) for q in pq[s].values())
        rec[name] = row
        if name == "m003":
            L = snappy.Manifold("L10n113")
            row["isometric to L10n113"] = bool(L.is_isometric_to(C))
            row["isometric to o10_150729"] = bool(snappy.Manifold("o10_150729").is_isometric_to(C))
            lk = L.link().linking_matrix()
            row["L10n113 linking matrix"] = lk
            n = len(lk)
            for s in (2, 3):
                ok = True
                for A in itertools.combinations(range(n), s):
                    rows = [[1 if j == i else 0 for j in range(n)] for i in A] + [list(lk[i]) for i in A]
                    q = coker(rows, n)
                    ok &= (q == ((1, ()) if s == 2 else (0, ())))
                row[f"linking-matrix check over {s} components"] = ok
        print(name, json.dumps({k: row[k] for k in ("|2 - tr|", "of them with d cusps", "companion H1 (free rank, torsion)",
                                                  "census names", "symmetry group", "cusp permutations realised",
                                                  "cusp permutations realised, orientation kept")}), flush=True)
    (HERE / "companions.json").write_text(json.dumps(rec, indent=1) + "\n")


if __name__ == "__main__":
    main()
