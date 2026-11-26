"""B2010 (GAP through sage: ~/.local/bin/sage -python -B bottom.py > bottom_run.txt). E1, E2 at mod 81 and 243: the kernel N
of the reduction G_k -> G_3; whether the six exceptional irreducibles (m != m') are trivial on N; whether every irreducible
non-trivial on N has m = m'. E3 at mod 27: the six exceptions' common kernel, the quotient and its structure."""
import json, pathlib, time
from sage.all import libgap
HERE = pathlib.Path(__file__).resolve().parent
data = json.loads((HERE / "perms.json").read_text())
f = libgap.eval("""function(gens, p0, red)
  local G, S, irr, rho, triv, psi, blocks, i, hom, N, exc, rows, chi, m, mp, onN, K, Q;
  G := Group(gens); S := Stabilizer(G, p0); irr := Irr(CharacterTable(G));
  rho := First(irr, x -> Degree(x) = 1 and gens[1]^x = E(3) and gens[2]^x = -1);
  triv := TrivialCharacter(S); psi := RestrictedClassFunction(rho, S);
  if red <> fail then
    blocks := List(Set(red), b -> Filtered([1..Length(red)], i -> red[i] = b));
    hom := ActionHomomorphism(G, blocks, OnSets); N := Kernel(hom);
  else N := TrivialSubgroup(G); fi;
  rows := [];
  for chi in irr do
    m := ScalarProduct(RestrictedClassFunction(chi, S), triv); mp := ScalarProduct(RestrictedClassFunction(chi, S), psi);
    onN := RestrictedClassFunction(chi, N) = Degree(chi) * TrivialCharacter(N);
    Add(rows, [Degree(chi), m, mp, onN]);
  od;
  exc := Filtered([1..Length(irr)], i -> rows[i][2] <> rows[i][3]);
  K := Intersection(List(exc, i -> KernelOfCharacter(irr[i])));
  Q := G / K;
  return [Size(G), Size(N), rows, exc, Size(K), Size(Q), StructureDescription(Q)];
end""")
t0 = time.time()
for k in ("3", "4", "5"):
    d = data[k]; P = lambda l: libgap.PermList([i + 1 for i in l])
    red = libgap([r + 1 for r in d["red27"]]) if k != "3" else libgap.eval("fail")
    res = f(libgap([P(d["C"]), P(d["S"])]), d["p0"] + 1, red)
    size, nsize = int(res[0]), int(res[1]); rows = [[int(r[0]), int(r[1]), int(r[2]), bool(r[3])] for r in res[2]]; exc = [int(i) - 1 for i in res[3]]
    nontriv = [r for r in rows if not r[3]]
    print("mod %d: |G| = %d; kernel of the reduction to mod 27: order %d; irreducibles %d, of which non-trivial on it %d  [%.0f s]" % (3 ** int(k), size, nsize, len(rows), len(nontriv), time.time() - t0), flush=True)
    print("    E1: the six exceptions are trivial on the kernel: %s (%d exceptions)" % (all(rows[i][3] for i in exc), len(exc)))
    print("    E2: every irreducible non-trivial on the kernel has m = m': %s" % all(r[1] == r[2] for r in nontriv))
    print("    E3: the exceptions' common kernel has order %d; the quotient has order %d, structure %s" % (int(res[4]), int(res[5]), str(res[6])), flush=True)
