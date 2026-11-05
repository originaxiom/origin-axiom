"""C4 (P-663, B47): the torsion |tau_RS(m004, omega)| the lane states (4/sqrt3) and its 'adjoint' number (4 - 2 sqrt3),
recomputed on main's side, exactly (sympy over Q(omega)), from SnapPy's presentation of m004 (not the lane's word):
 (1) Fox calculus on <a, b | aaabABBAb>: the Alexander polynomial and the abelian Reidemeister torsion Delta(t)/(t - 1) at
     t = omega = e^{2 pi i/3} (Milnor's torsion of the knot exterior for the character t -> omega);
 (2) the lane's relator R = x y^-1 x^-1 y x y^-1 x y x^-1 y^-1: Riley's parabolic representation satisfies it (so it
     presents the figure-eight group) and its Fox derivative gives the same Delta;
 (3) the SL(2, C)-twisted torsion with Riley's holonomy (Dunfield-Friedl-Jackson's T(t) = det Phi(dR/dx)/det(t rho(y) - 1)),
     to compare with the lane's 'adjoint torsion 4 - 2 sqrt3' (computed in the lane's code as |Delta(omega)| - 2|omega - 1|).
Prints deviations and exact forms only; no SM quantity."""
import sympy as sp
import snappy

t = sp.symbols("t")
w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2          # omega, a primitive cube root of unity

def fox(word, gens, rep):
    """word: list of (gen, +-1); rep: gen -> matrix (or scalar as 1x1); returns {gen: d word / d gen} under rep."""
    n = rep[gens[0]].shape[0]
    D = {g: sp.zeros(n) for g in gens}; prefix = sp.eye(n)
    for g, e in word:
        if e == 1:
            D[g] += prefix; prefix = prefix * rep[g]
        else:
            prefix = prefix * rep[g].inv(); D[g] -= prefix
    return D, prefix

def parse(s):
    return [(c.lower(), 1 if c.islower() else -1) for c in s]

out = []
# (1) SnapPy's presentation
G = snappy.Manifold("m004").fundamental_group()
rel = G.relators()[0]
word = parse(rel)
ea = sum(e for g, e in word if g == "a"); eb = sum(e for g, e in word if g == "b")
ab = {"a": sp.Matrix([[t ** 0]]) if ea == 1 and eb == 0 else None, "b": sp.Matrix([[t]])}
# H1: the relator's exponent sums (ea, eb) = (1, 0) force a = 0, b = generator
D, _ = fox(word, ["a", "b"], {"a": sp.Matrix([[1]]), "b": sp.Matrix([[t]])})
Delta = sp.factor(sp.expand(D["a"][0, 0]))
out.append("(1) SnapPy relator %s; exponent sums (a, b) = (%d, %d); Fox d/da abelianised = %s" % (rel, ea, eb, Delta))
norm = sp.expand(Delta * t ** -sp.degree(sp.numer(sp.together(Delta)), t) if False else Delta)
ok = sp.simplify(sp.expand(Delta) - (t ** 2 - 3 * t + 1)) == 0 or any(sp.simplify(sp.expand(s * t ** k * Delta) - (t ** 2 - 3 * t + 1)) == 0 for s in (1, -1) for k in range(-4, 5))
out.append("    equals t^2 - 3t + 1 up to a unit +-t^k: %s" % ok)
tau_ab = sp.nsimplify(sp.simplify(sp.Abs(Delta.subs(t, w) / (w - 1))))
out.append("    |Delta(omega)/(omega - 1)| = %s  (lane: 4/sqrt3 -> difference %s)" % (tau_ab, sp.simplify(tau_ab - 4 / sp.sqrt(3))))
# (2) the lane's word and Riley's representation
lane = [("x", 1), ("y", -1), ("x", -1), ("y", 1), ("x", 1), ("y", -1), ("x", 1), ("y", 1), ("x", -1), ("y", -1)]
X = sp.Matrix([[1, 1], [0, 1]])
best = None
for z in (w, sp.conjugate(w), sp.Integer(-1) * w):
    Yr = sp.Matrix([[1, 0], [-z, 1]])
    _, Rm = fox(lane, ["x", "y"], {"x": X, "y": Yr})
    dev = sp.simplify(Rm - sp.eye(2))
    if dev == sp.zeros(2): best = z
out.append("(2) Riley's rep x -> [[1,1],[0,1]], y -> [[1,0],[-z,1]] satisfies the lane's relator for z = %s" % best)
Dl, _ = fox(lane, ["x", "y"], {"x": sp.Matrix([[t]]), "y": sp.Matrix([[t]])})
out.append("    lane word, Fox d/dx abelianised = %s ; d/dy = %s" % (sp.factor(sp.expand(Dl["x"][0, 0])), sp.factor(sp.expand(Dl["y"][0, 0]))))
# (3) SL(2,C)-twisted torsion with Riley's holonomy (z = best), Phi = rho (x) ab
Yr = sp.Matrix([[1, 0], [-best, 1]])
Dt, _ = fox(lane, ["x", "y"], {"x": X * t, "y": Yr * t})
T = sp.simplify(sp.factor((Dt["x"].det()) / ((Yr * t - sp.eye(2)).det())))
out.append("(3) twisted torsion T(t) = det Phi(dR/dx) / det(t rho(y) - 1) = %s" % sp.simplify(sp.expand(T)))
for tv, name in ((1, "t = 1"), (w, "t = omega"), (-1, "t = -1")):
    out.append("    |T| at %s = %s" % (name, sp.nsimplify(sp.simplify(sp.Abs(T.subs(t, tv))))))
out.append("    lane's 'adjoint torsion' 4 - 2 sqrt3 = (sqrt3 - 1)^2 = %.6f is |Delta(omega)| - 2|omega - 1| in its code (no representation enters)" % float(4 - 2 * sp.sqrt(3)))
print("\n".join(out))
import pathlib
pathlib.Path(__file__).with_name("c4_run.txt").write_text("\n".join(out) + "\n")
