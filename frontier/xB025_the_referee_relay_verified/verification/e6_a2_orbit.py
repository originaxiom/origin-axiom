"""xB025 -- the E_6 A_2 orbit computation, the one checkable half of the referee report's
strongest new claim ("the SM sits in E_6 in exactly one way up to conjugacy", B1366,
resting on '120 A_2's, all one orbit').

Exact integer arithmetic in the simple-root basis.  No Lie-theory library: the Cartan matrix,
reflections, and a breadth-first orbit walk.  For a simply-laced system the Cartan matrix IS the
Gram matrix of the simple roots (all roots of squared length 2), so (a, b) = a^T C b exactly.
"""
import json
import os
from itertools import combinations

R = {}


def cartan(n, edges):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        C[i][i] = 2
    for (i, j) in edges:
        C[i - 1][j - 1] = C[j - 1][i - 1] = -1
    return C


def ip(C, a, b):
    n = len(C)
    return sum(a[i] * C[i][j] * b[j] for i in range(n) for j in range(n))


def refl(C, a, i):
    c = sum(a[j] * C[i][j] for j in range(len(C)))
    return tuple(a[j] - (c if j == i else 0) for j in range(len(C)))


def roots_of(C):
    n = len(C)
    simple = [tuple(1 if j == i else 0 for j in range(n)) for i in range(n)]
    roots, frontier = set(simple), list(simple)
    while frontier:
        nxt = []
        for a in frontier:
            for i in range(n):
                b = refl(C, a, i)
                if b not in roots:
                    roots.add(b)
                    nxt.append(b)
        frontier = nxt
    roots |= {tuple(-x for x in a) for a in roots}
    return sorted(roots)


def a2_subsystems(C, roots):
    """Closed rank-2 subsystems of type A_2: {+-a, +-b, +-(a+b)} with (a,b) = -1."""
    rs = set(roots)
    out = set()
    for a, b in combinations(roots, 2):
        if ip(C, a, b) != -1:
            continue
        u = tuple(x + y for x, y in zip(a, b))
        if u not in rs:
            continue
        sub = frozenset([a, b, u, tuple(-x for x in a), tuple(-x for x in b),
                         tuple(-x for x in u)])
        if len(sub) == 6:
            out.add(sub)
    return out


def a1_subsystems(roots):
    return {frozenset([a, tuple(-x for x in a)]) for a in roots}


def orbits(C, objs):
    """Weyl orbits, by breadth-first closure under the simple reflections."""
    n, seen, sizes = len(C), set(), []
    for s in objs:
        if s in seen:
            continue
        orb, fr = {s}, [s]
        while fr:
            nx = []
            for x in fr:
                for i in range(n):
                    y = frozenset(refl(C, r, i) for r in x)
                    if y not in orb:
                        orb.add(y)
                        nx.append(y)
            fr = nx
        seen |= orb
        sizes.append(len(orb))
    return sorted(sizes)


E6 = cartan(6, [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)])          # Bourbaki E_6
E7 = cartan(7, [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (2, 4)])  # Bourbaki E_7
E8 = cartan(8, [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4)])
A3 = cartan(3, [(1, 2), (2, 3)])
D4 = cartan(4, [(1, 2), (2, 3), (2, 4)])
A1A2 = cartan(3, [(2, 3)])        # DISCONNECTED: A_1 (node 1) + A_2 (nodes 2,3)


def K1():
    """Positive control: the generator must reproduce known root counts."""
    print("\nK1       ROOT-SYSTEM CONTROL -- the generator must give the textbook counts")
    want = {"A3": (A3, 12), "D4": (D4, 24), "E6": (E6, 72), "E7": (E7, 126), "E8": (E8, 240)}
    ok = True
    for nm, (C, n) in want.items():
        rs = roots_of(C)
        good = (len(rs) == n) and all(ip(C, r, r) == 2 for r in rs)
        ok &= good
        print(f"         {nm}: {len(rs)} roots (expect {n}); all |r|^2 = 2: "
              f"{all(ip(C, r, r) == 2 for r in rs)}   {'OK' if good else 'MISMATCH'}")
    R["K1"] = {"counts": {k: len(roots_of(v[0])) for k, v in want.items()}, "ok": bool(ok)}
    print(f"K1 {'PASS' if ok else 'FAIL'}")
    return ok


def K2():
    """THE CONTROL THAT MATTERS: the orbit walk must be able to SEE more than one orbit.
    A single-orbit answer is worthless from code that can only ever return one."""
    print("\nK2       NEGATIVE CONTROL -- can the orbit walk detect MORE than one orbit?")
    rs = roots_of(A1A2)
    o = orbits(A1A2, a1_subsystems(rs))
    print(f"         A_1 + A_2 (disconnected): {len(rs)} roots; A_1-subsystem orbits {o}")
    print("         The Weyl group cannot mix components, so the answer MUST be two orbits.")
    ok = len(o) == 2 and sorted(o) == [1, 3]
    R["K2"] = {"orbits": o, "ok": bool(ok)}
    print(f"K2 {'PASS' if ok else 'FAIL'}  the walk separates what must be separated, so a")
    print("         'single orbit' verdict below is a result and not an artefact of the code.")
    return ok


def K3():
    """The claim itself."""
    print("\nK3       E_6: THE A_2 SUBSYSTEMS AND THEIR WEYL ORBITS  (B1366's ingredient)")
    rs = roots_of(E6)
    subs = a2_subsystems(E6, rs)
    o = orbits(E6, subs)
    print(f"         E_6 roots: {len(rs)}")
    print(f"         A_2 subsystems: {len(subs)}")
    print(f"         Weyl orbits on them: {o}   -> single orbit: {len(o) == 1}")
    ok = (len(rs) == 72) and (len(subs) == 120) and (o == [120])
    R["K3"] = {"roots": len(rs), "a2_subsystems": len(subs), "orbits": o,
               "single_orbit": bool(len(o) == 1)}
    print(f"K3 {'PASS' if ok else 'FAIL'}  '120 A_2's, all one orbit' is CONFIRMED.")
    return ok


def K4():
    """What the confirmation does NOT establish -- stated as part of the result."""
    print("\nK4       WHAT K3 DOES NOT ESTABLISH  (the gap between ingredient and conclusion)")
    gaps = [
        ("root subsystems are not all subalgebras",
         "K3 counts A_2's GENERATED BY ROOTS.  Dynkin's classification separates regular from "
         "special (S-) subalgebras; a non-regular A_2 is not generated by roots and is NOT in "
         "this count at all.  The orbit walk cannot see it."),
        ("A_2 is colour, not the Standard Model",
         "SU(3) x SU(2) x U(1) additionally needs the SU(2) and both U(1)s placed.  Main's "
         "B1415 shows that placement is its own computation: of the 12 order-4 elements of "
         "exp(u(1)_Y + u(1)_gamma), EXACTLY 4 leave only the SM roots of su(6)."),
        ("conjugacy in WHICH group",
         "W(E_6), the adjoint group, or Aut(E_6) -- which contains the order-2 diagram "
         "automorphism, precisely the one relating 27 and 27bar.  These give different "
         "answers and the claim does not say which is meant."),
    ]
    for t, why in gaps:
        print(f"         - {t}:")
        for line in [why[i:i + 86] for i in range(0, len(why), 86)]:
            print(f"             {line}")
    print("         SO: the INGREDIENT is verified; the CONCLUSION 'unique SM embedding up to")
    print("         conjugacy' is NOT established by it, and this arc does not establish it.")
    R["K4"] = {"gaps": [t for t, _ in gaps]}
    return True


if __name__ == "__main__":
    res = {}
    for f in (K1, K2, K3, K4):
        try:
            res[f.__name__] = bool(f())
        except Exception as e:
            print(f"{f.__name__} EXCEPTION {type(e).__name__}: {e}")
            res[f.__name__] = False
    print("\n" + "=" * 78)
    for k, v in res.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    print("VERIFIED" if all(res.values()) else "NOT ALL CELLS PASSED")
    with open(os.path.join(os.path.dirname(__file__), "e6_a2_orbit.json"), "w",
              encoding="utf-8") as fh:
        json.dump({"cells": res, "results": R}, fh, indent=1, default=str)
