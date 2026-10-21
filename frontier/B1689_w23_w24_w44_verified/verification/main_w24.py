"""P-229: the SM seat's W24 (the six-dimensional census; the gauge side) checked on main by its own code and derivations,
from W24's recorded read-out (NOTE.md, W24), not its script.
 K1  the moves on the character variety X = C^3 (x, y, z) = (tr a, tr b, tr ab) as trace polynomials (L: a -> a, b -> ab;
     R: a -> ab, b -> b; P: the swap): kappa = x^2 + y^2 + z^2 - xyz - 2 kept; Jacobians; the points every move fixes;
     kappa's critical points; the linear parts at the common point and the group they generate.
 K1b the Euler characteristics of kappa's level sets (generic, at -2, at 2) by the projective closure (a cubic surface
     minus the triangle xyz = 0 at infinity) and the Milnor numbers of the nodes; the fibration check chi(C^3) = 1.
 K2  chi_orb(E^3 / G) for G = V4 (the parities), A4 and O = S4 acting by signed permutations: (1/|G|) sum over
     commuting pairs of the number of joint fixed points (Smith normal form; positive-dimensional fixed sets count 0).
 D1  chi_p (x) rho_Q = u_p rho_Q u_p^-1 with u_p = j, i, k.
 D2  the 248's character on Q8, through SU(2) x SU(3) x SU(6)' (W = rho_Q (x) C^3 in the 6) and through G2 x F4 (Q8 in
     G2 with 7 = three characters + 2 rho_Q, 14 = three characters + 3 trivial + 4 rho_Q).
 D3  the multiplicities of Q8's irreducibles in the 248: trivial (the centraliser's dimension), each character, rho_Q."""
import itertools, json
import numpy as np, sympy as sp
x, y, z = sp.symbols("x y z")
kappa = x**2 + y**2 + z**2 - x*y*z - 2
moves = {"L": (x, z, x*z - y), "R": (z, y, y*z - x), "P": (y, x, z)}
out = {"K1": {}}
for m, f in moves.items():
    k2 = kappa.subs({x: f[0], y: f[1], z: f[2]}, simultaneous=True)
    J = sp.Matrix(f).jacobian([x, y, z]).det()
    out["K1"][m] = {"keeps_kappa": sp.expand(k2 - kappa) == 0, "jacobian": str(sp.simplify(J))}
# R as a trace map: a -> ab, b -> b: tr(ab) = z, tr b = y, tr(ab b) = tr(a b^2) = y z - x
fixed = [p for p in [(0, 0, 0), (2, 2, 2), (-2, -2, 2), (2, -2, -2), (-2, 2, -2), (1, 1, 1)]
         if all(tuple(sp.Integer(c) for c in [e.subs({x: p[0], y: p[1], z: p[2]}) for e in f]) == p for f in moves.values())]
out["K1"]["fixed_by_every_move_among_candidates"] = fixed
crit = sp.solve([sp.diff(kappa, v) for v in (x, y, z)], [x, y, z], dict=True)
out["K1"]["critical_points"] = sorted({(int(c[x]), int(c[y]), int(c[z]), int(kappa.subs(c))) for c in crit})
lin = {m: sp.Matrix(f).jacobian([x, y, z]).subs({x: 0, y: 0, z: 0}) for m, f in moves.items()}
def gen(gs):
    els = [sp.eye(3)]; seen = {tuple(sp.eye(3))}; i = 0
    while i < len(els):
        for g in gs:
            Y = g * els[i]
            if tuple(Y) not in seen: seen.add(tuple(Y)); els.append(Y)
        i += 1
    return els
out["K1"]["linear_parts_at_common_point_order"] = len(gen([lin["L"], lin["R"]]))
out["K1"]["with_swap_order"] = len(gen([lin["L"], lin["R"], lin["P"]]))
# K1b: Euler characteristics. Projective closure of x^2 + y^2 + z^2 - xyz = c (c = kappa + 2) in P^3: w(x^2+y^2+z^2) - xyz
# = c w^3; at infinity (w = 0): xyz = 0, three lines forming a triangle, chi = 3 * 2 - 3 = 3. A smooth cubic surface has
# chi = 9 (P^2 blown up at six points). The closure is smooth along infinity for every c (checked below), so a generic
# level has chi = 9 - 3 = 6; each A1 node lowers chi by its Milnor number 1.
W = sp.symbols("w"); c = sp.symbols("c")
F = W*(x**2 + y**2 + z**2) - x*y*z - c*W**3
sing_inf = sp.solve([sp.diff(F, v) for v in (x, y, z, W)] + [W], [x, y, z, W], dict=True)
nonzero_inf = [s for s in sing_inf if any(s.get(v, v) != 0 for v in (x, y, z))]
H = sp.hessian(kappa, (x, y, z))
nodes = {pt: int(sp.Matrix(H.subs({x: pt[0], y: pt[1], z: pt[2]})).rank()) for pt in [(0, 0, 0), (2, 2, 2), (2, -2, -2), (-2, 2, -2), (-2, -2, 2)]}
generic = 9 - 3
chi_m2 = generic - 1; chi_p2 = generic - 4
out["K1b"] = {"singular_points_at_infinity": [str(s) for s in nonzero_inf], "hessian_ranks_at_critical_points": {str(k): v for k, v in nodes.items()},
              "chi_generic": generic, "chi_at_-2": chi_m2, "chi_at_2": chi_p2,
              "fibration_check_chi_C3": generic * 1 + (chi_m2 - generic) + (chi_p2 - generic)}
# K2: orbifold Euler characteristics
def smith_product(B):
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(sp.Matrix(B), domain=sp.ZZ)
    d = [abs(S[i, i]) for i in range(min(S.shape)) if S[i, i] != 0]
    return int(np.prod(d)) if len(d) == 3 else 0
def group(gens):
    return gen([sp.Matrix(g) for g in gens])
par = [np.diag(v) for v in ((1, -1, -1), (-1, 1, -1), (-1, -1, 1))]
cyc = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]); tr = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
quarter = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])          # L's linear part at the common point (det +1)
# "O" is the rotation group (det +1: the Calabi-Yau orbifold the standard embedding needs), generated with a quarter
# turn; T_d (the parities and the permutations, the kappa-preserving group, with reflections) is a labelled control
G = {"V4": group(par), "A4": group(par + [cyc]), "O": group(par + [cyc, quarter]), "T_d (control, not Calabi-Yau)": group(par + [cyc, tr])}
K2 = {}
for name, els in G.items():
    I3 = sp.eye(3); tot = 0
    for g, h in itertools.product(els, repeat=2):
        if g * h != h * g: continue
        n = smith_product(sp.Matrix.vstack(g - I3, h - I3))
        tot += n * n                                   # E = R^2/Z^2: the count per real torus factor squares
    K2[name] = {"order": len(els), "all_det_plus_1": all(M.det() == 1 for M in els), "chi_orb": sp.Rational(tot, len(els)), "net_generations_standard_embedding": sp.Rational(tot, 2 * len(els))}
out["K2"] = {k: {a: str(b) for a, b in v.items()} for k, v in K2.items()}
# D1
I2 = np.eye(2, dtype=complex); qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]], dtype=complex); qk = qi @ qj
rho = {"a": qi, "b": qj}
d1 = {}
for p, u in (((1, 0), qj), ((0, 1), qi), ((1, 1), qk)):
    ok = all(np.allclose(((-1) ** p[0] if g == "a" else (-1) ** p[1]) * rho[g], u @ rho[g] @ np.linalg.inv(u)) for g in ("a", "b"))
    d1[str(p)] = bool(ok)
out["D1"] = d1
# D2: characters on Q8 at 1, -1, an order-4 element, through two branchings
def ch6(e):                                     # the 6 = rho_Q (x) C^3 at an element with 2x2 matrix e: eigenvalues
    return np.concatenate([np.linalg.eigvals(e)] * 3)
def esym(ev, k): return sum(np.prod(c) for c in itertools.combinations(ev, k))
def chars_su6(e):
    ev = ch6(e); t6 = ev.sum()
    return {"6": t6, "15": esym(ev, 2), "20": esym(ev, 3), "35": abs(t6) ** 2 - 1}
def ch248_A(e):
    c = chars_su6(e)
    return (3 + 8 + c["35"] + 2 * 3 * c["6"].real * 0 + 2 * 3 * c["6"] + 2 * 3 * np.conj(c["6"]) + 3 * c["15"] + 3 * np.conj(c["15"]) + 2 * c["20"]) \
        - 2 * 3 * c["6"].real * 0
def ch248_A(e):                                  # 248 = (3,1,1)+(1,8,1)+(1,1,35)+(2,3,6)+(2,3b,6b)+(1,3,15)+(1,3b,15b)+(2,1,20)
    c = chars_su6(e)
    return 3 + 8 + c["35"] + 6 * c["6"] + 6 * np.conj(c["6"]) + 3 * c["15"] + 3 * np.conj(c["15"]) + 2 * c["20"]
def char_Q8(rep, e):                             # Q8 reps on one element: characters chi_p and rho
    return rep(e)
# Q8 restricted: trivial, three characters (+1 on one order-4 class, -1 on the other two), rho (trace)
def triv(e): return 1.0
def chis(e):                                     # sum of the three nontrivial characters
    if np.allclose(e, I2) or np.allclose(e, -I2): return 3.0
    return -1.0
def rho_tr(e): return np.trace(e)
def ch248_B(e):                                  # 248 = (14,1)+(1,52)+(7,26), 7|Q8 = 3 chars + 2 rho, 14|Q8 = 3 chars + 3 + 4 rho
    c7 = chis(e) + 2 * rho_tr(e); c14 = chis(e) + 3 + 4 * rho_tr(e)
    return c14 + 52 + 26 * c7
pts = {"1": I2, "-1": -I2, "i": qi}
out["D2"] = {"via_SU2xSU3xSU6": {k: complex(np.round(ch248_A(e), 9)).real for k, e in pts.items()},
             "via_G2xF4": {k: complex(np.round(ch248_B(e), 9)).real for k, e in pts.items()}}
# D3: multiplicities (class sizes 1, 1, 6)
v = out["D2"]["via_SU2xSU3xSU6"]
m_triv = (v["1"] + v["-1"] + 6 * v["i"]) / 8
m_chi = (v["1"] + v["-1"] + 2 * v["i"] * (1 - 1 - 1)) / 8
m_rho = (2 * v["1"] - 2 * v["-1"]) / 8
out["D3"] = {"trivial": m_triv, "each_character": m_chi, "rho": m_rho, "sum_check": m_triv + 3 * m_chi + 2 * m_rho}
import pathlib; json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
