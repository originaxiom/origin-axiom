"""SEALED-DIGEST CHECK c4 (value-free group theory).
Claims (agy Theorem 18 Part D; relay l.231-242; Theorem 20 docstring Part C.1):
 G16 = <K_Fi, K_Fj> (the Theorem-14 D4 compensators, in SO(10, I10)) has order 16, 3 central involutions (+-Z135, -I),
 12 elements of order 4 (8 square to +Z135, 4 to -Z135), is Z4 x| Z4 = SmallGroup(16, 4) -- 'correcting Theorem 14's
 label Q8 x {+-I}'; its adjoint image is Q8; the Clifford lifts to the chiral spinors 16+- generate order 32 with
 K^_i^4 = K^_j^4 = -1, K^_k^4 = +1; kernel words x_i^2 x_k^-2 (trivial in SU(2), -I on the vector) and x_i^4 x_k^-4
 (trivial on the vector, -1 on the spinors).
The compensator MATRICES are the lane's (their definition is the claim's subject): this script executes ONLY the matrix
construction lines of Part D (no firewalled quantity appears in them; asserted), never prints them, and then verifies
every claim with its own code -- including a spin lift solved from the Clifford intertwining equation, not the lane's."""
import hashlib, math, pathlib, re, subprocess, sys, textwrap
import numpy as np
ROOT = str(__import__('pathlib').Path(__file__).resolve().parents[4])
src = subprocess.run(["git", "show", "18c607040:src/origin_axiom/toe_closure.py"], capture_output=True, cwd=ROOT).stdout.decode()
lines = src.split("\n")
region = "\n".join(lines[2901:3313])
print("sealed region 2902-3313 sha256 (with/without final newline):", hashlib.sha256((region + "\n").encode()).hexdigest()[:16],
      hashlib.sha256(region.encode()).hexdigest()[:16], "(manifest 126bf26afb69e8b1)")
i0 = next(i for i in range(2901, 3313) if lines[i].lstrip().startswith("# Construct exact") and "Clifford" in lines[i])
i1 = next(i for i in range(i0, 3313) if lines[i].lstrip().startswith("skc_j_32 ="))
slice_ = "\n".join(lines[i0:i1 + 1])
FW = re.compile(r"y_?b\b|y_?t\b|y_?tau|m_?b\b|m_?t\b|m_?tau|tan|bottom|pdg|measur|held|level|inter|sigma_?3|ratio", re.I)
assert not FW.search(slice_), "firewall word in the executed slice"
ns = {"np": np, "math": math}
exec(textwrap.dedent(slice_), ns)
Ki, Kj, Kk, g = ns["kc_i_10"], ns["kc_j_10"], ns["kc_k_10"], ns["i10_mat"]
print("executed construction lines", i0 + 1, "-", i1 + 1, "(firewall words: none)")

def key(M): return tuple(np.round(np.asarray(M, dtype=complex), 7).ravel().view(float).tolist())
I10 = np.eye(10)
for nm, K in (("K_i", Ki), ("K_j", Kj), ("K_k", Kk)):
    print("  %s: |K^T g K - g| = %.1e  |K^+ K - I| = %.1e  det = %s" % (nm, np.abs(K.T @ g @ K - g).max(), np.abs(K.conj().T @ K - I10).max(), np.round(np.linalg.det(K), 10)))

def close(gens, dim):
    els = {key(np.eye(dim)): np.eye(dim, dtype=complex)}; frontier = list(els.values())
    while frontier:
        new = []
        for A in frontier:
            for Gm in gens:
                P = A @ Gm; k = key(P)
                if k not in els: els[k] = P; new.append(P)
        frontier = new
        if len(els) > 4096: raise RuntimeError("group too large")
    return list(els.values())
def order(M, dim, cap=64):
    P = M.copy()
    for n in range(1, cap + 1):
        if np.abs(P - np.eye(dim)).max() < 1e-7: return n
        P = P @ M
    return None

G = close([Ki, Kj], 10)
print("\n(1) |<K_i, K_j>| =", len(G), "; K_k in it:", any(np.abs(X - Kk).max() < 1e-7 for X in G))
Zm = Ki @ Ki
Z135 = np.diag([-1, 1, -1, 1, -1] * 2).astype(complex)
print("  K_i^2 = Z135 = diag(-1,1,-1,1,-1)^(+)2:", np.abs(Zm - Z135).max() < 1e-9, "; K_k^2 = -Z135:", np.abs(Kk @ Kk + Z135).max() < 1e-9,
      "; K_i^-1 K_k K_i = K_k^-1:", np.abs(np.linalg.inv(Ki) @ Kk @ Ki - np.linalg.inv(Kk)).max() < 1e-9)
ords = [order(X, 10) for X in G]
from collections import Counter
print("  element orders:", dict(Counter(ords)))
sq = Counter()
for X, o in zip(G, ords):
    if o == 4:
        S = X @ X; sq["+Z135" if np.abs(S - Z135).max() < 1e-7 else "-Z135" if np.abs(S + Z135).max() < 1e-7 else "-I" if np.abs(S + I10).max() < 1e-7 else "other"] += 1
print("  squares of the order-4 elements:", dict(sq))
center = [X for X in G if all(np.abs(X @ Y - Y @ X).max() < 1e-7 for Y in G)]
abel = len(center) == len(G)
hamil = all(all(any(np.abs(Y @ Xp @ np.linalg.inv(Y) - W).max() < 1e-7 for W in close([X], 10)) for Y in G) for X in G for Xp in [X])
print("  |center| =", len(center), "; abelian:", abel, "; every cyclic subgroup normal (Hamiltonian test):", hamil)
cls = "Z4 x| Z4 (SmallGroup(16,4))" if (not abel and set(ords) <= {1, 2, 4} and ords.count(2) == 3 and len(sq) == 2) else \
      "Q8 x Z2 (SmallGroup(16,12))" if (not abel and set(ords) <= {1, 2, 4} and ords.count(2) == 3 and len(sq) == 1) else "other"
print("  => isomorphism class by invariants (nonabelian, exponent 4, 3 involutions, distinct squares):", cls)
print("  -I in G:", any(np.abs(X + I10).max() < 1e-7 for X in G))
# Q8 relations for i -> K_i, j -> K_j, k -> K_k: in SO(10) and modulo +-I
def eq_pm(A, Bm): return "=" if np.abs(A - Bm).max() < 1e-7 else "=-" if np.abs(A + Bm).max() < 1e-7 else "no"
print("  Q8 test: K_i^2 vs K_j^2:", eq_pm(Ki @ Ki, Kj @ Kj), "; K_i^2 vs K_k^2:", eq_pm(Ki @ Ki, Kk @ Kk), "; K_i K_j vs K_k:", eq_pm(Ki @ Kj, Kk),
      "; K_j K_i vs K_k:", eq_pm(Kj @ Ki, Kk), "; K_k K_i vs K_j:", eq_pm(Kk @ Ki, Kj))

# (2) the adjoint image: G / (G cap {+-I})
reps = []
for X in G:
    if not any(np.abs(X - R).max() < 1e-7 or np.abs(X + R).max() < 1e-7 for R in reps): reps.append(X)
def ord_mod(X):
    P = X.copy()
    for n in range(1, 17):
        if np.abs(P - I10).max() < 1e-7 or np.abs(P + I10).max() < 1e-7: return n
        P = P @ X
print("\n(2) adjoint image order:", len(reps), "; orders mod +-I:", dict(Counter(ord_mod(R) for R in reps)),
      "(Q8 = 1 x1, 1 x2, 6 x4; D4 = 1, 5, 2; Z2^3 = 1, 7, 0; Z4 x Z2 = 1, 3, 4)")

# (3) spin lift solved from K^ Gam_M K^-1 = sum_N K_NM Gam_N (own Clifford algebra, own normalisation)
sp, sm, sz, e2 = np.array([[0, 1], [0, 0]], complex), np.array([[0, 0], [1, 0]], complex), np.diag([1, -1]).astype(complex), np.eye(2, dtype=complex)
def jw(a, op):
    M = np.array([[1.0 + 0j]])
    for b in range(5): M = np.kron(M, sz if b < a else (op if b == a else e2))
    return M
Gam = [jw(a, sp) for a in range(5)] + [jw(a, sm) for a in range(5)]
acerr = max(np.abs(Gam[m] @ Gam[n] + Gam[n] @ Gam[m] - g[m, n] * np.eye(32)).max() for m in range(10) for n in range(10))
chir = np.eye(32, dtype=complex)
for a in range(5): chir = chir @ (np.eye(32) - 2 * (Gam[a] @ Gam[a + 5]))
print("\n(3) own Clifford algebra: max |{G_M, G_N} - g_MN| =", acerr, "; chirality^2 = 1:", np.abs(chir @ chir - np.eye(32)).max() < 1e-12)
def solve_lift(K):
    Gp = [sum(K[n, m] * Gam[n] for n in range(10)) for m in range(10)]
    Abig = sum(((np.kron(Gam[m].T, np.eye(32)) - np.kron(np.eye(32), Gp[m]))).conj().T @ (np.kron(Gam[m].T, np.eye(32)) - np.kron(np.eye(32), Gp[m])) for m in range(10))
    w, v = np.linalg.eigh(Abig)
    X = v[:, 0].reshape(32, 32, order="F"); return X, w[0], w[1]
Cs = sum((np.kron(Gam[m], np.eye(32)) - np.kron(np.eye(32), Gam[m])).conj().T @ (np.kron(Gam[m], np.eye(32)) - np.kron(np.eye(32), Gam[m])) for m in range(10))
wc, vc = np.linalg.eigh(Cs); C = vc[:, 0].reshape(32, 32, order="F")     # solves C Gam^T = Gam C  (vec(C Gam^T) = (Gam (x) I) vec C)
print("  charge-conjugation C (C G^T C^-1 = G): nullity gap", wc[0], wc[1], "; check", max(np.abs(C @ Gam[m].T @ np.linalg.inv(C) - Gam[m]).max() for m in range(10)))
lifts = {}
for nm, K in (("i", Ki), ("j", Kj), ("k", Kk)):
    X, w0, w1 = solve_lift(K)
    X = X / math.sqrt(np.real(np.trace(X.conj().T @ X)) / 32)
    rv = C @ X.T @ np.linalg.inv(C) @ X; lam = np.trace(rv) / 32
    X = X / np.sqrt(lam)                                                        # now X^t X = 1: X in Spin(10), up to sign
    ierr = max(np.abs(X @ Gam[m] @ np.linalg.inv(X) - sum(K[n, m] * Gam[n] for n in range(10))).max() for m in range(10))
    lifts[nm] = X
    agy = ns["skc_%s_32" % nm]; dsign = min(np.abs(X - agy).max(), np.abs(X + agy).max())
    X4 = np.linalg.matrix_power(X, 4)
    print("  lift %s: nullspace eigs %.1e, %.1e ; intertwining err %.1e ; [X, chirality] %.1e ; X^4 = %s ; |X -+ lane's lift| = %.1e"
          % (nm, w0, w1, ierr, np.abs(X @ chir - chir @ X).max(), "+1" if np.abs(X4 - np.eye(32)).max() < 1e-8 else "-1" if np.abs(X4 + np.eye(32)).max() < 1e-8 else "other", dsign))
ev = np.where(np.real(np.diag(chir)) > 0)[0]; od = np.where(np.real(np.diag(chir)) < 0)[0]
for nmh, idx in (("16+", ev), ("16-", od)):
    Hs = close([lifts["i"][np.ix_(idx, idx)], lifts["j"][np.ix_(idx, idx)]], 16)
    print("  group generated on %s: order %d" % (nmh, len(Hs)))

# (4) the kernel words (Theorem 20 docstring): x_i^2 x_k^-2 and x_i^4 x_k^-4
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], complex); QK = QI @ QJ
def w(a, b, n): return np.linalg.matrix_power(a, n) @ np.linalg.inv(np.linalg.matrix_power(b, n))
for n in (2, 4):
    su2 = w(QI, QK, n); vec = w(Ki, Kk, n); spn = w(lifts["i"], lifts["k"], n)
    def nm(M, d): return "+I" if np.abs(M - np.eye(d)).max() < 1e-8 else "-I" if np.abs(M + np.eye(d)).max() < 1e-8 else ("+-chirality" if (np.abs(M - chir).max() < 1e-8 or np.abs(M + chir).max() < 1e-8) else "+-i*chirality (the lift of -I10)" if (np.abs(M - 1j * chir).max() < 1e-8 or np.abs(M + 1j * chir).max() < 1e-8) else "other")
    print("\n(4) word x_i^%d x_k^-%d: SU(2) (quaternions) %s ; vector 10 %s ; adjoint 45 %s ; spinor 32 %s" % (
        n, n, nm(su2, 2), nm(vec, 10), "trivial" if nm(vec, 10) in ("+I", "-I") else "nontrivial", nm(spn, 32)))
print("\n(5) e8 = (45,1)+(1,15)+(10,6)+(16,4)+(16b,4b): dimension", 45 + 15 + 60 + 64 + 64)
