"""B666 cell 1 (L105) — the 2O/E7 silver-hearing conjecture, group side.

SEALED QUESTION (campaign prereg, wave 1 cell 1): the silver word RRLL
(trace 6, det(A+I)=8, disc 32, eigenvalue field Q(sqrt2)) should hear
the binary octahedral group 2O (order 48, E7's McKay partner, character
field Q(sqrt2)) at ITS OWN conductor — the mod-8 shadow — mirroring the
banked golden theorem (B640/B644: mod-5 shadow = SL(2,5) = 2I = E8's
partner).

THIS SCRIPT (exact integer/rational arithmetic throughout):
  A. the mod-n shadows <R,L> mod n for n = 2,4,5,7,8: order, order
     profile, involution count, center, exponent; verify the mod-8
     shadow equals full SL(2,Z/8) by enumeration. (mod 5 = the banked
     golden control: order 120, unique involution = 2I.)
  B. the binary octahedral group 2O built EXACTLY as 48 unit quaternions
     over Q(sqrt2): closure, order profile, unique involution, the
     2-dim character values 2*Re (the sqrt2 character).
  C. head-to-head: is the mod-8 shadow (or the mod-4 shadow, the unique
     order-48 congruence quotient) isomorphic to 2O? Complete
     generating-pair isomorphism search, not just invariants.
  D. the FULL normal-subgroup lattice of SL(2,Z/8) (single-class normal
     closures + join closure — every normal subgroup is a join of class
     closures); every order-8 normal subgroup -> its order-48 quotient
     -> complete iso test vs 2O.  DECIDES: is 2O a quotient of the
     mod-8 shadow at all?
  E. subgroup search: does 2O embed in SL(2,Z/8)?  (Search over
     (order-8, order-3) generating pairs; Q16 = the 2O Sylow-2 as a
     cheap necessary screen.)  POSITIVE CONTROL: the same detector on
     SL(2,7), where the preimage of S4 < PSL(2,7) is a genuine 2O —
     the detector must FIND it there.
  F. abelianization of SL(2,Z/8) (bounds 1-dim character values; a
     REDUCIBLE 2-dim rep can carry sqrt2 = zeta8 + zeta8^-1 only if
     8 | exp(G^ab)).
  G. export regular-representation permutation generators (JSON) for
     the independent GAP/sage corroboration (IdGroup + character table).

Two-outcome: 2O CONFIRMED / NOT-2O (bank the actual group).
Exact arithmetic only; no floats anywhere in this script.
"""
import json
import os
import sys
from fractions import Fraction
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------- generic
class FinGroup:
    """finite group given by element hashables + mul + inv + identity."""

    def __init__(self, name, elems, mul, inv, e):
        self.name, self.mul, self.inv, self.e = name, mul, inv, e
        self.elems = list(elems)
        self.index = {g: i for i, g in enumerate(self.elems)}
        self._ord = {}

    @classmethod
    def closure(cls, name, gens, mul, inv, e):
        seen = {e}
        frontier = [e]
        gens = list(gens)
        while frontier:
            nxt = []
            for g in frontier:
                for s in gens:
                    h = mul(g, s)
                    if h not in seen:
                        seen.add(h)
                        nxt.append(h)
            frontier = nxt
        return cls(name, sorted(seen), mul, inv, e)

    def order(self):
        return len(self.elems)

    def elt_order(self, g):
        if g in self._ord:
            return self._ord[g]
        k, h = 1, g
        while h != self.e:
            h = self.mul(h, g)
            k += 1
        self._ord[g] = k
        return k

    def order_profile(self):
        prof = {}
        for g in self.elems:
            o = self.elt_order(g)
            prof[o] = prof.get(o, 0) + 1
        return dict(sorted(prof.items()))

    def involutions(self):
        return [g for g in self.elems if g != self.e
                and self.mul(g, g) == self.e]

    def center(self):
        return [g for g in self.elems
                if all(self.mul(g, h) == self.mul(h, g)
                       for h in self.elems)]

    def exponent(self):
        from math import lcm
        ex = 1
        for g in self.elems:
            ex = lcm(ex, self.elt_order(g))
        return ex

    def subgroup_elems(self, gens):
        seen = {self.e}
        frontier = [self.e]
        gens = list(gens)
        while frontier:
            nxt = []
            for g in frontier:
                for s in gens:
                    h = self.mul(g, s)
                    if h not in seen:
                        seen.add(h)
                        nxt.append(h)
            frontier = nxt
        return frozenset(seen)

    def conjugacy_classes(self, gens):
        """classes as frozensets; conjugation orbits under generators."""
        left = set(self.elems)
        classes = []
        while left:
            g = min(left, key=lambda x: self.index[x])
            orb = {g}
            frontier = [g]
            while frontier:
                nxt = []
                for h in frontier:
                    for s in gens:
                        c = self.mul(self.mul(s, h), self.inv(s))
                        if c not in orb:
                            orb.add(c)
                            nxt.append(c)
                frontier = nxt
            classes.append(frozenset(orb))
            left -= orb
        return classes

    def derived_subgroup(self):
        comms = set()
        for g in self.elems:
            gi = self.inv(g)
            for h in self.elems:
                comms.add(self.mul(self.mul(g, h),
                                   self.mul(gi, self.inv(h))))
        return self.subgroup_elems(comms)

    def quotient(self, N):
        """N a frozenset (normal). Returns FinGroup on coset ids."""
        Nl = sorted(N, key=lambda x: self.index[x])
        coset_of = {}
        reps = []
        for g in self.elems:
            if g in coset_of:
                continue
            cid = len(reps)
            reps.append(g)
            for n in Nl:
                coset_of[self.mul(g, n)] = cid
        k = len(reps)
        table = [[coset_of[self.mul(reps[i], reps[j])] for j in range(k)]
                 for i in range(k)]
        itab = [None] * k
        for i in range(k):
            for j in range(k):
                if table[i][j] == coset_of[self.e]:
                    itab[i] = j
        mul = lambda a, b: table[a][b]
        inv = lambda a: itab[a]
        return FinGroup(self.name + "/N", range(k), mul, inv,
                        coset_of[self.e])

    def perm_gens(self, gens):
        """regular representation of gens as permutations (right mult)."""
        out = []
        for s in gens:
            out.append([self.index[self.mul(g, s)] for g in self.elems])
        return out


def find_generating_pair(G):
    by_ord = sorted(G.elems, key=lambda g: -G.elt_order(g))
    n = G.order()
    for g in by_ord:
        for h in by_ord:
            if len(G.subgroup_elems([g, h])) == n:
                return g, h
    return None


def iso_test(A, gensA, B):
    """complete: does an isomorphism A->B exist sending gensA to some
    pair in B? gensA must generate A. Searches ALL candidate pairs in B
    (order-matched), builds the map by BFS, verifies homomorphism on all
    pairs + bijectivity. Returns a witness pair or None."""
    a1, a2 = gensA
    o1, o2 = A.elt_order(a1), A.elt_order(a2)
    n = A.order()
    if n != B.order():
        return None
    cand1 = [x for x in B.elems if B.elt_order(x) == o1]
    cand2 = [x for x in B.elems if B.elt_order(x) == o2]
    # precompute BFS word structure on A once
    parent = {A.e: None}
    order_bfs = [A.e]
    frontier = [A.e]
    while frontier:
        nxt = []
        for g in frontier:
            for si, s in enumerate((a1, a2)):
                h = A.mul(g, s)
                if h not in parent:
                    parent[h] = (g, si)
                    order_bfs.append(h)
                    nxt.append(h)
        frontier = nxt
    if len(order_bfs) != n:
        raise ValueError("gensA do not generate A")
    for x in cand1:
        for y in cand2:
            f = {A.e: B.e}
            ok = True
            for g in order_bfs[1:]:
                p, si = parent[g]
                f[g] = B.mul(f[p], (x, y)[si])
            if len(set(f.values())) != n:
                continue
            for g in A.elems:
                fg = f[g]
                if any(f[A.mul(g, h)] != B.mul(fg, f[h])
                       for h in A.elems):
                    ok = False
                    break
            if ok:
                return (x, y)
    return None


# ------------------------------------------------------------- mod-n side
def sl2_shadow(n):
    R, L = (1, 1, 0, 1), (1, 0, 1, 1)

    def mul(x, y):
        return ((x[0] * y[0] + x[1] * y[2]) % n,
                (x[0] * y[1] + x[1] * y[3]) % n,
                (x[2] * y[0] + x[3] * y[2]) % n,
                (x[2] * y[1] + x[3] * y[3]) % n)

    def inv(x):
        a, b, c, d = x
        return (d % n, -b % n, -c % n, a % n)

    e = (1, 0, 0, 1)
    G = FinGroup.closure(f"<R,L> mod {n}", [R, L], mul, inv, e)
    return G, R, L


def full_sl2_count(n):
    cnt = 0
    for a, b, c, d in product(range(n), repeat=4):
        if (a * d - b * c) % n == 1:
            cnt += 1
    return cnt


# ---------------------------------------------------------- quaternion 2O
class Q2:  # a + b*sqrt2 with a,b Fraction
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = Fraction(a), Fraction(b)

    def __add__(s, o):
        return Q2(s.a + o.a, s.b + o.b)

    def __sub__(s, o):
        return Q2(s.a - o.a, s.b - o.b)

    def __mul__(s, o):
        return Q2(s.a * o.a + 2 * s.b * o.b, s.a * o.b + s.b * o.a)

    def __neg__(s):
        return Q2(-s.a, -s.b)

    def __eq__(s, o):
        return s.a == o.a and s.b == o.b

    def __hash__(s):
        return hash((s.a, s.b))

    def __lt__(s, o):
        return (s.a, s.b) < (o.a, o.b)

    def __repr__(s):
        if s.b == 0:
            return str(s.a)
        if s.a == 0:
            return f"{s.b}*sqrt2"
        return f"({s.a}+{s.b}*sqrt2)"


def qmul(p, q):
    w1, x1, y1, z1 = p
    w2, x2, y2, z2 = q
    return (w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2)


def qinv(p):  # unit quaternion: inverse = conjugate
    w, x, y, z = p
    return (w, -x, -y, -z)


def build_2O():
    half = Fraction(1, 2)
    om = (Q2(half), Q2(half), Q2(half), Q2(half))          # (1+i+j+k)/2
    s = (Q2(0, half), Q2(0, half), Q2(0), Q2(0))           # (1+i)/sqrt2
    e = (Q2(1), Q2(0), Q2(0), Q2(0))
    return FinGroup.closure("2O", [om, s], qmul, qinv, e), om, s, e


def main():
    print("B666 cell 1 — the mod-8 shadow vs the binary octahedral 2O")
    print("=" * 68)

    # ---- A. shadows
    shadows = {}
    for n in (2, 4, 5, 7, 8):
        G, R, L = sl2_shadow(n)
        shadows[n] = (G, R, L)
        prof = G.order_profile()
        invs = G.involutions()
        Z = G.center()
        print(f"\n[A] <R,L> mod {n}:  order {G.order()}   "
              f"(full |SL(2,Z/{n})| = {full_sl2_count(n)})")
        print(f"    order profile: {prof}")
        print(f"    involutions: {len(invs)}   center order: {len(Z)} "
              f"({sorted(Z)})   exponent: {G.exponent()}")
    G8, R8, L8 = shadows[8]
    ok_full = G8.order() == full_sl2_count(8)
    print(f"\n    mod-8 shadow = FULL SL(2,Z/8): {ok_full}")
    g5 = shadows[5][0]
    print(f"    GOLDEN CONTROL (banked B640/B644): mod-5 shadow order "
          f"{g5.order()} with {len(g5.involutions())} involution(s) "
          f"-> 2I = SL(2,5): "
          f"{g5.order() == 120 and len(g5.involutions()) == 1}")

    # ---- B. 2O exact
    O2, om, s, eq = build_2O()
    print(f"\n[B] 2O (exact quaternions over Q(sqrt2)): order "
          f"{O2.order()}")
    print(f"    order profile: {O2.order_profile()}")
    print(f"    involutions: {len(O2.involutions())} (unique = "
          f"{len(O2.involutions()) == 1})   center order: "
          f"{len(O2.center())}   exponent: {O2.exponent()}")
    tr_hist = {}
    for g in O2.elems:
        t = g[0] + g[0]  # 2*Re = trace of the 2-dim rep
        tr_hist[repr(t)] = tr_hist.get(repr(t), 0) + 1
    print(f"    2-dim character values (2*Re) histogram: "
          f"{dict(sorted(tr_hist.items()))}")
    sqrt2_traces = sum(v for k, v in tr_hist.items() if "sqrt2" in k)
    print(f"    sqrt2-valued traces: {sqrt2_traces} elements "
          f"(character field Q(sqrt2): {sqrt2_traces > 0})")

    # ---- C. head-to-head iso tests
    print("\n[C] head-to-head:")
    print(f"    |mod-8 shadow| = {G8.order()} vs |2O| = 48  ->  "
          f"ISOMORPHIC IMPOSSIBLE (order mismatch)" if G8.order() != 48
          else "    order match; testing...")
    G4 = shadows[4][0]
    gp4 = find_generating_pair(G4)
    w = iso_test(G4, gp4, O2)
    print(f"    mod-4 shadow (order {G4.order()}) ~ 2O ?  "
          f"{'ISO, witness ' + str(w) if w else 'NOT isomorphic (complete pair search)'}")
    print(f"      discriminating invariants: involutions "
          f"{len(G4.involutions())} vs {len(O2.involutions())}; "
          f"profile {G4.order_profile()} vs {O2.order_profile()}")

    # ---- D. normal-subgroup lattice of SL(2,Z/8)
    print("\n[D] the full normal-subgroup lattice of SL(2,Z/8):")
    classes = G8.conjugacy_classes([R8, L8])
    print(f"    conjugacy classes: {len(classes)}  sizes "
          f"{sorted(len(c) for c in classes)}")
    base = set()
    for c in classes:
        base.add(G8.subgroup_elems(c))
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
    orders = sorted(len(N) for N in lattice)
    print(f"    normal subgroups: {len(lattice)}  orders {orders}")
    n8 = [N for N in lattice if len(N) == 8]
    print(f"    order-8 normal subgroups (kernels of 48-quotients): "
          f"{len(n8)}")
    any_2O_quot = False
    for k, N in enumerate(n8):
        Q = G8.quotient(N)
        gpQ = find_generating_pair(Q)
        wq = iso_test(Q, gpQ, O2)
        same4 = iso_test(Q, gpQ, G4)
        print(f"      N#{k}: quotient order {Q.order()}, profile "
              f"{Q.order_profile()}, involutions {len(Q.involutions())}"
              f" -> ~2O? {'YES' if wq else 'no'}; ~SL(2,Z/4)? "
              f"{'yes' if same4 else 'no'}")
        if wq:
            any_2O_quot = True
    print(f"    ==> 2O IS A QUOTIENT OF THE MOD-8 SHADOW: "
          f"{any_2O_quot}")

    # ---- E. subgroup search (with positive control on SL(2,7))
    print("\n[E] does 2O EMBED in the shadow?")

    def find_2O_subgroup(G):
        o8 = [g for g in G.elems if G.elt_order(g) == 8]
        o3 = [g for g in G.elems if G.elt_order(g) == 3]
        print(f"      ({G.name}: {len(o8)} order-8, {len(o3)} order-3 "
              f"elements)")
        gp2O = find_generating_pair(O2)
        # 2O is generated by (order-8, order-3) pairs? verify on 2O:
        o8O = [g for g in O2.elems if O2.elt_order(g) == 8]
        o3O = [g for g in O2.elems if O2.elt_order(g) == 3]
        gen_ok = any(len(O2.subgroup_elems([x, y])) == 48
                     for x in o8O for y in o3O)
        for x in o8:
            for y in o3:
                H = G.subgroup_elems([x, y])
                if len(H) == 48:
                    Hg = FinGroup(G.name + ">H48", sorted(H), G.mul,
                                  G.inv, G.e)
                    gph = find_generating_pair(Hg)
                    if iso_test(Hg, gph, O2):
                        return (x, y), gen_ok
        return None, gen_ok

    G7 = shadows[7][0]
    hit7, gen_ok = find_2O_subgroup(G7)
    print(f"      2O generated by some (order-8, order-3) pair "
          f"(search-completeness premise): {gen_ok}")
    print(f"    POSITIVE CONTROL SL(2,7): 2O subgroup "
          f"{'FOUND at ' + str(hit7) if hit7 else 'NOT FOUND (detector broken!)'}")
    hit8, _ = find_2O_subgroup(G8)
    print(f"    SL(2,Z/8): 2O subgroup "
          f"{'FOUND at ' + str(hit8) if hit8 else 'NOT FOUND (complete search over (8,3)-pairs)'}")
    # Q16 screen (Sylow-2 of 2O is Q16: x^8=1, y2=x4, yxy^-1=x^-1)
    def has_Q16(G):
        o8 = [g for g in G.elems if G.elt_order(g) == 8]
        for x in o8:
            x4 = G.mul(G.mul(x, x), G.mul(x, x))
            xi = G.inv(x)
            for y in G.elems:
                if (G.mul(y, y) == x4 and
                        G.mul(G.mul(y, x), G.inv(y)) == xi and
                        len(G.subgroup_elems([x, y])) == 16):
                    return (x, y)
        return None
    q16 = has_Q16(G8)
    print(f"    Q16 (= 2O's Sylow-2) inside SL(2,Z/8): "
          f"{'present at ' + str(q16) if q16 else 'ABSENT'}")

    # ---- F. abelianization
    D = G8.derived_subgroup()
    Ab = G8.quotient(D)
    print(f"\n[F] [G,G] order {len(D)}; G^ab order {Ab.order()}, "
          f"exponent {Ab.exponent()}, profile {Ab.order_profile()}")
    print(f"    8 | exp(G^ab): {Ab.exponent() % 8 == 0}  "
          f"(if False, no REDUCIBLE 2-dim rep can carry sqrt2)")

    # ---- G. export for GAP/sage corroboration
    out = {}
    out["mod8"] = {"n": G8.order(),
                   "gens": G8.perm_gens([R8, L8])}
    out["mod4"] = {"n": G4.order(),
                   "gens": G4.perm_gens([shadows[4][1], shadows[4][2]])}
    out["2O"] = {"n": O2.order(), "gens": O2.perm_gens([om, s])}
    for k, N in enumerate(n8):
        Q = G8.quotient(N)
        gq = find_generating_pair(Q)
        out[f"quot48_{k}"] = {"n": Q.order(), "gens": Q.perm_gens(list(gq))}
    with open(os.path.join(HERE, "b666c1_groups.json"), "w") as f:
        json.dump(out, f)
    print("\n[G] exported regular-rep permutation generators -> "
          "b666c1_groups.json")

    # ---- verdict (group side)
    print("\n" + "=" * 68)
    print("GROUP-SIDE VERDICT:")
    print(f"  the silver mod-8 shadow = SL(2,Z/8), order {G8.order()} "
          f"(not 48);")
    print(f"  mod-4 shadow ~ 2O: {'YES' if w else 'NO'};  "
          f"2O as quotient: {any_2O_quot};  2O as subgroup: "
          f"{bool(hit8)}")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
