"""B598 step 4b — the P2 map's classical side: the bending responses
(failure-enforcing).

THE FRAME (declared; see P2_MAP.md): the domain is the six BENDING lines
H0(T^2; V_m) at the weld torus (Johnson-Millson bending = the banked
B599-ALG twist family exp(t v_m), v_m = the block's highest vector).
Copy 2's letters are conjugated by c = exp(t v_m):  y = c b-bar c^{-1},
Y = c B-bar c^{-1} (b-bar = the K-conjugated mirror letter) — EXACTLY the
banked r4b_extraction frame, now J-paired per the chain's step-5 mandate.

GATES:
  (i)   v_m is peripherally fixed: Ad(rho(mu)) v_m = v_m and
        Ad(rho(lambda)) v_m = v_m in gl(27) (h0 >= 1 realized by the top
        vector) — the bending direction is well-defined;
  (ii)  degree-2 truncation vs the banked witnesses: r4b's slot is
        <exp(t v) v0, rho_t(b2) v0>_dot (t-dependent LEFT vector); its t^2
        Im-coefficient at m=4 is +2096640 and at m=8 is -536481792000
        (B599-ALG, exact Lagrange tables) — reproduced here by the
        degree-2 truncation, exactly;
  (iii) [CORRECTED after the first run — the original registered
        prediction FAILED and is preserved here permanently: it read
        "odd t^1 J-responses all zero AND even t^1 responses NOT all
        zero"; the even half was WRONG — a careless transfer from the
        P2-preflight TRACE functional, where even rows are generically
        nonzero. For the J-v0 functional the step-5 forced-zero
        criterion (<v_m u, u>_J forced 0 iff eps_m*c != -1, c = +1)
        FORCES the even-block zeros. Diagnosis: functional matters.]
        The corrected structural statement, now gated: the t^1
        J-responses vanish at ALL six blocks for all 20 words —
        FORCED at the even blocks, GENUINE (not forced, yet holding)
        at the odd blocks {4, 8}.
OUTPUT: the 20 x 6 matrices R1, R2 of exact t^1 / t^2 J-responses,
their ranks and kernels over Q(sqrt-3), and the equivariance report.

Run: OA_SLOW=1 python3 step4b_responses.py   (~1-2 h, pure exact K)
"""
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'B575_bridge_obstruction',
                        'l51_obstruction.py')).read()
ns = {'__name__': 'l51mod'}
sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K = ns['K']; K0 = ns['K0']; K1 = ns['K1']
mmul = ns['mmul']; madd = ns['madd']; mscale = ns['mscale']; meye = ns['meye']
msub = ns['msub']; nullspace = ns['nullspace']; rref = ns['rref']
A27 = ns['A27']; B27 = ns['B27']; A27i = ns['A27i']; B27i = ns['B27i']
BLOCKS = ns['BLOCKS']
LONGITUDE = "abABaaBAbA"

kc = lambda x: K(x.a, -x.b)


def mconj(M):
    return [[kc(x) for x in r] for r in M]


def matvec(M, v):
    return [sum((M[i][j] * v[j] for j in range(27) if not v[j].is_zero()), K0)
            for i in range(27)]


def word27(word):
    L = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
    M = meye(27)
    for ch in word:
        M = mmul(M, L[ch])
    return M


# ---- J (step 5's intertwiner) and v0 (the lemma cell's vector), rebuilt ----
e_pr = ns['e_pr']; f_pr = ns['f_pr']; h_pr = ns['h_pr']
half = K(Fr(1, 2))
Om = madd(madd(mmul(e_pr, f_pr), mmul(f_pr, e_pr)),
          mscale(half, mmul(h_pr, h_pr)))
v0 = nullspace(Om)[0]

# J solves rho(X)^T J + J rho(theta X) = 0 on {e_pr, f_pr, v4}; rebuilt by
# the steps3and5 recipe: solve on the weight-reduced support (exact).
V4 = BLOCKS[4][0]

# the banked weight-reduced recipe (steps3and5.py): support = weight-opposite
hdiag = all(h_pr[i][j].is_zero() for i in range(27) for j in range(27) if i != j)
assert hdiag, "h_pr not diagonal"
wts = [h_pr[i][i] for i in range(27)]
pairs_idx = [(i, j) for i in range(27) for j in range(27)
             if (wts[i] + wts[j]).is_zero()]
idx_of = {p: k for k, p in enumerate(pairs_idx)}
nunk = len(pairs_idx)


def add_equations(X, sign, rows_):
    for i in range(27):
        for j in range(27):
            row = [K0] * nunk
            any_nz = False
            for k in range(27):
                if not X[k][i].is_zero() and (k, j) in idx_of:
                    row[idx_of[(k, j)]] = row[idx_of[(k, j)]] + X[k][i]
                    any_nz = True
                if not X[k][j].is_zero() and (i, k) in idx_of:
                    row[idx_of[(i, k)]] = row[idx_of[(i, k)]] + (K(sign) * X[k][j])
                    any_nz = True
            if any_nz:
                rows_.append(row)


rows = []
add_equations(e_pr, 1, rows)
add_equations(f_pr, 1, rows)
add_equations(V4, -1, rows)
Js = nullspace(rows)
assert len(Js) == 1, f"J Schur gate: dim {len(Js)} != 1"
J = [[K0] * 27 for _ in range(27)]
for k, (i, j) in enumerate(pairs_idx):
    J[i][j] = Js[0][k]
sym = all((J[i][j] - J[j][i]).is_zero() for i in range(27) for j in range(27))
assert sym, "J not symmetric"
print("J rebuilt: Schur-unique, symmetric", flush=True)


def jpair(u, w):
    Ju = matvec(J, w)
    return sum((u[i] * Ju[i] for i in range(27) if not u[i].is_zero()), K0)


# ---- degree-2 truncated matrices: triples (M0, M1, M2) ----------------------
def tmul(X, Y):
    return (mmul(X[0], Y[0]),
            madd(mmul(X[0], Y[1]), mmul(X[1], Y[0])),
            madd(madd(mmul(X[0], Y[2]), mmul(X[1], Y[1])), mmul(X[2], Y[0])))


ZERO = [[K0] * 27 for _ in range(27)]


def const(M):
    return (M, ZERO, ZERO)


# ---- the frozen R4 word list (B599; two-copy weld language) -----------------
WORDS = ["a1", "b1", "a2", "b2", "a1b1", "a2b2", "a1b2", "a2b1", "a1a2",
         "b1b2", "a1b1a2b2", "a2b2a1b1", "a1b2a2b1", "a1b1A1B1", "a1b2A1B2",
         "a1a2b1b2", "b1a2b2a1", "a1b1a1", "a1b1b2", "a2b1b2"]


def parse(word):
    toks = []
    i = 0
    while i < len(word):
        toks.append(word[i:i + 2])
        i += 2
    return toks


EPS = {1: 1, 4: -1, 5: 1, 7: 1, 8: -1, 11: 1}
MU27 = A27
LAM27 = word27(LONGITUDE)
LAM27i = word27(LONGITUDE[::-1].swapcase())

R1 = {}
R2 = {}
R2raw = {}
allok = True
for m in sorted(BLOCKS):
    v = BLOCKS[m][0]
    # gate (i): peripheral fixedness of the bending direction
    fmu = msub(mmul(MU27, mmul(v, A27i)), v)
    flam = msub(mmul(LAM27, mmul(v, LAM27i)), v)
    gfix = all(all(x.is_zero() for x in r) for r in fmu) and \
           all(all(x.is_zero() for x in r) for r in flam)
    print(f"block m={m}: bending direction peripherally fixed: {gfix}",
          flush=True)
    allok &= gfix

    # c = exp(t v) truncated: I + t v + t^2 v^2/2 ; c^{-1} likewise with -t
    v2h = mscale(half, mmul(v, v))
    c = (meye(27), v, v2h)
    ci = (meye(27), mscale(K(-1), v), v2h)
    Bbar = mconj(B27); Bbari = mconj(B27i)
    y = tmul(tmul(c, const(Bbar)), ci)
    Y = tmul(tmul(c, const(Bbari)), ci)
    LM = {'a1': const(A27), 'b1': const(B27), 'A1': const(A27i),
          'B1': const(B27i), 'a2': const(A27), 'b2': y,
          'A2': const(A27i), 'B2': Y}

    r1v = []
    r2v = []
    Mb2 = None
    for w in WORDS:
        M = (meye(27), ZERO, ZERO)
        for tok in parse(w):
            M = tmul(M, LM[tok])
        if w == "b2":
            Mb2 = M
        u1 = matvec(M[1], v0)
        u2 = matvec(M[2], v0)
        r1v.append(jpair(v0, u1))
        r2v.append(jpair(v0, u2))
    R1[m] = r1v
    R2[m] = r2v
    # gate (ii) data: r4b's slot <exp(tv) v0, rho_t(b2) v0>_dot, t^2 coeff
    cu1 = matvec(v, v0)
    cu2 = matvec(v2h, v0)
    pdot = lambda x, z: sum((x[i] * z[i] for i in range(27)
                             if not x[i].is_zero()), K0)
    slot_t2 = (pdot(v0, matvec(Mb2[2], v0)) + pdot(cu1, matvec(Mb2[1], v0)) +
               pdot(cu2, matvec(Mb2[0], v0)))
    R2raw[m] = slot_t2
    print(f"  responses done ({len(WORDS)} words)", flush=True)

# gate (ii): the banked Im-witnesses at word b2 (r4b's slot, Lagrange-exact)
w4 = R2raw[4]
w8 = R2raw[8]
g4 = w4.b == Fr(2096640)
g8 = w8.b == Fr(-536481792000)
print(f"witness m=4/b2 slot t^2 Im = {w4.b} (banked +2096640): {g4}",
      flush=True)
print(f"witness m=8/b2 slot t^2 Im = {w8.b} (banked -536481792000): {g8}",
      flush=True)
allok &= g4 and g8

# gate (iii, corrected): t^1 J-responses vanish at ALL blocks
for m in sorted(BLOCKS):
    z = all(x.is_zero() for x in R1[m])
    tag = "GENUINE" if EPS[m] < 0 else "forced"
    print(f"parity m={m} ({tag} zero): all t^1 J-responses zero: {z}",
          flush=True)
    allok &= z

# ranks and kernels of R1, R2 (20 x 6 over K)
def matrix_rank(rows_):
    live = [list(r) for r in rows_ if any(not x.is_zero() for x in r)]
    if not live:
        return 0
    _, piv = rref(live)
    return len(piv)


cols = sorted(BLOCKS)
M1 = [[R1[m][i] for m in cols] for i in range(len(WORDS))]
M2 = [[R2[m][i] for m in cols] for i in range(len(WORDS))]
rk1 = matrix_rank(M1)
rk2 = matrix_rank(M2)
ker2 = nullspace(M2)
print(f"rank R1 = {rk1};  rank R2 = {rk2};  dim ker R2 = {len(ker2)} "
      f"(blocks {cols})", flush=True)
for kv in ker2:
    print("  ker R2 vector:", [f"({x.a},{x.b})" for x in kv], flush=True)

# the polarization quotient (slot 7): R2 modulo the span of R1 columns
# columns live in K^20: quotient rank = rank([R1cols | R2cols]) - rank(R1cols)
c1 = [[M1[i][j] for i in range(len(WORDS))] for j in range(6)]
c2 = [[M2[i][j] for i in range(len(WORDS))] for j in range(6)]
rq = matrix_rank(c1 + c2) - matrix_rank(c1)
print(f"polarization quotient: rank(R2 mod span R1) = {rq}", flush=True)

# the map's classical content: the two theta-odd R2 columns, exact
def fmtk(x):
    if x.is_zero():
        return "0"
    return f"({x.a}{'+' if x.b >= 0 else ''}{x.b}w)"


for m in (4, 8):
    print(f"R2 column m={m} (the hearing line, exact):", flush=True)
    for w, val in zip(WORDS, R2[m]):
        print(f"    {w:10s} {fmtk(val)}", flush=True)
gsupp = all(all(x.is_zero() for x in R2[m]) for m in (1, 5, 7, 11))
print(f"R2 supported on the theta-odd blocks only: {gsupp}", flush=True)
allok &= gsupp

assert allok, "STEP 4b FAILED"
print("STEP 4b DONE", flush=True)
