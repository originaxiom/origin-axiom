"""R70b -- B351's diagram automorphism theta (the F4-type, sigma-induced per B353/R60) transported to the icosian E6; its fixed Cartan,
its action on R68's frame, the object's theta-even directions and their charge spectra on the 27 and 78."""
import itertools, collections, random, sys
from fractions import Fraction as Fr
exec(open('frame_fast.py').read().replace("__file__.replace('frame_fast.py', 'r64_founding_ratio_type.py')", "'r64_founding_ratio_type.py'"))
sys.path.insert(0, 'rec/B351_exact_e6_chevalley'); import exact_e6 as X6
A = X6.A
for seed in range(7, 300):
    random.seed(seed); f = [Fr(random.randint(-97, 97)) for _ in range(8)]
    if all(sum(a*b for a, b in zip(f, [Fr(c) for c in vec(r)])) != 0 for r in E6r): break
fval = lambda q: sum(a*b for a, b in zip(f, [Fr(c) for c in vec(q)]))
posE6 = [r for r in E6r if fval(r) > 0]
def qadd(p, q): return tuple(fadd(a, b) for a, b in zip(p, q))
simpleE6 = [r for r in posE6 if not any(qadd(s, t) == r for s in posE6 for t in posE6)]
cart = [[int(2*B(a, b)) for b in simpleE6] for a in simpleE6]
pm = next(p for p in itertools.permutations(range(6)) if all(cart[p[i]][p[j]] == A[i][j] for i in range(6) for j in range(6)))
simpleB = [simpleE6[pm[i]] for i in range(6)]
import sympy as sp
G = sp.Matrix(6, 6, lambda i, j: sp.Rational(2*B(simpleB[i], simpleB[j])))
def coords6(r):
    c = G.solve(sp.Matrix([sp.Rational(2*B(r, s)) for s in simpleB])); assert all(x.is_integer for x in c); return tuple(int(x) for x in c)
rc = {r: coords6(r) for r in E6r}; inv_rc = {v: k for k, v in rc.items()}
FLIP = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}          # Bourbaki 1<->6, 3<->5 (0-based)
def theta_root(r):   # diagram automorphism on a root: permute simple-root coordinates
    c = rc[r]; return inv_rc[tuple(c[FLIP[i]] for i in range(6))]
def theta_vec(q):    # on a rational combination of roots: use linearity via the simple-root expansion (solve in Q)
    c = G.solve(sp.Matrix([sp.Rational(2*B(q, s)) for s in simpleB]))
    out = (ZERO5,)*4
    for j in range(6):
        cj = c[FLIP[j]] if False else c[j]
        # theta(alpha_j) = alpha_{FLIP[j]}
        coef = (Fr(int(c[j].p), int(c[j].q)), Fr(0))
        out = tuple(fadd(x, fmul(coef, y)) for x, y in zip(out, simpleB[FLIP[j]]))
    return out
assert all(theta_root(theta_root(r)) == r for r in E6r)
fixed_roots = sum(1 for r in E6r if theta_root(r) == r)
print(f"[theta_F4 on the icosian E6] involution: True; fixed roots: {fixed_roots};  conj fixes: {sum(1 for r in E6r if qconj(r) == r)} roots")
# fixed Cartan dimension: rank of (theta - 1) on the 6-dim space spanned by simple roots
Th = sp.Matrix(6, 6, lambda i, j: 1 if FLIP[j] == i else 0)
print(f"      fixed Cartan dim of theta_F4: {6 - (Th - sp.eye(6)).rank()};  of conj: computed below")
# conj on simple-root coordinates
Cj = sp.Matrix(6, 6, lambda i, j: sp.Rational(rc[qconj(simpleB[j])][i]) if qconj(simpleB[j]) in rc else sp.nan)
print(f"      conj is a root-system automorphism (maps simple roots to roots): {all(qconj(s) in rc for s in simpleB)};  fixed Cartan dim of conj: {6 - (Cj - sp.eye(6)).rank()}")
# is conj in W . theta_F4 ?  check det and whether conj o theta_F4 is in W (i.e. maps the positive system to a positive system for some element... simpler: outer iff it swaps the two 27-classes, already shown). Compare conj with -s_beta, beta = phi^-1
beta = next(r for r in E6r if qconj(r) == r and B(r, one) == 0)
def refl_root(r, b): 
    c = Fr(2)*Fr(B(r, b))/Fr(B(b, b)); return tuple(fsub(x, fmul((c, Fr(0)), y)) for x, y in zip(r, b))
print(f"      conj == -s_beta with beta = phi^-1 (the real root): {all(qconj(r) == tuple(fneg(x) for x in refl_root(r, beta)) for r in E6r)}")
# theta_F4 on the frame's planes
def plane_img(P): return frozenset(theta_root(r) for r in P)
perm = [frame.index(plane_img(P)) if plane_img(P) in frame else None for P in frame]
print(f"[frame] theta_F4 maps the three planes to: {perm}   (None = not to a frame plane)")
# theta_F4-fixed subspace of the E6 Cartan, and its intersection with the frame's Cartan directions
# work in simple-root coordinates: fixed vectors of Th
fixed_basis = (Th - sp.eye(6)).nullspace()
print(f"      theta_F4-fixed Cartan: dim {len(fixed_basis)}")
# candidate theta-even directions supplied by the frame: for each plane P (2-dim, spanned by roots r, gr), the theta-fixed part (r + theta r) etc.
def to_quat(vec6):
    out = (ZERO5,)*4
    for j in range(6):
        coef = (Fr(int(vec6[j].p), int(vec6[j].q)), Fr(0)); out = tuple(fadd(x, fmul(coef, y)) for x, y in zip(out, simpleB[j]))
    return out
def spectrum(u, name):
    q27 = collections.Counter(B(r, u) for r in c27); q78 = collections.Counter(B(a, u) for a in E6r); q78[Fr(0)] += 6
    cent = 6 + sum(1 for a in E6r if B(a, u) == 0)
    print(f"[u = {name}] centralizer dim {cent}; 27: {dict(sorted(q27.items()))}; 78: {dict(sorted(q78.items()))}")
cls = lambda r: (B(r, one), B(r, g)); c27 = [r for r in roots if cls(r) == (Fr(1,2), Fr(0))]
for i, P in enumerate(frame):
    r = next(iter(P)); rt = theta_root(r) if perm[i] == i else None
    if perm[i] == i:
        # theta acts on the plane; fixed line = r + theta(r) if nonzero, else the plane is pointwise... check both roots
        for rr in list(P)[:3]:
            v = tuple(fadd(x, y) for x, y in zip(rr, theta_root(rr)))
            if v != (ZERO5,)*4:
                spectrum(v, f"theta_F4-fixed direction in frame plane {i}"); break
        else: print(f"      plane {i}: theta_F4 acts as -1 (no fixed direction)")
# and the D2 direction for comparison: omega_1^vee, and its theta_F4 image
Cinv = sp.Matrix(A).inv()
uD2 = to_quat([Cinv[j, 0] for j in range(6)]); uD2t = theta_vec(uD2)
print(f"[D2] omega_1^vee theta_F4-even? {uD2t == uD2}   (omega_1 <-> omega_6 under the flip: expected odd/mixed)")
spectrum(uD2, "omega_1^vee (SO(10)xU(1))")
usum = tuple(fadd(x, y) for x, y in zip(uD2, uD2t)); spectrum(usum, "omega_1^vee + omega_6^vee (theta_F4-even)")
udiff = tuple(fsub(x, y) for x, y in zip(uD2, uD2t)); spectrum(udiff, "omega_1^vee - omega_6^vee (theta_F4-odd)")

# ---- the four theta_F4-even fundamental coweight directions and their spectra
def coweight(k): return to_quat([Cinv[j, k] for j in range(6)])
w = {k: coweight(k) for k in range(6)}
def add(u, v): return tuple(fadd(x, y) for x, y in zip(u, v))
for name, u in (("omega_2^vee", w[1]), ("omega_4^vee", w[3]), ("omega_3^vee + omega_5^vee", add(w[2], w[4])), ("omega_1^vee + omega_6^vee", add(w[0], w[5]))):
    assert theta_vec(u) == u, name
    spectrum(u, name + " (theta_F4-even)")
# the conj-fixed line of R70 (frame plane 2's real axis) is which coweight direction?
ax = next(r for r in frame[2] if qconj(r) == r) if any(qconj(r) == r for r in frame[2]) else None
for k in range(6):
    # proportional?
    if ax is not None:
        import sympy as sp
        vs = sp.Matrix([sp.Rational(str(c[0])) + sp.Rational(str(c[1]))*sp.sqrt(5) for c in ax]); vk = sp.Matrix([sp.Rational(str(c[0])) + sp.Rational(str(c[1]))*sp.sqrt(5) for c in w[k]])
        if vs.rank() == 1 and sp.Matrix.hstack(vs, vk).rank() == 1: print(f"[conj-fixed real axis of the frame] is proportional to omega_{k+1}^vee")
