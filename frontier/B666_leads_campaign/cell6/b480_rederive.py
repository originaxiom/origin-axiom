"""CELL 6 / ticket B480: re-derive the banked figure "level-ratio <r> = 0.16 at
N = 181, 301" for the quantized golden cat map A = [[2,1],[1,1]] (metallic m=1).

RECOVERY STATUS (established before this script): the source script NEVER existed
in-tree (commit fb3a75a added exactly FINDINGS.md + PREREGISTRATION.md +
qca_dispersion.py, none of which computes <r>; whole-history pickaxe for
kurlberg/level_ratio/cat_map .py finds nothing else). So: RE-DERIVE from the
described method ("Hecke / Kurlberg-Rudnick arithmetic symmetries").

METHOD (the correct discrete quantization, fixing cc2's failed attempt):
cc2's runs/b480_level_ratio.py used phase pi/(c*N)*(a k^2 - 2jk + d j^2) -- a
2N-th root of unity, NOT a function of (j,k) mod N; that breaks the group
structure (their homomorphism test failed, std ~0.6, verdict UNREPRODUCIBLE).
The correct Hannay-Berry / Weil propagator at odd N for A=[[a,b],[c,d]],
gcd(b,N)=1, is (up to a global phase, irrelevant for spacing statistics):

    U[j,k] = (1/sqrt(N)) * exp( (2*pi*i/N) * inv(2b) * (a k^2 - 2 j k + d j^2) )

with inv(2b) the MODULAR inverse of 2b mod N (exact integer arithmetic in the
exponent). Validation battery (all must pass before any statistic is read):
  V1 unitarity to machine precision;
  V2 projective homomorphism: U(A)U(A) = gamma*U(A^2), U(A)U(A^2)=gamma'*U(A^3),
     gamma a CONSTANT phase (elementwise-ratio std ~ 0);
  V3 U(A)^R = c*I for R = ord(A mod N) (eigenvalue slots exact);
  V4 the exact trace identity |tr U(A)^t|^2 = #Fix(A^t on (Z/N)^2) for all t
     (integer fixed-point counts via Smith normal form, EXACT).

STATISTIC: eigenphases of U; Oganesyan-Huse r_n = min(s_n,s_{n+1})/max(...).
Conventions reported (no script survives, so the convention is part of what we
must recover):
  C1 RAW-FLOAT: sorted raw eigenphases, circular closure (cc2's function,
     the likely original in-session convention);
  C2 EXACT-DEGENERATE: slot-clustered spectrum, within-slot gaps exactly 0,
     r for a (0,0) pair := 0 [and the skip-(0,0) variant], exact Fractions;
  C3 DISTINCT-SLOTS: occupied slots only, integer gaps, exact Fractions.
Poisson <r> ~ 0.386, GOE ~ 0.53; the banked claim is 0.16 at BOTH N.
"""
import numpy as np
from fractions import Fraction as Fr
from math import gcd

A = ((2, 1), (1, 1))  # golden cat map, m=1 metallic member


def matmul2(X, Y, mod=None):
    r = ((X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]),
         (X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]))
    if mod:
        r = tuple(tuple(v % mod for v in row) for row in r)
    return r


def matpow2(X, t, mod=None):
    R = ((1, 0), (0, 1))
    for _ in range(t):
        R = matmul2(R, X, mod)
    return R


def ord_mod(X, N):
    P = tuple(tuple(v % N for v in row) for row in X)
    Q = P
    for t in range(1, 8*N + 2):
        if Q == ((1, 0), (0, 1)):
            return t
        Q = matmul2(Q, P, N)
    raise RuntimeError("order not found")


def n_fixed(B, N):
    """#{v in (Z/N)^2 : (B-I)v = 0} EXACT via Smith normal form over Z."""
    M = ((B[0][0]-1, B[0][1]), (B[1][0], B[1][1]-1))
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    det = a*d - b*c
    s1 = gcd(gcd(a, b), gcd(c, d))
    if det == 0:
        # rank <= 1: solutions = N * gcd(N, s1)  (s1=0 means M=0: N^2)
        return N*N if s1 == 0 else N * gcd(N, s1)
    s2 = abs(det) // s1
    return gcd(N, s1) * gcd(N, s2)


def quantize_exact(B, N):
    """U[j,k] = exp(2 pi i /N * inv(2b)*(a k^2 - 2jk + d j^2))/sqrt(N), exact exponents."""
    a, b, c, d = B[0][0], B[0][1], B[1][0], B[1][1]
    assert gcd(2*b % N, N) == 1, f"2b not invertible mod {N}"
    inv2b = pow(2*b % N, -1, N)
    j = np.arange(N, dtype=np.int64).reshape(-1, 1)
    k = np.arange(N, dtype=np.int64).reshape(1, -1)
    E = (inv2b * ((a % N)*k*k - 2*j*k + (d % N)*j*j)) % N  # exact integer mod N
    return np.exp(2j*np.pi*E/N) / np.sqrt(N)


def ratio_std(X, Y):
    """std of elementwise ratio X/Y (constant-phase test); both full-modulus matrices."""
    r = (X / Y).ravel()
    return float(np.std(r)), complex(np.mean(r))


def raw_r_stat(phases):
    """C1: cc2's convention verbatim (circular closure, raw floats)."""
    ang = np.sort(np.mod(phases, 2*np.pi))
    s = np.diff(np.append(ang, ang[0] + 2*np.pi))
    s = np.maximum(s, 0)
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    r = r[np.isfinite(r)]
    return float(np.mean(r))


def exact_r_stats(mults, R):
    """C2/C3 from the exact multiplicity vector (length R, sum N).
    Gap list (circular, in units of 2pi/R): within an occupied slot of mult m,
    m-1 zero gaps; between consecutive occupied slots, the integer slot distance."""
    occ = [k for k in range(R) if mults[k] > 0]
    gaps = []  # integers (units 2pi/R)
    for i, k in enumerate(occ):
        gaps.extend([0]*(mults[k]-1))
        nxt = occ[(i+1) % len(occ)]
        gaps.append((nxt - k) % R if len(occ) > 1 else R)
    n = len(gaps)
    r_zero, cnt = Fr(0), 0
    r_skip, cnt_skip = Fr(0), 0
    for i in range(n):
        s1, s2 = gaps[i], gaps[(i+1) % n]
        if s1 == 0 and s2 == 0:
            cnt += 1  # 0/0 := 0 convention
        else:
            v = Fr(min(s1, s2), max(s1, s2))
            r_zero += v
            cnt += 1
            r_skip += v
            cnt_skip += 1
    c2_zero = r_zero / cnt
    c2_skip = r_skip / cnt_skip if cnt_skip else None
    # C3: distinct slots only
    dg = [( occ[(i+1) % len(occ)] - occ[i]) % R for i in range(len(occ))] \
        if len(occ) > 1 else [R]
    r3, c3n = Fr(0), 0
    for i in range(len(dg)):
        s1, s2 = dg[i], dg[(i+1) % len(dg)]
        r3 += Fr(min(s1, s2), max(s1, s2))
        c3n += 1
    return c2_zero, c2_skip, r3/c3n


print("="*78)
print("B480 re-derivation: <r> for the quantized golden cat map, N = 181, 301")
print("="*78)

for N in (181, 301):
    print(f"\n----- N = {N} " + "-"*50)
    R = ord_mod(A, N)
    fac = f" = 7 x 43; ord mod 7 = {ord_mod(A,7)}, ord mod 43 = {ord_mod(A,43)}" if N == 301 else ""
    print(f"ord(A mod {N}) = {R}{fac};  N/ord = {N/R:.3f}")

    U = quantize_exact(A, N)
    # V1 unitarity
    dev = np.max(np.abs(U.conj().T @ U - np.eye(N)))
    print(f"V1 unitarity: max|U+U - I| = {dev:.2e}")

    # V2 projective homomorphism (the check cc2's construction FAILED, std ~0.6)
    A2, A3 = matpow2(A, 2), matpow2(A, 3)
    s2, g2 = ratio_std(U @ U, quantize_exact(A2, N))
    s3, g3 = ratio_std(U @ quantize_exact(A2, N), quantize_exact(A3, N))
    print(f"V2 homomorphism: std[U(A)U(A)/U(A^2)] = {s2:.2e} (|gamma|={abs(g2):.6f});"
          f" std[U(A)U(A^2)/U(A^3)] = {s3:.2e}")

    # eigen decomposition
    lam = np.linalg.eigvals(U)
    print(f"   eigenvalue moduli: max||lam|-1| = {np.max(np.abs(np.abs(lam)-1)):.2e}")

    # V3: lam^R all equal (U^R = c I)
    zR = lam**R
    cph = np.mean(zR/np.abs(zR))
    print(f"V3 U^R = c*I: std(lam^R) = {np.std(zR):.2e}, c = exp({np.angle(cph):+.6f} i)")

    # V4 exact trace identity for all t = 1..R-1
    worst = 0.0
    for t in range(1, R):
        T = np.sum(lam**t)
        nf = n_fixed(matpow2(A, t), N)
        worst = max(worst, abs(abs(T)**2 - nf))
    print(f"V4 trace identity |tr U^t|^2 = #Fix(A^t) exact integers, t=1..{R-1}: "
          f"max deviation = {worst:.2e}")

    # slot clustering (exact multiplicities)
    theta0 = np.angle(cph)/R
    slots = np.rint(((np.angle(lam) - theta0) * R / (2*np.pi))).astype(int) % R
    slot_err = np.max(np.abs(np.angle(lam * np.exp(-1j*(theta0 + 2*np.pi*slots/R)))))
    mults = np.bincount(slots, minlength=R)
    hist = {}
    for m in mults:
        hist[int(m)] = hist.get(int(m), 0) + 1
    print(f"   slot assignment: max angular error = {slot_err:.2e}; "
          f"sum mult = {int(mults.sum())} (= N: {int(mults.sum())==N})")
    print(f"   multiplicity histogram {{mult: #slots}} = {dict(sorted(hist.items()))}")
    print(f"   distinct occupied slots: {int(np.sum(mults>0))}/{R}")

    # cross-check multiplicities via DFT of traces
    tvec = np.array([np.sum(lam**t) for t in range(R)])
    mdft = np.array([np.sum(tvec * np.exp(-2j*np.pi*np.arange(R)*k/R)
                            * np.exp(-1j*np.arange(R)*theta0)).real/R
                     for k in range(R)])
    print(f"   DFT-of-traces multiplicity cross-check: max|m_dft - m_slot| = "
          f"{np.max(np.abs(mdft - mults)):.2e}")

    # ---- the statistic under each convention ----
    c1 = raw_r_stat(np.angle(lam))
    c2z, c2s, c3 = exact_r_stats([int(m) for m in mults], R)
    print(f"C1 RAW-FLOAT      <r> = {c1:.4f}")
    print(f"C2 EXACT-DEGEN    <r> = {float(c2z):.4f}  (exact {c2z})   "
          f"[skip-0/0 variant: {float(c2s):.4f}]")
    print(f"C3 DISTINCT-SLOTS <r> = {float(c3):.4f}  (exact {c3})")
    print(f"   [banked claim: 0.16;  Poisson 0.386;  GOE 0.53]")

print("\n" + "="*78)
print("Controls: r-statistic code on Poisson & picket-fence references")
np.random.seed(0)
print(f"  Poisson control (301 uniform phases): <r> = "
      f"{raw_r_stat(np.random.uniform(0, 2*np.pi, 301)):.4f} (theory 0.386)")
print(f"  picket-fence control (301 equal slots): <r> = "
      f"{raw_r_stat(np.linspace(0, 2*np.pi, 301, endpoint=False)):.4f} (theory ~1)")
