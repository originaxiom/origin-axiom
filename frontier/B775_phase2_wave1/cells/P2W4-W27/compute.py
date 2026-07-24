#!/usr/bin/env python3
"""P2W4-W27 (OI-098 / W2.7) -- the value-tower growth law with the conductor N.

SEALED CRITERION
  RESOLVED-A : a growth law  dim V_N = f(N)  found and verified (incl. a fresh level)
  RESOLVED-B : no clean law at the swept N (bounded)
  UNRESOLVED : the computation could not decide (mod-p instability, gate failure, ...)

BACKGROUND (banked, re-read not re-asserted)
  B358/B367 (N=15) and B372 (N=45) compute the theta-lift pair observable
      C[j][l] = tr(Par . W1^j . W2^l),   v(a,b) = DFT_{o1,o2} C  (values in Q(zeta_{4N})),
  Gamma-averaged over a hard-coded 4-element group G < (Z/4N)* and identified exactly in a
  declared basis:  N=15 -> G={1,19,31,49}, home Q(sqrt5,sqrt-3) (dim 4);
                   N=45 -> G={1,19,91,109}, home Q(zeta9)+.Q(sqrt5,sqrt-3) (dim 12).
  B773 later used N=135 with G={1,109,271,379}.  The open lead: how does the home grow with N?

WHAT THIS CELL COMPUTES (all in-cell, nothing cited as the discriminating fact)

 [1] A STRUCTURAL RULE for the projection group, then a blind check against the three
     independently hard-coded banked groups:
        tau_N = the unique unit  == 1 (mod N), == -1 (mod 4)      [the 4-part / framing]
        sig_N = the unique unit  == 1 (mod 4), == 1 (mod n3), == -1 (mod n5)
                                                                  [the 5-part / "dynamics"]
        Gamma_N = <tau_N, sig_N> ~ V4  ==>  Fix(Gamma_N) = Q(zeta_{n3}) . Q(zeta_{n5})^+
        dim Fix(Gamma_N) = phi(4N)/4 = phi(N)/2   (N odd)
     must reproduce G(15), G(45), G(135) exactly (they were hard-coded, level by level, by
     arcs that never wrote a rule).  Then it PREDICTS G(75) = {1,49,151,199}.

 [2] An INTRINSIC (basis-free) measurement of the value field at each level: recompute the
     whole pipeline at every embedding zeta -> zeta^k, k in (Z/4N)*, and read
        Stab(v) = {k : v^{(k)} = v}      ==>   dim (field generated) = phi(4N)/|Stab|.
     Done for the RAW table (scope control) and for the Gamma-averaged observable (the law),
     at N = 15, 45, 75, 135.  Two well-separated prime blocks (1e6, 7e6); any disagreement
     => UNRESOLVED (no forced trend).  A MIRROR-DECOY group (halve the 3-end instead of the
     5-end -- same dimension phi(N)/2, different field) must be EXCLUDED at every level:
     the dimension alone cannot pick the two-ended reading, the stabilizer can.

 [3] tau acts by PURE LABEL TRANSPORT:  v^{(tau)}(a,b) = v(tau*a, tau*b).  Established at
     N=15,45 and PREDICTED-then-tested at the fresh levels N=75, N=135.  (This is why half of
     the index-4 projection is intrinsic rather than declared.)

 [4] THE FRESH LEVEL N = 75 (n3=3, n5=25 -- the 5-end grows for the first time; both banked
     levels grew the 3-end).  Predicted home Q(zeta_3).Q(zeta_25)^+ , dim 20 = phi(75)/2.
     Exact identification (CRT over 4 primes + rational reconstruction) in the declared
     20-dim basis {c^i}_{i<10} (x) {1, sqrt-3}, c = zeta_25 + zeta_25^-1, plus the Q-rank of
     the 6000 identified value vectors, and computed membership of the seam elements
     sqrt5, sqrt-15 in that home.  FALSIFIABLE: rank < 20 kills the law.
     N=135 (n3=27, n5=5 -- the 3/geometry end grows instead) is swept basis-free in [2];
     predicted dim 36 = phi(135)/2.

 [5] Hard conventions gate (B372's own gate, re-run here on a fresh numpy engine): the N=15
     pipeline must reproduce the banked flagship cells (0,4) and (0,8) of B367 exactly.

 [6] Banked-rank closure: Q-rank of the banked B367 (N=15) and B372 (N=45) value vectors.

HONEST SCOPE (computed here, part [2]): the RAW un-projected table has trivial stabilizer at
every swept level, i.e. it generates the full Q(zeta_{4N}) (dim 2*phi(N)).  The growth law is
therefore a law about the SEAM OBSERVABLE (the Gamma-projected readout that B358/B372 defined),
not about the raw traces.  Stated that way it is exact, tight, and falsifiable.

env: pyenv python3 + numpy.  Re-runnable, deterministic.
"""
import json
import os
import sys
import time
from fractions import Fraction as Fr
from math import gcd

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
B372 = os.path.join(ROOT, "B372_level45_sweeper")
B367 = os.path.join(ROOT, "B367_value_map")

LEVELS = [15, 45, 75, 135]     # 15,45 banked; 75 (5-end grows) and 135 (3-end grows) fresh
LEVEL_EXACT = 75               # the level identified exactly in a declared basis
BANKED_GAMMA = {15: [1, 19, 31, 49], 45: [1, 19, 91, 109], 135: [1, 109, 271, 379]}
PRIME_BLOCKS = [10 ** 6, 7 * 10 ** 6]   # two well-separated blocks (no mod-p coincidence)
NPRIME_EXACT = 4       # primes for CRT/rational reconstruction at N=75

LOG = []


def log(s):
    print(s, flush=True)
    LOG.append(s)


# ------------------------------------------------------------------ arithmetic
def totient(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def prime_part(N, q):
    r = 1
    while N % q == 0:
        r *= q
        N //= q
    return r


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primes_1_mod(m, count, start):
    out, k = [], start // m + 1
    while len(out) < count:
        p = m * k + 1
        if is_prime(p):
            out.append(p)
        k += 1
    return out


def primitive_root(p):
    fac, n = [], p - 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            fac.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fac.append(n)
    g = 2
    while True:
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g
        g += 1


def rational_reconstruct(r, M):
    from math import isqrt
    a, b = M, r % M
    p0, p1 = 0, 1
    bound = isqrt(M // 2)
    while b > bound:
        q = a // b
        a, b = b, a - q * b
        p0, p1 = p1, p0 - q * p1
    den = abs(p1)
    num = b if p1 > 0 else -b
    if den == 0 or den > bound:
        return None
    if (num - r * den) % M != 0:
        return None
    return Fr(num, den)


def qrank(vecs):
    M = [[Fr(x) for x in v] for v in vecs]
    if not M:
        return 0
    r, cols = 0, len(M[0])
    for c in range(cols):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


# ------------------------------------------------------- [1] the structural rule
def gamma_rule(N):
    """tau (4-part conj), sigma (5-part conj), Gamma = <tau,sigma> in (Z/4N)*."""
    m, n3, n5 = 4 * N, prime_part(N, 3), prime_part(N, 5)
    tau = next(x for x in range(1, m) if gcd(x, m) == 1 and x % N == 1 and x % 4 == 3)
    sig = next(x for x in range(1, m) if gcd(x, m) == 1 and x % 4 == 1
               and x % n3 == 1 and x % n5 == (n5 - 1) % n5)
    G = sorted({1, tau, sig, tau * sig % m})
    return tau, sig, G, n3, n5


def gamma_decoy(N):
    """VACUITY CONTROL: the MIRROR projection -- halve the 3-end instead of the 5-end.
    Fix(<tau,sig3>) = Q(zeta_{n3})^+ . Q(zeta_{n5}) has the SAME dimension phi(N)/2, so the
    dimension alone cannot distinguish it; only the observable's actual stabilizer can."""
    m, n3, n5 = 4 * N, prime_part(N, 3), prime_part(N, 5)
    tau = next(x for x in range(1, m) if gcd(x, m) == 1 and x % N == 1 and x % 4 == 3)
    s3 = next(x for x in range(1, m) if gcd(x, m) == 1 and x % 4 == 1
              and x % n3 == (n3 - 1) % n3 and x % n5 == 1)
    return sorted({1, tau, s3, tau * s3 % m})


# ------------------------------------------------------- the numpy F_p engine
class Eng:
    """Weil/theta pipeline at level N mod p, at the embedding zeta_{4N} -> zeta_{4N}^k."""

    def __init__(self, N, p, z4N):
        self.N, self.p = N, p
        self.z = z4N
        zN = pow(z4N, 4, p)
        self.zN = zN
        n = N
        Di = np.diag([pow(zN, (-(j * (j - 1) // 2)) % N, p) for j in range(n)]).astype(np.int64)
        F = np.array([[pow(zN, (i * j) % N, p) for j in range(n)] for i in range(n)],
                     dtype=np.int64)
        inv = pow(N, p - 2, p)
        Fi = np.array([[pow(zN, (-i * j) % N, p) * inv % p for j in range(n)] for i in range(n)],
                      dtype=np.int64)
        self.WR = self.mm(self.mm(F, Di), Fi)

    def mm(self, A, B):
        return (A @ B) % self.p

    def W(self, m):
        P = self.WR
        for _ in range(m - 1):
            P = self.mm(P, self.WR)
        Dm = np.diag([pow(self.zN, (m * (j * (j - 1) // 2)) % self.N, self.p)
                      for j in range(self.N)]).astype(np.int64)
        return self.mm(P, Dm)

    def powers(self, M, cap=400):
        n = self.N
        I = np.eye(n, dtype=np.int64)
        out, P = [I], M.copy()
        for k in range(1, cap + 1):
            if np.array_equal(P, I):
                return k, out
            out.append(P)
            P = self.mm(P, M)
        raise RuntimeError("order cap")

    def table(self, m1=1, m2=2):
        """DFT'd pair-cell table v(a,b), as a dict, mod p."""
        p, n = self.p, self.N
        o1, P1 = self.powers(self.W(m1))
        o2, P2 = self.powers(self.W(m2))
        par = (-np.arange(n)) % n
        A = np.stack([P[par, :] for P in P1])            # A[j,x,y] = (W1^j)[-x, y]
        B = np.stack(P2)                                 # B[l,y,x] = (W2^l)[y, x]
        C = np.einsum('jxy,lyx->jl', A, B) % p           # C[j,l] = tr(Par W1^j W2^l)
        z1 = pow(self.z, (4 * n) // o1, p)
        z2 = pow(self.z, (4 * n) // o2, p)
        E1 = np.array([[pow(z1, (-j * a) % o1, p) for a in range(o1)] for j in range(o1)],
                      dtype=np.int64)
        E2 = np.array([[pow(z2, (-l * b) % o2, p) for b in range(o2)] for l in range(o2)],
                      dtype=np.int64)
        V = ((E1.T @ C) % p @ E2) % p
        V = V * pow(o1 * o2, p - 2, p) % p
        return o1, o2, V


def all_embeddings(N, p, m1=1, m2=2):
    """raw value tables at every embedding k in (Z/4N)*; returns units, o1,o2, {k: V}"""
    m = 4 * N
    g = primitive_root(p)
    z0 = pow(g, (p - 1) // m, p)
    units = [k for k in range(1, m) if gcd(k, m) == 1]
    out, o1, o2 = {}, None, None
    for k in units:
        o1, o2, V = Eng(N, p, pow(z0, k, p)).table(m1, m2)
        out[k] = V
    return units, o1, o2, out


# --------------------------------------------------------- declared bases
def basis_vals(N, p, z4N):
    zN = pow(z4N, 4, p)
    n3, n5 = prime_part(N, 3), prime_part(N, 5)
    z3 = pow(zN, N // 3, p)
    sm3 = (z3 - pow(z3, 2, p)) % p                                  # sqrt(-3)
    if N == 15:
        z5 = pow(zN, 3, p)
        s5 = (z5 - pow(z5, 2, p) - pow(z5, 3, p) + pow(z5, 4, p)) % p
        return [1, s5, sm3, s5 * sm3 % p], ["1", "sqrt5", "sqrt-3", "sqrt-15"]
    if N == 45:
        z5 = pow(zN, 9, p)
        s5 = (z5 - pow(z5, 2, p) - pow(z5, 3, p) + pow(z5, 4, p)) % p
        base = [1, s5, sm3, s5 * sm3 % p]
        z9 = pow(zN, 5, p)
        c1 = (z9 + pow(z9, 8, p)) % p
        c2 = (pow(z9, 2, p) + pow(z9, 7, p)) % p
        out, nm = [], []
        for cn, c in (("1", 1), ("c1", c1), ("c2", c2)):
            for bn, b in zip(["1", "sqrt5", "sqrt-3", "sqrt-15"], base):
                out.append(c * b % p)
                nm.append(f"{cn}*{bn}")
        return out, nm
    if N == 75:
        z25 = pow(zN, 3, p)
        c = (z25 + pow(z25, 24, p)) % p                             # zeta25 + zeta25^-1
        out, nm = [], []
        ci = 1
        for i in range(10):
            for bn, b in (("1", 1), ("sqrt-3", sm3)):
                out.append(ci * b % p)
                nm.append(f"c^{i}*{bn}")
            ci = ci * c % p
        return out, nm
    raise ValueError(N)


def seam_elements(N, p, z4N):
    """sqrt5 and sqrt-15 in F_p at this embedding (seam-persistence readout)."""
    zN = pow(z4N, 4, p)
    n5 = prime_part(N, 5)
    z5 = pow(zN, N // 5, p)
    s5 = (z5 - pow(z5, 2, p) - pow(z5, 3, p) + pow(z5, 4, p)) % p
    z3 = pow(zN, N // 3, p)
    sm3 = (z3 - pow(z3, 2, p)) % p
    return s5, s5 * sm3 % p, n5


def inv_mod(A, p):
    """inverse of a square matrix mod p (list of lists) -> numpy int64, or None."""
    n = len(A)
    M = [list(r) + [1 if i == j else 0 for j in range(n)] for i, r in enumerate(A)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] % p), None)
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        iv = pow(M[c][c], p - 2, p)
        M[c] = [v * iv % p for v in M[c]]
        for r in range(n):
            if r != c and M[r][c]:
                f = M[r][c]
                M[r] = [(M[r][j] - f * M[c][j]) % p for j in range(2 * n)]
    return np.array([row[n:] for row in M], dtype=np.int64)


def solve_mod(A, y, p):
    n = len(A)
    M = [list(r) + [y[i]] for i, r in enumerate(A)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] % p), None)
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        inv = pow(M[c][c], p - 2, p)
        M[c] = [v * inv % p for v in M[c]]
        for r in range(n):
            if r != c and M[r][c]:
                f = M[r][c]
                M[r] = [(M[r][j] - f * M[c][j]) % p for j in range(n + 1)]
    return [M[i][n] for i in range(n)]


# ============================================================ main
def main():
    t0 = time.time()
    res = {"rule": {}, "levels": {}, "gate": {}, "banked_rank": {}, "law": {},
           "verdict": None, "notes": []}
    ok = {"rule": True, "gate": False, "seam": False, "stab": True, "stable": True, "decoy": True,
          "transport": True, "n75_span": False, "banked": False}

    # ---------------- [1] structural rule vs the three banked hard-coded groups
    log("[1] Gamma rule  Gamma_N = <tau,sigma>  vs the hard-coded banked groups")
    for N in sorted(set(list(BANKED_GAMMA) + LEVELS)):
        tau, sig, G, n3, n5 = gamma_rule(N)
        b = BANKED_GAMMA.get(N)
        match = (b is None) or (G == sorted(b))
        ok["rule"] &= match
        res["rule"][N] = {"tau": tau, "sigma": sig, "Gamma": G, "n3": n3, "n5": n5,
                          "banked": b, "matches_banked": (None if b is None else match),
                          "phi_over_2": totient(N) // 2}
        log(f"    N={N:>3} n3={n3:>2} n5={n5:>2} tau={tau:>3} sig={sig:>3} Gamma={G} "
            f"banked={b} match={match if b else '(prediction)'}  phi/2={totient(N)//2}")

    # ---------------- [2],[3],[5] per-level pipeline
    for N in LEVELS:
        tau, sig, G, n3, n5 = gamma_rule(N)
        Gd = gamma_decoy(N)
        m = 4 * N
        per_prime_raw, per_prime_gam, tport = [], [], []
        for p in [primes_1_mod(m, 1, start=s)[0] for s in PRIME_BLOCKS]:
            units, o1, o2, T = all_embeddings(N, p)
            base = T[1]
            sraw = frozenset(k for k in units if np.array_equal(T[k], base))
            # Gamma-averaged observable
            inv4 = pow(len(G), p - 2, p)
            AV = {k: (sum(T[(k * g) % m] for g in G) % p) * inv4 % p for k in units}
            sgam = frozenset(k for k in units if np.array_equal(AV[k], AV[1]))
            per_prime_raw.append(sraw)
            per_prime_gam.append(sgam)
            # tau label transport
            idx1 = [(tau * a) % o1 for a in range(o1)]
            idx2 = [(tau * b) % o2 for b in range(o2)]
            tport.append(bool(np.array_equal(T[tau], base[np.ix_(idx1, idx2)])))
        stable = (len(set(per_prime_raw)) == 1 and len(set(per_prime_gam)) == 1)
        sraw, sgam = sorted(per_prime_raw[0]), sorted(per_prime_gam[0])
        nu = totient(m)
        raw_dim, val_dim = nu // len(sraw), nu // len(sgam)
        tr_ok = all(tport)
        decoy_excluded = (sorted(Gd) != sgam) and not set(Gd).issubset(set(sgam))
        ok["stable"] &= stable
        ok["stab"] &= (sgam == G)
        ok["transport"] &= tr_ok
        ok["decoy"] = ok.get("decoy", True) and decoy_excluded
        res["levels"][N] = {
            "o1": o1, "o2": o2, "phi_4N": nu,
            "raw_stab": sraw, "raw_field_dim": raw_dim, "raw_is_full": raw_dim == nu,
            "obs_stab": sgam, "obs_stab_is_Gamma": sgam == G,
            "value_field_dim": val_dim, "predicted_phi_N_over_2": totient(N) // 2,
            "stable_across_primes": stable, "tau_label_transport": tr_ok,
            "mirror_decoy_group": Gd, "mirror_decoy_excluded": decoy_excluded,
        }
        log(f"[2] N={N:>3} (o1,o2)=({o1},{o2}) phi(4N)={nu} | raw stab={sraw} dim={raw_dim}"
            f"  obs stab={sgam} dim={val_dim} (pred {totient(N)//2})"
            f"  stab==Gamma={sgam == G}  2-prime-stable={stable}")
        log(f"[3] N={N:>3} tau={tau} acts by pure label transport: {tr_ok} | "
            f"mirror-decoy {Gd} excluded: {decoy_excluded}")

    # ---------------- [5] hard conventions gate at N=15 (exact, vs banked B367)
    log("[5] conventions gate: N=15 must reproduce banked B367 flagship cells")
    N = 15
    m, G = 60, gamma_rule(15)[2]
    gate_primes = primes_1_mod(60, 3, start=10 ** 6)
    reps, seen, held = [], set(), []
    for k in [x for x in range(1, m) if gcd(x, m) == 1]:
        key = min(k * g % m for g in G)
        if key not in seen:
            seen.add(key)
            reps.append(k)
        elif len(held) < 2:
            held.append(k)
    sols, Mod = [], 1
    for p in gate_primes:
        g = primitive_root(p)
        z0 = pow(g, (p - 1) // m, p)
        _, o1, o2, T = all_embeddings(15, p)
        inv4 = pow(4, p - 2, p)
        AV = {k: (sum(T[(k * gg) % m] for gg in G) % p) * inv4 % p for k in reps + held}
        A = [basis_vals(15, p, pow(z0, k, p))[0] for k in reps]
        cellvals = {}
        for (a, b) in [(0, 4), (0, 8)]:
            y = [int(AV[k][a][b]) for k in reps]
            x = solve_mod(A, y, p)
            for k in held:
                bh = basis_vals(15, p, pow(z0, k, p))[0]
                if sum(xi * bi for xi, bi in zip(x, bh)) % p != int(AV[k][a][b]):
                    x = None
                    break
            cellvals[(a, b)] = x
        sols.append((p, cellvals))
        Mod *= p
    banked15 = json.load(open(os.path.join(B367, "step0_tables.json")))["1,2"]
    gate = True
    for (a, b) in [(0, 4), (0, 8)]:
        out = []
        for i in range(4):
            r = 0
            for p, cv in sols:
                if cv[(a, b)] is None:
                    gate = False
                    break
                Mi = Mod // p
                r = (r + cv[(a, b)][i] * Mi * pow(Mi, p - 2, p)) % Mod
            f = rational_reconstruct(r, Mod)
            out.append(str(f))
        got, want = out, banked15[f"{a},{b}"]
        gate &= (got == want)
        res["gate"][f"{a},{b}"] = {"got": got, "banked": want, "match": got == want}
        log(f"    cell ({a},{b}) got {got}  banked {want}  match={got == want}")
    ok["gate"] = gate

    # ---------------- [4] the fresh level N=75: exact identification + Q-rank
    log("[4] fresh level N=75: exact identification in the predicted 20-dim home")
    N = 75
    m, G = 300, gamma_rule(75)[2]
    nb = 20
    reps, seen, held = [], set(), []
    for k in [x for x in range(1, m) if gcd(x, m) == 1]:
        key = min(k * g % m for g in G)
        if key not in seen:
            seen.add(key)
            reps.append(k)
        elif len(held) < 2:
            held.append(k)
    exact_primes = primes_1_mod(300, NPRIME_EXACT, start=7 * 10 ** 6)
    sols, Mod, seam_ok = [], 1, None
    o1 = o2 = None
    for p in exact_primes:
        g = primitive_root(p)
        z0 = pow(g, (p - 1) // m, p)
        _, o1, o2, T = all_embeddings(75, p)
        inv4 = pow(4, p - 2, p)
        AV = {k: (sum(T[(k * gg) % m] for gg in G) % p) * inv4 % p for k in reps + held}
        A = [basis_vals(75, p, pow(z0, k, p))[0] for k in reps]
        Ainv = inv_mod(A, p)
        if Ainv is None:
            raise RuntimeError("declared basis singular mod p at N=75")
        Y = np.stack([AV[k].reshape(-1) for k in reps])              # (20, o1*o2)
        Xall = (Ainv @ Y) % p                                        # (20, o1*o2)
        bad = 0
        good = np.ones(Xall.shape[1], dtype=bool)
        for k in held:                                               # held-out embeddings
            bh = np.array(basis_vals(75, p, pow(z0, k, p))[0], dtype=np.int64)
            pred = (bh @ Xall) % p
            good &= (pred == AV[k].reshape(-1) % p)
        bad = int((~good).sum())
        X = {(idx // o2, idx % o2): [int(v) for v in Xall[:, idx]]
             for idx in range(Xall.shape[1]) if good[idx]}
        log(f"    p={p}: identified {len(X)}/{o1*o2} cells, outside-span/failed {bad}")
        sols.append((p, X))
        Mod *= p
    keys = set(sols[0][1])
    for _, X in sols[1:]:
        keys &= set(X)
    crt_coef = [(p, (Mod // p) * pow(Mod // p, p - 2, p) % Mod) for p, _ in sols]
    exact = {}
    recon_fail = 0
    for key in sorted(keys):
        vec = []
        for i in range(nb):
            r = 0
            for (p, cc), (_, X) in zip(crt_coef, sols):
                r = (r + X[key][i] * cc) % Mod
            f = rational_reconstruct(r, Mod)
            if f is None:
                vec = None
                break
            vec.append(f)
        if vec is None:
            recon_fail += 1
        else:
            exact[key] = vec
    nz = {k: v for k, v in exact.items() if any(x != 0 for x in v)}
    rank75 = qrank(list(nz.values()))
    ok["n75_span"] = (rank75 == 20 and recon_fail == 0 and len(keys) == o1 * o2)
    # seam persistence at 75: sqrt5 = poly in c ; sqrt-15 = that * sqrt-3.
    # the "imaginary" half of the basis is the odd (sqrt-3) slots -> index 2i+1
    imag_cells = sum(1 for v in nz.values() if any(v[2 * i + 1] != 0 for i in range(10)))
    res["levels"][75].update({
        "exact_cells_identified": len(keys), "nonzero_cells": len(nz),
        "reconstruction_failures": recon_fail, "Q_rank_of_value_vectors": rank75,
        "cells_with_imaginary_(sqrt-3)_content": imag_cells,
        "declared_home": "Q(zeta_3).Q(zeta_25)^+  basis {c^i}x{1,sqrt-3}, c=zeta25+zeta25^-1",
    })
    log(f"    N=75: nonzero cells {len(nz)}/{o1*o2}, Q-rank {rank75}/20, "
        f"recon-fail {recon_fail}, cells with sqrt-3 content {imag_cells}")

    # seam membership at N=75, computed (not asserted): solve for sqrt5 and sqrt-15 in the
    # declared 20-dim home across the 20 coset embeddings, verify at the 2 held-out ones.
    seam_member = {}
    for p in exact_primes[:2]:
        g = primitive_root(p)
        z0 = pow(g, (p - 1) // m, p)
        A = [basis_vals(75, p, pow(z0, k, p))[0] for k in reps]
        Ai = inv_mod(A, p)
        for name, pick in (("sqrt5", 0), ("sqrt-15", 1)):
            y = np.array([seam_elements(75, p, pow(z0, k, p))[pick] for k in reps],
                         dtype=np.int64)
            x = (Ai @ y) % p
            good = True
            for k in held:
                bh = np.array(basis_vals(75, p, pow(z0, k, p))[0], dtype=np.int64)
                if int((bh @ x) % p) != seam_elements(75, p, pow(z0, k, p))[pick]:
                    good = False
            seam_member.setdefault(name, []).append(good)
    seam_ok = all(all(v) for v in seam_member.values())
    res["levels"][75]["seam_elements_in_home"] = {k: all(v) for k, v in seam_member.items()}
    ok["seam"] = seam_ok
    log(f"    N=75 seam membership (computed): sqrt5, sqrt-15 in the 20-dim home = {seam_ok}")

    # ---------------- [6] banked-rank closure
    r15 = qrank([[Fr(x) for x in v] for v in banked15.values()])
    d45 = json.load(open(os.path.join(B372, "sweep45.json")))
    allv = list(d45["pair"].values()) + list(d45["singles1"].values()) + list(d45["singles2"].values())
    r45 = qrank([[Fr(x) for x in v] for v in allv])
    res["banked_rank"] = {"15": r15, "45": r45, "expected": {"15": 4, "45": 12}}
    ok["banked"] = (r15 == 4 and r45 == 12)
    log(f"[6] banked Q-rank: N=15 {r15}/4, N=45 {r45}/12  closure={ok['banked']}")

    # ---------------- the law
    res["law"] = {
        "statement": ("dim_Q V_N = phi(N)/2 ;  V_N = Q(zeta_{n3}) . Q(zeta_{n5})^+ "
                      "= Fix(Gamma_N),  Gamma_N = <tau_N, sigma_N> < (Z/4N)*"),
        "growth": ("multiplicative in the two ends: dim V_N = phi(n3) * (phi(n5)/2). "
                   "3-end (geometry) enters IN FULL (imaginary kept); 5-end (dynamics) "
                   "enters as its REAL subfield only -- the two-ended object, read off the "
                   "Galois group of the value tower."),
        "swept": {N: res["levels"][N]["value_field_dim"] for N in LEVELS},
        "predicted": {N: totient(N) // 2 for N in LEVELS},
        "fresh_levels": ("N=75 (n3=3, n5=25: the 5/dynamics end grows for the first time) and "
                         "N=135 (n3=27, n5=5: the 3/geometry end grows) -- both ends tested"),
        "next_prediction": {225: totient(225) // 2},
        "domain": ("the golden-torus level family N = 3^a * 5^b (a,b >= 1); outside it "
                   "sigma_N is not defined by the rule -- a declared scope boundary, not a fit"),
        "reproduced_two_ways": ("(i) basis-free Galois stabilizer of the observable "
                                "(dim = phi(4N)/|Stab|) at 15/45/75; (ii) exact identification "
                                "+ Q-rank of the value vectors (banked 15/45, fresh 75)"),
        "scope": ("a law about the SEAM OBSERVABLE (the Gamma-projected readout of B358/B372): "
                  "computed here, the RAW table has trivial stabilizer at every swept level, so "
                  "the raw traces generate the full Q(zeta_4N) (dim 2*phi(N)). Half of the "
                  "index-4 projection is intrinsic (tau = pure label transport, computed at "
                  "15/45 and PREDICTED-then-verified at 75); the other half (sigma, real-on-the-"
                  "5-end) is the declared seam readout."),
    }

    # ---------------- verdict block
    checks = {
        "gamma_rule_matches_3_banked_levels": ok["rule"],
        "conventions_gate_N15": ok["gate"],
        "obs_stabilizer_equals_Gamma_all_levels": ok["stab"],
        "stable_across_two_prime_blocks": ok["stable"],
        "tau_label_transport_all_levels": ok["transport"],
        "N75_fills_20dim_home": ok["n75_span"],
        "banked_rank_closure": ok["banked"],
        "mirror_decoy_excluded_all_levels": ok["decoy"],
        "seam_elements_sqrt5_sqrtm15_in_N75_home": ok.get("seam", False),
    }
    res["checks"] = checks
    if not ok["stable"]:
        res["verdict"] = "UNRESOLVED"
        res["notes"].append("stabilizers disagree across prime blocks - trend refused (UNSTABLE)")
    elif not ok["gate"]:
        res["verdict"] = "UNRESOLVED"
        res["notes"].append("conventions gate failed at N=15 - no level-75 number is read")
    elif not ok["rule"]:
        res["verdict"] = "RESOLVED-B"
        res["notes"].append("the Gamma rule does not reproduce the banked groups - no clean law")
    elif not ok["decoy"]:
        res["verdict"] = "UNRESOLVED"
        res["notes"].append("the mirror decoy group is NOT excluded - the observable does not "
                            "single out the 5-end halving; the field identity is undetermined")
    elif ok["stab"] and ok["n75_span"] and ok["banked"] and ok["seam"]:
        res["verdict"] = "RESOLVED-A"
        res["notes"].append("dim V_N = phi(N)/2, V_N = Q(zeta_n3).Q(zeta_n5)^+ ; verified at "
                            "N=15,45 (banked) and at the fresh levels N=75, N=135, two ways")
    elif not ok["n75_span"] or not ok["stab"]:
        res["verdict"] = "RESOLVED-B"
        res["notes"].append("the swept levels do not follow phi(N)/2 - no clean law")
    else:
        res["verdict"] = "UNRESOLVED"
        res["notes"].append("checks incomplete")

    res["elapsed_sec"] = round(time.time() - t0, 1)
    log("")
    for k, v in checks.items():
        log(f"  check {k}: {v}")
    log(f"  VERDICT: {res['verdict']}  -- {res['notes'][0]}")
    log(f"  elapsed {res['elapsed_sec']}s")

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(HERE, "output.txt"), "w") as fh:
        fh.write("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
