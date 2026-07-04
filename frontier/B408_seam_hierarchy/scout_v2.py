"""B408 scout v2 -- the corrected pipeline: inner Pi_H average included.

s-part(cell) = the sqrt(-15)-coefficient of Pi_H(t): compute the table at ALL 16
embeddings e*g for g in the H-coset reps x the 4 flips; Pi_H = the mean over the
H-fixing subgroup lifts; then the 4-fold +--combination / (4 sqrt(-15)).
GATE (binding, unchanged): reproduce env15 = 1/48 and env45 = 0.02535468."""
import numpy as np, json, os, math
HERE = os.path.dirname(os.path.abspath(__file__))

def seam_envelope(N):
    M4 = 4*N
    units = [e for e in range(1, M4) if math.gcd(e, M4) == 1]
    # classification of a unit's action on sqrt5, sqrt(-3), i:
    def flips(e):
        f5 = 0 if e % 5 in (1, 4) else 1          # sqrt5 flips iff e non-residue mod 5
        f3 = 0 if e % 3 == 1 else 1               # sqrt(-3) flips iff e = 2 mod 3
        return f5, f3
    # H-fixing subgroup lifts: units fixing BOTH sqrt5 and sqrt(-3) (any i-action allowed:
    # values live in Q(zeta_{4N}) but the table entries lie in Q(zeta_N) x powers... be
    # safe: require e = 1 mod 4 as well, and average over the full fixing set)
    Hfix = [e for e in units if flips(e) == (0, 0)]
    reps = {}
    for (f5, f3) in ((0,0),(1,0),(0,1),(1,1)):
        reps[(f5,f3)] = next(e for e in units if flips(e) == (f5, f3) and e % 4 == 1)

    o1 = {15: 20, 45: 60, 135: 180}[N]; o2 = 12
    jj = np.arange(N)
    Par = np.zeros((N, N))
    for k in range(N): Par[(-k) % N, k] = 1

    cache = {}
    def table(e):
        if e in cache: return cache[e]
        z = np.exp(2j*np.pi*e/M4)
        zN = z**4
        D = np.diag(zN**(((jj*(jj-1))//2) % N))
        F = zN**(np.outer(jj, jj) % N)
        Fi = (zN**((-np.outer(jj, jj)) % N)) / N
        WR = F @ np.diag(1/np.diag(D)) @ Fi
        W1 = WR @ D
        W2 = WR @ WR @ D @ D
        C = np.empty((o1, o2), dtype=complex)
        W2p = [np.eye(N, dtype=complex)]
        for _ in range(o2-1): W2p.append(W2p[-1] @ W2)
        P1 = np.eye(N, dtype=complex)
        for a in range(o1):
            base = Par @ P1
            for b in range(o2):
                C[a, b] = np.trace(base @ W2p[b])
            P1 = P1 @ W1
        Fa = np.exp(-2j*np.pi*np.outer(np.arange(o1), np.arange(o1))/o1)
        Fb = np.exp(-2j*np.pi*np.outer(np.arange(o2), np.arange(o2))/o2)
        T = (Fa @ C @ Fb.T) / (o1*o2)
        cache[e] = T
        return T

    def PiH(e_mult):
        acc = np.zeros((o1, o2), dtype=complex)
        for g in Hfix:
            acc += table((g * e_mult) % M4)
        return acc / len(Hfix)

    T1  = PiH(1)
    T5  = PiH(reps[(1,0)])
    T3  = PiH(reps[(0,1)])
    T53 = PiH(reps[(1,1)])
    # sqrt(-15) at the base embedding
    z = np.exp(2j*np.pi/M4); zN = z**4
    z5r = zN**(N//5); z3r = zN**(N//3)
    sqrt5 = z5r - z5r**2 - z5r**3 + z5r**4
    sqrtm3 = z3r - z3r**2
    S = (T1 - T5 - T3 + T53) / (4 * (sqrt5 * sqrtm3))
    return float(np.max(np.abs(S))), len(Hfix)

out = {}
for N in (15, 45, 135):
    v, nfix = seam_envelope(N)
    out[str(N)] = v
    print(f"N={N}: corrected scout envelope = {v:.8f}   (|Hfix| = {nfix})", flush=True)
print("gate: 1/48 =", 1/48, " env45 =", 0.02535468)
json.dump(out, open(os.path.join(HERE, "scout_v2.json"), "w"), indent=1)
print("SCOUTDONE")
