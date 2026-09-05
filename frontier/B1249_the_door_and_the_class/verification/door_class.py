#!/usr/bin/env python3
"""B1249 -- WHAT THE McKAY DOOR DOES TO THE RELATIONAL CLASS.

B1248 gave the law: det X0 = squarefree(2 - kappa), kappa = tr[A,M] the Fricke-Vogt invariant.
This arc fires it at the chain's own door, pi_1(m004) ->> 2T ->> (McKay) E6.

COMPUTED HERE, all exact, no floats:
  (1) 2T built by closure from (i, j, omega); order 24; trace spectrum {-2,-1,0,1,2}.
  (2) THE FULL kappa SPECTRUM OF 2T over all 576 pairs is exactly {-2, 0, 2}. Nothing else.
      Hence 2 - kappa in {4, 2, 0} and the class D in {+1, 2, 0}: the class -1 -- THE BIT --
      NEVER OCCURS ANYWHERE IN 2T.
  (3) The fig-8 relator w x w^-1 = y (w = x^-1 y x y^-1) has 72 solutions in 2T, of which
      48 GENERATE (are surjections) and 24 are not. The 48 REPRODUCES THE BANKED COUNT
      (B237/B1019/B997) independently, from the relator alone.
  (4) All 48 surjections give kappa = 0 -- BUT SO DOES EVERY GENERATING PAIR.

      THE ATTRIBUTION THAT FAILED, recorded rather than dropped. A draft headlined
      "all 48 surjections give kappa = 0, so THE DOOR is not class-preserving". The
      discriminating control refutes it: ALL 384 GENERATING PAIRS of 2T already have
      kappa = 0, so the fig-8 relator CUTS NOTHING and kappa = 0 on the surjections is
      a fact about GENERATION IN 2T, not about the relator or the door.
      Correct statement, weaker and general: any surjection from any group onto 2T sends
      a generating pair to class D = 2; with (2), 2T CANNOT CARRY THE BIT HOWEVER ONE
      MAPS INTO IT. generating_pair_census() keeps this control permanent.

  (5) RAMIFICATION -- TWO FACTS, NO MAP BETWEEN THEM. The object's algebra (5,-5) is split
      everywhere; 2T's is (-1,-1), the HURWITZ quaternions, ramified at exactly {2, oo}.
      A draft said "the door ADDS ramification": REMOVED. No map between the two algebras
      is exhibited, so a causal reading is exactly the T-IDENTIFICATION-IS-AN-INPUT error.
      The two facts stand side by side; nothing is claimed to flow between them.

NOT CLAIMED: that SU(2) is derived. 2T sits inside SU(2) BY CONSTRUCTION, so its algebra
being the Hamiltonians is a property of that construction, not an output of the chain.
kappa is not a homomorphism invariant. No measured physical value. Gate 5 clean.
"""
import collections
import itertools

import sympy as sp
from sympy.functions.combinatorial.numbers import legendre_symbol

ONE = sp.eye(2)


def _key(m):
    return sp.ImmutableMatrix(sp.simplify(sp.expand(m)))


def build_2T():
    """Binary tetrahedral group by closure. Returns (elements, mul, inv, trace, identity)."""
    i_ = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    j_ = sp.Matrix([[0, 1], [-1, 0]])
    w0 = sp.simplify((-ONE + i_ + j_ + sp.simplify(i_ * j_)) / 2)
    els, seen, frontier = [ONE], {_key(ONE): 0}, [ONE]
    while frontier:
        nxt = []
        for m in frontier:
            for g in (i_, j_, w0):
                k = _key(m * g)
                if k not in seen:
                    seen[k] = len(els)
                    els.append(sp.Matrix(k))
                    nxt.append(sp.Matrix(k))
        frontier = nxt
    n = len(els)
    mul = [[seen[_key(els[a] * els[b])] for b in range(n)] for a in range(n)]
    e = seen[_key(ONE)]
    inv = [next(b for b in range(n) if mul[a][b] == e) for a in range(n)]
    tr = [sp.nsimplify(sp.simplify(sp.trace(m))) for m in els]
    return els, mul, inv, tr, e


def _word(mul, e, *ix):
    r = e
    for a in ix:
        r = mul[r][a]
    return r


def _generates(mul, inv, e, n, x, y):
    seen, frontier = {e}, [e]
    while frontier:
        nxt = []
        for m in frontier:
            for g in (x, y, inv[x], inv[y]):
                p = mul[m][g]
                if p not in seen:
                    seen.add(p)
                    nxt.append(p)
        frontier = nxt
    return len(seen)


def door_census():
    """Returns (order, kappa_spectrum_all_pairs, n_relator, n_surjective, kappa_on_surjections)."""
    els, mul, inv, tr, e = build_2T()
    n = len(els)
    kap = lambda x, y: tr[_word(mul, e, x, y, inv[x], inv[y])]
    allspec = collections.Counter(kap(x, y) for x in range(n) for y in range(n))
    surj, rel = [], 0
    for x, y in itertools.product(range(n), range(n)):
        w = _word(mul, e, inv[x], y, x, inv[y])
        if _word(mul, e, w, x, inv[w]) != y:
            continue
        rel += 1
        if _generates(mul, inv, e, n, x, y) == n:
            surj.append((x, y))
    return n, dict(allspec), rel, len(surj), collections.Counter(kap(x, y) for x, y in surj)


def generating_pair_census():
    """THE CONTROL THAT REFUTED THIS ARC'S DRAFT HEADLINE.

    Returns (n_generating, kappa_spectrum_of_generating_pairs). If the generating pairs
    already have the same spectrum as the relator-satisfying ones, then the relator
    discriminates NOTHING and no door-specific claim may be made.
    """
    els, mul, inv, tr, e = build_2T()
    n = len(els)
    kap = lambda x, y: tr[_word(mul, e, x, y, inv[x], inv[y])]
    gen = [(x, y) for x in range(n) for y in range(n)
           if _generates(mul, inv, e, n, x, y) == n]
    return len(gen), collections.Counter(kap(x, y) for x, y in gen)


def hilbert(a, b, p):
    """Hilbert symbol (a,b)_p over Q; p = 0 denotes the real place."""
    a, b = int(a), int(b)
    if p == 0:
        return -1 if (a < 0 and b < 0) else 1
    if p == 2:
        def v2(x):
            k = 0
            while x % 2 == 0:
                x //= 2
                k += 1
            return k, x
        va, ua = v2(abs(a))
        vb, ub = v2(abs(b))
        ua = ua if a > 0 else -ua
        ub = ub if b > 0 else -ub
        ee = lambda u: ((u - 1) // 2) % 2
        ww = lambda u: ((u * u - 1) // 8) % 2
        return (-1) ** (ee(ua) * ee(ub) + va * ww(ub) + vb * ww(ua))
    va = sp.multiplicity(p, abs(a))
    vb = sp.multiplicity(p, abs(b))
    ua = abs(a) // p ** va * (1 if a > 0 else -1)
    ub = abs(b) // p ** vb * (1 if b > 0 else -1)
    s = (-1) ** (va * vb * ((p - 1) // 2))
    t = 1
    if va % 2:
        t *= legendre_symbol(ub % p or 1, p)
    if vb % 2:
        t *= legendre_symbol(ua % p or 1, p)
    return s * t


def ramification(a, b):
    ps = {0, 2} | set(sp.factorint(abs(a))) | set(sp.factorint(abs(b)))
    return sorted([("oo" if p == 0 else p) for p in ps if hilbert(a, b, p) == -1], key=str)


def selftest(verbose=True):
    fails = []
    # ramification controls, known answers, both directions
    for a, b, want in [(-1, -1, [2, "oo"]), (1, 1, []), (-1, 1, []), (2, 3, [2, 3])]:
        got = ramification(a, b)
        if got != want:
            fails.append(f"ramification({a},{b}) = {got} != {want}")
    order, allspec, rel, nsurj, surjspec = door_census()
    if order != 24:
        fails.append(f"2T order {order} != 24")
    if set(allspec) != {-2, 0, 2}:
        fails.append(f"2T kappa spectrum {sorted(allspec)} != {{-2,0,2}}")
    if nsurj != 48:
        fails.append(f"surjections {nsurj} != 48 (the banked count)")
    if set(surjspec) != {0}:
        fails.append(f"kappa on surjections {sorted(surjspec)} != {{0}} -- NOT uniform")
    ngen, genspec = generating_pair_census()
    if ngen != 384:
        fails.append(f"generating pairs {ngen} != 384")
    if set(genspec) != {0}:
        fails.append(f"generating-pair kappa spectrum {sorted(genspec)} != {{0}}")
    if set(genspec) != set(surjspec):
        fails.append("the relator DOES discriminate -- the refuted attribution would be back in play; "
                     "re-open the door claim deliberately rather than silently")
    if verbose:
        print(f"  [2T ]  order {order}   kappa spectrum over all {order*order} pairs: {allspec}")
        print(f"  [rel]  relator solutions {rel}   SURJECTIVE {nsurj}   non-surjective {rel-nsurj}")
        print(f"  [door] kappa on the 48 surjections: {dict(surjspec)}  ->  2-kappa = 2, class D = 2")
        print(f"  [bit ]  class -1 occurs in 2T at all? {any(sp.Integer(2-k) == -1 for k in allspec)}")
        print(f"  [ctl ]  generating pairs {ngen}, kappa spectrum {dict(genspec)} -- SAME as the 48:")
        print(f"          the relator cuts NOTHING, so no door-specific claim is admissible.")
        print(f"  [ram ]  object (5,-5) ramifies at {ramification(5,-5)}   2T (-1,-1) at {ramification(-1,-1)}")
        print(f"          (two facts, NO map between them -- nothing is claimed to flow)")
    return fails


if __name__ == "__main__":
    print("B1249 -- the door and the class (selftest)")
    f = selftest()
    print()
    print("SELFTEST:", "PASS" if not f else "FAIL")
    for x in f:
        print("   !", x)
    raise SystemExit(1 if f else 0)
