"""The physical lane's NATIVE_SIGNED_ACTION_AND_INVARIANT_METRIC (its branch at 798281903): what main computes of it, from main's own
B1601 maps.  Nothing of the seat's is run.
 N1  the derivatives at zero of B1601's L(x,y,z) = (x, z, xz - y) and R(x,y,z) = (z, y, yz - x) (verification/meets.py, read at
     da6f87f5d) against its matrices (1); its custody: the git blobs it records for its four sources at da6f87f5d.
 N2  at the quaternion point a = i, b = j the substitutions a -> a, b -> ab and a -> ab, b -> b give its (3), and the matrices of
     (1) are their inverses in the basis (i, j, k).
 N3  G = <ell, r>: its order, determinants, the kernel of forgetting signs, the image; the number of involutions (2T has one).
 N4  G on X6 = {+-e1, +-e2, +-e3}: transitive; the stabilizer of e1 is <ell>; its orbits (6); G's orbits on ordered pairs.
 N5  the real symmetric forms B with ell^T B ell = r^T B r = B: their dimension and form; the commutant of G over C: its dimension;
     the character norm of the signed triplet.
 N6  the unsigned quotient: the permutation module of S3 on three points has character norm 2 (trivial plus the two-dimensional),
     and its character differs from the signed triplet's on G.
 N7  the carrier warnings: e1 is not on x^2 + y^2 + z^2 = xyz, nor on its tangent cone at zero."""
import subprocess, itertools
import sympy as sp
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
x, y, z = sp.symbols("x y z")
src = git("show", "da6f87f5d:frontier/B1601_the_common_point_is_the_geometry_mod_3/verification/meets.py").split("\n")
Lmap = sp.Matrix([x, z, x * z - y]); Rmap = sp.Matrix([z, y, y * z - x])
ell = Lmap.jacobian([x, y, z]).subs({x: 0, y: 0, z: 0}); r = Rmap.jacobian([x, y, z]).subs({x: 0, y: 0, z: 0})
print("N1: B1601's meets.py lines 35 and 36 at da6f87f5d: %s | %s" % (src[34].strip()[:90], src[35].strip()[:90]))
print("N1: dL(0) = %s, as (1): %s; dR(0) = %s, as (1): %s" % (ell.tolist(), ell == sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]]), r.tolist(), r == sp.Matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])))
blobs = {"frontier/B1601_the_common_point_is_the_geometry_mod_3/FINDINGS.md": "19b4b3ec64bb8dcdf5ad64f2cfdd166dc28cfdab", "frontier/B1601_the_common_point_is_the_geometry_mod_3/verification/meets.py": "1866b293848e577c3dcd23b823e2863c7cfc63fe",
         "frontier/B1600_the_weave_verified/verification/weave_verify.py": "096cdfa1e4cbc2da852c710166731b31ed8a3e0a", "docs/THE_WEAVE.md": "97fb9906382db70767a5a73e6446f5e1ce0a3858"}
print("N1: its recorded git blobs at da6f87f5d match: %s" % [git("rev-parse", "da6f87f5d:" + p).strip() == b for p, b in blobs.items()])
# quaternions as 2x2 complex matrices
I2 = sp.eye(2); qi = sp.Matrix([[sp.I, 0], [0, -sp.I]]); qj = sp.Matrix([[0, 1], [-1, 0]]); qk = qi * qj
basis = [qi, qj, qk]
def coords(M):
    for s, (n, B) in itertools.product((1, -1), enumerate(basis)):
        if M == s * B: return s, n
def mat(images):
    A = sp.zeros(3, 3)
    for col, M in enumerate(images): s, n = coords(M); A[n, col] = s
    return A
a, b = qi, qj
aL = mat([a, a * b, a * (a * b)]); aR = mat([a * b, b, (a * b) * b])   # images of i = a, j = b, k = ab
print("N2: alpha_L sends (i, j, k) to %s; alpha_R to %s; ell = alpha_L^-1: %s; r = alpha_R^-1: %s"
      % ([coords(M) for M in (a, a * b, a * (a * b))], [coords(M) for M in (a * b, b, (a * b) * b)], ell == aL.inv(), r == aR.inv()))
G = {sp.ImmutableMatrix(sp.eye(3))}; frontier = list(G)
while frontier:
    new = []
    for g in frontier:
        for h in (ell, r):
            k = sp.ImmutableMatrix(g * h)
            if k not in G: G.add(k); new.append(k)
    frontier = new
G = list(G); signs = lambda g: tuple(tuple(abs(e) for e in row) for row in g.tolist())
kernel = [g for g in G if signs(g) == signs(sp.eye(3))]; image = {signs(g) for g in G}
invol = [g for g in G if g * g == sp.eye(3) and g != sp.eye(3)]
print("N3: |G| = %d; all det 1: %s; kernel %d (diagonal: %s); image %d; involutions %d (2T has 1); ell^2 = %s, r^2 = %s"
      % (len(G), all(g.det() == 1 for g in G), len(kernel), sorted(tuple(g[i, i] for i in range(3)) for g in kernel), len(image), len(invol), [ell ** 2 * sp.Matrix([1, 1, 1])][0].T.tolist(), (r ** 2 * sp.Matrix([1, 1, 1])).T.tolist()))
X6 = [s * sp.eye(3)[:, n] for n in range(3) for s in (1, -1)]; key = lambda v: tuple(v)
orb = {key(g * X6[0]) for g in G}; stab = [g for g in G if g * X6[0] == X6[0]]
ellpow = {sp.ImmutableMatrix(ell ** n) for n in range(4)}
sorb = []; seen = set()
for v in X6:
    if key(v) in seen: continue
    o = {key(g * v) for g in stab}; seen |= o; sorb.append(sorted(o))
pairs = set()
for v, w in itertools.product(X6, X6):
    pairs.add(frozenset((key(g * v), key(g * w)) for g in G) and min(((key(g * v), key(g * w)) for g in G)))
print("N4: transitive on X6: %s; stabilizer of e1: %d elements, = <ell>: %s; its orbits: %s; G's orbits on ordered pairs: %d"
      % (len(orb) == 6, len(stab), set(map(sp.ImmutableMatrix, stab)) == ellpow, sorb, len(pairs)))
Bs = sp.symbols("b11 b12 b13 b22 b23 b33"); B = sp.Matrix([[Bs[0], Bs[1], Bs[2]], [Bs[1], Bs[3], Bs[4]], [Bs[2], Bs[4], Bs[5]]])
sol = sp.solve(list(ell.T * B * ell - B) + list(r.T * B * r - B), Bs, dict=True)[0]
C = sp.Matrix(3, 3, sp.symbols("c0:9")); csol = sp.solve(list(ell * C - C * ell) + list(r * C - C * r), list(C), dict=True)[0]
chi = lambda g: g.trace(); norm = sum(chi(g) ** 2 for g in G) / len(G)
print("N5: invariant symmetric B = %s (free parameters %d); commutant over C: %s (free %d); the signed triplet's character norm %s"
      % (B.subs(sol).tolist(), len(B.subs(sol).free_symbols), C.subs(csol).tolist(), len(C.subs(csol).free_symbols), norm))
perm = lambda g: sp.Matrix(3, 3, lambda i, j: abs(g[i, j]))
normp = sum(perm(g).trace() ** 2 for g in G) / len(G); inner = sum(perm(g).trace() * chi(g) for g in G) / len(G)
print("N6: the unsigned permutation module's character norm %s (trivial plus two-dimensional: 2); its inner product with the signed triplet %s; the characters differ: %s"
      % (normp, inner, any(perm(g).trace() != chi(g) for g in G)))
print("N7: e1 on x^2 + y^2 + z^2 = xyz: %s; on x^2 + y^2 + z^2 = 0: %s" % ((1 + 0 + 0) == 0, (1 + 0 + 0) == 0))
