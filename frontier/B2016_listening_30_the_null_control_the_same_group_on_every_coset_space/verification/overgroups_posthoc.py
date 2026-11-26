"""B2016, POST HOC (labelled; written after cosets_gap_run.txt showed the classes in (a) forming one chain of orders): the exporter
again, with one more field per class: whether H contains a conjugate of C (so that G_k/H is a G-quotient of the whole's orbit
G_k/<C>, B2005: the stabiliser of (3,3,3) is <C> at mod 27 and 81). The original docstring follows. for G_k (the image of <C, sigma> on the orbit of (3,3,3) mod 27,
then mod 81), a representative H of every conjugacy class of subgroups; on G_k/H (ActionHomomorphism on the right cosets) the permutations of C
and sigma; whether rho (rho(C) = E(3), rho(sigma) = -1) is trivial on H; whether H is conjugate to the stabiliser of
(3,3,3). Written to coset_actions_posthoc.json beside this script (regenerated, not committed; its sha256 is printed).
Split from cosets_gap.py's first form, which stopped at `import flint` before any output (sage's Python has no python-flint).
    ~/.local/bin/sage -python -B overgroups_posthoc.py > overgroups_posthoc_run.txt"""
import json, hashlib, pathlib, time
from sage.all import libgap
HERE = pathlib.Path(__file__).resolve().parent
t0 = time.time()


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
    c = libgap.PermList([idx[(v[1], v[2], v[0])] + 1 for v in pts]); s = libgap.PermList([idx[(v[1], v[0], (v[0] * v[1] - v[2]) % N)] + 1 for v in pts])
    return pts, idx, c, s



out = {}
for N in (27, 81):
    pts, idx, c, s = gens(N)
    G = libgap.Group(c, s)
    stab = libgap.Stabilizer(G, idx[(3, 3, 3)] + 1)
    ccl = libgap.ConjugacyClasses(G)
    rho = [x for x in libgap.Irr(G) if libgap.DegreeOfCharacter(x) == 1 and x[libgap.Position(ccl, libgap.ConjugacyClass(G, c)) - 1] == libgap.E(3)
           and x[libgap.Position(ccl, libgap.ConjugacyClass(G, s)) - 1] == -1][0]
    classes = libgap.ConjugacyClassesSubgroups(G)
    rows = []
    for cl in classes:
        H = libgap.Representative(cl); n = int(libgap.Index(G, H))
        # the action on the right cosets (FactorCosetAction refused the index-1 class in the first run; disclosed)
        hom = libgap.ActionHomomorphism(G, libgap.RightCosets(G, H), libgap.OnRight)
        Cp = [int(x) - 1 for x in libgap.ListPerm(libgap.Image(hom, c), n)]; Sp = [int(x) - 1 for x in libgap.ListPerm(libgap.Image(hom, s), n)]
        vals = libgap.ValuesOfClassFunction(libgap.RestrictedClassFunction(rho, H))
        rows.append(dict(order=int(libgap.Size(H)), index=n, C=Cp, S=Sp, rho_trivial=all(v == 1 for v in vals),
                         whole=bool(libgap.IsConjugate(G, H, stab)),
                         over_C=any(bool(libgap.IsConjugate(G, x, c)) for x in libgap.Elements(H) if int(libgap.Order(x)) == 3)))
    out[str(N)] = dict(order=int(libgap.Size(G)), classes=rows)
    print("mod %d: |G| = %s; %d classes of subgroups exported  [%.0f s]" % (N, libgap.Size(G), len(rows), time.time() - t0), flush=True)
b = json.dumps(out).encode()
(HERE / "coset_actions_posthoc.json").write_bytes(b)
print("the exported actions (regenerated, not committed) have sha256 %s" % hashlib.sha256(b).hexdigest())
