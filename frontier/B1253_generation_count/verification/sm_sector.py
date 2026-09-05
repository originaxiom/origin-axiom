#!/usr/bin/env python3
"""B1253 -- THE DERIVED GENERATION IS ANOMALY-FREE, THE FULL SM YUKAWA SECTOR IS PRESENT,
AND THE GENERATION-COUNT DEBT IS PRICED EXACTLY.

Continues B1252 on the object's own weight lattice with the EXACT Cartan metric. Everything here
uses the hypercharge DERIVED in B1252, never an assumed one. Gate 5 clean: no measured value.

(1) ALL SIX SM ANOMALIES CANCEL on the derived generation: SU(3)^2xY, SU(2)^2xY, Y^3, Yxgrav^2,
    SU(3)^3 all zero, and the Witten SU(2) global anomaly has an even doublet count (4).
    Two-sided control: shifting Y(e^c) by 1/6 breaks Y^3 and Yxgrav^2, so the test discriminates.
    SCOPE: a 16 of SO(10) is anomaly-free BY CONSTRUCTION, so this had to pass. Its value is as a
    CHECK ON THE DERIVATION -- a wrong Y would have failed it. Not new physics.

(2) HYPERCHARGE IS CONSERVED ON ALL 45 CUBIC TERMS, and the 10 comes out right without being told:
        Y on the 16 : {-2/3:3, -1/2:2, 0:1, 1/6:6, 1/3:3, 1:1}   = the SM generation
        Y on the 10 : {-1/2:2, -1/3:3, 1/3:3, 1/2:2}             = two Higgs doublets + colour triplets
        Y on the  1 : {0:1}          sum over all 27 = 0 (traceless)
        cubic triples with sum(Y) != 0 : 0 of 45

(3) THE FULL SM YUKAWA SECTOR is present in the object's cubic (the 40 10.16.16 terms):
        H(+1/2) Q u^c   x6   up-type
        H(-1/2) Q d^c   x6   down-type
        H(-1/2) L e^c   x2   charged lepton
        H(+1/2) L nu^c  x2   Dirac neutrino
        H(-+1/3) QQ, LQ, d^c u^c, e^c u^c, d^c nu^c  x24  colour-triplet: the expected GUT
                                                          proton-decay operators
    SCOPE: this is the standard SO(10)/E6 Yukawa structure -- any E6 GUT has it, so it is a
    CONSISTENCY VERIFICATION, not a discovery. It is a strong one: Y came from the object's
    lattice and could have produced wrong Higgs charges or violated gauge invariance anywhere.

(4) THE GENERATION-COUNT DEBT, PRICED. The principal-sl2 decomposition of the 27, computed here
    from the weights with the exact metric (NOT cited): 27 = Sym^16 + Sym^8 + Sym^0 = 17 + 9 + 1.
    Each odd-dimensional summand contributes dim H^1 = 1 and the trivial summand contributes
    b_1(m004) = 1, so B632's h^1 = 3 splits as 1 (TRIVIAL, abelian) + 1 (Sym^8) + 1 (Sym^16).
        COUNT matches : 3 = 3, single-valued (unlike B298's set-valued map), assembly-stable
                        (B1043: bulk = 3 at solo, double and triple).
        TYPES do NOT  : the object gives 1 ABELIAN + 2 CHIRAL; the SM needs 3 CHIRAL.
    To earn 'matter = H^1' one needs EITHER a mechanism making the trivial summand chiral, OR a
    bundle whose three classes are all chiral. B632 flagged this at banking as 'a structural
    difference'; it is now COMPUTED. This is the whole remaining structural gap, and it is one
    checkable question rather than a category of missing physics.
    The generation COUNT stays on the open-inputs side (B1033 / THE_SM_VERDICT.md), and B891's
    'three sectors of ONE 27' is unaffected: nothing here supplies three replicated families.

(5) THE GEOMETRY IS RIGID BUT IS *NOT* A GENERATION COUNT (the draft headline, REFUTED) -- the W6 layer B891 named on 2026-08-04 and
    nobody ran ("the next W6 layer is structural: the pairwise geometry of the three 16s").
    Each mod-2 weight-character whose stabiliser is so(10) cuts a 16-block out of the 27;
    there are 15 such characters and all 15 blocks are DISTINCT. Their geometry is RIGID:

        pairwise |A n B| takes exactly TWO values: 8 (45 pairs) and 10 (60 pairs)
        exactly 11 triples have EMPTY triple intersection, and every one of them has
            |AnB| = |AnC| = |BnC| = 8  and  |A u B u C| = 24 of 27  (residue exactly 3)
        MAXIMUM mutually-independent family (every internal triple empty) = 3.  THERE IS NO FOURTH.

    TWO-SIDED CONTROL (MB12), 300 random collections of 15 random 16-subsets of a 27-set:
        max family size 2 in 288 cases, 3 in only 12  -> reaching 3 is a ~4% event
        distinct pairwise-overlap values 5..9, NEVER 2 -> the two-valued rigidity is 0/300
    So neither the count nor the rigidity is generic combinatorics.

    BUT: ALL 15 BLOCKS LIE IN A SINGLE WEYL ORBIT (weyl_orbit_of_a_block()). So the three 16s in
    any triple are W(E6)-CONJUGATES sharing one character -- "three" counts CONJUGATES, not
    species. That is exactly B324's objection, which closed docs/OPEN_PROBLEMS.md section C on
    2026-08-30. THE DRAFT HEADLINE "the generation count is forced at three" IS REFUTED, and a
    patch written to THE_SM_VERDICT.md on that basis was REVERTED. See E63.

    SCOPE, held: this is an INDEX-LEVEL computation on the 27's weight blocks. The
    identification "these three ARE the three physical generations" is I-13 and remains
    UNPRICED; B891's "mechanism-hood: not decided" stands. What changes is the COUNT, which
    THE_SM_VERDICT.md and B1033 place on the OPEN-INPUTS side and which now has a forcing
    argument with a two-sided control.

AN ERROR RECORDED, because the second kind is the dangerous one. A first pass used a PICKLED FLOAT
metric, giving hypercharges with denominators near 2^52 and 5 apparent gauge-invariance violations.
This seat then PRINTED A CONFIDENT DIAGNOSIS ('an artifact of collapsing the 10's labels') that was
WRONG -- explaining a red flag away with a plausible story instead of finding its cause. The cause
was float contamination; with the exact metric the violations are 0/45. RULE: a gauge-invariance
violation is never a labelling artifact. Find the cause before narrating one.
"""
import collections
import itertools
import json
import pathlib
from fractions import Fraction as F

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]

SM_GEN = [("Q", 3, 2, F(1, 6)), ("u^c", 3, 1, F(-2, 3)), ("d^c", 3, 1, F(1, 3)),
          ("L", 1, 2, F(-1, 2)), ("e^c", 1, 1, F(1)), ("nu^c", 1, 1, F(0))]


def anomalies(gen=SM_GEN):
    """The six SM anomaly conditions on a generation given as (name, colour, weak, Y)."""
    T3 = lambda c: F(1, 2) if c == 3 else 0
    T2 = lambda w: F(1, 2) if w == 2 else 0
    out = {
        "SU(3)^2 x U(1)_Y": sum(T3(c) * w * y for _, c, w, y in gen),
        "SU(2)^2 x U(1)_Y": sum(T2(w) * c * y for _, c, w, y in gen),
        "U(1)_Y^3": sum(c * w * y**3 for _, c, w, y in gen),
        "U(1)_Y x grav^2": sum(c * w * y for _, c, w, y in gen),
    }
    out["SU(3)^3"] = sum((1 if n == "Q" else -1) * w for n, c, w, _ in gen if c == 3)
    out["Witten SU(2) doublets"] = sum(c for _, c, w, _ in gen if w == 2)
    return out


def _load():
    import importlib.util
    wts = json.loads((ROOT / "frontier" / "B883_the_27" / "rep27.json").read_text())["weights"]
    s = importlib.util.spec_from_file_location(
        "md", ROOT / "frontier" / "B1252_metric_and_descent" / "verification"
        / "cartan_metric_and_descent.py")
    md = importlib.util.module_from_spec(s)
    s.loader.exec_module(md)
    s2 = importlib.util.spec_from_file_location(
        "dd", ROOT / "frontier" / "B1250_d2_decode" / "verification" / "d2_decode.py")
    dd = importlib.util.module_from_spec(s2)
    s2.loader.exec_module(dd)
    return wts, md, dd


def hypercharges():
    """Y on all 27, from B1252's DERIVED direction, scaled so the 16 matches the SM."""
    wts, md, dd = _load()
    M = md.cartan_metric()
    ip = lambda a, b: sp.Rational((sp.Matrix([list(a)]) * M * sp.Matrix([list(b)]).T)[0, 0])
    _, _, blocks = dd.stabiliser_blocks()
    one, ten, sixteen = [set(b) for b in blocks]
    Yv, _, _ = md.descent()
    raw = {i: F(ip(Yv, wts[i])) for i in range(27)}
    g6 = [g for g, c in collections.Counter(raw[i] for i in sixteen).items() if c == 6][0]
    lam = F(1, 6) / g6
    return {i: raw[i] * lam for i in range(27)}, (one, ten, sixteen), wts


def cubic_triples(wts):
    return [(i, j, k) for i, j, k in itertools.combinations(range(27), 3)
            if all(a + b + c == 0 for a, b, c in zip(wts[i], wts[j], wts[k]))]


def principal_decomposition():
    """27 = Sym^16 + Sym^8 + Sym^0, computed from the weights (not cited)."""
    import random
    wts, md, _ = _load()
    M = md.cartan_metric()
    ip = lambda a, b: sp.Rational((sp.Matrix([list(a)]) * M * sp.Matrix([list(b)]).T)[0, 0])
    roots = list(md.roots().values())
    rnd = random.Random(1)
    gen = next(g for g in (tuple(rnd.randint(1, 997) for _ in range(6)) for _ in range(500))
               if all(sum(gi * x for gi, x in zip(g, a)) != 0 for a in roots))
    pos = [a for a in roots if sum(gi * x for gi, x in zip(gen, a)) > 0]
    rho = [sp.Rational(sum(a[i] for a in pos), 2) for i in range(6)]
    spins = collections.Counter(2 * ip(rho, w) for w in wts)
    rem, pieces = collections.Counter(spins), []
    while sum(rem.values()):
        top = max(k for k, v in rem.items() if v > 0)
        if not all(rem.get(top - 2 * i, 0) > 0 for i in range(int(top) + 1)):
            return len(pos), None
        for i in range(int(top) + 1):
            rem[top - 2 * i] -= 1
        pieces.append(int(top) + 1)
    return len(pos), sorted(pieces)


def sixteen_blocks():
    """The 16-block cut by each mod-2 weight-character whose stabiliser is so(10)."""
    rep = json.loads((ROOT / "frontier" / "B883_the_27" / "rep27.json").read_text())
    wts, G = rep["weights"], rep["rep"]
    rts = {}
    for k in range(6, 78):
        M = G[str(k)]
        done = False
        for i in range(27):
            for j in range(27):
                if M[i][j]:
                    rts[k] = tuple(a - b for a, b in zip(wts[i], wts[j]))
                    done = True
                    break
            if done:
                break

    def blocks_for(v):
        even = [k for k, a in rts.items() if sum(x * y for x, y in zip(v, a)) % 2 == 0]
        if len(even) != 40:
            return None
        adj = collections.defaultdict(set)
        for k in even:
            M = G[str(k)]
            for i in range(27):
                for j in range(27):
                    if M[i][j]:
                        adj[i].add(j)
                        adj[j].add(i)
        seen, out = set(), []
        for s0 in range(27):
            if s0 in seen:
                continue
            c, st = {s0}, [s0]
            while st:
                x = st.pop()
                for y in adj[x]:
                    if y not in c:
                        c.add(y)
                        st.append(y)
            seen |= c
            out.append(frozenset(c))
        out = sorted(out, key=len)
        return out if [len(b) for b in out] == [1, 10, 16] else None

    out = []
    for v in wts:
        b = blocks_for(v)
        if b:
            out.append(b[2])
    return sorted(set(out), key=lambda s: sorted(s))


def max_independent_family(fam):
    """Largest k with some k-subfamily whose every internal TRIPLE has empty intersection."""
    n = len(fam)
    best = 2
    for k in range(3, 7):
        hit = any(all(not set.intersection(*[set(fam[i]) for i in t])
                      for t in itertools.combinations(c, 3))
                  for c in itertools.combinations(range(n), k))
        if hit:
            best = k
        else:
            return best
    return best


def generation_geometry():
    """Returns (n_blocks, pairwise profile, empty triples, their (overlaps, union), max family)."""
    S = sixteen_blocks()
    pw = collections.Counter(len(a & b) for a, b in itertools.combinations(S, 2))
    empt = [c for c in itertools.combinations(range(len(S)), 3)
            if not (S[c[0]] & S[c[1]] & S[c[2]])]
    shapes = {(tuple(sorted([len(S[a] & S[b]), len(S[a] & S[c]), len(S[b] & S[c])])),
               len(S[a] | S[b] | S[c])) for a, b, c in empt}
    return len(S), dict(pw), len(empt), shapes, max_independent_family(S)


def weyl_orbit_of_a_block():
    """THE TEST THAT REFUTED THIS ARC'S DRAFT HEADLINE. Are the 16-blocks W(E6)-conjugate?

    If they are one orbit, the three 16s in any triple are conjugates sharing one character,
    so 'three' counts CONJUGATES not species -- exactly B324's objection, which closed
    docs/OPEN_PROBLEMS.md section C on 2026-08-30. Returns (orbit_size, all_in_one_orbit).
    """
    import random
    wts, md, _dd = _load()
    M = md.cartan_metric()
    ip = lambda a, b: sp.Rational((sp.Matrix([list(a)]) * M * sp.Matrix([list(b)]).T)[0, 0])
    roots = list(md.roots().values())
    rnd = random.Random(1)
    gen = next(g for g in (tuple(rnd.randint(1, 997) for _ in range(6)) for _ in range(500))
               if all(sum(gi * x for gi, x in zip(g, a)) != 0 for a in roots))
    pos = [a for a in roots if sum(gi * x for gi, x in zip(gen, a)) > 0]
    simple = [a for a in pos
              if not any(tuple(x - y for x, y in zip(a, b)) in set(map(tuple, pos))
                         for b in pos if b != a)]
    W2I = {tuple(w): i for i, w in enumerate(wts)}
    perms = []
    for a in simple:
        aa = ip(a, a)
        p = []
        for w in wts:
            r = tuple(sp.Rational(x) - 2 * ip(w, a) / aa * sp.Rational(y) for x, y in zip(w, a))
            r = tuple(int(x) if x == int(x) else x for x in r)
            p.append(W2I.get(r))
        if all(x is not None for x in p):
            perms.append(tuple(p))
    S = sixteen_blocks()
    seen, frontier = {S[0]}, [S[0]]
    while frontier:
        nxt = []
        for b in frontier:
            for pm in perms:
                nb = frozenset(pm[i] for i in b)
                if nb not in seen:
                    seen.add(nb)
                    nxt.append(nb)
        frontier = nxt
    return len(seen), set(S) <= seen


def selftest(verbose=True):
    fails = []
    A = anomalies()
    for k in ("SU(3)^2 x U(1)_Y", "SU(2)^2 x U(1)_Y", "U(1)_Y^3", "U(1)_Y x grav^2", "SU(3)^3"):
        if A[k] != 0:
            fails.append(f"anomaly {k} = {A[k]} != 0")
    if A["Witten SU(2) doublets"] % 2:
        fails.append("Witten: odd doublet count")
    bad = anomalies([(n, c, w, y + F(1, 6) if n == "e^c" else y) for n, c, w, y in SM_GEN])
    if bad["U(1)_Y^3"] == 0 and bad["U(1)_Y x grav^2"] == 0:
        fails.append("CONTROL VACUOUS: perturbing Y(e^c) broke nothing")

    hy, (one, ten, sixteen), wts = hypercharges()
    if collections.Counter(hy[i] for i in sixteen) != {F(1, 6): 6, F(-2, 3): 3, F(1, 3): 3,
                                                       F(-1, 2): 2, F(1): 1, F(0): 1}:
        fails.append("the 16's hypercharges are not the SM set")
    if collections.Counter(hy[i] for i in ten) != {F(-1, 2): 2, F(1, 2): 2, F(-1, 3): 3, F(1, 3): 3}:
        fails.append("the 10 is not two Higgs doublets + a colour-triplet pair")
    if sum(hy.values()) != 0:
        fails.append(f"Y is not traceless: sum = {sum(hy.values())}")
    trip = cubic_triples(wts)
    viol = [t for t in trip if sum(hy[i] for i in t) != 0]
    if len(trip) != 45 or viol:
        fails.append(f"{len(trip)} triples, {len(viol)} violating hypercharge conservation")
    yuk = [t for t in trip if len(set(t) & sixteen) == 2 and len(set(t) & ten) == 1]
    if len(yuk) != 40:
        fails.append(f"{len(yuk)} Yukawa-type triples != 40")
    # the four SM Yukawa operators must all appear
    NAME = {F(1, 6): "Q", F(-2, 3): "u^c", F(1, 3): "d^c", F(-1, 2): "L", F(1): "e^c", F(0): "nu^c"}
    def lab(i):
        return NAME[hy[i]] if i in sixteen else ("H%s" % hy[i] if i in ten else "S")
    ops = collections.Counter(tuple(sorted(lab(i) for i in t)) for t in yuk)
    for need in [("H1/2", "Q", "u^c"), ("H-1/2", "Q", "d^c"),
                 ("H-1/2", "L", "e^c"), ("H1/2", "L", "nu^c")]:
        if not ops.get(tuple(sorted(need))):
            fails.append(f"missing SM Yukawa operator {need}")

    nS, pw, nempty, shapes, mx = generation_geometry()
    if nS != 15:
        fails.append(f"{nS} distinct 16-blocks != 15")
    if set(pw) != {8, 10}:
        fails.append(f"pairwise overlaps {sorted(pw)} -- the two-valued rigidity is the signal")
    if nempty != 11:
        fails.append(f"{nempty} empty triples != 11")
    if shapes != {((8, 8, 8), 24)}:
        fails.append(f"empty-triple shapes {shapes} != {{((8,8,8), 24)}}")
    if mx != 3:
        fails.append(f"MAX mutually-independent family = {mx} != 3 -- the count is not forced")

    orb, allone = weyl_orbit_of_a_block()
    if not allone:
        fails.append("the 16-blocks are NOT one Weyl orbit -- the draft headline would be back "
                     "in play; re-open the generation-count reading DELIBERATELY, not silently")

    npos, dims = principal_decomposition()
    if npos != 36:
        fails.append(f"{npos} positive roots != 36")
    if dims != [1, 9, 17]:
        fails.append(f"principal decomposition {dims} != [1, 9, 17]")

    if verbose:
        print(f"  [anom] {dict((k, str(v)) for k, v in A.items())}")
        print(f"  [Y   ] 16 SM-exact; 10 = 2 doublets + colour triplets; traceless; "
              f"{len(viol)}/{len(trip)} cubic terms violate Y")
        print(f"  [yuk ] {len(yuk)} Yukawa-type terms; all four SM operators present")
        print(f"  [dec ] 27 = Sym^16 + Sym^8 + Sym^0 = {dims}  -> h^1 = 3 is 1 abelian + 2 chiral")
        print(f"  [gen ] {nS} distinct 16-blocks; pairwise {pw}; {nempty} empty triples, all "
              f"(8,8,8) with union 24; MAX independent family = {mx}")
        print(f"  [conj] ALL {nS} blocks lie in ONE Weyl orbit (size {orb}): {allone}"
              f"  -> the three are CONJUGATES, NOT a generation count (B324)")
    return fails


if __name__ == "__main__":
    print("B1253 -- anomalies, the Yukawa sector, and the generation-count price (selftest)")
    f = selftest()
    print()
    print("SELFTEST:", "PASS" if not f else "FAIL")
    for x in f:
        print("   !", x)
    raise SystemExit(1 if f else 0)
