"""B408 scout -- the seam envelope at 15/45/135 via complex embeddings (gated)."""
import numpy as np, json, os, math
HERE = os.path.dirname(os.path.abspath(__file__))

def seam_envelope(N, m1=1, m2=2):
    M4 = 4*N
    # flip exponents: a5 flips sqrt5 only (a5 = 1 mod 3-part & 4, non-QR-preserving mod 5-part...)
    # operational: sqrt5 = sum Legendre zeta5^k -> flips iff e is a non-residue mod 5;
    # sqrt(-3) flips iff e = 2 mod 3. Choose a5: nonresidue mod 5, =1 mod 3, =1 mod 4;
    # a3: =1 mod 5, =2 mod 3, =1 mod 4  (CRT within Z/(4N) on the relevant parts).
    def crt_cond(m5, m3):
        for e in range(1, M4):
            if math.gcd(e, M4) != 1: continue
            if e % 5 in m5 and e % 3 == m3 and e % 4 == 1:
                return e
        raise RuntimeError
    a5 = crt_cond({2, 3}, 1)      # non-residues mod 5: {2,3}
    a3 = crt_cond({1, 4}, 2)      # residues mod 5, flip mod 3
    a53 = (a5 * a3) % M4

    def table_max_s(e_base):
        tabs = {}
        for tag, mult in (("1", 1), ("5", a5), ("3", a3), ("53", a53)):
            e = (e_base * mult) % M4
            z = np.exp(2j*np.pi*e/M4)
            zN = z**4
            jj = np.arange(N)
            D = np.diag(zN**(((jj*(jj-1))//2) % N))
            F = zN**np.outer(jj, jj % N)
            Fi = np.conj(F).T / N * np.exp(0)     # F^{-1} = conj(F)/N at unit embedding... careful:
            # For general embedding, F^{-1}[i,j] = zN^{-ij}/N exactly:
            Fi = (zN**((-np.outer(jj, jj)) % N)) / N
            WR = F @ np.linalg.inv(D) @ Fi
            W1 = WR @ D
            W2 = WR @ WR @ D @ D
            # orders: 15/45: (20,12), (60,12); 135: (180,12)
            o1 = {15: 20, 45: 60, 135: 180}[N]; o2 = 12
            Par = np.zeros((N, N))
            for k in range(N): Par[(-k) % N, k] = 1
            # C table via power walk
            C = np.empty((o1, o2), dtype=complex)
            P1 = np.eye(N, dtype=complex)
            W2p = [np.eye(N, dtype=complex)]
            for _ in range(o2-1): W2p.append(W2p[-1] @ W2)
            for a in range(o1):
                base = Par @ P1
                for b in range(o2):
                    C[a, b] = np.trace(base @ W2p[b])
                P1 = P1 @ W1
            # DFT to t(a,b)
            Fa = np.exp(-2j*np.pi*np.outer(np.arange(o1), np.arange(o1))/o1)
            Fb = np.exp(-2j*np.pi*np.outer(np.arange(o2), np.arange(o2))/o2)
            tabs[tag] = (Fa @ C @ Fb.T) / (o1*o2)
        s15 = np.exp(2j*np.pi*e_base/M4)**4
        # sqrt(-15) at this embedding: product of gauss sums
        z5 = (np.exp(2j*np.pi*e_base/M4)**4)**(N//5 if N % 5 == 0 else 1)
        # simpler: sqrt5(e) and sqrt(-3)(e) from character sums at the embedding
        zz = np.exp(2j*np.pi*e_base/M4)
        z5r = zz**(4*(N//5))
        z3r = zz**(4*(N//3))
        sqrt5 = z5r**1 - z5r**2 - z5r**3 + z5r**4
        sqrtm3 = z3r - z3r**2
        sqrtm15 = sqrt5 * sqrtm3
        S = (tabs["1"] - tabs["5"] - tabs["3"] + tabs["53"]) / (4*sqrtm15)
        return float(np.max(np.abs(S)))

    best = 0.0
    # embeddings: enough to take e over a transversal of the c-classes; sample the units
    # e = 1 mod 4 with distinct action on zeta_{3-part}: for the scout take e in a small set
    Es = [e for e in range(1, M4) if math.gcd(e, M4) == 1 and e % 4 == 1][:9]
    for e in Es:
        best = max(best, table_max_s(e))
    return best

out = {}
for N in (15, 45, 135):
    v = seam_envelope(N)
    out[str(N)] = v
    print(f"N={N}: scout seam envelope = {v:.8f}", flush=True)
print("gate targets: 1/48 =", 1/48, " env45 =", 0.02535468)
json.dump(out, open(os.path.join(HERE, "scout_135.json"), "w"), indent=1)
print("SCOUTDONE")
