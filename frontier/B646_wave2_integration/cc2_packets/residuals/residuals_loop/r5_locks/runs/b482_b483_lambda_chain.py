"""Reimplementation (not a verbatim rerun -- the originating high-precision computation
n=55/40dps was described in prose, not saved as a script) for:
  B482 -- banked lambda_chain = 1.57705744122666946... ("per R/L letter", the FULL chain)
  B483 -- limits 3.5223870342 (per-FULL-letter true limit) vs 2.1775291199 (seat-2's own
          per-letter rung value; true limit of THAT clock = 2.177528751053)

Source basis (read-only, origin-axiom repo):
  - frontier/B471_chain_verification/chain_verify.py  (defines the FULL chain s_k, the
    HALF chain X_k, and F_k; already prints u_13^(1/F_13) vs u_14^(1/F_14) as
    "lambda_chain (per-FULL-letter growth)")
  - papers/P4_markov_stage/DRAFT_v8.md L560-565 (defines G_k := #R/L letters of s_k,
    Fibonacci recursion, and lambda_chain := lim (tr s_k)^(1/G_k) = 1.57705744122666946...)
  - frontier/B471_chain_verification/CHAIN_SCOUT_FINDINGS.md L36 (seat-2's own
    "per-letter growth unit lambda_chain = 2.1775291199...")
  - frontier/B471_chain_verification/FINDINGS.md L54-58 ("my per-full-letter 3.5223904...
    [=lambda_full] and their 2.1775291... satisfy lambda_mine = lambda_theirs^phi")
  - frontier/B483_fibonacci_anyon_face/FINDINGS.md ("true limit 3.5223870342"; seat-2's
    "2.1775291199 -> 2.177528751" true-limit statement)

NOTE on method: u_n, v_n grow doubly-exponentially in n (like lambda^(phi^n)), so at
n=55 they have ~10^11 digits -- exact Python big-ints are infeasible. Instead the
Fricke recursion u_{k+1}=u_k*u_{k-1}-u_{k-2} is run directly in mpmath floating point
(dps=80) -- valid because the subtracted term is exponentially smaller than the
product, so no precision is lost by staying in floating point throughout (standard
technique for these run-away Lyapunov-type sequences; cross-checked against exact
Python-int traces for n<=20 below).
"""
import mpmath as mp

mp.mp.dps = 80


def Am(m):
    return (m * m + 1, m, m, 1)  # (a,b,c,d) row-major 2x2


def mat_mul_int(A, B):
    a, b, c, d = A
    e, f, g, h = B
    return (a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h)


N_EXACT = 20
S = {0: Am(2), 1: Am(1)}
for k in range(2, N_EXACT + 1):
    S[k] = mat_mul_int(S[k - 1], S[k - 2])
u_exact = {k: S[k][0] + S[k][3] for k in S}

X = {0: (2, 1, 1, 0), 1: (1, 1, 1, 0)}
for k in range(2, N_EXACT + 1):
    X[k] = mat_mul_int(X[k - 1], X[k - 2])
v_exact = {k: X[k][0] + X[k][3] for k in X}

# --- letter-count sequences (plain ints -- these only grow like phi^n, totally tame) ---
NMAX = 60
F = {0: 1, 1: 1}
G = {0: 4, 1: 2}
H = {0: 2, 1: 1}
for k in range(2, NMAX + 1):
    F[k] = F[k - 1] + F[k - 2]
    G[k] = G[k - 1] + G[k - 2]
    H[k] = H[k - 1] + H[k - 2]

# --- floating-point (mpmath, dps=80) Fricke recursion for u_n up to n=60 ---
# Full chain: det(S_k) = 1 always (Am(m) has det 1), so the PLAIN Fricke recursion
# u_{k+1} = u_k u_{k-1} - u_{k-2} holds throughout.
uf = {0: mp.mpf(u_exact[0]), 1: mp.mpf(u_exact[1]), 2: mp.mpf(u_exact[2])}
for k in range(3, NMAX + 1):
    uf[k] = uf[k - 1] * uf[k - 2] - uf[k - 3]

# Half chain: det(X_k) alternates (X0,X1 both det -1; det(X_k)=det(X_{k-1})*det(X_{k-2})),
# so the TWISTED Fricke recursion v_{k+1} = v_k v_{k-1} - det(X_{k-1}) v_{k-2} must be used
# (chain_verify.py: "the breath is the sign in the composition law").
d_exact = {0: -1, 1: -1}
for k in range(2, NMAX + 1):
    d_exact[k] = d_exact[k - 1] * d_exact[k - 2]
vf = {0: mp.mpf(v_exact[0]), 1: mp.mpf(v_exact[1]), 2: mp.mpf(v_exact[2])}
for k in range(3, NMAX + 1):
    vf[k] = vf[k - 1] * vf[k - 2] - d_exact[k - 2] * vf[k - 3]

# sanity: cross-check float recursion against exact ints for n<=20
max_rel_err_u = max(abs(uf[k] - u_exact[k]) / u_exact[k] for k in range(N_EXACT + 1))
max_rel_err_v = max(abs(vf[k] - v_exact[k]) / v_exact[k] for k in range(N_EXACT + 1))
print(f"sanity: float-vs-exact max rel err (u) = {max_rel_err_u}, (v) = {max_rel_err_v}")
assert max_rel_err_u < mp.mpf('1e-70') and max_rel_err_v < mp.mpf('1e-70')

phi = (1 + mp.sqrt(5)) / 2


def root(x, exponent):
    return mp.power(x, mp.mpf(1) / exponent)


print()
print("=== headline comparisons at n=55 ===")
lam_chain = root(uf[55], G[55])
lam_full = root(uf[55], F[55])
seat2_F = root(vf[55], F[55])
half_own = root(vf[55], H[55])
print(f"lambda_chain  (u_55^(1/G_55))         = {lam_chain}")
print(f"  target (banked, B482)               = 1.57705744122666946...")
print(f"lambda_full   (u_55^(1/F_55))         = {lam_full}")
print(f"  target (B483 'true limit')          = 3.5223870342...")
print(f"seat-2 candidate (v_55^(1/F_55))      = {seat2_F}")
print(f"  target (B483, seat-2's true limit)  = 2.177528751053...")
print(f"half-chain own clock (v_55^(1/H_55))  = {half_own}")

print()
print("=== convergence: n=13,14,30,55,60 ===")
for k in (13, 14, 30, 55, 60):
    print(f"n={k:2d}: full/F={root(uf[k], F[k])}  full/G={root(uf[k], G[k])}  "
          f"half/F={root(vf[k], F[k])}  half/H={root(vf[k], H[k])}")

print()
print("=== rung values at n=13 (compare to FINDINGS' quoted finite-n artifacts) ===")
print(f"u_13^(1/F_13)  = {root(uf[13], F[13])}   (FINDINGS quotes 3.5223783 as the n=13 rung)")
print(f"v_13^(1/F_13)  = {root(vf[13], F[13])}   (candidate for seat-2's quoted 2.1775291199)")

print()
print("=== cross-check the golden-exponent relation lambda_full = seat2_clock^phi ===")
print(f"seat2_F ^ phi                        = {mp.power(seat2_F, phi)}")
print(f"lambda_full                          = {lam_full}")
print(f"match to 1e-30?                      = {abs(mp.power(seat2_F, phi) - lam_full) < mp.mpf('1e-30')}")

print()
print("=== ratio / power checks relating lambda_chain to the other clocks ===")
print(f"G_55/F_55 (letter-count ratio)        = {mp.mpf(G[55])/mp.mpf(F[55])}")
print(f"lambda_chain^(G55/F55)                = {mp.power(lam_chain, mp.mpf(G[55])/mp.mpf(F[55]))}  (should equal lambda_full)")
print(f"H_55/F_55 (half-chain letter ratio)   = {mp.mpf(H[55])/mp.mpf(F[55])}")
print(f"seat2_F^(H55/F55)                     = {mp.power(seat2_F, mp.mpf(H[55])/mp.mpf(F[55]))}  (should equal half_own)")
