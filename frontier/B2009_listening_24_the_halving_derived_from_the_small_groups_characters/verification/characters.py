"""B2009 (GAP through sage: ~/.local/bin/sage -python -B characters.py > characters_run.txt): for G_k at mod 27, 81, 243, every
irreducible character chi: degree, m = <chi|S, 1>, m' = <chi|S, psi> (psi = rho restricted to the stabiliser S of (3,3,3)),
and the dimension of C's neutral subspace (chi(1) + chi(C) + chi(C^2))/3; the irreducibles with m != m' listed."""
import json, pathlib, time
from sage.all import libgap
HERE = pathlib.Path(__file__).resolve().parent
data = json.loads((HERE / "perms.json").read_text())
f = libgap.eval("""function(gens, p0)
  local G, S, tbl, irr, rho, triv, psi, out, chi, r3;
  G := Group(gens); S := Stabilizer(G, p0); tbl := CharacterTable(G); irr := Irr(tbl);
  rho := First(irr, x -> Degree(x) = 1 and gens[1]^x = E(3) and gens[2]^x = -1);
  if rho = fail then return [Size(G), Size(S), false, []]; fi;
  r3 := rho^3; triv := TrivialCharacter(S); psi := RestrictedClassFunction(rho, S); out := [];
  for chi in irr do
    Add(out, [Degree(chi), ScalarProduct(RestrictedClassFunction(chi, S), triv), ScalarProduct(RestrictedClassFunction(chi, S), psi),
              (Degree(chi) + gens[1]^chi + (gens[1]^2)^chi) / 3, chi = TrivialCharacter(G), chi = r3, chi = rho]);
  od;
  return [Size(G), Size(S), true, out];
end""")
t0 = time.time()
for k in ("3", "4", "5"):
    d = data[k]; P = lambda l: libgap.PermList([i + 1 for i in l])
    res = f(libgap([P(d["C"]), P(d["S"])]), d["p0"] + 1)
    size, ssize, ok, rows = int(res[0]), int(res[1]), bool(res[2]), [[r[0], r[1], r[2], r[3], bool(r[4]), bool(r[5]), bool(r[6])] for r in res[3]]
    rows = [[int(a), int(b), int(c), int(e), t, s, rh] for a, b, c, e, t, s, rh in rows]
    exc = [r for r in rows if r[1] != r[2]]
    print("mod %d: |G| = %d, |S| = %d, rho found among the linear characters: %s; %d irreducible characters; with m != m': %d  [%.0f s]" % (
        3 ** int(k), size, ssize, ok, len(rows), len(exc), time.time() - t0), flush=True)
    for r in exc:
        print("    degree %d, m = %d, m' = %d, C-neutral dimension %d%s" % (r[0], r[1], r[2], r[3], " (trivial)" if r[4] else " (rho^3, S4's sign)" if r[5] else " (rho)" if r[6] else ""))
    print("    exceptions with a non-zero C-neutral subspace: %d; sum over all irreducibles of degree * (m - m') = %d; sum of (m - m') * C-neutral dimension = %d" % (
        sum(1 for r in exc if r[3] > 0), sum(r[0] * (r[1] - r[2]) for r in rows), sum((r[1] - r[2]) * r[3] for r in rows)), flush=True)
