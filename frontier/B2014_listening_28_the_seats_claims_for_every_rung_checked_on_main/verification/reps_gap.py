"""B2014, S4 (main, 2026-11-26; data-free; GAP through sage): B2009's exceptional irreducibles given their neutral values.
On the orbit of (3,3,3) mod 27 (72 points), G3 = <C, sigma> as permutations; S = the stabiliser of (3,3,3); rho the linear
character with rho(C) = E(3), rho(sigma) = -1. For every irreducible representation pi of G3 (GAP's
IrreducibleRepresentations, explicit matrices): m = <pi|S, 1>, m' = <pi|S, rho|S>, the dimension of pi(C)'s fixed space, and,
where it is one-dimensional with fixed vector v, the neutral value 6 <v, pi(sigma) v>/<v, v> (B2004: W on the neutral sector
is 6 Pi0 sigma Pi0). Also: G2 on the 8 points mod 9, an isomorphism onto Sym(4), and the signs of C's and sigma's images.
    ~/.local/bin/sage -python -B reps_gap.py > reps_gap_run.txt"""
from sage.all import libgap


def orbit(N, start=(3, 3, 3)):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]); Ri = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    s = tuple(c % N for c in start); seen, todo = {s}, [s]
    while todo:
        v = todo.pop()
        for g in (L, R, Li, Ri):
            u = g(v)
            if u not in seen:
                seen.add(u); todo.append(u)
    return sorted(seen)


def gens(N):
    pts = orbit(N); idx = {v: i for i, v in enumerate(pts)}
    C = [idx[(v[1], v[2], v[0])] + 1 for v in pts]
    S = [idx[(v[1], v[0], (v[0] * v[1] - v[2]) % N)] + 1 for v in pts]
    return pts, idx, libgap.PermList(C), libgap.PermList(S)


pts, idx, c, s = gens(27)
G = libgap.Group(c, s)
S = libgap.Stabilizer(G, idx[(3, 3, 3)] + 1)
print("G3: order %s; the stabiliser of (3,3,3): order %s" % (libgap.Size(G), libgap.Size(S)))
irr = libgap.Irr(G)
rho = [x for x in irr if libgap.DegreeOfCharacter(x) == 1 and x[libgap.Position(libgap.ConjugacyClasses(G), libgap.ConjugacyClass(G, c)) - 1] == libgap.E(3)
       and x[libgap.Position(libgap.ConjugacyClasses(G), libgap.ConjugacyClass(G, s)) - 1] == -1]
assert len(rho) == 1; rho = rho[0]
rhoS = libgap.RestrictedClassFunction(rho, S)
one = libgap.TrivialCharacter(S)
reps = libgap.IrreducibleRepresentations(G)
print("irreducible representations: %d" % len(reps))
rows = []
for r in reps:
    chi = libgap.ClassFunction(G, [libgap.TraceMat(libgap.Image(r, libgap.Representative(k))) for k in libgap.ConjugacyClasses(G)])
    chiS = libgap.RestrictedClassFunction(chi, S)
    m = int(libgap.ScalarProduct(chiS, one)); mp = int(libgap.ScalarProduct(chiS, rhoS))
    Mc = libgap.Image(r, c); Ms = libgap.Image(r, s); d = int(libgap.DegreeOfCharacter(chi))
    I = libgap.IdentityMat(d)
    ker = libgap.NullspaceMat(Mc - I)
    dim0 = len(ker)
    val = None
    if dim0 == 1:
        v = ker[0]
        vb = libgap.List(v, libgap.ComplexConjugate)
        # pi acts on row vectors from the right in GAP: v * M; take <v, v M> = sum conj(v_i) (v M)_i
        vM = v * Ms
        num = libgap.Sum([vb[i] * vM[i] for i in range(d)]); den = libgap.Sum([vb[i] * v[i] for i in range(d)])
        val = 6 * num / den
    rows.append((d, m, mp, dim0, val))
exc = [x for x in rows if x[1] != x[2]]
print("the irreducibles with m != m' (degree, m, m', C-neutral dimension, neutral value 6<v, pi(sigma) v>/<v, v>):")
for x in sorted(exc, key=lambda x: (x[0], -x[1])):
    print("   ", x[0], x[1], x[2], x[3], x[4])
print("count with m != m': %d; of them with a C-neutral line: %d; their neutral values: %s" % (
    len(exc), sum(1 for x in exc if x[3] == 1), sorted(str(x[4]) for x in exc if x[3] == 1)))
print("paired irreducibles (m = m') with a C-neutral line, a sample of their values: %s" % sorted({str(x[4]) for x in rows if x[1] == x[2] and x[3] == 1})[:8])

pts9, idx9, c9, s9 = gens(9)
G2 = libgap.Group(c9, s9)
iso = libgap.IsomorphismGroups(G2, libgap.SymmetricGroup(4))
print("G2 on the %d points mod 9: order %s, isomorphic to Sym(4): %s; sign of C's image %s, of sigma's image %s (rho^3 is C -> 1, sigma -> -1)" % (
    len(pts9), libgap.Size(G2), iso != libgap.fail, libgap.SignPerm(libgap.Image(iso, c9)), libgap.SignPerm(libgap.Image(iso, s9))))
