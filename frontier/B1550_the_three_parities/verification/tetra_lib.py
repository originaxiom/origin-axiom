#!/usr/bin/env python3
"""sm:B1550 -- the three parities: the tetrahedral covers. Library; nothing is computed on import.

THE PARITIES. A generated state M (sm:B1527's presentation: F = <a, b>, t g t^-1 = phi(g)) acts on H_1(F; F_2) = F_2^2,
the parities of the two records, by phi mod 2. det(phi - I) = 2 - tr phi, so when tr phi is odd phi mod 2 fixes no non-zero
parity, and it acts on the three non-zero parities as a 3-cycle (GL(2, F_2) = S_3). GENESIS's SE1 (|2 - tr phi| = 1) gives
an odd trace, so the root m004 = +LR is of this kind.

THE TETRAHEDRAL COVER. For tr phi odd, pi_1 M -> F_2^2 x| Z/3 = A4 (a -> e_a, b -> e_b, t -> the 3-cycle) is onto. Its kernel
is N, built here as sm:B1538's fibre-direction cover of the third level M_3 (the state word three times) with the lattice
2Z^2 and the class wbar that gives four cusps (0 for a + state, (1, 1) for a - state). N's four ends sit at the four
2-torsion points of the fibre torus, and A4 acts on them as on the vertices of a tetrahedron.

THE A4 ACTION on N's characters.
  - V4 = the deck group of N -> M_3: three_lib.deck_action.
  - Z/3: conjugation by M's stable letter t (golden_action). M_3's own stable letter is t_3 = t^3 c, where
    phi_3 = phi^3 o Ad(c) (twist; c = 1 for a + state). On F, t acts by phi; on N's tau = t_3 w it gives
    t tau t^-1 = tau X with X = w^-1 c^-1 phi(c) phi(w) in K.

THE LABEL of a character: its values on the four puncture loops l_x, x in Z^2/2Z^2 (sm:B1538's puncture_values). When the
values are non-zero at exactly two points x and y (an edge of the tetrahedron), the label is the parity x - y, one of the
three non-zero parities; opposite edges share a label. V4 preserves labels and the golden map permutes them by phi mod 2."""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _root():
    """the repository: the first parent holding frontier/ (or ORIGIN_AXIOM_ROOT when run outside it)"""
    for p in HERE.parents:
        if (p / "frontier").is_dir():
            return p
    import os
    return Path(os.environ["ORIGIN_AXIOM_ROOT"])


ROOT = _root()
B1549V = ROOT / "frontier" / "B1549_the_three_ended_covers" / "verification"


def _load(alias, path):
    if alias not in sys.modules:
        if str(path.parent) not in sys.path:
            sys.path.append(str(path.parent))
        spec = importlib.util.spec_from_file_location(alias, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


T = _load("three_lib", B1549V / "three_lib.py")       # sm:B1549's library (banked): the two routes, the frame, ranks
PC = T.PC

# the selection rule (sealed): every generated state of odd trace whose word has length <= 4
STATES = ["+LR", "-LR", "+LLLR", "-LLLR"]
M_ORDER = 4
LAT = (2, 0, 2)


def level3(sw):
    return sw[0] + sw[1:] * 3


def phi_mod2_order(sw):
    M = PC.State(sw).M
    A = [[x % 2 for x in r] for r in M]
    X, k = [row[:] for row in A], 1
    while X != [[1, 0], [0, 1]]:
        X = [[sum(X[i][l] * A[l][j] for l in range(2)) % 2 for j in range(2)] for i in range(2)]
        k += 1
    return k


_COV = {}


def tetra_cover(sw):
    """(wbar label, N): the unique class wbar for which the 2Z^2 cover of M_3 has four cusps"""
    if sw not in _COV:
        st3 = PC.State(level3(sw))
        hits = []
        for wl in range(4):
            C = PC.Cover(st3, LAT, wl)
            if len(C.cusps) == 4:
                hits.append((wl, C))
        assert len(hits) == 1, (sw, [h[0] for h in hits])
        wl, C = hits[0]
        # N is the kernel of pi_1 M -> A4: its stable letter tau = t_3 w = t^3 c w lies in t^3 K (c w has even parities),
        # and its index is 12
        cw = twist(sw) + C.w
        par = [sum(1 for ch in cw if ch == g) - sum(1 for ch in cw if ch == g.upper()) for g in "ab"]
        assert all(p % 2 == 0 for p in par) and 3 * C.d == 12, (sw, par)
        _COV[sw] = hits[0]
    return _COV[sw]


def twist(sw):
    """c in F with phi_3 = phi^3 o Ad(c), checked on a and b"""
    s1, s3 = PC.State(sw), PC.State(level3(sw))
    inv3 = lambda w: PC.substitute(PC.substitute(PC.substitute(w, s1.img_inv), s1.img_inv), s1.img_inv)
    x = inv3(s3.phi("a"))                                   # = c a c^-1, freely reduced
    c = x[:(len(x) - 1) // 2]
    for g in "ab":
        assert PC.free_reduce(c + g + PC.inv_word(c)) == inv3(s3.phi(g)), (sw, g, c)
    return c


def zeta(C, ez, word, m):
    """the character's value (exponent mod m) on a word of F lying in K"""
    vec = C.abelian(C.rewrite(word))
    return sum(e * v for e, v in zip(ez, vec)) % m


def golden_action(sw, C, ez, es, m):
    """chi -> chi o Ad(t), t the stable letter of M"""
    s1 = PC.State(sw)
    c = twist(sw)
    ez2 = tuple(zeta(C, ez, s1.phi(y), m) for y in C.gword)
    X = PC.inv_word(C.w) + PC.inv_word(c) + s1.phi(c) + s1.phi(C.w)
    return (ez2, (es + zeta(C, ez, X, m)) % m)


def characters(C, m):
    return [(ez, es) for ez in C.characters(m) for es in range(m)]


def a4_orbits(sw, C, m):
    """the A4 orbits on the characters of order dividing m; each sorted; with the V4 orbits inside"""
    chars = characters(C, m)
    S = set(chars)
    deck = {c: T.deck_action(C, c[0], c[1], m) for c in chars}
    gold = {c: golden_action(sw, C, c[0], c[1], m) for c in chars}
    for c in chars:
        assert set(deck[c].values()) <= S and gold[c] in S, ("an image is not a character", sw, c)
    seen, out = set(), []
    for c in chars:
        if c in seen:
            continue
        orb, front = {c}, [c]
        while front:
            nxt = []
            for x in front:
                for y in list(deck[x].values()) + [gold[x]]:
                    if y not in orb:
                        orb.add(y)
                        nxt.append(y)
            front = nxt
        seen |= orb
        v4 = []
        left = set(orb)
        while left:
            x = min(left)
            o = set(deck[x].values())
            v4.append(sorted(o))
            left -= o
        out.append({"orbit": sorted(orb), "v4 orbits": sorted(v4), "gold": {x: gold[x] for x in orb}})
    return out


def pattern(C, ez, m):
    """the values on the four puncture loops, the support, and the label (an edge's parity) when the support is an edge"""
    pv = C.puncture_values(ez, m)
    sup = [x for x in range(C.d) if pv[x]]
    label = None
    if len(sup) == 2:
        (x, y) = sup
        label = tuple((C.vecs[x][k] - C.vecs[y][k]) % 2 for k in range(2))
    return pv, sup, label


def char_list(c):
    return list(c[0]) + [c[1]]
