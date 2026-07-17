#!/usr/bin/env python3
"""B662 CELL I — the gamma5' upstream mathematics: the exact character map.

Task 1: decide by EXACT character arithmetic whether the ear's hearing
representation (B640/B644: rho_hear|ker(det) = chi_golden o mod-5, on
2I = SL(2,5)) IS the modular-flavor literature's Gamma_5'-doublet rep
2-hat or 2-hat' (Yao-Liu-Ding, arXiv:2011.03501, Table 11), under the
CANONICAL identification Gamma_5' = SL(2,Z)/Gamma(5) = SL(2,F5),
S -> [[0,1],[-1,0]], T -> [[1,1],[0,1]] (their Eq. (2), Eq. (5)).

Task 2: the weight-5 mechanism (H129): level-5 integral-weight forms =
degree-5k polynomials in the two weight-1/5 forms F1, F2 (their Eqs.
(12)-(14), ref [68] = Ibukiyama), whose projective SL(2,5)-action (their
Eq. (13)) is 2-hat up to 20th-root scalars that die on Sym^{5k}; hence
M_k(Gamma(5)) = Sym^{5k}(2-hat) as Gamma_5'-reps. Decompose exactly for
k = 1..6 (cross-check their Table 1) and locate the first doublet
occurrence: the Kostant/McKay generating function with the binary-
icosahedral invariant degrees 12, 20 forces first 5|n occurrence at
n = 25, i.e. weight 5.

Everything exact: arithmetic in Q(zeta_20) with Fraction coefficients
modulo Phi_20(x) = x^8 - x^6 + x^4 - x^2 + 1. No floats anywhere.
Gate 5 clean: pure representation theory; no SM values.
"""
from fractions import Fraction as Fr
from itertools import product

# ---------------------------------------------------------------------------
# S0. The exact cyclotomic field Q(zeta_20)
# ---------------------------------------------------------------------------
DEG = 8
# Phi_20(x) = x^8 - x^6 + x^4 - x^2 + 1  =>  x^8 = x^6 - x^4 + x^2 - 1
RED = (Fr(-1), Fr(0), Fr(1), Fr(0), Fr(-1), Fr(0), Fr(1), Fr(0))  # coeffs of x^8


def fzero():
    return (Fr(0),) * DEG


def fone():
    return (Fr(1),) + (Fr(0),) * (DEG - 1)


def fadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def fsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def fneg(a):
    return tuple(-x for x in a)


def fscale(a, r):
    return tuple(x * r for x in a)


def fmul(a, b):
    raw = [Fr(0)] * (2 * DEG - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    raw[i + j] += x * y
    # reduce degrees 14..8 downward via x^8 = RED
    for d in range(2 * DEG - 2, DEG - 1, -1):
        c = raw[d]
        if c:
            raw[d] = Fr(0)
            for j, r in enumerate(RED):
                raw[d - DEG + j] += c * r
    return tuple(raw[:DEG])


def fpow(a, n):
    r = fone()
    while n:
        if n & 1:
            r = fmul(r, a)
        a = fmul(a, a)
        n >>= 1
    return r


def zeta(k):
    """zeta_20^k as a field element."""
    k %= 20
    v = [Fr(0)] * DEG
    v[0] = Fr(1)
    e = tuple(v)
    x = tuple([Fr(0), Fr(1)] + [Fr(0)] * (DEG - 2))
    return fmul(e, fpow(x, k)) if k else fone()


def finv(a):
    """Field inverse by solving (mult-by-a) v = e0 with Fractions."""
    # columns of M = a * x^j
    cols = []
    xj = fone()
    x = zeta(1)
    for j in range(DEG):
        cols.append(fmul(a, xj))
        xj = fmul(xj, x)
    # augmented system M v = e0  (M[i][j] = cols[j][i])
    A = [[cols[j][i] for j in range(DEG)] + [Fr(1) if i == 0 else Fr(0)]
         for i in range(DEG)]
    for c in range(DEG):
        p = next(r for r in range(c, DEG) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(DEG):
            if r != c and A[r][c]:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return tuple(A[i][DEG] for i in range(DEG))


def galois(a, k):
    """The automorphism zeta -> zeta^k (k coprime to 20)."""
    out = fzero()
    for j, c in enumerate(a):
        if c:
            out = fadd(out, fscale(zeta(j * k), c))
    return out


def fconj(a):
    return galois(a, 19)


# named constants
ONE, ZERO = fone(), fzero()
II = zeta(5)                       # i
W5 = zeta(4)                       # omega_5 = e^{2 pi i / 5}
PHI = fadd(zeta(2), zeta(18))      # 2 cos(pi/5) = golden ratio phi
SQRT5 = fsub(fscale(PHI, Fr(2)), ONE)          # sqrt(5) = 2 phi - 1
C10 = fadd(zeta(1), zeta(19))      # 2 cos(pi/10) = sqrt(sqrt(5) phi)
INV_C10 = finv(C10)
IPHI = fsub(PHI, ONE)              # 1/phi = phi - 1

NAMED = [("2", fscale(ONE, Fr(2))), ("-2", fscale(ONE, Fr(-2))),
         ("1", ONE), ("-1", fneg(ONE)), ("0", ZERO),
         ("phi", PHI), ("-phi", fneg(PHI)),
         ("1/phi", IPHI), ("-1/phi", fneg(IPHI))]


def fname(a):
    for nm, v in NAMED:
        if a == v:
            return nm
    return str(a)


print("== S0: exact field self-tests (Q(zeta_20)) ==")
t0 = fadd(fsub(fadd(fsub(fpow(zeta(1), 8), fpow(zeta(1), 6)),
                    fpow(zeta(1), 4)), fpow(zeta(1), 2)), ONE)
print(f"  Phi_20(zeta) = 0: {t0 == ZERO}")
print(f"  i^2 = -1: {fmul(II, II) == fneg(ONE)}")
print(f"  omega_5^5 = 1: {fpow(W5, 5) == ONE}")
print(f"  phi^2 = phi + 1: {fmul(PHI, PHI) == fadd(PHI, ONE)}")
print(f"  (2cos(pi/10))^2 = sqrt5*phi: "
      f"{fmul(C10, C10) == fmul(SQRT5, PHI)}")
print(f"  1/phi = phi - 1 consistent: {fmul(PHI, IPHI) == ONE}")
print(f"  galois zeta->zeta^3 sends sqrt5 -> -sqrt5: "
      f"{galois(SQRT5, 3) == fneg(SQRT5)}")

# ---------------------------------------------------------------------------
# 2x2 exact matrices
# ---------------------------------------------------------------------------


def mmul(A, B):
    return ((fadd(fmul(A[0][0], B[0][0]), fmul(A[0][1], B[1][0])),
             fadd(fmul(A[0][0], B[0][1]), fmul(A[0][1], B[1][1]))),
            (fadd(fmul(A[1][0], B[0][0]), fmul(A[1][1], B[1][0])),
             fadd(fmul(A[1][0], B[0][1]), fmul(A[1][1], B[1][1]))))


def mscale(A, s):
    return tuple(tuple(fmul(s, x) for x in row) for row in A)


def mtrace(A):
    return fadd(A[0][0], A[1][1])


MID = ((ONE, ZERO), (ZERO, ONE))
MNEG = ((fneg(ONE), ZERO), (ZERO, fneg(ONE)))

# ---------------------------------------------------------------------------
# S1. The literature matrices (Yao-Liu-Ding arXiv:2011.03501, Table 11)
#   rho_2(S)  = i sqrt(1/(sqrt5 phi)) [[phi, 1], [1, -phi]],
#   rho_2(T)  = diag(w5^2, w5^3)
#   rho_2p(S) = i sqrt(1/(sqrt5 phi)) [[1, phi], [phi, -1]],
#   rho_2p(T) = diag(w5, w5^4);   rho(R) = -I on both.
# ---------------------------------------------------------------------------
cS = fmul(II, INV_C10)   # i / (2 cos(pi/10)) = i * sqrt(1/(sqrt5 phi))
R2_S = ((fmul(cS, PHI), cS), (cS, fneg(fmul(cS, PHI))))
R2_T = ((fpow(W5, 2), ZERO), (ZERO, fpow(W5, 3)))
R2P_S = ((cS, fmul(cS, PHI)), (fmul(cS, PHI), fneg(cS)))
R2P_T = ((W5, ZERO), (ZERO, fpow(W5, 4)))

print("\n== S1: Gamma_5' presentation checks on the literature matrices ==")
print("   (S^2 = R = -1, S^4 = T^5 = (ST)^3 = 1, S^2 T = T S^2;")
print("    Yao-Liu-Ding Eqs. (4), (A.1)-(A.2), with their S = [[0,1],[-1,0]])")
for nm, (MS, MT) in (("2-hat", (R2_S, R2_T)), ("2-hat'", (R2P_S, R2P_T))):
    S2 = mmul(MS, MS)
    S4 = mmul(S2, S2)
    T5 = MT
    for _ in range(4):
        T5 = mmul(T5, MT)
    ST = mmul(MS, MT)
    ST3 = mmul(mmul(ST, ST), ST)
    comm = mmul(S2, MT) == mmul(MT, S2)
    print(f"  {nm}: S^2 = -I: {S2 == MNEG}; S^4 = I: {S4 == MID}; "
          f"T^5 = I: {T5 == MID}; (ST)^3 = I: {ST3 == MID}; "
          f"S^2T = TS^2: {comm}")

# ---------------------------------------------------------------------------
# S2. Generate SL(2,5) concretely (mod-5) and both exact reps by BFS.
#     Canonical identification: S -> [[0,1],[-1,0]], T -> [[1,1],[0,1]] mod 5.
# ---------------------------------------------------------------------------


def m5mul(A, B):
    return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5),
            ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5))


S5 = ((0, 1), (4, 0))
T5 = ((1, 1), (0, 1))
I5 = ((1, 0), (0, 1))
NI5 = ((4, 0), (0, 4))

print("\n== S2: BFS closure of SL(2,5) with both exact reps attached ==")
elems = {I5: (MID, MID)}
frontier = [I5]
collisions = 0
bad = 0
while frontier:
    nxt = []
    for g in frontier:
        A2, A2P = elems[g]
        for g5, m2, m2p in ((S5, R2_S, R2P_S), (T5, R2_T, R2P_T)):
            h = m5mul(g, g5)
            B2, B2P = mmul(A2, m2), mmul(A2P, m2p)
            if h in elems:
                collisions += 1
                if elems[h] != (B2, B2P):
                    bad += 1
            else:
                elems[h] = (B2, B2P)
                nxt.append(h)
    frontier = nxt
print(f"  |group| = {len(elems)} (must be 120)")
print(f"  well-definedness: {collisions} collisions checked, "
      f"{bad} exact-matrix mismatches (must be 0)")
scal = [g for g, (A, _) in elems.items() if A[0][1] == ZERO
        and A[1][0] == ZERO and A[0][0] == A[1][1]]
print(f"  kernel of 2-hat (elements with scalar +/-I image): {scal} "
      f"-> faithful up to center: {sorted(scal) == sorted([I5, NI5])}")
print(f"  rho(R): image of -I mod 5 is -I in both reps: "
      f"{elems[NI5] == (MNEG, MNEG)}")

# ---------------------------------------------------------------------------
# S3. Conjugacy classes of the concrete group + the B644 class invariant.
# ---------------------------------------------------------------------------


def m5order(M):
    P, k = M, 1
    while P != I5:
        P = m5mul(P, M)
        k += 1
    return k


def class5(M):
    """B644's (order, qr-type) invariant, reimplemented verbatim."""
    o = m5order(M)
    if o not in (5, 10):
        return (o, None)
    N = M if o == 5 else m5mul(NI5, M)
    a = (N[0][0] - 1) % 5
    b = N[0][1] % 5
    c = N[1][0] % 5
    if c == 0 and a == 0:
        x = b
    elif c != 0:
        x = (-c) % 5
    else:
        x = b
    return (o, x in (1, 4))


all_g = list(elems)
inv_of = {}
for g in all_g:
    P = g
    while m5mul(P, g) != I5:
        P = m5mul(P, g)
    inv_of[g] = P  # g^{-1} (P*g = I)

classes = []
seen = set()
for g in all_g:
    if g in seen:
        continue
    orb = {m5mul(m5mul(h, g), inv_of[h]) for h in all_g}
    seen |= orb
    classes.append(sorted(orb))
print("\n== S3: conjugacy classes of SL(2,5) ==")
cls_info = []
for orb in classes:
    invs = {class5(g) for g in orb}
    assert len(invs) == 1, "B644 invariant not constant on a class!"
    cls_info.append((invs.pop(), len(orb), orb[0], orb))
cls_info.sort(key=lambda t: (t[0][0], str(t[0][1])))
for inv, sz, rep, _ in cls_info:
    print(f"  class {inv}: size {sz}, representative {rep}")
print(f"  number of classes: {len(cls_info)} (must be 9); "
      f"sizes sum: {sum(sz for _, sz, _, _ in cls_info)}")

# literature class labels via their representatives (Table 10 header)
lit_reps = {"1C1": I5, "1C2 (R)": NI5,
            "20C3 (ST)": m5mul(S5, T5),
            "30C4 (S)": S5,
            "12C5 (T)": T5,
            "12C5' (T^2)": m5mul(T5, T5),
            "20C6 (S^3T)": m5mul(m5mul(m5mul(S5, S5), S5), T5),
            "12C10 (TR)": m5mul(T5, NI5),
            "12C10' (T^2R)": m5mul(m5mul(T5, T5), NI5)}
lit_label = {}
for lab, m in lit_reps.items():
    lit_label[class5(m)] = lab

# ---------------------------------------------------------------------------
# S4. The exact character tables of 2-hat and 2-hat' on the concrete classes.
# ---------------------------------------------------------------------------
print("\n== S4: exact characters of the literature doublets by class ==")
chi2, chi2p = {}, {}
for inv, sz, rep, orb in cls_info:
    A2, A2P = elems[rep]
    v2, v2p = mtrace(A2), mtrace(A2P)
    # constancy on the whole class (exact):
    for g in orb:
        B2, B2P = elems[g]
        assert mtrace(B2) == v2 and mtrace(B2P) == v2p
    chi2[inv], chi2p[inv] = v2, v2p
    print(f"  {lit_label[inv]:>14}  (ord,qr)={str(inv):>11} size {sz:>2}: "
          f"chi_2hat = {fname(v2):>6}, chi_2hat' = {fname(v2p):>6}")

# cross-check against the extracted Table 10 rows (access 2026-07-17):
tab10_2 = {"1C1": "2", "1C2 (R)": "-2", "20C3 (ST)": "-1", "30C4 (S)": "0",
           "12C5 (T)": "-phi", "12C5' (T^2)": "1/phi", "20C6 (S^3T)": "1",
           "12C10 (TR)": "phi", "12C10' (T^2R)": "-1/phi"}
tab10_2p = {"1C1": "2", "1C2 (R)": "-2", "20C3 (ST)": "-1", "30C4 (S)": "0",
            "12C5 (T)": "1/phi", "12C5' (T^2)": "-phi", "20C6 (S^3T)": "1",
            "12C10 (TR)": "-1/phi", "12C10' (T^2R)": "phi"}
ok2 = all(fname(chi2[inv]) == tab10_2[lit_label[inv]]
          for inv, _, _, _ in cls_info)
ok2p = all(fname(chi2p[inv]) == tab10_2p[lit_label[inv]]
           for inv, _, _, _ in cls_info)
print(f"  matches the extracted Table 10 row for 2-hat:  {ok2}")
print(f"  matches the extracted Table 10 row for 2-hat': {ok2p}")

gal_pair = all(galois(chi2p[inv], 3) == chi2[inv] for inv, _, _, _ in cls_info)
print(f"  Galois pair (sqrt5 -> -sqrt5 sends chi_2hat' -> chi_2hat, "
      f"class-by-class): {gal_pair}")

# ---------------------------------------------------------------------------
# S5. The ear's banked character (B644, verified table) vs the doublets.
# ---------------------------------------------------------------------------
print("\n== S5: the ear's character (B644 banked, corrected table) ==")
ear = {(1, None): fscale(ONE, Fr(2)), (2, None): fscale(ONE, Fr(-2)),
       (4, None): ZERO, (3, None): fneg(ONE), (6, None): ONE,
       (5, True): IPHI, (5, False): fneg(PHI),
       (10, True): fneg(IPHI), (10, False): PHI}
# re-verify the banked table's character identities exactly:
sch = ZERO
for inv, sz, _, _ in cls_info:
    sch = fadd(sch, fscale(fmul(ear[inv], fconj(ear[inv])), Fr(sz)))
print(f"  Schur <chi_ear, chi_ear> = 1: {sch == fscale(ONE, Fr(120))}")
par = (ear[(2, None)] == fneg(ear[(1, None)])
       and ear[(6, None)] == fneg(ear[(3, None)])
       and ear[(10, True)] == fneg(ear[(5, True)])
       and ear[(10, False)] == fneg(ear[(5, False)]))
print(f"  chi(-g) = -chi(g) on all paired classes: {par}")

m2 = all(ear[inv] == chi2[inv] for inv, _, _, _ in cls_info)
m2p = all(ear[inv] == chi2p[inv] for inv, _, _, _ in cls_info)
print(f"  chi_ear == chi_2hat  (all 9 classes): {m2}")
print(f"  chi_ear == chi_2hat' (all 9 classes): {m2p}")

cat = m5mul(T5, ((1, 0), (1, 1)))  # the cat map RL mod 5 (letters R=T, L)
ccat = class5(cat)
print(f"  cat map RL mod 5 = {cat}, class {ccat} = {lit_label[ccat]}")
print(f"  chi_2hat'(cat) = {fname(chi2p[ccat])}  "
      f"(banked B640/B644 headline: tr rho_hear(RL) = -1/phi)")
print(f"  chi_2hat (cat) = {fname(chi2[ccat])}  "
      f"(banked B642 k=7-stage twist value: +phi)")

verdict1 = ("rho_hear IS the Gamma_5'-doublet 2-hat' (exact, all 9 classes)"
            if m2p and not m2 else
            "rho_hear IS the Gamma_5'-doublet 2-hat (exact, all 9 classes)"
            if m2 and not m2p else "MISMATCH — see table above")
print(f"  TASK-1 VERDICT: {verdict1}")

# ---------------------------------------------------------------------------
# S6. All nine irreducible characters (built from 2-hat by exact tensor
#     calculus), for the weight decompositions.
# ---------------------------------------------------------------------------
print("\n== S6: the full character table, built exactly ==")
# power-map on classes: need chi(g^j); use exact matrices per representative.
reps = {inv: rep for inv, _, rep, _ in cls_info}
sizes = {inv: sz for inv, sz, _, _ in cls_info}
inv_list = [inv for inv, _, _, _ in cls_info]


def chi_of_matrixrep(which):
    """Character (dict by class) of elems component 0 (2hat) or 1 (2hat')."""
    return {inv: mtrace(elems[reps[inv]][which]) for inv in inv_list}


def chi_pow(chi_elem_fn, j):
    """chi(g^j) per class, using concrete group powers."""
    out = {}
    for inv in inv_list:
        g = reps[inv]
        P = I5
        for _ in range(j):
            P = m5mul(P, g)
        out[inv] = chi_elem_fn(P)
    return out


def chi2_elem(g):
    return mtrace(elems[g][0])


chi_1 = {inv: ONE for inv in inv_list}
chi2_sq = chi_pow(chi2_elem, 2)   # chi_2hat(g^2)
chi2_cu = chi_pow(chi2_elem, 3)
chi2_q4 = chi_pow(chi2_elem, 4)
chi2_q5 = chi_pow(chi2_elem, 5)

half = Fr(1, 2)
chi_sym2 = {i: fscale(fadd(fmul(chi2[i], chi2[i]), chi2_sq[i]), half)
            for i in inv_list}
# Sym^3 = (p1^3 + 3 p1 p2 + 2 p3)/6
chi_sym3 = {i: fscale(fadd(fadd(fpow3 := fmul(fmul(chi2[i], chi2[i]),
                                              chi2[i]),
                                fscale(fmul(chi2[i], chi2_sq[i]), Fr(3))),
                           fscale(chi2_cu[i], Fr(2))), Fr(1, 6))
            for i in inv_list}
# For 2x2 with det 1 the clean route is the Chebyshev recursion:
#   h_n = chi * h_{n-1} - h_{n-2},  h_0 = 1, h_1 = chi.
h = {i: [ONE, chi2[i]] for i in inv_list}
for n in range(2, 76):
    for i in inv_list:
        h[i].append(fsub(fmul(chi2[i], h[i][n - 1]), h[i][n - 2]))
# consistency: Newton-route Sym^2/Sym^3 equal the recursion values
ok_newton = all(h[i][2] == chi_sym2[i] and h[i][3] == chi_sym3[i]
                for i in inv_list)
print(f"  Newton vs Chebyshev consistency (Sym^2, Sym^3): {ok_newton}")


def inner(ca, cb):
    s = ZERO
    for i in inv_list:
        s = fadd(s, fscale(fmul(ca[i], fconj(cb[i])), Fr(sizes[i])))
    # returns 120 * <ca, cb>
    return s


def is_irr(c):
    return inner(c, c) == fscale(ONE, Fr(120))


chi_3a = {i: h[i][2] for i in inv_list}          # Sym^2(2hat), 3-dim
chi_4p = {i: h[i][3] for i in inv_list}          # Sym^3(2hat), 4-dim
chi_5 = {i: h[i][4] for i in inv_list}           # Sym^4(2hat), 5-dim
chi_6 = {i: h[i][5] for i in inv_list}           # Sym^5(2hat), 6-dim
chi_4 = {i: fmul(chi2[i], chi2p[i]) for i in inv_list}   # 2 x 2' = 4
chi_3b = {i: galois(chi_3a[i], 3) for i in inv_list}     # Galois conj of 3a

# label 3 vs 3' by the value on 12C5 (T): Table 10 has chi_3(T) = phi.
cT = class5(T5)
if fname(chi_3a[cT]) == "phi":
    chi_3, chi_3p = chi_3a, chi_3b
else:
    chi_3, chi_3p = chi_3b, chi_3a

irreps = [("1", chi_1, 1), ("2-hat", chi2, 2), ("2-hat'", chi2p, 2),
          ("3", chi_3, 3), ("3'", chi_3p, 3), ("4", chi_4, 4),
          ("4'", chi_4p, 4), ("5", chi_5, 5), ("6-hat", chi_6, 6)]
for nm, c, d in irreps:
    print(f"  {nm:>6}: dim {d}, irreducible: {is_irr(c)}")
orth = all(inner(a[1], b[1]) == (fscale(ONE, Fr(120)) if a[0] == b[0]
                                 else ZERO)
           for a in irreps for b in irreps)
print(f"  full orthonormality of the 9 characters: {orth}")
print(f"  sum of dim^2 = {sum(d * d for _, _, d in irreps)} (must be 120)")

# ---------------------------------------------------------------------------
# S7. The weight mechanism, part 1: M_k(Gamma(5)) = Sym^{5k}(2-hat).
# ---------------------------------------------------------------------------
print("\n== S7: the scalar-lift identity and the weight decompositions ==")
# Eq. (13) action on (F1,F2):  S-matrix e^{i pi/10} (1/sqrt(sqrt5 phi)) *
# [[phi,1],[1,-phi]],  T-matrix diag(1, w5).  Claim (exact): these equal
# zeta_20^16 * rho_2hat(S) and zeta_20^12 * rho_2hat(T); the scalars are
# 20th roots that satisfy (zeta^16)^{5k} = (zeta^12)^{5k} = 1, so
# Sym^{5k}(F-action) = Sym^{5k}(rho_2hat) as honest Gamma_5' reps.
MS_F = mscale(((PHI, ONE), (ONE, fneg(PHI))), fmul(zeta(1), INV_C10))
MT_F = ((ONE, ZERO), (ZERO, W5))
okS = MS_F == mscale(R2_S, zeta(16))
okT = MT_F == mscale(R2_T, zeta(12))
print(f"  Eq.(13) S-matrix == zeta_20^16 * rho_2hat(S): {okS}")
print(f"  Eq.(13) T-matrix == zeta_20^12 * rho_2hat(T): {okT}")
print(f"  scalars die on Sym(5k): zeta^(16*5k)=zeta^(12*5k)=1 for all k: "
      f"{fpow(zeta(16), 5) == ONE and fpow(zeta(12), 5) == ONE}")

table1 = {1: {"6-hat": 1},
          2: {"3": 1, "3'": 1, "5": 1},
          3: {"4'": 1, "6-hat": 2},
          4: {"1": 1, "3": 1, "3'": 1, "4": 1, "5": 2},
          5: {"2-hat": 1, "2-hat'": 1, "4'": 1, "6-hat": 3},
          6: {"1": 1, "3": 2, "3'": 2, "4": 2, "5": 2}}
print("  decomposition of Sym^{5k}(2-hat) (= weight-k level-5 forms):")
all_match = True
for k in range(1, 7):
    n = 5 * k
    dec = {}
    for nm, c, d in irreps:
        m = inner({i: h[i][n] for i in inv_list}, c)
        assert all(x == 0 for x in m[1:]), f"non-rational inner at k={k},{nm}"
        mm = m[0] / 120
        assert mm.denominator == 1, f"non-integer multiplicity at k={k},{nm}"
        if mm:
            dec[nm] = int(mm)
    tot = sum(dec[nm] * d for nm, _, d in irreps if nm in dec)
    match = dec == table1[k]
    all_match &= match
    dstr = " + ".join(f"{v}x{nm}" if v > 1 else nm
                      for nm, v in sorted(dec.items()))
    print(f"    k={k} (dim {tot} = 5k+1={5 * k + 1}): {dstr}   "
          f"[matches their Table 1: {match}]")
print(f"  ALL SIX weights match Yao-Liu-Ding Table 1: {all_match}")

# ---------------------------------------------------------------------------
# S8. The weight mechanism, part 2: where the doublets live in Sym^n.
# ---------------------------------------------------------------------------
print("\n== S8: doublet occurrences in Sym^n(2-hat), n = 0..75 ==")
occ2, occ2p = [], []
mults2, mults2p = [], []
for n in range(76):
    hn = {i: h[i][n] for i in inv_list}
    i2, i2p = inner(hn, chi2), inner(hn, chi2p)
    assert all(x == 0 for x in i2[1:]) and all(x == 0 for x in i2p[1:])
    m2n, m2pn = i2[0] / 120, i2p[0] / 120
    assert m2n.denominator == 1 and m2pn.denominator == 1
    mults2.append(int(m2n))
    mults2p.append(int(m2pn))
    if m2n:
        occ2.append(n)
    if m2pn:
        occ2p.append(n)
print(f"  n with 2-hat  in Sym^n: {occ2}")
print(f"  n with 2-hat' in Sym^n: {occ2p}")

# closed-form check: Kostant/McKay generating function with the binary-
# icosahedral invariant degrees 12, 20 (the E8 degrees minus top):
#   sum_n mult_r(Sym^n) t^n = N_r(t) / ((1-t^12)(1-t^20)).
# Recover N_r(t) exactly by multiplying the computed series back:


def numerator(mults, upto):
    num = [0] * (upto + 1)
    # num = mults * (1 - t^12)(1 - t^20) = mults*(1 - t^12 - t^20 + t^32)
    for n in range(upto + 1):
        v = mults[n]
        if n >= 12:
            v -= mults[n - 12]
        if n >= 20:
            v -= mults[n - 20]
        if n >= 32:
            v += mults[n - 32]
        num[n] = v
    return num


num2 = numerator(mults2, 75)
num2p = numerator(mults2p, 75)
n2 = [n for n, v in enumerate(num2) if v]
n2p = [n for n, v in enumerate(num2p) if v]
print(f"  numerator of the 2-hat  series over (1-t^12)(1-t^20): "
      f"terms at {n2} with coeffs {[num2[n] for n in n2]}")
print(f"  numerator of the 2-hat' series over (1-t^12)(1-t^20): "
      f"terms at {n2p} with coeffs {[num2p[n] for n in n2p]}")
tail2 = all(v == 0 for v in num2[30:])
tail2p = all(v == 0 for v in num2p[30:])
print(f"  numerators are POLYNOMIALS (all higher terms vanish to n=75): "
      f"{tail2} / {tail2p}")

first5 = min(n for n in occ2 if n % 5 == 0)
first5p = min(n for n in occ2p if n % 5 == 0)
print(f"  first n = 0 mod 5 with 2-hat  in Sym^n: {first5} -> weight "
      f"{first5 // 5}")
print(f"  first n = 0 mod 5 with 2-hat' in Sym^n: {first5p} -> weight "
      f"{first5p // 5}")

# the congruence mechanism, stated from the computed numerators:
print("  mechanism: occurrences of 2-hat are n in {a + 12r + 20s} for the")
print(f"  numerator exponents a = {n2}; n = 0 mod 5 forces (with a=1):")
print("  1 + 12r + 20s = 0 mod 5  <=>  1 + 2r = 0 mod 5  <=>  r = 2 mod 5,")
print("  minimal n = 1 + 2*12 = 25 = 5*5  =>  the doublets first appear at")
print("  WEIGHT 5. The '5' of the weight = level 5 (degree-5k homogeneity in")
print("  the two weight-1/5 Ibukiyama generators) meshed with the McKay-E8")
print("  invariant degrees 12, 20 of the binary icosahedral group.")

v2 = "PASS" if (all_match and first5 == 25 and first5p == 25) else "FAIL"
print(f"\n  TASK-2 VERDICT: {v2} — weight-5 first appearance is FORCED "
      f"(Sym^(5k) structure + 2I invariant degrees 12, 20).")

print("\n== FINAL ==")
print(f"TASK 1: {verdict1}")
print("TASK 1 addendum: the Galois pair chi/chi-bar of the ear (B642 stage "
      "twist) = their (2-hat', 2-hat) pair: "
      f"{gal_pair and m2p and fname(chi2[ccat]) == 'phi'}")
print(f"TASK 2: doublets first at weight {first5 // 5} (both), mechanism "
      "verified exactly against the literature decompositions k = 1..6: "
      f"{all_match}")
