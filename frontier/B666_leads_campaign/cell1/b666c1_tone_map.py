"""B666 cell 1 (L105) — the explicit 2O quotient of the mod-8 shadow.

Script 1 (b666c1_shadow_group.py) proved exactly: SL(2,Z/8) has three
order-8 normal subgroups; one quotient is isomorphic to 2O. Here we
make the octahedral hearing map EXPLICIT and EXACT:

  pi : SL(2,Z) --mod 8--> SL(2,Z/8) --/N--> 2O  in SU(2) over Q(sqrt2)

- identify N (the kernel) elementwise; compare with K(4) = ker(mod-8
  -> mod-4);
- verify pi is a homomorphism on ALL 384^2 pairs (exact);
- exact 2-dim character values chi(pi(w)) = 2*Re for the letters and
  the metallic words (RL golden, RRLL silver, R^2L, R^3L, RRRLLL);
  plus the Galois-conjugate character (sqrt2 -> -sqrt2);
- the orders of pi(R), pi(L), pi(RRLL) in 2O.

Everything exact (Fractions over Q(sqrt2)); no floats.
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "c1", os.path.join(HERE, "b666c1_shadow_group.py"))
c1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c1)


def word_mat(word, n):
    R, L = (1, 1, 0, 1), (1, 0, 1, 1)
    G, _, _ = c1.sl2_shadow(n)  # for mul
    m = (1, 0, 0, 1)
    for ch in word:
        m = G.mul(m, R if ch == "R" else L)
    return m


def main():
    print("B666 cell 1 — the explicit octahedral hearing map pi")
    print("=" * 68)
    G8, R8, L8 = c1.sl2_shadow(8)
    O2, om, s, e2 = c1.build_2O()

    # order-8 normal subgroups again
    classes = G8.conjugacy_classes([R8, L8])
    base = set()
    for cl in classes:
        base.add(G8.subgroup_elems(cl))
    lattice = set(base)
    lattice.add(frozenset({G8.e}))
    changed = True
    while changed:
        changed = False
        cur = list(lattice)
        for i in range(len(cur)):
            for j in range(i + 1, len(cur)):
                J = G8.subgroup_elems(cur[i] | cur[j])
                if J not in lattice:
                    lattice.add(J)
                    changed = True
    n8 = sorted((N for N in lattice if len(N) == 8),
                key=lambda N: sorted(N))
    K4 = frozenset(g for g in G8.elems
                   if all(x % 4 == y for x, y in
                          zip(g, (1, 0, 0, 1))))
    print(f"K(4) = ker(mod4) elements: {sorted(K4)}")

    target = None
    for N in n8:
        Q = G8.quotient(N)
        if len(Q.involutions()) == 1:  # the 2O candidate (script-1 fact)
            target = N
    assert target is not None
    print(f"\nTHE KERNEL N (quotient = 2O), 8 elements:")
    for g in sorted(target):
        print(f"    [[{g[0]},{g[1]}],[{g[2]},{g[3]}]]  "
              f"(order {G8.elt_order(g)})")
    print(f"N == K(4)? {target == K4}")
    print(f"N ∩ K(4) size: {len(target & K4)}")
    print(f"-I=[[7,0],[0,7]] in N? {(7, 0, 0, 7) in target}")
    print(f"5I in N? {(5, 0, 0, 5) in target}")

    # quotient + explicit iso to 2O
    Q = G8.quotient(target)
    gpQ = c1.find_generating_pair(Q)
    wit = c1.iso_test(Q, gpQ, O2)
    assert wit is not None
    # rebuild the BFS map f: Q -> 2O
    a1, a2 = gpQ
    parent = {Q.e: None}
    order_bfs = [Q.e]
    frontier = [Q.e]
    while frontier:
        nxt = []
        for g in frontier:
            for si, sg in enumerate((a1, a2)):
                h = Q.mul(g, sg)
                if h not in parent:
                    parent[h] = (g, si)
                    order_bfs.append(h)
                    nxt.append(h)
        frontier = nxt
    f = {Q.e: e2}
    for g in order_bfs[1:]:
        p, si = parent[g]
        f[g] = c1.qmul(f[p], wit[si])

    # coset map G8 -> Q ids
    Nl = sorted(target, key=lambda x: G8.index[x])
    coset_of = {}
    reps = []
    for g in G8.elems:
        if g in coset_of:
            continue
        cid = len(reps)
        reps.append(g)
        for nn in Nl:
            coset_of[G8.mul(g, nn)] = cid

    def pi(g):
        return f[coset_of[g]]

    # verify pi is a homomorphism on all pairs (exact, complete)
    bad = 0
    for g in G8.elems:
        pg = pi(g)
        for h in G8.elems:
            if pi(G8.mul(g, h)) != c1.qmul(pg, pi(h)):
                bad += 1
    print(f"\npi homomorphism check on all 384^2 pairs: "
          f"{'PASS (0 failures)' if bad == 0 else f'FAIL ({bad})'}")
    img = {pi(g) for g in G8.elems}
    print(f"pi surjective onto 2O: {len(img) == 48}")

    def chi(q):  # 2-dim character = 2*Re
        return q[0] + q[0]

    def gal(x):  # sqrt2 -> -sqrt2 on Q2
        return c1.Q2(x.a, -x.b)

    print("\nletters and words under the octahedral character "
          "(chi = 2*Re, exact):")
    words = ["R", "L", "RL", "RRLL", "RRL", "RRRL", "RRRLLL",
             "RRLLRRLL", "RLRL"]
    for wname in words:
        m8 = word_mat(wname, 8)
        q = pi(m8)
        o8 = G8.elt_order(m8)
        oO = O2.elt_order(q)
        print(f"    {wname:>8}: mod8 [[{m8[0]},{m8[1]}],[{m8[2]},{m8[3]}]]"
              f" ord {o8:>2} -> 2O ord {oO:>2}   chi = {chi(q)}   "
              f"chi_gal = {gal(chi(q))}")

    m_silver = word_mat("RRLL", 8)
    q_silver = pi(m_silver)
    print(f"\nTHE SILVER WORD RRLL: mod-8 matrix "
          f"[[{m_silver[0]},{m_silver[1]}],[{m_silver[2]},{m_silver[3]}]]")
    print(f"    quaternion image: {q_silver}")
    print(f"    order in 2O: {O2.elt_order(q_silver)}")
    print(f"    chi(RRLL) = {chi(q_silver)}   "
          f"(Galois pair: {gal(chi(q_silver))})")
    sq = chi(q_silver)
    is_s2 = (sq.a == 0 and sq.b != 0)
    print(f"    chi(RRLL) is a pure sqrt2 multiple: {is_s2}")

    # golden comparison line
    print("\n(the golden banked analog: mod-5 shadow = 2I itself; "
          "tr rho(RL) = -1/phi.")
    print(" the silver refined analog: mod-8 shadow ->> 2O with "
          "kernel N; chi(pi(RRLL)) above.)")


if __name__ == "__main__":
    main()
