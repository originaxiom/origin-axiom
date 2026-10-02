#!/usr/bin/env python3
"""B1521 -- which class of Out(pi_1 m004) is main's period-2 symmetry P, and does it dualise Ballas' rho_q?

Main's B1297 (section 5.2) writes P in SnapPy's presentation <a, b | aaabABBAb> as a -> a^-1, b -> a^3 b
(orientation-preserving, +1 on the free part). Main's B1455 addendum (2026-10-02) reads B1455's L3 as "L3 with sigma = P"
and states that on Ballas' SL(4) family rho_q o P is dual to rho_q for every q > 0. B1520 (this seat) and B1455's own
table say instead that the swap fixes rho_q and that the inversion (and swap o inversion) dualise it.

This script decides it with no appeal to labels:
  1. An explicit isomorphism between SnapPy's <a, b | aaabABBAb> and B1520's <m, n | mnMNmNMnmN>, found and checked in
     SnapPy's high-precision holonomy, which is faithful (equality of matrices is equality in the group):
     m = ab (SnapPy's meridian), n = g (ab) g^-1 for a short word g; a and b recovered as words in m, n.
  2. P transported to <m, n>: P'(m), P'(n) as words; P' checked to be an automorphism (relator sent to 1, in the holonomy).
  3. H1 sign of P', and whether P' o s^-1 is inner (s: m <-> n), in the holonomy: the conjugator C with
     C rho(s(x)) C^-1 = rho(P'(x)) is found and tested against short group elements (only a sufficient test: a found
     element proves the class; none found is reported as such).
  4. Exact test on Ballas' family at rational q: the intertwiner spaces Hom(rho_q, rho_q o P') and
     Hom(rho_q^*, rho_q o P') (rho^* = inverse transpose), by exact Fraction Gaussian elimination.
Usage: python3 which_class_is_P.py   (writes which_class_is_P.json)"""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
import snappy

HERE = Path(__file__).resolve().parent
TOL = 1e-30


# ---------- words ----------
def inverse_word(w):
    return "".join(c.swapcase() for c in reversed(w))


def reduce_word(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def substitute(w, images):
    """images: dict letter -> word for lower-case letters; upper case gets the inverse."""
    parts = []
    for c in w:
        parts.append(images[c] if c.islower() else inverse_word(images[c.lower()]))
    return reduce_word("".join(parts))


def cyclic_reduce(w):
    w = reduce_word(w)
    while len(w) >= 2 and w[0] == w[-1].swapcase():
        w = w[1:-1]
    return w


def cyclic_rotations(w):
    return {w[i:] + w[:i] for i in range(len(w))}


def reduced_words(letters, max_len):
    yield ""
    frontier = [""]
    for _ in range(max_len):
        nxt = []
        for w in frontier:
            for c in letters:
                if w and w[-1] == c.swapcase():
                    continue
                nxt.append(w + c)
        for w in nxt:
            yield w
        frontier = nxt


# ---------- the faithful holonomy (SnapPy, high precision) ----------
G = snappy.ManifoldHP("m004").fundamental_group()
assert G.generators() == ["a", "b"] and G.relators() == ["aaabABBAb"], (G.generators(), G.relators())
MERIDIAN = G.peripheral_curves()[0][0]
assert MERIDIAN == "ab", MERIDIAN
mp.mp.dps = 60


class M2:
    """2x2 complex matrices at 60 digits (own arithmetic; SnapPy only supplies the entries)."""
    def __init__(self, e):
        self.e = e

    def __mul__(self, o):
        a, b, c, d = self.e
        w, x, y, z = o.e
        return M2((a * w + b * y, a * x + b * z, c * w + d * y, c * x + d * z))

    def inverse(self):
        a, b, c, d = self.e
        det = a * d - b * c
        return M2((d / det, -b / det, -c / det, a / det))


def _num(x):
    return mp.mpf(str(x).replace(" ", ""))


def from_snappy(X):
    return M2(tuple(mp.mpc(_num(X[i, j].real()), _num(X[i, j].imag())) for i in range(2) for j in range(2)))


HOL = {"a": from_snappy(G.SL2C("a")), "b": from_snappy(G.SL2C("b"))}
# SnapPy's SL2C is a lift up to sign: the relator goes to -I. a has exponent sum 3 - 2 = 1 in it, so a -> -a gives a
# genuine SL(2, C) representation (a lift of the faithful holonomy, hence itself faithful).
HOL["a"] = M2(tuple(-v for v in HOL["a"].e))
HOL["A"] = HOL["a"].inverse()
HOL["B"] = HOL["b"].inverse()
ONE = M2((mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)))


def hol(w):
    X = ONE
    for c in w:
        X = X * HOL[c]
    return X


def close(X, Y):
    return max(abs(u - v) for u, v in zip(X.e, Y.e)) < TOL


REL_SNAPPY = "aaabABBAb"
REL_B1520 = "mnMNmNMnmN"
assert close(hol(REL_SNAPPY), ONE)


def main():
    out = {"snappy": {"generators": G.generators(), "relators": G.relators(), "meridian": MERIDIAN}}
    # 1. find g with (m, n) = (ab, g ab g^-1) satisfying B1520's relator
    found = None
    for g in reduced_words("abAB", 6):
        n_word = reduce_word(g + "ab" + inverse_word(g))
        if n_word == "ab":
            continue
        rel = substitute(REL_B1520, {"m": "ab", "n": n_word})
        if close(hol(rel), ONE):
            found = (g, n_word)
            break
    assert found, "no conjugate meridian n found"
    g, n_word = found
    out["iso"] = {"m": "ab", "n": n_word, "conjugator_g": g}
    # recover a and b as words in m, n (search in the holonomy of m = ab, n = g ab g^-1)
    Hm, Hn = hol("ab"), hol(n_word)
    HOLmn = {"m": Hm, "n": Hn, "M": Hm.inverse(), "N": Hn.inverse()}

    def hol_mn(w):
        X = ONE
        for c in w:
            X = X * HOLmn[c]
        return X
    targets = {"a": HOL["a"], "b": HOL["b"]}
    words_ab = {}
    for w in reduced_words("mnMN", 9):
        X = hol_mn(w)
        for k, T in targets.items():
            if k not in words_ab and close(X, T):
                words_ab[k] = w
        if len(words_ab) == 2:
            break
    assert len(words_ab) == 2, words_ab
    out["iso"]["a_in_mn"] = words_ab["a"]
    out["iso"]["b_in_mn"] = words_ab["b"]
    # consistency: SnapPy's relator in the m, n words is 1 (as a word in m, n, read through the holonomy)
    rel_back = substitute(REL_SNAPPY, {"a": words_ab["a"], "b": words_ab["b"]})
    assert close(hol_mn(rel_back), ONE)
    # and the composite m -> ab -> (word in m,n) is m (likewise n): the two maps are mutually inverse
    m_back = substitute("ab", {"a": words_ab["a"], "b": words_ab["b"]})
    n_back = substitute(n_word, {"a": words_ab["a"], "b": words_ab["b"]})
    assert close(hol_mn(m_back), Hm) and close(hol_mn(n_back), Hn)
    out["iso"]["checked"] = "B1520's relator holds for (ab, n) in the faithful holonomy; a, b recovered; both composites are the identity on generators"
    # The isomorphism proved without the holonomy on the B1520 side (free-group words only):
    #   phi: <m,n | R'> -> pi_1, m -> ab, n -> aabA, is well defined (R' -> 1 in the faithful holonomy, above) and onto;
    #   psi: pi_1 -> <m,n | R'>, a -> MnmN, b -> nMNmm, is well defined if psi(R) lies in the normal closure N of R';
    #   psi(phi(m)) m^-1 and psi(phi(n)) n^-1 in N then give psi o phi = id, so phi is injective.
    N_conj = cyclic_rotations(REL_B1520) | cyclic_rotations(inverse_word(REL_B1520))
    pm = reduce_word(substitute(substitute("m", {"m": "ab", "n": n_word}), words_ab) + "M")
    pn = reduce_word(substitute(substitute("n", {"m": "ab", "n": n_word}), words_ab) + "N")
    assert pm == "" and (pn == "" or cyclic_reduce(pn) in N_conj), (pm, pn)
    cw = cyclic_reduce(substitute(REL_SNAPPY, words_ab))
    split = None
    for i in range(len(cw)):
        r = cw[i:] + cw[:i]
        for k in range(1, len(r)):
            if r[:k] in N_conj and r[k:] in N_conj:
                split = (i, r[:k], r[k:])
                break
        if split:
            break
    assert split, "psi(R) not shown to lie in the normal closure of R'"
    out["iso"]["free_group_proof"] = {
        "psi(phi(m)) m^-1": pm, "psi(phi(n)) n^-1 (a cyclic conjugate of R'^+-1)": pn,
        "psi(R) cyclically reduced": cw, "rotated by": split[0], "= u v with u, v cyclic conjugates of R'^+-1": [split[1], split[2]],
        "conclusion": "phi is an isomorphism <m,n | mnMNmNMnmN> -> pi_1(m004) = <a,b | aaabABBAb>"}

    # 2. P in SnapPy's presentation, transported
    P_ab = {"a": "A", "b": "aaab"}
    assert close(hol(substitute(REL_SNAPPY, P_ab)), ONE), "P is not an endomorphism"
    P_m = substitute(substitute("ab", P_ab), {"a": words_ab["a"], "b": words_ab["b"]})
    P_n = substitute(substitute(n_word, P_ab), {"a": words_ab["a"], "b": words_ab["b"]})
    assert close(hol_mn(substitute(REL_B1520, {"m": P_m, "n": P_n})), ONE)
    out["P_transported"] = {"P(m)": P_m, "P(n)": P_n}

    def h1(w):  # m, n both map to the generator of H1 = Z
        return sum(1 if c.islower() else -1 for c in w)
    out["P_transported"]["H1_images"] = [h1(P_m), h1(P_n)]

    # 3. P' o s^-1 inner?  find C with C rho(n) C^-1 = rho(P'(m)) and C rho(m) C^-1 = rho(P'(n)); test C = +-rho(h), h short
    def conj_search(img_m, img_n, src_m, src_n, max_len=8):
        Tm, Tn = hol_mn(img_m), hol_mn(img_n)
        for h in reduced_words("mnMN", max_len):
            H = hol_mn(h)
            Hi = H.inverse()
            if close(H * hol_mn(src_m) * Hi, Tm) and close(H * hol_mn(src_n) * Hi, Tn):
                return h
        return None
    h_s = conj_search(P_m, P_n, "n", "m")
    h_id = conj_search(P_m, P_n, "m", "n")
    out["P_class"] = {"P' = inner o swap, conjugator": h_s, "P' = inner (identity class), conjugator": h_id}

    # 4. exact Ballas test
    res = []
    for q in [F(2), F(3), F(1, 5), F(7, 3), F(1)]:
        rho = ballas(q)
        R = {"m": rho["m"], "n": rho["n"], "M": inv(rho["m"]), "N": inv(rho["n"])}

        def ev(w):
            X = eye()
            for c in w:
                X = mul(X, R[c])
            return X
        img = {"m": ev(P_m), "n": ev(P_n)}
        # sanity: Ballas satisfies both relators
        assert ev(REL_B1520) == eye()
        assert ev(substitute(REL_SNAPPY, {"a": words_ab["a"], "b": words_ab["b"]})) == eye()
        dual = {k: tr(inv(rho[k])) for k in ("m", "n")}
        same = {k: rho[k] for k in ("m", "n")}
        swap = {"m": rho["n"], "n": rho["m"]}
        inversion = {"m": inv(rho["m"]), "n": inv(rho["n"])}
        row = {"q": str(q)}
        for name, src in (("rho_q", same), ("rho_q^*", dual)):
            basis = intertwiners(src, img)  # X with img(g) X = X src(g)
            row[f"Hom({name}, rho_q o P)"] = {"dim": len(basis), "invertible_member": any(det(B) != 0 for B in basis)}
        for name, src in (("rho_q o swap", swap), ("rho_q o inversion", inversion)):
            basis = intertwiners(src, img)
            row[f"Hom({name}, rho_q o P)"] = {"dim": len(basis), "invertible_member": any(det(B) != 0 for B in basis)}
        res.append(row)
    out["ballas"] = res
    generic = [r for r in res if r["q"] != "1"]
    assert all(r["Hom(rho_q, rho_q o P)"]["invertible_member"] and r["Hom(rho_q^*, rho_q o P)"]["dim"] == 0 for r in generic)
    assert out["P_class"]["P' = inner o swap, conjugator"] is not None and out["P_transported"]["H1_images"] == [1, 1]
    out["verdict"] = ("P (main's B1297 period-2 symmetry) is the swap's class in Out(pi_1 m004): P = conj(nM) o swap. "
                      "On Ballas' family rho_q o P is isomorphic to rho_q and NOT to rho_q^* (q = 2, 3, 1/5, 7/3); "
                      "all four coincide at q = 1. The dualising symmetries of the family are the inversion and "
                      "swap o inversion (B1455's table, B1520's D.theta and D.s.theta), not P.")
    (HERE / "which_class_is_P.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(out, indent=1, ensure_ascii=False))


# ---------- exact 4x4 linear algebra over Q ----------
def ballas(q):
    t = q / 2
    m = [[F(1), F(0), F(1), t - 1], [F(0), F(1), F(1), t], [F(0), F(0), F(1), t + F(1, 2)], [F(0), F(0), F(0), F(1)]]
    n = [[F(1), F(0), F(0), F(0)], [2 + 1 / t, F(1), F(0), F(0)], [F(2), F(1), F(1), F(0)], [F(1), F(1), F(0), F(1)]]
    return {"m": m, "n": n}


def eye():
    return [[F(int(i == j)) for j in range(4)] for i in range(4)]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def tr(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]


def inv(A):
    M = [list(A[i]) + eye()[i] for i in range(4)]
    for c in range(4):
        p = next(r for r in range(c, 4) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(4):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[4:] for row in M]


def det(A):
    M = [list(r) for r in A]
    d = F(1)
    for c in range(4):
        p = next((r for r in range(c, 4) if M[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, 4):
            f = M[r][c] / M[c][c]
            M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return d


def nullspace(rows, ncols):
    M = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fc]
        basis.append(v)
    return basis


def intertwiners(src, img):
    """All X (4x4) with img[g] X = X src[g] for g in m, n; returned as matrices."""
    rows = []
    for g in ("m", "n"):
        A, B = img[g], src[g]
        for i in range(4):
            for j in range(4):
                row = [F(0)] * 16
                for k in range(4):
                    row[k * 4 + j] += A[i][k]      # (A X)_ij = sum_k A_ik X_kj
                    row[i * 4 + k] -= B[k][j]      # (X B)_ij = sum_k X_ik B_kj
                rows.append(row)
    return [[[v[i * 4 + j] for j in range(4)] for i in range(4)] for v in nullspace(rows, 16)]


if __name__ == "__main__":
    main()
