#!/usr/bin/env python3
"""W15, part 1: THE HAND THEOREM. W10's chiral triplet at every third tick of every odd-trace thread, proved.

W10 computed on 24 states, and W9's hand rule checked on 758, that at tick 3 the act of every odd-trace state is a
scalar on the weave's triplet T and on its conjugate. This script checks the ingredients of a proof for every word:

  (i)   T is the sum of three lines T_p = T n V_p, one in each parity's doublet V_p; likewise the conjugate triplet.
  (ii)  So a move with a lift acts on T by a monomial matrix in a basis (t_p): it permutes the lines as the move
        permutes the parities mod 2.
  (iii) A monomial 3 x 3 matrix whose permutation is a 3-cycle has its cube equal to its determinant times I. An
        odd-trace word cycles the parities (sm:B1550's parity lemma), so at tick 3 it acts on T as the scalar
        det(w|T), and on the conjugate triplet as the complex conjugate.
  (iv)  det(w|T) is the product of det(m|T) over the letters: a character of the moves, read here in eighths of a turn.
  (v)   So T and its conjugate sit at different kappa exactly when det(w|T) = +-i. With the generators' values this is
        n_L - n_R + 2 [sign -] = 2 (mod 4), W9's hand rule, and exactly one sign twin of each odd-trace word has it.
  (vi)  The swap (GENESIS GM5c) carries T to its conjugate, so the mirror thread sits at the conjugate kappa: the hand
        is mirror-odd. Main's B1487 proves the class index mirror-even; this handle is not an index.

The script checks (i), (ii) and (iv) on the generators with both lifts, (iii) against the direct computation of the
tick-3 act on every odd-trace state to length 8, and (v) on all 758 states of GENESIS to length 12 (both signs).

    python3 the_hand_theorem.py   ->  the_hand_theorem.json beside it
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
import the_weaves_laws as WL  # noqa: E402

TOL = 1e-8


def eighths(z):
    e = cmath.phase(z) / (2 * cmath.pi) * 8
    k = int(round(e)) % 8
    assert abs(abs(z) - 1) < 1e-6 and abs(e - round(e)) < 1e-6, z
    return k


def line_basis(C):
    """the vectors of the piece C (6 x 3) supported in one parity's block, one per block, if each is a line"""
    B = []
    for p in range(3):
        rows = [r for r in range(6) if r // 2 != p]
        _, s, vh = np.linalg.svd(C[rows, :])
        null = int(sum(s < TOL)) + (C.shape[1] - len(s))
        if null != 1:
            return None
        B.append(C @ vh[-1].conj())
    return np.array(B).T


def on_piece(B, M):
    X = np.linalg.lstsq(B, M @ B, rcond=None)[0]
    assert np.allclose(B @ X, M @ B, atol=1e-7)
    return X


def monomial_perm(X):
    """the permutation of a monomial matrix (column i goes to row perm[i]), or None"""
    nz = np.abs(X) > 1e-7
    if not (nz.sum(axis=0) == 1).all() or not (nz.sum(axis=1) == 1).all():
        return None
    return [int(np.argmax(nz[:, i])) for i in range(3)]


def parity_perm(phi):
    return [CT.PAR.index(CT.u_after(u, phi)) for u in CT.PAR]


def generators():
    return {m: [(g, CT.on_V(CP.AUT[m], g)) for g in CP.extend(CP.AUT[m])] for m in ("L", "R", "-I", "P")}


def run():
    gens = generators()
    lr = [M for m in ("L", "R") for _, M in gens[m]]
    G = CT.closure(lr)
    dec, comps = CT.decompose(lr, G)
    assert len(comps) == 2 and dec.get("the two pieces are complex conjugates")
    T, Tb = comps
    BT, BTb = line_basis(T), line_basis(Tb)
    res = {"(0) the group of L and R on V": {"order": len(G), **dec},
           "(i) each triplet is the sum of one line in each parity's doublet": bool(BT is not None and BTb is not None)}
    assert BT is not None and BTb is not None
    # (ii) and (iv) on the generators, both lifts
    gen_rows, det_eighths = {}, {}
    for m, lst in gens.items():
        rows = []
        for g, M in lst:
            par = parity_perm(CP.AUT[m])
            row = {"lift": [round(v, 6) + 0.0 for v in g]}
            if m != "P":
                XT, XTb = on_piece(BT, M), on_piece(BTb, M)
                pT, pTb = monomial_perm(XT), monomial_perm(XTb)
            if m == "P":
                # the swap exchanges the two triplets: T's image lies in the conjugate triplet
                img = M @ BT
                row["carries T to the conjugate triplet"] = bool(np.allclose(BTb @ np.linalg.lstsq(BTb, img, rcond=None)[0],
                                                                         img, atol=1e-7))
            else:
                row.update({"monomial on T and on the conjugate": bool(pT is not None and pTb is not None),
                            "permutation = the move's on the parities": bool(pT == par and pTb == par),
                            "det on T (eighths)": eighths(np.linalg.det(XT)),
                            "det on the conjugate (eighths)": eighths(np.linalg.det(XTb))})
                row["the two dets are conjugate"] = bool((row["det on T (eighths)"] + row["det on the conjugate (eighths)"]) % 8 == 0)
            rows.append(row)
        gen_rows[m] = rows
        if m != "P":
            det_eighths[m] = sorted(r["det on T (eighths)"] for r in rows)
    res["(ii, iv) the generators"] = gen_rows
    res["(iv) det on T by generator (eighths, the two lifts)"] = det_eighths
    # mod 4 the det is lift-independent (a lift's sign multiplies it by (-1)^3); which triplet is called T is a labelling,
    # and the other one has the conjugate values: L and R are 1 and 3 in some order, the sign 2
    mod4 = {m: sorted({d % 4 for d in v}) for m, v in det_eighths.items()}
    res["(iv) det on T mod 4 eighths (lift-independent)"] = mod4
    assert all(len(v) == 1 for v in mod4.values()) and {mod4["L"][0], mod4["R"][0]} == {1, 3} and mod4["-I"] == [2], mod4
    dL, dR, dS = mod4["L"][0], mod4["R"][0], mod4["-I"][0]
    # (iii) against the direct tick-3 act on every odd-trace state to length 8
    direct = {"odd-trace states read": 0, "act at tick 1 monomial with a 3-cycle": 0, "tick-3 act = det(w|T) I on T": 0,
              "and the conjugate on the other triplet": 0}
    for w in WL.states(8):
        for sign in (1, -1):
            phi1 = CP.word_aut(w, sign)
            M1 = CP.mat(w, sign)
            if int(np.trace(M1)) % 2 == 0:
                continue
            direct["odd-trace states read"] += 1
            g = CP.extend(phi1)[0]
            X1 = on_piece(BT, CT.on_V(phi1, g))
            perm = monomial_perm(X1)
            is3 = perm is not None and all(perm[i] != i for i in range(3))
            direct["act at tick 1 monomial with a 3-cycle"] += int(is3)
            d = np.linalg.det(X1)
            A3 = CT.on_V(CT.power(phi1, 3), CT.qpow(g, 3))
            direct["tick-3 act = det(w|T) I on T"] += int(np.allclose(on_piece(BT, A3), d * np.eye(3), atol=1e-6))
            direct["and the conjugate on the other triplet"] += int(np.allclose(on_piece(BTb, A3), np.conj(d) * np.eye(3),
                                                                                atol=1e-6))
    res["(iii) the direct tick-3 act, every odd-trace state to length 8 (both signs)"] = direct
    # (v) the hand rule from the determinant, on all 758 states to length 12
    hand = {"states (both signs)": 0, "odd trace": 0, "det = +-i (the triplets apart)": 0,
            "agrees with n_L - n_R + 2[sign -] = 2 mod 4": 0, "odd-trace words with exactly one twin apart": 0,
            "odd-trace words": 0}
    for w in WL.states(12):
        nL, nR = w.count("L"), w.count("R")
        apart_twins = []
        for sign in (1, -1):
            hand["states (both signs)"] += 1
            if int(np.trace(CP.mat(w, sign))) % 2 == 0:
                continue
            hand["odd trace"] += 1
            d4 = (dL * nL + dR * nR + (dS if sign < 0 else 0)) % 4     # det(w|T) mod 4 eighths, from (iv)
            apart = d4 == 2
            rule = (nL - nR + (2 if sign < 0 else 0)) % 4 == 2
            hand["det = +-i (the triplets apart)"] += int(apart)
            hand["agrees with n_L - n_R + 2[sign -] = 2 mod 4"] += int(apart == rule)
            apart_twins.append(apart)
        if len(apart_twins) == 2:
            hand["odd-trace words"] += 1
            hand["odd-trace words with exactly one twin apart"] += int(sum(apart_twins) == 1)
    res["(v) the hand rule from the determinant, GENESIS's states to length 12"] = hand
    res["summary"] = {
        "(i) holds": res["(i) each triplet is the sum of one line in each parity's doublet"],
        "(ii) holds": all(r.get("monomial on T and on the conjugate", True) and r.get("permutation = the move's on the parities", True)
                          for rows in gen_rows.values() for r in rows),
        "(iii) holds on every odd-trace state to length 8": direct["tick-3 act = det(w|T) I on T"] == direct["odd-trace states read"]
        == direct["and the conjugate on the other triplet"] == direct["act at tick 1 monomial with a 3-cycle"],
        "(v) holds on every odd-trace state to length 12": hand["agrees with n_L - n_R + 2[sign -] = 2 mod 4"] == hand["odd trace"]
        and hand["odd-trace words with exactly one twin apart"] == hand["odd-trace words"],
        "(vi) the swap carries T to the conjugate triplet": all(r["carries T to the conjugate triplet"] for r in gen_rows["P"]),
    }
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_hand_theorem.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(json.dumps(out["summary"]))
    print(json.dumps(out["(iv) det on T by generator (eighths, the two lifts)"]))
    print(json.dumps(out["(iii) the direct tick-3 act, every odd-trace state to length 8 (both signs)"]))
    print(json.dumps(out["(v) the hand rule from the determinant, GENESIS's states to length 12"]))
