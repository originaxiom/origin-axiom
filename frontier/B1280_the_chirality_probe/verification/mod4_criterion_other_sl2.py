#!/usr/bin/env python3
"""THE PAIRING CRITERION AT THE OTHER sl_2 POINTS -- pure root-system combinatorics.

theta_odd_pairing.py proves that the inversion iota acts on H^1(M; Sym^n rho_0) by eps_n = (-1)^(n/2 + 1) (exact, n <= 22)
and the period-2 swap by +1.  These signs depend only on n, not on where Sym^n sits inside e_6.  So at ANY sl_2-embedded
point rho = (sl_2 -> E_6) o Riley the question "does an isometry realise the E_6 outer automorphism theta on the Zariski
tangent space H^1(M; e_6) = sum over the summands V_n of e_6 (n even; each h^1 = 1)?" is decided by:
      every summand V_n of the FIXED algebra of theta (f_4 or sp(8), where theta = +1) must have n = 2 mod 4, and
      every summand V_n of the -1 part (the 26 or the 42) must have n = 0 mod 4          (THE MOD-4 CRITERION),
because eps_n = +1 iff n = 2 mod 4 (and eps_0 = -1 for the trivial summands, the meridian being inverted).

For an sl_2 whose triple lies in f_4 = the fixed algebra of the graph automorphism sigma of E_6 (Bourbaki: 1<->6, 3<->5), the
weights of h on f_4 and on the 26 follow from the roots: a sigma-fixed root contributes to f_4, a sigma-pair {a, sigma a}
contributes one weight to f_4 and one to the 26, the Cartan contributes 4 zeros to f_4 and 2 to the 26.  If those weight
multisets are not sl_2-modules, no triple through that h lies in f_4; then the other outer involution (fixed algebra
sp(8), -1 part the 42) is tested by the dimension count: the sp(8) part is a sub-multiset of the summands containing
V_2 with total dimension 36.

Only the nine even nilpotent orbits of E_6 (weighted Dynkin diagrams with labels in {0, 2}, all sigma-symmetric) carry
sl_2 points whose deformation classes are all of the h^1 = 1 type (odd n gives h^1 = 0); the principal one is the
geometric point of theta_odd_pairing.py (the control: f_4 = V2 + V10 + V14 + V22, 26 = V8 + V16, criterion TRUE).
"""
from __future__ import annotations
import itertools
from collections import Counter
import numpy as np

C = np.array([[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]])  # E6, Bourbaki
simple = [tuple(int(i == j) for j in range(6)) for i in range(6)]


def positive_roots():
    roots, frontier = set(simple), list(simple)
    while frontier:
        new = []
        for r in frontier:
            rv = np.array(r)
            for i in range(6):
                s = rv - (rv @ C[:, i]) * np.array(simple[i])
                t = tuple(int(x) for x in s)
                if t not in roots and all(x >= 0 for x in t) and any(t):
                    roots.add(t); new.append(t)
        frontier = new
    return sorted(roots)


POS = positive_roots()
ALL = POS + [tuple(-x for x in r) for r in POS]
sigma = lambda r: (r[5], r[1], r[4], r[3], r[2], r[0])


def strings(weights):
    """sl_2 decomposition of a weight multiset (highest weights n, dim n + 1), or None if it is not an sl_2-module."""
    cnt, out = Counter(weights), []
    while cnt:
        top = max(cnt)
        if top < 0:
            return None
        for k in range(top, -top - 1, -2):
            if cnt.get(k, 0) <= 0:
                return None
            cnt[k] -= 1
            if cnt[k] == 0:
                del cnt[k]
        out.append(top)
    return sorted(out)


def sigma_split(c):
    c = np.array(c)
    wf, w26, seen = [0] * 4, [0] * 2, set()
    for s in ALL:
        if s in seen:
            continue
        wt = int(np.array(s) @ c); ss = sigma(s)
        if ss == s:
            wf.append(wt); seen.add(s)
        else:
            wf.append(wt); w26.append(wt); seen.add(s); seen.add(ss)
    return strings(wf), strings(w26)


def sp8_partitions():
    """partitions of 8 whose odd parts have even multiplicity: the nilpotent orbits of sp(8)."""
    def parts(n, m):
        if n == 0:
            yield []
        for k in range(min(n, m), 0, -1):
            for rest in parts(n - k, k):
                yield [k] + rest
    out = []
    for lam in parts(8, 8):
        cnt = Counter(lam)
        if all(cnt[k] % 2 == 0 for k in cnt if k % 2 == 1):
            out.append(lam)
    return out


def sp8_split(lam):
    """the decompositions of sp(8) = Sym^2(W) and of the 42 = Lambda^4(W) - Lambda^2(W) under the sl_2 of the partition lam
    (W = sum of V_(k-1), the 8-dimensional symplectic representation), as highest-weight lists."""
    W = [w for k in lam for w in range(k - 1, -k, -2)]
    sym2 = [W[i] + W[j] for i in range(8) for j in range(i, 8)]
    lam2 = [W[i] + W[j] for i in range(8) for j in range(i + 1, 8)]
    lam4 = [sum(t) for t in itertools.combinations(W, 4)]
    c42 = Counter(lam4); c42.subtract(Counter(lam2))
    assert all(v >= 0 for v in c42.values())
    return strings(sym2), strings(list(c42.elements()))


def c4_options(S):
    """the sp(8)-type outer involutions fixing a triple of E_6-type S: partitions lam of 8 with Sym^2(W) + Lambda^4_0(W) = S."""
    out = []
    for lam in sp8_partitions():
        fixed, minus = sp8_split(lam)
        if fixed is not None and minus is not None and sorted(fixed + minus) == sorted(S):
            out.append((lam, fixed, minus))
    return out


eps = lambda n: (-1) ** (n // 2 + 1)


def criterion(fixed, minus):
    bad_fixed = [n for n in fixed if n % 2 == 0 and eps(n) != +1]
    bad_minus = [n for n in minus if n % 2 == 0 and eps(n) != -1]
    return (not bad_fixed and not bad_minus), bad_fixed, bad_minus


EVEN_ORBITS = [("E6 (principal; the geometric point)", (2, 2, 2, 2, 2, 2)), ("E6(a1) (subregular; B1256's I-25 point)", (2, 2, 2, 0, 2, 2)),
               ("D5", (2, 2, 0, 2, 0, 2)), ("E6(a3)", (2, 0, 0, 2, 0, 2)), ("D4", (0, 2, 0, 2, 0, 0)), ("A4", (2, 2, 0, 0, 0, 2)),
               ("D4(a1)", (0, 0, 0, 2, 0, 0)), ("2A2", (2, 0, 0, 0, 0, 2)), ("A2", (0, 2, 0, 0, 0, 0))]


def main():
    assert len(POS) == 36
    print("n -> eps_n(iota) = (-1)^(n/2+1):", {n: eps(n) for n in range(0, 24, 2)})
    print("\norbit | dim | e_6 under the sl_2 | tangent dim h^1(M; e_6) | fixed algebra of the theta fixing the triple | -1 part | mod-4 criterion (an isometry realises theta on the tangent space)")
    results = {}
    for name, c in EVEN_ORBITS:
        allw = [int(np.array(s_) @ np.array(c)) for s_ in ALL] + [0] * 6
        S = strings(allw)
        assert S is not None, name
        dimO = 78 - allw.count(0)
        tangent = sum(1 for n in S if n % 2 == 0)
        options = []
        f4, s26 = sigma_split(c)
        if f4 is not None and s26 is not None:
            options.append(("f_4 (sigma-split of the roots)", f4, s26))
        for lam, fixed, minus in c4_options(S):
            options.append((f"sp(8), sl_2 of partition {lam}", fixed, minus))
        verdicts = [(kind, fixed, minus) + criterion(fixed, minus) for (kind, fixed, minus) in options]
        any_ok = any(v[3] for v in verdicts)
        results[name] = dict(c=c, dim=dimO, summands=S, options=verdicts, ok=any_ok)
        print(f"\n{name} {c}: dim O = {dimO}; e_6 = {'+'.join('V%d' % n for n in S)}; tangent dim {tangent}")
        for kind, fixed, minus, ok, bf, bm in verdicts:
            print(f"    theta with fixed algebra {kind}: fixed {'+'.join('V%d' % n for n in fixed)} | -1 part {'+'.join('V%d' % n for n in minus)} | criterion {ok}"
                  + ("" if ok else f" -- unpaired: fixed {['V%d' % n for n in bf]}, minus {['V%d' % n for n in bm]}"))
        if not options:
            print("    no outer involution of either type fixes a triple of this shape")
        print(f"    => an isometry realises theta on the tangent space: {any_ok}")
    sub = results["E6(a1) (subregular; B1256's I-25 point)"]
    assert sub['summands'] == [2, 4, 6, 8, 10, 10, 14, 16]
    assert [v[:3] for v in sub['options']] == [("sp(8), sl_2 of partition [8]", [2, 6, 10, 14], [4, 8, 10, 16])], sub['options']
    print("\nVerdict: the criterion holds at", [k for k, v in results.items() if v['ok']], "and fails at every other even orbit.")
    print("At the subregular point the only outer involution fixing the triple is the sp(8)-type one (the sl_2 is the principal sl_2 of an")
    print("sp(8): e_6 = sp(8) + 42 = (V2+V6+V10+V14) + (V4+V8+V10+V16)), and exactly ONE direction is unpaired: the V10 of the 42 (theta = -1, iota* = +1).")
    return results


if __name__ == "__main__":
    r = main()
    ok = r["E6 (principal; the geometric point)"]['ok'] and not any(v['ok'] for k, v in r.items() if not k.startswith("E6 (principal"))
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
