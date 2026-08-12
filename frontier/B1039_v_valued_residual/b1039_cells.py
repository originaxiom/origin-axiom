"""B1039 -- THE V-VALUED RESIDUAL (sealed 874d9eee pre-compute).

Reuses B632 cell 2's ENTIRE banked machinery by exec (the cubic CFULL, C3, the corrected
cup_covector, the two H^2 coker functionals phis) -- nothing rebuilt. Adds: the double's
five classes (double-Fox on the full 27), the per-side functional-read tables (W2), the
MV difference assembly with its gauge control (W1/W3), the two sealed verdicts (W4).

Discipline: functional-read ONLY (klass), never raw; banked-number gates before any
pairing is read; sum(..., K0) throughout."""
import io
import os
import time
import contextlib

HERE = os.path.dirname(os.path.abspath(__file__))
CELL2 = os.path.join(HERE, "..", "B632_cubic_route", "cell2_texture.py")

ns = {"__name__": "b632_cell2", "__file__": CELL2}
t0 = time.time()
print("exec B632 cell2 (the full banked machinery)...", flush=True)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(compile(open(CELL2).read(), CELL2, "exec"), ns)
print(f"cell2 machinery loaded in {time.time()-t0:.1f}s "
      f"(its own output captured, {len(buf.getvalue())} chars)", flush=True)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
apply_ = ns["apply"]
C3, dot = ns["C3"], ns["dot"]
cup_covector = ns["cup_covector"]
phis = ns["phis"]
klass = ns["klass"]
REL = ns["REL"]
nullspace = ns["nullspace"]
rref = ns["ns"]["rref"]   # B575's, nested inside cell2's own ns


def meye(k):
    return [[K1 if i == j else K0 for j in range(k)] for i in range(k)]


def mzero(r, c):
    return [[K0] * c for _ in range(r)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(c, A):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mmul(A, B):
    m, k, c = len(A), len(B), len(B[0])
    out = [[K0] * c for _ in range(m)]
    for i in range(m):
        Ai = A[i]
        for t in range(k):
            a = Ai[t]
            if a.is_zero():
                continue
            Bt = B[t]
            oi = out[i]
            for j in range(c):
                if not Bt[j].is_zero():
                    oi[j] = oi[j] + a * Bt[j]
    return out


def mzero_p(A):
    return all(x.is_zero() for row in A for x in row)

LONG = "abABaaBAbA"
GENS = "abd"
def inv_word(w): return w[::-1].swapcase()
R1, R2 = REL, REL.replace('b', 'd').replace('B', 'D')
R3 = LONG + inv_word(LONG.replace('b', 'd').replace('B', 'D'))
RELS = [R1, R2, R3]
n = 27


def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


# ---- the double's five classes (full-27 double-Fox; banked-number gate: h1 = 5) ------
print("\n[double-Fox on the full 27]...", flush=True)
lets3 = {'a': A27, 'A': A27i, 'b': B27, 'B': B27i, 'd': B27, 'D': B27i}
rows_all = []
for w in RELS:
    L = {g: mzero(n, n) for g in GENS}
    Pi = meye(n)
    for ch in w:
        low = ch.lower()
        if ch.isupper():
            term = mscale(K(-1), mmul(Pi, lets3[ch]))
        else:
            term = mmul(Pi, meye(n))
        L[low] = madd(L[low], term)
        Pi = mmul(Pi, lets3[ch])
    assert mzero_p(msub(Pi, meye(n)))
    rows_all += [[L['a'][i][j] for j in range(n)] +
                 [L['b'][i][j] for j in range(n)] +
                 [L['d'][i][j] for j in range(n)] for i in range(n)]
Z1d = nullspace(rows_all)
Bgend = []
for j in range(n):
    v = [K1 if t == j else K0 for t in range(n)]
    Bgend.append([x - v[i] for i, x in enumerate(mat_vec(A27, v))] +
                 [x - v[i] for i, x in enumerate(mat_vec(B27, v))] +
                 [x - v[i] for i, x in enumerate(mat_vec(B27, v))])
_, pivB = rref([r[:] for r in Bgend])
h1d = len(Z1d) - len(pivB)
print(f"  h1(dbl; 27) = {h1d}", flush=True)
assert h1d == 5, "banked-number gate: the double's 5 must reproduce"

base = [list(r) for r in Bgend]
cur = len(rref([r[:] for r in base])[1])
reps = []
for z in Z1d:
    nr = len(rref([r[:] for r in (base + [list(z)])])[1])
    if nr > cur:
        reps.append(list(z)); base.append(list(z)); cur = nr
    if len(reps) == 5:
        break
assert len(reps) == 5

# classify each rep: per-side restriction a coboundary? (seam-born vs glued)
Bgen_side = []
for j in range(n):
    v = [K1 if t == j else K0 for t in range(n)]
    Bgen_side.append([x - v[i] for i, x in enumerate(mat_vec(A27, v))] +
                     [x - v[i] for i, x in enumerate(mat_vec(B27, v))])
_, pivS = rref([r[:] for r in Bgen_side])
rankS = len(pivS)


def side_class_nontrivial(zpair):
    _, piv2 = rref([r[:] for r in (Bgen_side + [list(zpair)])])
    return len(piv2) > rankS


kinds = []
for z in reps:
    zM = list(z[:n]) + list(z[n:2*n])
    zMb = list(z[:n]) + list(z[2*n:])
    kinds.append(("glued" if (side_class_nontrivial(zM) or side_class_nontrivial(zMb))
                  else "seam-born"))
print(f"  class kinds: {kinds}", flush=True)

# ---- W1: the functional-read coboundary control (halting) ----------------------------
print("\n[W1] functional-read coboundary control:", flush=True)
zM0 = list(reps[0][:n]) + list(reps[0][n:2*n])
db = Bgen_side[0]
pert = [zM0[i] + db[i] for i in range(2 * n)]
c_base = klass(cup_covector(zM0, zM0))
c_pert = klass(cup_covector(pert, pert))
gate = all((c_base[i] - c_pert[i]).is_zero() for i in range(len(c_base)))
print(f"  klass invariant under z -> z + db: {'PASS' if gate else 'FAIL'}", flush=True)
assert gate, "W1 CONTROL FAILED -- HALT (sealed clause)"

# ---- W2/W3: per-side symmetric tables + the MV difference ----------------------------
print("\n[W2/W3] the symmetric pairing, functional-read, both sides + the difference:",
      flush=True)


def sym_klass(zpair, wpair):
    a = klass(cup_covector(zpair, wpair))
    b = klass(cup_covector(wpair, zpair))
    return tuple(a[i] + b[i] for i in range(len(a)))


table = {}
present_dbl = []
for i in range(5):
    for j in range(i, 5):
        zi, zj = reps[i], reps[j]
        ziM = list(zi[:n]) + list(zi[n:2*n]); zjM = list(zj[:n]) + list(zj[n:2*n])
        ziB = list(zi[:n]) + list(zi[2*n:]);  zjB = list(zj[:n]) + list(zj[2*n:])
        sM = sym_klass(ziM, zjM)
        sB = sym_klass(ziB, zjB)
        diff = tuple(sM[t] - sB[t] for t in range(len(sM)))
        pres = any(not x.is_zero() for x in diff)
        table[(i, j)] = dict(M=sM, Mbar=sB, dbl_diff=diff, present=pres)
        if pres:
            present_dbl.append((i, j))
        print(f"  pair ({i},{j}) [{kinds[i]}x{kinds[j]}]: "
              f"M {'0' if all(x.is_zero() for x in sM) else 'NONZERO'} | "
              f"Mbar {'0' if all(x.is_zero() for x in sB) else 'NONZERO'} | "
              f"dbl {'PRESENT' if pres else 'absent'}", flush=True)

# ---- W4: the sealed verdicts ---------------------------------------------------------
print(f"\n[W4] EXISTENCE: {'YES -- support ' + str(present_dbl) if present_dbl else 'NO -- the support is EMPTY'}",
      flush=True)
if present_dbl:
    non_seam = [(i, j) for (i, j) in present_dbl
                if not (kinds[i] == 'seam-born' or kinds[j] == 'seam-born')]
    print(f"[W4] SEAM-LOCALITY: non-seam support pairs = {non_seam} "
          f"({'THE FORBID FIRES' if non_seam else 'all seam-attributable -- the forbid survives'})",
          flush=True)
else:
    print("[W4] SEAM-LOCALITY: conditional cell void (no support to classify)", flush=True)
print("\n==== B1039 compute done ====", flush=True)
