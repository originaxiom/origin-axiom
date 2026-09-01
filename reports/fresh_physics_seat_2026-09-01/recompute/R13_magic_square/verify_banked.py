"""R13 post-diff — verify the BANKED artifacts with my own checkers.

1. stage2c_tensor.pkl (their L(O,C') tensor): full exact Jacobi over all triples.
2. B854 e6_centralizer.py run byte-faithfully; its BB diffed against my re-implementation.
3. stage4c_phi.pkl (their phi): homomorphism check stage2c-tensor -> build on all 3003
   pairs, det, invertibility — using MY bracket evaluators only.
"""
from fractions import Fraction as F
import pickle, os, io, json, math, contextlib
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ARC = "/home/user/origin-axiom/frontier/B904_barton_sudbery"
NB = 78

# ---------- 1. their tensor ----------
RAW = pickle.load(open(os.path.join(ARC, "stage2c_tensor.pkl"), "rb"))
# keys "(p, q)" -> ? inspect value type
k0 = next(iter(RAW))
v0 = RAW[k0]
print("banked tensor value sample:", k0, type(v0), v0 if not hasattr(v0, '__len__') or len(str(v0)) < 200 else "...")

def parse_key(s):
    a, b = s.strip("()").split(",")
    return int(a), int(b)

# values: assume dict idx->Fraction or list; handle both
den = 1
entries = []
for ks, val in RAW.items():
    p, q = parse_key(ks)
    if isinstance(val, dict):
        it = val.items()
    else:
        it = enumerate(val)
    for k, c in it:
        c = F(c)
        if c != 0:
            entries.append((p, q, int(k), c))
            den = den * c.denominator // math.gcd(den, c.denominator)
print("their tensor: nonzero entries", len(entries), "common den", den)

CT = np.zeros((NB, NB, NB), dtype=np.int64)
for p, q, k, c in entries:
    iv = c * den
    assert iv.denominator == 1
    CT[p, q, k] += int(iv)
# antisymmetrize if only upper triangle stored
if np.array_equal(CT, -CT.transpose(1, 0, 2)):
    print("stored antisymmetrically already")
else:
    # assume upper-triangular storage
    CT2 = CT - CT.transpose(1, 0, 2)
    # but if some (q,p) also stored this would double; detect
    CT = CT2
    assert np.array_equal(CT, -CT.transpose(1, 0, 2))
    print("antisymmetrized from stored triangle")

mx = np.abs(CT).max()
print("max scaled entry:", mx, "bound", 78 * mx * mx)
T1 = np.einsum('bdc,ace->abde', CT, CT)
J = T1 + T1.transpose(1, 2, 0, 3) + T1.transpose(2, 0, 1, 3)
nzJ = J.any(axis=3)
badT = sum(1 for a in range(NB) for b in range(a+1, NB) for c in range(b+1, NB) if nzJ[a, b, c])
print("THEIR stage2c tensor, full Jacobi over 76,076 unordered triples: failures =", badT)

# ---------- 2. B854 byte-faithful run ----------
g = {"__file__": os.path.join("/home/user/origin-axiom/frontier/B854_centralizer_exact",
                              "e6_centralizer.py"), "__name__": "b854run"}
buf = io.StringIO()
src = open(g["__file__"]).read()
import tempfile, shutil
# run in a sandbox copy so its json.dump writes go to a scratch dir, not the arc dir
sand = os.path.join(HERE, "b854_sandbox")
os.makedirs(sand, exist_ok=True)
shutil.copy(g["__file__"], os.path.join(sand, "e6_centralizer.py"))
g["__file__"] = os.path.join(sand, "e6_centralizer.py")
with contextlib.redirect_stdout(buf):
    exec(compile(src, "b854", "exec"), g)
print("B854 run output (last lines):")
print("\n".join(buf.getvalue().splitlines()[-6:]))
BB = g["BB"]
CBLD = np.load(os.path.join(HERE, "build_C_int.npy"))
diff = 0
for p in range(NB):
    for q in range(NB):
        for k in range(NB):
            if F(BB[p][q][k]) != F(int(CBLD[p, q, k])):
                diff += 1
print("B854 BB vs my re-implemented build tensor: differing entries =", diff)

# ---------- 3. their phi ----------
PHIL = pickle.load(open(os.path.join(ARC, "stage4c_phi.pkl"), "rb"))
print("phi pickle: list of", len(PHIL), "rows; sample type:", type(PHIL[0]))
PH = sp.Matrix([[sp.Rational(F(x).numerator, F(x).denominator) for x in row] for row in PHIL])
print("phi det:", sp.det(PH), " (banked claim: -2/3)")

# homomorphism: phi([a,b]_their) = [phi a, phi b]_build for all 3003 pairs
PHc = [[PH[i, j] for j in range(NB)] for i in range(NB)]
PH_cols = [[PH[i, j] for i in range(NB)] for j in range(NB)]

def br_build(u, v):
    out = [sp.Integer(0)] * NB
    for p in range(NB):
        if u[p] == 0:
            continue
        for q in range(NB):
            if v[q] == 0:
                continue
            col = CBLD[p, q]
            cpq = u[p] * v[q]
            for k in range(NB):
                if col[k]:
                    out[k] += cpq * int(col[k])
    return out

# But WAIT: orientation — is phi their-BS -> build, or build -> their-BS? Test both.
def check(dirn):
    mism = 0
    for a in range(NB):
        for b in range(a + 1, NB):
            if dirn == "bs2build":
                lhs_raw = [sp.Rational(int(CT[a, b, k]), den) for k in range(NB)]
                lhs = [sum(PHc[i][j] * lhs_raw[j] for j in range(NB) if lhs_raw[j] != 0)
                       for i in range(NB)]
                rhs = br_build(PH_cols[a], PH_cols[b])
            else:
                # build -> bs: phi([a,b]_build) = [phi a, phi b]_their
                lhs_raw = [sp.Integer(int(CBLD[a, b, k])) for k in range(NB)]
                lhs = [sum(PHc[i][j] * lhs_raw[j] for j in range(NB) if lhs_raw[j] != 0)
                       for i in range(NB)]
                # [phi a, phi b]_their
                out = [sp.Integer(0)] * NB
                u, v = PH_cols[a], PH_cols[b]
                for p in range(NB):
                    if u[p] == 0:
                        continue
                    for q in range(NB):
                        if v[q] == 0:
                            continue
                        col = CT[p, q]
                        cpq = u[p] * v[q]
                        for k in range(NB):
                            if col[k]:
                                out[k] += cpq * sp.Rational(int(col[k]), den)
                rhs = out
            if lhs != rhs:
                mism += 1
    return mism

m1 = check("bs2build")
print("their phi as BS->build: mismatches on 3003 pairs =", m1)
if m1:
    m2 = check("build2bs")
    print("their phi as build->BS: mismatches on 3003 pairs =", m2)
else:
    m2 = None

json.dump(dict(their_tensor_jacobi_failures=int(badT), b854_bb_diff=int(diff),
               their_phi_det=str(sp.det(PH)), phi_bs2build_mismatches=int(m1),
               phi_build2bs_mismatches=(None if m2 is None else int(m2))),
          open(os.path.join(HERE, "banked_verify_result.json"), "w"), indent=1)
print("saved banked_verify_result.json")
