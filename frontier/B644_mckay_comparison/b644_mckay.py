"""B644 — the ear vs the mod-5 congruence shadow (prereg b77e5bdf)."""
import importlib.util
import os
import random
import sys

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "hp_stage", os.path.join(HERE, "..", "B629_interaction_values",
                             "exact_hearing.py"))
hp = importlib.util.module_from_spec(spec)
_argv = sys.argv
sys.argv = [spec.origin]
spec.loader.exec_module(hp)
sys.argv = _argv
mp.mp.dps = 60
PHI = (1 + mp.sqrt(5)) / 2

# ---- the hearing side (B640's verified construction) -------------------------
w, S, T, cc = hp.su3_data(2)
n = len(w)
Si = S ** -1
Ti = T ** -1
R_full, L_full = T, Si * Ti * S
pairs = []
seen = set()
for i, lam in enumerate(w):
    lc = (lam[1], lam[0])
    if lam == lc:
        continue
    j = w.index(lc)
    key = tuple(sorted((i, j)))
    if key not in seen:
        seen.add(key)
        pairs.append((i, j))
U = mp.zeros(n, 2)
for col, (i, j) in enumerate(pairs):
    U[i, col] = 1 / mp.sqrt(2)
    U[j, col] = -1 / mp.sqrt(2)
rho_R = U.T * R_full * U
rho_L = U.T * L_full * U

TOL = mp.mpf(10) ** -40


def fp(M):
    return tuple((round(float(M[i, j].real), 25),
                  round(float(M[i, j].imag), 25))
                 for i in range(2) for j in range(2))


elems = {fp(mp.eye(2)): ("", mp.eye(2))}
frontier = [("", mp.eye(2))]
while frontier:
    new = []
    for (wd, M) in frontier:
        for gname, G in (("R", rho_R), ("L", rho_L)):
            M2 = M * G
            k = fp(M2)
            if k not in elems:
                elems[k] = (wd + gname, M2)
                new.append((wd + gname, M2))
    frontier = new
assert len(elems) == 360

# ---- the arithmetic side ------------------------------------------------------
def m5mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 5
                       for j in range(2)) for i in range(2))


R5 = ((1, 1), (0, 1))
L5 = ((1, 0), (1, 1))
I5 = ((1, 0), (0, 1))
NI5 = ((4, 0), (0, 4))


def word5(wd):
    M = I5
    for ch in wd:
        M = m5mul(M, R5 if ch == "R" else L5)
    return M


print("== M1: the mod-5 closure ==", flush=True)
g5 = {I5}
fr5 = [I5]
while fr5:
    new = []
    for M in fr5:
        for G in (R5, L5):
            M2 = m5mul(M, G)
            if M2 not in g5:
                g5.add(M2)
                new.append(M2)
    fr5 = new
print(f"  |<R5, L5>| = {len(g5)}  (SL(2,5) order 120: {len(g5) == 120})",
      flush=True)


def ord5(M):
    P = I5
    for k in range(1, 61):
        P = m5mul(P, M)
        if P == I5:
            return k
    return 0


def class5(M):
    """(order, qr-type) — qr-type only meaningful for orders 5, 10."""
    o = ord5(M)
    if o not in (5, 10):
        return (o, None)
    # unipotent parameter: for o=5, M is conjugate to [[1,x],[0,1]];
    # invariant: whether (M - I) as rank-1 gives x*(square) — use the
    # standard invariant x mod squares via any nonzero entry of (M-I)
    # paired against the eigen-structure: for trace 2 (o=5) or trace 3
    # (o=10, = -unipotent), take N = M or -M (unipotent), then
    # x-class = QR-type of any nonzero entry ratio invariant:
    N = M if o == 5 else m5mul(NI5, M)
    # N unipotent != I: N - I has rank 1; the class invariant is
    # b/c-free: for N = [[1+ac', ...]] use the invariant tr-free form:
    # conjugation scales the parameter by squares; representative
    # parameter = any nonzero of (N-I) contracted with itself via the
    # symplectic form: x = c if c != 0 else b' pattern:
    a = (N[0][0] - 1) % 5
    b = N[0][1] % 5
    c = N[1][0] % 5
    # parameter class: x ~ b if c == 0 else ... the conjugation-invariant
    # is the value  c  (lower-left) when nonzero, else b, each mod QR —
    # BUT b and c classes differ by a square factor of the conjugator^2;
    # the true invariant: the quadratic class of the parameter x in
    # N ~ [[1,x],[0,1]] equals the class of (b) if c==0 and a==0, of
    # (-c) after the swap conj by [[0,1],[-1,0]]: x -> -c. Handle:
    if c == 0 and a == 0:
        x = b
    elif c != 0:
        x = (-c) % 5
    else:
        # a != 0, c == 0: N = [[1+a, b],[0, 1-a]]? not unipotent then;
        x = b
    qr = x in (1, 4)
    return (o, qr)


# ---- M2: the kernel comparison ------------------------------------------------
print("\n== M2: kernel match on 360 canonical + 200 random words ==",
      flush=True)


def is_scalar(M):
    return (abs(M[0, 1]) < TOL and abs(M[1, 0]) < TOL and
            abs(M[0, 0] - M[1, 1]) < TOL)


def hear(wd):
    M = mp.eye(2)
    for ch in wd:
        M = M * (rho_R if ch == "R" else rho_L)
    return M


fails = 0
for (wd, M) in elems.values():
    sc = is_scalar(M)
    m5 = word5(wd)
    pm = m5 in (I5, NI5)
    if sc != pm:
        fails += 1
random.seed(644)
for _ in range(200):
    wd = "".join(random.choice("RL") for _ in range(random.randint(1, 40)))
    sc = is_scalar(hear(wd))
    pm = word5(wd) in (I5, NI5)
    if sc != pm:
        fails += 1
print(f"  kernel mismatches: {fails}/560", flush=True)

# ---- M3: the character factorization -------------------------------------------
print("\n== M3: class-function factorization on ker(det) (120 words) ==",
      flush=True)
ker = [(wd, M) for (wd, M) in elems.values()
       if abs((M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]) - 1) < mp.mpf(10) ** -30]
print(f"  |ker det| = {len(ker)}", flush=True)

# the two candidate tables (Galois-conjugate; QR-convention A and B)
gold = {"phi": PHI, "iphi": 1 / PHI}
tableA = {(1, None): mp.mpf(2), (2, None): mp.mpf(-2), (4, None): mp.mpf(0),
          (3, None): mp.mpf(-1), (6, None): mp.mpf(1),
          (5, True): 1 / PHI, (5, False): -PHI,
          (10, True): PHI, (10, False): -1 / PHI}
tableB = {k: v for k, v in tableA.items()}
tableB[(5, True)] = -PHI
tableB[(5, False)] = 1 / PHI
tableB[(10, True)] = -1 / PHI
tableB[(10, False)] = PHI

per_class = {}
well_defined = True
for (wd, M) in ker:
    cl = class5(word5(wd))
    t = M[0, 0] + M[1, 1]
    if abs(t.imag) > 1e-25:
        print(f"  NONREAL trace at {wd}: {t}", flush=True)
    tv = t.real
    if cl in per_class:
        if abs(per_class[cl] - tv) > TOL:
            well_defined = False
            print(f"  NOT well-defined at class {cl}: {mp.nstr(per_class[cl], 8)} vs {mp.nstr(tv, 8)} (word {wd})", flush=True)
    else:
        per_class[cl] = tv
print(f"  class-function well-defined: {well_defined}", flush=True)
print("  observed class table:", flush=True)
for cl in sorted(per_class, key=lambda c: (c[0], str(c[1]))):
    print(f"    class {cl}: tr = {mp.nstr(per_class[cl], 12)}", flush=True)
for nm, tab in (("A", tableA), ("B", tableB)):
    ok = all(cl in tab and abs(tab[cl] - tv) < mp.mpf(10) ** -20
             for cl, tv in per_class.items())
    print(f"  matches golden table {nm}: {ok}", flush=True)

# ---- M4: the pentagon through the arithmetic side ------------------------------
print("\n== M4: the cat map ==", flush=True)
m5RL = word5("RL")
clRL = class5(m5RL)
print(f"  mod-5 matrix of RL: {m5RL}; class {clRL}", flush=True)
tRL = hear("RL")
print(f"  tr rho_hear(RL) = {mp.nstr((tRL[0,0]+tRL[1,1]).real, 25)}",
      flush=True)
print(f"  -1/phi           = {mp.nstr(-1/PHI, 25)}", flush=True)
print("\nB644 DONE", flush=True)
