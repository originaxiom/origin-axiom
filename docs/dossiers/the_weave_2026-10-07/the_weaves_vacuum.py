#!/usr/bin/env python3
"""W8 of the weave: the frame at the weave's own vacuum (design-time structure, no count).

The record's frames read a thread's own vacuum, its hyperbolic holonomy rho, through four(rho): X -> g X g* on 2 x 2
Hermitian matrices (sm:B1549's three_lib.four_mp). That is why main calls them thread instruments (S80). The weave has one
vacuum of its own, the common point rho_Q (W2): a -> i, b -> j, the only point every move fixes, extended over every thread
(W3). Its four is four(rho_Q) = 1 + 3, the 3 being the adjoint, which is W4's parity triplet thread by thread. So nu (x)
four(rho_Q) is a sum of characters, and by Shapiro every piece is a character of the thread's resolving tick: the frame at
the weave's vacuum reads rank-one lines. This script reads them exactly (sympy, over Q(i)).

The rule, named before the run: every state of GENESIS to length 6 (24 states), at its resolving tick k (the order of
phi mod 2), and on it
  (1) the three parity lines: the characters whose fibre restriction is a non-zero parity, at kappa = +1 and -1 (at any
      other kappa h1 = 0, because the tick acts on the one-dimensional H1(F; chi_p) by an integer sign);
  (2) every character of the tick of order dividing 4: its h1, whether it is trivial on the cusp, and n (h1 minus the rank
      of the restriction to the cusp). A member of the frame at the weave's vacuum is a character with n > 0.
The budget: one pass.

The law behind (1), proved (half lives, half dies): on a compact orientable 3-manifold with torus boundary, the image of
H1(M; L) in H1(boundary; L) is half its dimension for a unitary rank-one L. When L is trivial on the cusp that image is
one-dimensional, so a line with h1 = 1 restricts injectively and is never interior.

    python3 the_weaves_vacuum.py   ->  the_weaves_vacuum.json beside it
"""
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_parity_sectors as S  # noqa: E402  (the state list, the resolving tick, and sm:B1538's cover library)

PC = S.PC
I = sp.I
PARITY = {(1, 0): "(1/2, 0)", (0, 1): "(0, 1/2)", (1, 1): "(1/2, 1/2)"}


def fox(word, g, ch):
    """the left Fox derivative d word / d g at the character ch (capitals are inverses)"""
    tot, pref = sp.Integer(0), sp.Integer(1)
    for c in word:
        if c == g:
            tot += pref
        elif c == g.upper():
            tot -= pref / ch[g]
        pref = pref * (ch[c] if c.islower() else 1 / ch[c.lower()])
    return sp.expand(tot)


def value(word, ch):
    v = sp.Integer(1)
    for c in word:
        v = v * (ch[c] if c.islower() else 1 / ch[c.lower()])
    return sp.simplify(v)


def line(st, C, ch):
    """h1, cusp-trivial, n of the rank-one module ch on the tick's group <a, b, t | t g T = phi(g)>"""
    rels = ["t" + g + "T" + PC.inv_word(st.phi(g)) for g in "ab"]
    assert all(value(r, ch) == 1 for r in rels), "not a character"
    F = sp.Matrix([[fox(r, g, ch) for g in "abt"] for r in rels])
    Z = F.nullspace()
    B = sp.Matrix([ch[g] - 1 for g in "abt"])
    trivial = all(sp.simplify(ch[g] - 1) == 0 for g in "abt")
    h1 = len(Z) - (0 if trivial else 1)
    per = C.periph[0]
    cusp_trivial = all(value(w, ch) == 1 for w in per)
    if h1 == 0:
        return h1, cusp_trivial, 0
    if not cusp_trivial:
        return h1, cusp_trivial, h1                        # H1 of the torus with a non-trivial character is zero
    # the restriction: a cocycle's values on the two peripheral words (coboundaries vanish there)
    R = sp.Matrix([[sum(fox(w, g, ch) * z[i] for i, g in enumerate("abt")) for z in Z] for w in per])
    # modulo the coboundary direction
    if not trivial:
        rb = sp.Matrix([sum(fox(w, g, ch) * B[i] for i, g in enumerate("abt")) for w in per])
        assert all(sp.simplify(x) == 0 for x in rb)
    r1 = sp.Matrix(sp.simplify(R)).rank()
    return h1, cusp_trivial, h1 - r1


def tick(sw):
    w = sw[1:]
    k = S.resolving_tick(w)
    sign = sw[0] if k % 2 else "+"
    st = PC.State(sign + w * k)
    return k, sign + w * k, st, PC.Cover(st, (1, 0, 1), 0)


def run():
    out, tally = [], {"parity lines read": 0, "of them interior": 0, "members (order dividing 4)": 0}
    for sw in S.states():
        k, swk, st, C = tick(sw)
        lines = []
        for (pa, pb), name in PARITY.items():
            for kap in (1, -1):
                ch = {"a": sp.Integer(-1) ** pa, "b": sp.Integer(-1) ** pb, "t": sp.Integer(kap)}
                h1, ct, n = line(st, C, ch)
                if h1:
                    lines.append({"parity": name, "kappa": kap, "h1": h1, "trivial on the cusp": ct, "n": n})
                    tally["parity lines read"] += 1
                    tally["of them interior"] += int(n > 0)
        members, read = [], 0
        for ez in C.characters(4):
            for es in range(4):
                ch = {"a": I ** ez[0], "b": I ** ez[1], "t": I ** es}
                h1, ct, n = line(st, C, ch)
                read += 1
                if n > 0:
                    members.append({"fibre": [f"{e}/4" for e in ez], "kappa": f"{es}/4", "h1": h1,
                                    "trivial on the cusp": ct, "n": n})
        tally["members (order dividing 4)"] += len(members)
        out.append({"state": sw, "resolving tick": k, "the tick's state": swk, "the parity lines": lines,
                    "characters of order dividing 4 read": read, "members": members})
        print(sw, k, [(x["parity"], x["kappa"], x["n"]) for x in lines], "members:", len(members), flush=True)
    return {"rule": "every state to length 6 at its resolving tick; the frame at the weave's vacuum (rank-one lines)",
            "tally": tally, "states": out}


if __name__ == "__main__":
    res = run()
    with open(HERE / "the_weaves_vacuum.json", "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print(json.dumps(res["tally"]))
