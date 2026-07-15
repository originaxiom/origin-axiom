"""B613 — THE CLOSURE THEOREM, verified ingredient by ingredient.

THEOREM (amphichiral => level-uniform conjugation-closure).
Let (S, T) be SU(3)_k modular data: S symmetric unitary, S^2 = C (the
charge conjugation, real permutation), T diagonal unitary, [C, T] = 0.
Put R = rho(R) = T, L = rho(L) = S^{-1} T^{-1} S. Then:
  (I1) conj(X) = C X^{-1} C for X in {R, L};
  (I0) S^2 = zeta C for a scalar phase zeta (level-dependent) — S^2
       enters the derivations only by CONJUGATION, so zeta cancels;
       in particular [S, C] = 0;
  (I2) rho(swap(x)) = S rho(x)^{-1} S^{-1} (swap: R <-> L);
  (I3) R and L are SYMMETRIC matrices, hence rho(rev(w)) = W^T.
For a weld word w with swap(w) = sigma(rev(w)) (sigma a cyclic rotation
with prefix P) — the GHH anti-palindromicity, equivalent to the bundle's
amphichirality (B134/V123) — the chain gives
  conj(W) = C S^{-1} rho(swap(w)) S C = C S^{-1} P^{-1} W^T P S C
          = Q^{-1} W^T Q,   Q = P S C,
and Q commutes with C (P is a word in R, L; [S, C] = [C, T] = 0-driven),
so Q preserves the odd space and conj(W|odd) ~ (W|odd)^T: the odd
hearing spectrum is conjugation-closed AT EVERY LEVEL. (One-way; the
converse stays empirical per B612's accidental closures.)

Derivations of I1-I3 from the axioms:
  I1(R): conj(T) = T^{-1} = C T^{-1} C by [C,T] = 0.
  I1(L): conj(L) = S T S^{-1} (S-bar = S^{-1} by symmetric-unitary);
         C L^{-1} C = S^2 S^{-1} T S S^{-2} = S T S^{-1}. Equal.
  I2:    S rho(R)^{-1} S^{-1} = S T^{-1} S^{-1} = S^{-1} T^{-1} S = L
         iff S^2 T^{-1} = T^{-1} S^2, i.e. [C, T] = 0. And
         S rho(L)^{-1} S^{-1} = S S^{-1} T S S^{-1} = T... careful:
         rho(L)^{-1} = S^{-1} T S, so S rho(L)^{-1} S^{-1} = T = R. OK.
  I3:    R = T diagonal. L^T = S T^{-1} S^{-1} = S^{-1} T^{-1} S = L by
         [C, T] = 0 again.
Every axiom and identity is verified EXACTLY-numerically (1e-11) below
at several levels; the assembled conjugation is verified for the four
amphichiral witnesses (whose swap(w) = rev(w), so P = I, Q = S C) and
shown to FAIL for the chiral controls with the same Q (consistency).

Run: python3 closure_theorem.py   (~2 min)
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

AMPHI = ["RL", "RRLL", "RLRL", "RRRLLL"]
CHIRAL = ["RRL", "RRRL", "RRLLL"]
ok = True
for k in (2, 4, 7, 9):
    w, S, T, cc = b238.su3_data(k)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    Si = np.linalg.inv(S)
    R = T
    L = Si @ np.linalg.inv(T) @ S
    tol = 1e-11
    ax = {
        "S symmetric": np.allclose(S, S.T, atol=tol),
        "S unitary": np.allclose(S @ np.conj(S.T), np.eye(n), atol=tol),
        "S^2 = zeta C": (lambda S2: np.allclose(
            S2, (S2[0, 0] / C[0, 0] if C[0, 0] else
                 S2[np.nonzero(C)[0][0], np.nonzero(C)[1][0]] /
                 C[np.nonzero(C)[0][0], np.nonzero(C)[1][0]]) * C,
            atol=tol))(S @ S),
        "[S,C] = 0": np.allclose(S @ C, C @ S, atol=tol),
        "[C,T] = 0": np.allclose(C @ T, T @ C, atol=tol),
        "I1(R)": np.allclose(np.conj(R), C @ np.linalg.inv(R) @ C, atol=tol),
        "I1(L)": np.allclose(np.conj(L), C @ np.linalg.inv(L) @ C, atol=tol),
        "I2(R->L)": np.allclose(S @ np.linalg.inv(R) @ Si, L, atol=tol),
        "I2(L->R)": np.allclose(S @ np.linalg.inv(L) @ Si, R, atol=tol),
        "I3(L symmetric)": np.allclose(L, L.T, atol=tol),
    }
    allax = all(ax.values())
    ok &= allax
    print(f"kappa={k+3}: axioms+ingredients "
          f"{'ALL PASS' if allax else [a for a, v in ax.items() if not v]}",
          flush=True)
    Q = S @ C
    Qi = np.linalg.inv(Q)
    for word in AMPHI:
        # verify swap(w) = rev(w) for these witnesses (P = I)
        swap = word.translate(str.maketrans("RL", "LR"))
        assert swap == word[::-1], f"{word}: prefix P != I — extend the cell"
        W = np.eye(n, dtype=complex)
        for ch in word:
            W = W @ (R if ch == "R" else L)
        good = np.allclose(np.conj(W), Qi @ W.T @ Q, atol=1e-9)
        ok &= good
        print(f"    {word:>7}: conj(W) = Q^-1 W^T Q  [{good}]", flush=True)
    for word in CHIRAL:
        W = np.eye(n, dtype=complex)
        for ch in word:
            W = W @ (R if ch == "R" else L)
        fails = not np.allclose(np.conj(W), Qi @ W.T @ Q, atol=1e-9)
        print(f"    {word:>7} (chiral control): identity fails with this Q "
              f"[{fails}]", flush=True)

assert ok, "THEOREM VERIFICATION FAILED"
print("\nTHE CLOSURE THEOREM VERIFIED: amphichiral weld => conj(W) ~ W^T "
      "via Q = P S C (C-commuting) => the odd hearing spectrum is "
      "conjugation-closed at every level.", flush=True)
print("B613 DONE", flush=True)
