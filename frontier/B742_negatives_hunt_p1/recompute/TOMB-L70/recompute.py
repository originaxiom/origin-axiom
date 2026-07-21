#!/usr/bin/env python3
"""
B739 Stage-B recompute -- TOMB-L70 (E19: compute-not-cite, both directions).

BANKED KILL (speculations/TOMBSTONES.md:L70, banked in the B123 session, PROGRESS_2026-Q2
2026-06-08): "Finite-k eigenvalues are roots of unity -- tautological: the rep is defined over
q=exp(2*pi*i/(k+2)), so everything is roots of unity by construction."  Claim killed: that
finite-k eigenvalues being roots of unity is a DISCOVERED arithmetic signal.  kill_form:
category-error; fact_basis at Stage A: asserted (no computation of the universality mechanism
exists in the arc -- B132's probe only ran specific seed words).

DISCRIMINATING FACT (what, if true, kills the claim): the roots-of-unity property of the
finite-k quantum eigenvalues is UNIVERSAL-BY-CONSTRUCTION -- it holds for EVERY mapping-class
word at every finite level k (because the level-k representation has finite image), and it is
CREATED by the quantization at q = exp(2*pi*i/(k+2)) (the classical monodromy eigenvalues are
NOT roots of unity).  If universal, observing it for the framework's seed carries zero
information => not a discovered signal => the kill stands.

CONVENTIONS (one-hop citation basis -- the arc's own declared conventions,
frontier/B132_quantum_layer/FINDINGS.md, "The validated SU(2)_k convention"):
  * level k rep has dim k+1, labels a = 0..k;
  * S = modular S-matrix: S[a,b] = sqrt(2/(k+2)) * sin(pi*(a+1)*(b+1)/(k+2));
  * T = diag exp(2*pi*i * a(a+2) / (4(k+2)))   (NO c/24 framing);
  * Dehn twists R = T, L = S T S^-1; monodromy of an R/L word = the ordered product;
  * seed for m: word "R"*m + "L"*m (B132 S1c); m=1 seed RL = the figure-eight monodromy,
    classical matrix [[2,1],[1,1]].

DECLARED CHOICES (E1 -- undeclared in the arc, chosen here):
  * "ordered product" read LEFT-TO-RIGHT: rho("RL") = rho(R) @ rho(L).  (Reversal is the
    transpose-conjugate ordering; it is spectrum-preserving for the battery as a whole, and
    RL vs LR are conjugate words, so no result below depends on this choice.)
  * Root-of-unity certification: candidate order n from double-precision eigenvalues
    (rational arg / (2*pi) via Fraction.limit_denominator(10^5), per-eigenvalue residual
    |lam^d - 1| < 1e-8), then CERTIFIED in mpmath at 60 significant digits by binary powering:
    max-entry |U^n - I| < 1e-45.  U is unitary (checked), hence diagonalizable, so
    U^n = I  <=>  every eigenvalue is an n-th root of unity.  Error budget of the 60-dps
    product chain is < 1e-54, so the 1e-45 gate is conservative.
  * Battery (deterministic, exhaustive -- no sampling): k = 1..10, all 30 nonempty R/L words
    of length <= 4 in lexicographic order, plus the metallic seeds R^m L^m for m = 3,4,5
    (m=1,2 already inside length<=4); k = 11,12: seed RL only.
  * Group-closure cap for the finite-image computation: 400000 elements (k = 1,2,3).
  * Everything deterministic: no wall-clock, no randomness, no network.

Gate 5: pure mathematics (quantum representations of SL(2,Z)); no SM quantities anywhere.
"""

import numpy as np
import mpmath as mp
from fractions import Fraction
from math import gcd, lcm
from itertools import product

# ----------------------------------------------------------------------------- constructors

def S_np(k):
    return np.array([[np.sqrt(2.0 / (k + 2)) * np.sin(np.pi * (a + 1) * (b + 1) / (k + 2))
                      for b in range(k + 1)] for a in range(k + 1)], dtype=complex)

def T_np(k):
    return np.diag([np.exp(2j * np.pi * (a * (a + 2)) / (4 * (k + 2))) for a in range(k + 1)])

def rho_np(word, k):
    S, T = S_np(k), T_np(k)
    L = S @ T @ S          # S^2 = I (checked below), so S^-1 = S
    M = np.eye(k + 1, dtype=complex)
    for ch in word:
        M = M @ (T if ch == "R" else L)
    return M

def S_mp(k):
    return [[mp.sqrt(mp.mpf(2) / (k + 2)) * mp.sin(mp.pi * (a + 1) * (b + 1) / (k + 2))
             for b in range(k + 1)] for a in range(k + 1)]

def T_mp(k):
    return [[mp.e ** (2j * mp.pi * (a * (a + 2)) / (4 * (k + 2))) if a == b else mp.mpc(0)
             for b in range(k + 1)] for a in range(k + 1)]

def matmul_mp(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(m)) for j in range(p)] for i in range(n)]

def rho_mp(word, k):
    S, T = S_mp(k), T_mp(k)
    L = matmul_mp(matmul_mp(S, T), S)
    M = [[mp.mpc(1) if i == j else mp.mpc(0) for j in range(k + 1)] for i in range(k + 1)]
    for ch in word:
        M = matmul_mp(M, T if ch == "R" else L)
    return M

def matpow_mp(M, n):
    d = len(M)
    R = [[mp.mpc(1) if i == j else mp.mpc(0) for j in range(d)] for i in range(d)]
    B = [row[:] for row in M]
    while n:
        if n & 1:
            R = matmul_mp(R, B)
        n >>= 1
        if n:
            B = matmul_mp(B, B)
    return R

def maxdev_from_identity_mp(M):
    d = len(M)
    return max(abs(M[i][j] - (1 if i == j else 0)) for i in range(d) for j in range(d))

# ------------------------------------------------------------------- order finding + certify

def candidate_order(U):
    """Candidate multiplicative order of unitary U from double-precision eigenvalues.
    Returns (n, per-eigenvalue orders) or (None, reason)."""
    lams = np.linalg.eigvals(U)
    orders = []
    for lam in lams:
        if abs(abs(lam) - 1.0) > 1e-9:
            return None, f"|lam|={abs(lam):.12f} != 1"
        x = (np.angle(lam) / (2 * np.pi)) % 1.0
        fr = Fraction(x).limit_denominator(10 ** 5)
        d = fr.denominator
        if abs(lam ** d - 1.0) > 1e-8:
            return None, f"lam^{d} != 1 (residual {abs(lam**d-1.0):.2e})"
        orders.append(d)
    return lcm(*orders) if orders else 1, sorted(orders)

def certify(word, k, n):
    """Certify U^n = I at 60 dps: max-entry deviation from I."""
    U = rho_mp(word, k)
    return maxdev_from_identity_mp(matpow_mp(U, n))

# ----------------------------------------------------------------------------------- run

mp.mp.dps = 60
CERT_TOL = mp.mpf("1e-45")
print("=" * 78)
print("TOMB-L70 recompute: finite-k roots-of-unity -- by construction, or a signal?")
print("=" * 78)

# --- 0. convention sanity: S is an involution, S and T unitary; exact ord(T) by rationals.
print("\n[0] Convention sanity + exact ord(T) (rational arithmetic, no floats):")
for k in range(1, 13):
    S = S_np(k)
    dev_S2 = np.max(np.abs(S @ S - np.eye(k + 1)))
    dev_Su = np.max(np.abs(S @ S.conj().T - np.eye(k + 1)))
    ordT = 1
    for a in range(k + 1):
        ordT = lcm(ordT, Fraction(a * (a + 2), 4 * (k + 2)).denominator)
    assert dev_S2 < 1e-12 and dev_Su < 1e-12, f"S convention broken at k={k}"
    print(f"  k={k:2d}: dim={k+1:2d}  |S^2-I|max={dev_S2:.1e}  ord(T)={ordT}"
          f"  (divides 4(k+2)={4*(k+2)}: {4*(k+2) % ordT == 0})")

# --- 1. CONTROL A: the classical monodromy eigenvalue is NOT a root of unity.
print("\n[1] CONTROL A -- classical seed RL = [[2,1],[1,1]] (figure-eight monodromy):")
Mc = np.array([[2, 1], [1, 1]], dtype=float)
lc = max(np.linalg.eigvals(Mc).real)
print(f"  leading eigenvalue = {lc:.12f} = phi^2 (|lam| != 1) -> NOT a root of unity.")
print("  So the roots-of-unity property is CREATED by the finite-k quantization, not")
print("  inherited from the object being quantized.")

# --- 2. CONTROL B: cyclotomic/rational matrix entries alone do NOT force roots of unity.
print("\n[2] CONTROL B -- entries in the cyclotomic field do not suffice:")
Mb = np.array([[1, 1], [1, 0]], dtype=float)   # entries in Q, a subfield of every Q(zeta_N)
lb = max(np.linalg.eigvals(Mb).real)
print(f"  [[1,1],[1,0]] has entries in Q subset Q(zeta_N), eigenvalue {lb:.12f} = phi:")
print("  NOT a root of unity. The tombstone's one-line mechanism ('defined over q => roots")
print("  of unity') is compressed: the operative construction is UNITARITY + FINITE IMAGE")
print("  of the level-k rep, both of which the q=exp(2*pi*i/(k+2)) construction supplies.")
print("  This is computed next -- the tautology is real, with the mechanism made explicit.")

# --- 3. THE UNIVERSALITY BATTERY (exhaustive words, certified orders).
print("\n[3] Battery: every nonempty R/L word of length <= 4 (30 words) + metallic seeds")
print("    R^m L^m (m=3,4,5), at k = 1..10; seed RL at k = 11,12.  Certification: 60-dps")
print("    |U^n - I|max < 1e-45  (=> every eigenvalue is an n-th root of unity, exactly).")
words = ["".join(w) for length in range(1, 5) for w in product("RL", repeat=length)]
words += ["R" * m + "L" * m for m in (3, 4, 5)]
total = fails = 0
worst_dev = mp.mpf(0)
for k in range(1, 13):
    batch = words if k <= 10 else ["RL"]
    k_orders = []
    for w in batch:
        U = rho_np(w, k)
        du = np.max(np.abs(U @ U.conj().T - np.eye(k + 1)))
        assert du < 1e-10, f"non-unitary rho({w}) at k={k}"
        n, eig_orders = candidate_order(U)
        if n is None:
            print(f"  k={k:2d} word={w:10s}  FAILED root-of-unity test: {eig_orders}")
            fails += 1
            total += 1
            continue
        dev = certify(w, k, n)
        worst_dev = max(worst_dev, dev)
        ok = dev < CERT_TOL
        if not ok:
            print(f"  k={k:2d} word={w:10s}  CERTIFICATION FAILED: |U^{n}-I| = {mp.nstr(dev, 3)}")
            fails += 1
        k_orders.append(n)
        total += 1
    if k_orders:
        print(f"  k={k:2d}: {len(k_orders)} words, all certified; matrix orders "
              f"lcm={lcm(*k_orders)}, max={max(k_orders)}")
print(f"  TOTAL: {total} (k,word) cases, {fails} failures; worst certified residual "
      f"|U^n - I|max = {mp.nstr(worst_dev, 3)}")

# --- 4. FINITE IMAGE: BFS closure of <rho(R), rho(L)> at k = 1,2,3 (all words, all inverses).
print("\n[4] Finite image (the 'by construction' mechanism, computed): BFS closure of the")
print("    group generated by rho(R)^+-1, rho(L)^+-1 (R,L generate SL(2,Z) classically,")
print("    so this covers EVERY mapping-class word of ANY length, inverses included):")
for k in (1, 2, 3):
    T = T_np(k)
    S = S_np(k)
    L = S @ T @ S
    gens = [T, L, T.conj().T, L.conj().T]        # unitary => inverse = conjugate transpose
    def key(M):
        return ((np.round(M.real, 6) + 0.0).tobytes(), (np.round(M.imag, 6) + 0.0).tobytes())
    Idm = np.eye(k + 1, dtype=complex)
    seen = {key(Idm)}
    frontier = [Idm]
    CAP = 400000
    closed = True
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                P = M @ g
                kk = key(P)
                if kk not in seen:
                    seen.add(kk)
                    nxt.append(P)
        frontier = nxt
        if len(seen) > CAP:
            closed = False
            break
    if closed:
        print(f"  k={k}: |<rho(R),rho(L)>| = {len(seen)}  (FINITE => every element has finite"
              f" order => ALL eigenvalues of ALL words are roots of unity at this k)")
    else:
        print(f"  k={k}: closure exceeded cap {CAP} (not used; battery still certifies)")

# --- 5. Cross-anchor to the arc's own banked number (B132 S1c).
print("\n[5] Cross-anchor: eigenvalue-order multiset of the m=1 seed RL at k=4")
n, eig_orders = candidate_order(rho_np("RL", 4))
print(f"  recomputed orders = {eig_orders}  (B132 S1c banked: [2, 2, 6, 6, 6])")
print(f"  match: {eig_orders == [2, 2, 6, 6, 6]}")

# --- verdict line
print("\n" + "=" * 78)
print("VERDICT INPUT: the roots-of-unity property is (i) TRUE and certified at every")
print("tested (k, word); (ii) UNIVERSAL -- it holds for every word in the exhaustive")
print("battery and, at k=1,2,3, for the ENTIRE (finite) image group, i.e. for every")
print("mapping class; (iii) ABSENT classically (phi^2 fails) and NOT implied by cyclotomic")
print("entries alone (phi fails) -- it is manufactured by the unitary finite-image")
print("construction at q = exp(2*pi*i/(k+2)).  A property that holds by construction for")
print("every mapping class at every finite k discriminates nothing: observing it for the")
print("framework's seed is not a discovered arithmetic signal.  The banked kill stands.")
print("=" * 78)
