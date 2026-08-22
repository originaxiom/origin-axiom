#!/usr/bin/env python3
"""
INDEPENDENT verification of golden_gate memo 11 (FORK_THEOREM), banked at
577712f. I read fork_theorem.py for SPEC ONLY (to know which quantities to
reproduce) and did NOT import or copy it. This script imports ONLY the
banked+locked e6 module already on main
(frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py) per the
task's reuse instruction, and does everything else -- slot-finding,
centralizer linear algebra, the Weyl group closure, the S3-torsor tally --
with my own code (the rank/centralizer helpers are imported from
my_chevalley.py, which I wrote this session for the memo-14 leg; they are
generic linear algebra, not tied to any particular algebra's construction).

Claims under test:
  1. THE LADDER: dim z(T1) = 16, dim z(T1 u color) = 8, dim z(T1,T2) = 8,
     dim z(T1,T2 u color) = 0.
  2. Robustness: the ladder is recomputed from a DIFFERENT adjacent simple
     pair than the certificate used, as an invariance check (not just a
     replay of their exact slot choice).
  3. THE S3 FRAME TORSOR: the slot-preserving subgroup of W(E6) surjects
     onto S3 with uniform fibers of size 216 = |W(A2)|^3.
"""
import os
import sys
import itertools
from fractions import Fraction as Fr
from collections import Counter

_REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(_REPO, "frontier/B1102_exact_hypercharge_solve"))
import e6_bracket_vendored as V   # noqa: E402  (the banked+locked module; READ-ONLY use)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from my_chevalley import exact_rank, centralizer_rows  # my own generic linear algebra


class VendoredE6:
    """Thin adapter presenting the vendored e6 module through the same
    interface my_chevalley.ChevalleyAlgebra objects use, so the SAME
    generic centralizer_rows()/exact_rank() code (mine) can run over the
    banked e6 data without duplicating logic. No e6-specific math here."""
    def __init__(self):
        self.n = V.N
        self.DIM = V.DIM
        self.roots = V.ROOTS
        self.IDX = V.IDX
        self.A = V.A

    def hvec(self, i):
        return V.hvec(i)

    def evec(self, r):
        return V.evec(r)

    def br(self, u, v):
        return V.br(u, v)

    def pairing(self, r, s):
        return V.ip(r, s)


ALG = VendoredE6()
N = ALG.n


def cartan_vec(r):
    """Coroot direction h_r = sum r_k h_k, as a DIM-vector (Cartan part only)."""
    return [Fr(x) for x in list(r)] + [Fr(0)] * len(ALG.roots)


def a2_span(base_pair):
    """The 6 roots of the A2 spanned by two simple(ish) roots r,s with (r,s)=-1:
    {+-r, +-s, +-(r+s)} intersected with the actual root set."""
    r, s = base_pair
    out = set()
    for c1, c2 in itertools.product((-1, 0, 1), repeat=2):
        if c1 == 0 and c2 == 0:
            continue
        v = tuple(c1 * r[k] + c2 * s[k] for k in range(N))
        if v in ALG.IDX:
            out.add(v)
    return out


def find_a2_in(pool, forbid_spans=()):
    """Find r,s in pool with (r,s) = -1 and r+s also in pool (and not touching
    any root already used in forbid_spans)."""
    forbid = set().union(*forbid_spans) if forbid_spans else set()
    poolset = set(pool)
    for r, s in itertools.permutations(pool, 2):
        if r in forbid or s in forbid:
            continue
        if ALG.pairing(r, s) != -1:
            continue
        t = tuple(r[k] + s[k] for k in range(N))
        if t in poolset:
            return r, s
    raise RuntimeError("no A2 found in pool")


def principal_triple(base_pair):
    r, s = base_pair
    e = ALG.br  # not used here, just alias avoidance
    ev = ALG.evec
    e_vec = [a + b for a, b in zip(ev(r), ev(s))]
    h_vec = [Fr(2) * (a + b) for a, b in zip(cartan_vec(r), cartan_vec(s))]
    neg_r = tuple(-x for x in r)
    neg_s = tuple(-x for x in s)
    f_vec = [Fr(-2) * a + Fr(-2) * b for a, b in zip(ev(neg_r), ev(neg_s))]
    assert ALG.br(e_vec, f_vec) == h_vec, "principal sl2 triple failed [e,f]=h"
    assert ALG.br(h_vec, e_vec) == [Fr(2) * x for x in e_vec]
    assert ALG.br(h_vec, f_vec) == [Fr(-2) * x for x in f_vec]
    return [e_vec, h_vec, f_vec]


def color_gens(S2_roots):
    r2, s2 = find_a2_in(S2_roots)
    gens = [ALG.evec(r) for r in sorted(S2_roots)]
    gens.append(cartan_vec(r2))
    gens.append(cartan_vec(s2))
    return gens


def centralizer_dim(gens):
    rows = centralizer_rows(ALG, gens)
    return ALG.DIM - exact_rank(rows, ALG.DIM)


def run_ladder(base_pair, tag):
    print(f"\n--- slot choice {tag}: S0 base pair = {base_pair} ---")
    S0 = a2_span(base_pair)
    assert len(S0) == 6, f"S0 not a clean A2: {len(S0)} roots"
    a, b = base_pair
    Rperp = [r for r in ALG.roots if ALG.pairing(r, a) == 0 and ALG.pairing(r, b) == 0]
    # split Rperp into connected components under "nonzero inner product" adjacency
    comps = []
    left = set(Rperp)
    while left:
        seed = next(iter(left))
        comp = {seed}
        grown = True
        while grown:
            grown = False
            for r in list(left - comp):
                if any(ALG.pairing(r, x) != 0 for x in comp):
                    comp.add(r)
                    grown = True
        comps.append(comp)
        left -= comp
    print(f"    |Rperp| = {len(Rperp)}, splits into {len(comps)} component(s) of sizes "
          f"{sorted(len(c) for c in comps)}")
    assert len(comps) == 2 and all(len(c) == 6 for c in comps), \
        "expected exactly two orthogonal A2 components"
    S1, S2 = comps

    T1 = principal_triple(find_a2_in(S0))
    T2 = principal_triple(find_a2_in(S1))
    COLOR = color_gens(S2)

    d1 = centralizer_dim(T1)
    d2 = centralizer_dim(T1 + COLOR)
    d3 = centralizer_dim(T1 + T2)
    d4 = centralizer_dim(T1 + T2 + COLOR)
    print(f"    dim z(T1)            = {d1}  (expect 16)")
    print(f"    dim z(T1 u color)    = {d2}  (expect 8)")
    print(f"    dim z(T1,T2)         = {d3}  (expect 8)")
    print(f"    dim z(T1,T2 u color) = {d4}  (expect 0)")
    return (d1, d2, d3, d4), (S0, S1, S2)


def simple_reflection_perm(i):
    """Permutation of ALG.roots induced by the i-th simple reflection."""
    ai = tuple(1 if k == i else 0 for k in range(N))
    perm = []
    for r in ALG.roots:
        c = ALG.pairing(r, ai)
        s = tuple(r[k] - c * ai[k] for k in range(N))
        perm.append(ALG.IDX[s])
    return tuple(perm)


def build_weyl_group():
    nR = len(ALG.roots)
    gens = [simple_reflection_perm(i) for i in range(N)]
    ident = tuple(range(nR))
    seen = {ident}
    frontier = [ident]
    W = [ident]
    while frontier:
        nxt = []
        for p in frontier:
            for g in gens:
                q = tuple(p[g[i]] for i in range(nR))
                if q not in seen:
                    seen.add(q)
                    nxt.append(q)
                    W.append(q)
        frontier = nxt
    return W


def frame_torsor(W, S0, S1, S2):
    fs = [frozenset(ALG.IDX[r] for r in S) for S in (S0, S1, S2)]

    def action(p):
        images = [frozenset(p[i] for i in f) for f in fs]
        if any(im not in fs for im in images):
            return None
        return tuple(fs.index(im) for im in images)

    tally = Counter()
    for p in W:
        a = action(p)
        if a is not None:
            tally[a] += 1
    return tally


def main():
    print("=" * 78)
    print("MEMO 11 (FORK_THEOREM) -- independent re-derivation on the banked e6")
    print("=" * 78)

    # --- slot choice A: reproduce the certificate's own base pair (alpha_1, alpha_3) ---
    a0 = tuple(1 if k == 0 else 0 for k in range(N))
    a2 = tuple(1 if k == 2 else 0 for k in range(N))
    ladderA, slotsA = run_ladder((a0, a2), "A (matches cert's own choice, indices 0,2)")

    # --- slot choice B: a DIFFERENT adjacent simple pair (indices 3,4) ---
    a3 = tuple(1 if k == 3 else 0 for k in range(N))
    a4 = tuple(1 if k == 4 else 0 for k in range(N))
    ladderB, slotsB = run_ladder((a3, a4), "B (independent choice, indices 3,4)")

    ok_ladder = (ladderA == (16, 8, 8, 0)) and (ladderB == (16, 8, 8, 0))
    print(f"\nLADDER VERDICT: choice A = {ladderA}, choice B = {ladderB} -> "
          f"{'CONFIRMED (16/8/8/0 both, slot-independent)' if ok_ladder else 'MISMATCH'}")

    print("\n" + "=" * 78)
    print("THE S3 FRAME TORSOR (built on slot choice A)")
    print("=" * 78)
    S0, S1, S2 = slotsA
    W = build_weyl_group()
    print(f"|W(E6)| computed = {len(W)}  (expect 51840)")
    assert len(W) == 51840

    tally = frame_torsor(W, S0, S1, S2)
    print("Slot-permutation action tally over W(E6):")
    for perm, cnt in sorted(tally.items()):
        print(f"   permutation {perm} realized by {cnt} Weyl elements")
    six_perms = set(itertools.permutations((0, 1, 2)))
    realized = set(tally.keys())
    all_realized = realized == six_perms
    uniform = len(set(tally.values())) == 1
    fiber = next(iter(tally.values())) if uniform else None
    print(f"\nAll 6 permutations of S3 realized: {all_realized}")
    print(f"Uniform fiber size: {uniform} (fiber = {fiber}, expect 216)")
    print(f"Total stabilizer order = {sum(tally.values())} (expect 1296 = 6*216)")

    verdict_torsor = all_realized and uniform and fiber == 216
    print(f"\nTORSOR VERDICT: {'CONFIRMED (S3, fiber=216 each)' if verdict_torsor else 'MISMATCH'}")

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"Ladder 16/8/8/0 (fork = 0):  {'CONFIRMED' if ok_ladder else 'REFUTED'}")
    print(f"S3 frame torsor, fiber 216:  {'CONFIRMED' if verdict_torsor else 'REFUTED'}")


if __name__ == "__main__":
    main()
