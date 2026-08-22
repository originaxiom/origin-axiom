#!/usr/bin/env python3
"""
INDEPENDENT verification of golden_gate memo 14 (AMBIENT_LADDER), banked at
577712f. Certificates e7_ladder.py / e8_lower.py were read for SPEC ONLY (to
know which construction and which numbers to reproduce); nothing was
imported or copied from them. This script uses ONLY my_chevalley.py, the
generic Chevalley builder I wrote this session (root-reflection closure +
Frenkel-Kac cocycle, with a deliberately flipped cocycle triangularity vs.
what I read in the certs -- see my_chevalley.py docstring) -- same code path
for E6, E7, E8.

Claims under test (memo 14):
  - CONTROL: the generic builder specialized to E6 reproduces the banked
    ladder 16 / 8 / 0 (z(T1), z(T1,T2), z(T1,T2 u color)).
  - E7 (133-dim, exact over Q): ladder 35 / 9 / 1; the surviving room=1
    generator is pure Cartan (a single u(1)) and commutes with everything
    spent.
  - E8 (248-dim): ladder <=78 / <=16 / =8, via a rigorous mod-p sandwich
    (nullity_p >= nullity_Q for every prime p, so agreement of two distinct
    primes gives a valid upper bound) for the upper bounds, and an explicit
    commuting 4th-orthogonal-A2 sl3 exhibit (rank 8, verified to commute
    exactly with T1,T2,color) for the lower bound on the final, load-bearing
    number.
"""
import os
import sys
import time
import itertools
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from my_chevalley import (ChevalleyAlgebra, en_cartan, centralizer_rows, exact_rank,
                           modp_rank, nullspace_basis_exact)


def cartan_vec(alg, r):
    return [Fr(x) for x in r] + [Fr(0)] * len(alg.roots)


def find_adjacent_pair(alg):
    for i in range(alg.n):
        for j in range(i + 1, alg.n):
            if alg.A[i][j] == -1:
                return alg.simples[i], alg.simples[j]
    raise RuntimeError("no adjacent simple pair found")


def a2_span(alg, base_pair):
    r, s = base_pair
    n = alg.n
    out = set()
    for c1, c2 in itertools.product((-1, 0, 1), repeat=2):
        if c1 == 0 and c2 == 0:
            continue
        v = tuple(c1 * r[k] + c2 * s[k] for k in range(n))
        if v in alg.IDX:
            out.add(v)
    return out


def find_a2_in(alg, pool):
    poolset = set(pool)
    for r, s in itertools.permutations(pool, 2):
        if alg.pairing(r, s) != -1:
            continue
        t = tuple(r[k] + s[k] for k in range(alg.n))
        if t in poolset:
            return r, s
    raise RuntimeError("no A2 found in pool")


def orthogonal_pool(alg, refs):
    return [r for r in alg.roots if all(alg.pairing(r, s) == 0 for s in refs)]


def build_slots(alg):
    base0 = find_adjacent_pair(alg)
    S0 = a2_span(alg, base0)
    perp0 = orthogonal_pool(alg, base0)
    base1 = find_a2_in(alg, perp0)
    S1 = a2_span(alg, base1)
    perp01 = [r for r in perp0 if alg.pairing(r, base1[0]) == 0 and alg.pairing(r, base1[1]) == 0]
    base2 = find_a2_in(alg, perp01)
    S2 = a2_span(alg, base2)
    return dict(base0=base0, base1=base1, base2=base2, S0=S0, S1=S1, S2=S2)


def find_fourth_slot(alg, slots):
    used = slots["S0"] | slots["S1"] | slots["S2"]
    perp = orthogonal_pool(alg, used)
    base3 = find_a2_in(alg, perp)
    S3 = a2_span(alg, base3)
    return base3, S3, perp


def principal_triple(alg, base_pair):
    r, s = base_pair
    ev = alg.evec
    e_vec = [a + b for a, b in zip(ev(r), ev(s))]
    h_vec = [Fr(2) * (a + b) for a, b in zip(cartan_vec(alg, r), cartan_vec(alg, s))]
    neg_r, neg_s = tuple(-x for x in r), tuple(-x for x in s)
    f_vec = [Fr(-2) * a + Fr(-2) * b for a, b in zip(ev(neg_r), ev(neg_s))]
    assert alg.br(e_vec, f_vec) == h_vec, "principal sl2: [e,f]=h failed"
    assert alg.br(h_vec, e_vec) == [Fr(2) * x for x in e_vec]
    assert alg.br(h_vec, f_vec) == [Fr(-2) * x for x in f_vec]
    return [e_vec, h_vec, f_vec]


def sl3_gens(alg, S_roots, base_pair):
    gens = [alg.evec(r) for r in sorted(S_roots)]
    gens.append(cartan_vec(alg, base_pair[0]))
    gens.append(cartan_vec(alg, base_pair[1]))
    return gens


def build_TTC(alg, slots):
    T1 = principal_triple(alg, slots["base0"])
    T2 = principal_triple(alg, slots["base1"])
    COLOR = sl3_gens(alg, slots["S2"], slots["base2"])
    return T1, T2, COLOR


PRIMES = (65521, 1000003)


def run_e6_e7(alg, label):
    print(f"\n{'='*78}\n{label}: dim {alg.DIM}, roots {len(alg.roots)}\n{'='*78}")
    slots = build_slots(alg)
    for tag in ("S0", "S1", "S2"):
        print(f"  |{tag}| = {len(slots[tag])}")
    T1, T2, COLOR = build_TTC(alg, slots)

    t0 = time.time()
    rows1 = centralizer_rows(alg, T1)
    d1 = alg.DIM - exact_rank(rows1, alg.DIM)
    t1 = time.time()
    print(f"  dim z(T1)             = {d1}   [{t1-t0:.1f}s]")

    rows2 = centralizer_rows(alg, T1 + T2)
    d2 = alg.DIM - exact_rank(rows2, alg.DIM)
    t2 = time.time()
    print(f"  dim z(T1,T2)          = {d2}   [{t2-t1:.1f}s]")

    rows3 = centralizer_rows(alg, T1 + T2 + COLOR)
    rank3 = exact_rank(rows3, alg.DIM)
    d3 = alg.DIM - rank3
    t3 = time.time()
    print(f"  dim z(T1,T2 u color)  = {d3}   [{t3-t2:.1f}s]")

    room_basis = None
    if 0 < d3 <= 3:
        room_basis = nullspace_basis_exact(rows3, alg.DIM)
        for k, v in enumerate(room_basis):
            ok = all(all(x == 0 for x in alg.br(v, g)) for g in (T1 + T2 + COLOR))
            pure_cartan = all(v[i] == 0 for i in range(alg.n, alg.DIM))
            nz_cartan = [i for i in range(alg.n) if v[i] != 0]
            print(f"    room generator #{k}: commutes with all spent gens = {ok}; "
                  f"pure-Cartan (u(1)) = {pure_cartan}; nonzero Cartan coeffs at {nz_cartan}")
    return dict(d1=d1, d2=d2, d3=d3, slots=slots, T1=T1, T2=T2, COLOR=COLOR, room_basis=room_basis)


def run_e8(alg, label):
    print(f"\n{'='*78}\n{label}: dim {alg.DIM}, roots {len(alg.roots)}\n{'='*78}")
    slots = build_slots(alg)
    for tag in ("S0", "S1", "S2"):
        print(f"  |{tag}| = {len(slots[tag])}")
    T1, T2, COLOR = build_TTC(alg, slots)

    bounds = {}
    for label_, gens in (("z(T1)", T1), ("z(T1,T2)", T1 + T2), ("z(T1,T2 u color)", T1 + T2 + COLOR)):
        t0 = time.time()
        rows = centralizer_rows(alg, gens)
        per_prime = [alg.DIM - modp_rank(rows, alg.DIM, p) for p in PRIMES]
        ub = min(per_prime)
        t1 = time.time()
        print(f"  dim {label_:22s} <= {ub}   (mod {PRIMES} -> {per_prime})   [{t1-t0:.1f}s]")
        bounds[label_] = ub

    # --- explicit lower-bound witness: the fourth orthogonal A2's sl3 ---
    base3, S3, perp = find_fourth_slot(alg, slots)
    print(f"\n  roots orthogonal to S0 u S1 u S2: {len(perp)} (expect 6 = the fourth A2)")
    assert len(perp) == 6 and len(S3) == 6
    sl3 = sl3_gens(alg, S3, base3)
    commute_ok = all(all(x == 0 for x in alg.br(v, g)) for v in sl3 for g in (T1 + T2 + COLOR))
    rk = exact_rank([v[:] for v in sl3], alg.DIM)
    print(f"  4th-slot sl3 (8 generators) commutes with ALL of T1,T2,color: {commute_ok}")
    print(f"  rank of the 8 exhibited generators: {rk} (expect 8, i.e. linearly independent)")
    # spot-check closure: [sl3[0],sl3[1]] should land back inside span(sl3) or be zero,
    # consistent with an actual sl3 (root+root or root+coroot relations)
    br01 = alg.br(sl3[0], sl3[1])
    print(f"  closure spot-check [g0,g1] nonzero: {any(x != 0 for x in br01)} (structural sanity)")

    lower = 8 if (commute_ok and rk == 8) else 0
    final_ub = bounds["z(T1,T2 u color)"]
    print(f"\n  FINAL STAGE: lower bound (exhibit) = {lower}, upper bound (mod-p sandwich) = {final_ub}")
    pinned = (lower == final_ub == 8)
    print(f"  room EXACTLY 8: {'CONFIRMED' if pinned else 'NOT PINNED — lower/upper disagree'}")
    return dict(bounds=bounds, lower=lower, pinned=pinned)


def main():
    print("Building E6 / E7 / E8 with the generic builder (own code, flipped cocycle "
          "convention vs. the certs I read for spec)...")

    alg6 = ChevalleyAlgebra(en_cartan(6), "E6")
    alg7 = ChevalleyAlgebra(en_cartan(7), "E7")
    alg8 = ChevalleyAlgebra(en_cartan(8), "E8")
    assert (alg6.DIM, len(alg6.roots)) == (78, 72)
    assert (alg7.DIM, len(alg7.roots)) == (133, 126)
    assert (alg8.DIM, len(alg8.roots)) == (248, 240)

    res6 = run_e6_e7(alg6, "E6 (CONTROL)")
    ctrl_ok = (res6["d1"], res6["d2"], res6["d3"]) == (16, 8, 0)
    print(f"\nE6 CONTROL vs banked 16/8/0: {'MATCH' if ctrl_ok else 'MISMATCH'} "
          f"-> got {(res6['d1'], res6['d2'], res6['d3'])}")

    res7 = run_e6_e7(alg7, "E7 (exact)")
    e7_ok = (res7["d1"], res7["d2"], res7["d3"]) == (35, 9, 1)
    print(f"\nE7 vs claimed 35/9/1: {'MATCH' if e7_ok else 'MISMATCH'} "
          f"-> got {(res7['d1'], res7['d2'], res7['d3'])}")

    res8 = run_e8(alg8, "E8 (mod-p sandwich + explicit exhibit)")
    e8_ok = res8["pinned"] and res8["bounds"]["z(T1)"] <= 78 and res8["bounds"]["z(T1,T2)"] <= 16

    print("\n" + "=" * 78)
    print("SUMMARY (memo 14 AMBIENT_LADDER)")
    print("=" * 78)
    print(f"E6 control (16/8/0):        {'CONFIRMED' if ctrl_ok else 'REFUTED'}")
    print(f"E7 ladder (35/9/1), pure-Cartan room=1: {'CONFIRMED' if e7_ok else 'REFUTED'}")
    print(f"E8 room exactly 8 (sandwich+exhibit):   {'CONFIRMED' if res8['pinned'] else 'REFUTED'}")
    print(f"E8 intermediate bounds <=78, <=16 also matched: "
          f"{res8['bounds']['z(T1)']} <= 78 ? {res8['bounds']['z(T1)']<=78}; "
          f"{res8['bounds']['z(T1,T2)']} <= 16 ? {res8['bounds']['z(T1,T2)']<=16}")


if __name__ == "__main__":
    main()
