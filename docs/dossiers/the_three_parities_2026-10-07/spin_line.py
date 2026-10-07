#!/usr/bin/env python3
"""The line's room on the tetrahedral covers, and the four over the spin line. Structure only (no count).

  (1) The line's room n(zeta) = h1 - r1 of the one-dimensional local system zeta on the tetrahedral cover N of +LR and of
      -LR, at every character of order dividing 4, by A4 orbit: sm:B1538's exact reader (punct_present.read) mod two
      primes, which must agree.
  (2) On the root's N the room is 4 at exactly one character, the spin sign eps = [1, 1, 1, 0, 1 | 1] (congruence.py).
      Theorem C's floor at a frame member nu with nu^4 = eps is I(W1) >= -b0 - n(eps) = -4: room for four generations in
      one module. The frame's class lives in H^1(N; nu^5 (x) rho) with nu^5 = nu eps, so the four must have a class at a
      character mu with mu^4 = eps. Read here: all 1024 such mu (96 A4 orbits), the representative of each in route P and
      the first and last two in route S (sm:B1549's library at 50 digits): h^1(mu (x) rho).

    python3 spin_line.py   ->  spin_line.json beside this file"""
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _root():
    for p in HERE.parents:
        if (p / "frontier").is_dir():
            return p
    import os
    return Path(os.environ["ORIGIN_AXIOM_ROOT"])


import sys
sys.path.insert(0, str(_root() / "frontier" / "B1550_the_three_parities" / "verification"))
import tetra_lib as L  # noqa: E402

T = L.T
EPS = (1, 1, 1, 0, 1, 1)


def line_room(sw):
    wl, C = L.tetra_cover(sw)
    Pr = T.RP.Presentation(C)
    out = {}
    for m, primes in ((2, (1000003, 998244353)), (4, (1000033, 998244353))):
        tab = Counter()
        big = []
        for o in L.a4_orbits(sw, C, m):
            c = o["orbit"][0]
            reads = [T.RP.read(Pr, c[0], c[1], m, p) for p in primes]
            assert reads[0] == reads[1], (sw, c)
            pv, sup, lab = L.pattern(C, c[0], m)
            n = reads[0]["n"]
            tab[str([T.char_order(c, m), len(o["orbit"]), len(sup), reads[0]["h1"], reads[0]["r1"], n])] += 1
            if n >= 3:
                big.append({"character": L.char_list(c), "orbit size": len(o["orbit"]), "n": n})
        out[f"order dividing {m}: (order, orbit size, puncture support, h1, r1, n) -> orbits"] = dict(sorted(tab.items()))
        out[f"order dividing {m}: room 3 or more"] = big
    return out


def over_spin():
    sw = "+LR"
    s3 = L.level3(sw)
    wl, C = L.tetra_cover(sw)
    m = 8
    eps8 = tuple(4 * x % 8 for x in EPS)
    over = [c for ez in C.characters(m) for c in [(ez, es) for es in range(m)]
            if tuple(4 * x % 8 for x in L.char_list(c)) == eps8]
    S = set(over)
    deck = {c: T.deck_action(C, c[0], c[1], m) for c in over}
    gold = {c: L.golden_action(sw, C, c[0], c[1], m) for c in over}
    seen, orbs = set(), []
    for c in over:
        if c in seen:
            continue
        orb, fr = {c}, [c]
        while fr:
            nx = []
            for x in fr:
                for y in list(deck[x].values()) + [gold[x]]:
                    assert y in S
                    if y not in orb:
                        orb.add(y)
                        nx.append(y)
            fr = nx
        seen |= orb
        orbs.append(sorted(orb))
    tab = Counter()
    for o in orbs:
        c = o[0]
        P = T.read_P(s3, C, c[0], c[1], m)["structure"]
        tab[str([len(o), P["h1"], P["r1"], P["n"]])] += 1
    s_reads = []
    for o in orbs[:2] + orbs[-2:]:
        c = o[0]
        Sx = T.read_S(s3, C, c[0], c[1], m)["structure"]
        s_reads.append([L.char_list(c), Sx["h1"], Sx["r1"], Sx["n"]])
    return {"characters mu with mu^4 = eps": len(over), "A4 orbits": len(orbs),
            "route P: (orbit size, h1, r1, n) -> orbits": dict(sorted(tab.items())),
            "route S at four representatives: [mu, h1, r1, n]": s_reads}


def main():
    out = {"line room, +LR": line_room("+LR"), "line room, -LR": line_room("-LR"), "the four over the spin line": over_spin()}
    (HERE / "spin_line.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: (v.get("order dividing 4: room 3 or more") if k.startswith("line room") else
                          v["route P: (orbit size, h1, r1, n) -> orbits"]) for k, v in out.items()}))


if __name__ == "__main__":
    main()
