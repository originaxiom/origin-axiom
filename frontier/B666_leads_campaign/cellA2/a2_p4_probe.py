"""B666 CELL A' — P4 crash probe: why did the Casimir slot search find
no invertible 2x2 slot pair, and does the robust construction
(abstract eigenvalues from pure summand vectors) work?

Diagnostic only; writes nothing but stdout.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from a2_common import load, log   # noqa: E402

n = load(run_g0=False, need_bar=False)
K, K0, K1 = n.K, n.K0, n.K1
matofSym, coofSym = n.matofSym, n.coofSym
symco = n.symco
rvec = n.rvec

log("probe: trace form Gram + dual basis Yd...")


def trAB(A, B):
    s = K0
    for a in range(27):
        Aa = A[a]
        for b in range(27):
            x = Aa[b]
            if not x.is_zero():
                y = B[b][a]
                if not y.is_zero():
                    s = s + x * y
    return s


X78 = n.E6_BASIS
G = [[trAB(X78[i], X78[j]) for j in range(78)] for i in range(78)]
aug = [G[i][:] + [K1 if j == i else K0 for j in range(78)]
       for i in range(78)]
R, piv = n.rref(aug)
assert piv == list(range(78)), "Gram singular"
Ginv = [[R[i][78 + j] for j in range(78)] for i in range(78)]
Yd = []
for i in range(78):
    Mi = [[K0] * 27 for _ in range(27)]
    for j in range(78):
        c = Ginv[i][j]
        if not c.is_zero():
            Xj = X78[j]
            for a in range(27):
                Xja = Xj[a]
                for b in range(27):
                    if not Xja[b].is_zero():
                        Mi[a][b] = Mi[a][b] + c * Xja[b]
    Yd.append(Mi)
XT = [n.transpose(X) for X in X78]
log("Yd built")


def C2(S):
    out = [[K0] * 27 for _ in range(27)]
    for i in range(78):
        T = n.mmul(n.mmul(Yd[i], S), XT[i])
        for a in range(27):
            Ta = T[a]
            oa = out[a]
            for b in range(27):
                if not Ta[b].is_zero():
                    oa[b] = oa[b] + Ta[b]
    return out


S0 = matofSym(symco(rvec(101), rvec(202)))
S1 = C2(S0)
S2 = C2(S1)
log("probe: the crashed slot search, slot by slot")
slots = [(0, 1), (0, 2), (1, 2), (0, 0), (1, 1), (3, 5)]
for (a, b) in slots:
    log(f"  slot ({a},{b}): S0 = {S0[a][b]}  S1 = {S1[a][b]}  "
        f"S2 = {S2[a][b]}")
for t in range(1, len(slots)):
    (a1, b1), (a2, b2) = slots[t - 1], slots[t]
    det = S1[a1][b1] * S0[a2][b2] - S1[a2][b2] * S0[a1][b1]
    log(f"  det[{slots[t-1]},{slots[t]}] = {det}  zero: {det.is_zero()}")

# global proportionality test: S1 = c * S0 ?
cprop = None
for (a, b) in [(p, q) for p in range(27) for q in range(p, 27)]:
    if not S0[a][b].is_zero():
        cprop = S1[a][b] * S0[a][b].inv()
        break
if cprop is not None:
    prop = all((S1[a][b] - cprop * S0[a][b]).is_zero()
               for a in range(27) for b in range(27))
    log(f"probe: S1 globally proportional to S0: {prop}"
        + (f" (c = {cprop})" if prop else ""))

# how many slots of S0/S1 are zero?
nz0 = sum(1 for a in range(27) for b in range(a, 27)
          if not S0[a][b].is_zero())
nz1 = sum(1 for a in range(27) for b in range(a, 27)
          if not S1[a][b].is_zero())
log(f"probe: nonzero upper slots: S0 {nz0}/378, S1 {nz1}/378")

# global exact relation S2 = al S1 + be S0 via rref on [S0 S1 | S2]
rows = []
for m, (p, q) in enumerate(n.LE):
    rows.append([S0[p][q], S1[p][q], S2[p][q]])
RR, pv = n.rref(rows)
log(f"probe: rref pivots of [S0co S1co S2co] = {pv}")
if pv == [0, 1]:
    be_al = [RR[0][2], RR[1][2]]
    log(f"probe: S2 = ({be_al[1]}) S1 + ({be_al[0]}) S0 candidate")
    al, be = be_al[1], be_al[0]
    ok = all((S2[a][b] - al * S1[a][b] - be * S0[a][b]).is_zero()
             for a in range(27) for b in range(27))
    log(f"probe: relation verified on all slots: {ok}")

# abstract eigenvalues: e_a . e_a is a pure 351' (extreme weight) vector
log("probe: diagonal squares e_a o e_a as C2 eigenvectors...")
for a in (0, 13, 26):
    E = [[K0] * 27 for _ in range(27)]
    E[a][a] = K1
    CE = C2(E)
    lam = CE[a][a]
    iseig = all((CE[p][q] - (lam if (p, q) == (a, a) else K0)).is_zero()
                for p in range(27) for q in range(27))
    log(f"  a = {a}: C2(E_aa)[a][a] = {lam}; eigenvector: {iseig}")

# lamU from an image vector: v = C2(S0) - lamW S0 should be in U
E0 = [[K0] * 27 for _ in range(27)]
E0[0][0] = K1
lamW = C2(E0)[0][0]
V = [[S1[a][b] - lamW * S0[a][b] for b in range(27)] for a in range(27)]
CV = C2(V)
lamU = None
for a in range(27):
    for b in range(27):
        if not V[a][b].is_zero():
            lamU = CV[a][b] * V[a][b].inv()
            break
    if lamU is not None:
        break
iseig = all((CV[a][b] - lamU * V[a][b]).is_zero()
            for a in range(27) for b in range(27))
log(f"probe: lamW = {lamW}; lamU = {lamU}; "
    f"(C2 - lamW)S0 is a C2 eigenvector: {iseig}")
log("PROBE COMPLETE")
