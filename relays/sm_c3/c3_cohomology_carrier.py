#!/usr/bin/env python3
"""SM-C3, packet cohomology_carrier (the fork lane @ 0c6570bab, with its V2 correction): this seat's own exact check, rebuilt
from the packet's PROOF.md, not from its verifiers.  rho(a) = A = diag(i, -i), rho(b) = B = [[0,1],[-1,0]], and the three
parity twists (A, B) -> ((-1)^ea A, (-1)^eb B), (ea, eb) in {(1,0), (0,1), (1,1)}; cocycles z(gh) = z(g) + rho(g) z(h).
(a) A^2 = B^2 = -I, AB = -BA; the group generated has order 8 and derived group {I, -I};
(b) on F, H^1 = Z^1 / B^1 has dimension 4 - 2 = 2 for each twist (A - I invertible), six in all;
(c) the one-relation certificate: with z(a) = 0, z(b) = v, c = [a,b]: rho(c) = -I, z(c) = (A + I) v, z(a c a^-1) = A z(c),
z(r) = 4 v for r = [c, a c a^-1], for each twist; so imposing r = 1 (any metabelian quotient) kills H^1: G_2 gives 0;
(d) for every cocycle (z(a), z(b) arbitrary), z(t) = 0 at the F''' witness t = [r, a r a^-1], and at two more elements of
F''' ([r, b r b^-1] and [r, (ab) r (ab)^-1]): a window, consistent with (g);
(e) the sign character chi (a scalar module, (chi(a), chi(b)) = ((-1)^ea, (-1)^eb)): H^1(F) has dimension 1; z(r) = 0 for
every cocycle (a window, consistent with (g)); imposing c = 1 (the abelian quotient G_1) kills it;
(f) the affine path map E of positive_carrier kills r and t (F'' and F''' lie in its kernel), so G_2 and G_3 keep every
positive word; G_1 = Z^2 does not (ab = ba there);
(g) the general bound, made structural: a cocycle is a homomorphism g -> (z(g), rho(g)) into the affine group V x| H.
For the doublet, [(0,A),(v,I)] = ((A - I) v, I) with A - I invertible, so V lies in the derived group;
[(0,A),(0,B)] = (0, -I); and [(0,-I),(v,I)] = (-2v, I), so V lies in the second derived group, which is inside
V x| {I} = V, abelian: derived length 3, so every cocycle kills F''' (H^1(G_3) = H^1(F) = 2), while the certificate (c)
shows a nonzero class does not kill F''. For the sign characters the image {+1,-1} is abelian, so every commutator is a
translation and translations commute: derived length 2, every cocycle kills F'' (H^1(G_2) = H^1(F) = 1).
Not rebuilt here: the lifted six-dimensional move action and its central projector ranks, which the packet takes from
the packet bundle_transport (not one of the card's four).
Planted: (p1) the card's named plant, B transposed: B^T = -B is itself a parity twist, so it is not an error and is
expected NOT to change any count (reported as such); (p2) B replaced by I2 (a module whose image is abelian): by (g)
H^1(G_2) = H^1(F), which must not be 0, so the count changes, and is caught."""
import json
import sys
from pathlib import Path

import sympy as sp

I2 = sp.eye(2)
A0 = sp.diag(sp.I, -sp.I)
B0 = sp.Matrix([[0, 1], [-1, 0]])
TWISTS = [(1, 0), (0, 1), (1, 1)]
z = lambda M: sp.simplify(M) == sp.zeros(*M.shape)


def rho_of(A, B):
    return {"a": A, "b": B, "A": A.inv(), "B": B.inv()}


def cocycle(word, rho, za, zb):
    """z(word) by z(gx) = z(g) + rho(g) z(x); z(a^-1) = -A^-1 z(a)"""
    zz = {"a": za, "b": zb, "A": -rho["A"] * za, "B": -rho["B"] * zb}
    g = sp.eye(za.shape[0])
    total = za * 0
    for ch in word:
        total = total + g * zz[ch]
        g = g * rho[ch]
    return sp.simplify(total), g


inv_w = lambda w: "".join(c.swapcase() for c in reversed(w))
comm = lambda x, y: x + y + inv_w(x) + inv_w(y)
conj = lambda g, x: g + x + inv_w(g)
c = comm("a", "b")
r = comm(c, conj("a", c))
t = comm(r, conj("a", r))
t2 = comm(r, conj("b", r))
t3 = comm(r, conj("ab", r))


def reduce_free(w):
    st = []
    for ch in w:
        if st and st[-1] == ch.swapcase():
            st.pop()
        else:
            st.append(ch)
    return "".join(st)


out = {"word_lengths": {"c": len(c), "r": len(r), "t": len(t), "t2": len(t2), "t3": len(t3)},
       "freely_reduced": {"r": reduce_free(r), "t": reduce_free(t)}}
# (a)
grp, frontier = {tuple(I2)}, [I2]
while frontier:
    g = frontier.pop()
    for h in (A0, B0):
        k = sp.simplify(g * h)
        if tuple(k) not in grp:
            grp.add(tuple(k)); frontier.append(k)
mats = [sp.Matrix(2, 2, list(x)) for x in grp]
derived = {tuple(sp.simplify(x * y * x.inv() * y.inv())) for x in mats for y in mats}
out["(a)"] = {"A2=B2=-I": z(A0 * A0 + I2) and z(B0 * B0 + I2), "AB=-BA": z(A0 * B0 + B0 * A0), "order": len(grp),
              "derived_group": sorted(str(sp.Matrix(2, 2, list(d))) for d in derived)}
a_ok = out["(a)"]["A2=B2=-I"] and out["(a)"]["AB=-BA"] and len(grp) == 8 and len(derived) == 2
v1, v2, p1, p2, q1, q2 = sp.symbols("v1 v2 p1 p2 q1 q2")
v = sp.Matrix([v1, v2]); za_gen = sp.Matrix([p1, p2]); zb_gen = sp.Matrix([q1, q2])


def doublet_checks(A, B):
    rho = rho_of(A, B)
    res = {}
    # (b) H^1(F): Z^1 = C^4 (any pair of values); B^1 = image of v -> ((A - I) v, (B - I) v)
    cob = sp.Matrix.vstack(A - I2, B - I2)
    res["dim_H1_F"] = 4 - cob.rank()
    # (c) normalised cocycle z(a) = 0, z(b) = v
    zc, gc = cocycle(c, rho, sp.zeros(2, 1), v)
    zaca, _ = cocycle(conj("a", c), rho, sp.zeros(2, 1), v)
    zr, gr = cocycle(r, rho, sp.zeros(2, 1), v)
    res["rho(c)=-I"] = z(gc + I2)
    res["z(c)=(A+I)v"] = z(zc - (A + I2) * v)
    res["z(aca^-1)=A z(c)"] = z(zaca - A * zc)
    res["z(r)"] = str(zr.T)
    res["z(r)=4v"] = z(zr - 4 * v)
    res["rho(r)=I_so_coboundaries_vanish_on_r"] = z(gr - I2)
    # (d) general cocycle at the F''' elements
    res["z(t)=0_all_cocycles"] = all(z(cocycle(w, rho, za_gen, zb_gen)[0]) for w in (t, t2, t3))
    res["rho(t)=I"] = z(cocycle(t, rho, za_gen, zb_gen)[1] - I2)
    return res


dbl = {}
for ea, eb in TWISTS:
    A, B = (-1) ** ea * A0, (-1) ** eb * B0
    dbl[f"twist{ea}{eb}"] = doublet_checks(A, B)
out["(b-d)_doublets"] = dbl
bd_ok = all(d["dim_H1_F"] == 2 and d["rho(c)=-I"] and d["z(c)=(A+I)v"] and d["z(aca^-1)=A z(c)"] and d["z(r)=4v"] and d["rho(r)=I_so_coboundaries_vanish_on_r"]
            and d["z(t)=0_all_cocycles"] and d["rho(t)=I"] for d in dbl.values())
out["(b)_total_H1_F_three_twists"] = sum(d["dim_H1_F"] for d in dbl.values())
# (e) the sign characters (1 x 1 module)
sc = {}
s1, s2 = sp.symbols("s1 s2")
for ea, eb in TWISTS:
    ca, cb = sp.Matrix([[(-1) ** ea]]), sp.Matrix([[(-1) ** eb]])
    rho = rho_of(ca, cb)
    zA, zB = sp.Matrix([s1]), sp.Matrix([s2])
    cobs = sp.Matrix.vstack(ca - sp.eye(1), cb - sp.eye(1))
    dimF = 2 - cobs.rank()
    zr_ = cocycle(r, rho, zA, zB)[0]
    zc_ = cocycle(c, rho, zA, zB)[0]
    # on G_1 a cocycle must vanish on F' = normal closure of c (rho is trivial on F'), i.e. z(c) = 0
    A_, _ = sp.linear_eq_to_matrix(list(zc_), [s1, s2])
    kernel_dim = 2 - A_.rank()
    sc[f"twist{ea}{eb}"] = {"dim_H1_F": dimF, "z(r)=0_all": z(zr_), "dim_H1_G1": kernel_dim - cobs.rank()}
out["(e)_sign_characters"] = sc
e_ok = all(d["dim_H1_F"] == 1 and d["z(r)=0_all"] and d["dim_H1_G1"] == 0 for d in sc.values())
# (f) the affine path map kills r and t; G_1 identifies ab with ba
X, Y = sp.symbols("X Y")


def E(word):
    gens = {"a": (1, 0, sp.Integer(1), sp.Integer(0)), "b": (0, 1, sp.Integer(0), sp.Integer(1))}

    def mul(p, q):
        m = X ** p[0] * Y ** p[1]
        return (p[0] + q[0], p[1] + q[1], sp.expand(p[2] + m * q[2]), sp.expand(p[3] + m * q[3]))

    def inv(p):
        mi = X ** (-p[0]) * Y ** (-p[1])
        return (-p[0], -p[1], sp.expand(-mi * p[2]), sp.expand(-mi * p[3]))
    gens["A"], gens["B"] = inv(gens["a"]), inv(gens["b"])
    p = (0, 0, sp.Integer(0), sp.Integer(0))
    for ch in word:
        p = mul(p, gens[ch])
    return p


ident = (0, 0, 0, 0)
out["(f)"] = {"E(r)=1": E(r) == ident, "E(t)=1": E(t) == ident, "E(ab)!=E(ba)": E("ab") != E("ba")}
f_ok = all(out["(f)"].values())


# (g) derived length of the affine group V x| H
def aff(Mrho, zv):
    n = Mrho.shape[0]
    return sp.Matrix(sp.BlockMatrix([[Mrho, zv], [sp.zeros(1, n), sp.eye(1)]]))


cm = lambda x, y: sp.simplify(x * y * x.inv() * y.inv())
w1, w2 = sp.symbols("w1 w2"); wv = sp.Matrix([w1, w2])
gd = {}
for ea, eb in TWISTS:
    A, B = (-1) ** ea * A0, (-1) ** eb * B0
    kAv = cm(aff(A, sp.zeros(2, 1)), aff(I2, wv))
    kAB = cm(aff(A, sp.zeros(2, 1)), aff(B, sp.zeros(2, 1)))
    kmv = cm(aff(-I2, sp.zeros(2, 1)), aff(I2, wv))
    gd[f"twist{ea}{eb}"] = {
        "[(0,A),(v,I)]=((A-I)v,I)": z(kAv - aff(I2, (A - I2) * wv)), "A-I_invertible": (A - I2).rank() == 2,
        "[(0,A),(0,B)]=(0,-I)": z(kAB - aff(-I2, sp.zeros(2, 1))),
        "[(0,-I),(v,I)]=(-2v,I)": z(kmv - aff(I2, -2 * wv)),
        "translations_commute": z(cm(aff(I2, wv), aff(I2, v)) - sp.eye(3))}
out["(g)_derived_length_3_doublets"] = gd
g_ok = all(all(d.values()) for d in gd.values())
gs = {}
x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2")
for ea, eb in TWISTS:
    ca, cb = sp.Matrix([[(-1) ** ea]]), sp.Matrix([[(-1) ** eb]])
    k = cm(aff(ca, sp.Matrix([[x1]])), aff(cb, sp.Matrix([[y1]])))
    gs[f"twist{ea}{eb}"] = {"commutator_is_translation": k[0, 0] == 1 and k[1, 0] == 0 and k[1, 1] == 1,
                            "translations_commute": z(cm(aff(sp.eye(1), sp.Matrix([[x2]])),
                                                         aff(sp.eye(1), sp.Matrix([[y2]]))) - sp.eye(2))}
out["(g)_derived_length_2_signs"] = gs
g_ok = g_ok and all(all(d.values()) for d in gs.values())
out["checks_ok"] = {"a": a_ok, "b-d": bd_ok and out["(b)_total_H1_F_three_twists"] == 6, "e": e_ok, "f": f_ok, "g": g_ok}
out["H1_table_from_(b)-(g)"] = {
    "doublet_per_parity": {"G2": 0, "G3": dbl["twist10"]["dim_H1_F"], "F2": dbl["twist10"]["dim_H1_F"]},
    "sign": {"G1": sc["twist10"]["dim_H1_G1"], "G2": sc["twist10"]["dim_H1_F"], "F2": sc["twist10"]["dim_H1_F"]}}
# planted
pl1 = doublet_checks(A0, B0.T)
out["PLANTED_p1_B_transposed_is_a_twist_no_change"] = {"z(r)=4v": pl1["z(r)=4v"], "dim_H1_F": pl1["dim_H1_F"],
                                                       "B^T=-B": z(B0.T + B0)}
pl2 = doublet_checks(A0, I2)
image_abelian = z(A0 * I2 - I2 * A0)
out["PLANTED_p2_B_trivial"] = {"z(r)": pl2["z(r)"], "z(r)=4v": pl2["z(r)=4v"], "image_abelian": image_abelian,
                               "dim_H1_G2_by_(g)": pl2["dim_H1_F"]}
out["PLANTED_p2_caught"] = (not pl2["z(r)=4v"]) and image_abelian and pl2["dim_H1_F"] != 0
out["all_claims_hold_and_plants_caught"] = bool(all(out["checks_ok"].values()) and out["PLANTED_p2_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
