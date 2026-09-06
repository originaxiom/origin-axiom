"""R70 -- charge spectra of the 27 and 78 under the object's theta-even directions (R68's frame), vs the theta-odd D2 direction."""
import io, contextlib, itertools, collections, random, sys
from fractions import Fraction as Fr
exec(open('frame_fast.py').read().replace("__file__.replace('frame_fast.py', 'r64_founding_ratio_type.py')", "'r64_founding_ratio_type.py'"))
# (1) conjugation on E6: outer or inner?  It maps the 27-class with pairing (1/2,0) to which class?
cls = lambda r: (B(r, one), B(r, g))
c27 = [r for r in roots if cls(r) == (Fr(1,2), Fr(0))]; assert len(c27) == 27
img = collections.Counter(cls(qconj(r)) for r in c27)
print("[theta = conj] the 27-class (1/2,0) maps to class:", dict(img))
# classes: B1270: (27,3) orbit = three classes cycled by left-g; (27bar,3bar) = the other three. Determine the two orbits:
orbitA = set(); c = (Fr(1,2), Fr(0))
for _ in range(3):
    orbitA.add(c); r0 = next(r for r in roots if cls(r) == c); c = cls(qmul(g, r0))
print("       left-g orbit of (1/2,0):", sorted(orbitA), "; conj sends (1/2,0) into that orbit:", list(img)[0] in orbitA, "(False = 27 -> 27bar: outer)")
# (2) conj on the frame's three planes
def plane_img(P): return frozenset(qconj(r) for r in P)
perm = [frame.index(plane_img(P)) if plane_img(P) in frame else None for P in frame]
print("[frame] conj permutes the three planes as:", perm)
# theta-even directions: conj-fixed lines in each conj-stable plane (the plane's real axis), and the fixed subspace of the whole E6 Cartan
def real_axis(P):
    # find r in P with conj(r) = r, else the fixed vector (r + conj r)
    for r in P:
        if qconj(r) == r: return r
    r = next(iter(P)); return tuple(fadd(a, b) for a, b in zip(r, qconj(r)))
axes = [real_axis(P) for i, P in enumerate(frame) if perm[i] == i]
print("       conj-stable planes:", [i for i in range(3) if perm[i] == i], "; their real axes (quaternions):", [tuple(f"{c[0]}+{c[1]}r5" for c in a) for a in axes])
# (3) charge spectra
E6r = E6; adj = E6r
def spectrum(u, name, odd_note=""):
    q27 = collections.Counter(B(r, u) for r in c27)
    q78 = collections.Counter(B(a, u) for a in adj); q78[Fr(0)] += 6
    cent = 6 + sum(1 for a in adj if B(a, u) == 0)
    fixed = (qconj(u) == u)
    pos27 = sum(n for q, n in q27.items() if q > 0); neg27 = sum(n for q, n in q27.items() if q < 0); zero27 = q27[Fr(0)]
    print(f"[u = {name}] theta-even (conj-fixed): {fixed}{odd_note}; centralizer dim {cent}")
    print(f"     27 charges: {dict(sorted(q27.items()))}  -> positive {pos27} | zero {zero27} | negative {neg27}")
    print(f"     78 charges: {dict(sorted(q78.items()))}")
    return q27
for i, a in enumerate(axes): spectrum(a, f"real axis of plane {[j for j in range(3) if perm[j]==j][i]}")
if len(axes) >= 2:
    usum = axes[0]
    for a in axes[1:]: usum = tuple(fadd(x, y) for x, y in zip(usum, a))
    spectrum(usum, "sum of the real axes")
    udiff = tuple(fsub(x, y) for x, y in zip(axes[0], axes[1])); spectrum(udiff, "difference of two real axes")
# (4) control: the theta-odd D2 direction (the SO(10)xU(1) coweight omega_1^vee), via the Bourbaki matching of R66
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
Cinv = sp.Matrix(A).inv()
# omega_1^vee = sum_j (C^-1)_{j1} alpha_j  (simply laced: coroots = roots), as a quaternion (rational combination)
uD2 = (ZERO5,)*4
for j in range(6):
    cj = Cinv[j, 0]; coef = (Fr(int(cj.p), int(cj.q)), Fr(0))
    uD2 = tuple(fadd(x, fmul(coef, y)) for x, y in zip(uD2, simpleB[j]))
# scale to make pairings integral: B(alpha_1, omega_1^vee) should be 1/2 in the norm-1 scaling
spectrum(uD2, "D2 direction omega_1^vee (SO(10)xU(1))", odd_note="  [B1250/R60: theta-ODD; excluded from the Fix(theta) count]")
