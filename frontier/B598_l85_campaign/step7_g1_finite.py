"""B598 step 7 — G1-FINITE: the dial-map closure, in-repo, certified
longitude, finite t (failure-enforcing).

Closes the B582 provenance hole: the original G1 dial-map code was never
committed (caught in the item-6 adjudication); until now all mirror-double
existence claims were formal. This script re-derives the closure with
committed code:

  THE AMALGAM (the banked weld frame, finite t = 1): copy 1 contributes
  log rho(a) = e_pr and log rho(b) = omega f_pr; copy 2 (the mirror,
  K-conjugated) contributes log y = Ad(c) (omega-bar f_pr-bar) with
  c = exp(v_m), v_m the block-m top vector (the dial slot).

  GATES:
  (i)   the dial slots are peripheral: Ad(rho(mu)) v_m = v_m and
        Ad(rho(lambda)) v_m = v_m with the CERTIFIED longitude
        'abABaaBAbA' — exact, all six slots;
  (ii)  the SUBSET face: every generator (all dials) lies in the exact
        K-span of the 78 BLOCKS matrices  =>  every closure stays in e6;
  (iii) the RANK face: the bracket closure of the theta-odd dials
        m in {4, 8} reaches dim 78 mod p at TWO primes p == 1 (mod 3)
        (rank mod p <= rank over the field <= 78, so 78 mod p is an
        exact certificate of equality);
  (iv)  the dial map: closure dims reported for no-twist and all six
        slots (both primes must agree).

VERDICT on green: the theta-odd-twisted amalgam's algebra IS e6(C), dim
78, at finite t — B582's existence chain re-derived with committed code.

Run: OA_SLOW=1 python3 step7_g1_finite.py   (~20-30 min)
"""
import os
import sys
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'B575_bridge_obstruction',
                        'l51_obstruction.py')).read()
ns = {'__name__': 'l51mod'}
sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K = ns['K']; K0 = ns['K0']; K1 = ns['K1']
mmul = ns['mmul']; msub = ns['msub']; mscale = ns['mscale']; meye = ns['meye']
mexp_nil = ns['mexp_nil']
A27 = ns['A27']; B27 = ns['B27']; A27i = ns['A27i']; B27i = ns['B27i']
BLOCKS = ns['BLOCKS']
e_pr = ns['e_pr']; f_pr = ns['f_pr']
OMEGA = ns['OMEGA']
LONGITUDE = "abABaaBAbA"

kc = lambda x: K(x.a, -x.b)


def mconj(M):
    return [[kc(x) for x in r] for r in M]


def word27(word):
    L = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
    M = meye(27)
    for ch in word:
        M = mmul(M, L[ch])
    return M


LAM27 = word27(LONGITUDE)
LAM27i = word27(LONGITUDE[::-1].swapcase())

allok = True

# ---- gate (i): the dial slots are peripheral (certified longitude) ---------
print("gate (i): peripheral fixedness of the six dial slots:", flush=True)
for m in sorted(BLOCKS):
    v = BLOCKS[m][0]
    fmu = msub(mmul(A27, mmul(v, A27i)), v)
    flam = msub(mmul(LAM27, mmul(v, LAM27i)), v)
    g = all(all(x.is_zero() for x in r) for r in fmu) and \
        all(all(x.is_zero() for x in r) for r in flam)
    print(f"  slot m={m:2d}: fixed by (mu, lambda): {g}", flush=True)
    allok &= g

# ---- the generators per dial ------------------------------------------------
OMEGAbar = kc(OMEGA)
fbar = mconj(f_pr)
log_b1 = mscale(OMEGA, f_pr)


def dial_generators(m):
    if m is None:
        return [e_pr, log_b1, mscale(OMEGAbar, fbar)]
    v = BLOCKS[m][0]
    c = mexp_nil(v)
    ci = mexp_nil(mscale(K(-1), v))
    logy = mmul(c, mmul(mscale(OMEGAbar, fbar), ci))
    return [e_pr, log_b1, logy]


# ---- gate (ii): the SUBSET face (exact membership in the e6 span) ----------
def flat(M):
    return [M[i][j] for i in range(27) for j in range(27)]


basis_rows = [flat(X) for m in sorted(BLOCKS) for X in BLOCKS[m]]
assert len(basis_rows) == 78
# row-reduce the 78 basis rows once (exact), keeping the reduced rows
reduced = []          # list of (pivot_col, row)
for r in basis_rows:
    row = list(r)
    for pc, pr in reduced:
        if not row[pc].is_zero():
            f = row[pc]
            row = [x - f * y for x, y in zip(row, pr)]
    piv = next((k for k, x in enumerate(row) if not x.is_zero()), None)
    assert piv is not None, "e6 basis degenerate"
    inv = row[piv].inv()
    row = [x * inv for x in row]
    reduced.append((piv, row))
reduced.sort()


def in_e6(M):
    row = flat(M)
    for pc, pr in reduced:
        if not row[pc].is_zero():
            f = row[pc]
            row = [x - f * y for x, y in zip(row, pr)]
    return all(x.is_zero() for x in row)


print("gate (ii): generator membership in the exact e6 span:", flush=True)
for label, m in [("no-twist", None)] + [(f"slot {m}", m) for m in sorted(BLOCKS)]:
    gens = dial_generators(m)
    memb = [in_e6(G) for G in gens]
    print(f"  {label}: membership {memb}", flush=True)
    allok &= all(memb)

# ---- gates (iii)+(iv): mod-p bracket closure dims ---------------------------
PRIMES = [10009, 10039]                       # both == 1 (mod 3)


def sqrt_m3(p):
    for s in range(1, p):
        if (s * s + 3) % p == 0:
            return s
    raise ValueError(p)


def to_fp(M, p, s):
    out = np.zeros((27, 27), dtype=np.int64)
    for i in range(27):
        for j in range(27):
            x = M[i][j]
            if x.is_zero():
                continue
            a, b = Fr(x.a), Fr(x.b)
            va = (a.numerator * pow(a.denominator, -1, p)) % p
            vb = (b.numerator * pow(b.denominator, -1, p)) % p
            out[i, j] = (va + vb * s) % p
    return out


def closure_dim(gens_fp, p):
    rows = np.zeros((0, 729), dtype=np.int64)   # rref rows mod p
    pivs = []
    basis = []

    def add(M):
        nonlocal rows, pivs
        v = M.reshape(729) % p
        for r, pc in zip(rows, pivs):
            if v[pc]:
                v = (v - v[pc] * r) % p
        nz = np.nonzero(v)[0]
        if len(nz) == 0:
            return False
        pc = int(nz[0])
        v = (v * pow(int(v[pc]), -1, p)) % p
        rows = np.vstack([rows, v])
        pivs.append(pc)
        basis.append(M % p)
        return True

    queue = []
    for G in gens_fp:
        if add(G):
            queue.append(G % p)
    while queue and len(basis) < 300:
        X = queue.pop()
        for Y in list(basis):
            Z = (X @ Y - Y @ X) % p
            if add(Z):
                queue.append(Z)
    return len(basis)


print("gates (iii)+(iv): the dial map (mod-p closure dims):", flush=True)
dials = [("no-twist", None)] + [(f"slot {m}", m) for m in sorted(BLOCKS)]
dimtab = {}
for label, m in dials:
    gens = dial_generators(m)
    dims = []
    for p in PRIMES:
        s = sqrt_m3(p)
        dims.append(closure_dim([to_fp(G, p, s) for G in gens], p))
    agree = dims[0] == dims[1]
    dimtab[label] = dims[0]
    print(f"  {label}: closure dim = {dims[0]} / {dims[1]} "
          f"(primes agree: {agree})", flush=True)
    allok &= agree

g78 = dimtab["slot 4"] == 78 and dimtab["slot 8"] == 78
print(f"theta-odd dials reach 78 (= e6): {g78}", flush=True)
allok &= g78

assert allok, "STEP 7 FAILED"
print("STEP 7 (G1-FINITE) DONE: the theta-odd-twisted amalgam's algebra is "
      "e6(C) at finite t, certified longitude, committed code.", flush=True)
