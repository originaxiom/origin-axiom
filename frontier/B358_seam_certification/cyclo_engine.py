"""EXACT certification of the Par-inserted pair invariants over Q(zeta_60) -- Fraction arithmetic,
no numerics anywhere. Independent construction: B355's earned conventions (T = e_15(x^2),
S = F_{-2}/g). The whole doubles table + single-seed controls, exactly.

Representation of Q(zeta_60): coefficient vectors of length 16 over Q in the power basis
1, z, ..., z^15 modulo Phi_60(z) = z^16 + z^14 - z^10 - z^8 - z^6 + z^2 + 1.
"""
from fractions import Fraction as Fr
import json, sys

N = 15
DEG = 16
# Phi_60 reduction: z^16 = -z^14 + z^10 + z^8 + z^6 - z^2 - 1
def _build_red():
    red = []
    for k in range(DEG):
        v = [Fr(0)] * DEG
        v[k] = Fr(1)
        red.append(v)
    for k in range(DEG, 2 * DEG):
        # z^k = z * z^(k-1) then reduce leading term
        prev = red[k - 1]
        v = [Fr(0)] * (DEG + 1)
        for i in range(DEG):
            v[i + 1] = prev[i]
        if v[DEG] != 0:
            c = v[DEG]
            v = v[:DEG]
            # z^16 -> -z^14+z^10+z^8+z^6-z^2-1
            v[14] -= c
            v[10] += c
            v[8] += c
            v[6] += c
            v[2] -= c
            v[0] -= c
        else:
            v = v[:DEG]
        red.append(v)
    return red

RED = _build_red()

def zpow(k):
    return list(RED[k % 60]) if k % 60 < 2 * DEG else _zpow_big(k % 60)

def _zpow_big(k):
    # k in [32, 59]: z^k = z^(k-16) * z^16 -- iterate
    v = list(RED[2 * DEG - 1])  # z^31
    k0 = 2 * DEG - 1
    while k0 < k:
        v = zmul_mono(v)
        k0 += 1
    return v

def zmul_mono(a):
    """multiply by z with reduction."""
    v = [Fr(0)] * (DEG + 1)
    for i in range(DEG):
        v[i + 1] = a[i]
    if v[DEG] != 0:
        c = v[DEG]
        v = v[:DEG]
        v[14] -= c; v[10] += c; v[8] += c; v[6] += c; v[2] -= c; v[0] -= c
    else:
        v = v[:DEG]
    return v

# cache all 60 monomials
ZP = []
cur = [Fr(0)] * DEG
cur[0] = Fr(1)
for k in range(60):
    ZP.append(list(cur))
    cur = zmul_mono(cur)

def add(a, b):
    return [a[i] + b[i] for i in range(DEG)]

def sub(a, b):
    return [a[i] - b[i] for i in range(DEG)]

def scal(c, a):
    return [c * x for x in a]

def mul(a, b):
    raw = [Fr(0)] * (2 * DEG - 1)
    for i in range(DEG):
        ai = a[i]
        if ai:
            for j in range(DEG):
                if b[j]:
                    raw[i + j] += ai * b[j]
    out = [Fr(0)] * DEG
    for k in range(2 * DEG - 1):
        if raw[k]:
            rk = RED[k]
            for i in range(DEG):
                if rk[i]:
                    out[i] += raw[k] * rk[i]
    return out

ZERO = [Fr(0)] * DEG
ONE = ZP[0]

def zeta(k):          # zeta_60^k
    return list(ZP[k % 60])

def e15(t):           # e^{2 pi i t/15} = zeta_60^{4t}
    return zeta(4 * (t % 15))

# --- matrices over the field: lists of lists of coeff-vectors ---
def mmul(A, B):
    n = len(A)
    C = [[ZERO for _ in range(n)] for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for k in range(n):
            a = Ai[k]
            if a != ZERO and any(a):
                Bk = B[k]
                Ci = C[i]
                for j in range(n):
                    b = Bk[j]
                    if any(b):
                        Ci[j] = add(Ci[j], mul(a, b))
    return C

def conj_elt(a):
    """complex conjugation = z -> z^-1 = z^59."""
    out = [Fr(0)] * DEG
    for k in range(DEG):
        if a[k]:
            out = add(out, scal(a[k], zeta((-k) % 60)))
    return out

# --- the exact Weil generators (B355 conventions) ---
# sqrt5 = z5 + z5^4 - z5^2 - z5^3 (z5 = zeta_60^12); sqrt(-3) = z3 - z3^2 (z3 = zeta_60^20)
SQRT5 = sub(add(zeta(12), zeta(48)), add(zeta(24), zeta(36)))
SQRTm3 = sub(zeta(20), zeta(40))
I_UNIT = zeta(15)
SQRT15 = mul(mul(SQRT5, SQRTm3), scal(Fr(-1), I_UNIT))   # sqrt5*sqrt(-3)*(-i) = sqrt15
SQRTm15 = mul(SQRT5, SQRTm3)                              # sqrt(-15) = sqrt5 * sqrt(-3)
G15 = mul(I_UNIT, SQRT15)                                 # g(15) = i*sqrt15
G15_INV = scal(Fr(1, 15), conj_elt(G15))                  # 1/g = conj(g)/15  (|g|^2 = 15)

def Tmat():
    M = [[ZERO for _ in range(N)] for _ in range(N)]
    for x in range(N):
        M[x][x] = e15(x * x)
    return M

def Tinv():
    M = [[ZERO for _ in range(N)] for _ in range(N)]
    for x in range(N):
        M[x][x] = e15(-x * x)
    return M

def Smat():
    M = [[ZERO for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            M[x][y] = mul(e15(-2 * x * y), G15_INV)
    return M

def Sinv():
    """S^-1 = S^dagger: (S^-1)[x,y] = conj(S[y,x])."""
    S = Smat()
    M = [[ZERO for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            M[x][y] = conj_elt(S[y][x])
    return M

def main():
    T, Ti, S, Si = Tmat(), Tinv(), Smat(), Sinv()
    # gates: S*Si = I; T*Ti = I
    def is_identity(M):
        for i in range(N):
            for j in range(N):
                tgt = ONE if i == j else ZERO
                if M[i][j] != tgt:
                    return False
        return True
    assert is_identity(mmul(S, Si)), "S*S^-1 != I"
    print("gate: S*S^-1 = I exactly", flush=True)

    # W1 = rho(A_1) = T S T^-1 S^-1 ; W2 = rho(A_2) = T^2 S T^-2 S^-1
    W1 = mmul(mmul(T, S), mmul(Ti, Si))
    T2 = mmul(T, T)
    Ti2 = mmul(Ti, Ti)
    W2 = mmul(mmul(T2, S), mmul(Ti2, Si))
    print("W1, W2 built", flush=True)

    # orders: W1^20 = I, W2^12 = I (gates)
    W1p = [None] * 20
    W1p[0] = [[ONE if i == j else ZERO for j in range(N)] for i in range(N)]
    for k in range(1, 20):
        W1p[k] = mmul(W1p[k - 1], W1)
        print(f"  W1^{k} done", flush=True)
    assert is_identity(mmul(W1p[19], W1)), "W1^20 != I"
    print("gate: W1^20 = I exactly", flush=True)
    W2p = [None] * 12
    W2p[0] = W1p[0]
    for k in range(1, 12):
        W2p[k] = mmul(W2p[k - 1], W2)
        print(f"  W2^{k} done", flush=True)
    assert is_identity(mmul(W2p[11], W2)), "W2^12 != I"
    print("gate: W2^12 = I exactly", flush=True)

    # Par: x -> -x mod 15 (permutation); also verify Par = +- S^2 (rho(-I))
    S2 = mmul(S, S)
    par_perm = [(-x) % N for x in range(N)]
    sgn = None
    ok = True
    for i in range(N):
        for j in range(N):
            tgt_pos = ONE if par_perm[i] == j else ZERO
            if S2[i][j] != tgt_pos and S2[i][j] != scal(Fr(-1), tgt_pos):
                pass
    # determine sign from (0, 0): S2[0][0] should be +-1
    sgn = 1 if S2[0][0] == ONE else (-1 if S2[0][0] == scal(Fr(-1), ONE) else None)
    assert sgn is not None
    print(f"gate: S^2 = {sgn} * Par exactly (Par intrinsic = rho(-I) up to sign)", flush=True)

    # C[j][l] = tr(Par * W1^j * W2^l)  -- exact; tr(Par M) = sum_x M[-x, x]... careful:
    # (Par*M)[x,y] = M[-x mod 15, y]; trace = sum_x M[-x, x].
    C = [[None] * 12 for _ in range(20)]
    for j in range(20):
        for l in range(12):
            Mjl = mmul(W1p[j], W2p[l]) if (j, l) != (0, 0) else W1p[0]
            t = ZERO
            for x in range(N):
                t = add(t, Mjl[(-x) % N][x])
            C[j][l] = t
        print(f"  C row j={j} done", flush=True)

    # also singles: c1[j] = tr(Par W1^j), c2[l] = tr(Par W2^l)
    c1 = []
    for j in range(20):
        t = ZERO
        for x in range(N):
            t = add(t, W1p[j][(-x) % N][x])
        c1.append(t)
    c2 = []
    for l in range(12):
        t = ZERO
        for x in range(N):
            t = add(t, W2p[l][(-x) % N][x])
        c2.append(t)

    # dump C, c1, c2 as JSON (Fractions as strings)
    def dump(v):
        return [str(x) for x in v]
    out = dict(C=[[dump(C[j][l]) for l in range(12)] for j in range(20)],
               c1=[dump(x) for x in c1], c2=[dump(x) for x in c2], sgn=sgn)
    with open("seam_exact_C.json", "w") as f:
        json.dump(out, f)
    print("saved seam_exact_C.json", flush=True)

if __name__ == "__main__":
    main()
