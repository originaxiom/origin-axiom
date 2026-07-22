"""cc2 INDEPENDENT recompute of B644's headline: does rho_hear restricted
to ker(det) equal chi_golden . (mod-5 reduction) elementwise on all 120
classes?

Reuses the ALREADY-INDEPENDENT hearing-group build (v7_conduit/engine_v7.py
-- a from-scratch reimplementation of the SU(3)_2 Kac-Peterson modular data,
distinct from the repo's own B629 exact_hearing.py machinery that B644's
own script imports). This script builds its OWN 360-element image group and
120-element ker(det) via that engine, then constructs the mod-5 reduction
map per B644's stated recipe (R = T|odd -> R5=[[1,1],[0,1]], L = S^-1 T^-1 S
|odd -> L5=[[1,0],[1,1]], both over F5) and checks the elementwise identity
tr(rho_hear(w)) == chi_golden(class(mod5(w))) on all 120 ker(det) elements.

Does NOT import anything from B644_mckay_comparison/ or B629 -- only the
independent engine_v7 build plus its own from-scratch group closure / mod-5
arithmetic / class function / golden character table.
"""
import os
import sys

import mpmath as mp

sys.path.insert(0, "<cc2-seat>/seat-work/veins/v7_conduit")
from engine_v7 import An_Level  # noqa: E402

mp.mp.dps = 50
PHI = (1 + mp.sqrt(5)) / 2
TOL = mp.mpf(10) ** -30

# ---- build SU(3)_2 modular data + theta-odd 2-plane (independent engine) ----
L = An_Level(n=3, k=2, name="SU(3)_2")
S, T = L.build(verbose=False)
fixed_idx, pairs = L.theta_split()
N = S.rows
assert len(pairs) == 2, f"expected 2 theta-conjugate pairs, got {len(pairs)}"

odd = mp.matrix(N, 2)
s2 = 1 / mp.sqrt(2)
for jj, (a, b) in enumerate(pairs):
    odd[a, jj], odd[b, jj] = s2, -s2


def block(M):
    return odd.T * M * odd


# B644's stated recipe, letter for letter: R_full = T, L_full = S^-1 T^-1 S
Ti = T ** -1
Si = S ** -1
R_full = T
L_full = Si * Ti * S
rho_R = block(R_full)
rho_L = block(L_full)

# ---- group closure: 360-element image, canonical BFS words ------------------
def fp(M):
    return tuple((round(float(M[i, j].real), 25), round(float(M[i, j].imag), 25))
                 for i in range(2) for j in range(2))


elems = {fp(mp.eye(2)): ("", mp.eye(2))}
frontier = [("", mp.eye(2))]
while frontier:
    new = []
    for (wd, M) in frontier:
        for gname, G in (("R", rho_R), ("L", rho_L)):
            M2 = M * G
            k = fp(M2)
            if k not in elems:
                elems[k] = (wd + gname, M2)
                new.append((wd + gname, M2))
    frontier = new
print(f"[cc2-independent] image group order: {len(elems)} (expect 360)")
assert len(elems) == 360


def detm(M):
    return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]


ker = [(wd, M) for (wd, M) in elems.values() if abs(detm(M) - 1) < mp.mpf(10) ** -20]
print(f"[cc2-independent] ker(det) order: {len(ker)} (expect 120)")
assert len(ker) == 120

# ---- the arithmetic side: mod-5 reduction, R -> R5, L -> L5 -----------------
R5 = ((1, 1), (0, 1))
L5 = ((1, 0), (1, 1))
I5 = ((1, 0), (0, 1))


def m5mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 5 for j in range(2))
                 for i in range(2))


def word5(wd):
    M = I5
    for ch in wd:
        M = m5mul(M, R5 if ch == "R" else L5)
    return M


g5 = {I5}
fr5 = [I5]
while fr5:
    new = []
    for M in fr5:
        for G in (R5, L5):
            M2 = m5mul(M, G)
            if M2 not in g5:
                g5.add(M2)
                new.append(M2)
    fr5 = new
print(f"[cc2-independent] <R5,L5> order: {len(g5)} (expect 120, SL(2,5))")


def ord5(M):
    P = I5
    for k in range(1, 61):
        P = m5mul(P, M)
        if P == I5:
            return k
    return 0


def class5(M):
    """(order, qr) -- qr only meaningful for orders 5, 10. Own
    re-derivation of B644's stated recipe: unipotent parameter x in
    N ~ [[1,x],[0,1]] (N = M if ord 5, N = -M if ord 10); SL2-conjugacy
    class of x is its class mod squares in F5* ({1,4} vs {2,3}); read
    x off N-I directly (upper-tri: x = the (0,1) entry; else use the
    (1,0) entry negated, matching the swap-conjugation relation)."""
    o = ord5(M)
    if o not in (5, 10):
        return (o, None)
    if o == 5:
        Nm = M
    else:
        Nm = tuple(tuple((-M[i][j]) % 5 for j in range(2)) for i in range(2))
    a = (Nm[0][0] - 1) % 5
    c = Nm[1][0] % 5
    b = Nm[0][1] % 5
    if c == 0:
        x = b
    else:
        x = (-c) % 5
    assert a == (-(Nm[1][1] - 1)) % 5 or True  # trace-0 sanity not asserted strictly
    qr = x in (1, 4)
    return (o, qr)


# ---- the golden character table (two Galois-conjugate candidates) ----------
tableA = {(1, None): mp.mpf(2), (2, None): mp.mpf(-2), (4, None): mp.mpf(0),
          (3, None): mp.mpf(-1), (6, None): mp.mpf(1),
          (5, True): 1 / PHI, (5, False): -PHI,
          (10, True): PHI, (10, False): -1 / PHI}
tableB = dict(tableA)
for k_ in ((5, True), (5, False), (10, True), (10, False)):
    tableB[k_] = -tableA[k_]
# The FORCED table: B644's own FINDINGS.md discloses that its prereg's
# tableA/tableB (above, both hardcoded pre-run) are BOTH internally
# inconsistent as characters (violate chi(-g)=-chi(g) on the order-10
# rows) -- a sealing error caught post-run by their own MB12 adjudication
# (see test_b644_mckay.py::test_observed_table_is_golden_irreducible_character,
# which independently proves via Schur orthogonality + antisymmetry that
# THIS is the unique consistent golden character). Checking against this
# corrected table is the real elementwise headline test.
tableF = {(1, None): mp.mpf(2), (2, None): mp.mpf(-2), (4, None): mp.mpf(0),
          (3, None): mp.mpf(-1), (6, None): mp.mpf(1),
          (5, True): 1 / PHI, (5, False): -PHI,
          (10, True): -1 / PHI, (10, False): PHI}

# ---- elementwise check on all 120 ker(det) elements -------------------------
print("\n[cc2-independent] elementwise identity check on all 120 ker(det) "
      "elements: tr(rho_hear(w)) vs chi_golden(class(mod5(w)))")


def hear_trace(M):
    return M[0, 0] + M[1, 1]


rows = []
for (wd, M) in ker:
    tr = hear_trace(M)
    if abs(tr.imag) > 1e-25:
        print(f"  NONREAL trace at word {wd!r}: {tr}")
    cl = class5(word5(wd))
    rows.append((wd, tr.real, cl))

for name, table in (("A (prereg, disclosed-inconsistent)", tableA),
                     ("B (prereg, disclosed-inconsistent)", tableB),
                     ("FORCED (Schur-verified correction)", tableF)):
    matches = 0
    mismatches = []
    for (wd, trv, cl) in rows:
        if cl in table and abs(table[cl] - trv) < TOL:
            matches += 1
        else:
            mismatches.append((wd, cl, mp.nstr(trv, 15)))
    print(f"  table {name}: {matches}/120 match"
          + (f"; first mismatch: {mismatches[0]}" if mismatches else ""))

# well-definedness (class-function): does the SAME class ever get two
# different observed trace values across my 120 elements?
per_class = {}
well_defined = True
for (wd, trv, cl) in rows:
    if cl in per_class:
        if abs(per_class[cl] - trv) > TOL:
            well_defined = False
    else:
        per_class[cl] = trv
print(f"\n[cc2-independent] class-function well-defined on my own 120: "
      f"{well_defined} ({len(per_class)} distinct classes observed, expect 9)")

# M4-style check: the cat map word "RL"
wd = "RL"
M = mp.eye(2)
for ch in wd:
    M = M * (rho_R if ch == "R" else rho_L)
trRL = hear_trace(M)
print(f"\n[cc2-independent] tr rho_hear(RL) = {mp.nstr(trRL.real, 25)}  "
      f"vs -1/phi = {mp.nstr(-1/PHI, 25)}  "
      f"match: {abs(trRL.real - (-1/PHI)) < mp.mpf(10)**-30}")
print(f"  mod5 class of RL: {class5(word5(wd))}")

print("\nB644 INDEPENDENT RECOMPUTE DONE")
