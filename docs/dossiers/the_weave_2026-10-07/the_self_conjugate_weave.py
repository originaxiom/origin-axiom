#!/usr/bin/env python3
"""W25 of the weave: IS ANY GAUGE READING OF THE WEAVE'S FORCED BUNDLES CHIRAL WITHOUT A CHOICE? The rule is W25_RULE.md,
committed before this ran (2068244e).

A gauge group commuting with a bundle's holonomy H has chiral matter only if some multiplicity space Hom_H(sigma, 248)
is a complex representation of it; when every irreducible sigma of H occurring in the 248 is real or quaternionic, the
multiplicity spaces are self-conjugate (Frobenius-Schur), and chirality needs a choice. This reads, for the weave's
forced holonomies:
  F1 the Frobenius-Schur indicators of Q8's irreducibles (the fibre's holonomy);
  F2 the group generated on the six local solutions at the puncture by the moves' lifts, the fibre's holonomy and the
     parity grading: order, commutant, indicator;
  F3 the indicators of T, T-bar (the moves' group of order 96 on V) and of the parity triplet (the moves' linear parts);
  F4 centraliser dimensions in E8 (characters through SU(3) x SU(2) x SU(6)', the 6 carrying the 6 x 6 matrices) of
     Q8, of one parity's element, and of the odd-trace extension (Q8 with the lift of the order-3 move L^-1 R L^-2),
     with the multiplicities of the extension's complex one-dimensional characters;
  F5 the verdict.

    python3 the_self_conjugate_weave.py   ->  the_self_conjugate_weave.json beside it
"""
import cmath
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_common_point as CP  # noqa: E402
import the_chiral_triplet as CT  # noqa: E402
import the_holomorphic_triplet as HT  # noqa: E402
import the_six_dimensional_census as SC  # noqa: E402  (W24: the 6 x 6 lifts, the fibre's holonomy, commutants)

INV = SC.INV
OMEGA = cmath.exp(2j * cmath.pi / 3)


def closure(gens, n, cap=5000):
    key = lambda M: tuple(np.round(M.flatten(), 7))  # noqa: E731
    G = {key(np.eye(n, dtype=complex)): np.eye(n, dtype=complex)}
    fr = list(G.values())
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = A @ g
                k = key(B)
                if k not in G:
                    G[k] = B
                    nx.append(B)
        fr = nx
        assert len(G) <= cap
    return list(G.values())


def fs(mats):
    return round(float(np.real(sum(np.trace(g @ g) for g in mats)) / len(mats)), 9)


def chi248(h):
    """the 248's character at h, h a 6 x 6 matrix acting on the 6 of SU(6)' in SU(3) x SU(2) x SU(6)'"""
    c = np.poly(h)                                   # x^6 - e1 x^5 + e2 x^4 - e3 x^3 + ...
    e1, e2, e3 = -c[1], c[2], -c[3]
    c6, c15, c20 = e1, e2, e3
    c35 = abs(c6) ** 2 - 1
    val = 8 + 3 + c35 + 3 * c15 + 3 * np.conj(c15) + 6 * c6 + 6 * np.conj(c6) + 2 * c20
    return complex(val)


def average(G, weight=lambda g: 1.0):
    s = sum(chi248(g) * np.conj(weight(g)) for g in G) / len(G)
    return round(s.real, 6), round(s.imag, 6)


def coset_of(h):
    """the block permutation of a 6 x 6 matrix in the block basis: 0 = identity, 1 = the 3-cycle's, 2 = its inverse"""
    P = np.array([[1 if np.linalg.norm(h[2 * i:2 * i + 2, 2 * j:2 * j + 2]) > 1e-6 else 0 for j in range(3)]
                  for i in range(3)])
    return P


def run():
    res = {"rule": "W25_RULE.md (committed 2068244e before this ran)"}
    # F1: Q8 on C^2 and its four characters
    q8 = closure([SC.SR.QM["i"], SC.SR.QM["j"]], 2)
    chars = {"trivial": lambda g: 1.0}
    for name, unit in (("parity with kernel <i>", "i"), ("parity with kernel <j>", "j"), ("parity with kernel <k>", "k")):
        U = SC.SR.QM[unit]
        chars[name] = (lambda U: (lambda g: 1.0 if (np.allclose(g, np.eye(2)) or np.allclose(g, -np.eye(2))
                                                    or np.allclose(g, U) or np.allclose(g, -U)) else -1.0))(U)
    f1 = {"Q8's order": len(q8), "rho_Q (the spin doublet)": fs(q8)}
    for name, ch in chars.items():
        f1[name] = round(sum(ch(g @ g) for g in q8) / len(q8), 9)
    res["F1 Frobenius-Schur indicators of the fibre's holonomy (Q8): +1 real, -1 quaternionic, 0 complex"] = f1
    # F2: the six local solutions
    lifts = [SC.blocks_action(CP.AUT[m], g) for m in ("L", "R") for g in CP.extend(CP.AUT[m])]
    hol = [SC.W_of([1]), SC.W_of([2])]
    grading = [np.kron(np.diag([SC.chi_word(u, [gen]) for u in CT.PAR]), np.eye(2)) for gen in (1, 2)]
    G6 = closure(lifts + hol + grading, 6)
    k6, _ = SC.commutant(lifts + hol + grading, 6)
    res["F2 the group on the six local solutions (moves' lifts, holonomy, grading)"] = {
        "order": len(G6), "commutant (1 = irreducible)": k6, "Frobenius-Schur indicator": fs(G6)}
    Gm = closure(lifts, 6)
    res["F2 ... the moves' lifts alone"] = {"order": len(Gm), "commutant": SC.commutant(lifts, 6)[0],
                                           "Frobenius-Schur indicator of the whole six": fs(Gm)}
    # F3: the moves' group on V (order 96), T and T-bar; the parity triplet (the linear parts at the common point)
    lr = [CT.on_V(CP.AUT[m], g) for m in ("L", "R") for g in CP.extend(CP.AUT[m])]
    GV = CT.closure(lr)
    named, _ = HT.triplets()
    f3 = {"order on V": len(GV)}
    for name, C in named.items():
        f3[name] = round(float(np.real(sum(np.trace(HT.restrict(C, g @ g)) for g in GV)) / len(GV)), 9)
    lin = [np.array(m, dtype=float) for m in ([[1, 0, 0], [0, 0, 1], [0, -1, 0]], [[0, 0, 1], [0, 1, 0], [-1, 0, 0]])]
    GP = closure([m.astype(complex) for m in lin], 3)
    f3["the parity triplet (the moves' linear parts at the common point, the cube's rotations)"] = fs(GP)
    f3["... its order"] = len(GP)
    res["F3 Frobenius-Schur indicators on the cohomology and the tangent space"] = f3
    # F4: centralisers in E8
    Q8 = closure(hol, 6)
    f4 = {}
    d = average(Q8)
    f4["Q8 (W's holonomy, all three parities)"] = {"order": len(Q8), "centraliser dimension": d[0]}
    for gen, nm in ((1, "a"), (2, "b")):
        C4 = closure([SC.W_of([gen])], 6)
        f4["one parity's element alone, <W(%s)>" % nm] = {"order": len(C4), "centraliser dimension": average(C4)[0]}
    w3 = CP.compose(INV["L"], CP.compose(CP.AUT["R"], CP.compose(INV["L"], INV["L"])))
    g3 = CP.extend(w3)
    A3 = [SC.blocks_action(w3, g) for g in g3]
    H3 = closure(hol + A3, 6)
    f4["the order-3 move L^-1 R L^-2: its lifts in 2O"] = len(g3)
    cos = {}
    three = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    for h in H3:
        P = coset_of(h)
        tag = 0 if np.array_equal(P, np.eye(3, dtype=int)) else (1 if np.array_equal(P, three) else 2)
        cos[id(h)] = tag
    omega_char = lambda h: OMEGA ** cos[id(h)]  # noqa: E731
    m_triv = average(H3)
    m_w = average(H3, omega_char)
    m_w2 = average(H3, lambda h: np.conj(omega_char(h)))
    f4["the odd-trace extension: Q8 with the order-3 move's lift"] = {
        "order": len(H3), "centraliser dimension": m_triv[0],
        "multiplicity of the complex character omega (trivial on Q8)": m_w[0],
        "multiplicity of omega^2": m_w2[0],
        "block permutations met (identity, the 3-cycle, its inverse)": sorted({int(v) for v in cos.values()})}
    res["F4 centralisers in E8 (dimensions by characters)"] = f4
    # F5
    q8_self = all(v in (1.0, -1.0) for k, v in f1.items() if k != "Q8's order")
    ext_complex = m_w[0] > 0.5
    res["F5 the verdict"] = {
        "every irreducible of the fibre's holonomy Q8 is real or quaternionic": bool(q8_self),
        "the six local solutions are quaternionic under the weave's forced group": bool(fs(G6) == -1.0),
        "T and T-bar are complex (the weave's complex structure is the moves', on cohomology)": bool(
            f3.get("T") == 0.0 and f3.get("T-bar") == 0.0),
        "one parity's element alone has a centraliser containing E6 (82 = 78 + 3 + 1)": bool(
            all(v["centraliser dimension"] == 82.0 for k, v in f4.items() if k.startswith("one parity"))),
        "the odd-trace extension carries a complex character in the 248": bool(ext_complex),
        "so: on the fibre every gauge reading is self-conjugate; chirality needs a selected parity or the order-3 move "
        "in the holonomy (a thread)": bool(q8_self and ext_complex)}
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_self_conjugate_weave.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False, default=str)
    print(json.dumps(out, indent=1, ensure_ascii=False, default=str))
