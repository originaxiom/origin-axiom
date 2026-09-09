"""Part II: the 4-fold cyclic cover C4 (PREREG_C4.md).  Order: (1) exact rep + RS presentation + H1;  (2) symmetry census of the
32 isometries on H1(C4) and the forced zeros among the 8 order-3 characters -- PRINTED BEFORE (3) the table over all 45 torsion
characters: order-3 exact over Q(zeta_12) (+ SVD), order-5/15 numeric (SVD), with identities and Galois pairings checked."""
import os, sys, json, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import d2lib as L
from d2lib import K, OMEGA, I_, ONE, ZERO
from math import gcd

REL = L.word_from_snappy("aaabABBAb"); MER = L.word_from_snappy("ab"); LON = L.word_from_snappy("aBAbABab")
A = L.mat([[1 - OMEGA, 1], [-1, 0]]); B = L.mat([[0, -1], [1, OMEGA * (-2)]])
torus = L.Presentation(["m", "l"], [[("m", 1), ("l", 1), ("m", -1), ("l", -1)]])
N = 4
gens, rels, rewrite, t, others = L.rs_cyclic(["a", "b"], [REL], {"a": 0, "b": 1}, N)
pres = L.Presentation(gens, rels)
inv, cls, V, D, keep = L.h1_coordinates(gens, rels)
mC = rewrite(MER * N); lC = rewrite(LON)
print("C4 presentation:", gens, [L.word_to_snappy(R) for R in rels])
print("H1(C4) =", inv, " [m] =", cls(mC), " [l] =", cls(lC), " gen classes:", {g: cls([(g, 1)]) for g in gens})
tor_idx = [i for i, d in enumerate(inv) if d != 0]
def rho_gen(g, Bl=B):
    if g == "z":
        M = L.eye(2)
        for _ in range(N): M = L.mmul(M, Bl)
        return M
    j = int(g[1:]); M = A; Bi = L.inv2(Bl)
    for _ in range(j): M = L.mmul(L.mmul(Bl, M), Bi)
    return M
R = L.Rep({g: rho_gen(g) for g in gens})
print("exact rep satisfies the 4 cover relators:", all(L.meq(R(r), L.eye(2)) for r in rels))

# ---------- (2) symmetry census on H1(C4), before the table
An, Bn = np.array(L.to_cx(A)), np.array(L.to_cx(B))
letters = {"a": An, "b": Bn, "A": np.linalg.inv(An), "B": np.linalg.inv(Bn)}
def ev(word):
    M = np.eye(2, dtype=complex)
    for ch in word: M = M @ letters[ch]
    return M
ta, tb, tab = np.trace(An), np.trace(Bn), np.trace(An @ Bn)
def reduced(w):
    out = []
    for ch in w:
        if out and out[-1] == ch.swapcase(): out.pop()
        else: out.append(ch)
    return "".join(out)
def inv_str(w): return w.swapcase()[::-1]
def subst(word, ia, ib):
    out = ""
    for ch in word:
        img = ia if ch.lower() == "a" else ib
        out += img if ch.islower() else inv_str(img)
    return reduced(out)
def exps(w, g): return sum(1 if ch == g else -1 if ch == g.upper() else 0 for ch in w)
def triple_class(Ma, Mb):
    trip = (np.trace(Ma), np.trace(Mb), np.trace(Ma @ Mb))
    for sa in (1, -1):
        for sb in (1, -1):
            if all(abs(u - v) < 1e-9 for u, v in zip(trip, (sa * ta, sb * tb, sa * sb * tab))): return +1
            if all(abs(u - v) < 1e-9 for u, v in zip(trip, (sa * ta.conjugate(), sb * tb.conjugate(), sa * sb * tab.conjugate()))): return -1
    return 0
def is_pm_I(M): return np.allclose(M, np.eye(2), atol=1e-9) or np.allclose(M, -np.eye(2), atol=1e-9)
# the 8 outer classes: representatives from Part I (one per orientation/f type), then all 4 deck lifts by conjugation with b^k
reps = [("a", "b"), ("A", "B"), ("A", "aaab"), ("a", "AAAB"), ("ABab", "BABAba"), ("ABab", "BAbaba"), ("AbaB", "bABABa"), ("AbaB", "bABaba")]
autos = []
for ia, ib in reps:
    eps = triple_class(ev(ia), ev(ib)); assert eps != 0 and is_pm_I(ev(subst("aaabABBAb", ia, ib)))
    for k in range(N):
        ca = reduced("b" * k + ia + "B" * k); cb = reduced("b" * k + ib + "B" * k)
        autos.append((ca, cb, eps))
G = [cls([(g, 1)]) for g in gens]
def phi_on_H1(ia, ib):
    rows = []
    for j in range(N):
        rows.append(cls(rewrite(L.word_from_snappy(ib * j + ia + inv_str(ib) * j))))
    rows.append(cls(rewrite(L.word_from_snappy(ib * N))))
    return rows
# action on characters: a character is a tuple of exponents e_i on the SNF torsion factors (values exp(2 pi i e_i / d_i)); psi o phi (v) = psi(phi v)
# phi on H1 is Z-linear: phi(sum n_g [g]) = sum n_g rows[g]; a character psi is determined by psi([g]) for all g; (psi o phi)([g]) = psi(rows[g])
# we represent psi by its values on the torsion SNF basis; need phi as a matrix on the torsion SNF coordinates: solve from generator images
def torsion_matrix(rows):
    # find T (2x2 over Z, mod (d1,d2) respectively) and c with rows_tor[g] = T * G_tor[g] + c * G_free[g] (mod d_i), and f = +-1 on the free part
    d1, d2 = inv[tor_idx[0]], inv[tor_idx[1]]
    sols = []
    for T in itertools.product(range(d1), range(d1), range(d2), range(d2)):
        Tm = [[T[0], T[1]], [T[2], T[3]]]     # row i of T mod d_i
        for c in itertools.product(range(d1), range(d2)):
            for f in (1, -1):
                ok = True
                for gk, rk in zip(G, rows):
                    st = [gk[tor_idx[0]], gk[tor_idx[1]]]; sf = gk[2]
                    pred0 = (Tm[0][0] * st[0] + Tm[0][1] * st[1] + c[0] * sf) % d1
                    pred1 = (Tm[1][0] * st[0] + Tm[1][1] * st[1] + c[1] * sf) % d2
                    if pred0 != rk[tor_idx[0]] % d1 or pred1 != rk[tor_idx[1]] % d2 or f * sf != rk[2]: ok = False; break
                if ok: sols.append((Tm, c, f))
    return sols
actions = []
for ia, ib, eps in autos:
    sols = torsion_matrix(phi_on_H1(ia, ib))
    assert sols, ("no consistent action", ia, ib)
    Tm, c, f = sols[0]; actions.append(dict(a=ia, b=ib, eps=eps, T=Tm, c=list(c), f=f))
distinct = {(tuple(map(tuple, x["T"])), tuple(x["c"]), x["f"], x["eps"]) for x in actions}
print(f"\nisometries of C4 realised: {len(actions)} word pairs, {len(distinct)} distinct actions on H1(C4)  (|Isom(C4)| = 32)")
# characters: exponent vectors (e1 mod 3, e2 mod 15) -> psi(v) = exp(2 pi i (e1 v1/3 + e2 v2/15)); psi o phi has exponents e' with
# e'.v = e.(T v) => e' = e T  (row action), free-part twist c irrelevant for cusp-trivial evaluation? NO: (psi o phi)(free gen) = psi(c) != 1 possibly.
# We only need the action on TORSION characters restricted to torsion: e' = e T (mod d).  (phi maps Tors -> Tors since it is a group automorphism.)
d1, d2 = inv[tor_idx[0]], inv[tor_idx[1]]
def act(e, Tm):
    # e = (e1, e2) with e1 mod d1, e2 mod d2 ; psi(v) = e1 v1/d1 + e2 v2/d2 ; (psi o T)(v) = psi(T v) = e1 (T v)_1/d1 + e2 (T v)_2/d2
    # (T v)_1 = T00 v1 + T01 v2 (mod d1), (T v)_2 = T10 v1 + T11 v2 (mod d2)   -- T01 multiplies a mod-d2 coordinate into a mod-d1 one: only valid
    # if T is a genuine hom Z/d1+Z/d2 -> itself; we verify the resulting character is well defined by checking on the generator classes directly.
    return None
def char_vals_on_gens(e):
    return tuple(((e[0] * gk[tor_idx[0]]) % d1, (e[1] * gk[tor_idx[1]]) % d2) for gk in G)
def compose_char(e, rows):
    # (psi o phi)([g]) = psi(rows[g]) : gives values on generators; identify e' by matching values on all generators
    target = tuple(((e[0] * rk[tor_idx[0]]) % d1, (e[1] * rk[tor_idx[1]]) % d2) for rk in rows)
    # values are in (1/3, 1/15) units; compare as elements of Q/Z:
    def qz(vals): return tuple((v[0] * 5 + v[1]) % 15 for v in vals)   # e1/3 + e2/15 = (5 e1 + e2)/15
    tq = qz(target)
    for e1 in range(d1):
        for e2 in range(d2):
            if qz(char_vals_on_gens((e1, e2))) == tq: return (e1, e2)
    raise RuntimeError("character not found")
rows_by_auto = {(x["a"], x["b"]): phi_on_H1(x["a"], x["b"]) for x in actions}
chars = [(e1, e2) for e1 in range(d1) for e2 in range(d2) if (e1, e2) != (0, 0)]
def order(e): return max(d1 // gcd(d1, e[0]) if e[0] else 1, d2 // gcd(d2, e[1]) if e[1] else 1)
signed = {}
for x in actions:
    for e in chars:
        signed.setdefault(e, set()).add((compose_char(e, rows_by_auto[(x["a"], x["b"])]), x["eps"]))
# add inversion with sign -1 and close under composition on the fly (orbit-stabiliser with signs)
def inverse(e): return ((-e[0]) % d1, (-e[1]) % d2)
def forced_zero(e):
    # explore the signed orbit: nodes (char, sign); a contradiction (char, +1) and (char, -1) both reachable => J(char) = 0
    seen = {(e, 1)}; frontier = [(e, 1)]
    while frontier:
        new = []
        for (c, s) in frontier:
            nbrs = [(inverse(c), -s)] + [(c2, s * eps) for (c2, eps) in signed[c]]
            for nb in nbrs:
                if nb not in seen: seen.add(nb); new.append(nb)
        frontier = new
    return any((c, -1) in seen for (c, s) in seen if s == 1 and c == e) or ((e, -1) in seen)
print("\nCENSUS PREDICTION (before the table):")
for od in (3, 5, 15):
    cs = [e for e in chars if order(e) == od]
    fz = [e for e in cs if forced_zero(e)]
    print(f"  order {od:2d}: {len(cs):2d} characters, forced J = 0 by the signed symmetry group: {len(fz):2d}, free: {[e for e in cs if e not in fz]}")
P_rows = rows_by_auto[("A", "aaab")]
print("  period-2 lift (A, aaab) acts on the order-3 characters as:", {e: compose_char(e, P_rows) for e in chars if order(e) == 3})
census = dict(distinct=len(distinct), forced={f"{e[0]},{e[1]}": forced_zero(e) for e in chars})

# ---------- (3) the table
def nrank(M, tol=1e-7):
    if M.size == 0: return 0
    s = np.linalg.svd(M, compute_uv=False); return int(np.sum(s > tol * max(1.0, s[0])))
def nnull(M, tol=1e-7):
    u, s, vh = np.linalg.svd(M); r = int(np.sum(s > tol * max(1.0, s[0]))) if s.size else 0
    return vh[r:].conj().T
class NRep:
    def __init__(self, ims): self.im = {(g, 1): M for g, M in ims.items()}; self.dim = next(iter(ims.values())).shape[0]
    def letter(self, g, e):
        if e == -1 and (g, -1) not in self.im: self.im[(g, -1)] = np.linalg.inv(self.im[(g, 1)])
        return self.im[(g, e)]
    def __call__(self, w):
        M = np.eye(self.dim, dtype=complex)
        for g, e in w: M = M @ self.letter(g, e)
        return M
def nfox(rep, word, gs):
    n = rep.dim; Dd = {g: np.zeros((n, n), dtype=complex) for g in gs}; P = np.eye(n, dtype=complex)
    for g, e in word:
        if e == 1: Dd[g] += P; P = P @ rep.letter(g, 1)
        else: P = P @ rep.letter(g, -1); Dd[g] -= P
    return Dd
def ndata(rep):
    n = rep.dim
    d0 = np.block([[rep.letter(g, 1) - np.eye(n)] for g in gens]); d1 = np.block([[nfox(rep, Rr, gens)[g] for g in gens] for Rr in rels])
    r0, r1 = nrank(d0), nrank(d1); a0, a1, a2 = n - r0, n * len(gens) - r1 - r0, n * len(rels) - r1
    Z1 = nnull(d1); Res = np.block([[nfox(rep, w, gens)[g] for g in gens] for w in (mC, lC)])
    m, l = rep(mC), rep(lC); cd0 = np.vstack([m - np.eye(n), l - np.eye(n)])
    crep = NRep({"m": m, "l": l}); cd1 = np.block([[nfox(crep, [("m", 1), ("l", 1), ("m", -1), ("l", -1)], ["m", "l"])[g] for g in ["m", "l"]]])
    t0 = n - nrank(cd0); t1 = 2 * n - nrank(cd1) - nrank(cd0); t2 = n - nrank(cd1)
    rr = nrank(np.hstack([Res @ Z1, cd0])) - nrank(cd0)
    return dict(a=(a0, a1, a2), t=(t0, t1, t2), r1=rr)
def nindex(mats):
    Vv = NRep(mats); Vd = NRep({g: np.linalg.inv(M).T for g, M in mats.items()})
    Aa = ndata(Vv); Bb = ndata(Vd)
    I = (Aa["a"][0] - Bb["a"][0]) + Bb["t"][0] - Aa["r1"]; F = Aa["a"][1] - Bb["a"][1]
    ids = (Aa["r1"] + Bb["r1"] == Aa["t"][1]) and (Aa["t"][1] == Aa["t"][0] + Bb["t"][0]) and (F == (Aa["a"][0] - Bb["a"][0]) + Aa["r1"] - Aa["t"][0]) and (Aa["a"][0] - Aa["a"][1] + Aa["a"][2] == 0)
    return I, F, Aa, Bb, ids
sym2c = {g: np.array(L.to_cx(L.sym_power(rho_gen(g), 2))) for g in gens}
sym2x = {g: L.sym_power(rho_gen(g), 2) for g in gens}
print("\n== THE TABLE on C4: Sym^2 rho_geo (x) psi over the 45 torsion characters (all cusp-trivial) ==")
rows_out = []
for e in sorted(chars, key=lambda e: (order(e), e)):
    od = order(e)
    vals = {g: np.exp(2j * np.pi * (e[0] * gk[tor_idx[0]] / d1 + e[1] * gk[tor_idx[1]] / d2)) for g, gk in zip(gens, G)}
    matsn = {g: sym2c[g] * vals[g] for g in gens}
    I, F, Aa, Bb, ids = nindex(matsn)
    exact = None
    if od == 3:
        chi = {}
        for g, gk in zip(gens, G):
            k3 = (e[0] * gk[tor_idx[0]] * (3 // d1) + e[1] * gk[tor_idx[1]] * (3 // 3 if d2 == 3 else 0)) if False else None
            # value exp(2 pi i (e1 v1/3 + e2 v2/15)) with e2 v2/15 having order dividing 3 => e2 v2/15 = (e2 v2 / 5)/3 ; require 5 | e2 v2
            num = (e[0] * gk[tor_idx[0]] * 5 + e[1] * gk[tor_idx[1]]) % 15      # in units of 1/15
            assert num % 5 == 0; k3 = (num // 5) % 3
            v = ONE
            for _ in range(k3): v = v * OMEGA
            chi[g] = v
        matsx = {g: L.mscale(sym2x[g], chi[g]) for g in gens}
        d = L.index_data(pres, matsx, [mC, lC], torus)
        exact = (d["I"], d["F"], (d["V"]["a0"], d["V"]["a1"], d["V"]["a2"]), (d["V"]["t0"], d["V"]["t1"], d["V"]["t2"]), d["V"]["r1"], d["Vstar"]["r1"], all(d["checks"].values()))
    tag = "GALOIS-UNPROTECTED" if od % 3 == 0 and od != 15 else ("mixed (tau_5 pairs it with (e1,-e2))" if od == 15 else "Galois-protected")
    rows_out.append(dict(e=e, order=od, I=int(I), F=int(F), a=Aa["a"], t=Aa["t"], r1=Aa["r1"], r1s=Bb["r1"], ids=bool(ids), exact=exact, forced=census["forced"][f"{e[0]},{e[1]}"]))
    ex = f" exact: I={exact[0]:+d} a={exact[2]} t={exact[3]} r1={exact[4]} r1*={exact[5]} ids={exact[6]}" if exact else ""
    print(f" e={e} ord {od:2d} {tag:36s} numeric: I={I:+d} F={F:+d} a={Aa['a']} t={Aa['t']} r1={Aa['r1']} r1*={Bb['r1']} ids={ids} censusforced={census['forced'][f'{e[0]},{e[1]}']}{ex}")
nz = [r for r in rows_out if r["I"] != 0 or (r["exact"] and r["exact"][0] != 0)]
print(f"\nNONZERO INDICES among the 45 sectors: {len(nz)}   ;  order-3 (Galois-unprotected) sectors nonzero: {sum(1 for r in nz if r['order'] == 3)}")
print("all identities hold:", all(r["ids"] for r in rows_out), " exact == numeric on order-3:", all(r["exact"][0] == r["I"] for r in rows_out if r["exact"]))
json.dump(dict(inv=inv, census=census, table=rows_out), open("c4_table.json", "w"), indent=1, default=str)
