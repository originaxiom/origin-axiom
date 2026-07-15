"""High-precision (50-digit) rebuild of the E6_2 3x3 odd hearing matrix B,
mirroring frontier/B594_e6_hearing/e6_hearing.py (twisted weld B = U^T Cm rho(A1) U)
and frontier/B570_allowed_plays/c3_e6_level2_monodromy.py exactly, but with
EXACT integer arithmetic for W(E6)/root data and mpmath high-precision
transcendentals (roots of unity) for S, T.

Strategy: all rational data (Cartan inverse, shifted weights, W(E6) matrices)
are exact integers/rationals since det(Cartan_E6)=3. The only transcendental
inputs are 126th roots of unity (denominator of ips/KH always divides 9*14=126)
for S, and 252nd roots of unity for T (9 diagonal entries only, computed
directly). This lets us do the O(51840 x 45) summation as EXACT INTEGER
bincounts against a 126-length precomputed high-precision root-of-unity table.
"""
import mpmath as mp
from fractions import Fraction as F
import numpy as np
import sympy as sp
import sys, time

DPS = 100
mp.mp.dps = DPS

t0 = time.time()

# ---------------- exact integer/rational setup ----------------
C6 = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
      [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
KH = 14
C_int = np.array(C6, dtype=np.int64)

Cs = sp.Matrix(C6)
assert Cs.det() == 3
Cinv3_sp = 3 * Cs.inv()          # exact integer matrix (3 * Cartan^{-1})
Cinv3 = np.array([[int(x) for x in row] for row in Cinv3_sp.tolist()], dtype=np.int64)

PRIM = [(0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1),
        (2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 2), (1, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 1, 0)]
NAMES = ['1', '27', '27b', '351p', '351pb', '650', '78', '351', '351b']
theta = lambda w: (w[5], w[1], w[4], w[3], w[2], w[0])

ones6 = np.ones(6, dtype=np.int64)
shifted3 = [Cinv3 @ (np.array(p, dtype=np.int64) + ones6) for p in PRIM]   # = 3*(lambda+rho), exact int
lam3 = [Cinv3 @ np.array(p, dtype=np.int64) for p in PRIM]                 # = 3*lambda, exact int

# ---------------- exact W(E6), 51840 elements ----------------
def weyl_group():
    n = 6
    gens = []
    for j in range(n):
        M = np.eye(n, dtype=np.int64)
        M[j, :] -= C_int[:, j]
        gens.append(M)
    I = np.eye(n, dtype=np.int64)
    seen = {I.tobytes(): 1}
    frontier = [(I, 1)]
    mats, signs = [I], [1]
    while frontier:
        new = []
        for M, s in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen[key] = -s
                    new.append((Mg, -s))
                    mats.append(Mg)
                    signs.append(-s)
        frontier = new
    return np.array(mats), np.array(signs)

W, eps_signs = weyl_group()
assert len(W) == 51840
print(f"[{time.time()-t0:.1f}s] W(E6) built exactly, {len(W)} elements, max|entry|={np.max(np.abs(W))}")

# ---------------- exact ips (x9) for all (w,a,b), via 126th roots table ----------------
# ips(w,a,b) = (W[w] @ shifted[a]) . (C @ shifted[b])      [shifted = shifted3/3]
#            = [(W[w] @ shifted3[a]) . (C @ shifted3[b])] / 9        -- exact integer / 9
# exponent  exp(-2 pi i ips/KH) = exp(-2 pi i * ips9 / (9*KH)) = exp(-2 pi i * ips9 / 126)
Cb3 = [C_int @ s for s in shifted3]     # C @ shifted3[b], 9 integer vectors
Wl3 = np.einsum('wij,lj->wli', W, np.array(shifted3))   # W[w] @ shifted3[a], exact int64

MOD = 126
root_table = [mp.e**(-2j * mp.pi() * k / MOD) for k in range(MOD)]
root_table = mp.matrix(root_table)   # mpmath doesn't need this, keep as list
root_table = [mp.e**(mp.mpc(0, -1) * 2 * mp.pi() * k / MOD) for k in range(MOD)]

S = [[None]*9 for _ in range(9)]
for a in range(9):
    for b in range(a, 9):
        ips9 = Wl3[:, a, :] @ Cb3[b]           # exact int64 vector, len 51840
        assert ips9.dtype == np.int64
        pos = np.mod(ips9, MOD)                # 0..125
        coeffs = np.bincount(pos, weights=eps_signs, minlength=MOD)  # sums of +-1 per residue
        val = mp.mpc(0, 0)
        for r in range(MOD):
            c = coeffs[r]
            if c != 0:
                val += int(round(c)) * root_table[r]
        S[a][b] = val
        S[b][a] = val
print(f"[{time.time()-t0:.1f}s] S (unnormalized) built via exact 126-root bincount")

Sm = mp.matrix(S)
# normalize: S /= sqrt((S S^dagger)[0,0].real)
SSd00 = sum(Sm[0, k] * mp.conj(Sm[0, k]) for k in range(9))
norm = mp.sqrt(SSd00.real)
Sm = Sm / norm
if Sm[0, 0].real < 0:
    Sm = -Sm

# gate checks
uni = mp.norm(Sm * Sm.transpose_conj() - mp.eye(9))
sym = mp.norm(Sm - Sm.transpose())
print(f"[{time.time()-t0:.1f}s] GATE S: unitary dev={mp.nstr(uni, 6)}, symmetric dev={mp.nstr(sym, 6)}, S00={mp.nstr(Sm[0,0].real, 12)}")

# ---------------- T (exact fractions -> high-precision exp) ----------------
# ip(x,y) = x . (C @ y); hs[p] = ip(lam, lam+2*rho)/(2*KH); lam=root_coords(p); rho=root_coords(ones)
# lam3 = 3*lam ; (lam+2*rho)*3 = shifted3[p] + rho_w3   where rho_w3 = Cinv3@ones
rho_w3 = Cinv3 @ ones6
hs = []
for i, p in enumerate(PRIM):
    y3 = shifted3[i] + rho_w3          # = 3*(lambda + 2 rho)... check below
    # lambda + 2 rho = (lambda+rho) + rho = shifted[p] + rho  -> times 3: shifted3[p] + rho_w3
    num = int(lam3[i] @ (C_int @ y3))   # = 9 * ip(lam, lam+2rho)
    den = 9 * 2 * KH
    hs.append(F(num, den))

cc = F(2 * 78, KH)          # c = 2*78/14
c24 = cc / 24

Tdiag = []
for h in hs:
    expo = h - c24                      # exact Fraction
    ang = mp.mpf(expo.numerator) / mp.mpf(expo.denominator)
    Tdiag.append(mp.e**(mp.mpc(0, 1) * 2 * mp.pi() * ang))
Tm = mp.diag(Tdiag)
print(f"[{time.time()-t0:.1f}s] T built (exact fractions -> {DPS}-dps exp)")

# ---------------- rho(A1), Cm, weld ----------------
rho_mat = Tm * Tm * Sm * Tm
Cm = mp.matrix(9, 9)
S2 = Sm * Sm
for i in range(9):
    for j in range(9):
        Cm[i, j] = S2[i, j].real

# gate: S^2 should equal the theta-permutation matrix (real, 0/1)
conj_idx = [PRIM.index(theta(p)) for p in PRIM]
expect = mp.zeros(9, 9)
for i in range(9):
    expect[conj_idx[i], i] = 1
devperm = mp.norm(Cm - expect)
maximag = max(abs(S2[i, j].imag) for i in range(9) for j in range(9))
print(f"[{time.time()-t0:.1f}s] GATE S^2 = conjugation permutation: dev={mp.nstr(devperm, 6)}, max|Im(S^2)|={mp.nstr(maximag, 6)}")

comm = mp.norm(Cm * rho_mat - rho_mat * Cm)
print(f"[{time.time()-t0:.1f}s] GATE [Cm, rho] = 0: dev={mp.nstr(comm, 6)}")

# ---------------- odd 3-space U, weld, B ----------------
pairs = [(1, 2, "27"), (3, 4, "351'"), (7, 8, "351")]
U = mp.zeros(9, 3)
inv_sqrt2 = 1 / mp.sqrt(2)
for j, (a, b, _) in enumerate(pairs):
    U[a, j] = inv_sqrt2
    U[b, j] = -inv_sqrt2

Wt = Cm * rho_mat   # twisted weld
B = U.transpose() * Wt * U

print(f"\n[{time.time()-t0:.1f}s] ===== THE 3x3 ODD HEARING MATRIX B (twisted weld, {DPS} dps) =====")
for i in range(3):
    row = "  ".join(mp.nstr(B[i, j], 55, strip_zeros=False) for j in range(3))
    print(f"row {i}: {row}")

trB = B[0, 0] + B[1, 1] + B[2, 2]
print(f"\ntrace(B) = {mp.nstr(trB, 55)}   |trace+1| = {mp.nstr(abs(trB + 1), 6)}")

# order-4 consistency of U^T rho U
Prho = U.transpose() * rho_mat * U
P4 = Prho * Prho * Prho * Prho
dev4 = mp.norm(P4 - mp.eye(3))
print(f"order-4 dev of U^T rho U: {mp.nstr(dev4, 6)}")

# banked sine-kernel amplitudes at 100 dps
BANKED = {
    "27": (2 / mp.sqrt(7)) * mp.sin(2 * mp.pi() / 7) * mp.e**(mp.mpc(0, 1) * 2 * mp.pi() * 3 / 14),
    "351'": (2 / mp.sqrt(7)) * mp.sin(6 * mp.pi() / 7) * mp.e**(mp.mpc(0, 1) * 2 * mp.pi() * (-2) / 14),
    "351": (2 / mp.sqrt(7)) * mp.sin(4 * mp.pi() / 7) * mp.e**(mp.mpc(0, 1) * 2 * mp.pi() * (-1) / 14),
}
print("\nH2 check: diagonal entries vs -(BANKED sine-kernel amplitudes):")
for j, (a, b, nm) in enumerate(pairs):
    diff = abs(B[j, j] - (-BANKED[nm]))
    print(f"  {nm:>5}: B[{j},{j}] = {mp.nstr(B[j,j], 40)}   -BANKED = {mp.nstr(-BANKED[nm], 40)}   |diff| = {mp.nstr(diff, 6)}")

import pickle
with open('B_matrix.pkl', 'wb') as f:
    Bser = [[ (mp.nstr(B[i,j].real, DPS+10), mp.nstr(B[i,j].imag, DPS+10)) for j in range(3)] for i in range(3)]
    pickle.dump({'B': Bser, 'dps': DPS}, f)

# ================= (1) |B_ij|^2 =================
print("\n" + "="*70)
print("(1) |B_ij|^2  (3x3, exact-precision moduli-squared)")
print("="*70)
absB2 = mp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        absB2[i, j] = (B[i, j] * mp.conj(B[i, j])).real
    print(f"row {i}: " + "  ".join(mp.nstr(absB2[i, j], 50) for j in range(3)))

print("\nrow sums:   " + "  ".join(mp.nstr(sum(absB2[i, j] for j in range(3)), 50) for i in range(3)))
print("col sums:   " + "  ".join(mp.nstr(sum(absB2[i, j] for i in range(3)), 50) for j in range(3)))

# ================= (3) unitarity of B =================
print("\n" + "="*70)
print("(3) unitarity check: B B^dagger  (should be I if B unitary)")
print("="*70)
BBd = B * B.transpose_conj()
for i in range(3):
    print(f"row {i}: " + "  ".join(mp.nstr(BBd[i, j], 30) for j in range(3)))
dev_unitary = mp.norm(BBd - mp.eye(3))
print(f"||B B^dagger - I|| = {mp.nstr(dev_unitary, 8)}  -> B unitary: {dev_unitary < mp.mpf('1e-90')}")
BdB = B.transpose_conj() * B
dev_unitary2 = mp.norm(BdB - mp.eye(3))
print(f"||B^dagger B - I|| = {mp.nstr(dev_unitary2, 8)}")

# ================= (2a) eigen-decomposition B = V D V^-1 =================
print("\n" + "="*70)
print("(2a) eigen-decomposition (numpy.linalg.eig analogue): B V = V D")
print("="*70)
Evals, Evecs = mp.eig(B)
# normalize eigenvectors to unit 2-norm (numpy convention)
Vn = mp.zeros(3, 3)
for j in range(3):
    col = Evecs[:, j]
    nrm = mp.sqrt(sum((col[i] * mp.conj(col[i])).real for i in range(3)))
    for i in range(3):
        Vn[i, j] = col[i] / nrm

print("eigenvalues:")
for k in range(3):
    print(f"  lambda_{k} = {mp.nstr(Evals[k], 50)}   |lambda| = {mp.nstr(abs(Evals[k]), 30)}")

print("\neigenvector matrix V (columns = normalized eigenvectors):")
for i in range(3):
    print(f"row {i}: " + "  ".join(mp.nstr(Vn[i, j], 50) for j in range(3)))

print("\n|V_ij|^2:")
absV2 = mp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        absV2[i, j] = (Vn[i, j] * mp.conj(Vn[i, j])).real
    print(f"row {i}: " + "  ".join(mp.nstr(absV2[i, j], 50) for j in range(3)))

# verify eigen-decomposition
Dm = mp.diag([Evals[k] for k in range(3)])
resid = mp.norm(B * Vn - Vn * Dm)
print(f"\n||B V - V D|| = {mp.nstr(resid, 8)}")
detV = Vn[0,0]*(Vn[1,1]*Vn[2,2]-Vn[1,2]*Vn[2,1]) - Vn[0,1]*(Vn[1,0]*Vn[2,2]-Vn[1,2]*Vn[2,0]) + Vn[0,2]*(Vn[1,0]*Vn[2,1]-Vn[1,1]*Vn[2,0])
print(f"det(V) = {mp.nstr(detV, 30)}  (V unitary check ||V V^dagger - I||): ", end="")
devVunitary = mp.norm(Vn * Vn.transpose_conj() - mp.eye(3))
print(mp.nstr(devVunitary, 8))

# ================= (2b) SVD frame =================
print("\n" + "="*70)
print("(2b) SVD frame: B = Usvd Sigma Vsvd^dagger")
print("="*70)
BdB_h = B.transpose_conj() * B    # Hermitian PSD
Esv, VsvR = mp.eighe(BdB_h)       # ascending eigenvalues, unitary eigenvector matrix
# sort descending by eigenvalue (=singular value^2)
order = sorted(range(3), key=lambda k: -Esv[k])
sigma2 = [Esv[k] for k in order]
Vsv = mp.zeros(3, 3)
for newj, oldj in enumerate(order):
    for i in range(3):
        Vsv[i, newj] = VsvR[i, oldj]
sigma = [mp.sqrt(max(s, 0)) for s in sigma2]
print("singular values:")
for k in range(3):
    print(f"  sigma_{k} = {mp.nstr(sigma[k], 50)}")

Usv = mp.zeros(3, 3)
for j in range(3):
    col = B * Vsv[:, j]
    if sigma[j] > mp.mpf('1e-80'):
        for i in range(3):
            Usv[i, j] = col[i] / sigma[j]
    else:
        for i in range(3):
            Usv[i, j] = col[i]

print("\nUsvd (left singular vectors, columns):")
for i in range(3):
    print(f"row {i}: " + "  ".join(mp.nstr(Usv[i, j], 50) for j in range(3)))
print("\nVsvd (right singular vectors, columns):")
for i in range(3):
    print(f"row {i}: " + "  ".join(mp.nstr(Vsv[i, j], 50) for j in range(3)))

Sigma_m = mp.diag(sigma)
recon = Usv * Sigma_m * Vsv.transpose_conj()
print(f"\n||B - Usvd Sigma Vsvd^dagger|| = {mp.nstr(mp.norm(recon - B), 8)}")
devUunitary = mp.norm(Usv * Usv.transpose_conj() - mp.eye(3))
devVsvunitary = mp.norm(Vsv * Vsv.transpose_conj() - mp.eye(3))
print(f"Usvd unitary dev: {mp.nstr(devUunitary,8)}   Vsvd unitary dev: {mp.nstr(devVsvunitary,8)}")

# ================= (4) exact-form identification =================
print("\n" + "="*70)
print("(4) exact-form scan: cross-check against sqrt5, sqrt7, sqrt21, cos/sin(pi k/7), cos/sin(pi k/5)")
print("="*70)
import math
mp7 = mp.sqrt(7)
mp5 = mp.sqrt(5)
mp21 = mp.sqrt(21)
print("sqrt7 =", mp.nstr(mp7, 50))
print("sqrt5 =", mp.nstr(mp5, 50))
print("sqrt21 =", mp.nstr(mp21, 50))
print("\n(2/sqrt7) sin(2pi/7) =", mp.nstr((2/mp7)*mp.sin(2*mp.pi()/7), 50))
print("(2/sqrt7) sin(4pi/7) =", mp.nstr((2/mp7)*mp.sin(4*mp.pi()/7), 50))
print("(2/sqrt7) sin(6pi/7) =", mp.nstr((2/mp7)*mp.sin(6*mp.pi()/7), 50))

with open('all_matrices.pkl', 'wb') as f:
    def ser(M, rows=3, cols=3):
        return [[mp.nstr(M[i,j], DPS+10) for j in range(cols)] for i in range(rows)]
    pickle.dump({
        'B': ser(B), 'absB2': ser(absB2), 'BBd': ser(BBd),
        'Evals': [mp.nstr(Evals[k], DPS+10) for k in range(3)],
        'V': ser(Vn), 'absV2': ser(absV2),
        'Usv': ser(Usv), 'Vsv': ser(Vsv), 'sigma': [mp.nstr(s, DPS+10) for s in sigma],
        'dps': DPS
    }, f)

print(f"\n[{time.time()-t0:.1f}s] DONE")

# ================= exact-form identification of ALL 9 entries =================
print("\n" + "="*70)
print("(4b) exact-form scan: B_ij = -A_k * zeta14^m  pattern search")
print("="*70)
A = {1: (2/mp7)*mp.sin(2*mp.pi()/7), 2: (2/mp7)*mp.sin(4*mp.pi()/7), 3: (2/mp7)*mp.sin(6*mp.pi()/7)}
zeta14 = mp.e**(mp.mpc(0,1)*mp.pi()/7)
for i in range(3):
    for j in range(3):
        val = B[i, j]
        found = None
        for k in (1, 2, 3):
            for sgn in (1, -1):
                ratio = val / (sgn * A[k])
                # ratio should be unit modulus if match
                if abs(abs(ratio) - 1) < mp.mpf('1e-80'):
                    ang = mp.arg(ratio)
                    m14 = ang / (mp.pi()/7)
                    m14r = mp.nint(m14)
                    if abs(m14 - m14r) < mp.mpf('1e-70'):
                        found = (sgn, k, int(m14r))
                        break
            if found:
                break
        if found:
            sgn, k, m = found
            sgnstr = '-' if sgn == -1 else '+'
            print(f"  B[{i},{j}] = {sgnstr} A_{k} * zeta14^{m}   (A_{k}=(2/sqrt7)sin({2*k}pi/7), zeta14=exp(i pi/7))   [check: {mp.nstr(abs(val - sgn*A[k]*zeta14**m),6)}]")
        else:
            print(f"  B[{i},{j}] = {mp.nstr(val,30)}  -- no single A_k*zeta14^m match found")

print("\n" + "="*70)
print("B^4 check (should be exactly I, given eigenvalues {i,-i,-1}):")
print("="*70)
B2 = B*B; B4 = B2*B2
print("||B^4 - I|| =", mp.nstr(mp.norm(B4 - mp.eye(3)), 8))
print("B^2 =")
for i in range(3):
    print(" ", "  ".join(mp.nstr(B2[i,j], 30) for j in range(3)))
