"""Q2 (c): the character-blindness mechanism at the two k=2 anomaly rungs.
H-Q2' (SEALED, 287bfe86): SU(3)_2 odd block = rho_Fib (x) chi (chi order 3, either
Galois convention), kill = chi(A1-word) = 1 while ord(rho_Fib(A1)) = 10.
H-Q2'' (POST-HOC, formed after P-Q2-a's refutation; labeled as such): E6 k=2's 3-dim
odd block is REDUCIBLE = chi' (+) sigma with chi' an A1-blind character carrying the
mod-4 conductor part and sigma a 2-dim constituent whose own conductor drives the
k>=3 law (ord(A1 mod 21) = 8, split-7 kill -> 4 = banked clock)."""
import sys
sys.path.insert(0, '/Users/dri/oa-seat-cc2/seat-work/level_ladder_campaign/scripts')
sys.path.insert(0, '/Users/dri/oa-seat-cc2/seat-work/veins/v7_conduit')
import mpmath as mp
from engine import Level, weyl_group
from engine_v7 import An_Level

mp.mp.dps = 50
TOL = mp.mpf('1e-35')

def q(x):
    return int(mp.floor(x * mp.mpf(10) ** 30 + mp.mpf('0.5')))

def elt_order_scalar(z, cap=200):
    p = z
    for n in range(1, cap + 1):
        if abs(p - 1) < TOL:
            return n
        p *= z
    return None

# ---------- SU(3)_2: tensor factorization ----------
print("=== H-Q2' — SU(3)_2 odd block vs Fibonacci ===", flush=True)
L = An_Level(3, 2, name="SU(3)_2")
S, T = L.build(verbose=False)
fixed, pairs = L.theta_split()
s2 = 1 / mp.sqrt(2)
odd = mp.matrix(S.rows, 2)
for j, (a, b) in enumerate(pairs):
    odd[a, j], odd[b, j] = s2, -s2
S_o, T_o = odd.T * S * odd, odd.T * T * odd
phi = (1 + mp.sqrt(5)) / 2

for tag, hval, cval in (("Fib(c=14/5,h=2/5)", mp.mpf(2)/5, mp.mpf(14)/5),
                        ("YL-conj(c=-22/5,h=-1/5)", mp.mpf(-1)/5, mp.mpf(-22)/5),):
    nrm = 1 / mp.sqrt(phi + 2)
    S_f = mp.matrix([[nrm, nrm * phi], [nrm * phi, -nrm]])
    T_f = mp.matrix([[mp.e ** (-2j * mp.pi * cval / 24), 0],
                     [0, mp.e ** (2j * mp.pi * (hval - cval / 24))]])
    # ratio matrices: R_g = rho_odd(g) * rho_f(g)^{-1} — scalar iff factorization holds
    RS = S_o * S_f ** -1
    RT = T_o * T_f ** -1
    def scal(M):
        off = max(abs(M[0, 1]), abs(M[1, 0]))
        diag = abs(M[0, 0] - M[1, 1])
        return (off < TOL and diag < TOL), M[0, 0]
    okS, lamS = scal(RS)
    okT, lamT = scal(RT)
    print(f"  {tag}: S-ratio scalar {okS}, T-ratio scalar {okT}", flush=True)
    if okS and okT:
        oS, oT = elt_order_scalar(lamS), elt_order_scalar(lamT)
        lamA = lamT * lamT * lamS * lamT
        oA = elt_order_scalar(lamA)
        A_f = T_f * T_f * S_f * T_f
        # order of rho_Fib(A1-word)
        P = A_f.copy()
        oFib = None
        for n in range(1, 200):
            if max(abs(P[i, j] - (1 if i == j else 0)) for i in range(2) for j in range(2)) < TOL:
                oFib = n
                break
            P = P * A_f
        print(f"    chi(S) ord {oS}, chi(T) ord {oT}, chi(A1-word) ord {oA} "
              f"(BLIND iff 1); ord(rho_Fib(A1-word)) = {oFib} (banked clock 10)", flush=True)

# ---------- E6 k=2: decomposition ----------
print("\n=== H-Q2'' — E6 k=2 odd block decomposition (post-hoc label) ===", flush=True)
W, eps = weyl_group()
L2 = Level(2, W, eps)
S6 = L2.S_mp(50)
K = L2.K
t = [mp.e ** (2j * mp.pi * int(e) / (12 * K)) for e in L2.T_expo]
n_o = len(L2.pairs)
S_o = mp.matrix(n_o, n_o)
for i, (a, b) in enumerate(L2.pairs):
    for j, (c, d) in enumerate(L2.pairs):
        S_o[i, j] = (S6[a, c] - S6[a, d] - S6[b, c] + S6[b, d]) / 2
t_pairs = [t[a] for a, b in L2.pairs]
ordT_pairs = [elt_order_scalar(z) for z in t_pairs]
print(f"  pair T-eigenvalue orders: {ordT_pairs} (lcm = c_odd = 84 confirmed by q2 table)",
      flush=True)
print("  S_odd matrix (moduli, quantized):", flush=True)
for i in range(n_o):
    print("   ", [mp.nstr(abs(S_o[i, j]), 8) for j in range(n_o)], flush=True)
# 1-dim joint subrep <=> some coordinate i has S_o[i,j]=S_o[j,i]=0 for all j != i
for i in range(n_o):
    off = max(max(abs(S_o[i, j]), abs(S_o[j, i])) for j in range(n_o) if j != i)
    if off < TOL:
        chiT = t_pairs[i]
        chiS = S_o[i, i]
        oT = elt_order_scalar(chiT)
        oS = elt_order_scalar(chiS)
        chiA = chiT * chiT * chiS * chiT
        oA = elt_order_scalar(chiA)
        print(f"  DECOMPOSES: coordinate {i} is a 1-dim subrep: ord chi(T) = {oT}, "
              f"ord chi(S) = {oS}, ord chi(A1-word) = {oA} (BLIND iff 1)", flush=True)
        others = [j for j in range(n_o) if j != i]
        sub_t = [t_pairs[j] for j in others]
        # sigma conductor = lcm of T-eigenvalue orders on the 2-dim part
        import math
        from functools import reduce
        sig_c = reduce(lambda a, b: a * b // math.gcd(a, b),
                       [elt_order_scalar(z) for z in sub_t], 1)
        print(f"  sigma (2-dim) T-orders {[elt_order_scalar(z) for z in sub_t]} -> "
              f"sigma conductor {sig_c} (H-Q2'' wants 21)", flush=True)
        break
else:
    print("  NO coordinate 1-dim subrep — H-Q2'' fails in the diagonal-T basis "
          "(any 1-dim subrep must be coordinate-aligned unless T-degenerate; "
          "T-degeneracy:", len(set(map(q, [z.real for z in t_pairs]))) < n_o, ")", flush=True)
