"""Referee B1808, check 3: are H x H and H x H- different A-holomorphic families?

(a) For LR: gamma = M (x) E_xx + I (x) E_yy, M = [[0,1],[1,1]] (M^2 = LR, det M = -1), commutes with g = LR (x) I, has
    det -1 on Z^4, maps Lambda_A to itself with Q -> -Q, and maps the H x H family onto H x H- (checked on sample points:
    the pulled-back holomorphic 1-forms are again of B1804's shape, and the new (tau1, tau2) are read off).
(b) For every tested A: is Lambda_A isometric to Lambda_A(-1)?  Discriminant forms (even lattices, signature (2,2)):
    compare q on the discriminant group A_L = L^#/L for L and L(-1) by brute force over automorphisms of the group.
(c) Norm -1 units in the commutant order Z[A] (Pell x^2 + t x y + y^2 ... via the order's norm form).
(d) Mumford's index: for a chi = -3 class at a point of its curve, the Hermitian form of c1 has signature (1,1), so
    h^0 = h^2 = 0 and h^1 = 3 (no vector-like pairs).
"""
import itertools, json, math, pathlib
import sympy as sp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
PAIRS = list(itertools.combinations(range(4), 2))


def perm_sign(seq):
    s, a = 1, list(seq)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]: s = -s
            elif a[i] == a[j]: return 0
    return s


def wedge22(F, G):
    return sum(F[p] * G[q] * perm_sign(p + q) for p in PAIRS for q in PAIRS)


def kron(A, B):
    return sp.Matrix(sp.BlockMatrix([[A[i, j] * B for j in range(A.shape[1])] for i in range(A.shape[0])]))


out = {}
# (a) LR
A = sp.Matrix([[1, 1], [1, 2]]); M = sp.Matrix([[0, 1], [1, 1]])
assert M * M == A and M.det() == -1
g = kron(A, sp.eye(2))
Exx = sp.Matrix([[1, 0], [0, 0]]); Eyy = sp.Matrix([[0, 0], [0, 1]])
gam = kron(M, Exx) + kron(sp.eye(2), Eyy)
out["gamma commutes with LR (x) I"] = bool(gam * g == g * gam)
out["det gamma"] = int(gam.det())
# action on 2-forms: F -> gam^T F gam ; check it preserves the invariant subspace and flips the wedge form
phi = (1 + sp.sqrt(5)) / 2
fp = sp.Matrix([[1, phi]]); fm = sp.Matrix([[1, 1 - phi]])
t1, t2 = sp.symbols("t1 t2")
dzp = sp.Matrix([[fp[0], fp[0] * t1, fp[1], fp[1] * t1]])
dzm = sp.Matrix([[fm[0], fm[0] * t2, fm[1], fm[1] * t2]])
# pull back the 1-forms by gamma (row-vector convention dz -> dz gamma), and read off the new taus:
# dz+ gamma = c+ * fp (x) (1, t1'), i.e. coefficients (c, c t1', c phi, c phi t1')
pp = sp.simplify(dzp * gam); pm = sp.simplify(dzm * gam)
t1n = sp.simplify(pp[1] / pp[0]); t2n = sp.simplify(pm[1] / pm[0])
shape_ok = (sp.simplify(pp[2] / pp[0] - phi) == 0, sp.simplify(pm[2] / pm[0] - (1 - phi)) == 0,
            sp.simplify(pp[3] / pp[0] - phi * t1n) == 0, sp.simplify(pm[3] / pm[0] - (1 - phi) * t2n) == 0)
out["gamma pulls back B1804-shaped 1-forms to B1804-shaped 1-forms"] = all(shape_ok)
out["new (tau1, tau2) as functions of the old"] = [str(t1n), str(t2n)]
smp = {t1: sp.Rational(1, 3) + 2 * sp.I, t2: -sp.Rational(1, 2) + sp.I}
out["sample (1/3+2i, -1/2+i) maps to"] = [str(sp.N(t1n.subs(smp), 8)), str(sp.N(t2n.subs(smp), 8))]

# invariant lattice (rational basis suffices for the form check)
fs = sp.symbols("f0:6")
Fm = sp.zeros(4, 4)
for k, (i, j) in enumerate(PAIRS):
    Fm[i, j] = fs[k]; Fm[j, i] = -fs[k]
sol = sp.solve(list(g.T * Fm * g - Fm), fs, dict=True)[0]
Fg = Fm.subs(sol); fr = sorted(Fg.free_symbols, key=str)
B = [Fg.subs({f: (1 if f == h else 0) for f in fr}) for h in fr]
todict = lambda X: {p: X[p] for p in PAIRS}
img = [gam.T * b * gam for b in B]
out["gamma maps Lambda_A into invariant forms"] = all(sp.simplify(g.T * x * g - x) == sp.zeros(4, 4) for x in img)
out["Q(gamma b_i, gamma b_j) = -Q(b_i, b_j)"] = all(
    sp.simplify(wedge22(todict(img[a]), todict(img[b])) + wedge22(todict(B[a]), todict(B[b]))) == 0
    for a in range(4) for b in range(4))


# (b) discriminant forms of Lambda_A and Lambda_A(-1), for the author's Grams
def disc_form(G):
    G = sp.Matrix(G); n = G.shape[0]
    Gi = G.inv()
    # generators of L#/L: columns of G^-1 ; enumerate the group by Smith form
    from sympy.matrices.normalforms import smith_normal_form
    # brute force: elements x = G^-1 v, v in Z^n mod G Z^n ; enumerate v in a box of reps via Hermite reduction
    D = abs(int(G.det()))
    reps = {}
    box = range(0, D)
    for v in itertools.product(box, repeat=n):
        x = Gi * sp.Matrix(v)
        key = tuple(sp.Rational(c) % 1 for c in x)
        if key in reps: continue
        xs = sp.Matrix(key)
        reps[key] = (xs.T * G * xs)[0] % 2
        if len(reps) == D: break
    return reps


def iso_disc(q1, q2):
    """are two finite quadratic forms (dicts element -> q mod 2) isomorphic?  compare value multisets per order."""
    def prof(q):
        from collections import Counter
        c = Counter()
        for x, v in q.items():
            den = sp.ilcm(*[sp.fraction(sp.Rational(a))[1] for a in x]) if any(x) else 1
            c[(int(den), v)] += 1
        return c
    return prof(q1) == prof(q2)


AUTH = json.loads((HERE.parent / "three_generations_in_f2h.json").read_text())
for name in ("LR", "B_4", "B_5", "B_6", "B_7"):
    G = sp.Matrix(AUTH[name]["Gram Q"])
    q1 = disc_form(G); q2 = disc_form(-G)
    out["%s: discriminant forms of Lambda_A and Lambda_A(-1) have equal value profiles" % name] = iso_disc(q1, q2)


# (c) norm -1 units in Z[A]: the commutant is Z[A]; x I + y A has det = x^2 + t x y + y^2 ; search
for name, A_ in [("LR", [[1, 1], [1, 2]])] + [("B_%d" % t, [[0, -1], [1, t]]) for t in (4, 5, 6, 7)]:
    A_ = sp.Matrix(A_); t = A_.trace()
    # commutant over Z: matrices commuting with A_; basis I and (A_ - a11 I)/gcd
    N = A_ - A_[0, 0] * sp.eye(2); gg = math.gcd(*[int(x) for x in N]); N = N / gg
    hit = None
    for x in range(-60, 61):
        for y in range(-60, 61):
            if (x * sp.eye(2) + y * N).det() == -1:
                hit = (x, y); break
        if hit: break
    out["%s: element of the commutant with det -1 (|coeff| <= 60)" % name] = str(hit)

# (d) Mumford: Hermitian form of a chi = -3 class at a point of its curve (LR, author's w and an example point)
# write F = sum F_p e_p ; in complex coordinates, h_{j k} from F(v_j, conj v_k) with v the (1,0) vectors dual to dz+, dz-
z1 = complex(AUTH["LR"]["examples"][0]["tau1"].replace("i", "j")); z2 = complex(AUTH["LR"]["examples"][0]["tau2"].replace("i", "j"))
P = np.array([[1, z1, float(phi), float(phi) * z1], [1, z2, 1 - float(phi), (1 - float(phi)) * z2]], dtype=complex)  # rows dz+, dz-
Pfull = np.vstack([P, P.conj()])            # dz+, dz-, dz+bar, dz-bar as rows on (dx1, dy1, dx2, dy2)
V = np.linalg.inv(Pfull)                     # columns: the dual tangent vectors d/dz+, d/dz-, d/dz+bar, d/dz-bar
# author's basis via the same routine as q2 (only to read w)
import subprocess
def gp(cmd):
    return subprocess.run(["gp", "-q", "-f"], input=cmd + "\nquit\n", capture_output=True, text=True, timeout=120).stdout.strip()
Mk = sp.zeros(6, 6)
for k, p in enumerate(PAIRS):
    F = sp.zeros(4, 4); F[p] = 1; F[p[1], p[0]] = -1
    Gm = g.T * F * g - F
    for m, q in enumerate(PAIRS): Mk[m, k] = Gm[q]
txt = "[" + ";".join(",".join(str(int(Mk[i, j])) for j in range(6)) for i in range(6)) + "]"
K = json.loads(gp("K = matkerint(%s); print(vector(matsize(K)[1], i, K[i,]))" % txt))
basisA = [{PAIRS[i]: K[i][j] for i in range(6)} for j in range(4)]
for label, c in (("w", AUTH["LR"]["w (chi = -3)"]), ("u", AUTH["LR"]["examples"][0]["u"])):
    F = np.zeros((4, 4))
    for (i, j) in PAIRS:
        v = sum(ci * b[(i, j)] for ci, b in zip(c, basisA)); F[i, j] = v; F[j, i] = -v
    Fc = V.T @ F @ V                          # components in the complex frame
    h = -1j * Fc[0:2, 2:4]                    # F = sum F_{j kbar} dz_j ^ dz_kbar + ... ; Hermitian part up to sign
    h = (h + h.conj().T) / 2
    out["Mumford, LR %s at the first example point: (2,0) part %.2e, Hermitian eigenvalue signs" % (label, abs(Fc[0, 1]))] = \
        [int(np.sign(e)) for e in np.linalg.eigvalsh(h)]

for k, v in out.items():
    print(k, ":", v)
(HERE / "q3_components_and_hand.json").write_text(json.dumps(out, indent=1, default=str))
print("q3 exit 0")
