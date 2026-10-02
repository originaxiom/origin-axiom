#!/usr/bin/env python3
"""B1520 -- post-run checks (written and run AFTER the sealed population run; disclosed as such in FINDINGS).

The registered outcome is a NEGATIVE (outcome A). Before it is banked, it is checked for a bug by two further means that share no
code with route 1, route 2 or B1512:

X1. A third route at rational points, with own exact Fraction arithmetic only (no sympy, no traces). At q in Q_POINTS, for each of the
    sixteen maps and both targets, the 32 x 16 intertwiner system is solved by own Gaussian elimination. Expected from the sealed
    routes: a map that fixes q has a one-dimensional space with an invertible element towards rho_q and none towards rho_{1/q}
    (q != 1); a map that pairs, the reverse; at q = 1 both targets coincide.
X2. The witness against the audit lane's R47 F14 (received_r47/F14_FINDINGS.txt, section 1, read from the audit lane at 1e3d17b9):
    J(q) with M^T J = J M and N^T J = J N, det J = -q (q^2+q+1)^3 / [16 (q+1)^4]. D.theta's image of rho_q is g -> rho_q(g)^T on
    the generators, so any intertwiner X of D.theta(rho_q) with rho_q satisfies X J = lambda I. Checked exactly at the rational
    points, with X from X1's solver and J typed from F14.
X3. The twist (Lemma Tw) computed, not only proved: for each of the eight maps that fix q, at q = 2 and 1/3 and mu = 3, -2, 5/7,
    Phi(mu (x) rho_q) is compared with mu (x) rho_q and with mu^-1 (x) rho_q (mu (x) rho: m -> mu rho(m), n -> mu rho(n)). Expected:
    isomorphic to mu^e (x) rho_q exactly, e = (sigma's sign on H1) * (-1)^d, from symmetries.json.
X4. The stabiliser of a vacuum, solved directly over all sixteen maps at five vacua: (q, mu) = (2, 3) and (1/3, -2) (generic),
    (2, -1) (mu = +-1), (1, 3) (q = 1) and (1, -1). Expected from the sealed table and Lemma Tw: a map fixes mu (x) rho_q iff it
    fixes q (or q = 1) and mu^e = mu. Recorded with each stabiliser: its orientation-reversing and its count-odd members.
Usage: python3 post_run_check.py   (writes post_run_check.json)"""
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
Q_POINTS = [F(1, 3), F(1, 2), F(5, 7), F(1), F(7, 5), F(2), F(3)]


def ballas(q):
    t = q / 2
    m = [[F(1), F(0), F(1), t - 1], [F(0), F(1), F(1), t], [F(0), F(0), F(1), t + F(1, 2)], [F(0), F(0), F(0), F(1)]]
    n = [[F(1), F(0), F(0), F(0)], [2 + 1 / t, F(1), F(0), F(0)], [F(2), F(1), F(1), F(0)], [F(1), F(1), F(0), F(1)]]
    return {"m": m, "n": n}


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def eye():
    return [[F(int(i == j)) for j in range(4)] for i in range(4)]


def inv(A):
    n = 4
    M = [list(A[i]) + eye()[i] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]


def tr(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]


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


def word(gens, w):
    X = eye()
    for ch in w:
        X = mul(X, gens[ch] if ch.islower() else inv(gens[ch.lower()]))
    return X


def image(rho, sigma, dual):
    out = {}
    for g in ("m", "n"):
        X = word(rho, sigma[g])
        out[g] = tr(inv(X)) if dual else X
    return out


def nullspace(rows, ncols):
    """basis of {x : A x = 0} over Q, own elimination"""
    A = [list(r) for r in rows]
    piv, r = [], 0
    for c in range(ncols):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fc]
        basis.append(v)
    return basis


def intertwiners(S, T):
    """{X : X S(g) = T(g) X}: unknown x_{ab} at index 4a + b; equation (i, j): sum_k X_ik S_kj - T_ik X_kj = 0"""
    rows = []
    for g in ("m", "n"):
        for i in range(4):
            for j in range(4):
                row = [F(0)] * 16
                for k in range(4):
                    row[4 * i + k] += S[g][k][j]
                    row[4 * k + j] -= T[g][i][k]
                rows.append(row)
    return [[[v[4 * a + b] for b in range(4)] for a in range(4)] for v in nullspace(rows, 16)]


def f14_J(q):
    A, B, C = q / 4, q / (2 * (q + 1)), (q * q + 1) / (2 * (q + 1))
    return [[A, -A, B, C], [-A, A, -B, B], [B, -B, F(1), F(-1)], [C, B, F(-1), F(1)]]


def main():
    sym = json.loads((HERE / "symmetries.json").read_text(encoding="utf-8"))
    reps = {k: {"m": v["m"], "n": v["n"]} for k, v in sym["representatives"].items()}
    dec = json.loads((HERE / "decide.json").read_text(encoding="utf-8"))
    fixes = set(dec["stabiliser of a vacuum q != 1 (maps fixing every q)"])
    x1_rows, x1_ok = [], True
    x2_rows, x2_ok = [], True
    for q in Q_POINTS:
        rho, rho_inv = ballas(q), ballas(1 / q)
        for name, sig in reps.items():
            for dual in (False, True):
                key = ("D." if dual else "") + name
                S = image(rho, sig, dual)
                rec = {"q": str(q), "map": key}
                for label, T in (("to rho_q", rho), ("to rho_{1/q}", rho_inv)):
                    B = intertwiners(S, T)
                    rec[label] = [len(B), len(B) == 1 and det(B[0]) != 0]
                if q == 1:
                    expect = {"to rho_q": [1, True], "to rho_{1/q}": [1, True]}
                elif key in fixes:
                    expect = {"to rho_q": [1, True], "to rho_{1/q}": [0, False]}
                else:
                    expect = {"to rho_q": [0, False], "to rho_{1/q}": [1, True]}
                rec["as the sealed routes decided"] = all(rec[k] == v for k, v in expect.items())
                x1_ok &= rec["as the sealed routes decided"]
                x1_rows.append(rec)
        # X2: the witness against R47 F14
        J = f14_J(q)
        f14_holds = all(mul(tr(rho[g]), J) == mul(J, rho[g]) for g in ("m", "n"))
        dJ = det(J)
        dJ_formula = -q * (q * q + q + 1) ** 3 / (16 * (q + 1) ** 4)
        X = intertwiners(image(rho, reps["theta"], True), rho)
        XJ = mul(X[0], J) if len(X) == 1 else None
        scalar = XJ is not None and all(XJ[i][j] == (XJ[0][0] if i == j else 0) for i in range(4) for j in range(4)) and XJ[0][0] != 0
        x2_rows.append({"q": str(q), "M^T J = J M and N^T J = J N": f14_holds, "det J = F14's formula": dJ == dJ_formula,
                        "dim of D.theta's intertwiners": len(X), "X J = lambda I, lambda != 0": scalar})
        x2_ok &= f14_holds and dJ == dJ_formula and scalar
    x3_rows, x3_ok = [], True
    for q in (F(2), F(1, 3)):
        rho = ballas(q)
        for mu in (F(3), F(-2), F(5, 7)):
            tw = {g: [[mu * x for x in r] for r in rho[g]] for g in ("m", "n")}
            tw_inv = {g: [[x / mu for x in r] for r in rho[g]] for g in ("m", "n")}
            for key in sorted(fixes):
                dual = key.startswith("D.")
                name = key[2:] if dual else key
                e = sym["representatives"][name]["on H1"] * (-1 if dual else 1)
                S = image(tw, reps[name], dual)
                a, b = intertwiners(S, tw), intertwiners(S, tw_inv)
                got = [len(a) == 1 and det(a[0]) != 0, len(b) == 1 and det(b[0]) != 0]
                ok = got == ([True, False] if e == 1 else [False, True])
                x3_ok &= ok
                x3_rows.append({"q": str(q), "mu": str(mu), "map": key, "e": e, "to mu rho, to mu^-1 rho": got, "as Lemma Tw": ok})
    x4_rows, x4_ok = [], True
    orient = {k: v["orientation"] for k, v in sym["representatives"].items()}
    for q, mu in ((F(2), F(3)), (F(1, 3), F(-2)), (F(2), F(-1)), (F(1), F(3)), (F(1), F(-1))):
        rho = ballas(q)
        tw = {g: [[mu * x for x in r] for r in rho[g]] for g in ("m", "n")}
        stab, expect = [], []
        for name, sig in reps.items():
            for dual in (False, True):
                key = ("D." if dual else "") + name
                e = sym["representatives"][name]["on H1"] * (-1 if dual else 1)
                B = intertwiners(image(tw, sig, dual), tw)
                if len(B) == 1 and det(B[0]) != 0:
                    stab.append(key)
                if (q == 1 or key in fixes) and (e == 1 or mu * mu == 1):
                    expect.append(key)
        ok = sorted(stab) == sorted(expect)
        x4_ok &= ok
        x4_rows.append({"q": str(q), "mu": str(mu), "stabiliser": sorted(stab), "order": len(stab), "as expected": ok,
                        "orientation-reversing members": sorted(k for k in stab if orient[k[2:] if k.startswith("D.") else k] == "reversed"),
                        "count-odd members": sorted(k for k in stab if k.startswith("D."))})
    out = {"X1 third route at rational points (own Fraction elimination)": {"points": [str(q) for q in Q_POINTS],
                                                                            "all 224 decisions as sealed": x1_ok,
                                                                            "rows": x1_rows},
           "X2 the witness D.theta against R47 F14's J": {"all points": x2_ok, "rows": x2_rows}}
    out["X3 the twist computed (Lemma Tw)"] = {"all 48 as Lemma Tw": x3_ok, "rows": x3_rows}
    out["X4 the stabiliser of a vacuum, all sixteen maps"] = {"all five as expected": x4_ok, "rows": x4_rows}
    out["passed"] = x1_ok and x2_ok and x3_ok and x4_ok
    (HERE / "post_run_check.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"X1 all as sealed": x1_ok, "X2 all points": x2_ok, "X3 all as Lemma Tw": x3_ok, "X4": x4_rows,
                      "passed": out["passed"]}, indent=1))


if __name__ == "__main__":
    main()
