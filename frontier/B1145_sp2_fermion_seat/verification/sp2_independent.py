#!/usr/bin/env python3
"""
SP-2 INDEPENDENT VERIFICATION (own code).

Reuses ONLY banked machinery on the main lineage:
  frontier/B1102_exact_hypercharge_solve/b1102_common.py   (load_ccb + build_27)
  frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py  (the e6 Chevalley bracket)
Imports NOTHING from any golden_gate remote/branch or any session_handoff/ path.

Convention adaptation (declared, and internally consistent):
  The banked e6 module is defined ENTIRELY over Q (Fraction); its structure constants
  (Frenkel-Kac eps cocycle) are +-1 in Q, so rho27(X) is a rational matrix for any
  rational Lie-algebra vector X. The field Q(sqrt-3) enters ONLY through the beat
  construction (the scalar q in exp(q F), exp(q E), U=exp(q E)) and through gal = complex
  conjugation on Q(sqrt-3). Because every e6/27 matrix here is rational, gal fixes them
  and acts only on the introduced q -- exactly the "internally consistent" adaptation the
  task allows. gal is the matching conjugation (q -> q_bar = 1 - q); the closure result is
  convention-independent.

Field Q(sqrt-3): q = e^{i pi/3}, q^2 - q + 1 = 0 => q^2 = q - 1. Element a + b q stored as
(a, b) with exact Fractions. gal((a,b)) = (a+b, -b) [= a + b(1-q)]. All checks EXACT.
"""
import os, sys, importlib.util
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))  # verification/ -> B1145 -> frontier -> repo
BASE = os.path.join(_REPO, "frontier", "B1102_exact_hypercharge_solve")
# Pin the CCB module to the in-tree vendored file (hermetic; never a handoff/cloud path).
os.environ["B1102_CCB_PATH"] = os.path.join(BASE, "e6_bracket_vendored.py")

_spec = importlib.util.spec_from_file_location("b1102_common", os.path.join(BASE, "b1102_common.py"))
_c2 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_c2)
ccb = _c2.load_ccb()
weights, WIDX, rho27 = _c2.build_27(ccb)

N, DIM, ROOTS, IDX = ccb.N, ccb.DIM, ccb.ROOTS, ccb.IDX
evec, br = ccb.evec, ccb.br

report = {}

# ----------------------------------------------------------------- 1. dim e6 + rep sanity
assert DIM == 78, DIM
report["dim_e6"] = DIM

# module's own certification that rho27 is a Lie-algebra rep (exact, all C(78,2) pairs).
ok_rep, npairs, fails = _c2.verify_27_is_a_rep(ccb, rho27, full=True)
report["rho27_is_rep_all_pairs"] = (ok_rep, npairs, fails)
assert ok_rep, ("rho27 failed the module's own Chevalley-bracket certification", fails)

# ----------------------------------------------------------------- 2. A1 minimal nilpotent triple
r0 = ROOTS[0]
mr0 = tuple(-x for x in r0)
assert mr0 in IDX, "-r0 not a root?!"
e = evec(r0)
h = [F(0)] * DIM
for k in range(N):
    h[k] = F(r0[k])                 # coroot: h[k] = r0[k] in simple-root/coroot basis
f = [-c for c in evec(mr0)]         # f = -e_{-r0}

def veq(u, v):  # exact vector equality
    return all(a == b for a, b in zip(u, v))

he_ok = veq(br(h, e), [F(2) * c for c in e])
hf_ok = veq(br(h, f), [F(-2) * c for c in f])
ef_ok = veq(br(e, f), h)
report["triple_[h,e]=2e"] = he_ok
report["triple_[h,f]=-2f"] = hf_ok
report["triple_[e,f]=h"] = ef_ok
assert he_ok and hf_ok and ef_ok, "A1 triple relations failed"

# ----------------------------------------------------------------- 3. the 27-rep matrices + weights
E27 = rho27(e)      # rational (Fraction) 27x27 lists
H27 = rho27(h)
F27 = rho27(f)

# H27 must be diagonal; its diagonal is the multiset of sl2-weights on the 27.
offdiag_nonzero = sum(1 for i in range(27) for j in range(27) if i != j and H27[i][j] != 0)
assert offdiag_nonzero == 0, ("H27 not diagonal", offdiag_nonzero)
wmult = {}
for i in range(27):
    w = H27[i][i]
    assert w.denominator == 1, ("non-integer weight", w)
    wi = int(w)
    wmult[wi] = wmult.get(wi, 0) + 1
report["weight27_multiset"] = dict(sorted(wmult.items()))
odd = any(k % 2 != 0 for k in wmult)
report["stratum_is_ODD"] = odd
# The task's gate: must be {-1:6, 0:15, +1:6} (ODD). STOP if not.
if wmult != {-1: 6, 0: 15, 1: 6}:
    print("STOP: weight multiset is", dict(sorted(wmult.items())), "-- not the odd A1 stratum {-1:6,0:15,+1:6}")
    print("REPORT:", report)
    sys.exit(3)

# =================================================================== FIELD Q(sqrt-3) LAYER
# element (a,b) = a + b*q ; q^2 = q - 1
FZ = (F(0), F(0)); FI = (F(1), F(0)); Q = (F(0), F(1))
def fadd(x, y): return (x[0] + y[0], x[1] + y[1])
def fsub(x, y): return (x[0] - y[0], x[1] - y[1])
def fneg(x):    return (-x[0], -x[1])
def fmul(x, y):
    a, b = x; c, d = y
    return (a*c - b*d, a*d + b*c + b*d)      # (a+bq)(c+dq), q^2=q-1
def fgal(x):    return (x[0] + x[1], -x[1])  # complex conjugation q -> 1-q
def femb(r):    return (F(r), F(0))          # rational -> field
def fdivint(x, k): return (x[0] / k, x[1] / k)

def M_emb(Mrat):
    return [[femb(Mrat[i][j]) for j in range(27)] for i in range(27)]
def M_ident():
    return [[FI if i == j else FZ for j in range(27)] for i in range(27)]
def M_zero():
    return [[FZ] * 27 for _ in range(27)]
def M_add(A, B):
    return [[fadd(A[i][j], B[i][j]) for j in range(27)] for i in range(27)]
def M_scal(s, A):                             # field scalar s times matrix A
    return [[fmul(s, A[i][j]) for j in range(27)] for i in range(27)]
def M_scal_int_div(A, k):
    return [[fdivint(A[i][j], k) for j in range(27)] for i in range(27)]
def M_mul(A, B):
    C = [[FZ] * 27 for _ in range(27)]
    for i in range(27):
        Ai = A[i]; Ci = C[i]
        for t in range(27):
            a = Ai[t]
            if a == FZ:
                continue
            Bt = B[t]
            for j in range(27):
                b = Bt[j]
                if b != FZ:
                    Ci[j] = fadd(Ci[j], fmul(a, b))
    return C
def M_gal(A):
    return [[fgal(A[i][j]) for j in range(27)] for i in range(27)]
def M_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(27) for j in range(27))
def M_is_zero(A):
    return all(A[i][j] == FZ for i in range(27) for j in range(27))
def M_diff_stats(A, B):
    """residual report if not equal: count of differing entries + max |entry| as float."""
    import cmath
    ndiff = 0; mx = 0.0
    for i in range(27):
        for j in range(27):
            d = fsub(A[i][j], B[i][j])
            if d != FZ:
                ndiff += 1
                # |a + b q|, q = e^{i pi/3}
                a = float(d[0]); b = float(d[1])
                val = a + b * cmath.exp(1j * cmath.pi / 3)
                mx = max(mx, abs(val))
    return ndiff, mx

def matexp_nilpotent(Mfield, name=""):
    """exp(M) for nilpotent M over the field, as an EXACT finite sum I + M + M^2/2! + ...
    Terminates when a power vanishes; raises if it does not (not nilpotent)."""
    acc = M_ident()
    term = M_ident()            # M^0 / 0!
    k = 0
    while True:
        k += 1
        term = M_scal_int_div(M_mul(term, Mfield), k)   # term = (prev) * M / k = M^k/k!
        if M_is_zero(term):
            break
        acc = M_add(acc, term)
        if k > 60:
            raise RuntimeError(f"{name}: argument not nilpotent (no vanishing power by k=60)")
    return acc, k - 1   # k-1 = nilpotency degree (last nonzero power)

# lifts
E27f = M_emb(E27); F27f = M_emb(F27)
qE = M_scal(Q, E27f)
qF = M_scal(Q, F27f)

A27, degE = matexp_nilpotent(E27f, "E27")            # exp(E27)
B27, degF = matexp_nilpotent(qF, "qF27")             # exp(q F27)
U,   degU = matexp_nilpotent(qE, "qE27")             # U = exp(q E27)
report["nilpotency_degree_E27"] = degE
report["nilpotency_degree_F27"] = degF

# inverses via exp of the negated argument (exact); cross-checked against I below.
A27inv, _ = matexp_nilpotent(M_scal(fneg(FI), E27f), "-E27")
B27inv, _ = matexp_nilpotent(M_scal(fneg(Q),  F27f), "-qF27")
Uinv,   _ = matexp_nilpotent(M_scal(fneg(Q),  E27f), "-qE27")
report["inv_sanity_A"] = M_eq(M_mul(A27, A27inv), M_ident())
report["inv_sanity_B"] = M_eq(M_mul(B27, B27inv), M_ident())
report["inv_sanity_U"] = M_eq(M_mul(U,   Uinv),   M_ident())
assert report["inv_sanity_A"] and report["inv_sanity_B"] and report["inv_sanity_U"]

# ----------------------------------------------------------------- 4. the m004 relator word
# word "a bABa B AbaB" ; a=A27, A=A27inv, b=B27, B=B27inv (read left->right, product in order)
LET = {"a": A27, "A": A27inv, "b": B27, "B": B27inv}
word = [ch for ch in "a bABa B AbaB" if ch in LET]
assert word == list("abABaBAbaB"), word
Wm = M_ident()
for ch in word:
    Wm = M_mul(Wm, LET[ch])
relator_is_identity = M_eq(Wm, M_ident())
report["relator_word"] = "".join(word)
report["relator_is_identity"] = relator_is_identity
if not relator_is_identity:
    report["relator_residual"] = M_diff_stats(Wm, M_ident())

# ----------------------------------------------------------------- 5. oddness operator C
C = [[FZ] * 27 for _ in range(27)]
for i in range(27):
    w = int(H27[i][i])
    C[i][i] = FI if (w % 2 == 0) else fneg(FI)   # (-1)^weight ; weight in {-1,0,1}
C_neq_I = not M_eq(C, M_ident())
C_sq_I  = M_eq(M_mul(C, C), M_ident())
C_comm_A = M_eq(M_mul(C, A27), M_mul(A27, C))
C_comm_B = M_eq(M_mul(C, B27), M_mul(B27, C))
report["C_neq_I"] = C_neq_I
report["C_sq_eq_I"] = C_sq_I
report["C_commutes_A27"] = C_comm_A
report["C_commutes_B27"] = C_comm_B

# ----------------------------------------------------------------- 6. THE HINGE: beat Omega
def Omega(M):
    return M_mul(M_mul(U, M_gal(M)), Uinv)       # U . gal(M) . U^{-1}

# (a) Omega^2 = A27  <=>  U . gal(U) = A27
UgalU = M_mul(U, M_gal(U))
hinge_a = M_eq(UgalU, A27)
report["hinge_a_(U.gal(U)=A27)"] = hinge_a
if not hinge_a:
    report["hinge_a_residual"] = M_diff_stats(UgalU, A27)

# (b) Omega(A27) = A27
OmA = Omega(A27)
hinge_b = M_eq(OmA, A27)
report["hinge_b_(Omega(A27)=A27)"] = hinge_b
if not hinge_b:
    report["hinge_b_residual"] = M_diff_stats(OmA, A27)

# (c) Omega(B27) = rho27(w(B)),  w(B) = B^{-1} A B A^{-1} B  (letters B27inv,A27,B27,A27inv,B27)
OmB = Omega(B27)
wB = M_ident()
for Mx in (B27inv, A27, B27, A27inv, B27):
    wB = M_mul(wB, Mx)
hinge_c = M_eq(OmB, wB)
report["hinge_c_(Omega(B27)=B'ABA'B)"] = hinge_c
if not hinge_c:
    report["hinge_c_residual"] = M_diff_stats(OmB, wB)

# ----------------------------------------------------------------- VERDICT
all_exact = (relator_is_identity and C_neq_I and C_sq_I and C_comm_A and C_comm_B
             and hinge_a and hinge_b and hinge_c)
if all_exact:
    verdict = "SP-2 GREEN"
else:
    failed = []
    if not relator_is_identity: failed.append("relator!=I")
    if not C_neq_I: failed.append("C=I")
    if not C_sq_I: failed.append("C^2!=I")
    if not C_comm_A: failed.append("[C,A27]!=0")
    if not C_comm_B: failed.append("[C,B27]!=0")
    if not hinge_a: failed.append("hinge(a)")
    if not hinge_b: failed.append("hinge(b)")
    if not hinge_c: failed.append("hinge(c)")
    verdict = "SP-2 RED  (failed: " + ", ".join(failed) + ")"
report["VERDICT"] = verdict

print("=" * 72)
print("SP-2 INDEPENDENT VERIFICATION -- results")
print("=" * 72)
for k, v in report.items():
    print(f"{k:32s} : {v}")
print("=" * 72)
print("VERDICT:", verdict)
